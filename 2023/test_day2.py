from day2 import *

class TestParse:
    def test_draw_max_0(self):
        assert get_draw_max([' 3 blue, 4 red', ' 1 red, 2 green, 6 blue', ' 2 green']) \
            == {'red': 4, 'green': 2, 'blue': 6}

    def test_draw_max_1(self):
        assert get_draw_max(['0 blue, 1 red']) \
            == {'red': 1, 'green': 0, 'blue': 0}

class TestPowers:
    def test_