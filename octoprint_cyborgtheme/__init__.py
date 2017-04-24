# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class CyborgThemePlugin(octoprint.plugin.AssetPlugin):

	def get_assets(self):
		return dict(
			css=["css/cyborg.css", "css/overrides-min.css", "css/bootstrap-modal.css"]
	)
	
	def get_update_information(self):
		return dict(
			cyborgtheme=dict(
				displayName="Cyborg Theme",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="ntoff",
				repo="Octoprint-CyborgTheme",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/ntoff/Octoprint-CyborgTheme/archive/{target_version}.zip"
		)
	)

__plugin_name__ = "Cyborg Theme"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = __plugin_implementation__ = CyborgThemePlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}