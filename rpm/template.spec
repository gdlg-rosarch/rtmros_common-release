Name:           ros-hydro-rosnode-rtc
Version:        1.2.11
Release:        0%{?dist}
Summary:        ROS rosnode_rtc package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rosnode_rtc
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-openrtm-tools
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-openrtm-tools
BuildRequires:  ros-hydro-roscpp-tutorials
BuildRequires:  ros-hydro-rospy
BuildRequires:  ros-hydro-rostopic

%description
This package gives transparency between RTM and ROS. rtmros-data-bridge.py is a
RT-Component for dataport/topic. This automatically convert ROS/topic into
RTM/dataport.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
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
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Sat Apr 25 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.11-0
- Autogenerated by Bloom

* Fri Apr 24 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.10-0
- Autogenerated by Bloom

* Thu Apr 16 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.9-1
- Autogenerated by Bloom

* Sun Apr 12 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.9-0
- Autogenerated by Bloom

* Mon Mar 09 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.8-0
- Autogenerated by Bloom

* Fri Feb 13 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.7-0
- Autogenerated by Bloom

* Fri Oct 10 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.6-0
- Autogenerated by Bloom

* Sat Oct 04 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.5-2
- Autogenerated by Bloom

* Sat Oct 04 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.5-1
- Autogenerated by Bloom

* Sat Oct 04 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.5-0
- Autogenerated by Bloom

* Mon Sep 08 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.4-1
- Autogenerated by Bloom

* Mon Sep 08 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.4-0
- Autogenerated by Bloom

* Wed Sep 03 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.3-0
- Autogenerated by Bloom

* Sun Aug 31 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.2-0
- Autogenerated by Bloom

