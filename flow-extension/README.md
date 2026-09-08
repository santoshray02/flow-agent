# Flow Agent Chrome Extension

Chrome bridge for [kodelyx/flow-agent](https://github.com/kodelyx/flow-agent). It connects a logged-in Google Flow tab to the local Flow Agent backend.

## Features

- Live backend health and Flow credit status
- Premium light-mode side panel opened directly from the extension icon
- Quick image and video generation with persistent history
- Nano Banana 2 as the default image model
- Model, aspect ratio, and video duration controls
- Compact agent monitoring, token refresh, and Flow controls

## Install

1. Start the backend with `flow`.
2. Open `chrome://extensions` and enable **Developer mode**.
3. Click **Load unpacked** and select this `flow-extension` folder.
4. Open <https://labs.google/fx/tools/flow>, sign in, and keep the tab open.
5. Click the extension icon to open Flow Agent in Chrome's side panel.

## Flow site compatibility

The extension recognizes both the current `https://flow.google.com/` site and
the legacy `https://labs.google/fx/tools/flow` route. This is partial issue #10
compatibility: authentication and CAPTCHA behavior, plus the existing REST and
upload calls on the new site, have not been verified end to end and may still
require follow-up changes.

Main documentation: [Flow Agent README](../README.md)
