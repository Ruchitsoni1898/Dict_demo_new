capitals = {"USA": "Washington DC", "France": "Paris", "Turkey": "Ankara"}
print(type(capitals))

#getting items from the dictionary
france_capitals = capitals["France"]
print(france_capitals)

France_capital2 = capitals.get("France")
print(France_capital2)

Us_capitals = capitals["USA"]
print(Us_capitals)

# adding item to the dictionary
capitals = {"USA": "Washington DC", "France": "Paris", "Turkey": "Ankara"}
print("before add")
print(capitals)
capitals["India"]= "New delhi"
print("after add")
print(capitals)

#option 2
capitals.update({"Germany":"Berlin"})
print("add option")
print(capitals)

capitals = {"USA": "Washington DC", "France": "Paris", "Turkey": "Ankara"}
all_keys = capitals.keys()
all_values = capitals.values()
print(all_keys)
print(all_values)

# Another example of a dictionary
employee = {"name": "Ruchit Soni",
            "age": 25,
            "phone": 15101111111,
            "title": "Software Engineer",
            "skills": ["HTML", "Python", "CSS", "PHP"]
            }

e_name = employee['name']
e_age = employee['age']
e_skills = employee['skills']
print(type(e_skills))
user_skill_count = len(e_skills)
print(f"User has {user_skill_count} skills.")
print("User has {} skills".format(user_skill_count))
