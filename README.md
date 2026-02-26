# Superstore Analysis Project

## Overview

This project provides a comprehensive analysis of the Superstore Dataset, demonstrating a complete data workflow from raw CSV data processing using Python and SQL (DuckDB) to professional business intelligence visualization in Power BI. The goal is to extract actionable insights on sales performance, regional trends, and profit margins.

Dashboard Preview
<img width="1764" height="777" alt="Superstore Dashboard" src="https://github.com/user-attachments/assets/2c54b0f8-e946-493f-8c8e-369f8a4bcac5" />
---

## Features

- **SQL Integration**: Perform high-performance SQL queries directly on CSV files using DuckDB.  
- **Python Data Processing**: Clean and prepare the dataset, including handling encoding issues for non-UTF-8 (Latin-1) files.  
- **Business Intelligence Visualization**: Create an interactive Power BI dashboard to monitor key performance indicators (KPIs) such as sales trends, regional performance, and profit margins.

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


