
# ChatGPTJailbreakFinder

A workflow that searches for the best current ChatGPT Jailbreaks by performing the following steps: (1) Accessing the website https://www.jailbreakchat.com/ and filtering the list by JB score, parsing the top 10 prompts, and sending them to a Google Sheet. (2) Rating each prompt's effectiveness by loading the prompt into a fresh thread of ChatGPT, and asking ChatGPT if it would do anything unethical. A prompt is considered a good jailbreak if ChatGPT answers affirmatively. (3) After rating each jailbreak, the 3rd component orders them in the Google Sheet and ensures that the sheet is updated with the best jailbreaks every hour.
## Initial generation prompt
A workflow that searches for the best current ChatGPT Jailbreaks by performing the following steps: 1. Access the website https://www.jailbreakchat.com/ and filter the list by JB score, then parse the top 10 prompts and send them to a Google Sheet. 2. Rate each prompts effectiveness by loading the prompt into a fresh thread of ChatGPT and then and asking ChatGPT if it would do anything unethical. If it answered yes or in the affimrative, that would be a good jailbreak. 3. Finally, after the 2nd component has rated each jailbreak, the 3rd component will order them on the Google Sheet and always ensure the google sheet is updated with the best jailbreaks every hour!

## Authors: 
- yWorkflows
- DragonDreamweaver#8808
        