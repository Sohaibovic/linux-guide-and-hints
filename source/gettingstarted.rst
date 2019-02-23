Getting started
^^^^^^^^^^^^^^^

To save yourself time, you may prefer to download a `respin ISO <https://dl.fedoraproject.org/pub/alt/live-respins/>`_ that has updates
preinstalled. The ``WORK`` ISO comes with GNOME. We will be using packages and
repositories solely from `negativo17.org <https://negativo17.org/>`_ and *not*
RPMFusion (which is not compatible anyway). A few notes:

- gstreamer 0.10 is deprecated, install gstreamer1. The good news is that the
  myriad of packages has been reduced to about 5.

- Since we are not using RPMFusion, ``libmpg123`` is now ``mpg123``

The :doc:`fedora/negativo` article contains more information. This
script will get you off your feet (adapted from `Louis' script <https://github.com/nazunalika/useful-scripts/blob/master/fedora/fedora-desk.sh>`_):

.. raw:: html

   <script src="https://gist.github.com/remyabel/bbebf3043860abe24a19bf0b1d67bd33.js"></script>

Please don't use Skype unless you enjoy having the NSA read your messages. Finally, check out the
:doc:`fedora/pulseaudio` articles on troubleshooting tips.

Other things
------------

negativo17 provides Flash as well, but you should probably just avoid Flash altogether,
or at least leave it on "Ask to Activate". Fortunately, it seems most of the web has ditched
Flash in favor of moving to HTML5 for web players. I haven't had to activate Flash in a long
time.

Again, negativo17 provides Steam. However, if you have any games that are
Window only, you need to download Steam via Wine and install the games that way
or use Proton. See the :doc:`fedora/winetips` article for more information.

Finally, to ensure that Negativo's repo takes precedence over RPMFusion, edit ``/etc/yum.repos.d/fedora-multimedia.repo``
and add ``priority=1`` under ``[fedora-multimedia]``.
