# Sales Pipeline Analytics

This project analyzes CRM sales opportunity data to evaluate pipeline health, sales performance, and revenue drivers. The goal is to simulate the type of analytics work performed in Sales Operations and Revenue Operations roles, turning raw sales data into actionable insights for leadership.

---

## 📊 Dashboard Preview

<img width="1298" height="1610" alt="Sales Performance Overview" src="https://github.com/user-attachments/assets/732ed195-a2e4-459b-89a1-bac0245c2fc9" />


---

## 📌 Project Objectives

* Evaluate overall pipeline health and deal distribution across stages
* Measure sales performance at the representative level
* Analyze sales cycle efficiency and identify delays
* Identify key revenue drivers across products and accounts
* Calculate core sales KPIs such as win rate, pipeline value, and average deal size
* Simulate forecasting and pipeline reporting used by sales leadership

---

## 📈 Key Insights

**Pipeline Bottlenecks**
A significant concentration of deals occurs in late-stage pipeline phases, suggesting potential friction during negotiation and closing.

**Sales Performance Variability**
Revenue generation is unevenly distributed across sales representatives, indicating reliance on a small group of high performers.

**Sales Cycle Efficiency**
Sales cycle length varies across reps and deal types, highlighting opportunities to streamline processes and reduce time to close.

**Revenue Drivers**
Certain products contribute disproportionately to total revenue, indicating stronger product-market fit.

---

## 📊 Dashboard Metrics

The Tableau dashboard includes:

* Total Pipeline Value
* Win Rate
* Average Sales Cycle
* Average Deal Size
* Pipeline Funnel (Deal Stage Distribution)
* Revenue by Sales Representative
* Sales Cycle by Representative
* Rep Win Rate
* Pipeline Value By Stage
* Revenue by Product

---

## 🛠️ Tools & Technologies

* Python (Pandas, NumPy, Matplotlib, Scikit-learn)
* Tableau (Dashboard Development)
* SQL (Data querying concepts)
* Git & GitHub

---

## 📂 Repository Structure

```
sales-pipeline-analytics/
│
├── data/
│   Raw CSV datasets
│
├── notebooks/
│   pipeline_analysis.ipynb (EDA and visualization)
│
├── src/
│   data_cleaning.py
│   pipeline_metrics.py
│   forecasting_analysis.py
│   run_pipeline.py
│
├── dashboards/
│   sales_pipeline_dashboard.twbx
│
├── images/
│   dashboard_preview.png
│   pipeline_funnel.png
│   revenue_by_rep.png
│
├── sales_leadership_report.md
├── README.md
└── requirements.txt
```

---

## ⚙️ Key Calculations

**Win Rate**

```
SUM(IF [deal_stage] = "Won" THEN 1 END) / COUNT([opportunity_id])
```

**Sales Cycle Length**

```
DATEDIFF('day', [engage_date], [close_date])
```

**Pipeline Value**

```
IF [deal_stage] != "Lost" THEN ZN([close_value]) END
```

---

## 🔮 Forecasting Component

A basic predictive model was developed to estimate the likelihood of deal closure using features such as:

* Product
* Account
* Sales Agent
* Engagement timing

This simulates forecasting support commonly provided in sales analytics roles.

---

## 🚀 How to Run the Project

Clone the repository:

```
git clone https://github.com/ZinnNotZen/sales-pipeline-analytics
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the pipeline:

```
python src/run_pipeline.py
```

---

## 📎 Dataset

CRM Sales Opportunities dataset sourced from Kaggle.

---

## 👤 Author

Rowan Zinn
MS Data Science – Western Governors University

GitHub: https://github.com/ZinnNotZen

---

## 💡 Summary

This project demonstrates the ability to:

* Build end-to-end data analysis workflows
* Develop sales performance metrics and KPIs
* Create executive-ready dashboards
* Translate data into actionable business insights

It reflects real-world responsibilities in Sales Analytics and Business Intelligence roles.
