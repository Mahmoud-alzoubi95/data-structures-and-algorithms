import pytest
from challenges.Data_Structures.linked_list.linked_list import *


def test_insert(list_test):
    excpected = "{ 25 } -> { 1 } -> { 0 } -> NULL"
    actual = f"{list_test}"
    assert excpected == actual

def test_includes(list_test):
    inputs = ["m77",55,25]
    actual = [list_test.includes(ele) for ele in inputs]
    excpected = [False, False , True]
    assert excpected == actual

def test_append(append_test):
    excpected = "{ 25 } -> { 1 } -> { 0 } -> { ahmad } -> NULL"
    actual = f"{append_test}"
    assert excpected == actual

def test_insertBefore(before_test):
    excpected = "{ 25 } -> { khaled } -> { 1 } -> { 0 } -> NULL"
    actual = f"{before_test}"
    assert excpected == actual

def test_insertafter(after_test):
    excpected = "{ 25 } -> { 1 } -> { khaled } -> { 0 } -> NULL"
    actual = f"{after_test}"
    assert excpected == actual

def test_kth(k_test):
    excpected = '0'
    actual = f"{k_test}"
    assert excpected == actual

def test_kth_negative_case(k_test_negtivecase):
    excpected = "wrong value"
    actual = f"{k_test_negtivecase}"
    assert excpected == actual

def test_kth_over_case(k_test_overcase):
    excpected = "out of the index"
    actual = f"{k_test_overcase}"
    assert excpected == actual

@pytest.fixture
def list_test():
    linked = Linked_list()
    # linked.append_node()
    linked.insert_node(0)
    linked.insert_node(1)
    linked.insert_node(25)
    # linked.append_node("ahmad")
    # linked.insertBefore(1,"khaled")
    # linked.insertAfter(1,"khaled")
    return linked

@pytest.fixture
def k_test():
    linked = Linked_list()
    # linked.append_node()
    linked.insert_node(0)
    linked.insert_node(1)
    linked.insert_node(25)
    # linked.append_node("ahmad")
    # linked.insertBefore(1,"khaled")
    return linked.kth_from_the_end(0)

@pytest.fixture
def k_test_negtivecase():
    linked = Linked_list()
    linked.insert_node(0)
    linked.insert_node(1)
    linked.insert_node(25)
    # linked.append_node("ahmad")
    # linked.insertBefore(1,"khaled")
    return linked.kth_from_the_end(-3)

@pytest.fixture
def k_test_overcase():
    linked = Linked_list()
    linked.insert_node(0)
    linked.insert_node(1)
    linked.insert_node(25)
    # linked.append_node("ahmad")
    # linked.insertBefore(1,"khaled")
    return linked.kth_from_the_end(6)

@pytest.fixture
def append_test():
    linked = Linked_list()
    # linked.append_node()
    linked.insert_node(0)
    linked.insert_node(1)
    linked.insert_node(25)
    linked.append_node("ahmad")
    return linked



@pytest.fixture
def after_test():
    linked = Linked_list()
    # linked.append_node()
    linked.insert_node(0)
    linked.insert_node(1)
    linked.insert_node(25)
    linked.insertAfter(1,"khaled")
    return linked

@pytest.fixture
def before_test():
    linked = Linked_list()
    # linked.append_node()
    linked.insert_node(0)
    linked.insert_node(1)
    linked.insert_node(25)
    linked.insertBefore(1,"khaled")
    return linked
