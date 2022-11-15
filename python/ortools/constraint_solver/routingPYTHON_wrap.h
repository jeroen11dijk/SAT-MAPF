/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 4.0.1
 *
 * This file is not intended to be easily readable and contains a number of
 * coding conventions designed to improve portability and efficiency. Do not make
 * changes to this file unless you know what you are doing--modify the SWIG
 * interface file instead.
 * ----------------------------------------------------------------------------- */

#ifndef SWIG_pywrapcp_WRAP_H_
#define SWIG_pywrapcp_WRAP_H_

#include <map>
#include <string>


class SwigDirector_BaseObject : public operations_research::BaseObject, public Swig::Director {

public:
    SwigDirector_BaseObject(PyObject *self);
    virtual ~SwigDirector_BaseObject();
    virtual std::string DebugString() const;

/* Internal director utilities */
public:
    bool swig_get_inner(const char *swig_protected_method_name) const {
      std::map<std::string, bool>::const_iterator iv = swig_inner.find(swig_protected_method_name);
      return (iv != swig_inner.end() ? iv->second : false);
    }
    void swig_set_inner(const char *swig_protected_method_name, bool swig_val) const {
      swig_inner[swig_protected_method_name] = swig_val;
    }
private:
    mutable std::map<std::string, bool> swig_inner;

#if defined(SWIG_PYTHON_DIRECTOR_VTABLE)
/* VTable implementation */
    PyObject *swig_get_method(size_t method_index, const char *method_name) const {
      PyObject *method = vtable[method_index];
      if (!method) {
        swig::SwigVar_PyObject name = SWIG_Python_str_FromChar(method_name);
        method = PyObject_GetAttr(swig_get_self(), name);
        if (!method) {
          std::string msg = "Method in class BaseObject doesn't exist, undefined ";
          msg += method_name;
          Swig::DirectorMethodException::raise(msg.c_str());
        }
        vtable[method_index] = method;
      }
      return method;
    }
private:
    mutable swig::SwigVar_PyObject vtable[1];
#endif

};


class SwigDirector_PropagationBaseObject : public operations_research::PropagationBaseObject, public Swig::Director {

public:
    SwigDirector_PropagationBaseObject(PyObject *self, operations_research::Solver *const s);
    virtual ~SwigDirector_PropagationBaseObject();
    virtual std::string DebugString() const;
    virtual std::string name() const;

/* Internal director utilities */
public:
    bool swig_get_inner(const char *swig_protected_method_name) const {
      std::map<std::string, bool>::const_iterator iv = swig_inner.find(swig_protected_method_name);
      return (iv != swig_inner.end() ? iv->second : false);
    }
    void swig_set_inner(const char *swig_protected_method_name, bool swig_val) const {
      swig_inner[swig_protected_method_name] = swig_val;
    }
private:
    mutable std::map<std::string, bool> swig_inner;

#if defined(SWIG_PYTHON_DIRECTOR_VTABLE)
/* VTable implementation */
    PyObject *swig_get_method(size_t method_index, const char *method_name) const {
      PyObject *method = vtable[method_index];
      if (!method) {
        swig::SwigVar_PyObject name = SWIG_Python_str_FromChar(method_name);
        method = PyObject_GetAttr(swig_get_self(), name);
        if (!method) {
          std::string msg = "Method in class PropagationBaseObject doesn't exist, undefined ";
          msg += method_name;
          Swig::DirectorMethodException::raise(msg.c_str());
        }
        vtable[method_index] = method;
      }
      return method;
    }
private:
    mutable swig::SwigVar_PyObject vtable[2];
#endif

};


class SwigDirector_Decision : public operations_research::Decision, public Swig::Director {

public:
    SwigDirector_Decision(PyObject *self);
    virtual ~SwigDirector_Decision();
    virtual std::string DebugString() const;
    virtual void Apply(operations_research::Solver *const s);
    virtual void Refute(operations_research::Solver *const s);

/* Internal director utilities */
public:
    bool swig_get_inner(const char *swig_protected_method_name) const {
      std::map<std::string, bool>::const_iterator iv = swig_inner.find(swig_protected_method_name);
      return (iv != swig_inner.end() ? iv->second : false);
    }
    void swig_set_inner(const char *swig_protected_method_name, bool swig_val) const {
      swig_inner[swig_protected_method_name] = swig_val;
    }
private:
    mutable std::map<std::string, bool> swig_inner;

#if defined(SWIG_PYTHON_DIRECTOR_VTABLE)
/* VTable implementation */
    PyObject *swig_get_method(size_t method_index, const char *method_name) const {
      PyObject *method = vtable[method_index];
      if (!method) {
        swig::SwigVar_PyObject name = SWIG_Python_str_FromChar(method_name);
        method = PyObject_GetAttr(swig_get_self(), name);
        if (!method) {
          std::string msg = "Method in class Decision doesn't exist, undefined ";
          msg += method_name;
          Swig::DirectorMethodException::raise(msg.c_str());
        }
        vtable[method_index] = method;
      }
      return method;
    }
private:
    mutable swig::SwigVar_PyObject vtable[3];
#endif

};


