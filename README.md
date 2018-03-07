# Mention Bot (Reddit)
A bot to let you easily monitor subreddits of your choice for mentions of your product/company. It also returns the sentiment (polarity and subjectivity) of that comment, along with its score. Useful for entrepreneurs or customer service representatives who want to monitor conversations about their products and respond to customer feedback on Reddit.

Still very much in progress.

# Requirements
In order to run the script, make sure you have the following installed:
- python 3 
- praw 5.3.0
- textblob 0.15.1

# Instructions
1. Make a reddit account and register your app as a script
2. Enter your details in the praw_config.py file
3. Set your preferences for the bot in bot_config.py (including search term, subreddit, sentiment analysis and comment score on/off)
4. Run mentionBot.py from your terminal