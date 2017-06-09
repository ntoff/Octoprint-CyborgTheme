## Read before submitting an issue.

* Please look through the issues list (closed as well) to see if your issue already exists or was already fixed
* Please test against vanilla octoprint (ONLY this theme installed) as other plugins may interfere if they inject their own css styles.
* Please check your version against the latest version in the 'branches', perhaps your issue is already being worked on.

_"Plugin X looks funny after installing this theme"_

Some plugins inject their own conflicting CSS rather than relying on existing CSS, or add extra element id's that aren't present in vanilla octoprint's css. There's not much I can do about that. 

Or it could simply be a case that I missed something, or was a little too broad in selecting which elements to apply certain things to. In this case, go ahead and post a bug report.

_"Can you add an override for plugin X"_

I could, but I probably won't. I have to draw the line somewhere. I don't want this to end up as a hack job with overrides overriding overrides, and be forever chasing down issues with every new plugin that decides to override one of the standard css elements for no good reason.

##### Bug reports:

Please include:
* octoprint version (especially if you're using a non-release development version)
* theme plugin version
* be as descriptive as possible (perhaps also screenshots will help)