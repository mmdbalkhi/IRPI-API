from IRIP.utils import find_img_date, search_with_regex


def test_find_img_date():
    assert not find_img_date(img_name="test")
    assert find_img_date(img_name="azadi_tower")


def test_search_with_regex():
    assert not search_with_regex(name="test")
