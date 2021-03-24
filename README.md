# WHU-SIMLab_Report
 Template lab report for undergraduate students at WHU-SIM. 

武汉大学信息管理学院实验报告（本科生）。

## 项目结构

```
 ·
 ┠──── /template.docx  MS Office Word版本实验报告（来源：实验中心）
 ┠──── /template-docx.pdf  Word版本实验报告输出pdf
 ┠──── /template.tex  Latex版本实验报告（作者拟合，完善中）
 ┠──── /template-config.tex Latex版本实验报告（供合并脚本使用配置版，作者拟合，完善中）
 ┠──── /insert_notebook  将jupyter notebook导出的tex插入实验报告的程序，见该文件夹下readme
 ┠──── /out/
         ┠──── template.pdf     Latex版本实验报告输出pdf
         ┗──── MergedReport.pdf 脚本合并Jupyter Notebook输出实验报告pdf
```

请自行配置好latex环境后使用，安装好必要的包。本项目不提供任何环境配置方面的帮助。

> 个人捏合的模板，有一些没有优化到的细节或bug，欢迎issue、PR。

## 更新日志

* Mar 6th, 2021
  * 上传基础版本。实验报告四板块。
* Mar 24th, 2021
  * 进行了细节修改，增加了默认首行缩进。
  * 增加了合并jupyter notebook导出tex功能。同时上传了样例脚本文件和导出文件。