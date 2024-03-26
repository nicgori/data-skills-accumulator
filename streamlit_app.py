import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt

# Page title
st.set_page_config(page_title='Data Skillset Accumulator', page_icon='📊')
st.title('📊 Data Skillset Accumulator')

st.subheader('Find out what percentage of data anaylst job offers you can cover with your skillset!')

# Load data
df = pd.read_csv('data/skills_occurences_income.csv')
# df.year = df.year.astype('int')


# Function to calculate percentage
def calculate_percentage(skill_input):
    total_occurrences = df['count_occurrences'].sum()
    skill_occurrences = df.loc[df['skill'] == skill_input, 'count_occurrences'].iloc[0]
    skill_percentage = (skill_occurrences / total_occurrences) * 100
    return skill_percentage

# Function to calculate total percentage for multiple skills
def calculate_total_percentage(skills_input):
    total_percentage = 0
    for skill in skills_input:
        total_percentage += calculate_percentage(skill)
    return total_percentage

# Input widgets
## Genres selection
skills_list = df.skill.unique()
skills_selection = st.multiselect('Select skills', skills_list, ['python'])

# Calculate and display total percentage for selected skills
if skills_selection:
    total_percentage = calculate_total_percentage(skills_selection)
    st.write(f"The total percentage of selected skills is: {total_percentage:.2f}%")
# Calculate and display remainig percentage for selected skills
if skills_selection:
    remaining_percentage = 100 - total_percentage
    st.write(f"The total percentage of remaining skills is: {remaining_percentage:.2f}%")
    
  # Create DataFrame for visualization
    data = {
        'Type': ['Selected Skills','Skills Still to Learn',] * len(skills_selection),
        'Percentage': [total_percentage,remaining_percentage] * len(skills_selection),
        'Skill': skills_selection * 2
    }
    chart_df = pd.DataFrame(data)

