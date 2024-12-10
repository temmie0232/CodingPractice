
n = int(input())

patterns = ["S","H","C","D"]
existing_card = []
not_existing_card = []

for i in range(n):
    card = input()
    existing_card.append(card)

for pattern in patterns:
    for rank in range(1,14):
        card = f"{pattern} {rank}"
        if card not in existing_card:
            not_existing_card.append(card)

for i in not_existing_card:
    print(i)