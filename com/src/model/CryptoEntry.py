import datetime

class CryptoEntry:
    post_hash = None
    coin = None
    sub_reddit = None
    timestamp = None

    def __init__(self, post_hash: str, coin: str, sub_reddit: str, timestamp: datetime):
        self.post_hash = post_hash
        self.coin = coin
        self.sub_reddit = sub_reddit
        self.timestamp = timestamp

    def display(self):
        print("post_hash: " + str(self.post_hash))
        print("coin: " + self.coin)
        print("sub_reddit: " + self.sub_reddit)
        print("timestamp: " + str(self.timestamp))
    