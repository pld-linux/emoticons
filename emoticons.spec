#
Summary:	EmotIcons
Name:		emoticons
Version:	0.1
Release:	0.1
License:	GPL ?
Group:		Applications/Communications
Source0:	%{name}-gg-031212.tgz
URL:		http://www.gadu.gnu.pl/
BuildRequires:	ImageMagick-coder-png
BuildRequires:	iconv
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EmoteIcons

%package -n emoticons-kopete-gg
Summary:	Gadu-Gadu emoticons for kopete
Group:		X11/Applications/Networking
Requires:	kdenetwork-kopete

%description -n emoticons-kopete-gg
Gadu-Gadu emoticons for kopete

%prep
%setup -Tcqn %{name} -a0

%build
gcc -o conv conv.c

rm -rf out; mkdir out
# oryginal emots/2/emots.txt have some errors :(
cat emots/2/emots.txt | \
    sed 's/<soczek>,/<soczek>"/' | \
    sed 's:("<marzyciel>","oczy.gif"):"<marzyciel>","oczy.gif":' \
    > emots/2/emotsnew.txt
rm -f emots/2/emots.txt

FILES=`find emots -type f -iname "*.txt"`
cat $FILES > emots.txt

echo -e -n "<?xml version=\"1.0\"?>\n<messaging-emoticon-map>\n\n" > emoticons.xml.tmp
./conv emots.txt >> emoticons.xml.tmp
echo -e -n "</messaging-emoticon-map>\n" >> emoticons.xml.tmp

cat emoticons.xml.tmp | iconv -f cp1250 -t utf-8 > out/emoticons.xml
FILES=`find emots -type f -iname "*.gif"`
for FILE in $FILES
do
    F=`basename $FILE | tr '[:upper:]' '[:lower:]'`
    cp $FILE out/$F
done
convert out/wesoly_na.gif out/smile.png
rm -f out/*_na.*

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/apps/kopete/pics/emoticons/Gadu-Gadu/
cp out/* $RPM_BUILD_ROOT%{_datadir}/apps/kopete/pics/emoticons/Gadu-Gadu/

%clean
rm -rf $RPM_BUILD_ROOT

%files -n emoticons-kopete-gg
%defattr(644,root,root,755)
%{_datadir}/apps/kopete/pics/emoticons/Gadu-Gadu/*
