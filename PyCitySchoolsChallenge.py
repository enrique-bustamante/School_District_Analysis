#!/usr/bin/env python
# coding: utf-8

# In[135]:


# Add the Pandas dependency.
import pandas as pd
import numpy as np
import os


# In[136]:


# Create variables for the datasheets we are importing
school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"


# In[137]:


# Read the datasheets into a pandas dataframe
school_data_df = pd.read_csv(school_data_to_load)
student_data_df = pd.read_csv(student_data_to_load)


# In[138]:


# Add each prefix and suffix to remove to a list.
prefixes_suffixes = ["Dr. ", "Mr. ","Ms. ", "Mrs. ", "Miss ", " MD", " DDS", " DVM", " PhD"]


# In[139]:


taylor_ninth = student_data_df[(student_data_df["grade"] == "9th") & (student_data_df["school_name"] == "Thomas High School")]
taylor_ninth["math_score"].mean()

#%%
taylor_ninth["reading_score"].mean()

# In[140]:


# Remove the prefixes and suffixes from the data
for word in prefixes_suffixes:
    student_data_df["student_name"] = student_data_df["student_name"].str.replace(word, "")


# In[141]:


# Replace math and reading scores for 9th graders from Thomas HS using loc and np.nan
student_data_df.loc[(student_data_df['school_name'] == "Thomas High School") & (student_data_df['grade'] == "9th"),'reading_score'] = np.nan
student_data_df.loc[(student_data_df['school_name'] == "Thomas High School") & (student_data_df['grade'] == "9th"),'math_score'] = np.nan


# In[142]:


# Display the last 10 entries to see if the changes took place.
student_data_df.tail(10)


# In[143]:


# Merge the two data frames into one using a common column of data
school_data_complete_df = pd.merge(student_data_df, school_data_df, on = ["school_name", "school_name"])


# In[144]:


# Calculate the total student count for the district combined
student_count = school_data_complete_df["student_name"].count()
student_count


# In[145]:


# Calculate the total school count in the district
school_count = len(school_data_complete_df["school_name"].unique())
school_count


# In[146]:


# Calculate the total budget for the district combined
total_budget = school_data_df["budget"].sum()


# In[147]:


# Calculate the average reading score for the district combined
average_reading_score = school_data_complete_df["reading_score"].mean()
average_reading_score


# In[148]:


# Calculate the average math score for the district combined
average_math_score = school_data_complete_df["math_score"].mean()
average_math_score


# In[149]:


# Create the lists we will use to count the number of students who passed in their respective subject for schools combined
passing_math = school_data_complete_df[school_data_complete_df["math_score"] >= 70]
passing_reading = school_data_complete_df[school_data_complete_df["reading_score"] >= 70]
passing_math_count = passing_math["student_name"].count()
passing_reading_count = passing_reading["student_name"].count()


# In[150]:


# Calcuate the average of studentws who pass in the respective subject for schools combined
passing_percentage_math = passing_math_count / float(student_count) * 100
passing_percentage_reading = passing_reading_count / float(student_count) * 100


# In[151]:


# Print out the averages for math and reading for the entire district.
print(passing_percentage_math)
print(passing_percentage_reading)


# In[152]:


# Create the list of students who passed both subjects for all schools combined
passing_math_reading = school_data_complete_df[(school_data_complete_df["math_score"] >= 70) & (school_data_complete_df["reading_score"] >= 70)]
passing_math_reading


# In[153]:


# Create the count and use it to find the pass percentage for all schools combined
passing_math_reading_count = passing_math_reading["student_name"].count()
passing_math_reading_percentage = passing_math_reading_count / float(student_count) * 100
print(passing_math_reading_percentage)


# In[154]:


# Create a dataframe made from the values we calculated for the combined district
district_summary_df = pd.DataFrame([{
    "Total Schools": school_count, 
    "Total Students": student_count,
    "Total Budget": total_budget, 
    "Average Math Score": average_math_score, 
    "Average Reading Score": average_reading_score, 
    "% Passing Math": passing_percentage_math, 
    "% Passing Reading": passing_percentage_reading, 
    "% Overall Passing": passing_math_reading_percentage
}])


# In[155]:


