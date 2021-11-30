class XeMay():
    phankhoi: int
    tenxe: str
    xuatxu: str

    def __init__(self,CC,Broadname,From):
        self.phankhoi = CC
        self.tenxe = Broadname
        self.xuatxu = From

    def outputXeMay(self) -> str:
        result ='Phankhoi: '+ str(self.phankhoi) + '\nTenxe: '+ self.tenxe + '\nXuatxu: ' + self.xuatxu
        return result