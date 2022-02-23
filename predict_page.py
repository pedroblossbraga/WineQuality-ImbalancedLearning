import streamlit as st
import pickle
import numpy as np

def load_model():
    # loading the saved model
    with open('saved_model.pkl', 'rb') as file:
        data = pickle.load(file)

    return data['model']

model = load_model()

def show_predict_page():
    st.title('Wine Quality Prediction')
    
    st.write("""### Inform the wine features""")

    fixed_acidity = st.slider('fixed acidity', 4.0, 16.0, 8.319)
    volatile_acidity = st.slider('volatile acidity', 0.1, 1.6, 0.527)
    citric_acid = st.slider('citric acid', 0.0, 1.0, 0.27)
    residual_sugar = st.slider('residual sugar', 0.9, 15.5, 2.5)
    chlorides = st.slider('chlorides', 0.01, 0.7, 0.087)
    free_sulfur_dioxide = st.slider('free sulfur dioxide', 1.0, 72.0, 15.87)
    total_sulfur_dioxide = st.slider('total sulfur dioxide', 6.0, 289.0, 46.46)
    density = st.slider('density', 0.99, 1.1, 0.996)
    pH = st.slider('pH', 2.7, 4.1, 3.31)
    sulphates = st.slider('sulphates', 0.33, 2.0, 0.65)
    alcohol = st.slider('alcohol', 8.4, 15.0, 10.42)

    show_values = st.button('Show input')
    if show_values:
        st.write(""" You have selected the following input: """)
        st.write('{}'.format(
            dict(zip(
                ['fixed acidity',
                'volatile acidity',
                'citric acid',
                'residual sugar',
                'chlorides',
                'free sulfur dioxide',
                'total sulfur dioxide',
                'density',
                'pH',
                'sulphates',
                'alcohol',
                'quality'],
                [fixed_acidity,
                volatile_acidity,
                citric_acid,
                residual_sugar,
                chlorides,
                free_sulfur_dioxide,
                total_sulfur_dioxide,
                density,
                pH,
                sulphates,
                alcohol]
                ))
            ))
    show_model = st.button('Show model')
    if show_model:
        st.write('Model: {}'.format(model))

    ok = st.button('Estimate Prediction')

    if ok: # clicked on the button
        X = np.array(
            [[
                fixed_acidity,
                volatile_acidity,
                citric_acid,
                residual_sugar,
                chlorides,
                free_sulfur_dioxide,
                total_sulfur_dioxide,
                density,
                pH,
                sulphates,
                alcohol
            ]]
        )

        wine_quality = model.predict(X)[0]

        st.subheader(f"Estimated wine quality is {wine_quality}")
