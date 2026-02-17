# E-Commerce_Demand---Profitability_Intelligence_System
# 🛒 E-Commerce Demand & Profitability Intelligence System

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data_Manipulation-yellow)
![Power BI](https://img.shields.io/badge/Power_BI-Data_Visualization-yellow.svg)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

## 📌 Project Overview
E-commerce companies frequently lose profit margins due to hidden costs like high freight rates, suboptimal discounting, and product returns. This project builds an end-to-end **Business Intelligence System** using the Olist Brazilian E-Commerce dataset to identify profit leakages, optimize logistics, and forecast demand.

## 🎯 Business Objectives
1. **Identify Loss-Making Categories:** Uncover products where freight and operational costs outweigh revenue.
2. **Optimize Logistics Framework:** Analyze the `Freight-to-Value` ratio to find regions with inefficient delivery networks.
3. **Demand Forecasting:** Map seasonal sales trends to optimize inventory for peak periods.
4. **Pareto Analysis (80/20 Rule):** Identify the top 20% of product categories driving 80% of the net revenue.

## 🗄️ The Dataset (Olist E-Commerce)
This project utilizes a **Relational Database** structure comprising 100,000+ real transactions from Olist, Brazil's largest department store marketplace. 
* **Data Engineered Tables:** Orders, Order Items, Products, and Category Translations.
* **Volume:** 100k+ rows merged via complex SQL/Pandas joins to create a unified analytical master table.

## 🛠️ Tech Stack & Workflow
* **Data Extraction & Transformation (ETL):** `Python` (Pandas, NumPy) - Merged multiple CSVs, handled missing values, translated Portuguese categories to English, and engineered new KPIs (Estimated Cost, Profit Margin).
* **Data Modeling & Querying:** `SQL Logic` - Handled relational joins (Inner/Left Joins) to map items to their respective order timestamps and delivery statuses.
* **Data Visualization & Storytelling:** `Power BI` / `Matplotlib` - Built interactive dashboards for executive-level reporting.

## 💡 Key Business Insights
* **The Freight Trap:** Discovered that in specific remote regions, freight costs exceeded 30% of the total order value, severely impacting the conversion rate and profitability.
* **Category Performance:** Implemented a profitability simulation showing that while "Health & Beauty" drives high volume, heavy items (like "Furniture") often result in net losses due to logistics costs.
* **Seasonality:** Identified distinct revenue spikes around late November (Black Friday), requiring a 40% inventory bump in top-performing categories to prevent stockouts.

## 🚀 How to Run the Project
1. Clone this repository: `git clone https://github.com/NathishN/ecommerce-profitability-system.git`
2. Download the [Olist Dataset from Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) and extract it into the `/data` folder.
3. Run the ETL script: `python etl_pipeline.py`
4. Open the generated `master_data.csv` in Power BI or run the Jupyter Notebook `eda_analysis.ipynb` to view the charts.

---
*Developed by [Nathish] - Data Analyst*
