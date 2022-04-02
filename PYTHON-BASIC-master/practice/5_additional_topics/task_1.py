import os
import json
from typing import Dict, List
from decimal import Decimal
import xml.etree.ElementTree as ET
from xml.dom import minidom


def prettify(file_path: str) -> None:
    content: str = ''
    with open(file_path, 'r') as file:
        content = file.read()
    reparsed = minidom.parseString(content)
    pretty_content = reparsed.toprettyxml(indent='   ')
    with open(file_path, 'w') as file:
        file.write(pretty_content)


def weather(path: str, date: str = '2021-09-25', country: str = 'Spain') -> None:
    cities: Dict[str, List[Dict[str, Decimal]]] = dict()
    total_mean_temp_list: List[Decimal] = list()
    total_max_temp_list: List[Decimal] = list()
    total_min_temp_list: List[Decimal] = list()
    total_max_wind_speed_list: List[Decimal] = list()
    total_mean_wind_speed_list: List[Decimal] = list()

    for city in sorted(os.listdir(path)):
        temp_list: List[Decimal] = list()
        wind_speed_list: List[Decimal] = list()
        city_weather_path: str = os.path.join(path, city)

        with open(os.path.join(city_weather_path, '2021_09_25.json'), 'r') as weather_json:
            data = json.load(weather_json)
            for weather_hourly in data['hourly']:
                temp_list.append(weather_hourly['temp'])
                wind_speed_list.append(weather_hourly['wind_speed'])

        mean_temp: Decimal = Decimal(sum(temp_list) / len(temp_list)).quantize(Decimal('1.00'))
        mean_wind_speed: Decimal = Decimal(sum(wind_speed_list) / len(wind_speed_list)).quantize(Decimal('1.00'))
        min_temp: Decimal = Decimal(min(temp_list)).quantize(Decimal('1.00'))
        max_temp: Decimal = Decimal(max(temp_list)).quantize(Decimal('1.00'))
        min_wind_speed: Decimal = Decimal(min(wind_speed_list)).quantize(Decimal('1.00'))
        max_wind_speed: Decimal = Decimal(max(wind_speed_list)).quantize(Decimal('1.00'))
        total_min_temp_list.append(min_temp)
        total_max_temp_list.append(max_temp)
        total_mean_temp_list.append(mean_temp)
        total_max_wind_speed_list.append(max_wind_speed)
        total_mean_wind_speed_list.append(mean_wind_speed)
        city = city.replace(' ', '_')
        cities[city] = list()
        cities[city].append({'mean_temp': mean_temp})
        cities[city].append({'mean_wind_speed': mean_wind_speed})
        cities[city].append({'min_temp': min_temp})
        cities[city].append({'min_wind_speed': min_wind_speed})
        cities[city].append({'max_temp': max_temp})
        cities[city].append({'max_wind_speed': max_wind_speed})

    total_mean_temp: Decimal = Decimal(sum(total_mean_temp_list) / len(total_mean_temp_list))\
        .quantize(Decimal('1.00'))
    total_mean_wind_speed: Decimal = Decimal(sum(total_mean_wind_speed_list) / len(total_mean_wind_speed_list)) \
        .quantize(Decimal('1.00'))
    total_min_temp: Decimal = Decimal(min(total_min_temp_list)) \
        .quantize(Decimal('1.00'))
    total_max_temp: Decimal = Decimal(max(total_max_temp_list)) \
        .quantize(Decimal('1.00'))
    total_max_wind_speed: Decimal = Decimal(max(total_max_wind_speed_list)) \
        .quantize(Decimal('1.00'))

    coldest_place: str = ''
    warmest_place: str = ''
    windiest_place: str = ''

    for city, weather_info in cities.items():
        if weather_info[2]['min_temp'] == total_min_temp:
            coldest_place = city
        if weather_info[4]['max_temp'] == total_max_temp:
            warmest_place = city
        if weather_info[5]['max_wind_speed'] == total_max_wind_speed:
            windiest_place = city

    root = ET.Element('weather')
    root.set('country', country)
    root.set('date', date)
    summary = ET.SubElement(root, 'summary')
    summary.set('mean_temp', str(total_mean_temp))
    summary.set('mean_wind_speed', str(total_mean_wind_speed))
    summary.set('coldest_place', coldest_place)
    summary.set('warmest_place', warmest_place)
    summary.set('windiest_place', windiest_place)
    cities_xml = ET.SubElement(root, 'cities')
    for city_name, weather_info in cities.items():
        city_xml = ET.SubElement(cities_xml, city_name)
        city_xml.set('mean_temp', str(weather_info[0]['mean_temp']))
        city_xml.set('mean_wind_speed', str(weather_info[1]['mean_wind_speed']))
        city_xml.set('min_temp', str(weather_info[2]['min_temp']))
        city_xml.set('min_wind_speed', str(weather_info[3]['min_wind_speed']))
        city_xml.set('max_temp', str(weather_info[4]['max_temp']))
        city_xml.set('max_wind_speed', str(weather_info[5]['max_wind_speed']))

    tree = ET.ElementTree(root)
    tree.write('result.xml')
    prettify('result.xml')


path_dir: str = os.environ.get('path')
weather(path_dir)
