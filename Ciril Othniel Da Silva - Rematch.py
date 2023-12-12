import re

chenn = "hwhkerhwkrhiddenrendpasjkhkhkhkjhj"

karakte = re.search(r'hidden(.*?)endpas', chenn)

if karakte:
    print(f"Karakte nan mitan 'hidden' ak 'endpas' lan se : {karakte[1]}")
