# Visit Later - A Flask website for QA practice

 ## What is this project about?
- **Visit Later** is a Flask web app that tracks URLs that you want to visit later. 
It aims to be convenient and user friendly.
You will be able to save any type of link - videos, articles, etc.

**This project is intentionally simple and imperfect to create realistic conditions for QA practice.**

**Current app version:** v0.0.4-pre

 ### Features that I may add over time:
- Tagging, categorizing, or sectioning
- A daily feed
- Some form of reminders or push notifications
- Some automatic behaviors:
    - Auto categorization (Video / article / etc.) 
- The purpose of this project is to help me practice manual and automated testing.
    - I am keeping the app simple and unpolished on purpose. This leaves room for more bugs for me to find and document.

---

## Testing Artifacts
I also write test plans and test descriptions. After running the tests I log the results in a test report. All documents are in Markdown format.


## Bug Reports

I’m logging bugs that I find while testing the app.

- Bug reports are stored in `bug_logs/`
- Each bug is documented in Markdown, with a clear description, reproduction steps, expected vs actual results and environment info

Current logs:
- BUG-001: "contact us" link URL incorrect - FIXED
- BUG-002: '/contact' route returns 404, link exists but page isn't implemented - FIXED

---
