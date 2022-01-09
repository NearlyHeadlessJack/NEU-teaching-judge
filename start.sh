#!/bin/bash
echo -n "请输入您的学号:"
read id
echo -n "请输入您的密码:"
read password

echo -n "请输入需要评教的教师姓名:"

while read name
do
	python3 pj.py $id $password $name
	echo -n "评教成功，请输入下一位老师姓名:"
done
echo -n "谢谢使用！"