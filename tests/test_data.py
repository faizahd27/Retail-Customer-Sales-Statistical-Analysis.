import pandas as pd

def test_dataset_not_empty(retail_df):
    assert len(retail_df)>0

def test_expected_columns(retail_df):
    assert {"Sales","Profit","Discount","Quantity","Income","Region"}.issubset(retail_df.columns)

def test_sales_has_numeric_values(retail_df):
    assert pd.to_numeric(retail_df["Sales"],errors="coerce").notna().any()

def test_profit_has_numeric_values(retail_df):
    assert pd.to_numeric(retail_df["Profit"],errors="coerce").notna().any()

def test_region_groups_present(retail_df):
    regions=set(retail_df["Region"].astype(str).str.strip().str.title())
    assert {"North","South"}.issubset(regions)

def test_analysis_sample_nonempty(retail_df):
    fields=["Sales","Profit","Discount","Quantity","Income"]
    clean=retail_df.copy()
    for field in fields:clean[field]=pd.to_numeric(clean[field],errors="coerce")
    assert len(clean.dropna(subset=fields))>20
