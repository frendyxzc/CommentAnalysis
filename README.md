# CommentAnalysis
文章评论分析
`python`
`jieba`
`sklearn`
`flask`

<br>

## 训练生成服务

1.文章全集tf-idf词语权重统计 <br>
2.评论相关性分数计算，取两个极端，分数低的计入通配表，分数高的依据标签记入一个表（标签归类评论，方便使用）<br>

## 使用服务

1.通配库取评论，根据标签取评论 <br>
2.根据权重字典计算相关性得分 <br>
3.根据得分选用（选极低和极高）<br>

<br>
<br>

## Todo List

1.搭建服务