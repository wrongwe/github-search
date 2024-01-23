# github-search

## python编写的爬虫，用于爬取github上搜索中的内容，分为scan.py 和download.py俩部分

## scan.py

###### scan.py可以实现对搜索内容的爬取，并且保存信息到data.json文件中

###### 在图中scan.py添加apiaccess_token的值

<img width="957" alt="image" src="https://github.com/wrongwe/github-search/assets/134288619/d54104e5-fa96-43c3-936d-6250e8a6a172">


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

<img width="960" alt="image" src="https://github.com/wrongwe/github-search/assets/134288619/2830fa83-4523-4c3e-bd3b-c12b319e9f6f">


##### 在对应路径下命令行模式中打开download.py文件输入

```shell
python .\download.py
```

##### 如图

![image-20240123152910718](https://github.com/wrongwe/github-search/assets/134288619/b799734d-f322-4cc0-8580-9e72924d98a6)


## 完成后可以得到如下文件

![image-20240123153244239](https://github.com/wrongwe/github-search/assets/134288619/3acd973a-e3a2-4d42-be76-e62e8061edcb)

