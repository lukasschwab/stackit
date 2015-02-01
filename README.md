# stackit

<p align="center">

The essential sidekick to any superhero developer. <br />

<b>stackit</b> sends smart StackOverflow queries from your command line. <br />

Created at <a href="http://ucsbhacks.com">SB Hacks</a> 2015. <br />

<img src="http://i.giphy.com/3xz2BtvxJvZQb7Pyes.gif">
</p>

***

## Features

This currently includes some future features––update before pitch/etc

+ Written in Python
+ Works on Mac, Windows
+ Automatically pipes error messages into StackOverflow queries
+ Parses and displays relevant questions and answers directly on the command line in reader-friendly markdown format
+ Pay it forward––stackit integrates suggested answer contribution into your development process.

<br>

## Usage
To run the search arguments, there are two usages:

+ 'stackit -s "query"' runs a search of StackOverflow for the query put in quotation marks
+ 'stackit -p "command"' will run your command, (ex: python script.py) and automatically search StackOverflow for the generated error, if any

### Args
+ -v: verbose
+ -b: browser
+ -f: filter
+ -s: save
+ --version: version me, bro

### Command line arguments
+ none: version splash page // usage
+ `-h`, `--help`: version splash page // usage
+ `--version`: simple version report
+ `--verbose`: full text of top result and accepted answer
+ `-e`: `--stderr`: runs your program and searches by stderr output
+ `-s`: `--search`: search by user term (string)
+ `-t`: `--tags`: searches by tags in particular (multiple arguments)

### Interface flow commands
+ `m`: more: shows the next 5 questions
+ #: select: shows full question//top answer text in focus -- be careful that it's clearly not the SO question ID, but the list index
+ `--b`: opens focused question in browser
+ `--x`: exit: go back to the list focus

<br>

## Thanks
This project is possible because of several other pre-existing projects and their contributors:

+ [Py-StackExchange](https://github.com/lucjon/Py-StackExchange): a Python wrapper for the StackExchange API
+ [Requests](https://github.com/kennethreitz/requests): "HTTP for Humans"
+ [Beautiful Soup 4](http://www.crummy.com/software/BeautifulSoup/bs4/doc/): pretty data parsing for HTML/XML files, so you can read stuff
+ [Karan Goel](https://github.com/karan)'s work with [joe](https://github.com/karan/joe) was a tremendous help in designing a command line tool in Python, and his [Medium article](https://medium.com/@karan/these-6-simple-changes-made-my-recent-side-project-go-viral-53fd6571c11c) on putting together a good readme is an inspiration to us all. Thank you based joe.
+ Peter Downs has a great [article](http://peterdowns.com/posts/first-time-with-pypi.html) on how to submit a package to PyPI.

<br>

## Contributing

Contribution instructions coming soon.

For now, *hands off*.

<br>

### Contributors
+ [Vicki Niu](https://github.com/vickiniu)
+ [Leilani Reyes](https://github.com/lanidelrey)
+ [Eni Asebiomo](https://github.com/eniasebiomo)
+ [Lukas Schwab](https://github.com/lukasschwab)

***

## To-Do

+ README:
    + Installation instructions
    + Usage instructions
    + Contribution instructions
+ stackit-core.py:
+ Bash wrapper for stackit-core.py:
