#!/usr/bin/env python3

print('\033[33mWarning:\033[0m This script was very much a one-use type of ' +\
      'affair. It\'s just here for the curious.\n')

in_file = open('ter-u12n_unicode.bdf', 'r')
out_file = open('ter-u12n_unicode_shift.bdf', 'w')

i = 4
for line in in_file:
    i += 1
    if (i % 21) < 14 and i > 37:
        original_hex = line.rstrip('\n')
        original_int = int(original_hex, 16)
        original_bin = bin(original_int)[2:].zfill(8)[0:6]
        shift_bin = '0' + original_bin + '0'
        shift_int = int(shift_bin, 2)
        shift_hex = hex(shift_int)[2:].zfill(2).upper()
        out_file.write(shift_hex + '\n')
    else:
        if (i % 21) == 15 and i > 53:
            out_file.write('\n')
        out_file.write(line)
