class Solution:
    def calPoints(self, op: List[str]) -> int:
        record = []
        for i in range(len(op)):

            if op[i] in {"+", "C", "D"}:
                if op[i] == "+" and len(record) >= 2: 
                    record.append(record[-1]+record[-2])
                
                elif len(record) != 0:
                    if op[i] == "C": 
                        record.pop()
                    elif op[i] == "D": 
                        record.append(2*(record[-1]))
                    else:
                        break
            else:
                num = int(op[i])
                record.append(num)

        return sum(record)