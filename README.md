# LuanVanKHMT


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
How to use the Tool:

*** Cài python3x hoặc python2x để sử dụng tool:***

***Key events: ***

***nhấn nút Q:*** thoát khỏi ứng dụng

***Nhấn nút R:***  trở về ảnh trước

***Nhấn phím space: *** đi tới ảnh kế 

cú pháp sử dụng với terminal: python3 posneg_tool.py  index_of_image  data_folder_path positive_folder_path  negative_folder_path expect_prefix_name_of_file

***python3*** : phiên bản python sử dụng, có thể là python 2.x (python2)

***posneg_tool.py*** : file python xử lý cắt ảnh

***index_of_image*** : ảnh mà bạn muốn cắt trong folder

***data_folder_path*** : đường dẫn của folder chứa ảnh raw muốn cắt

***positive_folder_path*** : đường dẫn tới folder cần chưa các ảnh positive (ảnh chỉ chứa đối tượng bạn đã cắt)

***negative_folder_path*** :  đường dẫn tới folder cần chưa các ảnh negative (ảnh chỉ chứa background đã loại bỏ đi đối tượng bị cắt)

***expect_prefix_name_of_file*** : tiền tốt tên file ảnh sau khi save, phải trên 5 ký tự ví dụ: ABCDEF_0001_IMG.png


for example:

(lần đầu tiên chạy thì ảnh thứ nhất thì index là 1) python3 posneg_tool.py 1 ../DataPath ../PosPath ../NegPath ABCDEF


do tool này ko hỗ trợ cache workspace nên khi tắt máy đột ngột sẽ ko có lưu lại ảnh vừa cắt cho nên bạn phải xem ảnh đã cắt tới đâu và đánh index mới đê cắt tiếp

python3 posneg_tool.py (index of cut image) ../DataPath ../PosPath ../NegPath ABCDEF



----------------------------------------------------------------------------------------------------------------------------------------------------------
