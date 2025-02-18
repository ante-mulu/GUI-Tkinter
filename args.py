# def add(*args):
#     print(args)
#     sum=0
#     for i in args:
#         sum+=i
#     return sum
# sum=add(2,4,6,8,8,10)
# print(sum)
# **kwargs
# def calculator(n,**kwargs):
#     n+=kwargs["a"]
#     n*=kwargs["d"]
#     print(n)
# calculator(5,a=3,d=2)
class Car:
    def __init__(self,**kw):
        self.make=kw.get("make")
        self.model=kw.get("model")
