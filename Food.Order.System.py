italian_food= ["Pasta Bolognese", "Pepperoni pizza", "Margherita pizza", "Lasagna"]

indian_food = ["Curry","Chutney","Samosa","Naan"]

def find_meal(name, menu):
  return name if name in menu else None

def select_meal(name, food_type):
  if food_type == "Italian":
    return find_meal(name, italian_food)
  elif food_type == "Indian":
    return find_meal(name, indian_food)
  else:
    return None

    

def display_available_meals(food_type):
  if food_type == "Italian":
    print(f"Available Italian Meals: {italian_food}") 
  elif food_type == "Indian":
    print(f"Available Indian Meals: {indian_food}")
  else:
    print("Invalid food type")
  

def create_summary(name, amount, food_type):
  order= select_meal(name, food_type)
  if order:
    return f"You ordered {amount} {name} {food_type}"
  else:
    return "Meal not found"

print("Welcome to the Food Order System!")
type_input= input("What type of food would you like? Indian or Italian?")
display_available_meals(type_input)

name_input= input("What would you like to order?")
amount_input= input("How many would you like?")

create_summary(name_input, amount_input, type_input)

result= create_summary(name_input, amount_input, type_input)
print(result)
