
<div align="center">

## AppSec & Web Developer

<img src="./header.svg" width="49%" alt="Header">

<br>

[![Website](https://img.shields.io/badge/lgra.netlify.app-0a0a0a?style=flat-square&logo=netlify&logoColor=white)](https://lgra.netlify.app/)&nbsp;&nbsp;
[![TryHackMe](https://img.shields.io/badge/TryHackMe-0a0a0a?style=flat-square&logo=tryhackme&logoColor=white)](https://tryhackme.com/p/kOaDT)&nbsp;&nbsp;
[![Root-Me](https://img.shields.io/badge/Root--Me-0a0a0a?style=flat-square&logo=rootme&logoColor=white)](https://www.root-me.org/kOaDT)

</div>

<br>


<!-- CVE_REPORTED_START -->
<details>
<summary><b>CVE Reported (1)</b></summary>
<br>

| CVE | Score | Date | Description |
|:----|:------|:-----|:------------|
| [CVE-2026-32255](https://github.com/kanbn/kan/security/advisories/GHSA-qrx8-9hc6-jvqg) | 8.6 | 2026-03-19 | Kan is an open-source project management tool. In versions 0.5.4 and below, the /api/download/attatchment endpoint has no authentication and no URL validation. The Attachment Download endpoint accepts a user-supplied URL query parameter and passes it directly to fetch() server-side, and returns the full response body. An unauthenticated attacker can use this to make HTTP requests from the server to internal services, cloud metadata endpoints, or private network resources. This issue has been fixed in version 0.5.5. To workaround this issue, block or restrict access to /api/download/attatchment at the reverse proxy level (nginx, Cloudflare, etc.). |

</details>
<!-- CVE_REPORTED_END -->

<!-- POC_CVE_START -->
<details>
<summary><b>CVE Proof of Concepts (3)</b></summary>
<br>

| CVE | Description | ⭐ | 🍴 | 👁️ | 📥 |
|:----|:------------|---:|---:|----:|---:|
| [**CVE-2025-55182**](https://github.com/kOaDT/poc-cve-2025-55182) | This repository contains a POC of CVE-2025-55182, a critical (CVSS score 10.0) pre-authentication remote code execution vulnerability affecting React Server Components, also known as React2Shell. | 12 | 3 | 4492 | 1369 |
| [**CVE-2025-29927**](https://github.com/kOaDT/poc-cve-2025-29927) | This repository contains a POC and an exploit script for CVE-2025-29927, a critical vulnerability in Next.js that allows attackers to bypass authorization checks implemented in middleware. | 7 | 3 | 1744 | 527 |
| [**CVE-2026-32255**](https://github.com/kOaDT/poc-cve-2026-32255) | This repository contains a proof of concept (POC) for CVE-2026-32255, a high-severity Server-Side Request Forgery (SSRF) vulnerability in Kan, an open-source project management tool. | 2 | - | 882 | 226 |

</details>
<!-- POC_CVE_END -->

<!-- PROJECTS_START -->
<details>
<summary><b>Projects (5)</b></summary>
<br>

| Project | Description | ⭐ | 🍴 | 👁️ | 📥 |
|:--------|:------------|---:|---:|----:|---:|
| [**oss-oopssec-store**](https://github.com/kOaDT/oss-oopssec-store) | Security training for the apps you actually ship. Open your browser and start hacking. | 20 | 37 | 4449 | 50736 |
| [**cyber-bot**](https://github.com/kOaDT/cyber-bot) | Threat intelligence platform: RSS aggregation, NVD CVE tracking, ENISA EUVD, databreaches, ... | 5 | 1 | 240007 | 1253 |
| [**hate-crimes-map**](https://github.com/kOaDT/hate-crimes-map) | This project aims to visualize hate crime data to bring visibility to crimes that are often invisible or normalized by society. | 3 | - | 143 | 353 |
| [**crack-hash**](https://github.com/kOaDT/crack-hash) | A fast, multi-threaded hash cracking tool written in Rust. This tool performs dictionary attacks against hashed passwords. | 2 | - | 71 | 43 |
| [**awesome-pentest-tools**](https://github.com/kOaDT/awesome-pentest-tools) | Open-source offensive security tools, plus a vendor-agnostic AI agent that runs authorized pentest engagements using only tools from this list. | 2 | - | 5 | 113 |

</details>
<!-- PROJECTS_END -->

<!-- OSS_START -->
<details>
<summary><b>OSS Contributions (16)</b></summary>
<br>

| Repository | Description | ⭐ | 🍴 |
|:-----------|:------------|---:|---:|
| [**qazbnm456/awesome-web-security**](https://github.com/qazbnm456/awesome-web-security) | 🐶 A curated list of Web Security materials and resources. | 13427 | 1786 |
| [**kanbn/kan**](https://github.com/kanbn/kan) | The open source Trello alternative. | 4926 | 366 |
| [**beelzebub-labs/beelzebub**](https://github.com/beelzebub-labs/beelzebub) | A secure low code deception runtime framework, leveraging AI for System Virtualization. | 2028 | 198 |
| [**OWASP/www-community**](https://github.com/OWASP/www-community) | OWASP Community Pages are a place where OWASP can accept community contributions for security-related content. | 1364 | 828 |
| [**OWASP/www-project-vulnerable-web-applications-directory**](https://github.com/OWASP/www-project-vulnerable-web-applications-directory) | The OWASP Vulnerable Web Applications Directory Project (VWAD) is a comprehensive and well maintained registry of all known vulnerable web applications currently available. | 86 | 46 |
| [**usebruno/bruno**](https://github.com/usebruno/bruno) | Opensource IDE For Exploring and Testing API's (lightweight alternative to Postman/Insomnia) | 44594 | 2526 |
| [**infoslack/awesome-web-hacking**](https://github.com/infoslack/awesome-web-hacking) | A list of web application security | 6846 | 1285 |
| [**husnainfareed/awesome-ethical-hacking-resources**](https://github.com/husnainfareed/awesome-ethical-hacking-resources) | 😎 🔗 Awesome list about all kinds of resources for learning Ethical Hacking and Penetration Testing. | 3492 | 538 |
| [**lingdojo/kana-dojo**](https://github.com/lingdojo/kana-dojo) | Aesthetic, minimalist platform for learning Japanese inspired by Duolingo and Monkeytype, built with Next.js and sponsored by Vercel. Beginner-friendly with plenty of good first issues - all contributions are welcome! | 2517 | 2133 |
| [**fabionoth/awesome-cyber-security**](https://github.com/fabionoth/awesome-cyber-security) | A collection of awesome software, libraries, documents, books, resources and cools stuffs about security. | 1881 | 255 |
| [**vavkamil/awesome-vulnerable-apps**](https://github.com/vavkamil/awesome-vulnerable-apps) | Awesome Vulnerable Applications | 1411 | 216 |
| [**kaiiyer/awesome-vulnerable**](https://github.com/kaiiyer/awesome-vulnerable) | A curated list of VULNERABLE APPS and SYSTEMS which can be used as PENETRATION TESTING PRACTICE LAB. | 1318 | 216 |
| [**Grafikart/Grafikart.fr**](https://github.com/Grafikart/Grafikart.fr) | Dépôt pour la nouvelle version de Grafikart.fr | 686 | 186 |
| [**okhosting/awesome-cyber-security**](https://github.com/okhosting/awesome-cyber-security) | A curated list of cyber security resources and tools. | 540 | 78 |
| [**noraj/rawsec-cybersecurity-inventory**](https://github.com/noraj/rawsec-cybersecurity-inventory) | An inventory of tools and resources about CyberSecurity that  aims to help people to find everything related to CyberSecurity. | 337 | 72 |
| [**secnotes/awesome-cybersecurity**](https://github.com/secnotes/awesome-cybersecurity) | A collection of awesome github repositories about security | 73 | 7 |

</details>
<!-- OSS_END -->

<!-- PUBLICATIONS_START -->
<details>
<summary><b>Publications (1)</b></summary>
<br>

| Title | Platform | Category | Date |
|:------|:---------|:---------|:-----|
| [MCP Tool Poisoning](https://owasp.org/www-community/attacks/MCP_Tool_Poisoning) | OWASP | article | 2026-03-26 |

</details>
<!-- PUBLICATIONS_END -->

<details>
<summary><b>Github Metrics</b></summary>
<br>

<div align="center">

![](./profile-3d-contrib/profile-night-rainbow.svg)

<img src="https://streak-stats.demolab.com/?user=kOaDT&theme=dark"></img>

</div>


</details>

<!-- THM_STATS_START -->
<details>
<summary><b>TryHackMe Stats</b></summary>
<br>

| Global Rank | Top | Streak |
|-------------|-----|--------|
| N/A | N/A | N/A |

</details>
<!-- THM_STATS_END -->

<!-- THM_BADGES_START -->
<details>
<summary><b>TryHackMe Badges (0)</b></summary>
<br>

_No badges available_

</details>
<!-- THM_BADGES_END -->

<!-- THM_ROOMS_START -->
<details>
<summary><b>TryHackMe Completed Rooms (0)</b></summary>
<br>

_No rooms available_

</details>
<!-- THM_ROOMS_END -->

<!-- CERTIFICATIONS_START -->

<!-- CERTIFICATIONS_END -->

<!-- CERTIFICATES_START -->
<details>
<summary><b>Certificates (122)</b></summary>
<br>

- [Carry out a web penetration test](https://drive.proton.me/urls/BMT4ZEJX14#rSOX6TfYnj0X) — _2026-05_
- [Introduction to DevSecOps: Culture and Methodology](https://drive.proton.me/urls/PBCKBPPDN8#yllbpawU9Opt) — _2026-05_
- [Dive Into the World of Cyber Incident Detection and Response](https://drive.proton.me/urls/378A1SPJJ8#b4zbL1v6NI9R) — _2026-04_
- [Protect your Connected Digital Systems by Following the 12 Best Practices from ANSSI](https://drive.proton.me/urls/CZHTZ2PED8#9D9nE6GODsxt) — _2026-04_
- [Analyze and Manage IT Risks](https://drive.proton.me/urls/3Y1HWYQCT4#Ca90ucSn6oSN) — _2026-03_
- [Everything You Need to Know About Computer Networks in Just a Few Hours](https://drive.proton.me/urls/75M9G2HE5C#aFM44IX0srti) — _2026-02_
- [Secure your Data with Cryptography](https://drive.proton.me/urls/QR4P3AC5C0#WLyO8wmdWwCY) — _2026-02_
- [Raise Cybersecurity Awareness Effectively](https://drive.proton.me/urls/NTFEGNBVQC#v7ra3gs9Q9a5) — _2026-02_
- [Secure your Network with VPNs and Firewalls](https://drive.proton.me/urls/63VBNKC09W#QCJOTohtakpE) — _2026-02_
- [Conduct Your Cybersecurity Monitoring](https://drive.proton.me/urls/65N4GRE4CG#jK50yBFNBAFt) — _2026-02_
- [Discover the Basics of Digital Security](https://drive.proton.me/urls/D74PR8VB28#2zKus9QYxHpi) — _2026-02_
- [Discover the World of Cybersecurity](https://drive.proton.me/urls/V8B8XBCNVC#OYriuFlC0ElJ) — _2026-02_
- [Try Hack Me - Advent of Cyber 2025](https://drive.proton.me/urls/VPWHGJQ4KM#o8NqajkQTTJq) — _2025-12_
- [Try Hack Me - Security Engineer](https://drive.proton.me/urls/3ESE629GDW#FTJnVotyfc73) — _2025-09_
- [Try Hack Me - Web Fundamentals](https://drive.proton.me/urls/6T65407KTC#jasSYPa2elWu) — _2025-02_
- [Try Hack Me - Jr Penetration Tester](https://drive.proton.me/urls/GHP7890C68#NZ01dYC23p0j) — _2025-01_
- [Try Hack Me - Advent of Cyber 2024](https://drive.proton.me/urls/05PHY6GF98#8U10SVDPoUBv) — _2024-12_
- [Try Hack Me - Complete Beginner](https://drive.proton.me/urls/TQTMQ4BC2C#MXk2ykWOiEIe) — _2024-11_
- [Try Hack Me - Cyber Security 101](https://drive.proton.me/urls/3NCEA2MSXG#LXwKl07QVNoS) — _2024-11_
- [Try Hack Me - Introduction to Cyber Security](https://drive.proton.me/urls/GWK39ADZ38#5opgmy4Ygy0a) — _2024-09_
- [Try Hack Me - Pre Security](https://drive.proton.me/urls/CJ3RNT023G#p4QFH6vNjI2f) — _2024-08_
- [Ethical Hacking: Social Engineering](https://drive.proton.me/urls/4NTFVHMJWW#FEKlPWvaYTUV) — _2024-08_
- [OWASP Top 10](https://drive.proton.me/urls/8034PTTCCG#AXeDTR0sQwoW) — _2023-11_
- [Security for Developers](https://drive.proton.me/urls/XGBWMGFJDR#ZW1vq64P54nu) — _2023-11_
- [Ethical Hacking: the Complete Course](https://drive.proton.me/urls/T6YXMQEPG0#mm1klyOBPKs9) — _2023-10_
- [Use ChatGPT to improve your productivity](https://drive.proton.me/urls/EDGMM47ECM#hd8bq3nwLksh) — _2023-05_
- [Ethereum and Solidity: The Complete Developer's Guide](https://drive.proton.me/urls/W692X2619G#9qBhhlTFYgFX) — _2023-03_
- [Discover the world of Information Systems](https://drive.proton.me/urls/Q0GWTENYVG#WLC7xA7prPDr) — _2022-09_
- [Get started with Linux](https://drive.proton.me/urls/Y3GMCFCH4G#xo1pqgkTcjEY) — _2022-07_
- [Simulate network architectures with GNS3](https://drive.proton.me/urls/QF35MV7B2C#9mEYvZz6BLOD) — _2022-05_
- [Design your TCP/IP network](https://drive.proton.me/urls/J87KPKSHCR#Dp5tUzVPT4Z1) — _2022-05_
- [Draw up a functional specification](https://drive.proton.me/urls/VHS4KMPE7M#s5Xo74bTvlNj) — _2022-04_
- [Design a clickable interface](https://drive.proton.me/urls/29Q55GW87W#0rMujRf4EIkQ) — _2022-04_
- [Set up your front-end environment](https://drive.proton.me/urls/0QQ43YDTCC#PPzRM1bcQ0vj) — _2022-04_
- [Discover the jobs of developer](https://drive.proton.me/urls/N2H2QNSRFR#s5xlXkDOlvLp) — _2022-04_
- [Develop your soft skills](https://drive.proton.me/urls/67VZHPX1G0#G4lGLTSeASgH) — _2022-04_
- [Use the Redux state manager to manage the state of your applications](https://drive.proton.me/urls/H5N0G0NKJ0#AlhYmWhkgvSW) — _2022-04_
- [Use design patterns in JavaScript](https://drive.proton.me/urls/F91KCBXH0C#6e0mzGlYQFlY) — _2022-04_
- [Learn how to use the command line in a terminal](https://drive.proton.me/urls/E8D6FNF1X8#SD54HjihF8wE) — _2022-04_
- [Manage code with Git and GitHub](https://drive.proton.me/urls/NHB8JZJ9B4#GDELJylOfo2T) — _2022-03_
- [Create a complete React application](https://drive.proton.me/urls/3HCQMT6XBW#wfJZNEDMRdKk) — _2022-03_
- [Get started with React](https://drive.proton.me/urls/EG8SGRFKK8#pM2zjJlWHYVX) — _2022-01_
- [Manage your time efficiently](https://drive.proton.me/urls/RYQEDRXCBM#bK81jFNcYiVx) — _2022-01_
- [Create responsive websites with Bootstrap 4](https://drive.proton.me/urls/ADE2Q3223W#pPoZOlK9JGcm) — _2021-12_
- [Create modern CSS animations](https://drive.proton.me/urls/QMFX53W5J4#q0oHOTOL2suY) — _2021-12_
- [Code an accessible website with HTML & CSS](https://drive.proton.me/urls/GAFDHZF22C#ksDujK0BCR7c) — _2021-11_
- [Test your Front End applications with JavaScript](https://drive.proton.me/urls/1AGYMEE6RR#ofiAasXImMNm) — _2021-11_
- [Debug your website interface](https://drive.proton.me/urls/AGAEZT25CC#2FzoAh6clK6B) — _2021-10_
- [Write the technical documentation for your project](https://drive.proton.me/urls/RN9SZVBF5G#5rzKEpfhAaFe) — _2021-10_
- [Test the interface of your site](https://drive.proton.me/urls/7NJX1GGVBM#h7WQQyp3WQeW) — _2021-10_
- [Create a web application with Vue.js](https://drive.proton.me/urls/CTF46QZW4C#vWShD8zzoh7U) — _2021-10_
- [Adopt REST APIs for your web projects](https://drive.proton.me/urls/6XNG2VG714#0AosFWoqjoGN) — _2021-09_
- [Go full stack with Node.js, Express and MongoDB](https://drive.proton.me/urls/DR2P4CDFWM#wnDrtjMPlfqa) — _2021-08_
- [Write JavaScript for the web](https://drive.proton.me/urls/WDQZHM91A4#3JN87iWCanvJ) — _2021-07_
- [Design accessible web content](https://drive.proton.me/urls/NTMVRF5HG0#NhOiPPVtBwyN) — _2021-07_
- [Learn to program with JavaScript](https://drive.proton.me/urls/TT9PVSQ8MM#ZIzgmHiwW9Wp) — _2021-07_
- [Simplify CSS with Sass](https://drive.proton.me/urls/F5XX9N7C64#oTFUmudHHmjM) — _2021-06_
- [Increase your traffic with natural referencing (SEO)](https://drive.proton.me/urls/RZYP01NHN4#G02unqkHYdn9) — _2021-06_
- [Optimize the referencing of your site (SEO) by improving its technical performance](https://drive.proton.me/urls/F1XR38GRBR#V177aFRaeXCZ) — _2021-06_
- [Secure your web applications with OWASP](https://drive.proton.me/urls/X6H3HKGMWW#uPjpoOlBuKJV) — _2021-05_
- [Learn to learn](https://drive.proton.me/urls/XZV693PPV0#cuUJU9aWYt14) — _2021-02_
- [The stages of the Mentor's life](https://drive.proton.me/urls/2DA4ZD0XM8#3gI8rqjJ5jHH) — _2021-02_
- [Learn about Python for data analysis](https://drive.proton.me/urls/PF5Q4429NM#FbgiL0RgCWlb) — _2020-04_
- [Ultra-fast applications with Node.js](https://drive.proton.me/urls/AK4KNYKT58#lkGhvEOsrCSw) — _2020-02_
- [Perfect your agile project management](https://drive.proton.me/urls/7ZB7KDC01W#c4PAlzcNcVWJ) — _2019-02_
- [Understanding Bitcoin and the Blockchain](https://drive.proton.me/urls/RFVZV873DM#faTOLO6eRsDv) — _2019-02_
- [Discover the cloud with Amazon Web Services](https://drive.proton.me/urls/K90YHHK0B4#auCKPIdbkoJs) — _2019-02_
- [Manage your project with a Scrum team](https://drive.proton.me/urls/ZEP4F0JTZM#JWwZGIDJ8t9d) — _2019-02_
- [Continue with Ruby on Rails](https://drive.proton.me/urls/P14X44CV3R#h9I58HSe6QGY) — _2019-01_
- [Set up an information monitoring system](https://drive.proton.me/urls/K328S3H9C0#T3NAuv07eexM) — _2019-01_
- [Learn about agile project management](https://drive.proton.me/urls/XSRWEJC8QR#qlSuQNxdBLlV) — _2018-10_
- [Get started with Ruby on Rails](https://drive.proton.me/urls/0QT6G40384#J8N3VgFdD9Bh) — _2018-10_
- [Discover the agility posture](https://drive.proton.me/urls/JR0J48ZV4G#D2aBFvoAt1b4) — _2018-10_
- [Put the UX approach into practice](https://drive.proton.me/urls/22RCMAARHM#jSDdmlwq2OIY) — _2018-09_
- [Discover the world of cybersecurity_0](https://drive.proton.me/urls/N74VS1J26C#cLL2BiDMCbWi) — _2018-09_
- [Start programming with Ruby](https://drive.proton.me/urls/YVRXHEJMY0#5eslbVNS8TJv) — _2018-08_
- [React and Redux in practice](https://drive.proton.me/urls/QG74M664RC#unT6LNND1Brr) — _2018-06_
- [Really understand Javascript](https://drive.proton.me/urls/9FCCXFFSEM#q2XvgwJGEi26) — _2018-05_
- [Build a web application with React.js](https://drive.proton.me/urls/K0FJNVK48G#BgTNpBuBJteh) — _2018-04_
- [UX design: discover the basics!](https://drive.proton.me/urls/451WR90D9W#sN8paISvDvK3) — _2018-01_
- [Learn about Design Thinking](https://drive.proton.me/urls/8D92JE8E7G#4BdRPxODZkmO) — _2018-01_
- [Speak in public](https://drive.proton.me/urls/331WC4TD38#oDizZX96vIzG) — _2017-12_
- [Make a database with UML](https://drive.proton.me/urls/NKJEHTGP2G#JkZEZQXkK0Ty) — _2017-11_
- [Use REST APIs in your web projects](https://drive.proton.me/urls/GWQXN9B0N0#BmycgHljVdnX) — _2017-10_
- [Manage your IT project easily!](https://drive.proton.me/urls/9X3FGGTBG8#NeRTds7t9ECo) — _2017-09_
- [Start software analysis with UML](https://drive.proton.me/urls/KPXYHX1CAM#irDxVs6mh3FC) — _2017-09_
- [Improve your skills in Python](https://drive.proton.me/urls/0Q6ACPK3A0#F6YSOZy95kGW) — _2017-08_
- [Discover how the algorithms work](https://drive.proton.me/urls/Y0K3XCXYA8#VJ0sjKeuGwqS) — _2017-08_
- [Discover object-oriented programming with Python](https://drive.proton.me/urls/2XAS2MHW98#o9o1FzCKmyXf) — _2017-08_
- [Animate a Twitter community](https://drive.proton.me/urls/8BWV3KA6S4#Moej6r8rwEpi) — _2017-08_
- [Start your project with Python](https://drive.proton.me/urls/MW15KENBF4#GfFNU34vJN9Q) — _2017-07_
- [Launch your freelance activity](https://drive.proton.me/urls/ZGW85Z71JM#Q9Q9Bq2hOwh2) — _2017-06_
- [Succeed in your emailing campaign with MailChimp](https://drive.proton.me/urls/5BPEB0XPE4#XLPoVhrG6Qx8) — _2017-05_
- [Digital Marketing Fundamentals (Digital Active)](https://drive.proton.me/urls/FGRX0CS4EW#HjyaZBcnlQI9) — _2017-03_
- [Develop your website with the Symfony framework](https://drive.proton.me/urls/P0BPYBQT04#MuBze7MSNk79) — _2016-12_
- [Manage and pilot a multimedia project](https://drive.proton.me/urls/BJRRMRF4QW#U5BuWkJEC98G) — _2016-11_
- [Organize your multimedia project](https://drive.proton.me/urls/YTPNX5158G#hlKHAWPuDVz5) — _2016-11_
- [Draw up the specifications for a digital project](https://drive.proton.me/urls/060F2ZR4HC#7JLB2b27ogfc) — _2016-10_
- [Simplify your JavaScript development with jQuery](https://drive.proton.me/urls/0MH6KQXSBW#aV7I3HlxSMY1) — _2016-09_
- [Introduction to jQuery](https://drive.proton.me/urls/F7K2HQ472G#NaKvofw9Sxls) — _2016-08_
- [Big Data: Intelligence, Products and Markets in the Age of Big Analytics](https://drive.proton.me/urls/NYRWP4S37M#Yus6IXUyRoQG) — _2016-07_
- [Become an auto-entrepreneur](https://drive.proton.me/urls/DDZSGMX344#PAJ54GrlUuaK) — _2016-07_
- [Build modern and beautiful websites with WordPress](https://drive.proton.me/urls/XRXZJA4AKW#6XLGSOwoReaS) — _2016-06_
- [Create your professional website with WordPress](https://drive.proton.me/urls/RY0FPDASM0#486ILWllYdt9) — _2016-06_
- [Create interactive web pages with JavaScript](https://drive.proton.me/urls/3T1T19XDW8#zloY3lO6J6O4) — _2016-06_
- [Manage your databases with MySQL](https://drive.proton.me/urls/8TXK1P8BP4#jgGsGSSDGURg) — _2016-06_
- [Big Data is transforming my life and the lives of businesses](https://drive.proton.me/urls/5KYHXSYBF8#tDGzkbxqoCQY) — _2016-06_
- [Learn how to frame a multimedia project](https://drive.proton.me/urls/F8QJTBRQN4#oS24V2CO4jKB) — _2016-05_
- [Create your first website with WordPress](https://drive.proton.me/urls/XGED3T254R#ANW9v3NK8dmU) — _2016-04_
- [Design your website with PHP and MySQL](https://drive.proton.me/urls/MAKJXBFS7G#NsZJ1pz80c8E) — _2016-04_
- [Understanding Big Data through movies](https://drive.proton.me/urls/KQ924A6N3R#x8BXOIeO2F3F) — _2016-03_
- [Discover the basics of project management](https://drive.proton.me/urls/TFQG87XNGC#PVk0gF8fEi6O) — _2016-03_
- [Learn how to surf the Internet safely](https://drive.proton.me/urls/KNY611G8GC#EoWyN92BVAgu) — _2016-03_
- [Control the use of your personal data](https://drive.proton.me/urls/8Z65E5XPAM#LQy7fcuIj4ig) — _2016-03_
- [Take back control with Linux!](https://drive.proton.me/urls/RM74CYEPZC#sJSXwaBzya9k) — _2016-03_
- [Web Integrator](https://drive.proton.me/urls/XRSJMAWTJW#q2d6n9u1al2b) — _2016-03_
- [Get started with Bootstrap](https://drive.proton.me/urls/HP0M47X0EW#OOrIQoZTCjhK) — _2016-03_
- [Manage your code with Git and GitHub](https://drive.proton.me/urls/BZZBBXYY10#aEONc9gpQnO1) — _2016-03_
- [Discover CMS solutions](https://drive.proton.me/urls/T6VNC61RG8#OD4IrQHzKQ6q) — _2016-02_
- [Learn to code with JavaScript](https://drive.proton.me/urls/3Y0G67ZN8C#UrtzgTmhO0Cz) — _2016-02_
- [Understanding the Web](https://drive.proton.me/urls/GT29QX8S00#EzOw7iyHD0ot) — _2016-02_
- [Learn how to create your website with HTML5 and CSS3](https://drive.proton.me/urls/N7RG44JYPR#cY3JzUy1kYxF) — _2016-02_

</details>
<!-- CERTIFICATES_END -->
