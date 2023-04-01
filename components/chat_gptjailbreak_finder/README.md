
# ChatGPTJailbreakFinder

This component is designed to extract the top 10 jailbreaks from a target website and update the Google Sheet with new information. It takes in the target website URL and Google Sheet ID, scrapes the relevant information, and then updates the corresponding Google Sheet with the obtained jailbreak data. Finally, it outputs the updated list of top 10 jailbreaks.

## Initial generation prompt
description: "IOs - 'Inputs: url (str) - the target website URL; google_sheet_id (str)\
  \ - the ID of the\n  Google Sheet used for storing and updating the jailbreak data.\
  \ Outputs: top_jailbreaks\n  (List[str]) - The updated list of top 10 jailbreaks\
  \ from the Google Sheet.'\n"
name: ChatGPTJailbreakFinder


## Transformer breakdown
- Scrape the target website URL to extract top jailbreaks.
- Authenticate and access the Google Sheet using the provided ID.
- Update the jailbreak data in the Google Sheet with the extracted top jailbreaks.
- Retrieve the updated list of top 10 jailbreaks from the Google Sheet.
- Return the updated list of top 10 jailbreaks.

## Parameters
[]

        