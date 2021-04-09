import struct
import binascii

with open('udp_stream_2.dmp', 'r') as file:
    data = file.readlines()

# Remove the first entry in `data` since it is an empty line.
del data[0]

def get_filename(get_data):
    hex_string = get_data.strip()
    get_command = binascii.unhexlify(hex_string).decode("utf-8")
    filename = get_command[4:].rstrip('\x00')
    return filename

current_data = bytearray()
current_filename = get_filename(data[0])
next_segment_id = 1
for idx, segment in enumerate(data[1:]):
    segment_bytes = bytes.fromhex(segment.strip())

    # If segment starts with the word "get" or the end of `data` is reached then
    # a new file is being requested.
    end_of_data = idx+2 == len(data)
    if segment_bytes.startswith(bytes.fromhex("676574")) or end_of_data:
        print("Saving file %s" % current_filename)
        with open(current_filename, 'wb') as out:
            out.write(current_data)

        if end_of_data:
            break

        current_data = bytearray()
        current_filename = get_filename(segment)
        next_segment_id = 1
        print("Found file %s" % current_filename)
    elif len(segment) == 4129:
        segment_id, segment_op = struct.unpack('<QQ', segment_bytes[:16])

        if segment_id == next_segment_id:
            current_data.extend(segment_bytes[16:])
            next_segment_id += 1
        else:
            print("Error: Expected segment with ID %i, but got segment with ID %i" % (segment_id, next_segment_id))
