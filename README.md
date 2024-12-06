# GobbleCube_Task

This project involves creating a backend service to support an analytical dashboard. The service processes data from CSV files, provides RESTful APIs for querying data, and includes a simple frontend for user interaction. It enables efficient analysis of sales and market trends across product categories.

# Features
API Endpoints:
Retrieve total sales for a specified date range.
Fetch sales data grouped by product categories.
Identify significant changes in market share for categories.
Frontend Dashboard:
Built using HTML, CSS, and JavaScript.
Interactive inputs to specify date ranges and categories.
Visual response display for API results.
CSV Integration:
Data loaded from three CSV files:
Sales Data: Contains transaction details.
Category Share Data: Contains market share details.
Product Category Mapping: Maps products to categories.

# Technologies Used
Backend:
Flask: Lightweight Python framework for building RESTful APIs.
Pandas: For data manipulation and efficient CSV file handling.
Frontend:
HTML, CSS, JavaScript: To create a minimal dashboard for user interaction.
JavaScript's fetch API: To call the backend endpoints.
Tools:
Postman: For API testing.
Render (Deployment): Backend hosted for public access.

# API Endpoints
Retrieve Total Sales
Endpoint: /total_sales
Parameters: start_date, end_date.
Response: Total revenue within the date range.
Fetch Sales by Category
Endpoint: /sales_by_category
Parameters: start_date, end_date, category_id.
Response: Sales data for the specified category.
Analyze Market Share Changes
Endpoint: /market_share_changes
Parameters: start_date, end_date.
Response: Category with the most significant market share change.
Get Categories
Endpoint: /categories
Response: List of all product categories.
System Design
Architecture
Backend:
Flask handles API requests, processes data with Pandas, and merges datasets efficiently.
CSV files act as the database.
Frontend:
Provides input fields for selecting date ranges and categories.
Displays API results in JSON format for simplicity.
Data Joining Logic
Merged Sales Data with Product Category Mapping for category-level insights.
Merged the result with Category Share Data for market trend analysis.
