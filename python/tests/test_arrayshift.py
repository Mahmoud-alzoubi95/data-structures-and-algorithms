from challenges.array_shift.array_shift import ShiftArray

def test_shift():
    expected=[2,4,5,6,8]
    actual=ShiftArray([2,4,6,8],5)
    assert expected==actual
