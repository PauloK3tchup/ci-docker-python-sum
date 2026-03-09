from app import sumF

def test_sumF():
    assert sumF(1, 2) == 3
    assert sumF(-1, 5) == 4
    assert sumF(0, 0) == 0