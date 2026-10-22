"""Abeera's Streamlit interface. Recreated by Step 10 of each notebook."""
from pathlib import Path
import html
import pickle

import pandas as pd
import streamlit as st
from inference import predict_case

BASE = Path(__file__).resolve().parent


@st.cache_resource
def load_model(model_path):
    # Only the trusted bundle trained by the accompanying notebook is loaded.
    with Path(model_path).open("rb") as stream:
        return pickle.load(stream)


bundle = load_model(str(BASE / "models/model_bundle.pkl"))
heart = bundle["task"] == "Heart_Disease"
title = "Heart disease explorer" if heart else "Titanic survival explorer"
st.set_page_config(page_title=title + " | Abeera", page_icon="✦", layout="wide")
st.html("""
<style>
.stApp {background: #faf7f2; color: #23283d;}
[data-testid="stHeader"] {background: #faf7f2cc;}
[data-testid="stSidebar"] {background: #ede7f1; border-right: 1px solid #ded3e5;}
.block-container {max-width: 1200px; padding-top: 2rem; padding-bottom: 2rem;}
h1, h2, h3 {color: #26243c; letter-spacing: -.025em;}
.eyebrow {font-size: .72rem; letter-spacing: .16em; font-weight: 700; color: #71547f;}
.brand {font-size: 1.5rem; font-weight: 750; letter-spacing: -.06em; margin: .6rem 0 1.5rem;}
.identity {line-height: 1.8; font-size: .88rem; color: #554c64;}
.hero {background: #28273f; color: #fff9ed; padding: 2rem 2.4rem; border-radius: 24px; margin: .4rem 0 1.5rem; position: relative; overflow: hidden;}
.hero h1 {color: #fff9ed; font-size: clamp(2rem, 3.8vw, 3.1rem); max-width: 80%; margin: .5rem 0;}
.hero p {color: #ded9eb; max-width: 70%; margin-bottom: .3rem;}
.hero .eyebrow {color: #d5b7ec;}
.hero-art {position: absolute; right: 24px; top: 35px; width: 170px; opacity: .85;}
.tag {display: inline-block; background: #f1e7fa; color: #624271; border-radius: 30px; padding: .3rem .7rem; font-size: .75rem; margin-right: .4rem;}
.result-box {background: #efe8f5; border: 1px solid #d9cbe3; border-radius: 20px; padding: 1.6rem; min-height: 260px; margin-top: .5rem;}
.result-box h2 {font-size: 1.8rem; line-height: 1.2; margin: .9rem 0;}
.result-box p {color: #62566e; line-height: 1.6;}
.result-box.empty {background: #f3efe9; border: 1px dashed #d0c5b8;}
.result-label {font-size: .72rem; font-weight: 750; letter-spacing: .13em; color: #755186;}
[data-testid="stForm"] {border: 1px solid #e1d9ce; border-radius: 20px; padding: 1.3rem; background: #fffcf8;}
.stButton>button, .stFormSubmitButton>button {border-radius: 12px; font-weight: 650;}
button[kind="primary"] {background: #725084; border-color: #725084; color: white;}
[data-testid="stMetric"] {background: #fffcf8; border: 1px solid #e3dbd0; padding: 1rem; border-radius: 16px;}
[data-testid="stMetricValue"] {font-size: 1.6rem;}
.footer {border-top: 1px solid #dfd6cb; padding-top: 1rem; margin-top: 2rem; color: #746b7c; font-size: .78rem;}
@media(max-width: 700px) {.hero {padding: 1.5rem;} .hero-art {display: none;} .hero h1,.hero p {max-width: 100%;}}
</style>
""")

with st.sidebar:
    st.html('<div class="eyebrow">AIC354 / ASSIGNMENT 02</div><div class="brand">abeera<span style="color:#87619a">.ml</span></div>')
    st.markdown("**Two datasets. One learning journey.**")
    st.caption("From structured data to a working prediction system.")
    st.divider()
    st.html('<div class="identity"><b>Abeera</b><br>SP24-BSE-004<br>Machine Learning Fundamentals<br>COMSATS, Lahore Campus</div>')
    st.divider()
    st.markdown("**Current experiment**")
    st.write("02 / Heart Disease" if heart else "01 / Titanic")
    st.markdown("[Project on GitHub](https://github.com/Abeera0802/aic354-assignment2)")
    st.caption("Historical data · Educational project")

art = ('<svg viewBox="0 0 180 150"><circle cx="90" cy="75" r="65" fill="#665073"/>'
       '<path d="M20 80h30l15-25 20 52 20-70 17 43h35" stroke="#e4c8f8" stroke-width="4" fill="none" stroke-linejoin="round"/></svg>'
       if heart else '<svg viewBox="0 0 180 150"><circle cx="90" cy="75" r="65" fill="#454566"/>'
       '<path d="M30 91h120l-22 26H52z" fill="#d7c2e8"/><path d="M55 87V68h70v19M70 64V46h15v18M98 64V40h15v24" fill="#eee5d6"/>'
       '<path d="M25 126q16-10 32 0t32 0t32 0t32 0" stroke="#beaccf" stroke-width="3" fill="none"/></svg>')
intro = ("Explore a four-attribute classifier using the UCI Cleveland records." if heart
         else "Build a passenger profile and explore the instructor's survival classifier.")