# Format the cells to look better and more uniform
district_summary_df["Total Students"] = district_summary_df["Total Students"].map("{:,}".format)
district_summary_df["Total Budget"] = district_summary_df["Total Budget"].map("${:,.2f}".format)
district_summary_df["Average Math Score"] = district_summary_df["Average Math Score"].map("{:.1f}".format)
district_summary_df["Average Reading Score"] = district_summary_df["Average Reading Score"].map("{:.1f}".format)
district_summary_df["% Passing Math"] = district_summary_df["% Passing Math"].map("{:.0f}".format)
district_summary_df["% Passing Reading"] = district_summary_df["% Passing Reading"].map("{:.0f}".format)
district_summary_df["% Overall Passing"] = district_summary_df["% Overall Passing"].map("{:.0f}".format)


# In[156]:


# Display the district summary to see formatting changes
district_summary_df


# In[157]:


# create a school dataframe and set school name as the index
per_school_type = school_data_df.set_index(["school_name"])["type"]
per_school_type


# In[158]:


# Create a df to show how the school name can be used as the index. This is just an example and not part of the code.
df = pd.DataFrame(per_school_type)
df


# In[159]:


# set up the per school student counts 
per_school_counts = school_data_df.set_index(["school_name"])["size"]
per_school_counts


# In[160]:


# Set up the per school counts using the value_counts() method
per_school_counts = school_data_complete_df["school_name"].value_counts()
per_school_counts


# In[161]:


# Set up the per school budget
per_school_budget = school_data_df.set_index(["school_name"])["budget"]
per_school_budget


# In[162]:


# Calculate the budget spent per student by school
per_school_capita = per_school_budget / per_school_counts
per_school_capita


# In[163]:


# Calculate the average score per school
per_school_math_averages = school_data_complete_df.groupby("school_name")["math_score"].mean()
per_school_math_averages
per_school_read_averages = school_data_complete_df.groupby("school_name")["reading_score"].mean()
per_school_read_averages


# In[164]:


# Create a filter that makes a lists and counts of the students that passed the subjects
per_school_passing_math = school_data_complete_df[(school_data_complete_df["math_score"] >= 70)]
per_school_passing_math
per_school_passing_reading = school_data_complete_df[(school_data_complete_df["reading_score"] >= 70)]
per_school_passing_reading
per_school_passing_math = per_school_passing_math.groupby(["school_name"]).count()["student_name"]
per_school_passing_reading = per_school_passing_reading.groupby(["school_name"]).count()["student_name"]
per_school_passing_reading


# In[165]:


# Calculate the pass percentage per school
per_school_passing_math = per_school_passing_math / per_school_counts * 100
per_school_passing_reading = per_school_passing_reading / per_school_counts * 100


# In[166]:


# create lists and calculate the pass rate for those who passed both subjects by school
per_passing_math_reading = school_data_complete_df[(school_data_complete_df["math_score"] >= 70) & (school_data_complete_df["reading_score"] >= 70)]
per_passing_math_reading = per_passing_math_reading.groupby(["school_name"]).count()["student_name"]
per_passing_math_reading = per_passing_math_reading / per_school_counts * 100
per_passing_math_reading


# In[167]:


# Combine the dataframes to make one large dataframe by school
per_school_summary_df = pd.DataFrame({
    "School Type": per_school_type, 
    "Total Students": per_school_counts, 
    "Total School Budget": per_school_budget,
    "Per Student Budget": per_school_capita,
    "Average Math Score": per_school_math_averages,
    "Average Reading Score": per_school_read_averages,
    "% Passing Math": per_school_passing_math,
    "% Passing Reading": per_school_passing_reading,
    "% Overall Passing": per_passing_math_reading})
per_school_summary_df


# In[168]:


# Format the columns to be tidier
per_school_summary_df["Total School Budget"] = per_school_summary_df["Total School Budget"].map("${:,.2f}".format)
per_school_summary_df["Per Student Budget"] = per_school_summary_df["Per Student Budget"].map("${:,.2f}".format)
per_school_summary_df


# In[169]:


# Shows the top schools based on Overall Passing percentage
top_schools = per_school_summary_df.sort_values(["% Overall Passing"], ascending=False)
top_schools.head(10)


# In[170]:


# Shows the lowest performing schools based on Overall Passing Percentage
bottom_schools = per_school_summary_df.sort_values(["% Overall Passing"], ascending=True)
bottom_schools.head()


# In[171]:


# Filter dataframes to include only specific grades
ninth_graders = school_data_complete_df[(school_data_complete_df['grade'] == "9th")]
tenth_graders = school_data_complete_df[(school_data_complete_df['grade'] == "10th")]
eleventh_graders = school_data_complete_df[(school_data_complete_df['grade'] == "11th")]
twelfth_graders = school_data_complete_df[(school_data_complete_df['grade'] == "12th")]


