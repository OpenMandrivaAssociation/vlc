%define _disable_ld_no_undefined 1
%global optflags %{optflags} -O3 -Wno-unknown-warning-option

%define snapshot 20231120
%define pre 0

%define gitcommit de025b60
%define revision %{version}-0-%{gitcommit}

%define libmajor 12
%define coremajor 9

%if "%{snapshot}" != "%{nil}"
%define fname %{name}-%{version}-%{snapshot}
%else
%if %{pre}
%define fname %{name}-%{version}-%{pre}
%else
%define fname %{name}-3.0-%{version}
%endif
%endif

%bcond_with plf
%bcond_without fribidi
%bcond_without xml
%bcond_without ncurses
%bcond_without lirc
%bcond_without qt5
%bcond_without svlc
%bcond_without udev
%bcond_without aa
%bcond_without sdl
%bcond_without sdl_image
%bcond_without xvideo
%bcond_without twolame
%bcond_without schroedinger
%bcond_without fluidsynth
%bcond_without gme
%bcond_without zvbi
%bcond_without kate
%bcond_with kde
%bcond_with goom
%bcond_without projectm
%bcond_without ass
%bcond_without lua
%bcond_without taglib
%bcond_without mtp
%bcond_without xcb_randr
%bcond_without mad
%bcond_without ogg
%bcond_without theora
%bcond_without speex
%bcond_without flac
%bcond_without mkv
%bcond_without a52
%bcond_without vcd
%bcond_without cddb
%bcond_without dv
%bcond_without dvdnav
%bcond_without dvbpsi
%bcond_with satellite
%bcond_without mpeg2dec
%bcond_without mpc
%bcond_without lame
%bcond_without live
%bcond_without libv4l
%bcond_without sysfs
%bcond_without shout
%bcond_without pulse
%bcond_without jack
%bcond_without alsa
%bcond_without bonjour
%bcond_without upnp
%bcond_without smb
%bcond_without tar
%bcond_without mod
%bcond_without gnutls
%bcond_without bluray

# is non-free stuf
%ifarch %{arm} %{armx}
%bcond_with crystalhd
%else
%bcond_without crystalhd
%endif

%define libname %mklibname %{name} %{libmajor}
%define libnamecore %mklibname vlccore %{coremajor}
%define devname %mklibname -d %{name}

%if %{with plf}
# make EVR of plf build higher than regular to allow update, needed with rpm5 mkrel
%define extrarelsuffix plf
%define distsuffix plf
%bcond_without faac
%bcond_without faad
%bcond_without dts
%bcond_without x264
%bcond_without x265
%else
%bcond_with faac
%bcond_with faad
%bcond_with dts
%bcond_with x264
%bcond_with x265
%endif

%define git_url git://git.videolan.org/vlc.git
%global _exclude_files_from_autoreq ^%{_libdir}/vlc/plugins

Summary:	MPEG, MPEG2, DVD and DivX player
Name:		vlc
Version:	4.0.0
Release:	%{?snapshot:0.%{snapshot}.}1
#gw the shared libraries are LGPL
License:	GPLv2+ and LGPLv2+
Group:		Video
URL:		http://www.videolan.org/
%if 0%{?snapshot:1}
Source0:	https://code.videolan.org/videolan/vlc/-/archive/master/vlc-master.tar.bz2#/vlc-%{snapshot}.tar.bz2
%else
Source0:	http://download.videolan.org/pub/videolan/%{name}/%{version}/%{name}-%{version}.tar.xz
%endif

Source100:	%{name}.rpmlintrc
Patch1:		vlc-2.0.1-automake-1.12.patch
Patch2:		vlc-3.0.0-libarchive-tar.patch
Patch3:		vlc-3.0.20-mpg123-buildfix.patch
#Patch3:		vlc-3.0-clang.patch
#Patch4:		vlc-3.0-lua-5.3.patch
Patch6:		vlc-3.0.9.2-compile.patch

#Patch20:	vlc-2.1.2-fix-default-font.patch
#Patch21:	https://git.alpinelinux.org/aports/plain/community/vlc/libplacebo-5.patch
#Patch22:	vlc-2.1.2-live555-201306.patch
#Patch23:	vlc-live555-20210101.patch

#Patch25:	vlc-3.0.16-dav1d-0.9.3.patch
#Patch26:	Remove_legacy_caca.patch

Obsoletes:	%{name}-plugin-opengl < %{EVRD}

BuildRequires:	git
BuildRequires:	desktop-file-utils
BuildRequires:	libtool
BuildRequires:	yasm
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	gettext-devel
BuildRequires:	libmpcdec-devel
BuildRequires:	pkgconfig(minizip)
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(vpx) >= 1.8.0
BuildRequires:	pkgconfig(libva)
BuildRequires:	pkgconfig(libsystemd)
BuildRequires:	pkgconfig(libidn)
BuildRequires:	pkgconfig(wayland-protocols)
BuildRequires:	pkgconfig(wayland-egl)
BuildRequires:	pkgconfig(caca)
BuildRequires:	pkgconfig(dvdread)
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libarchive) >= 3.1.0
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libavcodec)
BuildRequires:	pkgconfig(libcdio)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libproxy-1.0)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(libssh2)
BuildRequires:	pkgconfig(libchromaprint)
BuildRequires:	pkgconfig(opencv4)
BuildRequires:	pkgconfig(opus)
BuildRequires:	pkgconfig(portaudio-2.0)
BuildRequires:	pkgconfig(vdpau)
BuildRequires:	pkgconfig(libvncclient)
BuildRequires:	pkgconfig(xcb-util)
BuildRequires:	pkgconfig(xcb-keysyms)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(libmpg123)
BuildRequires:	pkgconfig(libsecret-1)
BuildRequires:	pkgconfig(libnfs)
BuildRequires:	pkgconfig(protobuf-lite)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libmatroska)
BuildRequires:	pkgconfig(libplacebo)
BuildRequires:	pkgconfig(soxr)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(gstreamer-app-1.0)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(dav1d)
BuildRequires:	pkgconfig(aom)
# Intel Media SDK is x86 only
%ifarch %{x86_64}
BuildRequires:	pkgconfig(mfx)
%endif
%if %{with sysfs}
BuildRequires:	sysfsutils-devel
%endif
%if %{with tar}
BuildRequires:	libtar-devel
%endif
%if %{with mod}
BuildRequires:	pkgconfig(libmodplug)
%endif
%if %{with gnutls}
BuildRequires:	pkgconfig(gnutls)
Requires:	%{name}-plugin-gnutls
%endif
%if %{with fribidi}
BuildRequires:	pkgconfig(fribidi)
%endif
%if %{with libv4l}
BuildRequires:	pkgconfig(libv4l2)
%endif
%if %{with udev}
BuildRequires:	pkgconfig(udev)
%endif
%if %{with qt5}
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5X11Extras)
BuildRequires:	qmake5
%endif
%if %{with taglib}
BuildRequires:	pkgconfig(taglib)
%endif
%if %{with mtp}
BuildRequires:	pkgconfig(libmtp)
%endif
%if %{with mad}
BuildRequires:	pkgconfig(id3tag)
BuildRequires:	pkgconfig(mad)
%endif
%if %{with ogg}
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(vorbis)
%rename	vlc-plugin-ogg
%endif
%if %{with xcb_randr}
BuildRequires:	pkgconfig(xcb)
%endif
%if %{with speex}
BuildRequires:	pkgconfig(speex) >= 1.1.16
BuildRequires:	pkgconfig(speexdsp)
%endif
%if %{with flac}
BuildRequires:	pkgconfig(flac)
Suggests:	vlc-plugin-flac
%endif
%if %{with mkv}
BuildRequires:	libmatroska-devel >= 1.0.0
%endif
%if %{with dvdnav}
BuildRequires:	pkgconfig(dvdnav)
%rename	vlc-plugin-dvdnav
%endif
%if %{with a52}
BuildRequires:	a52dec-devel
%rename	vlc-plugin-a52
%endif
%if %{with vcd}
BuildRequires:	pkgconfig(libvcdinfo)
%endif
%if %{with cddb}
BuildRequires:	pkgconfig(libcddb)
%else
BuildConflicts:	pkgconfig(libcddb)
%endif
%if %{with smb}
BuildRequires:	pkgconfig(smbclient)
%endif
%if %{with lame}
BuildRequires:	lame-devel
%endif
%if %{with mpeg2dec}
BuildRequires:	pkgconfig(libmpeg2)
%endif
%if %{with mpc}
BuildRequires:	libmpcdec-devel
%endif
%if %{with faad}
BuildRequires:	faad2-devel >= 2.0
%rename	vlc-plugin-faad
%endif
%if %{with faac}
BuildRequires:	faac-devel
%endif
%if %{with alsa}
BuildRequires:	pkgconfig(alsa)
%endif
%if %{with pulse}
BuildRequires:	pkgconfig(libpulse)
%endif
%if %{with jack}
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(samplerate)
%endif
%if %{with bonjour}
BuildRequires:	pkgconfig(avahi-client)
%endif
%if %{with dvbpsi}
BuildRequires:	pkgconfig(libdvbpsi) >= 1.2.0
%endif
%if %{with dts}
BuildRequires:	pkgconfig(libdts)
%endif
%if %{with x264}
BuildRequires:	pkgconfig(x264)
%endif
%if %{with x265}
BuildRequires:	pkgconfig(x265)
%endif
%if %{with xml}
BuildRequires:	pkgconfig(libxml-2.0)
%endif
%if %{with live}
BuildRequires:	live-devel > 2011.12.23
%endif
%if %{with xvideo}
BuildRequires:	pkgconfig(xv)
%endif
%if %{with bluray}
BuildRequires:	pkgconfig(libbluray) >= 0.2.1
%endif
%if %{with crystalhd}
BuildRequires: crystalhd-devel
%endif

