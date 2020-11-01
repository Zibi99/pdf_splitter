
from PyPDF2 import PdfFileReader, PdfFileWriter

from probki import utworz_liste_stron

nazwa_wypracowania = "wypracowani_z_Adama_Mickiewicza_Dziady_"

lista_uczniow_i_stron_wejscie = [["Węgłowska Natalia", "1-2"], ["Witek Ewa", "3-4"], ["Sowa Adam", "5"], ["Gal Anonim", "6"]]


# wstawiam '_' pomiędzy nazwisko i imię
lista_uczniow_i_stron = [[x.replace(" ","_"),y] for [x,y] in lista_uczniow_i_stron_wejscie]



def zrob_nazwy_plikow(lista_wejsciowa, nazwa_wypracowania):
    zwrotka = []
    for indeks, nazwiska in enumerate(lista_wejsciowa):
        zwrotka.append([nazwa_wypracowania+"_"+lista_wejsciowa[indeks][0], lista_wejsciowa[indeks][1]])

    return zwrotka

# print(zrob_nazwy_plikow(lista_uczniow_i_stron, nazwa_wypracowania))

def pdf_splitter(wejsciowy_pdf, nazwa_wypracowania, lista_uczniow_i_stron):
    nazwa_wypracowania_wewnatrzna = zrob_nazwy_plikow(lista_uczniow_i_stron, nazwa_wypracowania)
    print("nazwa_wypracowania_wewnatrzna", nazwa_wypracowania_wewnatrzna)
    pdf = PdfFileReader(wejsciowy_pdf)

    lista_stron_wszystkich_uczniow = utworz_liste_stron(lista_uczniow_i_stron)
    print("lista_stron_wszystkich_uczniow", lista_stron_wszystkich_uczniow)
    print("\n")

    for indeks, wypracowanie in enumerate(nazwa_wypracowania_wewnatrzna):
        print("Pierwszy for, indeks ", indeks, wypracowanie)
        pdf_writer = PdfFileWriter()

        # add.Page musi dodawać wszystkie strony z zakresu dla danej osoby - wykonany tyle razy na
        # stronach dla danej osoby - zrobić w pętli for


        for i in lista_stron_wszystkich_uczniow[indeks]:
            print(f"lista_stron_wszystkich_uczniow i = {i}, {lista_stron_wszystkich_uczniow[indeks]}")

            pdf_writer.addPage(pdf.getPage(i))



            # po skończeniu obiektu pdf_writer - mam już odpowiednią liczbę stron

            # tu musze dać zrobioną nazwę
            output_filename = str(nazwa_wypracowania_wewnatrzna[indeks][0])+".pdf"
            with open(output_filename, 'wb') as out:
                pdf_writer.write(out)
            print(f'Utworzyłem {output_filename}')

        print("\n")

pdf_splitter("CCF25102020.pdf", nazwa_wypracowania, lista_uczniow_i_stron)