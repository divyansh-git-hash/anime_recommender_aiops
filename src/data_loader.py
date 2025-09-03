import pandas as pd

class AnimeDataLoader:

    def __init__(self, org_csv:str,processed_csv:str):
        self.org_csv = org_csv
        self.processed_csv = processed_csv

    def load_processed_data(self):
        df=pd.read_csv(self.org_csv, encoding="utf-8", on_bad_lines='skip').dropna()
        require_columns={"Name","Genres","sypnopsis"}
        missing_col=set(df.columns)-set(require_columns)
        if missing_col:
            print(f"Missing columns: {missing_col}")

        df["combined_info"] = (
            "Title: " + df["Name"] + " " + df["Genres"] + " " + df["sypnopsis"]
        )

        df[["combined_info"]].to_csv(self.processed_csv, index=False, encoding="utf-8")
        return self.processed_csv