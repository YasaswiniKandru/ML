# ML
Linear regression to predict COVID-19 mortality in the countries worldwide. For each country, we have the following two features:

1)Percentage of persons over the age of 65 in the population. This information can be found at https://en.wikipedia.org/wiki/List_of_countries_by_age_structure
2)The number of hospital beds per 1,000 people in the most recent reported year. This information can be found at https://data.worldbank.org/indicator/SH.MED.BEDS.ZS

The response variable for each country will be the number ofCOVID-19 deaths per 100K population. This information can be found at https://coronavirus.jhu.edu/data/mortalityTo train the model, use the data from 10 countries of your choice (excluding USA).

Then applied the trained model to predictt he number of deaths per 100K persons in the USA. I have used Linear Regression functions from sklearn package (https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)
