import requests
from bs4 import BeautifulSoup

page_content = requests.get("https://www.cs.utexas.edu/people/").content
soup = BeautifulSoup(page_content, "html.parser")

CUSTOMER = "div.view-content div.faculty-and-researchers"
NAME = "div.views-field.views-field-title span.field-content a"
POSITION = "div.views-field.views-field-field-contact-faculty-title div.field-content"
DEPARTMENT = "div.views-field.views-field-field-research-areas div.field-content a"

with open("customers.csv", mode='w', encoding="UTF-8") as file:
    file.write("name,position,departments\n")

    for person in soup.select(CUSTOMER):
        try:
            name = person.select_one(NAME).string
            print(name)
            position = repr(person.select_one(POSITION).string)
            print(position)
            departments = person.select(DEPARTMENT)

            depart = ','.join(repr(e.string) for e in departments)

            # for de in departments:
            #     tmp = repr(de.string)
            #     departs.append(tmp)

            # depart = ', '.join(departs)
            file.write(f"{name},{position},{depart}\n")
        except:
            pass
