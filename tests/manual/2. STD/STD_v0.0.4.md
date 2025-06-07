STD Version: 1.0
Author: Michael Shults
Date: 07/06/2025

## Introduction
This STD is about testing the v0.0.4-pre version of our app for immediate bugs or problems. 
Once all bugs are squashed, we will release it as v0.0.4.
Initial testing was performed by the developer, with only a minor emphasis on edge cases.
This testing cycle will be extensive and will try to cover most edge cases. 
This STD is based on tests/manual/STP/test_plan_v2.md.
Testing results recorded in tests/manual/STR/STR_v0.0.4.md

## Features to be tested

**UI - Index Page:**
- Load page
- Display items from database on page
- Add item functionality and basic validation (empty or whitespace title/url)
- Delete item functionality and basic validation (empty or whitespace title/url, based on radio item choice)


## Static test data for v0.0.4
- **Populated Database**
    - **TestDatabase:** `database/db.sqlite` 
    - **UnmodifiedDatabase:** `test_databases_read_only/db.sqlite`  
        - **Database Schema:** `(id, URL, Title)`
            - id (autoincrement PK) is present but not visible in UI or used in tests   
        - **Rows:** ("www.google.com","google"), ("www.wikipedia.com", "wikipedia")

## Precondition For TC01 - TC13
To ensure consistent test data between runs, before executing each test case:
1. Delete **TestDatabase**
2. Place an unmodified copy of the file **UnmodifiedDatabase** inplace of it.

## Precondition For TC02 - TC13
All tests assume the browser is open on `localhost:5000`

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
            3. 'Delete URL' button
            4. Radio input: 
                1. Legend: 'Delete by fields:'
                2. 3 radio options with the labels ('Title', 'URL', 'Title and URL')

---


## Test Cases - New
**Note:** Adding validation to the add-item functionality requires reformulation of previouly defined test cases.
Therefore, these are considered 'New' test cases.

**TC02:**
- **Title:** Add item - Title and URL
- **STP Features:** 4
- **Priority**: High
- **Steps:** 
    1. Fill in URL = "www.microsoft.com", title = "microsoft"
    2. Click the 'add URL' button
- **Expected Result:**
    1. Page reloads with `status 200` with no error in console
    2. New entry is now visible
    3. No other elements (other url list entries, menu, text content, forms) change

---

**TC03:**
- **Title:** Add item - Title and no URL
- **STP Features:** 4
- **Priority**: Medium
- **Steps:** 
    1. Fill in title = "facebook", leave URL blank
    2. Click the 'add URL' button
- **Expected Result:**
    1. No entry added
    2. Page reloads with status 200
    3. A message indicating missing URL appears

---

**TC04:**
- **Title:** Add item - URL and no title
- **STP Features:** 4
- **Priority**: Medium
- **Steps:** 
    1. Fill in URL = "www.facebook.com", leave title blank
    2. Click the 'add URL' button
- **Expected Result:**
    1. No entry added
    2. Page reloads with status 200
    3. A message indicating missing title appears

---

**TC05:**
- **Title:** Add item - no URL and no title
- **STP Features:** 4
- **Priority**: Medium
- **Steps:** 
    1. Leave title and URL blank
    2. Click the 'add URL' button
- **Expected Result:**
    1. No entry added
    2. Page reloads with status 200
    3. A message indicating missing title and URL appears

---

**TC06:**
- **Title:** Delete item - by title - title exists - url field empty
- **STP Features:** 4
- **Priority**: High
- **Steps:** 
    1. Fill in the delete form: title = 'google'
    2. Click the radio button labeled 'Title' under 'Delete by field'
    3. Click the 'Delete URL' button
- **Expected Result:**
    1. Page reloads with status 200
    2. The 'google www.google.com' entry is no longer visible
    3. No other elements (other url list entries, menu, text content, forms) change

---

**TC07:**
- **Title:** Delete item - by title - title doesn't exist - url field empty
- **STP Features:** 4
- **Priority**: Medium
- **Steps:** 
    1. Fill in the delete form: title = 'yahoo'
    2. Click the radio button labeled 'Title' under 'Delete by field'
    3. Click the 'Delete URL' button
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
    3. Click the 'Delete URL' button
- **Expected Result:**
    1. Page reloads with status 200
    2. The 'google www.google.com' entry is no longer visible
    3. No other elements (other url list entries, menu, text content, forms) change


---

**TC09:**
- **Title:** Delete item - by url - url doesn't exist - Title field empty
- **STP Features:** 4
- **Priority**: Medium
- **Steps:** 
    1. Fill in the delete form: url = 'www.yahoo.com'
    2. Click the radio button labeled 'URL' under 'Delete by field'
    3. Click the 'Delete URL' button
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
    3. Click the 'Delete URL' button
- **Expected Result:**
    1. Page reloads with status 200
    2. The 'google www.google.com' entry is no longer visible
    3. No other elements (other url list entries, menu, text content, forms) change

---

**TC11:**
- **Title:** Delete item - by title and url - url exists but title doesn't exist
- **STP Features:** 4
- **Priority**: Medium
- **Steps:** 
    1. Fill in the delete form: url = 'www.google.com', title = 'yahoo'
    2. Click the radio button labeled 'Title and URL' under 'Delete by field'
    3. Click the 'Delete URL' button
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
    3. Click the 'Delete URL' button
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
    3. Click the 'Delete URL' button
- **Expected Result:**
    1. Page reloads with status 200
    2. No change took place

---




### Environment
- OS: Windows 11 Home 24H2, 26100.4202
- Browsers:
    - Chrome: version 137.0.7151.69 (Official Build) (64-bit)
    - Firefox: version 139.0.1 (64-bit)
    - Opera One: version 119.0.5497.56
    - Edge: version 137.0.3296.58 (Official build) (64-bit)
- App Version: 0.0.4-pre
- Commit Hash: 795106f


---


## Features that will be tested
1. Static content and route ('about', 'contact', static content of 'index')
2. Menu and internal links
3. External links to other websites
4. Add and remove items from the urls list using web forms