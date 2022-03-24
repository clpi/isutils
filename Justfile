alias i:=install
alias r:=run
alias b:=build
alias p:=publish
alias gp:=gpush
alias v:=venv

BIN:="ISU"
OUT:="./dist"
RES:="./res"

default: brun

build:
    poetry build 

venv: 
    poetry shell

run: venv
    poetry run

brun:
    poetry run




buildext: nimc rustc-win
    nim c --app:lib --out:mymodule.pyd --threads:on --tlsEmulation:off --passL:-static src/isu.nim
    
   
nimc:
    nim c --app:lib --out:mymodule.pyd --threads:on --tlsEmulation:off --passL:-static src/isu.nim

rustc-win:
    cd isulib && maturin develop

install:
    poetry install

publish:
    echo ""

gpush:
    git add --a
    git commit -m 'n'
    git push gh main
