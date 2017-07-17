import logging
import sys
logging.basicConfig(filename="loggingfile.log",format='%(asctime)s %(levelname)s:%(message)s',level=logging.INFO)
logging.info('started the process')
text=raw_input("Enter additive sequence:")
line=text.split(',')
for i in line:
    try:
        int(i)
    except ValueError:
        logging.error('some strings (for example %s) are entered in the input.PLEASE CHECK',i)
        sys.exit(0)
line="".join(line)
class Solution(object):
# DFS: iterative implement.
    def is_additive_number(self, num):
        length = len(num)
        if length<3:
            logging.error("Entered sequence %s is too small",num)
            sys.exit(0)
        for i in range(1, int(length/2+1)):
            for j in range(1, int((length-i)/2 + 1)):
                first, second, others = num[:i], num[i:i+j], num[i+j:]
                if self.isValid(first, second, others):
                    return True
        return False

    def isValid(self, first, second, others):
        if ((len(first) > 1 and first[0] == "0") or
                (len(second) > 1 and second[0] == "0")):
            return False
        sum_str = str(int(first) + int(second))
        
        if sum_str == others:
            return True
        elif others.startswith(sum_str):
            return self.isValid(second, sum_str, others[len(sum_str):])
        else:
            return False

if __name__ == "__main__":
    print(Solution().is_additive_number(line))
    logging.info('process finished')




