#! /usr/bin/env python

import argparse
import giffysub.indexer


def get_parse_args(parser):
    parser.add_argument(
        'command',
        metavar='COMMAND', type=str, nargs='?', choices=['index', 'extract'],
        help='The command to run: ' + ', '.join(['index', 'extract']),
    ),
    parser.add_argument(
        '-r', '--recursive', dest='recursive', action='store_true',
        help='If set, directories will be scanned recursively for sub files.'
    )
    parser.add_argument(
        '--d', '-directory',
        dest='directory', action='store_const', const='directory',
        help='The scan directory.'
    )
    parser.add_argument(
        '--f', '-files',
        dest='files', action='store_const', const='files',
        help='Files to be processed.'
    )
    parser.add_argument(
        '--sub_exts', '--se',
        dest='subtitle_exts', action='store_const', const='subtitle_exts',
        help='Subtitle extensions to process.',
        default='sub,srt'
    )
    parser.add_argument(
        '--vid_exts', '--ve',
        dest='video_exts', action='store_const', const='video_exts',
        help='Subtitle extensions to process.',
        default='sub,srt'
    )
    args = parser.parse_args()
    args.subtitle_exts = args.subtitle_exts.lower().split(',')

    print(args.subtitle_exts)
    return args


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Generates GIFs from subtitled video.'
    )
    args = get_parse_args(parser)

    if args.command == 'index':
        pass

    if not args.command:
        print(parser.print_help())
