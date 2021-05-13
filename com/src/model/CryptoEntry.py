import datetime

class CryptoEntry:
    post = None
    coin = None
    sub_reddit = None
    timestamp = None

    def __init__(self, post: str, coin: str, sub_reddit: str, timestamp: datetime):
        self.post = post
        self.coin = coin
        self.sub_reddit = sub_reddit
        self.timestamp = timestamp

    def display(self):
        print("post: " + str(self.post))
        print("coin: " + self.coin)
        print("sub_reddit: " + self.sub_reddit)
        print("timestamp: " + str(self.timestamp))
    