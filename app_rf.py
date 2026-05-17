import pickle
import streamlit as st
import pandas as pd

# =========================
# LOAD MODEL
# =========================
model = pickle.load(open('rf_model.pkl', 'rb'))

# =========================
# TITLE
# =========================
st.title('HR Employee Attrition Classification App')

# =========================
# INPUTS
# =========================

Age = st.number_input('Age', min_value=18, max_value=60, value=36)

DailyRate = st.number_input(
    'DailyRate',
    min_value=102,
    max_value=1499,
    value=802
)

DistanceFromHome = st.number_input(
    'DistanceFromHome',
    min_value=1,
    max_value=29,
    value=7
)

Education = st.number_input(
    'Education',
    min_value=1,
    max_value=5,
    value=3
)

EmployeeNumber = st.number_input(
    'EmployeeNumber',
    min_value=1,
    max_value=2068,
    value=1020
)

EnvironmentSatisfaction = st.number_input(
    'EnvironmentSatisfaction',
    min_value=1,
    max_value=4,
    value=3
)

HourlyRate = st.number_input(
    'HourlyRate',
    min_value=30,
    max_value=100,
    value=66
)

JobInvolvement = st.number_input(
    'JobInvolvement',
    min_value=1,
    max_value=4,
    value=3
)

JobLevel = st.number_input(
    'JobLevel',
    min_value=1,
    max_value=5,
    value=2
)

JobSatisfaction = st.number_input(
    'JobSatisfaction',
    min_value=1,
    max_value=4,
    value=3
)

MonthlyIncome = st.number_input(
    'MonthlyIncome',
    min_value=1009,
    max_value=19999,
    value=4919
)

MonthlyRate = st.number_input(
    'MonthlyRate',
    min_value=2094,
    max_value=26999,
    value=14235
)

NumCompaniesWorked = st.number_input(
    'NumCompaniesWorked',
    min_value=0,
    max_value=9,
    value=2
)

PercentSalaryHike = st.number_input(
    'PercentSalaryHike',
    min_value=11,
    max_value=25,
    value=14
)

PerformanceRating = st.number_input(
    'PerformanceRating',
    min_value=3,
    max_value=4,
    value=3
)

RelationshipSatisfaction = st.number_input(
    'RelationshipSatisfaction',
    min_value=1,
    max_value=4,
    value=3
)

StockOptionLevel = st.number_input(
    'StockOptionLevel',
    min_value=0,
    max_value=3,
    value=1
)

TotalWorkingYears = st.number_input(
    'TotalWorkingYears',
    min_value=0,
    max_value=40,
    value=10
)

TrainingTimesLastYear = st.number_input(
    'TrainingTimesLastYear',
    min_value=0,
    max_value=6,
    value=3
)

WorkLifeBalance = st.number_input(
    'WorkLifeBalance',
    min_value=1,
    max_value=4,
    value=3
)

YearsAtCompany = st.number_input(
    'YearsAtCompany',
    min_value=0,
    max_value=40,
    value=5
)

YearsInCurrentRole = st.number_input(
    'YearsInCurrentRole',
    min_value=0,
    max_value=18,
    value=3
)

YearsSinceLastPromotion = st.number_input(
    'YearsSinceLastPromotion',
    min_value=0,
    max_value=15,
    value=1
)

YearsWithCurrManager = st.number_input(
    'YearsWithCurrManager',
    min_value=0,
    max_value=17,
    value=3
)

# =========================
# CATEGORICAL INPUTS
# =========================

OverTime = st.selectbox('OverTime', ('No', 'Yes'))

Gender = st.selectbox('Gender', ('Female', 'Male'))

Department = st.selectbox(
    'Department',
    (
        'Sales',
        'Research & Development',
        'Human Resources'
    )
)

BusinessTravel = st.selectbox(
    'BusinessTravel',
    (
        'Non-Travel',
        'Travel_Rarely',
        'Travel_Frequently'
    )
)

JobRole = st.selectbox(
    'JobRole',
    (
        'Sales Executive',
        'Research Scientist',
        'Laboratory Technician',
        'Manufacturing Director',
        'Healthcare Representative',
        'Manager',
        'Sales Representative',
        'Research Director',
        'Human Resources'
    )
)

EducationField = st.selectbox(
    'EducationField',
    (
        'Human Resources',
        'Life Sciences',
        'Marketing',
        'Medical',
        'Other',
        'Technical Degree'
    )
)

MaritalStatus = st.selectbox(
    'MaritalStatus',
    (
        'Divorced',
        'Married',
        'Single'
    )
)

# =========================
# ENCODING
# =========================

