# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Gekkofs(CMakePackage):
    """
    GekkoFS is a file system that aims to exploit this performance advantage to accelerate the I/O from scientific applications. The basic design idea behind GekkoFS is to construct a distributed storage space from node-local storage devices that has the same ephemeral life cycle of a batch-submitted job.
    """

    homepage = "https://storage.bsc.es/projects/gekkofs/"
    git = "https://storage.bsc.es/gitlab/hpc/gekkofs.git"

    maintainers = ['marcvef']

    version('develop', submodules=True)
    version('prometheus', sha256='cb477c7d32c1f983df322663dcd6796205083a83dd6978a7f7facc1ed6b2effd', url="https://france.paratools.com/tau_metric_proxy/gekkofs-prom.tar.gz")

    # Fix date dependency detection
    patch("date.patch", when="@develop")

    # All dependencies
    depends_on('syscall-intercept +gekkofs')
    depends_on('mochi-margo')
    depends_on('rocksdb +rtti')
    depends_on('lz4')
    depends_on('date +tz +shared cxxstd=14 tzdb=system')
    depends_on('tau-metric-proxy +mpi', when="+tau", type=('build', 'run'))

    # variant key : [ DOC, ENABLED_BY_DEFAULT, CMAKE_FLAG(BOOL) ]
    all_variants = {"jemalloc": ["Use Jemalloc allocator", False, None],
                    "doc": ["Build documentation", False, "GKFS_BUILD_DOCUMENTATION"],
                    "symlinks": ["Build symbolic link support", True, "SYMLINK_SUPPORT"],
                    "log": ["Enable logging messages", True, "ENABLE_CLIENT_LOG"],
                    "forwarding": ["Enable forwarding mode", False, "GKFS_ENABLE_FORWARDING"],
                    "agios": ["Enable AGIOS scheduling", False, "GKFS_ENABLE_AGIOS"],
                    "guided": ["Use guided data-distributor", False, "GKFS_USE_GUIDED_DISTRIBUTION"],
                    "tau": ["Enable tau metric proxy prometheus exporter", False, "GKFS_PROMETHEUS_STATS"],
                    "tests": ["Build tests", False, "GKFS_BUILD_TESTS"]}

    for k, v in all_variants.items():
        variant(k, default=v[1], description=v[0])

    conflicts("+tau", when="@develop",msg="Only the @prometheus version can have +tau")

    depends_on("jemalloc", when="+jemalloc")

    depends_on("doxygen", when="+doc")
    depends_on("py-sphinx", when="+doc")
    depends_on("py-breathe", when="+doc")

    depends_on("agios", when="+agios")

    def cmake_args(self):
        args = []

        for k, v in Gekkofs.all_variants.items():
            if not v[2]:
                continue
            if "+{}".format(k) in self.spec:
                args.append('-D{}=true'.format(v[2]))
            else:
                args.append('-D{}=false'.format(v[2]))

        return args
