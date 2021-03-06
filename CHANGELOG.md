*Happypanda v0.25*
- Added *Show in folder* entry in gallery contextmenu
- Gallery popups
	+ A contextmenu will now be shown when you rightclick a gallery
	+ Added *Skip* button in the metadata gallery chooser popup (the one asking you which gallery you want to extract metadata from)
	+ The text in metadata gallery chooser popups will now wrap
	+ Added tooltips displaying title and artist when hovering galleries in some popups
- Settings
	+ A new button allowing you to recreate your thumbnail cache is now in *Settings* -> *Advanced* -> *Gallery*
	+ Added new tab *Downloader* in *Web* section
	+ Renamed *General* tab in *Web* section to *Metadata*
	+ Some options in settings will now show a tooltip explaining the option on hover
- You can now go back to previous or to next search terms with the two new buttons beside the search bar (hidden until you actually search something)
	+ Back and Forward keys has been bound to these two buttons (very OS dependent but something like `ALT + LEFT ARROW` etc.) Back and Forward buttons on your mouse should also probably work (*shrugs*)
	+ Added *Use current gallery link* checkbox option in *Web* section
- Toolbar
	+ Renamed *Misc* to *Tools*
	+ New *Scan for new galleries* entry in *Gallery*
	+ New *Gallery Downloader* entry in *Tools*
- Gallery downloading
	+ Supports archive and torrent downloading
	+ archives will be automatically imported while torrents will be sent to your torrent client
	+ Currently supports ex/g.e gallery urls and panda.chaika.moe gallery/archive urls
		- Note: downloading archives from ex/g.e will be handled the same way as if you did it in your browser, i.e. it will cost you GP/credits.
- Tray icon
	+ You can now manually check for a new update by right clicking on the tray icon
	+ Triggering the tray icon, i.e. clicking on it, will now activate (showing it) the Happypanda window
- Fixed bugs:
	+ Fixed a bug where skipped galleries/paths would get moved
	+ Fixed a bug where gallery archives/folders containing images with `.jpeg` and/or capitalized (`.JPG`, etc.) extensions were treated as invalid gallery sources, or causing the program to behave very weird if they managed to get imported somehow
	+ Fixed a bug where you couldn't search with the Regex option turned on
	+ Fixed a bug where changing gallery covers would fail if the previous cover was not deleted or found.
	+ Fixed a bug where non-existent monitored folders were not detected
	+ Fixed a bug in the user settings (*settings.ini*) parsing, hence the reset
	+ Fixed other minor misc. bugs

*Happypanda v0.24.1*
- Fixed bugs:
	+ Removing a gallery and its files should now work
	+ Popups was staying on top of all windows

*Happypanda v0.24*
- Mostly gui fixes/improvements
	+ Changed toolbar style and icons
	+ Added new native spinners
	+ Added spinner for the metadata fetching process
	+ Added spinner for initial load
	+ Added spinner for DB activity
	+ Removed sort contextmenu and added it to the toolbar
	+ Removed some space around galleries in grid view
	+ Added kinetic scrolling when scrolling with middlemouse button
- New DB Overview window and tab in settings dialog
	+ you can now see all namespaces and tags in the `Namespace and Tags` tab
- Pressing the return-key will now open selected galleries
- New options in settings dialog
	+ Make extracting archives before opening optional in `Application -> General`
	+ Open chapters sequentially or all at once in `Application -> General`
- Added a confirmation when closing while there is still DB activity to avoid data loss
- Added log file rotation
	+ When happypanda.log reaches `10 mb` a new file will be made (rotating between 3 files)
- Fixed bugs:
	+ Temporarily fixed a critical bug where galleries wouldn't load
	+ Fixed a bug where the tray icon would stay even after closing the application
	+ Fixed a bug where clicking on a tag with no namespace in the Gallery Metdata Popup would search the tag with a blank namespace
	+ Fixed a minor bug where when opening the settings dialog a small window would appear first in a split second

*Happypanda v0.23*
- Stability and perfomance increase for very large libraries
	+ Instant startup: Galleries are now lazily loaded
	+ Application now supports very large galleries (tested with 10k galleries)
	+ Gallery searching will now scale with amount of galleries (means, no freezes when searching)
	+ Same with adding new galleries.
- The gallery window appearing when you click on a gallery is now interactable
	+ Clicking on a link will open it in your default browser
	+ Clicking on a tag will search for the tag
- Added some animation and a spinner
- Fixed bugs:
	+ Fixed critical bug where slected galleries were not mapped properly. (Which sometimes resulted in wrong galleries being removed)
	+ Fixed a bug where pressing CTRL + A to select all galleries would tell that i has selected the total amount of galleries multipled by 3
	+ Fixed a bug where the notificationbar would sometiems not hide itself
	+ & other minor bugs

*Happypanda v0.22*
- Added support for .rar files.
	+ To enable rar support, specify the path to unrar in Settings -> Application -> General. Follow the instructions for your OS.
- Fixed most (if not all) gallery importing issues
- Added a way to populate form archive.
	+ Note: Subfolders will always be treated as galleries when populating from an archive.
- Fixed a bug where users who tries Happypanda for the first time would see the 'rebuilding galleries' dialog.
- & other misc. changes

*Happypanda v0.21*
- The application will now ask if you want to view skipped paths after searching for galleries
- Added 'delete successful' in the notificationbar
- Bugfixes:
	+ Fixed critical bug: Could not open chapters
		+ If your gallery still won't open then please try re-adding the gallery.
	+ Fixed bug: Covers for archives with no folder in-between were not being found
	+ & other minor bugs

*Happypanda v0.20*
- Added support for recursively importing of galleries (applies to archives)
	+ Directories in archives will now be noticed when importing
	+ Directories with archives as chapters will now be properly imported
