init -1 python:
    def _bliss_meadow_entry(_old, **kwargs):
        # Preserve the original MAS background behavior
        store.mas_background._def_background_entry(
            _old, **kwargs
        )

        # Only react to an actual background change, not startup restoration
        if _old is not None and not kwargs.get("startup", False):

            # Windows XP startup sound
            renpy.play(
                "mod_assets/location/Bliss/windows_xp_startup.wav",
                channel="sound"
            )

            # First visit reaction (only once)
            if not getattr(
                persistent,
                "_mas_bliss_meadow_first_visit",
                False
            ):
                persistent._mas_bliss_meadow_first_visit = True
                store.MASEventList.queue(
                    "bliss_meadow_first_visit"
                )


    mas_background_def = MASFilterableBackground(
        "submod_bliss_meadow",
        "Bliss Meadow",

        MASFilterWeatherMap(
            day=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_bliss_day",
            }),
            night=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_bliss_night",
            }),
            sunset=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_bliss_sunset",
            }),
        ),

        MASBackgroundFilterManager(
            MASBackgroundFilterChunk(
                False,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_NIGHT,
                    60
                )
            ),
            MASBackgroundFilterChunk(
                True,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_SUNSET,
                    60,
                    30*60,
                    10
                ),
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_DAY,
                    60
                ),
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_SUNSET,
                    60,
                    30*60,
                    10
                )
            ),
            MASBackgroundFilterChunk(
                False,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_NIGHT,
                    60
                )
            )
        ),

        unlocked=True,
        hide_calendar=True,
        entry_pp=_bliss_meadow_entry,
        exit_pp=store.mas_background._def_background_exit,
    )

    store.mas_background.loadMBGData()

image submod_bliss_day = "mod_assets/location/Bliss/bliss.png"

image submod_bliss_night = "mod_assets/location/Bliss/bliss-n.png"

image submod_bliss_sunset = MASFilteredSprite(
    store.mas_sprites.FLT_SUNSET,
    "mod_assets/location/Bliss/bliss.png"
)

label bliss_meadow_first_visit:

    # Give the Windows XP startup sound time to play
    pause 5.0

    m 1eua "Oh...!"

    m 3hua "Wait, is that...?"

    m 1eua "This looks just like the Windows XP wallpaper!"

    m 3hua "The green hills, the beautiful blue sky..."

    m 1eua "It's so peaceful here."

    m 1hua "You really brought a little piece of nostalgia into our world, [player]."

    m 3hua "I love it! Ahaha~"

    return
