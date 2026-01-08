import duckdb
import os

# --- Configuration ---
FILE_NAME = 'Sample_Superstore.csv'
# Using DuckDB to connect to and query the CSV file directly
DB_PATH = FILE_NAME

def run_query(query_title, sql_query):
    """Executes a SQL query and prints the titled results."""
    print("-" * 60)
    print(f"✅ {query_title}")
    print("-" * 60)
    
    try:
        # Use a temporary DuckDB connection to read the CSV and execute the query
        result = duckdb.query(sql_query).to_df()
        
        # Determine the key insight based on the task
        if "Segment" in query_title:
            # Task 2: Find the most profitable segment
            most_profitable_segment = result.sort_values(by='Total_Profit', ascending=False).iloc[0]
            print(f"Key Insight: The '{most_profitable_segment['Segment']}' segment is the most profitable.")
        elif "Unprofitable Orders" in query_title and not result.empty:
            # Task 3: Find the category with the largest loss
            largest_loss_category = result.iloc[0]['Category']
            print(f"Key Insight: The largest losses are concentrated in the '{largest_loss_category}' category.")
        elif "Sales Trend" in query_title and not result.empty:
             # Task 4: Find the peak sales month
            peak_month = result.sort_values(by='Monthly_Sales', ascending=False).iloc[0]
            print(f"Key Insight: Sales peak in {peak_month['Order_Year_Month']} with a total of ${peak_month['Monthly_Sales']:.2f}.")
        
        print("\n--- RESULTS TABLE ---")
        print(result.to_string())
        
    except Exception as e:
        print(f"An error occurred during execution: {e}")
        print(f"SQL Attempted: \n{sql_query}")
        
    print("\n")


if os.path.exists(FILE_NAME):
    print("--- Superstore Data Analysis Project Start ---")

    # ----------------------------------------------------
    # PROJECT TASK 1: Overall Totals
    # Goal: Calculate total sales and profit across all years.
    # SQL Skill: SUM()
    # ----------------------------------------------------
    task_1_sql = f"""
    SELECT
        SUM(Sales) AS Grand_Total_Sales,
        SUM(Profit) AS Grand_Total_Profit
    FROM
        '{DB_PATH}';
    """
    run_query("Task 1: Grand Totals (Sales and Profit)", task_1_sql)

    # ----------------------------------------------------
    # PROJECT TASK 2: Segment Analysis
    # Goal: Calculate total sales and profit by Customer Segment.
    # SQL Skill: GROUP BY
    # ----------------------------------------------------
    task_2_sql = f"""
    SELECT
        Segment,
        SUM(Sales) AS Total_Sales,
        SUM(Profit) AS Total_Profit
    FROM
        '{DB_PATH}'
    GROUP BY
        Segment
    ORDER BY
        Total_Profit DESC;
    """
    run_query("Task 2: Sales & Profit by Customer Segment", task_2_sql)

    # ----------------------------------------------------
    # PROJECT TASK 3: Unprofitable Orders Report
    # Goal: Find large orders (Quantity > 10) that lost money (Profit < 0).
    # SQL Skill: WHERE with AND, ORDER BY
    # ----------------------------------------------------
    task_3_sql = f"""
    SELECT
        "Order ID",
        Profit,
        Quantity,
        Category
    FROM
        '{DB_PATH}'
    WHERE
        Profit < 0 AND Quantity > 10
    ORDER BY
        Profit ASC; -- ASC to put largest losses (most negative profit) at the top
    """
    run_query("Task 3: Unprofitable Orders Report (Quantity > 10)", task_3_sql)

    # ----------------------------------------------------
    # PROJECT TASK 4: Monthly Sales Trend Analysis
    # Goal: Calculate total sales for every Year and Month.
    # SQL Skill: STRFTIME (Date Formatting), GROUP BY
    # ----------------------------------------------------
    task_4_sql = f"""
    SELECT
        STRFTIME('%Y-%m', "Order Date") AS Order_Year_Month,
        SUM(Sales) AS Monthly_Sales
    FROM
        '{DB_PATH}'
    GROUP BY
        Order_Year_Month
    ORDER BY
        Order_Year_Month ASC;
    """
    run_query("Task 4: Monthly Sales Trend Analysis", task_4_sql)

    print("--- Project Complete ---")

else:
    print(f"Error: Data file '{FILE_NAME}' not found.")
    print("Please ensure the CSV file is in the same directory as the script.")
    
