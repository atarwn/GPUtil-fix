from setuptools import setup, find_packages

setup(
    name='GPUtil-fix',
    version='1.4.1',
    description='Utility to get the GPU status from NVIDA GPUs using nvidia-smi',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author = 'Anders Krogh Mortensen',
    author_email = 'anderskroghm@gmail.com',
    maintainer='atarwn', 
    maintainer_email='a@qwa.su',
    url='https://github.com/atarwn/GPUtil-fix',
    packages=find_packages(),
    install_requires=[
        # nothing
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.12',
    ],
)
