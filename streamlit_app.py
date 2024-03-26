import streamlit as st
import numpy as np
import pandas as pd
import altair as alt


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



# Display DataFrame

#df_editor = st.data_editor(df, height=212, use_container_width=True,
                            # column_config={"year": st.column_config.TextColumn("Year")},
                            #num_rows="dynamic")
# df_chart = pd.melt(df_editor.reset_index(), id_vars='year', var_name='genre', value_name='gross')

#Dispaly as Bar Chart

# Calculate total percentage for selected skills
if skills_selection:
    total_percentage = calculate_total_percentage(skills_selection)
    
    # Create DataFrame for visualization
    data = {'Skill': ['Total'], 'Percentage': [total_percentage]}
    chart_df = pd.DataFrame(data)
    #print(chart_df)
    # Display chart
    st.write(f"The total percentage of {'+'.join(skills_selection)} is: {total_percentage:.2f}% out of 100%")
    
    # Create horizontal bar chart
    chart = alt.Chart(chart_df).mark_bar().encode(
        y=alt.Y('Skill', title='Skill'),
        x=alt.X('Percentage', title='Percentage', axis=alt.Axis(format='%')),
        color=alt.value('blue')  # Color of the bar
    ).properties(
        width=600,
        title='Skill Percentage'
    )
    
    # Display chart
    st.altair_chart(chart, use_container_width=True)