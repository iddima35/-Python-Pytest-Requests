import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'Your_token'
HEADER = {'Content-Type' : 'application/json','trainer_token' :TOKEN}
TRAINER_ID = '27134'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200
    
    
def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()['data'][0]['trainer_name'] == 'ТагирЯИдуЗаТобой'


@pytest.mark.parametrize('key, value', [('id', TRAINER_ID), ('trainer_name', 'ТагирЯИдуЗаТобой'), ('level', '5')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()['data'][0][key] == value