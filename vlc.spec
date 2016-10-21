%define snapshot 0
%define pre 0
%define rel 5
%if %{pre}
%define release 0.%{pre}.%{rel}
%elsif %{snapshot}
%define release 0.%{snapshot}.%{rel}
%else
%define release %{rel}
%endif

%define libmajor 5
%define coremajor 8

%if %{snapshot}
%define fname %{name}-snapshot-%{snapshot}
%elsif %{pre}
%define fname %{name}-%{version}-%{pre}
%else
%define fname %{name}-%{version}
%endif

%define with_plf 0

%define with_fribidi 1
%define with_xml 1
%define with_ncurses 1
%define with_lirc 1
%ifarch %{ix86} x86_64 %{arm}
%define with_qt4 0
%define with_qt5 1
%else
%define with_qt4 0
%define with_qt5 1
%endif
%define with_svlc 1
%define with_udev 1
%define with_aa 1
%define with_sdl 1
%define with_sdl_image 1
%define with_xvideo 1
%define with_twolame 1
%define with_schroedinger 1
%define with_fluidsynth 1
%define with_gme 1
%define with_zvbi 1
%define with_kate 1
%define with_kde 0
%define with_goom 0
%define with_projectm 1
%define with_ass 1
%define with_lua 1
%define with_taglib 1
%define with_mtp 1
%define with_xcb_randr 1

%define with_mad 1
%define with_ogg 1
%define with_theora 1
%define with_speex 1
%define with_flac 1
%define with_mkv 1
%define with_a52 1
%define with_vcd 1
%define with_cddb 1
%define with_dv 1
%define with_dvdnav 1
%define with_dvbpsi 1
%define with_satellite 0
%define with_mpeg2dec 1
%define with_mpc 1
%define with_faad 0
%define with_faac 0
%define with_lame 0
%define with_dts 0
%define with_x264 0
%define with_x265 0
%define with_live 1
%define with_libv4l 1
%define with_sysfs 1
%define with_shout 1

%define with_pulse 1
%define with_jack 1
%define with_alsa 1

%define with_bonjour 1
%define with_upnp 1
%define with_smb 1
%define with_tar 1
%define with_mod 1
%define with_gnutls 1

%define with_bluray 1
# is non-free stuf
%ifarch %{arm}
%define with_crystalhd 0
%else
%define with_crystalhd 1
%endif

%define libname %mklibname %{name} %{libmajor}
%define libnamecore %mklibname vlccore %{coremajor}
%define devname %mklibname -d %{name}

# without
%{?_without_plf:	%{expand: %%global with_plf 0}}
%{?_without_fribidi:	%{expand: %%global with_fribidi 0}}
%{?_without_udev:	%{expand: %%global with_udev 0}}
%{?_without_ncurses:	%{expand: %%global with_ncurses 0}}
%{?_without_lirc:	%{expand: %%global with_lirc 0}}
%{?_without_qt4:	%{expand: %%global with_qt4 0}}
%{?_without_qt5:	%{expand: %%global with_qt5 0}}
%{?_without_svlc:	%{expand: %%global with_svlc 0}}

%{?_without_aa:   	%{expand: %%global with_aa 0}}
%{?_without_sdl:   	%{expand: %%global with_sdl 0}}
%{?_without_xvideo:	%{expand: %%global with_xvideo 0}}
%{?_without_twolame:	%{expand: %%global with_twolame 0}}
%{?_without_schroedinger: %{expand: %%global with_schroedinger 0}}
%{?_without_fluidsynth:	%{expand: %%global with_fluidsynth 0}}
%{?_without_gme:	%{expand: %%global with_gme 0}}
%{?_without_lua:	%{expand: %%global with_lua 0}}
%{?_without_zvbi:	%{expand: %%global with_zvbi 0}}
%{?_without_kate:	%{expand: %%global with_kate 0}}

%{?_without_mad:	%{expand: %%global with_mad 0}}
%{?_without_ogg:	%{expand: %%global with_ogg 0}}
%{?_without_theora:	%{expand: %%global with_theora 0}}
%{?_without_speex:	%{expand: %%global with_speex 0}}
%{?_without_flac:	%{expand: %%global with_flac 0}}
%{?_without_mkv:	%{expand: %%global with_mkv 0}}
%{?_without_mpeg2dec:	%{expand: %%global with_mpeg2dec 0}}
%{?_without_mpc:	%{expand: %%global with_mpc 0}}
%{?_without_faad:	%{expand: %%global with_faad 0}}
%{?_without_faac:	%{expand: %%global with_faac 0}}
%{?_without_x264:	%{expand: %%global with_x264 0}}
%{?_without_x265:	%{expand: %%global with_x265 0}}
%{?_without_lame:	%{expand: %%global with_lame 0}}
%{?_without_dts:	%{expand: %%global with_dts 0}}
%{?_without_live:	%{expand: %%global with_live 0}}
%{?_without_a52:	%{expand: %%global with_a52 0}}
%{?_without_dv:		%{expand: %%global with_dv 0}}
%{?_without_dvdnav:	%{expand: %%global with_dvdnav 0}}
%{?_without_dvbpsi:	%{expand: %%global with_dvbpsi 0}}
%{?_without_libv4l:	%{expand: %%global with_libv4l 0}}
%{?_without_sysfs:	%{expand: %%global with_sysfs 0}}
%{?_without_satellite:	%{expand: %%global with_satellite 0}}
%{?_without_vcd:	%{expand: %%global with_vcd 0}}
%{?_without_cddb:	%{expand: %%global with_cddb 0}}
%{?_without_shout:	%{expand: %%global with_shout 0}}

%{?_without_pulse:	%{expand: %%global with_pulse 0}}
%{?_without_jack:	%{expand: %%global with_jack 0}}
%{?_without_alsa:	%{expand: %%global with_alsa 0}}

%{?_without_bonjour:	%{expand: %%global with_bonjour 0}}
%{?_without_upnp:	%{expand: %%global with_upnp 0}}
%{?_without_tar:	%{expand: %%global with_tar 0}}
%{?_without_mod:	%{expand: %%global with_mod 0}}
%{?_without_gnutls:	%{expand: %%global with_gnutls 0}}

%{?_without_bluray:	%{expand: %%global with_bluray 0}}
%{?_without_crystalhd:	%{expand: %%global with_crystalhd 0}}

# with
%{?_with_plf:		%{expand: %%global with_plf 1}}
%{?_with_fribidi:	%{expand: %%global with_fribidi 1}}
%{?_with_udev:		%{expand: %%global with_udev 1}}
%{?_with_ncurses:	%{expand: %%global with_ncurses 1}}
%{?_with_lirc:		%{expand: %%global with_lirc 1}}
%{?_with_qt4:		%{expand: %%global with_qt4 1}}
%{?_with_qt5:		%{expand: %%global with_qt5 1}}
%{?_with_svlc:		%{expand: %%global with_svlc 1}}

%{?_with_aa:		%{expand: %%global with_aa 1}}
%{?_with_sdl:		%{expand: %%global with_sdl 1}}
%{?_with_xvideo:	%{expand: %%global with_xvideo 1}}
%{?_with_twolame:	%{expand: %%global with_twolame 1}}
%{?_with_schroedinger: 	%{expand: %%global with_schroedinger 1}}
%{?_with_fluidsynth:	%{expand: %%global with_fluidsynth 1}}
%{?_with_gme:		%{expand: %%global with_gme 1}}
%{?_with_lua:		%{expand: %%global with_lua 1}}
%{?_with_zvbi:		%{expand: %%global with_zvbi 1}}
%{?_with_kate:		%{expand: %%global with_kate 1}}

