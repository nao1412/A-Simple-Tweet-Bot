# coding : UTF-8
import twitter
import time
import schedule

def main1():
  auth = twitter.OAuth(consumer_key="XXX",
  consumer_secret="XXX",
  token="XXX",
  token_secret="XXX")

  def tweet():
    TWEET_FILE_NAME = "content/tweets.txt"

    with open(TWEET_FILE_NAME, "r", encoding="utf-8") as f:
      file_content = f.read()

    t = twitter.Twitter(auth=auth)

    #投稿するツイート
    t.statuses.update(status=file_content) #Twitterに投稿

  tweet()

if __name__ == '__main__':
  main1()

