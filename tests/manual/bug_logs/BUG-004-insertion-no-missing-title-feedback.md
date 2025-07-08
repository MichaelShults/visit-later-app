## BUG ID
BUG-004

## Bug Title
'missing title' user feedback not displayed for insertion with empty title.

## Summary
Page doesn't display a message to the user indicating 'missing title' near the insertion form, when adding an item with a filled in url field but empty title field 

## Date Reported
09/06/2025 

## Reported By
Michael Shults

## Status
Closed - fixed 11/06/2025

## Linked Test Case
- TC04 - Add item - URL and no title
- STD File: 'STD_v0.0.4.md'

## Steps to Reproduce:
1. Reset database by running 'reset_test_database.ps1'
2. Navigate to 'localhost:5000'
3. Enter 'www.facebook.com' into the 'URL' field of the insertion form.
4. Click the 'Add URL' button to submit the form

## Expected Results
- Page reloads with status 200
- No changes in text content, item deletion form, or item list
- An error message indicating 'missing title' is displayed to the user near the insertion form

## Actual Result
- Page reloads with status 200
- No changes to any of the elements on the page - text,  forms, item list
- No error message is displayed to the user for feedback on missing title field 


## Environment
- App Version: 0.0.4-pre
- Browser: Chrome version 137.0.7151.69
- OS: Windows 11 Home 24H2, 26100.4202

## Severity and Priority
- Severity: Medium
- Priority: High


