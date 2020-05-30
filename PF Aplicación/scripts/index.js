$(document).ready(function() {
    M.updateTextFields();
    let elems = document.querySelectorAll('select');
    let instances = M.FormSelect.init(elems);
});