# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class CyborgThemePlugin(octoprint.plugin.AssetPlugin):

    def get_assets(self):
        return dict(
            css=["css/cyborg.css", "css/overrides-min.css", "css/bootstrap-modal.css"]
        )

__plugin_name__ = "Cyborg Theme"
__plugin_implementation__ = CyborgThemePlugin()