"""Validation and inference shared by the notebook and web interface."""
import math
import pandas as pd


def encode_case(values, bundle):
    if set(values) != set(bundle["features"]):
        raise ValueError("Supply exactly the four declared input attributes.")
    frame = pd.DataFrame([values], columns=bundle["features"])
    if bundle["task"] == "Heart_Disease":
        bounds = {"age": (1, 120), "thalach": (30, 250), "oldpeak": (0, 10)}
        for field, (low, high) in bounds.items():
            value = float(values[field])
            if not math.isfinite(value) or not low <= value <= high:
                raise ValueError(f"{field} must be between {low} and {high}.")
            if field != "oldpeak" and not value.is_integer():
                raise ValueError(f"{field} must be a whole number.")
            frame[field] = value
    for field, encoder in bundle["encoders"].items():
        if values[field] not in encoder.classes_:
            raise ValueError(f"Unknown category for {field}.")
        frame[field] = encoder.transform(frame[field])
    return frame


def predict_case(values, bundle):
    return int(bundle["model"].predict(encode_case(values, bundle))[0])
