from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser") # failas ir privaloma dalis, ?
# print(soup.body) # isspausdins visa body
# print(soup.body.div) # paims pati pirma div is html failo
# print(soup.find("div")) # ras pati pirma div
# print(soup.find_all("div")) # ras visus div
# print(soup.find_all("div")[1]) # paduos antra elementa
# for div in soup.find_all("div"):
#     print(div)
# print(soup.find_all(class_ = "special")) # ras elementa su class special
# print(soup.find(attrs={"data-example": "yes"})) # ras atributa data-example
#--------- ----------- ---------- ---------- ------------ ------------ --------------
# print(soup.select_one("#first")) # paims pirma elementa su id=first
# print(soup.select(".special")) # paims su class=special
# print(soup.select("div")) # paims visus div, ir atiduos kaip masyva
# print(soup.select("[data-example]")) # paims pagal atributa data-example
#--------- ----------- ---------- ---------- ------------ ------------ --------------
# for element in soup.select(".special"): # is elementu su klase special paimt ir atspausdins viduje esanty teksta
#     print(element.get_text())
#     print(element.name) # elemento name
#     print(element.attrs) # elemento attributai
# for element in soup.select("[data-example]"):
#     # print(element.attrs)
#     # print(element["data-example"])
#     print(element.get_attribute_list("data-example")) # atspausdins visu su data-example attribute
#--------- ----------- ---------- ---------- ------------ ------------ --------------
# attribute = soup.select('div')[0]
# print(attribute)
#--------- ----------- ---------- ---------- ------------ ------------ --------------
# print(soup.body.contents) # isspausdins sandara body tago (turinys)
# print(soup.select(".special")[0].parent) # paims teviny elementa
# print(soup.select("li")[0].next_sibling.next_sibling) # paims sekanty sekancio siblinga
# print(soup.select_one("li").find_next_sibling(name="li")) # konreciai nurodyta sibling paduos 
print(soup.find("li").parent.previous_sibling.previous_sibling.h3.get_text())

