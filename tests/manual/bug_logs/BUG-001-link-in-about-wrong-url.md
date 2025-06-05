## BUG ID
BUG-001

## Bug Title
On the About page, a "Contact Us" link points incorrectly to '/about'. 

## Summary
On the 'About' page, a 'contact us' link incorrectly links to the current page, instead of the 'contact us' page.

## Date Reported
05/06/2025 

## Reported By
Michael Shults

## Status
Closed – Fixed on 05/06/2025

## Linked Test Case
- TC05 - Non menu links work in "About" page
- STD File: 'index_about_STD_v1.0.md'

## Steps to Reproduce:
1. Navigate to 'localhost:5000/about'
2. Locate the text "don't hesitate to contact us."
3. Right click on "contact us" and then 'Copy link address'
4. Paste the copied URL into the text editor

## Expected Results
- The pasted link is 'http://localhost:5000/contact'

## Actual Result
- The pasted link is 'http://localhost:5000/about'

## Environment
- App Version: 0.0.1
- Browser: Chrome version 137.0.7151.69
- OS: Windows 11 Home 24H2, 26100.4202

## Severity and Priority
- Severity: Medium
- Priority: High


