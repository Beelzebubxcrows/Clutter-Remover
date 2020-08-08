import os,shutil

list_files = os.listdir()

for i in list_files:
    if('.txt' in i or '.docx' in i or '.pdf' in i or '.rtf' in i or '.ppt' in i):
        cwd=os.getcwd()
        dir = os.path.join(cwd,"documents")
        if not os.path.exists(dir):
            os.mkdir(dir)
        shutil.move(i,dir)
        
        
    elif('.mp3' in i or '.wav' in i or '.flac' in i):
        cwd= os.getcwd()
        dir = os.path.join(cwd,"Audio_Files")
        if not os.path.exists(dir):
            os.mkdir(dir)
        shutil.move(i,dir)

    elif('.mp4' in i or '.flv' in i or '.3gp' in i or '.wmv' in i or '.avi' in i):
        cwd=os.getcwd()
        dir = os.path.join(cwd,"Video_Files")
        if not os.path.exists(dir):
            os.mkdir(dir)
        shutil.move(i,dir)

    elif('.exe' in i):
        cwd=os.getcwd()
        dir = os.path.join(cwd,"Applications")
        if not os.path.exists(dir):
            os.mkdir(dir)
        shutil.move(i,dir)

    elif('.parts' in i):
        cwd=os.getcwd()
        dir = os.path.join(cwd,"Part_files")
        if not os.path.exists(dir):
            os.mkdir(dir)
        shutil.move(i,dir)

    elif('.rar' in i or '.zip' in i):
        cwd=os.getcwd()
        dir = os.path.join(cwd,"Compressed_Files")
        if not os.path.exists(dir):
            os.mkdir(dir)
        shutil.move(i,dir)
        
    elif('.srt' in i):
        cwd=os.getcwd()
        dir = os.path.join(cwd,"Subtitles")
        if not os.path.exists(dir):
            os.mkdir(dir)
        shutil.move(i,dir)

    elif('.jpeg' in i or 'jpg' in i or 'png' in i or 'gif' in i or 'JPG' in i or 'trf' in i):
        cwd=os.getcwd()
        dir = os.path.join(cwd,"Images")
        if not os.path.exists(dir):
            os.mkdir(dir)
        shutil.move(i,dir)

    elif('.html' in i or '.css' in i or '.js' in i):
        cwd=os.getcwd()
        dir = os.path.join(cwd,"Webapge_files")
        if not os.path.exists(dir):
            os.mkdir(dir)
        shutil.move(i,dir)

    elif('.jar' in i or '.JAR' in i):
        cwd=os.getcwd()
        dir = os.path.join(cwd,"Java_files")
        if not os.path.exists(dir):
            os.mkdir(dir)
        shutil.move(i,dir)
    

    else:
        cwd=os.getcwd()
        
        dir = os.path.join(cwd,"Other_files")
        if (('.' in i) and (not 'Clutter' in i)):
            print(i)
            if not os.path.exists(dir):
                os.mkdir(dir)
            shutil.move(i,dir)
        
