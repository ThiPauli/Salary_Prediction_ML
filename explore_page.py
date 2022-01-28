import pandas as pd
import streamlit as st
import plotly.express as px

@st.cache #to store the df once loaded.
def load_df(file_name):
    df = pd.read_csv(file_name)
    return df

df = load_df(file_name='data_cleaned.csv')

def show_explore_page():
    st.title(':bar_chart: Data Exploration from Stack Overflow: Annual Developer Survey 2021')
    st.subheader('An Overview of the developers who participated in this survey:')

    # Graph 1: frequency of participants by country
    frequency_country = df['Country'].value_counts().reset_index()
    frequency_country.rename(columns={'index': 'Country', 'Country': 'Number of Participants'}, inplace=True)

    fig_freq_country = px.bar(frequency_country, x='Country', y='Number of Participants', color='Country')

    fig_freq_country.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis_title=None,
        yaxis_title=None,
        yaxis=(dict(showgrid=False)),
        showlegend=False,
        title='<b>Number of Participants by Country</b>'
    )

    st.plotly_chart(fig_freq_country, use_container_width=True)

    # Graph 2: frequency of participants by job
    frequency_job = df['DevType'].value_counts().reset_index()
    frequency_job.rename(columns={'index': 'Job Title', 'DevType': 'Number of Participants'}, inplace=True)

    fig_freq_job = px.bar(frequency_job, x='Job Title', y='Number of Participants', color='Job Title')

    fig_freq_job.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis_title=None,
        yaxis_title=None,
        yaxis=(dict(showgrid=False)),
        showlegend=False,
        title='<b>Number of Participants by Job</b>'
    )
    
    st.plotly_chart(fig_freq_job, use_container_width=True)

    #adding a markdown to separate.
    st.markdown('---')

    # Graph 3: Mean Salary by Country
    salary_country = df.groupby('Country')['AnualSalary'].mean().reset_index().sort_values(by='AnualSalary', ascending=False)

    fig_salary_country = px.bar(
        salary_country,
        x = 'AnualSalary', 
        y = 'Country',
        title = '<b>Mean Annual Salary in US$ by Country</b>',
        color = 'Country',
        template = 'plotly_white'
    )

    fig_salary_country.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis_title='Mean Annual Salary',
        yaxis_title=None,
        xaxis=(dict(showgrid=False)),
        showlegend=False
    )

    st.plotly_chart(fig_salary_country, use_container_width=True)

    # Graph 4: Mean Salary by Job
    salary_job = df.groupby('DevType')['AnualSalary'].mean().reset_index().sort_values(by='AnualSalary', ascending=False)

    fig_salary_job = px.bar(
        salary_job,
        x = 'AnualSalary', 
        y = 'DevType',
        title = '<b>Mean Annual Salary in US$ by Job</b>',
        color = 'DevType',
        template = 'plotly_white'
    )

    fig_salary_job.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis_title='Mean Annual Salary',
        yaxis_title=None,
        xaxis=(dict(showgrid=False)),
        showlegend=False
    )

    st.plotly_chart(fig_salary_job, use_container_width=True)

    #adding a markdown to separate.
    st.markdown('---')

    # Graph 5: Education level percentage
    percentage_edlevel = df['EdLevel'].value_counts(normalize=True)

    fig_percentage_edlevel = px.pie(df, values=percentage_edlevel.values, names=percentage_edlevel.index, title='<b>Percentage of Participants by Education Level</b>')

    #st.plotly_chart(fig_percentage_edlevel, use_container_width=True)

    # Graph 6: Mean Annual Salary by Experience

    year_exp_mean = df.groupby('YearsExperience')['AnualSalary'].mean()

    fig_year_exp_mean = px.line(df, x=year_exp_mean.index, y=year_exp_mean.values, title='<b>Mean Annual Salary by Experience</b>')

    fig_year_exp_mean.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis_title='Years of Experience',
        yaxis_title='Annual Salary US$',
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False)
    )

    #Ploting graph 5 and 6 side by side
    left_column, right_column = st.columns(2)
    left_column.plotly_chart(fig_percentage_edlevel, use_container_width=True)
    right_column.plotly_chart(fig_year_exp_mean, use_container_width=True)