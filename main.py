import pickle
import streamlit as st

# loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    
   with st.sidebar: 
    
    st.title("Multiple Desease Prediction System")
    choice = st.radio("Navigation", ["Diabetes Prediction","Heart Disease Prediction","Parkinsons Prediction"])
    st.info("Project is not 100% accurate ")
    
    
# Diabetes Prediction Page
if choice == 'Diabetes Prediction':
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies ( 0 - 17)')
        
    with col2:
        Glucose = st.text_input('Glucose Level (0 - 199)')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value ( 0 - 122)')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value ( 0 - 99)')
    
    with col2:
        Insulin = st.text_input('Insulin Level ( 0 - 846)')
    
    with col3:
        BMI = st.text_input('BMI value ( 0 - 67.1) ')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value ( 0.078 - 2.42 ) ')
    
    with col2:
        Age = st.text_input('Age of the Person ( 21 - 81)')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if choice == 'Heart Disease Prediction':
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)


# Parkinson's Prediction Page
if choice == "Parkinsons Prediction":
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz) ( 88 - 260)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz) (102 - 592) ')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz) (65 - 239)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%) (0.001680 - 0.033160)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs) ( 0.000007 - 0.000260)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP (0.000680 - 0.021440)')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ (0.000920 - 0.019580)')
        
    with col3:
        DDP = st.text_input('Jitter:DDP ( 0.002040 - 0.064330) ')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer (0.009540 - 0.119080)')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB) (0.085000 - 1.302000)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3 (0.01026 - 0.03134)')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5 (0.01161 - 0.04518)')
        
    with col3:
        APQ = st.text_input('MDVP:APQ (0.01373 - 0.04368)')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA ( 0.013640	- 0.169420)')
        
    with col5:
        NHR = st.text_input('NHR (0.000650 -  0.314820)')
        
    with col1:
        HNR = st.text_input('HNR (8.441000 - 33.047000 )')
        
    with col2:
        RPDE = st.text_input('RPDE (0.256570 - 0.685151)')
        
    with col3:
        DFA = st.text_input('DFA (0.574282 - 0.825288 )')
        
    with col4:
        spread1 = st.text_input('spread1 (-7.964984 - -2.434031 )')
        
    with col5:
        spread2 = st.text_input('spread2 ( 0.006274 - 0.450493)')
        
    with col1:
        D2 = st.text_input('D2 ( 1.423287 - 3.671155)')
        
    with col2:
        PPE = st.text_input('PPE (0.044539 - 0.527367)')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)
    hide_st_style = """
            <style>
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
              Design and Developed by Japanjot Singh 
            """
st.markdown(hide_st_style , unsafe_allow_html=True)
