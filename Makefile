backgrounds:
	mogrify -path . -resize 800x600 -quality 9 -filter point -format png fullsize/*.png 

clean:
	rm bg_*.png
