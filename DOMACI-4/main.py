#1. Data je lista stringova ["flower","flow","flight"]. Napisati funkciju koja koristi reduce da nađe najduži
# string među datim stringovima.

# list = ["flower","flow","flight"]
# from functools import reduce
#
# def najduzi_string(lista_stringova):
#     def pronadji_string(str1, str2):
#         if len(str1) > len(str2):
#             return str1
#         else:
#             return str2
#
#     najduzi = reduce(pronadji_string, lista_stringova)
#     return najduzi


#2. Date su dvije liste, jedna sa imenima studenata, a druga sa njihovim prosječnim ocjenama.
# Napisati funkciju koja pronalazi studente sa prosječnom ocjenom iznad 8.5 i vraća listu torki (ime,
# ocjena) za te studente.


# imena = ['Marko', 'Dusan', 'Petar']
#
# ocjene = [10.00, 9.82 ,8.3]
#
#
# def prosjecna_ocjena(imena, ocjene):
#
#     lista=[]
#     pomocna_lista = []
#     i=0
#     for _ in ocjene:
#
#         if _>= 8.5:
#             pomocna_lista.append(imena[i])
#             pomocna_lista.append(_)
#
#             lista.append(tuple(pomocna_lista))
#             pomocna_lista=[]
#             i+=1
#         else:
#             i +=1
#
#     return lista
#
# print(prosjecna_ocjena(imena,ocjene))


#3.Data je lista rječnika oblika [{ 'ime': 'Ana', 'godine': 22, 'prosek': 9.1 }, ...]. Napisati funkciju koja
# filtrira studente starije od 21 godine i sortira ih po prosjeku, koristeći filter, sort i lambda funkcije.

# lista = [{ 'ime': 'Ana', 'godine': 22, 'prosjek': 9.1 },
#          { 'ime': 'Marko', 'godine': 24, 'prosjek': 9.5 },
#          { 'ime': 'Goran', 'godine': 18, 'prosjek': 9.1 }]
#
# def sortiranje_ucenika(lista):
#
#     filter_godine = filter(lambda x:x['godine']>21, lista)
#     filter_godine_lista = list(filter_godine)
#
#     sorirana_lista = sorted(filter_godine_lista, key= lambda x: x['prosjek'], reverse=True)
#     print(sorirana_lista)
#
# sortiranje_ucenika(lista)

# 4. Data je lista ["Hello, World!", "Python is cool", "Functional programming rocks"]. Napisati funkciju
# koja broji ukupan broj riječi u svim stringovima koristeći map i reduce.

# from functools import reduce
#
#
# def broj_rijeci_u_stringovima(lista_str):
#
#     rijeci = map(lambda x: x.split(), lista_str)
#
#     ukupan_broj_rijeci = reduce(lambda x, y: x + len(y), rijeci,0)
#
#     return ukupan_broj_rijeci
#
# broj_rijeci_u_stringovima(["Hello, World!", "Python is cool", "Functional programming rocks"])

#5. Data je lista torki oblika [(ime, ocjena, predmet), ...]. Napisati funkciju koja koristi filter, map, i
# reduce da izračuna prosječnu ocjenu po predmetu.

#6. Dat je niz vrijednosti koji predstavlja vremensku seriju. Napisati funkciju koja koristi map da
# izračuna promjenu (diferenciju) između svakog uzastopnog para vrednosti.

# def racunanje_vremenske_serije():
#     vremenski_niz = [10,15,20,25]
#
#     a = map(lambda x,y: y-x,vremenski_niz, vremenski_niz[1:])
#
#     return list(a)


#7. Data je lista ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']. Napisati funkciju koja koristi
# map i reduce da izračuna frekvenciju svakog elementa.



#8.

# with open('link.txt', 'r') as f:
#
#     max_kvadrat = 0
#     for line in f:
#         s= 0
#         if line[0] == line[2]:
#             s = int(line[0])*int(line[2])
#
#             if max_kvadrat < s:
#                 max_kvadrat = s
#
#     print(max_kvadrat)


#9.

# with open('gradovi.txt', 'r') as f:
#
#     max_naselje = 'fake'
#     max_stanivnika = 0
#     for line in f:
#
#        a = line.strip().split(',')
#
#        if int(a[2]) > int(max_stanivnika):
#
#            max_stanivnika = a[2]
#            max_naselje = a[1]
#
#     print(max_naselje)

#10.

# with open('drzave.txt', 'r') as f:
#
#
#     min_populacija = 100000000
#     grad = ''
#     b = input('Unesite ime drzave')
#     for line in f:
#         a = line.strip().split(',')
#
#         if a[0] == b:
#
#             if int(a[2])<int(min_populacija):
#
#                 min_populacija = a[2]
#                 grad = a[1]
#
#     print(grad)


#11.

# with open('drzave.txt', 'r') as f:
#
#
#     populacija = 0
#
#     b = input('Unesite ime drzave')
#     for line in f:
#         a = line.strip().split(',')
#
#         if a[0] == b:
#
#             populacija = populacija + int(a[2])
#     print(populacija)

#12.
# suma = 0
#
#
# with open('hexadecimalni_brojevi.txt', 'r') as file:
#     for line in file:
#         number = line.strip()
#         if number[:2]=="0x":
#             decimalni_broj = int(number, 16)
#             if decimalni_broj % 10 == 3:
#                 suma += decimalni_broj
#
# print(suma)

#14.

# def dodaj_u_fajl(lista_studenata):
#     with open('studenti.txt', 'a') as f:
#         for student in lista_studenata:
#             f.write(f"{student['ime']},{student['prezime']},{student['godina']},{student['prosjek']}\n")
#
#
# def ocjene(godina, ocjena):
#     opsezi_ocjena = { 'A': (9.5, 10), 'B': (8.5, 9.5),'C': (7.5, 8.5),'D': (6.5, 7.5),'E': (6, 6.5)}
#     min_ocjena, max_ocjena = opsezi_ocjena[ocjena]
#     izabrani_studenti = []
#     with open('studenti.txt', 'r') as f:
#         for linija in f:
#             ime, prezime, godina, prosjek = linija.strip().split(',')
#             if int(godina) == godina and float(prosjek) >= min_ocjena and float(prosjek) < max_ocjena:
#                 izabrani_studenti.append({'ime': ime, 'prezime': prezime, 'godina': int(godina), 'prosek': float(prosjek)})
#     return izabrani_studenti






