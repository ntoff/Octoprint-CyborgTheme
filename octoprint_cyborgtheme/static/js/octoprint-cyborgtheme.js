$(function() {
    function CyborgThemePluginViewModel(parameters) {
        var self = this;

        $("html").eq(0).addClass("Cyborg")
        
        if ($("#touch body").length == 1) {
            $("html").removeClass("Cyborg");
        }
        
    }	
	OCTOPRINT_VIEWMODELS.push([
        CyborgThemePluginViewModel
    ]);
});