import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

def read_csv_into_dataframe(fileName):
    return pd.read_csv(fileName, skiprows=[0,1,2,3])

def plot_electric_power_consumption(X, Y):
    plt.plot(X, Y)
    plt.title('Per capita Electric power consumption from 1990 to 2014')
    plt.xlabel('Year')
    plt.ylabel('kWh')
    plt.show()
    
def plot_CO2_emission(X, Y):
    plt.plot(X, Y)
    plt.title('Per capita CO2 emission in metric tonnes from 1990 to 2014')
    plt.xlabel('Year')
    plt.ylabel('Metric tonnes')
    plt.show()

electric_power_consumption_data = read_csv_into_dataframe(
    'API_EG.USE.ELEC.KH.PC_DS2_en_csv_v2_4697520.csv')
co2_emission_data = read_csv_into_dataframe(
    'API_EN.ATM.CO2E.PC_DS2_en_csv_v2_4700403.csv')
X = range(1990, 2015)
electric_power_consumption = electric_power_consumption_data.iloc[259, 34:59]
co2_emission = co2_emission_data.iloc[259, 34:59]
df = pd.DataFrame({'Electricity consumption':electric_power_consumption, 
                   'CO2 emission':co2_emission})
print(df)
plot_electric_power_consumption(X, electric_power_consumption)
plot_CO2_emission(X, co2_emission)
print('The average per capita electric power consumption over the years is: ' +
      str(np.mean(electric_power_consumption)))
print('The average per capita CO2 emission over the years is :' +
      str(np.mean(co2_emission)))
print('The standard deviation of per capita electric power consumption is: ' + 
      str(electric_power_consumption.std()))
print('The standard deviation of per capita CO2 emission is: ' + 
      str(co2_emission.std()))
corr, pval = stats.pearsonr(electric_power_consumption, co2_emission)
print('The correlation between per capita electricity consumption and per capita co2 emission is: '+ str(corr))