def test_can_be_incremented():
    Counter.increment()
    assert Counter.value == 1

def test_can_be_incremented_multiple_times():
    Counter.increment()
    assert Counter.value == 2

class Counter:
    value = 0
    @staticmethod
    def increment():
        Counter.value += 1
