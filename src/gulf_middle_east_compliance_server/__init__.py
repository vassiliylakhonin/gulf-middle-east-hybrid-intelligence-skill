"""MCP transport skeleton for the Gulf and Middle East specialist skill.

Nothing in this package screens anything. Every declared tool refuses instead
of answering; see :func:`unimplemented_response`.
"""

from .contract import NOT_IMPLEMENTED, unimplemented_response

__all__ = ["NOT_IMPLEMENTED", "unimplemented_response"]
