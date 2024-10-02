def main():
    item = get_nutrition_facts(get_input("Item: "))
    if item:
        print(f"Calories: {item}")


def get_nutrition_facts(item):
    items = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80,
    }
    return items.get(item, None)


def get_input(string):
    return input(string)


if __name__ == "__main__":
    main()
