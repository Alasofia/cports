pkgname = "udisks"
pkgver = "2.10.1"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--disable-static",
    "--with-udevdir=/usr/lib/udev",
    "--enable-lvm2",
    "--enable-btrfs",
    "--enable-bcache",
    "--enable-vdo",
    "--enable-lvmcache",
    "--enable-introspection",
]
hostmakedepends = [
    "automake",
    "bash",
    "docbook-xsl-nons",
    "gettext-devel",
    "glib-devel",
    "gobject-introspection",
    "gtk-doc-tools",
    "libtool",
    "libxslt-progs",
    "pkgconf",
    "polkit",
]
makedepends = [
    "acl-devel",
    "btrfs-progs-devel",
    "elogind-devel",
    "libatasmart-devel",
    "libblockdev-devel",
    "libgudev-devel",
    "lvm2-devel",
    "polkit-devel",
]
pkgdesc = "Daemon, tools and libraries for disk manipulation"
license = "GPL-2.0-or-later"
url = "https://www.freedesktop.org/wiki/Software/udisks"
source = f"https://github.com/storaged-project/udisks/releases/download/udisks-{pkgver}/udisks-{pkgver}.tar.bz2"
sha256 = "b75734ccf602540dedb4068bec206adcb508a4c003725e117ae8f994d92d8ece"


def post_install(self):
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.rename("usr/share/zsh/site-functions/_udisks2", "_udisksctl")


@subpackage("udisks-devel")
def _(self):
    return self.default_devel()


@subpackage("udisks-libs")
def _(self):
    return self.default_libs()
