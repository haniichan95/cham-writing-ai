"""Dựng file Docs mẫu cho trang Chấm Writing: phần ĐỀ BÀI (Level, số từ, chữ đề) + bảng STT | Tên học sinh | Xong? | Bài làm.
Không dùng bảng nào khác ngoài bảng bài làm (trang web lấy bảng đầu tiên làm danh sách bài)."""
import sys
from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ROW_HEIGHT_RULE
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

OUT = sys.argv[1]
ROWS = 20
TEAL = RGBColor(0x0D, 0x7A, 0x68)
GRAY = RGBColor(0x64, 0x74, 0x8B)

doc = Document()
sec = doc.sections[0]
sec.page_width, sec.page_height = Cm(21), Cm(29.7)
for side in ("left_margin", "right_margin"):
    setattr(sec, side, Cm(1.8))
sec.top_margin = sec.bottom_margin = Cm(1.6)

st = doc.styles["Normal"]
st.font.name = "Arial"
st.font.size = Pt(11)
st.element.rPr.rFonts.set(qn("w:eastAsia"), "Arial")
st.paragraph_format.space_after = Pt(3)


def shade(el, fill):
    """Tô nền cho đoạn văn hoặc ô bảng."""
    pr = el.get_or_add_pPr() if hasattr(el, "get_or_add_pPr") else el.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill)
    pr.append(shd)


def para(text="", bold=False, size=None, color=None, italic=False, fill=None, after=None):
    p = doc.add_paragraph()
    if text:
        r = p.add_run(text)
        r.bold, r.italic = bold, italic
        if size: r.font.size = Pt(size)
        if color: r.font.color.rgb = color
    if fill: shade(p._p, fill)
    if after is not None: p.paragraph_format.space_after = Pt(after)
    return p


def rich(parts, fill=None, after=None):
    """Đoạn có nhiều phần chữ: [(text, bold)]."""
    p = doc.add_paragraph()
    for text, bold in parts:
        r = p.add_run(text)
        r.bold = bold
    if fill: shade(p._p, fill)
    if after is not None: p.paragraph_format.space_after = Pt(after)
    return p


# Tiêu đề
para("Lớp: ……………   ·   Buổi: ……………   ·   Writing", bold=True, size=16, color=TEAL, after=6)

# Ghi chú cho cô (dòng bắt đầu "(Cô" được trang web bỏ qua)
para("(Cô: điền sẵn tên cả lớp vào cột “Tên học sinh”, dán chữ đề vào phần ĐỀ BÀI, chia sẻ “Bất kỳ ai có "
     "đường liên kết” với quyền Người chỉnh sửa cho học sinh viết. Mỗi buổi học: nhân bản tab này. Nhận xét bằng "
     "Bình luận, không sửa thẳng hay tô màu vào bài.)", italic=True, size=9, color=GRAY, after=8)

# Hướng dẫn học sinh (đoạn tô nền, không dùng bảng)
FILL = "E7F4F1"
para("HƯỚNG DẪN CHO HỌC SINH", bold=True, color=TEAL, fill=FILL, after=0)
rich([("1. Tìm dòng có ", False), ("tên mình", True), (", viết bài vào ô ", False), ("Bài làm", True), (".", False)], fill=FILL, after=0)
rich([("2. ", False), ("Không sửa tên", True), (", không xoá hay thêm dòng.", False)], fill=FILL, after=0)
rich([("3. Viết xong thì gõ ", False), ("Xong", True), (" vào ô ", False), ("Xong?", True), (" của mình. Chưa xong thì để trống.", False)], fill=FILL, after=0)
rich([("4. Gõ Xong rồi vẫn sửa bài được, cô sẽ chấm lại phần đã sửa.", False)], fill=FILL, after=10)

# Đề bài
para("ĐỀ BÀI", bold=True, size=13, color=TEAL, after=2)
rich([("Level: ", True), ("___   (ghi 1 trong: A1 / A2 / B1 / B2)", False)], after=0)
rich([("Số từ: ", True), ("___", False)], after=2)
para("(Cô dán ảnh đề vào ngay dưới dòng này: ảnh đề bài và ảnh khung Review / Prepare to write. Không cần gõ lại "
     "chữ đề. Nếu cô gõ chữ đề ở đây thì trang chấm dùng phần chữ và bỏ qua ảnh.)", italic=True, size=10, color=GRAY, after=10)

# Bài làm
para("BÀI LÀM", bold=True, size=13, color=TEAL, after=4)
widths = [Cm(1.4), Cm(4.0), Cm(1.8), Cm(10.2)]
table = doc.add_table(rows=1 + ROWS, cols=4)
table.style = "Table Grid"
table.alignment = WD_TABLE_ALIGNMENT.CENTER
table.autofit = False
for i, h in enumerate(["STT", "Tên học sinh", "Xong?", "Bài làm"]):
    cell = table.rows[0].cells[i]
    cell.text = ""
    r = cell.paragraphs[0].add_run(h)
    r.bold = True
    r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    cell.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    shade(cell._tc, "0D7A68")
# Dòng tiêu đề lặp lại ở đầu mỗi trang
trPr = table.rows[0]._tr.get_or_add_trPr()
hdr = OxmlElement("w:tblHeader"); hdr.set(qn("w:val"), "true"); trPr.append(hdr)
for n in range(1, ROWS + 1):
    row = table.rows[n]
    row.height = Cm(1.6)
    row.height_rule = WD_ROW_HEIGHT_RULE.AT_LEAST
    row.cells[0].text = str(n)
    row.cells[0].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    row.cells[2].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
for row in table.rows:
    for i, w in enumerate(widths):
        row.cells[i].width = w
# Độ rộng cột ở lưới bảng + bố cục cố định: Google Docs/Word đọc phần này khi mở file
grid = table._tbl.tblGrid
for gc, w in zip(grid.findall(qn("w:gridCol")), widths):
    gc.set(qn("w:w"), str(int(w.twips)))
tblPr = table._tbl.tblPr
tblW = tblPr.find(qn("w:tblW"))
if tblW is None:
    tblW = OxmlElement("w:tblW"); tblPr.append(tblW)
tblW.set(qn("w:type"), "dxa"); tblW.set(qn("w:w"), str(int(sum(w.twips for w in widths))))
layout = OxmlElement("w:tblLayout"); layout.set(qn("w:type"), "fixed"); tblPr.append(layout)

para("(Cô: cần thêm dòng thì bấm chuột phải vào dòng cuối → Chèn hàng bên dưới.)", italic=True, size=9, color=GRAY)
doc.save(OUT)
print("saved", OUT)