%{?_with_mad:		%{expand: %%global with_mad 1}}
%{?_with_ogg:		%{expand: %%global with_ogg 1}}
%{?_with_theora:	%{expand: %%global with_theora 1}}
%{?_with_speex:		%{expand: %%global with_speex 1}}
%{?_with_flac:		%{expand: %%global with_flac 1}}
%{?_with_mkv:		%{expand: %%global with_mkv 1}}
%{?_with_mpeg2dec:	%{expand: %%global with_mpeg2dec 1}}
%{?_with_mpc:		%{expand: %%global with_mpc 1}}
%{?_with_faad:		%{expand: %%global with_faad 1}}
%{?_with_faac:		%{expand: %%global with_faac 1}}
%{?_with_x264:		%{expand: %%global with_x264 1}}
%{?_with_x265:		%{expand: %%global with_x265 1}}
%{?_with_lame:		%{expand: %%global with_lame 1}}
%{?_with_dts:		%{expand: %%global with_dts 1}}
%{?_with_live:		%{expand: %%global with_live 1}}
%{?_with_a52:		%{expand: %%global with_a52 1}}
%{?_with_dv:		%{expand: %%global with_dv 1}}
%{?_with_dvdnav:	%{expand: %%global with_dvdnav 1}}
%{?_with_dvbpsi:	%{expand: %%global with_dvbpsi 1}}
%{?_with_libv4l:	%{expand: %%global with_libv4l 1}}
%{?_with_sysfs:		%{expand: %%global with_sysfs 1}}
%{?_with_satellite:	%{expand: %%global with_satellite 1}}
%{?_with_vcd:		%{expand: %%global with_vcd 1}}
%{?_with_cddb:		%{expand: %%global with_cddb 1}}
%{?_with_shout:		%{expand: %%global with_shout 1}}

%{?_with_pulse:		%{expand: %%global with_pulse 1}}
%{?_with_jack:		%{expand: %%global with_jack 1}}
%{?_with_alsa:		%{expand: %%global with_alsa 1}}

%{?_with_bonjour:	%{expand: %%global with_bonjour 1}}
%{?_with_upnp:		%{expand: %%global with_upnp 1}}
%{?_with_tar:		%{expand: %%global with_tar 1}}
%{?_with_mod:		%{expand: %%global with_mod 1}}
%{?_with_gnutls:	%{expand: %%global with_gnutls 1}}

%{?_with_bluray:	%{expand: %%global with_bluray 1}}

%if %{mdvver} <= 201100
%define with_goom 1
%endif

%if %{mdvver} < 201100
%define with_libv4l 0
%define with_schroedinger 0
%endif

######################
# Hardcode PLF build
# define with_plf 1
######################

%if %{with_plf}
%if %{mdvver} >= 201100
# make EVR of plf build higher than regular to allow update, needed with rpm5 mkrel
%define extrarelsuffix plf
%endif
%define distsuffix plf
%global with_faac 1
%global with_faad 1
%global with_lame 1
%global with_dts 1
%global with_x264 1
%global with_x265 1
%endif

%define git_url git://git.videolan.org/vlc.git

Summary:	MPEG, MPEG2, DVD and DivX player
Name:		vlc
Version:	2.2.4
Release:	%{release}%{?extrarelsuffix}
#gw the shared libraries are LGPL
License:	GPLv2+ and LGPLv2+
Group:		Video
URL:		http://www.videolan.org/
%if %{snapshot}
Source0:	http://nightlies.videolan.org/build/source/%{fname}.tar.xz
%else
Source0:	http://download.videolan.org/pub/videolan/%{name}/%{version}/%{fname}.tar.xz
%endif
Patch1:		vlc-2.0.1-automake-1.12.patch
Patch20:	vlc-2.1.2-fix-default-font.patch
Patch22:	vlc-2.1.2-live555-201306.patch
Patch23:	vlc-2.1.5-fix-skins2-default-skin-creation.patch
# Disable errors when ffmpeg 3.0 is used, apparently it is safe as the
# commit in 2.9 causing issues was reverted for 3.0
Patch24:	vlc-ffmpeg3.patch
# Debian patch for compiling with ffmpeg 2.9+
Patch25:	ffmpeg_2.9.patch

BuildRequires:	desktop-file-utils
BuildRequires:	libtool
BuildRequires:	yasm
BuildRequires:	gettext-devel
BuildRequires:	libmpcdec-devel
BuildRequires:	pkgconfig(caca)
BuildRequires:	pkgconfig(dirac)
BuildRequires:	pkgconfig(dvdread)
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gnome-vfs-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libavcodec)
BuildRequires:	pkgconfig(libcdio)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libproxy-1.0)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(libssh2)
BuildRequires:	pkgconfig(libchromaprint)
BuildRequires:	pkgconfig(opencv)
BuildRequires:	pkgconfig(opus)
BuildRequires:	pkgconfig(portaudio-2.0)
BuildRequires:	pkgconfig(vdpau)
BuildRequires:	pkgconfig(libvncclient)
BuildRequires:	pkgconfig(xcb-util)
BuildRequires:	pkgconfig(xcb-keysyms)
BuildRequires:	pkgconfig(xpm)

%if %{with_sysfs}
BuildRequires:	sysfsutils-devel
%endif
%if %{with_tar}
BuildRequires:	libtar-devel
%endif
%if %{with_mod}
BuildRequires:	pkgconfig(libmodplug)
%endif
%if %{with_gnutls}
BuildRequires:	pkgconfig(gnutls)
%endif
%if %{with_fribidi}
BuildRequires:	pkgconfig(fribidi)
%endif
%if %{with_libv4l}
BuildRequires:	pkgconfig(libv4l2)
%endif
%if %{with_udev}
BuildRequires:	pkgconfig(udev)
%endif
%if %{with_qt4}
BuildRequires:	qt4-devel
%endif
%if %{with_qt5}
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5X11Extras)
BuildRequires:	qmake5
%endif
%if %{with_taglib}
BuildRequires:	pkgconfig(taglib)
%endif
%if %{with_mtp}
BuildRequires:	pkgconfig(libmtp)
%endif
%if %{with_mad}
BuildRequires:	pkgconfig(id3tag)
BuildRequires:	pkgconfig(mad)
%endif
%if %{with_ogg}
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(vorbis)
%rename	vlc-plugin-ogg
%endif
%if %{with_xcb_randr}
BuildRequires:	pkgconfig(xcb)
%endif
%if %{with_speex}
BuildRequires:	pkgconfig(speex) >= 1.1.16
BuildRequires:	pkgconfig(speexdsp)
%endif
%if %{with_flac}
BuildRequires:	pkgconfig(flac)
Suggests:	vlc-plugin-flac
%endif
%if %{with_mkv}
BuildRequires:	libmatroska-devel >= 1.0.0
%endif
%if %{with_dvdnav}
BuildRequires:	pkgconfig(dvdnav)
%rename	vlc-plugin-dvdnav
%endif
%if %{with_a52}
BuildRequires:	a52dec-devel
%rename	vlc-plugin-a52
%endif
%if %{with_vcd}
BuildRequires:	pkgconfig(libvcdinfo)
%endif
%if %{with_cddb}
BuildRequires:	pkgconfig(libcddb)
%else
BuildConflicts:	pkgconfig(libcddb)
%endif
%if %{with_smb}
BuildRequires:	pkgconfig(smbclient)
%endif
%if %{with_lame}
BuildRequires:	lame-devel
%endif
%if %{with_mpeg2dec}
BuildRequires:	pkgconfig(libmpeg2)
%endif
%if %{with_mpc}
BuildRequires:	libmpcdec-devel
%endif
%if %{with_faad}
BuildRequires:	faad2-devel >= 2.0
%rename	vlc-plugin-faad
%endif
%if %{with_faac}
BuildRequires:	faac-devel
%endif
%if %{with_alsa}
BuildRequires:	pkgconfig(alsa)
%endif
%if %{with_pulse}
BuildRequires:	pkgconfig(libpulse)
%endif
%if %{with_jack}
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(samplerate)
%endif
%if %{with_bonjour}
BuildRequires:	pkgconfig(avahi-client)
%endif
%if %{with_dvbpsi}
BuildRequires:	pkgconfig(libdvbpsi)
%endif
%if %{with_dts}
BuildRequires:	pkgconfig(libdts)
%endif
%if %{with_x264}
BuildRequires:	pkgconfig(x264)
%endif
%if %{with_x265}
BuildRequires:	pkgconfig(x265)
%endif
%if %{with_xml}
BuildRequires:	pkgconfig(libxml-2.0)
%endif
%if %{with_live}
BuildRequires:	live-devel > 2011.12.23
%endif
%if %{with_xvideo}
BuildRequires:	pkgconfig(xv)
%endif
%if %{with_kde}
BuildRequires:	kdelibs4-core
%endif
%if %{with_bluray}
BuildRequires:	pkgconfig(libbluray) >= 0.2.1
%endif
%if %{with_crystalhd}
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
%if %{with_pulse}
# needed when using pulseaudio
Requires:	vlc-plugin-pulse
%endif
Requires:	fonts-ttf-vera
Requires(post,postun):	desktop-file-utils
Conflicts:	vlc-plugin-common < %{version}-%{release}

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

