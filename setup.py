from setuptools import setup, find_packages

setup(
    name='Utilities',
    version='0.1.0',
    packages=find_packages(),
    description='Utility functions for interacting with Kubernetes secrets.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Maxwell Pryce',
    author_email='maxwell.pryce@qbdc.ch',
    url='https://github.com/yourusername/k8s-utilities',
    install_requires=[
        'kubernetes>=12.0.0',
        'base64',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
    python_requires='>=3.6',
)
