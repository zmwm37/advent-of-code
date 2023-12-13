import pytest
from day4 import *

def test_search_winners0():
    w = [1, 2, 3]
    h = [4, 6, 8, 10]
    n_winners = search_winners(w, h)
    assert n_winners == 0

def test_search_winners1():
    w = [1, 2, 3]
    h = [2, 4, 6, 8, 10]
    n_winners = search_winners(w, h)
    assert n_winners == 1

def test_search_winners2():
    w = [1, 2]
    h = [2]
    n_winners = search_winners(w, h)
    assert n_winners == 1

def test_search_winners3():
    w = [1, 2]
    h = [1]
    n_winners = search_winners(w, h)
    assert n_winners == 1

def test_search_winners4():
    w = [1, 2, 3, 4]
    h = [1]
    n_winners = search_winners(w, h)
    assert n_winners == 1

def test_search_winners5():
    w = [1, 2, 3, 4]
    h = [2]
    n_winners = search_winners(w, h)
    assert n_winners == 1

def test_search_winners6():
    w = [1, 2, 3, 4]
    h = [3]
    n_winners = search_winners(w, h)
    assert n_winners == 1

def test_search_winners7():
    w = [1, 2, 3, 4]
    h = [3]
    n_winners = search_winners(w, h)
    assert n_winners == 1

def test_search_winners8():
    w = [1, 2, 3, 4, 5]
    h = [1, 5]
    n_winners = search_winners(w, h)
    assert n_winners == 2

def test_search_winners9():
    w = [1, 2, 3, 4, 5]
    h = [2, 4]
    n_winners = search_winners(w, h)
    assert n_winners == 2

def test_search_winners10():
    w = [1, 2, 3, 4, 5]
    h = [1, 2, 3, 4, 5]
    n_winners = search_winners(w, h)
    assert n_winners == 5


def test_search_winners11():
    w = [3, 11, 15, 22, 34, 37, 44, 50, 60, 90]
    H =  [35, 60, 76, 3, 21, 84, 45, 52, 15, 72, 13, 31, 90, 6, 37, 44, 34, 53, 68, 22, 50, 38, 67, 11, 55]
    n_winners = search_winners(w, H)
    assert n_winners == 10