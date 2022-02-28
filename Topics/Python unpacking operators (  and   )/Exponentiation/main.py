info = input().split(', ')
# your code here
name, age, city, *miscellaneous = info
print(f"name: {name}\nage: {age}\ncity: {city}\nmiscellaneous: {' '.join(miscellaneous)}")

