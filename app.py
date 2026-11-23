import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
st.set_page_config(page_title="Retail Statistical Evidence",layout="wide")
st.title("Retail Statistical Evidence")
st.caption("Faiz Ahmad | Roll: 2026M01410048 | Data Analyst Mini Project 3")
@st.cache_data
def load():
    df=pd.read_csv(Path(__file__).parent / "retail_customer_sales_dataset.csv")
    for col in ["Sales","Profit","Discount","Age","Income","Quantity"]:
        df[col]=pd.to_numeric(df[col],errors="coerce")
    df["Region"]=df["Region"].astype("string").str.strip().str.title()
    df["Order_Date"]=pd.to_datetime(df["Order_Date"],errors="coerce",format="mixed")
    return df
df=load()
from scipy import stats
import statsmodels.api as sm
st.subheader("Evidence-based retail statistics")
clean=df.dropna(subset=["Sales","Profit","Discount","Quantity","Income"]).copy()
metric=st.selectbox("Confidence interval metric",["Sales","Profit"])
v=clean[metric];mean=v.mean();sem=stats.sem(v);lo,hi=stats.t.interval(.95,len(v)-1,loc=mean,scale=sem)
a,b,c=st.columns(3);a.metric("Sample size",len(v));b.metric("Mean",f"₹{mean:,.2f}");c.metric("95% confidence interval",f"₹{lo:,.0f}–₹{hi:,.0f}")
st.markdown("#### North vs South: Welch t-test")
x=clean.loc[clean.Region=="North","Sales"];y=clean.loc[clean.Region=="South","Sales"]
t,p=stats.ttest_ind(x,y,equal_var=False)
st.write({"t statistic":round(float(t),4),"p value":round(float(p),6),"Decision at alpha=0.05":"Reject H0" if p<.05 else "Fail to reject H0"})
st.markdown("#### Discount and profit: Pearson correlation")
r,cp=stats.pearsonr(clean["Discount"],clean["Profit"])
st.write({"Pearson r":round(float(r),4),"p value":round(float(cp),6)})
st.caption("Correlation is not proof of causation.")
st.markdown("#### Multiple linear regression: Sales ~ Quantity + Discount + Income")
model=sm.OLS(clean["Sales"],sm.add_constant(clean[["Quantity","Discount","Income"]])).fit()
st.write("R²",round(float(model.rsquared),4))
st.dataframe(pd.DataFrame({"Coefficient":model.params,"p-value":model.pvalues}),use_container_width=True)
st.caption("The submitted statistics notebook includes the required ANOVA, chi-square, simple regression, hypotheses, assumptions and written conclusions.")
