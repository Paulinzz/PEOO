import random

boneco_pos = (random.randint(0, 6), random.randint(0, 6))
objeto_pos = (random.randint(0, 6), random.randint(0, 6))

while True:
    for i in range(7):
        for j in range(7):
            if (i, j) == boneco_pos:
                print("B", end=" ")
            elif (i, j) == objeto_pos:
                print("O", end=" ")
            else:
                print("-", end=" ")
        print()
    print()

    movimento = input("Digite o movimento (w/a/s/d): ")

    if movimento == "w":
        boneco_pos = (boneco_pos[0] - 1, boneco_pos[1])
    elif movimento == "a":
        boneco_pos = (boneco_pos[0], boneco_pos[1] - 1)
    elif movimento == "s":
        boneco_pos = (boneco_pos[0] + 1, boneco_pos[1])
    elif movimento == "d":
        boneco_pos = (boneco_pos[0], boneco_pos[1] + 1)

    if boneco_pos == objeto_pos:
        print("Fim de jogo! Parabéns!")
        break