farben = {"blau": {"hellblau": "kornblumenblau", "dunkelblau": "ultramarin"}, "grün": {"hellgrün": "grasgrün", "dunkelgrün": "oliv"}}

for id, info in farben.items():
    print("Übergeordnete Farbe:", id)
    for key in info:
        print(key + ":", info[key])

