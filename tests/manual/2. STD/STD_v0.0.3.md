STD Version: 1.0
Author: Michael Shults
Date: 05/06/2025

## Introduction
This STD is about testing the v0.0.3 version of our app for immediate bugs or problems. 
This STD is based on tests/manual/STP/test_plan_v2.md.
Testing results recorded in tests/manual/STR/STR_v0.0.3.md

## Features to be tested

**UI - Index Page:**
- Load page
- Display items from database on page
- Add item functionality  


## Static test data for v0.0.3
- **Populated Database**
    - **TestDatabase:** `database/db.sqlite` 
    - **UnmodifiedDatabase:** `test_databases_read_only/db.sqlite`  
        - **Database Schema:** `(URL, Title)`  
        - **Rows:** ("www.google.com","google"), ("www.wikipedia.com", "wikipedia")
- **Data for 'add item' functionality:**
    1. URL = "www.microsoft.com", title = "microsoft"

## Precondition For TC01-TC05
To ensure consistent test data between runs, before executing each test case:
1. Delete **TestDatabase**
2. Place an unmodified copy of the file **UnmodifiedDatabase** inplace of it.

## Test Cases - Regression
**TC01:**
- **Title:** Load index page
- **STP Features**: 1, 4
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


---

## Test Cases - New

**TC02:**
- **Title:** Add item - Title and URL
- **STP Features:** 4, 5
- **Priority**: High
- **Steps:** 
    1. Open localhost:5000 in the browser
    2. Fill in URL = "www.microsoft.com", title = "microsoft"
    3. Click the 'add URL' button
- **Expected Result:**
    1. Page reloads with `status 200` with no error in console
    2. New entry is now visible
    3. No other elements change

---

**TC03:**
- **Title:** Add item - Title and no URL
- **STP Features:** 4, 5
- **Priority**: Medium
- **Steps:** 
    1. Open localhost:5000 in the browser
    2. Fill in title = "facebook", leave URL blank
    3. Click the 'add URL' button
- **Expected Result:**
    1. Page reloads with `status 200` with no error in console
    2. New entry is now visible (just the title)
    3. No other elements change

---

**TC04:**
- **Title:** Add item - URL and no title
- **STP Features:** 4, 5
- **Priority**: Medium
- **Steps:** 
    1. Open localhost:5000 in the browser
    2. Fill in URL = "www.facebook.com", leave title blank
    3. Click the 'add URL' button
- **Expected Result:**
    1. Page reloads with `status 200` with no error in console
    2. New entry is now visible (just the URL)
    3. No other elements change

---

**TC05:**
- **Title:** Add item - no URL and no title
- **STP Features:** 4, 5
- **Priority**: Medium
- **Steps:** 
    1. Open localhost:5000 in the browser
    2. Leave title and URL blank
    3. Click the 'add URL' button
- **Expected Result:**
    1. Page reloads with `status 200` with no error in console
    2. A blank line was visibly added (empty URL, empty title)
    3. No other elements change


---


### Environment
- OS: Windows 11 Home 24H2, 26100.4202
- Browsers:
    - Chrome: version 137.0.7151.69 (Official Build) (64-bit)
    - Firefox: version 139.0.1 (64-bit)
    - Opera One: version 119.0.5497.56
    - Edge: version 137.0.3296.58 (Official build) (64-bit)
- App Version: 0.0.3
- Commit Hash: 6c3a420


---

## For Reference (from the STP):
### Features that will be tested
1. Basic page loading
2. Menu and internal links
3. External links to other websites
4. CRUD functionality of the main app, from the UI side
5. API calls (/add, /delete, etc.)