from challenges.array_shift.array_shift import ShiftArray

def test_shift():
    expected=[2, 4, 6, 10, 8, 9, 11]
    actual=ShiftArray([2, 4, 6,8, 9, 11],10)
    assert expected==actual
