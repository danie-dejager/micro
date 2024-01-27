Name:           micro
Version:        2.0.13
Release:        1%{?dist}
Summary:        A modern and intuitive terminal-based text editor

License:        MIT and ASL 2.0
URL:            https://github.com/zyedidia/micro

Source0:        https://github.com/zyedidia/micro/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  golang
BuildRequires:  systemd-rpm-macros
BuildRequires:  git

Provides:       %{name} = %{version}

%description
micro is a terminal-based text editor that aims to be easy to use and intuitive, while also taking advantage of the capabilities of modern terminals. It comes as a single, batteries-included, static binary with no dependencies; you can download and use it right now!

As its name indicates, micro aims to be somewhat of a successor to the nano editor by being easy to install and use. It strives to be enjoyable as a full-time editor for people who prefer to work in a terminal, or those who regularly edit files over SSH.

%global debug_package %{nil}

%prep
%autosetup
sed -i "s|github.com/zyedidia/json5|github.com/flynn/json5|" $(find . -name "*.go")
# %autosetup

%build
export LDFLAGS="-X 'github.com/zyedidia/micro/internal/util.Version=%{version}' \
                -X 'github.com/zyedidia/micro/internal/util.CommitHash=%{shortcommit}' \
                -X 'github.com/zyedidia/micro/internal/util.CompileDate=%{compiledate}' \
                -X 'github.com/zyedidia/micro/internal/util.Debug=OFF'"
                
make build

%install
rm -rf $RPM_BUILD_ROOT
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp micro %{buildroot}%{_bindir}/

%check
 
%files
%license LICENSE LICENSE-THIRD-PARTY
%doc README.md
%{_bindir}/*
 
%changelog
* Sat Jan 27 2024 Danie de Jager - 2.0.13-1
- SPEC to build on AL2023.
