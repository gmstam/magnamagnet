from bs4 import BeautifulSoup
import argparse
from prettytable import PrettyTable

def normalize_str_with_emoji(text: str):
   return text.encode('latin').decode('utf-8')

parser = argparse.ArgumentParser(
                    prog='MagnaMagnetFrom1337x',
                    description='Search torrent file',
                    epilog='Text at the bottom of help')
parser.add_argument('-k', '--key', required=True)     
args = parser.parse_args()

key = args.key

search_key = key.strip().replace(' ', '+')

# rt = RequestsTor(tor_ports=(9050,), tor_cport=9051)
# url = f'https://1337x.to/search/{search_key}/1/'
# r = rt.get(url)
# html = r.text

html = '''
<table class="table-list table table-responsive table-striped">
              <thead>
                <tr>
                  <th class="coll-1 name">name</th>
                  <th class="coll-2">se</th>
                  <th class="coll-3">le</th>
                  <th class="coll-date">time</th>
                  <th class="coll-4"><span class="size">size</span> <span class="info">info</span></th>
                  <th class="coll-5">uploader</th>
                </tr>
              </thead>
              <tbody>
                                <tr>
                  <td class="coll-1 name"><a href="/sub/54/0/" class="icon"><i class="flaticon-h264"></i></a><a href="/torrent/5266507/L-Arminuta-2021-dvdrip-x264-ita-ac3-subs-fd-mkv/">L.Arminuta.2021.dvdrip.x264.ita.ac3.subs.fd.mkv</a></td>
                  <td class="coll-2 seeds">10</td>
                  <td class="coll-3 leeches">5</td>
                  <td class="coll-date">May. 25th '22</td>
                  <td class="coll-4 size mob-vip">1.1 GB<span class="seeds">10</span></td>
                  <td class="coll-5 vip"><a href="/user/eXpOrTeRICV/">eXpOrTeRICV</a></td>
                </tr>
                                <tr>
                  <td class="coll-1 name"><a href="/sub/42/0/" class="icon"><i class="flaticon-hd"></i></a><a href="/torrent/5399475/L-Arminuta-2021-iTA-AC3-WebRip-1080p-x264-TBR/">L.Arminuta.2021.iTA.AC3.WebRip.1080p.x264-TBR</a></td>
                  <td class="coll-2 seeds">7</td>
                  <td class="coll-3 leeches">0</td>
                  <td class="coll-date">Sep. 24th '22</td>
                  <td class="coll-4 size mob-uploader">1.6 GB<span class="seeds">7</span></td>
                  <td class="coll-5 uploader"><a href="/user/m1337e/">m1337e</a></td>
                </tr>
                              </tbody>
            </table>
'''

soup = BeautifulSoup(html, 'html5lib')

# First, select the desried table element (the 2nd one on the page)
table = soup.find_all('table', {'class':'table-list table table-responsive table-striped'})[0]

headers = []
rows = []

count_rows = 0

pretty_table = PrettyTable()
for i, row in enumerate(table.find_all('tr')):
    if i == 0:
        table_headers = [str(el.text.strip()) for el in row.find_all('th')]
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

print(pretty_table.get_string(fields=["choice", "name", "se", "le", "size info"]))

user_input = input('Select a torrent... \n')
selection = int(user_input)

print(rows[selection][7])