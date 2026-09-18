#!/bin/zsh
cd "$(dirname "$0")"
set -a; . ./.env; set +a
export BUDGET_USD=12
echo "=== phase 2a $(date)"
uv run run.py --datasets banking77_train,trec_train,emotion_train,sst2_train,ag_news_train --concurrency 16
echo "=== phase 2b $(date)"
uv run run.py --datasets tweet_sentiment,tweet_hate,tweet_irony,tweet_offensive,tweet_emotion,sst5,rotten_tomatoes,imdb,newsgroups,dbpedia,yelp,sms_spam,enron_spam,mnli,rte --concurrency 16
echo "=== CHAIN DONE $(date)"
