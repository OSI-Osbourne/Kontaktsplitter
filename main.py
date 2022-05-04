from Controller import Finder


def main():
    print(str(Finder.find("Frau Sandra Berger")))
    print(str(Finder.find("Herr Dr. Sandro Gutmensch")))
    print(str(Finder.find("Professor Heinreich Freiherr vom Wald")))
    print(str(Finder.find("Mrs. Doreen Faber")))
    print(str(Finder.find("Mme. Charlotte Noir")))
    print(str(Finder.find("Estobar y Gonzales")))
    print(str(Finder.find("Frau Prof. Dr. rer. nat. Maria von Leuthäuser-Schnarrenberger")))
    print(str(Finder.find("Herr Dipl. Ing. Max von Müller")))
    print(str(Finder.find("Dr. Russwurm, Winfried")))
    print(str(Finder.find("Dr. von Russwurm, Winfried")))
    print(str(Finder.find("Herr Dr.-Ing. Dr. rer. nat. Dr. h.c. mult. Paul Steffens")))


if __name__ == '__main__':
    main()
