Name:           micro
Version:        2.0.13
Release:        2%{?dist}
Summary:        A modern and intuitive terminal-based text editor

License:        MIT and ASL 2.0
URL:            https://github.com/zyedidia/micro

Source0:        https://github.com/zyedidia/micro/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  golang
BuildRequires:  systemd-rpm-macros
BuildRequires:  git

Provides:       %{name} = %{version}

%global debug_package %{nil}
%global compiledate     January\ 28,\ 2024
%global shortcommit     68d88b5

%description
micro is a terminal-based text editor that aims to be easy to use and intuitive, while also taking advantage of the capabilities of modern terminals. It comes as a single, batteries-included, static binary with no dependencies; you can download and use it right now!

As its name indicates, micro aims to be somewhat of a successor to the nano editor by being easy to install and use. It strives to be enjoyable as a full-time editor for people who prefer to work in a terminal, or those who regularly edit files over SSH.

%prep
%autosetup
sed -i "s|github.com/zyedidia/json5|github.com/flynn/json5|" $(find . -name "*.go")
# %autosetup

%build	
make build VERSION=%{version} HASH=%{shortcommit}

%install
rm -rf $RPM_BUILD_ROOT
install -m 0755 -vd                %{buildroot}%{_bindir}
install -m 0755 -vp micro 		     %{buildroot}%{_bindir}/

%check
 
%files
%license LICENSE LICENSE-THIRD-PARTY
%doc README.md
%{_bindir}/*
 
%changelog
* Sun Jan 28 2024 Danie de Jager - 2.0.13-2
- Fixed version and commit hash output.
* Sat Jan 27 2024 Danie de Jager - 2.0.13-1
- SPEC to build on AL2023.
