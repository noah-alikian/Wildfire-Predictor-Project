import streamlit as st

st.title('Model Types')
st.image('ML.jpg')
st.text('This is an informational page that allows users to understand the process that each model undergoes to make its prediction.')

st.subheader('AdaBoost')
st.markdown("- **How it Works:** Builds many tiny decision rules; each new one focuses on fixing the last one’s mistakes. They vote together.")
st.markdown("- **When to Use:** You want a quick, simple model for table-style data.")
st.markdown("- **Weaknesses:** Doesn’t handle messy/outlier labels well; can miss very complex patterns.")

st.subheader('Random Forest')
st.markdown("- **How it Works:** Grows lots of decision trees on shuffled versions of your data, then averages their answers.")
st.markdown("- **When to Use:** Safe, strong default for most table-style problems.")
st.markdown("- **Weaknesses:** Can be big and a bit slow; sometimes not as accurate as boosting methods.")

st.subheader('XGBoost')
st.markdown("- **How it Works:** Adds trees one at a time, each one fixing what the last ones got wrong.")
st.markdown("- **When to Use:** You want top accuracy on structured data and can spend a little time tuning.")
st.markdown("- **Weaknesses:** Easier to overfit if set too aggressively; more settings to tweak.")

st.subheader('Ensemble Voting')
st.markdown("- **How it Works:** Combines the three models’ probability scores; the more accurate a model is on validation data, the more say it gets.")
st.markdown("- **When to Use:** You want a steady, reliable result that’s usually better than any single model.")
st.markdown("- **Weaknesses:** If you set the weights using training data, it can “cheat”. Needs well-calibrated probabilities. Uses more computer power.")

st.sidebar.subheader('Model Documentation')
model = st.sidebar.selectbox('Select Model:', options = ['AdaBoost', 'Random Forest', 'XGBoost', 'Ensemble Voting'])
if model == 'AdaBoost':
    st.sidebar.markdown('- https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html')
elif model == 'Random Forest':
    st.sidebar.markdown('- https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html')
elif model == 'XGBoost':
    st.sidebar.markdown('- https://xgboost.readthedocs.io/en/stable/')
elif model == 'Ensemble Voting':
    st.sidebar.markdown('- No documentation as this model is a combination of the other three models used for this app.')