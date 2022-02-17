# add code here
MacroTab.title = "zi-alignment"

# ['钅','艹']
targetList = ['9485','8279']

font = Glyphs.font
#layer = font.selectedLayers[0]

for x in targetList:
	glyph = font.glyphs[x]
	#boxGlyph = glyph.layers[layer.layerId].bounds
	boxGlyph = glyph.layers[0].bounds
	print('==========', glyph.string, glyph.unicode, '==========')
	print('boxGlyph Origin:', boxGlyph.origin.x, boxGlyph.origin.y)
	print('boxGlyph Size:', boxGlyph.size.width, boxGlyph.size.height, '\n')

	# Origin X Always start form Baseline(X = 0)
	# Origin Y comes from designer's Metrics settings (the Descender)
	#print('boxImage Origin:', 0.0, layer.descender) 
	print('boxImage Origin:', 0.0, glyph.layers[0].descender) 
	
	# glyph Width comes from shapes and Sidebearing settings
	# glyph Height comes from designer's Metrics settings
	#glyphHeight = layer.ascender - layer.descender
	glyphHeight = glyph.layers[0].ascender - glyph.layers[0].descender
	#print('boxImage Size:', layer.width, glyphHeight, '\n')
	print('boxImage Size:', glyph.layers[0].width, glyphHeight, '\n')