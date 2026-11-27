<div align="center">

# 🛠️ Hardware Hackathon Works · 硬件黑客松作品雷达

**自动收录全球硬件 / 机器人 / 具身交互赛事里最有意思的作品**
MakeMIT · Build18 · MakeUofT · Reality Hack · HARD MODE · TreeHacks · Hackaday · Hackster · 立创开源 · AdventureX …

[![Works](https://img.shields.io/badge/作品-4478-38BDF8?style=flat-square)](https://hardware-hackathon-works.vercel.app/)
[![Winners](https://img.shields.io/badge/获奖作品-1268-F59E0B?style=flat-square)](https://hardware-hackathon-works.vercel.app/)
[![Events](https://img.shields.io/badge/赛事系列-37%20·%20277%20届-10B981?style=flat-square)](#-赛事覆盖)
[![New](https://img.shields.io/badge/本周新增-首轮-EC4899?style=flat-square)](#-本周新增)
[![Updated](https://img.shields.io/badge/自动更新-2026--11--27-6366F1?style=flat-square)](.github/workflows/update.yml)

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
| **场景** Domain | 🩺健康医疗 574 · 🎮游戏娱乐 529 · 🌱环境可持续 521 · 🏠家居生活 439 · 🎓教育学习 390 · 🚲出行交通 350 |
| **形态** Form factor | 📟桌面小装置 885 · ⌚可穿戴 416 · 🪑智能物件/家具 284 · ⚙️制造机器/机构 273 · 🥽XR/空间计算 226 · 🤖移动机器人 185 |
| **交互** Interaction | 📡环境感知/自主 1083 · 👋视觉/手势 797 · 💡光与显示 678 · 🗣️语音对话 419 · 🎛️实体操控 235 · 🧠生理信号 162 |
| **平台** Platform | ♾️Arduino 1926 · 🍓Raspberry Pi 781 · 📶ESP32/ESP8266 565 · 🔧其他 MCU 112 · 🟩NVIDIA Jetson 68 · 🛰️ROS 65 |
| **智能** AI capability | 👁️计算机视觉 655 · ✨大模型/生成式 536 · 📈机器学习 430 · 🎙️语音 AI 219 · 🦿机器人学习 53 · 🔋端侧 ML 36 |
| **工艺** Fabrication | 🧱3D 打印 465 · 📐CAD 建模 396 · 🔦激光切割 234 · 🧵织物/手工 59 · 🟢PCB 设计 36 |

### 「有意思指数」怎么算？（0–100）

`获奖等级（一等奖 38 / 赛道奖 26 / 赞助奖 16）` + `点赞数（对数）` + `GitHub Star（对数）` + `有演示视频 / 开源仓库 / 实拍图` + `文档完整度` + `硬件深度` + `纯硬件赛事加成` + `编辑精选 22`。
它不代表作品好坏，只用来把「最值得先看的」排在前面。公式见 [`pipeline/classify.py`](pipeline/classify.py)。

---

## ⭐ 编辑精选

| 作品 | 一句话 | 赛事 | 标签 | 指数 |
| :-- | :-- | :-- | :-- | --: |
| [**Unsynthesizer**](https://devpost.com/software/unsynthesizer-2jxeoy) | 不用电子元件、只靠声音的无线键盘：每个键敲出不同频率，电脑靠滤波识别按键 | MakeMIT 2020 | `工具与制造` `游戏娱乐` 🏆 First Place | 100 |
| [**Dreaming Objects**](https://devpost.com/software/living-room-dreaming-objects) | 台灯、收音机、镜子、篮子四件家居物件各有一个 AI 代理，会动、会说话，由中控调度互相配合 | HARD MODE: Hardware x AI Hackathon | `家居生活` 🏆 Grand Prize (E14 Fund) | 98 |
| [**Human Operator**](https://devpost.com/software/human-operator) | AI 通过电肌肉刺激（EMS）直接驱动佩戴者的手指和手腕：看第一人称画面、听语音指令，替你挥手、弹旋律、比 OK | HARD MODE: Hardware x AI Hackathon | `工具与制造` 🏆 LEARN - Track | 90 |
| [**Scribblr**](https://devpost.com/software/scribblr-0bxzq4) | 听课 → Gemini 提炼重点 → 单笔画 G-code → 机械手拿真粉笔写在黑板上 | MakeMIT x Harvard 2026 | `教育学习` 🏆 Seed Studio Interactive Signage | 74 |
| [**Whackathon**](https://devpost.com/software/whackathon-w0e27o) | 检测到你驼背成『虾』就立刻物理惩罚的椅子 | MakeMIT x Harvard 2026 | `健康医疗` `效率与自律` 🏆 [MLH] Best Use of ElevenLabs | 62 |
| [**Bless You Polar Bear**](https://github.com/NaemBi-Bap-MAKE-MIT-2026-Team) | 独居异乡打喷嚏没人说『Bless you』？北极熊玩偶用本地小模型听到喷嚏并回应关怀 | MakeMIT x Harvard 2026 | `社交情感` 🏆 Sustainability — 3rd Place | 54 |
| [**Locky**](https://github.com/Vishvenugopal/Locky-MakeMIT) | 把手机锁进会自己躲到你视线死角的小车，戒手机的『躲猫猫』 | MakeMIT x Harvard 2026 | `出行交通` `家居生活`  | 44 |
| [**A.L.I.C.E. MedDispenser**](https://github.com/preespp/MakeMIT_2026_Team7) | Jetson 本地人脸识别 + ESP32 出药的分药终端，LLM 只做可选建议并带本地降级 | MakeMIT x Harvard 2026 | `健康医疗`  | 40 |
| [**Auto-Focus Glasses**](https://github.com/laoeked1111/plase-read-instructions) | 双手占满时用语音让眼镜用丝杆物理变焦，给外科医生和电工的『放大镜』 | MakeMIT x Harvard 2026 | `效率与自律`  | 39 |

> 想推荐作品？在 [`config/picks.toml`](config/picks.toml) 里加几行（链接 + 一句话 + 点评）提个 PR 即可。

---

## 🗂️ 按场景浏览（每类 Top 5）

<details><summary><b>🩺 健康医疗 · Health & Medical</b> — 574 件</summary>

| 作品 | 一句话 | 赛事 | 标签 | 指数 |
| :-- | :-- | :-- | :-- | --: |
| [**Helping Hand**](https://devpost.com/software/helping-hand-y7z69j) | A smart glove that utilizes data from various sensors to accurately track a hand's positi… | MakeUofT 2021 | `健康医疗` 🏆 3rd Place Overall | 86 |
| [**Anti Anti-Masker Mask**](https://devpost.com/software/anti-anti-masker-mask) | Taking social distancing to the next level | MakeUofT 2022 | `健康医疗` `社交情感` 🏆 2nd Place Overall | 85 |
| [**Silent Voice**](https://devpost.com/software/silent-voice-s1f74p) | Cancer can take your voice, but we can give it back. | Cal Hacks 13.0 | `健康医疗` 🏆 Cal Hacks Second Overall | 85 |
| [**RxID**](https://devpost.com/software/rxid) | Managing medication is as simple as a tap. Our RFID health bracelet securely stores medic… | MakeUofT 2025 | `健康医疗` 🏆 1st Place Prize | 82 |
| [**Lucid**](https://devpost.com/software/lucid-k078qt) | Brain screening made accessible | HackPrinceton Fall '26 | `健康医疗` `无障碍辅助` 🏆 [Justin Bojarski] Best Physical AI Hack | 80 |

</details>

<details><summary><b>♿ 无障碍辅助 · Accessibility</b> — 334 件</summary>

| 作品 | 一句话 | 赛事 | 标签 | 指数 |
| :-- | :-- | :-- | :-- | --: |
| [**Shepherd**](https://devpost.com/software/raising-cane) | A smart cane that guides indoor and outdoor navigation for blind people, costing ~1/20 of… | TreeHacks 2026 | `无障碍辅助` `出行交通` 🏆 Treehacks Grand Prize (1st) | 88 |
| [**NeuroPilot: Brainwave Computer Control**](https://devpost.com/software/mindcontrolpc-control-computer-with-brainwaves) | Control your computer with just your mind. | TreeHacks 2025 | `无障碍辅助` 🏆 Scrapybara: Capy Prize (Japan offsite + $1k credits + Scrapybara Pro 6 months [1st] & $1k credits + Scrapybara Pro 3  months [2nd] & $100 credits + Scrapybara Pro 1 month [3rd]) | 86 |
| [**Braille Printer**](https://devpost.com/software/braille-printer) | A quick, affordable method to print braille. | Hack Western 3 | `无障碍辅助` 🏆 1st Place | 83 |
| [**Braille-iant**](https://devpost.com/software/braille-iant-o1gcya) | Let's make something Braille-iant. | TAMUmake 2020 | `无障碍辅助` 🏆 1st Place Winner | 83 |
| [**BrainChair**](https://devpost.com/software/brainchair) | Brain-controlled wheelchair | MakeUofT 2022 | `无障碍辅助` 🏆 1st Place Overall | 81 |

</details>

<details><summary><b>🌱 环境可持续 · Sustainability</b> — 521 件</summary>

| 作品 | 一句话 | 赛事 | 标签 | 指数 |
| :-- | :-- | :-- | :-- | --: |
| [**AutoDump: Autonomous Self-Emptying Trash Rover**](https://devpost.com/software/autodump-autonomous-self-emptying-trash-rover) | A Raspberry Pi rover that finds full bins, docks, and auto-dumps into a central can using… | MakeCU | `环境可持续` `家居生活` 🏆 3rd Place Overall | 84 |
| [**DeepTrash**](https://devpost.com/software/deeptrash) | Reinventing the trash can. We use machine learning to filter out disposed items automatic… | MakeHarvard 2019 | `环境可持续` `教育学习` 🏆 Best Overall (1st, 2nd, 3rd prizes) | 81 |
| [**SmartBar**](https://devpost.com/software/smartbar-nwuxg9) | A smart power bar that monitors, controls, and reduces power consumption to connected dev… | MakeUofT 2020 | `环境可持续` `家居生活` 🏆 2nd Place Overall | 76 |
| [**Twin**](https://devpost.com/software/twin-pywkb4) | Lost? Panicking? Heart racing?Twin’s got your back—and your head. Built into a hard hat,… | MakeUofT 2026 | `环境可持续` `健康医疗` 🏆 1st Place: Meta Glasses | 76 |
| [**PUSHPA - Pyro UAV System for High-risk Patrol and Alerting**](https://devpost.com/software/pushpa-pyro-uav-system-for-high-risk-patrol-and-alerting) | PUSHPA gives firefighters eyes on the ground and in the air. Smart glasses steer drones f… | TreeHacks 2025 | `环境可持续` `安全应急` 🏆 Edge AI Prize: Operator Optimization Champion ($5k Cash) | 75 |

</details>

<details><summary><b>🌾 农业食物 · Food & Agriculture</b> — 277 件</summary>

| 作品 | 一句话 | 赛事 | 标签 | 指数 |
| :-- | :-- | :-- | :-- | --: |
| [**Peak PerFARMance**](https://devpost.com/software/peak-perfarmance) | Data-driven smart agriculture solution to support small-scale farmers. | Hack Western 7 | `农业食物` 🏆 Fourth Place Overall | 82 |
| [**Smooth.io**](https://devpost.com/software/smooth-io) | What's in your smoothie? With this Alexa-enabled smoothie making experience, keep track o… | HackGT 6 Into the Rabbit Hole | `农业食物` `社交情感` 🏆 Alexa Skills for Students: Build Student-Focused Alexa Skills and Win Prizes and Recognition | 77 |
| [**Smart Sprout**](https://devpost.com/software/smart-sprout-ponbhq) | Smart Sprout uses real-time soil moisture data and an Arduino-powered motor to precisely… | Hack the North 2023 | `农业食物` `健康医疗` 🏆 Best Hack Built on Replit | 76 |
| [**We Are Sus Drones**](https://devpost.com/software/we-are-sus-farms) | Lets get close to fields | HackHarvard 2022: Control, Alt, Create | `环境可持续` `农业食物` 🏆 2nd Best Overall Hack | 75 |
| [**Vibrace**](https://devpost.com/software/ergonomic-arm-brace) | An astronomical solution to physical therapy. | MakeHarvard 2019 | `健康医疗` `农业食物` 🏆 Best Overall (1st, 2nd, 3rd prizes) | 74 |

</details>

<details><summary><b>🏠 家居生活 · Home & Everyday</b> — 439 件</summary>

| 作品 | 一句话 | 赛事 | 标签 | 指数 |
| :-- | :-- | :-- | :-- | --: |
| [**Dreaming Objects**](https://devpost.com/software/living-room-dreaming-objects) | 台灯、收音机、镜子、篮子四件家居物件各有一个 AI 代理，会动、会说话，由中控调度互相配合 | HARD MODE: Hardware x AI Hackathon | `家居生活` 🏆 Grand Prize (E14 Fund) | 98 |
| [**AutoDump: Autonomous Self-Emptying Trash Rover**](https://devpost.com/software/autodump-autonomous-self-emptying-trash-rover) | A Raspberry Pi rover that finds full bins, docks, and auto-dumps into a central can using… | MakeCU | `环境可持续` `家居生活` 🏆 3rd Place Overall | 84 |
| [**Kafa - Thermostat Enhancer**](https://devpost.com/software/kafa-thermostat-enhancer) | Kafa is a plug and play thermostat enhancer which brings new life to your current hardwar… | MakeUofT 2021 | `家居生活` `游戏娱乐` 🏆 1st Place Overall | 79 |
| [**FEEL — The room, in your palm**](https://devpost.com/software/feel-the-room-in-your-palm) | A LiDAR iPhone and a 24-pin palm puck that turn the room into touch. Feel what’s ahead an… | HackHarvard2026: Hack to the Moon | `家居生活` `出行交通` 🏆 First Place Overall | 78 |
| [**PetAlert**](https://devpost.com/software/doggoalert) | Calling all pet owners: never get out of bed early in the morning again! | Hack Western 9 | `家居生活` 🏆 Third Place Overall | 77 |

</details>

<details><summary><b>⏱️ 效率与自律 · Productivity & Habits</b> — 230 件</summary>

| 作品 | 一句话 | 赛事 | 标签 | 指数 |
| :-- | :-- | :-- | :-- | --: |
| [**RoboPill**](https://devpost.com/software/robopill-ufrcd4) | Dispensing Made Easy | MAKECU | `健康医疗` `效率与自律` 🏆 2nd Overall | 79 |
| [**BrickBots**](https://devpost.com/software/brickblock) | LEGOs for Robotics. | Cal Hacks 13.0 | `游戏娱乐` `效率与自律` 🏆 [Apify] 1st Customer Award | 78 |
| [**Desk Bot Companion**](https://devpost.com/software/desk-bot-companion) | A Robot that dances and guides with your schedule to cheer you up all day. | Hardware Hackfest | `效率与自律` `社交情感` 🏆 First Overall | 76 |
| [**Napkn**](https://devpost.com/software/napkn-kavgmw) | Easily reserve tables, analyze dining/study hall traffic, and optimize your eating and st… | IDEA Hacks 2020 | `效率与自律` `出行交通` 🏆 IDEA Hacks 1st Place Grand Prize | 76 |
| [**LumiGUI**](https://devpost.com/software/lumigui) | MHacks #1. A more inclusive, contact-free experience for all form users. | MHacks 15 | `健康医疗` `效率与自律` 🏆 1st Place | 71 |

</details>

<details><summary><b>🎓 教育学习 · Education</b> — 390 件</summary>

| 作品 | 一句话 | 赛事 | 标签 | 指数 |
| :-- | :-- | :-- | :-- | --: |
| [**DeepTrash**](https://devpost.com/software/deeptrash) | Reinventing the trash can. We use machine learning to filter out disposed items automatic… | MakeHarvard 2019 | `环境可持续` `教育学习` 🏆 Best Overall (1st, 2nd, 3rd prizes) | 81 |
| [**Portable Braille**](https://devpost.com/software/portable-braille-cdq8v5) | Educational device that encourages young visually impaired people to learn and practice B… | TreeHacks 2025 | `无障碍辅助` `教育学习` 🏆 NVIDIA: Robo Prize (Jetson Dev kit per team member) | 79 |
| [**Quick Mouse**](https://devpost.com/software/quick-mouse) | Quick Mouse turns your phone into a precise wireless mouse. No extra hardware. Open the a… | MakeUC 2025 | `工具与制造` `教育学习` 🏆 First Place | 79 |
| [**DronesNet**](https://devpost.com/software/dronesnet) | An urban drone traffic management system that visualizes regional drone activities and in… | MHacks 9 | `出行交通` `教育学习` 🏆 C2's Best Hack for Air Traffic Control | 77 |
| [**LABKickstart**](https://devpost.com/software/labkickstart) | It’s nobody’s fault that modern physics experimentation is broken | IDEA Hacks 2026 | `教育学习` 🏆 1st Place Prize | 76 |

</details>

<details><summary><b>🛡️ 安全应急 · Safety & Security</b> — 285 件</summary>

| 作品 | 一句话 | 赛事 | 标签 | 指数 |
| :-- | :-- | :-- | :-- | --: |
| [**Sophi - The Physical Augmentation Walker**](https://devpost.com/software/sophi) | Sophi is an AI-powered walker with an always-on voice agent for Q&A and GPS navigation, p… | Cal Hacks 13.0 | `安全应急` `无障碍辅助` 🏆 Cal Hacks First Overall | 80 |
| [**OpenReality**](https://devpost.com/software/real-eyes-mra8n6) | OpenClaw in the real world! Generate and reason in a 3d map with just your phone! | HackIllinois 2026 | `安全应急` `工具与制造` 🏆 Most Creative | 79 |
| [**ResQme**](https://devpost.com/software/resqme-jq52al) | Connecting lives when the world goes offline. ResQMe is an ESP32-based offline mesh netwo… | HackHarvard 2025: Compile the Decade | `安全应急` 🏆 2nd Best Overall Hack | 79 |
| [**Dispatch**](https://devpost.com/software/dispatch-u7fwrv) | A novel VR locomotion solution to provide accessible immersive training experiences for f… | HackGT 12: Midnight at the Museum | `安全应急` `无障碍辅助` 🏆 Hall of Illusions - 1st Place | 75 |
| [**PUSHPA - Pyro UAV System for High-risk Patrol and Alerting**](https://devpost.com/software/pushpa-pyro-uav-system-for-high-risk-patrol-and-alerting) | PUSHPA gives firefighters eyes on the ground and in the air. Smart glasses steer drones f… | TreeHacks 2025 | `环境可持续` `安全应急` 🏆 Edge AI Prize: Operator Optimization Champion ($5k Cash) | 75 |

</details>

<details><summary><b>🚲 出行交通 · Mobility & Transport</b> — 350 件</summary>

| 作品 | 一句话 | 赛事 | 标签 | 指数 |
| :-- | :-- | :-- | :-- | --: |
| [**Shepherd**](https://devpost.com/software/raising-cane) | A smart cane that guides indoor and outdoor navigation for blind people, costing ~1/20 of… | TreeHacks 2026 | `无障碍辅助` `出行交通` 🏆 Treehacks Grand Prize (1st) | 88 |
| [**FEEL — The room, in your palm**](https://devpost.com/software/feel-the-room-in-your-palm) | A LiDAR iPhone and a 24-pin palm puck that turn the room into touch. Feel what’s ahead an… | HackHarvard2026: Hack to the Moon | `家居生活` `出行交通` 🏆 First Place Overall | 78 |
| [**OrchestrAI**](https://devpost.com/software/orchestrai) | An improvisational AI that unleashes the creative power of an entire orchestra to music p… | MHacks 8 | `艺术音乐` `出行交通` 🏆 Best Use of Wolfram Technologies | 78 |
| [**DronesNet**](https://devpost.com/software/dronesnet) | An urban drone traffic management system that visualizes regional drone activities and in… | MHacks 9 | `出行交通` `教育学习` 🏆 C2's Best Hack for Air Traffic Control | 77 |
| [**Napkn**](https://devpost.com/software/napkn-kavgmw) | Easily reserve tables, analyze dining/study hall traffic, and optimize your eating and st… | IDEA Hacks 2020 | `效率与自律` `出行交通` 🏆 IDEA Hacks 1st Place Grand Prize | 76 |

</details>

<details><summary><b>🎨 艺术音乐 · Art & Music</b> — 303 件</summary>

| 作品 | 一句话 | 赛事 | 标签 | 指数 |
| :-- | :-- | :-- | :-- | --: |
| [**Cadence**](https://devpost.com/software/cadence-l1axr5) | With Cadence, your hands are the only instrument you need. Wear the glove, move your fing… | MakeMIT x Harvard 2026 | `艺术音乐` 🏆 Infosys Overall Grand Prize | 79 |
| [**OrchestrAI**](https://devpost.com/software/orchestrai) | An improvisational AI that unleashes the creative power of an entire orchestra to music p… | MHacks 8 | `艺术音乐` `出行交通` 🏆 Best Use of Wolfram Technologies | 78 |
| [**flatline**](https://devpost.com/software/flatline-wryife) | play your heart out &lt;3 | HackUMass XIV | `艺术音乐` `游戏娱乐` 🏆 [HACKUMASS] Grand Prize | 76 |
| [**Ludwig**](https://devpost.com/software/ludwig) | A physical robot to play any sheet music you want! | Hack the North 2024 | `艺术音乐` `游戏娱乐` 🏆 Hack the North 2024 Finalists | 74 |
| [**The Meloditron**](https://devpost.com/software/the-melodicon) | The musical abacus loopmaker | MakeHarvard 2020 | `艺术音乐` `教育学习` 🏆 1st Place | 72 |

</details>

<details><summary><b>🎮 游戏娱乐 · Games & Fun</b> — 529 件</summary>

| 作品 | 一句话 | 赛事 | 标签 | 指数 |
| :-- | :-- | :-- | :-- | --: |
| [**Unsynthesizer**](https://devpost.com/software/unsynthesizer-2jxeoy) | 不用电子元件、只靠声音的无线键盘：每个键敲出不同频率，电脑靠滤波识别按键 | MakeMIT 2020 | `工具与制造` `游戏娱乐` 🏆 First Place | 100 |
| [**Speakeasy**](https://devpost.com/software/speakeasy-5wl7z2) | Practice your speech in front of an audience and receive real time feedback on your vocal… | Reality Virtually Hackathon 2017  | `工具与制造` `游戏娱乐` 🏆 Grand Prize in VR | 82 |
| [**PrimePong**](https://devpost.com/software/primepong) | PrimePong fuses cutting-edge tech with table tennis! Our fully equipped paddle tracks eve… | MakeUofT 2025 | `游戏娱乐` 🏆 3rd Place Overall | 81 |
| [**Kafa - Thermostat Enhancer**](https://devpost.com/software/kafa-thermostat-enhancer) | Kafa is a plug and play thermostat enhancer which brings new life to your current hardwar… | MakeUofT 2021 | `家居生活` `游戏娱乐` 🏆 1st Place Overall | 79 |
| [**POLL: Pong Over Laser Link**](https://devpost.com/software/poll-pong-over-laser-link) | Wireless video gaming. | MAKECU | `游戏娱乐` 🏆 Best Domain.com Name | 79 |

</details>

<details><summary><b>💞 社交情感 · Social & Emotional</b> — 311 件</summary>

| 作品 | 一句话 | 赛事 | 标签 | 指数 |
| :-- | :-- | :-- | :-- | --: |
| [**Anti Anti-Masker Mask**](https://devpost.com/software/anti-anti-masker-mask) | Taking social distancing to the next level | MakeUofT 2022 | `健康医疗` `社交情感` 🏆 2nd Place Overall | 85 |
| [**Smooth.io**](https://devpost.com/software/smooth-io) | What's in your smoothie? With this Alexa-enabled smoothie making experience, keep track o… | HackGT 6 Into the Rabbit Hole | `农业食物` `社交情感` 🏆 Alexa Skills for Students: Build Student-Focused Alexa Skills and Win Prizes and Recognition | 77 |
| [**Desk Bot Companion**](https://devpost.com/software/desk-bot-companion) | A Robot that dances and guides with your schedule to cheer you up all day. | Hardware Hackfest | `效率与自律` `社交情感` 🏆 First Overall | 76 |
| [**ROOMBAlling**](https://devpost.com/software/roomballing) | The SUCKIEST game of bowling known to man. | HackGT presents: BuildGT 2 | `社交情感` `家居生活` 🏆 1st Place | 76 |
| [**AlexaGo**](https://devpost.com/software/alexago) | Moving voice-assistive technology forward by putting it on wheels. | MakeHarvard 2018 | `无障碍辅助` `社交情感` 🏆 Best Overall | 75 |

</details>

<details><summary><b>🛠️ 工具与制造 · Tools & Industry</b> — 318 件</summary>

| 作品 | 一句话 | 赛事 | 标签 | 指数 |
| :-- | :-- | :-- | :-- | --: |
| [**Unsynthesizer**](https://devpost.com/software/unsynthesizer-2jxeoy) | 不用电子元件、只靠声音的无线键盘：每个键敲出不同频率，电脑靠滤波识别按键 | MakeMIT 2020 | `工具与制造` `游戏娱乐` 🏆 First Place | 100 |
| [**Human Operator**](https://devpost.com/software/human-operator) | AI 通过电肌肉刺激（EMS）直接驱动佩戴者的手指和手腕：看第一人称画面、听语音指令，替你挥手、弹旋律、比 OK | HARD MODE: Hardware x AI Hackathon | `工具与制造` 🏆 LEARN - Track | 90 |
| [**Quakey**](https://devpost.com/software/quakey) | A vision-first autonomous robot for where lidar fails. | Robotech 2026 | `工具与制造` 🏆 1st Place Autonomous Track | 82 |
| [**Speakeasy**](https://devpost.com/software/speakeasy-5wl7z2) | Practice your speech in front of an audience and receive real time feedback on your vocal… | Reality Virtually Hackathon 2017  | `工具与制造` `游戏娱乐` 🏆 Grand Prize in VR | 82 |
| [**VIGIL: Assistive Eyewear with an Autonomous Aerial Scout**](https://devpost.com/software/vigil-assistive-eeywear-with-an-autonomous-aerial-scout) | VIGIL reimagines assistive eyewear via an autonomous aerial scout, extending perception b… | HackGT 13: Seaside Market | `无障碍辅助` `工具与制造` 🏆 Best Overall - 3rd Place | 81 |

</details>

---

## 🏁 赛事覆盖

| 赛事 | 类型 | 地区 | 收录届数 | 作品 | 获奖 |
| :-- | :-- | :-- | --: | --: | --: |
| [Hackaday 大奖与主题赛](https://hackaday.io/prize) | 长周期大奖 | Global | 13 | 648 | 0 |
| [MakeUofT](https://makeuoft.ca/) | 造物赛 | North America | 8 | 514 | 81 |
| [MakeMIT](https://makemit.org/) | 造物赛 | North America | 9 | 285 | 91 |
| [IDEA Hacks（UCLA）](https://ideahacks.la/) | 造物赛 | North America | 8 | 227 | 49 |
| [其他硬件/机器人黑客松](https://devpost.com/hackathons) | 造物赛 | Global | 14 | 225 | 47 |
| [Build18（CMU）](https://www.build18.org/garage) | 造物节 | North America | 10 | 220 | 7 |
| [MakeHarvard](https://makeharvard.io/) | 造物赛 | North America | 4 | 215 | 43 |
| [UTRA Hacks（多伦多机器人）](https://utrahacks.ca/) | 造物赛 | North America | 4 | 205 | 36 |
| [Hack the North](https://hackthenorth.com/) | 综合黑客松 ·硬件赛道 | North America | 11 | 190 | 92 |
| [TreeHacks（斯坦福）](https://www.treehacks.com/) | 综合黑客松 ·硬件赛道 | North America | 11 | 161 | 83 |
| [Cal Hacks](https://calhacks.io/) | 综合黑客松 ·硬件赛道 | North America | 8 | 130 | 51 |
| [PennApps](https://pennapps.com/) | 综合黑客松 ·硬件赛道 | North America | 14 | 127 | 81 |
| [RoboTech](https://robotech.devpost.com/) | 造物赛 | North America | 4 | 114 | 30 |
| [HackPrinceton](https://www.hackprinceton.com/) | 综合黑客松 ·硬件赛道 | North America | 18 | 111 | 70 |
| [MakeNJIT](https://makenjit.org/) | 造物赛 | North America | 4 | 102 | 12 |
| [HackGT](https://hack.gt/) | 综合黑客松 ·硬件赛道 | North America | 14 | 91 | 33 |
| [MHacks](https://mhacks.org/) | 综合黑客松 ·硬件赛道 | North America | 14 | 77 | 46 |
| [AdventureX](https://www.adventure-x.cn/) | 综合黑客松 ·硬件赛道 | China | 4 | 70 | 40 |
| [MakeCU（哥伦比亚）](https://makecu.org/) | 造物赛 | North America | 4 | 70 | 36 |
| [MIT Reality Hack](https://www.realityhackatmit.com/) | XR 黑客松 ·硬件赛道 | North America | 9 | 66 | 44 |
| [BuildGT（佐治亚理工）](https://hack.gt/) | 造物赛 | North America | 2 | 63 | 9 |
| [HackHarvard](https://hackharvard.io/) | 综合黑客松 ·硬件赛道 | North America | 10 | 54 | 30 |
| [HackIllinois](https://hackillinois.org/) | 综合黑客松 ·硬件赛道 | North America | 8 | 54 | 20 |
| [DeltaHacks](https://deltahacks.com/) | 综合黑客松 ·硬件赛道 | North America | 9 | 54 | 33 |
| [Hack Western](https://hackwestern.com/) | 综合黑客松 ·硬件赛道 | North America | 8 | 51 | 22 |
| [nwHacks](https://nwhacks.io/) | 综合黑客松 ·硬件赛道 | North America | 9 | 46 | 34 |
| [HackMIT](https://hackmit.org/) | 综合黑客松 ·硬件赛道 | North America | 5 | 41 | 29 |
| [Hacktech（加州理工）](https://hacktech.io/) | 综合黑客松 ·硬件赛道 | North America | 12 | 38 | 18 |
| [uOttaHack](https://uottahack.ca/) | 综合黑客松 ·硬件赛道 | North America | 6 | 29 | 19 |
| [BoilerMake](https://boilermake.org/) | 综合黑客松 ·硬件赛道 | North America | 9 | 28 | 17 |
| [TAMUmake（德州农工）](https://tamumake.com/) | 造物赛 | North America | 2 | 27 | 11 |
| [UGAHacks Makeathon](https://ugahacks.com/) | 造物赛 | North America | 2 | 26 | 6 |
| [MakeUC（辛辛那提）](https://makeuc.io/) | 综合黑客松 ·硬件赛道 | North America | 6 | 24 | 15 |
| [HARD MODE（MIT 硬件 × AI 黑客松）](https://hardmode.media.mit.edu/) | 造物赛 | North America | 1 | 23 | 12 |
| [IEEE UofT Hardware Hack](https://hardwarehack.ca/) | 造物赛 | North America | 1 | 21 | 4 |
| [LA Hacks](https://lahacks.com/) | 综合黑客松 ·硬件赛道 | North America | 2 | 15 | 9 |
| [地瓜机器人黑客松](https://hackathon.d-robotics.cc/) | 综合黑客松 | China | — | 5 | 0 |

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

<div align="center"><sub>本页面由 <code>pipeline/render.py</code> 自动生成 · 最后更新 2026-11-27 · 作品版权归各自作者所有，本仓库仅做索引</sub></div>
