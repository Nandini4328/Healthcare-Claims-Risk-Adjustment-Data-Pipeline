import pandas as pd

def transform_data(input_path):
    df = pd.read_json(input_path)

    # Deduplication
    df = df.drop_duplicates(subset=["claim_id"])

    # Simple RAF-like flag
    high_risk_codes = ["E11", "I10"]
    df["high_risk_flag"] = df["diagnosis_code"].isin(high_risk_codes)

    return df

if __name__ == "__main__":
    df = transform_data("../data/sample_claims.json")
    print(df)
