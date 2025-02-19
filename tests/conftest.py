import pytest


@pytest.fixture
def coll():
    return ["mom", "like", "apple"]


@pytest.fixture
def testing_masks():
    return "1596832323455199"


@pytest.fixture
def testing_card_number():
    return "73654108430135874305"


@pytest.fixture
def testing():
    return "2018-07-11T02:26:18.671407"


@pytest.fixture
def test_sort():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
