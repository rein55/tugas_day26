from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."
def get_requirements(file_path:str) -> List[str]:
    """
    Function will return the list of requirements
    """
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name             = 'tugas day26',
    version          = '0.0.1',
    author           = 'Rein L Tobing',
    author_email     = 'reinltobing@gmail.com',
    packages         = find_packages(include=['src', 'src.*']),
    #package_dir={'': 'src'},
    install_requires =get_requirements('requirements.txt')
    
)