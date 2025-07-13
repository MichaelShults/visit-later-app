**STD Version: 1.2**  
**Author**: Michael Shults  
**Date**: 17/06/2025  
**Last Updated**: 03/07/2025  

## Introduction
This STD is about testing `v0.0.5-pre` of our app.  
It is based on `tests/manual/STP/test_plan_v2.md` and on `spec/visit_later_spec.md`.  
Testing results are recorded in `tests/manual/STR/STR_v0.0.5-pre.md  `

## Features that will be tested (STP/test_plan_v2.md)
- Static content of 'index' page and presence of menu links - #1 in STP
- View links list, and add and remove items from it using web forms - #4 in STP

## Features that will not be tested
- 'about' and 'contact' page contents
- Menu functionality

## Static test data for v0.0.5-pre
- **Databases**
    - **TestDatabase:** `database/db.sqlite` 
    - **UnmodifiedDatabase:** `test_databases_read_only/db.sqlite`  
        - **Database Schema:** `(id, url, title)`
            - `id` (autoincrement PK) is present but not visible in UI or used in tests   
        - **Rows:** 
            - `url`='www.google.com', `title` = 'google'
            - `url` = 'www.wikipedia.com', `title` = 'wikipedia'
- **Strings for TC19, TC20:**
    - Can be generated with the Python interpreter by typing the command: `NUMBER_OF_CHARACTERS * 'a'` and then hitting enter.
        - 300 character string = `300 * 'a'`
        - 500 character string = `500 * 'a'`
        - 301 character string = `301 * 'a'`
        - 501 character string = `501 * 'a'`





## Notes on UI changes:
- For clarity, the 'Add URL' and 'Delete URL' buttons were renamed to 'Add Link' and 'Delete Link' respectively.
- Due to added styling with CSS, the UI is now centered and aligned, and some design elements are applied. However the content and functionality aren't supposed to be any different.

## Page Loading
**TC01 - Load index page**
- **STP Features:** 1, 4
- **Based on:** TC01 from `index_about_STD_v1.0.md`
- **Priority:** High
- **Steps:** 
    1. Run 'scripts/reset_test_database.ps1' to reset test database
    2. Open `localhost:5000` in the browser
- **Expected Result:**
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
                2. Three radio options with the labels ('Title', 'URL', 'Title and URL')

---

## Add Link:
### Steps
#### For each test case:
1. Run `scripts/reset_test_database.ps1` to reset test database.
2. Open `localhost:5000` in the browser.
3. Fill in the provided 'Title' and 'URL' values in the 'Add Link' form.
4. Click the 'Add Link' button and observe what happens next.

|TC# |Title  |URL            |Page Reloads?|Entry added?|Missing Title Error?|Missing URL Error?|Priority|
|----|-------|---------------|-------------|------------|--------------------|------------------|--------|
|TC02|'yahoo'|'www.yahoo.com'|      Yes    |    Yes     |          No        |         No       | High   |
|TC03|'yahoo'|empty          |      No     |    No      |          No        |         Yes      | High   |
|TC04|empty  |'www.yahoo.com'|      No     |    No      |          Yes       |         No       | High   |
|TC05|empty  |empty          |      No     |    No      |          Yes       |         Yes      | High   |

#### Column Names Legend:
- Page Reloads? = page reloads after clicking the 'Add Link' button
- Entry added? = A new entry with the 'Title' and 'URL' provided in the test case is now shown in the links table
- Missing Title Error? = A browser native field validation popup is shown just below the 'Title' field, with the message 'Title cannot be empty'
- Missing URL Error? = A browser native field validation popup is shown just below the 'URL' field, with the message 'URL cannot be empty'


## Delete Link - by Title or by URL:
### Steps
#### For each test case:
1. Run `scripts/reset_test_database.ps1` to reset test database.
2. Open `localhost:5000` in the browser.
3. In the 'Delete Link' form, select the provided 'Delete by Field' radio option, and fill in 'Title' and 'URL' values.
4. Click the 'Delete Link' button and observe what happens next.

|TC#  |Delete by Field|Title   |Title exists?|      URL       |URL Exists?|
|-----|---------------|--------|-------------|----------------|-----------|
| TC06|Title          |'google'|Yes          |empty           |   N/A     |
| TC07|Title          |'yahoo' |No           |empty           |   N/A     |
| TC08|Title          |empty   |     N/A     |empty           |   N/A     |
| TC09|URL            |empty   |     N/A     |'www.google.com'|   Yes     |
| TC10|URL            |empty   |     N/A     |'www.yahoo.com' |   No      |
| TC11|URL            |empty   |     N/A     |empty           |   N/A     |

### Expected Results
|TC#  |Page Reloads?|Entries Deleted?                |Missing Title Error?|Missing URL Error?|Priority|
|-----|-------------|--------------------------------|--------------------|------------------|--------|
| TC06|Yes          |Yes:('google', 'www.google.com')|No                  |No                | High   |
| TC07|Yes          |No                              |No                  |No                | Medium |
| TC08|No           |No                              |Yes                 |No                | Medium |
| TC09|Yes          |Yes:('google', 'www.google.com')|No                  |No                | High   |
| TC10|Yes          |No                              |No                  |No                | Medium |
| TC11|No           |No                              |No                  |Yes               | Medium |


