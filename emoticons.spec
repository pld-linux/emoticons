Summary:	EmotIcons
Summary(pl.UTF-8):	EmotIkonki
Name:		emoticons
Version:	0.1
Release:	0.1
License:	GPL (?)
Group:		Applications/Communications
Source0:	%{name}-gg-031212.tgz
# Source0-md5:	eb824103b01d2fb4bd376b0540ba176d
URL:		http://www.gadu.gnu.pl/
BuildRequires:	ImageMagick-coder-png
BuildRequires:	iconv
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EmoteIcons.

%description -l pl.UTF-8
EmotIkonki.

%package kopete-gg
Summary:	Gadu-Gadu emoticons for kopete
Summary(pl.UTF-8):	Emotikonki Gadu-Gadu dla kopete
Group:		X11/Applications/Networking
Requires:	kdenetwork-kopete

%description kopete-gg
Gadu-Gadu emoticons for kopete.

%description kopete-gg -l pl.UTF-8
Emotikonki Gadu-Gadu dla kopete.

%prep
%setup -qc

%build
%{__cc} %{rpmldflags} %{rpmcflags} -o conv conv.c

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
install -d $RPM_BUILD_ROOT%{_datadir}/apps/kopete/pics/emoticons/Gadu-Gadu

cp out/* $RPM_BUILD_ROOT%{_datadir}/apps/kopete/pics/emoticons/Gadu-Gadu

%clean
rm -rf $RPM_BUILD_ROOT

%files kopete-gg
%defattr(644,root,root,755)
%{_datadir}/apps/kopete/pics/emoticons/Gadu-Gadu
