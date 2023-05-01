# goodreads-berkeley-library
A Python script to check which books from a Goodreads "Want to Read" shelf are currently available in UC Berkeley's library.

## Usage
1. Goodreads no longer has a public AP so you need sign in and export your library to a CSV file on [this page](https://www.goodreads.com/review/import).
2. Run the script. ```python search.py goodreads_library_export.csv```


## Issues
- It is slow... 
- May yield duplicate results because there are duplicates in the UC Berkeley library database.
