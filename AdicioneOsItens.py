menu = ["pizza", "fritas", "wings", "salad"]

menu.insert(0, "steak")


if "hamburguer" not in menu:
    menu.remove("fritas")
    print("Não temos hamburgues...")
elif "fritas" not in menu:
    menu.remove("hamburguer")
    print("Não temos Frita...")
else:
    print("Temos os dois, em preparação....")
        
    
print(menu)