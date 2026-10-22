# Measured results

**Abeera | SP24-BSE-004**

| Held-out measure | Titanic | Heart Disease |
|---|---:|---:|
| Source rows | 100 | 303 |
| Training / testing | 80 / 20 | 242 / 61 |
| Accuracy | 80.00% | 81.97% |
| Positive precision | 100.00% | 84.00% |
| Positive recall | 60.00% | 75.00% |
| Positive F1 | 0.750 | 0.792 |
| ROC AUC | 0.810 | 0.919 |
| Training-majority baseline accuracy | 50.00% | 54.10% |

The heart inputs are age, cp, thalach and oldpeak. The binary target is num > 0.
These are measured outcomes on fixed splits, not claims of clinical or broad historical validity.
Both public cloud apps were checked with default and changed inputs; details are in deployment_status.json.
External user/expert feedback and Google Classroom submission have not been claimed.
