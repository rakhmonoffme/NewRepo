from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = "-e ."
def get_requirements(file_path:str) -> list[str]:
    """
    This function will return a list of requirements
    
    """
    requirements = []
    with open(file_path) as file_object:
        requirements = file_object .readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup(
    name = "New Project",
    version = "0.1.0",
    author = "Boburshoh",
    author_email= "boburshakh1998@gmail.com",
    description = "A small example package",
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt'),
    )