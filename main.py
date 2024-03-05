"""
The main module of the application. Connects the builder, the UI, and the data.
"""

#I am not so sure if i made the dummy write

from faker import Faker
import pandas as pd
fake = Faker()
data = [fake.profile() for i in range(50)]
data = pd.DataFrame(data)
print(data.head())
