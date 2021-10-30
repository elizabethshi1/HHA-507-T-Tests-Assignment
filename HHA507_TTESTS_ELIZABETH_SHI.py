# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 15:34:06 2021

@author: Elizabeth Shi
"""

import pandas as pd
from scipy.stats import ttest_ind
url ="https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Datasets/Diabetes/DB1_Diabetes/diabetic_data.csv"
diabetes = pd.read_csv(url)

# 1) Is there a difference between sex (M:F) and the number of days in hospital?
# Sex is IV and number of days in hospital is DV

Female = diabetes[diabetes['gender']=='Female']
Male = diabetes[diabetes['gender']=='Male']

ttest_ind(Female['time_in_hospital'], Male['time_in_hospital'])

# Ttest_indResult(statistic=9.542637042242887, pvalue=1.4217299655114968e-21)
# There is a significant difference between sex and the number of days in the hospital because the pvalue is below .05 which means that it does not
# fall within the normal distribution.



# 2) Is there a difference between RACE (Caucasian and African American) and the number of days in hospital?
# Race is IV and number of days in hospital is DV

Caucasian = diabetes[diabetes['race']=='Caucasian']
African_American = diabetes[diabetes['race'] == 'AfricanAmerican']

ttest_ind(Caucasian['time_in_hospital'], African_American['time_in_hospital'])

#  Ttest_indResult(statistic=-5.0610017032095325, pvalue=4.178330085585203e-07)
# There is a difference between the race (Caucasian and African American) and the number of days in the hospital because the pvalue is below .05
# which means that it does not fall within the normal distribution.



# 3) Is there a difference between RACE (Asian and African American) and the number of lab procedures performed?
# Race is IV and the number of lab procedures is DV

Asian = diabetes[diabetes['race']=='Asian']
African_American = diabetes[diabetes['race'] == 'AfricanAmerican']

ttest_ind(Asian['num_lab_procedures'], African_American['num_lab_procedures'])

# Ttest_indResult(statistic=-3.9788715315360292, pvalue=6.948907528800307e-05)
# There is a difference between the race (Asian and African American) and the number of days in the hospital because the pvalue is below .05 which
# means that it does not fall within the normal distribution.