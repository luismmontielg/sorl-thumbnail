import socket
import sys
from django.conf import settings


# When True Thumbnail.render can raise errors
THUMBNAIL_DEBUG = False

# Thumbnail backend
THUMBNAIL_BACKEND = 'sorl.thumbnail.backends.pil.ThumbnalBackend'

# Image format, common formats are: JPEG, PNG
# Make sure the backend can handle the format you specify
THUMBNAIL_FORMAT = 'JPEG'

# Colorspace, backends are required to implement: RGB, GRAY
# Setting this to None will keep the original colorspace.
THUMBNAIL_COLORSPACE = 'RGB'

# Quality, 0-100
THUMBNAIL_QUALITY = 95

# Default file storage for the generated thumbnail
THUMBNAIL_FILE_STORAGE = settings.DEFAULT_FILE_STORAGE

# DB Cache timeout. You should keep this at maximum since invalidating is taken
# care of already
THUMBNAIL_CACHE_TIMEOUT = sys.maxint

# DB Cache prefix, make sure this does not collide with other cache keys
THUMBNAIL_CACHE_PREFIX = 'sorl-thumbnail-'

# Return this when an error is raised and THUMBNAIL_DEBUG is False
THUMBNAIL_ERROR = ''

# Timeout for fetching remote images
THUMBNAIL_URL_TIMEOUT = socket._GLOBAL_DEFAULT_TIMEOUT

