# Software Test Report v1  
**Tested App Version:** 0.0.4-pre  
**Author:** Michael Shults    
**Date:** 08/06/2025  
**Based on STD:** STD_v0.0.4


### Environment
- OS: Windows 11 Home 24H2, 26100.4202
- Browsers:
    - Chrome: version 137.0.7151.69 (Official Build) (64-bit)
    - Firefox: version 139.0.1 (64-bit)
    - Opera One: version 119.0.5497.56
    - Edge: version 137.0.3296.58 (Official build) (64-bit)
- App Version: 0.0.4-pre
- Commit Hash: 795106f



## Test Results Summary

**TC01 - Load index page**  
Result: Pass 
Notes: Passed on all 4 browsers

**TC02 - Add item - Title and URL**  
Result: Pass 
Notes: Passed on all 4 browsers

**TC03 - Add item - Title and no URL**  
Result: Partial Fail
Notes: On all 4 browsers page reloaded with status 200 and no change took place, but there wasn't a message for the user indicating 'missing url'

**TC04 - Add item - URL and no title**  
Result: Partial Fail
Notes: On all 4 browsers page reloaded with status 200 and no change took place, but there wasn't a message for the user indicating 'missing title'

**TC05 - Add item - no URL and no title**  
Result: Partial Fail
Notes: On all 4 browsers page reloaded with status 200 and no change took place, but there wasn't a message for the user indicating 'missing title and URL'

**TC06 - Delete item - by title - title exists - url field empty**  
Result: Pass 
Notes: Passed on all 4 browsers

**TC07 - Delete item - by title - title doesn't exist - url field empty**  
Result: Pass 
Notes: Passed on all 4 browsers

**TC08 - Delete item - by url - url exists - Title field empty**  
Result: Pass 
Notes: Passed on all 4 browsers

**TC09 - Delete item - by url - url doesn't exist - Title field empty**  
Result: Pass
Notes: Passed on all 4 browsers

**TC10 - Delete item - by title and url - url and title combination exist in one entry**  
Result: Pass
Notes: Passed on all 4 browsers

**TC11 - Delete item - by title and url - url exists but title doesn't exist**  
Result: Pass
Notes: Passed on all 4 browsers

**TC12 - Delete item - by title and url - title exists but url doesn't exist**  
Result: Pass
Notes: Passed on all 4 browsers

**TC13 - Delete item - by title and url - title and url don't exist anywhere in the list**  
Result: Pass
Notes: Passed on all 4 browsers

## Test Data
All test data used here is directly from `STD_v0.0.4.md`.  
Inputs were tested exactly how they are written there.
- Titles (facebook, yahoo, google)
- URLs (www.facebook.com, www.yahoo.com, www.google.com)
- Empty fields where required by test case


## Bugs Found
**Bug-003:** page doesn't display a message to the user indicating 'missing url' near the insertion form, when adding an item with a filled in Title field but empty url field 
**Bug-004:** page doesn't display a message to the user indicating  'missing Title' near the insertion form, when adding an item with a filled in url field but empty title field 
**Bug-005:** page doesn't display a message to the user indicating  'missing Title and URL' near the insertion form, when adding an item with an empty url field and empty title field 

## Notes
- No other inconsistencies were observed in this test run except the 3 bugs.
- Firefox console showed a 404 for a favicon.ico, but this is not critical to the app's functionality at this stage
## **Bugs tracked in**
 /tests/manual/bugs_logs/
