// Wait for the DOM to be fully loaded
$(document).ready(function() {
  // Add a click event handler to the div with id add_item
  $('#add_item').click(function() {
    // Create a new li element and append it to the UL with class my_list
    $('<li>Item</li>').appendTo('ul.my_list');
  });

  // Add a click event handler to the div with id remove_item
  $('#remove_item').click(function() {
    // Remove the last li element from the UL with class my_list
    $('ul.my_list li:last-child').remove();
  });

  // Add a click event handler to the div with id clear_list
  $('#clear_list').click(function() {
    // Remove all li elements from the UL with class my_list
    $('ul.my_list').empty();
  });
});
