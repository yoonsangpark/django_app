//----------------------------------------------------------------------

//[1] Base

[OS] Windows 11 Pro

[Editer] vscode

[python] python --version

		Python 3.13.7

[git] Git-2.51.0-64-bit.exe

https://gitforwindows.org/

[Power Shell : 관리자권한으로 실행]

PS C:\WINDOWS\system32> Set-ExecutionPolicy Unrestricted

실행 규칙 변경
실행 정책은 신뢰하지 않는 스크립트로부터 사용자를 보호합니다. 실행 정책을 변경하면 about_Execution_Policies 도움말
항목(https://go.microsoft.com/fwlink/?LinkID=135170)에 설명된 보안 위험에 노출될 수 있습니다. 실행 정책을
변경하시겠습니까?
[Y] 예(Y)  [A] 모두 예(A)  [N] 아니요(N)  [L] 모두 아니요(L)  [S] 일시 중단(S)  [?] 도움말 (기본값은 "N"): Y




django_app

 |-webenv
 
 |-webbase
 
 |-webbase/smartschool(***)

//----------------------------------------------------------------------

//[2] VENV

1. make working dir.

C:\django_app

*django_app : working dir.


2. VS Code : File -> Open Folder...


3. VS Code : Terminal -> New Terminal


4. make venv(virtual environment)

PS C:\django_app> python -m venv webenv

*webenv : virtual environment name


5. activate venv

PS C:\django_app> .\webenv\Scripts\activate

(webenv) PS C:\django_app> 

//----------------------------------------------------------------------

//[3] Install Django

(webenv) PS C:\django_app> pip install django

(webenv) PS C:\django_app> pip install django-rest-framework


//----------------------------------------------------------------------

//[4] Make project

1. make project

PS C:\django_app> django-admin startproject webbase

*webbase : project name

2. run project

(webenv) PS C:\django_app> python webbase/manage.py runserver

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
September 20, 2025 - 23:28:40
Django version 5.2.6, using settings 'webbase.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
For more information on production servers see: https://docs.djangoproject.com/en/5.2/howto/deployment/

//----------------------------------------------------------------------

//[5] Make app

(webenv) PS C:\django_app> cd .\webbase\

*smartschool : app name

(webenv) PS C:\django_app\webbase> python manage.py startapp smartschool

//----------------------------------------------------------------------

//[6]

pip freeze > requirements.txt

pip install -r requirements.txt

//----------------------------------------------------------------------

//[7] git

https://github.com/yoonsangpark/django_app

git init

git remote add origin git@github.com:yoonsangpark/django_app.git

git add .

git commit -m "initial setup"

git push --set-upstream origin master

git push origin main


https://www.toptal.com/developers/gitignore

https://www.toptal.com/developers/gitignore/api/windows,visualstudiocode,django



(base) C:\Users\yoonsangpark>ssh-keygen

Generating public/private ed25519 key pair.

Enter file in which to save the key (C:\Users\yoonsangpark/.ssh/id_ed25519):

Enter passphrase (empty for no passphrase):

Enter same passphrase again:

Your identification has been saved in C:\Users\yoonsangpark/.ssh/id_ed25519

Your public key has been saved in C:\Users\yoonsangpark/.ssh/id_ed25519.pub

The key fingerprint is:

SHA256:xxxxxx yoonsangpark@jupiter

The key's randomart image is:
+--[ED25519 256]--+
|    ..o          |
|o .  =. .        |
|.+  o..o .       |
|  ==o++ .        |
| o.B=*. S        |
|=o* * *.         |
|=E.*.= o         |
|o +=+ o          |
| o+o..           |
+----[SHA256]-----+

