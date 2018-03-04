import praw
import datetime
from textblob import TextBlob

import praw_config
import bot_config

def init_bot_login():
	# Initialize PRAW with config file details and return reddit object
	reddit = praw.Reddit(client_id=praw_config.client_id, client_secret=praw_config.client_secret, user_agent=praw_config.user_agent)
	return reddit

def add_to_seen(comments_seen_file, comment_id):
	comments_seen_writer = open(comments_seen_file,'a+')
	comments_seen_writer.write(comment_id + '\n')
	comments_seen_writer.close()

def check_if_seen(comments_seen_file, comment_id):
	comments_seen_reader = open(comments_seen, 'r')

	if comment_id in comments_seen_reader.read().splitlines():
		print("Comment " + comment_id +  " already visited. Skipping.")
		print("-----------------------------------------------------------------")
		comments_seen_reader.close()
		return True

	comments_seen_reader.close()	
	return False

def get_comment_time(time_utc):
	time_human_readable = datetime.datetime.utcfromtimestamp(time_utc)
	print("")
	print("Comment posted on " + str(time_human_readable) + " UTC")


def get_sentiment_analysis(get_sentiment, get_subjectivity):
	if get_sentiment:
		comment_text_blob = TextBlob(comment_text)
		print("")
		print("Sentiment:")
		print("Polarity = " + str(comment_text_blob.sentiment.polarity))

		if get_subjectivity:
			print("Subjectivity = " + str(comment_text_blob.sentiment.subjectivity))
			print("")

def get_comment_score(get_score, get_score_breakdown):
	if bot_config.get_score:
		print("Comment Score = " + str(comment.score))
		if bot_config.get_score_breakdown:
			print("Comment Upvotes = " + str(comment.ups))
			print("Comment Downvotes = " + str(comment.downs))

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

			# Print Time of comment
			get_comment_time(comment.created_utc)
			
			# Print URL
			print(comment.submission.url + comment.id)
			print("")

			# Print Body
			comment_text = comment.body
			print("Comment Text:")
			print(comment_text)
			
			# Analyze and print sentiment:
			get_sentiment_analysis(bot_config.get_sentiment, bot_config.get_subjectivity)

			# Comment Score
			get_comment_score(bot_config.get_comment_score, bot_config.get_score_breakdown)

			print("-----------------------------------------------------------------")

if __name__ == '__main__':

	# Fetch data from bot_config
	subreddit_name = bot_config.subreddit_name
	search_term = bot_config.search_term

	# Init and run bot
	reddit = init_bot_login()
	run_bot(reddit, subreddit_name, search_term)
