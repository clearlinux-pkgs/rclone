PKG_NAME := rclone
URL = https://github.com/rclone/rclone/releases/download/v1.58.0/rclone-v1.58.0.tar.gz
ARCHIVES = $(CGIT_BASE_URL)/projects/rclone-vendor/snapshot/rclone-vendor-1.58.0.tar.xz ./

include ../common/Makefile.common
