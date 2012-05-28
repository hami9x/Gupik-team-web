//This function takes a string "year:month:day:hour:min" in UTC and converts to local time
//Returns a string representation of the time
function toLocalTime(str) {
    var timeArr = msg.time.split(":");
    for (var i=0; i<timeArr.length(); i++) {
        timeArr[i] = parseInt(timeArr[i]);
    }
    var d = new Date(timeArr[0], timeArr[1], timeArr[2], timeArr[3], timeArr[4], 0, 0);
    var nd = new Date(d + getTimezoneOffset()*60000);
    var year = nd.getFullYear();
    var month = nd.getMonth()+1;
    var day = nd.getDay();
    var hour = nd.getHours();
    var min = nd.getMinutes();
    return year+"/"+month+"/"+day+" "+hour+":"+min;
}

function chatbox_onMessage(message) {
    var msg = eval("("+message.data+")");
    if (msg.type !== "chatMsg") return;
    var timeStr = toLocalTime(msg.time);
    $("#result").prepend('<span class="time">['+timeStr+']</span>'+
                            '<span class="user">'+msg.nickname+'</span>'+
                            ': <span class="pagetext">'+msg.content+'</span>'+
                            '<br/>');
}

registerMessageHandler(chatbox_onMessage);

$(document).ready(function(){
    $("#chip_chatbox > #do").click(function(){
        var speed = 'fast';
        var str = $("#chip_chatbox").serialize();
        $("#result").fadeOut(speed,function(){
            if (!validate()) return;
            $.post('/chatbox', str);
        });
    });
});
