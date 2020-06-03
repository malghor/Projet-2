
mot=input("votre phrase : ")
motX=mot.rstrip().split(" ")
nombres=[]

def test (mot,nombre):
    resultat=[]
    for i in mot:
        if i.isdigit():
            i=float(i)
            nombre.append(i)
    resultat.append(sum(nombre))
    print(resultat)

test(motX,nombres)