# pythonで作ったスクリプト置き場

## Lyric Merger
洋楽の歌詞と訳を1:1で対応させます

### 使い方
1. ```lyric_merge.py```を実行
2. ```raw_lyrics```ディレクトリが生成されるのでそこに```"曲名".txt```,```"曲名_en".txt```を作って入れる。
  それぞれ"```曲名".txt```は訳、```"曲名_en".txt```には歌詞を入れる。
3. 再度```lyric_merge.py```を実行
4. profit
### 注意
訳と歌詞の行数が一致していないと対応させた際にズレるのでその際は別途フォーマットを整える必要あり
