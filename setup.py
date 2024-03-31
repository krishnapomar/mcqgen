from setuptools import setup, find_packages

setup(
    name="mcq-generator",
    version="0.0.1",
    author="Krishna Pomar",
    author_email="krishna.pomar@gmail.com",
    install_requires=["openai", "langchain", "streamlit", "python-dotenv", "PyPDF2"],
    packages=find_packages()
    )