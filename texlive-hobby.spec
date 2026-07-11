%global tl_name hobby
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.12
Release:	%{tl_revision}.1
Summary:	An implementation of Hobbys algorithm for PGF/TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/hobby
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hobby.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hobby.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hobby.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package defines a path generation function for PGF/TikZ which
implements Hobby's algorithm for a path built out of Bezier curves which
passes through a given set of points. The path thus generated may by
used as a TikZ 'to path'. The implementation is in LaTeX3.

