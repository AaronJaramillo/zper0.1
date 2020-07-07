from zcash_tools import zcashd
from zcashd_controller import zcashd_control
#from tasks import query_transactions


def pay_for_product():
    z_addr = "zregtestsapling1n56lzsggwwgx4dqyg0qz564utkh724pdmst5tkff96j4l57kufp30sr7qtc383ta53wq7c4zjzr"
    controller = zcashd_control()
    t_addr = "tmBjXgMEqHhkSs33eB9eSysNoe6SnoavAnx"
    controller.send_to_address(str(t_addr), 50)
    controller.generate(2)
    pubkey = "046243F5071FD42A9BFFF0F431D8F99FA808A1E8F77F599AE882A2599482BDCF95710A9553B54E424FF2A19B50B0A99A4073717530D931C7BCF8ED3360713C0F10"
    controller.send_to_z_address("tmWpExNfpDgzHWJPckHKH4wz6AZBtrvwCCH", [{
        "address": z_addr,
        "amount": 1,
        "memo": pubkey
    }])
    controller.generate(2)

pay_for_product()
#query_transactions()


