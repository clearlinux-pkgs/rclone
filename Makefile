PKG_NAME := rclone
URL = https://github.com/rclone/rclone/releases/download/v1.54.1/rclone-v1.54.1.tar.gz
ARCHIVES = $(CGIT_BASE_URL)/projects/rclone-vendor/snapshot/rclone-vendor-1.54.0.tar.xz ./

include ../common/Makefile.common
