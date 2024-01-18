from setuptools import setup, find_packages

setup(
    name='kaggle_competition',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ejecucion_proyecto = mi_repo.__main__:main',
        ],
    },
)
