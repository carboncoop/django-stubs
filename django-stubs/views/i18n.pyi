# Stubs for django.views.i18n (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.views.generic import View
from typing import Any, Optional

from django.core.handlers.wsgi import WSGIRequest
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from typing import Any, Dict, List, Optional, Union

LANGUAGE_QUERY_PARAMETER: str

def set_language(request: WSGIRequest) -> HttpResponseRedirect: ...
def get_formats() -> Dict[str, Union[str, int, List[str]]]: ...

js_catalog_template: str

def render_javascript_catalog(
    catalog: Optional[Any] = ..., plural: Optional[Any] = ...
): ...
def null_javascript_catalog(
    request: Any, domain: Optional[Any] = ..., packages: Optional[Any] = ...
): ...

class JavaScriptCatalog(View):
    domain: str = ...
    packages: Any = ...
    translation: Any = ...
    def get(self, request: WSGIRequest, *args: Any, **kwargs: Any) -> HttpResponse: ...
    def get_paths(self, packages: List[str]) -> List[str]: ...
    @property
    def _num_plurals(self) -> int: ...
    @property
    def _plural_string(self) -> Optional[str]: ...
    def get_plural(self) -> Optional[str]: ...
    def get_catalog(self) -> Dict[str, Union[str, List[str]]]: ...
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]: ...
    def render_to_response(
        self,
        context: Dict[
            str,
            Optional[
                Union[
                    Dict[str, str],
                    Dict[str, Union[str, int, List[str]]],
                    Dict[str, Union[str, List[str]]],
                ]
            ],
        ],
        **response_kwargs: Any,
    ) -> HttpResponse: ...

class JSONCatalog(JavaScriptCatalog):
    def render_to_response(
        self,
        context: Dict[
            str,
            Union[
                Dict[str, Union[str, List[str]]], Dict[str, Union[str, int, List[str]]], str
            ],
        ],
        **response_kwargs: Any,
    ) -> JsonResponse: ...