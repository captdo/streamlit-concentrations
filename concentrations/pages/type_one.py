import streamlit as st
from ..utils.unit_convertion import (
    set_power_ten,
    strip_power_ten,
)


st.header("Type 1 conversion:")

with st.form("Type One Form"):
    c1 = st.number_input(label="C1")
    c1_unit = st.radio(
        label="C1 Unit", horizontal=True, options=["Mol", "mMol", "uMol"]
    )
    c2 = st.number_input(label="C2")
    c2_unit = st.radio(
        label="C2 Unit", horizontal=True, options=["Mol", "mMol", "uMol"]
    )
    mw = st.number_input(label="Mw")

    output_unit = st.radio(
        label="Output Unit", horizontal=True, options=["g", "mg", "ug", "L", "mL", "uL"]
    )
    submitted = st.form_submit_button("Submit")
    if submitted:
        if c1_unit != "Mol":
            power = (-3, -6)["mMol" == c1_unit]
            c1 = strip_power_ten(c1, power)
        if c2_unit != "Mol":
            power = (-3, -6)["mMol" == c2_unit]
            c2 = strip_power_ten(c2, power)

        result = mw * c2 / c1

        if "m" in output_unit:
            result = set_power_ten(result, -3)
        elif "u" in output_unit:
            result = set_power_ten(result, -6)

        st.write(f"The result is: {result} {output_unit}")
