import sqlite3
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

key_words = ['Demokratie', 'demokratisch', 'demokratische', 'demokratischen', 'Demokratisch', 'Demokratische',
             'Demokratischen', 'Bürger', 'Bürgern', 'Bürgerin', 'Bürgerinnen', 'Person', 'Personen', 'Volksabstimmung',
             'Volksabstimmungen', 'Abstimmung', 'Abstimmungen', 'abstimmen', 'souverän', 'souveränen', 'Souveränität']

populism_key_words = ['Volk', 'Volke', 'völkisch', 'völkische', 'völkisches', 'Elite', 'Eliten', 'Elitegruppen',
                      'Person', 'Personen', 'souverän', 'souveränen', 'Souveränität', 'Korruption', 'korrupt',
                      'korrupte', 'korrupten', 'korruptes', 'bestechlich', 'bestechliche', 'bestechlichen',
                      'bestechliches']

driver = webdriver.Chrome()

# Create DB Tables

'''
def make_tables():
    conn = sqlite3.connect("PoliticalPartyWebScraper.db")
    c = conn.cursor()
    
     c.execute("""CREATE TABLE populist_words_from_afd (
                page_url text,
                page_title text,
                word text
            )""")
    c.execute("""CREATE TABLE populist_words_from_spd (
            page_url text,
            page_title text,
            word text
        )""")
    c.execute("""CREATE TABLE populist_words_from_cdu (
            page_url text,
            page_title text,
            word text
        )""")
    
    c.execute("""CREATE TABLE words_from_afd (
        page_url text,
        page_title text,
        word text
    )""")
    c.execute("""CREATE TABLE words_from_spd (
        page_url text,
        page_title text,
        word text
    )""")
    c.execute("""CREATE TABLE words_from_cdu (
        page_url text,
        page_title text,
        word text
    )""")
    conn.commit()
    conn.close()


make_tables()
'''


# Functions to write populism related words to DBs
def write_to_db_afd_pop(url, page_title, word):
    conn = sqlite3.connect("PoliticalPartyWebScraper.db")
    c = conn.cursor()
    c.execute("INSERT INTO populist_words_from_afd VALUES (?,?,?)", (url, page_title, word))
    conn.commit()


def write_to_db_spd_pop(url, page_title, word):
    conn = sqlite3.connect("PoliticalPartyWebScraper.db")
    c = conn.cursor()
    c.execute("INSERT INTO populist_words_from_spd VALUES (?,?,?)", (url, page_title, word))
    conn.commit()
    conn.close()


def write_to_db_cdu_pop(url, page_title, word):
    conn = sqlite3.connect("PoliticalPartyWebScraper.db")
    c = conn.cursor()
    c.execute("INSERT INTO populist_words_from_cdu VALUES (?,?,?)", (url, page_title, word))
    conn.commit()
    conn.close()


# Functions to write democracy related words to DBs
def write_to_db_afd(url, page_title, word):
    conn = sqlite3.connect("PoliticalPartyWebScraper.db")
    c = conn.cursor()
    c.execute("INSERT INTO words_from_afd VALUES (?,?,?)", (url, page_title, word))
    conn.commit()


def write_to_db_spd(url, page_title, word):
    conn = sqlite3.connect("PoliticalPartyWebScraper.db")
    c = conn.cursor()
    c.execute("INSERT INTO words_from_spd VALUES (?,?,?)", (url, page_title, word))
    conn.commit()
    conn.close()


def write_to_db_cdu(url, page_title, word):
    conn = sqlite3.connect("PoliticalPartyWebScraper.db")
    c = conn.cursor()
    c.execute("INSERT INTO words_from_cdu VALUES (?,?,?)", (url, page_title, word))
    conn.commit()
    conn.close()


# web scrape AfD
print("Scraping AfD...\n")
driver.get("https://www.afd.de/")


