from pytest import mark
# Testando se a idade é maior que 18

def initiateClone(age):
    if age == 18:
        return 0
    elif age >= 18:
        return 1
    else:
        return 2



@mark.skip
@mark.maior_que_18
@mark.parametrize(
    "entry",
    [12, 14, 17, 23, 35, 44]
)
def test_initiate_maior_que_18(entry, expect=None): # Maiores de 18 anos
    assert initiateClone(entry) == 1



