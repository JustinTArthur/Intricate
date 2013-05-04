"""
A source pixel is a list of numerical values, for example R,G, & B integers.
A source bitmap is source pixels, arranged in rows. Looks like:
[
	[ [24,200,51],[100,55,62],[3,45,140] ],
	[ [244,1,8],[70,55,6],[3,45,140] ],
	[ [73,20,51],[10,5,62],[3,45,140] ],
]
This one has a width of 3
"""

def allEqual(iterable):
    try:
        first = next(iterable)
        return all(first == rest for rest in iterable)
    except StopIteration:
        return True

def validate_images(images):
    #Same size?:
    if not allEqual(len(i) for i in images):
        raise Exception("Invalid")


def technique1(stack_of_source_images, group_incidents_by="pixel", difference_threshold=(255/2), noise_threshold=0):
    """
    Returns a single image, consisting of the result sub-pixels.


    :param stack_of_source_images:
    :param group_incidents_by:
    :param difference_threshold: The maximum difference between two pixels' channel sums before they can be grouped into the same incident group.
    :param noise_threshold: The percent of source images that need to have a similar incident in the same place before that incident's color or whatever is considered legit/non-noise.
    """

    from itertools import izip
    from cluster import HierarchicalClustering
    from pixel_difference import all_channels_diff

    minimum_incidents_per_group = len(stack_of_source_images) * (noise_threshold * 0.01)

    for s_rows_zip in izip(stack_of_source_images):
        for s_pixels_zip in zip(s_rows_zip):
            # Group the pixels into clusters of similar ones, based on the threshold of total difference in all channels.
            clusters=HierarchicalClustering(s_pixels_zip, all_channels_diff).getlevel(difference_threshold)
            # TODO: offer clustering and whatnot from the channel level instead of pixel level.

            #Filter out noise:
            clusters = [cluster for cluster in clusters if len(cluster) > minimum_incidents_per_group]