# Copyright cocotb contributors
# Licensed under the Revised BSD License, see LICENSE for details.
# SPDX-License-Identifier: BSD-3-Clause

# generated with mypy's stubgen script

from typing import Any

DRIVERS: int
ENUM: int
GENARRAY: int
INTEGER: int
LOADS: int
MEMORY: int
MODULE: int
NET: int
NETARRAY: int
OBJECTS: int
PACKAGE: int
REAL: int
REG: int
STRING: int
STRUCTURE: int
UNKNOWN: int

class gpi_cb_hdl:
    def deregister(self) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...

class gpi_iterator_hdl:
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __iter__(self) -> gpi_iterator_hdl: ...
    def __next__(self) -> gpi_sim_hdl: ...

class gpi_sim_hdl:
    def get_const(self) -> bool: ...
    def get_definition_file(self) -> str: ...
    def get_definition_name(self) -> str: ...
    def get_handle_by_index(self, index: int) -> gpi_sim_hdl: ...
    def get_handle_by_name(self, name: str) -> gpi_sim_hdl: ...
    def get_name_string(self) -> str: ...
    def get_num_elems(self) -> int: ...
    def get_range(self) -> tuple[int, int]: ...
    def get_signal_val_binstr(self) -> str: ...
    def get_signal_val_long(self) -> int: ...
    def get_signal_val_real(self) -> float: ...
    def get_signal_val_str(self) -> bytes: ...
    def get_type(self) -> int: ...
    def get_type_string(self) -> str: ...
    def iterate(self, mode: int) -> gpi_iterator_hdl: ...
    def set_signal_val_binstr(self, action: int, value: str) -> None: ...
    def set_signal_val_int(self, action: int, value: int) -> None: ...
    def set_signal_val_real(self, action: int, value: float) -> None: ...
    def set_signal_val_str(self, action: int, value: bytes) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...

def get_precision() -> int: ...
def get_root_handle(name: str) -> gpi_sim_hdl: ...
def get_sim_time() -> tuple[int, int]: ...
def get_simulator_product() -> str: ...
def get_simulator_version() -> str: ...
def is_running() -> bool: ...
def log_level(level: int) -> None: ...
def package_iterate() -> gpi_iterator_hdl: ...
def register_nextstep_callback(func, *args: Any) -> gpi_cb_hdl: ...
def register_readonly_callback(func, *args: Any) -> gpi_cb_hdl: ...
def register_rwsynch_callback(func, *args: Any) -> gpi_cb_hdl: ...
def register_timed_callback(time: int, func, *args: Any) -> gpi_cb_hdl: ...
def register_value_change_callback(
    signal: gpi_sim_hdl, func, edge: int, *args: Any
) -> gpi_cb_hdl: ...
def stop_simulator() -> None: ...
