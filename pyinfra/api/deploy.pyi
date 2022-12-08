from typing import (Any, Callable, Dict, Generic, Iterable, List, Mapping,
                    Protocol, Tuple, overload)

from typing_extensions import ParamSpec

from pyinfra.api.host import Host
from pyinfra.api.state import State

P = ParamSpec("P")

class Deploy(Generic[P], Protocol):
    def __call__(self, 
        _sudo: bool|None = None,
        _sudo_user: str|None = None,
        _use_sudo_login: bool|None = None,
        _use_sudo_password: bool|None = None,
        _preserve_sudo_env: bool|None = None,
        _su_user: str|None = None,
        _use_su_login: bool|None = None,
        _preserve_su_env: bool|None = None,
        _su_shell: str|None = None,
        _doas: bool|None = None,
        _doas_user: str|None = None,
        _shell_executable: str|None = None,
        _chdir: str|None = None,
        _env: Mapping[str, str]|None = None,
        _success_exit_codes: Iterable[int]|None = None,
        _timeout: int|None = None,
        _get_pty: bool|None = None,
        _stdin: str|List[str]|Tuple[str, ...]|None = None,
        name: str|None = None,
        _ignore_errors: bool|None = None,
        _continue_on_error: bool|None = None,
        _precondition: str|None = None,
        _postcondition: str|None = None,
        _on_success: Callable[[State, Host, str], None]|None = None,
        _on_error: Callable[[State, Host, str], None]|None = None,
        _parallel: int|None = None,
        _run_once: bool|None = None,
        _serial: bool|None = None,
        *args: P.args, 
        **kwargs: P.kwargs
    ) -> None: ...


def deploy(
    name: str,
    data_defaults: Dict[str, Any]|None = None,
) -> Callable[[Callable[P, None]], Deploy[P]]: ...