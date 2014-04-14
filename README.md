# What is this?

This is an example for teaching principles for good unit tests.

There are different stages of the example.

* [_master_](https://github.com/alexbepple/first-principles-python/tree/alpha) contains examples of bad tests. They are not unit tests at all or just bad unit tests.
* The branch [_beispielloesungen_](https://github.com/alexbepple/first-principles-python/tree/beispielloesungen) contains suggestions for fixing some of the non-obvious ones. For the Templater example, I have included two possible solutions.


# Run tests

Install dependencies.

    pip install -r requirements.txt

Now you should have a green bar.

    py.test

Run tests continuously.

    make tdd