%if %{with_plf}
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

%if %{with_zvbi}
%package plugin-zvbi
Summary:	Add Teletext and Closed Caption support to VLC
Group:		Video
Requires:	%{name} = %{version}
BuildRequires:	pkgconfig(zvbi-0.2)

%description plugin-zvbi
This package adds support for Raw VBI, Teletext and Closed Caption based on
the ZVBI library to VLC.
%endif

%if %{with_kate}
%package plugin-kate
Summary:	Add subtitle and Karaoke text support to VLC
Group:		Video
Requires:	%{name} = %{version}
BuildRequires:	pkgconfig(tiger)

%description plugin-kate
This package adds support for subtitles and Karaoke text display based on
the libkate library to VLC.
%endif

%if %{with_ass}
%package plugin-libass
Summary:	Add subtitle support to VLC using libass
Group:		Video
Requires:	%{name} = %{version}
BuildRequires:	pkgconfig(libass)

%description plugin-libass
This package adds support for subtitles based on the libass library to VLC.
%endif

%if %{with_lua}
%package plugin-lua
Summary:	Add Lua scripting to vlc
Group:		Video
Requires:	%{name} = %{version}
BuildRequires:	pkgconfig(lua)

%description plugin-lua
This plugin adds lua scripting and provides a few example scripts as well.
%endif

%if %{with_ncurses}
%package plugin-ncurses
Summary:	Ncurses console-based plugin for the VLC media player
Group:		Video
Requires:	%{name} = %{version}
BuildRequires:	pkgconfig(ncurses)

%description plugin-ncurses
This plugin adds a ncurses interface to the VLC media player. To
activate it, use the `--intf ncurses' flag.
%endif

%if %{with_lirc}
%package plugin-lirc
Summary:	Lirc plugin for the VLC media player
Group:		Video
Requires:	%{name} = %{version}
%rename	vlc-lirc
BuildRequires:	pkgconfig(liblircclient0)

%description plugin-lirc
This plugin is an infrared lirc interface for the VLC media player. To
activate it, use the `--extraintf lirc' flag.
%endif

%package -n svlc
Summary:	Skinned GUI plugin for the VLC media player
Group:		Video
Requires:	%{name} = %{version}
Provides:	vlc-gui
Requires(post,postun): desktop-file-utils

%description -n svlc
This plugin adds a skinned GUI interface to the VLC media player. To
activate it, run the `svlc' program.

#
# video plugins
%if %{with_aa}
%package plugin-aa
Summary:	ASCII art video plugin for the VLC media player
Group:		Video
Requires:	%{name} = %{version}
%rename	vlc-aa
BuildRequires:	aalib-devel

%description plugin-aa
This is an ASCII art video output plugin for the VLC media playe. To
activate it, use the `--vout aa' flag or select the `aa' video output
plugin from the preferences menu.
%endif

%if %{with_sdl}
%package plugin-sdl
Summary:	Simple DirectMedia Layer video plugin for the VLC media player
Group:		Video
Requires:	%{name} = %{version}
%rename	vlc-sdl
%if %{with_sdl_image}
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

%if %{with_shout}
%package plugin-shout
Summary:	Shoutcast and Icecast connector
Group:		Sound
Requires:	%{name} = %{version}
BuildRequires:	pkgconfig(shout)

%description plugin-shout
This plugin adds support for Icecast and Shoutcast servers.
%endif

%package plugin-opengl
Summary:	OpenGL video output plugin for the VLC media player
Group:		Video
Requires:	%{name} = %{version}

%description plugin-opengl
This plugin adds support for OpenGL video output to
the VLC media player.

# visualization plugins

%if %{with_goom}
%package plugin-goom
Summary:	Visualization plugin for the VLC media player
Group:		Video
BuildRequires:	libgoom2-devel
Requires:	%{name} = %{version}

%description plugin-goom
This is a visualization plugin for VLC media player based on the Goom library.
%endif

%if %{with_projectm}
%package plugin-projectm
Summary:	Visualization plugin for the VLC media player
Group:		Video
BuildRequires:	pkgconfig(libprojectM)
Requires:	%{name} = %{version}

%description plugin-projectm
This is a visualization plugin for VLC media player based on projectm.
%endif

%if %{with_theora}
%package plugin-theora
Summary:	Theora video codec for the VLC media player
Group:		Video
Requires:	%{name} = %{version}
BuildRequires:	pkgconfig(theora)

%description plugin-theora
These plugin adds support for the Ogg Theora video format to the VLC
media player. They are autodetected.
%endif

%if %{with_twolame}
%package plugin-twolame
Summary:	MP2 encoder plugin for VLC
Group:		Sound
Requires:	%{name} = %{version}
BuildRequires:	pkgconfig(twolame)

%description plugin-twolame
These plugins add support for the Twolame MPEG Audio Layer 2 encoder
to the VLC media player. They are autodetected.
%endif

%if %{with_fluidsynth}
%package plugin-fluidsynth
Summary:	Add MIDI playback support to VLC based on Fluidsynth
Group:		Sound
Requires:	%{name} = %{version}
BuildRequires:	pkgconfig(fluidsynth)

%description plugin-fluidsynth
This plugin adds support for MIDI playback to VLC based on the Fluidsynth
library.
%endif

%if %{with_gme}
%package plugin-gme
Summary:	Add game music playback support to VLC based on libgme
Group:		Sound
Requires:	%{name} = %{version}
BuildRequires:	libgme-devel

%description plugin-gme
This plugin adds support for video game music playback to VLC based on the
GME library.
%endif

%if %{with_schroedinger}
%package plugin-schroedinger
Summary:	Dirac plugin for VLC based on Schroedinger
Group:		Video
Requires:	%{name} = %{version}
BuildRequires:	pkgconfig(schroedinger-1.0)

%description plugin-schroedinger
These plugins add support for the Dirac video format based on Schroedinger.
to the VLC media player.
%endif

%package plugin-speex
Summary:	Ogg Speex codec plugin for the VLC media player
Group:		Sound
Requires:	%{name} = %{version}

%description plugin-speex
These plugins add support for the Ogg Speex codec to the VLC media
player. They are autodetected.

%package plugin-flac
Summary:	Flac codec plugin for the VLC media player
Group:		Video
Requires:	%{name} = %{version}

%description plugin-flac
These plugins add support for the FLAC compressed audio format to the
VLC media player.

%package plugin-opus
Summary:	Opus codec plugin for the VLC media player
Group:		Sound
Requires:	%name = %version

%description plugin-opus
These plugins add support for the Opus codec to the VLC media
player. They are autodetected.

%if %{with_dv}
%package plugin-dv
Summary:	DV codec plugin for the VLC media player
Group:		Video
Requires:	%{name} = %{version}
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
Requires:	%{name} = %{version}

%description plugin-mod
This plugin adds support for music module playback based on libmodplug
to the VLC media player.

