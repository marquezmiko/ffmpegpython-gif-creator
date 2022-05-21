import sys
import ffmpeg

filepath = input('Enter input filename (including path)')
service = sys.argv[1]
print(service)


def gif_vid():
	(
		ffmpeg
		.input(filepath)
		.filter('fps', fps=15, round='up')
		.output(filepath+'_gifd.gif', format='gif')
	.run()
	)

def hflip_vid():
	stream = ffmpeg.input(filepath)
	stream = ffmpeg.hflip(stream)
	stream = ffmpeg.output(stream, filepath+'_hflip.mp4')
	ffmpeg.run(stream)

def vflip_vid():
	stream = ffmpeg.input(filepath)
	stream = ffmpeg.vflip(stream)
	stream = ffmpeg.output(stream, filepath+'_vflip.mp4')
	ffmpeg.run(stream)

def reformat_vid():
	newFormat = sys.argv[2]
	stream = ffmpeg.input(filepath)
	stream = ffmpeg.output(stream, filepath[:-4]+'_reformated.' + newFormat, format=newFormat)
	ffmpeg.run(stream)


if service == 'gif':
	gif_vid()
elif service == 'hflip':
	hflip_vid()
elif service == 'vflip':
	vflip_vid()
elif service == 'reformat':
	reformat_vid()