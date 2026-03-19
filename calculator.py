class calculator:

    def add(self,a,b):
        c=a+b
        return c

    def sub(self,a,b):
        c=a-b
        return c


    def mul(self,a,b):
        c=a*b
        return c


    def div(self,a,b):
        c=a/b
        return c

c=calculator()
print("addition of two number",c.add(2,2))
print(c.sub(2,2))

print(c.mul(2,2))
print(c.div(2,2))


# def happybirthday(name,age):

#     print(f"Happy birthday{name}1 ")
#     print(f"You are {age}")
#     print(f"Happy birthday {name}3")
#     print()

# happybirthday("Ajit",20)
# happybirthday("Arun",21)   
# happybirthday("Abinav",24)         