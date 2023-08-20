import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import logging
import re
import csv

# URL вашего сайта
website_url = 'https://www.votpusk.ru'
# Максимальная глубина сканирования
max_depth = 2

# Список ссылок или паттернов, которые нужно игнорировать
ignore_list = [
    r'https://votpusk\.ru/pattern/\d+'
]

# Компилируем регулярные выражения для паттернов ссылок
ignore_patterns = [re.compile(pattern) for pattern in ignore_list]

# Конфигурация логгера
logging.basicConfig(filename='scan_results.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Путь к файлу для сохранения результатов в формате CSV
csv_file = 'scan_results.csv'

# Глобальная переменная для счетчика ошибок
error_count = 0


# Функция для проверки ссылок
def check_links(url, depth=0):
    global error_count  # Используем глобальную переменную для счетчика ошибок
    try:
        response = requests.get(url, allow_redirects=False)
        response.raise_for_status()  # Генерировать исключение в случае ошибки HTTP
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            links = soup.find_all('a')
            for link in links:
                href = link.get('href')
                if should_ignore_link(href):
                    continue
                if href.startswith('/'):
                    # Если ссылка относительная, добавляем ее к базовому URL
                    href = website_url + href
                check_status_code(href, link)
                if depth < max_depth:
                    check_links(href, depth + 1)
        elif response.status_code == 301:
            new_url = response.headers['Location']
            print(f'Redirected to: {new_url}')
            check_links(new_url, depth)
        else:
            error_count += 1  # Увеличиваем счетчик ошибок
            error_message = f'Error {response.status_code} found at {url} (Error #{error_count})'
            logging.error(error_message)
            print(error_message)
    except requests.exceptions.RequestException as e:
        error_count += 1  # Увеличиваем счетчик ошибок
        error_message = f'Error connecting to {url}: {e} (Error #{error_count})'
        logging.error(error_message)
        print(error_message)
    except Exception as e:
        error_count += 1  # Увеличиваем счетчик ошибок
        error_message = f'Error checking links: {e} (Error #{error_count})'
        logging.error(error_message)
        print(error_message)


# Функция для проверки кода ответа ссылки и вывода информации о ней
def check_status_code(url, link):
    global error_count  # Используем глобальную переменную для счетчика ошибок
    try:
        response = requests.get(url, allow_redirects=False)
        response.raise_for_status()  # Генерировать исключение в случае ошибки HTTP
        if response.status_code >= 400:
            error_count += 1  # Увеличиваем счетчик ошибок
            error_message = f'Error {response.status_code} found at {url} (Error #{error_count})'
            logging.error(error_message)
            print(error_message)
            print(f'Location: {link}')
            save_to_csv(url, link)
    except requests.exceptions.RequestException as e:
        error_count += 1  # Увеличиваем счетчик ошибок
        error_message = f'Error connecting to {url}: {e} (Error #{error_count})'
        logging.error(error_message)
        print(error_message)
    except Exception as e:
        error_count += 1  # Увеличиваем счетчик ошибок
        error_message = f'Error checking status code: {e} (Error #{error_count})'
        logging.error(error_message)
        print(error_message)


# Функция для проверки, нужно ли игнорировать ссылку
def should_ignore_link(url):
    for pattern in ignore_patterns:
        if pattern.match(url):
            return True
    return False


# Функция для сохранения результатов в формате CSV
def save_to_csv(url, link):
    global error_count  # Используем глобальную переменную для счетчика ошибок
    try:
        with open(csv_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([url, link])
    except Exception as e:
        error_count += 1  # Увеличиваем счетчик ошибок
        error_message = f'Error saving to CSV: {e} (Error #{error_count})'
        logging.error(error_message)
        print(error_message)


# Запускаем проверку ссылок на странице с использованием многопоточности
def run_check_links():
    with ThreadPoolExecutor() as executor:
        executor.submit(check_links, website_url)


# Запускаем скрипт
run_check_links()
