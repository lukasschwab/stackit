from setuptools import setup, find_packages
setup(
    name = "stackit",
    version = "0.1.0",
    packages = find_packages(),
    
    # dependencies
    install_requires=[
        'Py-StackExchange',
        'requests',
        'beautifulsoup4',
        'html2text',
    ],

    # metadata for upload to PyPI
    author = "SB Hacks Crew",
    author_email = "lukas.schwab@gmail.com",
    description = "stackit sends smart StackOverflow queries from your command line",
    license = "MIT",
    keywords = "error stderr stack overflow stackoverflow stack exchange stackexchange",
    url = "http://stackitfor.me", # project homepage
)
