installdir = ../soundless
input_filename = Lull_Icon.png
input = ./original/$(input_filename)
output = .

all: android-icon.png android-ldpi-icon.png android-mdpi-icon.png android-hdpi-icon.png android-xhdpi-icon.png android-xxhdpi-icon.png

android-icon.png: 
	mogrify -path $(output) -resize 256x256 -quality 9 -filter point -format png $(input)
	mv $(output)/$(input_filename) $(output)/$@
android-ldpi-icon.png:
	mogrify -path $(output) -resize 36x36 -quality 9 -filter point -format png $(input)
	mv $(output)/$(input_filename) $(output)/$@
android-mdpi-icon.png:
	mogrify -path $(output) -resize 48x48 -quality 9 -filter point -format png $(input)
	mv $(output)/$(input_filename) $(output)/$@
android-hdpi-icon.png:
	mogrify -path $(output) -resize 72x72 -quality 9 -filter point -format png $(input)
	mv $(output)/$(input_filename) $(output)/$@
android-xhdpi-icon.png:
	mogrify -path $(output) -resize 96x96 -quality 9 -filter point -format png $(input)
	mv $(output)/$(input_filename) $(output)/$@
android-xxhdpi-icon.png:
	mogrify -path $(output) -resize 144x144 -quality 9 -filter point -format png $(input)
	mv $(output)/$(input_filename) $(output)/$@

install: all
	cp $(output)/android-*-icon.png $(installdir)

uninstall:
	rm $(installdir)/android-*icon.png

clean:
	rm $(output)/android-*icon.png