%package plugin-mpc
Summary:	MPC audio decoder plugin for the VLC media player
Group:		Sound
Requires:	%{name} = %{version}

%description plugin-mpc
This plugin adds support for Musepack audio playback based on libmpcdec
to the VLC media player.

# audio plugins
%if %{with_pulse}
%package plugin-pulse
Summary:	PulseAudio plugin for the VLC media player
Group:		Video
Requires:	%{name} = %{version}
%rename	vlc-pulse

%description plugin-pulse
This plugin adds support for the PulseAudio Sound Daemon to the VLC
media player. To activate it, use the `--aout pulse' flag or select the
`pulse' audio output plugin from the preferences menu.
%endif

%package plugin-jack
Summary:	Jack audio plugin for the VLC media player
Group:		Video
Requires:	%{name} = %{version}
%rename	vlc-jack

%description plugin-jack
This plugin adds support for the Jack Audio Connection Kit to the VLC
media player. To activate it, use the `--aout jack' flag or select the
`jack' audio output plugin from the preferences menu.

%package plugin-bonjour
Summary:	Bonjour service discovery plugin for the VLC media player
Group:		Video
Requires:	%{name} = %{version}

%description plugin-bonjour
This plugin adds support for Bonjour service discovery to
the VLC media player.

%if %{with_upnp}
%package plugin-upnp
Summary:	UPNP service discovery plugin for the VLC media player
Group:		Video
Requires:	%{name} = %{version}
BuildRequires:	pkgconfig(libupnp)

%description plugin-upnp
This plugin adds support for UPNP service discovery to
the VLC media player.
%endif

%package plugin-gnutls
Summary:	Secure Socket Layer plugin for the VLC media player
Group:		Video
Requires:	%{name} = %{version}

%description plugin-gnutls
This plugin adds support for SSL/TLS to the VLC media player.

%package plugin-libnotify
Summary:	Notification popup plugin for the VLC media player
Group:		Video
Requires:	%{name} = %{version}

%description plugin-libnotify
This plugin adds support for notification popup messages to
the VLC media player.

%prep
%if %{snapshot}
%setup -q -n %{name}
%else
%setup -q -n %{fname}
%endif

%patch1 -p1 -b .automake12~
%patch20 -p1 -b .fonts
%patch22 -p1 -b .live555
%patch23 -p1 -b .skintar
%patch24 -p1
%patch25 -p1

#gw if we want to regenerate libtool, we must remove the local versions of
# the libtool m4 files, aclocal will replace them
pushd m4
rm -fv argz.m4 libtool.m4 ltdl.m4 ltoptions.m4 ltsugar.m4 ltversion.m4 lt~obsolete.m4
popd

# Our Qt is patched with the bit below -- no point in erroring out
sed -i -e 's/.*ERROR.*I78ef29975181ee22429c9bd4b11d96d9e68b7a9c.*/AC_MSG_WARN([OMV Qt is good])/' configure.ac

%if %{snapshot}
./bootstrap
%endif
autoreconf -fiv

%build
#export CC=gcc
#export CXX=g++

# add missing ebml include dir
export CPPFLAGS="$CPPFLAGS -I/usr/include/ebml"
#gw the speex headers have moved
export CPPFLAGS="$CPPFLAGS -I%{_includedir}/speex"
# locate libsmbclient.h
export CPPFLAGS="$CPPFLAGS -I%{_includedir}/samba-4.0"

%configure \
--disable-dependency-tracking \
%ifarch %{ix86}
--disable-sse \
%endif
--disable-sid \
%if %{with_bonjour}
--enable-bonjour \
%else
--disable-bonjour \
%endif
%if %{with_smb}
--enable-smbclient \
%else
--disable-smbclient \
%endif
%if %{with_ncurses}
--enable-ncurses \
%endif
%if %{with_lirc}
--enable-lirc \
%endif
--enable-xvideo \
%if %{with_aa}
--enable-aa \
%endif
%if %{with_sdl}
--enable-sdl \
%endif
%if %{with_mad}
--enable-mad \
%endif
%if %{with_ogg}
--enable-vorbis \
--enable-ogg \
%else
--disable-vorbis \
--disable-ogg \
%endif
%if %{with_theora}
--enable-theora \
%endif
%if %{with_speex}
--enable-speex \
%else
--disable-speex \
%endif
%if %{with_flac}
--enable-flac \
%else
--disable-flac \
%endif
%if %{with_mkv}
--enable-mkv \
%else
--disable-mkv \
%endif
%if %{with_dv}
--enable-dv1394 \
%else
--disable-dv1394 \
%endif
%if %{with_dvbpsi}
--enable-dvbpsi \
%else
--disable-dvbpsi \
%endif
%if %{with_shout}
--enable-shout \
%endif
%if ! %{with_pulse}
--disable-pulse \
%endif
%if %{with_jack}
--enable-jack \
%endif
%if ! %{with_alsa}
--disable-alsa \
%endif
%if %{with_mpeg2dec}
--enable-libmpeg2 \
%else
--disable-libmpeg2 \
%endif
%if %{with_faad}
--enable-faad \
%endif
%if %{with_dts}
--enable-dca \
%else
--disable-dca \
%endif
%if ! %{with_svlc}
--disable-skins2 \
%endif
%if ! %{with_dvdnav}
--disable-dvdnav \
%endif
%if %{with_live}
--enable-live555 \
%endif
%if %{with_gnutls}
--enable-gnutls \
%endif
--disable-rpath \
%if %{with_vcd}
--enable-vcdx \
%endif
%if %{with_cddb}
--enable-libcddb \
%else
--disable-libcddb \
%endif
%if %{with_x264}
--enable-x264 \
%else
--disable-x264 \
%endif
%if %{with_x265}
--enable-x265 \
%else
--disable-x265 \
%endif
%if %{with_twolame}
--enable-twolame \
%endif
%if %{with_bluray}
--enable-bluray \
%else
--disable-bluray \
%endif
--enable-realrtsp \
%if !%{with_kde}
--without-kde-solid \
%endif
%ifarch x86_64
--with-pic
%endif

%make --output-sync=target -j1

%install
%__mkdir_p %{buildroot}%{_libdir}
%makeinstall_std transform=""
find %{buildroot}%{_libdir}/vlc -name \*.la -exec %__rm -f {} \;
%find_lang %{name}
%__rm -rf installed-docs
%__mv %{buildroot}%{_datadir}/doc/vlc installed-docs
%if ! %{with_svlc}
%__rm -rf %{buildroot}%{_datadir}/vlc/skin*
%endif
# menu

desktop-file-install --vendor="" \
--add-mime-type="x-content/video-dvd" \
--add-mime-type="x-content/video-vcd" \
--add-mime-type="x-content/video-svcd" \
--add-mime-type="x-content/audio-cdda" \
--add-category="Qt" \
--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%if %{with_svlc}
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
%__mkdir_p %{buildroot}/{%{_miconsdir},%{_liconsdir}}
%__install -m 644 %{pngdir}/16x16/vlc.png %{buildroot}/%{_miconsdir}/vlc.png
%__install -m 644 %{pngdir}/32x32/vlc.png %{buildroot}/%{_iconsdir}/vlc.png
%__install -m 644 %{pngdir}/48x48/vlc.png %{buildroot}/%{_liconsdir}/vlc.png

