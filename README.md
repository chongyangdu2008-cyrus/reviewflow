# 拾記（ReviewFlow）支援網站

App Store Connect 需要的「技術支援網址」和「隱私權政策網址」，用 GitHub Pages 發佈。共六種語言：簡體中文、繁體中文、英文、日文、韓文、西班牙文。

- 首頁：`index.html`（選擇語言）
- 各語言：`<語言>/support.html`（技術支援）、`<語言>/privacy.html`（隱私權政策），語言資料夾為 `zh-Hans`、`zh-Hant`、`en`、`ja`、`ko`、`es`

## 修改內容

所有文字都在 `tools/build.py`。改完後執行下面的指令，重新產生全部頁面：

```bash
python3 tools/build.py
```

不要直接改產生出來的 `.html`，下次產生時會被覆蓋。

## 內容依據（2026-10-21 核對工程 `~/Desktop/拾記`）

- 程式沒有任何網路請求，沒有第三方 SDK、廣告、分析或帳號；三個 target 的 PrivacyInfo.xcprivacy 都宣告不收集資料、不追蹤。
- 權限：相機（拍照）、照片（系統選擇器）、通知（本機提醒）。
- 資料只存在本機的 App Group；備份是使用者手動匯出的未加密 JSON；不使用 iCloud 同步。
- 最低系統版本 iOS 17.0；支援 iPhone 與 iPad。

App 的功能或資料處理方式改變時（例如加入同步、分析或網路功能），要同時更新隱私權政策和 App Store Connect 的「App 隱私權」問卷。
