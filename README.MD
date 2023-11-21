# Dillinger
## _The Last Markdown Editor, Ever_

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

# Panel SM
> RSS to webowa aplikacja. Celem jest ujednolicenie miejsca przechowywania wszystkich pozwów zarówno przeciwko Spółdzielni jak i wniesionych przez Spółdzielnię

## Menu
* [Info](#general-info)
* [Zrzuty ekrnau](#screenshots)
* [Technologie](#technologies)
* [Setup](#setup)
* [Kod](#code)
* [Rozwój](#features)
* [Status](#status)
* [Inspiracja](#inspiration)
* [Kontakt](#contact)

## Info
Aplikacja webowa jest bazą pozwów w Spółdzielni. Możesz dodawać, edytować, filtrować. Kompatybilna na urządzenia przeznośne.
Wystarczy dostęp do Internetu i przeglądarka.

## Zrzuty ekranu
![Example screenshot](./img/screenshot.png)

## Technologie
* Python - version 3.8
* Django
* HTML
* Bootstrap
* CSS

## Setup
Aplikacja webowa, działa pod przeglądarkami www:
* Safari, Edge, Chrome, Mozilla, Opera

## Code Examples
Przykład, użyty w projekcie:<br>
`   def dashboard_przez(request):
        my_records = Record.objects.all()
    p = Paginator(Record.objects.all(), 10)
    page = request.GET.get("page")
    my_record = p.get_page(page)`

## Rozwój
To-do list:
* Wysyłka smsów
* Dodawanie plików do sprawy
* Raporty

## Status
Projekt: _in progress_, 

## Inspiracja
Pomysł własny, realizacja własna.

## Kontakt
Projekt i wykonanie [@ithelparturgolata](ithelparturgolata@gmail.com)