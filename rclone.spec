#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rclone
Version  : 1.52.1
Release  : 7
URL      : https://github.com/rclone/rclone/releases/download/v1.52.1/rclone-v1.52.1.tar.gz
Source0  : https://github.com/rclone/rclone/releases/download/v1.52.1/rclone-v1.52.1.tar.gz
Summary  : rsync for cloud storage
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause ISC MIT
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
%setup -q -n rclone-v1.52.1
cd %{_builddir}/rclone-v1.52.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1591819496
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
make  %{?_smp_mflags}  || go build -mod vendor


%install
export SOURCE_DATE_EPOCH=1591819496
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/rclone
cp %{_builddir}/rclone-v1.52.1/COPYING %{buildroot}/usr/share/package-licenses/rclone/8fb789d383906a5e83d6a74149e094f8d6921812
cp %{_builddir}/rclone-v1.52.1/vendor/cloud.google.com/go/LICENSE %{buildroot}/usr/share/package-licenses/rclone/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/Azure/azure-pipeline-go/LICENSE %{buildroot}/usr/share/package-licenses/rclone/eee5b07a657266ef6c5c20acee6685ac6732cd19
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/Azure/azure-storage-blob-go/LICENSE %{buildroot}/usr/share/package-licenses/rclone/eee5b07a657266ef6c5c20acee6685ac6732cd19
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/Unknwon/goconfig/LICENSE %{buildroot}/usr/share/package-licenses/rclone/34774a54e4b286739f317922b31ba5eb3ec9195e
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/a8m/tree/LICENSE %{buildroot}/usr/share/package-licenses/rclone/5e179fa54e9195abd2ac3ed2fff7516ad9730bcf
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/aalpar/deheap/LICENSE.txt %{buildroot}/usr/share/package-licenses/rclone/1cddd03fee670202871bd209987552bd5bd08f2f
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/abbot/go-http-auth/LICENSE %{buildroot}/usr/share/package-licenses/rclone/04319952ed7b0f3b3a70ae4d5d9f954317b8f970
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/anacrolix/dms/LICENSE %{buildroot}/usr/share/package-licenses/rclone/b9061705ec712d183d4e81fe1ec8bccfd5439c0f
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/atotto/clipboard/LICENSE %{buildroot}/usr/share/package-licenses/rclone/5485efdb8b4f1167116feb7f4df9798329000329
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/aws/aws-sdk-go/LICENSE.txt %{buildroot}/usr/share/package-licenses/rclone/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/aws/aws-sdk-go/internal/sync/singleflight/LICENSE %{buildroot}/usr/share/package-licenses/rclone/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/beorn7/perks/LICENSE %{buildroot}/usr/share/package-licenses/rclone/b2e4520feb0f9b51ad373256b94c3faf4c1e6871
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/btcsuite/btcutil/LICENSE %{buildroot}/usr/share/package-licenses/rclone/df6498c1204c9432dcba1a6078f92c99d9d11505
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/calebcase/tmpfile/LICENSE %{buildroot}/usr/share/package-licenses/rclone/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/calebcase/tmpfile/LICENSE.golang %{buildroot}/usr/share/package-licenses/rclone/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/cespare/xxhash/v2/LICENSE.txt %{buildroot}/usr/share/package-licenses/rclone/7be82c1a81e7197640a88df91dc82d64b77c7acd
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/coreos/go-semver/LICENSE %{buildroot}/usr/share/package-licenses/rclone/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/cpuguy83/go-md2man/v2/LICENSE.md %{buildroot}/usr/share/package-licenses/rclone/b7a606730713ac061594edab33cf941704b4a95c
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/davecgh/go-spew/LICENSE %{buildroot}/usr/share/package-licenses/rclone/d2f340a01dd48b589a70f627cf7058c585a315e4
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/djherbis/times/LICENSE %{buildroot}/usr/share/package-licenses/rclone/ca04462637a0f2b5cfe49647eb67d2b02b88d299
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/dropbox/dropbox-sdk-go-unofficial/LICENSE %{buildroot}/usr/share/package-licenses/rclone/dffd9523ff0a2a713b70c269f38400c6a7ebb8b5
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/gogo/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/rclone/06b27345acae9303e13dde9974d2b2e318b05989
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/golang/groupcache/LICENSE %{buildroot}/usr/share/package-licenses/rclone/172ca3bbafe312a1cf09cfff26953db2f425c28e
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/golang/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/rclone/aa9b240f558caed367795f667629ccbca28f20b2
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/google/go-querystring/LICENSE %{buildroot}/usr/share/package-licenses/rclone/5d833085cd09e0a70fe9071b1f2edf6d31b91d45
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/googleapis/gax-go/v2/LICENSE %{buildroot}/usr/share/package-licenses/rclone/2bda142bd58fd76f408cf18fa997d8fab0278a22
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/hanwen/go-fuse/v2/LICENSE %{buildroot}/usr/share/package-licenses/rclone/49e5e923ba863435babb0b94920a67e66a2dbd53
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/inconshreveable/mousetrap/LICENSE %{buildroot}/usr/share/package-licenses/rclone/9174f93c54ad0022bbb9b445480cfb6b4217226a
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/jlaffaye/ftp/LICENSE %{buildroot}/usr/share/package-licenses/rclone/f11754cdb6a138a3420443feef5d64ca5917f207
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/jmespath/go-jmespath/LICENSE %{buildroot}/usr/share/package-licenses/rclone/4052101a660a7d8343c13ada130123f75f1dd408
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/jzelinskie/whirlpool/LICENSE %{buildroot}/usr/share/package-licenses/rclone/982be8423926a050d9494c059be0a50cd9df9fcb
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/kardianos/osext/LICENSE %{buildroot}/usr/share/package-licenses/rclone/7f7a12bcfc16fab2522aa1a562fd3d2aee429d3b
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/konsorten/go-windows-terminal-sequences/LICENSE %{buildroot}/usr/share/package-licenses/rclone/e2ee43b586677eaafd7dd7af25adff48adfa7cf3
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/koofr/go-httpclient/LICENSE %{buildroot}/usr/share/package-licenses/rclone/9cafe275ac14100e5ef048da7c9ebbbd6d26ccda
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/koofr/go-koofrclient/LICENSE %{buildroot}/usr/share/package-licenses/rclone/9cafe275ac14100e5ef048da7c9ebbbd6d26ccda
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/kr/fs/LICENSE %{buildroot}/usr/share/package-licenses/rclone/7f7a12bcfc16fab2522aa1a562fd3d2aee429d3b
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/mattn/go-colorable/LICENSE %{buildroot}/usr/share/package-licenses/rclone/5ca808f075931c5322193d4afd5a3370c824f810
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/mattn/go-ieproxy/LICENSE %{buildroot}/usr/share/package-licenses/rclone/0b47ccf4a62f15a75149f3705b8be8e7327f1b99
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/mattn/go-isatty/LICENSE %{buildroot}/usr/share/package-licenses/rclone/5b53018d7f0706e49275a92d36b54cfbfbb71367
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/mattn/go-runewidth/LICENSE %{buildroot}/usr/share/package-licenses/rclone/5ca808f075931c5322193d4afd5a3370c824f810
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/matttproud/golang_protobuf_extensions/LICENSE %{buildroot}/usr/share/package-licenses/rclone/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/minio/sha256-simd/LICENSE %{buildroot}/usr/share/package-licenses/rclone/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/mitchellh/go-homedir/LICENSE %{buildroot}/usr/share/package-licenses/rclone/5ad2002bc8d2b22e2034867d159f71ba6258e18f
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/ncw/go-acd/LICENSE %{buildroot}/usr/share/package-licenses/rclone/391d45842b9f73858dc098d238c442fa626fe77a
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/ncw/swift/COPYING %{buildroot}/usr/share/package-licenses/rclone/8fb789d383906a5e83d6a74149e094f8d6921812
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/nsf/termbox-go/LICENSE %{buildroot}/usr/share/package-licenses/rclone/c920b3ea022bef40a99a9cc0768985d691010fb0
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/okzk/sdnotify/LICENSE %{buildroot}/usr/share/package-licenses/rclone/2f9b13cc99f8675c7d401778181716b421efcfcf
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/patrickmn/go-cache/LICENSE %{buildroot}/usr/share/package-licenses/rclone/4da388cb14535cb8d2beb61b160aab2a2043a8c0
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/pengsrc/go-shared/LICENSE %{buildroot}/usr/share/package-licenses/rclone/c70af8de765cf6b3ea8511100f570be42dfc63a3
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/pkg/errors/LICENSE %{buildroot}/usr/share/package-licenses/rclone/9c1bedc0d42f24c24a1bd266f3ce101a4b0579fc
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/pkg/sftp/LICENSE %{buildroot}/usr/share/package-licenses/rclone/2510861d72bd971c91b53a5c5fc291e2971c669e
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/pmezard/go-difflib/LICENSE %{buildroot}/usr/share/package-licenses/rclone/cd3e4d932cee20da681e6b3bee8139cb4f734034
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/prometheus/client_golang/LICENSE %{buildroot}/usr/share/package-licenses/rclone/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/prometheus/client_golang/NOTICE %{buildroot}/usr/share/package-licenses/rclone/fd6460234f122a19f21affb6d6885269340b9176
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/prometheus/client_model/LICENSE %{buildroot}/usr/share/package-licenses/rclone/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/prometheus/common/LICENSE %{buildroot}/usr/share/package-licenses/rclone/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/prometheus/procfs/LICENSE %{buildroot}/usr/share/package-licenses/rclone/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/putdotio/go-putio/putio/LICENSE %{buildroot}/usr/share/package-licenses/rclone/a48a884fcdfd5c46023bed86b6058508cfc7b841
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/rfjakob/eme/LICENSE %{buildroot}/usr/share/package-licenses/rclone/7b00728bec591be7fabd9a50b6509e349371ff11
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/russross/blackfriday/v2/LICENSE.txt %{buildroot}/usr/share/package-licenses/rclone/da34754c05d40ff81f91de8c1b85ea6e5503e21d
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/sevlyar/go-daemon/LICENSE %{buildroot}/usr/share/package-licenses/rclone/2184cef9f9bd59fca7453d6db8523cfdb3dbdddd
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/shurcooL/sanitized_anchor_name/LICENSE %{buildroot}/usr/share/package-licenses/rclone/c111106ab0af1873aa6350f797759fe1519c8be1
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/sirupsen/logrus/LICENSE %{buildroot}/usr/share/package-licenses/rclone/a1c7852c717fed2c9a0284ed112ea66013230da6
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/skratchdot/open-golang/LICENSE %{buildroot}/usr/share/package-licenses/rclone/a25a6744be0a23436014541afd340d2f2aa1e46c
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/spacemonkeygo/errors/LICENSE %{buildroot}/usr/share/package-licenses/rclone/172ca3bbafe312a1cf09cfff26953db2f425c28e
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/spacemonkeygo/monkit/v3/LICENSE %{buildroot}/usr/share/package-licenses/rclone/172ca3bbafe312a1cf09cfff26953db2f425c28e
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/spf13/cobra/LICENSE.txt %{buildroot}/usr/share/package-licenses/rclone/c7feacb4667f8c63c89e2eeeb9a913bd3ced8ac2
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/spf13/pflag/LICENSE %{buildroot}/usr/share/package-licenses/rclone/b3c86ae465b21f7323059db335158b48187731c7
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/stretchr/testify/LICENSE %{buildroot}/usr/share/package-licenses/rclone/136eeb14eace5be586388a959df1108bdb3575ac
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/t3rm1n4l/go-mega/LICENSE %{buildroot}/usr/share/package-licenses/rclone/ace53a5dfc4d77db3b8c7c525c02169aa7b7a748
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/vivint/infectious/LICENSE %{buildroot}/usr/share/package-licenses/rclone/a4e91d03ec7c2d2090cbee6d780946dbfeb709a3
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/xanzy/ssh-agent/LICENSE %{buildroot}/usr/share/package-licenses/rclone/669a1e53b9dd9df3474300d3d959bb85bad75945
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/youmark/pkcs8/LICENSE %{buildroot}/usr/share/package-licenses/rclone/7a68d66c33fbdaa3e1a4d562ea7e47da5ad027ba
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/yunify/qingstor-sdk-go/v3/LICENSE %{buildroot}/usr/share/package-licenses/rclone/7d856e08ce2872888e5122b0574c14859e7c8464
cp %{_builddir}/rclone-v1.52.1/vendor/github.com/zeebo/errs/LICENSE %{buildroot}/usr/share/package-licenses/rclone/2a80ddae1870dbf22e867ca2dcf65f98f896bda7
cp %{_builddir}/rclone-v1.52.1/vendor/go.etcd.io/bbolt/LICENSE %{buildroot}/usr/share/package-licenses/rclone/66c5c002958b1f31f74410b353972d622d74e007
cp %{_builddir}/rclone-v1.52.1/vendor/go.opencensus.io/LICENSE %{buildroot}/usr/share/package-licenses/rclone/1128f8f91104ba9ef98d37eea6523a888dcfa5de
cp %{_builddir}/rclone-v1.52.1/vendor/go.uber.org/atomic/LICENSE.txt %{buildroot}/usr/share/package-licenses/rclone/fa2149c34ba4570e3325d4e09aee1b7f32d76679
cp %{_builddir}/rclone-v1.52.1/vendor/go.uber.org/multierr/LICENSE.txt %{buildroot}/usr/share/package-licenses/rclone/5761b1b12cf8cb4d42446dc11f5db436d40c0484
cp %{_builddir}/rclone-v1.52.1/vendor/go.uber.org/zap/LICENSE.txt %{buildroot}/usr/share/package-licenses/rclone/e721d2f494384c806fef4b5fed9e8a2b6d6ff5db
cp %{_builddir}/rclone-v1.52.1/vendor/goftp.io/server/LICENSE %{buildroot}/usr/share/package-licenses/rclone/0146be22c720ce2731a03efa6ba1d97084293b06
cp %{_builddir}/rclone-v1.52.1/vendor/golang.org/x/crypto/LICENSE %{buildroot}/usr/share/package-licenses/rclone/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/rclone-v1.52.1/vendor/golang.org/x/net/LICENSE %{buildroot}/usr/share/package-licenses/rclone/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/rclone-v1.52.1/vendor/golang.org/x/oauth2/LICENSE %{buildroot}/usr/share/package-licenses/rclone/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/rclone-v1.52.1/vendor/golang.org/x/sync/LICENSE %{buildroot}/usr/share/package-licenses/rclone/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/rclone-v1.52.1/vendor/golang.org/x/sys/LICENSE %{buildroot}/usr/share/package-licenses/rclone/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/rclone-v1.52.1/vendor/golang.org/x/text/LICENSE %{buildroot}/usr/share/package-licenses/rclone/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/rclone-v1.52.1/vendor/golang.org/x/time/LICENSE %{buildroot}/usr/share/package-licenses/rclone/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/rclone-v1.52.1/vendor/google.golang.org/api/LICENSE %{buildroot}/usr/share/package-licenses/rclone/ab32a5c14ccc0a6d38e173568a5577493e3f6870
cp %{_builddir}/rclone-v1.52.1/vendor/google.golang.org/api/internal/third_party/uritemplates/LICENSE %{buildroot}/usr/share/package-licenses/rclone/475b0ccf682da5e05e3aa1eb6146b30132ae717d
cp %{_builddir}/rclone-v1.52.1/vendor/google.golang.org/appengine/LICENSE %{buildroot}/usr/share/package-licenses/rclone/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/rclone-v1.52.1/vendor/google.golang.org/genproto/LICENSE %{buildroot}/usr/share/package-licenses/rclone/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/rclone-v1.52.1/vendor/google.golang.org/grpc/LICENSE %{buildroot}/usr/share/package-licenses/rclone/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/rclone-v1.52.1/vendor/gopkg.in/yaml.v2/LICENSE %{buildroot}/usr/share/package-licenses/rclone/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/rclone-v1.52.1/vendor/gopkg.in/yaml.v2/LICENSE.libyaml %{buildroot}/usr/share/package-licenses/rclone/ad00ce7340d89dc13ccc59920ef75cb55af5b164
cp %{_builddir}/rclone-v1.52.1/vendor/gopkg.in/yaml.v2/NOTICE %{buildroot}/usr/share/package-licenses/rclone/9522d95b2b9b284285cc3fb6ecc445aa3ee5e785
cp %{_builddir}/rclone-v1.52.1/vendor/storj.io/common/LICENSE %{buildroot}/usr/share/package-licenses/rclone/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/rclone-v1.52.1/vendor/storj.io/drpc/LICENSE %{buildroot}/usr/share/package-licenses/rclone/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
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
/usr/share/package-licenses/rclone/0b47ccf4a62f15a75149f3705b8be8e7327f1b99
/usr/share/package-licenses/rclone/1128f8f91104ba9ef98d37eea6523a888dcfa5de
/usr/share/package-licenses/rclone/136eeb14eace5be586388a959df1108bdb3575ac
/usr/share/package-licenses/rclone/172ca3bbafe312a1cf09cfff26953db2f425c28e
/usr/share/package-licenses/rclone/1cddd03fee670202871bd209987552bd5bd08f2f
/usr/share/package-licenses/rclone/2184cef9f9bd59fca7453d6db8523cfdb3dbdddd
/usr/share/package-licenses/rclone/2510861d72bd971c91b53a5c5fc291e2971c669e
/usr/share/package-licenses/rclone/2a80ddae1870dbf22e867ca2dcf65f98f896bda7
/usr/share/package-licenses/rclone/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/rclone/2bda142bd58fd76f408cf18fa997d8fab0278a22
/usr/share/package-licenses/rclone/2f9b13cc99f8675c7d401778181716b421efcfcf
/usr/share/package-licenses/rclone/34774a54e4b286739f317922b31ba5eb3ec9195e
/usr/share/package-licenses/rclone/391d45842b9f73858dc098d238c442fa626fe77a
/usr/share/package-licenses/rclone/4052101a660a7d8343c13ada130123f75f1dd408
/usr/share/package-licenses/rclone/475b0ccf682da5e05e3aa1eb6146b30132ae717d
/usr/share/package-licenses/rclone/49e5e923ba863435babb0b94920a67e66a2dbd53
/usr/share/package-licenses/rclone/4da388cb14535cb8d2beb61b160aab2a2043a8c0
/usr/share/package-licenses/rclone/5485efdb8b4f1167116feb7f4df9798329000329
/usr/share/package-licenses/rclone/5761b1b12cf8cb4d42446dc11f5db436d40c0484
/usr/share/package-licenses/rclone/5ad2002bc8d2b22e2034867d159f71ba6258e18f
/usr/share/package-licenses/rclone/5b53018d7f0706e49275a92d36b54cfbfbb71367
/usr/share/package-licenses/rclone/5ca808f075931c5322193d4afd5a3370c824f810
/usr/share/package-licenses/rclone/5d833085cd09e0a70fe9071b1f2edf6d31b91d45
/usr/share/package-licenses/rclone/5e179fa54e9195abd2ac3ed2fff7516ad9730bcf
/usr/share/package-licenses/rclone/669a1e53b9dd9df3474300d3d959bb85bad75945
/usr/share/package-licenses/rclone/66c5c002958b1f31f74410b353972d622d74e007
/usr/share/package-licenses/rclone/7a68d66c33fbdaa3e1a4d562ea7e47da5ad027ba
/usr/share/package-licenses/rclone/7b00728bec591be7fabd9a50b6509e349371ff11
/usr/share/package-licenses/rclone/7be82c1a81e7197640a88df91dc82d64b77c7acd
/usr/share/package-licenses/rclone/7d856e08ce2872888e5122b0574c14859e7c8464
/usr/share/package-licenses/rclone/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
/usr/share/package-licenses/rclone/7f7a12bcfc16fab2522aa1a562fd3d2aee429d3b
/usr/share/package-licenses/rclone/8fb789d383906a5e83d6a74149e094f8d6921812
/usr/share/package-licenses/rclone/9174f93c54ad0022bbb9b445480cfb6b4217226a
/usr/share/package-licenses/rclone/92170cdc034b2ff819323ff670d3b7266c8bffcd
/usr/share/package-licenses/rclone/9522d95b2b9b284285cc3fb6ecc445aa3ee5e785
/usr/share/package-licenses/rclone/982be8423926a050d9494c059be0a50cd9df9fcb
/usr/share/package-licenses/rclone/9c1bedc0d42f24c24a1bd266f3ce101a4b0579fc
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
/usr/share/package-licenses/rclone/b7a606730713ac061594edab33cf941704b4a95c
/usr/share/package-licenses/rclone/b9061705ec712d183d4e81fe1ec8bccfd5439c0f
/usr/share/package-licenses/rclone/c111106ab0af1873aa6350f797759fe1519c8be1
/usr/share/package-licenses/rclone/c70af8de765cf6b3ea8511100f570be42dfc63a3
/usr/share/package-licenses/rclone/c7feacb4667f8c63c89e2eeeb9a913bd3ced8ac2
/usr/share/package-licenses/rclone/c920b3ea022bef40a99a9cc0768985d691010fb0
/usr/share/package-licenses/rclone/ca04462637a0f2b5cfe49647eb67d2b02b88d299
/usr/share/package-licenses/rclone/cd3e4d932cee20da681e6b3bee8139cb4f734034
/usr/share/package-licenses/rclone/d2f340a01dd48b589a70f627cf7058c585a315e4
/usr/share/package-licenses/rclone/d6a5f1ecaedd723c325a2063375b3517e808a2b5
/usr/share/package-licenses/rclone/da34754c05d40ff81f91de8c1b85ea6e5503e21d
/usr/share/package-licenses/rclone/df6498c1204c9432dcba1a6078f92c99d9d11505
/usr/share/package-licenses/rclone/dffd9523ff0a2a713b70c269f38400c6a7ebb8b5
/usr/share/package-licenses/rclone/e2ee43b586677eaafd7dd7af25adff48adfa7cf3
/usr/share/package-licenses/rclone/e721d2f494384c806fef4b5fed9e8a2b6d6ff5db
/usr/share/package-licenses/rclone/eee5b07a657266ef6c5c20acee6685ac6732cd19
/usr/share/package-licenses/rclone/f11754cdb6a138a3420443feef5d64ca5917f207
/usr/share/package-licenses/rclone/fa2149c34ba4570e3325d4e09aee1b7f32d76679
/usr/share/package-licenses/rclone/fd6460234f122a19f21affb6d6885269340b9176

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/rclone.1
