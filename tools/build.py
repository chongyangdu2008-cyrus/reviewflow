#!/usr/bin/env python3
"""Generates the support and privacy pages of 拾記 (ReviewFlow) in six languages.

Edit the texts below, then run:  python3 tools/build.py
It rewrites index.html, style.css and <language>/support.html, <language>/privacy.html.
"""
from pathlib import Path
import html

ROOT = Path(__file__).resolve().parent.parent
EMAIL = "chongyangdu2008@gmail.com"
YEAR = "2026"

# Order of the language menu. Each entry: code (folder), html lang, native name.
LANGUAGES = [
    ("zh-Hans", "zh-Hans", "简体中文"),
    ("zh-Hant", "zh-Hant", "繁體中文"),
    ("en", "en", "English"),
    ("ja", "ja", "日本語"),
    ("ko", "ko", "한국어"),
    ("es", "es", "Español"),
]

# Placeholders inside the texts: {mail} = e-mail link, {privacy} / {support} = link to the other page.
TEXT = {
"zh-Hans": dict(
    app="拾记", support="技术支持", privacy="隐私政策", language="语言",
    updated="最后更新：2026 年 10 月 21 日", effective="生效日期：2026 年 10 月 21 日",
    support_lead="拾记是一款在本机运行的学习复习 App：把文字和图片记下来，按遗忘曲线安排下一次复习，到期提醒你，复习时按记忆情况反馈。无需注册账号，没有广告。",
    support_sections=[
        ("联系我们", """<p>如有问题、建议或发现错误，请发送邮件至 {mail}，我们会尽快回复。</p>
<p>为了更快定位问题，请在邮件中附上：</p>
<ul><li>设备型号，以及 iOS 或 iPadOS 版本；</li>
<li>拾记的版本号（可在系统「设置」→「通用」→「iPhone 存储空间」→「拾记」中查看）；</li>
<li>问题描述和重现步骤，必要时附截图（请勿发送你不想分享的内容）。</li></ul>"""),
        ("系统要求", """<p>需要 iOS 17.0 或 iPadOS 17.0 及以上版本，支持 iPhone 和 iPad。</p>
<p>App 支持简体中文、繁体中文、英文、日文、韩文和西班牙文，可在 App 的「设置」→「语言」中切换。</p>"""),
    ],
    faq_title="常见问题",
    faq=[
        ("需要注册账号或联网吗？", "不需要。拾记没有账号、广告和订阅，所有功能都在你的设备上完成。"),
        ("数据保存在哪里？会自动同步吗？", "数据只保存在你的设备上，不会上传到任何服务器，也不会通过 iCloud 自动同步。如需换机或留存数据，请在「设置」中点「导出备份」，把完整备份（包含图片、复习记录和设置）保存到「文件」或 iCloud Drive，再在另一台设备上点「导入备份」恢复。"),
        ("恢复备份会发生什么？", "恢复会用备份内容取代当前的全部数据和设置。恢复前会先显示备份内容让你确认，并自动保存一份恢复前的安全备份。备份文件没有加密，请妥善保管。"),
        ("删除 App 会丢失数据吗？", "会。删除 App 时，保存在本机的内容会一并删除，请先导出备份。另外，删除单条内容会立即生效，没有回收站；删除分类前会请你确认。"),
        ("复习是怎么安排的？", "在「设置」中可以选择反馈方式：两档（不记得／记得）按 1、2、4、7、15、30 天的间隔推进，之后保持 30 天；三档（忘了／记得／很熟）和四档（忘了／困难／记得／很熟）根据你的反馈和上次的实际间隔计算，最长 365 天，也可以关闭「根据复习反馈自动调整间隔」。只有点了反馈按钮才算复习，打开或搜索内容不会改变安排；最近一次反馈可在 10 分钟内撤销。"),
        ("为什么收不到到期提醒？", "请在拾记的「设置」中开启「到期提醒」，并在系统「设置」→「通知」→「拾记」中允许通知；专注模式也可能让提醒静音。到期提醒是设备上的本地通知，不需要联网。"),
        ("如何使用主屏幕小组件？", "长按主屏幕空白处，点「编辑」→「添加小组件」，搜索「拾记」。中号和大号小组件可以直接点反馈按钮完成复习（可能需要先解锁设备）。小组件的刷新时间由系统决定。"),
        ("如何从其他 App 添加内容？", "在 Safari、照片、备忘录等 App 中点「分享」，选择「添加到拾记」，即可保存文字、网址或图片（每次最多 8 张）。也可以在「快捷指令」App 中使用拾记的「添加文本」「添加图片」动作。"),
        ("能搜索图片里的文字吗？", "可以。图片中的文字由 Apple 的文字识别在你的设备上识别，不会上传；第一次识别可能需要几秒钟。"),
        ("图片有什么限制？", "每条内容最多 8 张图片，每张不超过 25 MB、6000 万像素。"),
    ],
    support_privacy=("隐私", "<p>拾记不收集你的个人信息。详情请参阅{privacy}。</p>"),
    privacy_lead="拾记（以下简称“本 App”）由个人开发者开发和提供。我们重视你的隐私：本 App 不收集、不上传，也不出售你的任何个人信息。本政策说明本 App 如何处理你在设备上使用它时产生的数据。",
    privacy_sections=[
        ("我们不收集的信息", """<ul><li>本 App 没有账号注册和登录。</li>
<li>本 App 没有广告，也没有使用任何分析、崩溃统计、广告或其他第三方 SDK。</li>
<li>本 App 不追踪你，不读取广告标识符，也不会把你的数据与其他公司的数据关联。</li>
<li>开发者没有运营任何服务器，本 App 不会把你的内容发送给开发者或任何第三方。</li></ul>"""),
        ("保存在你设备上的数据", """<p>你在本 App 中输入或添加的内容（分类、标题、正文、图片、标签和重要程度），以及复习记录、复习安排和 App 设置，都只保存在你的设备上：存放在本 App 及其小组件、分享扩展共用的 App 存储空间里，并受 iOS 数据保护机制保护。</p>
<p>为了支持“搜索图片中的文字”，本 App 会在设备上识别图片文字，并把识别结果作为缓存保存在本机。开发者无法访问这些数据。</p>"""),
        ("权限", """<ul><li><strong>相机</strong>：仅在你点「拍照」时使用，用于拍摄需要复习的内容。</li>
<li><strong>照片</strong>：通过系统的照片选择器选择图片，本 App 只会取得你选中的图片。</li>
<li><strong>通知</strong>：用于在设备上安排到期提醒（本地通知），可随时关闭。</li></ul>
<p>你可以随时在系统「设置」中更改这些权限。</p>"""),
        ("Apple 提供的系统功能", "<p>图片文字识别使用 Apple 的 Vision 框架在设备上完成。主屏幕小组件、分享扩展和快捷指令动作都在你的设备上运行。当你通过 Siri 或「快捷指令」使用本 App 的动作时，相关数据由 Apple 按照其隐私政策处理。</p>"),
        ("备份与 iCloud", "<p>本 App 不使用 iCloud 同步。你可以手动导出备份，并把备份文件保存到你选择的位置（例如「文件」App 或 iCloud Drive）。备份文件包含你的全部内容、图片、复习记录和设置，没有加密，请妥善保管，不要分享给不信任的人。如果你开启了 iCloud 云备份或电脑备份，iOS 可能会把本 App 的数据纳入设备备份，由 Apple 处理。</p>"),
        ("购买", "<p>如果你在 App Store 购买本 App，付款由 Apple 处理。开发者不会收到你的付款信息，也不会收到可以识别你身份的信息。</p>"),
        ("你联系我们时", "<p>当你通过电子邮件联系我们时，我们会收到你的邮箱地址和你在邮件中提供的内容。这些信息只用于回复和处理你的问题，不会用于其他目的，也不会提供给第三方。</p>"),
        ("儿童隐私", "<p>本 App 不收集任何人的个人信息，包括儿童。</p>"),
        ("数据保留与删除", "<p>你的数据会一直保存在你的设备上，直到你删除。你可以在 App 中删除单条内容或分类；删除本 App 会同时删除保存在本机的数据（不包括你另外导出的备份文件和设备备份）。由于开发者不持有你的数据，我们无法替你找回或删除这些数据。</p>"),
        ("你的权利", "<p>根据适用的法律（例如中国《个人信息保护法》和欧盟《通用数据保护条例》），你对自己的个人信息享有查阅、更正、删除等权利。由于本 App 不收集你的个人信息，你可以直接在设备上查看、修改、导出（「导出备份」）和删除自己的数据。如有任何疑问，请联系我们。</p>"),
        ("本政策的变更", "<p>如果本政策有更新，我们会在本页面发布新版本，并更新上方的生效日期。</p>"),
        ("联系我们", "<p>对本政策有任何疑问，请发送邮件至 {mail}。另见{support}。</p>"),
    ],
),
"zh-Hant": dict(
    app="拾記", support="技術支援", privacy="隱私權政策", language="語言",
    updated="最後更新：2026 年 10 月 21 日", effective="生效日期：2026 年 10 月 21 日",
    support_lead="拾記是一款在本機運作的學習複習 App：把文字和圖片記下來，依遺忘曲線安排下一次複習，到期提醒你，複習時依記憶情況回饋。不需要註冊帳號，沒有廣告。",
    support_sections=[
        ("聯絡我們", """<p>如有問題、建議或發現錯誤，請寄信至 {mail}，我們會盡快回覆。</p>
<p>為了更快找到問題，請在信中附上：</p>
<ul><li>裝置型號，以及 iOS 或 iPadOS 版本；</li>
<li>拾記的版本號（可在系統「設定」→「一般」→「iPhone 儲存空間」→「拾記」中查看）；</li>
<li>問題描述和重現步驟，必要時附上截圖（請勿寄送你不想分享的內容）。</li></ul>"""),
        ("系統需求", """<p>需要 iOS 17.0 或 iPadOS 17.0 以上版本，支援 iPhone 和 iPad。</p>
<p>App 支援簡體中文、繁體中文、英文、日文、韓文和西班牙文，可在 App 的「設定」→「語言」中切換。</p>"""),
    ],
    faq_title="常見問題",
    faq=[
        ("需要註冊帳號或連網嗎？", "不需要。拾記沒有帳號、廣告和訂閱，所有功能都在你的裝置上完成。"),
        ("資料存在哪裡？會自動同步嗎？", "資料只存在你的裝置上，不會上傳到任何伺服器，也不會透過 iCloud 自動同步。如需換機或保存資料，請在「設定」中點「匯出備份」，把完整備份（包含圖片、複習紀錄和設定）存到「檔案」或 iCloud Drive，再在另一台裝置上點「匯入備份」恢復。"),
        ("恢復備份會發生什麼事？", "恢復會用備份內容取代目前的全部資料和設定。恢復前會先顯示備份內容讓你確認，並自動保存一份恢復前的安全備份。備份檔沒有加密，請妥善保管。"),
        ("刪除 App 會遺失資料嗎？", "會。刪除 App 時，存在本機的內容會一併刪除，請先匯出備份。另外，刪除單條內容會立即生效，沒有垃圾桶；刪除分類前會請你確認。"),
        ("複習是怎麼安排的？", "在「設定」中可以選擇回饋方式：兩檔（不記得／記得）依 1、2、4、7、15、30 天的間隔推進，之後維持 30 天；三檔（忘了／記得／很熟）和四檔（忘了／困難／記得／很熟）依你的回饋和上次的實際間隔計算，最長 365 天，也可以關閉「根據複習回饋自動調整間隔」。只有點了回饋按鈕才算複習，打開或搜尋內容不會改變安排；最近一次回饋可在 10 分鐘內撤銷。"),
        ("為什麼收不到到期提醒？", "請在拾記的「設定」中開啟「到期提醒」，並在系統「設定」→「通知」→「拾記」中允許通知；專注模式也可能讓提醒靜音。到期提醒是裝置上的本機通知，不需要連網。"),
        ("如何使用主畫面小工具？", "長按主畫面空白處，點「編輯」→「加入小工具」，搜尋「拾記」。中型和大型小工具可以直接點回饋按鈕完成複習（可能需要先解鎖裝置）。小工具的更新時間由系統決定。"),
        ("如何從其他 App 加入內容？", "在 Safari、照片、備忘錄等 App 中點「分享」，選擇「新增至拾記」，就能保存文字、網址或圖片（每次最多 8 張）。也可以在「捷徑」App 中使用拾記的「加入文字」「加入圖片」動作。"),
        ("能搜尋圖片裡的文字嗎？", "可以。圖片中的文字由 Apple 的文字辨識在你的裝置上辨識，不會上傳；第一次辨識可能需要幾秒鐘。"),
        ("圖片有什麼限制？", "每條內容最多 8 張圖片，每張不超過 25 MB、6000 萬像素。"),
    ],
    support_privacy=("隱私權", "<p>拾記不收集你的個人資料。詳情請參閱{privacy}。</p>"),
    privacy_lead="拾記（以下簡稱「本 App」）由個人開發者開發與提供。我們重視你的隱私：本 App 不收集、不上傳，也不出售你的任何個人資料。本政策說明本 App 如何處理你在裝置上使用它時產生的資料。",
    privacy_sections=[
        ("我們不收集的資料", """<ul><li>本 App 沒有帳號註冊和登入。</li>
<li>本 App 沒有廣告，也沒有使用任何分析、當機統計、廣告或其他第三方 SDK。</li>
<li>本 App 不追蹤你，不讀取廣告識別碼，也不會把你的資料與其他公司的資料連結。</li>
<li>開發者沒有經營任何伺服器，本 App 不會把你的內容傳送給開發者或任何第三方。</li></ul>"""),
        ("存在你裝置上的資料", """<p>你在本 App 中輸入或加入的內容（分類、標題、正文、圖片、標籤和重要程度），以及複習紀錄、複習安排和 App 設定，都只存在你的裝置上：存放在本 App 及其小工具、分享延伸功能共用的 App 儲存空間裡，並受 iOS 資料保護機制保護。</p>
<p>為了支援「搜尋圖片中的文字」，本 App 會在裝置上辨識圖片文字，並把辨識結果作為快取存在本機。開發者無法存取這些資料。</p>"""),
        ("權限", """<ul><li><strong>相機</strong>：只在你點「拍照」時使用，用於拍攝需要複習的內容。</li>
<li><strong>照片</strong>：透過系統的照片選擇器選擇圖片，本 App 只會取得你選取的圖片。</li>
<li><strong>通知</strong>：用於在裝置上安排到期提醒（本機通知），可隨時關閉。</li></ul>
<p>你可以隨時在系統「設定」中變更這些權限。</p>"""),
        ("Apple 提供的系統功能", "<p>圖片文字辨識使用 Apple 的 Vision 框架在裝置上完成。主畫面小工具、分享延伸功能和捷徑動作都在你的裝置上執行。當你透過 Siri 或「捷徑」使用本 App 的動作時，相關資料由 Apple 依其隱私權政策處理。</p>"),
        ("備份與 iCloud", "<p>本 App 不使用 iCloud 同步。你可以手動匯出備份，並把備份檔存到你選擇的位置（例如「檔案」App 或 iCloud Drive）。備份檔包含你的全部內容、圖片、複習紀錄和設定，沒有加密，請妥善保管，不要分享給不信任的人。如果你開啟了 iCloud 雲端備份或電腦備份，iOS 可能會把本 App 的資料納入裝置備份，由 Apple 處理。</p>"),
        ("購買", "<p>如果你在 App Store 購買本 App，付款由 Apple 處理。開發者不會收到你的付款資料，也不會收到可以識別你身分的資料。</p>"),
        ("你聯絡我們時", "<p>當你透過電子郵件聯絡我們時，我們會收到你的電子郵件地址和你在信中提供的內容。這些資料只用於回覆和處理你的問題，不會用於其他目的，也不會提供給第三方。</p>"),
        ("兒童隱私", "<p>本 App 不收集任何人的個人資料，包括兒童。</p>"),
        ("資料保留與刪除", "<p>你的資料會一直存在你的裝置上，直到你刪除。你可以在 App 中刪除單條內容或分類；刪除本 App 會同時刪除存在本機的資料（不包括你另外匯出的備份檔和裝置備份）。由於開發者沒有持有你的資料，我們無法替你找回或刪除這些資料。</p>"),
        ("你的權利", "<p>依適用的法律（例如中國《個人資訊保護法》和歐盟《一般資料保護規則》），你對自己的個人資料享有查閱、更正、刪除等權利。由於本 App 不收集你的個人資料，你可以直接在裝置上查看、修改、匯出（「匯出備份」）和刪除自己的資料。如有任何疑問，請聯絡我們。</p>"),
        ("本政策的變更", "<p>如果本政策有更新，我們會在本頁面發布新版本，並更新上方的生效日期。</p>"),
        ("聯絡我們", "<p>對本政策有任何疑問，請寄信至 {mail}。另見{support}。</p>"),
    ],
),
"en": dict(
    app="ReviewFlow", support="Support", privacy="Privacy Policy", language="Language",
    updated="Last updated: October 21, 2026", effective="Effective date: October 21, 2026",
    support_lead="ReviewFlow is a study review app that runs on your device: write down text and images, get the next review scheduled along a forgetting curve, receive a reminder when it is due, and give feedback on how well you remembered. No account, no ads.",
    support_sections=[
        ("Contact Us", """<p>For questions, suggestions or bug reports, email {mail}. We will reply as soon as we can.</p>
<p>To help us find the problem faster, please include:</p>
<ul><li>your device model and iOS or iPadOS version;</li>
<li>the ReviewFlow version (Settings › General › iPhone Storage › ReviewFlow);</li>
<li>what happened and the steps to reproduce it, with screenshots if helpful (please don’t send content you’d rather keep private).</li></ul>"""),
        ("Requirements", """<p>Requires iOS 17.0 or iPadOS 17.0 or later. Works on iPhone and iPad.</p>
<p>The app is available in Simplified Chinese, Traditional Chinese, English, Japanese, Korean and Spanish. Change it in the app under Settings › Language.</p>"""),
    ],
    faq_title="Frequently Asked Questions",
    faq=[
        ("Do I need an account or an internet connection?", "No. ReviewFlow has no accounts, ads or subscriptions, and everything works on your device."),
        ("Where is my data stored? Does it sync?", "Your data stays on your device. It is never uploaded to a server and is not synced through iCloud. To move to a new device or keep a copy, tap Export Backup in Settings and save the full backup (images, review history and settings included) to Files or iCloud Drive; then use Import Backup on the other device."),
        ("What happens when I restore a backup?", "Restoring replaces all current data and settings with the backup. You first see what the backup contains and confirm, and the app automatically keeps a safety backup of your data from before the restore. Backup files are not encrypted, so keep them somewhere safe."),
        ("Will I lose my data if I delete the app?", "Yes. Deleting the app removes the content stored on the device, so export a backup first. Note that deleting a single item takes effect immediately and there is no trash; deleting a folder asks you to confirm."),
        ("How are reviews scheduled?", "Choose a feedback style in Settings. Two options (Not Remembered / Remembered) advance through intervals of 1, 2, 4, 7, 15 and 30 days, then stay at 30 days. Three options (Forgot / Remembered / Fluent) and four options (Forgot / Difficult / Remembered / Fluent) calculate the next interval from your feedback and the last actual interval, up to 365 days; you can also turn off “Adapt intervals from review feedback”. Only tapping a feedback button counts as a review — opening or searching an item does not change its schedule. Your most recent feedback can be undone within 10 minutes."),
        ("Why don’t I get due reminders?", "Turn on Due reminders in the app’s Settings and allow notifications in Settings › Notifications › ReviewFlow. A Focus may also silence them. Reminders are local notifications on your device and do not need the internet."),
        ("How do I use the Home Screen widget?", "Touch and hold an empty area of the Home Screen, tap Edit › Add Widget and search for ReviewFlow. The medium and large widgets let you tap a feedback button to complete a review (you may need to unlock your device first). The system decides when widgets refresh."),
        ("How do I add content from other apps?", "In Safari, Photos, Notes and other apps, tap Share and choose Add to ReviewFlow to save text, a web link or images (up to 8 at a time). You can also use ReviewFlow’s Add Text and Add Images actions in the Shortcuts app."),
        ("Can I search the text in images?", "Yes. Text in images is recognized on your device by Apple’s text recognition and is never uploaded. The first recognition can take a few seconds."),
        ("Are there limits on images?", "Each item can hold up to 8 images, each up to 25 MB and 60 megapixels."),
    ],
    support_privacy=("Privacy", "<p>ReviewFlow does not collect your personal information. See the {privacy} for details.</p>"),
    privacy_lead="ReviewFlow (“the app”) is developed and provided by an individual developer. We take your privacy seriously: the app does not collect, upload or sell any of your personal information. This policy explains how the app handles the data created when you use it on your device.",
    privacy_sections=[
        ("Information We Don’t Collect", """<ul><li>The app has no account sign-up or sign-in.</li>
<li>The app shows no ads and includes no analytics, crash-reporting, advertising or other third-party SDKs.</li>
<li>The app does not track you, does not read the advertising identifier, and does not link your data with data from other companies.</li>
<li>The developer runs no servers, and the app never sends your content to the developer or to any third party.</li></ul>"""),
        ("Data Stored on Your Device", """<p>The content you enter or add in the app (folders, titles, text, images, tags and importance), together with your review history, review schedule and app settings, is stored only on your device — in storage shared by the app and its widget and share extension — and is protected by iOS data protection.</p>
<p>To let you search text inside images, the app recognizes that text on your device and keeps the results as a local cache. The developer cannot access any of this data.</p>"""),
        ("Permissions", """<ul><li><strong>Camera</strong>: used only when you tap Take Photo, to photograph content you want to review.</li>
<li><strong>Photos</strong>: you pick images with the system photo picker, and the app receives only the images you select.</li>
<li><strong>Notifications</strong>: used to schedule due reminders on your device (local notifications). You can turn them off at any time.</li></ul>
<p>You can change these permissions in the system Settings app at any time.</p>"""),
        ("System Features from Apple", "<p>Text recognition in images uses Apple’s Vision framework on your device. The Home Screen widget, the share extension and the Shortcuts actions run on your device. When you use the app’s actions through Siri or the Shortcuts app, Apple processes the related data under its own privacy policy.</p>"),
        ("Backups and iCloud", "<p>The app does not use iCloud sync. You can export a backup manually and save it to a location you choose, such as the Files app or iCloud Drive. A backup contains all your content, images, review history and settings and is not encrypted, so keep it safe and don’t share it with anyone you don’t trust. If you use iCloud Backup or back up to a computer, iOS may include the app’s data in your device backup, which Apple handles.</p>"),
        ("Purchases", "<p>If you buy the app on the App Store, Apple processes the payment. The developer does not receive your payment details or any information that identifies you.</p>"),
        ("When You Contact Us", "<p>If you email us, we receive your email address and whatever you include in your message. We use it only to answer and resolve your request, never for any other purpose, and we do not share it with third parties.</p>"),
        ("Children’s Privacy", "<p>The app does not collect personal information from anyone, including children.</p>"),
        ("Data Retention and Deletion", "<p>Your data stays on your device until you delete it. You can delete individual items or folders in the app; deleting the app also deletes the data stored on the device (but not backup files you exported or device backups). Because the developer does not hold your data, we cannot recover or delete it for you.</p>"),
        ("Your Rights", "<p>Under applicable laws, such as China’s Personal Information Protection Law and the EU General Data Protection Regulation, you have rights to access, correct and delete your personal information. Since the app does not collect your personal information, you can view, change, export (Export Backup) and delete your data directly on your device. If you have any questions, please contact us.</p>"),
        ("Changes to This Policy", "<p>If we update this policy, we will post the new version on this page and update the effective date above.</p>"),
        ("Contact Us", "<p>If you have any questions about this policy, email {mail}. See also {support}.</p>"),
    ],
),
"ja": dict(
    app="拾記", support="サポート", privacy="プライバシーポリシー", language="言語",
    updated="最終更新日：2026年10月21日", effective="施行日：2026年10月21日",
    support_lead="拾記は、端末上で動作する学習用の復習アプリです。テキストや画像を記録すると、忘却曲線に沿って次の復習日を決め、期限になると通知し、復習のたびに覚え具合を評価できます。アカウント登録は不要で、広告もありません。",
    support_sections=[
        ("お問い合わせ", """<p>ご質問、ご要望、不具合のご報告は {mail} までメールでお送りください。できるだけ早くお返事します。</p>
<p>問題を早く特定するため、次の情報を添えてください。</p>
<ul><li>デバイスの機種と iOS または iPadOS のバージョン</li>
<li>拾記のバージョン（「設定」>「一般」>「iPhone ストレージ」>「拾記」で確認できます）</li>
<li>起きたことと再現手順。必要に応じてスクリーンショット（共有したくない内容は送らないでください）</li></ul>"""),
        ("動作環境", """<p>iOS 17.0 または iPadOS 17.0 以降が必要です。iPhone と iPad に対応しています。</p>
<p>アプリは簡体字中国語、繁体字中国語、英語、日本語、韓国語、スペイン語に対応しており、アプリの「設定」>「言語」で切り替えられます。</p>"""),
    ],
    faq_title="よくある質問",
    faq=[
        ("アカウント登録やインターネット接続は必要ですか？", "いいえ。拾記にはアカウント、広告、サブスクリプションはなく、すべての機能が端末上で動作します。"),
        ("データはどこに保存されますか？自動で同期されますか？", "データは端末内にのみ保存され、サーバーにアップロードされることはなく、iCloud で自動同期されることもありません。機種変更やデータの保管には、「設定」の「バックアップを書き出す」で、画像・復習履歴・設定を含むバックアップを「ファイル」または iCloud Drive に保存し、別の端末で「バックアップを読み込む」を使ってください。"),
        ("バックアップを読み込むとどうなりますか？", "現在のすべてのデータと設定が、バックアップの内容に置き換わります。読み込む前にバックアップの内容が表示されて確認でき、置き換える前のデータは安全のために自動で保存されます。バックアップファイルは暗号化されていないため、大切に保管してください。"),
        ("アプリを削除するとデータは消えますか？", "はい。アプリを削除すると、端末内の内容も削除されます。先にバックアップを書き出してください。なお、項目を 1 件削除すると直ちに反映され、ゴミ箱はありません。フォルダを削除するときは確認が表示されます。"),
        ("復習の予定はどのように決まりますか？", "「設定」で評価の方法を選べます。2 段階（覚えていない／覚えた）は 1・2・4・7・15・30 日の間隔で進み、その後は 30 日のままです。3 段階（忘れた／覚えた／すらすら）と 4 段階（忘れた／難しい／覚えた／すらすら）は、評価と前回の実際の間隔から計算し、最長 365 日です。「復習の評価に合わせて間隔を調整」をオフにすることもできます。評価ボタンを押したときだけ復習として記録され、項目を開いたり検索したりしても予定は変わりません。直近の評価は 10 分以内なら取り消せます。"),
        ("期限のリマインダーが届きません", "アプリの「設定」で「期限のリマインダー」をオンにし、端末の「設定」>「通知」>「拾記」で通知を許可してください。集中モードによって通知が消音になることもあります。リマインダーは端末上のローカル通知で、インターネット接続は不要です。"),
        ("ホーム画面のウィジェットの使い方は？", "ホーム画面の何もないところを長押しし、「編集」>「ウィジェットを追加」から「拾記」を検索してください。中サイズと大サイズのウィジェットでは、評価ボタンを押して復習を完了できます（先にロック解除が必要な場合があります）。ウィジェットの更新タイミングはシステムが決めます。"),
        ("ほかのアプリから内容を追加するには？", "Safari、写真、メモなどのアプリで「共有」をタップし、「拾記に追加」を選ぶと、テキスト、Web リンク、画像（一度に 8 枚まで）を保存できます。「ショートカット」アプリで拾記の「テキストを追加」「画像を追加」アクションを使うこともできます。"),
        ("画像の中の文字を検索できますか？", "はい。画像内の文字は Apple の文字認識により端末上で認識され、アップロードされることはありません。初回の認識には数秒かかることがあります。"),
        ("画像に制限はありますか？", "1 件の項目に画像は 8 枚まで、1 枚あたり 25 MB・6000 万画素までです。"),
    ],
    support_privacy=("プライバシー", "<p>拾記はお客様の個人情報を収集しません。詳しくは{privacy}をご覧ください。</p>"),
    privacy_lead="拾記（以下「本アプリ」）は個人の開発者が開発・提供しています。私たちはお客様のプライバシーを大切にしています。本アプリは、お客様の個人情報を収集、アップロード、販売することは一切ありません。本ポリシーでは、端末で本アプリを使うときに生じるデータの取り扱いについて説明します。",
    privacy_sections=[
        ("収集しない情報", """<ul><li>本アプリにはアカウントの登録やサインインはありません。</li>
<li>本アプリには広告がなく、分析、クラッシュレポート、広告などのサードパーティ SDK も使用していません。</li>
<li>本アプリはお客様を追跡せず、広告識別子を読み取らず、お客様のデータをほかの企業のデータと結び付けることもありません。</li>
<li>開発者はサーバーを運営しておらず、本アプリがお客様の内容を開発者や第三者に送信することはありません。</li></ul>"""),
        ("端末に保存されるデータ", """<p>本アプリで入力・追加した内容（フォルダ、タイトル、本文、画像、タグ、重要度）と、復習履歴、復習の予定、アプリの設定は、端末内にのみ保存されます。保存先は本アプリとそのウィジェット、共有機能拡張が共用するアプリのストレージで、iOS のデータ保護によって保護されます。</p>
<p>画像内の文字を検索できるよう、本アプリは端末上で文字を認識し、その結果をキャッシュとして端末内に保存します。開発者はこれらのデータにアクセスできません。</p>"""),
        ("アクセス許可", """<ul><li><strong>カメラ</strong>：「写真を撮る」をタップしたときにのみ、復習したい内容を撮影するために使用します。</li>
<li><strong>写真</strong>：システムの写真ピッカーで画像を選び、本アプリは選択された画像のみを受け取ります。</li>
<li><strong>通知</strong>：端末上で期限のリマインダー（ローカル通知）を予約するために使用します。いつでもオフにできます。</li></ul>
<p>これらのアクセス許可は、端末の「設定」でいつでも変更できます。</p>"""),
        ("Apple が提供するシステム機能", "<p>画像内の文字認識には、Apple の Vision フレームワークを使い、端末上で処理します。ホーム画面のウィジェット、共有機能拡張、ショートカットのアクションは端末上で動作します。Siri や「ショートカット」アプリから本アプリのアクションを使う場合、関連するデータは Apple のプライバシーポリシーに従って処理されます。</p>"),
        ("バックアップと iCloud", "<p>本アプリは iCloud による同期を使用しません。バックアップは手動で書き出し、「ファイル」アプリや iCloud Drive など、お客様が選んだ場所に保存できます。バックアップにはすべての内容、画像、復習履歴、設定が含まれ、暗号化されていないため、大切に保管し、信頼できない相手と共有しないでください。iCloud バックアップやコンピュータへのバックアップを利用している場合、iOS が本アプリのデータを端末のバックアップに含めることがあり、それは Apple によって取り扱われます。</p>"),
        ("購入", "<p>App Store で本アプリを購入した場合、支払いは Apple が処理します。開発者がお客様の支払い情報や、お客様を特定できる情報を受け取ることはありません。</p>"),
        ("お問い合わせいただいた場合", "<p>メールでお問い合わせいただいた場合、私たちはお客様のメールアドレスとメールに記載された内容を受け取ります。これらはお問い合わせへの回答と対応のためにのみ使用し、ほかの目的には使用せず、第三者に提供することもありません。</p>"),
        ("お子様のプライバシー", "<p>本アプリは、お子様を含め、どなたの個人情報も収集しません。</p>"),
        ("データの保存期間と削除", "<p>データはお客様が削除するまで端末内に保存されます。アプリ内で項目やフォルダを削除でき、本アプリを削除すると端末内のデータも削除されます（別途書き出したバックアップファイルや端末のバックアップは除きます）。開発者はお客様のデータを保持していないため、代わりに復元や削除を行うことはできません。</p>"),
        ("お客様の権利", "<p>適用される法律（中国の個人情報保護法や EU の一般データ保護規則など）に基づき、お客様はご自身の個人情報の閲覧、訂正、削除などの権利を有します。本アプリは個人情報を収集しないため、お客様は端末上で直接、データの確認、変更、書き出し（「バックアップを書き出す」）、削除を行えます。ご不明な点はお問い合わせください。</p>"),
        ("本ポリシーの変更", "<p>本ポリシーを更新する場合は、このページに新しい版を掲載し、上記の施行日を更新します。</p>"),
        ("お問い合わせ", "<p>本ポリシーについてのご質問は {mail} までメールでお送りください。{support}もご覧ください。</p>"),
    ],
),
"ko": dict(
    app="ReviewFlow", support="지원", privacy="개인정보 처리방침", language="언어",
    updated="최종 업데이트: 2026년 10월 21일", effective="시행일: 2026년 10월 21일",
    support_lead="ReviewFlow는 기기에서 동작하는 학습 복습 앱입니다. 텍스트와 이미지를 기록하면 망각 곡선에 따라 다음 복습을 예약하고, 마감되면 알려 주며, 복습할 때마다 얼마나 기억했는지 피드백할 수 있습니다. 계정이 필요 없고 광고도 없습니다.",
    support_sections=[
        ("문의하기", """<p>질문, 제안 또는 오류 신고는 {mail}(으)로 이메일을 보내 주세요. 최대한 빨리 답변드리겠습니다.</p>
<p>문제를 빨리 찾을 수 있도록 다음 정보를 함께 보내 주세요.</p>
<ul><li>기기 모델과 iOS 또는 iPadOS 버전</li>
<li>ReviewFlow 버전(설정 > 일반 > iPhone 저장 공간 > ReviewFlow에서 확인)</li>
<li>발생한 문제와 재현 방법, 필요하면 스크린샷(공유하고 싶지 않은 내용은 보내지 마세요)</li></ul>"""),
        ("시스템 요구 사항", """<p>iOS 17.0 또는 iPadOS 17.0 이상이 필요하며 iPhone과 iPad를 지원합니다.</p>
<p>앱은 중국어(간체), 중국어(번체), 영어, 일본어, 한국어, 스페인어를 지원하며, 앱의 설정 > 언어에서 바꿀 수 있습니다.</p>"""),
    ],
    faq_title="자주 묻는 질문",
    faq=[
        ("계정이나 인터넷 연결이 필요한가요?", "아니요. ReviewFlow에는 계정, 광고, 구독이 없으며 모든 기능이 기기에서 동작합니다."),
        ("데이터는 어디에 저장되나요? 자동으로 동기화되나요?", "데이터는 기기에만 저장되며 서버로 업로드되지 않고 iCloud로 자동 동기화되지도 않습니다. 기기를 바꾸거나 데이터를 보관하려면 설정에서 '백업 내보내기'를 눌러 이미지, 복습 기록, 설정이 모두 포함된 백업을 '파일' 앱이나 iCloud Drive에 저장한 뒤, 다른 기기에서 '백업 가져오기'로 복원하세요."),
        ("백업을 복원하면 어떻게 되나요?", "현재의 모든 데이터와 설정이 백업 내용으로 바뀝니다. 복원하기 전에 백업 내용을 보여 주고 확인을 받으며, 복원 전 데이터는 안전을 위해 자동으로 따로 저장됩니다. 백업 파일은 암호화되지 않으므로 안전하게 보관하세요."),
        ("앱을 삭제하면 데이터가 사라지나요?", "네. 앱을 삭제하면 기기에 저장된 내용도 함께 삭제되므로 먼저 백업을 내보내세요. 또한 항목 하나를 삭제하면 바로 적용되며 휴지통이 없습니다. 폴더를 삭제할 때는 확인을 요청합니다."),
        ("복습 일정은 어떻게 정해지나요?", "설정에서 피드백 방식을 고를 수 있습니다. 2단계(기억나지 않음/기억함)는 1, 2, 4, 7, 15, 30일 간격으로 진행된 뒤 30일로 유지됩니다. 3단계(잊음/기억함/능숙함)와 4단계(잊음/어려움/기억함/능숙함)는 피드백과 지난번 실제 간격으로 다음 간격을 계산하며 최대 365일입니다. '복습 피드백에 따라 간격 조정'을 끌 수도 있습니다. 피드백 버튼을 눌러야만 복습으로 기록되며, 항목을 열거나 검색해도 일정은 바뀌지 않습니다. 가장 최근의 피드백은 10분 안에 취소할 수 있습니다."),
        ("마감 알림이 오지 않아요.", "앱의 설정에서 '마감 알림'을 켜고, 기기의 설정 > 알림 > ReviewFlow에서 알림을 허용하세요. 집중 모드 때문에 알림이 무음 처리될 수도 있습니다. 마감 알림은 기기의 로컬 알림이므로 인터넷이 필요하지 않습니다."),
        ("홈 화면 위젯은 어떻게 사용하나요?", "홈 화면의 빈 곳을 길게 누른 뒤 '편집' > '위젯 추가'를 누르고 ReviewFlow를 검색하세요. 중간 크기와 큰 크기 위젯에서는 피드백 버튼을 눌러 복습을 마칠 수 있습니다(먼저 기기 잠금을 해제해야 할 수 있습니다). 위젯이 새로 고쳐지는 시점은 시스템이 결정합니다."),
        ("다른 앱에서 내용을 추가하려면?", "Safari, 사진, 메모 등의 앱에서 '공유'를 누르고 'ReviewFlow에 추가'를 선택하면 텍스트, 웹 링크, 이미지(한 번에 최대 8장)를 저장할 수 있습니다. '단축어' 앱에서 ReviewFlow의 '텍스트 추가', '이미지 추가' 동작을 사용할 수도 있습니다."),
        ("이미지 속 글자도 검색할 수 있나요?", "네. 이미지 속 글자는 Apple의 텍스트 인식으로 기기에서 인식되며 업로드되지 않습니다. 처음 인식할 때는 몇 초가 걸릴 수 있습니다."),
        ("이미지에 제한이 있나요?", "항목 하나에 이미지를 최대 8장까지 넣을 수 있으며, 각 이미지는 25MB, 6,000만 화소 이하여야 합니다."),
    ],
    support_privacy=("개인정보 보호", "<p>ReviewFlow는 사용자의 개인정보를 수집하지 않습니다. 자세한 내용은 {privacy}을 참고하세요.</p>"),
    privacy_lead="ReviewFlow(이하 '앱')는 개인 개발자가 개발하고 제공합니다. 저희는 사용자의 개인정보를 소중히 여깁니다. 앱은 사용자의 개인정보를 수집하거나 업로드하거나 판매하지 않습니다. 이 방침은 기기에서 앱을 사용할 때 생기는 데이터를 앱이 어떻게 다루는지 설명합니다.",
    privacy_sections=[
        ("수집하지 않는 정보", """<ul><li>앱에는 계정 가입이나 로그인이 없습니다.</li>
<li>앱에는 광고가 없으며 분석, 충돌 보고, 광고 등 어떤 타사 SDK도 사용하지 않습니다.</li>
<li>앱은 사용자를 추적하지 않고, 광고 식별자를 읽지 않으며, 사용자의 데이터를 다른 회사의 데이터와 연결하지 않습니다.</li>
<li>개발자는 서버를 운영하지 않으며, 앱은 사용자의 내용을 개발자나 제3자에게 보내지 않습니다.</li></ul>"""),
        ("기기에 저장되는 데이터", """<p>앱에 입력하거나 추가한 내용(폴더, 제목, 본문, 이미지, 태그, 중요도)과 복습 기록, 복습 일정, 앱 설정은 기기에만 저장됩니다. 저장 위치는 앱과 앱의 위젯, 공유 확장 프로그램이 함께 쓰는 앱 저장 공간이며, iOS 데이터 보호 기능으로 보호됩니다.</p>
<p>이미지 속 글자를 검색할 수 있도록 앱은 기기에서 글자를 인식하고, 그 결과를 캐시로 기기에 저장합니다. 개발자는 이 데이터에 접근할 수 없습니다.</p>"""),
        ("권한", """<ul><li><strong>카메라</strong>: '사진 촬영'을 누를 때만 복습할 내용을 촬영하는 데 사용합니다.</li>
<li><strong>사진</strong>: 시스템 사진 선택기로 이미지를 고르며, 앱은 사용자가 선택한 이미지만 받습니다.</li>
<li><strong>알림</strong>: 기기에서 마감 알림(로컬 알림)을 예약하는 데 사용하며, 언제든지 끌 수 있습니다.</li></ul>
<p>이 권한들은 기기의 설정 앱에서 언제든지 변경할 수 있습니다.</p>"""),
        ("Apple이 제공하는 시스템 기능", "<p>이미지 속 글자 인식은 Apple의 Vision 프레임워크를 사용해 기기에서 처리됩니다. 홈 화면 위젯, 공유 확장 프로그램, 단축어 동작은 기기에서 실행됩니다. Siri나 '단축어' 앱으로 앱의 동작을 사용할 때 관련 데이터는 Apple의 개인정보 처리방침에 따라 처리됩니다.</p>"),
        ("백업과 iCloud", "<p>앱은 iCloud 동기화를 사용하지 않습니다. 백업은 직접 내보내서 '파일' 앱이나 iCloud Drive 등 원하는 위치에 저장할 수 있습니다. 백업에는 모든 내용, 이미지, 복습 기록, 설정이 들어 있고 암호화되지 않으므로 안전하게 보관하고 신뢰할 수 없는 사람과 공유하지 마세요. iCloud 백업이나 컴퓨터 백업을 사용하는 경우 iOS가 앱의 데이터를 기기 백업에 포함할 수 있으며, 이는 Apple이 처리합니다.</p>"),
        ("구매", "<p>App Store에서 앱을 구매하면 결제는 Apple이 처리합니다. 개발자는 사용자의 결제 정보나 사용자를 식별할 수 있는 정보를 받지 않습니다.</p>"),
        ("문의하실 때", "<p>이메일로 문의하시면 저희는 사용자의 이메일 주소와 메일에 적어 주신 내용을 받습니다. 이 정보는 문의에 답변하고 처리하는 데에만 사용하며, 다른 목적으로 사용하거나 제3자에게 제공하지 않습니다.</p>"),
        ("아동의 개인정보", "<p>앱은 아동을 포함해 누구의 개인정보도 수집하지 않습니다.</p>"),
        ("데이터 보관 및 삭제", "<p>데이터는 사용자가 삭제할 때까지 기기에 저장됩니다. 앱에서 항목이나 폴더를 삭제할 수 있으며, 앱을 삭제하면 기기에 저장된 데이터도 함께 삭제됩니다(따로 내보낸 백업 파일과 기기 백업은 제외). 개발자는 사용자의 데이터를 보관하지 않으므로 대신 복구하거나 삭제해 드릴 수 없습니다.</p>"),
        ("사용자의 권리", "<p>적용되는 법률(예: 중국 개인정보보호법, EU 일반 개인정보 보호법)에 따라 사용자는 자신의 개인정보를 열람, 정정, 삭제할 권리 등을 가집니다. 앱은 개인정보를 수집하지 않으므로, 사용자는 기기에서 직접 데이터를 확인, 수정, 내보내기('백업 내보내기'), 삭제할 수 있습니다. 궁금한 점이 있으면 문의해 주세요.</p>"),
        ("방침의 변경", "<p>이 방침을 변경하는 경우 이 페이지에 새 버전을 게시하고 위의 시행일을 업데이트합니다.</p>"),
        ("문의하기", "<p>이 방침에 대해 궁금한 점이 있으면 {mail}(으)로 이메일을 보내 주세요. {support} 페이지도 참고하세요.</p>"),
    ],
),
"es": dict(
    app="ReviewFlow", support="Soporte", privacy="Política de privacidad", language="Idioma",
    updated="Última actualización: 21 de octubre de 2026", effective="Fecha de entrada en vigor: 21 de octubre de 2026",
    support_lead="ReviewFlow es una app de repaso para estudiar que funciona en tu dispositivo: guarda textos e imágenes, programa el siguiente repaso según la curva del olvido, te avisa cuando toca y te deja indicar cuánto recordabas. No necesita cuenta y no tiene anuncios.",
    support_sections=[
        ("Contacto", """<p>Si tienes preguntas, sugerencias o encuentras un error, escribe a {mail}. Te responderemos lo antes posible.</p>
<p>Para ayudarnos a encontrar el problema más rápido, incluye:</p>
<ul><li>el modelo del dispositivo y la versión de iOS o iPadOS;</li>
<li>la versión de ReviewFlow (Ajustes › General › Almacenamiento del iPhone › ReviewFlow);</li>
<li>qué ocurrió y los pasos para reproducirlo, con capturas si ayudan (no envíes contenido que prefieras no compartir).</li></ul>"""),
        ("Requisitos", """<p>Requiere iOS 17.0 o iPadOS 17.0 o posterior. Funciona en iPhone y iPad.</p>
<p>La app está disponible en chino simplificado, chino tradicional, inglés, japonés, coreano y español. Puedes cambiar el idioma en la app, en Ajustes › Idioma.</p>"""),
    ],
    faq_title="Preguntas frecuentes",
    faq=[
        ("¿Necesito una cuenta o conexión a internet?", "No. ReviewFlow no tiene cuentas, anuncios ni suscripciones, y todo funciona en tu dispositivo."),
        ("¿Dónde se guardan mis datos? ¿Se sincronizan?", "Tus datos se quedan en tu dispositivo: nunca se suben a un servidor ni se sincronizan con iCloud. Para pasarlos a otro dispositivo o conservar una copia, toca «Exportar copia» en Ajustes y guarda la copia completa (con imágenes, historial de repasos y ajustes) en Archivos o iCloud Drive; después usa «Importar copia» en el otro dispositivo."),
        ("¿Qué ocurre al restaurar una copia?", "La restauración sustituye todos los datos y ajustes actuales por los de la copia. Antes verás qué contiene la copia y tendrás que confirmarlo, y la app guarda automáticamente una copia de seguridad de tus datos anteriores. Los archivos de copia no están cifrados, así que guárdalos en un lugar seguro."),
        ("¿Pierdo mis datos si elimino la app?", "Sí. Al eliminar la app se borra el contenido guardado en el dispositivo, así que exporta una copia antes. Ten en cuenta que eliminar un elemento se aplica al instante y no hay papelera; al eliminar una carpeta se te pide confirmación."),
        ("¿Cómo se programan los repasos?", "Elige el tipo de respuesta en Ajustes. Con dos opciones (No lo recuerdo / Recordado), los intervalos avanzan 1, 2, 4, 7, 15 y 30 días, y después se mantienen en 30 días. Con tres opciones (Olvidado / Recordado / Dominado) y cuatro (Olvidado / Difícil / Recordado / Dominado), el siguiente intervalo se calcula a partir de tu respuesta y del último intervalo real, hasta 365 días; también puedes desactivar «Adaptar los intervalos según la respuesta». Solo cuenta como repaso cuando tocas un botón de respuesta: abrir o buscar un elemento no cambia su programación. Puedes deshacer tu última respuesta durante 10 minutos."),
        ("¿Por qué no recibo los recordatorios?", "Activa «Recordatorios de vencimiento» en los Ajustes de la app y permite las notificaciones en Ajustes › Notificaciones › ReviewFlow. Un modo de concentración también puede silenciarlos. Los recordatorios son notificaciones locales del dispositivo y no necesitan internet."),
        ("¿Cómo uso el widget de la pantalla de inicio?", "Mantén pulsado un espacio vacío de la pantalla de inicio, toca «Editar» › «Añadir widget» y busca ReviewFlow. En los widgets mediano y grande puedes tocar un botón de respuesta para completar un repaso (puede que antes tengas que desbloquear el dispositivo). El sistema decide cuándo se actualizan los widgets."),
        ("¿Cómo añado contenido desde otras apps?", "En Safari, Fotos, Notas y otras apps, toca «Compartir» y elige «Añadir a ReviewFlow» para guardar texto, un enlace o imágenes (hasta 8 a la vez). También puedes usar las acciones «Añadir texto» y «Añadir imágenes» de ReviewFlow en la app Atajos."),
        ("¿Puedo buscar el texto de las imágenes?", "Sí. El texto de las imágenes se reconoce en tu dispositivo con el reconocimiento de texto de Apple y nunca se sube. El primer reconocimiento puede tardar unos segundos."),
        ("¿Hay límites para las imágenes?", "Cada elemento admite hasta 8 imágenes, de hasta 25 MB y 60 megapíxeles cada una."),
    ],
    support_privacy=("Privacidad", "<p>ReviewFlow no recopila tu información personal. Consulta la {privacy} para más detalles.</p>"),
    privacy_lead="ReviewFlow («la app») ha sido desarrollada y la ofrece un desarrollador independiente. Nos tomamos en serio tu privacidad: la app no recopila, no sube ni vende ninguna información personal tuya. Esta política explica cómo trata la app los datos que se generan cuando la usas en tu dispositivo.",
    privacy_sections=[
        ("Información que no recopilamos", """<ul><li>La app no tiene registro ni inicio de sesión.</li>
<li>La app no muestra anuncios ni incluye SDK de terceros de análisis, informes de fallos, publicidad ni de ningún otro tipo.</li>
<li>La app no te rastrea, no lee el identificador de publicidad y no vincula tus datos con datos de otras empresas.</li>
<li>El desarrollador no tiene servidores, y la app nunca envía tu contenido al desarrollador ni a terceros.</li></ul>"""),
        ("Datos guardados en tu dispositivo", """<p>El contenido que escribes o añades en la app (carpetas, títulos, textos, imágenes, etiquetas e importancia), junto con tu historial de repasos, la programación y los ajustes de la app, se guarda solo en tu dispositivo, en el almacenamiento que comparten la app, su widget y su extensión para compartir, y está protegido por la protección de datos de iOS.</p>
<p>Para que puedas buscar el texto de las imágenes, la app lo reconoce en tu dispositivo y guarda los resultados como caché local. El desarrollador no puede acceder a ninguno de estos datos.</p>"""),
        ("Permisos", """<ul><li><strong>Cámara</strong>: solo se usa cuando tocas «Hacer foto», para fotografiar contenido que quieras repasar.</li>
<li><strong>Fotos</strong>: eliges las imágenes con el selector de fotos del sistema y la app solo recibe las que seleccionas.</li>
<li><strong>Notificaciones</strong>: se usan para programar en tu dispositivo los recordatorios de vencimiento (notificaciones locales). Puedes desactivarlas cuando quieras.</li></ul>
<p>Puedes cambiar estos permisos en cualquier momento en la app Ajustes del sistema.</p>"""),
        ("Funciones del sistema de Apple", "<p>El reconocimiento de texto en imágenes usa el framework Vision de Apple en tu dispositivo. El widget de la pantalla de inicio, la extensión para compartir y las acciones de Atajos se ejecutan en tu dispositivo. Cuando usas las acciones de la app mediante Siri o la app Atajos, Apple trata los datos relacionados según su propia política de privacidad.</p>"),
        ("Copias de seguridad e iCloud", "<p>La app no usa la sincronización con iCloud. Puedes exportar una copia manualmente y guardarla donde elijas, como la app Archivos o iCloud Drive. La copia contiene todo tu contenido, imágenes, historial de repasos y ajustes, y no está cifrada, así que guárdala en un lugar seguro y no la compartas con nadie de quien no te fíes. Si usas la copia de seguridad de iCloud o haces copias en un ordenador, iOS puede incluir los datos de la app en la copia del dispositivo, que gestiona Apple.</p>"),
        ("Compras", "<p>Si compras la app en el App Store, Apple procesa el pago. El desarrollador no recibe tus datos de pago ni ninguna información que te identifique.</p>"),
        ("Cuando nos contactas", "<p>Si nos escribes, recibimos tu dirección de correo y lo que incluyas en el mensaje. Solo lo usamos para responder y resolver tu consulta, nunca para otros fines, y no lo compartimos con terceros.</p>"),
        ("Privacidad de los menores", "<p>La app no recopila información personal de nadie, incluidos los menores.</p>"),
        ("Conservación y eliminación de datos", "<p>Tus datos se conservan en tu dispositivo hasta que los eliminas. Puedes eliminar elementos o carpetas en la app; al eliminar la app también se borran los datos guardados en el dispositivo (pero no las copias que hayas exportado ni las copias de seguridad del dispositivo). Como el desarrollador no conserva tus datos, no podemos recuperarlos ni eliminarlos por ti.</p>"),
        ("Tus derechos", "<p>Según la legislación aplicable, como la Ley de Protección de Información Personal de China y el Reglamento General de Protección de Datos de la UE, tienes derecho a acceder a tu información personal, rectificarla y suprimirla, entre otros. Como la app no recopila tu información personal, puedes ver, modificar, exportar («Exportar copia») y eliminar tus datos directamente en tu dispositivo. Si tienes alguna pregunta, contáctanos.</p>"),
        ("Cambios en esta política", "<p>Si actualizamos esta política, publicaremos la nueva versión en esta página y actualizaremos la fecha de entrada en vigor indicada arriba.</p>"),
        ("Contacto", "<p>Si tienes preguntas sobre esta política, escribe a {mail}. Consulta también la página de {support}.</p>"),
    ],
),
}

