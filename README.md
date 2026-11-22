<div align="center">

# 🛠️ Hardware Hackathon Works · 硬件黑客松作品雷达

**自动收录全球硬件 / 机器人 / 具身交互赛事里最有意思的作品**
MakeMIT · Build18 · MakeUofT · Reality Hack · TreeHacks · Hackaday · Hackster · 立创开源 · AdventureX …

[![Works](https://img.shields.io/badge/作品-4156-38BDF8?style=flat-square)](https://hardware-hackathon-works.vercel.app/)
[![Winners](https://img.shields.io/badge/获奖作品-953-F59E0B?style=flat-square)](https://hardware-hackathon-works.vercel.app/)
[![Events](https://img.shields.io/badge/赛事系列-36%20·%20263%20届-10B981?style=flat-square)](#-赛事覆盖)
[![New](https://img.shields.io/badge/本周新增-首轮-EC4899?style=flat-square)](#-本周新增)
[![Updated](https://img.shields.io/badge/自动更新-2026--11--22-6366F1?style=flat-square)](.github/workflows/update.yml)

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
| **场景** Domain | 🩺健康医疗 503 · 🌱环境可持续 482 · 🎮游戏娱乐 468 · 🏠家居生活 393 · 🎓教育学习 333 · 🚲出行交通 313 |
| **形态** Form factor | 📟桌面小装置 817 · ⌚可穿戴 394 · 🪑智能物件/家具 266 · ⚙️制造机器/机构 250 · 🥽XR/空间计算 182 · 🤖移动机器人 175 |
| **交互** Interaction | 📡环境感知/自主 983 · 👋视觉/手势 664 · 💡光与显示 614 · 🗣️语音对话 361 · 🎛️实体操控 207 · 🧠生理信号 143 |
| **平台** Platform | ♾️Arduino 1612 · 🍓Raspberry Pi 603 · 📶ESP32/ESP8266 539 · 🔧其他 MCU 83 · 🟩NVIDIA Jetson 61 · 🛰️ROS 51 |
| **智能** AI capability | 👁️计算机视觉 555 · ✨大模型/生成式 529 · 📈机器学习 340 · 🎙️语音 AI 196 · 🦿机器人学习 51 · 🔋端侧 ML 31 |
| **工艺** Fabrication | 🧱3D 打印 433 · 📐CAD 建模 352 · 🔦激光切割 205 · 🧵织物/手工 49 · 🟢PCB 设计 33 |

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

<details><summary><b>🩺 健康医疗 · Health & Medical</b> — 503 件</summary>

| 作品 | 一句话 | 赛事 | 标签 | 指数 |
| :-- | :-- | :-- | :-- | --: |
| [**Helping Hand**](https://devpost.com/software/helping-hand-y7z69j) | A smart glove that utilizes data from various sensors to accurately track a hand's positi… | MakeUofT 2021 | `健康医疗` 🏆 3rd Place Overall | 86 |
| [**Anti Anti-Masker Mask**](https://devpost.com/software/anti-anti-masker-mask) | Taking social distancing to the next level | MakeUofT 2022 | `健康医疗` `社交情感` 🏆 2nd Place Overall | 85 |
| [**Silent Voice**](https://devpost.com/software/silent-voice-s1f74p) | Cancer can take your voice, but we can give it back. | Cal Hacks 13.0 | `健康医疗` 🏆 Cal Hacks Second Overall | 85 |
| [**RxID**](https://devpost.com/software/rxid) | Managing medication is as simple as a tap. Our RFID health bracelet securely stores medic… | MakeUofT 2025 | `健康医疗` 🏆 1st Place Prize | 82 |
| [**Lucid**](https://devpost.com/software/lucid-k078qt) | Brain screening made accessible | HackPrinceton Fall '26 | `健康医疗` `无障碍辅助` 🏆 [Justin Bojarski] Best Physical AI Hack | 80 |

</details>

<details><summary><b>♿ 无障碍辅助 · Accessibility</b> — 297 件</summary>

| 作品 | 一句话 | 赛事 | 标签 | 指数 |
| :-- | :-- | :-- | :-- | --: |
| [**Shepherd**](https://devpost.com/software/raising-cane) | A smart cane that guides indoor and outdoor navigation for blind people, costing ~1/20 of… | TreeHacks 2026 | `无障碍辅助` `出行交通` 🏆 Treehacks Grand Prize (1st) | 88 |
| [**NeuroPilot: Brainwave Computer Control**](https://devpost.com/software/mindcontrolpc-control-computer-with-brainwaves) | Control your computer with just your mind. | TreeHacks 2025 | `无障碍辅助` 🏆 Scrapybara: Capy Prize (Japan offsite + $1k credits + Scrapybara Pro 6 months [1st] & $1k credits + Scrapybara Pro 3  months [2nd] & $100 credits + Scrapybara Pro 1 month [3rd]) | 86 |
| [**Braille-iant**](https://devpost.com/software/braille-iant-o1gcya) | Let's make something Braille-iant. | TAMUmake 2020 | `无障碍辅助` 🏆 1st Place Winner | 83 |
| [**BrainChair**](https://devpost.com/software/brainchair) | Brain-controlled wheelchair | MakeUofT 2022 | `无障碍辅助` 🏆 1st Place Overall | 81 |
| [**VIGIL: Assistive Eyewear with an Autonomous Aerial Scout**](https://devpost.com/software/vigil-assistive-eeywear-with-an-autonomous-aerial-scout) | VIGIL reimagines assistive eyewear via an autonomous aerial scout, extending perception b… | HackGT 13: Seaside Market | `无障碍辅助` `工具与制造` 🏆 Best Overall - 3rd Place | 81 |

</details>

<details><summary><b>🌱 环境可持续 · Sustainability</b> — 482 件</summary>

| 作品 | 一句话 | 赛事 | 标签 | 指数 |
| :-- | :-- | :-- | :-- | --: |
| [**AutoDump: Autonomous Self-Emptying Trash Rover**](https://devpost.com/software/autodump-autonomous-self-emptying-trash-rover) | A Raspberry Pi rover that finds full bins, docks, and auto-dumps into a central can using… | MakeCU | `环境可持续` `家居生活` 🏆 3rd Place Overall | 84 |
| [**DeepTrash**](https://devpost.com/software/deeptrash) | Reinventing the trash can. We use machine learning to filter out disposed items automatic… | MakeHarvard 2019 | `环境可持续` `教育学习` 🏆 Best Overall (1st, 2nd, 3rd prizes) | 81 |
| [**SmartBar**](https://devpost.com/software/smartbar-nwuxg9) | A smart power bar that monitors, controls, and reduces power consumption to connected dev… | MakeUofT 2020 | `环境可持续` `家居生活` 🏆 2nd Place Overall | 76 |
| [**Twin**](https://devpost.com/software/twin-pywkb4) | Lost? Panicking? Heart racing?Twin’s got your back—and your head. Built into a hard hat,… | MakeUofT 2026 | `环境可持续` `健康医疗` 🏆 1st Place: Meta Glasses | 76 |
| [**PUSHPA - Pyro UAV System for High-risk Patrol and Alerting**](https://devpost.com/software/pushpa-pyro-uav-system-for-high-risk-patrol-and-alerting) | PUSHPA gives firefighters eyes on the ground and in the air. Smart glasses steer drones f… | TreeHacks 2025 | `环境可持续` `安全应急` 🏆 Edge AI Prize: Operator Optimization Champion ($5k Cash) | 75 |

</details>

<details><summary><b>🌾 农业食物 · Food & Agriculture</b> — 250 件</summary>

| 作品 | 一句话 | 赛事 | 标签 | 指数 |
| :-- | :-- | :-- | :-- | --: |
| [**Smart Sprout**](https://devpost.com/software/smart-sprout-ponbhq) | Smart Sprout uses real-time soil moisture data and an Arduino-powered motor to precisely… | Hack the North 2023 | `农业食物` `健康医疗` 🏆 Best Hack Built on Replit | 76 |
| [**Vibrace**](https://devpost.com/software/ergonomic-arm-brace) | An astronomical solution to physical therapy. | MakeHarvard 2019 | `健康医疗` `农业食物` 🏆 Best Overall (1st, 2nd, 3rd prizes) | 74 |
| [**AvocadoBro**](https://devpost.com/software/glycemic-index-tracker) | An essential grocery shopping companion | Longhorn Robotics 2nd Annual Hackathon | `农业食物` `社交情感` 🏆 1st Place | 73 |
| [**OmNom**](https://devpost.com/software/omnom-hg16v3) | OmNom is your late night food savior, autonomously navigating a variety of outdoor and in… | TreeHacks 2025 | `环境可持续` `农业食物` 🏆 Most Creative Hack (Pioneer DJ DDJ-FLX4 Pack per team member) | 72 |
| [**Safe Sphere**](https://devpost.com/software/safe-sphere) | An all-in-one IoT device which help people to keep their home safe, calculate the number… | Hardware Hackfest | `农业食物` `安全应急` 🏆 Third Overall | 72 |

</details>

<details><summary><b>🏠 家居生活 · Home & Everyday</b> — 393 件</summary>

| 作品 | 一句话 | 赛事 | 标签 | 指数 |
| :-- | :-- | :-- | :-- | --: |
| [**AutoDump: Autonomous Self-Emptying Trash Rover**](https://devpost.com/software/autodump-autonomous-self-emptying-trash-rover) | A Raspberry Pi rover that finds full bins, docks, and auto-dumps into a central can using… | MakeCU | `环境可持续` `家居生活` 🏆 3rd Place Overall | 84 |
| [**Kafa - Thermostat Enhancer**](https://devpost.com/software/kafa-thermostat-enhancer) | Kafa is a plug and play thermostat enhancer which brings new life to your current hardwar… | MakeUofT 2021 | `家居生活` `游戏娱乐` 🏆 1st Place Overall | 79 |
| [**FEEL — The room, in your palm**](https://devpost.com/software/feel-the-room-in-your-palm) | A LiDAR iPhone and a 24-pin palm puck that turn the room into touch. Feel what’s ahead an… | HackHarvard2026: Hack to the Moon | `家居生活` `出行交通` 🏆 First Place Overall | 78 |
| [**ROOMBAlling**](https://devpost.com/software/roomballing) | The SUCKIEST game of bowling known to man. | HackGT presents: BuildGT 2 | `社交情感` `家居生活` 🏆 1st Place | 76 |
| [**SmartBar**](https://devpost.com/software/smartbar-nwuxg9) | A smart power bar that monitors, controls, and reduces power consumption to connected dev… | MakeUofT 2020 | `环境可持续` `家居生活` 🏆 2nd Place Overall | 76 |

</details>

<details><summary><b>⏱️ 效率与自律 · Productivity & Habits</b> — 219 件</summary>

| 作品 | 一句话 | 赛事 | 标签 | 指数 |
| :-- | :-- | :-- | :-- | --: |
| [**RoboPill**](https://devpost.com/software/robopill-ufrcd4) | Dispensing Made Easy | MAKECU | `健康医疗` `效率与自律` 🏆 2nd Overall | 79 |
| [**BrickBots**](https://devpost.com/software/brickblock) | LEGOs for Robotics. | Cal Hacks 13.0 | `游戏娱乐` `效率与自律` 🏆 [Apify] 1st Customer Award | 78 |
| [**Desk Bot Companion**](https://devpost.com/software/desk-bot-companion) | A Robot that dances and guides with your schedule to cheer you up all day. | Hardware Hackfest | `效率与自律` `社交情感` 🏆 First Overall | 76 |
| [**Napkn**](https://devpost.com/software/napkn-kavgmw) | Easily reserve tables, analyze dining/study hall traffic, and optimize your eating and st… | IDEA Hacks 2020 | `效率与自律` `出行交通` 🏆 IDEA Hacks 1st Place Grand Prize | 76 |
| [**LumiGUI**](https://devpost.com/software/lumigui) | MHacks #1. A more inclusive, contact-free experience for all form users. | MHacks 15 | `健康医疗` `效率与自律` 🏆 1st Place | 71 |

</details>

<details><summary><b>🎓 教育学习 · Education</b> — 333 件</summary>

| 作品 | 一句话 | 赛事 | 标签 | 指数 |
| :-- | :-- | :-- | :-- | --: |
| [**DeepTrash**](https://devpost.com/software/deeptrash) | Reinventing the trash can. We use machine learning to filter out disposed items automatic… | MakeHarvard 2019 | `环境可持续` `教育学习` 🏆 Best Overall (1st, 2nd, 3rd prizes) | 81 |
| [**Portable Braille**](https://devpost.com/software/portable-braille-cdq8v5) | Educational device that encourages young visually impaired people to learn and practice B… | TreeHacks 2025 | `无障碍辅助` `教育学习` 🏆 NVIDIA: Robo Prize (Jetson Dev kit per team member) | 79 |
| [**Quick Mouse**](https://devpost.com/software/quick-mouse) | Quick Mouse turns your phone into a precise wireless mouse. No extra hardware. Open the a… | MakeUC 2025 | `工具与制造` `教育学习` 🏆 First Place | 79 |
| [**LABKickstart**](https://devpost.com/software/labkickstart) | It’s nobody’s fault that modern physics experimentation is broken | IDEA Hacks 2026 | `教育学习` 🏆 1st Place Prize | 76 |
| [**SurgeVue**](https://devpost.com/software/surgikalai) | A multi-model solution specifically designed for professional surgeons and medical studen… | PennApps XXV | `健康医疗` `教育学习` 🏆 Best Overall 3rd | 76 |

</details>

<details><summary><b>🛡️ 安全应急 · Safety & Security</b> — 249 件</summary>

| 作品 | 一句话 | 赛事 | 标签 | 指数 |
| :-- | :-- | :-- | :-- | --: |
| [**Sophi - The Physical Augmentation Walker**](https://devpost.com/software/sophi) | Sophi is an AI-powered walker with an always-on voice agent for Q&A and GPS navigation, p… | Cal Hacks 13.0 | `安全应急` `无障碍辅助` 🏆 Cal Hacks First Overall | 80 |
| [**OpenReality**](https://devpost.com/software/real-eyes-mra8n6) | OpenClaw in the real world! Generate and reason in a 3d map with just your phone! | HackIllinois 2026 | `安全应急` `工具与制造` 🏆 Most Creative | 79 |
| [**ResQme**](https://devpost.com/software/resqme-jq52al) | Connecting lives when the world goes offline. ResQMe is an ESP32-based offline mesh netwo… | HackHarvard 2025: Compile the Decade | `安全应急` 🏆 2nd Best Overall Hack | 79 |
| [**Dispatch**](https://devpost.com/software/dispatch-u7fwrv) | A novel VR locomotion solution to provide accessible immersive training experiences for f… | HackGT 12: Midnight at the Museum | `安全应急` `无障碍辅助` 🏆 Hall of Illusions - 1st Place | 75 |
| [**PUSHPA - Pyro UAV System for High-risk Patrol and Alerting**](https://devpost.com/software/pushpa-pyro-uav-system-for-high-risk-patrol-and-alerting) | PUSHPA gives firefighters eyes on the ground and in the air. Smart glasses steer drones f… | TreeHacks 2025 | `环境可持续` `安全应急` 🏆 Edge AI Prize: Operator Optimization Champion ($5k Cash) | 75 |

</details>

<details><summary><b>🚲 出行交通 · Mobility & Transport</b> — 313 件</summary>

| 作品 | 一句话 | 赛事 | 标签 | 指数 |
| :-- | :-- | :-- | :-- | --: |
| [**Shepherd**](https://devpost.com/software/raising-cane) | A smart cane that guides indoor and outdoor navigation for blind people, costing ~1/20 of… | TreeHacks 2026 | `无障碍辅助` `出行交通` 🏆 Treehacks Grand Prize (1st) | 88 |
| [**FEEL — The room, in your palm**](https://devpost.com/software/feel-the-room-in-your-palm) | A LiDAR iPhone and a 24-pin palm puck that turn the room into touch. Feel what’s ahead an… | HackHarvard2026: Hack to the Moon | `家居生活` `出行交通` 🏆 First Place Overall | 78 |
| [**Napkn**](https://devpost.com/software/napkn-kavgmw) | Easily reserve tables, analyze dining/study hall traffic, and optimize your eating and st… | IDEA Hacks 2020 | `效率与自律` `出行交通` 🏆 IDEA Hacks 1st Place Grand Prize | 76 |
| [**Mirage**](https://devpost.com/software/synsplatt) | Robots and self-driving cars need training data. Mirage synthesizes 3D world-model traini… | TreeHacks 2026 | `出行交通` 🏆 [Modal] Inference Track (Inference Track Grand Prize: $5K in Modal Credits per person, paid visit (flight & hotel) to SF or NY Office with lunch with Modal team,.   Inference Track Runner Up Prize:  $1K in Modal credits, airpods for each team member.) | 75 |
| [**Project Jeremy and DriveCode**](https://devpost.com/software/project-just-coding-destructive-jam-kite-robot-j-c-d-j-k-r) | Our magnificent 2 Wheeled Robot Jeremy will be able to tackle this obstacle course in sev… | UTRA Hacks 2026 | `出行交通` 🏆 UTRA Hacks 2026: 1st Place  - ASUS ROG Zephyrus G16 (2025) | 74 |

</details>

<details><summary><b>🎨 艺术音乐 · Art & Music</b> — 277 件</summary>

| 作品 | 一句话 | 赛事 | 标签 | 指数 |
| :-- | :-- | :-- | :-- | --: |
| [**Cadence**](https://devpost.com/software/cadence-l1axr5) | With Cadence, your hands are the only instrument you need. Wear the glove, move your fing… | MakeMIT x Harvard 2026 | `艺术音乐` 🏆 Infosys Overall Grand Prize | 79 |
| [**flatline**](https://devpost.com/software/flatline-wryife) | play your heart out &lt;3 | HackUMass XIV | `艺术音乐` `游戏娱乐` 🏆 [HACKUMASS] Grand Prize | 76 |
| [**Ludwig**](https://devpost.com/software/ludwig) | A physical robot to play any sheet music you want! | Hack the North 2024 | `艺术音乐` `游戏娱乐` 🏆 Hack the North 2024 Finalists | 74 |
| [**The Meloditron**](https://devpost.com/software/the-melodicon) | The musical abacus loopmaker | MakeHarvard 2020 | `艺术音乐` `教育学习` 🏆 1st Place | 72 |
| [**Lucid Weave**](https://devpost.com/software/lucid-weave) | Lucid Weave is a living spatial manifestation of dreams where gestures sculpt music, melo… | Reality Hack @ MIT 2026 | `艺术音乐` 🏆 Bronze Prize | 69 |

</details>

<details><summary><b>🎮 游戏娱乐 · Games & Fun</b> — 468 件</summary>

| 作品 | 一句话 | 赛事 | 标签 | 指数 |
| :-- | :-- | :-- | :-- | --: |
| [**Unsynthesizer**](https://devpost.com/software/unsynthesizer-2jxeoy) | 不用电子元件、只靠声音的无线键盘：每个键敲出不同频率，电脑靠滤波识别按键 | MakeMIT 2020 | `工具与制造` `游戏娱乐` 🏆 First Place | 100 |
| [**PrimePong**](https://devpost.com/software/primepong) | PrimePong fuses cutting-edge tech with table tennis! Our fully equipped paddle tracks eve… | MakeUofT 2025 | `游戏娱乐` 🏆 3rd Place Overall | 81 |
| [**Kafa - Thermostat Enhancer**](https://devpost.com/software/kafa-thermostat-enhancer) | Kafa is a plug and play thermostat enhancer which brings new life to your current hardwar… | MakeUofT 2021 | `家居生活` `游戏娱乐` 🏆 1st Place Overall | 79 |
| [**POLL: Pong Over Laser Link**](https://devpost.com/software/poll-pong-over-laser-link) | Wireless video gaming. | MAKECU | `游戏娱乐` 🏆 Best Domain.com Name | 79 |
| [**BrickBots**](https://devpost.com/software/brickblock) | LEGOs for Robotics. | Cal Hacks 13.0 | `游戏娱乐` `效率与自律` 🏆 [Apify] 1st Customer Award | 78 |

</details>

<details><summary><b>💞 社交情感 · Social & Emotional</b> — 283 件</summary>

| 作品 | 一句话 | 赛事 | 标签 | 指数 |
| :-- | :-- | :-- | :-- | --: |
| [**Anti Anti-Masker Mask**](https://devpost.com/software/anti-anti-masker-mask) | Taking social distancing to the next level | MakeUofT 2022 | `健康医疗` `社交情感` 🏆 2nd Place Overall | 85 |
| [**Desk Bot Companion**](https://devpost.com/software/desk-bot-companion) | A Robot that dances and guides with your schedule to cheer you up all day. | Hardware Hackfest | `效率与自律` `社交情感` 🏆 First Overall | 76 |
| [**ROOMBAlling**](https://devpost.com/software/roomballing) | The SUCKIEST game of bowling known to man. | HackGT presents: BuildGT 2 | `社交情感` `家居生活` 🏆 1st Place | 76 |
| [**AlexaGo**](https://devpost.com/software/alexago) | Moving voice-assistive technology forward by putting it on wheels. | MakeHarvard 2018 | `无障碍辅助` `社交情感` 🏆 Best Overall | 75 |
| [**AvocadoBro**](https://devpost.com/software/glycemic-index-tracker) | An essential grocery shopping companion | Longhorn Robotics 2nd Annual Hackathon | `农业食物` `社交情感` 🏆 1st Place | 73 |

</details>

<details><summary><b>🛠️ 工具与制造 · Tools & Industry</b> — 299 件</summary>

| 作品 | 一句话 | 赛事 | 标签 | 指数 |
| :-- | :-- | :-- | :-- | --: |
| [**Unsynthesizer**](https://devpost.com/software/unsynthesizer-2jxeoy) | 不用电子元件、只靠声音的无线键盘：每个键敲出不同频率，电脑靠滤波识别按键 | MakeMIT 2020 | `工具与制造` `游戏娱乐` 🏆 First Place | 100 |
| [**Quakey**](https://devpost.com/software/quakey) | A vision-first autonomous robot for where lidar fails. | Robotech 2026 | `工具与制造` 🏆 1st Place Autonomous Track | 82 |
| [**VIGIL: Assistive Eyewear with an Autonomous Aerial Scout**](https://devpost.com/software/vigil-assistive-eeywear-with-an-autonomous-aerial-scout) | VIGIL reimagines assistive eyewear via an autonomous aerial scout, extending perception b… | HackGT 13: Seaside Market | `无障碍辅助` `工具与制造` 🏆 Best Overall - 3rd Place | 81 |
| [**OpenReality**](https://devpost.com/software/real-eyes-mra8n6) | OpenClaw in the real world! Generate and reason in a 3d map with just your phone! | HackIllinois 2026 | `安全应急` `工具与制造` 🏆 Most Creative | 79 |
| [**Quick Mouse**](https://devpost.com/software/quick-mouse) | Quick Mouse turns your phone into a precise wireless mouse. No extra hardware. Open the a… | MakeUC 2025 | `工具与制造` `教育学习` 🏆 First Place | 79 |

</details>

---

## 🏁 赛事覆盖

| 赛事 | 类型 | 地区 | 收录届数 | 作品 | 获奖 |
| :-- | :-- | :-- | --: | --: | --: |
| [Hackaday 大奖与主题赛](https://hackaday.io/prize) | 长周期大奖 | Global | 13 | 669 | 0 |
| [MakeUofT](https://makeuoft.ca/) | 造物赛 | North America | 8 | 514 | 81 |
| [MakeMIT](https://makemit.org/) | 造物赛 | North America | 9 | 285 | 91 |
| [其他硬件/机器人黑客松](https://devpost.com/hackathons) | 造物赛 | Global | 15 | 247 | 59 |
| [IDEA Hacks（UCLA）](https://ideahacks.la/) | 造物赛 | North America | 8 | 227 | 49 |
| [Build18（CMU）](https://www.build18.org/garage) | 造物节 | North America | 10 | 220 | 7 |
| [MakeHarvard](https://makeharvard.io/) | 造物赛 | North America | 4 | 215 | 43 |
| [UTRA Hacks（多伦多机器人）](https://utrahacks.ca/) | 造物赛 | North America | 4 | 205 | 36 |
| [Hack the North](https://hackthenorth.com/) | 综合黑客松 ·硬件赛道 | North America | 11 | 155 | 62 |
| [TreeHacks（斯坦福）](https://www.treehacks.com/) | 综合黑客松 ·硬件赛道 | North America | 11 | 142 | 59 |
| [Cal Hacks](https://calhacks.io/) | 综合黑客松 ·硬件赛道 | North America | 8 | 124 | 45 |
| [RoboTech](https://robotech.devpost.com/) | 造物赛 | North America | 4 | 114 | 30 |
| [MakeNJIT](https://makenjit.org/) | 造物赛 | North America | 4 | 102 | 12 |
| [PennApps](https://pennapps.com/) | 综合黑客松 ·硬件赛道 | North America | 14 | 79 | 33 |
| [HackPrinceton](https://www.hackprinceton.com/) | 综合黑客松 ·硬件赛道 | North America | 16 | 78 | 37 |
| [HackGT](https://hack.gt/) | 综合黑客松 ·硬件赛道 | North America | 12 | 76 | 18 |
| [AdventureX](https://www.adventure-x.cn/) | 综合黑客松 ·硬件赛道 | China | 4 | 70 | 40 |
| [MakeCU（哥伦比亚）](https://makecu.org/) | 造物赛 | North America | 4 | 70 | 36 |
| [BuildGT（佐治亚理工）](https://hack.gt/) | 造物赛 | North America | 2 | 63 | 9 |
| [MHacks](https://mhacks.org/) | 综合黑客松 ·硬件赛道 | North America | 13 | 57 | 26 |
| [MIT Reality Hack](https://www.realityhackatmit.com/) | XR 黑客松 ·硬件赛道 | North America | 8 | 55 | 34 |
| [HackIllinois](https://hackillinois.org/) | 综合黑客松 ·硬件赛道 | North America | 8 | 44 | 10 |
| [HackHarvard](https://hackharvard.io/) | 综合黑客松 ·硬件赛道 | North America | 10 | 36 | 13 |
| [DeltaHacks](https://deltahacks.com/) | 综合黑客松 ·硬件赛道 | North America | 9 | 34 | 13 |
| [nwHacks](https://nwhacks.io/) | 综合黑客松 ·硬件赛道 | North America | 9 | 31 | 19 |
| [TAMUmake（德州农工）](https://tamumake.com/) | 造物赛 | North America | 2 | 27 | 11 |
| [UGAHacks Makeathon](https://ugahacks.com/) | 造物赛 | North America | 2 | 26 | 6 |
| [HackMIT](https://hackmit.org/) | 综合黑客松 ·硬件赛道 | North America | 5 | 24 | 12 |
| [MakeUC（辛辛那提）](https://makeuc.io/) | 综合黑客松 ·硬件赛道 | North America | 6 | 22 | 13 |
| [IEEE UofT Hardware Hack](https://hardwarehack.ca/) | 造物赛 | North America | 1 | 21 | 4 |
| [uOttaHack](https://uottahack.ca/) | 综合黑客松 ·硬件赛道 | North America | 5 | 21 | 11 |
| [Hacktech（加州理工）](https://hacktech.io/) | 综合黑客松 ·硬件赛道 | North America | 10 | 19 | 6 |
| [BoilerMake](https://boilermake.org/) | 综合黑客松 ·硬件赛道 | North America | 7 | 18 | 7 |
| [LA Hacks](https://lahacks.com/) | 综合黑客松 ·硬件赛道 | North America | 2 | 15 | 9 |
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

<div align="center"><sub>本页面由 <code>pipeline/render.py</code> 自动生成 · 最后更新 2026-11-22 · 作品版权归各自作者所有，本仓库仅做索引</sub></div>
