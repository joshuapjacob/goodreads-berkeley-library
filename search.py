import sys
import random
import time

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

BATCH_SIZE = 10

def run(csv_file):
    
    # Load Goodreads library.
    df = pd.read_csv(csv_file)

    # Only search for "to-read" books.
    df = df[df["Exclusive Shelf"] == "to-read"]

    # Clean ISBNs and remove books without it.
    df["ISBN"] = df["ISBN"].apply(lambda x: x.split('"')[-2])
    df = df[df["ISBN"].str.len() > 0]

    # Make list of ISBNs.
    isbn_list = list(df["ISBN"])
    random.shuffle(isbn_list)

    def make_url(isbn_list):
        prefix = "https://berkeley.primo.exlibrisgroup.com/discovery/search?query=isbn,exact,"
        suffix = ",AND&tab=Default_UCLibrarySearch&search_scope=DN_and_CI&sortby=rank&vid=01UCS_BER:UCB&facet=tlevel,include,available_p,lk&mfacet=institution,include,6532,1&mode=advanced&offset=0"
        return prefix+",OR&query=isbn,exact,".join(isbn_list)+suffix

    # Use headless Chrome as browser.
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    for s in range(0, len(isbn_list), BATCH_SIZE):
        e = min(len(isbn_list), s+BATCH_SIZE)
        url = make_url(isbn_list[s:e])

        # Search for ISBNs.
        driver.get(url)
        time.sleep(5) # TODO: Change to explicit wait.

        # Set number of results per page to be 50.
        # This doesn't work so batch size stays at for now 10.
        # driver.find_element(By.XPATH, "// button[contains(text(),'50')]").click()
        # time.sleep(10)
        
        # Parse HTML.
        html = driver.page_source
        soup = BeautifulSoup(html, "lxml")
        
        # Find results.
        results = soup.find_all("prm-brief-result-container", {"class": "list-item"})

        for result in results:
            
            # Ignore if result is not currently avaiable.
            if result.find("span", {"class":"available_in_library"}) is None:
                continue
                
            title_element = result.find("h3", {"class":"item-title"})
            title = title_element.find("prm-highlight").get_text().strip()
            link = title_element.find("a")["href"].split()[0]
            
            # Print result to console.
            print()
            print("\033[1m"+title+"\033[0m")
            print(link)

    driver.quit()

if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("Pass Goodreads library CSV file name as argument.")
    else:
        csv_file = sys.argv[1]
        try:
            print("Searching and streaming results...")
            run("goodreads_library_export.csv")
        except KeyboardInterrupt:
            pass
            

