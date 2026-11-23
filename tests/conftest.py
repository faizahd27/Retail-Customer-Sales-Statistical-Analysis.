from pathlib import Path
import pandas as pd
import pytest
@pytest.fixture(scope="session")
def retail_df():
    return pd.read_csv(Path(__file__).resolve().parents[1] / "retail_customer_sales_dataset.csv")
