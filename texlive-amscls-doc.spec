%global tl_name amscls-doc
%global tl_revision 46110

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	User documentation for AMS document classes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/amscls-doc
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/amscls-doc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/amscls-doc.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This collection comprises a set of four manuals, or Author Handbooks,
each documenting the use of a class of publications based on one of the
AMS document classes amsart, amsbook, amsproc and one "hybrid", as well
as a guide to the generation of the four manuals from a coordinated set
of LaTeX source files. The Handbooks comprise the user documentation for
the pertinent document classes. As the source for the Handbooks consists
of a large number of files, and the intended output is multiple
different documents, the principles underlying this collection can be
used as a model for similar projects. The manual "Compiling the AMS
Author Handbooks" provides information about the structure of and
interaction between the various components.

