# github-search

## python编写的爬虫，用于爬取github上搜索中的内容，分为scan.py 和download.py俩部分

## scan.py

###### scan.py可以实现对搜索内容的爬取，并且保存信息到data.json文件中

###### 在图中scan.py添加apiaccess_token的值

![image-20240123154642682](github-search/image-20240123154642682.png)

##### 在对应路径下命令行模式中打开scan.py文件输入

```shell
python .\scan.py 
Enter the start page number: 1 #设置起始位置，
Enter the end page number: 1 #设置终止位置，本脚本中设置每page为30个url，可以自己定义最大可到每页一百url，当然写多了会因为api的限制而爬取到空目标，建议少量多次爬取。
Enter the keyword you want to search: goby #设置搜索关键词
```

##### 如图

<img width="1044" alt="image" src="https://github.com/wrongwe/github-search/assets/134288619/8684d3e5-3e2d-4b8a-a9c6-86283663f0b3">

## download.py

##### download.py可以实现对data.json文件中所保存的仓库进行下载并创建且保存到download.zip文件中

如图在download.py添加apiaccess_token的值

![image-20240123152749410](github-search/image-20240123152749410.png)

##### 在对应路径下命令行模式中打开download.py文件输入

```shell
python .\download.py
```

##### 如图

![image-20240123152910718](github-search/image-20240123152910718.png)

## 完成后可以得到如下文件

![image-20240123153244239](github-search/image-20240123153244239.png)
