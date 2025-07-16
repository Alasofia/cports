pkgname = "kimageformats"
pkgver = "6.16.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DKIMAGEFORMATS_HEIF=ON"]
# jpegxr; exr write fails on ppc64le
# dds; read fails on ppc64le
# xcf; read fails on aarch64
# avci; needs libheif built against openh264 but that SIGILLs atm
make_check_args = [
    "-E",
    "kimageformats-(write-exr|read-(dds|hej2|xcf|avci))",
]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja", "pkgconf"]
makedepends = [
    "karchive-devel",
    "libavif-devel",
    "libheif-devel",
    "libjxl-devel",
    "libraw-devel",
    "openexr-devel",
    "openjpeg-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "Image format plugins for Qt6"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kimageformats/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kimageformats-{pkgver}.tar.xz"
sha256 = "86dfbb05ab845f7b19a7fec88e135d14e47af14dc1713d9fb391966510c1dc4b"
