# Zadanie 3

uczniowie = ["Anna Kowalska", "Jan Nowak", "Piotr Wiśniewski", "Ewa Zielińska"]

posortowani = sorted(uczniowie, key=lambda x: x.split()[1])
inicjaly = list(map(lambda x: "".join(imie[0] for imie in x.split()), uczniowie))

print(posortowani)
print(inicjaly)
