
ASCII_TABLE = [[0]*8  for i in range(16)]
#https://datatracker.ietf.org/doc/html/rfc20#section-2
'''
8 bit byte whose high order bit is always 0

The standard 7-bit character representation, with b7 the high-order
bit and b1 the low-order bit, is shown below: 

EXAMPLE: The bit representation for the character "K," positioned in
   column 4, row 11, is

   b7 b6 b5 b4 b3 b2 b1
   1  0  0  1  0  1  1

Thus 01001011 becomes "K"

(CC) Communication Control
(FE) Format Effector
(IS) Information Separator
'''

ASCII_TABLE[0][0]   = "NUL" # Control Character: Null  The all-zeros character which may serve to accomplish time fill and media fill.
ASCII_TABLE[0][1]   = "DLE" # Data Link Escape (CC) A communication control character which will change the meaning of a limited number of contiguously following characters.  It is used exclusively to provide supplementary controls in data communication networks.
ASCII_TABLE[0][2]   = "SP"
ASCII_TABLE[0][3]   = "0"
ASCII_TABLE[0][4]   = "@"
ASCII_TABLE[0][5]   = "P"
ASCII_TABLE[0][6]   = "`"
ASCII_TABLE[0][7]   = "p"

ASCII_TABLE[1][0]   = "SOH" # Control Character: Start of Heading (CC)  A communication control character used at the beginning of a sequence of characters which constitute a machine-sensible address or routing information.  Such a sequence is referred to as the "heading."  An STX character has the effect of terminating a heading.
ASCII_TABLE[1][1]   = "DC1" # Device Control 1
ASCII_TABLE[1][2]   = "!"
ASCII_TABLE[1][3]   = "1"
ASCII_TABLE[1][4]   = "A"
ASCII_TABLE[1][5]   = "Q"
ASCII_TABLE[1][6]   = "a"
ASCII_TABLE[1][7]   = "q"

ASCII_TABLE[2][0]   = "STX" # Start of Text (CC) A communication control character which precedes a sequence of characters that is to be treated as an entity and entirely transmitted through to the ultimate destination.  Such a sequence is referred to as "text."  STX may be used to terminate a sequence of characters started by SOH.
ASCII_TABLE[2][1]   = "DC2" # Device Control 2
ASCII_TABLE[2][2]   = "\""
ASCII_TABLE[2][3]   = "2"
ASCII_TABLE[2][4]   = "B"
ASCII_TABLE[2][5]   = "R"
ASCII_TABLE[2][6]   = "b"
ASCII_TABLE[2][7]   = "r"

ASCII_TABLE[3][0]   = "ETX" # End of Text (CC) A communication control character used to terminate a sequence of characters started with STX and transmitted as an entity.
ASCII_TABLE[3][1]   = "DC3" # Device Control 3
ASCII_TABLE[3][2]   = "#"
ASCII_TABLE[3][3]   = "3"
ASCII_TABLE[3][4]   = "C"
ASCII_TABLE[3][5]   = "S"
ASCII_TABLE[3][6]   = "c"
ASCII_TABLE[3][7]   = "s"

ASCII_TABLE[4][0]   = "EOT" # End of Transmission (CC) A communication control character used to indicate the conclusion of a transmission, which may have contained one or more texts and any associated headings.
ASCII_TABLE[4][1]   = "DC4" # Device Control 4 (Stop)
ASCII_TABLE[4][2]   = "$"
ASCII_TABLE[4][3]   = "4"
ASCII_TABLE[4][4]   = "D"
ASCII_TABLE[4][5]   = "T"
ASCII_TABLE[4][6]   = "d"
ASCII_TABLE[4][7]   = "t"

