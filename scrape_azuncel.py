import requests 
from bs4 import BeautifulSoup
import time

value_first_date ="1899-12-31"
value_last_date = "2022-12-13"

def content_soup(value_first_date, value_last_date, value_page):
    URL = "https://www.worldathletics.org/records/all-time-toplists/sprints/100-metres/outdoor/men/senior?regionType=world&timing=electronic&windReading=regular&page=" + value_page + "&bestResultsOnly=false&firstDay=" + value_first_date + "&lastDay=" + value_last_date
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, "html.parser")
    return soup


def content_header():
    results_header = soup.find_all('th')
    for th in results_header:
        mi_texto = th.get_text().strip() + ','
        database_txt.write(mi_texto)


def content_files():
    results_rows = soup.find('table', class_="records-table")
    for rows in results_rows.find_all('tr'):
        for fields in rows.find_all('td'):
            mis_fields = fields.get_text().strip()+ ','
            database_txt.write(mis_fields)
        database_txt.write('\n')

def create_file():
    content_header() 
    for i in range(page):
        content_soup(value_first_date, value_last_date, str(i)) 
        content_files()
        print(time.time())


#Lee parámetros para header y páginas
soup = content_soup(value_first_date, value_last_date,"1")
results_last_page = soup.find('a', class_="btn--number btn--pagination pag--end pag--show" ) 
for last_page in results_last_page:
    value_page = last_page.get_text().strip()
    page = int(value_page)

with open('database.txt', 'w', encoding='utf-8') as database_txt:     
    create_file()
    
    








'''


# soup = BeautifulSoup(page.content, "html.parser")
# def content_files():
#     results_fields = soup.find('table', class_="records-table")
#     for fields in results_fields.find_all('td'):
#         database_txt.write(fields.get_text().strip()+ ',')




MAS LARGO
results = soup.find("table")

python_records = results.find_all(
    "tr", string=lambda text: "/*/" 
)
python_records_elements = [
    tr_element for tr_element in python_records
]

####Título
python_title = python_records_elements[0].find_all("th", string=lambda text: "/*/" )
python_titles_elements = [ th_element for th_element in python_title]
for title_value in python_titles_elements:
    print(title_value.text.strip())

###Registros
for record_element in python_records_elements:
        python_field = results.find_all("td", string=lambda text: "/*/" )
        python_fields_elements = [ td_element for td_element in python_field]
        for field_value in python_fields_elements:
            print(field_value.text.strip())
for record_element in python_records_elements.find.all("td"):
    print(record_element.get_text())
'''


    