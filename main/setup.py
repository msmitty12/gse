from setuptools import setup

setup(
    name='GSE',
    version='1.0',
    long_description=__doc__,
    packages=['gse'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)