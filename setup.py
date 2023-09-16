import setuptools

with open("README.md", "r",encoding ="utf-8") as fh:
    long_description = fh.read()

__version__ ="0.0.0"

REPO_NAME = "Text_Summarization"
AUTHOR_USER_NAME = "Octopus30"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "akhilreddy30121996@gmail.com"

#code for local package setup

setuptools.setup(
    name = SRC_REPO,
    veresion = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "A small python package for NLP applications",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src")
    
) 