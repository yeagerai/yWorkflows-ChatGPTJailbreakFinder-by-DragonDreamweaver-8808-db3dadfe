
import os
import requests
from typing import Dict, List, Optional
from bs4 import BeautifulSoup
from google.oauth2 import service_account
from googleapiclient.discovery import build

import yaml
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from core.abstract_component import AbstractComponent


class WebScraperInputDict(BaseModel):
    URL: str
    JB_score_threshold: int


class WebScraperOutputDict(BaseModel):
    top_prompts: List[Dict]


class WebScraper(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()
        with open(self.component_configuration_path(), "r", encoding="utf-8") as file:
            yaml_data = yaml.safe_load(file)
        self.google_sheet_id: str = yaml_data["parameters"]["google_sheet_id"]
        self.sheet_name: str = yaml_data["parameters"]["sheet_name"]
        self.google_credentials: Optional[str] = os.environ.get(
            yaml_data["parameters"]["google_credentials"]
        )

    def transform(
        self, args: WebScraperInputDict
    ) -> WebScraperOutputDict:
        # Fetch the HTML content from the URL
        response = requests.get(args.URL)
        soup = BeautifulSoup(response.text, "html.parser")

        # Parse the HTML and extract the prompts with their corresponding JB scores
        prompts = soup.select("table tr > td:nth-child(1)")
        JB_scores = soup.select("table tr > td:nth-child(2)")

        # Filter and select the top 10 prompts based on the JB score threshold
        top_prompts = []
        for prompt, score in zip(prompts, JB_scores):
            if len(top_prompts) >= 10:
                break
            elif int(score.text.strip()) >= args.JB_score_threshold:
                top_prompts.append({"prompt": prompt.text.strip(), "score": int(score.text.strip())})

        # Send the top 10 prompts to the specified Google Sheet
        if self.google_credentials:
            credentials = service_account.Credentials.from_service_account_file(
                self.google_credentials
            )
            service = build("sheets", "v4", credentials=credentials)
            body = {"values": [prompt.values() for prompt in top_prompts]}
            range_name = f"{self.sheet_name}!A1:B{len(top_prompts)}"
            service.spreadsheets().values().update(
                spreadsheetId=self.google_sheet_id,
                range=range_name,
                valueInputOption="RAW",
                body=body,
            ).execute()

        return WebScraperOutputDict(top_prompts=top_prompts)


load_dotenv()
web_scraper_app = FastAPI()


@web_scraper_app.post("/transform/")
async def transform(
    args: WebScraperInputDict,
) -> WebScraperOutputDict:
    web_scraper = WebScraper()
    return web_scraper.transform(args)

