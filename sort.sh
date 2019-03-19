sqlite3 -header -csv /scratch/usaspending.sqlite "SELECT DISTINCT
fiscal_year, total_obligation, awarding_agency_id, funding_agency_id
FROM universal_transaction_matview;" > distinct_transaction.csv
