import pandas as pd
import sqlalchemy as sqla

_conn = sqla.create_engine('sqlite:///transaction')

query = """
select recipient_unique_id, awarding_agency_id
from 'transaction'
limit 50
"""	

print(pd.read_sql_query(query, _conn))
