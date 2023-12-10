import re

chenn = "hwhkerhwkrhiddenrendpasjkhkhkhkjhj"

karakte = re.search(r'hidden(.*?)endpas', chenn)

if karakte:
    karakte = karakte.group(1)
    print(f"Karakte nan mitan 'hidden' ak 'endpas' lan se : {karakte}")
