guests = {
    "Мурат": 24,
    "Эржан": 21,
    "Карина": 24,
    "Алтынай": 17,
    "Айбек": 16
}

club_allowed = {name: age for name, age in guests.items() if age >= 17}

print("В клуб могут пойти следующие гости:")
for name in club_allowed:
    print(name)