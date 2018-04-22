# Script generated with Bloom
pkgdesc="ROS - This package gives transparency between RTM and ROS. rtmros-data-bridge.py is a RT-Component for dataport/topic. This automatically convert ROS/topic into RTM/dataport."
url='http://ros.org/wiki/rosnode_rtc'

pkgname='ros-kinetic-rosnode-rtc'
pkgver='1.4.2_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-openrtm-tools'
'ros-kinetic-roscpp-tutorials'
'ros-kinetic-rospy'
'ros-kinetic-rostopic'
)

depends=('ros-kinetic-openrtm-tools'
)

conflicts=()
replaces=()

_dir=rosnode_rtc
source=()
md5sums=()

prepare() {
    cp -R $startdir/rosnode_rtc $srcdir/rosnode_rtc
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

