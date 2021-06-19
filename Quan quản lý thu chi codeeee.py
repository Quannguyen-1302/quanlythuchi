def tinhTongThuChi():
  def income():
    luong = float(input("Nhập số tiền lương của bạn: "))
    tienTietKiem = float(input("Nhập số tiền tiết kiệm của bạn: "))
    lai = float(input("Nhập số tiền lãi của bạn: "))
    return luong + tienTietKiem + lai


  def outcome():
    tienSinhHoat = float(input("Nhập số tiền sinh hoat của bạn: "))
    tienAn = float(input("Nhập số tiền an của bạn: "))
    tienDiChoi = float(input("Nhập số tiền di choi của bạn: "))
    return tienSinhHoat + tienAn + tienDiChoi

  def tongThuChi():
    return income() - outcome()
  print(tongThuChi())
tinhTongThuChi()