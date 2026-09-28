# declared-behaviour — three things a document asks its host for

One page, three declared behaviours: a sound (`sound.play`), a position (`location`), a map
(`map` widget). Each box prints only what came back through `onSuccess` / `onError`. The runtime
draws nothing in place of a thing it cannot do (UI DSL §6.13).

## Run it

AppPlayer → `Add app → Bundle → Folder` → `declared_behaviour.mbd/`. Press the two buttons.

## Measured on

`flutter_mcp_ui_runtime 0.7.7 · core 0.6.5 · appplayer_core 0.1.27`, AppPlayer Standard (macOS
debug build), 2026-09-04. Captures = the host's own `ui.screenshot`.

| ask | host declares it | what the document received |
|---|---|---|
| `sound.play` chime | yes (`RuntimeCapabilities.sound = JustAudioSoundPort()`) | performed; `onError` did not fire |
| `location` (coarse) | no | `onError` · `LOCATION_UNAVAILABLE` · "capability unavailable: location (this runtime does not claim the Location Profile)" |
| `map` | no (`mapBuilder` not set) | `onError` at build · `CAPABILITY_UNAVAILABLE` · "capability unavailable: map"; the map box stays empty |

Two hosts were compared by their composition roots, not by running both: AppPlayer Standard
(`os/appplayer/appplayer/dart/lib/app/composition_root.dart`) and AppPlayer Cloud
(`saas_app/appplayer_cloud/lib/app/composition_root.dart`) declare the same set — `sound`, `media`
(video), `webViewBuilder`, `lottieBuilder`, `pdfBuilder` — and neither declares `mapBuilder`,
`payment` or `location`. This document gets the same three answers on either.
