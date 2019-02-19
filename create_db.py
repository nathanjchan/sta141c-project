import pandas as pd
import sqlalchemy as sqla
import subprocess
"""
creates a database from csv file
"""

filename = 'transaction.csv'
_chunksize = 50000

#lines = subprocess.check_output('cat ' + filename + ' | wc -l', shell=True)
#lines = int(lines.decode())
lines = 10000000

reader = pd.read_csv(filename, chunksize=_chunksize, low_memory=False)
chunk = next(reader)
#sqlite_filename = filename.split('.')[0]
sqlite_filename = 'small'
_conn = sqla.create_engine('sqlite:///' + sqlite_filename)
chunk.to_sql(sqlite_filename, _conn, if_exists='replace')

count = 0
for chunk in reader:
	count += _chunksize
	print('appending... ', str(count) + '/' + str(lines), '{0:.2f}%'.format((count / lines) * 100))
	chunk.to_sql(sqlite_filename, _conn, if_exists='append')
	if count > 1000:
		break
