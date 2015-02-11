from setuptools import setup


setup(
    name="stackit",
    version="0.1.5",
    packages=['stackit'],

    # dependencies
    install_requires=[
        'Py-StackExchange',
        'requests',
        'beautifulsoup4',
        'html2text',
        'Click',
    ],

    # metadata for upload to PyPI
    author="SB Hacks Crew",
    author_email="lukas.schwab@gmail.com",
    description="stackit sends smart StackOverflow queries from your command line",
    license="MIT",
    keywords="error stderr stack overflow stackoverflow stack exchange stackexchange",
    url="http://stackitfor.me",  # project homepage
    download_url="https://github.com/lukasschwab/stackit/tarball/0.1.5",

    entry_points={
        'console_scripts': [
            'stackit=stackit.stackit_core:main'
        ]
    }
)
