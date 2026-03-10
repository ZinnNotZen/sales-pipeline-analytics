# CRM Sales Opportunities Dataset – Data Dictionary

This dataset simulates a CRM sales pipeline with information on accounts, products, sales teams, and deal opportunities.

Source: Kaggle CRM Sales Opportunities Dataset (https://www.kaggle.com/datasets/innocentmfa/crm-sales-opportunities)

---

# accounts.csv

Contains information about customer companies.

| Column | Description |
|------|-------------|
| account | Unique company identifier |
| sector | Industry sector of the company |
| year_established | Year the company was founded |
| revenue | Annual company revenue |
| employees | Number of employees |
| office_location | Geographic office location |
| subsidiary_of | Parent company (if applicable) |

---

# products.csv

Contains information about products being sold.

| Column | Description |
|------|-------------|
| product | Product name |
| series | Product series category |
| sales_price | Price of the product |

---

# sales_teams.csv

Contains information about the sales organization.

| Column | Description |
|------|-------------|
| sales_agent | Sales representative |
| manager | Sales manager responsible for the rep |
| regional_office | Office location of the sales team |

---

# sales_pipeline.csv

Contains sales opportunity pipeline data.

| Column | Description |
|------|-------------|
| opportunity_id | Unique identifier for each opportunity |
| sales_agent | Sales representative managing the deal |
| product | Product being sold |
| account | Customer company |
| deal_stage | Current stage of the deal |
| engage_date | Date the opportunity entered the pipeline |
| close_date | Date the deal closed |
| close_value | Revenue generated from the deal |
