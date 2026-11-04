products = [
    {
        "id": 1,
        "name": "Laptop",
        "category": "Electronics",
        "price": 25000000,
        "stock": 8,
        "sales": [2, 3, 1]
    },
    {
        "id": 2,
        "name": "Mouse",
        "category": "Accessories",
        "price": 500000,
        "stock": 20,
        "sales": [5, 8, 6]
    },
    {
        "id": 3,
        "name": "Keyboard",
        "category": "Accessories",
        "price": 1200000,
        "stock": 4,
        "sales": [3, 2, 4]
    },
    {
        "id": 4,
        "name": "Monitor",
        "category": "Electronics",
        "price": 8000000,
        "stock": 6,
        "sales": [1, 2, 3]
    }
]

for product in products:
    total_sales = 0
    for sale in product["sales"]:
        total_sales += sale
    product["3-month-sales"] = total_sales
    print("Product total sale :", product["name"], product["3-month-sales"])

def calculate_revenue(total_sales, price):
    return total_sales * price
for product in products:
    product["revenue"] = calculate_revenue(product["3-month-sales"], product["price"])
    print("Product revenue :", product["name"], product["revenue"])

ranked_products_by_revenue = sorted(
    products,
    key=lambda product: product["revenue"],
    reverse=True
)

def find_low_stock_products(products):
    low_stuck_products = []
    for product in products:
        if product["stock"] < 5:
            low_stuck_products.append(product["name"])
    return low_stuck_products
low_stuck_products = find_low_stock_products(products)
print(low_stuck_products)

def group_products_by_category(products):
    products_category = {}
    for product in products:
        category = product["category"]
        if category not in products_category:
            products_category[category] = []
        products_category[category].append(product["name"])
    return products_category
products_category = group_products_by_category(products)
print(products_category)

def total_store_revenue(products):
    total_revenue = 0
    for product in products:
        total_revenue += product["revenue"]
    return total_revenue
def count_product(products):
    return len(products)

def search_product(products):
    searched_product = input("Enter product : ")
    for product in products:
        if searched_product.lower() == product["name"].lower():
            return product
    return None
result = search_product(products)
print(result)
