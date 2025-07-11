## BUG ID
BUG-008

## Bug Title
Incorrect labels and legends for inputs

## Summary
The input labels and the radio fieldset legend in the 'Add Link' and 'Delete Link' forms don't all match the defined labels in terms of capitalization.

## Date Reported
08/07/2025

## Reported By
Michael Shults

## Status
Closed - fixed 11/07/2025

## Linked Test Case
- TC01 - Load index page
- STD File: 'STD_v0.0.5-pre.md'

## Steps to Reproduce:
1. Run 'scripts/reset_test_database.ps1' to reset test database
2. Open `localhost:5000` in the browser

## Expected Results
1. Page loads
2. Page contains a main menu with `Home` and `About` links
3. The following elements are visible:
    - **Heading**: 'Welcome to Visit Later'
    - **Text**: 'Save any link to visit it later'
    - **Populated Database:** All rows and columns
    - **Add Link form:** 
        1. 'Add Link' form Title
        2. Textbox with a 'Title' label just above it
        3. Textbox with a 'URL' label just above it
        4. 'Add Link' button
    - **Delete Link form:** 
        1. 'Delete Link' form Title
        2. Textbox with a 'Title' label just above it
        3. Textbox with a 'URL' label just above it
        4. 'Delete Link' button
        5. Radio input: 
            1. Legend: 'Delete by Field'
            2. 3 radio options with the labels ('Title', 'URL', 'Title and URL')

## Actual Result
The results outlined in Expected Results, except:
- **Add Link form:**
    - Textbox labels have incorrect capitalization:
        - 'title' instead of 'Title' above first textbox
        - 'url' instead of 'URL' above second textbox
- **Delete Link form:**
    - Textbox labels have incorrect capitalization:
        - 'title' instead of 'Title' above first textbox
        - 'url' instead of 'URL' above second textbox
    - Radio fieldset legend has incorrect capitalization
        - 'Delete by field' instead of 'Delete by Field'
    - Radio fieldset labels have incorrect capitalization:
        - 'title' instead of 'Title'
        - 'url' instead of 'URL'


## Environment
- App Version: 0.0.5-pre
- Browser: Chrome, Firefox, Opera, Edge (latest versions)

## Severity and Priority
- Severity: Medium, affects professionalism of app.
- Priority: High, since it's a quick fix, and can improve app polish.


