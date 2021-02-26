class CryptoEntry:
    post_hash = None
    coin = None
    sub_reddit = None
    timestamp = None

    def __init__(self, post_hash: str, coin: str, sub_reddit: str, timestamp: str):
        self.post_hash = post_hash
        self.coin = coin
        self.sub_reddit = sub_reddit
        self.timestamp = timestamp

    