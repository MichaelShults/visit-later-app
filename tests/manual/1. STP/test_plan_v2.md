# Software Test Plan V2
### **Project Name**: Visit Later  
**Creation Date**: 05/06/2025  
**Last Updated**: 13/07/2025 (minor updates)


## Introduction
This document is an updated and revamped version of `test_plan_v1.md`. The motivation behind this new version is to increase precision and broaden the scope, so that the plan stays relevant for future versions of the app.

## Objectives
The goal is to have a solid test coverage of the website and the main app. Both major and minor bugs should be detected. The website should work smoothly, and the CRUD part of the app should function as expected from a typical user.

## Features that will be tested
1. Static content and routes (`index`, `/about`, `/contact`)
2. Menu and internal links
3. Links to external resources, such as `mailto` links
4. View links, and add and remove items from it using web forms

## Features that will not be tested
1. Security
2. Accessibility
3. Mobile

## Test Types
- Manual UI testing
- Manual exploratory testing (UI)
- Focused regression before release version tagging

## Tools and Environment
- Windows 11 Desktop
- Browsers: Chrome, Firefox, Opera, Edge - latest versions
- Tools used: Browser dev tools

## Documents and Artifacts
- Software Test Plan - this doc
- STD and STR files in Markdown
- Bug logs in Markdown format

## Roles and Responsibilities
- Tester and developer: Michael Shults

## Timeline
- Full STD + STR cycle before version tagging
- Light testing after each commit

