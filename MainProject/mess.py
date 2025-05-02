from matrix_image_editor import MatrixImgEdit as mie

editor = mie()
editor.load_grayscale('MainProject\img data\python-logo-symbol.png')
editor.right_shift(400)
editor.show()
