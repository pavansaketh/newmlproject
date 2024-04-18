from setuptools import find_packages,setup
from typing import List


hypen_e_dot = "-e ."
def get_requirements(filepath:str) -> List[str]:
    '''
    this is used for the returning of list of requirements 
    '''

    requirements=[]
    with open(filepath) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]

        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)

    return requirements



setup(

    name="ML projects",
    version="0.0.1",
    author="saketh",
    author_email="pavansaketh1033@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")

)