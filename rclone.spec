#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rclone
Version  : 1.46
Release  : 2
URL      : https://github.com/ncw/rclone/releases/download/v1.46/rclone-v1.46.tar.gz
Source0  : https://github.com/ncw/rclone/releases/download/v1.46/rclone-v1.46.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause ISC MIT
Requires: rclone-bin = %{version}-%{release}
Requires: rclone-license = %{version}-%{release}
BuildRequires : buildreq-golang

%description
This is a fork of the encoding/xml package at ca1d6c4, the last commit before
https://go.googlesource.com/go/+/c0d6d33 "encoding/xml: restore Go 1.4 name
space behavior" made late in the lead-up to the Go 1.5 release.

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


%prep
%setup -q -n rclone-v1.46

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
go build -mod vendor

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/rclone
cp COPYING %{buildroot}/usr/share/package-licenses/rclone/COPYING
cp docs/content/licence.md %{buildroot}/usr/share/package-licenses/rclone/docs_content_licence.md
cp vendor/bazil.org/fuse/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_bazil.org_fuse_LICENSE
cp vendor/cloud.google.com/go/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_cloud.google.com_go_LICENSE
cp vendor/github.com/Azure/azure-pipeline-go/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_github.com_Azure_azure-pipeline-go_LICENSE
cp vendor/github.com/Azure/azure-storage-blob-go/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_github.com_Azure_azure-storage-blob-go_LICENSE
cp vendor/github.com/Azure/go-ansiterm/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_github.com_Azure_go-ansiterm_LICENSE
cp vendor/github.com/Unknwon/goconfig/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_github.com_Unknwon_goconfig_LICENSE
cp vendor/github.com/a8m/tree/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_github.com_a8m_tree_LICENSE
cp vendor/github.com/abbot/go-http-auth/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_github.com_abbot_go-http-auth_LICENSE
cp vendor/github.com/anacrolix/dms/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_github.com_anacrolix_dms_LICENSE
cp vendor/github.com/aws/aws-sdk-go/LICENSE.txt %{buildroot}/usr/share/package-licenses/rclone/vendor_github.com_aws_aws-sdk-go_LICENSE.txt
cp vendor/github.com/coreos/bbolt/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_github.com_coreos_bbolt_LICENSE
cp vendor/github.com/cpuguy83/go-md2man/LICENSE.md %{buildroot}/usr/share/package-licenses/rclone/vendor_github.com_cpuguy83_go-md2man_LICENSE.md
cp vendor/github.com/davecgh/go-spew/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_github.com_davecgh_go-spew_LICENSE
cp vendor/github.com/djherbis/times/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_github.com_djherbis_times_LICENSE
cp vendor/github.com/dropbox/dropbox-sdk-go-unofficial/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_github.com_dropbox_dropbox-sdk-go-unofficial_LICENSE
cp vendor/github.com/goftp/server/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_github.com_goftp_server_LICENSE
cp vendor/github.com/golang/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_github.com_golang_protobuf_LICENSE
cp vendor/github.com/google/go-querystring/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_github.com_google_go-querystring_LICENSE
cp vendor/github.com/inconshreveable/mousetrap/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_github.com_inconshreveable_mousetrap_LICENSE
cp vendor/github.com/jlaffaye/ftp/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_github.com_jlaffaye_ftp_LICENSE
cp vendor/github.com/jmespath/go-jmespath/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_github.com_jmespath_go-jmespath_LICENSE
cp vendor/github.com/kardianos/osext/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_github.com_kardianos_osext_LICENSE
cp vendor/github.com/kr/fs/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_github.com_kr_fs_LICENSE
cp vendor/github.com/mattn/go-runewidth/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_github.com_mattn_go-runewidth_LICENSE
cp vendor/github.com/ncw/go-acd/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_github.com_ncw_go-acd_LICENSE
cp vendor/github.com/ncw/swift/COPYING %{buildroot}/usr/share/package-licenses/rclone/vendor_github.com_ncw_swift_COPYING
cp vendor/github.com/nsf/termbox-go/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_github.com_nsf_termbox-go_LICENSE
cp vendor/github.com/okzk/sdnotify/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_github.com_okzk_sdnotify_LICENSE
cp vendor/github.com/patrickmn/go-cache/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_github.com_patrickmn_go-cache_LICENSE
cp vendor/github.com/pengsrc/go-shared/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_github.com_pengsrc_go-shared_LICENSE
cp vendor/github.com/pkg/errors/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_github.com_pkg_errors_LICENSE
cp vendor/github.com/pkg/sftp/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_github.com_pkg_sftp_LICENSE
cp vendor/github.com/pmezard/go-difflib/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_github.com_pmezard_go-difflib_LICENSE
cp vendor/github.com/rfjakob/eme/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_github.com_rfjakob_eme_LICENSE
cp vendor/github.com/russross/blackfriday/LICENSE.txt %{buildroot}/usr/share/package-licenses/rclone/vendor_github.com_russross_blackfriday_LICENSE.txt
cp vendor/github.com/sevlyar/go-daemon/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_github.com_sevlyar_go-daemon_LICENSE
cp vendor/github.com/skratchdot/open-golang/LICENSE-MIT %{buildroot}/usr/share/package-licenses/rclone/vendor_github.com_skratchdot_open-golang_LICENSE-MIT
cp vendor/github.com/spf13/cobra/LICENSE.txt %{buildroot}/usr/share/package-licenses/rclone/vendor_github.com_spf13_cobra_LICENSE.txt
cp vendor/github.com/spf13/pflag/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_github.com_spf13_pflag_LICENSE
cp vendor/github.com/stretchr/testify/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_github.com_stretchr_testify_LICENSE
cp vendor/github.com/xanzy/ssh-agent/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_github.com_xanzy_ssh-agent_LICENSE
cp vendor/github.com/yunify/qingstor-sdk-go/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_github.com_yunify_qingstor-sdk-go_LICENSE
cp vendor/golang.org/x/crypto/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_golang.org_x_crypto_LICENSE
cp vendor/golang.org/x/net/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_golang.org_x_net_LICENSE
cp vendor/golang.org/x/oauth2/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_golang.org_x_oauth2_LICENSE
cp vendor/golang.org/x/sync/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_golang.org_x_sync_LICENSE
cp vendor/golang.org/x/sys/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_golang.org_x_sys_LICENSE
cp vendor/golang.org/x/text/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_golang.org_x_text_LICENSE
cp vendor/golang.org/x/time/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_golang.org_x_time_LICENSE
cp vendor/google.golang.org/api/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_google.golang.org_api_LICENSE
cp vendor/google.golang.org/api/googleapi/internal/uritemplates/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_google.golang.org_api_googleapi_internal_uritemplates_LICENSE
cp vendor/google.golang.org/appengine/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_google.golang.org_appengine_LICENSE
cp vendor/gopkg.in/yaml.v2/LICENSE %{buildroot}/usr/share/package-licenses/rclone/vendor_gopkg.in_yaml.v2_LICENSE
cp vendor/gopkg.in/yaml.v2/LICENSE.libyaml %{buildroot}/usr/share/package-licenses/rclone/vendor_gopkg.in_yaml.v2_LICENSE.libyaml
cp vendor/gopkg.in/yaml.v2/NOTICE %{buildroot}/usr/share/package-licenses/rclone/vendor_gopkg.in_yaml.v2_NOTICE

