# NEU-teaching-judge
<img src="https://img.shields.io/badge/License-MIT-green" alt=""> 
<img src="https://img.shields.io/badge/platform-macOS%7CLinux%20-blue" alt=""> 
这是用来应付每学期末教务处要求的“量化评教”的半自动脚本。

基于微软开源项目[Playwright](https://github.com/microsoft/playwright)，因此本脚本所需要的依赖有：Python3.6+ | Playwright( 1.17.1 )
# 说明
## 关于Playwright的安装
Playwright安装分为两步，第一步是安装Playwright本体，第二步是安装所使用到的浏览器内核。
```Shell
# 第一步：
pip install playwright
# 第二步：
python -m playwright install
```
如果下载速度过慢，可以考虑将第一步替换为清华大学源
```Shell
pip install playwright -i https://pypi.tuna.tsinghua.edu.cn/simple
```
第二步则需要参考[这篇博客](https://blog.csdn.net/qq_37673575/article/details/113978787?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522164174943116780271590806%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=164174943116780271590806&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~rank_v31_ecpm-5-113978787.pc_search_result_cache&utm_term=playwright&spm=1018.2226.3001.4187)将包提前下载好后使用
## 脚本使用
输入学号与密码后便开始评教，默认打满分并评价“很好！”。评测需要老师的姓名，请准确输入老师的姓名。<br>
完成一个老师的量化评教后会提示输入下一个老师的姓名。
关于如何能将输入老师姓名这一步骤也省去从而变成一个全自动的评教工具，欢迎各位同学发起[PR](https://github.com/NearlyHeadlessJack/NEU-teaching-judge/pulls)或者[提出issue](https://github.com/NearlyHeadlessJack/NEU-teaching-judge/issues)。
# 使用方法
**请先设置好Python3.6+环境与Playwright后使用以下代码**
## Linux/macOS(需要wget)
Shell中输入以下代码
```Shell
curl -fsSL https://gitee.com/NHJ2001/NEU-teaching-judge/raw/main/install.sh | sh
```
## Windows
PowerShell中输入以下代码
```PowerShell
待更新
```
# License
MIT © [@NearlyHeadlessJack](https://github.com/NearlyHeadlessJack) ([Gitee](https://gitee.com/NHJ2001)仅用于加速国内访问)







