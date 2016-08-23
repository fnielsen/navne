# -*- coding: utf-8 -*-
"""Gender.

Usage:
    gender <name>


Description:

    python -m navne.gender Finn

"""

from __future__ import division, print_function

import codecs

from os.path import join, split


class Gender(object):
    """Gender algorithms."""

    def __init__(self):
        self.setup_name_files()

    def load_name_file(self, filename):
        """Load a name file.

        Parameters
        ----------
        filename : str
            Full filename path to text file.

        Returns
        -------
        names : list with (unicode) str
           List with names.

        """
        with codecs.open(filename, encoding='utf-8') as f:
            names = [name.strip() for name in f.readlines()]
        return names

    def setup_name_files(self):
        """Setup up data structure for gender prediction."""
        data_path = join(split(__file__)[0], 'data')
        self.name_to_gender_map = {}
        datasets = [
            ('pigenavne.txt', 0.0),
            ('drengenavne.txt', 1.0),
            ('unisexnavne.txt', 0.5)]
        for filename, value in datasets:
            names = self.load_name_file(join(data_path, filename))
            for name in names:
                self.name_to_gender_map[name] = value

    def predict(self, name):
        u"""Predict gender of name.

        Parameters
        ----------
        name : str
            String with name

        Returns
        -------
        value : float
            Value for gender.

        Examples
        --------
        >>> gender = Gender()
        >>> gender.predict('Finn')
        1.0
        >>> gender.predict('Anna')
        0.0
        >>> gender.predict('ZZZ')
        0.5
        >>> gender.predict(u'Bjørn')
        1.0
        >>> gender.predict('Finn Nielsen')
        1.0

        """
        name_parts = name.split()
        return self.name_to_gender_map.get(name_parts[0], 0.5)


def main():
    """Handle command-line interface."""
    import sys

    from docopt import docopt

    arguments = docopt(__doc__)

    gender = Gender()

    encoding = sys.getfilesystemencoding()
    name = arguments['<name>'].decode(encoding)
    value = gender.predict(name)
    print(value)


if __name__ == '__main__':
    main()
