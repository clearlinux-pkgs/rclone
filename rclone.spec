#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rclone
Version  : 1.58.0
Release  : 41
URL      : https://github.com/rclone/rclone/releases/download/v1.58.0/rclone-v1.58.0.tar.gz
Source0  : https://github.com/rclone/rclone/releases/download/v1.58.0/rclone-v1.58.0.tar.gz
Source1  : http://localhost/cgit/projects/rclone-vendor/snapshot/rclone-vendor-1.58.0.1.tar.xz
Summary  : rsync for cloud storage
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause ISC MIT MPL-2.0-no-copyleft-exception
Requires: rclone-bin = %{version}-%{release}
Requires: rclone-license = %{version}-%{release}
Requires: rclone-man = %{version}-%{release}
BuildRequires : buildreq-golang

%description
Rclone ("rsync for cloud storage") is a command line program to sync files and directories to and from different cloud storage providers.

%package bin
Summary: bin components for the rclone package.
Group: Binaries
Requires: rclone-license = %{version}-%{release}

%description bin
bin components for the rclone package.


%package license
Summary: license components for the rclone package.
Group: Default

%description license
license components for the rclone package.


%package man
Summary: man components for the rclone package.
Group: Default

%description man
man components for the rclone package.


%prep
%setup -q -n rclone-v1.58.0
cd %{_builddir}
tar xf %{_sourcedir}/rclone-vendor-1.58.0.1.tar.xz
cd %{_builddir}/rclone-v1.58.0
mkdir -p ./
cp -r %{_builddir}/rclone-vendor-1.58.0.1/* %{_builddir}/rclone-v1.58.0/./

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1648580181
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
make  %{?_smp_mflags}  -f Makefile GOFLAGS='-mod=vendor -buildmode=pie -v'


%install
export SOURCE_DATE_EPOCH=1648580181
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/rclone
cp %{_builddir}/rclone-v1.58.0/COPYING %{buildroot}/usr/share/package-licenses/rclone/8fb789d383906a5e83d6a74149e094f8d6921812
cp %{_builddir}/rclone-v1.58.0/cmd/bisync/LICENSE.cjnaz %{buildroot}/usr/share/package-licenses/rclone/6df09dff6c2398859a6546f84451715f3a01c2cd
cp %{_builddir}/rclone-v1.58.0/docs/content/licence.md %{buildroot}/usr/share/package-licenses/rclone/e580fcc37b848519c520bdab2d1c96be07079dbe
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/cloud.google.com/go/LICENSE %{buildroot}/usr/share/package-licenses/rclone/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/Azure/azure-pipeline-go/LICENSE %{buildroot}/usr/share/package-licenses/rclone/eee5b07a657266ef6c5c20acee6685ac6732cd19
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/Azure/azure-storage-blob-go/LICENSE %{buildroot}/usr/share/package-licenses/rclone/eee5b07a657266ef6c5c20acee6685ac6732cd19
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/Azure/go-autorest/LICENSE %{buildroot}/usr/share/package-licenses/rclone/308c47a3ea356402d2d14241da9a9f64cf404008
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/Azure/go-autorest/autorest/adal/LICENSE %{buildroot}/usr/share/package-licenses/rclone/308c47a3ea356402d2d14241da9a9f64cf404008
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/Azure/go-autorest/autorest/date/LICENSE %{buildroot}/usr/share/package-licenses/rclone/308c47a3ea356402d2d14241da9a9f64cf404008
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/Azure/go-autorest/logger/LICENSE %{buildroot}/usr/share/package-licenses/rclone/308c47a3ea356402d2d14241da9a9f64cf404008
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/Azure/go-autorest/tracing/LICENSE %{buildroot}/usr/share/package-licenses/rclone/308c47a3ea356402d2d14241da9a9f64cf404008
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/Azure/go-ntlmssp/LICENSE %{buildroot}/usr/share/package-licenses/rclone/90778a2b78620d46a521986f99136e44a1dde89f
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/Max-Sum/base32768/LICENSE %{buildroot}/usr/share/package-licenses/rclone/8f51413d2595fb4510abed657da6da9056b7cd50
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/Microsoft/go-winio/LICENSE %{buildroot}/usr/share/package-licenses/rclone/11a8fec351554e8f6c3f4dac5a1f4049dd467ba8
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/StackExchange/wmi/LICENSE %{buildroot}/usr/share/package-licenses/rclone/c0f4ffe120079028c20033cf13619b9f52434c22
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/Unknwon/goconfig/LICENSE %{buildroot}/usr/share/package-licenses/rclone/34774a54e4b286739f317922b31ba5eb3ec9195e
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/a8m/tree/LICENSE %{buildroot}/usr/share/package-licenses/rclone/5e179fa54e9195abd2ac3ed2fff7516ad9730bcf
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/aalpar/deheap/LICENSE.txt %{buildroot}/usr/share/package-licenses/rclone/1cddd03fee670202871bd209987552bd5bd08f2f
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/abbot/go-http-auth/LICENSE %{buildroot}/usr/share/package-licenses/rclone/04319952ed7b0f3b3a70ae4d5d9f954317b8f970
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/anacrolix/dms/LICENSE %{buildroot}/usr/share/package-licenses/rclone/b9061705ec712d183d4e81fe1ec8bccfd5439c0f
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/atotto/clipboard/LICENSE %{buildroot}/usr/share/package-licenses/rclone/5485efdb8b4f1167116feb7f4df9798329000329
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/aws/aws-sdk-go/LICENSE.txt %{buildroot}/usr/share/package-licenses/rclone/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/aws/aws-sdk-go/internal/sync/singleflight/LICENSE %{buildroot}/usr/share/package-licenses/rclone/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/beorn7/perks/LICENSE %{buildroot}/usr/share/package-licenses/rclone/b2e4520feb0f9b51ad373256b94c3faf4c1e6871
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/btcsuite/btcutil/LICENSE %{buildroot}/usr/share/package-licenses/rclone/df6498c1204c9432dcba1a6078f92c99d9d11505
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/buengese/sgzip/GO_LICENSE %{buildroot}/usr/share/package-licenses/rclone/7f7a12bcfc16fab2522aa1a562fd3d2aee429d3b
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/buengese/sgzip/LICENSE %{buildroot}/usr/share/package-licenses/rclone/360d21b032bddd1e5793ae8ddbe5c165a6780efa
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/calebcase/tmpfile/LICENSE %{buildroot}/usr/share/package-licenses/rclone/b770d387efdd7502573c35a14fcc8454af0f1ef7
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/calebcase/tmpfile/LICENSE.golang %{buildroot}/usr/share/package-licenses/rclone/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/cespare/xxhash/v2/LICENSE.txt %{buildroot}/usr/share/package-licenses/rclone/7be82c1a81e7197640a88df91dc82d64b77c7acd
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/colinmarc/hdfs/v2/LICENSE.txt %{buildroot}/usr/share/package-licenses/rclone/13f93ed9ec15f4f9d608e7a417e1bae94645bf2f
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/coreos/go-semver/LICENSE %{buildroot}/usr/share/package-licenses/rclone/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/coreos/go-systemd/LICENSE %{buildroot}/usr/share/package-licenses/rclone/172ca3bbafe312a1cf09cfff26953db2f425c28e
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/cpuguy83/go-md2man/v2/LICENSE.md %{buildroot}/usr/share/package-licenses/rclone/b7a606730713ac061594edab33cf941704b4a95c
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/davecgh/go-spew/LICENSE %{buildroot}/usr/share/package-licenses/rclone/d2f340a01dd48b589a70f627cf7058c585a315e4
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/dop251/scsu/LICENSE %{buildroot}/usr/share/package-licenses/rclone/9236ef275fc742ec6f33c0919f30dc86647c6ea9
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/dropbox/dropbox-sdk-go-unofficial/v6/LICENSE %{buildroot}/usr/share/package-licenses/rclone/dffd9523ff0a2a713b70c269f38400c6a7ebb8b5
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/gabriel-vasile/mimetype/LICENSE %{buildroot}/usr/share/package-licenses/rclone/4a06de85fbb53323c0ed1925df9bbff1bfecf459
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/go-chi/chi/v5/LICENSE %{buildroot}/usr/share/package-licenses/rclone/134abc2fa7aa177835bdf93b124636715eab4c33
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/go-ole/go-ole/LICENSE %{buildroot}/usr/share/package-licenses/rclone/565471fdf06cfb21b7c69c5fc329a1341d5d9ad0
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/gogo/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/rclone/06b27345acae9303e13dde9974d2b2e318b05989
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/golang-jwt/jwt/v4/LICENSE %{buildroot}/usr/share/package-licenses/rclone/5e975d829f4ea420c028ba512f8bb3e0ebaaf574
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/golang/groupcache/LICENSE %{buildroot}/usr/share/package-licenses/rclone/172ca3bbafe312a1cf09cfff26953db2f425c28e
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/golang/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/rclone/aa9b240f558caed367795f667629ccbca28f20b2
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/google/go-querystring/LICENSE %{buildroot}/usr/share/package-licenses/rclone/5d833085cd09e0a70fe9071b1f2edf6d31b91d45
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/google/uuid/LICENSE %{buildroot}/usr/share/package-licenses/rclone/08021ae73f58f423dd6e7b525e81cf2520f7619e
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/googleapis/gax-go/v2/LICENSE %{buildroot}/usr/share/package-licenses/rclone/2bda142bd58fd76f408cf18fa997d8fab0278a22
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/hanwen/go-fuse/v2/LICENSE %{buildroot}/usr/share/package-licenses/rclone/49e5e923ba863435babb0b94920a67e66a2dbd53
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/hashicorp/go-uuid/LICENSE %{buildroot}/usr/share/package-licenses/rclone/fa7c4d75bae3a641d1f9ab5df028175bfb8a69ca
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/iguanesolutions/go-systemd/v5/LICENSE %{buildroot}/usr/share/package-licenses/rclone/db69a7e014e68367238cc08a26a1de580d89895e
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/inconshreveable/mousetrap/LICENSE %{buildroot}/usr/share/package-licenses/rclone/9174f93c54ad0022bbb9b445480cfb6b4217226a
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/jcmturner/aescts/v2/LICENSE %{buildroot}/usr/share/package-licenses/rclone/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/jcmturner/dnsutils/v2/LICENSE %{buildroot}/usr/share/package-licenses/rclone/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/jcmturner/gofork/LICENSE %{buildroot}/usr/share/package-licenses/rclone/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/jcmturner/goidentity/v6/LICENSE %{buildroot}/usr/share/package-licenses/rclone/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/jcmturner/gokrb5/v8/LICENSE %{buildroot}/usr/share/package-licenses/rclone/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/jcmturner/rpc/v2/LICENSE %{buildroot}/usr/share/package-licenses/rclone/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/jmespath/go-jmespath/LICENSE %{buildroot}/usr/share/package-licenses/rclone/4052101a660a7d8343c13ada130123f75f1dd408
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/jzelinskie/whirlpool/LICENSE %{buildroot}/usr/share/package-licenses/rclone/982be8423926a050d9494c059be0a50cd9df9fcb
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/klauspost/compress/LICENSE %{buildroot}/usr/share/package-licenses/rclone/0e8f2042647b8140e79c4eb7d233d1b39231db09
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/koofr/go-httpclient/LICENSE %{buildroot}/usr/share/package-licenses/rclone/9cafe275ac14100e5ef048da7c9ebbbd6d26ccda
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/koofr/go-koofrclient/LICENSE %{buildroot}/usr/share/package-licenses/rclone/9cafe275ac14100e5ef048da7c9ebbbd6d26ccda
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/kr/fs/LICENSE %{buildroot}/usr/share/package-licenses/rclone/7f7a12bcfc16fab2522aa1a562fd3d2aee429d3b
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/lufia/plan9stats/LICENSE %{buildroot}/usr/share/package-licenses/rclone/5786fda6d2a0e23fb7f39ae56257eb3a113a4add
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/mattn/go-colorable/LICENSE %{buildroot}/usr/share/package-licenses/rclone/5ca808f075931c5322193d4afd5a3370c824f810
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/mattn/go-ieproxy/LICENSE %{buildroot}/usr/share/package-licenses/rclone/0b47ccf4a62f15a75149f3705b8be8e7327f1b99
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/mattn/go-isatty/LICENSE %{buildroot}/usr/share/package-licenses/rclone/5b53018d7f0706e49275a92d36b54cfbfbb71367
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/mattn/go-runewidth/LICENSE %{buildroot}/usr/share/package-licenses/rclone/5ca808f075931c5322193d4afd5a3370c824f810
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/matttproud/golang_protobuf_extensions/LICENSE %{buildroot}/usr/share/package-licenses/rclone/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/mitchellh/go-homedir/LICENSE %{buildroot}/usr/share/package-licenses/rclone/5ad2002bc8d2b22e2034867d159f71ba6258e18f
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/ncw/go-acd/LICENSE %{buildroot}/usr/share/package-licenses/rclone/391d45842b9f73858dc098d238c442fa626fe77a
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/ncw/swift/v2/COPYING %{buildroot}/usr/share/package-licenses/rclone/8fb789d383906a5e83d6a74149e094f8d6921812
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/nsf/termbox-go/LICENSE %{buildroot}/usr/share/package-licenses/rclone/c920b3ea022bef40a99a9cc0768985d691010fb0
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/patrickmn/go-cache/LICENSE %{buildroot}/usr/share/package-licenses/rclone/4da388cb14535cb8d2beb61b160aab2a2043a8c0
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/pengsrc/go-shared/LICENSE %{buildroot}/usr/share/package-licenses/rclone/c70af8de765cf6b3ea8511100f570be42dfc63a3
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/pkg/sftp/LICENSE %{buildroot}/usr/share/package-licenses/rclone/2510861d72bd971c91b53a5c5fc291e2971c669e
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/pmezard/go-difflib/LICENSE %{buildroot}/usr/share/package-licenses/rclone/cd3e4d932cee20da681e6b3bee8139cb4f734034
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/prometheus/client_golang/LICENSE %{buildroot}/usr/share/package-licenses/rclone/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/prometheus/client_golang/NOTICE %{buildroot}/usr/share/package-licenses/rclone/fd6460234f122a19f21affb6d6885269340b9176
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/prometheus/client_model/LICENSE %{buildroot}/usr/share/package-licenses/rclone/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/prometheus/common/LICENSE %{buildroot}/usr/share/package-licenses/rclone/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/prometheus/procfs/LICENSE %{buildroot}/usr/share/package-licenses/rclone/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/putdotio/go-putio/putio/LICENSE %{buildroot}/usr/share/package-licenses/rclone/a48a884fcdfd5c46023bed86b6058508cfc7b841
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/rclone/ftp/LICENSE %{buildroot}/usr/share/package-licenses/rclone/f11754cdb6a138a3420443feef5d64ca5917f207
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/rfjakob/eme/LICENSE %{buildroot}/usr/share/package-licenses/rclone/7b00728bec591be7fabd9a50b6509e349371ff11
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/rivo/uniseg/LICENSE.txt %{buildroot}/usr/share/package-licenses/rclone/f60d047cd34de4c91b3a045ebf117fe54b3c279e
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/russross/blackfriday/v2/LICENSE.txt %{buildroot}/usr/share/package-licenses/rclone/da34754c05d40ff81f91de8c1b85ea6e5503e21d
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/shirou/gopsutil/v3/LICENSE %{buildroot}/usr/share/package-licenses/rclone/d68d075275fd3d508ed2f3e417cc390d5a070b00
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/sirupsen/logrus/LICENSE %{buildroot}/usr/share/package-licenses/rclone/a1c7852c717fed2c9a0284ed112ea66013230da6
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/skratchdot/open-golang/LICENSE %{buildroot}/usr/share/package-licenses/rclone/a25a6744be0a23436014541afd340d2f2aa1e46c
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/spacemonkeygo/monkit/v3/LICENSE %{buildroot}/usr/share/package-licenses/rclone/172ca3bbafe312a1cf09cfff26953db2f425c28e
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/spf13/cobra/LICENSE.txt %{buildroot}/usr/share/package-licenses/rclone/c7feacb4667f8c63c89e2eeeb9a913bd3ced8ac2
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/spf13/pflag/LICENSE %{buildroot}/usr/share/package-licenses/rclone/b3c86ae465b21f7323059db335158b48187731c7
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/stretchr/testify/LICENSE %{buildroot}/usr/share/package-licenses/rclone/892204393ca075d09c8b1c1d880aba1ae0a2b805
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/t3rm1n4l/go-mega/LICENSE %{buildroot}/usr/share/package-licenses/rclone/ace53a5dfc4d77db3b8c7c525c02169aa7b7a748
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/tklauser/go-sysconf/LICENSE %{buildroot}/usr/share/package-licenses/rclone/d3deb80a5a64709b76f565f3ef031c6e833ac06c
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/tklauser/numcpus/LICENSE %{buildroot}/usr/share/package-licenses/rclone/c7d29e63abb9879f033368ba0ed4323dfb8046c5
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/vivint/infectious/LICENSE %{buildroot}/usr/share/package-licenses/rclone/a4e91d03ec7c2d2090cbee6d780946dbfeb709a3
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/xanzy/ssh-agent/LICENSE %{buildroot}/usr/share/package-licenses/rclone/669a1e53b9dd9df3474300d3d959bb85bad75945
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/youmark/pkcs8/LICENSE %{buildroot}/usr/share/package-licenses/rclone/7a68d66c33fbdaa3e1a4d562ea7e47da5ad027ba
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/yunify/qingstor-sdk-go/v3/LICENSE %{buildroot}/usr/share/package-licenses/rclone/7d856e08ce2872888e5122b0574c14859e7c8464
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/github.com/zeebo/errs/LICENSE %{buildroot}/usr/share/package-licenses/rclone/2a80ddae1870dbf22e867ca2dcf65f98f896bda7
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/go.etcd.io/bbolt/LICENSE %{buildroot}/usr/share/package-licenses/rclone/66c5c002958b1f31f74410b353972d622d74e007
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/go.opencensus.io/LICENSE %{buildroot}/usr/share/package-licenses/rclone/1128f8f91104ba9ef98d37eea6523a888dcfa5de
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/goftp.io/server/LICENSE %{buildroot}/usr/share/package-licenses/rclone/0146be22c720ce2731a03efa6ba1d97084293b06
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/golang.org/x/crypto/LICENSE %{buildroot}/usr/share/package-licenses/rclone/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/golang.org/x/net/LICENSE %{buildroot}/usr/share/package-licenses/rclone/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/golang.org/x/oauth2/LICENSE %{buildroot}/usr/share/package-licenses/rclone/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/golang.org/x/sync/LICENSE %{buildroot}/usr/share/package-licenses/rclone/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/golang.org/x/sys/LICENSE %{buildroot}/usr/share/package-licenses/rclone/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/golang.org/x/term/LICENSE %{buildroot}/usr/share/package-licenses/rclone/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/golang.org/x/text/LICENSE %{buildroot}/usr/share/package-licenses/rclone/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/golang.org/x/time/LICENSE %{buildroot}/usr/share/package-licenses/rclone/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/google.golang.org/api/LICENSE %{buildroot}/usr/share/package-licenses/rclone/ab32a5c14ccc0a6d38e173568a5577493e3f6870
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/google.golang.org/api/internal/third_party/uritemplates/LICENSE %{buildroot}/usr/share/package-licenses/rclone/475b0ccf682da5e05e3aa1eb6146b30132ae717d
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/google.golang.org/appengine/LICENSE %{buildroot}/usr/share/package-licenses/rclone/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/google.golang.org/genproto/LICENSE %{buildroot}/usr/share/package-licenses/rclone/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/google.golang.org/grpc/LICENSE %{buildroot}/usr/share/package-licenses/rclone/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/google.golang.org/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/rclone/74850a25a5319bdddc0d998eb8926c18bada282b
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/gopkg.in/yaml.v2/LICENSE %{buildroot}/usr/share/package-licenses/rclone/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/gopkg.in/yaml.v2/LICENSE.libyaml %{buildroot}/usr/share/package-licenses/rclone/ad00ce7340d89dc13ccc59920ef75cb55af5b164
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/gopkg.in/yaml.v2/NOTICE %{buildroot}/usr/share/package-licenses/rclone/9522d95b2b9b284285cc3fb6ecc445aa3ee5e785
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/gopkg.in/yaml.v3/LICENSE %{buildroot}/usr/share/package-licenses/rclone/b74b3b31bc15ad5e94fc1947d682aa3d84132fce
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/gopkg.in/yaml.v3/NOTICE %{buildroot}/usr/share/package-licenses/rclone/9522d95b2b9b284285cc3fb6ecc445aa3ee5e785
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/storj.io/common/LICENSE %{buildroot}/usr/share/package-licenses/rclone/9770d86eee2c38c5f4359d62153286ecfe801bd4
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/storj.io/drpc/LICENSE %{buildroot}/usr/share/package-licenses/rclone/9770d86eee2c38c5f4359d62153286ecfe801bd4
cp %{_builddir}/rclone-vendor-1.58.0.1/vendor/storj.io/uplink/LICENSE %{buildroot}/usr/share/package-licenses/rclone/9770d86eee2c38c5f4359d62153286ecfe801bd4
true
## install_append content
install -d %{buildroot}/usr/bin/
install -m0755 rclone %{buildroot}/usr/bin/
install -Dpm0644 ./rclone.1 %{buildroot}/usr/share/man/man1/rclone.1
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/rclone

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/rclone/0146be22c720ce2731a03efa6ba1d97084293b06
/usr/share/package-licenses/rclone/04319952ed7b0f3b3a70ae4d5d9f954317b8f970
/usr/share/package-licenses/rclone/06b27345acae9303e13dde9974d2b2e318b05989
/usr/share/package-licenses/rclone/08021ae73f58f423dd6e7b525e81cf2520f7619e
/usr/share/package-licenses/rclone/0b47ccf4a62f15a75149f3705b8be8e7327f1b99
/usr/share/package-licenses/rclone/0e8f2042647b8140e79c4eb7d233d1b39231db09
/usr/share/package-licenses/rclone/1128f8f91104ba9ef98d37eea6523a888dcfa5de
/usr/share/package-licenses/rclone/11a8fec351554e8f6c3f4dac5a1f4049dd467ba8
/usr/share/package-licenses/rclone/134abc2fa7aa177835bdf93b124636715eab4c33
/usr/share/package-licenses/rclone/13f93ed9ec15f4f9d608e7a417e1bae94645bf2f
/usr/share/package-licenses/rclone/172ca3bbafe312a1cf09cfff26953db2f425c28e
/usr/share/package-licenses/rclone/1cddd03fee670202871bd209987552bd5bd08f2f
/usr/share/package-licenses/rclone/2510861d72bd971c91b53a5c5fc291e2971c669e
/usr/share/package-licenses/rclone/2a80ddae1870dbf22e867ca2dcf65f98f896bda7
/usr/share/package-licenses/rclone/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/rclone/2bda142bd58fd76f408cf18fa997d8fab0278a22
/usr/share/package-licenses/rclone/308c47a3ea356402d2d14241da9a9f64cf404008
/usr/share/package-licenses/rclone/34774a54e4b286739f317922b31ba5eb3ec9195e
/usr/share/package-licenses/rclone/360d21b032bddd1e5793ae8ddbe5c165a6780efa
/usr/share/package-licenses/rclone/391d45842b9f73858dc098d238c442fa626fe77a
/usr/share/package-licenses/rclone/4052101a660a7d8343c13ada130123f75f1dd408
/usr/share/package-licenses/rclone/475b0ccf682da5e05e3aa1eb6146b30132ae717d
/usr/share/package-licenses/rclone/49e5e923ba863435babb0b94920a67e66a2dbd53
/usr/share/package-licenses/rclone/4a06de85fbb53323c0ed1925df9bbff1bfecf459
/usr/share/package-licenses/rclone/4da388cb14535cb8d2beb61b160aab2a2043a8c0
/usr/share/package-licenses/rclone/5485efdb8b4f1167116feb7f4df9798329000329
/usr/share/package-licenses/rclone/565471fdf06cfb21b7c69c5fc329a1341d5d9ad0
/usr/share/package-licenses/rclone/5786fda6d2a0e23fb7f39ae56257eb3a113a4add
/usr/share/package-licenses/rclone/5ad2002bc8d2b22e2034867d159f71ba6258e18f
/usr/share/package-licenses/rclone/5b53018d7f0706e49275a92d36b54cfbfbb71367
/usr/share/package-licenses/rclone/5ca808f075931c5322193d4afd5a3370c824f810
/usr/share/package-licenses/rclone/5d833085cd09e0a70fe9071b1f2edf6d31b91d45
/usr/share/package-licenses/rclone/5e179fa54e9195abd2ac3ed2fff7516ad9730bcf
/usr/share/package-licenses/rclone/5e975d829f4ea420c028ba512f8bb3e0ebaaf574
/usr/share/package-licenses/rclone/669a1e53b9dd9df3474300d3d959bb85bad75945
/usr/share/package-licenses/rclone/66c5c002958b1f31f74410b353972d622d74e007
/usr/share/package-licenses/rclone/6df09dff6c2398859a6546f84451715f3a01c2cd
/usr/share/package-licenses/rclone/74850a25a5319bdddc0d998eb8926c18bada282b
/usr/share/package-licenses/rclone/7a68d66c33fbdaa3e1a4d562ea7e47da5ad027ba
/usr/share/package-licenses/rclone/7b00728bec591be7fabd9a50b6509e349371ff11
/usr/share/package-licenses/rclone/7be82c1a81e7197640a88df91dc82d64b77c7acd
/usr/share/package-licenses/rclone/7d856e08ce2872888e5122b0574c14859e7c8464
/usr/share/package-licenses/rclone/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
/usr/share/package-licenses/rclone/7f7a12bcfc16fab2522aa1a562fd3d2aee429d3b
/usr/share/package-licenses/rclone/892204393ca075d09c8b1c1d880aba1ae0a2b805
/usr/share/package-licenses/rclone/8f51413d2595fb4510abed657da6da9056b7cd50
/usr/share/package-licenses/rclone/8fb789d383906a5e83d6a74149e094f8d6921812
/usr/share/package-licenses/rclone/90778a2b78620d46a521986f99136e44a1dde89f
/usr/share/package-licenses/rclone/9174f93c54ad0022bbb9b445480cfb6b4217226a
/usr/share/package-licenses/rclone/92170cdc034b2ff819323ff670d3b7266c8bffcd
/usr/share/package-licenses/rclone/9236ef275fc742ec6f33c0919f30dc86647c6ea9
/usr/share/package-licenses/rclone/9522d95b2b9b284285cc3fb6ecc445aa3ee5e785
/usr/share/package-licenses/rclone/9770d86eee2c38c5f4359d62153286ecfe801bd4
/usr/share/package-licenses/rclone/982be8423926a050d9494c059be0a50cd9df9fcb
/usr/share/package-licenses/rclone/9cafe275ac14100e5ef048da7c9ebbbd6d26ccda
/usr/share/package-licenses/rclone/a1c7852c717fed2c9a0284ed112ea66013230da6
/usr/share/package-licenses/rclone/a25a6744be0a23436014541afd340d2f2aa1e46c
/usr/share/package-licenses/rclone/a48a884fcdfd5c46023bed86b6058508cfc7b841
/usr/share/package-licenses/rclone/a4e91d03ec7c2d2090cbee6d780946dbfeb709a3
/usr/share/package-licenses/rclone/aa9b240f558caed367795f667629ccbca28f20b2
/usr/share/package-licenses/rclone/ab32a5c14ccc0a6d38e173568a5577493e3f6870
/usr/share/package-licenses/rclone/ace53a5dfc4d77db3b8c7c525c02169aa7b7a748
/usr/share/package-licenses/rclone/ad00ce7340d89dc13ccc59920ef75cb55af5b164
/usr/share/package-licenses/rclone/b2e4520feb0f9b51ad373256b94c3faf4c1e6871
/usr/share/package-licenses/rclone/b3c86ae465b21f7323059db335158b48187731c7
/usr/share/package-licenses/rclone/b74b3b31bc15ad5e94fc1947d682aa3d84132fce
/usr/share/package-licenses/rclone/b770d387efdd7502573c35a14fcc8454af0f1ef7
/usr/share/package-licenses/rclone/b7a606730713ac061594edab33cf941704b4a95c
/usr/share/package-licenses/rclone/b9061705ec712d183d4e81fe1ec8bccfd5439c0f
/usr/share/package-licenses/rclone/c0f4ffe120079028c20033cf13619b9f52434c22
/usr/share/package-licenses/rclone/c70af8de765cf6b3ea8511100f570be42dfc63a3
/usr/share/package-licenses/rclone/c7d29e63abb9879f033368ba0ed4323dfb8046c5
/usr/share/package-licenses/rclone/c7feacb4667f8c63c89e2eeeb9a913bd3ced8ac2
/usr/share/package-licenses/rclone/c920b3ea022bef40a99a9cc0768985d691010fb0
/usr/share/package-licenses/rclone/cd3e4d932cee20da681e6b3bee8139cb4f734034
/usr/share/package-licenses/rclone/d2f340a01dd48b589a70f627cf7058c585a315e4
/usr/share/package-licenses/rclone/d3deb80a5a64709b76f565f3ef031c6e833ac06c
/usr/share/package-licenses/rclone/d68d075275fd3d508ed2f3e417cc390d5a070b00
/usr/share/package-licenses/rclone/d6a5f1ecaedd723c325a2063375b3517e808a2b5
/usr/share/package-licenses/rclone/da34754c05d40ff81f91de8c1b85ea6e5503e21d
/usr/share/package-licenses/rclone/db69a7e014e68367238cc08a26a1de580d89895e
/usr/share/package-licenses/rclone/df6498c1204c9432dcba1a6078f92c99d9d11505
/usr/share/package-licenses/rclone/dffd9523ff0a2a713b70c269f38400c6a7ebb8b5
/usr/share/package-licenses/rclone/e580fcc37b848519c520bdab2d1c96be07079dbe
/usr/share/package-licenses/rclone/eee5b07a657266ef6c5c20acee6685ac6732cd19
/usr/share/package-licenses/rclone/f11754cdb6a138a3420443feef5d64ca5917f207
/usr/share/package-licenses/rclone/f60d047cd34de4c91b3a045ebf117fe54b3c279e
/usr/share/package-licenses/rclone/fa7c4d75bae3a641d1f9ab5df028175bfb8a69ca
/usr/share/package-licenses/rclone/fd6460234f122a19f21affb6d6885269340b9176

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/rclone.1
