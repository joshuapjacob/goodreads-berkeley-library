# goodreads-berkeley-library
A Python script to check which books from a Goodreads "to-read" shelf are currently available to borrow from UC Berkeley's library.

## Installation
```console
pip install -r requirements.txt
```
Selenium uses Chrome as a driver so make sure you have that installed as well.

## Usage
1. Goodreads no longer has a public AP so you need sign in and export your library to a CSV file on [this page](https://www.goodreads.com/review/import).
2. Run the script. 
```console
python search.py goodreads_library_export.csv
```

## Issues
- It is not fast.
- May yield duplicate results because there are duplicates in the UC Berkeley library database.