CSS = """:root{color-scheme:light dark;--bg:#ffffff;--fg:#1d1d1f;--muted:#6e6e73;--line:#e5e5ea;--card:#f5f5f7;--link:#0066cc}
@media (prefers-color-scheme:dark){:root{--bg:#000000;--fg:#f5f5f7;--muted:#a1a1a6;--line:#2c2c2e;--card:#1c1c1e;--link:#4ea1ff}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:17px/1.65 -apple-system,BlinkMacSystemFont,"SF Pro Text","PingFang SC","PingFang TC","Hiragino Sans","Apple SD Gothic Neo","Helvetica Neue",Arial,sans-serif;-webkit-text-size-adjust:100%}
a{color:var(--link);text-decoration:none}a:hover{text-decoration:underline}
.wrap{max-width:760px;margin:0 auto;padding:0 20px}
header{border-bottom:1px solid var(--line)}
.bar{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;padding:14px 0}
.brand{display:flex;align-items:center;gap:10px;font-weight:600;color:var(--fg)}
.brand img{width:36px;height:36px;border-radius:9px}
.pages{display:flex;gap:18px;font-size:15px}
.pages a[aria-current=page]{color:var(--fg);font-weight:600}
.langs{display:flex;flex-wrap:wrap;gap:6px 14px;padding:10px 0 12px;font-size:14px;color:var(--muted)}
.langs a[aria-current=true]{color:var(--fg);font-weight:600}
main{padding:28px 0 40px}
h1{font-size:32px;line-height:1.25;margin:0 0 6px}
.meta{color:var(--muted);font-size:14px;margin:0 0 20px}
.lead{font-size:18px}
h2{font-size:22px;margin:36px 0 10px;padding-top:4px}
h3{font-size:17px;margin:22px 0 4px}
ul{padding-left:1.3em}li{margin:4px 0}
.faq{background:var(--card);border-radius:14px;padding:4px 18px 14px;margin-top:8px}
.faq p{margin:0 0 6px}
footer{border-top:1px solid var(--line);color:var(--muted);font-size:14px;padding:18px 0 40px}
.home h1{margin-top:8px}
.choices{list-style:none;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:12px}
.choices li{background:var(--card);border-radius:14px;padding:14px 16px;margin:0}
.choices strong{display:block;margin-bottom:4px}
.choices a{margin-right:14px}
"""


