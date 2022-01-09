#!/bin/bash
echo -n "请输入您的学号:"
read id
echo -n "请输入您的密码:"
read password

echo -n "请输入需要评教的教师姓名（输入0停止）"
read name
while(( $name!=5 ))
do
	python3 pj.py id password
	echo -n "评教成功！"
done
echo -n "谢谢使用！"