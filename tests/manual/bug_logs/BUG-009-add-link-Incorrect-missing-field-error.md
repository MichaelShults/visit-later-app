## BUG ID
BUG-009

## Bug Title
Add Link - Incorrect 'missing field' error 

## Summary
In the 'Add Link' form, if one or both of the inputs are empty (both required), 'missing field' error messages are displayed using browser native popups, but the error text is not according to the application spec. 

## Date Reported
09/07/2025

## Reported By
Michael Shults

## Status
Open

## Linked Test Cases
- TC03, TC04, TC05 - 'Add Link' form test cases
    - Note: TC05 not included. TC03 and TC04 capture the bug fully.
- STD File: 'STD_v0.0.5-pre.md'

## Steps to Reproduce:
For each test case:
1. Run 'scripts/reset_test_database.ps1' to reset test database.
2. Open `localhost:5000` in the browser.
3. Fill in the provided 'Title' and 'URL' values in the 'Add Link' form.
4. Click the 'Add Link' button and observe what happens next.

|TC# |Title  |URL            |
|----|-------|---------------|
|TC03|'yahoo'|empty          |
|TC04|empty  |'www.yahoo.com'|



## Expected and Actual Results
|TC# |                                   Expected Result                                                     |                                                     Actual Result                                            |
|----|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
|TC03|Browser native 'missing field' error appears below 'URL' field, with the custom text "URL cannot be empty"    | Browser native 'missing field' error appears below 'URL' field, with the default text "Please fill out this field."  |
|TC04|Browser native 'missing field' error appears below 'Title' field, with the custom text "Title cannot be empty"| Browser native 'missing field' error appears below 'Title' field, with the default text "Please fill out this field."|

Note: The application spec requires overriding of the default error with custom error message.


## Environment
- App Version: 0.0.5-pre
- Browser: Chrome, Firefox, Opera, Edge (latest versions)

## Severity and Priority
- Severity: Low
- Priority: Medium


