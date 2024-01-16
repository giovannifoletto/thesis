#!/usr/bin/python3
from Parsing.utils import feature_extraction, drain_testing, refine_to_json
from other_ideas import use_spell_vectorizer, log_components_extraction
import argparse

corpus = []
unique_keys = set()
output_keys = []

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["train", "prepare", "predict", "template"])
    parser.add_argument("--templating", choices=["spell", "drain"], required=False)
    
    args = parser.parse_args()

    if args.mode == "template":
        if args.templating == "spell":
            feature = feature_extraction()
            use_spell_vectorizer(feature)
        elif args.templating == "drain":
            feature_extraction()
            drain_testing()
        else:
            print("Not implemented")
    if args.mode == "train":
        print("TRAINING")
    elif args.mode == "prepare":
        refine_to_json()
    else:
        #feature_extraction()
        drain_testing()

