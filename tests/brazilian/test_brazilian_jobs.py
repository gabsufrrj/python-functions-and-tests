from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    jobs = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    for entry in jobs:
        assert ("title" in entry) is True
        assert ("salary" in entry) is True
        assert ("type" in entry) is True
