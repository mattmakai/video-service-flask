// Create window-scope variable for support convo
var supportConversation;

// incoming or outgoing, display streams on screen
function showVideoStreams(conversation) {
    // show local video
    var localVideoElement = $('.me').get(0);

    // create a localStream object to mute and end
    supportConversation = conversation;
    conversation.localStream.attach(localVideoElement);

    conversation.on('participantConnected', function(participant) {
        // show participant video
        var remoteVideoElement = $('.main').get(0);
        participant.stream.attach(remoteVideoElement);
    });
}

// Initialize twilio video components
$(function() {
    var ice = JSON.parse(iceServers);

    // Create endpoint for current person, using the capability token
    // already created in the window scope
    new Twilio.Endpoint.createWithToken(token, {
        debug: true,
        iceServers: ice
    }).then(function(endpoint) {
        // automatically answer any incoming calls
        endpoint.on('invite', function(invite) {
            invite.accept().then(function(conversation) {
                $(document).trigger('inviteAccepted');
                showVideoStreams(conversation);
            });
        });

        // Fire event on the document with endpoint when created
        $(document).trigger('endpointCreated', endpoint);

    }, function(error) {
        alert('Sorry, there was a problem connecting to Twilio :(');
    });

    // Video controls
    var muted = false;
    var $mute = $('#mute');
    $mute.on('click', function() {
        supportConversation.localStream.muted = !muted;
        muted = !muted;
        $mute.html((muted) ? 'Unmute' : 'Mute');
    });

    $('#hangup').on('click', function() {
        supportConversation.leave();
        $(document).trigger('conversationLeft');
    });
});