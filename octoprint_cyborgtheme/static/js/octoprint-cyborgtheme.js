$(function() {
    function CyborgThemePluginViewModel(parameters) {
        var self = this;

        $("body").eq(0).addClass("OctoPrintTheme-Cyborg")
        $("#settings_dialog").eq(0).addClass("Cyborgified_Settings")

        }	
		OCTOPRINT_VIEWMODELS.push([
        CyborgThemePluginViewModel,
		[]
		
    ]);
});