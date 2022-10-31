# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install tau-metric-proxy
#
# You can edit this file again by typing:
#
#     spack edit tau-metric-proxy
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class TauMetricProxy(AutotoolsPackage):
    """An HPC oriented prometheus proxy"""

    homepage = "https://www.admire-eurohpc.eu/"
    url      = "http://france.paratools.com/tau_metric_proxy/tau_metric_proxy-0.1.tar.gz"

    maintainers = ['besnardjb']

    version('0.2', sha256='90070c53426b38b57e5cdfc3f81b0825b81ecc7b5b0e627b3ee9ff943111018a')
    version('0.1', sha256='9df23747746e63c60638e19ff2b1615a984cb6a2ec0755804a1766ab2bf1e292')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')


    variant("python", default=False, description="Build the python CLI client")
    depends_on('py-pip', type=('build', 'run'), when="+python")

    variant("mpi", default=False, description="Build the MPI exporter library")
    depends_on("mpi", when="+mpi")

    def autoreconf(self, spec, prefix):
        autoreconf('--install', '--verbose', '--force')

    def configure_args(self):
        args = []
        return args