def scrape_afd():
    page_url = driver.current_url
    page_title = driver.find_element_by_class_name("breadcrumb-leaf").text

    word_list = []

    try:
        upper_text = driver.find_element_by_xpath('//div[@class="fusion-text"]')
        upper_words = upper_text.get_attribute("innerHTML")
        upper_words_split = upper_text.text.split(" ")
        for word in upper_words_split:
            word = word.strip(r".,<>'/\|_=?!")
            if word in key_words:
                word_list.append(word)
                write_to_db_afd(str(page_url), str(page_title), str(word))
            elif word in populism_key_words:
                word_list.append(word)
                write_to_db_afd_pop(str(page_url), str(page_title), str(word))

    except NoSuchElementException:
        pass

    headings = driver.find_elements_by_xpath('//div[@class="fusion-toggle-heading"]')
    head_num = 0
    while head_num < len(headings):
        for heading in headings:
            try:   # if the tab is open, scrape
                active = driver.find_element_by_xpath('//a[@class="active"]')
                if active:
                    page_text = driver.find_elements_by_xpath(
                        '//div[@class="panel-body toggle-content fusion-clearfix"]')[head_num]
                    page_words = page_text.get_attribute("innerHTML")
                    words = page_words.split(" ")
                    for word in words:
                        word = word.strip(r",.<>'/\|?!")
                        if word in key_words:
                            word_list.append(word)
                            write_to_db_afd(str(page_url), str(page_title), str(word))
                        if word in populism_key_words:
                            word_list.append(word)
                            write_to_db_afd_pop(str(page_url), str(page_title), str(word))
                    try:
                        heading.click()   # click on the tab once scraped to close it
                    except ElementClickInterceptedException:
                        pass
            except NoSuchElementException:   # If the tab is closed, click on it to open it, then scrape
                try:
                    heading.click()
                except ElementClickInterceptedException:
                    driver.execute_script("window.scrollTo(0, 500)")
                    heading.click()
                page_text = driver.find_elements_by_xpath(
                    '//div[@class="panel-body toggle-content fusion-clearfix"]')[head_num]
                page_words = page_text.get_attribute("innerHTML")
                words = page_words.split(" ")
                for word in words:
                    word = word.strip(r",.<>'/\|")
                    if word in key_words:
                        word_list.append(word)
                        write_to_db_afd(str(page_url), str(page_title), str(word))
                    elif word in populism_key_words:
                        word_list.append(word)
                        write_to_db_afd_pop(str(page_url), str(page_title), str(word))
            head_num += 1
    print("URL:", page_url)
    print("Page:", page_title)
    return len(word_list)


pages = ["demokratie-in-deutschland/", "aussenpolitik_sicherheit/", "euro-finanzen-eu/", "innere-sicherheit/",
         "zuwanderung-asyl/", "familie-bevoelkerung/", "bildung-schule/", "kultur-medien/", "sozialpolitik/",
         "steuern-finanzen-wirtschaft-arbeit/", "gesundheit/", "energie-umwelt-klima/", "umwelt-agrar-verbraucher/",
         "verkehr-infrastruktur/"]
page_num = 0

# click on button to accept cookies and close pop-up
driver.find_element_by_xpath('//a[@class="_brlbs-btn _brlbs-btn-accept-all cursor"]').click()

while page_num < len(pages):
    driver.find_element_by_xpath(f'//a[contains(@href,"/{pages[page_num]}")]').click()
    print("Number of Occurrences:", scrape_afd())
    page_num += 1
    driver.execute_script("window.history.go(-1)")

print("AFD complete")
driver.close()


# web scrape SPD
print("Scraping SPD...\n")
driver.get("https://www.spd.de/standpunkte/")


def scrape_spd():
    spd_word_list = []

    clicked = True
    ids = ["c55449", "c55452", "c55455", "0", "0", "0", "c55458"]
    try:
        WebDriverWait(driver, 12).until(EC.element_to_be_clickable((By.ID, ids[spd_page_num]))).click()
    except (NoSuchElementException, TimeoutException):
        clicked = False
        pass

    spd_url = driver.current_url
    spd_page_title = spd_url[31:].capitalize()
    spd_page_title = spd_page_title.strip(r"/0")

    if clicked:
        page_text = WebDriverWait(driver, 12).until(
            EC.presence_of_all_elements_located((By.XPATH, '//div[@class="text "]')))
    else:
        page_text = WebDriverWait(driver, 12).until(
            EC.presence_of_all_elements_located((By.XPATH, '//div[@class="text__body"]')))

    for element in page_text:
        page_words = element.get_attribute("innerHTML")
        words = page_words.split(" ")
        for word in words:
            word = word.strip(r",.<>'/\|_=?!")
            if word in key_words:
                spd_word_list.append(word)
                write_to_db_spd(str(spd_url), str(spd_page_title), str(word))
            if word in populism_key_words:
                spd_word_list.append(word)
                write_to_db_spd_pop(str(spd_url), str(spd_page_title), str(word))

    print("URL:", spd_url)
    print("Page title:", spd_page_title)
    if clicked:
        driver.execute_script("window.history.go(-1)")
    return len(spd_word_list)


