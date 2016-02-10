import pymp4parse
import widevine_pssh_pb2


class WvPsshExtractor(object):

    @classmethod
    def extract(cls, mp4_file):
        """
        Parameters
        ----------
        mp4_file : str
            MP4 file with a PSSH header


        Returns
        -------
        WidevinePsshData

        """

        boxes = pymp4parse.F4VParser.parse(filename=mp4_file)
        for box in boxes:
            if box.header.box_type == 'moof':
                pssh_box = box.pssh

                pssh = widevine_pssh_pb2.WidevinePsshData()
                pssh.ParseFromString(pssh_box.payload)
                return pssh

        # No Moof or PSSH header found
        return None

def main():

    import argparse
    import sys

    parser = argparse.ArgumentParser(description='Extracts and prints the WV PSSH data from an MP4 / ISO BMFF file')
    parser.add_argument('filename', metavar='mp4_file', nargs='+', help='mp4 file to parse')
    args = parser.parse_args()

    for filename in args.filename:
        if args.filename.index(filename) > 0:
            print ''

        print 'Filename: ' + filename
        pssh = WvPsshExtractor.extract(mp4_file=filename)

        if not pssh:
            print 'No PSSH found in "{file}"'.format(file=file)
            sys.exit(1)

        print ' algorith: ' + pssh.Algorithm.items()[pssh.algorithm][0]
        print ' key_id: ' + str(pssh.key_id).encode('hex')
        print ' provider: ' + pssh.provider
        print ' content_id: ' + pssh.content_id
        print ' track_type: ' + pssh.track_type
        print ' policy: ' + pssh.policy
        print ' crypto_period_index: ' + str(pssh.crypto_period_index)
        print ' grouped_license: ' + str(pssh.grouped_license)


if __name__ == "__main__":
    main()
