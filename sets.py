set1 = {"James", "Jack", "James"}
print(set1)
set_2 = {"fa", "ya"}

set1 = {"James", "Jack", "James", False, 0, 1}
print(set1)

# updating
set1.update(set_2)
print(set1)

# Dictionaries
# they are ordered, duplicates not allowed
data1 = {
    "name": "Abbie",
    "year": 2003,
    "gender": "female",
    "date": "12-34-4576"}
print(data1)
data1.update({"color": "black"})
print(data1)
data1.pop("gender")
print(data1)