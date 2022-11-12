Name:		texlive-concmath
Version:	17219
Release:	1
Summary:	Concrete Math fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/concmath
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/concmath.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/concmath.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/concmath.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A LaTeX package and font definition files to access the
Concrete mathematics fonts, which were derived from Computer
Modern math fonts using parameters from Concrete Roman text
fonts.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/concmath/concmath.sty
%{_texmfdistdir}/tex/latex/concmath/omlccm.fd
%{_texmfdistdir}/tex/latex/concmath/omlccr.fd
%{_texmfdistdir}/tex/latex/concmath/omsccr.fd
%{_texmfdistdir}/tex/latex/concmath/omsccsy.fd
%{_texmfdistdir}/tex/latex/concmath/omxccex.fd
%{_texmfdistdir}/tex/latex/concmath/ot1ccr.fd
%{_texmfdistdir}/tex/latex/concmath/ucca.fd
%{_texmfdistdir}/tex/latex/concmath/uccb.fd
%doc %{_texmfdistdir}/doc/fonts/concmath/CATALOGUE
%doc %{_texmfdistdir}/doc/fonts/concmath/README
%doc %{_texmfdistdir}/doc/fonts/concmath/concmath.pdf
#- source
%doc %{_texmfdistdir}/source/latex/concmath/Makefile
%doc %{_texmfdistdir}/source/latex/concmath/concmath.dtx
%doc %{_texmfdistdir}/source/latex/concmath/concmath.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
