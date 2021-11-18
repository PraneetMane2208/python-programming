# n! = 1*2*3*4*5. . . *n
# n! = n*(n-1)!
# n=5
# product =1
# for i in range(n):
#     product = product * (i+1)
# print(product)

# n=5
# def factorial_iter(n):
#     product=1
#     for i in range(n):
#         product=product * (i+1)
#     return product
# f= factorial_iter(5)
# print(f)


# def factorial_recursive(n):
#     if n==1 or n==0:
#         return 1
#     return n * factorial_recursive(n-1)
# f= factorial_recursive(6)
# print(f)


def sum_recursive(n):
    if n==1:
        return 1
    return n + sum_recursive(n-1)
s = sum_recursive(8)
print(s)