ASCII_TABLE[5][0]   = "ENQ" # Enquiry (CC)  A communication control character used in data communication systems as a request for a response from a remote station.  It may be used as a "Who Are You" (WRU) to obtain identification, or may be used to obtain station status, or both.
ASCII_TABLE[5][1]   = "NAK" # Negative Acknowledge (CC) A communication control character transmitted by a receiver as a negative response to the sender.
ASCII_TABLE[5][2]   = "%"
ASCII_TABLE[5][3]   = "5"
ASCII_TABLE[5][4]   = "E"
ASCII_TABLE[5][5]   = "U"
ASCII_TABLE[5][6]   = "e"
ASCII_TABLE[5][7]   = "u"

ASCII_TABLE[6][0]   = "ACK" # Acknowledge (CC)  A communication control character transmitted by a receiver as an affirmative response to a sender.
ASCII_TABLE[6][1]   = "SYN" # Synchronous Idle (CC) A communication control character used by a synchronous transmission system in the absence of any other character to provide a signal from which synchronism may be achieved or retained.
ASCII_TABLE[6][2]   = "&"
ASCII_TABLE[6][3]   = "6"
ASCII_TABLE[6][4]   = "F"
ASCII_TABLE[6][5]   = "V"
ASCII_TABLE[6][6]   = "f"
ASCII_TABLE[6][7]   = "v"

ASCII_TABLE[7][0]   = "BEL" # Bell (audible or attention signal) A character for use when there is a need to call for human attention.  It may control alarm or attention devices.
ASCII_TABLE[7][1]   = "ETB" # End of Transmission Block (CC)  A communication control character used to indicate the end of a block of data for communication purposes.  ETB is used for blocking data where the block structure is not necessarily related to the processing format.
ASCII_TABLE[7][2]   = "'"
ASCII_TABLE[7][3]   = "7"
ASCII_TABLE[7][4]   = "G"
ASCII_TABLE[7][5]   = "W"
ASCII_TABLE[7][6]   = "g"
ASCII_TABLE[7][7]   = "w"

ASCII_TABLE[8][0]   = "BS" # Backspace (FE) A format effector which controls the movement of the printing position one printing space backward on the same printing line.  (Applicable also to display devices.)
ASCII_TABLE[8][1]   = "CAN" # Cancel A control character used to indicate that the data with which it is sent is in error or is to be disregarded
ASCII_TABLE[8][2]   = "("
ASCII_TABLE[8][3]   = "8"
ASCII_TABLE[8][4]   = "H"
ASCII_TABLE[8][5]   = "X"
ASCII_TABLE[8][6]   = "h"
ASCII_TABLE[8][7]   = "x"

ASCII_TABLE[9][0]   = "HT" # Horizontal Tabulation (punched card skip) (FE) A format effector which controls the movement of the printing position to the next in a series of predetermined positions along the printing line.  (Applicable also to display devices and the skip function on punched cards.)
ASCII_TABLE[9][1]   = "EM" # End of Medium A control character associated with the sent data which may be used to identify the physical end of the medium, or the end of the used, or wanted, portion of information recorded on a medium. (The position of this character does not necessarily correspond to the physical end of the medium.)
ASCII_TABLE[9][2]   = ")"
ASCII_TABLE[9][3]   = "9"
ASCII_TABLE[9][4]   = "I"
ASCII_TABLE[9][5]   = "Y"
ASCII_TABLE[9][6]   = "i"
ASCII_TABLE[9][7]   = "y"

ASCII_TABLE[10][0]  = "LF"  # Line Feed (FE) A format effector which controls the movement of the printing position to the next printing line.  (Applicable also to display devices.) Where appropriate, this character may have the meaning "New Line" (NL), a format effector which controls the movement of the printing point to the first printing position on the next printing line.  Use of this convention requires agreement between sender and recipient of data.
ASCII_TABLE[10][1]  = "SUB" # Substitute  A character that may be substituted for a character which is determined to be invalid or in error.
ASCII_TABLE[10][2]  = "*"
ASCII_TABLE[10][3]  = ":"
ASCII_TABLE[10][4]  = "J"
ASCII_TABLE[10][5]  = "Z"
ASCII_TABLE[10][6]  = "j"
ASCII_TABLE[10][7]  = "z"

