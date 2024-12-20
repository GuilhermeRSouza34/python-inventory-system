from setuptools import setup, find_packages

setup(
    name='python-inventory-system',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'openpyxl',
    ],
    entry_points={
        'console_scripts': [
            'inventory-system=main:main',  # Supondo que a função principal em main.py se chama main
        ],
    },
)