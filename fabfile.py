import random

from fabric.api import run
from fabric.api import sudo
from fabric.api import local
from fabric.context_managers import cd
from fabric.contrib.files import exists


def _install_python_3_6_9():
    python_version = run("python3 -V")

    if python_version == "Python 3.6.9":
        return

    # 의존성 모듈들 설치.
    sudo(
        "apt-get -y install libncursesw5-dev libgdbm-dev libc6-dev zlib1g-dev libsqlite3-dev tk-dev"
    )
    sudo("apt-get -y install build-essential python-dev python-setuptools python-pip python-smbus")
    sudo("apt-get -y install libssl-dev openssl libffi-dev python-dev python3-dev")

    run("wget https://www.python.org/ftp/python/3.6.9/Python-3.6.9.tgz")
    run("tar xvfz Python-3.6.9.tgz")
    run("cd $HOME/Python-3.6.9 && ./configure")
    run("cd $HOME/Python-3.6.9 && make")
    run("cd $HOME/Python-3.6.9 && sudo make install")

    sudo("yes | rm -R $HOME/Python-3.6.9")
    run("cd $HOME/Python-3.6.9 && ./c.9.tgz")

    assert (
        run("python3 -V") == "Python 3.6.9"
    ), "python3.6.9를 설치했지만, 기본git python3이(가) 3.6.9버전으로 설정되지 않았습니다."


def _install_open_jdk():
    sudo("apt -y install openjdk-8-jdk")


def _install_pip3():
    sudo("apt -y install python3-pip")


def _install_konlpy():

    sudo("pip3 install konlpy")


def _install_mecab_ko():
    run("wget https://bitbucket.org/eunjeon/mecab-ko/downloads/mecab-0.996-ko-0.9.2.tar.gz ")
    run("tar xvfz mecab-0.996-ko-0.9.2.tar.gz")

    with cd("mecab-0.996-ko-0.9.2"):
        run("./configure")
        run("make")
        run("make check")
        sudo("make install")
    sudo("yes | rm -R mecab-0.996-ko-0.9.2.tar.gz")


def _install_mecab_ko_dict():

    # sudo("apt update")
    sudo("apt -y install automake1.11")

    run(
        "wget https://bitbucket.org/eunjeon/mecab-ko-dic/downloads/mecab-ko-dic-2.1.1-20180720.tar.gz"
    )
    run("tar xvfz mecab-ko-dic-2.1.1-20180720.tar.gz")

    with cd("mecab-ko-dic-2.1.1-20180720"):
        run("wget https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh")
        run("./autogen.sh")
        sudo("./configure")
        sudo("ldconfig")
        sudo("make")
        sudo("make install")

    sudo("yes | rm -R mecab-ko-dic-2.1.1-20180720.tar.gz")


def _install_mecab_python3():
    run("pip3 install mecab-python3")


def deploy():

    _install_python_3_6_9()

    _install_open_jdk()
    _install_pip3()
    _install_konlpy()

    _install_mecab_ko()
    _install_mecab_ko_dict()
    _install_mecab_python3()
