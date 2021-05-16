import requests
import webbrowser
import bs4
import csv


def build_csv():
    quest_completed = []
    quest_count = 0
    link = "https://www.malayalachalachithram.com/listsongs.php?tot=147&g=1414&p="
    with open("data/dataset.csv", "w") as ifile:
        writer = csv.writer(ifile)
        csv_arr = []
        for i in range(5):
            res = requests.get(link + str(i))
            noStarchSoup = bs4.BeautifulSoup(res.text, "html.parser")
            table = noStarchSoup.findAll("table", {"class": "mdetails"})
            for rows in table:
                for row in rows:
                    row_arr = []
                    cells = row.findAll('td')
                    if(not cells):
                        continue
                    row_arr.append(cells[2].getText())
                    for a in cells[1].find_all('a', href=True):
                        row_arr.append(a.getText()[:-4])
                        row_arr.append(
                            "https://www.malayalachalachithram.com/" + a['href'])
                    csv_arr.append(row_arr)
        writer.writerows(csv_arr)


if __name__ == "__main__":
    build_csv()
