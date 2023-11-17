fruit = input("Фрукт: ").lower()
fruits = {"apple": 130, "avocado": 50, "banana": 110, "cantaloupe": 50,
           "grapes": 90, "honeydew melon": 50, "kivifruit": 90, "lemon": 15, "lime": 20,
          "nectarine": 60, "orange": 80, "peach": 60, "pear": 100, "pineapple": 50, "plums": 70,
          "strawberries": 50, "sweetcheries": 100, "tanherine": 50, "watermelon": 80}
if fruit in fruits:
    print(f"Калории: {fruits[fruit]}")