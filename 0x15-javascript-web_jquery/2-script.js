// Wait for the document to be ready
$(document).ready(function() {
  // Add a click event handler to the div with id red_header
  $('div#red_header').click(function() {
    // Update the text color of the header to red
    $('header').css('color', '#FF0000');
  });
});
