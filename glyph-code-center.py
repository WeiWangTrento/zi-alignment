# run this code in glyph app.

MacroTab.title = "zi-alignment"

# ['钅','艹']
targetList = ['9485','8279']

font = Glyphs.font
layer = font.selectedLayers[0]

for x in targetList:
	glyph = font.glyphs[x]
	boxGlyph = glyph.layers[layer.layerId].bounds
	print('==========', glyph.string, glyph.unicode, '==========')
	print('boxGlyph Origin:', boxGlyph.origin.x, boxGlyph.origin.y)
	print('boxGlyph Size:', boxGlyph.size.width, boxGlyph.size.height, '\n')

	# Origin X Always start form Baseline(X = 0)
	# Origin Y comes from designer's Metrics settings (the Descender)
	print('boxImage Origin:', 0.0, layer.descender) 

	# glyph Width comes from shapes and Sidebearing settings
	# glyph Height comes from designer's Metrics settings
	glyphHeight = layer.ascender - layer.descender
	print('boxImage Size:', layer.width, glyphHeight, '\n')


