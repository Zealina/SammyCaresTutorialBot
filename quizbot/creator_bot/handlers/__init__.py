"""
Advance Quiz Bot — Open Source Project
This project was originally developed by Gagan (github.com/devgaganin).
Reference: https://t.me/advance_quiz_bot
The codebase has been reviewed and verified with the assistance of Claude AI.
"""

from __future__ import annotations

from pyrogram import Client

from . import (
    admin,
    ai_keys,
    auth,
    batches,
    file_import,  # noqa: F401 -- imported for side-effect-free reuse by quiz_creation
    inline,
    payments,
    quiz_creation,
    quiz_editing,
    quiz_management,
    reports,
    settings,
)

__all__ = ["register"]

async def debug_all_callbacks(client, callback_query):
    print("\n========== CALLBACK QUERY ==========")
    print("data:", repr(callback_query.data))
    print("from_user:", callback_query.from_user.id if callback_query.from_user else None)
    print("message:", callback_query.message.id if callback_query.message else None)
    print("====================================\n")


def register(app: Client) -> None:
    """Register every handler module's commands/callbacks on `app`."""
    #app.on_callback_query()(debug_all_callbacks)
    admin.register(app)
    auth.register(app)
    quiz_creation.register(app)
    payments.register(app)
    ai_keys.register(app)
    settings.register(app)
    quiz_management.register(app)
    batches.register(app)
    reports.register(app)
    quiz_editing.register(app)
    inline.register(app)
