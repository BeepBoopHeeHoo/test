myPokemon = []
pokemonDB = []
pokemonAdded = False
file = open("Pokemon.txt", "r")

for line in file:
    pokemon = line.replace('\n', '').split(',')

    pokemonDB += [pokemon]

while len(myPokemon) < 6:
    pokemonAdded = False
    findPokemon = input('input pokemon name or "stop" to finish team building: ')
    findPokemon = findPokemon[0:1].upper()+findPokemon[1:len(findPokemon)].lower()
    if findPokemon == "Stop":
        break

    i = 0
    while i < len(pokemonDB):
        if findPokemon == pokemonDB[i][1]:
            formFinder = 1
            forms = [pokemonDB[i][2]]
            j = 1
            while pokemonDB[i][0] == pokemonDB[i+j][0]:
                forms += [pokemonDB[i+j][2]]
                j += 1

            if len(forms) > 1:
                print("This pokemon has multiple forms, please type the form you want:")

                k = 0
                while k < len(forms):
                    if forms[k] == '':
                        forms[k] = pokemonDB[i][1]

                    print(forms[k], end="")

                    if forms[k] != forms[-1]:
                        print(", ", end="")

                    else:
                        print(end="\n")

                    k += 1

                form = input()
                m = 0
                while m < len(forms):
                    if form.lower() == forms[m].lower():
                        pokemon = pokemonDB[i][1]
                        if forms[m] != pokemonDB[i][1]:
                            pokemon = f"{pokemon} – {forms[m]}"
                        myPokemon += [pokemon]
                        pokemonAdded = True
                        break

                    if m == len(forms)-1:
                        form = input(f"Unable to find \"{pokemonDB[i][1]}–{form}\", please make sure you typed the form's name correctly: ")
                        m = 0

                    m += 1

            if not pokemonAdded:
                myPokemon += [findPokemon]

            i = 0
            break

        if i == len(pokemonDB)-1:
            print(f'Unable to find the pokemon "{findPokemon}", please make sure you typed the pokemon\'s name correctly')

        i += 1


print(myPokemon)
file.close()
