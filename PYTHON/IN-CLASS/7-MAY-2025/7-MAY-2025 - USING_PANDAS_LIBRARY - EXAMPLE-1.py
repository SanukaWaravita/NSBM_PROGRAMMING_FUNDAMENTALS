# Example: Pandas

# Python + Pandas = Data Manipulation

import pandas as pd

# creating a data frame
data = {'Name' :['Anne', 'Ravi', 'Sunil'],
        'Age' :[25, 22, 23],
        'City' :['Colombo', 'Kandy', 'Galle']
        }

df = pd.DataFrame (data)
print(df)