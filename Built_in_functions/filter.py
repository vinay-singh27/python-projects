def even_check(num):
    if num%2 ==0:
        return True

lst =range(20)

print(list(filter(even_check,lst)))