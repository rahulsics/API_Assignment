import pytest
import requests
from json_checker import Checker
import json

def test_Assignment(set_up, test_data, schema_validate):
    base_Url = set_up
    d = test_data
    r = requests.post(base_Url, data=d)
    checker = Checker(schema_validate)
    valid_sc = json.loads(r.content.decode('utf-8'))
    assert checker.validate(valid_sc) 
    assert r.status_code == 201
    assert r.elapsed.seconds<2
    assert "application/json" in r.headers['Content-Type']
    
    

