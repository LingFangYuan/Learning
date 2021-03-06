with open(r'test.txt', 'a') as f:
    f.write('hello, world\n')
with open(r'test.txt', 'r') as f:
    for line in f:
        print(line)


import os, stat, shutil

print("获得当前Python脚本工作的目录路径: os.getcwd()")
print(os.getcwd())
print("返回指定目录下的所有文件和目录名: os.listdir(r'c:\\')")
print(os.listdir(r'c:\\'))
# 创建单个目录
os.mkdir('test')
print("检验给出的路径是否是一个文件: os.path.isfile(r'test.txt')")
print(os.path.isfile(r'test.txt'))
print("检验给出的路径是否是一个目录: os.path.isdir(r'test')")
print(os.path.isdir(r'test'))
print("判断是否是绝对路径: os.path.isabs(r'c:\\')")
print(os.path.isabs(r'c:\\'))
print("检验路径是否真的存在: os.path.exits(r'f:\\Python')")
print(os.path.exists(r'f:\\Python'))
print("分离一个路径的目录名和文件名: os.path.split(r'/home/ling/Downloads/test.txt')")
print(os.path.split(r'/home/ling/Downloads/test.txt'))
print("分离扩展名: os.path.splitext(r'/home/ling/Downloads/test.txt')")
print(os.path.splitext(r'/home/ling/Downloads/test.txt'))
print("获取路径名: os.path.dirname(r'/home/ling/Downloads/test.txt')")
print(os.path.dirname(r'/home/ling/Downloads/test.txt'))
print("获取文件名: os.path.basename(r'/home/ling/Downloads/test.txt')")
print(os.path.basename(r'/home/ling/Downloads/test.txt'))
print("读取和设置环境变量: os.getenv('PATH')和os.putenv()")
print(os.getenv('PATH'))
print("给出当前平台使用的行终止符: os.linesep")
print(repr(os.linesep))
print("指示你正在使用的平台: os.name")
print(os.name)
# 重命名文件或者目录: os.rename(old, new)
os.rename(r'test.txt', r'test1.txt')
# 创建多级目录: os.makedirs(r'python\test')
os.makedirs(r'python\\test')
os.removedirs(r'python\\test')
print("获取文件属性: os.stat('test1.txt')")
print(os.stat('test1.txt'))
# 修改文件权限和时间戳: os.chmod('test1.txt', 'stat.S_IROTH')
print("获取文件大小: os.path.getsize('test1.txt')")
print(os.path.getsize('test1.txt'))
# 复制文件夹: shutil.copytree('test', 'test1')
shutil.copytree('test', 'test1')
# 复制文件: shutil.copyfile('test1.txt', 'test2.txt')
shutil.copyfile('test1.txt', 'test2.txt')
# 移动文件或目录: shutil.move('test2.txt', 'test3.txt')
shutil.move('test2.txt', 'test3.txt')

# 删除一个文件
os.remove('test1.txt')
os.remove('test3.txt')
# 删除多个空目录, shutil.rmtree('dir'): 空目录、有内容的目录都可以删除
os.rmdir('test')
os.rmdir('test1')