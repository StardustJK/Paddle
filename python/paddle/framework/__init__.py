#   Copyright (c) 2020 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# TODO: import framework api under this directory

from . import random  # noqa: F401
from .random import seed  # noqa: F401
from .framework import get_default_dtype  # noqa: F401
from .framework import set_default_dtype  # noqa: F401

from ..fluid.param_attr import ParamAttr  # noqa: F401
from ..fluid.core import CPUPlace  # noqa: F401
from ..fluid.core import IPUPlace  # noqa: F401
from ..fluid.core import CUDAPlace  # noqa: F401
from ..fluid.core import CUDAPinnedPlace  # noqa: F401
from ..fluid.core import NPUPlace  # noqa: F401
from ..fluid.core import MLUPlace  # noqa: F401
from ..fluid.core import CustomPlace  # noqa: F401
from ..fluid.core import VarBase  # noqa: F401

from ..fluid import core  # noqa: F401
from ..fluid.dygraph import base, layers, to_variable
from ..fluid.dygraph.base import no_grad_ as no_grad  # noqa: F401
from ..fluid.dygraph.base import grad  # noqa: F401
from .io import save  # noqa: F401
from .io import load  # noqa: F401

from .io_utils import _open_file_buffer  # noqa: F401
from .io_utils import is_parameter  # noqa: F401
from .io_utils import is_persistable  # noqa: F401
from .io_utils import is_belong_to_optimizer  # noqa: F401
from .io_utils import _clone_var_in_block_  # noqa: F401
from .io_utils import _pickle_loads_mac
from .io_utils import _pack_loaded_dict
from .io_utils import _unpack_saved_dict
from .io_utils import _load_program_scope

from ..fluid import monkey_patch_variable
from ..fluid.dygraph import monkey_patch_math_varbase
from ..fluid.framework import disable_signal_handler  # noqa: F401
from ..fluid.framework import get_flags  # noqa: F401
from ..fluid.framework import set_flags  # noqa: F401
from ..fluid.framework import Parameter, ParamBase
from ..fluid.dygraph.base import enable_dygraph as disable_static  # noqa: F401
from ..fluid.dygraph.base import disable_dygraph as enable_static  # noqa: F401
from ..fluid.framework import _non_static_mode as in_dynamic_mode  # noqa: F401
from ..fluid.framework import (  # noqa: F401
    _non_static_mode,  # temporary used for hackson
)
from ..fluid.framework import (
    _current_expected_place,
    _get_paddle_place,
)  # noqa: F401
from ..fluid.framework import dygraph_only  # noqa: F401
from ..fluid.framework import dygraph_not_support  # noqa: F401
from ..fluid.framework import (
    convert_np_dtype_to_dtype_,
    _varbase_creator,
    OpProtoHolder,
)  # noqa: F401
from ..fluid.framework import _dygraph_tracer  # noqa: F401
from ..fluid.framework import generate_control_dev_var_name  # noqa: F401

from ..fluid.layer_helper import LayerHelper  # noqa: F401
from ..fluid.framework import in_dygraph_mode  # noqa: F401
from ..fluid.framework import _global_flags  # noqa: F401
from ..fluid.framework import _apply_pass  # noqa: F401
from ..fluid.framework import switch_main_program
from ..fluid.framework import switch_startup_program
from ..fluid.framework import _set_expected_place  # noqa: F401
from ..fluid.framework import Block, Program  # noqa: F401
from ..fluid.framework import IrGraph  # noqa: F401
from ..fluid.framework import deprecate_stat_dict

__all__ = []
