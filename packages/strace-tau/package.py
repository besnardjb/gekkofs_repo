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
#     spack install strace-tau
#
# You can edit this file again by typing:
#
#     spack edit strace-tau
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class StraceTau(AutotoolsPackage):
    """A modified version of strace sending data to the tau-metric-proxy"""

    homepage = "https://www.admire-eurohpc.eu/"
    url      = "http://france.paratools.com/tau_metric_proxy/strace_tau-0.1.tar.gz"

    maintainers = ['besnardjb']

    version('0.2', sha256='2276014c12f5a06c538640addcc79e4ae3e8ab488acf5b497bdc023af3173303')
    version('0.1', sha256='5a3e4e5fdb9eaaa7b4c682128e3a442bd620197d59483f5ce0203197a8f4e35b')

    depends_on('tau-metric-proxy', type=('build', 'run'))

    def configure_args(self):
        args = ["--enable-mpers=check", "--program-prefix=tau_"]
        return args