%rename	gvlc
%rename	gnome-vlc
%rename	kvlc
%rename	vlc-plugin-alsa
%rename	vlc-plugin-dvb
%rename	vlc-plugin-mad
%rename	vlc-plugin-slp
%rename	wxvlc
# might be useful too:
Suggests:	vlc-plugin-theora
Requires:	fonts-ttf-vera
Requires(post,postun):	desktop-file-utils
Conflicts:	vlc-plugin-common < %{version}-%{release}
Suggests:	vdpau-drivers
Requires:	%{name}-core = %{EVRD}

%description
VideoLAN is an OpenSource streaming solution for every OS developed by
students from the Ecole Centrale Paris and developers from all over the
World.
VLC (VideoLAN Client) is a media player that can play MPEG1, MPEG2 and
MPEG4 (aka DivX) files, DVDs, VCDs, SVCDs, from a satellite card, from
a stream sent by VLS (VideoLAN Server), from another VLC, or from a Web
server.
This package contains no CSS unscrambling functionality for DVDs ;
you need the libdvdcss library available from
http://www.videolan.org/libdvdcss/

%if %{with plf}
This package is in restricted as it is violating software patents.
%endif

#general packages
%package -n %{libname}
Summary:	Shared code for the VLC media player
Group:		System/Libraries

%description -n %{libname}
Shared code for the VLC media player
This package contains code that is shared by different modules of the
VLC media player.

%package -n %{libnamecore}
Summary:	Shared core code for the VLC media player
Group:		System/Libraries
#gw needed by the python bindings:
Provides:	libvlccore = %{version}-%{release}

%description -n %{libnamecore}
Shared core code for the VLC media player
This package contains code that is shared by different modules of the
VLC media player.

%package -n %{devname}
Summary:	Development files for the VLC media player
Group:		Development/C
Requires:	%{libname} = %{version}
Requires:	%{libnamecore} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname -d %{name} 0

%description -n %{devname}
Development files for the VLC media player
This package contains headers and a static library required to build plugins
for the VLC media player, or standalone applications using features from VLC.

%if %{with zvbi}
%package plugin-zvbi
Summary:	Add Teletext and Closed Caption support to VLC
Group:		Video
Requires:	%{name}-core = %{version}
BuildRequires:	pkgconfig(zvbi-0.2)

%description plugin-zvbi
This package adds support for Raw VBI, Teletext and Closed Caption based on
the ZVBI library to VLC.
%endif

%if %{with kate}
%package plugin-kate
Summary:	Add subtitle and Karaoke text support to VLC
Group:		Video
Requires:	%{name}-core = %{version}
BuildRequires:	pkgconfig(tiger)

%description plugin-kate
This package adds support for subtitles and Karaoke text display based on
the libkate library to VLC.
%endif

%if %{with ass}
%package plugin-libass
Summary:	Add subtitle support to VLC using libass
Group:		Video
Requires:	%{name}-core = %{version}
BuildRequires:	pkgconfig(libass)

%description plugin-libass
This package adds support for subtitles based on the libass library to VLC.
%endif

%if %{with lua}
%package plugin-lua
Summary:	Add Lua scripting to vlc
Group:		Video
Requires:	%{name}-core = %{version}
BuildRequires:	pkgconfig(lua)

%description plugin-lua
This plugin adds lua scripting and provides a few example scripts as well.
%endif

%if %{with ncurses}
%package plugin-ncurses
Summary:	Ncurses console-based plugin for the VLC media player
Group:		Video
Requires:	%{name}-core = %{version}
BuildRequires:	pkgconfig(ncurses)

%description plugin-ncurses
This plugin adds a ncurses interface to the VLC media player. To
activate it, use the `--intf ncurses' flag.
%endif

%if %{with lirc}
%package plugin-lirc
Summary:	Lirc plugin for the VLC media player
Group:		Video
Requires:	%{name}-core = %{version}
%rename	vlc-lirc
BuildRequires:	pkgconfig(liblircclient0)

%description plugin-lirc
This plugin is an infrared lirc interface for the VLC media player. To
activate it, use the `--extraintf lirc' flag.
%endif

%package -n svlc
Summary:	Skinned GUI plugin for the VLC media player
Group:		Video
Requires:	%{name}-core = %{version}
Provides:	vlc-gui
Requires(post,postun): desktop-file-utils

%description -n svlc
This plugin adds a skinned GUI interface to the VLC media player. To
activate it, run the `svlc' program.

#
# video plugins
%if %{with aa}
%package plugin-aa
Summary:	ASCII art video plugin for the VLC media player
Group:		Video
Requires:	%{name}-core = %{version}
%rename	vlc-aa
BuildRequires:	aalib-devel

%description plugin-aa
This is an ASCII art video output plugin for the VLC media playe. To
activate it, use the `--vout aa' flag or select the `aa' video output
plugin from the preferences menu.
%endif

%if %{with sdl}
%package plugin-sdl
Summary:	Simple DirectMedia Layer video plugin for the VLC media player
Group:		Video
Requires:	%{name}-core = %{version}
%rename	vlc-sdl
%if %{with sdl_image}
BuildRequires:	pkgconfig(SDL_image)
%endif
BuildRequires:	pkgconfig(sdl)
BuildRequires:	nas-devel

%description plugin-sdl
This plugin adds support for the Simple DirectMedia Layer library to
the VLC media player. To activate it, use the `--vout sdl' or
`--aout sdl' flags or select the `sdl' video or audio output plugin
from the preferences menu.
%endif

%if %{with shout}
%package plugin-shout
Summary:	Shoutcast and Icecast connector
Group:		Sound
Requires:	%{name}-core = %{version}
BuildRequires:	pkgconfig(shout)

%description plugin-shout
This plugin adds support for Icecast and Shoutcast servers.
%endif

# visualization plugins

%if %{with goom}
%package plugin-goom
Summary:	Visualization plugin for the VLC media player
Group:		Video
BuildRequires:	libgoom2-devel
Requires:	%{name}-core = %{version}

%description plugin-goom
This is a visualization plugin for VLC media player based on the Goom library.

%post plugin-goom
%{_libdir}/vlc/vlc-cache-gen %{_libdir}/vlc/plugins
%endif

%if %{with projectm}
%package plugin-projectm
Summary:	Visualization plugin for the VLC media player
Group:		Video
BuildRequires:	pkgconfig(libprojectM)
Requires:	%{name}-core = %{version}

%description plugin-projectm
This is a visualization plugin for VLC media player based on projectm.
%endif

%if %{with theora}
%package plugin-theora
Summary:	Theora video codec for the VLC media player
Group:		Video
Requires:	%{name}-core = %{version}
BuildRequires:	pkgconfig(theora)

%description plugin-theora
These plugin adds support for the Ogg Theora video format to the VLC
media player. They are autodetected.
%endif

%if %{with twolame}
%package plugin-twolame
Summary:	MP2 encoder plugin for VLC
Group:		Sound
Requires:	%{name}-core = %{version}
BuildRequires:	pkgconfig(twolame)

%description plugin-twolame
These plugins add support for the Twolame MPEG Audio Layer 2 encoder
to the VLC media player. They are autodetected.
%endif

%if %{with fluidsynth}
%package plugin-fluidsynth
Summary:	Add MIDI playback support to VLC based on Fluidsynth
Group:		Sound
Requires:	%{name}-core = %{version}
BuildRequires:	pkgconfig(fluidsynth)

%description plugin-fluidsynth
This plugin adds support for MIDI playback to VLC based on the Fluidsynth
library.
%endif

%if %{with gme}
%package plugin-gme
Summary:	Add game music playback support to VLC based on libgme
Group:		Sound
Requires:	%{name}-core = %{version}
BuildRequires:	libgme-devel

%description plugin-gme
This plugin adds support for video game music playback to VLC based on the
GME library.
%endif

