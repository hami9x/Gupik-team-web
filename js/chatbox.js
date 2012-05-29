//This function takes a string "year:month:day:hour:min" in UTC and converts to local time
//Returns a string representation of the time
function toLocalTime(str) {
    var timeArr = str.split(":");
    for (var i=0; i<timeArr.length; i++) {
        timeArr[i] = parseInt(timeArr[i]);
    }
    var d = new Date(timeArr[0], timeArr[1], timeArr[2], timeArr[3], timeArr[4], 0, 0);
    var d2 = new Date();
    var nd = new Date(d.getTime() - d2.getTimezoneOffset()*60000);
    var year = nd.getFullYear();
    var month = nd.getMonth();
    var day = nd.getDate();
    var hour = nd.getHours();
    var min = nd.getMinutes();
    return year+"/"+month+"/"+day+" "+hour+"h"+min;
}

function addChatMessage(msg) {
    var timeStr = toLocalTime(msg.time);
    $("#result").prepend('<span class="time">['+timeStr+']</span> '+
                            '<span class="user">'+msg.nickname+'</span>'+
                            ': <span class="pagetext">'+msg.content+'</span>'+
                            '<br/>');
}

function chatbox_onMessage(message) {
    var msg = eval("("+message.data+")");
    if (msg.type !== "chatMsg") return;
    addChatMessage(msg)
}

registerMessageHandler(chatbox_onMessage);

$(document).ready(function() {
    $("#chip_chatbox > #do").click(function(event) {
        event.preventDefault();
        event.stopPropagation();
        var speed = 'fast';
        var str = $("#chip_chatbox").serialize();
        if (!validate()) return;
        $.post('/chatbox', str);
        var textbox = $("#chip_chatbox > #text");
        textbox.val("");
        textbox.focus();
    });
});
