from dataclasses import dataclass

from jinja2 import Environment, FileSystemLoader, select_autoescape, Template #type:ignore

fileloader = FileSystemLoader("src/templates")
gtemplates = Environment(loader=fileloader, autoescape=select_autoescape())


@dataclass(frozen=True)
class HTMLTemplate:
    WELCOME: Template = gtemplates.get_template("email/welcome.html")