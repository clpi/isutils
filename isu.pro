QT += widgets core gui concurrent
CONFIG += plugin sdk_no_version_check
TEMPLATE = lib/tmp
#qmake_cxxflags = -std=++11

# greaterthan(qt_major_version, 5): qt += widgets

# requires(qtconfig(combobox))

# target.path = ./dist
# installs += target
# target = vfp
# template = app

FORMS      += ./isu/ui/window.ui \
              ./isu/ui/prod.ui \
              ./isu/ui/ops/tab.ui \
              ./isu/ui/ops/render.ui \
              ./isu/ui/ops/shell.ui \
              ./isu/ui/ops/insert.ui \
              ./isu/ui/ops/section.ui \
              ./isu/ui/ops/audio.ui \
              ./isu/ui/ops/pace.ui \
              ./isu/ui/ops/text.ui \
              ./isu/ui/ops/crop.ui \
              ./isu/ui/comp/op.ui \
              ./isu/ui/tabs.ui \
              ./isu/ui/comp/prefs.ui\
              ./isu/ui/data/steps.ui \
              ./isu/ui/views/demo.ui \
              ./isu/ui/c/main.ui

INCLUDEPATH += $$pwd \
               res

HEADERS    += view/demo.h \
              isu/ui/c/main.h \
              view/main.cpp

SOURCES  += isu/__init__.py \
            isu/isu.py \
            isu/qt.py \
            isu/app.py \
            isu/data/__init__.py \
            isu/data/context.py \
            isu/data/store.py \
            isu/data/models.py \
            isu/models/__init__.py \
            isu/models/script.py \
            isu/models/demo.py \
            isu/models/step.py \
            isu/models/section.py \
            isu/models/video.py \
            isu/models/audio.py \
            isu/models/actions/box.py \
            isu/models/actions/text.py \
            isu/models/actions/jump.py \
            isu/models/actions/box.py \
            isu/models/actions/audio.py \
            isu/models/demo/save.py \
            isu/models/demo/__init__.py \
            isu/operation/__init__.py\
            isu/operation/shell.py\
            isu/operation/insert.py\
            isu/operation/crop.py\
            isu/operation/section.py\
            isu/operation/audio.py\
            isu/operation/pace.py\
            isu/operation/render.py\
            isu/operation/text.py\
            isu/ui/__init__.py \
            isu/ui/window.py \
            isu/ui/comp/__init__.py \
            isu/ui/tabs.py \
            isu/ui/comp/op.py \
            isu/ui/comp/prog.py \
            isu/ui/comp/prefs.py \
            isu/ui/ops/__init__.py \
            isu/ui/ops/tab.py \
            isu/ui/ops/shell.py \
            isu/ui/ops/insert.py \
            isu/ui/ops/crop.py \
            isu/ui/ops/section.py \
            isu/ui/ops/audio.py \
            isu/ui/ops/pace.py \
            isu/ui/ops/text.py \
            isu/ui/ops/render.py \
            isu/ui/data/__init__.py \
            isu/ui/data/steps.py \
            isu/ui/views/__init__.py.py \
            isu/ui/views/demo.py.py \
            isu/utils/__init__.py \
            test/test.py \
            main.py \
            lab.py \
            setup.py \
    isu/ui/c/main.cpp

OTHER_FILES += pyproject.toml \
            ./res/icons8-cursor-24.png\
            ./res/icons8-cursor-48.png \
            ./lib/main.py \



# install

DISTFILES += \
    isu/ui/comp/canvas.qml
