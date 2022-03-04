from setuptools import setup, find_packages


def main():
    with open('requirements.txt') as file:
        requirements = file.read().splitlines()

    setup(
        name='ixload_py',
        keywords='IxLoad test automation',
        description='Python wrapper for IxLoad automation',
        author='Alberto Villarreal',
        author_email='alberto.villarreal@keysight.com',
        url='https://github.com/albertovillarreal-keys/ixload_py',
        version='1.0',
        install_requires=requirements,
        packages=find_packages(where='Utils'),
        package_dir={'': 'Utils'},
        classifiers=[
                    'Programming Language :: Python :: 3.7',
                    'Programming Language :: Python :: 3.8',
                    'Intended Audience :: Developers',
                    'License :: OSI Approved :: MIT License',
                    'Operating System :: OS Independent',
                ]
    )


if __name__ == '__main__':
    main()
