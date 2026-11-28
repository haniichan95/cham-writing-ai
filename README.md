# Chấm Writing

Trang web giúp giáo viên chấm bài Writing tiếng Anh theo giáo trình Cambridge **Prepare** bằng AI (Gemini). Trang không chấm điểm: chỉ đánh dấu lỗi, giải thích vì sao sai, đối chiếu với đề, nhận xét chung và đưa bản viết lại.

**Mở trang:** https://haniichan95.github.io/cham-writing-ai/

## Cách dùng

1. Chọn **Level** (Beginners / Elementary / Pre-intermediate / Intermediate).
2. **Đề bài (mục 03):** dán ảnh đề hoặc chữ đề. Lấy bài từ Google Docs thì ảnh đề ở đầu Docs tự vào đây.
3. **Bài làm (mục 05):** chọn một trong các cách:
   - Dán **link Google Docs** rồi bấm **"Lấy bài"**. Mỗi dòng trong bảng Tên | Bài thành 1 bài.
   - Dán hoặc kéo thả **ảnh** bài làm.
   - Bấm **"+ Thêm bài viết học sinh"** để gõ hoặc dán chữ.
4. Dán **Gemini API Key** vào mục "Kết nối AI" (lấy miễn phí tại [Google AI Studio](https://aistudio.google.com/apikey)). Key chỉ lưu trên trình duyệt của bạn.
5. Bấm **"Chấm bài"**. Mỗi học sinh hiện thành một tab riêng.

### Chấm theo đợt (học sinh nộp lúc sớm lúc muộn)

- Bạn nào nộp sau thì bấm **"Lấy bài"** lại. Trang báo kiểu *"2 bài mới · 1 bài đã sửa · 1 bạn chưa nộp"*.
- Bấm **"Chấm bài"** thì chỉ những bài mới hoặc vừa sửa được chấm, bài đã chấm giữ nguyên.
- **Bảng "Tình trạng lớp"** ở mục 05 cho biết mỗi bạn đang ở trạng thái nào: Chưa nộp / Chờ chấm / Đang chấm / Đã chấm. Bấm vào tên là mở bài của bạn đó.
- **Trang nhớ lớp đang chấm.** Lỡ đóng tab thì mở lại trang, bấm **"Lấy bài"** là các bài đã chấm hiện lại, không tốn lượt AI chấm lại. Trang chỉ nhớ trên trình duyệt đang dùng.
- Qua lớp mới thì bấm **"Reset lớp mới"**.

## Để lấy bài từ link Google Docs

1. Mở trang bằng link **https://haniichan95.github.io/cham-writing-ai/**. Nếu mở file `index.html` bằng cách bấm đúp, Google sẽ không cho lấy bài từ Docs.
2. Docs phải chia sẻ **"Bất kỳ ai có đường liên kết"** (quyền Người xem).
3. Bài nằm trong bảng 2 cột **Tên | Bài**. Ảnh đề đặt ở đầu Docs, trước bảng.
4. Bình luận của giáo viên ([a], [b]…) và chữ màu giáo viên chèn vào không bị lấy vào bài.

**Bật trang web (chỉ cần làm 1 lần):** vào repo → **Settings** → **Pages** → ở mục Branch chọn **main** → **Save**. Chờ khoảng 1 phút là link trên dùng được.

## Thay đổi gần đây (11/2026)

**Lỗi đã sửa**
1. **Chấm nhiều bài hay bị treo hoặc báo lỗi.** Trước đây cả lớp gửi cho AI cùng một lúc nên dễ quá giờ. Giờ AI chấm từng bạn riêng, 3 bạn cùng lúc. Bạn nào chấm xong thì hiện ngay; bạn nào lỗi thì chấm lại riêng bạn đó.
2. **Bài viết bị dính thành một đoạn.** Giờ các dòng như "Hi Rob," hay "Keep in touch," xuống dòng đúng như học sinh viết.
3. **Sửa bài rồi chấm lại thì ra thêm một tab trùng tên.** Giờ kết quả mới thay vào đúng tab cũ.

**Chức năng mới**
1. Lấy bài từ **link Google Docs**: không cần chụp ảnh, và AI giữ đúng lỗi của học sinh (đọc ảnh thì AI hay tự sửa mất lỗi).
2. **Chấm theo đợt**, **bảng Tình trạng lớp** và **nhớ lớp đang chấm** (xem phần "Chấm theo đợt" ở trên).
