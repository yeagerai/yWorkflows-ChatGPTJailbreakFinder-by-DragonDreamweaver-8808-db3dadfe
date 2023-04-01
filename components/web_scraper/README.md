markdown
# Component Name

WebScraper

## Description

WebScraper is a Yeager Workflow component designed to scrape a given URL for a specific data structure, filter the data based on a threshold, and store the top results in a Google Sheet. This component is particular useful for web scraping tasks involving standard HTML tables.

## Input and Output Models

### Input Model

WebScraperInputDict - Contains the following fields:
- URL: str - The URL of the webpage to be scraped.
- JB_score_threshold: int - The minimum JB score for a prompt to be included in the results.

### Output Model

WebScraperOutputDict - Contains the following field:
- top_prompts: List[Dict] - A list of dictionaries containing the top 10 prompts and their corresponding JB scores.

## Parameters

- google_sheet_id: str - The ID of the Google Sheet where the results will be written.
- sheet_name: str - The name of the sheet where the results will be written.
- google_credentials: Optional[str] - The path to the Google API credentials file. 

## Transform Function

The `transform()` method of the WebScraper component follows these steps:

1. Fetch the HTML content from the provided URL using the `requests` library.
2. Parse the HTML content with BeautifulSoup, extracting the prompts' text and corresponding JB scores.
3. Filter and select the top 10 prompts based on the provided JB score threshold.
4. If the Google Sheet credentials are provided, send the top 10 prompts to the specified Google Sheet using the Google Sheets API.

## External Dependencies

- requests: Used to fetch the HTML content from the provided URL.
- beautifulsoup4: Used to parse the HTML content and extract the relevant data.
- google.oauth2: Used to authenticate and authorize the Google Sheets API requests.
- googleapiclient: Used to interact with the Google Sheets API.
- yaml: Used to parse the component's configuration file.
- dotenv: Used to load environment variables for sensitive data.
- fastapi: Used to expose the component functionality as a RESTful API.
- pydantic: Used to validate and serialize input and output data models.

## API Calls

The following external API calls are made in this component:

1. Google Sheets API:
   - The `update()` function is used to write the top 10 prompts data to the specified Google Sheet.

## Error Handling

This component does not explicitly handle errors. It relies on the libraries' exceptions and FastAPI's error handling. However, you can add custom error handling tailored to your specific use cases.

## Examples

