# github-search
python编写的爬虫，用于爬取github上搜索中的内容，分为scan.py 和download.py俩部分

scan.py可以实现对搜索内容的爬取，并且保存信息到data.json文件中
在图中scan.py添加apiaccess_token的值
down<img width="960" alt="image" src="https://github.com/wrongwe/github-search/assets/134288619/6fe1bf95-c087-449b-aed6-d9f2ae7799cd">

在对应路径下命令行模式中打开scan.py文件输入python .\scan.py
<img width="1044" alt="image" src="https://github.com/wrongwe/github-search/assets/134288619/8684d3e5-3e2d-4b8a-a9c6-86283663f0b3">

load.py可以实现对data.json文件中所保存的仓库进行下载并创建且保存到download.zip文件中
