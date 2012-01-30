#######################################################
# This spec is based on Falticska Florin's work for MRB
#######################################################

Name:		gmediafinder
Version:	0.9.9.1
Release:	%mkrel 1
Summary:	Application to search, stream and/or download files from YouTube
License:	GPLv2
Group:		Video
URL:		http://gnomefiles.org/content/show.php/Gmediafinder?content=138588&PHPSESSID=9c909890a42ce1ac7a555efab2b34b83
Source0:	http://github.com/smolleyes/gmediafinder.git/gmediafinder-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	python-mechanize
BuildRequires:	python-setuptools
BuildRequires:	python-distutils-extra
BuildRequires:	intltool
Requires:	python-beautifulsoup
Requires:	python-html5lib
Requires:	gstreamer0.10-python
Requires:	gstreamer0.10-ffmpeg
Requires:	python-gdata
Requires:	pygtk2.0
Requires:	pygtk2.0-libglade
Requires:	python-mechanize
Requires:	ffmpeg
Requires:	python-xlib
Requires:	gstreamer0.10-tools
Requires:	gstreamer0.10-libvisual
Requires:	libvisual-plugins
Requires:	python-configobj

%description
Gmediafinder is a software to search stream an/or download files form YouTube
without Flash, Google and some mp3 search engines (you know the rules...).
It supports fullscreen mode, visualisation and uses the gstreamer engine
for YouTube. You can select prefered resolution and give the priority to
mp4 format for video searching! (and lower cpu usage compared to flv...).


%prep
%setup -q -n %{name}
%__chmod 644 CHANGELOG gpl-2.0.txt README VERSION

%build
%__python setup.py build

%install
%__rm -rf %{buildroot}

%__python setup.py install --root=%{buildroot}
%__cp data/img/throbber.png %{buildroot}%{_datadir}/%{name}/
%__sed -i s,"AudioVideo","AudioVideo;",g %{buildroot}%{_datadir}/applications/%{name}.desktop
%__chmod 644 %{buildroot}%{_datadir}/applications/%{name}.desktop
%__chmod 644 %{buildroot}%{_datadir}/%{name}/*.png
%__chmod 644 %{buildroot}%{_datadir}/%{name}/*/*

%find_lang %{name}

%clean
%__rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc CHANGELOG gpl-2.0.txt README VERSION
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{py_sitedir}/*/*
%{_datadir}/%{name}/*
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/pyshared/GmediaFinder/*

