# Software Test Report v1.0  
Tested App Version: 0.0.1  
Author: Michael Shults  
Date: 03/06/2025  
Based on STD: index_about_STD_v1.0 

## Environment
- OS: Windows 11 Home 24H2, 26100.4202
- Browsers:
    - Chrome: version 137.0.7151.69 (Official Build) (64-bit)
    - Firefox: version 139.0.1 (64-bit)
    - Opera One: version 119.0.5497.56
    - Edge: version 137.0.3296.58 (Official build) (64-bit)
- App Version: 0.0.1
- Commit Hash: e0a083f


## Test Results Summary

**TC01 - Load index page**  
Result: Pass  
Notes: Verified in all 4 browsers.

**TC02 - Load About page**  
Result: Pass  
Notes: Verified in all 4 browsers.

**TC03 - Main Menu button for current page reloads page**  
Result: Pass  
Notes: Verified in all 4 browsers.

**TC04 - Main Menu button for different page redirects correctly**  
Result: Pass  
Notes: Verified in all 4 browsers.

**TC05 - Non menu links work in "About" page**  
Result: Fail  
Notes: "Contact Us" link incorrectly points to '/about'. Also, '/contact' does not exist yet. Issue present in all 4 browsers.


## Bugs Found

**Bug001**: On the About page, a "Contact Us" link points incorrectly to '/about'. 

**Bug002**: The "Contact Us" page is linked but not implemented. All browsers return 404.


## **Bugs tracked in**
 /tests/manual/bugs_logs/