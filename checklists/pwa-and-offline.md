# PWA and offline

## Installability
- Manifest loads without authentication (a password gate in front of the test site can block it with a 401).
- Name, short name, icons (including maskable), start URL, display mode, theme colour.
- Android: install prompt appears on a supported browser; installed app opens full screen.
- iPhone: "Add to Home Screen" from the browser share menu; icon and name are right; no install prompt exists, so check the guidance wording.

## Service worker
- Registers over HTTPS; scope is correct.
- Offline: the app shell opens; pages that need data show a clear offline message, not a blank page.
- Update: a new release reaches installed users. Check the stale-cache case (old version after deploy).
- Authenticated pages are not cached for the next user on a shared device.

## Behaviour
- Rotate the device; small and large screens; safe areas (notch).
- Back button and deep links inside the installed app.
- Session and token storage after the app is closed and reopened.
- Push notifications (if any): permission prompt timing, denied state.

## Evidence
Record device, OS and browser version, build, and whether the app was installed or in a tab.
