# API Locator Dashboard  

This project is an *API Dashboard* for tracking total sales, category-specific sales, and market share changes across products. It features a front-end user interface for interacting with the APIs and a back-end built with Flask. The project is hosted online and integrates datasets for sales, product categories, and market share.  

## Features  
- *Fetch Total Sales:* Calculate total sales within a specified date range.  
- *Category-Specific Sales:* Retrieve total sales for a specific product category within a date range.  
- *Market Share Changes:* Identify the category with the highest market share change (positive or negative) within a date range.  
- *Dynamic Dropdowns:* Fetch and display available product categories dynamically from the API.  

---

## Live Demo  
The project is hosted at: [API Locator Dashboard](https://gobblecube-api-dashboard.onrender.com/)  

---

## Installation  

### Prerequisites  
- Python 3.10 or higher  
- Flask  
- Pandas  
- A modern browser (e.g., Chrome, Firefox)  

### Steps  

1. Clone the repository:  
   bash
   git clone [https://github.com/username/repo-name.git](https://github.com/Riteeeeee/GobbleCube_Task/)
   cd GobbleCube_Task
     

2. Install dependencies:  
   bash
   pip install -r requirements.txt
     

3. Run the application:  
   bash
   python app.py
     

4. Open the application in your browser:  
   arduino
   http://127.0.0.1:5000

## API Endpoints  

### 1. /total_sales  
- *Method:* GET  
- *Description:* Retrieves the total sales within a specified date range.  
- *Parameters:*  
  - start_date (required): Start of the date range.  
  - end_date (required): End of the date range.  

### 2. /categories  
- *Method:* GET  
- *Description:* Fetches the available product categories.  

### 3. /sales_by_category  
- *Method:* GET  
- *Description:* Retrieves total sales for a specific category in a date range.  
- *Parameters:*  
  - start_date (required): Start of the date range.  
  - end_date (required): End of the date range.  
  - category_id (required): ID of the category to retrieve sales for.  

### 4. /market_share_changes  
- *Method:* GET  
- *Description:* Identifies the category with the highest market share change.  
- *Parameters:*  
  - start_date (required): Start of the date range.  
  - end_date (required): End of the date range.  

---

## Technologies Used  
- *Back-end:* Flask  
- *Front-end:* HTML, CSS, JavaScript  
- *Data Processing:* Pandas  
- *Hosting:* [Render](https://render.com)  

---

## Author  
Developed by *Ritee Sharma*.  
GitHub: [https://github.com/riteesharma](https://github.com/Riteeeeee)
