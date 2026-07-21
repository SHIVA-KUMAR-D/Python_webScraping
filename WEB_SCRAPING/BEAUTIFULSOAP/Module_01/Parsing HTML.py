from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html>

<head>
    <title>Online Store</title>
</head>

<body>

    <h1>Electronics Store</h1>

    <div class="product" id="p1">

        <h2>iPhone 16</h2>

        <img src="iphone.jpg"
             alt="iPhone">

        <span class="price">$999</span>

        <a href="/iphone">
            View Product
        </a>

    </div>

    <div class="product" id="p2">

        <h2>Samsung S25</h2>

        <img src="samsung.jpg"
             alt="Samsung">

        <span class="price">$899</span>

        <a href="/samsung">
            View Product
        </a>

    </div>

</body>

</html>
"""

soup = BeautifulSoup(html, "html.parser")
print(f"{type(soup)}, {type(html)}")
print(soup.prettify())
print("=" * 50)
print(soup.title)
print("=" * 50)
print(soup.title.text)
print("=" * 50)
print(soup.h1)
print("=" * 50)
for product in soup.find_all("div", class_="product"):
    print(product.h2.text)
    print(product.find("img")["src"])
    print(product.find("span", class_="price").text)
    print(product.a["href"])
    print("=" * 50)

