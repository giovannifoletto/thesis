#!/usr/bin/python3
from Parsing.utils import feature_extraction, drain_testing, refine_to_json
import argparse

corpus = []
unique_keys = set()
output_keys = []

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["train", "prepare", "predict"])
    args = parser.parse_args()

    if args.mode == "train":
        print("TRAINING")
        pass
    elif args.mode == "prepare":
        refine_to_json()
    else:
        #feature_extraction()
        drain_testing()

