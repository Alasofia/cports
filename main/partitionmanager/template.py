pkgname = "partitionmanager"
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
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kio-devel",
    "kjobwidgets-devel",
    "kpmcore-devel",
    "kwidgetsaddons-devel",
    "kwindowsystem-devel",
    "kxmlgui-devel",
    "polkit-qt-1-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE drive management utility"
license = "GPL-3.0-or-later"
url = "https://apps.kde.org/partitionmanager"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/partitionmanager-{pkgver}.tar.xz"
)
sha256 = "216a4574d9b63b52c74ab386c92cf8d5c2b634afecbcfbdd734b68d9fce5ebca"
