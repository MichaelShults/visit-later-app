## BUG ID
BUG-006

## Bug found in exploratory testing session

## Bug Title
Delete by 'title and URL' proceeds with only one input filled.

## Summary
When "Delete by Fields" is set to "Title and URL", and only one of the fields is filled in with a Title / URL that exists in the item list, deletion is performed based on the filled in field.

## Date Reported
09/06/2025 

## Reported By
Michael Shults

## Status
Closed - fixed 11/06/2025

## Linked Exploratory Session
- 'session-001-delete-edge-cases.md'

## Steps to Reproduce (Run steps 1-5 with A option, then repeat steps 1-5 with B option):
1. Reset database by running 'reset_test_database.ps1'
2. Navigate to 'localhost:5000'
3. Select 'Title and URL' in the radio box labeled 'Delete by fields:'
A. (Title filled, URL missing)
4. Fill in 'google' in the title field of deletion form
5. Click the 'Delete URL' button to submit the form
B. (URL filled, title missing)
4. Fill in 'www.google.com' in the URL field of deletion form
5. Click the 'Delete URL' button to submit the form

**Expected result:**
- Page reloads with status 200
- An error message is displayed to the user indicating 'missing url' (for option A) or 'missing title' (for option B) 
- No items are deleted.

## Actual Result
- Page reloads with status 200
- For options A and B the item "www.google.com google" is deleted


## Environment
- App Version: 0.0.4-pre
- Browser: Chrome version 137.0.7151.69
- OS: Windows 11 Home 24H2, 26100.4202

## Severity and Priority
- Severity: Medium
- Priority: High


