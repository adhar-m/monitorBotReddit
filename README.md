# Mention Bot (Reddit)
A bot to let you easily monitor subreddits of your choice for mentions of your product/company. It also returns the sentiment (polarity and subjectivity) of that comment, along with its score. Useful for entrepreneurs or customer service representatives who want to monitor conversations about their products and respond to customer feedback on Reddit.

Still very much in progress.

# Requirements
In order to run the script, make sure you have the following installed:
- python 3 
- praw 5.3.0
- textblob 0.15.1

# Instructions
1. Clone or download this repository
2. [Authorize this app as a script](https://github.com/reddit-archive/reddit/wiki/OAuth2) from your reddit account
3. Enter your authorization details in the praw_config.py file
4. Set your settings for the bot in bot_config.py (including search term, subreddit, sentiment analysis and comment score on/off)
5. Run mentionBot.py from your terminal

#Sample Alert
![Sample Alert](https://pasteboard.co/HdtIcsv.png)