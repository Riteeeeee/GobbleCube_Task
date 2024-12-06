
// Function to fetch categories from backend
async function fetchCategories() {
    const url = 'https://gobblecube-api-dashboard.onrender.com/categories';

    try {
        const response = await fetch(url);
        const data = await response.json();

        const categorySelect = document.getElementById('category');
        categorySelect.innerHTML = ""; // Clear existing options

        const defaultOption = document.createElement('option');
        defaultOption.value = "";
        defaultOption.text = "Select a category";
        categorySelect.appendChild(defaultOption);

        data.forEach(category => {
            const option = document.createElement('option');
            option.value = category.category_id;
            option.text = `Category ${category.category_id}`;
            categorySelect.appendChild(option);
        });
    } catch (error) {
        console.error('Error fetching categories:', error);
        alert("Failed to load categories. Check the console for details.");
    }
}

// Function to get total sales (without category)
async function getTotalSales() {
    const startDate = document.getElementById('start_date').value;
    const endDate = document.getElementById('end_date').value;

    if (!startDate || !endDate) {
        alert("Please select both start and end dates.");
        return;
    }

    const url = `https://gobblecube-api-dashboard.onrender.com/total_sales?start_date=${startDate}&end_date=${endDate}`;
    const resultContainer = document.getElementById('total_sales_result');

    try {
        resultContainer.textContent = "Loading...";
        const response = await fetch(url);

        if (!response.ok) {
            throw new Error(`Error: ${response.status} ${response.statusText}`);
        }

        const data = await response.json();
        resultContainer.textContent = JSON.stringify(data, null, 2);
    } catch (error) {
        console.error("Error:", error);
        resultContainer.textContent = "An error occurred. Please check the console for details.";
    }
}

// Function to get sales by category
async function getSalesByCategory() {
    const startDate = document.getElementById('start_date').value;
    const endDate = document.getElementById('end_date').value;
    const categoryId = document.getElementById('category').value;

    if (!startDate || !endDate || !categoryId) {
        alert("Please select a category and both start and end dates.");
        return;
    }

    const url = `https://gobblecube-api-dashboard.onrender.com/sales_by_category?start_date=${startDate}&end_date=${endDate}&category_id=${categoryId}`;
    const resultContainer = document.getElementById('sales_by_category_result');

    try {
        resultContainer.textContent = "Loading...";
        const response = await fetch(url);

        if (!response.ok) {
            throw new Error(`Error: ${response.status} ${response.statusText}`);
        }

        const data = await response.json();
        resultContainer.textContent = JSON.stringify(data, null, 2);
    } catch (error) {
        console.error("Error:", error);
        resultContainer.textContent = "An error occurred. Please check the console for details.";
    }
}

// Function to get market share changes
async function getMarketShareChanges() {
    const startDate = document.getElementById('start_date').value;
    const endDate = document.getElementById('end_date').value;

    if (!startDate || !endDate) {
        alert("Please select both start and end dates.");
        return;
    }

    const url = `https://gobblecube-api-dashboard.onrender.com/market_share_changes?start_date=${startDate}&end_date=${endDate}`;
    const resultContainer = document.getElementById('market_share_changes_result');

    try {
        resultContainer.textContent = "Loading...";
        const response = await fetch(url);

        if (!response.ok) {
            throw new Error(`Error: ${response.status} ${response.statusText}`);
        }

        const data = await response.json();
        resultContainer.textContent = JSON.stringify(data, null, 2);
    } catch (error) {
        console.error("Error:", error);
        resultContainer.textContent = "An error occurred. Please check the console for details.";
    }
}

// Fetch categories when the page loads
window.onload = fetchCategories;
