#!/usr/bin/env python
#http://eli.thegreenplace.net/2010/06/25/
#aes-encryption-of-files-in-python-with-pycrypto

import os, random, struct, hashlib, argparse
from Crypto.Cipher import AES

def encrypt_file(key, in_filename, out_filename=None, \
                 chunksize=64*1024):
    '''
    Encrypts a file using AES (CBC mode) with the
    given key

    key:
        The encryption key - a string that must be
        either 16, 24 or 32 bytes long. Longer keys
        are more secure

    in_filename:
        Name of the input file

    out_filename:
        If None, '<in_filename>.enc' will be used.

    chunksize:
        Sets the size of the chink which the function
        uses to read and encrypt the file. Larger chunk
        sizes can be faster for some files and machines.
        chunksize must be divisible by 16.
    '''

    if not out_filename:
        out_filename = in_filename + '.enc'

    iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(in_filename)

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)

                outfile.write(encryptor.encrypt(chunk))


def decrypt_file(key, in_filename, out_filename=None, \
                 chunksize=24*1024):
    '''
    Decrypts a file using AES (CBC mode) with the
    given key. Parameters are similar to encrypt a file,
    with one difference: out_filename, if not supplied
    will be in_filename without its last extension
    (i.e. if in_filename is 'aaa.zip.enc' the out_filename
    will be 'aaa.zip')
    '''

    if not out_filename:
        out_filename = 'out_' + os.path.splitext(in_filename)[0]

    with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(\
            struct.calcsize('Q')))[0]
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(origsize)

def main():

    parser = argparse.ArgumentParser(description='Enc/De crypt \
        some file')
    parser.add_argument('-m','--mode',dest='mode',action='store',
        choices={'encrypt','decrypt'})
    parser.add_argument('-k','--key',dest='key',action='store')
    args = parser.parse_args()

    if not args.key:
        password = 'kitty'
    else:
        password = args.key

    # Generate a 32-byte key from the password
    key = hashlib.sha256(password).digest()

    if args.mode == 'encrypt':
        #Encrypt the file: key, infile, outfile
        encrypt_file(key,'aes_crypt.py')
    elif args.mode == 'decrypt':
        #Decrypt the file: key, infile, outfile
        decrypt_file(key, 'aes_crypt.py.enc')
    else:
        parser.print_help()
        exit(1)

if __name__ == '__main__':
    main()
