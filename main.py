import sys
import ffmpeg

#filepath = input('Enter input filename (including path)')
service = sys.argv[1]
print(service)
if service == 'gif':
	gif_vid()
elif service == 'flip':
	flip_vid()

def gif_vid():
	print('giffing')

def flip_vid():
	stream = ffmpeg.input(filepath)
	stream = ffmpeg.vflip(stream)
	stream = ffmpeg.output(stream, 'output2.mp4')
	ffmpeg.run(stream)