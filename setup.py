from setuptools import setup, find_packages


setup(
    name='pybashutil',
    version='0.1',
    author='Omar Khairat',
    author_email='omaralkhairat@gmail.com',
    packages = find_packages(),
    package_dir = {'': '.'},
    entry_points = {
        'console_scripts' : [],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    zip_safe=True,
)