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
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "http://france.paratools.com/tau_metric_proxy/strace_tau-0.1.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('0.1', sha256='5a3e4e5fdb9eaaa7b4c682128e3a442bd620197d59483f5ce0203197a8f4e35b')

    # FIXME: Add dependencies if required.
    depends_on('tau-metric-proxy +mpi')

    def configure_args(self):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = ["--enable-mpers=check"]
        return args