st.html(f'<div class="hero"><div class="eyebrow">EXPERIMENT {"02" if heart else "01"} / SUPERVISED LEARNING</div><h1>{title}</h1><p>{intro}</p><div class="hero-art">{art}</div></div>')
st.html('<span class="tag">4 input attributes</span><span class="tag">Support Vector Classifier</span><span class="tag">Abeera · SP24-BSE-004</span>')
st.write("")

predict_tab, report_tab, guide_tab = st.tabs(["Make a prediction", "Model report", "Data guide"])
with predict_tab:
    left, right = st.columns([1.12, 1], gap="large")
    with left:
        st.subheader("Configure your case")
        st.caption("Choose all four attributes, then run the model.")
        with st.form("case_form"):
            a, b = st.columns(2)
            if heart:
                pain = {1: "Typical angina", 2: "Atypical angina", 3: "Non-anginal pain", 4: "Asymptomatic"}
                with a:
                    age = st.number_input("Age (years)", 1, 120, 50, 1)
                    rate = st.number_input("Maximum heart rate (beats/min)", 30, 250, 160, 1)
                with b:
                    cp = st.selectbox("Chest-pain type", [1, 2, 3, 4], format_func=lambda x: pain[x])
                    oldpeak = st.number_input("ST depression (oldpeak)", 0.0, 10.0, 1.0, 0.1, help="Exercise-induced ST depression relative to rest, as recorded in UCI.")
                values = {"age": age, "cp": cp, "thalach": rate, "oldpeak": oldpeak}
            else:
                with a:
                    pclass = st.selectbox("Passenger class", ["First", "Second", "Third"])
                    sibling = st.selectbox("Siblings / spouses aboard", ["Zero", "One", "Two", "Three"])
                with b:
                    gender = st.selectbox("Gender", ["Female", "Male"])
                    embarked = st.selectbox("Embarkation port", ["Southampton", "Cherbourg", "Queenstown"])
                values = {"PClass": pclass, "Gender": gender, "Sibling": sibling, "Embarked": embarked}
            submitted = st.form_submit_button("Run prediction →", type="primary", width="stretch")
        if submitted:
            try:
                label = predict_case(values, bundle)
                st.session_state["last_prediction"] = (values.copy(), label)
            except (ValueError, TypeError) as error:
                st.error(str(error))
    with right:
        st.subheader("Prediction")
        st.caption("The result describes your last submitted case.")
        result = st.session_state.get("last_prediction")
        if result:
            used, label = result
            wording = bundle["labels"][label]
            st.html(f'<div class="result-box"><div class="result-label">MODEL OUTPUT / CLASS {label}</div><h2>{html.escape(wording)}</h2><p>This is a predicted class label. It is not an individual probability or a guaranteed outcome.</p></div>')
            with st.expander("View submitted attributes"):
                st.dataframe(pd.DataFrame([used]), hide_index=True, width="stretch")
            if heart and any(not lo <= float(used[name]) <= hi for name, (lo, hi) in bundle["training_ranges"].items()):
                st.warning("One or more values fall outside the training data range. Interpret this result with extra caution.")
        else:
            st.html('<div class="result-box empty"><div class="result-label">READY WHEN YOU ARE</div><h2>A profile becomes<br>a prediction.</h2><p>Complete the form to see the saved model in action.</p></div>')
        if heart:
            st.info("For learning only. This historical-data model is not a medical diagnosis and must not guide treatment.")
        else:
            st.caption("A classroom experiment using a simplified 100-passenger sample.")

with report_tab:
    st.subheader("A look at the held-out results")
    m = bundle["metrics"]
    cols = st.columns(4)
    for col, name, value in zip(cols, ["Test accuracy", "Positive recall", "Positive F1", "Test records"],
                                [f'{m["accuracy"]:.1%}', f'{m["recall"]:.1%}', f'{m["f1"]:.3f}', str(m["test_rows"])]):
        col.metric(name, value)
    st.caption(f'Training records: {m["train_rows"]} · Majority baseline: {m["baseline_accuracy"]:.1%} · One fixed held-out split; future performance may differ.')
    c1, c2 = st.columns([1, 1.3], gap="large")
    with c1:
        st.markdown("**Confusion matrix**")
        st.dataframe(pd.DataFrame(m["confusion_matrix"], index=["Actual 0", "Actual 1"], columns=["Predicted 0", "Predicted 1"]), width="stretch")
    with c2:
        st.markdown("**How to read these results**")
        st.write("Recall measures how many actual positive records the model identified. F1 balances positive precision and recall. The test records were held out during training.")
        st.write(bundle["limitation"])
    st.caption("No external feedback or clinical validation has been claimed.")

with guide_tab:
    st.subheader("Know the four inputs")
    st.dataframe(pd.DataFrame(bundle["feature_guide"]), hide_index=True, width="stretch")
    st.markdown("**Output labels**")
    for code, text in bundle["labels"].items():
        st.write(f"{code} — {text}")
    st.markdown(f'[Original data / teaching source]({bundle["source_url"]})')
    st.caption("Inputs are processed in memory for prediction; this app does not save personal records.")

st.html('<div class="footer">Designed and prepared for Abeera · SP24-BSE-004 &nbsp; / &nbsp; AIC354 · Fall 2026</div>')
