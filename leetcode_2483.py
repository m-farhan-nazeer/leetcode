class Solution(object):
    def bestClosingTime(self, customers):
        """
        :type customers: str
        :rtype: int
        """
        total_yes = 0 
        total_no = 0
        for items in customers:
            if items == "Y":
                total_yes += 1
            else :
                total_no += 1

        pre_yes = 0
        pre_no = 0 
        mini = float('inf')
        best =0 
        for i in range(len(customers)):
            pen = (total_yes - pre_yes )+ pre_no 
            if pen < mini :
                mini = pen
                best = i
            if customers[i] == "Y":
                pre_yes += 1
            else :
                pre_no += 1
        pen =  total_no 
        if pen < mini :
            mini = pen
            best = len(customers)
        return best

        