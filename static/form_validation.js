
const missing_title_error = "Title cannot be empty";
const missing_url_error = "URL cannot be empty";

const add_link_form = document.getElementById("add-link-form");
const add_link_title = document.getElementById("title-add");
const add_link_url = document.getElementById("url-add");
const add_link_button = document.getElementById("add-link-button");
const by_field = document.querySelectorAll("input[name='by_field']");
const delete_link_form = document.getElementById("delete-link-form");
const delete_link_title = document.getElementById("title-delete");
const delete_link_url = document.getElementById("url-delete");
const delete_link_button = document.getElementById("delete-links-button");


add_link_form.addEventListener('submit', function (e) {
    
    if (add_link_title.value.trim() == ''){
        add_link_title.setCustomValidity(missing_title_error);
        
    }
    else {
        add_link_title.setCustomValidity("");
        
    }
    if (add_link_url.value.trim() == ''){
        add_link_url.setCustomValidity(missing_url_error);
        
    }
    else {
        add_link_url.setCustomValidity("");
    }

    if (!add_link_form.checkValidity()) {
        e.preventDefault();
        add_link_url.reportValidity();
        add_link_title.reportValidity();
    }
});

add_link_url.addEventListener('input', () => {add_link_url.setCustomValidity("");});
add_link_title.addEventListener('input', () => {add_link_title.setCustomValidity("");});

delete_link_form.addEventListener('submit', function (e) {
    by_field_selected = document.querySelector("input[name='by_field']:checked").value;
    if ((by_field_selected == 'title' || by_field_selected =='title-url') && delete_link_title.value.trim() == ''){
        delete_link_title.setCustomValidity(missing_title_error);
    }
    else {
        delete_link_title.setCustomValidity("");
    }
    if ((by_field_selected == 'url' || by_field_selected =='title-url')&& delete_link_url.value.trim() == ''){
        delete_link_url.setCustomValidity(missing_url_error);
        
    }
    else {
        delete_link_url.setCustomValidity("");
    }
    if (!delete_link_form.checkValidity()) {
        e.preventDefault();
        delete_link_url.reportValidity();
        delete_link_title.reportValidity();
    }
});

delete_link_url.addEventListener('input', () => {delete_link_url.setCustomValidity("");});
delete_link_title.addEventListener('input', () => {delete_link_title.setCustomValidity("");});
by_field.forEach(radio => {
    radio.addEventListener('change', function() {
            delete_link_url.setCustomValidity("");
            delete_link_title.setCustomValidity("");
    });
});
