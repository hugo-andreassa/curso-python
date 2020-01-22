a = input()
b = input()
c = input()

saida = ""

vertebrado = {
    "ave": {"carnivoro": "aguia",
            "onivoro": "pomba"},
    "mamifero": {"herbivoro": "vaca",
                 "onivoro": "homem"}
}
invertebrado = {
    "inseto": {"hematofago": "pulga",
               "herbivoro": "lagarta"},
    "anelideo": {"hematofago": "sanguessuga",
                 "onivoro": "minhoca"}
}

if a == "vertebrado":
    saida = vertebrado[b][c]
else:
    saida = invertebrado[b][c]

print(saida)
