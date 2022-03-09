QT += widgets core gui concurrent designer
# TEMPLATE = templ

greaterThan(QT_MAJOR_VERSION, 5): QT += widgets

requires(qtConfig(combobox))
INSTALLS =
TARGET = Vfp
TEMPLATE = app

QMAKE_CXXFLAGS = -std=++11



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
