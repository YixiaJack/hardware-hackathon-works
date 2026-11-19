<div align="center">

# 🛠️ Hardware Hackathon Works · 硬件黑客松作品雷达

**自动收录全球硬件 / 机器人 / 具身交互赛事里最有意思的作品**
MakeMIT · Build18 · MakeUofT · Reality Hack · TreeHacks · Hackaday · Hackster · 立创开源 · AdventureX …

[![Works](https://img.shields.io/badge/作品-3952-38BDF8?style=flat-square)](https://hardware-hackathon-works.vercel.app/)
[![Winners](https://img.shields.io/badge/获奖作品-764-F59E0B?style=flat-square)](https://hardware-hackathon-works.vercel.app/)
[![Events](https://img.shields.io/badge/赛事系列-36%20·%20261%20届-10B981?style=flat-square)](#-赛事覆盖)
[![New](https://img.shields.io/badge/本周新增-首轮-EC4899?style=flat-square)](#-本周新增)
[![Updated](https://img.shields.io/badge/自动更新-2026--11--19-6366F1?style=flat-square)](.github/workflows/update.yml)

### 👉 [打开可视化作品库](https://hardware-hackathon-works.vercel.app/) · [RSS 订阅](https://hardware-hackathon-works.vercel.app/feed.xml) · [JSON 数据](data/projects.json)

</div>

> [!TIP]
> 本仓库是 [AlexDrives/hardware-hackathon-radar](https://github.com/AlexDrives/hardware-hackathon-radar)（追踪**赛事**）的姊妹项目，专注于**作品**：
> 每 6 小时由 GitHub Actions 自动抓取 Devpost / GitHub / Build18 / Hackster / 立创开源 等来源，
> 按 6 个正交维度自动分类、按「有意思指数」排序，并发布到可筛选的网页作品库。

---

## 🧭 分类方法：6 个正交维度

一件作品同时回答 6 个问题，每个维度独立筛选、可自由组合（例如「**无障碍 × 可穿戴 × 触觉反馈 × ESP32**」）：

| 维度 | 回答的问题 | 举例 |
| :-- | :-- | :-- |
| **场景** Domain | 为谁、解决什么问题？ | 健康医疗 · 无障碍 · 效率自律 · 社交情感 · 艺术音乐 … |
| **形态** Form | 做出来是个什么东西？ | 可穿戴 · 移动机器人 · 机械臂 · 陪伴玩偶 · 制造机器 … |
| **交互** Interaction | 人怎么和它打交道？ | 语音 · 视觉手势 · 触觉 · 实体操控 · 生理信号 … |
| **平台** Platform | 用了什么硬件平台？ | Arduino · ESP32 · Raspberry Pi · Jetson · ROS … |
| **智能** AI | 用了什么 AI 能力？ | 大模型 · 计算机视觉 · 端侧 ML · 机器人学习 … |
| **工艺** Fabrication | 怎么造出来的？ | 3D 打印 · 激光切割 · PCB 设计 · CAD … |

外加 **赛事 / 年份 / 获奖等级 / 编辑精选 / 亮点（脑洞·温度·硬核·实用·社会价值）** 五个辅助维度。
分类规则全部写在 [`config/taxonomy.toml`](config/taxonomy.toml)，改关键词即可重新分类；可选的 LLM 精修见 [`pipeline/enrich.py`](pipeline/enrich.py)。

**当前分布**

| 维度 | 分布 Top |
| :-- | :-- |
| **场景** Domain | 🌱环境可持续 414 · 🩺健康医疗 395 · 🎮游戏娱乐 371 · 🏠家居生活 369 · 🚲出行交通 271 · 🛠️工具与制造 268 |
| **形态** Form factor | 📟桌面小装置 673 · ⌚可穿戴 337 · 🪑智能物件/家具 240 · ⚙️制造机器/机构 207 · 🤖移动机器人 154 · 🛴载具 142 |
| **交互** Interaction | 📡环境感知/自主 817 · 💡光与显示 380 · 👋视觉/手势 379 · 🗣️语音对话 237 · 🎛️实体操控 136 · 🧠生理信号 110 |
| **平台** Platform | ♾️Arduino 657 · 📶ESP32/ESP8266 265 · 🍓Raspberry Pi 240 · 🟩NVIDIA Jetson 37 · 🔧其他 MCU 32 · 🛰️ROS 25 |
| **智能** AI capability | 👁️计算机视觉 281 · ✨大模型/生成式 258 · 📈机器学习 118 · 🎙️语音 AI 79 · 🦿机器人学习 30 · 🔋端侧 ML 23 |
| **工艺** Fabrication | 🧱3D 打印 204 · 📐CAD 建模 114 · 🔦激光切割 106 · 🧵织物/手工 36 · 🟢PCB 设计 12 |

### 「有意思指数」怎么算？（0–100）

`获奖等级（一等奖 38 / 赛道奖 26 / 赞助奖 16）` + `点赞数（对数）` + `GitHub Star（对数）` + `有演示视频 / 开源仓库 / 实拍图` + `文档完整度` + `硬件深度` + `纯硬件赛事加成` + `编辑精选 22`。
它不代表作品好坏，只用来把「最值得先看的」排在前面。公式见 [`pipeline/classify.py`](pipeline/classify.py)。

---

## ⭐ 编辑精选

| 作品 | 一句话 | 赛事 | 标签 | 指数 |
| :-- | :-- | :-- | :-- | --: |
| [**Unsynthesizer**](https://devpost.com/software/unsynthesizer-2jxeoy) | 不用电子元件、只靠声音的无线键盘：每个键敲出不同频率，电脑靠滤波识别按键 | MakeMIT 2020 | `工具与制造` `游戏娱乐` 🏆 First Place | 100 |
| [**Scribblr**](https://devpost.com/software/scribblr-0bxzq4) | 听课 → Gemini 提炼重点 → 单笔画 G-code → 机械手拿真粉笔写在黑板上 | MakeMIT x Harvard 2026 | `教育学习` 🏆 Seed Studio Interactive Signage | 74 |
| [**Whackathon**](https://devpost.com/software/whackathon-w0e27o) | 检测到你驼背成『虾』就立刻物理惩罚的椅子 | MakeMIT x Harvard 2026 | `健康医疗` `效率与自律` 🏆 [MLH] Best Use of ElevenLabs | 62 |
| [**Bless You Polar Bear**](https://github.com/NaemBi-Bap-MAKE-MIT-2026-Team) | 独居异乡打喷嚏没人说『Bless you』？北极熊玩偶用本地小模型听到喷嚏并回应关怀 | MakeMIT x Harvard 2026 | `社交情感` 🏆 Sustainability — 3rd Place | 54 |
| [**Locky**](https://github.com/Vishvenugopal/Locky-MakeMIT) | 把手机锁进会自己躲到你视线死角的小车，戒手机的『躲猫猫』 | MakeMIT x Harvard 2026 | `出行交通` `家居生活`  | 44 |
| [**A.L.I.C.E. MedDispenser**](https://github.com/preespp/MakeMIT_2026_Team7) | Jetson 本地人脸识别 + ESP32 出药的分药终端，LLM 只做可选建议并带本地降级 | MakeMIT x Harvard 2026 | `健康医疗`  | 40 |
| [**Auto-Focus Glasses**](https://github.com/laoeked1111/plase-read-instructions) | 双手占满时用语音让眼镜用丝杆物理变焦，给外科医生和电工的『放大镜』 | MakeMIT x Harvard 2026 | `效率与自律`  | 39 |

> 想推荐作品？在 [`config/picks.toml`](config/picks.toml) 里加几行（链接 + 一句话 + 点评）提个 PR 即可。

---

## 🗂️ 按场景浏览（每类 Top 5）

<details><summary><b>🩺 健康医疗 · Health & Medical</b> — 395 件</summary>

| 作品 | 一句话 | 赛事 | 标签 | 指数 |
| :-- | :-- | :-- | :-- | --: |
| [**RxID**](https://devpost.com/software/rxid) | Managing medication is as simple as a tap. Our RFID health bracelet securely stores medic… | MakeUofT 2025 | `健康医疗` 🏆 1st Place Prize | 82 |
| [**Twin**](https://devpost.com/software/twin-pywkb4) | Lost? Panicking? Heart racing?Twin’s got your back—and your head. Built into a hard hat,… | MakeUofT 2026 | `环境可持续` `健康医疗` 🏆 1st Place: Meta Glasses | 76 |
| [**The Exercists**](https://devpost.com/software/the-exercists) | Expelling the laziness from our bodies; like Typeracer for your muscles. | UTRA Hacks 2025 | `健康医疗` 🏆 Best AI Project with Databricks Open Source - Assorted Lego Sets | 70 |
| [**Healthbox**](https://devpost.com/software/healthbox) | Healthbox helps users take medication on time with ongoing reminders, camera-assisted rec… | MakeCU | `效率与自律` `健康医疗` 🏆 Hacker's Choice Winning Team | 69 |
| [**Forget Me Not**](https://devpost.com/software/forget-me-not-674kto) | Keeping Watch. | UTRA Hacks 2025 | `健康医疗` `安全应急` 🏆 Open Challenge | 68 |

</details>

<details><summary><b>♿ 无障碍辅助 · Accessibility</b> — 227 件</summary>

| 作品 | 一句话 | 赛事 | 标签 | 指数 |
| :-- | :-- | :-- | :-- | --: |
| [**BrailleBridge**](https://devpost.com/software/braillebridge-41nacb) | Words in, Braille out! | MadHacks 2026 | `无障碍辅助` 🏆 N+1 Institute Prize Track - 1st place | 77 |
| [**Alfred Robot Butler**](https://devpost.com/software/alfred-robot-butler) | Alfred Butler is a voice-powered personal care assistant to help users who lack fine moto… | Robotic Agents Hackathon | `无障碍辅助` `家居生活` 🏆 Grand Prize: Cyberwave Track | 70 |
| [**DotSight**](https://devpost.com/software/dotsight-cdelxi) | DotSight helps deaf & blind users identify everyday objects. Point the camera, press a bu… | MakeCU | `无障碍辅助` `家居生活` 🏆 Healthcare Track Winning Team | 68 |
| [**Tactile - Perceived by Touch**](https://devpost.com/software/tactile-par4yx) | Real Time Text to Braille Translator | MakeMIT 2016 | `无障碍辅助` 🏆 1st Place | 68 |
| [**CPR Trainer**](https://devpost.com/software/cpr-trainer-a9olkm) | Educate the public with an accessible CPR trainer that eliminates the need for expensive… | IDEA Hacks 2026 | `健康医疗` `无障碍辅助` 🏆 2nd Place Prize | 67 |

</details>

<details><summary><b>🌱 环境可持续 · Sustainability</b> — 414 件</summary>

| 作品 | 一句话 | 赛事 | 标签 | 指数 |
| :-- | :-- | :-- | :-- | --: |
| [**AutoDump: Autonomous Self-Emptying Trash Rover**](https://devpost.com/software/autodump-autonomous-self-emptying-trash-rover) | A Raspberry Pi rover that finds full bins, docks, and auto-dumps into a central can using… | MakeCU | `环境可持续` `家居生活` 🏆 3rd Place Overall | 84 |
| [**Twin**](https://devpost.com/software/twin-pywkb4) | Lost? Panicking? Heart racing?Twin’s got your back—and your head. Built into a hard hat,… | MakeUofT 2026 | `环境可持续` `健康医疗` 🏆 1st Place: Meta Glasses | 76 |
| [**The Quicker Picker Upper**](https://devpost.com/software/the-quicker-picker-upper) | Save the 5 minute pause at the trash cans trying to figure out if you're cup is recyclabl… | MakeUofT 2025 | `环境可持续` `家居生活` 🏆 2nd Place Overall | 73 |
| [**TrusToken & Autonomous Vehicle (Seperate)**](https://devpost.com/software/dontgotoneyet) | Transforming everyday sustainable actions into AI-verified, NFTs that people can trust, e… | UTRA Hacks 2026 | `环境可持续` `出行交通` 🏆 UTRA Hacks 2026: 3rd Place - MSI Radeon RX 6600 XT GAMING X 8G (graphics card) | 69 |
| [**MA-NO**](https://devpost.com/software/ma-no-092j5i) | MA-NO is an AI-powered recycling robot that uses computer vision and a robotic arm to ide… | Robotic Agents Hackathon | `环境可持续` 🏆 Best Manipulation Use Case: Cyberwave Track | 66 |

</details>

<details><summary><b>🌾 农业食物 · Food & Agriculture</b> — 208 件</summary>

| 作品 | 一句话 | 赛事 | 标签 | 指数 |
| :-- | :-- | :-- | :-- | --: |
| [**AvocadoBro**](https://devpost.com/software/glycemic-index-tracker) | An essential grocery shopping companion | Longhorn Robotics 2nd Annual Hackathon | `农业食物` `社交情感` 🏆 1st Place | 73 |
| [**PlantPartner**](https://devpost.com/software/plantpartner) | An inexpensive robotic assistant that monitors plants and diagnoses issues using AI techn… | MakeNJIT Hardware Hackathon 2024 | `农业食物` `工具与制造` 🏆 First Place | 66 |
| [**Sator**](https://devpost.com/software/sator-hjvswp) | Turn fields into live dashboards. Sator translates ground truth from a compact rover into… | MakeCU | `农业食物` 🏆 2nd Place Overall | 66 |
| [**TofuPresto**](https://devpost.com/software/tofupresto) | Eating tofu is modernized by a hands-off IoT tofu press that gradually presses your tofu… | MakeMIT 2019 | `农业食物` 🏆 First Place | 64 |
| [**Plant Pal**](https://devpost.com/software/plant-pal-tpl7e4) | Plant Pal connects to sensors to monitor soil and light, giving real-time tips and alerts… | MakeNJIT 2025 | `农业食物` `健康医疗` 🏆 Second Place | 61 |

</details>

<details><summary><b>🏠 家居生活 · Home & Everyday</b> — 369 件</summary>

| 作品 | 一句话 | 赛事 | 标签 | 指数 |
| :-- | :-- | :-- | :-- | --: |
| [**AutoDump: Autonomous Self-Emptying Trash Rover**](https://devpost.com/software/autodump-autonomous-self-emptying-trash-rover) | A Raspberry Pi rover that finds full bins, docks, and auto-dumps into a central can using… | MakeCU | `环境可持续` `家居生活` 🏆 3rd Place Overall | 84 |
| [**The Quicker Picker Upper**](https://devpost.com/software/the-quicker-picker-upper) | Save the 5 minute pause at the trash cans trying to figure out if you're cup is recyclabl… | MakeUofT 2025 | `环境可持续` `家居生活` 🏆 2nd Place Overall | 73 |
| [**Alfred Robot Butler**](https://devpost.com/software/alfred-robot-butler) | Alfred Butler is a voice-powered personal care assistant to help users who lack fine moto… | Robotic Agents Hackathon | `无障碍辅助` `家居生活` 🏆 Grand Prize: Cyberwave Track | 70 |
| [**Dreaming Objects**](https://devpost.com/software/living-room-dreaming-objects) | Everyday items that interact, empathize, and thrive together. | HARD MODE: Hardware x AI Hackathon | `家居生活` 🏆 Grand Prize (E14 Fund) | 69 |
| [**Dormmate**](https://devpost.com/software/dormmate-eqzk0n) | Dormmate is a smart doorbell that sends push notifications to your phone when visitors ar… | MakeCU | `家居生活` 🏆 1st Place Overall | 68 |

</details>

<details><summary><b>⏱️ 效率与自律 · Productivity & Habits</b> — 181 件</summary>

| 作品 | 一句话 | 赛事 | 标签 | 指数 |
| :-- | :-- | :-- | :-- | --: |
| [**Healthbox**](https://devpost.com/software/healthbox) | Healthbox helps users take medication on time with ongoing reminders, camera-assisted rec… | MakeCU | `效率与自律` `健康医疗` 🏆 Hacker's Choice Winning Team | 69 |
| [**Progress Pal**](https://devpost.com/software/productivity-tracker-1nvc36) | Track your productivity, and receive feedback on how to optimize your daily routine. | Longhorn Robotics 2nd Annual Hackathon | `效率与自律` 🏆 2nd Place | 63 |
| [**Whackathon**](https://devpost.com/software/whackathon-w0e27o) | 检测到你驼背成『虾』就立刻物理惩罚的椅子 | MakeMIT x Harvard 2026 | `健康医疗` `效率与自律` 🏆 [MLH] Best Use of ElevenLabs | 62 |
| [**Napkn**](https://devpost.com/software/napkn-kavgmw) | Easily reserve tables, analyze dining/study hall traffic, and optimize your eating and st… | IDEA Hacks 2020 | `效率与自律` `出行交通` 🏆 IDEA Hacks 1st Place Grand Prize | 60 |
| [**PiggyBack**](https://devpost.com/software/piggyback-3sh48q) | Today's digital money feels invisible. PiggyBack makes your digital spending physical aga… | MakeCU | `效率与自律` 🏆 [MLH] Best Use of Tiger Data | 59 |

</details>

<details><summary><b>🎓 教育学习 · Education</b> — 221 件</summary>

| 作品 | 一句话 | 赛事 | 标签 | 指数 |
| :-- | :-- | :-- | :-- | --: |
| [**LABKickstart**](https://devpost.com/software/labkickstart) | It’s nobody’s fault that modern physics experimentation is broken | IDEA Hacks 2026 | `教育学习` 🏆 1st Place Prize | 76 |
| [**Scribblr**](https://devpost.com/software/scribblr-0bxzq4) | 听课 → Gemini 提炼重点 → 单笔画 G-code → 机械手拿真粉笔写在黑板上 | MakeMIT x Harvard 2026 | `教育学习` 🏆 Seed Studio Interactive Signage | 74 |
| [**PillBoy**](https://devpost.com/software/pillboy) | An IOT prescription manager that seamlessly (and aesthetically) integrates into your day… | MakeMIT 2019 | `健康医疗` `教育学习` 🏆 Infosys Most Innovative Hack | 61 |
| [**Rockin' A Sweet Seat**](https://devpost.com/software/rockin-a-sweet-seat) | Car Seats need to be smarter. Data for parents, kids and the manufacturer is critical. Le… | IoTHackDay 2017 | `出行交通` `教育学习` 🏆 Grand Prize Winner - Prize Weighted Towards Ideas with Startup Business Potential | 61 |
| [**TransLyte**](https://devpost.com/software/trans-lyte) | To elevate the students of tomorrow in their educational journey and boost confidence in… | IDEA Hacks 2026 | `教育学习` 🏆 3rd Place Prize | 59 |

</details>

<details><summary><b>🛡️ 安全应急 · Safety & Security</b> — 217 件</summary>

| 作品 | 一句话 | 赛事 | 标签 | 指数 |
| :-- | :-- | :-- | :-- | --: |
| [**Forget Me Not**](https://devpost.com/software/forget-me-not-674kto) | Keeping Watch. | UTRA Hacks 2025 | `健康医疗` `安全应急` 🏆 Open Challenge | 68 |
| [**PipeX**](https://devpost.com/software/pipex) | PipeX is a pipe crawling robot that automates risky pipe inspection and maintenance. Pipe… | RoboTech 2025 | `工具与制造` `安全应急` 🏆 Advanced Track - Winner | 66 |
| [**RuffTerrain**](https://devpost.com/software/ruffterrain) | RuffTerrain sends autonomous robots into active wildfires to find survivors using compute… | Robotic Agents Hackathon | `环境可持续` `安全应急` 🏆 First Prize: Scrapegraph AI Track | 66 |
| [**Hear-O Squad**](https://devpost.com/software/hear-o-squad) | Silent No More: A Wearable Device That Lets You See and Feel Important Sounds | MakeUofT 2025 | `安全应急` `无障碍辅助` 🏆 Theme Prize: Wearable Tech | 64 |
| [**LIFE-line**](https://devpost.com/software/lifeline-pcsmi2) | Relief for your family, make sure get there in time. A lagless response, immediate action… | IDEA Hacks 2024 | `安全应急` `社交情感` 🏆 $500 cash divided amongst team from Patient Safety | 61 |

</details>

<details><summary><b>🚲 出行交通 · Mobility & Transport</b> — 271 件</summary>

| 作品 | 一句话 | 赛事 | 标签 | 指数 |
| :-- | :-- | :-- | :-- | --: |
| [**Project Jeremy and DriveCode**](https://devpost.com/software/project-just-coding-destructive-jam-kite-robot-j-c-d-j-k-r) | Our magnificent 2 Wheeled Robot Jeremy will be able to tackle this obstacle course in sev… | UTRA Hacks 2026 | `出行交通` 🏆 UTRA Hacks 2026: 1st Place  - ASUS ROG Zephyrus G16 (2025) | 74 |
| [**TrusToken & Autonomous Vehicle (Seperate)**](https://devpost.com/software/dontgotoneyet) | Transforming everyday sustainable actions into AI-verified, NFTs that people can trust, e… | UTRA Hacks 2026 | `环境可持续` `出行交通` 🏆 UTRA Hacks 2026: 3rd Place - MSI Radeon RX 6600 XT GAMING X 8G (graphics card) | 69 |
| [**Rockin' A Sweet Seat**](https://devpost.com/software/rockin-a-sweet-seat) | Car Seats need to be smarter. Data for parents, kids and the manufacturer is critical. Le… | IoTHackDay 2017 | `出行交通` `教育学习` 🏆 Grand Prize Winner - Prize Weighted Towards Ideas with Startup Business Potential | 61 |
| [**WALL-E**](https://devpost.com/software/wannabe-wall-e) | Arduino-powered robot with various sensors that can play capture the flag and solve mazes | UTRA Hacks 2025 | `出行交通` `游戏娱乐` 🏆 Closed Challenge | 61 |
| [**Napkn**](https://devpost.com/software/napkn-kavgmw) | Easily reserve tables, analyze dining/study hall traffic, and optimize your eating and st… | IDEA Hacks 2020 | `效率与自律` `出行交通` 🏆 IDEA Hacks 1st Place Grand Prize | 60 |

</details>

<details><summary><b>🎨 艺术音乐 · Art & Music</b> — 231 件</summary>

| 作品 | 一句话 | 赛事 | 标签 | 指数 |
| :-- | :-- | :-- | :-- | --: |
| [**Cadence**](https://devpost.com/software/cadence-l1axr5) | With Cadence, your hands are the only instrument you need. Wear the glove, move your fing… | MakeMIT x Harvard 2026 | `艺术音乐` 🏆 Infosys Overall Grand Prize | 79 |
| [**flatline**](https://devpost.com/software/flatline-wryife) | play your heart out &lt;3 | HackUMass XIV | `艺术音乐` `游戏娱乐` 🏆 [HACKUMASS] Grand Prize | 76 |
| [**Vinyl Vision**](https://devpost.com/software/vivis) | Display your music from your record player! | IDEA Hacks 2025 | `艺术音乐` 🏆 1st Place Winner | 69 |
| [**RobTop**](https://devpost.com/software/robtop) | A robot arm for your desk that takes on whatever you put in front of it: it draws, feeds… | HackUMass XIV | `游戏娱乐` `艺术音乐` 🏆 [HACKUMASS] [HARDWARE] Best Mechanical Hack | 67 |
| [**Wearable CPR Guide (No One Bites The Dust)**](https://devpost.com/software/no-one-bites-the-dust) | Tired of staring into training mannequins' soulless eyes? Try the wearable CPR guide, an… | MakeUofT 2026 | `艺术音乐` `健康医疗` 🏆 (Survival Theme) North Face Fanny Pack | 63 |

</details>

<details><summary><b>🎮 游戏娱乐 · Games & Fun</b> — 371 件</summary>

| 作品 | 一句话 | 赛事 | 标签 | 指数 |
| :-- | :-- | :-- | :-- | --: |
| [**Unsynthesizer**](https://devpost.com/software/unsynthesizer-2jxeoy) | 不用电子元件、只靠声音的无线键盘：每个键敲出不同频率，电脑靠滤波识别按键 | MakeMIT 2020 | `工具与制造` `游戏娱乐` 🏆 First Place | 100 |
| [**PrimePong**](https://devpost.com/software/primepong) | PrimePong fuses cutting-edge tech with table tennis! Our fully equipped paddle tracks eve… | MakeUofT 2025 | `游戏娱乐` 🏆 3rd Place Overall | 81 |
| [**flatline**](https://devpost.com/software/flatline-wryife) | play your heart out &lt;3 | HackUMass XIV | `艺术音乐` `游戏娱乐` 🏆 [HACKUMASS] Grand Prize | 76 |
| [**RobTop**](https://devpost.com/software/robtop) | A robot arm for your desk that takes on whatever you put in front of it: it draws, feeds… | HackUMass XIV | `游戏娱乐` `艺术音乐` 🏆 [HACKUMASS] [HARDWARE] Best Mechanical Hack | 67 |
| [**Magnus Force Nerf Gun**](https://devpost.com/software/magnus_gun) | This nerf gun curves its shots midair to hit targets detected with computer vision | MakeMIT 2019 | `游戏娱乐` 🏆 Second Place | 65 |

</details>

<details><summary><b>💞 社交情感 · Social & Emotional</b> — 217 件</summary>

| 作品 | 一句话 | 赛事 | 标签 | 指数 |
| :-- | :-- | :-- | :-- | --: |
| [**AvocadoBro**](https://devpost.com/software/glycemic-index-tracker) | An essential grocery shopping companion | Longhorn Robotics 2nd Annual Hackathon | `农业食物` `社交情感` 🏆 1st Place | 73 |
| [**TeddyTalk**](https://devpost.com/software/teddytalk-eh5gjm) | Have you ever wanted an AI Build-A-Bear? | MakeUofT 2026 | `社交情感` 🏆 Best Use of Arduino Uno Q (1st Place) | 67 |
| [**Cupid Glasses**](https://devpost.com/software/cupid-glasses) | Wearable smart glasses that recognize a saved profile (friend) and generates personalized… | MakeUofT 2026 | `社交情感` 🏆 (Valentine's Theme) Lego Cherry Blossoms | 63 |
| [**Anti Anti-Masker Mask**](https://devpost.com/software/anti-anti-masker-mask) | Taking social distancing to the next level | MakeUofT 2022 | `社交情感` `健康医疗` 🏆 2nd Place Overall | 61 |
| [**LIFE-line**](https://devpost.com/software/lifeline-pcsmi2) | Relief for your family, make sure get there in time. A lagless response, immediate action… | IDEA Hacks 2024 | `安全应急` `社交情感` 🏆 $500 cash divided amongst team from Patient Safety | 61 |

</details>

<details><summary><b>🛠️ 工具与制造 · Tools & Industry</b> — 268 件</summary>

| 作品 | 一句话 | 赛事 | 标签 | 指数 |
| :-- | :-- | :-- | :-- | --: |
| [**Unsynthesizer**](https://devpost.com/software/unsynthesizer-2jxeoy) | 不用电子元件、只靠声音的无线键盘：每个键敲出不同频率，电脑靠滤波识别按键 | MakeMIT 2020 | `工具与制造` `游戏娱乐` 🏆 First Place | 100 |
| [**Quakey**](https://devpost.com/software/quakey) | A vision-first autonomous robot for where lidar fails. | Robotech 2026 | `工具与制造` 🏆 1st Place Autonomous Track | 82 |
| [**Human Operator**](https://devpost.com/software/human-operator) | A Human Augmentation Tool for On-Body Intelligence with EMS. | HARD MODE: Hardware x AI Hackathon | `工具与制造` 🏆 LEARN - Track | 68 |
| [**PipeX**](https://devpost.com/software/pipex) | PipeX is a pipe crawling robot that automates risky pipe inspection and maintenance. Pipe… | RoboTech 2025 | `工具与制造` `安全应急` 🏆 Advanced Track - Winner | 66 |
| [**PlantPartner**](https://devpost.com/software/plantpartner) | An inexpensive robotic assistant that monitors plants and diagnoses issues using AI techn… | MakeNJIT Hardware Hackathon 2024 | `农业食物` `工具与制造` 🏆 First Place | 66 |

</details>

---

## 🏁 赛事覆盖

| 赛事 | 类型 | 地区 | 收录届数 | 作品 | 获奖 |
| :-- | :-- | :-- | --: | --: | --: |
| [Hackaday 大奖与主题赛](https://hackaday.io/prize) | 长周期大奖 | Global | 13 | 627 | 0 |
| [MakeUofT](https://makeuoft.ca/) | 造物赛 | North America | 8 | 525 | 81 |
| [MakeMIT](https://makemit.org/) | 造物赛 | North America | 9 | 286 | 91 |
| [其他硬件/机器人黑客松](https://devpost.com/hackathons) | 造物赛 | Global | 15 | 247 | 59 |
| [IDEA Hacks（UCLA）](https://ideahacks.la/) | 造物赛 | North America | 8 | 227 | 49 |
| [Build18（CMU）](https://www.build18.org/garage) | 造物节 | North America | 10 | 220 | 7 |
| [MakeHarvard](https://makeharvard.io/) | 造物赛 | North America | 4 | 218 | 43 |
| [UTRA Hacks（多伦多机器人）](https://utrahacks.ca/) | 造物赛 | North America | 4 | 205 | 36 |
| [TreeHacks（斯坦福）](https://www.treehacks.com/) | 综合黑客松 ·硬件赛道 | North America | 11 | 130 | 39 |
| [Hack the North](https://hackthenorth.com/) | 综合黑客松 ·硬件赛道 | North America | 11 | 123 | 32 |
| [RoboTech](https://robotech.devpost.com/) | 造物赛 | North America | 4 | 114 | 30 |
| [MakeNJIT](https://makenjit.org/) | 造物赛 | North America | 4 | 102 | 12 |
| [Cal Hacks](https://calhacks.io/) | 综合黑客松 ·硬件赛道 | North America | 8 | 101 | 22 |
| [PennApps](https://pennapps.com/) | 综合黑客松 ·硬件赛道 | North America | 14 | 72 | 27 |
| [AdventureX](https://www.adventure-x.cn/) | 综合黑客松 ·硬件赛道 | China | 4 | 70 | 40 |
| [MakeCU（哥伦比亚）](https://makecu.org/) | 造物赛 | North America | 4 | 70 | 36 |
| [HackPrinceton](https://www.hackprinceton.com/) | 综合黑客松 ·硬件赛道 | North America | 16 | 63 | 21 |
| [BuildGT（佐治亚理工）](https://hack.gt/) | 造物赛 | North America | 2 | 63 | 9 |
| [HackGT](https://hack.gt/) | 综合黑客松 ·硬件赛道 | North America | 12 | 63 | 5 |
| [MHacks](https://mhacks.org/) | 综合黑客松 ·硬件赛道 | North America | 12 | 46 | 15 |
| [HackIllinois](https://hackillinois.org/) | 综合黑客松 ·硬件赛道 | North America | 8 | 39 | 6 |
| [MIT Reality Hack](https://www.realityhackatmit.com/) | XR 黑客松 ·硬件赛道 | North America | 8 | 36 | 12 |
| [HackHarvard](https://hackharvard.io/) | 综合黑客松 ·硬件赛道 | North America | 10 | 30 | 7 |
| [TAMUmake（德州农工）](https://tamumake.com/) | 造物赛 | North America | 2 | 27 | 11 |
| [UGAHacks Makeathon](https://ugahacks.com/) | 造物赛 | North America | 2 | 26 | 6 |
| [DeltaHacks](https://deltahacks.com/) | 综合黑客松 ·硬件赛道 | North America | 9 | 25 | 5 |
| [HackMIT](https://hackmit.org/) | 综合黑客松 ·硬件赛道 | North America | 5 | 23 | 11 |
| [IEEE UofT Hardware Hack](https://hardwarehack.ca/) | 造物赛 | North America | 1 | 21 | 4 |
| [nwHacks](https://nwhacks.io/) | 综合黑客松 ·硬件赛道 | North America | 9 | 18 | 6 |
| [Hacktech（加州理工）](https://hacktech.io/) | 综合黑客松 ·硬件赛道 | North America | 9 | 18 | 5 |
| [BoilerMake](https://boilermake.org/) | 综合黑客松 ·硬件赛道 | North America | 7 | 17 | 6 |
| [MakeUC（辛辛那提）](https://makeuc.io/) | 综合黑客松 ·硬件赛道 | North America | 6 | 17 | 8 |
| [uOttaHack](https://uottahack.ca/) | 综合黑客松 ·硬件赛道 | North America | 5 | 15 | 5 |
| [LA Hacks](https://lahacks.com/) | 综合黑客松 ·硬件赛道 | North America | 2 | 12 | 6 |
| [Hack Western](https://hackwestern.com/) | 综合黑客松 ·硬件赛道 | North America | 5 | 12 | 2 |
| [地瓜机器人黑客松](https://hackathon.d-robotics.cc/) | 综合黑客松 | China | — | 3 | 0 |

新一届比赛只要上了 Devpost，就会被**自动发现并收录**；新增一个赛事系列只需在 [`config/events.toml`](config/events.toml) 里加一段。

---

## 🆕 本周新增

_首轮全量收录完成；之后每次更新会在这里列出最近 7 天新收录的高分作品。_

---

## ⚙️ 它是怎么自动更新的

```mermaid
flowchart LR
  A["⏰ GitHub Actions<br/>每 6 小时"] --> B["抓取<br/>Devpost · GitHub · Build18<br/>Hackster · 立创 · AdventureX"]
  B --> C["合并去重<br/>(同一仓库只留一条)"]
  C --> D["硬件判定 + 6 维分类<br/>taxonomy.toml"]
  D --> E["有意思指数<br/>+ 编辑精选"]
  E --> F["data/projects.json<br/>README · RSS"]
  F --> G["🌐 Vercel<br/>可视化作品库"]
```

- **增量抓取**：详情页按作品缓存（`data/cache/`），每次只请求新作品；单个来源失败时保留上次的数据，不会清空。
- **全站新作流**：除了固定赛事，还会按时间倒序扫描 Devpost 上所有含 Arduino / ESP32 / 树莓派 / 机器人 等标签的新作品，获奖或有点赞的会被收录。
- **本地运行**：`python -m pipeline.run`（零依赖，Python ≥ 3.11）；只改了分类规则就跑 `python -m pipeline.run --reclassify`；打开网页：`python -m http.server -d site`。

## 🤝 参与

| 你想做什么 | 怎么做 |
| :-- | :-- |
| 推荐一个作品 | 编辑 [`config/picks.toml`](config/picks.toml) |
| 新增一个赛事 / 数据源 | 编辑 [`config/events.toml`](config/events.toml)，或在 `pipeline/sources/` 加一个采集器 |
| 改进分类 | 编辑 [`config/taxonomy.toml`](config/taxonomy.toml) 后 `--reclassify` 看效果 |
| 让 AI Agent 接力维护 | 把 [`AGENTS.md`](AGENTS.md) 发给它 |

<div align="center"><sub>本页面由 <code>pipeline/render.py</code> 自动生成 · 最后更新 2026-11-19 · 作品版权归各自作者所有，本仓库仅做索引</sub></div>
