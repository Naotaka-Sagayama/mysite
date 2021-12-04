import os
import glob
import jaconv


#****************************
# ＜設定＞
ENV_TGT_PATH = './test見積書' #対象パス
# ENV_TGT_PATH = 'D:/test/test1'
ENV_LOG_FILE = './result.log' #ログファイル
ENV_ERR_LOG_FILE = './error.log' #ログファイル


#****************************
# ＜処理内容＞
# ログ出力
# ＜引数＞
# msg:出力内容
#
def writeLog(logpath, msg): #「defで関数の定義」


    f = open(logpath, 'a', encoding='UTF-8')    #「open(ファイル名, オプション, 文字エンコード)▶ファイルの新規作成、保存、書き込み」
    
    try:    #「try,exceptで例外処理してるらしいけど、よく分からん」
        f.write(msg + ' \n')
    except UnicodeEncodeError as e:
        # 例外が発生したらコンソールに表示
        print(e)
        print(type(e))


    f.close()


#****************************
# ＜処理内容＞
# 変更前パスと変更後パスのログを出力する
# ＜引数＞
# before_path:変更前パス
# after_path:変更後パス
#
def writeChangeDirNameLog(before_path, after_path):
    writeLog(ENV_LOG_FILE, '【変更前】' + before_path + '\t' + '【変更後】' + after_path)


#****************************
# ＜処理内容＞
# エラーログ出力
# ＜引数＞
# msg:出力内容
#
def writeErrorLog(ENV_ERR_LOG_FILE, msg):
    writeLog('【エラー】' + msg)


#****************************
# ＜処理内容＞
# ディレクトリ名に使用できない文字を除外する
# ＜引数＞
# file_name:ディレクトリ名
# ＜戻り値＞
# ディレクトリ名
def cleansingDirName(file_name):


    cleansing_dir_name = file_name
    cleansing_dir_name = cleansing_dir_name.replace('\\', ' ')
    cleansing_dir_name = cleansing_dir_name.replace('/', ' ')
    cleansing_dir_name = cleansing_dir_name.replace(':', ' ')
    cleansing_dir_name = cleansing_dir_name.replace('*', ' ')
    cleansing_dir_name = cleansing_dir_name.replace('?', ' ')
    cleansing_dir_name = cleansing_dir_name.replace('"', ' ')
    cleansing_dir_name = cleansing_dir_name.replace('<', ' ')
    cleansing_dir_name = cleansing_dir_name.replace('>', ' ')
    cleansing_dir_name = cleansing_dir_name.replace('|', ' ')


    # 先頭と末尾の空白を除去して返す
    return cleansing_dir_name.strip()


#****************************
# ＜処理内容＞
# ファイル名が重複したら、先頭にアンダーバーを付与する
# ＜引数＞
# path:ファイルパス
# name:ファイル名
# ＜戻り値＞
# 重複しないファイルパス
def duplicateName(path, name):  #「このnameの使い方よく分からん」


    tgt_name = name
    tgt_path = os.path.join(path, name)


    while os.path.exists(tgt_path):
        tgt_name = '_' + tgt_name
        tgt_path = os.path.join(path, tgt_name)


    return tgt_path


#****************************
# ＜処理内容＞
# ディレクトリ名を全角から半角に変更する
# ＜引数＞
# tgt_path:対象パス
#
def changeFileNameToHankaku(tgt_path):


    #対象ディレクトリ配下を取得
    files = os.listdir(tgt_path)


    for f in files:


        #フルパスを取得
        full_path = os.path.join(tgt_path, f)


        #ファイル、かつ、全角文字があれば半角に変更
        if os.path.isfile(full_path):


            #変更後のディレクトリ名を取得
            #カタカナは半角にしない
            #数字は半角にする
            #アルファベットと記号は半角にする
            after_name = jaconv.z2h(f, kana=False, digit=True, ascii=True)


            # ファイルに使用できない文字を除去する
            after_name = cleansingDirName(after_name)


            # 変更後のパスを取得
            after_path = os.path.join(tgt_path, after_name)


            if after_path != full_path:


                # 重複しないファイル名に変更
                after_path = duplicateName(tgt_path, after_name)


                #ファイル名変更
                os.rename(full_path, after_path)
                writeChangeDirNameLog(full_path, after_path)


        #ディレクトリ、かつ、全角文字があれば半角に変更
        elif os.path.isdir(full_path):


            #サブディレクトリも変更する
            changeFileNameToHankaku(full_path)
        else:
            writeErrorLog(ENV_ERR_LOG_FILE, 'ファイルでもフォルダでもありません:' + full_path)


#****************************
# メイン処理
#****************************
changeFileNameToHankaku(ENV_TGT_PATH)

#****************************
# アンダーバーに変換
#****************************
#ファイル名に含まれる変更したい単語と変更後の単語
before_word = ["     ","    ","   ","  "," "]
after_word = "_"

for i in before_word:
    #ファイルを取得する
    files_2 = glob.glob('./test見積書/*'+ i +'*')
    #print(files_2)

    #before_wordの単語をafter_wordに変更
    for before_file_name in files_2:
        after_file_name = before_file_name.replace(i,after_word)
        os.rename(before_file_name,after_file_name)
