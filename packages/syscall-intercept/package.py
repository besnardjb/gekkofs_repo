# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class SyscallIntercept(CMakePackage):
    """Userspace syscall intercepting library."""
    homepage = "https://github.com/pmem/syscall_intercept"
    url = "https://github.com/pmem/syscall_intercept"
    git = "https://github.com/pmem/syscall_intercept.git"

    # Only available on github
    version('master', branch="master")

    depends_on('capstone +shared')
    depends_on('perl')

    # Build doc ?
    variant('doc', default=False, description="Build documentation")
    depends_on('pandoc', when="+doc")

    # Build tests ?
    variant('tests', default=False, description="Build tests")

    # Add gekkofs extended syscall interception patch
    variant('gekkofs', default=False, description="Apply gekkofs patches")
    patch('syscall_intercept.patch', when="+gekkofs")

    # Fix capstone detection
    patch('dep-capstone.patch')

    def cmake_args(self):
        args = ["-DBUILD_EXAMPLES=false"]

        if "+tests" in self.spec:
            args.append("-DBUILD_TESTS=true")
        else:
            args.append("-DBUILD_TESTS=false")

        return args
