letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Harry"

print(letter.format(country, name)) # previous
print(f"Hey my name is {name} and I am from {country}")
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")
price = 49.09999
txt = f"For only {price:.2f} dollars!"   # :.2f means decimal upto 2 
print(txt)
# print(txt.format())
print(type(f"{2 * 30}"))


txt2="asdsjfhsjfh{}jdsehfjsfh"
print(txt2.format(2137))


s=str(input())
n=int(input())
print("Hi my name is",s,"and my age is",n)
print(f"Hi my name is {s} and my age is {n}.")

print(f"{n * 10}")  # internally operation will be done as int/float but result will be string ( check type())