import jinja2
import os

jinjaEnv = jinja2.Environment(
        loader = jinja2.FileSystemLoader(os.path.dirname(__file__)))

def templateRender(name, values={}):
    return jinjaEnv.get_template(name).render(values)