# In[172]:


# Calculate the math score average for each grade
ninth_grade_math_scores = ninth_graders.groupby(['school_name']).mean()['math_score']
tenth_grade_math_scores = tenth_graders.groupby(['school_name']).mean()['math_score']
eleventh_grade_math_scores = eleventh_graders.groupby(['school_name']).mean()['math_score']
twelfth_grade_math_scores = twelfth_graders.groupby(['school_name']).mean()['math_score']


# In[173]:


# Calculate the reading score average for each grade
ninth_grade_reading_scores = ninth_graders.groupby(['school_name']).mean()['reading_score']
tenth_grade_reading_scores = tenth_graders.groupby(['school_name']).mean()['reading_score']
eleventh_grade_reading_scores = eleventh_graders.groupby(['school_name']).mean()['reading_score']
twelfth_grade_reading_scores = twelfth_graders.groupby(['school_name']).mean()['reading_score']


# In[174]:


twelfth_grade_reading_scores


# In[175]:


# Create dataframe for all math score averages by school by grade
math_scores_by_grade = pd.DataFrame({
    "9th": ninth_grade_math_scores, 
    "10th": tenth_grade_math_scores, 
    "11th": eleventh_grade_math_scores, 
    "12th": twelfth_grade_math_scores
})


# In[176]:


# Create dataframe for all reading score averages by school by grade
reading_scores_by_grade = pd.DataFrame({"9th": ninth_grade_reading_scores, 
                                        "10th": tenth_grade_reading_scores, 
                                        "11th": eleventh_grade_reading_scores, 
                                        "12th": twelfth_grade_reading_scores
                                       })


# In[177]:


# Format the math scores by grade data frame
math_scores_by_grade["9th"] = math_scores_by_grade["9th"].map("{:.1f}".format)
math_scores_by_grade["10th"] = math_scores_by_grade["10th"].map("{:.1f}".format)
math_scores_by_grade["11th"] = math_scores_by_grade["11th"].map("{:.1f}".format)
math_scores_by_grade["12th"] = math_scores_by_grade["12th"].map("{:.1f}".format)


# In[178]:


# This code ensures the columns are in the correct order
math_scores_by_grade = math_scores_by_grade[
                 ["9th", "10th", "11th", "12th"]]


# In[179]:


# remove the index name
math_scores_by_grade.index.name = None
math_scores_by_grade.head()


# In[180]:


# reformat the reading scores by grade
reading_scores_by_grade["9th"] = reading_scores_by_grade["9th"].map("{:.1f}".format)
reading_scores_by_grade["10th"] = reading_scores_by_grade["10th"].map("{:.1f}".format)
reading_scores_by_grade["11th"] = reading_scores_by_grade["11th"].map("{:.1f}".format)
reading_scores_by_grade["12th"] = reading_scores_by_grade["12th"].map("{:.1f}".format)


# In[181]:


# ensure proper order of columns
reading_scores_by_grade = reading_scores_by_grade[["9th", "10th", "11th", "12th"]]


# In[182]:


# remove the index name
reading_scores_by_grade.index.name = None
reading_scores_by_grade.head()


# In[183]:


# see a statistical breakdown of the per capita dataframe
per_school_capita.describe()


# In[184]:


# set up spending bins to group schools by amount spent per student
spending_bins = [0, 585, 630, 645, 675]
per_school_capita.groupby(pd.cut(per_school_capita, spending_bins)).count()
group_names = ["<$584", "$585-629", "$630-644", "$645-675"]


# In[185]:


# This adds the bin range for each school
per_school_summary_df["Spending Ranges (Per Student)"] = pd.cut(per_school_capita, spending_bins, labels = group_names)


# In[186]:


per_school_summary_df


# In[187]:


# find the averages by spending bin
spending_math_scores = per_school_summary_df.groupby(["Spending Ranges (Per Student)"]).mean()["Average Math Score"]
spending_reading_scores = per_school_summary_df.groupby(["Spending Ranges (Per Student)"]).mean()["Average Reading Score"]
spending_passing_math = per_school_summary_df.groupby(["Spending Ranges (Per Student)"]).mean()["% Passing Math"]
spending_passing_reading = per_school_summary_df.groupby(["Spending Ranges (Per Student)"]).mean()["% Passing Reading"]
overall_passing_spending = per_school_summary_df.groupby(["Spending Ranges (Per Student)"]).mean()["% Overall Passing"]


