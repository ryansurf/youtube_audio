from pkgutil import get_data
import yt_dlp as youtube_dl

def get_mp3(link):
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = link, download = False
    )
    options = {
        'format' : 'bestaudio[ext=m4a]',
        'keepvideo' : False,
        #'outtmpl': '~/Desktop/%(title)s'+'.mp3',
        'no-check-certificate' : True,
        'nooverwrites': True,
    }


    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
        info_dict = ydl.extract_info(link, download=False)
        filename = ydl.prepare_filename(info_dict)
        video_title = info_dict.get('title', None)

    return filename, video_title





def get_video(link):
    video_info = youtube_dl.YoutubeDL().extract_info(
    url = link, download = False
    )

    options = {
                'no-check-certificate' : True,
                'format' : 'mp4', 
                'nooverwrites': True,
                }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([link])
        #ydl.download([video_info['webpage_url']])
        info_dict = ydl.extract_info(link, download=False)
        filename = ydl.prepare_filename(info_dict)
        video_title = info_dict.get('title', None)

    return filename, video_title

    