class SwigDirector_DecisionBuilder : public operations_research::DecisionBuilder, public Swig::Director {

public:
    SwigDirector_DecisionBuilder(PyObject *self);
    virtual ~SwigDirector_DecisionBuilder();
    virtual std::string DebugString() const;
    virtual operations_research::Decision *Next(operations_research::Solver *const s);

/* Internal director utilities */
public:
    bool swig_get_inner(const char *swig_protected_method_name) const {
      std::map<std::string, bool>::const_iterator iv = swig_inner.find(swig_protected_method_name);
      return (iv != swig_inner.end() ? iv->second : false);
    }
    void swig_set_inner(const char *swig_protected_method_name, bool swig_val) const {
      swig_inner[swig_protected_method_name] = swig_val;
    }
private:
    mutable std::map<std::string, bool> swig_inner;

#if defined(SWIG_PYTHON_DIRECTOR_VTABLE)
/* VTable implementation */
    PyObject *swig_get_method(size_t method_index, const char *method_name) const {
      PyObject *method = vtable[method_index];
      if (!method) {
        swig::SwigVar_PyObject name = SWIG_Python_str_FromChar(method_name);
        method = PyObject_GetAttr(swig_get_self(), name);
        if (!method) {
          std::string msg = "Method in class DecisionBuilder doesn't exist, undefined ";
          msg += method_name;
          Swig::DirectorMethodException::raise(msg.c_str());
        }
        vtable[method_index] = method;
      }
      return method;
    }
private:
    mutable swig::SwigVar_PyObject vtable[2];
#endif

};


class SwigDirector_Demon : public operations_research::Demon, public Swig::Director {

public:
    SwigDirector_Demon(PyObject *self);
    virtual ~SwigDirector_Demon();
    virtual std::string DebugString() const;
    virtual void Run(operations_research::Solver *const s);
    virtual operations_research::Solver::DemonPriority priority() const;

/* Internal director utilities */
public:
    bool swig_get_inner(const char *swig_protected_method_name) const {
      std::map<std::string, bool>::const_iterator iv = swig_inner.find(swig_protected_method_name);
      return (iv != swig_inner.end() ? iv->second : false);
    }
    void swig_set_inner(const char *swig_protected_method_name, bool swig_val) const {
      swig_inner[swig_protected_method_name] = swig_val;
    }
private:
    mutable std::map<std::string, bool> swig_inner;

#if defined(SWIG_PYTHON_DIRECTOR_VTABLE)
/* VTable implementation */
    PyObject *swig_get_method(size_t method_index, const char *method_name) const {
      PyObject *method = vtable[method_index];
      if (!method) {
        swig::SwigVar_PyObject name = SWIG_Python_str_FromChar(method_name);
        method = PyObject_GetAttr(swig_get_self(), name);
        if (!method) {
          std::string msg = "Method in class Demon doesn't exist, undefined ";
          msg += method_name;
          Swig::DirectorMethodException::raise(msg.c_str());
        }
        vtable[method_index] = method;
      }
      return method;
    }
private:
    mutable swig::SwigVar_PyObject vtable[3];
#endif

};


class SwigDirector_Constraint : public operations_research::Constraint, public Swig::Director {

public:
    SwigDirector_Constraint(PyObject *self, operations_research::Solver *const solver);
    virtual ~SwigDirector_Constraint();
    virtual std::string DebugString() const;
    virtual std::string name() const;
    virtual void Post();
    virtual void InitialPropagate();
    virtual void Accept(operations_research::ModelVisitor *const visitor) const;
    virtual operations_research::IntVar *Var();

/* Internal director utilities */
public:
    bool swig_get_inner(const char *swig_protected_method_name) const {
      std::map<std::string, bool>::const_iterator iv = swig_inner.find(swig_protected_method_name);
      return (iv != swig_inner.end() ? iv->second : false);
    }
    void swig_set_inner(const char *swig_protected_method_name, bool swig_val) const {
      swig_inner[swig_protected_method_name] = swig_val;
    }
private:
    mutable std::map<std::string, bool> swig_inner;

#if defined(SWIG_PYTHON_DIRECTOR_VTABLE)
/* VTable implementation */
    PyObject *swig_get_method(size_t method_index, const char *method_name) const {
      PyObject *method = vtable[method_index];
      if (!method) {
        swig::SwigVar_PyObject name = SWIG_Python_str_FromChar(method_name);
        method = PyObject_GetAttr(swig_get_self(), name);
        if (!method) {
          std::string msg = "Method in class Constraint doesn't exist, undefined ";
          msg += method_name;
          Swig::DirectorMethodException::raise(msg.c_str());
        }
        vtable[method_index] = method;
      }
      return method;
    }
private:
    mutable swig::SwigVar_PyObject vtable[5];
#endif

};


