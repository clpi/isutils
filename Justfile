alias r:=run

default: nimc rustc-win

build:
    poetry build

run:
    poetry shell && poetry run
   
nimc:
    nim c --app:lib --out:mymodule.pyd --threads:on --tlsEmulation:off --passL:-static src/isu.nim

rustc-win:
    cd isulib && maturin develop

rustc:
    nim c --app:lib --out:mymodule.so --threads:on mymodule
