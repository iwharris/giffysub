import pysrt
from metadata import SeasonalEpisodeMetadata


class SubIngestor(object):

    def __init__(self):
        pass

    def save(self):
        raise NotImplementedError("Abstract method is not implemented")


class SubFileProcessor(SubIngestor):

    def __init__(self, path):
        super(SubIngestor, self).__init__()
        self.path = path

        self.metadata = SeasonalEpisodeMetadata()
        self.metadata.episode = 1
        self.metadata.season = 3
        self.metadata.title = 'parks_and_recreation'
        self.metadata.locale = 'en'
        self.encoding = None
        self.subs = pysrt.open(self.path)

    def debug(self):
        for s in self.subs:
            print(self.to_string(s))

    def get_id(self, sub):
        return '%s_%s' % (self.metadata.to_id_string(), sub.index)

    def to_string(self, sub):
        return '%s: %s' % (self.get_id(sub), sub.text.replace('\n', ' '))

    def save(self):
        print('save')