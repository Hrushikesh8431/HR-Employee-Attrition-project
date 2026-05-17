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
# NUMERICAL INPUTS
# =========================

Age = st.number_input('Age', 18, 60, 36)

DailyRate = st.number_input('DailyRate', 102, 1499, 802)

DistanceFromHome = st.number_input('DistanceFromHome', 1, 29, 7)

Education = st.number_input('Education', 1, 5, 3)

EmployeeNumber = st.number_input('EmployeeNumber', 1, 2068, 1020)

EnvironmentSatisfaction = st.number_input(
    'EnvironmentSatisfaction',
    1,
    4,
    3
)

HourlyRate = st.number_input('HourlyRate', 30, 100, 66)

JobInvolvement = st.number_input('JobInvolvement', 1, 4, 3)

JobLevel = st.number_input('JobLevel', 1, 5, 2)

JobSatisfaction = st.number_input('JobSatisfaction', 1, 4, 3)

MonthlyIncome = st.number_input(
    'MonthlyIncome',
    1009,
    19999,
    4919
)

MonthlyRate = st.number_input(
    'MonthlyRate',
    2094,
    26999,
    14235
)

NumCompaniesWorked = st.number_input(
    'NumCompaniesWorked',
    0,
    9,
    2
)

PercentSalaryHike = st.number_input(
    'PercentSalaryHike',
    11,
    25,
    14
)

PerformanceRating = st.number_input(
    'PerformanceRating',
    3,
    4,
    3
)

RelationshipSatisfaction = st.number_input(
    'RelationshipSatisfaction',
    1,
    4,
    3
)

StockOptionLevel = st.number_input(
    'StockOptionLevel',
    0,
    3,
    1
)

TotalWorkingYears = st.number_input(
    'TotalWorkingYears',
    0,
    40,
    10
)

TrainingTimesLastYear = st.number_input(
    'TrainingTimesLastYear',
    0,
    6,
    3
)

WorkLifeBalance = st.number_input(
    'WorkLifeBalance',
    1,
    4,
    3
)

YearsAtCompany = st.number_input(
    'YearsAtCompany',
    0,
    40,
    5
)

YearsInCurrentRole = st.number_input(
    'YearsInCurrentRole',
    0,
    18,
    3
)

YearsSinceLastPromotion = st.number_input(
    'YearsSinceLastPromotion',
    0,
    15,
    1
)

YearsWithCurrManager = st.number_input(
    'YearsWithCurrManager',
    0,
    17,
    3
)

# =========================
# CATEGORICAL INPUTS
# =========================

OverTime = st.selectbox('OverTime', ['No', 'Yes'])

Gender = st.selectbox('Gender', ['Female', 'Male'])

Department = st.selectbox(
    'Department',
    [
        'Sales',
        'Research & Development',
        'Human Resources'
    ]
)

BusinessTravel = st.selectbox(
    'BusinessTravel',
    [
        'Non-Travel',
        'Travel_Rarely',
        'Travel_Frequently'
    ]
)

JobRole = st.selectbox(
    'JobRole',
    [
        'Sales Executive',
        'Research Scientist',
        'Laboratory Technician',
        'Manufacturing Director',
        'Healthcare Representative',
        'Manager',
        'Sales Representative',
        'Research Director',
        'Human Resources'
    ]
)

EducationField = st.selectbox(
    'EducationField',
    [
        'Human Resources',
        'Life Sciences',
        'Marketing',
        'Medical',
        'Other',
        'Technical Degree'
    ]
)

MaritalStatus = st.selectbox(
    'MaritalStatus',
    [
        'Divorced',
        'Married',
        'Single'
    ]
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
# CREATE DATAFRAME
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

    # Match exact training columns
    model_features = model.feature_names_in_

    input_features = input_features.reindex(
        columns=model_features,
        fill_value=0
    )

    # Prediction
    prediction = model.predict(input_features)[0]

    # Probability
    prediction_proba = model.predict_proba(
        input_features
    )[0][1]

    # Progress Bar
    st.subheader("Prediction Probability")

    st.progress(int(prediction_proba * 100))

    st.write(
        f"Attrition Probability: "
        f"{prediction_proba * 100:.2f}%"
    )

    # Final Output
    if prediction == 1:
        st.error(
            f'⚠️ High risk of Attrition '
            f'({prediction_proba*100:.2f}%)'
        )
    else:
        st.success(
            f'😊 Low risk of Attrition '
            f'({(1-prediction_proba)*100:.2f}%)'
        )

    # Show input data
    with st.expander("View Input Features"):
        st.write(input_features)
