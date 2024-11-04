#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v3
# autospec commit: c1050fe
#
Name     : R-fstcore
Version  : 0.9.18
Release  : 17
URL      : https://cran.r-project.org/src/contrib/fstcore_0.9.18.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fstcore_0.9.18.tar.gz
Summary  : R Bindings to the 'Fstlib' Library
Group    : Development/Tools
License  : BSD-3-Clause MPL-2.0
Requires: R-fstcore-lib = %{version}-%{release}
Requires: R-fstcore-license = %{version}-%{release}
Requires: R-Rcpp
BuildRequires : R-Rcpp
BuildRequires : R-lintr
BuildRequires : buildreq-R
BuildRequires : pkgconfig(liblz4)
BuildRequires : pkgconfig(libzstd)

%description
'fst' format. The 'fst' format allows for random access of stored data and compression with the 'LZ4' and 'ZSTD'
    compressors.

%package lib
Summary: lib components for the R-fstcore package.
Group: Libraries
Requires: R-fstcore-license = %{version}-%{release}

%description lib
lib components for the R-fstcore package.


%package license
Summary: license components for the R-fstcore package.
Group: Default

%description license
license components for the R-fstcore package.


%prep
%setup -q -n fstcore
pushd ..
cp -a fstcore buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1701828999

%install
export SOURCE_DATE_EPOCH=1701828999
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-fstcore
cp %{_builddir}/fstcore/LICENSE %{buildroot}/usr/share/package-licenses/R-fstcore/9cf097120d3d9eea0e9790d7d44ae80e6231a35a || :
cp %{_builddir}/fstcore/src/fstlib/LICENSE %{buildroot}/usr/share/package-licenses/R-fstcore/9cf097120d3d9eea0e9790d7d44ae80e6231a35a || :
cp %{_builddir}/fstcore/src/fstlib/ZSTD/LICENSE %{buildroot}/usr/share/package-licenses/R-fstcore/e663fbf883f36aceb8a037739fe8bd2c7e55303a || :
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/fstcore/DESCRIPTION
/usr/lib64/R/library/fstcore/INDEX
/usr/lib64/R/library/fstcore/LICENSE
/usr/lib64/R/library/fstcore/Meta/Rd.rds
/usr/lib64/R/library/fstcore/Meta/features.rds
/usr/lib64/R/library/fstcore/Meta/hsearch.rds
/usr/lib64/R/library/fstcore/Meta/links.rds
/usr/lib64/R/library/fstcore/Meta/nsInfo.rds
/usr/lib64/R/library/fstcore/Meta/package.rds
/usr/lib64/R/library/fstcore/NAMESPACE
/usr/lib64/R/library/fstcore/NEWS.md
/usr/lib64/R/library/fstcore/R/fstcore
/usr/lib64/R/library/fstcore/R/fstcore.rdb
/usr/lib64/R/library/fstcore/R/fstcore.rdx
/usr/lib64/R/library/fstcore/WORDLIST
/usr/lib64/R/library/fstcore/help/AnIndex
/usr/lib64/R/library/fstcore/help/aliases.rds
/usr/lib64/R/library/fstcore/help/figures/fstcore.png
/usr/lib64/R/library/fstcore/help/fstcore.rdb
/usr/lib64/R/library/fstcore/help/fstcore.rdx
/usr/lib64/R/library/fstcore/help/paths.rds
/usr/lib64/R/library/fstcore/html/00Index.html
/usr/lib64/R/library/fstcore/html/R.css
/usr/lib64/R/library/fstcore/include/fstcore.h
/usr/lib64/R/library/fstcore/include/fstcore_RcppExports.h
/usr/lib64/R/library/fstcore/tests/testthat.R
/usr/lib64/R/library/fstcore/tests/testthat/fst_helpers.R
/usr/lib64/R/library/fstcore/tests/testthat/test_lintr.R
/usr/lib64/R/library/fstcore/tests/testthat/test_long_tables.R
/usr/lib64/R/library/fstcore/tests/testthat/test_null_tables.R
/usr/lib64/R/library/fstcore/tests/testthat/test_omp.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/fstcore/libs/fstcore.so
/usr/lib64/R/library/fstcore/libs/fstcore.so.avx2
/usr/lib64/R/library/fstcore/libs/fstcore.so.avx512

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-fstcore/9cf097120d3d9eea0e9790d7d44ae80e6231a35a
/usr/share/package-licenses/R-fstcore/e663fbf883f36aceb8a037739fe8bd2c7e55303a
