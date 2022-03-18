# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Capstone(CMakePackage):
    """Capstone is a lightweight multi-platform, multi-architecture disassembly framework."""

    homepage = "https://www.capstone-engine.org/"
    url = "https://github.com/aquynh/capstone/archive/4.0.2.tar.gz"
    git = "https://github.com/capstone-engine/capstone"

    version('develop', branch='next')
    version('5.0-rc2',
            sha256='869d94813a887329bc11b4bf1f4410a7a2b7f270176439e90b158127d5a215dd')
    version('5.0-rc1',
            sha256='b82146147c86924371fb87cba170f0b1c163366d60ae61db3ded47ba49ea6df2')
    version('4.0.2',
            sha256='7c81d798022f81e7507f1a60d6817f63aa76e489aa4e7055255f21a22f5e526a')
    version('4.0.1',
            sha256='79bbea8dbe466bd7d051e037db5961fdb34f67c9fac5c3471dd105cfb1e05dc7')
    version('4.0-alpha5',
            sha256='003b21b00bcae8842002cc83da1f3277cf386202a3559849d7e9d52c6babc706')
    version('4.0-alpha4',
            sha256='d75d0a2b8e74a5fab0732d338ee743adef640e05fea75599a0073f7deec0b759')
    version('4.0',        sha256='26c6461618670d59215635602ef5fb6f90bf6724006983af88e4983d6af1e67a')
    version('3.0.5-rc3',
            sha256='a811d0fee15e0ca49df0e84c41dc4996adf8d41adda446d61b0d584052ee8381')
    version('3.0.5-rc2',
            sha256='587c092454ad59137686529f3c008c265cc6d427a85d5d2e8f6a902b72d215b3')
    version('3.0.5',
            sha256='913dd695e7c5a2b972a6f427cb31f2e93677ec1c38f39dda37d18a91c70b6df1')

    # variant key : [ DOC, ENABLED_BY_DEFAULT, CMAKE_FLAG(BOOL) ]
    all_variants = {"shared": ["Build capstone shared library", True, "BUILD_SHARED_LIBS"],
                    "diet":   ["Build diet library", False, "CAPSTONE_BUILD_DIET"],
                    "osxkernel": ["Build osx kernel module support", False, "CAPSTONE_OSXKERNEL_SUPPORT"],
                    "disablex86att": ["Disable x86 at&t syntax", False, "CAPSTONE_X86_ATT_DISABLE"],
                    "x86reduce": ["Reduce x86 instruction-set", False, "CAPSTONE_X86_REDUCE"],
                    "cstool": ["Build cstool", False, "CAPSTONE_BUILD_CSTOOL"]}

    for k, v in all_variants.items():
        variant(k, default=v[1], description=v[0])

    def cmake_args(self):
        args = []

        for k, v in Capstone.all_variants.items():
            if "+{}".format(k) in self.spec:
                args.append('-D{}=true'.format(v[2]))
            else:
                args.append('-D{}=false'.format(v[2]))

        return args
