pkgname = "plasma-disks"
pkgver = "6.4.0"
pkgrel = 0
build_style = "cmake"
# XXX drop libexec
configure_args = ["-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib"]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcoreaddons-devel",
    "kdbusaddons-devel",
    "knotifications-devel",
    "ki18n-devel",
    "solid-devel",
    "kservice-devel",
    "kio-devel",
    "kauth-devel",
    "kcmutils-devel",
    "qt6-qtdeclarative-devel",
]
depends = ["smartmontools"]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE disk failure monitor"
license = "GPL-2.0-only OR GPL-3.0-only"
url = "https://invent.kde.org/plasma/plasma-disks"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma-disks-{pkgver}.tar.xz"
sha256 = "94c95ed1bd494448c81e35360dc8b49ae05acec131651ec81716f4a52218ea90"
hardening = ["vis"]
