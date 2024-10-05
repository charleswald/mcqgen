from setuptools import find_packages,setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='charles sucre',
    author_email='charleswuld@gmail.com',
    requires=["openai","langchain","streamlit","python-dotenv","PyPDF2","langchain_community"],
    packages=find_packages()
)