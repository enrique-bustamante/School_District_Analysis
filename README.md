# School_District_Analysis
This analysis was conducted to compare the impact of removing the 9th grade class scores from Thomas High School.



### District Summary
How is the district summary affected?

When we removed the Thomas High School 9th grade class scores, we saw a slight decrease in the district math average dropping from 79.0 to 78.9. However, the reading average stayed relatively unchanged. This may be due to the fact that there are 39,170 students in the entire district and only 461 were removed, having minimal impact.

### School Summary

How is the school summary affected?

Looking at how it affected the school, we saw no noticeable change in math average. There was a nominal increase in the reading score, increasing from 83.8 to 83.9, with the 9th graders removed for Thomas High School. No other school data was impacted by the removal of the scores of this group.

### School Rankings

How does replacing the ninth graders’ math and reading scores affect Thomas High School’s performance, relative to the other schools?

While looking at the averages doesn't change the metrics too drastically, the pass percentage numbers are greatly affected due to the fact that these percentages are still counting these students in the student count, hence decreasing the pass percentage by a large amount. As a result, since we are ranking schools by the percentage of overall passing, Thomas High School dropped from 2nd to 8th.


### Scores by Grade

How did replacing the ninth graders' math and reading scores affect the scores by grade?
The math and reading scores were unaffected with the exception of the 9th grade class of Thomas High School. Since their values were all set to NaN, the class average value is nan.


### Scores by School Spending
How did replacing the ninth graders' math and reading scores affect the school spending summary?
Thomas High School fell within the 3rd Per Capita bracket ($630-644). While the math and reading averages were unaffected, we saw an impact to the percentage of students passing for math, reading, and overall. The decreases were from 73 to 67, 84 to 77, and 63 to 56 percent, respectively. This is, again, indicative of the fact that there are 461 no values being counted in these three metrics, which do impact the percentage in an incorrect fashion for this spending range. There was no impact to the other spending ranges.


### Scores by School Size
How did replacing the ninth graders' math and reading scores affect the school size summary?
Since, Thomas High School fell into the Medium size range of schools, you will not see any impact to the Large and Small groups. The math and reading average scores were unchanged, but you see the same impact to the Medium group in the percent passing for math, reading, and overall. We saw a decrease of 94 to 88% for math, 97 to 91% for reading, and 91 to 85% for overall. Without removing the 9th grade Thomas High students from the population, these numbers will continue to be lower than when they were included.

### Scores by School Type
How did replacing the ninth graders' math and reading scores affect the school type summary?
Thomas High School is a charter school, so the District measures will not be affected. There was no change to the math and reading average scores for the Charter group, as we saw in the Medium, and 3rd spending ranges. Percent of passing for math, reading, and overall were impacted, but not as much as we saw in other groups, due to this group consisting of more students than the other comparisons we saw. There was a decrease in math from 94 to 90%, reading 97 to 93%, and overall 90 to 87%.

### Recommendations

While we did remove the scores of the 9th grade class, we should have also removed their student count when looking at pass percentage of the school to provide a true representation of the school. These numbers are greatly deflated due to having the scores being removed but still having the students count towards population.
