## BUG ID
BUG-013

## Bug Title
All Input Fields - Max character limit is incorrect 

## Summary
For all textbox fields in both the 'Add Link' and 'Delete Link' form, the max character limit does not match the app specification.

## Date Reported
10/07/2025

## Reported By
Michael Shults

## Status
Closed - fixed 11/07/2025

## Linked Test Cases
- TC19, TC20
- STD File: 'STD_v0.0.5-pre.md'

## Steps to Reproduce:
Follow TC19 and TC20 steps.

## Expected Results
Max characters that fit in the 'Title' fields is 300, and in the 'URL' fields is 500.

## Actual Results
Max characters that fit in the 'Title' fields is 100, and in the 'URL' fields is 100.

## Environment
- App Version: 0.0.5-pre
- Browser: Chrome, Firefox, Opera, Edge (latest versions)

## Severity and Priority
- Severity: Medium
- Priority: Medium