global map_str, map_i

map_str = '0000000000\n0000000000\n0000000000\n0000000000\n0000000000\n0000000000\n0000000000\n0000000000\n0000000000\n0000000000\n'
map_i = 0

class Request():
    def __init__(self, raw_request):
        self.raw = raw_request.decode()
        self.method = ""
        self.url = ""
        l = self.raw.split(' ')

        self.method = l[0]
        self.url = l[1]
        self.url_list = self.url.split('/')
        try:
            while 1: self.url_list.remove('')
        except:
            pass
    
    def __str__(self):
        return f'Request: {self.method} {self.url}'

    def treat(self):
        global map_str, map_i
        if self.url == "/":
            return Response(200, file='game.html',
                            other={'Allow-Control-Origin-Access' : '*'})
        
        if len(self.url_list) == 0 :
            print(self.url)
            return Response(200, "Empty url")
        if self.url_list[0] == "game_state":
            map_str = map_str[:map_i] + '0' + map_str[map_i + 1:]
            map_i += 1
            if (map_str[map_i] == '\n'):
                map_i += 1
            if (len(map_str) <= map_i ):
                map_i = 0
            map_str = map_str[:map_i] + '#' + map_str[map_i + 1:]
            return Response(200, map_str,
                            {'Allow-Control-Origin-Access' : '*'})
        elif self.url == '/render.js':
            return Response(200, file='render.js',
                            other={'Allow-Control-Origin-Access' : '*'})
        else:
            print(self.url, self.url_list)
            return Response(200, "LOL")

class Response():
    def __init__(self, code, content=None, other = None, file=None):
        self.code = code
        self.content = content
        self.file = file
        if self.file:
            self.content = ""
            f = open(file, 'r')
            self.content += f.read()
            f.close()
        if (other):
            self.other = other
        else:
            self.other = {}
        

    def build(self):
        other_res = ""
        for k, v in self.other.items():
            other_res += '\r\n'
            other_res += f'{k}:{v}'
        return bytes(f'HTTP/1.1 {self.code} OK{other_res}\r\n\r\n{self.content}', 'utf-8')