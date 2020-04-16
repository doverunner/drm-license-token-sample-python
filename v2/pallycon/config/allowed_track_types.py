ALLOWED_TRACK_TYPES = ('SD_ONLY', 'SD_HD', 'SD_UHD1', 'SD_UHD2')

#: Type of the allowed_track_types
SD_ONLY = ALLOWED_TRACK_TYPES[0]
SD_HD = ALLOWED_TRACK_TYPES[1]
SD_UHD1 = ALLOWED_TRACK_TYPES[2]
SD_UHD2 = ALLOWED_TRACK_TYPES[3]


def check(allowed_track_types):
    return allowed_track_types in ALLOWED_TRACK_TYPES
