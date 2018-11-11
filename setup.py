from setuptools import setup

setup(
    name='morphine-maker',
    packages=['morphine'],
    version='2.0.2',
    author='Gurkirat Singh',
    author_email='tbhaxor@gmail.com',
    url='https://github.com/tbhaxor/morphine',
    download_url='https://github.com/tbhaxor/morphine/archive/master.zip',
    description=
    'Morphine is GUI python framework that empowers you to create a setup.py in approx 4 - 5 mins',
    long_description=open('/mnt/Programs/python/morphine/README.md').read(),
    long_description_content_type="text/markdown",
    license='',
    keywords='morphine, maker, tbhaxor, t3r@byt3, gurkirat, framework',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: X11 Applications :: Qt',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.3',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License'
    ],
    python_requires='>=2, >=3',
    entry_points={'gui_scripts': ['morphine=morphine.startup:main']})
