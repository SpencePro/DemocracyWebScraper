# DemocracyWebScraper

-- UPDATED 11/21/2020 --

This is a webscraper project I created for political science research purposes. The goal was to assess the extent to
which three German political parties, the AfD, the CDU, and the SPD, are populist and/or concerned with democratic
legitimacy, particularly the AfD. This was done through scraping the websites of these three parties with Selenium, and
counting the occurrence of key words related to democracy, populism, and immigration. The results were tallied in an 
SQLite database, parsed/organized with the Pandas module (Python), and visualized with the Matplotlib module (Python).
For a more detailed explanation of the project, as well as the analysis of the results, see:
Web Scraping Populism Analysis.docx 


The project consists of the following components:

env - The virtual environment containing the modules used in this project; these are: selenium, pandas, matplotlib, and
sqlite3. 

Visuals - The folder where the graphs used in Web Scraping Populism Analysis.docx are stored, including some graphs
unused in the final version. 

Main.py - The main webscraper of the project. Creates the SQLite tables, scrapes the websites, and writes the results
to the database. Selenium was chosen as the scraper of choice due to the high level of interactability and amount of 
JavaScript elements in the three websites, and due to the number of pages that had to be clicked through on each 
website. Selenium gave the greatest flexibility for doing this.

DataAnalysis.py - The file where the database is queried, the results are converted to Pandas dataframes, and Matplotlib
creates the visuals. 

PoliticalPartyWebscraper.db - The database which holds the scraped key words, along with their URL and page title. 
SQLite was used as the database due to being lightweight, and to the low number of items to be placed in it. 

Web Scraping Populism Analysis.docx - The essay explaining my web scraping analysis results. It provides background on
the ares of research, defines the terms used, presents the results of the web scraping in graphs from Visuals, and 
assesses what those results mean. Includes a Works Cited Page, a (rough) translation of the key words into English from 
German, and the raw data tables found in the PoliticalPartyWebscraper.db.

Democracy Web Scraper Jupyter Notebook.ipynb - The Jupyter notebook version of the project's data visualization, which
combines the code and visuals from DataAnalysis.py with the content from Web Scraping Populism Analysis.docx, presented
cleanly in a Jupyter notebook for those who prefer that. 

chromedriver.exe - The webdriver in this project is Chrome Webdriver version 87. If you wish to use this program for
yourself you will need to use the correct webdriver for your browser and version. 

Additional Instructions:

The SQLite table creation in Main.py can be un-commented to create the table. Each website's webscraper may need to be 
run one after the other, by un-commenting and commenting each section as it becomes and ceases to be relevant.
Likewise, the dataframes, Matplotlib visualization code, and other components of the data visualization process in 
DataAnalysis.py can be selectively un-commented and combined with each other in different ways to create various 
graphs. 
