## Widevine Modular PSSH Decoder
 
Python based PSSH header dumper for MP4 / MP4 ISO Base Media File Format / DASH Fragments

## Usage

### Script

    wvpsshdump myfile.mp4 

Output:

    Filename: myfile.mp4
     algorith: AESCTR
     key_id: ffffff
     provider: myprovider
     content_id: 1234567890
     track_type: 
     policy: 
     crypto_period_index: 1198817
     grouped_license: 


## Programmatically


    >>> import pywvpssh
    >>> pssh = WvPsshExtractor.extract(mp4_file=filename)
    >>> type(pssh)
    widevine_pssh_pb2.WidevinePsshData
    
    >>> pssh.content_id
    1234567890


## Installation

## Quick

Pip install with dependencies:

    pip install https://github.com/use-sparingly/pymp4parse/zipball/master \
                https://github.com/use-sparingly/pywvpssh/zipball/master 

### Requirements

- pymp4parse: https://github.com/use-sparingly/pymp4parse
- Protobuf: https://pypi.python.org/pypi/protobuf


