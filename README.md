# allegro_zad3

Intern - obszar Technology - zadanie rekrutacyjne do wyboru.


## Zadanie nr 3. Software Engineer

Aplikacja realizuje cele postawione w zadadniu, tj.:

- listowanie repozytoriów (nazwa i liczba gwiazdek)
- zwracanie sumy gwiazdek we wszystkich repozytoriach

dla dowolnego użytkownika serwisu GitHub.

Dane są zwracane za pomocą protokołu HTTP w formacie JSON.

Aplikacja jest napisana w języku Python z wykorzystaniem frameworka Flask.

Działanie zostało przetestowane jedynie na systemie Linux (Ubuntu).


## Instrukcja instalacji/uruchomienia
Koniecznym do uruchomienia aplikacji jest zainstalowanie Flaska, np. za pomocą polecenia `pip install flask`.


## GitHub API
Aplikacja pobiera potrzebne dane korzystając z GitHub REST API. Wykorzystuje endpoint `GET /users/{username}/repos`.

https://docs.github.com/en/rest/reference/repos#list-repositories-for-a-user


## Propozycje na rozszerzenie


## Uwagi


