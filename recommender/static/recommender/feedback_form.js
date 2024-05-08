document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("submitFeedback").addEventListener("click", function() {
        var response = $('input[name="response"]:checked').val();
        $.ajax({
            type: 'POST',
            url: 'submit_feedback/',
            data: {
                'response': response,
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            },
            success: function(data) {
                document.getElementById("feedbackForm").style.display = "none";
                document.getElementById("feedbackSent").style.display = "block";
            },
            error: function(xhr, textStatus, errorThrown) {
                console.log('Error:', errorThrown);
            }
        });
    });
});