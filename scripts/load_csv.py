import pandas as pd
from sqlalchemy import create_engine

# Load CSV
df = pd.read_csv("data/sales.csv")

# SQL Server connection
server = "localhost"
database = "CustomerSales"

connection_string = (
    f"mssql+pyodbc://@{server}/{database}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

engine = create_engine(connection_string)

# Load to SQL Server
df.to_sql(
    "sales",
    engine,
    if_exists="replace",
    index=False
)

print("Data loaded successfully.")