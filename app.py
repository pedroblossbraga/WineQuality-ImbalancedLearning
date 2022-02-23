from matplotlib.pyplot import show
import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page, show_explore_features_page, show_project_page

page = st.sidebar.selectbox('Explore or Predict', ('Predict', 
                                                    'Explore - wine quality',
                                                    'Explore - Features',
                                                    'Project/Contact'))

if page == 'Predict':
    show_predict_page()
elif page == 'Explore - wine quality':
    show_explore_page()
elif page == 'Project/Contact':
    show_project_page()
else:
    show_explore_features_page()