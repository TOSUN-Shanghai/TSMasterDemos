TEMPLATE = app
CONFIG += console c++11
CONFIG -= app_bundle

SOURCES += \
        main.cpp

LIBS += -L$$PWD/../lib/ -lTSCANApiOnLinux
LIBS += -L$$PWD/../lib/ -lTSH

HEADERS += \
    TSCANDef.hpp

