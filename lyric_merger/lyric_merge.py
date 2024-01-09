import os

if os.path.isdir("./lyrics") != True:
    os.mkdir("lyrics")
if os.path.isdir("./raw_lyrics") != True:
    os.mkdir("raw_lyrics")
else:
    title = input("input lyric filename:")
    jp_raw = open("raw_lyrics/" + title + '.txt', 'r', encoding='utf-8')
    en_raw = open("raw_lyrics/" + title + '_en.txt', 'r', encoding='utf-8')
    lyric_output = open("lyrics/" + title + '_lyric.txt', 'w',encoding='utf-8')

    jp = jp_raw.read().splitlines()
    en = en_raw.read().splitlines()

    mergelyric = []
    for i in range(len(jp)):
        try:
            mergelyric.append(en[i])
            mergelyric.append(jp[i])
        except:
            break

    for i in mergelyric:
        lyric_output.write(i + "\n")

