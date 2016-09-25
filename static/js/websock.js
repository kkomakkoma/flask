'use strict';

var socket = io.connect('https://' + document.domain + ':' + location.port);
socket.on('connect', function() {
        socket.emit('my event', {data: 'I\'m connected!'});
});



var constraints = {video: true, audio: false};
var video = document.querySelector('video');


function successCallback(stream){
        var videoTracks = stream.getVideoTracks();
        console.log('Got stream with constraints:', constraints);
        console.log('Using video device: ' + videoTracks[0].label);
        stream.oninactive = function() {
                console.log('Stream inactive');
        };
        window.stream = stream;
        video.srcObject = stream;
        //video.src = window.URL.createObjectURL(stream);
}

function errorCallback(error) {
        console.log("navigator.getUserMedia error: ", error);
}


navigator.getUserMedia(constraints, successCallback, errorCallback);