def page(code, kind):
    t = TEXT[code]
    htmllang = dict((c, h) for c, h, _ in LANGUAGES)[code]
    mail = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'
    other = {"support": ("privacy", t["privacy"]), "privacy": ("support", t["support"])}
    links = {"privacy": f'<a href="privacy.html">{t["privacy"]}</a>', "support": f'<a href="support.html">{t["support"]}</a>'}

    def fill(s):
        return s.format(mail=mail, privacy=links["privacy"], support=links["support"])

    title = t["support"] if kind == "support" else t["privacy"]
    alternates = "\n".join(
        f'<link rel="alternate" hreflang="{h}" href="../{c}/{kind}.html">' for c, h, _ in LANGUAGES)
    langs = " ".join(
        f'<a href="../{c}/{kind}.html" lang="{h}"{" aria-current=true" if c == code else ""}>{name}</a>'
        for c, h, name in LANGUAGES)
    if kind == "support":
        body = [f'<p class="lead">{t["support_lead"]}</p>']
        for heading, content in t["support_sections"]:
            body.append(f"<h2>{heading}</h2>\n{fill(content)}")
        body.append(f'<h2>{t["faq_title"]}</h2>\n<div class="faq">')
        for q, a in t["faq"]:
            body.append(f"<h3>{html.escape(q)}</h3>\n<p>{html.escape(a)}</p>")
        body.append("</div>")
        heading, content = t["support_privacy"]
        body.append(f"<h2>{heading}</h2>\n{fill(content)}")
        meta = t["updated"]
    else:
        body = [f'<p class="lead">{t["privacy_lead"]}</p>']
        for index, (heading, content) in enumerate(t["privacy_sections"], 1):
            body.append(f"<h2>{index}. {heading}</h2>\n{fill(content)}")
        meta = t["effective"]
    nav = (f'<a href="support.html"{" aria-current=page" if kind == "support" else ""}>{t["support"]}</a>'
           f'<a href="privacy.html"{" aria-current=page" if kind == "privacy" else ""}>{t["privacy"]}</a>')
    return f"""<!doctype html>
<html lang="{htmllang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · {t["app"]}</title>
<meta name="description" content="{html.escape(t["support_lead"] if kind == "support" else t["privacy_lead"])}">
<link rel="icon" href="../assets/icon.png">
<link rel="stylesheet" href="../style.css">
{alternates}
</head>
<body>
<header><div class="wrap">
<div class="bar"><a class="brand" href="../index.html"><img src="../assets/icon.png" alt="">{t["app"]}</a><nav class="pages">{nav}</nav></div>
<nav class="langs" aria-label="{t["language"]}">{langs}</nav>
</div></header>
<main class="wrap">
<h1>{t["app"]} {title}</h1>
<p class="meta">{meta}</p>
{chr(10).join(body)}
</main>
<footer><div class="wrap">© {YEAR} {t["app"]} · {mail}</div></footer>
</body>
</html>
"""


