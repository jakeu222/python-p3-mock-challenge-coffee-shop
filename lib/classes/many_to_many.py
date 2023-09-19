class Coffee:
    def __init__(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self.name = name
        else:
            raise ValueError("Not valid name")

    def get_name(self):
        return self._name

    def set_name(self, value):
        if not hasattr(self, "name") and isinstance(value, str) and len(value) >= 3:
            self._name = value
        else:
            raise ValueError("Not valid name")

    name = property(get_name, set_name)

    def orders(self):
        r_list = []
        for order in Order.all:
            if isinstance(order, Order) and order.coffee is self:
                r_list.append(order)
        return r_list

    def customers(self):
        r_list = []
        for order in Order.all:
            if order.coffee is self and isinstance(order.customer, Customer) and order.customer not in r_list:
                r_list.append(order.customer)
        return r_list

    def num_orders(self):
        count = 0
        for order in Order.all:
            if order.coffee is self:
                count += 1
        return count

    def average_price(self):
        count = 0
        sum = 0
        for order in Order.all:
            if order.coffee is self:
                count += 1
                sum += order.price
        if count == 0:
            return 0
        return sum / count


class Customer:
    def __init__(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self.name = name
        else:
            raise ValueError("Not valid name")

    def get_name(self):
        return self._name

    def set_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Not valid name")

    name = property(get_name, set_name)

    def orders(self):
        r_list = []
        for order in Order.all:
            if isinstance(order, Order) and order.customer is self:
                r_list.append(order)
        return r_list

    def coffees(self):
        r_list = []
        for order in Order.all:
            if order.customer is self and isinstance(order.coffee, Coffee) and order.coffee not in r_list:
                r_list.append(order.coffee)
        return r_list

    def create_order(self, coffee, price):
        return Order(self, coffee, price)


class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    def get_price(self):
        return self._price

    def set_price(self, value):
        if isinstance(value, float) and 1.0 <= value <= 10.0 and not hasattr(self, "price"):
            self._price = value
        else:
            raise ValueError("Not valid price")

    price = property(get_price, set_price)

    def get_customer(self):
        return self._customer

    def set_customer(self, value):
        if isinstance(value, Customer):
            self._customer = value
        else:
            raise ValueError("Not valid customer")

    customer = property(get_customer, set_customer)

    def get_coffee(self):
        return self._coffee

    def set_coffee(self, value):
        if isinstance(value, Coffee):
            self._coffee = value
        else:
            raise ValueError("Not valid coffee")

    coffee = property(get_coffee, set_coffee)





# class Coffee:
#     def __init__(self, name):
#         # if type(name) is str and 3<=len(name):
#         self.name = name
    
#     def get_name(self):
#         return self._name
#     def set_name(self,value):
#         if not hasattr(self,"name") and type(value) is str and 3<=len(value):
#             self._name = value
#         else:
#             raise ValueError("Not valid name")
#     name = property(get_name,set_name)
    
#     def orders(self):
#         r_list = []
#         for order in Order.all:
#             if type(order) is Order and order.coffee is self:
#                 r_list.append(order)
#         return r_list
    
#     def customers(self):
#         r_list = []
#         for order in Order.all:
#             if order.coffee is self and type(order.customer) is Customer and order.customer not in r_list:
#                 r_list.append(order.customer)
#         return r_list
    
#     def num_orders(self):
#         count = 0
#         for order in Order.all:
#             if order.coffee is self:
#                 count += 1
#         return count
    
#     def average_price(self):
#         count = 0
#         sum = 0
#         for order in Order.all:
#             if order.coffee is self:
#                 count += 1
#                 sum += order.price
#         if count == 0:
#             return 0
#         return sum/count

# class Customer:
#     def __init__(self, name):
#         self.name = name
    
#     def get_name(self):
#         return self._name
#     def set_name(self,value):
#         if type(value) is str and 1<=len(value)<=15:
#             self._name = value
#         else:
#             raise ValueError("Not valid name")
#     name = property(get_name,set_name)

#     def orders(self):
#         r_list = []
#         for order in Order.all:
#             if type(order) is Order and order.customer is self:
#                 r_list.append(order)
#         return r_list
    
#     def coffees(self):
#         r_list = []
#         for order in Order.all:
#             if order.customer is self and type(order.coffee) is Coffee and order.coffee not in r_list:
#                 r_list.append(order.coffee)
#         return r_list
    
#     def create_order(self, coffee, price):
#         return Order(self,coffee,price)
    
# class Order:
#     all = []
#     def __init__(self, customer, coffee, price):
#         self.customer = customer
#         self.coffee = coffee
#         self.price = price
#         Order.all.append(self)

#     def get_price(self):
#         return self._price
#     def set_price(self,value):
#         if isinstance(value,float) and 1.0<=value<=10.0 and not hasattr(self,"price"):
#             self._price=value
#         else:
#             raise ValueError("Not valid price")
#     price = property(get_price,set_price)

#     def get_customer(self):
#         return self._customer
#     def set_customer(self, value):
#         if type(value) is Customer:
#             self._customer = value
#         else:
#             raise ValueError("Not valid customer")
#     customer = property(get_customer,set_customer)

#     def get_coffee(self):
#         return self._coffee
#     def set_coffee(self, value):
#         if type(value) is Coffee:
#             self._coffee = value
#         else:
#             raise ValueError("Not valid coffee")
#     coffee = property(get_coffee,set_coffee)

    


# # class Coffee:
    
# #     def __init__(self, name):
# #         self.name = name

# #     def get_name(self):
# #         return self._name
    
# #     def set_name(self, name):
# #         if isinstance(name, str) and not hasattr(self, "name") and 3 <= len(name):
# #             self._name = name
# #         else:
# #             print("Python sucks!")

# #     name = property(get_name, set_name)
        
# #     def orders(self):
# #         pass
    
# #     def customers(self):
# #         pass
    
# #     def num_orders(self):
# #         pass
    
# #     def average_price(self):
# #         pass

# # class Customer:
# #     def __init__(self, name):
# #         self.name = name

# #     def get_name(self):
# #         return self._name
    
# #     def set_name(self, name):
# #         if isinstance(name, str) and 1 <= len(name) and len(name)<= 15:
# #             self._name = name
# #         else:
# #             print("Python sucks!")

# #     name = property(get_name, set_name)

    
        
# #     def orders(self):
# #         pass
    
# #     def coffees(self):
# #         pass
    
# #     def create_order(self, coffee, price):
# #         pass
    
# # class Order:
# #     all = []

# #     def __init__(self, customer, coffee, price):
# #         self.customer = customer
# #         self.coffee = coffee
# #         self.price = price
# #         type(self).all.append(self)

# #     def get_price(self):
# #         return self._price
    
# #     def set_price(self, price):
# #         if isinstance(price, float) and not hasattr(self, "price") and 1.0 <= price and price <= 10.0 :
# #             self._price = price 
# #         else:
# #             print("Setting price invalid")

# #     price = property(get_price, set_price)

# #     def get_customer(self):
# #         return self._customer
    
# #     def set_customer(self, customer):
# #         if isinstance(customer, Customer):
# #             self._customer = customer
# #         else:
# #             print("Setting")

# #     customer = property(get_customer, set_customer)

# #     def get_coffee(self):
# #         return self._coffee
    
# #     def set_coffee(self, coffee):
# #         if isinstance(coffee, Coffee):
# #             self._coffee = coffee
# #         else:
# #             print("Setting")

# #     coffee = property(get_coffee, set_coffee)

