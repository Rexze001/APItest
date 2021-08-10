import json
import requests
import pytest


class TestLever:
    api_Url = "http://localhost:8072/api/lever/total"

    @pytest.mark.parametrize('classA,classB,lever', [
        [80, 160, 'Invalid result!'],
        [50, 150, 'Lever A'],
        [50, -15, 'Wrong number!'],
        [-50, 15, 'Wrong number!'],
        [75, 25, 'Lever B'],
        [0, 0, 'Lever C']
    ])
    def test_leverToal(self, classA, classB, lever):
        url = self.api_Url + "?classA={}&classB={}".format(classA, classB)
        r = requests.get(url)
        assert r.text == lever
        print("运行结束。。。")
