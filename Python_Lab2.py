import math

name = "Dylan McGuffey"
age = 32
height = 6.2
favorite_color = "Green"

print(name)
print(age)
print(height)
print(favorite_color)

print(name, age, height, favorite_color)

print(f"""Hello there, my name is {name}, and my favorite color is {favorite_color}. I'm {age} years old and about {height} feet tall.""")

print(f"""
Name:{name}
Age:{age}
""")

Radius = 5
Circle_Area = ((math.pi*Radius)**2)

print(f"The Area of the Circle is {Circle_Area:.1f} units.")

print(f"The square root of my age is {math.sqrt(age)}")

print(f"The sine and cosine of my height are {math.sin(height)} and {math.cos(height)} respectively.")

print(f"""{age+5}
{age+height}
{height+4}
{height/2}
{age/3:.1f}
{age**2}
""")

def convert_temp(f):
    return (f-32)*(5/9)



t = input("What's the temperature in Celsius?:")
t = int(t)
print(f"I guess it's about {convert_temp(t):.2f} degrees celsius.")


