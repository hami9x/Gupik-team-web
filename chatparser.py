import cgi
import json
from google.appengine.api import memcache

def quote_escape(str):
    esc_list = ['"', "'"]
    return "".join(("\\"+c) if (c in esc_list) else c for c in str)

def get_emoticon_config():
    config = memcache.get("emo_config")
    if config is None:
        f = open("config/emoticons.json", "r")
        config = json.load(f)
        memcache.add("emo_config", config)
    return config



def parse_emoticon(message):
    config = get_emoticon_config()
    for emo in reversed(config):
        img = '<img src="%s"/>' % emo[1]
        message = message.replace(cgi.escape(emo[0]), img)
    return message


def parse_message(message):
    return parse_emoticon(cgi.escape(message))

def decorate_message(message, request):
    decorate_list = []
    if request.get("upbold") == "B*": decorate_list.append(("<b>", "</b>"))
    if request.get("upitalic") == "I*": decorate_list.append(("<i>", "</i>"))
    if request.get("upunderline") == "U*": decorate_list.append(("<u>", "</u>"))
    decorate_list.append(("<span style='color: %s'>" % request.get("ccolor"), "</span>"))

    prepend_str = "".join(tag[0] for tag in decorate_list)
    append_str = "".join(tag[1] for tag in decorate_list)

    return prepend_str+message+append_str
