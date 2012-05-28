

/*ajax*/
var httpRequest = false;
var type,obj=null;
var url_last_request="";
var ajaxState="";
function makeRequest(url,type,obj,add) {
/*tranh xung dot 2 request cung luc*/
if(ajaxState==1) {this.url_temp=url;this.type_temp=type;this.obj_temp=obj;setTimeout("makeRequest(url_temp,type_temp,obj_temp)",500);return false;}
/**/
this.url=url;
this.type=type;
this.obj=obj;
this.add=add;
url_last_request=url;
httpRequest = false;
if (window.XMLHttpRequest) 
	{
		httpRequest = new XMLHttpRequest();
		if (httpRequest.overrideMimeType) 
		{
			httpRequest.overrideMimeType("text/xml");
		}
	}
	else if (window.ActiveXObject) 
	{
		try 
		{
			httpRequest = new ActiveXObject("Msxml2.XMLHTTP");
		} 
		catch (e) 
		{
			try 
			{
				httpRequest = new ActiveXObject("Microsoft.XMLHTTP");
			} 
			catch (e) 
			{
				alert('Không xác định được sự kiện này!');
			}
		}
	}
	if (!httpRequest)
	{
		alert('Không thể tạo sự kiện XMLHTTP!');
		return false;
	}
	httpRequest.onreadystatechange = alertContents;
	httpRequest.open("GET", url, true);
	httpRequest.send(null);
}

function alertContents() 
{
	ajaxState=httpRequest.readyState;
	if (httpRequest.readyState == 4)
	{
		if (httpRequest.status == 200)
		{
			if(type=="html") {
				if(obj)
				{
					//alert(document.getElementById(obj).innerHTML);
					if(add=="add") document.getElementById(obj).innerHTML=httpRequest.responseText+document.getElementById(obj).innerHTML;
					else document.getElementById(obj).innerHTML=httpRequest.responseText;
				}
			}
			else eval(httpRequest.responseText);
		}
		//else {alert('Có vấn đề trong quá trình kết nối máy chủ!');}
	}
}




var loading = "Loading...";

function ajax_load(url,id)
{
var ajax;
try
	{
	ajax = new XMLHttpRequest();
	}
	catch(e)
	{
	try
		{
		ajax = new ActiveXObject('Microsoft.XMLHTTP');
		}
		catch(e)
		{
		try
			{
			ajax = new ActiveXObject('Msxml2.XMLHTTP');
			}
			catch(e)
			{
			alert('Your browser does not support AJAX');
			}
		}	
	}
ajax.onreadystatechange = check;

ajax.open("GET",url,true);

ajax.send(null);

	function check()
	{
	 document.getElementById(id).innerHTML = loading;
	 if(ajax.readyState == 4 && ajax.status == 200)
	  {
	  document.getElementById(id).innerHTML = ajax.responseText;
	  }
	  else
	  {
	  document.getElementById(id).innerHTML = loading;
	  }
	}

}	



