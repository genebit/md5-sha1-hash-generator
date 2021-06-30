
# Reference links that helped me in writing this project:
# https://www.geeksforgeeks.org/difference-between-md5-and-sha1/
# https://www.geeksforgeeks.org/md5-hash-python/
# 
# NOTE: this link is 11 years old, but still a fun read on md5
# https://stackoverflow.com/questions/1240852/is-it-possible-to-decrypt-md5-hashes
# 
# NOTE: MD5 and SHA1 hash algorithm are apparently not secured anymore.
#       still, this algorithm are still hard to break.
#       might use this for small password encryptions for projects where securities are not too important.

try:
    import hashlib
except ImportError as err:
    print('An Error occured importing hashlib\n Error log: {0}'.format(err))

string = input('Enter string to convert: ')

class HashGenerator:
    def md5_convert(string):
        convert = hashlib.md5(string.encode())
        res = convert.hexdigest()
        return res

    def sha1_convert(string):
        convert = hashlib.sha1(string.encode())
        res = convert.hexdigest()
        return res

md5_result = HashGenerator.md5_convert(string)
sha1_result = HashGenerator.sha1_convert(string)

if __name__ == '__main__':
    print('MD5 Hash: {0}'.format(md5_result))
    print('SHA1 Hash: {0}'.format(sha1_result))