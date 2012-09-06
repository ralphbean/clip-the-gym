""" Clip-the-gym - download audio from youtube videos.

Requirements:

    $ sudo yum install xsel youtube-dl python-sh

For Melissa.

"""

import os
import optparse

try:
    import sh
except ImportError:
    import pbs as sh

pynotify = None
try:
    import pynotify
    pynotify.init('clip-the-gym')
except ImportError, e:
    pass


def notify(message, cls='dialog-message'):
    print message
    if not pynotify:
        return False
    notif = pynotify.Notification("clip-the-gym", message, cls)
    return notif.show()


def parse_args():
    p = optparse.OptionParser()
    # TODO -- add options here
    return p.parse_args()


def main(url):
    opts, args = parse_args()

    if "youtube.com" not in url:
        return "%r is not a valid youtube url." % url

    notify("Grabbing %r" % url)
    prefix = os.path.expanduser("~/Music/youtube")

    if not os.path.exists(prefix):
        os.makedirs(prefix)

    location = "%s/%%(stitle)s.%%(ext)s" % prefix
    output = sh.youtube_dl(
        url,
        extract_audio=True,
        audio_format="mp3",
        output=location,
    )
    # Just report on the last line of text..
    output = unicode(output).strip().split('\n')[-1]
    return output


def cmd():
    try:
        #Copy from the clipboard
        url = os.popen('xsel').read()

        # Grab it
        stdout = main(url)

        # And report
        notify(stdout)
    except Exception, e:
        notify("%s failed.\n%s" % (__file__, str(e)), 'dialog-warning')
