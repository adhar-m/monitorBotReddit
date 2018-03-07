import praw
import datetime
from textblob import TextBlob

import praw_config
import bot_config

def init_bot_login():
	# Initialize PRAW with config file details and return reddit object
	print("Logging you in...")
	reddit = praw.Reddit(client_id=praw_config.client_id,
		client_secret=praw_config.client_secret,
		password=praw_config.password, 
		user_agent=praw_config.user_agent,
		username=praw_config.username
		)
	
	print("Authentication as " + str(reddit.user.me()) + " succesful!\n")
	return reddit

def construct_message_string(comment, comment_time, comment_url, comment_text):
	match_found_line = "Match found for comment by user *{}*, posted on {} UTC \n\n".format(comment.author, str(comment_time))
	url_line = comment_url + "\n\n"
	sentiment_line = ""
	score_line = ""

	if bot_config.get_sentiment:
		sentiment = get_sentiment_analysis(comment_text)
		sentiment_line = "**Sentiment polarity:** {} (subjectivity: {})\n\n".format(sentiment.polarity, sentiment.subjectivity)

	if bot_config.get_score:
		score = get_comment_score(comment)
		score_line = "**Comment score:**  {} ({} upvotes and {} downvotes)".format(score[0], score[1], score[2])
	
	msg = match_found_line + url_line + sentiment_line + score_line
	return msg

def add_to_seen(comments_seen_file, comment_id):
	with open(comments_seen_file,"a+") as comments_seen_writer:
		comments_seen_writer.write(comment_id + "\n")
		print("Comment " + comment_id + " added to log file.")

def check_if_seen(comments_seen_file, comment_id):
	with open(comments_seen_file, "r") as comments_seen_reader:

		if comment_id in comments_seen_reader.read().splitlines():
			print("Comment " + comment_id +  " already seen. Skipping.\n")
			return True
		return False

def get_comment_time(time_utc):
	time_human_readable = datetime.datetime.utcfromtimestamp(time_utc)
	return time_human_readable


def get_sentiment_analysis(comment_text):
	comment_text_blob = TextBlob(comment_text)
	return comment_text_blob.sentiment

def get_comment_score(comment):
	return (comment.score, comment.ups, comment.downs)

def run_bot(reddit_instance, subreddit_name, string_to_match):

	# Point bot to desired subreddit(s)
	subreddit = reddit_instance.subreddit(subreddit_name)
	comments_seen_file = bot_config.comments_seen

	for comment in subreddit.stream.comments():
		if string_to_match in comment.body.lower():

			# Check if comment already exsists in log and add if necessary
			if check_if_seen(comments_seen_file, comment.id):
				continue
			add_to_seen(comments_seen_file, comment.id)

			comment_time = get_comment_time(comment.created_utc)
			comment_url = comment.submission.url + comment.id
			comment_text = comment.body

			msg = construct_message_string(comment, comment_time, comment_url, comment_text)

			reddit.redditor(praw_config.username).message("Mention bot found a match (keyword: {})".format(bot_config.search_term), msg)
			print("Messaged user about comment " + comment.id +'\n')

if __name__ == '__main__':

	# Fetch data from bot_config
	subreddit_name = bot_config.subreddit_name
	search_term = bot_config.search_term

	# Init and run bot
	reddit = init_bot_login()
	run_bot(reddit, subreddit_name, search_term)