%package plugin-rist
Summary:	Rist plugin for the VLC media player
Group:		Video/Players
Requires:	%{name}-core = %{version}

%description plugin-rist
This plugin adds support for the RIST (Reliable Internet Stream Transport) input module to the VLC media player.

%if %{with schroedinger}
%package plugin-schroedinger
Summary:	Dirac plugin for VLC based on Schroedinger
Group:		Video
Requires:	%{name}-core = %{version}
BuildRequires:	pkgconfig(schroedinger-1.0)

%description plugin-schroedinger
These plugins add support for the Dirac video format based on Schroedinger.
to the VLC media player.
%endif

%package plugin-speex
Summary:	Ogg Speex codec plugin for the VLC media player
Group:		Sound
Requires:	%{name}-core = %{version}

%description plugin-speex
These plugins add support for the Ogg Speex codec to the VLC media
player. They are autodetected.

%package plugin-flac
Summary:	Flac codec plugin for the VLC media player
Group:		Video
Requires:	%{name}-core = %{version}

%description plugin-flac
These plugins add support for the FLAC compressed audio format to the
VLC media player.

%package plugin-opus
Summary:	Opus codec plugin for the VLC media player
Group:		Sound
Requires:	%{name}-core = %{version}

%description plugin-opus
These plugins add support for the Opus codec to the VLC media
player. They are autodetected.

%if %{with dv}
%package plugin-dv
Summary:	DV codec plugin for the VLC media player
Group:		Video
Requires:	%{name}-core = %{version}
BuildRequires:	pkgconfig(libavc1394)
BuildRequires:	pkgconfig(libdc1394-2)
BuildRequires:	pkgconfig(libdv)
BuildRequires:	pkgconfig(libraw1394)

%description plugin-dv
This plugin adds support for the DV video format to the VLC media player.
The plugin is autodetected.
%endif

%package plugin-mod
Summary:	MOD audio decoder plugin for the VLC media player
Group:		Sound
Requires:	%{name}-core = %{version}

%description plugin-mod
This plugin adds support for music module playback based on libmodplug
to the VLC media player.

%package plugin-mpc
Summary:	MPC audio decoder plugin for the VLC media player
Group:		Sound
Requires:	%{name}-core = %{version}

%description plugin-mpc
This plugin adds support for Musepack audio playback based on libmpcdec
to the VLC media player.

# audio plugins
%if %{with pulse}
%package plugin-pulse
Summary:	PulseAudio plugin for the VLC media player
Group:		Video
Requires:	%{name}-core = %{version}
%rename	vlc-pulse

%description plugin-pulse
This plugin adds support for the PulseAudio Sound Daemon to the VLC
media player. To activate it, use the `--aout pulse' flag or select the
`pulse' audio output plugin from the preferences menu.
%endif

%package plugin-jack
Summary:	Jack audio plugin for the VLC media player
Group:		Video
Requires:	%{name}-core = %{version}
%rename	vlc-jack

%description plugin-jack
This plugin adds support for the Jack Audio Connection Kit to the VLC
media player. To activate it, use the `--aout jack' flag or select the
`jack' audio output plugin from the preferences menu.

%package plugin-bonjour
Summary:	Bonjour service discovery plugin for the VLC media player
Group:		Video
Requires:	%{name}-core = %{version}

%description plugin-bonjour
This plugin adds support for Bonjour service discovery to
the VLC media player.

%package plugin-chromecast
Summary:	ChromeCast output plugin for VLC
Group:		Video
Requires:	%{name}-core = %{version}

%description plugin-chromecast
This plugin adds ChromeCast output support to
the VLC media player.

%if %{with upnp}
%package plugin-upnp
Summary:	UPNP service discovery plugin for the VLC media player
Group:		Video
Requires:	%{name}-core = %{version}
BuildRequires:	pkgconfig(libupnp)

%description plugin-upnp
This plugin adds support for UPNP service discovery to
the VLC media player.
%endif

%package plugin-gnutls
Summary:	Secure Socket Layer plugin for the VLC media player
Group:		Video
Requires:	%{name}-core = %{version}

%description plugin-gnutls
This plugin adds support for SSL/TLS to the VLC media player.

%package plugin-libnotify
Summary:	Notification popup plugin for the VLC media player
Group:		Video
Requires:	%{name}-core = %{version}

%description plugin-libnotify
This plugin adds support for notification popup messages to
the VLC media player.

%package core
Summary:	Core components of the VLC media player
Group:		Video
%if %{with pulse}
# needed when using pulseaudio
Requires:	vlc-plugin-opus
Requires:	vlc-plugin-pulse
%endif

%description core
Core components of the VLC media player

This includes core plugins used by libvlc, needed if you want
to use an application that uses VLC libraries (e.g. the Phonon
VLC plugin) even if you don't want to use the VLC player itself.

%prep
%autosetup -p1 -n %{name}-%{?snapshot:master}%{!?snapshot:%{version}}
# Make prebuilt stuff with old flex/bison great again...
cd modules/codec/webvtt
flex -o CSSLexer.c CSSLexer.l
bison --update CSSGrammar.y
bison -HCSSGrammar.h -oCSSGrammar.c CSSGrammar.y
cd ../../..

#gw if we want to regenerate libtool, we must remove the local versions of
# the libtool m4 files, aclocal will replace them
#cd m4
#rm -fv argz.m4 libtool.m4 ltdl.m4 ltoptions.m4 ltsugar.m4 ltversion.m4 lt~obsolete.m4
#cd ..

# Our Qt is patched with the bit below -- no point in erroring out
sed -i -e 's/.*ERROR.*I78ef29975181ee22429c9bd4b11d96d9e68b7a9c.*/AC_MSG_WARN([OMV Qt is good])/' configure.ac

%if "%{snapshot}" != ""
./bootstrap
%endif

#libtoolize --install --force --copy
#aclocal -I m4
#autoheader
#autoconf
#automake -acf

# (crazy) try with autoreconf only
# actually our libtool breaks huh?
autoreconf -vif
%build
# add missing ebml include dir
export CPPFLAGS="$CPPFLAGS -I/usr/include/ebml"
#gw the speex headers have moved
export CPPFLAGS="$CPPFLAGS -I%{_includedir}/speex"
# locate libsmbclient.h
export CPPFLAGS="$CPPFLAGS -I%{_includedir}/samba-4.0"

#echo "%revision" >> src/revision.txt
#echo "const char psz_vlc_changeset[] = \"%revision\";" >> src/revision.c

%configure \
%if %{without lua}
	--disable-lua \
%endif
	--disable-dependency-tracking \
%ifarch %{ix86}
	--disable-sse \
%endif
	--disable-sid \
%if %{with bonjour}
	--enable-bonjour \
%else
	--disable-bonjour \
%endif
%if %{with smb}
	--enable-smbclient \
%else
	--disable-smbclient \
%endif
%if %{with ncurses}
	--enable-ncurses \
%endif
%if %{with lirc}
	--enable-lirc \
%endif
	--enable-xvideo \
%if %{with aa}
	--enable-aa \
%endif
%if %{with sdl}
	--enable-sdl \
%endif
%if %{with mad}
	--enable-mad \
%endif
%if %{with ogg}
	--enable-vorbis \
	--enable-ogg \
%else
	--disable-vorbis \
	--disable-ogg \
%endif
%if %{with theora}
	--enable-theora \
%endif
%if %{with speex}
	--enable-speex \
%else
	--disable-speex \
%endif
%if %{with flac}
	--enable-flac \
%else
	--disable-flac \
%endif
%if %{with mkv}
	--enable-mkv \
%else
	--disable-mkv \
%endif
%if %{with dv}
	--enable-dv1394 \
%else
	--disable-dv1394 \
%endif
%if %{with dvbpsi}
	--enable-dvbpsi \
%else
	--disable-dvbpsi \
%endif
%if %{with shout}
	--enable-shout \
%endif
%if ! %{with pulse}
	--disable-pulse \
%endif
%if %{with jack}
	--enable-jack \
%endif
%if ! %{with alsa}
	--disable-alsa \
%endif
%if %{with mpeg2dec}
	--enable-libmpeg2 \
%else
	--disable-libmpeg2 \
%endif
%if %{with faad}
	--enable-faad \
%else
	--disable-faad \
%endif
%if %{with dts}
	--enable-dca \
%else
	--disable-dca \
%endif
%if ! %{with svlc}
	--disable-skins2 \
%endif
%if ! %{with dvdnav}
	--disable-dvdnav \
%endif
%if %{with live}
	--enable-live555 \
%endif
%if %{with gnutls}
	--enable-gnutls \
%endif
--disable-rpath \
%if %{with vcd}
	--enable-vcdx \
%endif
%if %{with cddb}
	--enable-libcddb \
%else
	--disable-libcddb \
