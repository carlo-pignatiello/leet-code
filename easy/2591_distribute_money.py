# You are given an integer money denoting the amount
# of money (in dollars) that you have and another
# integer children denoting the number of children
# that you must distribute the money to.

# You have to distribute the money according
# to the following rules:

#  All money must be distributed.
#  Everyone must receive at least 1 dollar.
#  Nobody receives 4 dollars.

#  Return the maximum number of children who
#  may receive exactly 8 dollars if you distribute
#  the money according to the aforementioned rules.
#  If there is no way to distribute the money, return -1.
def distMoney(money: int, children: int) -> int:
    if money < children:
        return -1
    money -= children
    q, r = divmod(money, 7)
    if q >= children:
        if q == children and r == 0:
            return children
        else:
            return children - 1
    else:
        if r == 3:
            if q < children - 1:
                return q
            else:
                return q - 1
        else:
            return q


print(distMoney(16, 3))


def test_distMoneyFirst():
    assert distMoney(16, 2) == 2


def test_distMoneyTwo():
    assert distMoney(20, 3) == 1
