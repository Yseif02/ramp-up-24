# Create a function that takes two arguments: 
# the original price and the discount percentage as integers 
# and returns the final price after the discount.
def calculate_final_price(price, discount):
    discount_amount = price * (discount / 100)
    final_price = price - discount_amount
    return final_price

