# 협궤 고속열차 세트
[English](./README.md) | [한국어](./README.ko.md)

[![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://www.gnu.org/licenses/gpl-2.0.html)

협궤 고속열차 세트는 가상의 1067mm궤간의 200km이상의 열차와 그외의 열차를 추가해주는 OpenTTD NewGRF입니다.
**[Github release 페이지](https://github.com/kimjostars/Narrow-Gauge-fast-train/releases)** 에서 다운로드 할수있습니다.
이세트를 게임에 적용할때 **[JP+ Track](https://github.com/OpenTTD-JPplus/JPplusTracks)** 과 같이 적용하는것을 추천합니다.
## 개발
### 빌드하는 방법
이 NewGRF를 빌드하려면 [NML](https://github.com/OpenTTD/nml)(>= 0.9.0), **Python 3**이 필요합니다.  
파일 합치기 `build.py --entry src/{메인파일}.pnml --merge {프로젝트 파일명}/{메인파일}.nml`
컴파일 `nmlc -l ./lang/ ./{메인파일}.nml`
### 번역
이세트의 기본언어는 한국어 입니다.
다른언어로 번역하고 싶으시다면 이 Github 프로젝트에 Pull Request를 열어주세요.
Pull Request를 열 줄 모르신다면, Issues에 올리셔도 괜찮습니다. 이 파일을 번역하시면 됩니다.
- **[src/lang/korean.lng](https://github.com/kimjostars/Narrow-Gauge-fast-train/blob/main/src/lang/korean.lng)** : 한국어
번역은 언제나 환영입니다.
### Contributors
코드 : kimjostars, irice7350

그래픽 : kimjostars, raeun_cos, [JP+](https://github.com/OpenTTD-JPplus)(에셋 사용), [600계 스프라이트 출처](https://www.tt-wiki.net/wiki/NMLTutorial/Train_single_engine) 

본프로젝트에 기여함은 라이선스에 동의함을 의미합니다.
