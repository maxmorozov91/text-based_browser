import bs4

with open("/home/maxmorozov91/Repositories/text-based_browser/test_html_doc.txt", "r") as file:
    html_doc = file.read()

soup = bs4.BeautifulSoup(html_doc, "html.parser")

# print(soup.prettify())

# print(soup.title, soup.title.name, soup.title.string, soup.title.parent.name, sep="\n")

# print(soup.p)

for link in soup.find_all("a"):
    print(link.get("href"))