%endif
%if %{with x264}
	--enable-x264 \
	--enable-x26410b \
%else
	--disable-x264 \
	--disable-x26410b \
%endif
%if %{with x265}
	--enable-x265 \
%else
	--disable-x265 \
%endif
%if %{with twolame}
	--enable-twolame \
%endif
%if %{with bluray}
	--enable-bluray \
%else
	--disable-bluray \
%endif
	--enable-realrtsp \
%if %{with kde}
	--with-kde-solid=%{_datadir}/apps/solid/actions \
%else
	--without-kde-solid \
%endif
%ifarch x86_64
	--with-pic
%endif

%make_build --output-sync=target

%install
mkdir -p %{buildroot}%{_libdir}
%make_install transform=""
find %{buildroot}%{_libdir}/vlc -name \*.la -exec %__rm -f {} \;
%find_lang %{name}
rm -rf installed-docs
mv %{buildroot}%{_datadir}/doc/vlc installed-docs
%if ! %{with svlc}
rm -rf %{buildroot}%{_datadir}/vlc/skin*
%endif
# menu

desktop-file-install --vendor="" \
--add-mime-type="x-content/video-dvd" \
--add-mime-type="x-content/video-vcd" \
--add-mime-type="x-content/video-svcd" \
--add-mime-type="x-content/audio-cdda" \
--add-category="Qt" \
--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%if %{with svlc}
%__cat > %{buildroot}%{_datadir}/applications/mandriva-svlc.desktop << EOF
[Desktop Entry]
Name=VLC skinned GUI media player
Comment=VLC is a free MPEG, MPEG2, DVD and DivX player
Exec=%{_bindir}/svlc %U
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=AudioVideo;Audio;Video;Player;
EOF
fgrep MimeType= %{buildroot}%{_datadir}/applications/vlc.desktop >> %{buildroot}%{_datadir}/applications/mandriva-svlc.desktop
%endif

# icons
%define pngdir share/icons
mkdir -p %{buildroot}/{%{_miconsdir},%{_liconsdir}}
install -m 644 %{pngdir}/16x16/vlc.png %{buildroot}/%{_miconsdir}/vlc.png
install -m 644 %{pngdir}/32x32/vlc.png %{buildroot}/%{_iconsdir}/vlc.png
install -m 644 %{pngdir}/48x48/vlc.png %{buildroot}/%{_liconsdir}/vlc.png

%files core
%dir %{_libdir}/vlc
%dir %{_libdir}/vlc/plugins
%ghost %{_libdir}/vlc/plugins/plugins.dat
%dir %{_libdir}/vlc/plugins/access
%{_libdir}/vlc/plugins/access/libfilesystem_plugin.so
%dir %{_libdir}/vlc/plugins/audio_output
%if %{with alsa}
%{_libdir}/vlc/plugins/audio_output/libalsa_plugin.so*
%endif
%dir %{_libdir}/vlc/plugins/codec
%{_libdir}/vlc/plugins/codec/libavcodec_plugin.so
%if %{with ogg}
%{_libdir}/vlc/plugins/demux/libogg_plugin.so*
%{_libdir}/vlc/plugins/codec/libvorbis_plugin.so*
%endif
%{_libdir}/vlc/plugins/codec/libvaapi_plugin.so
%dir %{_libexecdir}/vlc
%{_libexecdir}/vlc/vlc-cache-gen
%dir %{_libdir}/vlc/plugins/demux
%{_libdir}/vlc/plugins/demux/libavformat_plugin.so
%{_libdir}/vlc/plugins/demux/libdmxmus_plugin.so
%{_libdir}/vlc/plugins/demux/libhx_plugin.so
%{_libdir}/vlc/plugins/demux/libytdl_plugin.so
%dir %{_libdir}/vlc/plugins/video_chroma
%{_libdir}/vlc/plugins/video_chroma/libgrey_yuv_plugin.so
%{_libdir}/vlc/plugins/video_chroma/libi420_rgb_*plugin.so*
%{_libdir}/vlc/plugins/video_chroma/libi420_yuy2_*plugin.so*
%{_libdir}/vlc/plugins/video_chroma/libi422_i420_plugin.so
%{_libdir}/vlc/plugins/video_chroma/libi420_nv12_plugin.so
%{_libdir}/vlc/plugins/video_chroma/libi422_yuy2_*plugin.so*
%{_libdir}/vlc/plugins/video_chroma/librv32_plugin.so
%{_libdir}/vlc/plugins/video_chroma/libyuy2_i420_plugin.so
%{_libdir}/vlc/plugins/video_chroma/libyuy2_i422_plugin.so
%{_libdir}/vlc/plugins/video_chroma/libyuvp_plugin.so
%{_libdir}/vlc/plugins/video_chroma/libswscale_plugin.so
%{_libdir}/vlc/plugins/video_chroma/libchain_plugin.so
%dir %{_libdir}/vlc/plugins/video_output/
%{_libdir}/vlc/plugins/video_output/libxcb_x11_plugin.so*
%{_libdir}/vlc/plugins/video_output/libxcb_window_plugin.so*
%{_libdir}/vlc/libvlc_xcb_events.so*
%{_libdir}/vlc/plugins/video_output/libgl_plugin.so
%{_libdir}/vlc/plugins/video_output/libglx_plugin.so
%{_libdir}/vlc/plugins/video_output/libdrm_display_plugin.so
%{_libdir}/vlc/plugins/video_output/libegl_display_gbm_plugin.so
%{_libdir}/vlc/plugins/video_output/libegl_display_generic_plugin.so
%{_libdir}/vlc/plugins/video_output/libegl_pbuffer_filter_plugin.so
%{_libdir}/vlc/plugins/video_output/libegl_wl_plugin.so
%{_libdir}/vlc/plugins/video_output/libglfilter_draw_plugin.so
%{_libdir}/vlc/plugins/video_output/libglinterop_gst_mem_plugin.so
%{_libdir}/vlc/plugins/video_output/libglinterop_sw_plugin.so
%{_libdir}/vlc/plugins/video_output/libglinterop_vdpau_plugin.so
%{_libdir}/vlc/plugins/video_output/libkms_plugin.so
%{_libdir}/vlc/plugins/video_output/libplacebo_gl_plugin.so
%{_libdir}/vlc/plugins/video_output/libplacebo_plugin.so
%{_libdir}/vlc/plugins/video_output/libplacebo_vk_plugin.so
%{_libdir}/vlc/plugins/video_output/libvgl_plugin.so
%{_libdir}/vlc/plugins/video_output/libvideo_splitter_plugin.so
%{_libdir}/vlc/plugins/video_output/libvk_wl_plugin.so
%{_libdir}/vlc/plugins/video_output/libvk_x11_plugin.so
%{_libdir}/vlc/plugins/video_output/libwdummy_plugin.so
%{_libdir}/vlc/plugins/video_output/libwextern_plugin.so
%{_libdir}/vlc/plugins/video_output/libwl_shell_plugin.so
%{_libdir}/vlc/plugins/video_output/libwl_shm_plugin.so
%{_libdir}/vlc/plugins/video_output/libxcb_egl_plugin.so
%{_libdir}/vlc/plugins/video_output/libxcb_render_plugin.so
%{_libdir}/vlc/plugins/video_output/libxdg_shell_plugin.so

