from setuptools import setup

setup(
    name='loggers',
    version='0.1.4',
    author='jonDel',
    author_email='jdellagostin@gmail.com',
    url='https://github.com/jonDel/loggers',
    packages=['loggers'],
    license='GPLv3',
    classifiers=[
     'Development Status :: 3 - Alpha',
     'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
     'Programming Language :: Python :: 2.6',
     'Programming Language :: Python :: 2.7',
     'Programming Language :: Python :: 3.6',
     'Topic :: System :: Logging',
    ],
    description='Usefull wrapper methods for logging native package',
    long_description=open('README.rst').read(),
    install_requires=[],
    include_package_data=True,
    zip_safe=False,
)
