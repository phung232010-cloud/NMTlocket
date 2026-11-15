# Hướng dẫn đưa Web Locket Gold lên GitHub và Deploy

Thư mục này (`web-locketgold`) đã được gom đầy đủ toàn bộ mã nguồn, giao diện, cấu hình và loại bỏ các file rác / file nặng thừa (`cloudflared.exe`, database tạm, cache).

---

## 1. Các file có trong thư mục:
- `app.py`: Backend Flask chính (đã sửa lỗi giải mã dữ liệu RevenueCat).
- `auth.py`, `database.py`, `wallet.py`, `payos.py`, `security.py`, `config.py`: Các module quản lý tài khoản, ví, nạp tiền, bảo mật.
- `requirements.txt`: Danh sách thư viện Python cần thiết (`flask`, `aiohttp`, `psycopg2-binary`, ...).
- `vercel.json`, `.vercelignore`, `.python-version`: Cấu hình deploy tự động lên Vercel.
- `templates/`: Toàn bộ giao diện HTML (trang chủ, đăng nhập, nạp tiền, admin, hỗ trợ...).
- `static/`: File tĩnh CSS, JS, logo, icon.
- `locket-gold-new/`: Toàn bộ file script và file `.conf` Shadowrocket chuẩn.

---

## 2. Cách tải thư mục này lên GitHub

### Cách 1: Dùng trình duyệt (Web GitHub) - Đơn giản nhất
1. Truy cập [github.com](https://github.com) và đăng nhập.
2. Bấm vào dấu **+** ở góc trên bên phải → Chọn **New repository**.
3. Đặt tên repository (ví dụ: `web-locketgold`) → Để chế độ **Public** hoặc **Private** → Bấm **Create repository**.
4. Ở trang vừa tạo, bấm vào dòng **"uploading an existing file"**.
5. Kéo thả toàn bộ các file và thư mục trong thư mục `web-locketgold` này vào trình duyệt.
6. Bấm **Commit changes** để lưu.

### Cách 2: Dùng Git Command Line (nếu máy có cài Git)
Mở PowerShell tại thư mục `web-locketgold`:
```bash
git init
git add .
git commit -m "Initial commit web locketgold"
git branch -M main
git remote add origin https://github.com/TÊN_GITHUB_CỦA_BẠN/web-locketgold.git
git push -u origin main
```

---

## 3. Cách kết nối Vercel để tạo trang Web (Deploy)
1. Truy cập [vercel.com](https://vercel.com) và đăng nhập bằng tài khoản GitHub.
2. Bấm **Add New...** → Chọn **Project**.
3. Tìm và chọn repository `web-locketgold` bạn vừa tạo trên GitHub → Bấm **Import**.
4. Vào [neon.tech](https://neon.tech) tạo 1 database PostgreSQL miễn phí (hoặc tạo Vercel Postgres trong tab Storage).
5. Trong mục **Environment Variables** trên Vercel, thêm 2 biến bắt buộc:
   - `DATABASE_URL`: Đường dẫn kết nối PostgreSQL từ Neon (dạng `postgresql://user:pass@host/dbname?sslmode=require`).
   - `SECRET_KEY`: Một chuỗi ký tự ngẫu nhiên bất kỳ để bảo mật phiên đăng nhập.
6. Bấm nút **Deploy**.
7. Chờ 1-2 phút, Vercel sẽ cấp cho bạn một tên miền miễn phí (dạng `https://web-locketgold-xxx.vercel.app`) hoạt động 24/7!
