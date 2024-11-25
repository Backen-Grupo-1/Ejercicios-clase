# templates.py
import os

class Template:
    def render_template(nombre):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        template_dir = os.path.join(current_dir, 'templates')
        template_path = os.path.join(template_dir, nombre)
        print(template_path)

        try:
            with open(template_path, 'r') as template_file:
                return template_file.read()
        except FileNotFoundError:
            return "Template no encontrado."