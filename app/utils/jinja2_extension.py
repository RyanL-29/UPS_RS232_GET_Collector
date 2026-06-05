from typing import Any
from jinja2 import Environment, Undefined, Template, meta

class PreserveUndefined(Undefined):
    def __str__(self):
        return f"{{{{ {self._undefined_name} }}}}"
    
    
class XTemplate(Template):
    def __init__(self, template_str) -> None:
        super().__init__()
        self.env = Environment(undefined=PreserveUndefined)
        self.template_str = template_str
        self.__template = self.env.from_string(template_str)
    
    def hybrid_render(self, *args: Any, **kwargs: Any):
        rendered = self.__template.render(*args, **kwargs)
        return rendered
    
    def get_param(self) -> set[str]:
        env = Environment()
        parsed_content = env.parse(self.template_str)
        variable = meta.find_undeclared_variables(parsed_content)
        
        return variable