from youtubesearchpython import VideosSearch
from pytube import YouTube


previousprogress = 0
def on_progress(stream, chunk, bytes_remaining):
    global previousprogress
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining 

    liveprogress = (int)(bytes_downloaded / total_size * 100)
    if liveprogress > previousprogress:
        previousprogress = liveprogress
        print(f'{liveprogress}% Done !')

def yts(srch):
    videosSearch = VideosSearch(srch, limit = 20)
    print(f'Do you want to download:(yes, no, restart) ')
    for i in range(20):
        temp=videosSearch.result()['result'][i]['title']
        key=str(input(f'{temp}  ? '))
        if key=='yes':
            url=videosSearch.result()['result'][i]['link']
            return url
        if key=='restart':
            url=yts(str(input('Enter search term:  ')))
            return url

srch=str(input('Enter search term:  '))
url=yts(srch)
yt=YouTube(url)
qual=str(input('Choose the format (360p,720p,audio): '))
if qual=='audio':
    stream=yt.streams.get_audio_only()
else:
    stream = yt.streams.get_by_resolution(qual)
dtry=str(input('Enter the full file path:  '))
sze=stream.filesize
nm=stream.default_filename
sze=sze/1000000
print(f'Estimate file size will be {sze} bytes')
print(f'File name will be : {nm}')
yt.register_on_progress_callback(on_progress)
fname=srch+'.mp3'
if qual=='audio':
    stream.download(output_path=dtry,filename=fname,skip_existing=False)
else:
    stream.download(output_path=dtry)