- Added drag and drop feature for directories and archives
- Galleries that was unsuccesful during gallery fetching will now be displayed in a popup
- Added support for directory or archive ignoring
- Added support for changing gallery covers
- Added: move imported galleries to a specified folder feature
- Increased speed of Populate from folder and Add galleries...
- Improved title parser to now remove unneecessary whitespaces
- Improved gallery hashing to avoid unnecessary hashing
- Added 'Add archive' button in chapter dialog
- Popups will now center on parent window correctly
	+ It is now possible to move popups by leftclicking and dragging
	+ Added background blur effect when popups are shown
- The rebuild galleries popup will now show real progress
- Settings:
	+ Added new option: Treat subfolders as galleries
	+ Added new option: Move imported galleries
	+ Added new option: Scroll to new galleries (disabled)
	+ Added new option: Open random gallery chapters
	+ Added new option: Rename gallery source (disabled)
	+ Added new tab in Advanced section: Gallery
	+ Added new options: Gallery renamer (disabled)
	+ Added new tab in Application section: Ignore
	+ Enabled General tab in Application section
	+ Reenabled Display on gallery options
- Contextmenu:
	+ When selecting more galleries only options that apply to selected galleries will be shown
	+ It is now possible to favourite/Unfavourite selected galleries
	+ Reenabled removing of selected galleries
	+ Added: Advanced and Change cover
- Updated database to version 0.2
- Bugfixes:
	+ Fixed critical bug: not being able to add chapters
	+ Fixed bug: removing a chapter would always remove the first chapter
	+ Fixed bug: fetched metadata title and artist would not be formatted correctly
	+ & other minor bugs

*Happypanda v0.19*
- Improved stability
- Updated and fixed auto metadata fetcher:
    + Now twice as fast
    + No more need to restart application because it froze
    + Updated to support namespace fetching directly from the official API
- Improved tag autocompletion in gallery dialog
- Added a system tray to notify you about events such as auto metadata fetcher being done
- Sorting:
    + Added a new sort option: Publication Date
    + Added an indicator to the current sort option.
    + Your current sort option will now be saved
    + Increased pecision of date added
- Settings:
    + Added new options:
        * Continue auto metadata fetcher from where it left off
        * Use japanese title
    + Enabled option:
        * Auto add new galleries on startup
    + Removed options:
        * HTML Parsing or API
- Bugfixes:
    + Fixed critical bug: Fetching metadata from exhentai not working
    + Fixed critical bug: Duplicates were being created in database
    + Fixed a bug causing the update checker to always fail.

*Happypanda v0.18*
- Greatly improved stability
- Added numbers to show how many galleries are left when fetching for metadata
- Possibly fixed a bug causing the *"big changes are about to occur"* popup to never disappear
- Fixed auto metadata fetcher (did not work before)

*Happypanda v0.17*
- Improved UI
- Improved stability
- Improved the toolbar
-	+ Added a way to find duplicate galleries
	+ Added a random gallery opener
	+ Added a way to fetch metadata for all your galleries
- Added a way to automagically fetch metadata from g.e-/exhentai
	+ Fetching metadata is now safer, and should not get you banned
- Added a new sort option: Date added
- Added a place for gallery hashes in the database
- Added folder monitoring support
	+ You will now be informed when you rename, remove or add a gallery source in one of your monitored folders
	+ The application will scan for new galleries in all of your monitored folders on startup
- Added a new section in settings dialog: Application
	+ Added new options in settings dialog
	+ Enabled the 'General' tab in the Web section
- Bugfixes:
	+ Fixed a bug where you could only open the first chapter of a gallery
	+ Fixed a bug causing the application to crash when populating new galleries
	+ Fixed some issues occuring when adding archive files
	+ Fixed some issues occuring when editing galleries
	+ other small bugfixes
- Disabled gallery source type and external program viewer icons because of memory leak (will be reenabled in a later version)
- Cleaned up some code

*Happypanda v0.16*
- A more proper way to search for namespace and tags is now available
- Added support for external image viewers
- Added support for CBZ
- The settings button will now open up a real settings dialog
	+ Tons of new options are now available in the settings dialog
- Restyled the grid view
- Restyled the tooltip to now show other metadata in grid view
- Added troubleshoot, regex and search guides
- Fixed bugs:
	+ Application crashing when adding a gallery
	+ Application crashing when refreshing
	+ Namespace & tags not being shown correctly
	+ & other small bugs

*Happypanda v0.15*
- More options are now available in contextmenu when rightclicking a gallery
- It's now possible to add and remove chapters from a gallery
- Added a way to select more galleries
	+ More options are now available in contextmenu for selected galleries
- Added more columns to tableview
	+ Language
	+ Link
	+ Chapters
- Tweaked the grid view to reduce the lag when scrolling
- Added 1 more way to add galleries
- Already exisiting galleries will now be ignored
- Database will now try to auto update to newest version
- Updated Database to version 0.16 (breaking previous versions)
- Bugfixes

*Happypanda v0.14*
- New tableview. Switch easily between grid view and table view with the new button beside the searchbar
- Now able to add and read ZIP archives (You don't need to extract anymore).
	+ Added temp folder for when opening a chapter
- Changed icons to white icons
- Added tag autocomplete in series dialog
- Searchbar is now enabled for searching
	+ Autocomplete will complete series' titles
	+ Search for title or author
	+ Tag searching is only partially supported.
- Added sort options in contextmenu
- Title of series is now included in the 'Opening chapter' string
- Happypanda will now check for new version on startup
- Happypanda will now log errors.
	+ Added a --debug or -d option to create a detailed log
- Updated Database version to 0.15 (supports 0.14 & 0.13)
	+ Now with unique tag mappings
	+ A new metadata: times_read

*Happypanda v0.13*
- First public release