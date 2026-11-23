import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm

def prepared(df):
    df=df.copy()
    for col in ["Sales","Profit","Discount","Quantity","Income"]:df[col]=pd.to_numeric(df[col],errors="coerce")
    df["Region"]=df["Region"].astype("string").str.strip().str.title()
    return df.dropna(subset=["Sales","Profit","Discount","Quantity","Income"])

def test_sales_mean_is_finite(retail_df):
    assert np.isfinite(prepared(retail_df).Sales.mean())

def test_confidence_interval_contains_mean(retail_df):
    s=prepared(retail_df).Sales
    low,high=stats.t.interval(.95,len(s)-1,loc=s.mean(),scale=stats.sem(s))
    assert low<=s.mean()<=high

def test_welch_t_test_valid_p_value(retail_df):
    df=prepared(retail_df)
    a=df.loc[df.Region=="North","Sales"];b=df.loc[df.Region=="South","Sales"]
    _,p=stats.ttest_ind(a,b,equal_var=False)
    assert np.isfinite(p) and 0<=p<=1

def test_pearson_correlation_valid(retail_df):
    df=prepared(retail_df)
    r,p=stats.pearsonr(df.Discount,df.Profit)
    assert -1<=r<=1 and 0<=p<=1

def test_regression_r_squared_valid(retail_df):
    df=prepared(retail_df)
    fit=sm.OLS(df.Sales,sm.add_constant(df[["Quantity","Discount","Income"]])).fit()
    assert 0<=fit.rsquared<=1

def test_regression_coefficients_finite(retail_df):
    df=prepared(retail_df)
    fit=sm.OLS(df.Sales,sm.add_constant(df[["Quantity","Discount","Income"]])).fit()
    assert np.isfinite(fit.params.to_numpy()).all()
