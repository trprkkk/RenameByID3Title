import os
import eyed3

# スクリプトファイルのパスから親ディレクトリを取得
script_dir = os.path.dirname(os.path.abspath(__file__))

# フォルダのパスを指定
folder_path = script_dir  # スクリプトファイルのあるフォルダを使用

# フォルダ内のすべての.mp3ファイルを取得
mp3_files = [f for f in os.listdir(folder_path) if f.endswith(".mp3")]

# 各ファイルに対してID3v2タグからタイトルを取得してファイル名を変更
for filename in mp3_files:
    file_path = os.path.join(folder_path, filename)
    
    # ID3v2タグを読み込む
    audiofile = eyed3.load(file_path)
    
    # タイトルが存在する場合、ファイル名を変更
    if audiofile and audiofile.tag and audiofile.tag.title:
        new_title = audiofile.tag.title
        new_filename = new_title + ".mp3"
        new_file_path = os.path.join(folder_path, new_filename)
        
        # ファイル名を変更
        os.rename(file_path, new_file_path)
        print(f"ファイル名を変更: {filename} -> {new_filename}")
    else:
        print(f"ID3タグのタイトルが存在しないため、ファイル名を変更できません: {filename}")



