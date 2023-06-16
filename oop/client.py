from tech import Tech
from mobile import Mobile
from laptop import Laptop
from salesPerson import SalesPerson
from datetime import date


phone_1 =Mobile('iphone_11',60000, 500,'Black','1920-1080',10)
phone_2 =Mobile('iphone_12',70000, 550,'Silver','1920-1080',12)
phone_3 =Mobile('iphone_11',80000, 580,'Project Red','1920-1080',13)

laptop_1 = Laptop('Asus g14', 130000, 1.6, 'Moonlight Silver',16, 'Ryzen 480',1000)
laptop_2 = Laptop('Mackbook Pro 13', 130000, 1.7, 'Dark Grey',8, 'Intel Core',520)
laptop_3 = Laptop('Dell XPS 13', 140000, 1.4, 'White',16, 'Intel Core I7',520)

# Test method 

# print(phone_1)
# print(laptop_3)

# Apling the discount 

# phone_1.apply_discount()
# print(phone_1)

# Total Number of Products
# print(Tech.get_total_products())

# Shipping Cost 
# print(laptop_2.calculate_shiping_cost(10))

# Setting the double price for the 1st laptop 
# print(laptop_1.price)
# laptop_1.set_double_price()
# print(laptop_1.price)

# Canging specs for laptop3
# print(laptop_3)
# laptop_3.change_specs(32,1000)
# print(laptop_3)

sales_person_1 = SalesPerson(
    'Ariful',
    'Islam',
    40000,
    date(2020,1,5)
)

# Adding the products
sales_person_1.sell_product(phone_1)
sales_person_1.sell_product(phone_2)
sales_person_1.sell_product(laptop_3)

# Total products sold
print(sales_person_1.total_products_sold())

#  products sold
sales_person_1.display_seles()

# Calculate Commission 
print(sales_person_1.calculate_commission(0.2))

# sort the sold products by price 
sales_person_1.sort_by_price()
sales_person_1.display_seles()