from challenges.Data_Structures.linked_list.linked_list import Linked_list
# from linked_list.linked_list import *
from challenges.ll_zip.ll_zip import zipLists
import pytest


def test_ziplist(test_zip_test):
    expected = "{ 1 } -> { 2 } -> { 3 } -> { 4 } -> { 5 } -> { 6 } -> { 7 } -> { 8 } -> { 9 } -> { 10 } -> NULL"
    actual = f"{test_zip_test}"
    assert actual == expected

@pytest.fixture
def test_zip_test():
    list=Linked_list()
    list1=Linked_list()
    list2=Linked_list()
    list1.append_node("1")
    list1.append_node("3")
    list1.append_node("5")
    list1.append_node("7")
    list2.append_node("2")
    list2.append_node("4")
    list2.append_node("6")
    list2.append_node("8")
    list2.append_node("9")
    list2.append_node("10")
    a=zipLists(list1,list2)
    return a

