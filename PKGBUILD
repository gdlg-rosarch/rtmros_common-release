# Script generated with Bloom
pkgdesc="ROS - hrpsys_ros_bridge package provides basic functionalities to bind <a href="http://wiki.ros.org/hrpsys">hrpsys</a>, a <a href="http://openrtm.org/">OpenRTM</a>-based controller, and ROS.<br/> By using this package, you can write your ROS packages that communicate with your non-ROS robots that run on hrpsys. For communicating with the robots that run on OpenRTM without hrpsys, you can use <a href="http://wiki.ros.org/openrtm_ros_bridge">openrtm_ros_bridge</a> package."
url='http://wiki.ros.org/hrpsys_ros_bridge'

pkgname='ros-kinetic-hrpsys-ros-bridge'
pkgver='1.4.2_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('git'
'inetutils'
'net-tools'
'pkg-config'
'procps-ng'
'python2-rosdep'
'ros-kinetic-actionlib'
'ros-kinetic-angles'
'ros-kinetic-camera-info-manager'
'ros-kinetic-catkin'
'ros-kinetic-collada-urdf'
'ros-kinetic-control-msgs'
'ros-kinetic-diagnostic-aggregator'
'ros-kinetic-diagnostic-msgs'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-euscollada'
'ros-kinetic-geometry-msgs'
'ros-kinetic-hrpsys-tools'
'ros-kinetic-hrpsys>=315.3.1'
'ros-kinetic-image-transport'
'ros-kinetic-message-generation'
'ros-kinetic-mk'
'ros-kinetic-nav-msgs'
'ros-kinetic-pr2-msgs'
'ros-kinetic-robot-pose-ekf'
'ros-kinetic-robot-state-publisher'
'ros-kinetic-rosbuild'
'ros-kinetic-roscpp'
'ros-kinetic-roslang'
'ros-kinetic-rosnode'
'ros-kinetic-rostest'
'ros-kinetic-rqt-gui'
'ros-kinetic-rqt-gui-py'
'ros-kinetic-rqt-robot-dashboard'
'ros-kinetic-rqt-robot-monitor'
'ros-kinetic-rtmbuild'
'ros-kinetic-sensor-msgs'
'ros-kinetic-tf'
'ros-kinetic-visualization-msgs'
'subversion'
)

depends=('ipython2'
'python2-psutil'
'ros-kinetic-actionlib'
'ros-kinetic-camera-info-manager'
'ros-kinetic-collada-urdf'
'ros-kinetic-control-msgs'
'ros-kinetic-diagnostic-aggregator'
'ros-kinetic-diagnostic-msgs'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-geometry-msgs'
'ros-kinetic-hrpsys'
'ros-kinetic-hrpsys-tools'
'ros-kinetic-image-transport'
'ros-kinetic-nav-msgs'
'ros-kinetic-pr2-msgs'
'ros-kinetic-robot-pose-ekf'
'ros-kinetic-robot-state-publisher'
'ros-kinetic-roscpp'
'ros-kinetic-rosnode'
'ros-kinetic-rostest'
'ros-kinetic-rqt-gui'
'ros-kinetic-rqt-gui-py'
'ros-kinetic-rqt-robot-dashboard'
'ros-kinetic-rqt-robot-monitor'
'ros-kinetic-rtmbuild'
'ros-kinetic-sensor-msgs'
'ros-kinetic-tf'
'ros-kinetic-visualization-msgs'
)

conflicts=()
replaces=()

_dir=hrpsys_ros_bridge
source=()
md5sums=()

prepare() {
    cp -R $startdir/hrpsys_ros_bridge $srcdir/hrpsys_ros_bridge
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

