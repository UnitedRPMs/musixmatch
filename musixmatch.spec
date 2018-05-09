AutoReqProv: no
%global debug_package %{nil}
%global opt_mu /opt/Musixmatch
%define md5_musixmatch 0a95f8c685bf8f50553740c17878b015 

Summary: Installer for the musixmatch
Name: musixmatch
Version: 0.19.4
Release: 1%{dist}
License: Proprietary
Group: Applications/Internet
URL: https://www.musixmatch.com/
Requires: xz tar wget curl
Requires: gtk-update-icon-cache libnotify libXtst nss
BuildRequires: binutils xz tar wget curl 
# Display the lyrics of the currently playing song
Recommends: spotify-client
ExclusiveArch: x86_64

%description

This package will download and install the proprietary musixmatch.

Lyrics platform where users can search and share lyrics.

%prep

%build

%install

# Make destiny directories
install -dm 755 %{buildroot}/%{opt_mu} \
%{buildroot}/%{opt_mu}/locales \
%{buildroot}/%{opt_mu}/resources \
%{buildroot}/usr/share/icons/hicolor \
%{buildroot}/usr/share/doc/musixmatch \
%{buildroot}/%{_bindir} 

install -dm 755 %{buildroot}/%{_datadir}/applications
cat > %{buildroot}/%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Musixmatch
Comment=Musixmatch Desktop App
Exec="/usr/bin/musixmatch"
Terminal=false
Type=Application
Categories=AudioVideo;
Icon=musixmatch
EOF

# Icons
install -dm 755 %{buildroot}/usr/share/icons/hicolor/16x16/apps/ \
  %{buildroot}/usr/share/icons/hicolor/24x24/apps/ \
  %{buildroot}/usr/share/icons/hicolor/32x32/apps/ \
  %{buildroot}/usr/share/icons/hicolor/48x48/apps/ \
  %{buildroot}/usr/share/icons/hicolor/64x64/apps/ \
  %{buildroot}/usr/share/icons/hicolor/96x96/apps/ \
  %{buildroot}/usr/share/icons/hicolor/128x128/apps/ \
  %{buildroot}/usr/share/icons/hicolor/256x256/apps/ \
  %{buildroot}/usr/share/icons/hicolor/512x512/apps/ 

touch %{buildroot}/usr/share/icons/hicolor/16x16/apps/musixmatch.png
touch %{buildroot}/usr/share/icons/hicolor/24x24/apps/musixmatch.png
touch %{buildroot}/usr/share/icons/hicolor/32x32/apps/musixmatch.png
touch %{buildroot}/usr/share/icons/hicolor/48x48/apps/musixmatch.png
touch %{buildroot}/usr/share/icons/hicolor/64x64/apps/musixmatch.png
touch %{buildroot}/usr/share/icons/hicolor/96x96/apps/musixmatch.png
touch %{buildroot}/usr/share/icons/hicolor/128x128/apps/musixmatch.png
touch %{buildroot}/usr/share/icons/hicolor/256x256/apps/musixmatch.png
touch %{buildroot}/usr/share/icons/hicolor/512x512/apps/musixmatch.png

# The package
touch %{buildroot}/usr/share/doc/musixmatch/changelog.gz
chmod 755 %{buildroot}/usr/share/doc/musixmatch/changelog.gz
touch %{buildroot}%{opt_mu}/locales
touch %{buildroot}%{opt_mu}/resources
touch %{buildroot}%{opt_mu}/LICENSE.electron.txt
touch %{buildroot}%{opt_mu}/LICENSES.chromium.html
touch %{buildroot}%{opt_mu}/views_resources_200_percent.pak
chmod 755 %{buildroot}%{opt_mu}/views_resources_200_percent.pak
touch %{buildroot}%{opt_mu}/content_shell.pak
chmod 755 %{buildroot}%{opt_mu}/content_shell.pak
touch %{buildroot}%{opt_mu}/icudtl.dat
chmod 755 %{buildroot}%{opt_mu}/icudtl.dat
touch %{buildroot}%{opt_mu}/natives_blob.bin
chmod 755 %{buildroot}%{opt_mu}/natives_blob.bin
touch %{buildroot}%{opt_mu}/snapshot_blob.bin
chmod 755 %{buildroot}%{opt_mu}/snapshot_blob.bin
touch %{buildroot}%{opt_mu}/blink_image_resources_200_percent.pak
chmod 755 %{buildroot}%{opt_mu}/blink_image_resources_200_percent.pak
touch %{buildroot}%{opt_mu}/content_resources_200_percent.pak
chmod 755 %{buildroot}%{opt_mu}/content_resources_200_percent.pak
touch %{buildroot}%{opt_mu}/ui_resources_200_percent.pak
chmod 755 %{buildroot}%{opt_mu}/ui_resources_200_percent.pak
touch %{buildroot}%{opt_mu}/pdf_viewer_resources.pak
chmod 755 %{buildroot}%{opt_mu}/pdf_viewer_resources.pak
touch %{buildroot}%{opt_mu}/libffmpeg.so
chmod 755 %{buildroot}%{opt_mu}/libffmpeg.so
touch %{buildroot}%{opt_mu}/libnode.so
chmod 755 %{buildroot}%{opt_mu}/libnode.so
touch %{buildroot}%{opt_mu}/musixmatch
chmod 755 %{buildroot}%{opt_mu}/musixmatch

