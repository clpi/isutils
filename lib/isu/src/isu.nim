import nimpy

type Demo* = ref object of PyNimObjectExperimental
    field: string

proc hello*() {.exportpy.} =
    echo("Hello world")

func greet*(name: string): string {.exportpy.} = 
    "Hello, " & name & "!" 

when isMainModule:
    echo "\x1b[32;1mIS MAIN MODULE:"