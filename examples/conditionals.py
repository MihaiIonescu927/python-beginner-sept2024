name = "Felix"
is_cat = False

if is_cat is True:
    print(f"{name} is a cat.")

print("Bye from cat world!")

x, y = 10, 20

if x > 5:
    if y > 15:
        print("Both x and y are greater than their respective thresholds.")
        print("Still under if y > 15")
    else:
        print("x is greater than 5, but y is not greater than 15.")
else:
    print("x is not greater than 5.")