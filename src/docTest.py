"""
docTest.py
====================================
The core module of my example project
copied from https://eikonomega.medium.com/getting-started-with-sphinx-autodoc-part-1-2cebbbca5365

author: Seth McNeill
copyright: 2025, Seth McNeill 
"""

def about_me(your_name):
    """
    Return the most important thing about a person.

    Parameters
    ----------
    your_name
        A string indicating the name of the person.

    """
    return "The wise {} loves Python.".format(your_name)


class ExampleClass:
    """An example docstring for a class definition."""

    def __init__(self, name):
        """
        Blah blah blah.

        Parameters
        ---------
        name
            A string to assign to the `name` instance attribute.

        """
        self.name = name

    def about_self(self):
        """
        Return information about an instance created from ExampleClass.
        """
        return "I am a very smart {} object.".format(self.name)