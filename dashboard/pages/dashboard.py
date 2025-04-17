import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.title("This is the Dashboard Page")

df = sns.load_dataset("titanic")
st.dataframe(df) # print dataset in dashboard

#gender filter
gender = st.sidebar.multiselect('Gender',
                                options = df['sex'].unique(),
                                default = df['sex'].unique())
# pclass filter
pclass = st.sidebar.multiselect('Passenger Class',
                                options = df['pclass'].unique(),
)

filtered_df = df[
       (df['sex'].isin(gender)) & #to cheack whether the gender filter has the data of 
       (df['pclass'].isin(pclass)) #to check whether the pclass filter has the data of

]

fig = px.sunburst(filtered_df, path=['pclass','sex','survived'],values='age',
            title='survival by class and gender', width=500, height=500,
            template='plotly_dark', color='age', color_continuous_scale='PiYG')
st.plotly_chart(fig)   # to display plotly chart in streamlit

fig = px.scatter(filtered_df, x='age', y='fare', color='survived',
           title='age vs fare by survival status',template='plotly_dark')
st.plotly_chart(fig)   

fig = px.treemap(df, path=['pclass','survived'], values='age',
           title='Survival by class', width=800, height=500,
           template='plotly_dark', color='age', color_continuous_scale='RdBu',)
st.plotly_chart(fig) 

fig = px.box(df, x='pclass', y='fare', color='pclass',
       title='Fare Distribution by Class', template='plotly_dark')
st.plotly_chart(fig)

fig = px.violin(df, x='sex', y='age', color='survived', box=True,
          title='Age Distribution by Gender and Survival', template='plotly_dark')
st.plotly_chart(fig)

survived_counts = filtered_df['survived'].value_counts()
fig = px.pie(names=survived_counts.index, values=survived_counts.values,
       title='Survival Rate', template='plotly_dark',
       width=500, height=500)
st.plotly_chart(fig)