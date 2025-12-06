import requests
import re
import json

'''
爬取哔哩哔哩视频（音频文件 和 视频文件）
'''


url = r'https://www.bilibili.com/video/BV1S7LVzGEZg/?vd_source=b4387356af6e40475182e5245bcafe50'
headers = {
    "cookie": "buvid3=50080445-F77F-DF2B-6BA9-81B21791D65747321infoc; b_nut=1764489247; bsource=search_google; _uuid=DD9DDB66-9B110-3910F-7B7F-14525E17241848669infoc; buvid_fp=a3b1df86fa41e32c27d36e005570fec3; home_feed_column=5; browser_resolution=1920-928; bmg_af_switch=1; bmg_src_def_domain=i0.hdslb.com; buvid4=3CAD7612-77B9-17B7-E3DA-A25F063215E153404-025113015-KvvsqI5d0iM7wcDCk2Wprw%3D%3D; CURRENT_QUALITY=0; rpdid=|(J~lu)J)ull0J'u~YRR)mk~Y; SESSDATA=aac2e8e9%2C1780041395%2Cddccc%2Ab1CjCme9ru64i_Xn0MlBr8y8qF3xX37fb3mAmGAKBYyBpRNJxlHN14K6aAyz2PAnnQCP0SVk52bXVsbVEwcDZNbmlKUFRtODc2YW1idGRnWDZKRkY4YTlyMGFxeUtwZ0ZjRzUyajdwTW1BT1NkZDB2aVJ0ekFCd21vZ0toUkhDeXAza2JCUDREMUpnIIEC; bili_jct=375bd42ee73e1a83ac70f80f095ec9c9; DedeUserID=509875061; DedeUserID__ckMd5=789509c2a2a527f0; sid=7gdxmrbu; theme-tip-show=SHOWED; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NjQ3NTc1OTgsImlhdCI6MTc2NDQ5ODMzOCwicGx0IjotMX0.CalIBRkCwrfYv0Wwm-lGDqmeY7BkQY20kdxtE2tHhIk; bili_ticket_expires=1764757538; CURRENT_FNVAL=4048; b_lsid=C17FB66B_19ADA433077",
    'referer': 'https://www.bilibili.com',
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
}
content = requests.get(url, headers=headers)
content.encoding = 'utf-8'
playinfo = re.findall('<script>window.__playinfo__=(.*?)</script>', content.text)[0]
playinfo_json = json.loads(playinfo)

audio_url = playinfo_json['data']['dash']['audio'][0]
video_url = playinfo_json['data']['dash']['video'][0]

with open('/Users/liujie/PycharmProjects/learn-python3/src/crawer/video/audio.mp3', mode='wb') as f:
    audio_response = requests.get(url=audio_url['baseUrl'], headers=headers)
    f.write(audio_response.content)

with open('/Users/liujie/PycharmProjects/learn-python3/src/crawer/video/video.mp4', mode='wb') as f:
    video_response = requests.get(url=video_url['baseUrl'], headers=headers)
    f.write(video_response.content)
