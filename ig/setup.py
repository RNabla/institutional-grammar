import setuptools

setuptools.setup(
    name='ig',
    version='1.0',
    description='',
    author='',
    author_email='example@evil.com',
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': ['ig = ig.main:console_entry']
    }
)
