# Script generated with Bloom
pkgdesc="ROS - The openrtm_tools package"
url='http://ros.org/wiki/openrtm_tools'

pkgname='ros-kinetic-openrtm-tools'
pkgver='1.4.2_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-openrtm-aist'
'ros-kinetic-openrtm-aist-python'
'ros-kinetic-rosbash'
'ros-kinetic-rostest'
'ros-kinetic-rtshell'
)

depends=('ros-kinetic-openrtm-aist'
'ros-kinetic-openrtm-aist-python'
'ros-kinetic-rosbash'
'ros-kinetic-rtshell'
)

conflicts=()
replaces=()

_dir=openrtm_tools
source=()
md5sums=()

prepare() {
    cp -R $startdir/openrtm_tools $srcdir/openrtm_tools
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

