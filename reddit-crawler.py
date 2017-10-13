import praw
import json
from tqdm import *

reddit = praw.Reddit(user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36', client_id='N1GOnnH_0kniQg', client_secret='OMk7ujOk9s9CVnu-HSIx2SBl9Xk')

submissions = reddit.subreddit('2007scape').submissions(1494417600, 1497087209)

for submission in tqdm(total=13296, iterable=submissions):
    submission.comments.replace_more(limit=0)
    for comment in submission.comments.list():
        json_comment = {}
        json_comment['author'] = str(comment.author)
        json_comment['created'] = comment.created_utc
        json_comment['message'] = str(comment.body)
        with open('reddit-comments.json', 'a') as outfile:
            json.dump(json_comment, outfile)

