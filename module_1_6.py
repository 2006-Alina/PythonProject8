my_dict = {"Galina": 1973, "Alina": 2005,"Vera":1953}
print(my_dict)
print(my_dict["Galina"])
print(my_dict.get("Marusya"))
my_dict.update({"Roza": 1998,"Dima": 2004})
print(my_dict)
del my_dict["Galina"]
print(my_dict)

my_set = {1973,13,5,6,"German","Ivan"}
print(my_set)
my_set.add(53)
my_set.add("Tanya")
my_set.discard(1973)
print(my_set)


