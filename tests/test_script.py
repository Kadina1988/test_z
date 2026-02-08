import pytest 
import tempfile
import csv 
from pathlib import Path

from script import parse_csv, prepare_report

def test_parse_csv_with_valid_file():
    csv_file_path = create_sample_csv()
    result = parse_csv([csv_file_path])
    expected = [
        {'country': 'United States', 'year': '2023', 'gdp': '25462', 'gdp_growth': '2.1', 'inflation': '3.4', 'unemployment': '3.7', 'population': '339'}
    ]
    assert result == expected


def test_parse_csv_when_file_not_found():
        with pytest.raises(FileNotFoundError):
            parse_csv(['expample.csv'])


def test_prepare_report():
    data = [
        {'country': 'United States', 'year': '2023', 'gdp': '25462', 'gdp_growth': '2.1', 'inflation': '3.4', 'unemployment': '3.7', 'population': '339'}
    ]
    expect = [['United States', 25462]]
    result = prepare_report(data, 'gdp')
    assert result == expect 


def test_prepare_report_when_nonexist_key():
     data = [
        {'country': 'United States', 'year': '2023', 'gdp': '25462', 'gdp_growth': '2.1', 'inflation': '3.4', 'unemployment': '3.7', 'population': '339'}
    ]
     with pytest.raises(KeyError):
          prepare_report(data, 'error_key')
         


def create_sample_csv():
    """Создает мок csv файл"""
    temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, newline='', suffix='.csv')  
    writer = csv.writer(temp_file)
    writer.writerow(['country', 'year', 'gdp', 'gdp_growth', 'inflation', 'unemployment', 'population'])  
    writer.writerow(['United States', '2023', '25462', '2.1', '3.4', '3.7', '339'])
    temp_file.close()
    return temp_file.name