class SwigDirector_SearchMonitor : public operations_research::SearchMonitor, public Swig::Director {

public:
    SwigDirector_SearchMonitor(PyObject *self, operations_research::Solver *const s);
    virtual ~SwigDirector_SearchMonitor();
    virtual std::string DebugString() const;
    virtual void EnterSearch();
    virtual void RestartSearch();
    virtual void ExitSearch();
    virtual void BeginNextDecision(operations_research::DecisionBuilder *const b);
    virtual void EndNextDecision(operations_research::DecisionBuilder *const b, operations_research::Decision *const d);
    virtual void ApplyDecision(operations_research::Decision *const d);
    virtual void RefuteDecision(operations_research::Decision *const d);
    virtual void AfterDecision(operations_research::Decision *const d, bool apply);
    virtual void BeginFail();
    virtual void EndFail();
    virtual void BeginInitialPropagation();
    virtual void EndInitialPropagation();
    virtual bool AcceptSolution();
    virtual bool AtSolution();
    virtual void NoMoreSolutions();
    virtual bool LocalOptimum();
    virtual bool AcceptDelta(operations_research::Assignment *delta, operations_research::Assignment *deltadelta);
    virtual void AcceptNeighbor();
    virtual void AcceptUncheckedNeighbor();
    virtual bool IsUncheckedSolutionLimitReached();
    virtual void PeriodicCheck();
    virtual int ProgressPercent();
    virtual void Accept(operations_research::ModelVisitor *const visitor) const;
    virtual void Install();

/* Internal director utilities */
public:
    bool swig_get_inner(const char *swig_protected_method_name) const {
      std::map<std::string, bool>::const_iterator iv = swig_inner.find(swig_protected_method_name);
      return (iv != swig_inner.end() ? iv->second : false);
    }
    void swig_set_inner(const char *swig_protected_method_name, bool swig_val) const {
      swig_inner[swig_protected_method_name] = swig_val;
    }
private:
    mutable std::map<std::string, bool> swig_inner;

#if defined(SWIG_PYTHON_DIRECTOR_VTABLE)
/* VTable implementation */
    PyObject *swig_get_method(size_t method_index, const char *method_name) const {
      PyObject *method = vtable[method_index];
      if (!method) {
        swig::SwigVar_PyObject name = SWIG_Python_str_FromChar(method_name);
        method = PyObject_GetAttr(swig_get_self(), name);
        if (!method) {
          std::string msg = "Method in class SearchMonitor doesn't exist, undefined ";
          msg += method_name;
          Swig::DirectorMethodException::raise(msg.c_str());
        }
        vtable[method_index] = method;
      }
      return method;
    }
private:
    mutable swig::SwigVar_PyObject vtable[19];
#endif

};


class SwigDirector_LocalSearchOperator : public operations_research::LocalSearchOperator, public Swig::Director {

public:
    SwigDirector_LocalSearchOperator(PyObject *self);
    virtual ~SwigDirector_LocalSearchOperator();
    virtual std::string DebugString() const;
    virtual bool MakeNextNeighbor(operations_research::Assignment *delta, operations_research::Assignment *deltadelta);
    virtual void Start(operations_research::Assignment const *assignment);
    virtual void Reset();
    virtual bool HasFragments() const;
    virtual bool HoldsDelta() const;

/* Internal director utilities */
public:
    bool swig_get_inner(const char *swig_protected_method_name) const {
      std::map<std::string, bool>::const_iterator iv = swig_inner.find(swig_protected_method_name);
      return (iv != swig_inner.end() ? iv->second : false);
    }
    void swig_set_inner(const char *swig_protected_method_name, bool swig_val) const {
      swig_inner[swig_protected_method_name] = swig_val;
    }
private:
    mutable std::map<std::string, bool> swig_inner;

#if defined(SWIG_PYTHON_DIRECTOR_VTABLE)
/* VTable implementation */
    PyObject *swig_get_method(size_t method_index, const char *method_name) const {
      PyObject *method = vtable[method_index];
      if (!method) {
        swig::SwigVar_PyObject name = SWIG_Python_str_FromChar(method_name);
        method = PyObject_GetAttr(swig_get_self(), name);
        if (!method) {
          std::string msg = "Method in class LocalSearchOperator doesn't exist, undefined ";
          msg += method_name;
          Swig::DirectorMethodException::raise(msg.c_str());
        }
        vtable[method_index] = method;
      }
      return method;
    }
private:
    mutable swig::SwigVar_PyObject vtable[3];
#endif

};


