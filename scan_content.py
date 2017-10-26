import requests
from multiprocessing.dummy import Pool as ThreadPool

def scan_content(url):
    r = requests.get(url)
    print(str(r.status_code)+'    '+url+'\n')

def read_file(file,url):
    global content
    content = []
    for line in file:
        tl = line.rstrip('\n')
        content.append(url+tl)
    del content[-0]
    return content
def main():
    url = input("Please enter url:")
    print ('-' * 60)
    try:
        file = open ('..//map//func//dir.txt','r',encoding='utf-8')
        #file = open ('dir.txt',encoding='utf-8')
    except IOError:
        print ('open file(dir.txt) fail!')
    else:
        if (url.strip()==''):
            url = 'https://www.baidu.com'
            read_file(file,url)
            pool = ThreadPool(2)
            pool.map(scan_content,content)
            pool.close()
            pool.join()
            #scan_content(content)
        else:
            read_file(file,url)
            pool = ThreadPool(2)
            pool.map(scan_content,content)
            pool.close()
            pool.join()
            #scan_content(content)
    print('scan end')

if __name__ == '__main__':
    main()
