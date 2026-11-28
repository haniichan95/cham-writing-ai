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

## Mẫu Google Docs cho lớp (nên dùng)

File mẫu: [`mau-docs/mau-bai-viet-lop-cham-writing.docx`](mau-docs/mau-bai-viet-lop-cham-writing.docx). Mẫu có phần **ĐỀ BÀI** (Level, số từ, chữ đề) và bảng **STT | Tên học sinh | Xong? | Bài làm**.

**Cách dùng mẫu:**
1. Tải file lên Google Drive → mở bằng Google Tài liệu → **Tệp → Lưu dưới dạng Google Tài liệu**. Bắt buộc bước này: file .docx để nguyên thì trang không lấy bài được.
2. **Điền sẵn tên cả lớp** vào cột "Tên học sinh".
3. Phần ĐỀ BÀI: ghi **Level** (A1 / A2 / B1 / B2) và **Số từ**, rồi **dán ảnh đề** ngay dưới dòng ghi chú (VD ảnh đề bài + ảnh khung "Review / Prepare to write"). Không cần gõ lại chữ đề. Nếu cô gõ chữ đề ở đây thì trang dùng phần chữ và bỏ qua ảnh.
4. Chia sẻ **"Bất kỳ ai có đường liên kết"** với quyền **Người chỉnh sửa** để học sinh viết.
5. Mỗi buổi học: nhân bản tab (mỗi buổi 1 tab), dán link của tab đó vào trang.

**Mẫu giúp gì khi chấm:**
- Học sinh viết xong thì gõ **Xong** (hoặc x, ok, có) vào cột "Xong?". Trang chỉ tích chọn chấm những bài đã Xong; bài chưa Xong hiện **"Đang viết"** và **không gửi cho AI**, nên không tốn lượt cho bài viết dở.
- Mỗi bài có ô tích **"Chấm"**: cô tự tích bài muốn chấm (VD bạn quên gõ Xong) hoặc bỏ tích bài để lại sau. Lần "Lấy bài" sau không đổi lại lựa chọn của cô.
- Trang tự lấy **ảnh đề** (hoặc **chữ đề** nếu cô gõ) vào mục 03, tự chọn **Level** và ghi nhận **Số từ**. Gõ chữ đề thì trang không gửi ảnh kèm từng bài: AI đọc chữ chính xác hơn và chấm rẻ hơn.
- Tên điền sẵn nên trang luôn nhận đúng từng bạn qua các lần "Lấy bài"; bạn chưa viết hiện **"Chưa nộp"**.
- Nhận xét bằng **Bình luận** của Google Docs, không sửa thẳng hay tô màu vào bài, để bài gốc giữ nguyên lỗi cho AI chấm.

Docs cũ không theo mẫu (bảng Tên | Bài) vẫn dùng được như trước.

## Ghi lỗi đã chốt vào Google Docs

Chấm xong, cô chọn những lỗi đồng ý rồi bấm một nút là trang ghi thẳng vào ô bài của học sinh trong Docs:

> I like ~~walking~~ **walk** with my dog. *(chữ sai gạch ngang, chữ sửa màu đỏ)*

**Cách dùng:**
1. Ở **Bảng tổng hợp lỗi**, tích ô **Chốt** ở lỗi muốn gửi (hoặc bấm nút **Chốt** trong khung chi tiết lỗi, hoặc **Chốt tất cả**). Lỗi đã chốt có dấu ✓ trên bài.
2. Muốn ghi kèm lý do thì bật **Kèm lý do**: cuối ô bài có thêm mục "Ghi chú sửa" liệt kê từng lỗi và lý do.
3. Bấm **Ghi … lỗi đã chốt vào Google Docs**. Lần đầu trang mở cửa sổ đăng nhập Google: chọn Gmail có quyền sửa Docs của lớp.

**Cần biết:**
- Google không cho trang web tạo "Đề xuất" (Thay thế / Thêm) như khi cô sửa tay, nên trang ghi theo kiểu gạch ngang + chữ đỏ.
- Trang tìm dòng của học sinh theo **tên**: tên trên trang và trong Docs phải giống nhau.
- Lỗi đã ghi thì không ghi lại lần nữa. Chốt thêm lỗi rồi bấm Ghi thì chỉ lỗi mới được ghi.
- Lần "Lấy bài" sau, trang tự bỏ chữ đỏ và giữ chữ gạch ngang, nên vẫn đọc đúng bài gốc (bài không bị tính là "đã sửa"). Khi học sinh tự sửa lại bài, trang sẽ nhận ra "đã sửa · chờ chấm".
- Chỉ chạy khi mở trang bằng link GitHub Pages (hoặc localhost), không chạy khi mở file bằng bấm đúp.

### Cài đặt 1 lần (khoảng 10 phút, dùng Gmail cá nhân)

1. Vào [Google Cloud Console](https://console.cloud.google.com/), đăng nhập **Gmail cá nhân** → tạo dự án mới, đặt tên VD "Cham Writing".
2. Bật Google Docs API: **APIs & Services → Library** → tìm **Google Docs API** → **Enable**.
3. Màn hình xin quyền: **Google Auth Platform** (hoặc **OAuth consent screen**) → **Get started**:
   - App name: "Chấm Writing", email hỗ trợ: Gmail của mình.
   - Audience: **External**.
   - Ở mục **Audience → Test users**, thêm **Gmail sẽ đăng nhập để ghi vào Docs** (Gmail của cô, và Gmail của người khác nếu họ cũng ghi).
4. Tạo Client ID: **Clients** (hoặc **Credentials → Create credentials → OAuth client ID**) → loại **Web application** → mục **Authorized JavaScript origins** thêm:
   - `https://haniichan95.github.io`
   - `http://localhost:5198` (chỉ khi chạy thử trên máy)

   Bấm **Create** rồi chép **Client ID** (dạng `….apps.googleusercontent.com`).
5. Mở trang Chấm Writing → mục **Ghi vào Google Docs** (cột bên trái) → dán Client ID. Trang tự nhớ trên trình duyệt đó.

Lần đầu đăng nhập, Google báo **"Google chưa xác minh ứng dụng này"**: đây là ứng dụng của chính mình ở chế độ thử, bấm **Tiếp tục**, rồi tích ô cho phép sửa tài liệu Google Docs. Mỗi lần đăng nhập dùng được khoảng 1 giờ; hết giờ trang tự hỏi lại. Client ID không phải mật khẩu, dán lên trang được.

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
3. **Mẫu Google Docs cho lớp** với cột "Xong?" và ô tích "Chấm" để không chấm bài viết dở (xem phần "Mẫu Google Docs cho lớp").
4. **Ghi lỗi đã chốt vào Google Docs**: chọn lỗi đồng ý, bấm một nút là lỗi được ghi vào ô bài của học sinh (xem phần "Ghi lỗi đã chốt vào Google Docs").
