# Script generated with Bloom
pkgdesc="ROS - openrtm_ros_bridge package provides basic functionalities to bind two robotics framework: <a href="http://openrtm.org/">OpenRTM</a> and ROS.<br/> By using this package, you can write your ROS packages that communicate with your non-ROS robots that run on OpenRTM. For communicating with the robots that run on hrpsys, you can use <a href="http://wiki.ros.org/hrpsys_ros_bridge">hrpsys_ros_bridge</a> package."
url='http://wiki.ros.org/openrtm_ros_bridge'

pkgname='ros-kinetic-openrtm-ros-bridge'
pkgver='1.4.2_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-message-generation'
'ros-kinetic-openrtm-tools'
'ros-kinetic-roscpp'
'ros-kinetic-rostest'
'ros-kinetic-rtmbuild'
'ros-kinetic-std-msgs'
)

depends=('ros-kinetic-openrtm-tools'
'ros-kinetic-roscpp'
'ros-kinetic-std-msgs'
)

conflicts=()
replaces=()

_dir=openrtm_ros_bridge
source=()
md5sums=()

prepare() {
    cp -R $startdir/openrtm_ros_bridge $srcdir/openrtm_ros_bridge
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

