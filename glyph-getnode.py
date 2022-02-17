font = Glyphs.font
glyphA = font.glyphs['2EBE'] #yi6291 A0041 2EBE
print(glyphA)
print('Layer Num',len(glyphA.layers))
print(glyphA.layers[0])
print('Shape Num', len(glyphA.layers[0].shapes))
print('Component Num', len(glyphA.layers[0].components))

for shape in glyphA.layers[0].shapes:
	print(shape)
	for node in shape.nodes:
		print(node)
print(type(node))
#	shape.applyTransform((
#    0.5, # x scale factor
#    0.0, # x skew factor
#    0.0, # y skew factor
#    0.5, # y scale factor
#    0.0, # x position
#    0.0  # y position
#    ))
#	for node in shape.nodes:
#		print('after affine transformation')
#		print(node)

#print(glyphA.layers[0].shapes[0])
#shapeX = glyphA.layers[0].shapes[0]
#for node in shapeX.nodes:
#    print(node)

print('done')