def index():
    items = "\n".join(
        f'<li lang="{h}"><strong>{name}</strong><a href="{c}/support.html">{TEXT[c]["support"]}</a>'
        f'<a href="{c}/privacy.html">{TEXT[c]["privacy"]}</a></li>' for c, h, name in LANGUAGES)
    return f"""<!doctype html>
<html lang="zh-Hans">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>拾记 · 拾記 · ReviewFlow</title>
<meta name="description" content="拾记（ReviewFlow）的技术支持与隐私政策 · Support and Privacy Policy for ReviewFlow.">
<link rel="icon" href="assets/icon.png">
<link rel="stylesheet" href="style.css">
</head>
<body class="home">
<header><div class="wrap"><div class="bar"><span class="brand"><img src="assets/icon.png" alt="">拾记 · 拾記 · ReviewFlow</span></div></div></header>
<main class="wrap">
<h1>拾记 · 拾記 · ReviewFlow</h1>
<p class="lead">记下来，再拾起。<br><span lang="en">Write it down, pick it up again.</span></p>
<ul class="choices">
{items}
</ul>
</main>
<footer><div class="wrap">© {YEAR} 拾记 · ReviewFlow · <a href="mailto:{EMAIL}">{EMAIL}</a></div></footer>
</body>
</html>
"""


def main():
    (ROOT / "style.css").write_text(CSS, encoding="utf-8")
    (ROOT / "index.html").write_text(index(), encoding="utf-8")
    (ROOT / ".nojekyll").write_text("", encoding="utf-8")
    for code, _, _ in LANGUAGES:
        folder = ROOT / code
        folder.mkdir(exist_ok=True)
        for kind in ("support", "privacy"):
            (folder / f"{kind}.html").write_text(page(code, kind), encoding="utf-8")
    print("Wrote index.html, style.css and", len(LANGUAGES) * 2, "pages")


if __name__ == "__main__":
    main()
