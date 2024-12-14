import streamlit as st
from add_update import add_update_tab
from add_analytics_by_category import analytics_tab
from analytics_month import analytics_months_tab

API_URL="http://127.0.0.1:8000"

st.title("Expense Management System")

tab1, tab2, tab3 = st.tabs(["Add/Update", "Analytics By Category", "Analytics By Months"])
with tab1:
    add_update_tab()

with tab2:
    analytics_tab()

with tab3:
    analytics_months_tab()