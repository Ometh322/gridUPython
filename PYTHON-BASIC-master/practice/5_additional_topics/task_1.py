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


def write_xml(total_mean_temp: Decimal, total_mean_wind_speed: Decimal,
              coldest_place: str, warmest_place: str, windiest_place: str, country_weather) -> None:
    root = ET.Element('weather')
    root.set('country', country_weather.country)
    root.set('date', country_weather.date)
    summary = ET.SubElement(root, 'summary')
    summary.set('mean_temp', str(total_mean_temp))
    summary.set('mean_wind_speed', str(total_mean_wind_speed))
    summary.set('coldest_place', coldest_place)
    summary.set('warmest_place', warmest_place)
    summary.set('windiest_place', windiest_place)
    cities_xml = ET.SubElement(root, 'cities')
    for city_name, weather_info in country_weather.cities.items():
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


def calculate_fields(county_weather) -> None:

    total_mean_temp: Decimal = \
        Decimal(sum(county_weather.total_mean_temp_list) / len(county_weather.total_mean_temp_list)) \
        .quantize(Decimal('1.00'))
    total_mean_wind_speed: Decimal = \
        Decimal(sum(county_weather.total_mean_wind_speed_list) / len(county_weather.total_mean_wind_speed_list)) \
        .quantize(Decimal('1.00'))

    coldest_place: str = ''
    warmest_place: str = ''
    windiest_place: str = ''

    for city, weather_info in county_weather.cities.items():
        if weather_info[0]['mean_temp'] == min(county_weather.total_mean_temp_list):
            coldest_place = city
        if weather_info[0]['mean_temp'] == max(county_weather.total_mean_temp_list):
            warmest_place = city
        if weather_info[1]['mean_wind_speed'] == max(county_weather.total_mean_wind_speed_list):
            windiest_place = city
    write_xml(total_mean_temp, total_mean_wind_speed, coldest_place, warmest_place, windiest_place,
              county_weather)


def weather(path: str, date: str = '2021-09-25', country: str = 'Spain') -> None:
    country_weather: CountryWeather = CountryWeather(country, date)

    for city in sorted(os.listdir(path)):
        temp_list: List[Decimal] = list()
        wind_speed_list: List[Decimal] = list()
        city_weather_path: str = os.path.join(path, city)

        with open(os.path.join(city_weather_path, '2021_09_25.json'), 'r') as weather_json:
            data = json.load(weather_json)
            for weather_hourly in data['hourly']:
                temp_list.append(weather_hourly['temp'])
                wind_speed_list.append(weather_hourly['wind_speed'])

        country_weather.calculate_weather_info(temp_list, wind_speed_list)
        city = city.replace(' ', '_')
        country_weather.calculate_city_info(city, temp_list, wind_speed_list)

    calculate_fields(country_weather)


class CountryWeather:
    def __init__(self, country: str, date: str):
        self.country = country
        self.date = date
        self.total_mean_temp_list: List[Decimal] = list()
        self.total_max_temp_list: List[Decimal] = list()
        self.total_min_temp_list: List[Decimal] = list()
        self.total_max_wind_speed_list: List[Decimal] = list()
        self.total_mean_wind_speed_list: List[Decimal] = list()
        self.cities: Dict[str, List[Dict[str, Decimal]]] = dict()

    def calculate_weather_info(self, temp_list: List[Decimal], wind_speed_list: List[Decimal]):
        self.total_min_temp_list.append(Decimal(min(temp_list)).quantize(Decimal('1.00')))
        self.total_max_temp_list.append(Decimal(max(temp_list)).quantize(Decimal('1.00')))
        self.total_mean_temp_list.append(Decimal(sum(temp_list) / len(temp_list)).quantize(Decimal('1.00')))

        self.total_max_wind_speed_list.append(Decimal(max(wind_speed_list)).quantize(Decimal('1.00')))
        self.total_mean_wind_speed_list.append(Decimal(sum(wind_speed_list) / len(wind_speed_list)).quantize(Decimal('1.00')))

    def calculate_city_info(self, city_name: str, temp_list: List[Decimal], wind_speed_list: List[Decimal]):
        mean_temp: Decimal = Decimal(sum(temp_list) / len(temp_list)).quantize(Decimal('1.00'))
        mean_wind_speed: Decimal = Decimal(sum(wind_speed_list) / len(wind_speed_list)).quantize(Decimal('1.00'))
        min_temp: Decimal = Decimal(min(temp_list)).quantize(Decimal('1.00'))
        max_temp: Decimal = Decimal(max(temp_list)).quantize(Decimal('1.00'))
        min_wind_speed: Decimal = Decimal(min(wind_speed_list)).quantize(Decimal('1.00'))
        max_wind_speed: Decimal = Decimal(max(wind_speed_list)).quantize(Decimal('1.00'))
        self.cities[city_name] = list()
        self.cities[city_name].append({'mean_temp': mean_temp})
        self.cities[city_name].append({'mean_wind_speed': mean_wind_speed})
        self.cities[city_name].append({'min_temp': min_temp})
        self.cities[city_name].append({'min_wind_speed': min_wind_speed})
        self.cities[city_name].append({'max_temp': max_temp})
        self.cities[city_name].append({'max_wind_speed': max_wind_speed})


path_dir: str = os.environ.get('path')
weather(path_dir)
