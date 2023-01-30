from setuptools import setup, find_packages

setup(
    name='Calculator',
    version='1.0',
    description='Console application that calculates',
    author='Aistis Jampolskis',
    author_email='aistis.jampolskis@gmail.com',
    url='https://example.com/project_name',
    packages=find_packages(),
    install_requires=[
        'dependency1',
        'dependency2',
        # ...
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.9',
        # ...
    ],
)

