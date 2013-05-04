"""
Functions that can be used for comparison of pixels, for example when clustering. Pixels in this case are lists of
channel values.
"""

def all_channels_diff(pixel, other_pixel):
    #Return the difference of both pixel's channels, accumulated.
    return sum(abs(channel - other_channel) for channel, other_channel in izip(pixel, other_pixel))

def each_channels_diff(channel_value, other_channel_value):
    return abs(channel_value-other_channel_value)