from conan import ConanFile
from conan.tools.build import check_max_cppstd, check_min_cppstd
from conan.tools.cmake import CMake, CMakeToolchain, cmake_layout
from conan.tools.scm import Git


class saltyRecipe(ConanFile):
    name = "salty"
    version = "1.0"
    package_type = "library"  # what others are there?

    # Optional metadata
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of salty package here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    # Binary configuration
    settings = ("os", "compiler", "build_type", "arch")
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    generators = "CMakeDeps"

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = ("CMakeLists.txt", "src/*", "include/*")

    def validate(self):
        check_min_cppstd(self, "11")
        check_max_cppstd(self, "20")

    def requirements(self):
        self.requires("fmt/8.1.1")

    def source(self):
        git = Git(self)
        git.clone(url="https://github.com/conan-io/libhello.git", target=".")
        # Please, be aware that using the head of the branch instead of an immutable tag
        # or commit is not a good practice in general
        git.checkout("require_fmt")

    def config_options(self):
        if self.settings.os == "Windows":
            self.options.rm_safe("fPIC")

    def configure(self):
        if self.options.shared:
            self.options.rm_safe("fPIC")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        # if this generate method is all the defaults, it could be simplified to an
        # attribute e.g. generators = "CMakeToolchain"
        # This is what translates the conan options to CMake options
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["salty"]
