# -*- coding: windows-1251 -*-
# -*- coding: utf-8 -*-

"""
�������� ��������� ������� ������������� ������ �� https://store.steampowered.com/ � ���� ������ �������� ���������
� ������� �������� ���� ��������� �� 1 ��������.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service('/path/to/chromedriver')
driver = webdriver.Chrome(service=service)
driver.get('https://store.steampowered.com/')

search_box = driver.find_element(By.XPATH, '//input[@name="term"]')
search_box.send_keys('���������')
search_box.submit()

titles = driver.find_elements(By.CLASS_NAME, 'title')
game_names = [title.text for title in titles]

for name in game_names:
    print(name)

driver.quit()