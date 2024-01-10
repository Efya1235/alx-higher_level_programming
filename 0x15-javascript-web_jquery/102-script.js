// Wait for the DOM to be fully loaded
$(document).ready(function() {
    // Add a click event handler to the button with id btn_translate
    $('#btn_translate').click(function() {
        // Get the language code from the input with id language_code
        var languageCode = $('#language_code').val();

        // Fetch translation data from the API based on the entered language code
        $.ajax({
            url: 'https://www.fourtonfish.com/hellosalut/hello/',
            method: 'GET',
            data: { lang: languageCode },
            success: function(data) {
                // Update the content of the div with id hello with the translation
                $('#hello').text(data.hello);
            },
            error: function(error) {
                console.log('Error fetching translation data:', error);
            }
        });
    });
});
