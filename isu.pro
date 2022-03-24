QT += widgets core gui concurrent designer uitools
CONFIG += plugin
TEMPLATE = lib/tmp
QMAKE_CXXFLAGS = -std=++11

greaterThan(QT_MAJOR_VERSION, 5): QT += widgets

requires(qtConfig(combobox))

target.path = $$[QT_INSTALL_PLUGINS]/designer
INSTALLS += target
TARGET = Vfp
TEMPLATE = app
INCLUDEPATH += $$PWD

HEADERS    += view/demo.h \
              view/main.cpp

SOURCES    += isu/main.py \
              isu/main.cpp \
              isu/ui/main.ui \
              isu/ui/window.ui \
              isu/ui/ops/tab.ui \
              isu/ui/ops/render.ui \
              isu/ui/ops/shell.ui \
              isu/ui/ops/insert.ui \
OTHER_FILES += pyproject.toml
              
              

# install
target.path = isu
INSTALLS += target
