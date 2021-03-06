#!/usr/bin/env python3

import codecs
import os
from distutils.core import setup

version = '?'
root = os.path.dirname(os.path.abspath(__file__))
# Path to __version__ module
version_file = os.path.join(root, 'roberta', '__version__.py')
# Check if this is a source distribution.
# If not create the __version__ module containing the version
if not os.path.exists(os.path.join(root, 'PKG-INFO')):
    fd = codecs.open(version_file, 'w', 'utf-8')
    fd.write('version = %r\n' % os.getenv('VERSION', '?'))
    fd.close()
# Load version
exec(open(version_file).read())

# TODO: convert README.md to long_desc
# https://gist.github.com/aubricus/9184003#file-setup_snippet-py

setup(name='openrobertalab',
      version=version,
      description='lab.open-roberta.org connector for ev3dev.org',
      author='Stefan Sauer',
      author_email='ensonic@google.com',
      url='https://www.open-roberta.org/',
      scripts=['openrobertalab'],
      packages=['roberta'],
      package_data={'roberta': ['ter-*.p??']},
      # other deps: apt-get-install python3-bluez python3-dbus python3-ev3dev python3-gi
      # install_requires=['python3-ev3dev']
      )