%files -f %{name}.lang
%doc NEWS README COPYING AUTHORS THANKS
%doc installed-docs/* doc/lirc/
%{_bindir}/cvlc
%{_bindir}/qvlc
%{_bindir}/vlc
%{_bindir}/vlc-wrapper
%dir %{_datadir}/vlc/
%{_datadir}/vlc/*.*
%{_datadir}/vlc/utils
%dir %{_libdir}/vlc
%{_libdir}/vlc/vlc-cache-gen
%{_libdir}/vlc/libvlc_vdpau.so.*

%dir %{_libdir}/vlc/plugins
%{_libdir}/vlc/plugins/plugins.dat

%dir %{_libdir}/vlc/plugins/access
%{_libdir}/vlc/plugins/access/libattachment_plugin.so
%{_libdir}/vlc/plugins/access/libavio_plugin.so
%{_libdir}/vlc/plugins/access/libaccess_bd_plugin.so
%if %{with_dvdnav}
%{_libdir}/vlc/plugins/access/libdvdnav_plugin.so
%endif
%{_libdir}/vlc/plugins/access/libgnomevfs_plugin.so
%{_libdir}/vlc/plugins/access/libimem_plugin.so
%if %{with_mtp}
%{_libdir}/vlc/plugins/access/libaccess_mtp_plugin.so
%{_libdir}/vlc/plugins/services_discovery/libmtp_plugin.so
%endif
%{_libdir}/vlc/plugins/access/librar_plugin.so
%{_libdir}/vlc/plugins/access/libaccess_realrtsp_plugin.so
%{_libdir}/vlc/plugins/access/libshm_plugin.so
%{_libdir}/vlc/plugins/access/libsftp_plugin.so
%{_libdir}/vlc/plugins/access/libcdda_plugin.so*
%{_libdir}/vlc/plugins/access/libftp_plugin.so*
%{_libdir}/vlc/plugins/access/libhttp_plugin.so*
%{_libdir}/vlc/plugins/access/libaccess_mms_plugin.so*
%if %{with_smb}
%{_libdir}/vlc/plugins/access/libsmb_plugin.so*
%endif
%{_libdir}/vlc/plugins/access/libtcp_plugin.so*
%{_libdir}/vlc/plugins/access/libudp_plugin.so*
%{_libdir}/vlc/plugins/access/libvdr_plugin.so*
%{_libdir}/vlc/plugins/access/libdv1394_plugin.so*
%{_libdir}/vlc/plugins/access/libdtv_plugin.so*
%{_libdir}/vlc/plugins/access/libdvb_plugin.so*
%{_libdir}/vlc/plugins/access/libidummy_plugin.so
%{_libdir}/vlc/plugins/access/libfilesystem_plugin.so
%if %{with_live}
%{_libdir}/vlc/plugins/access/liblive555_plugin.so
%endif
%{_libdir}/vlc/plugins/access/libvnc_plugin.so
%{_libdir}/vlc/plugins/access/librtp_plugin.so
%{_libdir}/vlc/plugins/access/libsdp_plugin.so
%{_libdir}/vlc/plugins/access/libtimecode_plugin.so
%{_libdir}/vlc/plugins/access/libv4l2_plugin.so*
%{_libdir}/vlc/plugins/access/libdvdread_plugin.so*
%if %{with_vcd}
%{_libdir}/vlc/plugins/access/libvcdx_plugin.so*
%endif
%{_libdir}/vlc/plugins/access/libvcd_plugin.so*
%{_libdir}/vlc/plugins/access/libxcb_screen_plugin.so
%{_libdir}/vlc/plugins/access/libzip_plugin.so
%if %{with_bluray}
%{_libdir}/vlc/plugins/access/liblibbluray_plugin.so
%endif

%dir %{_libdir}/vlc/plugins/access_output/
%{_libdir}/vlc/plugins/access_output/libaccess_output_dummy_plugin.so*
%{_libdir}/vlc/plugins/access_output/libaccess_output_file_plugin.so*
%{_libdir}/vlc/plugins/access_output/libaccess_output_http_plugin.so*
%{_libdir}/vlc/plugins/access_output/libaccess_output_livehttp_plugin.so*
%{_libdir}/vlc/plugins/access_output/libaccess_output_udp_plugin.so*

%dir %{_libdir}/vlc/plugins/audio_filter
%{_libdir}/vlc/plugins/audio_filter/libaudiobargraph_a_plugin.so
%{_libdir}/vlc/plugins/audio_filter/libaudio_format_plugin.so*
%{_libdir}/vlc/plugins/audio_filter/libchorus_flanger_plugin.so
%{_libdir}/vlc/plugins/audio_filter/libcompressor_plugin.so
%if %{with_dts}
%{_libdir}/vlc/plugins/audio_filter/libdtstofloat32_plugin.so*
%endif
%{_libdir}/vlc/plugins/audio_filter/libdolby_surround_decoder_plugin.so*
%{_libdir}/vlc/plugins/audio_filter/libdtstospdif_plugin.so*
%{_libdir}/vlc/plugins/audio_filter/libequalizer_plugin.so*
%{_libdir}/vlc/plugins/audio_filter/libheadphone_channel_mixer_plugin.so*
%{_libdir}/vlc/plugins/audio_filter/libkaraoke_plugin.so
%{_libdir}/vlc/plugins/audio_filter/libmono_plugin.so
%if %{with_mad}
%{_libdir}/vlc/plugins/audio_filter/libmpgatofixed32_plugin.so*
%endif
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

%dir %{_libdir}/vlc/plugins/audio_mixer
%{_libdir}/vlc/plugins/audio_mixer/libfloat_mixer_plugin.so
%{_libdir}/vlc/plugins/audio_mixer/libinteger_mixer_plugin.so

%dir %{_libdir}/vlc/plugins/audio_output
%{_libdir}/vlc/plugins/audio_output/libadummy_plugin.so
%{_libdir}/vlc/plugins/audio_output/libamem_plugin.so
%{_libdir}/vlc/plugins/audio_output/libafile_plugin.so

%dir %{_libdir}/vlc/plugins/codec
%if %{with_a52}
%{_libdir}/vlc/plugins/codec/liba52_plugin.so*
%{_libdir}/vlc/plugins/audio_filter/liba52tofloat32_plugin.so*
%{_libdir}/vlc/plugins/audio_filter/liba52tospdif_plugin.so*
%endif
%{_libdir}/vlc/plugins/codec/libadpcm_plugin.so*
%{_libdir}/vlc/plugins/codec/libaes3_plugin.so
%{_libdir}/vlc/plugins/codec/libaraw_plugin.so*
%{_libdir}/vlc/plugins/codec/libavcodec_plugin.so
%{_libdir}/vlc/plugins/codec/libcc_plugin.so
%{_libdir}/vlc/plugins/codec/libcdg_plugin.so
%if %{with_crystalhd}
%{_libdir}/vlc/plugins/codec/libcrystalhd_plugin.so
%endif
%{_libdir}/vlc/plugins/codec/libcvdsub_plugin.so*
%{_libdir}/vlc/plugins/codec/libddummy_plugin.so
%{_libdir}/vlc/plugins/codec/libedummy_plugin.so
%{_libdir}/vlc/plugins/codec/librawvideo_plugin.so*
%{_libdir}/vlc/plugins/codec/libsubsusf_plugin.so
%{_libdir}/vlc/plugins/codec/libstl_plugin.so
%{_libdir}/vlc/plugins/codec/libsvcdsub_plugin.so*
%{_libdir}/vlc/plugins/codec/libt140_plugin.so
%{_libdir}/vlc/plugins/codec/libdts_plugin.so*
%{_libdir}/vlc/plugins/codec/liblpcm_plugin.so*
%{_libdir}/vlc/plugins/codec/liblibmpeg2_plugin.so*
%{_libdir}/vlc/plugins/codec/libmpeg_audio_plugin.so*
%{_libdir}/vlc/plugins/codec/libpng_plugin.so*
%{_libdir}/vlc/plugins/codec/libsubsdec_plugin.so*
%if %{with_x264}
%{_libdir}/vlc/plugins/codec/libx264_plugin.so*
%endif
%if %{with_x265}
%{_libdir}/vlc/plugins/codec/libx265_plugin.so*
%endif
%{_libdir}/vlc/plugins/codec/libspudec_plugin.so*
%{_libdir}/vlc/plugins/codec/libdvbsub_plugin.so*
%if %{with_faad}
%{_libdir}/vlc/plugins/codec/libfaad_plugin.so*
%endif
%{_libdir}/vlc/plugins/codec/libtelx_plugin.so
%{_libdir}/vlc/plugins/codec/libg711_plugin.so
%{_libdir}/vlc/plugins/codec/libscte27_plugin.so
%{_libdir}/vlc/plugins/codec/libuleaddvaudio_plugin.so
%{_libdir}/vlc/plugins/codec/libxwd_plugin.so
%{_libdir}/vlc/plugins/codec/libgstdecode_plugin.so
%{_libdir}/vlc/plugins/codec/libhwdummy_plugin.so
%{_libdir}/vlc/plugins/codec/libjpeg_plugin.so
%{_libdir}/vlc/plugins/codec/libsubstx3g_plugin.so
%{_libdir}/vlc/plugins/codec/libsvgdec_plugin.so
%{_libdir}/vlc/plugins/codec/libvaapi_drm_plugin.so
%{_libdir}/vlc/plugins/codec/libvaapi_x11_plugin.so
%{_libdir}/vlc/plugins/codec/libvpx_plugin.so

%dir %{_libdir}/vlc/plugins/control
%{_libdir}/vlc/plugins/control/libdbus_plugin.so
%{_libdir}/vlc/plugins/control/libdummy_plugin.so
%{_libdir}/vlc/plugins/control/libhotkeys_plugin.so*
%{_libdir}/vlc/plugins/control/libmotion_plugin.so
%{_libdir}/vlc/plugins/control/libnetsync_plugin.so
%{_libdir}/vlc/plugins/control/liboldrc_plugin.so*
%{_libdir}/vlc/plugins/control/libgestures_plugin.so*
%{_libdir}/vlc/plugins/control/libxcb_hotkeys_plugin.so

%dir %{_libdir}/vlc/plugins/demux
%{_libdir}/vlc/plugins/demux/libaiff_plugin.so*
%{_libdir}/vlc/plugins/demux/libasf_plugin.so*
%{_libdir}/vlc/plugins/demux/libau_plugin.so*
%{_libdir}/vlc/plugins/demux/libavformat_plugin.so
%{_libdir}/vlc/plugins/demux/libavi_plugin.so*
%{_libdir}/vlc/plugins/demux/libdemux_cdg_plugin.so
%{_libdir}/vlc/plugins/demux/libdemux_stl_plugin.so
%{_libdir}/vlc/plugins/demux/libdemuxdump_plugin.so*
%{_libdir}/vlc/plugins/demux/libes_plugin.so
%{_libdir}/vlc/plugins/demux/libh264_plugin.so*
%{_libdir}/vlc/plugins/demux/libimage_plugin.so
%{_libdir}/vlc/plugins/demux/libmjpeg_plugin.so*
%{_libdir}/vlc/plugins/demux/libmkv_plugin.so
%{_libdir}/vlc/plugins/demux/libmp4_plugin.so*
%{_libdir}/vlc/plugins/demux/libmpgv_plugin.so*
%{_libdir}/vlc/plugins/demux/libnsc_plugin.so*
%{_libdir}/vlc/plugins/demux/libnsv_plugin.so*
%{_libdir}/vlc/plugins/demux/libnuv_plugin.so*
%{_libdir}/vlc/plugins/demux/libplaylist_plugin.so*
%{_libdir}/vlc/plugins/demux/libps_plugin.so*
%{_libdir}/vlc/plugins/demux/libpva_plugin.so*
%{_libdir}/vlc/plugins/demux/librawaud_plugin.so
%{_libdir}/vlc/plugins/demux/librawdv_plugin.so*
%{_libdir}/vlc/plugins/demux/librawvid_plugin.so
%{_libdir}/vlc/plugins/demux/libreal_plugin.so*
%{_libdir}/vlc/plugins/demux/libsmf_plugin.so
%{_libdir}/vlc/plugins/demux/libsubtitle_plugin.so*
%{_libdir}/vlc/plugins/demux/libtta_plugin.so
%{_libdir}/vlc/plugins/demux/libty_plugin.so*
%{_libdir}/vlc/plugins/demux/libvobsub_plugin.so*
%{_libdir}/vlc/plugins/demux/libvc1_plugin.so
%{_libdir}/vlc/plugins/demux/libvoc_plugin.so*
%{_libdir}/vlc/plugins/demux/libwav_plugin.so*
%if %{with_dvbpsi}
%{_libdir}/vlc/plugins/demux/libts_plugin.so*
%endif
%{_libdir}/vlc/plugins/demux/libxa_plugin.so*
%if %{with_ogg}
%{_libdir}/vlc/plugins/demux/libogg_plugin.so*
%{_libdir}/vlc/plugins/codec/libvorbis_plugin.so*
%endif
%{_libdir}/vlc/plugins/demux/libcaf_plugin.so
%{_libdir}/vlc/plugins/demux/libdiracsys_plugin.so
%{_libdir}/vlc/plugins/demux/libhevc_plugin.so
%if %{with_satellite}
%{_libdir}/vlc/plugins/access/libsatellite_plugin.so*
%endif
%dir %{_libdir}/vlc/plugins/meta_engine
%{_libdir}/vlc/plugins/meta_engine/libfolder_plugin.so
%if %{with_taglib}
%{_libdir}/vlc/plugins/meta_engine/libtaglib_plugin.so
%endif
%dir %{_libdir}/vlc/plugins/misc
%{_libdir}/vlc/plugins/misc/libaudioscrobbler_plugin.so
%{_libdir}/vlc/plugins/misc/libexport_plugin.so*
%{_libdir}/vlc/plugins/misc/liblogger_plugin.so*
%{_libdir}/vlc/plugins/misc/libstats_plugin.so
%{_libdir}/vlc/plugins/misc/libvod_rtsp_plugin.so*
%{_libdir}/vlc/plugins/misc/libxdg_screensaver_plugin.so*
%{_libdir}/vlc/plugins/misc/libfingerprinter_plugin.so
%if %{with_xml}
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
%if %{with_ogg}
%{_libdir}/vlc/plugins/mux/libmux_ogg_plugin.so*
%endif
%{_libdir}/vlc/plugins/mux/libmux_ps_plugin.so*
%{_libdir}/vlc/plugins/mux/libmux_ts_plugin.so
%{_libdir}/vlc/plugins/mux/libmux_wav_plugin.so*
%dir %{_libdir}/vlc/plugins/gui/
%if %{with_qt4}
%{_libdir}/vlc/plugins/gui/libqt4_plugin.so
%endif
%if %{with_qt5}
%{_libdir}/vlc/plugins/gui/libqt4_plugin.so
%endif
%dir %{_libdir}/vlc/plugins/packetizer
%{_libdir}/vlc/plugins/packetizer/libpacketizer_copy_plugin.so*
%{_libdir}/vlc/plugins/packetizer/libpacketizer_dirac_plugin.so
%{_libdir}/vlc/plugins/packetizer/libpacketizer_flac_plugin.so
%{_libdir}/vlc/plugins/packetizer/libpacketizer_h264_plugin.so*
%{_libdir}/vlc/plugins/packetizer/libpacketizer_mlp_plugin.so
%{_libdir}/vlc/plugins/packetizer/libpacketizer_mpeg4audio_plugin.so*
%{_libdir}/vlc/plugins/packetizer/libpacketizer_mpeg4video_plugin.so*
%{_libdir}/vlc/plugins/packetizer/libpacketizer_mpegvideo_plugin.so*
%{_libdir}/vlc/plugins/packetizer/libpacketizer_vc1_plugin.so
%{_libdir}/vlc/plugins/packetizer/libpacketizer_avparser_plugin.so
%{_libdir}/vlc/plugins/packetizer/libpacketizer_hevc_plugin.so

%{_libdir}/vlc/plugins/vdpau
%{_libdir}/vlc/plugins/video_splitter

%dir %{_libdir}/vlc/plugins/services_discovery/
%{_libdir}/vlc/plugins/services_discovery/libmediadirs_plugin.so
%{_libdir}/vlc/plugins/services_discovery/libpodcast_plugin.so*
%{_libdir}/vlc/plugins/services_discovery/libsap_plugin.so*
%if %{with_udev}
%{_libdir}/vlc/plugins/services_discovery/libudev_plugin.so*
%endif
%{_libdir}/vlc/plugins/services_discovery/libxcb_apps_plugin.so

%dir %{_libdir}/vlc/plugins/stream_filter/
%{_libdir}/vlc/plugins/stream_filter/libdecomp_plugin.so
%{_libdir}/vlc/plugins/stream_filter/libdash_plugin.so
%{_libdir}/vlc/plugins/stream_filter/libhttplive_plugin.so
%{_libdir}/vlc/plugins/stream_filter/librecord_plugin.so
%{_libdir}/vlc/plugins/stream_filter/libsmooth_plugin.so

%dir %{_libdir}/vlc/plugins/stream_out
%{_libdir}/vlc/plugins/stream_out/libstream_out_autodel_plugin.so
%{_libdir}/vlc/plugins/stream_out/libstream_out_bridge_plugin.so*
%{_libdir}/vlc/plugins/stream_out/libstream_out_delay_plugin.so
%{_libdir}/vlc/plugins/stream_out/libstream_out_description_plugin.so*
%{_libdir}/vlc/plugins/stream_out/libstream_out_display_plugin.so*
%{_libdir}/vlc/plugins/stream_out/libstream_out_dummy_plugin.so*
%{_libdir}/vlc/plugins/stream_out/libstream_out_duplicate_plugin.so*
%{_libdir}/vlc/plugins/stream_out/libstream_out_es_plugin.so*
%{_libdir}/vlc/plugins/stream_out/libstream_out_gather_plugin.so*
%{_libdir}/vlc/plugins/stream_out/libstream_out_langfromtelx_plugin.so
%{_libdir}/vlc/plugins/stream_out/libstream_out_mosaic_bridge_plugin.so*
%{_libdir}/vlc/plugins/stream_out/libstream_out_raop_plugin.so
%{_libdir}/vlc/plugins/stream_out/libstream_out_record_plugin.so
%{_libdir}/vlc/plugins/stream_out/libstream_out_rtp_plugin.so*
%{_libdir}/vlc/plugins/stream_out/libstream_out_stats_plugin.so
%{_libdir}/vlc/plugins/stream_out/libstream_out_setid_plugin.so
%{_libdir}/vlc/plugins/stream_out/libstream_out_smem_plugin.so*
%{_libdir}/vlc/plugins/stream_out/libstream_out_standard_plugin.so*
%{_libdir}/vlc/plugins/stream_out/libstream_out_transcode_plugin.so*
%{_libdir}/vlc/plugins/stream_out/libstream_out_chromaprint_plugin.so
%dir %{_libdir}/vlc/plugins/text_renderer
%{_libdir}/vlc/plugins/text_renderer/libfreetype_plugin.so*
%{_libdir}/vlc/plugins/text_renderer/libsvg_plugin.so
%{_libdir}/vlc/plugins/text_renderer/libtdummy_plugin.so

%dir %{_libdir}/vlc/plugins/video_chroma
%{_libdir}/vlc/plugins/video_chroma/libgrey_yuv_plugin.so
%{_libdir}/vlc/plugins/video_chroma/libi420_rgb_*plugin.so*
%{_libdir}/vlc/plugins/video_chroma/libi420_yuy2_*plugin.so*
%{_libdir}/vlc/plugins/video_chroma/libi422_i420_plugin.so
%{_libdir}/vlc/plugins/video_chroma/libi422_yuy2_*plugin.so*
%{_libdir}/vlc/plugins/video_chroma/librv32_plugin.so
%{_libdir}/vlc/plugins/video_chroma/libyuy2_i420_plugin.so
%{_libdir}/vlc/plugins/video_chroma/libyuy2_i422_plugin.so
%{_libdir}/vlc/plugins/video_chroma/libswscale_plugin.so
%{_libdir}/vlc/plugins/video_chroma/libchain_plugin.so

%dir %{_libdir}/vlc/plugins/video_filter
%{_libdir}/vlc/plugins/video_filter/libadjust_plugin.so*
%{_libdir}/vlc/plugins/video_filter/libalphamask_plugin.so
%{_libdir}/vlc/plugins/video_filter/libantiflicker_plugin.so
%{_libdir}/vlc/plugins/video_filter/libaudiobargraph_v_plugin.so
%{_libdir}/vlc/plugins/video_filter/libatmo_plugin.so
%{_libdir}/vlc/plugins/video_filter/libball_plugin.so
%{_libdir}/vlc/plugins/video_filter/libblendbench_plugin.so
%{_libdir}/vlc/plugins/video_filter/libblend_plugin.so*
%{_libdir}/vlc/plugins/video_filter/libbluescreen_plugin.so
%{_libdir}/vlc/plugins/video_filter/libcanvas_plugin.so
%{_libdir}/vlc/plugins/video_filter/libcolorthres_plugin.so
%{_libdir}/vlc/plugins/video_filter/libcroppadd_plugin.so
%{_libdir}/vlc/plugins/video_filter/libdeinterlace_plugin.so*
%{_libdir}/vlc/plugins/video_filter/libdynamicoverlay_plugin.so
%{_libdir}/vlc/plugins/video_filter/liberase_plugin.so
%{_libdir}/vlc/plugins/video_filter/libextract_plugin.so
%{_libdir}/vlc/plugins/video_filter/libgaussianblur_plugin.so
%{_libdir}/vlc/plugins/video_filter/libgradient_plugin.so
%{_libdir}/vlc/plugins/video_filter/libgradfun_plugin.so
%{_libdir}/vlc/plugins/video_filter/libgrain_plugin.so
%{_libdir}/vlc/plugins/video_filter/libhqdn3d_plugin.so
%{_libdir}/vlc/plugins/video_filter/libinvert_plugin.so*
%{_libdir}/vlc/plugins/video_filter/liblogo_plugin.so*
%{_libdir}/vlc/plugins/video_filter/libmagnify_plugin.so*
%{_libdir}/vlc/plugins/video_filter/libmarq_plugin.so*
%{_libdir}/vlc/plugins/video_filter/libmirror_plugin.so
%{_libdir}/vlc/plugins/video_filter/libmosaic_plugin.so*
%{_libdir}/vlc/plugins/video_filter/libmotionblur_plugin.so*
%{_libdir}/vlc/plugins/video_filter/libmotiondetect_plugin.so*
%{_libdir}/vlc/plugins/video_filter/libposterize_plugin.so
%{_libdir}/vlc/plugins/video_filter/libpostproc_plugin.so
%{_libdir}/vlc/plugins/video_filter/libpsychedelic_plugin.so
%{_libdir}/vlc/plugins/video_filter/libpuzzle_plugin.so
%{_libdir}/vlc/plugins/video_filter/libremoteosd_plugin.so
%{_libdir}/vlc/plugins/video_filter/libripple_plugin.so
%{_libdir}/vlc/plugins/video_filter/librotate_plugin.so
%{_libdir}/vlc/plugins/video_filter/librss_plugin.so*
%{_libdir}/vlc/plugins/video_filter/libscale_plugin.so*
%{_libdir}/vlc/plugins/video_filter/libscene_plugin.so
%{_libdir}/vlc/plugins/video_filter/libsepia_plugin.so
%{_libdir}/vlc/plugins/video_filter/libsharpen_plugin.so
%{_libdir}/vlc/plugins/video_filter/libsubsdelay_plugin.so
%{_libdir}/vlc/plugins/video_filter/libtransform_plugin.so*
%{_libdir}/vlc/plugins/video_filter/libwave_plugin.so
%{_libdir}/vlc/plugins/video_filter/libyuvp_plugin.so
%{_libdir}/vlc/plugins/video_filter/libanaglyph_plugin.so
%{_libdir}/vlc/plugins/video_filter/libopencv_example_plugin.so
%{_libdir}/vlc/plugins/video_filter/libopencv_wrapper_plugin.so
%{_libdir}/vlc/plugins/video_filter/libfreeze_plugin.so
%{_libdir}/vlc/plugins/video_filter/liboldmovie_plugin.so
%{_libdir}/vlc/plugins/video_filter/libvhs_plugin.so

%dir %{_libdir}/vlc/plugins/video_output
%{_libdir}/vlc/plugins/video_output/libcaca_plugin.so
%{_libdir}/vlc/plugins/video_output/libegl_x11_plugin.so*
%{_libdir}/vlc/plugins/video_output/libfb_plugin.so*
%{_libdir}/vlc/plugins/video_output/libvmem_plugin.so
%{_libdir}/vlc/plugins/video_output/libyuv_plugin.so
%{_libdir}/vlc/plugins/video_output/libvdummy_plugin.so
%{_libdir}/vlc/plugins/video_output/libxcb_x11_plugin.so*
%{_libdir}/vlc/plugins/video_output/libxcb_window_plugin.so*
%if %{with_xvideo}
%{_libdir}/vlc/plugins/video_output/libxcb_xv_plugin.so*
%endif
%{_libdir}/vlc/plugins/video_output/libgl_plugin.so
%{_libdir}/vlc/plugins/video_output/libglx_plugin.so

%dir %{_libdir}/vlc/plugins/visualization
%{_libdir}/vlc/plugins/visualization/libvisual_plugin.so*
%{_libdir}/vlc/plugins/visualization/libglspectrum_plugin.so*
%if %{with_alsa}
%{_libdir}/vlc/plugins/access/libaccess_alsa_plugin.so
%{_libdir}/vlc/plugins/audio_output/libalsa_plugin.so*
%endif
%{_mandir}/man1/vlc.*
%{_mandir}/man1/vlc-wrapper.1*
%{_datadir}/applications/vlc.desktop
%{_miconsdir}/vlc.png
%{_iconsdir}/vlc.png
%{_liconsdir}/vlc.png
%{_iconsdir}/hicolor/*/apps/*
%if %{with_kde}
%{_datadir}/apps/solid/actions/*.desktop
%endif

%files -n %{libname}
%{_libdir}/libvlc.so.%{libmajor}*

%files -n %{libnamecore}
%{_libdir}/libvlccore.so.%{coremajor}*

%files -n %{devname}
%doc README doc/release-howto.txt doc/skins
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

%if %{with_shout}
%files plugin-shout
%doc README
%{_libdir}/vlc/plugins/access_output/libaccess_output_shout_plugin.so
%endif

# intf plugins
%if %{with_svlc}
%files -n svlc
%doc README
%{_bindir}/svlc
%{_libdir}/vlc/plugins/gui/libskins2_plugin.so*
%{_datadir}/applications/mandriva-svlc.desktop
%{_datadir}/vlc/skins2
%endif

%if %{with_zvbi}
%files plugin-zvbi
%doc README
%{_libdir}/vlc/plugins/access/liblinsys_hdsdi_plugin.so
%{_libdir}/vlc/plugins/access/liblinsys_sdi_plugin.so
%{_libdir}/vlc/plugins/codec/libzvbi_plugin.so
%endif

%if %{with_kate}
%files plugin-kate
%doc README
%{_libdir}/vlc/plugins/codec/libkate_plugin.so
%endif

%if %{with_ass}
%files plugin-libass
%doc README
%{_libdir}/vlc/plugins/codec/liblibass_plugin.so
%endif

%if %{with_lua}
%files plugin-lua
%doc README
%{_libdir}/vlc/plugins/lua/liblua_plugin.so
%{_libdir}/vlc/lua
%{_datadir}/vlc/lua
%{_bindir}/rvlc
%endif

%if %{with_ncurses}
%files plugin-ncurses
%doc README
%{_bindir}/nvlc
%{_libdir}/vlc/plugins/gui/libncurses_plugin.so*
%endif

%if %{with_lirc}
%files plugin-lirc
%doc README
%{_libdir}/vlc/plugins/control/liblirc_plugin.so*
%endif

# video plugins
%if %{with_sdl}
%files plugin-sdl
%doc README
%if %{with_sdl_image}
%{_libdir}/vlc/plugins/codec/libsdl_image_plugin.so*
%endif
%{_libdir}/vlc/plugins/video_output/libvout_sdl_plugin.so*
%endif

%files plugin-opengl
%doc README
%{_libdir}/vlc/plugins/video_output/libxcb_glx_plugin.so*

%if %{with_aa}
%files plugin-aa
%doc README
%{_libdir}/vlc/plugins/video_output/libaa_plugin.so*
%endif

%if %{with_goom}
%files plugin-goom
%doc README
%{_libdir}/vlc/plugins/visualization/libgoom_plugin.so
%endif

%if %{with_projectm}
%files plugin-projectm
%doc README
%{_libdir}/vlc/plugins/visualization/libprojectm_plugin.so
%endif

%if %{with_theora}
%files plugin-theora
%doc README
%{_libdir}/vlc/plugins/codec/libtheora_plugin.so
%endif

%if %{with_fluidsynth}
%files plugin-fluidsynth
%doc README
%{_libdir}/vlc/plugins/codec/libfluidsynth_plugin.so
%endif

%if %{with_gme}
%files plugin-gme
%doc README
%{_libdir}/vlc/plugins/demux/libgme_plugin.so
%endif

%if %{with_schroedinger}
%files plugin-schroedinger
%doc README
%{_libdir}/vlc/plugins/codec/libschroedinger_plugin.so
%endif

%if %{with_twolame}
%files plugin-twolame
%doc README
%{_libdir}/vlc/plugins/codec/libtwolame_plugin.so*
%endif

%if %{with_speex}
%files plugin-speex
%doc README
%{_libdir}/vlc/plugins/audio_filter/libspeex_resampler_plugin.so
%{_libdir}/vlc/plugins/codec/libspeex_plugin.so*
%endif

%files plugin-flac
%doc README
%{_libdir}/vlc/plugins/demux/libflacsys_plugin.so
%{_libdir}/vlc/plugins/codec/libflac_plugin.so*

%files plugin-opus
%{_libdir}/vlc/plugins/codec/libopus_plugin.so*

%if %{with_dv}
%files plugin-dv
%doc README
%{_libdir}/vlc/plugins/access/libdc1394_plugin.so
%endif

%if %{with_mod}
%files plugin-mod
%doc README
%{_libdir}/vlc/plugins/demux/libmod_plugin.so*
%endif

%if %{with_mpc}
%files plugin-mpc
%doc README
%{_libdir}/vlc/plugins/demux/libmpc_plugin.so*
%endif

#audio plugins
%if %{with_pulse}
%files plugin-pulse
%doc README
%{_libdir}/vlc/plugins/access/libpulsesrc_plugin.so
%{_libdir}/vlc/plugins/audio_output/libpulse_plugin.so*
%{_libdir}/vlc/plugins/services_discovery/libpulselist_plugin.so
%endif

%if %{with_jack}
%files plugin-jack
%doc README
%{_libdir}/vlc/plugins/access/libaccess_jack_plugin.so
%{_libdir}/vlc/plugins/audio_output/libjack_plugin.so*
%endif

%if %{with_bonjour}
%files plugin-bonjour
%doc README
%{_libdir}/vlc/plugins/services_discovery/libbonjour_plugin.so*
%endif

%if %{with_upnp}
%files plugin-upnp
%doc README
%{_libdir}/vlc/plugins/services_discovery/libupnp_plugin.so*
%endif

%if %{with_gnutls}
%files plugin-gnutls
%doc README
%{_libdir}/vlc/plugins/misc/libgnutls_plugin.so*
%endif

%files plugin-libnotify
%doc README
%{_libdir}/vlc/plugins/notify/libnotify_plugin.so*

