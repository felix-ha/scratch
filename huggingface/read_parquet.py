import pandas as pd
from datasets import load_dataset

path = "huggingface/data/text_data.csv"

df = pd.read_csv(path, sep=";")

path_parquet_train = "huggingface/data/train.parquet"
path_parquet_validation = "huggingface/data/validation.parquet"
df[0:4].to_parquet(path_parquet_train)
df[4:].to_parquet(path_parquet_validation)


dataset = load_dataset("parquet", data_files={'train': path_parquet_train, 'test': path_parquet_validation})

print(dataset)


