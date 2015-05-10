from jinja2 import Template
import argparse
import os
import glob

def _relative_path(rel_path):
    """Return the absolute path given a relative path, rel_path.

    Args:
        rel_path (str): The relative path.
    """

    file_directory = os.path.dirname(__file__)
    return os.path.join(file_directory, rel_path)

def deploy_scaffold(project, root='.'):
    """Create the directory structure for the project.

    Args:
        project (str): The name of the project.
        root (str): The root of the new python project.
    """

    directory_structure = [
        os.path.join(root, project),
        os.path.join(root, project, project),
        os.path.join(root, project, "build"),
    ]

    for directory in directory_structure:
        os.makedirs(directory)


def fill_template(template_text, template_args):
    """Takes the Jinja2 template from template_text and fills it
    with the arguments from template_args

    Args:
        template_text (str): The raw template text.
        template_args (dict): A dictionary mapping template keys
            to values.
    """

    template = Template(template_text)
    return template.render(**template_args)

def write_template(template_location, template_destination, template_args):
    """Take a template from template_location, fill it with template_args,
    then write it to template_destination.

    Args:
        template_location (str): Where the template currently lives.
        template_destination (str): The filepath where the filled template
            with reside.
        template_args (dict): The arguments to fill the template with.
    """

    full_location = _relative_path(os.path.join("./templates/", template_location))

    with open(full_location) as input_temp, open(template_destination, "w+") as out_temp:
        template_text = input_temp.read()
        filled_text = fill_template(template_text, template_args)
        out_temp.write(filled_text)

def main():
    parser = argparse.ArgumentParser(description='Create a boilerplate for a python project')

    parser.add_argument('-repository', type=str, help='The name of the repository')
    parser.add_argument('-namespace', type=str, help='The name of the namespace')
    parser.add_argument('-project', type=str, help='The name of the project')

    args = vars(parser.parse_args())

    deploy_scaffold(args["project"])

    assets = {
        # admin
        "Makefile.template": os.path.join(args["project"], "Makefile"),
        "Dockerfile.template": os.path.join(args["project"], "Dockerfile"),
        "setup.py.template": os.path.join(args["project"], "setup.py"),
        "requirements.txt.template": os.path.join(args["project"], "requirements.txt"),

        # package
        "main.py.template": os.path.join(args["project"], args["project"], "main.py"),
        "__init__.py.template": os.path.join(args["project"], args["project"], "__init__.py"),
        "__init__.py.template": os.path.join(args["project"], args["project"], "__init__.py"),
        "build/Dockerfile.template": os.path.join(args["project"], "build", "Dockerfile"),
    }

    for asset, save_location in assets.items():
        write_template(asset, save_location, args)

if __name__ == '__main__':
    main()
