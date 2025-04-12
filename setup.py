from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    file_path:str ==> This is given beacuse we need to use only string
    this function will return the list of requiremnts.txt
    List[str]==>This Function will return a list 

    '''


    with open(file_path) as file_obj:
        requirements=file_obj.readlines()

        requirements=[req.replace("\n","") for req in requirements]
      
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup(
    name='Software_Log_Clasification',
    version='0.0.1',
    author='Gokulasuthan M',
    author_email='gokulasuthan55@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)