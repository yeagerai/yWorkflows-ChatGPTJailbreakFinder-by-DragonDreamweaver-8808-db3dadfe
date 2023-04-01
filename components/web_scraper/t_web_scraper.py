
# test_web_scraper.py

import pytest
import requests
from typing import Dict, List
from pydantic import BaseModel
from bs4 import BeautifulSoup
from unittest.mock import MagicMock, patch

from .web_scraper import WebScraper, WebScraperInputDict, WebScraperOutputDict


test_cases = [
    (
        {
            "URL": "https://example.com",
            "JB_score_threshold": 50,
        },
        [
            {"prompt": "sample prompt 1", "score": 90},
            {"prompt": "sample prompt 2", "score": 80},
        ],
    ),
    (
        {
            "URL": "https://other-example.com",
            "JB_score_threshold": 70,
        },
        [
            {"prompt": "other prompt 1", "score": 100},
        ],
    ),
]

@pytest.mark.parametrize("args, expected_output", test_cases)
def test_transform(args: Dict, expected_output: List[Dict]):
    with patch("requests.get") as mock_get:
        mock_get.return_value.text = """
        <table>
            <tr><td>sample prompt 1</td><td>90</td></tr>
            <tr><td>sample prompt 2</td><td>80</td></tr>
            <tr><td>sample prompt 3</td><td>40</td></tr>
            <tr><td>other prompt 1</td><td>100</td></tr>
            <tr><td>other prompt 2</td><td>60</td></tr>
        </table>
        """

        input_data = WebScraperInputDict(**args)
        expected_output_data = WebScraperOutputDict(top_prompts=expected_output)

        web_scraper = WebScraper()
        
        with patch.object(web_scraper, "google_credentials", new=None):
            actual_output_data = web_scraper.transform(input_data)

        assert actual_output_data == expected_output_data