%files -f %{name}.lang
%doc NEWS COPYING AUTHORS THANKS
%doc installed-docs/* doc/lirc/
%{_bindir}/cvlc
%{_bindir}/rvlc
%{_bindir}/qvlc
%{_bindir}/vlc
%{_bindir}/vlc-wrapper
%dir %{_datadir}/vlc/
%{_datadir}/vlc/*.*
%{_datadir}/vlc/utils
%dir %{_libdir}/vlc
%{_libdir}/vlc/libvlc_vdpau.so.*

%{_libdir}/vlc/plugins/access/libaccess_concat_plugin.so
%{_libdir}/vlc/plugins/access/libavio_plugin.so
%{_libdir}/vlc/plugins/access/libimem_plugin.so
%{_libdir}/vlc/plugins/access/libaccess_imem_plugin.so
%{_libdir}/vlc/plugins/access/libhttps_plugin.so
%{_libdir}/vlc/plugins/access/libnfs_plugin.so
%{_libdir}/vlc/plugins/access/libsatip_plugin.so
%if %{with dvdnav}
%{_libdir}/vlc/plugins/access/libdvdnav_plugin.so
%endif
%if %{with mtp}
%{_libdir}/vlc/plugins/access/libaccess_mtp_plugin.so
%{_libdir}/vlc/plugins/services_discovery/libmtp_plugin.so
%endif
%{_libdir}/vlc/plugins/access/libshm_plugin.so
%{_libdir}/vlc/plugins/access/libsftp_plugin.so
%{_libdir}/vlc/plugins/access/libcdda_plugin.so*
%{_libdir}/vlc/plugins/access/libftp_plugin.so*
%{_libdir}/vlc/plugins/access/libhttp_plugin.so*
%{_libdir}/vlc/plugins/access/libaccess_mms_plugin.so*
%{_libdir}/vlc/plugins/access/libtcp_plugin.so*
%{_libdir}/vlc/plugins/access/libudp_plugin.so*
%{_libdir}/vlc/plugins/access/libvdr_plugin.so*
%{_libdir}/vlc/plugins/access/libdv1394_plugin.so*
%{_libdir}/vlc/plugins/access/libdtv_plugin.so*
%{_libdir}/vlc/plugins/access/libdvb_plugin.so*
%{_libdir}/vlc/plugins/access/libidummy_plugin.so
%if %{with live}
%{_libdir}/vlc/plugins/access/liblive555_plugin.so
%endif
%{_libdir}/vlc/plugins/access/libvnc_plugin.so
%{_libdir}/vlc/plugins/access/librtp_plugin.so
%dir %{_libdir}/vlc/plugins/access/rtp
%{_libdir}/vlc/plugins/access/rtp/*_plugin.so
%{_libdir}/vlc/plugins/codec/librtp_rawvid_plugin.so
%{_libdir}/vlc/plugins/access/libsdp_plugin.so
%{_libdir}/vlc/plugins/access/libtimecode_plugin.so
%{_libdir}/vlc/plugins/access/libv4l2_plugin.so*
%{_libdir}/vlc/plugins/access/libdvdread_plugin.so*
%{_libdir}/vlc/plugins/access/libvcd_plugin.so*
%{_libdir}/vlc/plugins/access/libxcb_screen_plugin.so
%if %{with bluray}
%{_libdir}/vlc/plugins/access/liblibbluray_plugin.so
%endif
%{_libdir}/vlc/plugins/access/libamt_plugin.so
%{_libdir}/vlc/plugins/access/libdata_plugin.so
%{_libdir}/vlc/plugins/access/libgopher_plugin.so
%{_libdir}/vlc/plugins/access/librdp_plugin.so
%{_libdir}/vlc/plugins/access/libsmbc_plugin.so
%{_libdir}/vlc/plugins/access/libwl_screenshooter_plugin.so
%{_libdir}/vlc/plugins/control/librc_plugin.so
%{_libdir}/vlc/plugins/logger/libjson_tracer_plugin.so
%{_libdir}/vlc/plugins/misc/libwl_idle_inhibit_plugin.so
%{_libdir}/vlc/plugins/nvdec/libglinterop_nvdec_plugin.so
%{_libdir}/vlc/plugins/nvdec/libnvdec_chroma_plugin.so
%{_libdir}/vlc/plugins/nvdec/libnvdec_plugin.so
%{_libdir}/vlc/plugins/packetizer/libpacketizer_mjpeg_plugin.so
%{_libdir}/vlc/plugins/services_discovery/libudisks_plugin.so
%{_libdir}/vlc/plugins/video_chroma/libgst_mem_plugin.so
%{_libdir}/vlc/plugins/video_chroma/liborient_plugin.so
%{_libdir}/vlc/plugins/video_filter/libformatcrop_plugin.so
%{_libdir}/vlc/plugins/video_filter/libglblend_plugin.so
%{_libdir}/vlc/plugins/video_filter/libopengl_filter_plugin.so
%{_libdir}/vlc/plugins/video_filter/libpl_scale_plugin.so
%{_datadir}/applications/vlc-openbd.desktop
%{_datadir}/applications/vlc-opencda.desktop
%{_datadir}/applications/vlc-opendvd.desktop
%{_datadir}/applications/vlc-openvcd.desktop
%dir %{_libdir}/vlc/plugins/access_output/
%{_libdir}/vlc/plugins/access_output/libaccess_http_put_plugin.so
%{_libdir}/vlc/plugins/access_output/libaccess_output_dummy_plugin.so*
%{_libdir}/vlc/plugins/access_output/libaccess_output_file_plugin.so*
%{_libdir}/vlc/plugins/access_output/libaccess_output_http_plugin.so*
%{_libdir}/vlc/plugins/access_output/libaccess_output_livehttp_plugin.so*

%dir %{_libdir}/vlc/plugins/audio_filter
%{_libdir}/vlc/plugins/audio_filter/libscaletempo_pitch_plugin.so
%{_libdir}/vlc/plugins/audio_filter/libaudiobargraph_a_plugin.so
%{_libdir}/vlc/plugins/audio_filter/libaudio_format_plugin.so*
%{_libdir}/vlc/plugins/audio_filter/libchorus_flanger_plugin.so
%{_libdir}/vlc/plugins/audio_filter/libcompressor_plugin.so
%if %{with dts}
%{_libdir}/vlc/plugins/audio_filter/libdtstofloat32_plugin.so*
%endif
%{_libdir}/vlc/plugins/audio_filter/libdolby_surround_decoder_plugin.so*
%{_libdir}/vlc/plugins/audio_filter/libequalizer_plugin.so*
%{_libdir}/vlc/plugins/audio_filter/libheadphone_channel_mixer_plugin.so*
%{_libdir}/vlc/plugins/audio_filter/libkaraoke_plugin.so
%{_libdir}/vlc/plugins/audio_filter/libmono_plugin.so
%if %{with mad}
%{_libdir}/vlc/plugins/audio_filter/libmad_plugin.so
%endif
%{_libdir}/vlc/plugins/audio_filter/libsoxr_plugin.so
%{_libdir}/vlc/plugins/audio_filter/libtospdif_plugin.so
%{_libdir}/vlc/plugins/audio_filter/libnormvol_plugin.so*
%{_libdir}/vlc/plugins/audio_filter/libparam_eq_plugin.so*
%{_libdir}/vlc/plugins/audio_filter/libsamplerate_plugin.so
%{_libdir}/vlc/plugins/audio_filter/libscaletempo_plugin.so
%{_libdir}/vlc/plugins/audio_filter/libsimple_channel_mixer_plugin.so*
%{_libdir}/vlc/plugins/audio_filter/libspatializer_plugin.so
%{_libdir}/vlc/plugins/audio_filter/libtrivial_channel_mixer_plugin.so*
%{_libdir}/vlc/plugins/audio_filter/libugly_resampler_plugin.so*
%{_libdir}/vlc/plugins/audio_filter/libgain_plugin.so
%{_libdir}/vlc/plugins/audio_filter/libremap_plugin.so
%{_libdir}/vlc/plugins/audio_filter/libstereo_widen_plugin.so
%{_libdir}/vlc/plugins/audio_filter/libcenter_plugin.so
%{_libdir}/vlc/plugins/audio_filter/libebur128_plugin.so
%{_libdir}/vlc/plugins/audio_filter/librnnoise_plugin.so
%{_libdir}/vlc/plugins/audio_filter/libstereopan_plugin.so

%dir %{_libdir}/vlc/plugins/audio_mixer
%{_libdir}/vlc/plugins/audio_mixer/libfloat_mixer_plugin.so
%{_libdir}/vlc/plugins/audio_mixer/libinteger_mixer_plugin.so

%{_libdir}/vlc/plugins/audio_output/libadummy_plugin.so
%{_libdir}/vlc/plugins/audio_output/libamem_plugin.so
%{_libdir}/vlc/plugins/audio_output/libafile_plugin.so
%{_libdir}/vlc/plugins/audio_output/libsndio_plugin.so

%dir %{_libdir}/vlc/plugins/codec
%if %{with a52}
%{_libdir}/vlc/plugins/codec/liba52_plugin.so*
%endif
%{_libdir}/vlc/plugins/codec/libadpcm_plugin.so*
%{_libdir}/vlc/plugins/codec/libaes3_plugin.so
%{_libdir}/vlc/plugins/codec/libaraw_plugin.so*
%{_libdir}/vlc/plugins/codec/libcc_plugin.so
%{_libdir}/vlc/plugins/codec/libcdg_plugin.so
%{_libdir}/vlc/plugins/codec/libmpg123_plugin.so
%{_libdir}/vlc/plugins/codec/libaom_plugin.so
%{_libdir}/vlc/plugins/codec/libdav1d_plugin.so
%{_libdir}/vlc/plugins/codec/liboggspots_plugin.so
%{_libdir}/vlc/plugins/codec/librtpvideo_plugin.so
%{_libdir}/vlc/plugins/codec/libscte18_plugin.so
%{_libdir}/vlc/plugins/codec/libspdif_plugin.so
%{_libdir}/vlc/plugins/codec/libtextst_plugin.so
%{_libdir}/vlc/plugins/codec/libttml_plugin.so
%{_libdir}/vlc/plugins/codec/libcvdsub_plugin.so*
%{_libdir}/vlc/plugins/codec/libddummy_plugin.so
%{_libdir}/vlc/plugins/codec/libedummy_plugin.so
%{_libdir}/vlc/plugins/codec/librawvideo_plugin.so*
%{_libdir}/vlc/plugins/codec/libsubsusf_plugin.so
%{_libdir}/vlc/plugins/codec/libstl_plugin.so
%{_libdir}/vlc/plugins/codec/libsvcdsub_plugin.so*
%{_libdir}/vlc/plugins/codec/libt140_plugin.so
%{_libdir}/vlc/plugins/codec/liblpcm_plugin.so*
%{_libdir}/vlc/plugins/codec/liblibmpeg2_plugin.so*
%{_libdir}/vlc/plugins/codec/libpng_plugin.so*
%{_libdir}/vlc/plugins/codec/libwebvtt_plugin.so
%{_libdir}/vlc/plugins/codec/libsubsdec_plugin.so*
%if %{with x264}
%{_libdir}/vlc/plugins/codec/libx264_plugin.so*
%endif
%if %{with x265}
%{_libdir}/vlc/plugins/codec/libx265_plugin.so*
%endif
%ifarch %{x86_64}
# Intel Media SDK -- x86 only
%{_libdir}/vlc/plugins/codec/libqsv_plugin.so
%endif
%{_libdir}/vlc/plugins/codec/libspudec_plugin.so*
%{_libdir}/vlc/plugins/codec/libdvbsub_plugin.so*
%if %{with faad}
%{_libdir}/vlc/plugins/codec/libfaad_plugin.so*
%endif
%{_libdir}/vlc/plugins/codec/libtelx_plugin.so
%{_libdir}/vlc/plugins/codec/libg711_plugin.so
%{_libdir}/vlc/plugins/codec/libscte27_plugin.so
%{_libdir}/vlc/plugins/codec/libuleaddvaudio_plugin.so
%{_libdir}/vlc/plugins/codec/libxwd_plugin.so
%{_libdir}/vlc/plugins/codec/libgstdecode_plugin.so
%{_libdir}/vlc/plugins/codec/libjpeg_plugin.so
%{_libdir}/vlc/plugins/codec/libsubstx3g_plugin.so
%{_libdir}/vlc/plugins/codec/libsvgdec_plugin.so
#{_libdir}/vlc/plugins/codec/libvaapi_drm_plugin.so
%{_libdir}/vlc/plugins/codec/libvpx_plugin.so
%{_libdir}/vlc/plugins/codec/librav1e_plugin.so

%dir %{_libdir}/vlc/plugins/control
%{_libdir}/vlc/plugins/control/libdbus_plugin.so
%{_libdir}/vlc/plugins/control/libdummy_plugin.so
%{_libdir}/vlc/plugins/control/libhotkeys_plugin.so*
%{_libdir}/vlc/plugins/control/libgestures_plugin.so*
%{_libdir}/vlc/plugins/control/libxcb_hotkeys_plugin.so

%dir %{_libdir}/vlc/plugins/demux
%{_libdir}/vlc/plugins/demux/libadaptive_plugin.so
%{_libdir}/vlc/plugins/demux/libdirectory_demux_plugin.so
%{_libdir}/vlc/plugins/demux/libh26x_plugin.so
%{_libdir}/vlc/plugins/demux/libnoseek_plugin.so
%{_libdir}/vlc/plugins/demux/libaiff_plugin.so*
%{_libdir}/vlc/plugins/demux/libasf_plugin.so*
%{_libdir}/vlc/plugins/demux/libau_plugin.so*
%{_libdir}/vlc/plugins/demux/libavi_plugin.so*
%{_libdir}/vlc/plugins/demux/libdemux_cdg_plugin.so
%{_libdir}/vlc/plugins/demux/libdemux_stl_plugin.so
%{_libdir}/vlc/plugins/demux/libdemuxdump_plugin.so*
%{_libdir}/vlc/plugins/demux/libes_plugin.so
%{_libdir}/vlc/plugins/demux/libimage_plugin.so
%{_libdir}/vlc/plugins/demux/libmjpeg_plugin.so*
%{_libdir}/vlc/plugins/demux/libmp4_plugin.so*
%{_libdir}/vlc/plugins/demux/libmpgv_plugin.so*
%{_libdir}/vlc/plugins/demux/libnsv_plugin.so*
%{_libdir}/vlc/plugins/demux/libnuv_plugin.so*
%{_libdir}/vlc/plugins/demux/libplaylist_plugin.so*
%{_libdir}/vlc/plugins/demux/libps_plugin.so*
%{_libdir}/vlc/plugins/demux/libpva_plugin.so*
%{_libdir}/vlc/plugins/demux/librawaud_plugin.so
%{_libdir}/vlc/plugins/demux/librawdv_plugin.so*
%{_libdir}/vlc/plugins/demux/librawvid_plugin.so
%{_libdir}/vlc/plugins/demux/libsmf_plugin.so
%{_libdir}/vlc/plugins/demux/libsubtitle_plugin.so*
%{_libdir}/vlc/plugins/demux/libtta_plugin.so
%{_libdir}/vlc/plugins/demux/libty_plugin.so*
%{_libdir}/vlc/plugins/demux/libvobsub_plugin.so*
%{_libdir}/vlc/plugins/demux/libvc1_plugin.so
%{_libdir}/vlc/plugins/demux/libvoc_plugin.so*
%{_libdir}/vlc/plugins/demux/libwav_plugin.so*
%{_libdir}/vlc/plugins/demux/libmkv_plugin.so
%if %{with dvbpsi}
%{_libdir}/vlc/plugins/demux/libts_plugin.so*
%endif
%{_libdir}/vlc/plugins/demux/libxa_plugin.so*
%{_libdir}/vlc/plugins/demux/libcaf_plugin.so
%if %{with satellite}
%{_libdir}/vlc/plugins/access/libsatellite_plugin.so*
%endif

%dir %{_libdir}/vlc/plugins/keystore
%{_libdir}/vlc/plugins/keystore/libfile_keystore_plugin.so
%{_libdir}/vlc/plugins/keystore/libsecret_plugin.so
%{_libdir}/vlc/plugins/keystore/libkwallet_plugin.so
%{_libdir}/vlc/plugins/keystore/libmemory_keystore_plugin.so

%dir %{_libdir}/vlc/plugins/logger
%{_libdir}/vlc/plugins/logger/libconsole_logger_plugin.so
%{_libdir}/vlc/plugins/logger/libfile_logger_plugin.so
%{_libdir}/vlc/plugins/logger/libsd_journal_plugin.so
%{_libdir}/vlc/plugins/logger/libsyslog_plugin.so

%dir %{_libdir}/vlc/plugins/meta_engine
%{_libdir}/vlc/plugins/meta_engine/libfolder_plugin.so
%if %{with taglib}
%{_libdir}/vlc/plugins/meta_engine/libtaglib_plugin.so
%endif
%dir %{_libdir}/vlc/plugins/misc
%{_libdir}/vlc/plugins/misc/libaudioscrobbler_plugin.so
%{_libdir}/vlc/plugins/misc/libexport_plugin.so*
%{_libdir}/vlc/plugins/misc/libstats_plugin.so
%{_libdir}/vlc/plugins/misc/libxdg_screensaver_plugin.so*
%{_libdir}/vlc/plugins/misc/libfingerprinter_plugin.so
%if %{with xml}
%{_libdir}/vlc/plugins/misc/libxml_plugin.so*
%endif
%{_libdir}/vlc/plugins/misc/libdbus_screensaver_plugin.so
%{_libdir}/vlc/plugins/misc/libaddonsfsstorage_plugin.so
%{_libdir}/vlc/plugins/misc/libaddonsvorepository_plugin.so

%dir %{_libdir}/vlc/plugins/mux
%{_libdir}/vlc/plugins/mux/libmux_asf_plugin.so*
%{_libdir}/vlc/plugins/mux/libmux_avi_plugin.so*
%{_libdir}/vlc/plugins/mux/libmux_dummy_plugin.so*
%{_libdir}/vlc/plugins/mux/libmux_mp4_plugin.so*
%{_libdir}/vlc/plugins/mux/libmux_mpjpeg_plugin.so*
%if %{with ogg}
%{_libdir}/vlc/plugins/mux/libmux_ogg_plugin.so*
%endif
%{_libdir}/vlc/plugins/mux/libmux_ps_plugin.so*
%{_libdir}/vlc/plugins/mux/libmux_ts_plugin.so
%{_libdir}/vlc/plugins/mux/libmux_wav_plugin.so*
%dir %{_libdir}/vlc/plugins/gui/
%if %{with qt5}
%{_libdir}/vlc/plugins/gui/libqt_plugin.so
%{_libdir}/vlc/plugins/gui/libqt_gtktheme_plugin.so
%{_libexecdir}/vlc/vlc-qt-check
%endif
%dir %{_libdir}/vlc/plugins/packetizer
%{_libdir}/vlc/plugins/packetizer/libpacketizer_a52_plugin.so
%{_libdir}/vlc/plugins/packetizer/libpacketizer_av1_plugin.so
%{_libdir}/vlc/plugins/packetizer/libpacketizer_dts_plugin.so
%{_libdir}/vlc/plugins/packetizer/libpacketizer_mpegaudio_plugin.so
%{_libdir}/vlc/plugins/packetizer/libpacketizer_copy_plugin.so*
%{_libdir}/vlc/plugins/packetizer/libpacketizer_flac_plugin.so
%{_libdir}/vlc/plugins/packetizer/libpacketizer_h264_plugin.so*
%{_libdir}/vlc/plugins/packetizer/libpacketizer_mlp_plugin.so
%{_libdir}/vlc/plugins/packetizer/libpacketizer_mpeg4audio_plugin.so*
%{_libdir}/vlc/plugins/packetizer/libpacketizer_mpeg4video_plugin.so*
%{_libdir}/vlc/plugins/packetizer/libpacketizer_mpegvideo_plugin.so*
%{_libdir}/vlc/plugins/packetizer/libpacketizer_vc1_plugin.so
%{_libdir}/vlc/plugins/packetizer/libpacketizer_avparser_plugin.so
%{_libdir}/vlc/plugins/packetizer/libpacketizer_hevc_plugin.so

%dir %{_libdir}/vlc/plugins/vaapi
%{_libdir}/vlc/plugins/vaapi/libdecdev_vaapi_drm_plugin.so
%{_libdir}/vlc/plugins/vaapi/libdecdev_vaapi_wl_plugin.so
%{_libdir}/vlc/plugins/vaapi/libdecdev_vaapi_x11_plugin.so
%{_libdir}/vlc/plugins/video_output/libglinterop_vaapi_plugin.so
%{_libdir}/vlc/plugins/vaapi/libvaapi_filters_plugin.so

%{_libdir}/vlc/plugins/vdpau
%{_libdir}/vlc/plugins/video_splitter

%dir %{_libdir}/vlc/plugins/services_discovery/
%{_libdir}/vlc/plugins/services_discovery/libpodcast_plugin.so*
%{_libdir}/vlc/plugins/services_discovery/libsap_plugin.so*
%if %{with udev}
%{_libdir}/vlc/plugins/services_discovery/libudev_plugin.so*
%endif
%{_libdir}/vlc/plugins/services_discovery/libxcb_apps_plugin.so

%dir %{_libdir}/vlc/plugins/spu
%{_libdir}/vlc/plugins/spu/libaudiobargraph_v_plugin.so
%{_libdir}/vlc/plugins/spu/libdynamicoverlay_plugin.so
%{_libdir}/vlc/plugins/spu/liblogo_plugin.so
%{_libdir}/vlc/plugins/spu/libmarq_plugin.so
%{_libdir}/vlc/plugins/spu/libmosaic_plugin.so
%{_libdir}/vlc/plugins/spu/librss_plugin.so
%{_libdir}/vlc/plugins/spu/libsubsdelay_plugin.so

%dir %{_libdir}/vlc/plugins/stream_filter/
%{_libdir}/vlc/plugins/stream_filter/libadf_plugin.so
%{_libdir}/vlc/plugins/stream_filter/libcache_block_plugin.so
%{_libdir}/vlc/plugins/stream_filter/libcache_read_plugin.so
%{_libdir}/vlc/plugins/stream_filter/libhds_plugin.so
%{_libdir}/vlc/plugins/stream_filter/libinflate_plugin.so
%{_libdir}/vlc/plugins/stream_filter/libprefetch_plugin.so
%{_libdir}/vlc/plugins/stream_filter/libskiptags_plugin.so
%{_libdir}/vlc/plugins/stream_filter/libdecomp_plugin.so
%{_libdir}/vlc/plugins/stream_filter/librecord_plugin.so

%dir %{_libdir}/vlc/plugins/stream_extractor
%{_libdir}/vlc/plugins/stream_extractor/libarchive_plugin.so

%dir %{_libdir}/vlc/plugins/stream_out
%{_libdir}/vlc/plugins/stream_out/libstream_out_cycle_plugin.so
%{_libdir}/vlc/plugins/stream_out/libstream_out_autodel_plugin.so
%{_libdir}/vlc/plugins/stream_out/libstream_out_bridge_plugin.so*
%{_libdir}/vlc/plugins/stream_out/libstream_out_delay_plugin.so
%{_libdir}/vlc/plugins/stream_out/libstream_out_display_plugin.so*
%{_libdir}/vlc/plugins/stream_out/libstream_out_dummy_plugin.so*
%{_libdir}/vlc/plugins/stream_out/libstream_out_duplicate_plugin.so*
%{_libdir}/vlc/plugins/stream_out/libstream_out_es_plugin.so*
%{_libdir}/vlc/plugins/stream_out/libstream_out_gather_plugin.so*
%{_libdir}/vlc/plugins/stream_out/libstream_out_mosaic_bridge_plugin.so*
%{_libdir}/vlc/plugins/stream_out/libstream_out_record_plugin.so
%{_libdir}/vlc/plugins/stream_out/libstream_out_rtp_plugin.so*
%{_libdir}/vlc/plugins/stream_out/libstream_out_stats_plugin.so
%{_libdir}/vlc/plugins/stream_out/libstream_out_setid_plugin.so
%{_libdir}/vlc/plugins/stream_out/libstream_out_smem_plugin.so*
%{_libdir}/vlc/plugins/stream_out/libstream_out_standard_plugin.so*
%{_libdir}/vlc/plugins/stream_out/libstream_out_transcode_plugin.so*
%{_libdir}/vlc/plugins/stream_out/libstream_out_chromaprint_plugin.so
%{_libdir}/vlc/plugins/stream_out/libstream_out_hls_plugin.so
%{_libdir}/vlc/plugins/stream_out/libstream_out_trace_plugin.so
%{_libdir}/vlc/plugins/stream_out/libstream_out_udp_plugin.so
%dir %{_libdir}/vlc/plugins/text_renderer
%{_libdir}/vlc/plugins/text_renderer/libfreetype_plugin.so*
%{_libdir}/vlc/plugins/text_renderer/libsvg_plugin.so
%{_libdir}/vlc/plugins/text_renderer/libtdummy_plugin.so

%dir %{_libdir}/vlc/plugins/video_filter
%{_libdir}/vlc/plugins/video_filter/libadjust_plugin.so*
%{_libdir}/vlc/plugins/video_filter/libalphamask_plugin.so
%{_libdir}/vlc/plugins/video_filter/libantiflicker_plugin.so
%{_libdir}/vlc/plugins/video_filter/libball_plugin.so
%{_libdir}/vlc/plugins/video_filter/libblendbench_plugin.so
%{_libdir}/vlc/plugins/video_filter/libblend_plugin.so*
%{_libdir}/vlc/plugins/video_filter/libbluescreen_plugin.so
%{_libdir}/vlc/plugins/video_filter/libcanvas_plugin.so
%{_libdir}/vlc/plugins/video_filter/libcolorthres_plugin.so
%{_libdir}/vlc/plugins/video_filter/libcroppadd_plugin.so
%{_libdir}/vlc/plugins/video_filter/libdeinterlace_plugin.so*
%{_libdir}/vlc/plugins/video_filter/libedgedetection_plugin.so
%{_libdir}/vlc/plugins/video_filter/liberase_plugin.so
%{_libdir}/vlc/plugins/video_filter/libextract_plugin.so
%{_libdir}/vlc/plugins/video_filter/libfps_plugin.so
%{_libdir}/vlc/plugins/video_filter/libgaussianblur_plugin.so
%{_libdir}/vlc/plugins/video_filter/libgradient_plugin.so
%{_libdir}/vlc/plugins/video_filter/libgradfun_plugin.so
%{_libdir}/vlc/plugins/video_filter/libgrain_plugin.so
%{_libdir}/vlc/plugins/video_filter/libhqdn3d_plugin.so
%{_libdir}/vlc/plugins/video_filter/libinvert_plugin.so*
%{_libdir}/vlc/plugins/video_filter/libmagnify_plugin.so*
%{_libdir}/vlc/plugins/video_filter/libmirror_plugin.so
%{_libdir}/vlc/plugins/video_filter/libmotionblur_plugin.so*
%{_libdir}/vlc/plugins/video_filter/libmotiondetect_plugin.so*
%{_libdir}/vlc/plugins/video_filter/libposterize_plugin.so
%{_libdir}/vlc/plugins/video_filter/libpostproc_plugin.so
%{_libdir}/vlc/plugins/video_filter/libpsychedelic_plugin.so
%{_libdir}/vlc/plugins/video_filter/libpuzzle_plugin.so
%{_libdir}/vlc/plugins/video_filter/libripple_plugin.so
%{_libdir}/vlc/plugins/video_filter/librotate_plugin.so
%{_libdir}/vlc/plugins/video_filter/libscale_plugin.so*
%{_libdir}/vlc/plugins/video_filter/libscene_plugin.so
%{_libdir}/vlc/plugins/video_filter/libsepia_plugin.so
%{_libdir}/vlc/plugins/video_filter/libsharpen_plugin.so
%{_libdir}/vlc/plugins/video_filter/libtransform_plugin.so*
%{_libdir}/vlc/plugins/video_filter/libwave_plugin.so
%{_libdir}/vlc/plugins/video_filter/libanaglyph_plugin.so
#{_libdir}/vlc/plugins/video_filter/libopencv_example_plugin.so
#{_libdir}/vlc/plugins/video_filter/libopencv_wrapper_plugin.so
%{_libdir}/vlc/plugins/video_filter/libfreeze_plugin.so
%{_libdir}/vlc/plugins/video_filter/liboldmovie_plugin.so
%{_libdir}/vlc/plugins/video_filter/libvhs_plugin.so

%{_libdir}/vlc/plugins/video_output/libcaca_plugin.so
%{_libdir}/vlc/plugins/video_output/libegl_x11_plugin.so*
#{_libdir}/vlc/plugins/video_output/libegl_wl_plugin.so*
%{_libdir}/vlc/plugins/video_output/libflaschen_plugin.so*
%{_libdir}/vlc/plugins/video_output/libvmem_plugin.so
%{_libdir}/vlc/plugins/video_output/libyuv_plugin.so
%{_libdir}/vlc/plugins/video_output/libvdummy_plugin.so
#{_libdir}/vlc/plugins/video_output/libwl_shell_plugin.so
#{_libdir}/vlc/plugins/video_output/libwl_shm_plugin.so
#{_libdir}/vlc/plugins/video_output/libxdg_shell_plugin.so

%dir %{_libdir}/vlc/plugins/visualization
%{_libdir}/vlc/plugins/visualization/libvisual_plugin.so*
%{_libdir}/vlc/plugins/visualization/libglspectrum_plugin.so*
%if %{with alsa}
%{_libdir}/vlc/plugins/access/libaccess_alsa_plugin.so
%endif
%{_mandir}/man1/vlc.*
%{_mandir}/man1/vlc-wrapper.1*
%{_datadir}/applications/vlc.desktop
%{_miconsdir}/vlc.png
%{_iconsdir}/vlc.png
%{_liconsdir}/vlc.png
%{_iconsdir}/hicolor/*/apps/*
%if %{with kde}
%{_datadir}/apps/solid/actions/*.desktop
%endif

%{_datadir}/metainfo/vlc.appdata.xml

%files -n %{libname}
%{_libdir}/libvlc.so.%{libmajor}*

%files -n %{libnamecore}
%{_libdir}/libvlccore.so.%{coremajor}*

%files -n %{devname}
%doc doc/release-howto.txt doc/skins
%dir %{_includedir}/vlc
%{_libdir}/libvlc.so
%{_libdir}/libvlccore.so
%{_libdir}/vlc/libvlc_vdpau.so
%{_libdir}/vlc/libcompat.a
%{_includedir}/vlc/*
%if %{mdvver} <= 201100
%attr(644,root,root) %{_libdir}/*.la
%endif
%{_libdir}/pkgconfig/*

%if %{with shout}
%files plugin-shout
%{_libdir}/vlc/plugins/access_output/libaccess_output_shout_plugin.so
%endif

# intf plugins
%if %{with svlc}
%files -n svlc
%{_bindir}/svlc
%{_libdir}/vlc/plugins/gui/libskins2_plugin.so*
%{_datadir}/applications/mandriva-svlc.desktop
%{_datadir}/vlc/skins2
%endif

%if %{with zvbi}
%files plugin-zvbi
%{_libdir}/vlc/plugins/access/liblinsys_hdsdi_plugin.so
%{_libdir}/vlc/plugins/access/liblinsys_sdi_plugin.so
%{_libdir}/vlc/plugins/codec/libzvbi_plugin.so
%endif

%if %{with kate}
%files plugin-kate
%{_libdir}/vlc/plugins/codec/libkate_plugin.so
%endif

%if %{with ass}
%files plugin-libass
%{_libdir}/vlc/plugins/codec/liblibass_plugin.so
%endif

%if %{with lua}
%files plugin-lua
%{_libexecdir}/vlc/lua
%{_libdir}/vlc/plugins/lua/liblua_plugin.so
%{_datadir}/vlc/lua
%{_bindir}/rvlc
%endif

%if %{with ncurses}
%files plugin-ncurses
%{_bindir}/nvlc
%{_libdir}/vlc/plugins/gui/libncurses_plugin.so*
%endif

%if %{with lirc}
%files plugin-lirc
%{_libdir}/vlc/plugins/control/liblirc_plugin.so*
%endif

# video plugins
%if %{with sdl}
%files plugin-sdl
%if %{with sdl_image}
%endif
%endif

%if %{with aa}
%files plugin-aa
%endif

%if %{with goom}
%files plugin-goom
%{_libdir}/vlc/plugins/visualization/libgoom_plugin.so
%endif

%if %{with projectm}
%files plugin-projectm
%{_libdir}/vlc/plugins/visualization/libprojectm_plugin.so
%endif

%if %{with theora}
%files plugin-theora
%{_libdir}/vlc/plugins/codec/libtheora_plugin.so
%endif

%if %{with fluidsynth}
%files plugin-fluidsynth
%{_libdir}/vlc/plugins/codec/libfluidsynth_plugin.so
%endif

%if %{with gme}
%files plugin-gme
%{_libdir}/vlc/plugins/demux/libgme_plugin.so
%endif

%files plugin-rist

%if %{with schroedinger}
%files plugin-schroedinger
%{_libdir}/vlc/plugins/codec/libschroedinger_plugin.so
%endif

%if %{with twolame}
%files plugin-twolame
%{_libdir}/vlc/plugins/codec/libtwolame_plugin.so*
%endif

%if %{with speex}
%files plugin-speex
%{_libdir}/vlc/plugins/audio_filter/libspeex_resampler_plugin.so
%{_libdir}/vlc/plugins/codec/libspeex_plugin.so*
%endif

%files plugin-flac
%{_libdir}/vlc/plugins/demux/libflacsys_plugin.so
%{_libdir}/vlc/plugins/codec/libflac_plugin.so*

%files plugin-opus
%{_libdir}/vlc/plugins/codec/libopus_plugin.so*

%if %{with dv}
%files plugin-dv
%{_libdir}/vlc/plugins/access/libdc1394_plugin.so
%endif

%if %{with mod}
%files plugin-mod
%{_libdir}/vlc/plugins/demux/libmod_plugin.so*
%endif

%if %{with mpc}
%files plugin-mpc
%endif

#audio plugins
%if %{with pulse}
%files plugin-pulse
%{_libdir}/vlc/libvlc_pulse.so*
%{_libdir}/vlc/plugins/access/libpulsesrc_plugin.so
%{_libdir}/vlc/plugins/audio_output/libpulse_plugin.so*
%{_libdir}/vlc/plugins/services_discovery/libpulselist_plugin.so
%endif

%if %{with jack}
%files plugin-jack
%{_libdir}/vlc/plugins/access/libaccess_jack_plugin.so
%{_libdir}/vlc/plugins/audio_output/libjack_plugin.so*
%endif

%if %{with bonjour}
%files plugin-bonjour
%{_libdir}/vlc/plugins/services_discovery/libavahi_plugin.so
%endif

%if %{with upnp}
%files plugin-upnp
%{_libdir}/vlc/plugins/services_discovery/libupnp_plugin.so*
%endif

%if %{with gnutls}
%files plugin-gnutls
%{_libdir}/vlc/plugins/misc/libgnutls_plugin.so*
%endif

%files plugin-libnotify
%{_libdir}/vlc/plugins/notify/libnotify_plugin.so*

%files plugin-chromecast
%{_libdir}/vlc/plugins/demux/libdemux_chromecast_plugin.so
%{_libdir}/vlc/plugins/stream_out/libstream_out_chromecast_plugin.so

%post core
%{_libdir}/vlc/vlc-cache-gen %{_libdir}/vlc/plugins

%post
%{_libdir}/vlc/vlc-cache-gen %{_libdir}/vlc/plugins

%transfiletriggerin -- %{_libdir}/vlc/plugins
%{_libdir}/vlc/vlc-cache-gen %{_libdir}/vlc/plugins

%transfiletriggerpostun -- %{_libdir}/vlc/plugins
%{_libdir}/vlc/vlc-cache-gen %{_libdir}/vlc/plugins
