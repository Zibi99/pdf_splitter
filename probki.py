
# lista_wejsciowa = [['wypracowanie_nr1_Węgłowska_Natalia', '1-3'], ['wypracowanie_nr1_Witek_Ewa', '4'], ['wypracowanie_nr1_Witek_Ewa', '5-10']]


def zrob_zakres(lista_wejsciowa):
    """metoda wewnętrzna tworząca listę list z początkową liczbą i liczbą końcową - z 1-3 zrobi [1,3], z 4 zrobi [4]"""
    zwrotka = []

    for indeks, wartosc in enumerate(lista_wejsciowa):

        wejscie = lista_wejsciowa[indeks][1]


        if len(str(wejscie).split("-"))>=2:
            zwrotka.append([int(list(str(wejscie).split("-"))[0])-1, int(list(str(wejscie).split("-"))[1])-1])
        else:
            zwrotka.append([int(wejscie)-1, int(wejscie)-1])

    return zwrotka


# print(zrob_zakres(lista_wejsciowa))

def utworz_liste_stron(lista_wejsciowa):
    """Metoda tworzy listę list z numerami konkretnych stron dla każdego elementu listy.
    Dla wejścia: [['wypracowanie_nr1_Węgłowska_Natalia', '1-3'], ['wypracowanie_nr1_Witek_Ewa', '4'], ['wypracowanie_nr1_Witek_Ewa', '5-10']]
    Zwróci: [[1, 2, 3], [4], [5, 6, 7, 8, 9, 10]] """

    koncowa_lista = []

    for indeks_elementu, val in enumerate(zrob_zakres(lista_wejsciowa)):
        posrednia_lista = []
        for i in range(zrob_zakres(lista_wejsciowa)[indeks_elementu][0], zrob_zakres(lista_wejsciowa)[indeks_elementu][1] + 1):
            posrednia_lista.append(int(i))
        koncowa_lista.append(posrednia_lista)
    return koncowa_lista

def utworz_nazwe_skanu_wielostornicowego():

    import os
    import datetime

    current_time = datetime.datetime.now()
    pliki = os.listdir()

    # dodaję 0 dnia i miesiąca, żeby utworzyć nazwę pliku z datą
    miesiac = '0' + str(current_time.month) if len(str(current_time.month)) == 1 else str(current_time.month)
    dzien = '0' + str(current_time.day) if len(str(current_time.day)) == 1 else str(current_time.day)
    nazwa_oczekiwana_poczatek = 'CCF' + dzien + miesiac + str(current_time.year)

    # sprawdzam czy w bieżącym katalogu jest plik zaczynający się prawidłowo - zeskanowany dziś plik wielostronicowy
    # ze wszystkimi pracami
    pliki_z_prawidlowym_poczatkiem = [x for x in pliki if str(x).startswith(nazwa_oczekiwana_poczatek)]

    # zwracam tylko pierwszy znaleziony element
    if len(pliki_z_prawidlowym_poczatkiem)> 0:
        return 'SKUCES', pliki_z_prawidlowym_poczatkiem[0]
    else:
        return 'BŁĄD', f'BŁĄD: w katalogu skryptu brak dzisiejszego pliku pdf zaczynającego się na {nazwa_oczekiwana_poczatek}'

