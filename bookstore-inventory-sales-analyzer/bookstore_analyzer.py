books = [
    {
        "id": 1,
        "title": "Python Basics",
        "author": "John Smith",
        "genre": "Programming",
        "price": 450000,
        "stock": 12,
        "monthly_sales": [5, 8, 6]
    },
    {
        "id": 2,
        "title": "Linux Essentials",
        "author": "David Miller",
        "genre": "Technology",
        "price": 380000,
        "stock": 4,
        "monthly_sales": [7, 9, 8]
    },
    {
        "id": 3,
        "title": "Clean Code",
        "author": "Robert Martin",
        "genre": "Programming",
        "price": 620000,
        "stock": 8,
        "monthly_sales": [10, 12, 9]
    },
    {
        "id": 4,
        "title": "Atomic Habits",
        "author": "James Clear",
        "genre": "Psychology",
        "price": 520000,
        "stock": 15,
        "monthly_sales": [8, 6, 11]
    },
    {
        "id": 5,
        "title": "Computer Networks",
        "author": "Andrew Tanenbaum",
        "genre": "Technology",
        "price": 750000,
        "stock": 3,
        "monthly_sales": [4, 6, 5]
    },
    {
        "id": 6,
        "title": "Deep Work",
        "author": "Cal Newport",
        "genre": "Psychology",
        "price": 490000,
        "stock": 10,
        "monthly_sales": [6, 8, 7]
    }
]
for book in books:
    total_sales = 0
    for monthly_sale in book["monthly_sales"]:
        total_sales += monthly_sale
    book["total_sales"] = total_sales

for book in books:
    book["total_revenue"] = book["total_sales"] * book["price"]

unique_genres = {book["genre"] for book in books}

ranked_books_by_total_revenue = sorted(
    books,
    key=lambda book : book["total_revenue"],
    reverse=True
)
total_stock = 0
total_revenue_all = 0 
total_sales_all = 0
for book in books:
    total_stock += book["stock"]
    total_sales_all += book["total_sales"]
    total_revenue_all += book["total_revenue"]

print("Books count :", len(books))
print("Genres count :", len(unique_genres))
print(f"Total stock : {total_stock}")
print(f"Total sales : {total_sales_all}")
print(f"Total revenue : {total_revenue_all}")
ranked_books_by_total_sales = sorted(
    books,
    key=lambda book: book["total_sales"],
    reverse=True
)
print("Best-selling book :", ranked_books_by_total_sales[0]["title"])
print("Top 3 Books by Revenue :")
for index, book in enumerate(ranked_books_by_total_revenue):
    print(index+1, ".", book["title"], "-", book["total_revenue"])
    if index > 1:
        break
low_stock_books_info = [book for book in books if book["stock"] < 6]
print("Low Stock Books :")
for book in low_stock_books_info:
    print(book["title"], ":", book["stock"])
print("Available Genres :")
for genre in sorted(unique_genres):
    print(genre)
