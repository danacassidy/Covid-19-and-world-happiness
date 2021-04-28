import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#import confirmed covid cases dataset
covid_dataset_csv= pd.read_csv('/Users/danacassidy/Code_projects/python_projects/covid19analysis/covid19_Confirmed_dataset.csv')
covid_dataset_csv.head(10)

#check the shape of the dataframe
covid_dataset_csv.shape

#delete the useless columns
covid_dataset_csv.drop(['Lat','Long'],axis=1, inplace=True)
covid_dataset_csv.head(10)

#aggregating the rows by the country
covid_dataset_aggregated = covid_dataset_csv.groupby("Country/Region").sum()
covid_dataset_aggregated.head()
covid_dataset_aggregated.shape

#visualizing data related to a country

covid_dataset_aggregated.loc["China"].plot()
covid_dataset_aggregated.loc["Italy"].plot()
covid_dataset_aggregated.loc["Spain"].plot()
plt.legend()


#finding the maximm infection rate
covid_dataset_aggregated.loc["China"].diff().max()
covid_dataset_aggregated.loc["Italy"].diff().max()
covid_dataset_aggregated.loc["Spain"].diff().max()

#finding the maximum infection rate for all of the countries
countries = list(covid_dataset_aggregated.index)
max_infection_rates=[]
for x in countries:
    max_infection_rates.append(covid_dataset_aggregated.loc[x].diff().max())
covid_dataset_aggregated["max_infection_rate"]=max_infection_rates

covid_dataset_aggregated.head()

#creating a new dataframe with only the needed column
corona_data = pd.DataFrame(covid_dataset_aggregated['max_infection_rate'])
corona_data.head()

##moving on to the worldhappinessreport.csv

#importing the worldhappiness dataset
happiness_report_csv = pd.read_csv('/Users/danacassidy/Code_projects/python_projects/covid19analysis/worldwide_happiness_report.csv')
happiness_report_csv.head()

#dropping the useless columns
useless_cols = ['Overall rank','Score','Generosity', "Perceptions of corruption"]
happiness_report_csv.drop(useless_cols, axis=1,inplace=True)
happiness_report_csv.head()

#changing the indices of the dataframe
happiness_report_csv.set_index('Country or region', inplace=True)
happiness_report_csv.head()

#joining the two datasets together

#covid dataset
corona_data.head()
corona_data.shape

#happiness dataset
happiness_report_csv.head()
happiness_report_csv.shape

#correlation matrix
data = corona_data.join(happiness_report_csv, how = "inner")

#Let us do some visualizing, yall!
x = data['GDP per capita']
y= data['max_infection_rate']


sns.scatterplot(x,np.log(y))
plt.show()
sns.regplot(x,np.log(y))
plt.show()





