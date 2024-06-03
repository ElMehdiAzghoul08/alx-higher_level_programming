$(document).ready(function() {
    $('#add_item').click(function() {
        $('<li>Item</li>').appendTo('ul.my_list');
    });
});