class SwigDirector_IntVarLocalSearchOperator : public operations_research::IntVarLocalSearchOperator, public Swig::Director {

public:
    SwigDirector_IntVarLocalSearchOperator(PyObject *self);
    SwigDirector_IntVarLocalSearchOperator(PyObject *self, std::vector< operations_research::IntVar * > const &vars, bool keep_inverse_values = false);
    virtual ~SwigDirector_IntVarLocalSearchOperator();
    virtual std::string DebugString() const;
    virtual bool MakeNextNeighbor(operations_research::Assignment *delta, operations_research::Assignment *deltadelta);
    virtual void Reset();
    virtual bool HasFragments() const;
    virtual bool HoldsDelta() const;
    virtual bool IsIncremental() const;
    virtual bool SkipUnchanged(int index) const;
    virtual void OnStart();
    virtual bool MakeOneNeighbor();
    virtual bool MakeOneNeighborSwigPublic() {
      return operations_research::IntVarLocalSearchOperator::MakeOneNeighbor();
    }

/* Internal director utilities */
public:
    bool swig_get_inner(const char *swig_protected_method_name) const {
      std::map<std::string, bool>::const_iterator iv = swig_inner.find(swig_protected_method_name);
      return (iv != swig_inner.end() ? iv->second : false);
    }
    void swig_set_inner(const char *swig_protected_method_name, bool swig_val) const {
      swig_inner[swig_protected_method_name] = swig_val;
    }
private:
    mutable std::map<std::string, bool> swig_inner;

#if defined(SWIG_PYTHON_DIRECTOR_VTABLE)
/* VTable implementation */
    PyObject *swig_get_method(size_t method_index, const char *method_name) const {
      PyObject *method = vtable[method_index];
      if (!method) {
        swig::SwigVar_PyObject name = SWIG_Python_str_FromChar(method_name);
        method = PyObject_GetAttr(swig_get_self(), name);
        if (!method) {
          std::string msg = "Method in class IntVarLocalSearchOperator doesn't exist, undefined ";
          msg += method_name;
          Swig::DirectorMethodException::raise(msg.c_str());
        }
        vtable[method_index] = method;
      }
      return method;
    }
private:
    mutable swig::SwigVar_PyObject vtable[5];
#endif

};


class SwigDirector_BaseLns : public operations_research::BaseLns, public Swig::Director {

public:
    SwigDirector_BaseLns(PyObject *self, std::vector< operations_research::IntVar * > const &vars);
    virtual ~SwigDirector_BaseLns();
    virtual std::string DebugString() const;
    virtual bool MakeNextNeighbor(operations_research::Assignment *delta, operations_research::Assignment *deltadelta);
    virtual void Reset();
    virtual bool HasFragments() const;
    virtual bool HoldsDelta() const;
    virtual bool IsIncremental() const;
    virtual void InitFragments();
    virtual bool NextFragment();

/* Internal director utilities */
public:
    bool swig_get_inner(const char *swig_protected_method_name) const {
      std::map<std::string, bool>::const_iterator iv = swig_inner.find(swig_protected_method_name);
      return (iv != swig_inner.end() ? iv->second : false);
    }
    void swig_set_inner(const char *swig_protected_method_name, bool swig_val) const {
      swig_inner[swig_protected_method_name] = swig_val;
    }
private:
    mutable std::map<std::string, bool> swig_inner;

#if defined(SWIG_PYTHON_DIRECTOR_VTABLE)
/* VTable implementation */
    PyObject *swig_get_method(size_t method_index, const char *method_name) const {
      PyObject *method = vtable[method_index];
      if (!method) {
        swig::SwigVar_PyObject name = SWIG_Python_str_FromChar(method_name);
        method = PyObject_GetAttr(swig_get_self(), name);
        if (!method) {
          std::string msg = "Method in class BaseLns doesn't exist, undefined ";
          msg += method_name;
          Swig::DirectorMethodException::raise(msg.c_str());
        }
        vtable[method_index] = method;
      }
      return method;
    }
private:
    mutable swig::SwigVar_PyObject vtable[5];
#endif

};


