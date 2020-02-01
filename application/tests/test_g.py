import pytest
import africastalking


@pytest.fixture
def sms_setup():
    username = app.config.from_object('config.Config.USERNAME')
    api_key = app.config.from_object('API_KEY')
    africastalking.initialize(username, api_key)
    sms = africastalking.SMS
    return sms

@pytest.fixture
def input_value():
    input = 39
    return input


def test_divisible_by_3(input_value):
    assert input_value % 3 == 0


def test_divisible_by_6(input_value):
    assert input_value % 6 == 0
