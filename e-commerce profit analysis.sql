--The Pulse Check: Order Status Breakdown
SELECT 
order_status, 
COUNT(order_id) AS total_orders
FROM 
olist_orders_dataset
GROUP BY 
order_status
ORDER BY 
total_orders DESC;

--The Customer Map: Where are they located?
SELECT 
customer_state, 
COUNT(customer_id) AS total_customers
FROM 
olist_customers_dataset
GROUP BY 
customer_state
ORDER BY 
total_customers DESC
LIMIT 5;

--The Quick Scan: Top 10 Most Expensive Products
SELECT 
product_id, 
price
FROM 
olist_order_items_dataset
ORDER BY 
price DESC
LIMIT 10;

--The Category Check: Distinct Product Categories
SELECT DISTINCT 
product_category_name_english AS category_name
FROM 
product_category_name_translation
ORDER BY 
category_name ASC;

--The Cash Flow Check: Most Popular Payment Methods
SELECT 
    payment_type, 
    COUNT(order_id) AS total_transactions,
    ROUND(SUM(payment_value), 2) AS total_revenue_generated
FROM 
    olist_order_payments_dataset
GROUP BY 
    payment_type
ORDER BY 
    total_transactions DESC;