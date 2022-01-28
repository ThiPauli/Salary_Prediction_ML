import pandas as pd
import numpy as np
import pickle # to load the ML model
import streamlit as st
import plotly.express as px

# main page

@st.cache #to store the df once loaded.
def load_df(file_name):
    df = pd.read_csv(file_name)
    return df

df = load_df(file_name='data_cleaned.csv')

@st.cache
def load_model(file_name):
    with open(file_name , 'rb') as file:
        data = pickle.load(file)

    return data

data = load_model(file_name='preprocessor&model.pkl')

regressor_model = data['model']
preprocessor = data['column_transormer']

def show_predict_page():
    # ---- main page -----
    st.title(':money_with_wings: Salary Estimator')
    st.header('Salary Prediction based on the Survey Data from StackOverflow 2021')


    #defining the variables which users can choose: Country, Job and Education Level
    countries = (
        'United States of America',
        'India',
        'Germany',
        'United Kingdom of Great Britain and Northern Ireland',
        'Canada',
        'France',
        'Brazil',
        'Spain',
        'Netherlands',
        'Australia',
        'Poland',
        'Italy',
        'Russian Federation',
        'Sweden',
        'Turkey',
        'Switzerland',
        'Israel',
        'Norway'
    )

    jobs = (
        'Developer, full-stack',
        'Developer, front-end',
        'Developer, back-end',
        'Developer, mobile',
        'Developer, desktop or enterprise applications',
        'Engineer, data',
        'Data scientist or machine learning specialist',
        'Developer, embedded applications or devices',
        'Academic researcher',
        'DevOps specialist',
        'Engineering manager',
        'Developer, QA or test',
        'Data or business analyst'
    )

    education = (
        'Less than a Bachelor’s',
        'Bachelor’s degree',
        'Master’s degree',
        'Postgraduate',
    )

    #creating the select box for each variable

    # ---- Country -----
    countries = sorted(countries)
    country_select = st.selectbox('Choose a Country', countries)

    # ---- Job -----
    job_select = st.selectbox('Choose a Job Title', jobs)

    # ---- Education -----
    education_select = st.selectbox('Choose an Education Level', education)

    # ---- Years of Experience -----
    experience = st.slider('Years of Experience', 0, 30, 5)

    #define a button to calculate the salary
    run = st.button('Calculate Salary')

    #attributing the fields selected for the user to feed the model and predict the salary
    if run:
        data = np.array([[country_select, education_select, experience, job_select]])
        
        df_inputs = pd.DataFrame(data, columns=['Country', 'EdLevel', 'YearsExperience', 'DevType'])
        df_inputs['YearsExperience'] = pd.to_numeric(df_inputs['YearsExperience'], downcast='float')

        #passing through the model
        df_inputs_transformed = preprocessor.transform(df_inputs)
        salary_predicted = regressor_model.predict(df_inputs_transformed)
        st.write(f'### The estimated annual salary is US$ {salary_predicted[0]:,.2f}')

        # plotting the graphs and info related with the user's inputs
        df_filtered = df[(df['Country'] == country_select) & (df['DevType'] == job_select) & (df['EdLevel'] == education_select)].describe()

        st.markdown('---')

        st.write('#### Overview based on:')
        st.write(f'''
            * **Country**: {country_select}
            * **Job**: {job_select}
            * **Education Level**: {education_select}'''
        )

        st.write(f"""
            | Number of Participants | Min | Max | Mean | Range Years of Experience |
            | ----------- | ----------- | ---------- | ---------- | ---------- |
            | {df_filtered['AnualSalary']['count']:.0f} | US$ {df_filtered['AnualSalary']['min']:,.2f} | US$ {df_filtered['AnualSalary']['max']:,.2f} | US$ {df_filtered['AnualSalary']['mean']:,.2f} | {df_filtered['YearsExperience']['min']:.3g} - {df_filtered['YearsExperience']['max']:.0f} |
            """
        )

        # since there are specific cases which it does not have sufficient samples of data.
        if df_filtered['AnualSalary']['count'] <= 5:
            st.markdown('###')
            st.write('##### Warning: This estimation may not be appropriate due to the lack of data.')

        st.markdown('---')

        st.write(f'#### Statistics regarding {country_select}:')

        # graph 1: Mean Annual Salary in US$ by Job and Education Level
        df_filtered_country = df[df['Country'] == country_select]
        df_group = df_filtered_country.groupby(['DevType', 'EdLevel'])['AnualSalary'].mean().reset_index()
        df_group.rename(columns={'AnualSalary': 'Mean Annual Salary', 'EdLevel': 'Education Level', 'DevType': 'Job Title'}, inplace=True)

        fig1 = px.bar(df_group, x='Job Title', y='Mean Annual Salary',
                    color='Education Level',
                    title = f'<b>Mean Annual Salary in {country_select} by Job and Education Level</b>',
                    template = 'plotly_white')

        fig1.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis_title=None,
            yaxis_title=None,
            yaxis=dict(showgrid=False, tickformat=",.2f")
        )

        st.plotly_chart(fig1, use_container_width=True)

        # graph 2: Number of Participants by Job and Education Level
        number_contribution = df_filtered_country.groupby(['DevType', 'EdLevel'])['YearsExperience'].count().reset_index()
        number_contribution.rename(columns={'YearsExperience': 'Number of Participants', 'EdLevel': 'Education Level', 'DevType': 'Job Title'}, inplace=True)

        fig2 = px.bar(number_contribution, x='Job Title', y='Number of Participants',
                    color='Education Level',
                    title = f'<b>Number of Participants from {country_select} by Job and Education Level</b>',
                    template = 'plotly_white')

        fig2.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis_title=None,
            yaxis_title=None,
            yaxis=dict(showgrid=False)
        )
        
        st.plotly_chart(fig2, use_container_width=True)
