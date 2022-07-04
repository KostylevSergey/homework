import requests
import json
from pprint import pprint
from ya_disk import YandexDisk

TOKEN = ''

heroes_list = ['Hulk', 'Captain america', 'Thanos']
intelligence_dict = {'Hulk': 0, 'Captain america': 0, 'Thanos': 0}
url = 'https://www.superheroapi.com/api.php/2619421814940190/search/'

def who_is_smarter(dict, list):
    for hero in list:
        hero_dict = json.loads(requests.get(url + hero).content)
        dict[hero] = int(hero_dict['results'][0]['powerstats']['intelligence'])

    smart_hero = ''
    intelligence_hero = 0
    for hero, intelligence in dict.items():
        if intelligence_hero < intelligence:
            intelligence_hero = intelligence
            smart_hero = hero
    return f'Самый умный герой {smart_hero}'




if __name__ == '__main__':
    pprint(who_is_smarter(intelligence_dict, heroes_list))

    ya = YandexDisk(token=TOKEN)
    ya.upload_file_to_disk(disk_file_path='disk:/new/test.txt', filename='test.txt')


