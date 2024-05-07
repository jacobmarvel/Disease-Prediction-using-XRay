import setuptools 

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


setuptools.setup(
    name='DiseasePredictionXray',
    version='1.0.0',
    description='Disease prediction using X-ray plates',
    author='Marvel Samuel Jacob',
    author_email='marvelsamueljacob@gmail.com',
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
    
)
