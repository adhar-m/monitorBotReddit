# Enter the name of the subreddit(s) you want to monitor.
# Multiple subs can be monitored by entering: "sub1+sub2+sub3"
subreddit_name = "Change Me!"

# Enter the search term you want to monitor (eg: your company's name)
search_term = "Change Me!"

# Name of file storing comments already seen
comments_seen = "comments_seen.txt"

# The next few options are booleans. True to enable, False to disable

# Conduct sentiment analysis?
get_sentiment = True

# Display subjectivity with sentiment?
get_subjectivity = True

# Fetch Comment Score?
get_score = True

# Fetch number of up/down votes for Score?
get_score_breakdown = True

# Message you the results?
get_messages = True

# Create a digest? If True, how many messages per digest?
get_digest = (True, 10)
