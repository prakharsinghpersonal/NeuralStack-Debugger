#pragma once
#include <string>

namespace neural_stack {

class IProfiler {
public:
    virtual void start() = 0;
    virtual void stop() = 0;
    virtual void dump_results(const std::string& filename) = 0;
    virtual ~IProfiler() = default;
};

} // namespace neural_stack
