# mortgage.py
#
# Exercise 1.7
# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

month = 0
extra_payment = 1000.0
extra_payment_months = 12

while principal > 0:
    month = month + 1

    # Bước 1: Tính lãi
    interest = principal * (rate / 12)
    principal = principal + interest

    # Bước 2: Xác định số tiền trả
    if month <= extra_payment_months:
        current_pay = payment + extra_payment
    else:
        current_pay = payment

    # Bước 3: Xử lý tháng cuối
    if principal < current_pay:
        current_pay = principal

    # Bước 4: Trừ nợ và cộng dồn tiền đã trả
    principal = principal - current_pay
    total_paid = total_paid + current_pay

# In kết quả với 2 chữ số thập phân
print('Total paid:', round(total_paid, 2))
print('Months:', month)