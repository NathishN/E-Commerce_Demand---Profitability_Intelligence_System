import pandas as pd

# --- STEP 1: LOAD THE 4 KEY TABLES ---
# Update this path to your actual folder path
path = "" 

# 1. Orders (Time & Status)
orders = pd.read_csv(path + r"C:\Users\nathi\Downloads\Desktop\Data Analyst\Ecommerce Project 1\Ollist E-Commerce Dataset\olist_orders.csv")

# 2. Items (Price & Quantity) - This is the "Main" table for sales
items = pd.read_csv(path + r"C:\Users\nathi\Downloads\Desktop\Data Analyst\Ecommerce Project 1\Ollist E-Commerce Dataset\olist_order_items.csv")

# 3. Products (Category Names)
products = pd.read_csv(path + r"C:\Users\nathi\Downloads\Desktop\Data Analyst\Ecommerce Project 1\Ollist E-Commerce Dataset\olist_products.csv")

# 4. Translations (Portuguese to English)
translations = pd.read_csv(path + r"C:\Users\nathi\Downloads\Desktop\Data Analyst\Ecommerce Project 1\Ollist E-Commerce Dataset\product_category_name_translation.csv")

print("Files Loaded Successfully!")

# --- STEP 2: MERGE THE DATA (The "Senior" Skill) ---

# Merge 1: Connect Items to Orders (to get Dates)
# We use an 'inner' join because we only want items that have a valid order.
main_df = pd.merge(items, orders, on='order_id', how='inner')

# Merge 2: Connect Products to get Category Names
main_df = pd.merge(main_df, products, on='product_id', how='left')

# Merge 3: Translate Category Names to English
# The dataset has categories in Portuguese (e.g., 'beleza_saude'). We switch them to English.
main_df = pd.merge(main_df, translations, on='product_category_name', how='left')

# --- STEP 3: CLEAN UP ---
# Rename the English column to just 'Category' for easier use
main_df.rename(columns={'product_category_name_english': 'Category'}, inplace=True)

# Filter: We only want "delivered" orders for accurate sales analysis
main_df = main_df[main_df['order_status'] == 'delivered']

# Create a Total Value column
main_df['Total_Value'] = main_df['price'] + main_df['freight_value']

print(f"Final Dataset Shape: {main_df.shape}")
print("Sample Data:")
print(main_df[['order_purchase_timestamp', 'Category', 'price', 'Total_Value']].head())

# --- CRITICAL NOTE FOR PROFITABILITY ---
# The Olist dataset has 'Price' (Revenue) but NOT 'Cost'.
# To do a "Profitability" analysis, we must simulate a Cost.
# Assumption: Let's assume a 25% Profit Margin on all goods to demonstrate your logic.
main_df['Estimated_Cost'] = main_df['price'] * 0.75
main_df['Estimated_Profit'] = main_df['price'] - main_df['Estimated_Cost']

print("Master Data Created with Estimated Profit!")

# Save the master dataset as a CSV file
output_csv_path = r"C:\Users\nathi\Downloads\Desktop\Data Analyst\Ecommerce Project 1\Ollist E-Commerce Dataset\master_dataset.csv"
main_df.to_csv(output_csv_path, index=False)
print(f"Master dataset saved to: {output_csv_path}")