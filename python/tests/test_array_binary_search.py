from challenges.array_binary_search.array_binary_search import binary_search

def testone():
    actual=binary_search([4,8,15,16,23,42],15)
    expected=2
    assert actual==expected

def testtow():
    actual=binary_search([4,8,15,16,23,42],10)
    expected= -1
    assert actual==expected


