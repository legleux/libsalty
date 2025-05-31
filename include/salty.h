#pragma once

#include <vector>
#include <string>


#ifdef _WIN32
  #define SALTY_EXPORT __declspec(dllexport)
#else
  #define SALTY_EXPORT
#endif

SALTY_EXPORT void salty();
SALTY_EXPORT void salty_print_vector(const std::vector<std::string> &strings);
