# Software Test Plan
# Project Name: Visit Later

## Introduction
We test the basic functionality of the UI and edge cases for inputs. We aim for the application to be functional, easy to use and without major bugs. Also we aim to get a clear understanding for directions for further development.

## Objectives
- Test a barebones version of the app with minimal functionality
- Smoke test, verify menu functionality, displaying items fetched from database. Verify all these work across different browsers

## Features that will be tested
1. Basic loading of the pages
2. Main menu
3. Links in pages
4. App UI

## Features that will not be tested
- SQL Injection / security
- Accessibility
- API / Database
- Mobile browser

## Test Types
- Manual UI testing
- Manual exploratory testing (UI)

## Tools and Environment
- Windows 11 Desktop: Chrome, Firefox, Opera, Edge - latest versions
- Fully manual testing with a regular browser

## Documents and Artifacts
- This document (STP)
- Bug logs
- Test report (STR)

## Roles and Responsibilities
- Tester: Michael Shults

## Timeline
- Testing after each commit
- All tests must pass before version tagging

## Risk Areas and Assumptions
- Some tests might not be outlined here, but will be relevant once more
features are added

## Exit Criteria
- All test cases that are relevant to the version must pass without any regressions




