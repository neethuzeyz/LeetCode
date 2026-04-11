import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    invaild_tweets_df = tweets[tweets['content'].str.len()>15]
    result_df = invaild_tweets_df[['tweet_id']]
    return result_df