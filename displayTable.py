from i18n import en

# Function to generate the wikitext for the report page
# @param wiki - Language code for the wiki (eg: 'en', 'es', 'it')
# @param content - Python 2D array (nested list) containing table entries
def display_report( wiki, content ):
	wikitext = '{| class="wikitable sortable" style="width:100%; margin:auto;" \n |- \n'
	collen = len( content[0] )
	rowlen = len( content )

	for x in range( 0, collen ):
		wikitext = wikitext + '! ' + en[ str( content[0][x] ) ] + '\n'

	for x in range( 1, rowlen ):
		wikitext = wikitext + '|- \n'
		for i in range( 0, collen ):
			wikitext = wikitext + '| ' + str( content[x][i] ) + '\n'

	wikitext = wikitext + '|}'
	return wikitext
