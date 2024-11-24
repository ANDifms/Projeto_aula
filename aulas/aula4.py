
n = int(input( "Digite o valor final da sequencia"))

seq = 1
i = 0

while i < n:
    if i == 0:
        print(seq)
    else:
        if i % 2 == 0:
            seq *= 2
        else:
            seq += 3
    print(seq)
    i += 1
