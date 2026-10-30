import sys
from urllib.request import urlopen
from html.parser import HTMLParser


class LicznikLinkow(HTMLParser):
    def __init__(self):
        super().__init__()
        self.licznik = 0

    def handle_starttag(self, tag, attrs):
        if tag == "a" and "href" in dict(attrs):
            self.licznik += 1


if len(sys.argv) != 2:
    print("Użycie: python zadanie37.py https://example.com")
else:
    with urlopen(sys.argv[1]) as strona:
        kodowanie = strona.headers.get_content_charset() or "utf-8"
        tekst = strona.read().decode(kodowanie, errors="replace")

    parser = LicznikLinkow()
    parser.feed(tekst)

    print("Liczba linków:", parser.licznik)

