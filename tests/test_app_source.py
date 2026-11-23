from pathlib import Path
import ast

def test_app_python_syntax():
    source=(Path(__file__).resolve().parents[1]/"app.py").read_text(encoding="utf-8")
    ast.parse(source)

def test_app_has_statistical_sections():
    source=(Path(__file__).resolve().parents[1]/"app.py").read_text(encoding="utf-8")
    assert all(x in source for x in ["ttest_ind","pearsonr","OLS","confidence interval"])
