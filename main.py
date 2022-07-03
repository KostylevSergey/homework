import requests
import json

from pprint import pprint

def test_request():
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url=url)
    response_json = response.json()
    # return response_json
    # pprint(response.json())
    # pprint(response.content)
    contents = response.content
    final_contents = contents.json()
    return final_contents

if __name__ == '__main__':
    # test_request()
    with open('file.json', 'a', encoding='utf-8') as file:
        file.write(test_request())