#### Column Names Legend:
- Title exists? = a row with a title column that equals to the provided Title exists in `TestDatabase`
- URL exists? = a row with a url column that equals to the provided URL exists in `TestDatabase`
- Page Reloads? = page reloads after clicking the 'Delete Link' button
- Entries Deleted? = All matching entries are deleted and are no longer shown in the links table
- Missing Title Error? = A browser native field validation popup is shown just below the 'Title' field, with the message 'Title cannot be empty'
- Missing URL Error? = A browser native field validation popup is shown just below the 'URL' field, with the message 'URL cannot be empty'


## Delete Link - by Title and URL:
### Steps
#### For each test case:
1. Run `scripts/reset_test_database.ps1` to reset test database.
2. Open `localhost:5000` in the browser.
3. In the 'Delete Link' form:
    1. Select the 'Title and URL' option in the 'Delete by Field' radio choice.
    2. Fill in the provided 'Title' and 'URL' values.
4. Click the 'Delete Link' button and observe what happens next.

|TC#  |Title   |Title exists?|      URL       |URL Exists?|
|-----|--------|-------------|----------------|-----------|
| TC12|'google'|      Yes    |'www.google.com'|   Yes     |
| TC13|'yahoo' |      No     |'www.google.com'|   Yes     |
| TC14|'google'|      Yes    |'www.yahoo.com' |   No      |
| TC15|'yahoo' |      No     |'www.yahoo.com' |   No      |
| TC16|empty   |     N/A     |'www.google.com'|   Yes     |
| TC17|'google'|     Yes     |empty           |   N/A     |
| TC18|empty   |     N/A     |empty           |   N/A     |

### Expected Results
|TC#  |Page Reloads?|Entries Deleted?                |Missing Title Error?|Missing URL Error?|Priority|
|-----|-------------|--------------------------------|--------------------|------------------|--------|
| TC12|Yes          |Yes:('google', 'www.google.com')|No                  |No                | High   |
| TC13|Yes          |No                              |No                  |No                | Medium |
| TC14|Yes          |No                              |No                  |No                | Medium |
| TC15|Yes          |No                              |No                  |No                | Medium |
| TC16|No           |No                              |Yes                 |No                | Medium |
| TC17|No           |No                              |No                  |Yes               | Medium |
| TC18|No           |No                              |Yes                 |Yes               | High   |


#### Column Names Legend:
- Title exists? = a row with a title column that equals to the provided Title exists in `TestDatabase`
- URL exists? = a row with a url column that equals to the provided URL exists in `TestDatabase`
- Page Reloads? = page reloads after clicking the 'Delete Link' button
- Entries Deleted? = All matching entries are deleted and are no longer shown in the links table
- Missing Title Error? = A browser native field validation popup is shown just below the 'Title' field, with the message 'Title cannot be empty'
- Missing URL Error? = A browser native field validation popup is shown just below the 'URL' field, with the message 'URL cannot be empty'


## Input Fields Character Limit
**TC19 - Input Fields Character Limit - Within Range**
- **STP Features:** 4
- **Priority:** Medium
### Steps
1. Run `scripts/reset_test_database.ps1` to reset test database.
2. Open `localhost:5000` in the browser.
3. In the 'Add Link' form paste the 300 character string into the 'Title' field, and then the 500 character string into the 'URL' field
4. Count the number of characters that are now displayed in each field.
    1. You can use 'https://www.grammarly.com/word-counter' - copy the field content and paste it into the word-counter textbox. Note the 'Characters without spaces' number.
5. repeat steps 1,2 for the 'Delete Link' form.
### Expected Results:
1. The character counts for both the 'Title' fields is exactly 300
2. The character counts for both the 'URL' field is exactly 500

---


**TC20 - Input Fields Character Limit - Outside Range**
- **STP Features:** 4
- **Priority:** Medium
### Steps
1. Run `scripts/reset_test_database.ps1` to reset test database.
2. Open `localhost:5000` in the browser.
3. In the 'Add Link' form paste the 301 character string into the 'Title' field, and then the 501 character string into the 'URL' field
4. Count the number of characters that are now displayed in each field.
    1. You can use 'https://www.grammarly.com/word-counter' - copy the field content and paste it into the word-counter textbox. Note the 'Characters without spaces' number.
5. repeat steps 1,2 for the 'Delete Link' form.
### Expected Results:
1. Inputs are truncated:
    1. The character counts for both the 'Title' fields is exactly 300
    2. The character counts for both the 'URL' field is exactly 500


    
---



### Environment
- OS: Windows 11 Home 24H2, 26100.4351
- Browsers:
    - Chrome: latest version (Official Build) (64-bit)
    - Firefox: latest version (64-bit)
    - Opera One: latest version (64-bit)
    - Edge: latest version (Official build) (64-bit)
- App Version: 0.0.5-pre
- Commit Hash: 677dc3c


---


