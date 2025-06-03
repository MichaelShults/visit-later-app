STD Version: 1.0
Author: Michael Shults
Date: 03/06/2025

## Introduction
This STD is about testing the barebones v0.0.1 version of our app for immediate bugs or problems. 
This STD is based on tests/manual/STP/test_plan_v1.md.
Testing results recorded in tests/manual/STR/STR_v1.0.md

## Feature to be tested
UI issues:
- basic loading (index, about)
- links (main menu, link in pages)
- formatting

## Test Cases
**TC01:**
- Title: load index page
- STP feature number: 1, 4
- Steps: 
    1. Open localhost:5000 in the browser
- Expected Result:
    1. Page loads with status 200 and no error in console
    2. Contains a main menu with Home and About links
    3. index.html non-dynamic elements are all present
    4. Contains dynamically loaded entries from the database (URL, title)
        - Static test database content for v0.0.1 of our app (URL: title) = {www.google.com: google, www.wikipedia.com: wikipedia}
- Priority: High

**TC02:**
- Title: load About page
- STP feature number: 1
- Steps: 
    1. Open localhost:5000/about in the browser
- Expected Result:
    1. Page loads with status 200 and no error in console
    2. Contains a main menu with Home and About links
    3. about.html non-dynamic elements are all present
- Priority: High

**TC03:**
- Title: Main Menu button for current page reloads page
- STP feature number: 2
- Steps (Test both parts, one after the other): 
    - Part 1 - Index page:
        1. Open localhost:5000 in the browser
        2. Make sure the page loads and the main menu with "Home" and "About" is visible
        3. Click the "Home" link
    - Part 2 - About page:
        1. Open localhost:5000/about in the browser
        2. Make sure the page loads and the main menu with "Home" and "About" is visible
        3. Click the "About" link
- Expected Result:
    1. Page reloads, redirecting to the same URL as before for both Home (index) and about pages
- Priority: High

**TC04:**
- Title: Main Menu button for different page redirects correctly
- STP feature number: 2
- Steps (Test both parts, one after the other): 
    - Part 1 - Index page:
        1. Open localhost:5000 in the browser
        2. Make sure the page loads and the main menu with "Home" and "About" is visible
        3. Click the "About" link
    - Part 2 - About page:
        1. Open localhost:5000/about in the browser
        2. Make sure the page loads and the main menu with "Home" and "About" is visible
        3. Click the "Home" link
- Expected Result:
    - Page redirects to the correct page
        - Part 1 - redirect to "About"
        - Part 2 - redirect to "Home" (index)  
- Priority: High

**TC05:**
- Title: Non menu links work in "About" page
- STP feature number: 3
- Steps:  
    1. Open localhost:5000/about in the browser
    2. Make sure the page loads
    3. Locate the following web link texts (full match, case insensitive):
        - "Contact Us": "localhost:5000/contact"
        - "Contact": "localhost:5000/contact"
    4. Click on the link
    5. Observe whether page redirects, and to which URL
    6. Repeat steps 3-5 for each link.
- Expected Result:
    - For each link the browser should redirect to the matching URL
- Priority: Medium



## Environment
- OS: Windows 11 Home 24H2, 26100.4202
- Browsers:
    - Chrome: version 137.0.7151.69 (Official Build) (64-bit)
    - Firefox: version 139.0.1 (64-bit)
    - Opera: Opera One(version: 119.0.5497.56)
    - Edge: version 137.0.3296.58 (Official build) (64-bit)
- App Version: 0.0.1
- Commit Hash: e0a083f


_____
for reference here is a section from my stp:
## Features that will be tested
1. Basic loading of the pages
2. Main menu
3. Links in pages
4. App UI