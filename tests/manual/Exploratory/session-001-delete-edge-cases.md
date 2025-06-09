# Exploratory Testing Session Report

**Title:** Explore edge cases of delete item functionality

**Tester:** Michael Shults
**Date:** 09/06/2025
**Timebox:** 20 minutes
**Environment:** 
- App Version: v0.0.4-pre
- Browser: Chrome 137.0.7151.69
- OS: Windows 11 24H2
- Role: App user

## Test Notes
- I reset the database by running the `scripts/reset_test_database.ps1` PowerShell script when I needed a fresh pre-populated database
    - It contains the entries {id PK AUTOINCREMENT, title, url}:
        - {'google', 'www.google.com'}, {'wikipedia', 'www.wikipedia}

## Bugs Found
### **BUG-006:** Delete by 'title and URL' proceeds with only one input filled
**Description:** When "Delete by Fields" is set to "Title and URL", and only one of the fields is filled in (with a Title / URL that exists in the item list), deletion is performed based on the filled in field.
**Expected result:**  An error message for the user and no items are deleted.
**Actual result:** An item is deleted according to the non-empty field.

### **BUG-007:** Deleting by Title with a very long title, when title doesn't exist in db entry, causes 'Request Entity Too Large' error
**Description:** Filling a very long string in the Title field for the delete form, selecting 'delete by title', then clicking the 'delete url' button (which submits the form) causes a server error.
**Expected result:** Redirecting back to 'index', and displaying a more user friendly error near the delete form.
**Actual result:** redirects to 'localhost:5000/delete' and renders a server error:
"Request Entity Too Large
The data value transmitted exceeds the capacity limit."



## Observations
- Bug-006 is high priority, since it involves a destructive action, and user data may be lost.
- Bug-007 is medium priority. It doesn't affect the database, and is outside of usual user interactions.
- Deletion logic needs to be clarified, and valid/invalid input should be well defined, with specified effects and user feedback.

