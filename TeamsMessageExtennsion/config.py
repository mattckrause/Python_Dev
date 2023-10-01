#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "ec08a649-17fc-4179-a18c-6933c50fdd00")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "Uge8Q~ydSnfqjPyovVtOarHu-JFhe-cXl5~_ydx5")
