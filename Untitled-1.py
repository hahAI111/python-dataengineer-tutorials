# *args - 接收任意数量的位置参数（元组）
def sum_all(*args):
    return sum(args)

sum_all(1, 2, 3)      # 6
print(sum_all(1, 2, 3, 4, 5))  # 15

# **kwargs - 接收任意数量的关键字参数（字典）
def create_user(**kwargs):
    return (kwargs)

print(create_user(name="Alice", age=30, city="Berlin"))
# {'name': 'Alice', 'age': 30, 'city': 'Berlin'}
print(create_user(name="Alice", city="Berlin"))
