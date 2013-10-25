### RPM external libtool 1.5.22
Source: http://mirror.switch.ch/ftp/mirror/gnu/%n/%n-%realversion.tar.gz

%prep
%setup -n %n-%{realversion}
 
%build
./configure --prefix=%{i} --enable-static=no
make %makeprocesses

%install
make install