# run script
echo '#!/bin/bash
if [ `getconf LONG_BIT` = "64" ]; then
libdir=/usr/lib64
else
libdir=/usr/lib
fi

cd %{opt_mu}/
LD_LIBRARY_PATH=$libdir/:%{opt_mu}/ %{opt_mu}/musixmatch "$@" ' >> %{buildroot}/%{_bindir}/%{name}

chmod a+x %{buildroot}/%{_bindir}/%{name} 


%pre

# The installation
pushd /usr/src >/dev/null 2>&1
echo 'Downloading musixmatch, please wait...'
curl 'https://download-app.musixmatch.com/' -A 'Linux x86_64' -D headers.txt -OJf

pkgver() {
  # Extract the version from the filename.
  grep -oiP 'content-disposition: attachment; filename=.*musixmatch_\K([0-9.]+)(?=_amd64.deb.*)' headers.txt
}

if [ -f /usr/src/%{name}_%{version}_amd64.deb ] ; then
    #
    # Check the package
    #
if [ "$( md5sum %{name}_%{version}_amd64.deb | awk '{print $1}' )" != %{md5_musixmatch} ]; then
echo 'md5 sums mismatch'
rm -f %{name}_%{version}_amd64.deb
else
echo 'checksums OK'
fi
fi
#
if [ ! -f /usr/src/%{name}_%{version}_amd64.deb ]; then
    #
    # Get the package
    #
    echo 'Downloading musixmatch, please wait...'
    curl 'https://download-app.musixmatch.com/' -A 'Linux x86_64' -D headers.txt -OJf
    #
    # Check the package
    #
if [ "$( md5sum %{name}_%{version}_amd64.deb | awk '{print $1}' )" != %{md5_musixmatch} ]; then
echo 'md5 sums mismatch'
rm -f %{name}_%{version}_amd64.deb
else
echo 'checksums OK'
fi
fi
#

# extract data from the deb package
ar x %{name}_%{version}_amd64.deb 
if [ -f data.tar.xz ]; then
tar xJf data.tar.xz -C $PWD
elif [ -f data.tar.gz ]; then 
tar xmzvf data.tar.gz -C $PWD
fi

cp -rn $PWD/opt/Musixmatch /opt/
cp -rn $PWD/usr/share/icons/hicolor/* /usr/share/icons/hicolor/
cp -rf $PWD/usr/share/doc/musixmatch /usr/share/doc/

rm -f *.tar.gz
rm -f *.tar.xz
rm -rf $PWD/usr
rm -rf $PWD/opt
rm -f debian-binary
rm -rf $PWD/usr/share/icons/hicolor/*
rm -f %{name}_%{version}_amd64.deb

popd

%post
touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%postun
#
if [ "$1" == "0" ] ; then
#
[ -d %{opt_mu} ] && rm -rf %{opt_mu}
#
fi

touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :


%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%ghost %{_docdir}/musixmatch/changelog.gz
%ghost %dir %{opt_mu}/
%ghost %dir %{opt_mu}/locales/
%ghost %dir %{opt_mu}/resources/
%ghost /usr/share/icons/hicolor/*/apps/musixmatch.png
%ghost %{opt_mu}/LICENSE.electron.txt
%ghost %{opt_mu}/LICENSES.chromium.html
%ghost %{opt_mu}/views_resources_200_percent.pak
%ghost %{opt_mu}/content_shell.pak
%ghost %{opt_mu}/icudtl.dat
%ghost %{opt_mu}/natives_blob.bin
%ghost %{opt_mu}/snapshot_blob.bin
%ghost %{opt_mu}/blink_image_resources_200_percent.pak
%ghost %{opt_mu}/content_resources_200_percent.pak
%ghost %{opt_mu}/ui_resources_200_percent.pak
%ghost %{opt_mu}/pdf_viewer_resources.pak
%ghost %{opt_mu}/libffmpeg.so
%ghost %{opt_mu}/libnode.so
%ghost %{opt_mu}/musixmatch


%changelog

* Mon May 07 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 0.19.4-1
- Initial build
