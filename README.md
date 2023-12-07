# mwo-project
## Opis gałęzi
Jest tylko jedna gałąź: main. Na niej jest plik index.py, który zawiera testy Selenium.
W folderze **website** jest plik .html ze stroną internetową.
W folderze **backend** jest plik server.js z wspierającym serwerem do zapytań i przechowywania książek.
Niestety, nie udało mi się zintegrować zgłaszania błędów z Azure devops, jednak reszta działa poprawnie, czyli: testy UI w selenium oraz 
skonfigurowane github actions, uruchamiające się automatycznie podczas pull requestów.
## Opis aplikacji
Aplikacja pozwala na dodawanie książek do bazy danych i jest oparta o architekture MVC.
Aby dodać książke należy:
### 1. Wypełnić formularz nowej książki
![1](https://github.com/ThinCan/mwo-project/assets/20555497/cd410f1f-6b74-4d32-94a1-8e158dad1bb3)
### 2. Nacisnąć przycisk "Dodaj"
Jak widać, nowa książka pojawia się od razu na liście.\
![2](https://github.com/ThinCan/mwo-project/assets/20555497/097c139d-afcb-420d-ba86-87c390384976)

### Aktualizowanie parametrów książki:
Aby zaktualizować wybraną książke, należy nacisnąć przycisk "Update" w odpowiadającym książce wierszu. Spowoduje to dynamiczne ukazanie się pól wejściowych
Pola należy wypełnić i nacisnąć guzik "Update". Naciśnięcie guzika "Cancel" skasuje zmiany i schowa pola edycji.\
![3](https://github.com/ThinCan/mwo-project/assets/20555497/cf6793d8-39aa-4ce5-bc30-1d02c3a9291f)

![4](https://github.com/ThinCan/mwo-project/assets/20555497/ae4dc9cc-8958-4a18-903c-378d5495e061)

### Usuwanie
Aby usunąć książke, należy nacisnąć przycisk "Delete".\
![5](https://github.com/ThinCan/mwo-project/assets/20555497/1e2b7d0d-37c8-44e2-8004-6229e369f1be)

## Opis testów
Testy zostały napisane w selenium w języku Python. Kod testu znajduje się w pliku index.py i jego zadanie to:
- Dodać książke
- Sprawdzić, czy pojawiła się na liście
- Zaktualizować książkę
- Sprawdzić, czy zmiany zaszły
- Usunąć książkę
- Sprawdzić, czy została usunięta:\
![6](https://github.com/ThinCan/mwo-project/assets/20555497/7fd2167c-9082-4cb8-90d6-1f70e75cd7c7)

## Skonfigurowanie skryptu akcji githuba
Skrypt uruchamia maszynę ubuntu-latest, następnie instaluje przeglądarke chrome i pythona. Następnie uruchamia skrypt pythona:\
![7](https://github.com/ThinCan/mwo-project/assets/20555497/ed2492af-8d44-47b1-8ea0-348c5b8216fd)

Oto wynik działania:\
![8](https://github.com/ThinCan/mwo-project/assets/20555497/87892f1a-e59a-4bec-81d3-746f2360339b)

## Konfiguracja gałęzi:
Konfiguracja opiera się na włączeniu wymogu utworzenia Pull Request, aby dodać zmiany na gałąź main. Dodatkowo wymagane jest przejście sprawdzenia statusów akcji githuba:\
![9](https://github.com/ThinCan/mwo-project/assets/20555497/82b91675-43c7-4841-b5aa-f167822563a6)

## Tworzenie pull requesta
Na gałąź "website" dodałem plik strony internetowej i serwera.
Teraz chcę scalić ją z main. 
### W tym celu tworze pull requesta z "website" na "main":
![10](https://github.com/ThinCan/mwo-project/assets/20555497/0d4f7f29-3151-4beb-b1eb-beb548af8a63)

### Automatycznie uruchamia się skrypt, sprawdzający poprawność:
![11](https://github.com/ThinCan/mwo-project/assets/20555497/7efc4af6-c8e4-47df-9a4a-a5c74c4c3791)

### I przeszedł sukcesem. Gałęzie mogą być scalone
![12](https://github.com/ThinCan/mwo-project/assets/20555497/90f5753b-579f-4a42-8ccf-663ad5250a1d)

