#**Pandas Basic codes**

#Data Acquisition

# Import the necessary libraries

import pandas as pd



# Import the dataset

data = pd.read_csv('titanic.csv')

"""#Exploratry Data Analysis ---- Examine the data
**name** - # print the first 30 and last 30 rows
**head()**- # print the first 5 rows
**tail()** - # print the last 5 
**describe()** - # describe any numeric columns
**info()** - # concise summary
"""

data

data.head()

data.tail()

data.describe()

data.describe(include = "all")

data.age.describe()



"""Mean age of members"""

round(data.age.mean())



"""Age with least occurrence"""

data.age.value_counts().tail()

data.info()


"""# Dataset Format

*  **survival** - Survival (0 = No; 1 = Yes)
*  **class** - Passenger Class (1 = 1st; 2 = 2nd; 3 = 3rd)
*  **name** - Name
*  **sex** - Sex
*  **age** - Age
*  **sibsp** - Number of Siblings/Spouses
*  **parch** - Number of Parents/Children Aboard
*  **ticket** - Ticket Number
*  **fare** - Passenger Fare
*  **cabin** - Cabin
*  **embarked** - Port of Embarkation
(**C** = Cherbourg; **Q** = Queenstown; **S** = Southampton)
*  **boat** - Lifeboat (if survived
*  **body** - Body number (if did not survive and body was recovered)
"""

print(data.columns)

data.columns[10]

data.values[18][7]

print(data.shape)

data.shape[0]

print(data.groupby('name').size())

data.index

a = data.sort_values(['age'], ascending = True)

print(a)


""" # Examine the data types of the different columns"""

data.dtypes


"""# Data Type"""

pd.Series(data.name)

pd.DataFrame(data.ticket)


"""# Examine and grouping the data set for survived members"""

# Analysing survived the count of survied / unsurvied  members
b = data.groupby('survived')

b = b.sum()

print(b.pclass)

# Specific Coloumn
print("Specific Coloumn\n")

a= data[['name','ticket']]
a

data.boat.nunique()

print(data.to_string())

a = data.isnull().sum()
print (a)
