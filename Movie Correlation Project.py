# Import Python Libraries
import numpy as np
import pandas as pd

pd.set_option('display.max_columns', 20)
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

plt.style.use('ggplot')

matplotlib.rcParams['figure.figsize'] = (12, 8)  # plot config

# Read in the data

df = pd.read_csv('/Users/matthewalderman/documents/movies2.csv')

# print(df.head())

# Looking for missing data

for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    # print('{} - {}%'.format(col, pct_missing))

# ID Data Types

# print(df.dtypes)
# Change data type of columns

df['budget'] = df['budget'].astype('int64')
df['gross'] = df['gross'].astype('int64')

# Create Correct Year Column

df['year_correct'] = df['released'].astype(str).str[:4]

df = df.sort_values(by=['gross'], inplace=False, ascending=False)

# print(df)

# Drop duplicate values

df['company'] = df['company'].drop_duplicates().sort_values(ascending=False)

# Pyplot Chart

plt.scatter(x=df['budget'], y=df['gross'])

plt.title('Budget vs Gross Earnings')
plt.xlabel('Budget')
plt.ylabel('Gross')
# plt.show()

# Plot Data Using Seaborn
# sns.regplot(x='budget', y='gross', data=df, line_kws={'color': 'blue'})

# Let's dive deeper into the correlation

# print(df.corr(method='pearson'))  # Other options: Kendall and spearman
# High correlation between budget and gross

# correlation_matrix = df.corr(method='pearson')
# sns.heatmap(correlation_matrix, annot=True)
# plt.title('Movie Feature Correlation Matrix')
# plt.xlabel('Movie Features')
# plt.ylabel('Movie Features')
# plt.show()

# Try to find a correlation with companies

df_numerized = df

for col_name in df_numerized.columns:
    if df_numerized[col_name].dtype == 'object':
        df_numerized[col_name] = df_numerized[col_name].astype('category')
        df_numerized[col_name] = df_numerized[col_name].cat.codes

# Validate that change was effective
# print(df_numerized.dtypes)

correlation_matrix = df_numerized.corr(method='pearson')
sns.heatmap(correlation_matrix, annot=True)
plt.title('Movie Feature Correlation Matrix')
plt.xlabel('Movie Features')
plt.ylabel('Movie Features')
# plt.show()

correlation_mat = df_numerized.corr(method='pearson')
corr_pairs = correlation_mat.unstack()

sorted_pairs = corr_pairs.sort_values(ascending=True)

high_corr = sorted_pairs[sorted_pairs > 0.5]
# print(high_corr)

# Company has low correlation
