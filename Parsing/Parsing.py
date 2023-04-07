# -*- coding: windows-1251 -*-
# -*- coding: utf-8 -*-

"""
Соберите данные с чартов яндекс музыки https://music.yandex.ru/chart
Внимательно изучите источник, посмотрите как именно на сайт приходит информация.
Сохраните данные в json файл в формате:
{
место в чарте: (исполнитель,трек)
}
"""

import requests
import json
from bs4 import BeautifulSoup

response = requests.get('https://music.yandex.ru/chart')
soup = BeautifulSoup(response.content, 'html.parser')
tracks = soup.find_all('div', {'class': 'chart-track'})
chart = []

for i, track in enumerate(tracks):
    artist = track.find('div', {'class': 'chart-track__artists'}).text.strip()
    title = track.find('div', {'class': 'chart-track__name'}).text.strip()
    chart.append((i+1, (artist, title)))
with open('chart.json', 'w', encoding='utf-8') as f:
    json.dump(dict(chart), f, ensure_ascii=False, indent=4)
for position, track in chart:
    print(f'{position}. {track[0]} - {track[1]}')

