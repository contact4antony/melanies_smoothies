# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
st.text(fruityvice_response)
