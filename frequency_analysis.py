# Decrypting a Substitution Cipher by Frequency Analysis and Guesses
import operator
import sys

cipher_txt = """lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi
bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx
ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr
yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk
lmird jk xjubt trmui jx ibndt
  wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi
iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m
vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd
wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr
jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii
ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh
mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb
bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd
wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr
riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb"""


class attack:
    def __init__(self):
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.freq = {}
        self.key = {}
        self.freq_eng = {'a': 0.0817, 'b': 0.0150, 'c': 0.0278, 'd': 0.0425, 'e': 0.1270, 'f': 0.0223,
                         'g': 0.0202, 'h': 0.0609, 'i': 0.0697, 'j': 0.0015, 'k': 0.0077, 'l': 0.0403,
                         'm': 0.0241, 'n': 0.0675, 'o': 0.0751, 'p': 0.0193, 'q': 0.0010, 'r': 0.0599,
                         's': 0.0633, 't': 0.0906, 'u': 0.0276, 'v': 0.0098, 'w': 0.0236, 'x': 0.0015,
                         'y': 0.0197, 'z': 0.0007}
        self.mappings = {}
        self.plain_chars_left = 'abcdefghijklmnopqrstuvwxyz'
        self.cipher_char_left = 'abcdefghijklmnopqrstuvwxyz'

    def freq_cipher(self, cipher):
        let_cnt = len(cipher) - len(cipher.split()) - 1  # no of letters in cipher
        for x in self.alphabet:
            self.freq[x] = cipher_txt.count(x)
        for g in self.freq:
            self.freq[g] = round(self.freq[g] / let_cnt, 4)
        return self.freq

    def print_freq(self):
        n_c = 0
        for i in self.freq:
            print(i, ':', self.freq[i], ' ', end='')
            if n_c % 2 == 1:
                print()
            n_c += 1

    def calc_matches(self):
        for x in self.freq:
            l = {}
            for y in self.freq_eng:
                dev = abs(self.freq[x] - self.freq_eng[y])
                l[y] = round(dev, 4)
            self.mappings[x] = sorted(l.items(), key=operator.itemgetter(1))
            '''ref=list(l.keys())
            l_d= list(l.values())
            k= l_d.index(min(l_d))
            self.mappings[x]=ref[k]
        return self.mappings'''

    def guess_key(self):
        for x in self.cipher_char_left:
            for y, d in self.mappings[x]:
                if y in self.plain_chars_left:
                    self.key[x] = y
                    self.plain_chars_left = self.plain_chars_left.replace(y, '')
                    break

    def get_key(self):
        return self.key

    def set_key_mapping(self, x, y) :
        if x not in self.cipher_char_left or y not in self.plain_chars_left:
            print("ERROR: key mapping error", x, y)
            sys.exit(-1)
        self.key[x] = y
        self.plain_chars_left = self.plain_chars_left.replace(y, '')
        self.cipher_char_left = self.cipher_char_left.replace(x, '')


def decrypt(key, cipher):
    msg = ''
    for j in cipher:
        if j in key:
            msg += key[j]
        else:
            msg += j
    return msg

a = attack()
a.freq_cipher(cipher_txt)
a.print_freq()
a.calc_matches()

print(a.mappings)
a.set_key_mapping('a', 'x')
a.set_key_mapping('d', 'd')
a.set_key_mapping('e', 'v')
a.set_key_mapping('m', 'a')
a.set_key_mapping('p', 'h')
a.set_key_mapping('q', 'k')
a.set_key_mapping('r', 'e')
a.set_key_mapping('s', 'p')
a.set_key_mapping('f','q')
a.set_key_mapping('g','z')
a.set_key_mapping('t', 'y')
a.set_key_mapping('u', 'r')
a.set_key_mapping('v', 'c')
a.set_key_mapping('w', 'i')
a.set_key_mapping('x', 'f')
a.set_key_mapping('y', 'm')
a.set_key_mapping('o','g')
a.set_key_mapping('c','w')


a.guess_key()
key=a.get_key()

print()
print(key)
m=decrypt(key,cipher_txt)
m_l= m.splitlines()
c_l=cipher_txt.splitlines()
for x in range(len(m_l)):
    print('P:',m_l[x])
    print('C:',c_l[x])
print(m)