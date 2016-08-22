class Metadata(object):

    def __init__(self):
        pass

    def to_id_string(self):
        raise NotImplementedError("Abstract method is not implemented")

    def get_metadata_type(self):
        raise NotImplementedError("Abstract method is not implemented")


class SeasonalEpisodeMetadata(Metadata):

    def __init__(self):
        super(Metadata, self).__init__()
        self.season = None
        self.episode = None
        self.title = None
        self.locale = None

    def to_id_string(self):
        return '%s_s%.2de%.2d_%s' % (self.title, self.season, self.episode, self.locale)

    def get_metadata_type(self):
        return 'seasonal_episode'


class MovieMetadata(Metadata):

    def __init__(self):
        super(Metadata, self).__init__()
        self.title = None
        self.locale = None

    def to_id_string(self):
        return '%s_%s' % (self.title, self.locale)

    def get_metadata_type(self):
        return 'movie'
