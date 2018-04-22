# Script generated with Bloom
pkgdesc="ROS - A package suite that provides all the capabilities for the ROS users to connect to the robots that run on <a href="http://www.openrtm.org/openrtm/en/content/what-rt-middleware-0">RT Middleware</a> or RTM-based controllers."
url='http://wiki.ros.org/rtmros_common'

pkgname='ros-kinetic-rtmros-common'
pkgver='1.4.2_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-hrpsys-ros-bridge'
'ros-kinetic-hrpsys-tools'
'ros-kinetic-openrtm-ros-bridge'
'ros-kinetic-openrtm-tools'
'ros-kinetic-rosnode-rtc'
'ros-kinetic-rtmbuild'
)

conflicts=()
replaces=()

_dir=rtmros_common
source=()
md5sums=()

prepare() {
    cp -R $startdir/rtmros_common $srcdir/rtmros_common
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

