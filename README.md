
# BigData Science Practical Training Course

<div align='right'><font size=2 color='gray'>Python For BigData @ <font color='blue'><a href='https://www.facebook.com/jskim.kr'>FB / jskim.kr</a></font>, [김진수](bigpycraft@gmail.com)</font></div>
<br>

## SBA 2019, Seoul Business Agency Innovation Growth Intensive Training

<img src="./images/img_main_front.png">

## Notice 
* [Homesite] : http://www.seoulit.or.kr/main/main.html
* [Sharings] : https://github.com/bigpycraft/sba19-seoulit
* [Password] : bigpycraft19

<hr>

## Innovation Growth Intensive Training
- Python Programming Basics
- Python Packages and Modules
- Data Processing and Analysis
- Web Cralwling
- Natural Language Processing
- Machine Learning
- Deep Learning

<hr>

## Python Develop Environment

<hr>

<h3> Python </h3>

<table align="left">
    <tr align="left">
        <td width="200">
            <a href="https://www.python.org/">
            <img src="./images/python-logo.png" width="150" />
            </a>
        </td>
        <td width="800">
<div align="left">
<b> Latest: Python 3.7.4</b>
<br/><br/>
- Download : https://www.python.org/downloads/windows/
<br/>
- Download the latest version 
<br/>
- Check the OS version & bit (32bit / 64bit)
</div></td>
    </tr>
</table>
<br/>


<hr>

<h3> PyCharm </h3>

<table align="left">
    <tr align="left">
        <td width="200">
            <a href="https://www.jetbrains.com/pycharm/">
            <img src="./images/pycharm-logo.png" width="150" />
            </a>
        </td>
        <td width="800">
<div align="left">
<b> Latest : Python 3.7 version | Release Date: July 24, 2019</b>
<br/><br/>
- Download : https://www.jetbrains.com/pycharm/download/
<br/>
- Version: 2019.2
<br/>
- Build: 192.5728.105
<br/>
- July 24, 2019
<br/>
- Download Community Version 
</div></td>
    </tr>
</table>
<br/>


<hr>

<h3> Jupyter Notebook </h3>

<table align="left">
    <tr align="left">
        <td width="200">
            <a href="https://www.anaconda.com/distribution/">
            <img src="./images/jupyter.jpg" width="150" />
            </a>
        </td>
        <td width="800">
<div align="left">
<b> Latest : Version 2019.07 | Release Date: July 25, 2019 </b>
<br/>
- Python 3.7 version
<br/>
- Filename : Anaconda3-2019.07-Windows-x86_64.exe
<br/>
- Download : https://www.anaconda.com/distribution/
<br/>
- Check the OS version & bit (32bit / 64bit)
</div>
<br/>
<div align="left">
<b> Recommand Previous: Version 5.2 | Release Date: May 30, 2018 </b>
<br/>
- Filename : Anaconda3-5.2.0-Windows-x86_64.exe
<br/>
- Download : https://repo.continuum.io/archive/ 
<br/>
- Reason : TF Requires Python 3.4, 3.5, or 3.6 
<br/>
- TensorFlow : https://www.tensorflow.org/install/pip
</div></td>
    </tr>
</table>
<br/>


<hr>

### Selenium WebDriver 

<table align="left">
    <tr align="left">
        <td width="200">
            <a href="https://www.seleniumhq.org/projects/webdriver/">
            <img src="./images/SeleniumHQ-logo.png" width="150" />
            </a>
        </td>
        <td width="800">
<div align="left">
    <b> - Selenium HQ </b> : https://www.seleniumhq.org/projects/webdriver/
    <br/><br/> - 아래 사이트에서 OS에 맞는 웹드라이브를 다운받아 압축을 풀어 driver 폴더에 복사
    <br/><br/>
    <b> 1. Chrome WebDriver </b> &nbsp;&nbsp; : <a href='http://chromedriver.chromium.org/downloads'>[다운로드1]</a>, &nbsp;&nbsp;&nbsp;<a href='https://sites.google.com/a/chromium.org/chromedriver/downloads'>[다운로드2]</a>
    <br/><br/>
    <b> 2. Firefox WebDriver </b> &nbsp;&nbsp;&nbsp;&nbsp; : <a href='https://github.com/mozilla/geckodriver/releases'>[다운로드]</a>
    <br/><br/>
    <b> 3. Microsoft WebDriver </b> : <a href='https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/'>[다운로드]</a>
    <br/><br/>
    <b> cf. 가장 보편적으로 많이 사용하는 크롬 웹드라이브를 다운받아서 설치한다. </b>
</div>
        </td>
    </tr>
