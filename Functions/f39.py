# Write a function describe_person(name, **kwargs) where name is a  required argument, and other details like age, job, and city are optional keyword arguments. 
def describe_person(name, **kwargs):
    print(f"Name: {name}")
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")