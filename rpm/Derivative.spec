#
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
#

Name:       Derivative

# >> macros
# << macros

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    Derivative
Version:    0.8.3
Release:    1
Group:      Qt/Qt
License:    LGPLv3
URL:        http://www.robertocolistete.net/derivative/
Source0:    %{name}-%{version}.tar.bz2
BuildArch:  noarch
Requires:   libsailfishapp-launcher
Requires:   sailfishsilica-qt5 >= 0.10.9
Requires:   pyotherside-qml-plugin-python3-qt5 >= 1.2
Requires:   python3-base
Requires:   python3-sympy

BuildRequires:  qt5-qttools-linguist
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.3
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  desktop-file-utils

%description
Derivative - Calculation of mathematical derivatives using Python & SymPy module

%if "%{?vendor}" == "chum"
PackageName: Derivative
Type: desktop-application
Categories:
 - Science
 - Utility
DeveloperName: Roberto Colistete
PackagerName: Mark Washeim (poetaster)
Custom:
 - Repo: https://github.com/rcolistete/derivative-sailfish
 - PackagingRepo: https://github.com/sailfishos-chum/derivative-sailfish
Icon: https://github.com/sailfishos-chum/derivative-sailfish/blob/c80a621e04bbf247139c393b5776eb717be0e206/Derivative.png
%endif


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qtc_qmake5

%qtc_make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%defattr(0644,root,root,-)
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
# >> files
# << files
