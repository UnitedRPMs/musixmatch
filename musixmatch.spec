AutoReqProv: no
%global debug_package %{nil}
%global opt_mu /opt/Musixmatch

Summary: Installer for the musixmatch
Name: musixmatch
Version: 3.6.1
Release: 1%{dist}
License: Proprietary
Group: Applications/Internet
URL: https://www.musixmatch.com/
Source: eula.html
Requires: xz tar wget curl
Requires: gtk-update-icon-cache libnotify libXtst nss
BuildRequires: binutils xz tar curl dpkg
# Display the lyrics of the currently playing song
Recommends: spotify-client
ExclusiveArch: x86_64

%description

This package will download and install the proprietary musixmatch.

Lyrics platform where users can search and share lyrics.

%prep

# The installation
echo 'Downloading musixmatch, please wait...'
curl 'https://download-app.musixmatch.com/' -A 'Linux x86_64' -D headers.txt -OJf

# extract data from the deb package
mkdir -p $PWD/out
ar x %{name}*.deb 
if [ -f data.tar.xz ]; then
tar xaf data.tar.xz -C $PWD/out
elif [ -f data.tar.gz ]; then 
tar xmzvf data.tar.gz -C $PWD/out
fi

%autosetup -T -D -n out
cp -f %{S:0} $PWD

%build

%install
mkdir -p %{buildroot}/opt/
cp -rf opt/ %{buildroot}/
cp -rf usr/ %{buildroot}/

mkdir -p "%{buildroot}/usr/bin"
ln -s /opt/Musixmatch/%{name} "%{buildroot}/usr/bin/%{name}"

%files
%defattr(-,root,root)
%license eula.html
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_docdir}/musixmatch/changelog.gz
%{_datadir}/icons/hicolor/*/apps/musixmatch.png
%{opt_mu}/

%changelog

* Wed Aug 21 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 3.6.1-1
- Updated to 3.6.1

* Thu Aug 08 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 3.6.0-1
- Updated to 3.6.0

* Fri Jun 07 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 3.3.1-1
- Updated to 3.3.1

* Fri May 17 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 3.2.0-1
- Updated to 3.2.0

* Tue Apr 23 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 0.21.26-1
- Updated to 0.21.26

* Mon Oct 22 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 0.21.4-1
- Updated to 0.21.4

* Fri Sep 07 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 0.20.20-1
- Updated to 0.20.20

* Mon May 07 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 0.19.4-1
- Initial build
