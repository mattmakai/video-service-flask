// Get a query parameter from the current page
function getParameterByName(name) {
    name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
    var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
        results = regex.exec(location.search);
    return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
}

$(function() {
    var initial = 'Need Help? Chat with Support Now!';
    var waiting = 'Waiting for the next available agent...';
    var $help = $('#help');

    $help.on('click', function(e) {
        e.preventDefault();
        $help.html(waiting);

        // Create support request
        $.ajax({
            url: '/tickets',
            method: 'POST',
            data: {
                endpoint: window.endpointId,
                productUrl: getParameterByName('url')
            },
            dataType: 'json'
        }).done(function(data) {
            alert(data.message);
        }).fail(function() {
            $help.html(initial);
            alert('Oops! There was a problem. Please try again.');
        });
    });

    // hide button and show video when an invitation has been accepted
    $(document).on('inviteAccepted', function() {
        $help.hide();
        $('.video-widget').show();
    });

    $(document).on('conversationLeft', function() {
        $('.video-widget').hide();
        $help.html(initial);
        $help.show();
    });
});