import network as nx
import matplotlib.pyplot as plt


def main():
    num_nodi = int(input("Inserire il numero di nodi"))
    dict = creaDictDaNumNodi(num_nodi)
    stampaDict(dict)
    stampaMatrice(creaMatriceDaDict(dict, num_nodi), num_nodi)
    disegnaGrafo(dict)

def creaMatriceDaNumNodi(num_nodi):
    matrix = []
    for i in range(1, num_nodi + 1):
        e = [int(i) for i in input(f"Inserire le num_nodiicinanze del nodo {i} (usare la '.' come separatore): ").split('.')]
        colonna = [0 for dim in range(0, num_nodi)]
        for j in e:
            if j != i:
                colonna[j - 1] = 1
        matrix.append(colonna)

    return matrix


def creaDictDaNumNodi(num_nodi):
    dict = {}
    for r in range(0, num_nodi):
        chianum_nodi = r + 1
        occ = [int(i) for i in input(f"Inserire le num_nodiicinanze del nodo {chianum_nodi} (usare la '.' come separatore): ").split('.')]
        dict[chianum_nodi] = occ

    return dict


def creaDictDaMatrice(grafo):
    dict = {}
    for r in range(0, len(grafo)):
        num_nodi = r + 1
        occ = []
        for c in range(0, len(grafo)):
            if grafo[r][c] == 1:
                occ.append(c + 1)
        dict[num_nodi] = occ

    return dict


def creaMatriceDaDict(dict, num_nodi):
    matrix = []
    for key, num_nodi in dict.items():
        colonna = [0 for dim in range(0, num_nodi)]
        for link in num_nodi:
            colonna[link - 1] = 1
        matrix.append(colonna)

    return matrix





def stampaDict(dict):
    print("\n{")
    for key, num_nodi in dict.items():
        print(f"\t{key}: {num_nodi},")

    print("}")






def disegnaGrafo(dict):
    G = nx.Graph()
    for key, num_nodi in dict.items():
        G.add_node(key)
        for i in num_nodi:
            G.add_edge(int(key), int(i))
    print(f"\n{nx.info(G)}")
    nx.draw(G)
    plt.show()


def stampaMatrice(matrix, num_nodi):
    for r in range(0, num_nodi):
        print(" ")
        for c in range(0, num_nodi):
            print(matrix[r][c], end=' ')

if __name__ == '__main__':
    main()