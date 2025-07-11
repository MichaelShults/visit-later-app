# Visit Later App - Functional Specification

**Author**: Michael Shults
**Date**: 21/06/2025
**Last Updated**: 11/07/2025
**App Version**: 0.0.5  
**Spec Version**: 1.1

**Context**: Written after the `v0.0.5-pre` version tag was pushed to GitHub. This document reflects desired specification, and currently not all functionality and UI is implemented according to this spec.
Purpose: Establish ground truth for functionality and UI, to bring clarity to the QA process.

**Description**: 'Visit Later' is a simple flask web app which allows viewing, adding and removing links to websites you might want to visit later.

## UI Layout
### Home page (`/`):

- Content is centered and is in a single column layout.
- Page contents (top to bottom):
    1. Two item menu, 'Home' on the left and 'About' on the right
        1. The items are rectangular buttons, with consistent spacing and black text, even after they are visited.
    2. A title, 'Welcome to Visit Later', large black text
    3. A subtitle, 'Save any link to visit it later', medium sized bolded black text
    4. The links table
        1. The table header ('Title', 'URL') is always visible, even if table is empty
        2. If the table is empty, only the header is shown, with no empty rows or placeholders
        3. All text is black
        4. Cells are visually separated both vertically and horizontally
        5. The columns' widths are fixed regardless of content size or whether entries are present or not.
        6. Table height grows with content
        7. Text and links overflow to fit cell widths
        8. Table is centered, regardless of screen size
        9. URLs are plain text and not clickable
            - User must manually select and copy the URL if they want to visit the link
    5. Horizontal separator line (gray)
    6. The 'Add Link' form:
        1. 'Add Link' title, bold, black
        2. A text input box with the label 'Title' just above it
        3. A text input box with the label 'URL' just above it
        4. A button with inner text 'Add Link'
            1. The button is always visually enabled and clickable, even when the inputs are not valid.
    7. Horizontal separator line (gray)
    8. The 'Delete Link' form:
        1. 'Delete Link' title, bold, black
        2. A text input box with the label 'Title' just above it
        3. A text input box with the label 'URL' just above it
        4. 'Delete by Field' radio inputs group
            1. 'Delete by Field' label above
            2. Three radio inputs with labels to their right
                1. 'Title' (preselected default)
                2. 'URL'
                3. 'Title and URL'
        5. A button with inner text 'Delete Link'
            1. The button is always visually enabled and clickable, even when the inputs are not valid.
    


### About page (`/about`):
- Content is centered and is in a single column layout.
- Page contents (top to bottom):
    1. Two item menu, 'Home' on the left and 'About' on the right
        1. The items are rectangular buttons, with consistent spacing and black text, even after they are visited.
    2. A title, 'About Us', large black text
    3. Text paragraphs, describing the app, black text
    4. Text encouraging user to contact us with any feedback or problems encountered, that includes a link to the '/contact' route, black text, link blue if unvisited, purple if visited.


### Contact page (`/contact`):
- Content is centered and is in a single column layout.
- Page contents (top to bottom):
    1. Two item menu, 'Home' on the left and 'About' on the right
        1. The items are rectangular buttons, with consistent spacing and black text, even after they are visited.
    2. A title, 'Contact Us', large black text
    3. Text encouraging user to contact us with any feedback or problems encountered, that includes a `mailto:` link to the the email address 'contact@example.com'. Text is black, link is blue both visited and unvisited.


## Functionality
### Menu:
When a menu button is clicked:
- 'Home' menu button redirect to the `/` route
- 'About' menu button redirect to the `/about` route

### Links Table:
- Displays all the rows in `database/db.sqlite`. Only the `url` and `title` fields are displayed. `id` should not be displayed to the user.

### Add Link Form:
- The user must fill in both 'Title' and 'URL' to proceed with addition.
- Validation is only fully enforced on the frontend 
    - Bypassing the frontend and sending malformed requests may create unexpected behaviors.
- Rules to enforce:
    - Maximum input size:
     - Title: 300 characters
     - URL: 500 characters
    - Minimum input size:
        - Title: 1 non whitespace character
        - URL: 1 non whitespace character
    - Title and URL cannot be a sequence of whitespace characters. They must contain at least one non whitespace character
    - URL and title are trimmed (`.trim()`) of whitespaces on the backend.
- Not enforced:
    - URL validation
    - Limits on the allowed characters in the inputs.
    - Sequences of two or more whitespaces in the middle of the string. These may not be rendered correctly, and are not supported by the app. There is no validation for that for now.
- Enforcement methods and validation errors:
    - Input size is enforced with the `maxlength` and `minlength` text input attributes
    - Empty or whitespace only field:
         - should cause the following message to display:
            - "URL cannot be empty" for the URL
            - "Title cannot be empty" for the title
        - Use the browser native validation popups to show the message. They can be triggered by the javascript `input.reportValidity()` method.
            - Since browser allows only one popup at a time, if both fields are empty or are a whitespace sequence, a popup will be displayed just for the title field.   

### Delete Link Form:
- Validation is only fully enforced on the frontend 
    - Bypassing the frontend and sending malformed requests may create unexpected behaviors.
- Rules to enforce:
    - Maximum input size:
     - Title: 300 characters
     - URL: 500 characters
    - 'Delete by field' radio buttons:
        - If 'Title' is selected:
            - 'Title' field must not be empty or a whitespace sequence to proceed with deletion.
            - 'URL' field can be either empty or not, and is ignored on form submission.
            - 'Title' is trimmed (`.trim()`) of whitespaces on the backend.
        - If 'URL' is selected:
            - 'URL' field must not be empty or a whitespace sequence to proceed with deletion.
            - 'Title' field can be either empty or not, and is ignored on form submission.
            - 'URL' is trimmed (`.trim()`) of whitespaces on the backend.
        - If 'Title and URL' is selected:
            - 'URL' and 'Title' fields must not be empty or a whitespace sequences to proceed with deletion.
            - 'URL' and 'Title' are trimmed (`.trim()`) of whitespaces on the backend
- Not enforced:
    - URL validation
    - Limits on the allowed characters in the inputs.
    - Sequences of two or more whitespaces in the middle of the string may create unexpected behavior.
- If no matching entry exists, the page reloads and no entry is deleted. No message is displayed to the user. 
- Enforcement methods and validation errors:
    - Input size is enforced with the `maxlength` text input attributes
    - Empty or whitespace only field
         - should cause the following message to display:
            - "URL cannot be empty" for the URL (If deletion is by URL)
            - "Title cannot be empty" for the title (If deletion is by Title)
            - "URL cannot be empty" and "Title cannot be empty" (If deletion is by 'Title and URL')
        - Use the browser native validation popups to show the message. They can be triggered by the javascript `input.reportValidity()` method.
            - Each message will be displayed below its respective field.
            - Since browser allows only one popup at a time, if deletion is by 'Title and URL' both fields are empty or are a whitespace sequence, a popup will be displayed just for the title field.   

    






     










