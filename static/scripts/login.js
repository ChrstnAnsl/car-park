$(document).ready(function() {
    $('#loginForm').submit(function(event) {
        event.preventDefault(); // Prevent default form submission behavior
        
        // Perform AJAX request to login endpoint
        $.ajax({
            url: '/login',
            type: 'POST',
            data: $('#loginForm').serialize(),
            success: function(response) {
                // Redirect to index page upon successful login
                window.location.href = '/index';
            },
            error: function(error) {
                console.error('Login error:', error);
            }
        });
    });
});
