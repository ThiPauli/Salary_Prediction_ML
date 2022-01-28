#main file
import streamlit as st

#defining the page title and icon 
st.set_page_config(page_title='Salary Estimator', page_icon=':money_with_wings:', layout='wide')

from predict_page import show_predict_page
from explore_page import show_explore_page

# ---- sidebar section -----
# Creating the sidebar section to enable filter pages between explore or predicit
st.sidebar.subheader('Welcome to my Salary Estimator: You can predict it giving specific inputs or explore the numbers globally.')
side_bar_selection = st.sidebar.selectbox('Please Select the Web Page:', ('Predict', 'Explore'))


if side_bar_selection == 'Explore':
    show_explore_page()
else:
    show_predict_page()