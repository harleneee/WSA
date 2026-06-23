
layers = 5

for i in range(1, layers + 1):
    spaces = " " * (layers - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)


