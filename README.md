## Retail Customer Sales Analytics

### Purposes:
1 - Set up a modern analytics stack including VS Code, Miniconda, DuckDB and dbt.
2 - Create a realistic modern warehouse project, including testing, documentation, snapshots, and incremental models.
3 - Simulate a small retail business to address business questions:
-- Who are the top customers?
-- What products generate the most revenue?
-- Which customers are becoming inactive?
-- Monthly sales trends
-- Repeat customer behaviour
-- Customer lifetime value (CLV)
-- Refund and return analysis

### Architecture
CSV Raw Files -- raw injection layer
     ↓
DuckDB 
     ↓
dbt staging models -- data cleaning 
     ↓
dbt intermediate models -- business transformation
     ↓
dbt marts -- BI-ready tables
     ↓
Power BI / Tableau

It also includes: 
Tests	-- Data quality
Documentation	-- Data governance
Snapshots	-- Slowly changing dimensions
Incremental models	-- Large-scale optimisation
Macros	-- Reusable SQL
Seeds	-- Small reference tables
Exposures	-- BI lineage
dbt DAG	-- Dependency management

