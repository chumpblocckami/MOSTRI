from bestiare import Bestiare
from tamer import Tamer

if __name__ == '__main__':
    bestiare = Bestiare()

    tamer1 = Tamer(bestiare)
    print("Tamer1")
    print(tamer1.cage)
    print("----" * 10)

    tamer2 = Tamer(bestiare)
    print("Tamer2")
    print(tamer2.cage)
    print("----" * 10)
