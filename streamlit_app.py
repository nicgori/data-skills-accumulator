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
skills_selection = st.multiselect('Select skills', skills_list, ['python','sql'])

# Calculate and display total percentage for selected skills
if skills_selection:
    total_percentage = calculate_total_percentage(skills_selection)
    st.write(f"The total percentage of selected skills is: {total_percentage:.2f}%")
# Calculate and display remainig percentage for selected skills
if skills_selection:
    remaining_percentage = 100 - total_percentage
    st.write(f"The total percentage of remaining skills is: {remaining_percentage:.2f}%")
    
# # Create DataFrame for visualization

# data = {
#      'Skills': ['Selected Skills', 'Skills Still to Learn'],
#      'Percentage': [total_percentage, remaining_percentage]
#  }
# chart_df = pd.DataFrame(data)
# # Create stacked column bar chart with Altair'

# data = {
#       'Skills': ['Selected Skills', 'Skills Still to Learn'],
#       'Percentage': [total_percentage, 100 - total_percentage]
#   }
# chart_df = pd.DataFrame(data)
# # Create stacked column bar chart with Altair'

#print(chart_df)


# # Create stacked column bar chart with Altair
# bar_chart = alt.Chart(chart_df).mark_bar().encode(
#     x=alt.X('Skills:N', axis=alt.Axis(title=None)),
#     y=alt.Y('Percentage:Q', axis=alt.Axis(title='Percentage')),
#     color=alt.Color('Skills:N', scale=alt.Scale(range=['#1f77b4', '#ff7f0e']), legend=None),
# )

# # Display chart
# st.altair_chart(bar_chart, use_container_width=True)

# Create DataFrame for visualization
# 
# Create DataFrame for visualization
# data = {
#     'Skills': ['Selected Skills', 'Remaining Skills'],
#     'Percentage': [total_percentage, 100 - total_percentage]
# }
# chart_df = pd.DataFrame(data)

# # Create stacked column bar chart with Altair
# bar_chart = alt.Chart(chart_df).mark_bar().encode(
#     x=alt.X('Skills:N', axis=alt.Axis(title=None)),
#     y=alt.Y('Percentage:Q', axis=alt.Axis(title='Percentage')),
#     color=alt.Color('Skills:N', scale=alt.Scale(range=['#1f77b4', '#ff7f0e']), legend=None),
# )

# # Display chart
# st.altair_chart(bar_chart, use_container_width=True)
#
#Create variable 100 %

# total_percentage = 50  # Example value for total_percentage
# index = ["Skillset"]
# df = pd.DataFrame({"Selected Skills": [total_percentage], "Skills Still to Learn": [100]}, index=index)
# st.pyplot(df.plot.barh(stacked=True).figure)