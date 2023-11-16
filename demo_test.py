from src.run import search_str


def test_search_string():
    assert search_str('nono', 'norbert') == {'n','o'}