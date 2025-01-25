# Beta Version #
# Note to be added ## 

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Assuming data is stored in a DataFrame called df
df = pd.DataFrame({
    'Country': ['India', 'Nigeria', 'Algeria', 'Kenya', 'Senegal', 'Pakistan', 'Vietnam', 'Canada', 'Australia', 'Myanmar', 'Uganda', 'Tanzania', 'Sudan', 'Rwanda', 'Bangladesh', 'Sierra Leone', 'Jamaica', 'Malta', 'Ghana', 'Malaysia', 'Zimbabwe', 'Cameroon', 'Tunisia', 'Madagascar', 'Morocco', 'Lebanon', 'Mali', 'Ivory Coast', 'Chad', 'Niger', 'Burkina Faso', 'Guinea', 'Benin', 'Central African Rep', 'Congo', 'Gabon', 'Mauritius', 'Fiji', 'Botswana', 'Papua New Guinea'],
    'Happiness Index': [3.573, 5.269, 5.233, 4.583, 5.446, 5.653, 5.353, 7.6, 7.22, 4.394, 4.432, 4.635, 4.139, 3.334, 4.694, 4.709, 5.935, 6.77, 5.088, 5.522, 4.123, 5.329, 4.804, 5.385, 5.545, 5.948, 4.983, 5.235, 4.559, 4.298, 4.769, 4.535, 4.883, 3.47, 4.805, 5.728, 6.574, 6.186, 5.099, 4.509],
    'Independence From': ['UK', 'UK', 'France', 'UK', 'France', 'UK', 'France', 'UK', 'UK', 'UK', 'UK', 'UK', 'UK', 'Belgium', 'UK', 'UK', 'UK', 'UK', 'UK', 'UK', 'UK', 'France', 'France', 'France', 'France', 'France', 'France', 'France', 'France', 'France', 'France', 'France', 'France', 'France', 'France', 'France', 'UK', 'UK', 'UK', 'UK']
})

plt.figure(figsize=(10, 6))
sns.boxplot(x='Independence From', y='Happiness Index', data=df)
plt.title('Distribution of Happiness Index based on Country of Independence')
plt.show()

from scipy.stats import ttest_ind, mannwhitneyu

# Separate the data into two groups
group_uk = df[df['Independence From'] == 'UK']['Happiness Index']
group_france = df[df['Independence From'] == 'France']['Happiness Index']

# Perform t-test (assuming normal distribution)
ttest_results = ttest_ind(group_uk, group_france)
print('t-test results:', ttest_results)

# Perform Mann-Whitney U test
mannwhitneyu_results = mannwhitneyu(group_uk, group_france)
print('Mann-Whitney U test results:', mannwhitneyu_results)

import numpy as np

# Cohen&#x27;s d for the t-test
cohens_d = (np.mean(group_uk) - np.mean(group_france)) / np.sqrt((np.std(group_uk)**2 + np.std(group_france)**2) / 2)
print('Cohen&#x27;s d:', cohens_d)