# Goodreads Berkeley Library
A Python script to check which books from a Goodreads "to-read" shelf are currently available to borrow from UC Berkeley's library.

Built with [Selenium](https://www.selenium.dev/) and [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/).

Unfortunately, the [Library Extension](https://www.libraryextension.com/) does not support UC Berkeley's library so I made this to save me from manually checking which books on my reading list are currently available.

## Installation
```console
pip install -r requirements.txt
```
Selenium uses Chrome as a driver so make sure you have that installed as well.

## Usage
1. Goodreads no longer has a public API so you need sign in and export your library to a CSV file on [this page](https://www.goodreads.com/review/import).
2. Run the script as follows. 
```console
python search.py goodreads_library_export.csv
```

### Example Output
```console
Searching and streaming results...

The pragmatic programmer : from journeyman to master
https://berkeley.primo.exlibrisgroup.com/discovery/fulldisplay?docid=alma991080851389706532&context=L&vid=01UCS_BER:UCB&lang=en&search_scope=DN_and_CI&adaptor=Local

Trust me, I'm lying : the tactics and confessions of a media manipulator
https://berkeley.primo.exlibrisgroup.com/discovery/fulldisplay?docid=alma991000883859706532&context=L&vid=01UCS_BER:UCB&lang=en&search_scope=DN_and_CI&adaptor=Local

Rosencrantz & Guildenstern are dead
https://berkeley.primo.exlibrisgroup.com/discovery/fulldisplay?docid=alma991071720859706532&context=L&vid=01UCS_BER:UCB&lang=en&search_scope=DN_and_CI&adaptor=Local
```

## Issues
- It is not fast but fast enough for a human to read the titles and make up their mind about what to read next.
- May yield duplicate results because there are duplicates in the UC Berkeley library database.
