Name:           backup_app
Version:        1.0
Release:        1%{?dist}
Summary:        Program for backup.

License:
URL:            https://github.com/Hojang2/Backup_app_teamwork
Source0:        %{name}-%{version}.tar.gz
BuildArch: 	noarch

BuildRequires:

Requires:       python3-gzip
Requires:	python3-os
Requires:	python3-time
Requires:	python3-sys
Requires:	python3-argparse
Requires:	python3-PyQt5


%description
Program for backing up your files, compressing them and
then restoring them in the target directory.
There is CLI a GUI avalible. This program was created
as part of school teamwork.

%prep
%autosetup


%build
%configure
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%license add-license-file-here
%doc add-docs-here



%changelog
* Thu Jun  6 2019 Jan Buchmaier <janbuchmaier@seznam.cz>
- Created main program structure. Added main functions for backup and restore.
