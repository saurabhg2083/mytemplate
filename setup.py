import setuptools

__version__ = '0.0.1'

with open("README.md", "r", encoding="utf-8") as f:
    long_description=f.read()

REPO_NAME="mytemplate"
AUTHOR_NAME="Saurabh Gupta"
GIT_USER="saurabhg2083"
SRC_REPO="CNNClassifier"
AUTHOR_Email="saurabhg2083@gmail.com"

setuptools.setup(
        name=SRC_REPO,
        version=__version__,
        author=AUTHOR_NAME,
        author_email=AUTHOR_Email,
        description="this is my classifcation project",
        long_description=long_description,
        long_description_content="text/markdown",
        url=f"https://github.com/{GIT_USER}/{REPO_NAME}",
        
        project_urls={
                      
        "Bug Tracker": f"https://github.com/{GIT_USER}/{REPO_NAME}/issues",  
                      
                     },
        package_dir={"":"src"},
        packages=setuptools.find_packages(where="src")
                 
                 
                 
                 )