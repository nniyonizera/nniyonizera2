from src.run import search_str


def test_search_string():
    assert search_str('rebe', 'rebecca') == {'r','b','e'}