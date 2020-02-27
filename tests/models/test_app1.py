import pytest
from src.models.app1 import App1

def test_sample(mocker):
    responseMock = mocker.Mock()
    responseMock.status_code = 404
    responseMock.text = '127.0.0.1'

    mocker.patch('requests.get').return_value = responseMock

    actual = App1.sample()
    assert actual['statusCode'] == 404
    assert actual['ip'] == '127.0.0.1'