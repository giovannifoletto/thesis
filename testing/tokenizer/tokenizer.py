import numpy as np
import polars as pl

from enum import Enum
class AWSKubeLog(Enum):
    userAgent: str
    eventID: str
    eventType: str
    sourceIpAddress: str
    eventName: str
    eventSource: str
    recipientAccountId: str
    awsRegion: str
    requestID: str
    eventVersion: str
    eventTime: str
    errorMessage: str
    errorCode: str
    readOnly: str 

class Tokenizer:
    def __init__(self, path):
        self.dlp    = pl.read_csv(path)
        self.columns= dict()

    def create_vocabulary(self):
        for col in self.dlp.columns:
            self.columns[col] = self.dlp.select(pl.col(col)).unique().to_numpy()

    def get_token(self, value):
        for col in self.columns:
            print(f"Col: {col}")

    def main(self):
        self.create_vocabulary()
        self.get_token()


if __name__ == "__main__":

    path = "../data/fixed.csv"

    tokenizer = Tokenizer()
    tokenizer.main()
