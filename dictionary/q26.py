#How do you use a dictionary to simulate a switch-case statement?
def gold_member():
    return "Gold Member: 20% discount applied"

def silver_member():
    return "Silver Member: 10% discount applied"

def bronze_member():
    return "Bronze Member: 5% discount applied"

def no_membership():
    return "No membership: No discount applied"

membership_discounts = {
    "gold": gold_member,
    "silver": silver_member,
    "bronze": bronze_member
}

membership_type = input("enter type of membership")
discount_message = membership_discounts.get(membership_type, no_membership)()
print(discount_message)  