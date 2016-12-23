# coding: utf-8
__author__ = 'frendy'

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import jieba
import jieba.posseg as pseg
import os
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import traceback
import json
import csv
import codecs

news_ids = ["7547214", "7545969"]
#news_ids = ["7547214"]

if __name__ == "__main__":
	#############################文章处理
	# 加载文章数据
	corpus = [];
	for id in news_ids:
		try:
			content = open('./data/news/' + id + '.txt', 'rb').read()
			seg_list = jieba.cut(content, cut_all=False)
			corpus.append(" ".join(seg_list))
		except:
			#traceback.print_exc();
			if id != "":
				print 'Error: ' + str(id)
	
	#该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j]表示j词在i类文本下的词频
	vectorizer = CountVectorizer()
	#该类会统计每个词语的tf-idf权值
	transformer = TfidfTransformer()
	#第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵
	tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
	
	#获取词袋模型中的所有词语
	word = vectorizer.get_feature_names()
	#将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重
	weight = tfidf.toarray()
	
	#打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
	dict1 = {}
	for i in range(len(weight)):
		print "\n-------Article " + bytes(i) + " words and weights of tf-idf------\n"
		dict2 = {}
		for j in range(len(word)):
			print word[j], weight[i][j]
			dict2[word[j]] = weight[i][j]
		
		#初始化文章词汇和权重字典
		dict1[news_ids[i]] = dict2

		
	#############################评论处理
	for id in news_ids:
		try:
			print "\n-------Comments " + bytes(i) + " content and score------\n"
			c_f = file('./data/comments/' + id + '.json')
			comments = json.load(c_f);
			list = comments["RECORDS"]
			for item in list:
				#print item["content"]
				seg_list = jieba.lcut(item["content"], cut_all=False)
				score = 0.0
				for seg in seg_list:
					if dict1[id].has_key(seg):
						score = score + dict1[id][seg]
				score = score * 100 / len(seg_list)
				print '*****Comment: ' + item["content"] + '\n Score:' + bytes(score)			
		except:
			traceback.print_exc();
			if id != "":
				print 'Error comments: ' + str(id)
				
				
