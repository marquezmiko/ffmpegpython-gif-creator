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
	stream = ffmpeg.output(stream, 'output2.mp4')
	ffmpeg.run(stream)


if service == 'gif':
	gif_vid()
elif service == 'hflip':
	hflip_vid()