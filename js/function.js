var msgHandlers = new Array();
    function registerMessageHandler(func) {
        msgHandlers.push(func);
    }

    function onMessage(message) {
        console.log("^^^");
        for (var i=0; i<msgHandlers.length(); i++) {
            (msgHandlers[i])(message);
        }
    }

function addsmile(kitu)
{
	window.opener.document.chip_chatbox.text.value = opener.document.chip_chatbox.text.value + kitu;
}


function c_style(element)
	{
		if (element == 'b')
		{
			if (document.chip_chatbox.cbold.value == 'B')
			{
				document.chip_chatbox.cbold.value = 'B*';
				document.chip_chatbox.upbold.value = 'B*';
				textstyle.style.fontWeight = 'bold';
			}
			else
			{
				document.chip_chatbox.cbold.value = 'B';
				document.chip_chatbox.upbold.value = 'B';
				textstyle.style.fontWeight = 'normal';
			}

		}
		else if (element == 'i')
		{
			if (document.chip_chatbox.citalic.value == 'I')
			{
				document.chip_chatbox.citalic.value = 'I*';
				document.chip_chatbox.upitalic.value = 'I*';
				textstyle.style.fontStyle = 'italic';
			}
			else
			{
				document.chip_chatbox.citalic.value = 'I';
				document.chip_chatbox.upitalic.value = 'I';
				textstyle.style.fontStyle = 'normal';
			}

		}
		else if (element == 'u')
		{
			if (document.chip_chatbox.cunderline.value == 'U')
			{
				document.chip_chatbox.cunderline.value = 'U*';
				document.chip_chatbox.upunderline.value = 'U*';
				textstyle.style.textDecoration = 'underline';
			}
			else
			{
				document.chip_chatbox.cunderline.value = 'U';
				document.chip_chatbox.upunderline.value = 'U';
				textstyle.style.textDecoration = 'none';
			}

		}
		else if (element == 'color')
		{
			textstyle.style.color = document.chip_chatbox.ccolor.value;
			document.chip_chatbox.upcolor.value = document.chip_chatbox.ccolor.value;;
		}


	}
	function validate()
	{
        if(document.chip_chatbox.text.value=='')
        {
            document.chip_chatbox.text.focus();
            return false;
        }
		if(document.chip_chatbox.text.value.length>255)
		{
			alert("Nội dung ko được dài quá 255 ký tự");
			document.chip_chatbox.text.value = document.chip_chatbox.text.value.substring(0,255);
			document.chip_chatbox.text.focus();
			return false;
		}
        return true;
	}

	function smiliepopup()
	{
		window.open("?chip_smilies", "", "location=no,scrollbars=yes,width=500,height=500");
	}
