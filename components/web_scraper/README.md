
# WebScraper

Scrapes the target website https://www.jailbreakchat.com/ and filters the list by JB score. Parses the top 10 prompts and sends them to the Google Sheet.

## Initial generation prompt
description: Scrapes the target website https://www.jailbreakchat.com/ and filters
  the list by JB score. Parses the top 10 prompts and sends them to the Google Sheet.
name: WebScraper


## Transformer breakdown
- Fetch the HTML content from the URL
- Parse the HTML and extract the prompts with their corresponding JB scores
- Filter and select the top 10 prompts based on the JB score threshold
- Format the top 10 prompts into a list of dictionaries
- Send the top 10 prompts to the specified Google Sheet

## Parameters
[{'name': 'google_sheet_id', 'default_value': '', 'description': 'The ID of the Google Sheet to send the top 10 prompts to.', 'type': 'str'}, {'name': 'sheet_name', 'default_value': 'Sheet1', 'description': 'The name of the sheet within the Google Sheet where the prompts will be sent.', 'type': 'str'}]

        