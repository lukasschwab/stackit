# stackit

<p align="center">

The essential sidekick to any superhero developer. <br />

<b>stackit</b> sends smart StackOverflow queries from your command line. <br />

<a href="http://stackitfor.me">stackitfor.me</a> -- Created at <a href="http://ucsbhacks.com">SB Hacks</a> 2015. <br />

<img src="http://i.giphy.com/3xz2BtvxJvZQb7Pyes.gif">
</p>

***

## Features

+ Written entirely in Python
+ Works on UNIX (Mac OS X, Linux); Windows support coming eventually!
+ Automatically pipes error messages into StackOverflow queries
+ Parses and displays relevant questions and answers directly on the command line in reader-friendly markdown format

## Installation

There are two ways to install stackit. Both should have roughly the same outcome, but have their advantages/disadvantages.

**1. PyPI/pip**

This method will always produce some stable build, but may not be the most up to date version. New functionality will come slower than building from this repo.

    $ pip install stackit

Note, depending on your computer's settings, you may need to `sudo pip install stackit`.

**2. Build from this repo**

This method will always include the latest features, but sometimes will not work at all. Oops!

Clone the repo, then use setup.py to install the package. Note, this process will differ only slightly in a non-bash shell.

    $ git clone https://github.com/lukasschwab/stackit.git
    $ cd stackit
    $ python setup.py install

Note, depending on your computer's settings, you may need to `sudo python setup.py install`.

## Usage

The install process establishes an alias, `stackit`, for stackit_core.py's functionality. Instead of using `python stackit_core.py`, you will *always* simply use `stackit` at the command prompt.

<p align="center"><img src="http://i.imgur.com/Y9hpErQ.gif"></p>

### Command line arguments
+ `-h`, `--help`: version splash page // usage
+ `-s`: `--search`: search by user term (string)
+ `--version`: simple version report
+ `--verbose`: full text of top result and accepted answer
+ `-e`: `--stderr`: runs your program and searches by stderr output
+ `-t`: `--tags`: searches by tags in particular (multiple arguments)

### Interface flow commands
+ `m`: more: shows the next 5 questions
+ #: select: shows full question//top answer text in focus -- be careful that it's clearly not the SO question ID, but the list index
+ `--b`: opens focused question in browser
+ `--x`: exit: go back to the list focus

### Examples
To search Stack Overflow for "How do I create a bash alias" with the tags, "shell";

    $ stackit -s "How do I create a bash alias?" -t "shell"
More examples on [our website](http://www.stackitfor.me)

## Thanks
This project is possible because of several other pre-existing projects and their contributors:

+ [Py-StackExchange](https://github.com/lucjon/Py-StackExchange): a Python wrapper for the StackExchange API
+ [Requests](https://github.com/kennethreitz/requests): "HTTP for Humans"
+ [Beautiful Soup 4](http://www.crummy.com/software/BeautifulSoup/bs4/doc/): pretty data parsing for HTML/XML files, so you can read stuff
+ [Pyfancy](https://github.com/ilovecode1/pyfancy) makes your print statements colorful // legible. This project doesn't incorporate `pyfancy.py` verbatim, but this project demonstrates the method.
+ [Karan Goel](https://github.com/karan)'s work with [joe](https://github.com/karan/joe) was a tremendous help in designing a command line tool in Python, and his [Medium article](https://medium.com/@karan/these-6-simple-changes-made-my-recent-side-project-go-viral-53fd6571c11c) on putting together a good readme is an inspiration to us all. Thank you based joe.
+ Peter Downs has a great [article](http://peterdowns.com/posts/first-time-with-pypi.html) on how to submit a package to PyPI.

## Contributing

We <3 issue submissions, and address your problem as quickly as possible!

If you want to write code:

1. Fork the repository
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'add some feature'`)
4. Push to your branch (`git push origin my-new-feature`)
5. Create a new Pull Request

### Contributors

#### OG (SB Hacks 2015 Crew)

+ [Vicki Niu](https://github.com/vickiniu)
+ [Leilani Reyes](https://github.com/lanidelrey)
+ [Eni Asebiomo](https://github.com/eniasebiomo)
+ [Lukas Schwab](https://github.com/lukasschwab)

#### Pull Requests

+ [Phil (schwartzmx)](https://github.com/schwartzmx): [#4](https://github.com/lukasschwab/stackit/pull/4), [#6](https://github.com/lukasschwab/stackit/pull/6)
+ [Steeve (WnP)](https://github.com/WnP): [#8](https://github.com/lukasschwab/stackit/pull/8#issuecomment-73205402), [#7](https://github.com/lukasschwab/stackit/pull/7), [#9](https://github.com/lukasschwab/stackit/pull/9), [README .gif 2/10/15](http://i.imgur.com/Y9hpErQ.gif), [#10](https://github.com/lukasschwab/stackit/pull/10), [#13](https://github.com/lukasschwab/stackit/pull/13), [#14](https://github.com/lukasschwab/stackit/pull/14)
+ [Robert (grobbie94)](https://github.com/grobbie94): [#12](https://github.com/lukasschwab/stackit/pull/12)
