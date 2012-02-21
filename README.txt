python-xmltv
============

Introduction
------------
python-xmltv is a Python module that provides access to XMLTV data. XMLTV is
an XML format for storing TV listings.

More information on XMLTV can be found at http://membled.com/work/apps/xmltv/


Requirements
------------
There are no requirements for Python 2.5 and up. For older versions,
ElementTree is required, which can be found at
http://effbot.org/zone/element-index.htm


Usage
-----
Usage of the module is generally straight-forward::

    import xmltv
    from pprint import pprint

    # If you need to change the locale:
    # xmltv.locale = 'Latin-1'

    # If you need to change the date format used in the XMLTV file:
    # xmltv.date_format = '%Y%m%d%H%M%S %Z'

    filename = '/path/to/xmltv/file'

    # Print info for XMLTV file (source, etc.)
    pprint(xmltv.read_data(open(filename, 'r')))

    # Print channels
    pprint(xmltv.read_channels(open(filename, 'r')))

    # Print programmes
    pprint(xmltv.read_programmes(open(filename, 'r')))

There are currently three functions for reading that should be used:

    **read_data** ``(file_object) -> dict``
    Get the source and other info from an XMLTV file.

        Returns a dictionary of <tv> attributes, eg::

        {'date': u'20030702230041 -0300',
         'generator-info-name': u'tv_grab_na V3.20030629',
         'generator-info-url': u'http://sourceforge.net/projects/xmltv',
         'source-info-name': u'Zap2It',
         'source-info-url': u'http://www.zap2it.com'}

    **read_channels** ``(file_object) -> list``
    Get all of the channels.

    Returns a list of hashes, each representing a channel, eg::

        [{'display-name': [(u'Channel 10 ELTV', u'')],
          'id': u'C10eltv.zap2it.com'},
         {'display-name': [(u'Channel 11 CBHT', u'')],
          'icon': [{'desc': '','src': u'http://tvlistings2.zap2it.com/tms_network_logos/cbc.gif'}],
          'id': u'C11cbht.zap2it.com'}]

    **read_programmes** ``(file_object) -> list``
    Get all of the programmes.

    Returns a list of hashes, each representing a programme, eg::

        [{'audio': [{'stereo': [u'stereo']}],
          'category': [(u'Biz', u''), (u'Fin', u'')],
          'channel': u'C23robtv.zap2it.com',
          'start': u'20030702000000 ADT',
          'stop': u'20030702003000 ADT',
          'title': [(u'This Week in Business', u'')]},
         {'audio': [{'stereo': [u'stereo']}],
          'channel': u'C36wuhf.zap2it.com',
          'desc': [(u'In an effort to grow up, George proposes marriage to former girlfriend Susan.',
                    u'')],
          'rating': [{'system': u'VCHIP', 'value': u'PG'}],
          'start': u'20030702000000 ADT',
          'stop': u'20030702003000 ADT',
          'sub-title': [(u'The Engagement', u'')],
          'subtitles': [{'type': u'teletext'}],
          'title': [(u'Seinfeld', u'')]}]

There is also a Writer class. It should always write proper XMLTV data. All
strings, except for dictionary keys, should be in Unicode.

It contains the following methods:

    **__init__** ``(fp, encoding="iso-8859-1", date=None, source_info_url=None, source_info_name=None, generator_info_url=None, generator_info_name=None)`` -> ``Writer``
        Returns a Writer object.

    Arguments:

        ``fp``
        A File object to write XMLTV data to

            ``encoding``
        The text encoding that will be used. *Defaults to
        ``iso-8859-1``*

            ``date``
        The date this data was generated. *Optional*

            ``source_info_url``
        A URL for information about the source of the data. *Optional*

            ``source_info_name``
        A human readable description of ``source_info_url``.
        *Optional*

            ``generator_info_url``
        A URL for information about the program that is generating the
        XMLTV document. *Optional*

            ``generator_info_name``
        A human readable description of ``generator_info_url``.
        *Optional*

    **write_channel** ``(channel)``
    Write a channel dictionary

    Here's an example channel dictionary::

        {'display-name': [(u'Channel 11 CBHT', u'en')],
             'icon': [{'src': u'http://tvlistings2.zap2it.com/tms_network_logos/cbc.gif'}],
             'id': u'C11cbht.zap2it.com',
         'url': u:'http://www.cbc.com'}

    **write_programme** ``(programme)``
    Write a programme dictionary

    Here's an example programme dictionary::

        {'audio': [{'stereo': u'stereo'}],
             'category': [(u'Comedy', u'')],
             'channel': u'C36wuhf.zap2it.com',
             'country': [(u'USA', u'')],
             'credits': [{'producer': [u'Larry David'], 'actor': [u'Jerry Seinfeld']}],
             'date': [u'1995'],
             'desc': [(u'In an effort to grow up, George proposes marriage to former girlfriend Susan.',
                       u'')],
             'episode-num': [(u'7 . 1 . 1/1', u'xmltv_ns')],
             'language': [(u'English', u'')],
             'last-chance': [(u'Hah!', u'')],
             'length': [{'units': u'minutes', 'length': 22}],
             'new': [1],
             'orig-language': [(u'English', u'')],
             'premiere': [(u'Not really. Just testing', u'en')],
             'previously-shown': [{'channel': u'C12whdh.zap2it.com',
                                   'start': u'19950921103000 ADT'}],
             'rating': [{'icon': [{'height': u'64',
                                   'src': u'http://some.ratings/PGicon.png',
                                   'width': u'64'}],
                         'system': u'VCHIP',
                         'value': u'PG'}],
             'star-rating': [{'icon': [{'height': u'32',
                                        'src': u'http://some.star/icon.png',
                                        'width': u'32'}],
                              'value': u'4/5'}],
             'start': u'20030702000000 ADT',
             'stop': u'20030702003000 ADT',
             'sub-title': [(u'The Engagement', u'')],
             'subtitles': [{'type': u'teletext', 'language': (u'English', u'')}],
             'title': [(u'Seinfeld', u'')],
             'video': [{'colour': 1, 'aspect': u'4:3', 'present': 1}]}

    **end** ``()``
    Write end tag

    Call this before closing a file.

Reporting Bugs
--------------
Please send all bugs, comments, and questions to James Oakley
<jfunk@funktronics.ca>
