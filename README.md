# Superstore Analysis Project

## Overview
This project provides a comprehensive analysis of the Superstore Dataset, demonstrating a complete data workflow from raw CSV data processing using Python and SQL (DuckDB) to professional business intelligence visualization in Power BI. The goal is to extract actionable insights on sales performance, regional trends, and profit margins to support data-driven decision-making.

## Dashboard Preview
<img width="1764" height="777" alt="Superstore Dashboard" src="https://github.com/user-attachments/assets/2c54b0f8-e946-493f-8c8e-369f8a4bcac5" />

## Features
SQL Integration: High-performance SQL queries executed directly on CSV files using DuckDB.

Python Data Processing: Data cleaning and preparation, including handling encoding issues for non-UTF-8 (Latin-1) files.

Business Intelligence: Interactive Power BI dashboard monitoring key performance indicators (KPIs) such as total sales, profit trends, and regional performance.

Loss Analysis: Targeted identification of unprofitable orders with high quantity for strategic review.

---

## Project Structure

| File | Description |
|------|-------------|
| `Sample_Superstore.csv` | Primary dataset containing sales, category, and regional data. |
| `project_analysis.py` | Python script using DuckDB for SQL-based aggregation and analysis. |
| `Superstore_Dashboard.pbix` | Power BI file with interactive visual analysis. |

---

## Requirements

To run the Python analysis:

- Python 3.x  
- DuckDB (`pip install duckdb`)  
- Pandas (`pip install pandas`)  

To view the Power BI dashboard:

- Power BI Desktop (required to open `.pbix` file)

---

## Getting Started

1. **Clone the repository**
```bash
git clone https://github.com/Evgeniia7/Superstore-Analysis-Project.git
cd Superstore-Analysis-Project

### Run the Python analysis
python3 project_analysis.py

#### View the Power BI Dashboard
Open Power BI Desktop

Open Superstore_Dashboard.pbix

Use the slicers (filters) to explore data by Region, Category, or Segment


