import duckdb

con = duckdb.connect("sales.duckdb")

result = con.execute("""
    SELECT customer,
           SUM(amount) AS total_sales
    FROM read_csv_auto('data/sales.csv')
    GROUP BY customer
    ORDER BY total_sales DESC
""").fetchdf()

print(result)