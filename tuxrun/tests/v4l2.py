# vim: set ts=4
#
# Copyright 2022-present Linaro Limited
#
# SPDX-License-Identifier: MIT

from tuxrun.tests import Test


class V4L2(Test):
    devices = ["qemu-*", "fvp-aemva"]
    name = "v4l2"
    timeout = 25
    need_test_definition = True

    def render(self, **kwargs):
        kwargs["name"] = self.name
        kwargs["timeout"] = self.timeout

        return self._render("v4l2.yaml.jinja2", **kwargs)
