def validate_data(df):
    assert df["claim_id"].isnull().sum() == 0, "Null claim_id found"
    assert df["amount"].min() >= 0, "Negative amount found"
    print("Data quality checks passed!")
