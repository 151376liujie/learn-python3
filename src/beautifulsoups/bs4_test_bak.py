from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    response = requests.get("http://www.baidu.com")
    print(response.content)
    parser = BeautifulSoup(response.content, "html.parser")
    for inputbox in parser.find_all(name="input", attrs={'type': 'submit'}):
        print(inputbox)
