## BUG ID
BUG-010

## Bug Title
Add Link - no error for missing URL when both title and URL empty

## Summary
In the 'Add Link' form, if both 'Title' and 'URL' fields are empty, the spec (`spec/visit_later_spec.md`) requires missing field errors to be displayed simultaneously for both fields. However, the validation message is only displayed for the 'Title' field.

## Date Reported
09/07/2025

## Reported By
Michael Shults

## Status
Closed - 11/07/2025 - no longer considered a bug, due to spec change from v1.0 to v1.1. There is a technical limitations on displaying browser native validation tooltips / popups for more than one field at the same time.

## Linked Test Cases
- TC05 - Add Link, Title empty, URL empty
- STD File: 'STD_v0.0.5-pre.md'

## Steps to Reproduce:
For each test case:
1. Run 'scripts/reset_test_database.ps1' to reset test database.
2. Open `localhost:5000` in the browser.
3. Make sure the 'Title' and 'URL' text fields in the 'Add Link' form are empty
4. Click the 'Add Link' button and observe what happens next.

## Expected Results
Page doesn't reload. Two browser native validation messages appear: one below the
'Title' field and one below the 'URL' field, indicating the field is missing. 

## Actual Results
Page doesn't reload. The native error message / tooltip appears only below the 'Title' field.

## Environment
- App Version: 0.0.5-pre
- Browser: Chrome, Firefox, Opera, Edge (latest versions)

## Severity and Priority
- Severity: Low
- Priority: Low  
- Severity and priority are low, since once the user fills in the 'Title' field, according to the error, and tries to submit the form again, they are shown an error indicating a missing URL. This still results in the user understanding that both fields need to be filled, and form submission is prevented.