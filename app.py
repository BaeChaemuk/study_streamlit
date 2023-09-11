import pandas as pd
import streamlit as st

view = [100,50,150]
st.write('# Youtube view')
st.write('## raw')
view
st.write('#bar chart')
st.bar_chart(view)

Sview = pd.Series(view)
Sview