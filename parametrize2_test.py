from pytest import mark
# Testando se a idade é maior que 18

def initiateClone(age):
    if age == 18:
        return 0
    elif age >= 18:
        return 1
    else:
        return 2


@mark.parametrize(
    "entry, expect", [(12,2), (14,2), (17,2), (23,1), (35,1), (44,1)]
)
def test_initiate_expect_entry(entry, expect): # entradas esperadas
    assert initiateClone(entry) == expect


