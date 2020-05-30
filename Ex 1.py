nb=3
poids=[67,121,88]

def carburant(nb,poids):
    carburant_moins=60
    carburant_plus=80
    carburant_total=0

    assert len(poids)==nb,"votre liste de poids doit comprendre autant de poids que de passagers. Par exemple si il y a 3 passager, il faut 3 poids, et non 2 poids ou 4"

    while nb>0:
        for i in poids:
            if i > 90:
                carburant_total+=carburant_plus
                nb-=1
            else :
                carburant_total+=carburant_moins
                nb-=1
    print(carburant_total)

carburant(nb,poids)
