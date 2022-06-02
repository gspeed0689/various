from secrets import token_urlsafe as TUS

class xuid:
    def __init__(self, TUS_length=64):
        """Initializes a string using secrets.token_urlsafe, this string is
            split into sections to imitate a uuid.

            Upon initialization it creates some of the same standard outputs
                as uuid, including urn (urn:xuid:{xuid}) and fields (tuple of
                values). 

        Args:
            TUS_length (int, optional): An int that is used in the 
                secrets.token_urlsafe (TUS) function to generate the random 
                string of characters. Defaults to 64. 
        """
        if TUS_length <= 0:
            raise ValueError("TUS_length cannot be less than or equal to 0. "
                             "An integer greater than or equal to 30 is "
                             "recommended, default is 64.")
        initial_string = TUS(TUS_length).replace("_", "").replace("-", "")
        while len(initial_string) <= 32:
            initial_string += TUS(TUS_length).replace("_", "").replace("-", "")
        self.used_chars = initial_string[:32]
        segments = (initial_string[0:8],
                    initial_string[8:12],
                    initial_string[12:16],
                    initial_string[16:20],
                    initial_string[20:32])
        self.xuid_join = "-".join(segments)
        self.fields = segments
        self.urn = f"urn:xuid:{self.xuid_join}"
    def __str__(self):
        """Returns a simple 36 character string in the same style as UUID
        """
        return(self.xuid_join)
    def __int__(self):
        """Returns an integer generated from the UTF-8 ordinal values of the 
            initial random string. 
        """
        return(self.shoint())
    def __index__(self):
        """Enables the return of hex and byte values using an integer generated 
            from the UTF-8 ordinal values of the initial random string.  
        """
        return(self.shoint())
    def __repr__(self):
        return(f"XUID('{self.xuid_join}')")
    def long_interizer(self):
        """A step by step approach to creating an integer from the randomly 
            generated string of letters from secrets.token_urlsafe.
            Steps:
            1. Convert string to list of chars
            2. Create list of ordinal values from list of chars
            3. Create list of binary from ordinal values
            4. Create list of strings from binary values
            5. Correct list of binary strings to meet 8-bits per binary string.
            6. Concatenate binary strings into longer binary string suitable
                for conversion using int() built in.
            7. Return int(long binary string)
        """
        charlist = list(self.used_chars)
        ordlist = [ord(x) for x in charlist]
        binlist = [bin(x) for x in ordlist]
        strbin = [str(x)[2:] for x in binlist]
        strbin8 = [f"{'0' * (8-len(x))}{x}" for x in strbin]
        bstr = "0b" + "".join(strbin8)
        return(int(bstr, 2))
    def short_interizer(self):
        """A short version of long_interizer() using list comprehension better.

            See the documentation for long_interizer for the steps to create 
                the integer.  

            Testing shows this is a faster method than long_interizer()
        """
        strlist = [str(bin(ord(x)))[2:] for x in list(self.used_chars)]
        return(int("0b" +  "".join(
                [f"{'0' * (8-len(x))}{x}" for x in strlist]), 2))
    def shoint(self):
        """An even shorter version of long_interizer() using list comprehension.
        
            See the documentation for long_interizer for the steps to create
                the integer.
                
            Testing shows this is a faster method than short_interizer()"""
        return(
            int("0b" +  "".join(
                [f"{'0'*8}{str(bin(ord(x)))[2:]}"[-8:] for x in list(self.used_chars)]
                               ), 2
            ))