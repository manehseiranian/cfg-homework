"""

TASK 1

Write a class to represent a Cash Register.
Your class should keep the state of price total and purchased items

Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.

"""



class CashRegister:

    def __init__(self):
        self.total_items = dict()
        self.total_price = 0
        self.discount = 0

    def add_item(self, item, price):
        self.total_items[item] = price
        return self.total_items

    def remove_item(self, item):
        self.total_items.pop(item)
        return self.total_items

    def apply_discount(self, item, discount_applicable, discount):
        if discount_applicable:
            discounted_price = self.total_items[item]*(1-discount/100)
            print(f"{item}: £{'%.2f' % round(discounted_price,2)}")
            self.total_items[item] = discounted_price
        else:
            print(f"{item}: £{'%.2f' % round(self.total_items[item],2)}")


    def get_total(self):
        print(f"The total cost is £{'%.2f' % round(sum(self.total_items.values()),2)}")


    def show_items(self):
        print(f"The following items are about to be purchased:")
        for item in self.total_items:
            print(item)

    def reset_register(self):
        self.total_items.clear()


# EXAMPLE code run:

list_of_items = CashRegister()

# Adding items to the cash register:

list_of_items.add_item('parmesan', 1.40)
list_of_items.add_item('burrata', 3.15)
list_of_items.add_item('grapes', 2.20)
list_of_items.add_item('crackers', 1.60)

# Removing an example item from the cash register:
list_of_items.remove_item('grapes')

# Applying a discount to discounted items:

list_of_items.apply_discount('parmesan', True, 50)
list_of_items.apply_discount('burrata', True, 30)
list_of_items.apply_discount('crackers', False, None)

# Showing the total cost of the purchase:
list_of_items.get_total()

# Viewing all the items in teh cash register:
list_of_items.show_items()


# removing all the items from the cash register:
list_of_items.reset_register()

list_of_items.show_items() # the view function is used once again to show that all the items have been deleted from the list
