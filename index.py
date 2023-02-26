import os


def func_clear_console():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def func_center(pm_string, pm_separator):
    string_center = pm_string.center(45, pm_separator)
    print(f"|{string_center}|")


def string_header(*args):
    func_center("=", "=")
    for i in args:
        func_center(i, " ")
    func_center("=", "=")


def possible_choices(pm_list, pm_exit):
    choice = input("|  Introduzca la alternativa a elegir: ").strip().lower()
    while choice not in pm_list:
        choice = (
            input("Incorrecto. Introduzca una alternativa entre las opciones: ")
            .strip()
            .lower()
        )

    if choice == pm_exit:
        func_clear_console()
        print("Terminando...")
        print("Programa terminado")
        exit()

    return choice


def print_choices(pm_choices):
    initial = 0
    for item in pm_choices:
        if isinstance(item, dict):
            print(
                f"|  {letters[initial].upper()}  |  {item['price']} $  |  {item['name'].capitalize()}"
            )
            initial += 1
        else:
            print(f"|  {letters[initial].upper()}  |  {item.capitalize()}")
            initial += 1
    print(f"|  {letters[initial].upper()}  |  Exit")


# * Welcome
string_restaurant = "RESTAURANTE S.A."
string_menu = "MENÚ"

# * Choices
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"]

# * Meals + Foods
list_general = [
    {
        "name": "desayuno",
        "item": 1,
        "food": [
            {"name": "café", "price": 4.50},
            {"name": "chocolate", "price": 5.00},
            {"name": "jugo de fresas", "price": 9.00},
            {"name": "jugo de papaya", "price": 8.00},
            {"name": "pan con pollo", "price": 7.00},
            {"name": "pan con tortilla", "price": 7.00},
            {"name": "pan con jamon", "price": 7.00},
        ],
    },
    {
        "name": "almuerzo",
        "item": 2,
        "food": [
            {"name": "café", "price": 4.50},
            {"name": "chocolate", "price": 5.00},
            {"name": "jugo de fresas", "price": 9.00},
            {"name": "jugo de papaya", "price": 8.00},
            {"name": "pan con pollo", "price": 7.00},
            {"name": "pan con tortilla", "price": 7.00},
            {"name": "pan con jamon", "price": 7.00},
        ],
    },
    {
        "name": "cena",
        "item": 3,
        "food": [
            {"name": "pizza exprés", "price": 9.50},
            {"name": "ensalada campera", "price": 7.50},
            {"name": "gazpacho", "price": 6.00},
            {"name": "caldo de gallina", "price": 6.00},
            {"name": "pollo al horno", "price": 5.50},
            {"name": "menestrón", "price": 4.00},
        ],
    },
]

# * Length for each meal
list_length = []
for item in list_general:
    list_length.append({"name": item["name"], "length": len(item["food"])})

# * User choices
user_cart_meal = []
user_cart_price = []


# * Welcome & Name
func_clear_console()
string_header(string_restaurant, string_menu)
username = input("|  Nombre: ").strip()


# * Meals
func_clear_console()
string_header(string_restaurant, string_menu)
print_choices([item["name"] for item in list_general])

# * Meals - user
user_choice_meal = possible_choices(
    letters[: len(list_general) + 1], letters[len(list_length)]
)
user_index_meal = letters.index(user_choice_meal)
user_name_meal = list_general[user_index_meal]["name"]
user_cart_meal.append(user_name_meal)


# * Foods
func_clear_console()
string_header(string_restaurant, string_menu, user_name_meal.capitalize())
print_choices(list_general[user_index_meal]["food"])

# * Foods - user
user_choice_food = possible_choices(
    letters[: list_length[user_index_meal]["length"] + 1],
    letters[list_length[user_index_meal]["length"]],
)
user_index_food = letters.index(user_choice_food)
user_name_food = list_general[user_index_meal]["food"][user_index_food]["price"]
user_cart_price.append(user_name_food)


# * Print price

func_clear_console()
string_header(string_restaurant, string_menu, "Boleta de Ventas")
print(f"   Cliente: {username}")
print(f"   Comida: {user_cart_meal[0].capitalize()}")
func_center("-", "-")
print(f"   Subtotal: {user_cart_price[0]}")
print(f"   IGV: {round(user_cart_price[0] * 0.18, 2)}")
print(f"   Total: {user_cart_price[0] + (user_cart_price[0] * 0.18)}")
func_center("-", "-")
func_center("Gracias por su compra", " ")
func_center("Vuelva pronto", " ")
func_center("=", "=")
