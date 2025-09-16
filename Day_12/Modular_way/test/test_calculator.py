import datetime 
from age_calculate_in_min.Calculator import age_in_min, year_valid 


def test_is_valid_year():
    current_year = datetime.datetime.today().year
    assert year_valid(2000) is True
    assert year_valid(current_year + 1) is False
    assert year_valid(1800) is False