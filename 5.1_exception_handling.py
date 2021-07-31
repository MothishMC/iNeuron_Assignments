def div(a, b):
    try:
        c = a / b
    except:
        print("You are trying to divide a number with zero!!!")
        c = "Not possible!"
    finally:
        return c


print(div(1, 2))
print(div(5, 5))
print(div(5, 0))
