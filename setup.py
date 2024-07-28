from setuptools import setup, find_packages

setup(
    name='classical-archives',
    version='0.1.0',
    description='A package to fetch classical composers information from Classical Archives',
    author='JarbasAI',
    author_email='jarbasai@mailfence.com',
    url='https://github.com/OpenJarbas/classical_archives',
    packages=["classical_archives"],
    install_requires=[
        'requests'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
