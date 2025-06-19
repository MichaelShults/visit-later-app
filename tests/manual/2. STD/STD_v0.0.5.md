STD Version: 1.0
Author: Michael Shults
Date: 17/06/2025

## Introduction
This STD is about testing the v0.0.5-pre version of our app for regressions. I will also be doing an exploratory testing session, mainly for usability and UI/UX. 
This STD is based on tests/manual/STP/test_plan_v2.md.
Testing results are recorded in tests/manual/STR/STR_v0.0.5.md
Exploratory testing is documented in tests/manual/Exploratory/session-002-usability_UI_UX_v0.0.5.md

## Features that will be tested (STP/test_plan_v2.md)
Static content and route ('about', 'contact', static content of 'index') - #1 in STP
View links list, and add and remove items from it using web forms - #4 in STP


## Static test data for v0.0.5
- **Populated Database**
    - **TestDatabase:** `database/db.sqlite` 
    - **UnmodifiedDatabase:** `test_databases_read_only/db.sqlite`  
        - **Database Schema:** `(id, URL, Title)`
            - id (autoincrement PK) is present but not visible in UI or used in tests   
        - **Rows:** ("www.google.com","google"), ("www.wikipedia.com", "wikipedia")

## Precondition For TC01 - TC17
To ensure consistent test data between runs, before executing each test case:
1. Delete **TestDatabase**
2. Place an unmodified copy of the file **UnmodifiedDatabase** in place of it.
Alternatively: You can run scripts/reset_test_database.ps1, which does steps 1 and 2 automatically. 
3. All tests assume the browser is open on `localhost:5000`

## Notes on UI changes:
- For clarity, the 'Add URL' and 'Delete URL' buttons were renamed to 'Add Link' and 'Delete Link' respectively.
- Due to added styling with css, the UI in now centered and aligned, and some design elements are applied. However the content and functionality isn't supposed to be any different.

## Test Cases - Regression
**TC01:**
- **Title:** Load index page
- **STP Features:** 1, 4
- **Based on:** TC01 from `index_about_STD_v1.0.md`
- **Priority:** High
- **Steps:** 
    1. Open `localhost:5000` in the browser
- **Expected Result:**
    1. Page loads with `status 200` and no error in console
    2. Page contains a main menu with `Home` and `About` links
    3. The following elements are visible:
        - **Heading**: "Welcome to Visit Later"
        - **Text**: "Save any url to visit it later"
        - **Populated Database** All rows and columns
        - **Add item form:** 
            1. Textbox with a 'title' label
            2. Textbox with a 'URL' label
            3. 'Add URL' button
        - **Delete item form:** 
            1. Textbox with a 'title' label
            2. Textbox with a 'URL' label
            3. 'Delete Link' button
            4. Radio input: 
                1. Legend: 'Delete by fields:'
                2. 3 radio options with the labels ('Title', 'URL', 'Title and URL')

---

**TC02:**
- **Title:** Add item - Title and URL
- **STP Features:** 4
- **Priority**: High
- **Steps:** 
    1. Fill in URL = "www.microsoft.com", title = "microsoft"
    2. Click the 'Add Link' button
- **Expected Result:**
    1. Page reloads with `status 200` with no error in console
    2. New entry is now visible
    3. No other elements (other url table entries, menu, text content, forms) change

---

**TC03:**
- **Title:** Add item - Title and no URL
- **STP Features:** 4
- **Priority**: Medium
- **Steps:** 
    1. Fill in title = "facebook", leave URL blank
    2. Click the 'Add Link' button
- **Expected Result:**
    1. No entry added
    2. Page reloads with status 200
    3. A message indicating missing URL appears near the URL field.

---

**TC04:**
- **Title:** Add item - URL and no title
- **STP Features:** 4
- **Priority**: Medium
- **Steps:** 
    1. Fill in URL = "www.facebook.com", leave title blank
    2. Click the 'Add Link' button
- **Expected Result:**
    1. No entry added
    2. Page reloads with status 200
    3. A message indicating missing title appears near the Title field.

---

**TC05:**
- **Title:** Add item - no URL and no title
- **STP Features:** 4
- **Priority**: Medium
- **Steps:** 
    1. Leave title and URL blank
    2. Click the 'Add Link' button
- **Expected Result:**
    1. No entry added
    2. Page reloads with status 200
    3. Message indicating missing URL and missing title appear near each field respectively.

---

**TC06:**
- **Title:** Delete item - by title - title exists - url field empty
- **STP Features:** 4
- **Priority**: High
- **Steps:** 
    1. Fill in the delete form: title = 'google'
    2. Click the radio button labeled 'Title' under 'Delete by field'
    3. Click the 'Delete Link' button
- **Expected Result:**
    1. Page reloads with status 200
    2. The 'google www.google.com' entry is no longer visible
    3. No other elements (other url table entries, menu, text content, forms) change

---

**TC07:**
- **Title:** Delete item - by title - title doesn't exist - url field empty
- **STP Features:** 4
- **Priority**: Medium
- **Steps:** 
    1. Fill in the delete form: title = 'yahoo'
    2. Click the radio button labeled 'Title' under 'Delete by field'
    3. Click the 'Delete Link' button
- **Expected Result:**
    1. Page reloads with status 200
    2. No change took place

---

**TC08:**
- **Title:** Delete item - by url - url exists - Title field empty
- **STP Features:** 4
- **Priority**: Medium
- **Steps:** 
    1. Fill in the delete form: url = 'www.google.com'
    2. Click the radio button labeled 'URL' under 'Delete by field'
    3. Click the 'Delete Link' button
- **Expected Result:**
    1. Page reloads with status 200
    2. The 'google www.google.com' entry is no longer visible
    3. No other elements (other url table entries, menu, text content, forms) change


