class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        record =[]
        for i in operations:
        
            if i.isnumeric():
                record.append(int(i))
            elif i == "C":
                record.pop()
            elif i == "D":
                record.append(2 *record[-1]) 
            elif i == "+":
                record.append( record[-2] + record[-1])
        return sum(record)
            