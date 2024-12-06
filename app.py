from flask import Flask, request, jsonify, render_template
import pandas as pd
app = Flask(__name__)
try:
    sales_data = pd.read_csv('database/sales_data.csv')
    category_share_data = pd.read_csv('database/category_share_data.csv')
    product_category_mapping = pd.read_csv('database/product_category_mapping.csv')
except FileNotFoundError as e:
    raise FileNotFoundError(f"Error loading CSV files: {e}")

sales_data['date'] = pd.to_datetime(sales_data['date'], errors='coerce')
category_share_data['date'] = pd.to_datetime(category_share_data['date'], errors='coerce')

# Merge sales data with product-category mapping
sales_data = sales_data.merge(product_category_mapping, on='product_id', how='left')

# Validate that all required columns are present
required_sales_columns = {'date', 'product_id', 'revenue'}
required_category_columns = {'date', 'product_id', 'market_share'}
required_mapping_columns = {'product_id', 'category_id'}

if not required_sales_columns.issubset(sales_data.columns):
    missing_columns = required_sales_columns - set(sales_data.columns)
    raise ValueError(f"Missing required columns in sales_data: {missing_columns}")
if not required_category_columns.issubset(category_share_data.columns):
    missing_columns = required_category_columns - set(category_share_data.columns)
    raise ValueError(f"Missing required columns in category_share_data: {missing_columns}")
if not required_mapping_columns.issubset(product_category_mapping.columns):
    missing_columns = required_mapping_columns - set(product_category_mapping.columns)
    raise ValueError(f"Missing required columns in product_category_mapping: {missing_columns}")

# print("Sample Sales Data:")
# print(sales_data.head())


# Home route
@app.route('/')
def home():
    return render_template("index.html")

# API to calculate total sales within a specified date range
@app.route('/total_sales', methods=['GET'])
def total_sales():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    if not start_date or not end_date:
        return jsonify({'error': 'start_date and end_date are required'}), 400

    try:
        filtered_data = sales_data[
            (sales_data['date'] >= pd.to_datetime(start_date)) & 
            (sales_data['date'] <= pd.to_datetime(end_date))
        ]
    except Exception as e:
        return jsonify({'error': f"Invalid date format: {e}"}), 400

    # Calculate total sales
    total_sales = filtered_data['revenue'].sum()

    return jsonify({'total_sales': float(total_sales)})


@app.route('/categories', methods=['GET'])
def get_categories():
    categories = product_category_mapping['category_id'].unique()
    categories_list = [{'category_id': category} for category in categories]
    print(categories_list)
    return jsonify(categories_list)

# Route to calculate sales for a specific category within a date range
@app.route('/sales_by_category', methods=['GET'])
def sales_by_category():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    category_id = request.args.get('category_id')
    if not start_date or not end_date:
        return jsonify({'error': 'start_date and end_date are required'}), 400
    if not category_id:
        return jsonify({'error': 'category_id is required'}), 400
    try:
        filtered_data = sales_data[
            (sales_data['date'] >= pd.to_datetime(start_date)) &
            (sales_data['date'] <= pd.to_datetime(end_date)) &
            (sales_data['category_id'] == category_id)
        ]
    except Exception as e:
        return jsonify({'error': f"Invalid input: {e}"}), 400
    total_sales = filtered_data['revenue'].sum()
    return jsonify({'category_id': category_id, 'total_sales': float(total_sales)})

@app.route('/market_share_changes', methods=['GET'])
def market_share_changes():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    if not start_date or not end_date:
        return jsonify({'error': 'start_date and end_date are required parameters'}), 400
    try:
        filtered_data = category_share_data[
            (category_share_data['date'] >= pd.to_datetime(start_date)) & 
            (category_share_data['date'] <= pd.to_datetime(end_date))
        ]
    except Exception as e:
        return jsonify({'error': f"Invalid date format: {e}"}), 400
    merged_data = filtered_data.merge(product_category_mapping, on='product_id', how='left')
    category_share_changes = (
        merged_data.groupby('category_id')['market_share']
        .agg(['min', 'max'])
        .reset_index()
    )
    category_share_changes['share_change'] = category_share_changes['max'] - category_share_changes['min']
    significant_changes = category_share_changes.loc[
        category_share_changes['share_change'].abs().idxmax()
    ]
    result = {
        'category_id': significant_changes['category_id'],
        'share_change': float(significant_changes['share_change'])
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
