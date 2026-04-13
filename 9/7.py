import numpy as np

sales_data = np.array([
    [150, 80, 100],  # Январь
    [200, 120, 150], # Февраль
    [180, 90, 110]   # Март
])

months = ["Январь", "Февраль", "Март"]
categories = ["Футболки", "Штаны", "Платья"]

monthly_totals = sales_data.sum(axis=1)
best_month_idx = np.argmax(monthly_totals)
print(f"Месяц с наибольшими продажами: {months[best_month_idx]}")

category_totals = sales_data.sum(axis=0)
best_cat_idx = np.argmax(category_totals)
print(f"Категория с наибольшими продажами: {categories[best_cat_idx]}")

mean_sales = np.mean(sales_data, axis=0).round(2)
print(f"Среднее количество продаж: {mean_sales}")

tshirt_sales = sales_data[:, 0]
print(f"Массив продаж футболок: {tshirt_sales}")

best_tshirt_month_idx = np.argmax(tshirt_sales)
print(f"Месяц с наибольшими продажами футболок: {months[best_tshirt_month_idx]}")