# Retail Statistical Evidence — Faiz Ahmad

**Student:** Faiz Ahmad  
**Roll:** 2026M01410048  
**Topic:** Project 3 — Advanced Statistics (Retail Customer Sales)

## Run Streamlit

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

The dashboard reads `retail_customer_sales_dataset.csv` from the project root.

## Run tests

```bash
python -m pip install -r requirements.txt -r requirements-dev.txt
python -m pytest -q tests
```

Saved test output is in `outputs/test_results.txt`. Tests verify dataset, statistical calculations, and app source syntax. They do **not** certify a live browser deployment.

## Files

- `app.py`: Streamlit dashboard
- `notebooks/`: original statistics notebook
- `reports/`: synopsis, project report, code snapshot, test report
- `outputs/statistics_summary.json`: computed results from this dataset
- `tests/`: executable automated tests

**GitHub URL:** To be added after repository creation.  
**Streamlit URL:** To be added after deployment.
