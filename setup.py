from setuptools import setup, find_packages

setup(
    name='repo_prueba_kaggle',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ejecucion_proyecto = repo_prueba_kaggle.__main__:main',
        ],
    },
)
