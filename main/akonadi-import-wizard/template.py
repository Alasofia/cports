pkgname = "akonadi-import-wizard"
pkgver = "25.04.3"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "akonadi-devel",
    "karchive-devel",
    "kauth-devel",
    "kconfig-devel",
    "kcontacts-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "kiconthemes-devel",
    "kidentitymanagement-devel",
    "kio-devel",
    "kmailtransport-devel",
    "mailcommon-devel",
    "mailimporter-devel",
    "messagelib-devel",
    "pimcommon-devel",
    "qt6-qtdeclarative-devel",
    "qtkeychain-devel",
]
pkgdesc = "KDE Akonadi assistant for importing data into KDEPIM"
license = "LGPL-2.0-or-later AND GPL-2.0-or-later"
url = "https://invent.kde.org/pim/akonadi-import-wizard"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/akonadi-import-wizard-{pkgver}.tar.xz"
sha256 = "a397fdb3739ad4cb93c0d97f796689aa78f48fb2965f0fad5d804162a8a44c1c"


@subpackage("akonadi-import-wizard-devel")
def _(self):
    self.depends += ["kmailtransport-devel"]
    return self.default_devel()
