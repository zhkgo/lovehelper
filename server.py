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
app.run(port=10086)