ASCII_TABLE[11][0]  = "VT"  # Vertical Tabulation (FE)  A format effector which controls the movement of the printing position to the next in a series of predetermined printing lines.  (Applicable also to display devices.)
ASCII_TABLE[11][1]  = "ESC" # Escape A control character intended to provide code extension (supplementary characters) in general information interchange.  The Escape character itself is a prefix affecting the interpretation of a limited number of contiguously following characters.
ASCII_TABLE[11][2]  = "+"
ASCII_TABLE[11][3]  = ";"
ASCII_TABLE[11][4]  = "K"
ASCII_TABLE[11][5]  = "["
ASCII_TABLE[11][6]  = "k"
ASCII_TABLE[11][7]  = "{"

ASCII_TABLE[12][0]  = "FF" # Form Feed (FE) A format effector which controls the movement of the printing position to the first pre-determined printing line on the next form or page.  (Applicable also to display devices.)
ASCII_TABLE[12][1]  = "FS" # File Separator (IS)
ASCII_TABLE[12][2]  = ","
ASCII_TABLE[12][3]  = "<"
ASCII_TABLE[12][4]  = "L"
ASCII_TABLE[12][5]  = "\\"
ASCII_TABLE[12][6]  = "l"
ASCII_TABLE[12][7]  = "|"

ASCII_TABLE[13][0]  = "CR" # Carriage Return (FE) A format effector which controls the movement of the printing position to the first printing position on the same printing line.  (Applicable also to display devices.)
ASCII_TABLE[13][1]  = "GS" # Group Separator (IS)
ASCII_TABLE[13][2]  = "-"
ASCII_TABLE[13][3]  = "="
ASCII_TABLE[13][4]  = "M"
ASCII_TABLE[13][5]  = "]"
ASCII_TABLE[13][6]  = "m"
ASCII_TABLE[13][7]  = "}"

ASCII_TABLE[14][0]  = "SO" # Shift Out  A control character indicating that the code combinations which follow shall be interpreted as outside of the character set of the standard code table until a Shift In character is reached.
ASCII_TABLE[14][1]  = "RS" # Record Separator (IS)
ASCII_TABLE[14][2]  = "."
ASCII_TABLE[14][3]  = ">"
ASCII_TABLE[14][4]  = "N"
ASCII_TABLE[14][5]  = "^"
ASCII_TABLE[14][6]  = "n"
ASCII_TABLE[14][7]  = "~"

ASCII_TABLE[15][0]  = "SI" # Shift In   A control character indicating that the code combinations which follow shall be interpreted according to the standard code table.
ASCII_TABLE[15][1]  = "US" # Unit Separator (IS)
ASCII_TABLE[15][2]  = "/"
ASCII_TABLE[15][3]  = "?"
ASCII_TABLE[15][4]  = "O"
ASCII_TABLE[15][5]  = "_"
ASCII_TABLE[15][6]  = "o"
ASCII_TABLE[15][7]  = "DEL" # Delete [1] In the strict sense, DEL is not a control character. This character is used primarily to "erase" or "obliterate" erroneous or unwanted characters in perforated tape.



def to_ascii(bdata: bytes) -> str: 
    # map raw bytes to the corresponding character
    return ''.join([ASCII_TABLE[int(bdata[(i*8)+4:(i*8)+8],base=2)][int(bdata[(i*8)+1:(i*8)+4],base=2)] for i in range((len(bdata)+7) // 8)])

def to_ascii_hex(bdata: bytes) -> str:
    return '\\'+'\\'.join([hex(ord(ASCII_TABLE[int(bdata[(i*8)+4:(i*8)+8],base=2)][int(bdata[(i*8)+1:(i*8)+4],base=2)]))[1:] for i in range((len(bdata)+7) // 8)])


if __name__ == "__main__":
    bin_data = b'010010110100101101001011010010110100101101001011'  # Example binary data
    text = to_ascii_hex(bin_data)
    print(text)
