import pandas
import streamlit as st

st.set_page_config(layout="wide")

st.title("The Best Company")
st.write("""Consulted perpetual of pronounce me delivered. Too months nay end change relied who beauty wishes matter.
 Shew of john real park so rest we on. Ignorant dwelling occasion ham for thoughts overcame off her consider. Polite 
 it elinor is depend. His not get talked effect worthy barton. Household shameless incommode at no objection behaviour.
  Especially do at he possession insensible sympathize boisterous it. Songs he on an widen me event truth. Certain law 
  age brother sending amongst why covered.
""")

st.header("Our Team")

col1, blank_col1, col2, blank_col2, col3 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5])

company_data = pandas.read_csv("data.csv")

with col1:
    for index, row in company_data[:4].iterrows():
        name = row["first name"].capitalize() + " " + row["last name"].capitalize()
        st.header(name)
        st.write(row["role"])
        st.image("images/" + row["image"])

with col2:
    for index, row in company_data[4:8].iterrows():
        name = row["first name"].capitalize() + " " + row["last name"].capitalize()
        st.header(name)
        st.write(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index, row in company_data[8:].iterrows():
        name = row["first name"].capitalize() + " " + row["last name"].capitalize()
        st.header(name)
        st.write(row["role"])
        st.image("images/" + row["image"])
