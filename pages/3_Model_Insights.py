import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.title('Model Insights')
st.text('This page provides insights on model performance')

model = st.sidebar.radio('Select Model:', options = ['AdaBoost', 'Random Forest', 'XGBoost', 'Ensemble Voting'])

tab1, tab2, tab3 = st.tabs(['Classification Report', 'Confusion Matrix', 'Feature Importance'])

if model == 'AdaBoost':
    with tab1:
        st.subheader('AdaBoost Classification Report')
        cr_df = pd.read_csv('ada_report.csv', index_col= 0)
        cr_df = cr_df.transpose()
        styled_cr_df = cr_df.style.background_gradient(cmap = 'Greens')
        st.dataframe(styled_cr_df)
        st.caption('Provides metrics used to check model performance')

    with tab2:
        st.subheader('AdaBoost Confusion Matrix')
        st.image('ada_matrix.svg')
        st.caption('Provides accuracy of model predictions')

    with tab3:
        st.subheader('AdaBoost Feature Importance')
        st.image('ada_importance.svg')
        st.caption('Provides importance of feature used by the model')

elif model == 'Random Forest':
    with tab1:
        st.subheader('Random Forest Classification Report')
        cr_df = pd.read_csv('rf_report.csv', index_col= 0)
        cr_df = cr_df.transpose()
        styled_cr_df = cr_df.style.background_gradient(cmap = 'Reds')
        st.dataframe(styled_cr_df)
        st.caption('Provides metrics used to check model performance')

    with tab2:
        st.subheader('Random Forest Confusion Matrix')
        st.image('rf_matrix.svg')
        st.caption('Provides accuracy of model predictions')

    with tab3:
        st.subheader('Random Forest Feature Importance')
        st.image('rf_importance.svg')
        st.caption('Provides importance of feature used by the model')

elif model == 'XGBoost':
    with tab1:
        st.subheader('XGBoost Classification Report')
        cr_df = pd.read_csv('xg_report.csv', index_col= 0)
        cr_df = cr_df.transpose()
        styled_cr_df = cr_df.style.background_gradient(cmap = 'Blues')
        st.dataframe(styled_cr_df)
        st.caption('Provides metrics used to check model performance')

    with tab2:
        st.subheader('XGBoost Confusion Matrix')
        st.image('xg_matrix.svg')
        st.caption('Provides accuracy of model predictions')

    with tab3:
        st.subheader('XGBoost Feature Importance')
        st.image('xg_importance.svg')
        st.caption('Provides importance of feature used by the model')

elif model == 'Ensemble Voting':
    with tab1:
        st.subheader('Ensemble Voting Classification Report')
        cr_df = pd.read_csv('ensemble_report.csv', index_col= 0)
        cr_df = cr_df.transpose()
        styled_cr_df = cr_df.style.background_gradient(cmap = 'Purples')
        st.dataframe(styled_cr_df)
        st.caption('Provides metrics used to check model performance')

    with tab2:
        st.subheader('Ensemble Voting Confusion Matrix')
        st.image('ensemble_matrix.svg')
        st.caption('Provides accuracy of model predictions')

    with tab3:
        st.subheader('Ensemble Voting Feature Importance')
        st.image('ensemble_importance.svg')
        st.caption('Provides importance of feature used by the model')