## install_append content
install -d %{buildroot}/usr/bin/
install -m0755 rclone %{buildroot}/usr/bin/
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/rclone

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/rclone/COPYING
/usr/share/package-licenses/rclone/docs_content_licence.md
/usr/share/package-licenses/rclone/vendor_bazil.org_fuse_LICENSE
/usr/share/package-licenses/rclone/vendor_cloud.google.com_go_LICENSE
/usr/share/package-licenses/rclone/vendor_github.com_Azure_azure-pipeline-go_LICENSE
/usr/share/package-licenses/rclone/vendor_github.com_Azure_azure-storage-blob-go_LICENSE
/usr/share/package-licenses/rclone/vendor_github.com_Azure_go-ansiterm_LICENSE
/usr/share/package-licenses/rclone/vendor_github.com_Unknwon_goconfig_LICENSE
/usr/share/package-licenses/rclone/vendor_github.com_a8m_tree_LICENSE
/usr/share/package-licenses/rclone/vendor_github.com_abbot_go-http-auth_LICENSE
/usr/share/package-licenses/rclone/vendor_github.com_anacrolix_dms_LICENSE
/usr/share/package-licenses/rclone/vendor_github.com_aws_aws-sdk-go_LICENSE.txt
/usr/share/package-licenses/rclone/vendor_github.com_coreos_bbolt_LICENSE
/usr/share/package-licenses/rclone/vendor_github.com_cpuguy83_go-md2man_LICENSE.md
/usr/share/package-licenses/rclone/vendor_github.com_davecgh_go-spew_LICENSE
/usr/share/package-licenses/rclone/vendor_github.com_djherbis_times_LICENSE
/usr/share/package-licenses/rclone/vendor_github.com_dropbox_dropbox-sdk-go-unofficial_LICENSE
/usr/share/package-licenses/rclone/vendor_github.com_goftp_server_LICENSE
/usr/share/package-licenses/rclone/vendor_github.com_golang_protobuf_LICENSE
/usr/share/package-licenses/rclone/vendor_github.com_google_go-querystring_LICENSE
/usr/share/package-licenses/rclone/vendor_github.com_inconshreveable_mousetrap_LICENSE
/usr/share/package-licenses/rclone/vendor_github.com_jlaffaye_ftp_LICENSE
/usr/share/package-licenses/rclone/vendor_github.com_jmespath_go-jmespath_LICENSE
/usr/share/package-licenses/rclone/vendor_github.com_kardianos_osext_LICENSE
/usr/share/package-licenses/rclone/vendor_github.com_kr_fs_LICENSE
/usr/share/package-licenses/rclone/vendor_github.com_mattn_go-runewidth_LICENSE
/usr/share/package-licenses/rclone/vendor_github.com_ncw_go-acd_LICENSE
/usr/share/package-licenses/rclone/vendor_github.com_ncw_swift_COPYING
/usr/share/package-licenses/rclone/vendor_github.com_nsf_termbox-go_LICENSE
/usr/share/package-licenses/rclone/vendor_github.com_okzk_sdnotify_LICENSE
/usr/share/package-licenses/rclone/vendor_github.com_patrickmn_go-cache_LICENSE
/usr/share/package-licenses/rclone/vendor_github.com_pengsrc_go-shared_LICENSE
/usr/share/package-licenses/rclone/vendor_github.com_pkg_errors_LICENSE
/usr/share/package-licenses/rclone/vendor_github.com_pkg_sftp_LICENSE
/usr/share/package-licenses/rclone/vendor_github.com_pmezard_go-difflib_LICENSE
/usr/share/package-licenses/rclone/vendor_github.com_rfjakob_eme_LICENSE
/usr/share/package-licenses/rclone/vendor_github.com_russross_blackfriday_LICENSE.txt
/usr/share/package-licenses/rclone/vendor_github.com_sevlyar_go-daemon_LICENSE
/usr/share/package-licenses/rclone/vendor_github.com_skratchdot_open-golang_LICENSE-MIT
/usr/share/package-licenses/rclone/vendor_github.com_spf13_cobra_LICENSE.txt
/usr/share/package-licenses/rclone/vendor_github.com_spf13_pflag_LICENSE
/usr/share/package-licenses/rclone/vendor_github.com_stretchr_testify_LICENSE
/usr/share/package-licenses/rclone/vendor_github.com_xanzy_ssh-agent_LICENSE
/usr/share/package-licenses/rclone/vendor_github.com_yunify_qingstor-sdk-go_LICENSE
/usr/share/package-licenses/rclone/vendor_golang.org_x_crypto_LICENSE
/usr/share/package-licenses/rclone/vendor_golang.org_x_net_LICENSE
/usr/share/package-licenses/rclone/vendor_golang.org_x_oauth2_LICENSE
/usr/share/package-licenses/rclone/vendor_golang.org_x_sync_LICENSE
/usr/share/package-licenses/rclone/vendor_golang.org_x_sys_LICENSE
/usr/share/package-licenses/rclone/vendor_golang.org_x_text_LICENSE
/usr/share/package-licenses/rclone/vendor_golang.org_x_time_LICENSE
/usr/share/package-licenses/rclone/vendor_google.golang.org_api_LICENSE
/usr/share/package-licenses/rclone/vendor_google.golang.org_api_googleapi_internal_uritemplates_LICENSE
/usr/share/package-licenses/rclone/vendor_google.golang.org_appengine_LICENSE
/usr/share/package-licenses/rclone/vendor_gopkg.in_yaml.v2_LICENSE
/usr/share/package-licenses/rclone/vendor_gopkg.in_yaml.v2_LICENSE.libyaml
/usr/share/package-licenses/rclone/vendor_gopkg.in_yaml.v2_NOTICE
