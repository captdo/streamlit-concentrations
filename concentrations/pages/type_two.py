import streamlit as st
from ..utils.unit_convertion import (
    set_power_ten,
    strip_power_ten,
)


st.header("Type 2 conversion:")

with st.form("Type One Form"):
    volume = st.number_input(label="Volume")
    volume_unit = st.radio(label="C1 Unit", horizontal=True, options=["L", "mL", "uL"])
    c2 = st.number_input(label="C2")
    c2_unit = st.radio(label="C2 Unit", horizontal=True, options=["L", "mL", "uL"])
    mw = st.number_input(label="Mw")

    output_unit = st.radio(
        label="Output Unit", horizontal=True, options=["g", "mg", "ug", "L", "mL", "uL"]
    )
    submitted = st.form_submit_button("Submit")
    if submitted:
        if volume_unit != "L":
            power = (-3, -6)["mL" == volume_unit]
            volume = strip_power_ten(volume, power)
        if c2_unit != "L":
            power = (-3, -6)["mMol" == c2_unit]
            c2 = strip_power_ten(c2, power)

        result = mw * c2 * volume

        if "m" in output_unit:
            result = set_power_ten(result, -3)
        elif "u" in output_unit:
            result = set_power_ten(result, -6)

        st.write(f"The result is: {result} {output_unit}")
