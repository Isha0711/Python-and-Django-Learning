#30. How do you handle mutable objects as dictionary keys, and what problems can it cause?
#If you use a mutable object (like a list) as a key and then modify that object,
#  the dictionary will behave unpredictably because the hash value of the key 
# will change. This can make it impossible to retrieve the value associated with
#  that key.


#Python dictionaries rely on hash values to manage keys. Mutable objects do not have a stable hash value.
#  When you try to add a mutable object as a key,
#  Python will raise a TypeError.

# Attempt to use a list as a key (which will raise an error)
try:
    my_dict = {
        ["key1", "key2"]: "value"
    }
except TypeError as e:
    print("Error:", e)  # Output: "Error: unhashable type: 'list'"