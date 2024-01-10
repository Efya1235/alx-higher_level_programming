// Wait for the document to be ready
$(document).ready(function() {
  // Add a click event handler to the div with id add_item
  $('div#add_item').click(function() {
    // Create a new li element
    var newListItem = $('<li>Item</li>');

    // Append the new li element to the UL with class my_list
    $('ul.my_list').append(newListItem);
  });
});
