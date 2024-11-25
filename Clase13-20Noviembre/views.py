# views.py
from templates import Template

class View:
    def get_response(self):
        return Template.render_template('home.html')