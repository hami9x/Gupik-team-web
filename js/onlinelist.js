function onlinelist_onMessage(message) {
        var msg = eval("("+message.data+")");
        if (msg.type !== "onlineStatus") return;
        if (msg.on === 0) {
            $("#online-list > #"+msg.uid).remove();
        } else {
            $("#online-list").append("<li id="+msg.uid+">"+msg.nickname+"</li>");
        }
    }

registerMessageHandler(onlinelist_onMessage);
