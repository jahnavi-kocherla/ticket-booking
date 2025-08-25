print("Welcome to your digital recipe book!")
Recipes = ["1.Pasta Carbonara","2.Classic Caesar Salad","3. Simple Fruit Smoothie"]
Ingridents = [["Spagetti", "eggs","bacon","parmesan cheese"],["lettuce","croutons","parmesan cheese","caesar dressing"],["banana","spinach","milk","honey"]]
print("Here are your recipes:")
print("f\nPlease choose an option:")
print("1. Look up a recipe's ingredients")
print("2.Find recipes by a main ingredient")
choice=input("Enter your choice:")
if choice == "1":
    print("Here are your recipes:")
    print(Recipes)
    recipe_choice = input("Enter the recipe number:")
    if recipe_choice == "1":
        print("Here are the ingredients for Pasta Carbonara:")
        print(Ingridents[0])
    elif recipe_choice == "2":
        print("Here are the ingredients for Classic Caesar Salad:")
        print(Ingridents[1])
    elif recipe_choice == "3":
        print("Here are the ingredients for Simple Fruit Smoothie:")
        print(Ingridents[2])
    else:
        print("Invalid choice. Please try again.")
elif choice == "2":
    ingredient_choice = input("Enter the main ingredient:".lower())
    found = False
    for i in range(len(Recipes)):
        if ingredient_choice in Ingridents[i]:
            print("Here is a recipe that includes", ingredient_choice, ":")
            print(Recipes[i])
            found = True
      

