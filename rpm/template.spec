Name:           ros-hydro-openrtm-ros-bridge
Version:        1.2.6
Release:        0%{?dist}
Summary:        ROS openrtm_ros_bridge package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/openrtm_ros_bridge
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-openrtm-tools
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-std-msgs
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-openrtm-tools
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-rostest
BuildRequires:  ros-hydro-rtmbuild
BuildRequires:  ros-hydro-std-msgs

%description
openrtm_ros_bridge package provides basic functionalities to bind two robotics
framework: OpenRTM and ROS. By using this package, you can write your ROS
packages that communicate with your non-ROS robots that run on OpenRTM. For
communicating with the robots that run on hrpsys, you can use hrpsys_ros_bridge
package.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Fri Oct 10 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.6-0
- Autogenerated by Bloom

* Sat Oct 04 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.5-2
- Autogenerated by Bloom

* Sat Oct 04 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.5-0
- Autogenerated by Bloom

* Sat Oct 04 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.5-1
- Autogenerated by Bloom

* Mon Sep 08 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.4-1
- Autogenerated by Bloom

* Mon Sep 08 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.4-0
- Autogenerated by Bloom

* Wed Sep 03 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.3-0
- Autogenerated by Bloom

* Sun Aug 31 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.2-0
- Autogenerated by Bloom

