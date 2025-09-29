from random import randint

def stampa_griglia(n, pos, uscita):
    """Stampa la griglia con G = giocatore, U = uscita, . = spazio vuoto"""
    for riga in range(n):
        for colonna in range(n):
            if [riga, colonna] == pos:
                print('G', end=' ')
            elif [riga, colonna] == uscita:
                print('U', end=' ')
            else:
                print('.', end=' ')
        print()


def muovi(pos, mossa):
    """Aggiorna la posizione in base alla mossa"""
    nuova_pos = pos.copy()
    if mossa == 'n':
        nuova_pos[0] -= 1
    elif mossa == 's':
        nuova_pos[0] += 1
    elif mossa == 'o':
        nuova_pos[1] -= 1
    elif mossa == 'e':
        nuova_pos[1] += 1

    return nuova_pos


def gestisci_livello(livello):
    """ Gestisce un singolo livello del gioco
    Ritorna:
    * True se il giocatore raggiunge l'uscita
    * False se il giocatore va oltre i limiti della griglia.
    """

    n = livello + 2
    uscita = [n - 1, n - 1]

    pos = [randint(0, n - 2), randint(0, n - 2)]
    print(f'Livello {livello}) Griglia {n}x{n}')

    while True:
        stampa_griglia(n, pos, uscita)


        if pos == uscita:
            print('Hai raggiunto l\'uscita!')
            return True

        mossa = input('Mossa (n/s/e/o): ').strip().lower()


        if mossa not in ['n', 's', 'e', 'o']:
            print('Mossa non valida! Usa n/s/e/o')
            continue

        nuova_pos = muovi(pos, mossa)


        if (nuova_pos[0] < 0 or nuova_pos[0] >= n or
                nuova_pos[1] < 0 or nuova_pos[1] >= n):
            print('GAMEOVER: Sei uscito dalla griglia!')
            return False

        pos = nuova_pos


def main():
    print("=== Benvenuto in Room Escape ===")
    livello = 0
    max_livello = 5



    while livello <= max_livello:
        completato = gestisci_livello(livello)
        if completato:
            livello += 1
        else:
            break

    if livello > max_livello:
        print('Complimenti! Hai completato tutti i livelli!')
    else:
        print(f'Game Over! Hai completato {livello} livelli.')


if __name__ == "__main__":
    main()
