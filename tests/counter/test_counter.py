from src.counter import count_ocurrences


def test_counter():
    assert count_ocurrences("src/jobs.csv", "exceptional") == 299
