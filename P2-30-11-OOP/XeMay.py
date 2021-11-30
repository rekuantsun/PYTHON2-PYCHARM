class XeMay():
    phankhoi: int
    tenxe: str
    xuatxu: str

    def __init__(self,CC,Brandname,From):
        self.phankhoi = CC
        self.tenxe = Brandname
        self.xuatxu = From

    def outputXeMay(self) -> str:
        result ='Phankhoi: '+ str(self.phankhoi) + '\nTenxe: '+ self.tenxe + '\nXuatxu: ' + self.xuatxu
        return result