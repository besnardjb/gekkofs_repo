# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Agios(CMakePackage):
    """an I/O request scheduling library at file level"""

    homepage = "https://github.com/francielizanon/agios"
    url      = "https://github.com/francielizanon/agios"
    git      = "https://github.com/francielizanon/agios.git"

    version('develop', branch="master")

    depends_on('libconfig')
