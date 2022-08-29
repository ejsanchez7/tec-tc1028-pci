def hipotenusa(cat_a, cat_b) :
    hipo = ((cat_a ** 2) + (cat_b ** 2)) ** 0.5
    return hipo

cat_a = float(input("Escribe el valor del cateto A: "))
cat_b = float(input("Escribe el valor del cateto B: "))

print(f"La hipotenusa es {hipotenusa(cat_a, cat_b)}")