spd_pages = ["Familien", "Pflege", "Wohnen", "Ausbildung", "Steuern", "Umwelt"]
spd_page_num = 0
while spd_page_num < len(spd_pages):
    try:
        driver.find_element_by_link_text(spd_pages[spd_page_num]).click()
    except NoSuchElementException:
        WebDriverWait(driver, 12).until(EC.element_to_be_clickable((By.LINK_TEXT, spd_pages[spd_page_num]))).click()
    print(driver.current_url)
    print(scrape_spd(), "\n")
    spd_page_num += 1
    driver.execute_script("window.history.go(-1)")

try:   # done separately because the link for 'Grundrente' was not in the bottom summary with the others
    driver.find_elements_by_xpath('//a[contains(@href,"/standpunkte/grundrente/")]')[1].click()
except (NoSuchElementException, ElementNotInteractableException):
    WebDriverWait(driver, 12).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@href,"/standpunkte/grundrente/")]')))[1].click()
print(scrape_spd())

print("SPD complete")
driver.close()


# web scrape CDU
print("Scraping CDU...\n")
driver.get("https://www.cdu.de/themen")


def scrape_cdu():
    cdu_word_list = []

    cdu_url = driver.current_url
    cdu_page_title = cdu_pages[cdu_page_num]

    page_text = WebDriverWait(driver, 12).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="text"]')))

    page_words = page_text.text
    words = page_words.split(" ")
    for word in words:
        word = word.strip(r",.<>'/\|_=?!")
        if word in key_words:
            cdu_word_list.append(word)
            write_to_db_cdu(str(cdu_url), str(cdu_page_title), str(word))
        if word in populism_key_words:
            cdu_word_list.append(word)
            write_to_db_cdu_pop(str(cdu_url), str(cdu_page_title), str(word))
            

    print("URL:", cdu_url)
    print("Page title:", cdu_page_title)
    return len(cdu_word_list)


WebDriverWait(driver, 12).until(EC.element_to_be_clickable((By.ID, "edit-submit-all"))).click()
# click to dismiss pop-up

cdu_pages = ["Arbeit und Soziales", "Außen- und Verteidigungspolitik", "Bildung und Forschung", "Demografie",
             "Energiepolitik", "Entwicklungs- und Menschenrechtspolitik", "Europapolitik und Euro",
             "Familie, Frauen, Jugend und Senioren", "Gesundheit und Pflege", "Haushalt, Finanzen, Steuern",
             "Innere Sicherheit und Rechtspolitik", "Integration, Zuwanderung und Aussiedler", "Kommunalpolitik, Ehrenamt und Sport",
             "Kultur, Medien und Netzpolitik", "Landwirtschaft und ländlicher Raum", "Menschen mit Behinderungen/Inklusion",
             "Umwelt, Natur und Klimaschutz", "Verbraucherschutz", "Verkehr, Bau und Infrastruktur", "Wirtschaft"]
cdu_page_num = 0

while cdu_page_num < len(cdu_pages):
    try:
        driver.find_element_by_link_text(cdu_pages[cdu_page_num]).click()
    except NoSuchElementException:
        WebDriverWait(driver, 12).until(EC.element_to_be_clickable((By.LINK_TEXT, "Arbeit und Soziales"))).click()
    print(scrape_cdu())
    cdu_page_num += 1
    driver.execute_script("window.history.go(-1)")
print("Done")

print("CDU Complete")
driver.close()
