# coding=utf8
from __future__ import unicode_literals

import random
import datetime

from flask import Flask, render_template,render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/type0/")
def type0():
	words="小草莓我好喜欢你，我们在一起吧"
	return render_template('type0.html', words=words)	

@app.route("/type1/")
def type1():
	words="青椒！|我|想见|你"
	music_url="https://love-1252419034.cos.ap-shanghai.myqcloud.com/love.mp3"
	date_start="2/20/2018 00:00:00"
	url_image="http://wx1.sinaimg.cn/large/006gFOhdly1fr0hdrzlolj30b40b4dg7.jpg"
	return render_template("type1.html",words=words,music_url=music_url,date_start=date_start,url_image=url_image)
@app.route("/type2/")
def type2():
	name1="青椒"   #表白方
	name2="草莓"   #被表白方
	name3="小草莓" #全称
	name4="工科男" #身份
	return render_template("type2.htm",name1=name1,name2=name2,name3=name3,name4=name4)
@app.route("/type3/")
def type3():
	wordlistl=[ ["我如果爱你——",
				"绝不像攀援的凌霄花，",
				"借你的高枝炫耀自己；",
				"我如果爱你——",
				"绝不学痴情的鸟儿，",
				"为绿荫重复单调的歌曲；"],
				["也不止像泉源，",
				"常年送来清凉的慰藉；",
				"也不止像险峰，",
				"增加你的高度，衬托你的威仪。",
				"甚至日光，",
				"甚至春雨。",
				"不，这些都还不够！"],
				["我必须是你近旁的一株木棉，",
				"作为树的形象和你站在一起。",
				"根，紧握在地下；",
				"叶，相触在云里。",
				"每一阵风过，",
				"我们都互相致意，"],
	]
	wordlistr=[["但没有人，",
				"听懂我们的言语。",
				"你有你的铜枝铁干，",
				"像刀，像剑，也像戟；",
				"我有我红硕的花朵，",
				"像沉重的叹息，",
				"又像英勇的火炬。"],
				["我们分担寒潮、风雷、霹雳；",
				"我们共享雾霭、流岚、虹霓。",
				"仿佛永远分离，",
				"却又终身相依。",
				"这才是伟大的爱情，",
				"坚贞就在这里："],
				["爱——",
				"不仅爱你伟岸的身躯，",
				"也爱你坚持的位置，",
				"足下的土地。",
				"    ————致橡树",
				" ",
				"大青椒永远爱你!"],
	]
	hearttime=400
	girlname="小草莓"
	words="我们在一起吧"
	accept="点击这里把我领回家"
	endwords="爱你"
	boyname="大青椒"
	return render_template("type3.html",hearttime=hearttime,wordlistl=wordlistl,wordlistr=wordlistr,girlname=girlname,words=words,accept=accept,endwords=endwords,boyname=boyname)
@app.route("/type4/")
def type4():
	wordlistl=[ ["我如果爱你——",
				"绝不像攀援的凌霄花，",
				"借你的高枝炫耀自己；",
				"我如果爱你——",
				"绝不学痴情的鸟儿，",
				"为绿荫重复单调的歌曲；"],
				["也不止像泉源，",
				"常年送来清凉的慰藉；",
				"也不止像险峰，",
				"增加你的高度，衬托你的威仪。",
				"甚至日光，",
				"甚至春雨。"],
				["不，这些都还不够！",
				"我必须是你近旁的一株木棉，",
				"作为树的形象和你站在一起。",
				"根，紧握在地下；",
				"叶，相触在云里。",
				"每一阵风过，",
				"我们都互相致意，"],
	]
	wordlistr=[["但没有人，",
				"听懂我们的言语。",
				"你有你的铜枝铁干，",
				"像刀，像剑，也像戟；",
				"我有我红硕的花朵，",
				"像沉重的叹息，",
				"又像英勇的火炬。"],
				["我们分担寒潮、风雷、霹雳；",
				"我们共享雾霭、流岚、虹霓。",
				"仿佛永远分离，",
				"却又终身相依。",
				"这才是伟大的爱情，",
				"坚贞就在这里：",
				"爱——",
				"不仅爱你伟岸的身躯，",
				"也爱你坚持的位置，",
				"足下的土地。",
				"    ————致橡树",
				" ",
				"大青椒永远爱你!"],
	]
	href1='https://user.qzone.qq.com/896378080'
	href2='https://user.qzone.qq.com/1127396695'
	name1='大青椒'
	name2='小草莓'
	return render_template("type4.html",wordlistl=wordlistl,wordlistr=wordlistr,name1=name1,name2=name2,href1=href1,href2=href2)

app.run(port=10086)
