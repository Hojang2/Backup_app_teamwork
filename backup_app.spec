Name:           backup_app
Version:        1.0
Release:        1%{?dist}
Summary:        Program for backup.

License:	GPLv3+
URL:            https://github.com/Hojang2/Backup_app_teamwork
Source0:        %{name}-%{version}.tar.gz
BuildArch: 	noarch


Requires:       python3
Requires:	bash

%description
Program for backing up your files, compressing them and
then restoring them in the target directory.
There is CLI a GUI avalible. This program was created
as part of school teamwork.

%prep
%setup -q


%build


%install
mkdir -p %{buildroot}/%{_bindir}/
install -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}

%files
%license LICENSE
%{_bindir}/%{name}



%changelog
* Thu Jun  6 2019 Jan Buchmaier <janbuchmaier@seznam.cz>
- Created main program structure. Added main functions for backup and restore.
