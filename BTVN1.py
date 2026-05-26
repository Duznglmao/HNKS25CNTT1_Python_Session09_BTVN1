"""
Lệnh insert(0, "GE000") chèn đơn hàng mới vào đầu, đẩy toàn bộ phần tử cũ lùi về sau 1 vị trí 
Danh sách thành: ["GE000", "GE001", "GE002", "GE003-CANCEL", "GE004"]

Lệnh delivery_orders[1] = GE002-UPDATED sửa sai đơn hàng vì lúc này vị trí index 1 thuộc về GE001
Sau khi chèn GE000 thì GE002 dã dịch chuyển sang index 2.

Lệnh remove(3) gây lỗi vì nó xóa theo giá trị, không phải vị trí index. 
Trong list không có giá trị số 3 nên báo lỗi

Muốn xóa GE003-CANCEL thì ta nên dùng remove() vì nó sẽ xóa theo giá trị

Phương thức pop() xóa phần tử cuối cùng và trả về giá trị của phần tử đó.

In biến transferred_order báo lỗi là do biến này chưa được khởi tạo.

Muốn lưu lại phần tử từ .pop() thì ta có thể lưu giá trị phần tử bị pop() xóa bằng cách gán kết quả trả về vào biến khác
"""
delivery_orders = ["GE001", "GE002", "GE003-CANCEL"]
delivery_orders.append("GE004")
delivery_orders.insert(0, "GE000")
delivery_orders[2] = "GE002-UPDATED"
delivery_orders.remove("GE003-CANCEL")
transferred_order = delivery_orders.pop()

print("Danh sách đơn hàng còn lại:", delivery_orders)
print("Đơn hàng được bàn giao:", transferred_order)