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
Requires(pre):	texlive-tlpkg
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

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/doc/latex/amscls-doc
%doc %{_datadir}/texmf-dist/doc/latex/amscls-doc/AH_Bibliography.tex
%doc %{_datadir}/texmf-dist/doc/latex/amscls-doc/Author_Handbook_Body.tex
%doc %{_datadir}/texmf-dist/doc/latex/amscls-doc/Author_Handbook_Journals.pdf
%doc %{_datadir}/texmf-dist/doc/latex/amscls-doc/Author_Handbook_Journals.tex
%doc %{_datadir}/texmf-dist/doc/latex/amscls-doc/Author_Handbook_Memo.pdf
%doc %{_datadir}/texmf-dist/doc/latex/amscls-doc/Author_Handbook_Memo.tex
%doc %{_datadir}/texmf-dist/doc/latex/amscls-doc/Author_Handbook_Mono.pdf
%doc %{_datadir}/texmf-dist/doc/latex/amscls-doc/Author_Handbook_Mono.tex
%doc %{_datadir}/texmf-dist/doc/latex/amscls-doc/Author_Handbook_ProcColl.pdf
%doc %{_datadir}/texmf-dist/doc/latex/amscls-doc/Author_Handbook_ProcColl.tex
%doc %{_datadir}/texmf-dist/doc/latex/amscls-doc/Color2Gray.eps
%doc %{_datadir}/texmf-dist/doc/latex/amscls-doc/Color2Gray.pdf
%doc %{_datadir}/texmf-dist/doc/latex/amscls-doc/Graphics_Guidelines.tex
%doc %{_datadir}/texmf-dist/doc/latex/amscls-doc/J-Checklist.tex
%doc %{_datadir}/texmf-dist/doc/latex/amscls-doc/J-Series.tex
%doc %{_datadir}/texmf-dist/doc/latex/amscls-doc/M-Checklist.tex
%doc %{_datadir}/texmf-dist/doc/latex/amscls-doc/M-Series.tex
%doc %{_datadir}/texmf-dist/doc/latex/amscls-doc/Mem-Checklist.tex
%doc %{_datadir}/texmf-dist/doc/latex/amscls-doc/PC-Checklist.tex
%doc %{_datadir}/texmf-dist/doc/latex/amscls-doc/PC-Series.tex
%doc %{_datadir}/texmf-dist/doc/latex/amscls-doc/README-AH.txt
%doc %{_datadir}/texmf-dist/doc/latex/amscls-doc/ResourcesHelp.tex
%doc %{_datadir}/texmf-dist/doc/latex/amscls-doc/Submitting2AMS.tex
%doc %{_datadir}/texmf-dist/doc/latex/amscls-doc/TopMatterTags_J.tex
%doc %{_datadir}/texmf-dist/doc/latex/amscls-doc/TopMatterTags_M.tex
%doc %{_datadir}/texmf-dist/doc/latex/amscls-doc/TopMatterTags_Mem.tex
%doc %{_datadir}/texmf-dist/doc/latex/amscls-doc/TopMatterTags_PC.tex
%doc %{_datadir}/texmf-dist/doc/latex/amscls-doc/ahandinstr-r.sty
%doc %{_datadir}/texmf-dist/doc/latex/amscls-doc/ams-author-handbook-doc.pdf
%doc %{_datadir}/texmf-dist/doc/latex/amscls-doc/ams-author-handbook-doc.tex
%doc %{_datadir}/texmf-dist/doc/latex/amscls-doc/gamuts.eps
%doc %{_datadir}/texmf-dist/doc/latex/amscls-doc/gamuts.pdf
%doc %{_datadir}/texmf-dist/doc/latex/amscls-doc/manifest.txt
%doc %{_datadir}/texmf-dist/doc/latex/amscls-doc/rgb-cmyk.eps
%doc %{_datadir}/texmf-dist/doc/latex/amscls-doc/rgb-cmyk.pdf
%doc %{_datadir}/texmf-dist/doc/latex/amscls-doc/spectrum.eps
%doc %{_datadir}/texmf-dist/doc/latex/amscls-doc/spectrum.pdf
