import io


class SmartBuffer(io.StringIO):
    def peek(self, n: int):
        curr_pos = self.tell()
        data = self.read(n)
        self.seek(curr_pos)
        return data

    def chomp_newline(self):
        end = self.seek(0, io.SEEK_END)
        if end > 0:
            last_char_pos = end - 1
            self.seek(last_char_pos)
            if self.peek(1) == "\n":
                self.truncate(last_char_pos)
                self.seek(last_char_pos)
                self.write(" ")

    def strip(self):
        end_pos = self.seek(0, io.SEEK_END)
        while end_pos > 0:
            self.seek(end_pos)
            if self.peek(1) not in (" ", "", "\n"):
                self.truncate(end_pos + 1)
                self.seek(end_pos + 1)
                return
            end_pos -= 1

    def __str__(self):
        return self.getvalue()

    def __repr__(self):
        return repr(str(self))
