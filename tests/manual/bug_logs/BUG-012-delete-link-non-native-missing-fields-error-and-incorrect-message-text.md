## BUG ID
BUG-012

## Bug Title
Delete Link - Non-native missing fields error + incorrect message text

## Summary
In the delete link form, the error messages for input fields are plain text and not customized native browser validation popups/tooltips triggered by the JavaScript `input.reportValidity()` function. In addition the error text does not match spec.

## Date Reported
10/07/2025

## Reported By
Michael Shults

## Status
Closed - fixed 11/07/2025
Note: simultaneously displaying of tooltips/popups for more than one field is no longer needed in the updated spec (v1.1).

## Linked Test Cases
- TC08, TC11, TC16, TC17, TC18 - 'Delete Link' from test cases
- STD File: 'STD_v0.0.5-pre.md'

## Steps to Reproduce:
### Steps
#### For each test case:
1. Run 'scripts/reset_test_database.ps1' to reset test database.
2. Open `localhost:5000` in the browser.
3. In the 'Delete Link' form, select the provided 'Delete by Field' radio option, and fill in 'Title' and 'URL' values.
4. Click the 'Delete Link' button and observe what happens next.

|TC#  |Delete by Field|Title   |      URL       |
|-----|---------------|--------|----------------|
| TC08|Title          |empty   |empty           |
| TC11|URL            |empty   |empty           |
| TC16|Title and URL  |empty   |'www.google.com'|
| TC17|Title and URL  |'google'|empty           |
| TC18|Title and URL  |empty   |empty           |

## Expected Results
|TC#  |Missing Title Error    |Missing URL Error    |
|-----|-----------------------|---------------------|
| TC08|"Title cannot be empty"|N/A                  |
| TC11|N/A                    |"URL cannot be empty"|
| TC16|"Title cannot be empty"|N/A                  |
| TC17|N/A                    |"URL cannot be empty"|
| TC18|"Title cannot be empty"|"URL cannot be empty"|


All messages are rendered with the native browser validation popup/tooltip.  
For TC18 the messages are displayed simultaneously.

## Actual Results
|TC#  |Missing Title Error    |Missing URL Error    |
|-----|-----------------------|---------------------|
| TC08|"Please fill in title."|N/A                  |
| TC11|N/A                    |"Please fill in URL."|
| TC16|"Please fill in title."|N/A                  |
| TC17|N/A                    |"Please fill in URL."|
| TC18|"Please fill in title."|"Please fill in URL."|


All messages are shown below the field or fields as plain text.   
For TC18 the messages are displayed simultaneously.

## Environment
- App Version: 0.0.5-pre
- Browser: Chrome, Firefox, Opera, Edge (latest versions)

## Severity and Priority
- Severity: Medium
- Priority: Medium
- Severity and priority are medium since validation messages are shown, but not in the correct format, according to the app spec. 