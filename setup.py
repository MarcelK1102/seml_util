from setuptools import find_packages, setup

install_requires = [
    "pytorch_lightning",
    "seml",
]

setup(
    name="seml_util",
    version="0.1.0",
    description="SEML utility",
    packages=find_packages("."),
    install_requires=install_requires,
    zip_safe=False,
)
