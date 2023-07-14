weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')

if unit.upper() == "K":
    converted = weight * 0.45
    print(converted)

elif unit.upper() == "L":
    converted = weight / 0.45
    print(converted)
