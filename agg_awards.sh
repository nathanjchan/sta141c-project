# generates aggregated annual spending for each awarding/funding agency
sqlite3 -header -csv /scratch/usaspending.sqlite "SELECT fiscal_year, awarding_agency_id, funding_agency_id,
SUM(total_obligation) as annual_spending
FROM awards
GROUP BY fiscal_year, awarding_agency_id, funding_agency_id;" > agg_awards.csv
