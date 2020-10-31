from urllib.request import urlopen
import urllib.parse
import json  # 导入json模块，为了使下载的js文件更容易得到所需的信息
import time
import sys
import os
print('本程序由世界上最帅的赵铎然开发编写')
print('未经许可，禁止传播')
print('此程序应用到的爬虫技术属于侵权行为')
print("如有BUG，请联系开发者，感谢使用！")

# 导入sys和time模块是为了显示进度条

def Time_1():  # 进度条函数
    for i in range(1, 51):
        sys.stdout.write('\r')
        sys.stdout.write('{0}% |{1}'.format(int(i % 51) * 2, int(i % 51) * '■'))
        sys.stdout.flush()
        time.sleep(0.125)
    sys.stdout.write('\n')


def KuGou_music():
    keyword = urllib.parse.urlencode({'keyword': input('请输入歌名或歌星名:')})
    keyword = keyword[keyword.find('=') + 1:]
    url = 'https://songsearch.kugou.com/song_search_v2?callback=jQuery1124042761514747027074_1580194546707&keyword=' + keyword + '&page=1&pagesize=30&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0&_=1580194546709'
    content = urlopen(url=url)
    content = content.read().decode('utf-8')
    str_1 = content[content.find('(') + 1:-2]
    str_2 = json.loads(str_1)
    Music_Hash = {}
    Music_id = {}
    for dict_1 in str_2['data']['lists']:
        Music_Hash[dict_1['FileName']] = dict_1['FileHash']
        Music_id[dict_1['FileName']] = dict_1['AlbumID']
        # print(dict_1)

    list_music_1 = [music for music in Music_Hash]  # 匹配到的所有歌曲名  列表
    list_music = [music for music in Music_Hash]

    for i in range(len(list_music)):
        if '- <em>' in list_music[i]:
            list_music[i] = list_music[i].replace('- <em>', '-')
        if '</em>' in list_music[i]:
            list_music[i] = list_music[i].replace('</em>', '')
        if '<em>' in list_music[i]:
            list_music[i] = list_music[i].replace('<em>', '')

        # 使歌曲名称更加美观
        # 如： < em > 战狼 < / em > - 断情笔  经过这个处理之后     战狼 - 断情笔

    for i in range(len(list_music)):
        print("{}-:{}".format(i + 1, list_music[i]))

    music_id_1 = int(input('请输入你想下载的歌曲序号:'))

    # 'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash=E77548A33D7AF84F727C32A786C107D0&album_id=542163&dfid=2SSV0x4LWcsx0iylej1F6w7P&mid=44328d3dc4bfce21cf2b95cf9e76b968&platid=4'
    # 一个加载js文件的标椎式样网址

    url = 'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash=' + Music_Hash[
        list_music_1[music_id_1 - 1]] + '&album_id=' + Music_id[list_music_1[
        music_id_1 - 1]] + '&dfid=2SSV0x4LWcsx0iylej1F6w7P&mid=44328d3dc4bfce21cf2b95cf9e76b968&platid=4'
    js_content = urlopen(url=url)
    str_3 = js_content.read().decode('utf-8')  # 所加载的js中的内容
    dict_2 = json.loads(str_3)  # 将这个js格式转换成为字典格式

    try:
        music_href = dict_2['data']['play_backup_url']  # 下载的歌曲网址

        music_content = urlopen(url=music_href).read()
        try:
            os.mkdir('D:\酷狗音乐下载')
        except Exception as e:
            print(e, '但不要紧,程序仍然执行')
        finally:
            music_path = 'D:\酷狗音乐下载\\' + list_music[music_id_1 - 1] + '.mp3'  # 歌曲下载路径
            with open(music_path, 'wb') as f:
                print('正在下载当中...')
                f.write(music_content)
                Time_1()
                print('{}.mp3下载成功！'.format(list_music[music_id_1 - 1]))

    except:
        print('对不起，没有该歌曲的版权！')


if __name__ == '__main__':

    KuGou_music()
input()