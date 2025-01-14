alph = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"


encript = input("Enter encripted text: ").replace(" ", "")
original = input("Enter orginal text: ")

res = [
    (alph.index(enc) - alph.index(orig)) % len(alph) 
    for orig, enc in zip(original, encript)
]

print(f"Result: {''.join(alph[i % len(alph)] for i in res)}")
