# Zaawansowane struktury danych - zadania
Jeśli będziesz miał problem z implementacją niektórych struktur, tutaj znajdziesz dodatkowe informacje, które mogą ci pomóc:  [Start here](https://github.com/szczepanikoww/Advanced-Data-Structures---excercies/wiki)

***
## Zadanie 1.
Wykorzystując funkcjonalność stosu, uzupełnij funkcję w taki sposób, aby odwracała podany tekst

> Podpowiedź: Wykorzystaj funkcję  ``.pop()``

## Zadanie 2.
Uzupełnij funkcję ``symuluj_drukowanie``, aby zdejmowała z kolejki kolejne dokumenty i wypisywała ich nazwy, symulując działanie drukarki pracującej w trybie FIFO (pierwszy zgłoszony, pierwszy drukowany).

> Podpowiedź: Wykorzystaj funkcję  ``.popleft()``

## Zadanie 3.
Wyobraź sobie, że reprezentujesz strukturę katalogów i podkatalogów jako drzewo binarne. Każdy katalog (węzeł) może mieć co najwyżej dwa podkatalogi (lewy i prawy).

Korzystając z biblioteki ``binarytree``, utwórz drzewo binarne oraz napisz następujące funkcje:

* ``zlicz_foldery(korzen)`` – zwraca całkowitą liczbę folderów w strukturze.

* ``czy_zawiera_folder(korzen, nazwa)`` – sprawdza, czy drzewo zawiera folder o podanej nazwie.

Drzewo w zadniu wygląda w sposób następujący:
```
          root
         /    \
      docs    media
     /   \       \
  szkice  pdf   video
```

