from bs4 import BeautifulSoup
from requests import get
import html5lib


class WebSpider:

    def __init__(self):
        self.resposta = 0
        self.tags = 0

    def site(self, link_site):
        self.resposta = get(link_site)
        self.tags = BeautifulSoup(self.resposta.text, "html5lib")
        return self.resposta.ok

    def title_page(self):
        title = self.tags.find("title")
        print(f"Página principal: {title.text}")

    def webcrawler(self):

        allLinks = self.tags.find("html").find_all("a")

        lista_links = []
        for link in allLinks:
            x = str(link).split(" ")
            for y in x:
                if 'href' and '/wiki/' in y:
                    lista_links.append(y)

        lista_wiki = []
        for link in lista_links:
            link = link.split('"')
            for link_valido in link:
                if "/wiki/" in link_valido:
                    lista_wiki.append(link_valido)

        for link in lista_wiki:
            if 'https' in link:
                resposta = get(link)
                tags = BeautifulSoup(resposta.text, "html5lib")
                title = tags.find("title")
                print(f"Página secundária: {title.text}")

            else:
                resposta = get('https://pt.wikipedia.org' + link)
                tags = BeautifulSoup(resposta.text, "html5lib")
                title = tags.find("title")
                print(f"Página secundária: {title.text}")

    def webcrawler_output(self):
        allLinks = self.tags.find("html").find_all("a")

        lista_links = []
        for link in allLinks:
            x = str(link).split(" ")
            for y in x:
                if 'href' and '/wiki/' in y:
                    lista_links.append(y)

        lista_wiki = []
        for link in lista_links:
            link = link.split('"')
            for link_valido in link:
                if "/wiki/" in link_valido:
                    lista_wiki.append(link_valido)

        for link in lista_wiki:
            if 'https' in link:
                resposta = get(link)
                tags = BeautifulSoup(resposta.text, "html5lib")
                title = tags.find("title")
                with open("links_titulos.txt", 'a') as titulos:
                    titulos.write(f"Título = {title.text}\nLink = {link}\n\n")
            else:
                resposta = get('https://pt.wikipedia.org' + link)
                tags = BeautifulSoup(resposta.text, "html5lib")
                title = tags.find("title")
                with open("links_titulos.txt", 'a') as titulos:
                    titulos.write(
                        f"Título = {title.text}\nLink = https://pt.wikipedia.org{link}\n\n")
