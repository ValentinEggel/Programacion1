serie = {
    "titulo": "Rick y Morty",
    "año": 2013,
    "temporadas": 7,
    "en_emision": True
}

print("Título:", serie["titulo"])
print("Año:", serie["año"])

serie["temporadas"] = 9
serie["genero"] = "comedia"

print("Cantidad de claves:", len(serie))
