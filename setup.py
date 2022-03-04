from setuptools import setup, find_packages


def main():
    with open('requirements.txt') as file:
        requirements = file.read().splitlines()

    setup(
        name='ixload_py',
        description='Python wrapper for IxLoad automation',
        author='Alberto Villarreal',
        author_email='alberto.villarreal@keysight.com',

        version='1.0',
        install_requires=requirements,
        packages=find_packages(where='Utils'),
        package_dir={'': 'Utils'}
    )


if __name__ == '__main__':
    main()
