# What is this?

This is an example for teaching principles for good unit tests.

This branch contain different stages of the example. _master_ is most likely not where you want to start.

* [_alpha_](https://github.com/alexbepple/first-principles-python/tree/alpha) contains examples of bad tests. They are not unit tests at all or just bad unit tests. `git checkout alpha` gets you there.
* The tip of this branch contains suggestions for fixing some of the non-obvious ones. For the Templater example, I have included two possible solutions.


# Run tests

Install dependencies.

    pip install -r requirements.txt

Now you should have a green bar.

    make test.once


# Run tests continuously

Install dependencies

    bundle install

If you are not on OS X, you are better off with

    bundle install --without osx

Now the tests will automatically rerun when you change files.

    make test.continuously
