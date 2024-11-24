
morse_code = {
    'a': ".-",    'b': "-...",  'c': "-.-.",  'd': "-..",   'e': ".",  
    'f': "..-.",  'g': "--.",   'h': "....",  'i': "..",    'j': ".---",
    'k': "-.-",   'l': ".-..",  'm': "--",    'n': "-.",    'o': "---",
    'p': ".--.",  'q': "--.-",  'r': ".-.",   's': "...",   't': "-",
    'u': "..-",   'v': "...-",  'w': ".--",   'x': "-..-",  'y': "-.--",
    'z': "--..",
    '0': "-----", '1': ".----", '2': "..---", '3': "...--", '4': "....-",
    '5': ".....", '6': "-....", '7': "--...", '8': "---..", '9': "----."
}

morse_letra = {
    ".-": "a",    "-...": "b",  "-.-.": "c",  "-..": "d",   ".": "e",
    "..-.": "f",  "--.": "g",   "....": "h",  "..": "i",    ".---": "j",
    "-.-": "k",   ".-..": "l",  "--": "m",    "-.": "n",    "---": "o",
    ".--.": "p",  "--.-": "q",  ".-.": "r",   "...": "s",   "-": "t",
    "..-": "u",   "...-": "v",  ".--": "w",   "-..-": "x",  "-.--": "y",
    "--..": "z",
    "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
    ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9"
}
nome = input("qual é seu nome ?")
print(f"Olá {nome} meu nome é Mijaro Namia Motu, sou gerenal da marinha do Japao \nquero que voce escreva alguma coisa pro nosso outro navio ")
opcao = int(input("Conversor em morse = 1 \nTraduzir morse = 2 "))

if opcao == 1:
    palavra = input("digite uma palavra: ")
    print(" conversor de morse")
    for letra in palavra:
        letra = letra.lower()
        if letra in morse_code:
            print(morse_code[letra], end=" ")

elif opcao == 2:
    palavra = input("digite o codigo morse: ")
    print(" tradutor de morse ")
    morse_letras = palavra.split() # divide o codigo morse por espaço
    for morse in morse_letras:
        if morse in morse_letra:
            print(morse_letra[morse], end=" ")

    # palavra = input("Digite o código Morse para traduzir (use espaço entre cada letra): ")
    # print("Tradutor de código Morse:")
    # morse_letras = palavra.split()  # Divide o código Morse por espaços
    # for morse in morse_letras:
    #     if morse in morse_letra:
    #         print(morse_letra[morse], end="")
    # print()  # Para quebra de linha após a tradução
