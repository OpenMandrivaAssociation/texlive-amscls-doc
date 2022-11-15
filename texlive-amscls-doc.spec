Name:		texlive-amscls-doc
Version:	46110
Release:	1
Summary:	User documentation for AMS document classes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/amscls-doc
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amscls-doc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amscls-doc.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This collection comprises a set of four manuals, or Author
Handbooks, each documenting the use of a class of publications
based on one of the AMS document classes amsart, amsbook,
amsproc and one "hybrid", as well as a guide to the generation
of the four manuals from a coordinated set of LaTeX source
files. The Handbooks comprise the user documentation for the
pertinent document classes. As the source for the Handbooks
consists of a large number of files, and the intended output is
multiple different documents, the principles underlying this
collection can be used as a model for similar projects. The
manual "Compiling the AMS Author Handbooks" provides
information about the structure of and interaction between the
various components.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/latex/amscls-doc

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
