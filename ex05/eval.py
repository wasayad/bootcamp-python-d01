class Evaluator():
    def zip_evaluate(coefs, words):
        if len(words) != len(coefs):
            return(print("Error length of coeff and word isn't the same."))
        test = zip(words, coefs)
        res = 0
        test = set(test)
        to = len(tuple(test))
        for i in range(0, to):
            res = res + len(tuple(test)[i][0]) * float(tuple(test)[i][1])
        return(res)

    def enumerate_evaluate(coefs, words):
        res = 0
        char = ""
        for i, c in enumerate(coefs):
            res = res + c * len(words[i])
        return(res)