Over_Time = 1 if OverTime == 'Yes' else 0

Gender_Female = 1 if Gender == 'Female' else 0
Gender_Male = 1 if Gender == 'Male' else 0

Department_dict = {
    'Sales': 0,
    'Research & Development': 1,
    'Human Resources': 2
}

Department_Code = Department_dict[Department]

BusinessTravel_dict = {
    'Non-Travel': 0,
    'Travel_Rarely': 1,
    'Travel_Frequently': 2
}

BusinessTravel_Code = BusinessTravel_dict[BusinessTravel]

JobRole_dict = {
    'Sales Executive': 0,
    'Research Scientist': 1,
    'Laboratory Technician': 2,
    'Manufacturing Director': 3,
    'Healthcare Representative': 4,
    'Manager': 5,
    'Sales Representative': 6,
    'Research Director': 7,
    'Human Resources': 8
}

JobRole_Code = JobRole_dict[JobRole]

# =========================
# ONE HOT ENCODING
# =========================

EducationField_HR = 1 if EducationField == 'Human Resources' else 0
EducationField_LS = 1 if EducationField == 'Life Sciences' else 0
EducationField_MKT = 1 if EducationField == 'Marketing' else 0
EducationField_MED = 1 if EducationField == 'Medical' else 0
EducationField_OTH = 1 if EducationField == 'Other' else 0
EducationField_TD = 1 if EducationField == 'Technical Degree' else 0

MaritalStatus_Divorced = 1 if MaritalStatus == 'Divorced' else 0
MaritalStatus_Married = 1 if MaritalStatus == 'Married' else 0
MaritalStatus_Single = 1 if MaritalStatus == 'Single' else 0

# =========================
# DATAFRAME
# =========================

input_features = pd.DataFrame({

    'Age': [Age],
    'DailyRate': [DailyRate],
    'DistanceFromHome': [DistanceFromHome],
    'Education': [Education],
    'EmployeeNumber': [EmployeeNumber],
    'EnvironmentSatisfaction': [EnvironmentSatisfaction],
    'HourlyRate': [HourlyRate],
    'JobInvolvement': [JobInvolvement],
    'JobLevel': [JobLevel],
    'JobSatisfaction': [JobSatisfaction],
    'MonthlyIncome': [MonthlyIncome],
    'MonthlyRate': [MonthlyRate],
    'NumCompaniesWorked': [NumCompaniesWorked],
    'PercentSalaryHike': [PercentSalaryHike],
    'PerformanceRating': [PerformanceRating],
    'RelationshipSatisfaction': [RelationshipSatisfaction],
    'StockOptionLevel': [StockOptionLevel],
    'TotalWorkingYears': [TotalWorkingYears],
    'TrainingTimesLastYear': [TrainingTimesLastYear],
    'WorkLifeBalance': [WorkLifeBalance],
    'YearsAtCompany': [YearsAtCompany],
    'YearsInCurrentRole': [YearsInCurrentRole],
    'YearsSinceLastPromotion': [YearsSinceLastPromotion],
    'YearsWithCurrManager': [YearsWithCurrManager],
    'Over_Time': [Over_Time],
    'Gender_Female': [Gender_Female],
    'Gender_Male': [Gender_Male],
    'Department_Code': [Department_Code],
    'BusinessTravel_Code': [BusinessTravel_Code],
    'JobRole_Code': [JobRole_Code],

    'EducationField_Human Resources': [EducationField_HR],
    'EducationField_Life Sciences': [EducationField_LS],
    'EducationField_Marketing': [EducationField_MKT],
    'EducationField_Medical': [EducationField_MED],
    'EducationField_Other': [EducationField_OTH],
    'EducationField_Technical Degree': [EducationField_TD],

    'MaritalStatus_Divorced': [MaritalStatus_Divorced],
    'MaritalStatus_Married': [MaritalStatus_Married],
    'MaritalStatus_Single': [MaritalStatus_Single]
})

# =========================
# PREDICTION
# =========================

if st.button('Predict'):

    prediction = model.predict(input_features)[0]

    prediction_proba = model.predict_proba(input_features)[0][1]

    st.subheader("Prediction Probability")

    st.progress(int(prediction_proba * 100))

    st.write(
        f"Attrition Probability: {prediction_proba * 100:.2f}%"
    )

    if prediction == 1:
        st.error(
            f'⚠️ High risk of Attrition ({prediction_proba*100:.2f}%)'
        )
    else:
        st.success(
            f'😊 Low risk of Attrition ({(1-prediction_proba)*100:.2f}%)'
        )

    # DEBUG VIEW
    with st.expander("View Input Features"):
        st.write(input_features)
