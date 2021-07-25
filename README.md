# whereU
#Mile1 
Read a RAW IP HEADER

we need only the format characters B (1-byte unsigned char), H (2-byte unsigned short), and s (a byte array that requires a byte-width specification; 4s means a 4-byte string)

Of the first byte of header data we receive, we want to assign the ver variable only the high-order nybble, so right shift by 4 and it gives us the original byte