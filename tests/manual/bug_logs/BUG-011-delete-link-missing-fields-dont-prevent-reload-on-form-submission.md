## BUG ID
BUG-011

## Bug Title
Delete Link - missing fields don't prevent reload on form submission

## Summary
The 'Delete by Field' option required the chosen text inputs to be non empty before submitting. The spec defines that when they are empty, form submission shouldn't trigger reload, and form validation error messages should be shown below missing fields. However in these cases page does reload before showing the error messages. According to the app spec, validation should happen on the frontend. Reload indicates it may be only happening on the backend.

## Date Reported
10/07/2025

## Reported By
Michael Shults

## Status
Closed - fixed 11/07/2025

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
Page doesn't reload in all the test cases above, and no entry is deleted from the links table. Validation error messages shown.

## Actual Results
Page reloads in all the test cases, and no entry is deleted from the links table. Validation error messages shown.

## Environment
- App Version: 0.0.5-pre
- Browser: Chrome, Firefox, Opera, Edge (latest versions)

## Severity and Priority
- Severity: Medium
- Priority: Medium
- Severity and priority are medium because the validation is still being done on the backend, which prevents accepting invalid input. However the app spec requires validation to be enforced on the front end.