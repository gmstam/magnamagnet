from prettytable import PrettyTable
from requests_tor import RequestsTor
from bs4 import BeautifulSoup
import argparse
import platform
import pyfiglet

VERSION = '1.0.0'
HTML_LIB = 'html5lib'

def get_ports(operative_system):
  match operative_system:
    case "Darwin": return (9150, 9151)
    case "Linux": return (9050, 9051)
    case _: return (9050, 9051)

def normalize_str_with_emoji(text: str):
   return text.encode('latin').decode('utf-8')

def call_and_get_html(rt: RequestsTor, url: str):
  r = rt.get(url)
  return r.text

ascii_banner = pyfiglet.figlet_format("MagnaMagnet")
print(ascii_banner)
print(f'Version {VERSION}\n')

parser = argparse.ArgumentParser(
                    prog='MagnaMagnetFrom1337x',
                    description='Search torrent file',
                    epilog='Text at the bottom of help')
parser.add_argument('-k', '--key', required=True)     
args = parser.parse_args()

key = args.key
search_key = key.strip().replace(' ', '+')

HOST = 'https://1337x.to'

tor_port, client_port = get_ports(platform.system())

rt = RequestsTor(tor_ports=(tor_port,), tor_cport=client_port)
html = call_and_get_html(rt, f'{HOST}/search/{search_key}/1/')

soup = BeautifulSoup(html, HTML_LIB)

table = soup.find_all('table', {'class':'table-list table table-responsive table-striped'})[0]

headers = []
rows = []
count_rows = 0

pretty_table = PrettyTable()

for i, row in enumerate(table.find_all('tr')):
    if (i >= 10): 
       break
    if i == 0:
        table_headers = [el.text.strip() for el in row.find_all('th')]
        table_headers.insert(0, 'choice')
        table_headers.insert(len(table_headers), 'link')
        headers = table_headers
    else:
        row.find('span', class_="seeds").decompose() # remove unwanted element
        result = [normalize_str_with_emoji(el.text.strip()) for el in row.find_all('td')]
        result.insert(0, str(count_rows))
        
        links = row.find_all('a', href=True)
        for link in links:
          if "/torrent" in link['href']:
            result.insert(len(result), link['href'])
        count_rows = count_rows + 1
        rows.append(result)

pretty_table.field_names = headers
pretty_table.add_rows(rows)
pretty_table.align['name'] = "l"
pretty_table.align['size info'] = "r"

print(f'Search results for: {key}')
print(pretty_table.get_string(fields=["choice", "name", "se", "le", "size info"]))

user_input = input(f'Press a key from 0 to {count_rows - 1} to select a torrent. (CTRL + C to exit)\n')
selection = int(user_input)

key = rows[selection][7]
print('+---------------+')
print(f'Selected => {key} \n')

html = call_and_get_html(rt, f'{HOST}{key}')

soup = BeautifulSoup(html, HTML_LIB)

links = soup.find_all('a', href=True)
for link in links:
  if "magnet" in link['href']:
    print('The magnet link is: \n')
    print(link['href'])
    break

