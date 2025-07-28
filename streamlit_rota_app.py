import streamlit as st
import pandas as pd
from collections import defaultdict

st.title("AI Rota Generator (Prototype)")

uploaded_file = st.file_uploader("Upload staff preferences CSV", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Staff Data", df)

    days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    rota = defaultdict(list)

    for day in days:
        for idx, row in df.iterrows():
            available_days = row['Availability'].split(',')
            if day in available_days:
                rota[day].append(row["Name"])

    # Padding: Make all lists the same length
    max_length = max(len(staff_list) for staff_list in rota.values())
    for day in days:
        while len(rota[day]) < max_length:
            rota[day].append("")

    rota_df = pd.DataFrame(dict(rota)).T
    rota_df.columns = [f"Slot {i+1}" for i in range(rota_df.shape[1])]
    rota_df.index.name = "Day"

    st.write("### Generated Rota", rota_df)

    csv = rota_df.to_csv().encode('utf-8')
    st.download_button("Download Rota CSV", data=csv, file_name="generated_rota.csv", mime="text/csv")
