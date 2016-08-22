class CollectionMetadata(object):

    def __init__(self):
        pass

    def to_id_string(self):
        raise NotImplementedError("Abstract method is not implemented")


class SeasonalEpisodeMetadata(CollectionMetadata):

    def __init__(self):
        super(CollectionMetadata, self).__init__()
        self.season = None
        self.episode = None
        self.title = None
        self.locale = None

    def to_id_string(self):
        return '%s_s%.2de%.2d_%s' % (self.title, self.season, self.episode, self.locale)