</table>
<br/>


### Selenium 1.0 + WebDriver = Selenium 2.0
- HomeSite : https://www.seleniumhq.org/projects/webdriver/
- WebDriver is designed in a simpler and more concise programming interface along with addressing some limitations in the Selenium-RC API.
- WebDriver is a compact Object Oriented API when compared to Selenium1.0
- It drives the browser much more effectively and overcomes the limitations of Selenium 1.x which affected our functional test coverage, like the file upload or download, pop-ups and dialogs barrier
- WebDriver overcomes the limitation of Selenium RC's Single Host origin policy

<hr> 

### KoNLPy Install Guide  

<table align="left">
    <tr align="left">
        <td width="200">
            <a href="http://konlpy.org/ko/v0.5.0/install/">
            <img src="./images/konlpy.png" width="150" />
            </a>
        </td>
        <td width="800">
<div align="left">
    <b> 1. JAVA 환경 </b> : <a href="https://www.oracle.com/technetwork/java/javase/downloads/">JDK (>=1.8)</a> Install & JAVA Environmnmet Variable Setting
    <br/><br/>
    <b> 2. MS Visual C++ 설치 </b> : <a href="https://www.scivision.co/python-windows-visual-c++-14-required/">Build Tools for Visual Studio 2017 (>=14.0) </a> Install 
    <br/><br/>
    <b> 3. JPype 설치 </b> : <a href="https://www.lfd.uci.edu/~gohlke/pythonlibs/#jpype">JPype1  (>=0.5.7) </a>Install
    <br/> &nbsp;&nbsp; (Anaconda Prompt) C:\Users\user> <b> pip install --upgrade pip </b>
    <br/> &nbsp;&nbsp; (Anaconda Prompt) C:\Users\user> <b> pip install JPype1‑0.6.3‑cp36‑cp36m‑win_amd64.whl </b>
    <br/><br/>
    <b> 4. KoNLPy 설치 </b> :
    <br/> &nbsp;&nbsp; (Anaconda Prompt) C:\Users\user> <b> pip install konlpy </b>
</div>
        </td>
    </tr>
</table>
<br/>


<hr>

### JDK Install & JAVA Environment Setting

<table align="left">
    <tr align="left">
        <td width="200">
            <a href="https://www.oracle.com/technetwork/java/javase/downloads/">
            <img src="./images/java-se-downloads-1612441.gif" width="150" />
            </a>
        </td>
        <td width="800">
<div align="left"> 
    <b> - Download </b> : https://www.oracle.com/technetwork/java/javase/downloads/
    <br/><br/> 
    <b> - 시스템 환경변수 </b>
    <br/><br/> 
    <b> 1. JAVA_HOME </b> = C:\Java\jdk1.8.0
    <br/><br/> 
    <b> 2. Path </b> = %Path%; %JAVA_HOME%\bin
    <br/><br/>
    <b> 3. CLASSPATH </b> = .; %JAVA_HOME%\lib;
</div>
        </td>
    </tr>
</table>


<hr>

### TensorFlow

<table align="left">
    <tr align="left">
        <td width="200">
            <a href="https://www.tensorflow.org/">
            <img src="./images/TensorFlow_logo2.png" width="150" />
            </a>
        </td>
        <td width="800">
<div align="left">
    <b> - TensorFlow.org </b> : https://www.tensorflow.org/
    <br/><br/> - An open source machine learning library for research and production.
    <br/><br/>
    <b> 1. TenforFlow Install  : <a href='https://www.tensorflow.org/install/'>[설치가이드]</a>
    <br/><br/>
    <b> 2. TenforFlow Develop : <a href='https://www.tensorflow.org/tutorials/'>[튜토리얼]</a>
    <br/><br/>
    <b> 3. TensorFlow Community </b> : <a href='https://www.tensorflow.org/community/'>[커뮤니티]</a>
    <br/><br/>
    <b> cf. Environment : Install a Python 3.6.x or Python 3.7.x 64-bit release for Windows </b>
</div>
        </td>
    </tr>
</table>
<br/>


<hr>

### Microsoft Azuer Notebooks

<table align="left">
    <tr align="left">
        <td width="200">
            <a href="https://notebooks.azure.com/">
            <img src="./images/microsoft.jpg" width="100" />
            </a>
        </td>
        <td width="800">
<div align="left">
- <b> Microsoft Azure Notebooks </b> : https://notebooks.azure.com/
<br/><br/>
- Interactive coding in my browser
<br/><br/>
- Free, in the cloud, powered by jupyter
</div></td>
    </tr>
</table>
<br/>


<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
