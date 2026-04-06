import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://miguel:1234@localhost:5432/testdb"
)

df = pd.read_sql("SELECT version();", engine)

print(df)
