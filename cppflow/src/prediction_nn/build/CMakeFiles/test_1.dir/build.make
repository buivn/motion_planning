# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.21

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/bin/cmake

# The command to remove a file.
RM = /usr/local/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/dzungbui/learning_ws/icra22/cppflow/src/prediction_nn

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/dzungbui/learning_ws/icra22/cppflow/src/prediction_nn/build

# Include any dependencies generated for this target.
include CMakeFiles/test_1.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/test_1.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/test_1.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/test_1.dir/flags.make

CMakeFiles/test_1.dir/predict.cpp.o: CMakeFiles/test_1.dir/flags.make
CMakeFiles/test_1.dir/predict.cpp.o: ../predict.cpp
CMakeFiles/test_1.dir/predict.cpp.o: CMakeFiles/test_1.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/dzungbui/learning_ws/icra22/cppflow/src/prediction_nn/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/test_1.dir/predict.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/test_1.dir/predict.cpp.o -MF CMakeFiles/test_1.dir/predict.cpp.o.d -o CMakeFiles/test_1.dir/predict.cpp.o -c /home/dzungbui/learning_ws/icra22/cppflow/src/prediction_nn/predict.cpp

CMakeFiles/test_1.dir/predict.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/test_1.dir/predict.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/dzungbui/learning_ws/icra22/cppflow/src/prediction_nn/predict.cpp > CMakeFiles/test_1.dir/predict.cpp.i

CMakeFiles/test_1.dir/predict.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/test_1.dir/predict.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/dzungbui/learning_ws/icra22/cppflow/src/prediction_nn/predict.cpp -o CMakeFiles/test_1.dir/predict.cpp.s

# Object files for target test_1
test_1_OBJECTS = \
"CMakeFiles/test_1.dir/predict.cpp.o"

# External object files for target test_1
test_1_EXTERNAL_OBJECTS =

test_1: CMakeFiles/test_1.dir/predict.cpp.o
test_1: CMakeFiles/test_1.dir/build.make
test_1: /usr/local/lib/libtensorflow.so
test_1: CMakeFiles/test_1.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/dzungbui/learning_ws/icra22/cppflow/src/prediction_nn/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable test_1"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/test_1.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/test_1.dir/build: test_1
.PHONY : CMakeFiles/test_1.dir/build

CMakeFiles/test_1.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/test_1.dir/cmake_clean.cmake
.PHONY : CMakeFiles/test_1.dir/clean

CMakeFiles/test_1.dir/depend:
	cd /home/dzungbui/learning_ws/icra22/cppflow/src/prediction_nn/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/dzungbui/learning_ws/icra22/cppflow/src/prediction_nn /home/dzungbui/learning_ws/icra22/cppflow/src/prediction_nn /home/dzungbui/learning_ws/icra22/cppflow/src/prediction_nn/build /home/dzungbui/learning_ws/icra22/cppflow/src/prediction_nn/build /home/dzungbui/learning_ws/icra22/cppflow/src/prediction_nn/build/CMakeFiles/test_1.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/test_1.dir/depend

