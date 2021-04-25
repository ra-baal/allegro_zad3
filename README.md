# allegro_zad3
Intern - obszar Technology - zadanie rekrutacyjne do wyboru.


## Zadanie nr 3. Software Engineer
Aplikacja realizuje cele postawione w zadadniu, tj.:

- listowanie repozytoriów (nazwa i liczba gwiazdek)
- zwracanie sumy gwiazdek we wszystkich repozytoriach

dla dowolnego użytkownika serwisu GitHub.

Dane są zwracane za pomocą protokołu HTTP w formacie JSON.

Aplikacja jest napisana w języku Python z wykorzystaniem frameworka Flask.

Działanie zostało przetestowane jedynie pod nadzorem systemu Linux (Ubuntu).


## Instrukcja instalacji i uruchomienia
Koniecznym do uruchomienia aplikacji jest zainstalowanie frameworka *Flask*, np. za pomocą polecenia `pip3 install flask`.

Należy również zainstalować moduł *requests* poleceniem `pip3 install requests`.

Uruchomić aplikację można za pomocą polecenia `python3 allegro_zad3.py`.

## Endpointy
Aplikacja udostępnia dwa endpointy. Parametr *username* oznacza nazwę wybranego użytkownika.

### 1. Lista repozytoriów (nazwa i liczba gwiazdek) dla danego użytkownika
```
/{username}
```

### 2. Suma gwiazek repozytoriów dla danego użytkownika
```
/{username}/starssum
```


## GitHub API
Aplikacja pobiera potrzebne dane korzystając z GitHub REST API. Wykorzystuje endpoint `GET /users/{username}/repos`.

https://docs.github.com/en/rest/reference/repos#list-repositories-for-a-user


## Propozycje na rozszerzenie
W przyszłości można rozbudować aplikację o wsparcie dla większej liczby endpointów


## Uwagi


