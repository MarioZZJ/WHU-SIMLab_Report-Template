# Jupyter notebook合并至实验报告

可以将Jupyter Notebook导出的tex与实验报告进行合并，生成较为美观、同时格式与学院要求近似的pdf版本实验报告。

关于Jupyter Notebook的使用与多格式导出，欢迎参考我的博文：[Hello Jupyter Notebook!](https://blog.mariozzj.cn/posts/0108/)

## 运行方法

进入`insert_notebook`目录后，运行`parse.py`并传递参数。

['notebook_dir','output_dir','template_dir','config_dir']

> `notebook_dir`：jupyter notebook导出的`.tex`文件地址。
>
> `output_dir`: 转换成功后的`.tex`文件地址。
> > 由于tex文件中很可能存在对外部图片资源等的引用，所以最好该文件与原notebook导出tex在同一目录下，以免引用失效。
> 
> `template_dir`（可选）:模板实验报告文件。默认为项目根目录下`template-config.tex`。
> 
> `config_dir`（可选）：配置文件。默认为当前目录下的`report_config.json`文件。该文件参数值为空。

## 配置文件

```json5
{
  "use": false, //是否使用配置文件插入信息
  "indent": false, //是否保持段落首行缩进2格
  "name": "", //姓名
  "StudentID": "", //学号
  "StudentGrade": "", //年级
  "tutor": "", //指导老师
  "major": "", //专业
  "labType": 1, //实验课类型 //该项暂未启用，可自行调整
  "labTerm": "", //实验学习
  "labWeek": "", //实验周
  "labHour": "", //实验学时数
  "courseName": "", //相关课程
  "projectName": "", //相关科研项目
  "labName": "", //实验名称

  "preview": {
    "use": false, //是否填入预习部分
    "theory": "", //实验原理
    "device": "", //主要仪器设备
    "goal": "", //实验目标
    "content": "" //实验内容
  },
  "summary": {
    "use": false, //是否填入实验总结
    "text": "" //实验总结内容
  }
}
```

配置文件须以此格式书写。样例见当前目录下`report_config.sample.json`[查看](./report_config.json)。

## 导出样例

在本目录下运行

```shell
$ python3 parse.py ./sample/Sample.tex ./sample/MergedReport.tex ./report_config.sample.json
```

可得到`MergedReport.tex`。继续使用xelatex转化为pdf：
```shell
$ xelatex -file-line-error -interaction=nonstopmode -synctex=1 -output-directory=../../out MergedReport.tex ./MergedReport.tex
```
可生成[pdf示例](../out/MergedReport.pdf)。


## 已知问题
1. json的部分内容填充只能加纯文本，暂不支持富文本格式导入。您可以自行更改内容。
2. 第一部分为表格形式，不可续页；二、三部分为fancybox可续页。如果第一部分填充太长会让表格超出页面，您可根据渲染效果调整内容。
3. 图片等内容默认以0.9页宽展示，可以自行调整宽度。
4. notebook中的表格如果本身列数过多，内容过长会超出页面，不能自动续页，需在notebook自行调整输出。

## 提示
1. 这个合并脚本比较简单，适合无latex基础同学使用。不过需要安装好latex环境和ctex等宏包，使用xelatex渲染。
2. 目前脚本在测试notebook中可以正常导出，但是仍然可能存在问题，欢迎提issue或PR。
3. 未来视精力和需求可能会将此功能做成在线版本，目前**懒**得写！不过欢迎有兴趣有能力有时间的同学联系我一起完善。

