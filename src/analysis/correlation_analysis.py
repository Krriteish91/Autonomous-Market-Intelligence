import pandas as pd

INPUT_PATH = "data/analysis/sentiment_market_merged.csv"

df = pd.read_csv(INPUT_PATH) # type: ignore
df = df.dropna(subset=["avg_sentiment", "daily_return"]) # type: ignore
corr_sent, corr_market = df["avg_sentiment"].std(), df["daily_return"].std()

#correlation = df["avg_sentiment"].corr(df["daily_return"])
count = df[["avg_sentiment", "daily_return"]].isna().sum()
corr = df["avg_sentiment"].corr(df["daily_return"])
df["sentiment_lag_1"] = df["avg_sentiment"].shift(1)
lag_corr = df["sentiment_lag_1"].corr(df["daily_return"])
print("Lag-1 correlation:", lag_corr)


print("Correlation between sentiment and market return:")
print(f"Correlation: {corr:.6f}")


print("Correlation between sentiment and market return:")
print(f"Sentiment STD: {corr_sent}")
print(f"Market Return STD: {corr_market}")
print(f"Missing values:\n{count}")