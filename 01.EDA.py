import os
from pyprojroot import here
import pandas as pd

uk_ind = pd.read_excel(
    os.path.join(
        here(), "extract", "Big Data Set - Assessing potential measures of GDP.xlsx"
        ), sheet_name="Tabelle1", skiprows=3)

uk_ind.head()