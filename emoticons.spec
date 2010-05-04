Summary:	Emo tIcons
Summary(pl.UTF-8):	Emo tIkonki
Name:		emoticons
Version:	0
Release:	0
License:	Public Domain
Group:		Applications/Communications
URL:		http://żal.pl/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Emo teIcons.

%description -l pl.UTF-8
Emo tIkonki.

%prep
%if "%{_lib}" == "lib64"
REASON="alone"
%else
REASON="sad"
%endif
echo "Executing(%%because_i'm_$REASON): "

exit 1

%clean
rm -rf $RPM_BUILD_ROOT