---

**TC09:**
- **Title:** Delete item - by url - url doesn't exist - Title field empty
- **STP Features:** 4
- **Priority**: Medium
- **Steps:** 
    1. Fill in the delete form: url = 'www.yahoo.com'
    2. Click the radio button labeled 'URL' under 'Delete by field'
    3. Click the 'Delete Link' button
- **Expected Result:**
    1. Page reloads with status 200
    2. No change took place

---


**TC10:**
- **Title:** Delete item - by title and url - url and title combination exist in one entry
- **STP Features:** 4
- **Priority**: High
- **Steps:** 
    1. Fill in the delete form: url = 'www.google.com', title = 'google'
    2. Click the radio button labeled 'Title and URL' under 'Delete by field'
    3. Click the 'Delete Link' button
- **Expected Result:**
    1. Page reloads with status 200
    2. The 'google www.google.com' entry is no longer visible
    3. No other elements (other url table entries, menu, text content, forms) change

---

**TC11:**
- **Title:** Delete item - by title and url - url exists but title doesn't exist
- **STP Features:** 4
- **Priority**: Medium
- **Steps:** 
    1. Fill in the delete form: url = 'www.google.com', title = 'yahoo'
    2. Click the radio button labeled 'Title and URL' under 'Delete by field'
    3. Click the 'Delete Link' button
- **Expected Result:**
    1. Page reloads with status 200
    2. No change took place

---

**TC12:**
- **Title:** Delete item - by title and url - title exists but url doesn't exist
- **STP Features:** 4
- **Priority**: Medium
- **Steps:** 
    1. Fill in the delete form: url = 'www.yahoo.com', title = 'google'
    2. Click the radio button labeled 'Title and URL' under 'Delete by field'
    3. Click the 'Delete Link' button
- **Expected Result:**
    1. Page reloads with status 200
    2. No change took place

---

**TC13:**
- **Title:** Delete item - by title and url - title and url don't exist anywhere in the list
- **STP Features:** 4
- **Priority**: Medium
- **Steps:** 
    1. Fill in the delete form: url = 'www.yahoo.com', title = 'yahoo'
    2. Click the radio button labeled 'Title and URL' under 'Delete by field'
    3. Click the 'Delete Link' button
- **Expected Result:**
    1. Page reloads with status 200
    2. No change took place

---

**TC14:**
- **Title:** Delete item - by title and url - title exists, url field empty
- **STP Features:** 4
- **Priority**: High
- **Steps:**
    1. Select 'Title and URL' in the radio box labeled 'Delete by fields:'
    2. Fill in 'google' in the title field of deletion form
    3. Click the 'Delete Link' button to submit the form

- **Expected Result:**
    1. Page reloads
    2. A message indicating missing URL appears near the URL field.

---

**TC15:**
- **Title:** Delete item - by title and url - title field empty, url exists
- **STP Features:** 4
- **Priority**: High
- **Steps:**
    1. Select 'Title and URL' in the radio box labeled 'Delete by fields:'
    2. Fill in 'www.google.com' in the URL field of deletion form
    3. Click the 'Delete Link' button to submit the form
- **Expected Result:**
    1. Page reloads
    2. A message indicating missing title appears near the title field.

---

**TC16:**
- **Title:** A very long input string - pasting into a field - Add link
- **STP Features:** 4 
- **Priority**: Low  
- **Steps:** 
    1. Copy all the text from the file "tests\manual\test_data\very_long_string.txt"
    2. Paste it into the 'Title' field of the "Add Link" form.
    3. Fill in 'www.yahoo.com' into the 'URL' field of the "Add Link" form
    4. Click the "Add Link" button.
    5. Reset database, go to `localhost:5000`
    6. Copy all the text from the file "tests\manual\test_data\very_long_string.txt"
    7. Paste it into the 'URL' field of the "Add Link" form.
    8. Fill in 'yahoo' into the 'URL' field of the "Add Link" form
    9. Click the "Add Link" button.
- **Expected Result:**
    1. Steps 1-4: A new entry is added to the saved links table, with title being the first 100 character of "very_long_string.txt" file contents, and the URL being 'www.yahoo.com' 
    2. Steps 5-9: A new entry is added to the saved links table, with URL being the first 100 character of "very_long_string.txt" file contents, and the title being 'yahoo' 
    3. No other elements (other url table entries, menu, text content, forms) change

---

**TC17:**
- **Title:** A very long input string - pasting into a field - Delete link
- **STP Features:** 4 
- **Priority**: Low  
- **Steps:** 
    1. Copy all the text from the file "tests\manual\test_data\very_long_string.txt"
    2. Paste it into the 'Title' field of the "Delete Link" form
    3. Click the radio button labeled 'Title' under 'Delete by field'
    4. Click the "Delete Link" button.
    5. Reset database, go to `localhost:5000`
    6. Copy all the text from the file "tests\manual\test_data\very_long_string.txt"
    7. Paste it into the 'URL' field of the "Delete Link" form
    8. Click the radio button labeled 'URL' under 'Delete by field'
    9. Click the "Delete Link" button.
- **Expected Result:**
    1. Page reloads with status 200, and no change took place, both for steps 1-4 and 6-9

---




### Environment
- OS: Windows 11 Home 24H2, 26100.4351
- Browsers:
    - Chrome: version 137.0.7151.104 (Official Build) (64-bit)
    - Firefox: version 139.0.4 (64-bit)
    - Opera One: version 119.0.5497.88 (64-bit)
    - Edge: version 137.0.3296.83 (Official build) (64-bit)
- App Version: 0.0.5-pre
- Commit Hash: 677dc3c


---


