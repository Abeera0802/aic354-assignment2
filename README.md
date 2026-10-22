# Assignment 2: End-to-End Machine Learning

**Abeera | SP24-BSE-004 | AIC354 | Fall 2026**

GitHub: https://github.com/Abeera0802/aic354-assignment2

**Both cloud apps verified on 22 October 2026 (Asia/Karachi).**

- [Titanic live app](https://abeera-sp24-bse-004-titanic.streamlit.app/)
- [Heart Disease live app](https://abeera-sp24-bse-004-heart.streamlit.app/)

Default and changed-input predictions matched the saved local models. Each notebook starts with its own live link.

| Task | Executed notebook | Source data | Trained model | Streamlit entry point |
|---|---|---|---|---|
| Titanic | `Titanic/Titanic.ipynb` | `Titanic/data/titanic.csv` | `Titanic/models/model_bundle.pkl` | `Titanic/app.py` |
| Heart Disease | `Heart_Disease/Heart_Disease.ipynb` | `Heart_Disease/data/processed.cleveland.data` | `Heart_Disease/models/model_bundle.pkl` | `Heart_Disease/app.py` |

The notebooks contain saved outputs and generate their own models, evaluation plots, CSV predictions,
inference helper and web app. HTML copies are included for easy reading. The source UCI data and
the instructor's 100-row Titanic data were downloaded independently from their official sources.

## Run on this computer

From `C:\Users\MY PC\Desktop\Abeera` in PowerShell:

```powershell
.\.venv\Scripts\python.exe -m notebook SP24-BSE-004_Abeera_ML_Assignment_2
.\.venv\Scripts\python.exe -m streamlit run SP24-BSE-004_Abeera_ML_Assignment_2/Titanic/app.py
# A separate terminal for the heart app:
.\.venv\Scripts\python.exe -m streamlit run SP24-BSE-004_Abeera_ML_Assignment_2/Heart_Disease/app.py --server.port 8502
```

## Run after extracting elsewhere

Use Python 3.14. From this folder:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-notebook.txt
.\.venv\Scripts\python.exe -m notebook
```

Choose the environment's Python kernel and Restart Kernel / Run All. On Linux use `.venv/bin/python`.
Keep pinned scikit-learn consistent with the saved bundles, or retrain before deploying with a different version.
Only load the included trusted model bundles. They were freshly trained for this submission.

## Design and method

The Streamlit apps use Abeera's cream, plum and navy visual design with an illustrated banner,
side identity panel, input/result columns and separate model report and data guide tabs.
The heart model uses exactly **age, cp, thalach and oldpeak**, with `num > 0` as its target.
The numbered teaching steps and SVC algorithm are retained; dataset-specific changes are explained.
The score and limitations are measured in each notebook, not copied from a classmate's results.

## Deployment and submission

1. Upload this folder's contents to `https://github.com/Abeera0802/aic354-assignment2` under branch `main`.
2. In Abeera's Streamlit Community Cloud workspace choose Create app, deploy an existing GitHub app.
3. Deploy `Titanic/app.py` and `Heart_Disease/app.py` as two apps from the same repo; choose Python 3.14.
4. Verify default and changed-input predictions against the locally saved models, then record the actual URLs in the first notebook cells.
5. Upload the notebooks, code, datasets and trained model bundles to Google Classroom per the instructor's instructions.

Cloud status must be read from `deployment_status.json`. A local test does not establish a cloud deployment.
No claim is made that the assignment has been uploaded to Google Classroom.

## Attribution and limitations

- Teaching workflow: https://github.com/haqnawaz99/ml-teaching-notebooks (commit `c5f67db8361bd8953c4facf9e5ab98ce9242f314`).
  Original authors: Mr. Mohsin Afzal and Dr. Rao Muhammad Adeel Nawab.
- UCI Heart Disease: Janosi, A., Steinbrunn, W., Pfisterer, M., & Detrano, R. (1989),
  https://doi.org/10.24432/C52P4X, CC BY 4.0. Cleveland subset only.
- `PROVENANCE.json` records dataset hashes and selected attributes.
- Prepared with AI assistance. Abeera should understand the code, results and limitations before submission.
- Heart predictions are educational and are not medical advice or a clinical diagnosis.
- No real external reviewer feedback is claimed; a blank template is supplied.