# In[188]:


# Create a spending summary database using the smaller databases
spending_summary_df = pd.DataFrame({
    "Average Math Score": spending_math_scores,
    "Average Reading Score": spending_reading_scores,
    "% Passing Math": spending_passing_math,
    "% Passing Reading": spending_passing_reading,
    "% Overall Passing": overall_passing_spending
})


# In[189]:


# Format the values in the spending summary dataframe
spending_summary_df["Average Math Score"] = spending_summary_df["Average Math Score"].map("{:.1f}".format)
spending_summary_df["Average Reading Score"] = spending_summary_df["Average Reading Score"].map("{:.1f}".format)
spending_summary_df["% Passing Math"] = spending_summary_df["% Passing Math"].map("{:.0f}".format)
spending_summary_df["% Passing Reading"] = spending_summary_df["% Passing Reading"].map("{:.0f}".format)
spending_summary_df["% Overall Passing"] = spending_summary_df["% Overall Passing"].map("{:.0f}".format)


# In[190]:


spending_summary_df


# In[191]:


#establish the school size bins
size_bins = [0, 1000, 2000, 5000]
group_names_size = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]


# In[192]:


# add column that has the proper label based on student population
per_school_summary_df["School Size"] = pd.cut(per_school_summary_df["Total Students"],size_bins, labels=group_names_size)


# In[193]:


per_school_summary_df.head()


# In[194]:


# get the averages based on school size category
size_math_scores = per_school_summary_df.groupby(["School Size"]).mean()["Average Math Score"]
size_reading_scores = per_school_summary_df.groupby(["School Size"]).mean()["Average Reading Score"]
size_passing_math = per_school_summary_df.groupby(["School Size"]).mean()["% Passing Math"]
size_passing_reading = per_school_summary_df.groupby(["School Size"]).mean()["% Passing Reading"]
size_overall_passing = per_school_summary_df.groupby(["School Size"]).mean()["% Overall Passing"]


# In[195]:


# Create a dataframe for the size summary
size_summary_df = pd.DataFrame({
    "Average Math Score": size_math_scores, 
    "Average Reading Score": size_reading_scores, 
    "% Passing Math": size_passing_math, 
    "% Passing Reading": size_passing_reading, 
    "% Overall Passing": size_overall_passing
})


# In[196]:


# Format the size summary values
size_summary_df["Average Math Score"] = size_summary_df["Average Math Score"].map("{:.1f}".format)
size_summary_df["Average Reading Score"] = size_summary_df["Average Reading Score"].map("{:.1f}".format)
size_summary_df["% Passing Math"] = size_summary_df["% Passing Math"].map("{:.0f}".format)
size_summary_df["% Passing Reading"] = size_summary_df["% Passing Reading"].map("{:.0f}".format)
size_summary_df["% Overall Passing"] = size_summary_df["% Overall Passing"].map("{:.0f}".format)


# In[197]:


size_summary_df


# In[198]:


# Get the averages and passing rates based on type of school
type_math_scores = per_school_summary_df.groupby(["School Type"]).mean()["Average Math Score"]
type_reading_scores = per_school_summary_df.groupby(["School Type"]).mean()["Average Reading Score"]
type_passing_math = per_school_summary_df.groupby(["School Type"]).mean()["% Passing Math"]
type_passing_reading = per_school_summary_df.groupby(["School Type"]).mean()["% Passing Reading"]
type_overall_passing = per_school_summary_df.groupby(["School Type"]).mean()["% Overall Passing"]


# In[199]:


type_summary_df = pd.DataFrame({"Average Math Score": type_math_scores, "Average Reading Score": type_reading_scores, "% Passing Math": type_passing_math, "% Passing Reading": type_passing_reading, "% Overall Passing": type_overall_passing})


# In[200]:


# Format the values in the type summary dataframe
type_summary_df["Average Math Score"] = type_summary_df["Average Math Score"].map("{:.1f}".format)
type_summary_df["Average Reading Score"] = type_summary_df["Average Reading Score"].map("{:.1f}".format)
type_summary_df["% Passing Math"] = type_summary_df["% Passing Math"].map("{:.0f}".format)
type_summary_df["% Passing Reading"] = type_summary_df["% Passing Reading"].map("{:.0f}".format)
type_summary_df["% Overall Passing"] = type_summary_df["% Overall Passing"].map("{:.0f}".format)


# In[201]:


type_summary_df


# In[ ]:




