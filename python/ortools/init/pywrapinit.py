# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _pywrapinit
else:
    import _pywrapinit

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class CppFlags(object):
    r"""Simple structure that holds useful C++ flags to setup from non-C++ languages."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    logtostderr = property(_pywrapinit.CppFlags_logtostderr_get, _pywrapinit.CppFlags_logtostderr_set, doc=r"""If true, all logging message will be sent to stderr.""")
    log_prefix = property(_pywrapinit.CppFlags_log_prefix_get, _pywrapinit.CppFlags_log_prefix_set, doc=r"""Controls is time and source code info are used to prefix logging messages.""")
    cp_model_dump_prefix = property(_pywrapinit.CppFlags_cp_model_dump_prefix_get, _pywrapinit.CppFlags_cp_model_dump_prefix_set, doc=r"""Prefix filename for all dumped files (models, solutions, lns sub-models).""")
    cp_model_dump_models = property(_pywrapinit.CppFlags_cp_model_dump_models_get, _pywrapinit.CppFlags_cp_model_dump_models_set, doc=r"""
    DEBUG ONLY: Dump CP-SAT models during solve.

     When set to true, SolveCpModel() will dump its model protos
    (original model, presolved model, mapping model) in text  format to
    'FLAGS_cp_model_dump_prefix'{model|presolved_model|mapping_model}.pbtxt.
    """)
    cp_model_dump_lns = property(_pywrapinit.CppFlags_cp_model_dump_lns_get, _pywrapinit.CppFlags_cp_model_dump_lns_set, doc=r"""
    DEBUG ONLY: Dump CP-SAT LNS models during solve.

    When set to true, solve will dump all lns models proto in text format to
    'FLAGS_cp_model_dump_prefix'lns_xxx.pbtxt.
    """)
    cp_model_dump_response = property(_pywrapinit.CppFlags_cp_model_dump_response_get, _pywrapinit.CppFlags_cp_model_dump_response_set, doc=r"""
    DEBUG ONLY: Dump the CP-SAT final response found during solve.

    If true, the final response of each solve will be dumped to
    'FLAGS_cp_model_dump_prefix'response.pbtxt.
    """)

    def __init__(self):
        _pywrapinit.CppFlags_swiginit(self, _pywrapinit.new_CppFlags())
    __swig_destroy__ = _pywrapinit.delete_CppFlags

# Register CppFlags in _pywrapinit:
_pywrapinit.CppFlags_swigregister(CppFlags)

class CppBridge(object):
    r"""
    This class performs various C++ initialization.

    It is meant to be used once at the start of a program.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    @staticmethod
    def InitLogging(program_name: "std::string const &") -> "void":
        r"""
        Initialize the C++ logging layer.

        This must be called once before any other library from OR-Tools are used.
        """
        return _pywrapinit.CppBridge_InitLogging(program_name)

    @staticmethod
    def ShutdownLogging() -> "void":
        r"""
        Shutdown the C++ logging layer.

        This can be called to shutdown the C++ logging layer from OR-Tools.
        It should only be called once.
        """
        return _pywrapinit.CppBridge_ShutdownLogging()

    @staticmethod
    def SetFlags(flags: "CppFlags") -> "void":
        r"""Sets all the C++ flags contained in the CppFlags structure."""
        return _pywrapinit.CppBridge_SetFlags(flags)

    @staticmethod
    def LoadGurobiSharedLibrary(full_library_path: "std::string const &") -> "bool":
        r"""
        Load the gurobi shared library.

        This is necessary if the library is installed in a non canonical
        directory, or if for any reason, it is not found.
        You need to pass the full path, including the shared library file.
        It returns true if the library was found and correctly loaded.
        """
        return _pywrapinit.CppBridge_LoadGurobiSharedLibrary(full_library_path)

    def __init__(self):
        _pywrapinit.CppBridge_swiginit(self, _pywrapinit.new_CppBridge())
    __swig_destroy__ = _pywrapinit.delete_CppBridge

# Register CppBridge in _pywrapinit:
_pywrapinit.CppBridge_swigregister(CppBridge)

def CppBridge_InitLogging(program_name: "std::string const &") -> "void":
    r"""
    Initialize the C++ logging layer.

    This must be called once before any other library from OR-Tools are used.
    """
    return _pywrapinit.CppBridge_InitLogging(program_name)

def CppBridge_ShutdownLogging() -> "void":
    r"""
    Shutdown the C++ logging layer.

    This can be called to shutdown the C++ logging layer from OR-Tools.
    It should only be called once.
    """
    return _pywrapinit.CppBridge_ShutdownLogging()

def CppBridge_SetFlags(flags: "CppFlags") -> "void":
    r"""Sets all the C++ flags contained in the CppFlags structure."""
    return _pywrapinit.CppBridge_SetFlags(flags)

def CppBridge_LoadGurobiSharedLibrary(full_library_path: "std::string const &") -> "bool":
    r"""
    Load the gurobi shared library.

    This is necessary if the library is installed in a non canonical
    directory, or if for any reason, it is not found.
    You need to pass the full path, including the shared library file.
    It returns true if the library was found and correctly loaded.
    """
    return _pywrapinit.CppBridge_LoadGurobiSharedLibrary(full_library_path)



