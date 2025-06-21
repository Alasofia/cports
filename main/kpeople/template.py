pkgname = "kpeople"
pkgver = "6.15.0"
pkgrel = 0
build_style = "cmake"
# FIXME: off by one in rows after merging people
make_check_args = ["-E", "personsmodeltest"]
hostmakedepends = ["cmake", "extra-cmake-modules", "gettext", "ninja"]
makedepends = [
    "kcontacts-devel",
    "kitemviews-devel",
    "kwidgetsaddons-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
# qt sqlite use at runtime
depends = ["qt6-qtbase-sql"]
checkdepends = [*depends]
pkgdesc = "KDE contact api"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kpeople/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kpeople-{pkgver}.tar.xz"
sha256 = "5005f39b72578569a0cb9523e57cf8e62e81572326fc691be9fbecf28e638ea8"
hardening = ["vis"]


@subpackage("kpeople-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]

    return self.default_devel()
