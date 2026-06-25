import streamlit as st
import re

txt = st.text_area(
    "Copy from SEM starting at HAZARDOUS CHEMICALS POTENTIALLY ENCOUNTERED BY LABOR CATEGORY")

#finding individual exposures
pattern = r"Review details for this chemical \t(.*?) CAS"
matches = re.findall(pattern, txt)

st.write("Exposures:")
#print list
for i in matches:
  st.write(i.strip())
