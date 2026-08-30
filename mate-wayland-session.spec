Name:           mate-wayland-session
Version:        1.28.6
Release:        1
Summary:        Wayland session using wayfire for the MATE desktop
License:        GPL-2.0-or-later
Group:          Graphical desktop/Other
URL:            https://mate-desktop.org/
Source:         https://github.com/mate-desktop/mate-wayland-session/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildArch:      noarch

Recommends:  wayfire

%description
Wayland session using wayfire for the MATE desktop.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}


%files -f %{name}.lang
%doc README.md NEWS
%license LICENSE
%{_bindir}/mate-wayland*
%{_datadir}/firedecor
%{_datadir}/glib-2.0/schemas/10_mate-wayland.gschema.override
%dir %{_datadir}/wayland-sessions
%{_datadir}/wayland-sessions/MATE.desktop