class SwigDirector_ChangeValue : public operations_research::ChangeValue, public Swig::Director {

public:
    SwigDirector_ChangeValue(PyObject *self, std::vector< operations_research::IntVar * > const &vars);
    virtual ~SwigDirector_ChangeValue();
    virtual std::string DebugString() const;
    virtual bool MakeNextNeighbor(operations_research::Assignment *delta, operations_research::Assignment *deltadelta);
    virtual void Reset();
    virtual bool HasFragments() const;
    virtual bool HoldsDelta() const;
    virtual bool IsIncremental() const;
    virtual bool SkipUnchanged(int index) const;
    virtual void OnStart();
    virtual bool MakeOneNeighbor();
    virtual bool MakeOneNeighborSwigPublic() {
      return operations_research::ChangeValue::MakeOneNeighbor();
    }
    virtual int64_t ModifyValue(int64_t index, int64_t value);

/* Internal director utilities */
public:
    bool swig_get_inner(const char *swig_protected_method_name) const {
      std::map<std::string, bool>::const_iterator iv = swig_inner.find(swig_protected_method_name);
      return (iv != swig_inner.end() ? iv->second : false);
    }
    void swig_set_inner(const char *swig_protected_method_name, bool swig_val) const {
      swig_inner[swig_protected_method_name] = swig_val;
    }
private:
    mutable std::map<std::string, bool> swig_inner;

#if defined(SWIG_PYTHON_DIRECTOR_VTABLE)
/* VTable implementation */
    PyObject *swig_get_method(size_t method_index, const char *method_name) const {
      PyObject *method = vtable[method_index];
      if (!method) {
        swig::SwigVar_PyObject name = SWIG_Python_str_FromChar(method_name);
        method = PyObject_GetAttr(swig_get_self(), name);
        if (!method) {
          std::string msg = "Method in class ChangeValue doesn't exist, undefined ";
          msg += method_name;
          Swig::DirectorMethodException::raise(msg.c_str());
        }
        vtable[method_index] = method;
      }
      return method;
    }
private:
    mutable swig::SwigVar_PyObject vtable[6];
#endif

};


class SwigDirector_IntVarLocalSearchFilter : public operations_research::IntVarLocalSearchFilter, public Swig::Director {

public:
    SwigDirector_IntVarLocalSearchFilter(PyObject *self, std::vector< operations_research::IntVar * > const &vars);
    virtual ~SwigDirector_IntVarLocalSearchFilter();
    virtual std::string DebugString() const;
    virtual void Relax(operations_research::Assignment const *delta, operations_research::Assignment const *deltadelta);
    virtual void Commit(operations_research::Assignment const *delta, operations_research::Assignment const *deltadelta);
    virtual bool Accept(operations_research::Assignment const *delta, operations_research::Assignment const *deltadelta, int64_t objective_min, int64_t objective_max);
    virtual bool IsIncremental() const;
    virtual void Synchronize(operations_research::Assignment const *assignment, operations_research::Assignment const *delta);
    virtual void Revert();
    virtual void Reset();
    virtual int64_t GetSynchronizedObjectiveValue() const;
    virtual int64_t GetAcceptedObjectiveValue() const;
    virtual void OnSynchronize(operations_research::Assignment const *delta);
    virtual void OnSynchronizeSwigPublic(operations_research::Assignment const *delta) {
      operations_research::IntVarLocalSearchFilter::OnSynchronize(delta);
    }

/* Internal director utilities */
public:
    bool swig_get_inner(const char *swig_protected_method_name) const {
      std::map<std::string, bool>::const_iterator iv = swig_inner.find(swig_protected_method_name);
      return (iv != swig_inner.end() ? iv->second : false);
    }
    void swig_set_inner(const char *swig_protected_method_name, bool swig_val) const {
      swig_inner[swig_protected_method_name] = swig_val;
    }
private:
    mutable std::map<std::string, bool> swig_inner;

#if defined(SWIG_PYTHON_DIRECTOR_VTABLE)
/* VTable implementation */
    PyObject *swig_get_method(size_t method_index, const char *method_name) const {
      PyObject *method = vtable[method_index];
      if (!method) {
        swig::SwigVar_PyObject name = SWIG_Python_str_FromChar(method_name);
        method = PyObject_GetAttr(swig_get_self(), name);
        if (!method) {
          std::string msg = "Method in class IntVarLocalSearchFilter doesn't exist, undefined ";
          msg += method_name;
          Swig::DirectorMethodException::raise(msg.c_str());
        }
        vtable[method_index] = method;
      }
      return method;
    }
private:
    mutable swig::SwigVar_PyObject vtable[4];
#endif

};


#endif
