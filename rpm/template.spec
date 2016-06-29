Name:           ros-kinetic-turtlebot-apps
Version:        2.3.6
Release:        0%{?dist}
Summary:        ROS turtlebot_apps package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/turtlebot_apps
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-turtlebot-actions
Requires:       ros-kinetic-turtlebot-calibration
Requires:       ros-kinetic-turtlebot-follower
Requires:       ros-kinetic-turtlebot-navigation
Requires:       ros-kinetic-turtlebot-rapps
BuildRequires:  ros-kinetic-catkin

%description
turtlebot_apps is a group of simple demos and exmaples to run on your TurtleBot
to help you get started with ROS and TurtleBot.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Wed Jun 29 2016 Daniel Stonier <stonier@rnd.yujinrobot.com> - 2.3.6-0
- Autogenerated by Bloom

* Tue Jun 28 2016 Daniel Stonier <stonier@rnd.yujinrobot.com> - 2.3.5-0
- Autogenerated by Bloom

