#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-jomo
Version  : 2.7.2
Release  : 9
URL      : https://cran.r-project.org/src/contrib/jomo_2.7-2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/jomo_2.7-2.tar.gz
Summary  : Multilevel Joint Modelling Multiple Imputation
Group    : Development/Tools
License  : GPL-2.0
Requires: R-jomo-lib = %{version}-%{release}
Requires: R-lme4
Requires: R-ordinal
BuildRequires : R-lme4
BuildRequires : R-ordinal
BuildRequires : buildreq-R

%description
Novel aspects of 'jomo' are the possibility of handling binary and categorical data through latent normal variables, the option to use cluster-specific covariance matrices and to impute compatibly with the substantive model.

%package lib
Summary: lib components for the R-jomo package.
Group: Libraries

%description lib
lib components for the R-jomo package.


%prep
%setup -q -c -n jomo
cd %{_builddir}/jomo

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1642444312

%install
export SOURCE_DATE_EPOCH=1642444312
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library jomo
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library jomo
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library jomo
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc jomo || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/jomo/CITATION
/usr/lib64/R/library/jomo/DESCRIPTION
/usr/lib64/R/library/jomo/INDEX
/usr/lib64/R/library/jomo/Meta/Rd.rds
/usr/lib64/R/library/jomo/Meta/data.rds
/usr/lib64/R/library/jomo/Meta/features.rds
/usr/lib64/R/library/jomo/Meta/hsearch.rds
/usr/lib64/R/library/jomo/Meta/links.rds
/usr/lib64/R/library/jomo/Meta/nsInfo.rds
/usr/lib64/R/library/jomo/Meta/package.rds
/usr/lib64/R/library/jomo/NAMESPACE
/usr/lib64/R/library/jomo/R/jomo
/usr/lib64/R/library/jomo/R/jomo.rdb
/usr/lib64/R/library/jomo/R/jomo.rdx
/usr/lib64/R/library/jomo/data/Rdata.rdb
/usr/lib64/R/library/jomo/data/Rdata.rds
/usr/lib64/R/library/jomo/data/Rdata.rdx
/usr/lib64/R/library/jomo/help/AnIndex
/usr/lib64/R/library/jomo/help/aliases.rds
/usr/lib64/R/library/jomo/help/jomo.rdb
/usr/lib64/R/library/jomo/help/jomo.rdx
/usr/lib64/R/library/jomo/help/paths.rds
/usr/lib64/R/library/jomo/html/00Index.html
/usr/lib64/R/library/jomo/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/jomo/libs/jomo.so
/usr/lib64/R/library/jomo/libs/jomo.so.avx2
/usr/lib64/R/library/jomo/libs/jomo.so.avx512
