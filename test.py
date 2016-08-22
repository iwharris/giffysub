from ingest import SubFileProcessor as SubFileProcessor
import os

if __name__ == '__main__':
    process = SubFileProcessor(os.path.join('examples', 's03e01.en.srt'))
    process.debug()
