from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        i = 0
        result = []
        while i < len(words):
            c = 0
            s = i
            while c < maxWidth:
                c += len(words[i])
                if i + 1 < len(words):
                    if len(words[i+1]) + c < maxWidth:
                        c += 1  # you can add the space and go to the next word
                    else:
                        continue  # get out of the inner while
                else:
                    continue
                i += 1
            i += 1

            num_words = i - s
            min_spaces = num_words - 1
            max_spaces = maxWidth - (sum([len(w) for w in words[s:i]]))
            q = max_spaces // (num_words - 1) if (num_words - 1) > 0 else 1
            r = max_spaces % (num_words - 1) if (num_words - 1) > 0 else 0

            total = q * num_words + r

            final_string = ""
            if num_words == 1:
                final_string = words[i - 1] + "".join([" " for _ in range(maxWidth - len(words[i-1]))])
            else:
                if i != len(words):
                    for k in range(num_words):
                        final_string += words[s + k]
                        one = 1 if r > 0 else 0
                        if k < min_spaces:
                            final_string += "".join([" " for _ in range(q + one)])
                            r -= 1
                else:
                    final_string = " ".join(words[s:i])
                    to_add = maxWidth - len(final_string)
                    final_string += "".join([" " for _ in range(to_add)])

            result.append(final_string)

        return result

s = Solution()
l = ("This is a text that should be justified properly. Hopefully it will work. Some short words here and there just "
     "to make it more difficult. A A A A A A AAAAA. Aaaaaaaaaaaaaaaa a").split(" ")

l = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
r = s.fullJustify(l, 20)
for el in r:
    print(len(el))
for el in r:
    print(el)

# works. had to try many times. not the fastest. algo looks bad. it is an hard tho so im happy
