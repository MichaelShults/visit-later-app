## BUG ID
BUG-007

## Bug found in exploratory testing session

## Bug Title
Deleting by Title with a very long title, when title doesn't exist in db entry, causes 'Request Entity Too Large' error

## Summary
Filling a very long string in the Title field for the delete form, selecting 'delete by title', then clicking the 'delete url' button (which submits the form) causes a 'Request entity too large error', instead of giving a clear feedback near the deletion form.

## Date Reported
09/06/2025 

## Reported By
Michael Shults

## Status
Open

## Linked Exploratory Session
- 'session-001-delete-edge-cases.md'

## Steps to Reproduce (Run steps 1-5 with A option, then repeat steps 1-5 with B option):
1. Reset database by running 'reset_test_database.ps1'
2. Navigate to 'localhost:5000'
3. Select 'Title' in the radio box labeled 'Delete by fields:'
4. Copy all the text from the file "tests\manual\test_data\very_long_string.txt'
5. Paste it into the 'Title' field
6. Press "Delete URL" to submit the form



**Expected result:**
- The user is not allowed to submit the form if the string is too long
- alternatively, there should be a character limit on the input field.

## Actual Result
- Page redirects to localhost:5000/delete
- A 'Request Entity Too Large' error is displayed


## Environment
- App Version: 0.0.4-pre
- Browser: Chrome version 137.0.7151.69
- OS: Windows 11 Home 24H2, 26100.4202

## Severity and Priority
- Severity: Medium
- Priority: Medium


