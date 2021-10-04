PKG_NAME := rclone
URL = https://github.com/rclone/rclone/releases/download/v1.56.2/rclone-v1.56.2.tar.gz
ARCHIVES = $(CGIT_BASE_URL)/projects/rclone-vendor/snapshot/rclone-vendor-1.56.2.tar.xz ./

include ../common/Makefile.common
