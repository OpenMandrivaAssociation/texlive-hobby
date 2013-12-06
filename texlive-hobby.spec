# revision 29895
# category Package
# catalog-ctan /graphics/pgf/contrib/hobby
# catalog-date 2013-04-15 11:53:39 +0200
# catalog-license lppl1.3
# catalog-version 1.2
Name:		texlive-hobby
Version:	1.2
Release:	5
Summary:	An implementation of Hobby's algorithm for PGF/TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/hobby
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hobby.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hobby.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hobby.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package defines a path generation function for PGF/TikZ
which implements Hobby's algorithm for a path built out of
Bezier curves which passes through a given set of points. The
path thus generated may by used as a TikZ 'to path'. The
implementation is in LaTeX3.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/hobby/hobby.code.tex
%{_texmfdistdir}/tex/latex/hobby/pgflibraryhobby.code.tex
%{_texmfdistdir}/tex/latex/hobby/pml3array.sty
%{_texmfdistdir}/tex/latex/hobby/tikzlibraryhobby.code.tex
%doc %{_texmfdistdir}/doc/latex/hobby/README.txt
%doc %{_texmfdistdir}/doc/latex/hobby/hobby_doc.pdf
%doc %{_texmfdistdir}/doc/latex/hobby/hobby_doc.tex
#- source
%doc %{_texmfdistdir}/source/latex/hobby/hobby.dtx
%doc %{_texmfdistdir}/source/latex/hobby/hobby.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
