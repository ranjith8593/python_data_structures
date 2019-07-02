def isBalanced(ip):
    str_list = list(ip)
    opp_stack = []
    in_stack = []
    opp_list = [")", "}", "]"]
    opp_map = {
        "{": "}",
        "(": ")",
        "[": "]",
    }
    for a in str_list:
        if a in opp_list:
            if len(opp_stack) is not 0 and opp_stack[0] is a:
                in_stack.pop(0)
                opp_stack.pop(0)
        else:
            in_stack.insert(0,a)
            opp = opp_map.get(a)
            opp_stack.insert(0, opp)
    if len(in_stack) == 0 and len(opp_stack) == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    print(isBalanced("[()]{}{[()()]()}"))
