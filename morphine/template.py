__minimal__ = """
from setuptools import setup

setup(
    name='{name}',
    packages={packages},
    version='{version}',
    author='{auth_name}',
    author_email='{auth_email}',
    url='{home_url}',
    download_url='{down_url}',
    description='{short_desc}',
    long_description=open('{long_desc}').read(),
    long_description_content_type="text/markdown",
    license='{license}',
    keywords='{keywords}',
    classifiers={classifiers},
    python_requires='{python_required}')
"""

__minimal_deps__ = """
from setuptools import setup

setup(
    name='{name}',
    packages={packages},
    version='{version}',
    author='{auth_name}',
    author_email='{auth_email}',
    url='{home_url}',
    download_url='{down_url}',
    description='{short_desc}',
    long_description=open('{long_desc}').read(),
    long_description_content_type="text/markdown",
    license='{license}',
    keywords='{keywords}',
    classifiers={classifiers},
    install_requires={install_requires},
    python_requires='{python_required}')
"""

__minimal_exec__ = """
from setuptools import setup

setup(
    name='{name}',
    packages={packages},
    version='{version}',
    author='{auth_name}',
    author_email='{auth_email}',
    url='{home_url}',
    download_url='{down_url}',
    description='{short_desc}',
    long_description=open('{long_desc}').read(),
    long_description_content_type="text/markdown",
    license='{license}',
    keywords='{keywords}',
    classifiers={classifiers},
    python_requires='{python_required}',
    entry_points= {entry_points})
"""

__minimal_exec_deps__ = """
from setuptools import setup

setup(
    name='{name}',
    packages={packages},
    version='{version}',
    author='{auth_name}',
    author_email='{auth_email}',
    url='{home_url}',
    download_url='{down_url}',
    description='{short_desc}',
    long_description=open('{long_desc}').read(),
    long_description_content_type="text/markdown",
    license='{license}',
    keywords='{keywords}',
    classifiers={classifiers},
    python_requires='{python_required}',
    install_requires='{install_requires}',
    entry_points= {entry_points})
"""