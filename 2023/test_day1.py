from day1 import *

class TestSpell:
    def test_spelled_int_0(self):
        assert is_spelled_int('t','xtwox', 1) == '2'

    def test_spelled_int_1(self):
        assert is_spelled_int('t','xtwo', 0) == None

    def test_spelled_int_2(self):
        assert is_spelled_int('e', 'xeerht', 1, reverse=True) == '3'

    def test_spelled_int_3(self):
        assert is_spelled_int('e', 'xeerht', 2, reverse=True) == None

    def test_spelled_int_4(self):
        assert is_spelled_int('t','three1nine', 0) == '3'

    def test_spelled_int_5(self):
        assert is_spelled_int('e','enin1eerht', 0, reverse=True) == '9'
        
class TestFind:
    def test_find_int_0(self):
        assert find_int('two1nine') == '2'

    def test_find_int_1(self):
        assert find_int('enin1eerht', reverse=True) == '9'

        def test_find_int_2(self):
            assert find_int('oneowt', reverse=True) == '2'