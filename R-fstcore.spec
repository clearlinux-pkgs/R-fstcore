#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-fstcore
Version  : 0.9.10
Release  : 2
URL      : https://cran.r-project.org/src/contrib/fstcore_0.9.10.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fstcore_0.9.10.tar.gz
Summary  : R Bindings to the 'Fstlib' Library
Group    : Development/Tools
License  : BSD-3-Clause MPL-2.0
Requires: R-fstcore-lib = %{version}-%{release}
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

%description lib
lib components for the R-fstcore package.


%prep
%setup -q -c -n fstcore
cd %{_builddir}/fstcore

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1647961805

%install
export SOURCE_DATE_EPOCH=1647961805
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fstcore
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fstcore
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fstcore
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc fstcore || :


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
