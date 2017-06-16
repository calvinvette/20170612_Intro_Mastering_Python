from functools import wraps

def my_logging_wrapper(the_func):
    @wraps(the_func)
    def wrapped(*args, **kwargs):
        print('log start time')
        # print(*args)
        # print(**kwargs)
        # if args[0] == 1234:
        #     cust = 9999
        # else:
        #     cust = args[0]
        # if len(args) == 2:
        #     orderId = args[1]
        #     ret = the_func((orderId, cust), **kwargs)
        # else:
        #     ret = the_func(cust, **kwargs)
        ret = the_func(*args, **kwargs)
        print('log end time')
        return ret
    return wrapped

@my_logging_wrapper
def my_business_logic_funct(customer_id):
    print("Customer Lookup for: %d" % customer_id)

@my_logging_wrapper
def other_BL(order_id, customer_id):
    print("Order Lookup for %d for Customer %d" % (order_id, customer_id))

@my_logging_wrapper
def more_BL():
    print("More Busines Logic")

if __name__ == '__main__':
    my_business_logic_funct(1234)
    my_business_logic_funct(1662)
    other_BL(9331, 1234)
    other_BL(7311, 1234)
    more_BL()

