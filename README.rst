`clip-the-gym` is just a script that:

  - takes a youtube url in your clipboard
  - tries to download it
  - extracts the audio in your ~/Music folder

It makes a nice 'hotkey' in whatever window manager you're using.

If you have notify-python installed, it will
pop up nice messages for you.

  - http://www.galago-project.org/downloads.php

You'll need to have ``xsel`` on your system::

  $ sudo yum -y install xsel

To install clip-the-gym itself:  ``$ pip install clip-the-gym``

----

Based off the code of `bitlyclip
<http://pypi.python.org/pypi/bitlyclip>`_.
