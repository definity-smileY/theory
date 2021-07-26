import pay_module_base

# 변수 사용
print(pay_module_base.version)

# 함수 사용
pay_module_base.printAuthor()

# 클래스 사용
pay_info = pay_module_base.Pay("A102030", 13000, "2021-07-26")
print(pay_info.get_pay_info())

print(pay_module_base.__name__)