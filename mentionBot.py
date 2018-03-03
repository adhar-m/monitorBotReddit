import praw
import datetime
from textblob import TextBlob

import praw_config
import bot_config

def init_bot_login():
	# Initialize PRAW with config file details and return reddit object
	reddit = praw.Reddit(client_id=praw_config.client_id, client_secret=praw_config.client_secret, user_agent=praw_config.user_agent)
	return reddit
 
def run_bot(reddit_instance, subreddit_name, string_to_match):

	# Point bot to desired subreddit(s)
	subreddit = reddit_instance.subreddit(subreddit_name)

	for comment in subreddit.stream.comments():
		if string_to_match in comment.body.lower():

			# Print Time of comment
			time_utc = comment.created_utc
			time_human_readable = datetime.datetime.utcfromtimestamp(time_utc)
			print("")
			print("Comment posted on " + str(time_human_readable) + " UTC")

			# Print URL
			print(comment.submission.url + comment.id)
			print("")

			# Print Body
			comment_text = comment.body
			print("Comment Text:")
			print(comment_text)
			
			# Analyze and print sentiment:
			comment_text_blob = TextBlob(comment_text)
			print("")
			print("Sentiment:")
			print("Polarity = " + str(comment_text_blob.sentiment.polarity))
			print("Subjectivity = " + str(comment_text_blob.sentiment.subjectivity))
			print("")

			# Comment Score
			print("Comment Score = " + str(comment.score))
			print("Comment Upvotes = " + str(comment.ups))
			print("Comment Downvotes = " + str(comment.downs))

			print("-----------------------------------------------------------------")



if __name__ == '__main__':

	# Fetch data from bot_config
	subreddit_name = bot_config.subreddit_name
	search_term = bot_config.search_term

	# Init and run bot
	reddit = init_bot_login()
	run_bot(reddit, subreddit_name, search_term)