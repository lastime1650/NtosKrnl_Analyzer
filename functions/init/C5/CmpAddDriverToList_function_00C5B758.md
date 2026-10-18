# CmpAddDriverToList

- RVA: `0x00C5B758`–`0x00C5BE7B` (길이 `1,827` bytes)
- VA: `0x0000000140C5B758`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D722C`
- 디코드: `473`개 명령, `1,827/1,827` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **64**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **9**

### Outgoing calls
- `0x00C5B7E4` → [HvpGetCellFlat](../../page/85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00C5B7EB` → [HvpGetCellPaged](../../page/85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00C5B806` → [CmpGetNodeName](CmpGetNodeName_function_00C5C95C.md) (function, `0x00C5C95C`)
- `0x00C5B81E` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (function, `0x00463960`)
- `0x00C5B83C` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00C5B858` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00C5B8A2` → [CmpFindValueByName](../../page/84/CmpFindValueByName_function_00844E1C.md) (function, `0x00844E1C`)
- `0x00C5B8CA` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00C5B8E9` → [RtlAppendUnicodeToString](../../text/40/RtlAppendUnicodeToString_function_0040F990.md) (function, `0x0040F990`)
- `0x00C5B8F9` → [RtlAppendUnicodeStringToString](../../text/40/RtlAppendUnicodeStringToString_function_0040FA50.md) (function, `0x0040FA50`)
- `0x00C5B90D` → [RtlAppendUnicodeToString](../../text/40/RtlAppendUnicodeToString_function_0040F990.md) (function, `0x0040F990`)
- `0x00C5B932` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00C5B947` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00C5B965` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00C5B97F` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00C5B997` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00C5B9A7` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00C5B9C9` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00C5B9ED` → [HvpGetCellFlat](../../page/85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00C5B9F4` → [HvpGetCellPaged](../../page/85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00C5BA17` → [CmpValueToData](../../page/7F/CmpValueToData_function_007F3934.md) (function, `0x007F3934`)
- `0x00C5BA2F` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00C5BA36` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00C5BA55` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00C5BA73` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00C5BA7D` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00C5BA90` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00C5BAAD` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00C5BAB4` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00C5BAE0` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00C5BAFD` → [RtlAppendUnicodeStringToString](../../text/40/RtlAppendUnicodeStringToString_function_0040FA50.md) (function, `0x0040FA50`)
- `0x00C5BB11` → [RtlAppendUnicodeStringToString](../../text/40/RtlAppendUnicodeStringToString_function_0040FA50.md) (function, `0x0040FA50`)
- `0x00C5BB29` → [RtlAppendUnicodeStringToString](../../text/40/RtlAppendUnicodeStringToString_function_0040FA50.md) (function, `0x0040FA50`)
- `0x00C5BB3D` → [RtlAppendUnicodeStringToString](../../text/40/RtlAppendUnicodeStringToString_function_0040FA50.md) (function, `0x0040FA50`)
- `0x00C5BB5E` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00C5BB84` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00C5BBCB` → [CmpFindValueByName](../../page/84/CmpFindValueByName_function_00844E1C.md) (function, `0x00844E1C`)
- `0x00C5BBF8` → [HvpGetCellFlat](../../page/85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00C5BBFF` → [HvpGetCellPaged](../../page/85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00C5BC22` → [CmpValueToData](../../page/7F/CmpValueToData_function_007F3934.md) (function, `0x007F3934`)
- `0x00C5BC3A` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00C5BC41` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00C5BC67` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00C5BC6E` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00C5BC80` → [CmpFindValueByName](../../page/84/CmpFindValueByName_function_00844E1C.md) (function, `0x00844E1C`)
- `0x00C5BCAB` → [HvpGetCellFlat](../../page/85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00C5BCB2` → [HvpGetCellPaged](../../page/85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00C5BCD5` → [CmpValueToData](../../page/7F/CmpValueToData_function_007F3934.md) (function, `0x007F3934`)
- `0x00C5BCEE` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00C5BCF5` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00C5BD14` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00C5BD1B` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00C5BD47` → [CmpFindValueByName](../../page/84/CmpFindValueByName_function_00844E1C.md) (function, `0x00844E1C`)
- `0x00C5BD72` → [HvpGetCellFlat](../../page/85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00C5BD79` → [HvpGetCellPaged](../../page/85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00C5BD9C` → [CmpValueToData](../../page/7F/CmpValueToData_function_007F3934.md) (function, `0x007F3934`)
- `0x00C5BDB5` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00C5BDBC` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00C5BDDB` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00C5BDE2` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00C5BE0E` → [CmpFindValueByName](../../page/84/CmpFindValueByName_function_00844E1C.md) (function, `0x00844E1C`)
- `0x00C5BE26` → [CmpFindTagIndex](CmpFindTagIndex_function_00C5C628.md) (function, `0x00C5C628`)
- `0x00C5BE4D` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00C5BE57` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)

### Direct callers
- [CmpFindDrivers](CmpFindDrivers_function_00C5BFBC.md) at `0x00C5C137`
- [CmpFindDrivers](CmpFindDrivers_function_00C5BFBC.md) at `0x00C5C1DD`

### Static image references
- `0x00C5B869` → RVA `0x00C82310` (`CmpImagePathString`; read)
- `0x00C5B8DE` → RVA `0x00C7E570` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C5B902` → RVA `0x00C7E5A0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C5BAF2` → RVA `0x00C82178` (`CmpRegistryRootKeyPath`; read)
- `0x00C5BB1E` → RVA `0x00C821D0` (`CmpServicesSubKeyPath`; read)
- `0x00C5BBB0` → RVA `0x00C82340` (`CmpErrorControlString`; read)
- `0x00C5BC73` → RVA `0x00C82350` (`CmpGroupString`; read)
- `0x00C5BD3A` → RVA `0x00C82260` (`CmpDriverDependencyString`; read)
- `0x00C5BE01` → RVA `0x00C822B0` (`CmpTagString`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **62**
  - `0x00C5B7E4` → [HvpGetCellFlat](../../page/85/HvpGetCellFlat_function_00854C60.md) (`INIT` → `PAGE`)
  - `0x00C5B7EB` → [HvpGetCellPaged](../../page/85/HvpGetCellPaged_function_00854CB0.md) (`INIT` → `PAGE`)
  - `0x00C5B81E` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (`INIT` → `.text`)
  - `0x00C5B83C` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`INIT` → `.text`)
  - `0x00C5B858` → [memset](../../text/6C/memset_function_006C6C40.md) (`INIT` → `.text`)
  - `0x00C5B8A2` → [CmpFindValueByName](../../page/84/CmpFindValueByName_function_00844E1C.md) (`INIT` → `PAGE`)
  - `0x00C5B8CA` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`INIT` → `.text`)
  - `0x00C5B8E9` → [RtlAppendUnicodeToString](../../text/40/RtlAppendUnicodeToString_function_0040F990.md) (`INIT` → `.text`)
  - `0x00C5B8F9` → [RtlAppendUnicodeStringToString](../../text/40/RtlAppendUnicodeStringToString_function_0040FA50.md) (`INIT` → `.text`)
  - `0x00C5B90D` → [RtlAppendUnicodeToString](../../text/40/RtlAppendUnicodeToString_function_0040F990.md) (`INIT` → `.text`)
  - `0x00C5B932` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`INIT` → `.text`)
  - `0x00C5B947` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`INIT` → `.text`)
  - `0x00C5B965` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`INIT` → `.text`)
  - `0x00C5B97F` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`INIT` → `.text`)
  - `0x00C5B997` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`INIT` → `.text`)
  - `0x00C5B9A7` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`INIT` → `.text`)
  - `0x00C5B9C9` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (`INIT` → `PAGE`)
  - `0x00C5B9ED` → [HvpGetCellFlat](../../page/85/HvpGetCellFlat_function_00854C60.md) (`INIT` → `PAGE`)
  - `0x00C5B9F4` → [HvpGetCellPaged](../../page/85/HvpGetCellPaged_function_00854CB0.md) (`INIT` → `PAGE`)
  - `0x00C5BA17` → [CmpValueToData](../../page/7F/CmpValueToData_function_007F3934.md) (`INIT` → `PAGE`)
  - `0x00C5BA2F` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (`INIT` → `PAGE`)
  - `0x00C5BA36` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (`INIT` → `PAGE`)
  - `0x00C5BA55` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`INIT` → `.text`)
  - `0x00C5BA73` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (`INIT` → `PAGE`)
  - `0x00C5BA7D` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (`INIT` → `PAGE`)
  - `0x00C5BA90` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`INIT` → `.text`)
  - `0x00C5BAAD` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (`INIT` → `PAGE`)
  - `0x00C5BAB4` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (`INIT` → `PAGE`)
  - `0x00C5BAE0` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`INIT` → `.text`)
  - `0x00C5BAFD` → [RtlAppendUnicodeStringToString](../../text/40/RtlAppendUnicodeStringToString_function_0040FA50.md) (`INIT` → `.text`)
  - `0x00C5BB11` → [RtlAppendUnicodeStringToString](../../text/40/RtlAppendUnicodeStringToString_function_0040FA50.md) (`INIT` → `.text`)
  - `0x00C5BB29` → [RtlAppendUnicodeStringToString](../../text/40/RtlAppendUnicodeStringToString_function_0040FA50.md) (`INIT` → `.text`)
  - `0x00C5BB3D` → [RtlAppendUnicodeStringToString](../../text/40/RtlAppendUnicodeStringToString_function_0040FA50.md) (`INIT` → `.text`)
  - `0x00C5BB5E` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`INIT` → `.text`)
  - `0x00C5BB84` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`INIT` → `.text`)
  - `0x00C5BBCB` → [CmpFindValueByName](../../page/84/CmpFindValueByName_function_00844E1C.md) (`INIT` → `PAGE`)
  - `0x00C5BBF8` → [HvpGetCellFlat](../../page/85/HvpGetCellFlat_function_00854C60.md) (`INIT` → `PAGE`)
  - `0x00C5BBFF` → [HvpGetCellPaged](../../page/85/HvpGetCellPaged_function_00854CB0.md) (`INIT` → `PAGE`)
  - `0x00C5BC22` → [CmpValueToData](../../page/7F/CmpValueToData_function_007F3934.md) (`INIT` → `PAGE`)
  - `0x00C5BC3A` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (`INIT` → `PAGE`)
  - `0x00C5BC41` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (`INIT` → `PAGE`)
  - `0x00C5BC67` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (`INIT` → `PAGE`)
  - `0x00C5BC6E` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (`INIT` → `PAGE`)
  - `0x00C5BC80` → [CmpFindValueByName](../../page/84/CmpFindValueByName_function_00844E1C.md) (`INIT` → `PAGE`)
  - `0x00C5BCAB` → [HvpGetCellFlat](../../page/85/HvpGetCellFlat_function_00854C60.md) (`INIT` → `PAGE`)
  - `0x00C5BCB2` → [HvpGetCellPaged](../../page/85/HvpGetCellPaged_function_00854CB0.md) (`INIT` → `PAGE`)
  - `0x00C5BCD5` → [CmpValueToData](../../page/7F/CmpValueToData_function_007F3934.md) (`INIT` → `PAGE`)
  - `0x00C5BCEE` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (`INIT` → `PAGE`)
  - `0x00C5BCF5` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (`INIT` → `PAGE`)
  - `0x00C5BD14` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (`INIT` → `PAGE`)
  - `0x00C5BD1B` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (`INIT` → `PAGE`)
  - `0x00C5BD47` → [CmpFindValueByName](../../page/84/CmpFindValueByName_function_00844E1C.md) (`INIT` → `PAGE`)
  - `0x00C5BD72` → [HvpGetCellFlat](../../page/85/HvpGetCellFlat_function_00854C60.md) (`INIT` → `PAGE`)
  - `0x00C5BD79` → [HvpGetCellPaged](../../page/85/HvpGetCellPaged_function_00854CB0.md) (`INIT` → `PAGE`)
  - `0x00C5BD9C` → [CmpValueToData](../../page/7F/CmpValueToData_function_007F3934.md) (`INIT` → `PAGE`)
  - `0x00C5BDB5` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (`INIT` → `PAGE`)
  - `0x00C5BDBC` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (`INIT` → `PAGE`)
  - `0x00C5BDDB` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (`INIT` → `PAGE`)
  - `0x00C5BDE2` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (`INIT` → `PAGE`)
  - `0x00C5BE0E` → [CmpFindValueByName](../../page/84/CmpFindValueByName_function_00844E1C.md) (`INIT` → `PAGE`)
  - `0x00C5BE4D` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`INIT` → `.text`)
  - `0x00C5BE57` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (`INIT` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C5B758  48 8B C4                        mov rax, rsp
00C5B75B  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00C5B75F  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
00C5B763  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
00C5B767  55                              push rbp
00C5B768  56                              push rsi
00C5B769  57                              push rdi
00C5B76A  41 54                           push r12
00C5B76C  41 55                           push r13
00C5B76E  41 56                           push r14
00C5B770  41 57                           push r15
00C5B772  48 8D 68 B9                     lea rbp, [rax - 0x47]
00C5B776  48 81 EC A0 00 00 00            sub rsp, 0xa0
00C5B77D  41 83 CF FF                     or r15d, 0xffffffff
00C5B781  4C 8D 45 B7                     lea r8, [rbp - 0x49]
00C5B785  48 8B D9                        mov rbx, rcx
00C5B788  44 89 7D B7                     mov dword ptr [rbp - 0x49], r15d
00C5B78C  33 C9                           xor ecx, ecx
00C5B78E  44 89 7D DF                     mov dword ptr [rbp - 0x21], r15d
00C5B792  0F 57 C0                        xorps xmm0, xmm0
00C5B795  89 4D BB                        mov dword ptr [rbp - 0x45], ecx
00C5B798  0F 57 C9                        xorps xmm1, xmm1
00C5B79B  89 4D E3                        mov dword ptr [rbp - 0x1d], ecx
00C5B79E  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
00C5B7A5  44 8B F1                        mov r14d, ecx
00C5B7A8  89 4D DB                        mov dword ptr [rbp - 0x25], ecx
00C5B7AB  8B F9                           mov edi, ecx
00C5B7AD  89 4D 9F                        mov dword ptr [rbp - 0x61], ecx
00C5B7B0  44 8A E1                        mov r12b, cl
00C5B7B3  89 4D D3                        mov dword ptr [rbp - 0x2d], ecx
00C5B7B6  89 4D B3                        mov dword ptr [rbp - 0x4d], ecx
00C5B7B9  89 4D AB                        mov dword ptr [rbp - 0x55], ecx
00C5B7BC  66 89 4D 4F                     mov word ptr [rbp + 0x4f], cx
00C5B7C0  88 4D 7F                        mov byte ptr [rbp + 0x7f], cl
00C5B7C3  48 8B CB                        mov rcx, rbx
00C5B7C6  44 89 7D D7                     mov dword ptr [rbp - 0x29], r15d
00C5B7CA  44 89 7D CF                     mov dword ptr [rbp - 0x31], r15d
00C5B7CE  44 89 7D AF                     mov dword ptr [rbp - 0x51], r15d
00C5B7D2  0F 11 45 F7                     movups xmmword ptr [rbp - 9], xmm0
00C5B7D6  44 89 7D A7                     mov dword ptr [rbp - 0x59], r15d
00C5B7DA  0F 11 45 BF                     movups xmmword ptr [rbp - 0x41], xmm0
00C5B7DE  0F 11 4D E7                     movups xmmword ptr [rbp - 0x19], xmm1
00C5B7E2  74 07                           je 0x140c5b7eb
00C5B7E4  E8 77 94 BF FF                  call 0x140854c60
00C5B7E9  EB 05                           jmp 0x140c5b7f0
00C5B7EB  E8 C0 94 BF FF                  call 0x140854cb0
00C5B7F0  4C 8B E8                        mov r13, rax
00C5B7F3  48 85 C0                        test rax, rax
00C5B7F6  0F 84 22 01 00 00               je 0x140c5b91e
00C5B7FC  4C 8D 45 4F                     lea r8, [rbp + 0x4f]
00C5B800  48 8B D0                        mov rdx, rax
00C5B803  48 8B CB                        mov rcx, rbx
00C5B806  E8 51 11 00 00                  call 0x140c5c95c
00C5B80B  48 8B F0                        mov rsi, rax
00C5B80E  48 85 C0                        test rax, rax
00C5B811  0F 84 07 01 00 00               je 0x140c5b91e
00C5B817  48 8B D0                        mov rdx, rax
00C5B81A  48 8D 4D F7                     lea rcx, [rbp - 9]
00C5B81E  E8 3D 81 80 FF                  call 0x140463960
00C5B823  85 C0                           test eax, eax
00C5B825  0F 88 17 06 00 00               js 0x140c5be42
00C5B82B  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
00C5B82F  33 D2                           xor edx, edx
00C5B831  B9 90 00 00 00                  mov ecx, 0x90
00C5B836  41 B8 43 4D 31 20               mov r8d, 0x20314d43
00C5B83C  E8 8F F2 A5 FF                  call 0x1406baad0
00C5B841  48 8B F8                        mov rdi, rax
00C5B844  48 85 C0                        test rax, rax
00C5B847  0F 84 F5 05 00 00               je 0x140c5be42
00C5B84D  33 D2                           xor edx, edx
00C5B84F  41 B8 90 00 00 00               mov r8d, 0x90
00C5B855  48 8B C8                        mov rcx, rax
00C5B858  E8 E3 B3 A6 FF                  call 0x1406c6c40
00C5B85D  0F B7 4D 4F                     movzx ecx, word ptr [rbp + 0x4f]
00C5B861  4C 8D 67 78                     lea r12, [rdi + 0x78]
00C5B865  48 8B 45 6F                     mov rax, qword ptr [rbp + 0x6f]
00C5B869  4C 8D 05 A0 6A 02 00            lea r8, [rip + 0x26aa0]
00C5B870  48 89 5F 40                     mov qword ptr [rdi + 0x40], rbx
00C5B874  49 8B D5                        mov rdx, r13
00C5B877  4C 8B F7                        mov r14, rdi
00C5B87A  0F 10 00                        movups xmm0, xmmword ptr [rax]
00C5B87D  33 C0                           xor eax, eax
00C5B87F  F3 0F 7F 47 48                  movdqu xmmword ptr [rdi + 0x48], xmm0
00C5B884  48 89 47 28                     mov qword ptr [rdi + 0x28], rax
00C5B888  48 89 47 18                     mov qword ptr [rdi + 0x18], rax
00C5B88C  8D 41 FE                        lea eax, [rcx - 2]
00C5B88F  48 89 B7 80 00 00 00            mov qword ptr [rdi + 0x80], rsi
00C5B896  66 41 89 04 24                  mov word ptr [r12], ax
00C5B89B  66 89 4F 7A                     mov word ptr [rdi + 0x7a], cx
00C5B89F  48 8B CB                        mov rcx, rbx
00C5B8A2  E8 75 95 BE FF                  call 0x140844e1c
00C5B8A7  8B F0                           mov esi, eax
00C5B8A9  41 3B C7                        cmp eax, r15d
00C5B8AC  0F 85 29 01 00 00               jne 0x140c5b9db
00C5B8B2  41 0F B7 0C 24                  movzx ecx, word ptr [r12]
00C5B8B7  33 D2                           xor edx, edx
00C5B8B9  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
00C5B8BD  83 C1 2E                        add ecx, 0x2e
00C5B8C0  41 B8 43 4D 33 20               mov r8d, 0x20334d43
00C5B8C6  66 89 4D C1                     mov word ptr [rbp - 0x3f], cx
00C5B8CA  E8 01 F2 A5 FF                  call 0x1406baad0
00C5B8CF  33 F6                           xor esi, esi
00C5B8D1  48 89 45 C7                     mov qword ptr [rbp - 0x39], rax
00C5B8D5  48 85 C0                        test rax, rax
00C5B8D8  0F 84 F5 00 00 00               je 0x140c5b9d3
00C5B8DE  48 8D 15 8B 2C 02 00            lea rdx, [rip + 0x22c8b]
00C5B8E5  48 8D 4D BF                     lea rcx, [rbp - 0x41]
00C5B8E9  E8 A2 40 7B FF                  call 0x14040f990
00C5B8EE  85 C0                           test eax, eax
00C5B8F0  78 28                           js 0x140c5b91a
00C5B8F2  49 8B D4                        mov rdx, r12
00C5B8F5  48 8D 4D BF                     lea rcx, [rbp - 0x41]
00C5B8F9  E8 52 41 7B FF                  call 0x14040fa50
00C5B8FE  85 C0                           test eax, eax
00C5B900  78 18                           js 0x140c5b91a
00C5B902  48 8D 15 97 2C 02 00            lea rdx, [rip + 0x22c97]
00C5B909  48 8D 4D BF                     lea rcx, [rbp - 0x41]
00C5B90D  E8 7E 40 7B FF                  call 0x14040f990
00C5B912  85 C0                           test eax, eax
00C5B914  0F 89 A3 01 00 00               jns 0x140c5babd
00C5B91A  44 8A 65 7F                     mov r12b, byte ptr [rbp + 0x7f]
00C5B91E  48 8B 4D C7                     mov rcx, qword ptr [rbp - 0x39]
00C5B922  48 8D 73 20                     lea rsi, [rbx + 0x20]
00C5B926  48 85 C9                        test rcx, rcx
00C5B929  74 0C                           je 0x140c5b937
00C5B92B  0F B7 55 BF                     movzx edx, word ptr [rbp - 0x41]
00C5B92F  48 8B 06                        mov rax, qword ptr [rsi]
00C5B932  E8 99 F1 A5 FF                  call 0x1406baad0
00C5B937  48 8B 4D EF                     mov rcx, qword ptr [rbp - 0x11]
00C5B93B  48 85 C9                        test rcx, rcx
00C5B93E  74 0C                           je 0x140c5b94c
00C5B940  0F B7 55 E7                     movzx edx, word ptr [rbp - 0x19]
00C5B944  48 8B 06                        mov rax, qword ptr [rsi]
00C5B947  E8 84 F1 A5 FF                  call 0x1406baad0
00C5B94C  4D 85 F6                        test r14, r14
00C5B94F  74 5B                           je 0x140c5b9ac
00C5B951  49 8B 4E 18                     mov rcx, qword ptr [r14 + 0x18]
00C5B955  4C 8B FE                        mov r15, rsi
00C5B958  48 85 C9                        test rcx, rcx
00C5B95B  74 11                           je 0x140c5b96e
00C5B95D  41 0F B7 56 10                  movzx edx, word ptr [r14 + 0x10]
00C5B962  48 8B 06                        mov rax, qword ptr [rsi]
00C5B965  E8 66 F1 A5 FF                  call 0x1406baad0
00C5B96A  4C 8D 7B 20                     lea r15, [rbx + 0x20]
00C5B96E  49 8B 4E 28                     mov rcx, qword ptr [r14 + 0x28]
00C5B972  48 85 C9                        test rcx, rcx
00C5B975  74 0D                           je 0x140c5b984
00C5B977  41 0F B7 56 20                  movzx edx, word ptr [r14 + 0x20]
00C5B97C  48 8B 06                        mov rax, qword ptr [rsi]
00C5B97F  E8 4C F1 A5 FF                  call 0x1406baad0
00C5B984  48 8B 8F 80 00 00 00            mov rcx, qword ptr [rdi + 0x80]
00C5B98B  48 85 C9                        test rcx, rcx
00C5B98E  74 0C                           je 0x140c5b99c
00C5B990  0F B7 57 78                     movzx edx, word ptr [rdi + 0x78]
00C5B994  49 8B 07                        mov rax, qword ptr [r15]
00C5B997  E8 34 F1 A5 FF                  call 0x1406baad0
00C5B99C  49 8B 07                        mov rax, qword ptr [r15]
00C5B99F  BA 90 00 00 00                  mov edx, 0x90
00C5B9A4  48 8B CF                        mov rcx, rdi
00C5B9A7  E8 24 F1 A5 FF                  call 0x1406baad0
00C5B9AC  4D 85 ED                        test r13, r13
00C5B9AF  0F 84 A7 04 00 00               je 0x140c5be5c
00C5B9B5  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
00C5B9BC  48 8D 55 B7                     lea rdx, [rbp - 0x49]
00C5B9C0  48 8B CB                        mov rcx, rbx
00C5B9C3  0F 84 8E 04 00 00               je 0x140c5be57
00C5B9C9  E8 52 12 C0 FF                  call 0x14085cc20
00C5B9CE  E9 89 04 00 00                  jmp 0x140c5be5c
00C5B9D3  44 8A E6                        mov r12b, sil
00C5B9D6  E9 43 FF FF FF                  jmp 0x140c5b91e
00C5B9DB  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
00C5B9E2  4C 8D 45 A7                     lea r8, [rbp - 0x59]
00C5B9E6  8B D6                           mov edx, esi
00C5B9E8  48 8B CB                        mov rcx, rbx
00C5B9EB  74 07                           je 0x140c5b9f4
00C5B9ED  E8 6E 92 BF FF                  call 0x140854c60
00C5B9F2  EB 05                           jmp 0x140c5b9f9
00C5B9F4  E8 B7 92 BF FF                  call 0x140854cb0
00C5B9F9  48 85 C0                        test rax, rax
00C5B9FC  0F 84 18 FF FF FF               je 0x140c5b91a
00C5BA02  48 8D 4D AF                     lea rcx, [rbp - 0x51]
00C5BA06  4C 8B C0                        mov r8, rax
00C5BA09  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00C5BA0E  4C 8D 4D 9F                     lea r9, [rbp - 0x61]
00C5BA12  48 8B CB                        mov rcx, rbx
00C5BA15  8B D6                           mov edx, esi
00C5BA17  E8 18 7F B9 FF                  call 0x1407f3934
00C5BA1C  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
00C5BA23  48 8D 55 A7                     lea rdx, [rbp - 0x59]
00C5BA27  4C 8B F8                        mov r15, rax
00C5BA2A  48 8B CB                        mov rcx, rbx
00C5BA2D  74 07                           je 0x140c5ba36
00C5BA2F  E8 EC 11 C0 FF                  call 0x14085cc20
00C5BA34  EB 05                           jmp 0x140c5ba3b
00C5BA36  E8 05 A5 BF FF                  call 0x140855f40
00C5BA3B  4D 85 FF                        test r15, r15
00C5BA3E  0F 84 D6 FE FF FF               je 0x140c5b91a
00C5BA44  8B 75 9F                        mov esi, dword ptr [rbp - 0x61]
00C5BA47  33 D2                           xor edx, edx
00C5BA49  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
00C5BA4D  8B CE                           mov ecx, esi
00C5BA4F  41 B8 43 4D 33 20               mov r8d, 0x20334d43
00C5BA55  E8 76 F0 A5 FF                  call 0x1406baad0
00C5BA5A  48 89 45 C7                     mov qword ptr [rbp - 0x39], rax
00C5BA5E  48 85 C0                        test rax, rax
00C5BA61  75 24                           jne 0x140c5ba87
00C5BA63  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
00C5BA6A  48 8D 55 AF                     lea rdx, [rbp - 0x51]
00C5BA6E  48 8B CB                        mov rcx, rbx
00C5BA71  74 0A                           je 0x140c5ba7d
00C5BA73  E8 A8 11 C0 FF                  call 0x14085cc20
00C5BA78  E9 9D FE FF FF                  jmp 0x140c5b91a
00C5BA7D  E8 BE A4 BF FF                  call 0x140855f40
00C5BA82  E9 93 FE FF FF                  jmp 0x140c5b91a
00C5BA87  4C 8B C6                        mov r8, rsi
00C5BA8A  49 8B D7                        mov rdx, r15
00C5BA8D  48 8B C8                        mov rcx, rax
00C5BA90  E8 AB AD A6 FF                  call 0x1406c6840
00C5BA95  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
00C5BA9C  48 8D 55 AF                     lea rdx, [rbp - 0x51]
00C5BAA0  66 89 75 BF                     mov word ptr [rbp - 0x41], si
00C5BAA4  48 8B CB                        mov rcx, rbx
00C5BAA7  66 89 75 C1                     mov word ptr [rbp - 0x3f], si
00C5BAAB  74 07                           je 0x140c5bab4
00C5BAAD  E8 6E 11 C0 FF                  call 0x14085cc20
00C5BAB2  EB 05                           jmp 0x140c5bab9
00C5BAB4  E8 87 A4 BF FF                  call 0x140855f40
00C5BAB9  41 83 CF FF                     or r15d, 0xffffffff
00C5BABD  48 8B 75 6F                     mov rsi, qword ptr [rbp + 0x6f]
00C5BAC1  33 D2                           xor edx, edx
00C5BAC3  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
00C5BAC7  41 B8 43 4D 34 20               mov r8d, 0x20344d43
00C5BACD  0F B7 0E                        movzx ecx, word ptr [rsi]
00C5BAD0  66 83 C1 5E                     add cx, 0x5e
00C5BAD4  66 41 03 0C 24                  add cx, word ptr [r12]
00C5BAD9  0F B7 C9                        movzx ecx, cx
00C5BADC  66 89 4D E9                     mov word ptr [rbp - 0x17], cx
00C5BAE0  E8 EB EF A5 FF                  call 0x1406baad0
00C5BAE5  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
00C5BAE9  48 85 C0                        test rax, rax
00C5BAEC  0F 84 28 FE FF FF               je 0x140c5b91a
00C5BAF2  48 8D 15 7F 66 02 00            lea rdx, [rip + 0x2667f]
00C5BAF9  48 8D 4D E7                     lea rcx, [rbp - 0x19]
00C5BAFD  E8 4E 3F 7B FF                  call 0x14040fa50
00C5BB02  85 C0                           test eax, eax
00C5BB04  0F 88 10 FE FF FF               js 0x140c5b91a
00C5BB0A  48 8B D6                        mov rdx, rsi
00C5BB0D  48 8D 4D E7                     lea rcx, [rbp - 0x19]
00C5BB11  E8 3A 3F 7B FF                  call 0x14040fa50
00C5BB16  85 C0                           test eax, eax
00C5BB18  0F 88 FC FD FF FF               js 0x140c5b91a
00C5BB1E  48 8D 15 AB 66 02 00            lea rdx, [rip + 0x266ab]
00C5BB25  48 8D 4D E7                     lea rcx, [rbp - 0x19]
00C5BB29  E8 22 3F 7B FF                  call 0x14040fa50
00C5BB2E  85 C0                           test eax, eax
00C5BB30  0F 88 E4 FD FF FF               js 0x140c5b91a
00C5BB36  49 8B D4                        mov rdx, r12
00C5BB39  48 8D 4D E7                     lea rcx, [rbp - 0x19]
00C5BB3D  E8 0E 3F 7B FF                  call 0x14040fa50
00C5BB42  45 33 E4                        xor r12d, r12d
00C5BB45  85 C0                           test eax, eax
00C5BB47  0F 88 CD FD FF FF               js 0x140c5b91a
00C5BB4D  48 8B 4F 18                     mov rcx, qword ptr [rdi + 0x18]
00C5BB51  48 85 C9                        test rcx, rcx
00C5BB54  74 0D                           je 0x140c5bb63
00C5BB56  0F B7 57 10                     movzx edx, word ptr [rdi + 0x10]
00C5BB5A  48 8B 43 20                     mov rax, qword ptr [rbx + 0x20]
00C5BB5E  E8 6D EF A5 FF                  call 0x1406baad0
00C5BB63  0F 10 45 BF                     movups xmm0, xmmword ptr [rbp - 0x41]
00C5BB67  48 8B 4F 28                     mov rcx, qword ptr [rdi + 0x28]
00C5BB6B  0F 57 C9                        xorps xmm1, xmm1
00C5BB6E  F3 0F 7F 47 10                  movdqu xmmword ptr [rdi + 0x10], xmm0
00C5BB73  0F 11 4D BF                     movups xmmword ptr [rbp - 0x41], xmm1
00C5BB77  48 85 C9                        test rcx, rcx
00C5BB7A  74 0D                           je 0x140c5bb89
00C5BB7C  0F B7 57 20                     movzx edx, word ptr [rdi + 0x20]
00C5BB80  48 8B 43 20                     mov rax, qword ptr [rbx + 0x20]
00C5BB84  E8 47 EF A5 FF                  call 0x1406baad0
00C5BB89  0F 10 45 E7                     movups xmm0, xmmword ptr [rbp - 0x19]
00C5BB8D  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
00C5BB91  0F 57 C9                        xorps xmm1, xmm1
00C5BB94  F3 0F 7F 47 20                  movdqu xmmword ptr [rdi + 0x20], xmm0
00C5BB99  48 8B 08                        mov rcx, qword ptr [rax]
00C5BB9C  0F 11 4D E7                     movups xmmword ptr [rbp - 0x19], xmm1
00C5BBA0  48 39 41 08                     cmp qword ptr [rcx + 8], rax
00C5BBA4  74 07                           je 0x140c5bbad
00C5BBA6  B9 03 00 00 00                  mov ecx, 3
00C5BBAB  CD 29                           int 0x29
00C5BBAD  48 89 0F                        mov qword ptr [rdi], rcx
00C5BBB0  4C 8D 05 89 67 02 00            lea r8, [rip + 0x26789]
00C5BBB7  48 89 47 08                     mov qword ptr [rdi + 8], rax
00C5BBBB  49 8B D5                        mov rdx, r13
00C5BBBE  48 89 79 08                     mov qword ptr [rcx + 8], rdi
00C5BBC2  4D 8B F4                        mov r14, r12
00C5BBC5  48 8B CB                        mov rcx, rbx
00C5BBC8  48 89 38                        mov qword ptr [rax], rdi
00C5BBCB  E8 4C 92 BE FF                  call 0x140844e1c
00C5BBD0  8B F0                           mov esi, eax
00C5BBD2  41 3B C7                        cmp eax, r15d
00C5BBD5  75 0F                           jne 0x140c5bbe6
00C5BBD7  C7 87 8C 00 00 00 01 00 00 00   mov dword ptr [rdi + 0x8c], 1
00C5BBE1  E9 8D 00 00 00                  jmp 0x140c5bc73
00C5BBE6  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
00C5BBED  4C 8D 45 A7                     lea r8, [rbp - 0x59]
00C5BBF1  8B D6                           mov edx, esi
00C5BBF3  48 8B CB                        mov rcx, rbx
00C5BBF6  74 07                           je 0x140c5bbff
00C5BBF8  E8 63 90 BF FF                  call 0x140854c60
00C5BBFD  EB 05                           jmp 0x140c5bc04
00C5BBFF  E8 AC 90 BF FF                  call 0x140854cb0
00C5BC04  48 85 C0                        test rax, rax
00C5BC07  0F 84 11 FD FF FF               je 0x140c5b91e
00C5BC0D  48 8D 4D CF                     lea rcx, [rbp - 0x31]
00C5BC11  4C 8B C0                        mov r8, rax
00C5BC14  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00C5BC19  4C 8D 4D 9F                     lea r9, [rbp - 0x61]
00C5BC1D  48 8B CB                        mov rcx, rbx
00C5BC20  8B D6                           mov edx, esi
00C5BC22  E8 0D 7D B9 FF                  call 0x1407f3934
00C5BC27  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
00C5BC2E  48 8D 55 A7                     lea rdx, [rbp - 0x59]
00C5BC32  48 8B F0                        mov rsi, rax
00C5BC35  48 8B CB                        mov rcx, rbx
00C5BC38  74 07                           je 0x140c5bc41
00C5BC3A  E8 E1 0F C0 FF                  call 0x14085cc20
00C5BC3F  EB 05                           jmp 0x140c5bc46
00C5BC41  E8 FA A2 BF FF                  call 0x140855f40
00C5BC46  48 85 F6                        test rsi, rsi
00C5BC49  0F 84 CF FC FF FF               je 0x140c5b91e
00C5BC4F  8B 06                           mov eax, dword ptr [rsi]
00C5BC51  48 8D 55 CF                     lea rdx, [rbp - 0x31]
00C5BC55  89 87 8C 00 00 00               mov dword ptr [rdi + 0x8c], eax
00C5BC5B  48 8B CB                        mov rcx, rbx
00C5BC5E  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
00C5BC65  74 07                           je 0x140c5bc6e
00C5BC67  E8 B4 0F C0 FF                  call 0x14085cc20
00C5BC6C  EB 05                           jmp 0x140c5bc73
00C5BC6E  E8 CD A2 BF FF                  call 0x140855f40
00C5BC73  4C 8D 05 D6 66 02 00            lea r8, [rip + 0x266d6]
00C5BC7A  49 8B D5                        mov rdx, r13
00C5BC7D  48 8B CB                        mov rcx, rbx
00C5BC80  E8 97 91 BE FF                  call 0x140844e1c
00C5BC85  8B F0                           mov esi, eax
00C5BC87  41 3B C7                        cmp eax, r15d
00C5BC8A  75 0D                           jne 0x140c5bc99
00C5BC8C  44 89 67 68                     mov dword ptr [rdi + 0x68], r12d
00C5BC90  4C 89 67 70                     mov qword ptr [rdi + 0x70], r12
00C5BC94  E9 A1 00 00 00                  jmp 0x140c5bd3a
00C5BC99  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
00C5BCA0  4C 8D 45 A7                     lea r8, [rbp - 0x59]
00C5BCA4  8B D6                           mov edx, esi
00C5BCA6  48 8B CB                        mov rcx, rbx
00C5BCA9  74 07                           je 0x140c5bcb2
00C5BCAB  E8 B0 8F BF FF                  call 0x140854c60
00C5BCB0  EB 05                           jmp 0x140c5bcb7
00C5BCB2  E8 F9 8F BF FF                  call 0x140854cb0
00C5BCB7  48 85 C0                        test rax, rax
00C5BCBA  0F 84 5E FC FF FF               je 0x140c5b91e
00C5BCC0  48 8D 4D D7                     lea rcx, [rbp - 0x29]
00C5BCC4  4C 8B C0                        mov r8, rax
00C5BCC7  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00C5BCCC  4C 8D 4D 9F                     lea r9, [rbp - 0x61]
00C5BCD0  48 8B CB                        mov rcx, rbx
00C5BCD3  8B D6                           mov edx, esi
00C5BCD5  E8 5A 7C B9 FF                  call 0x1407f3934
00C5BCDA  48 89 47 70                     mov qword ptr [rdi + 0x70], rax
00C5BCDE  48 8D 55 A7                     lea rdx, [rbp - 0x59]
00C5BCE2  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
00C5BCE9  48 8B CB                        mov rcx, rbx
00C5BCEC  74 07                           je 0x140c5bcf5
00C5BCEE  E8 2D 0F C0 FF                  call 0x14085cc20
00C5BCF3  EB 05                           jmp 0x140c5bcfa
00C5BCF5  E8 46 A2 BF FF                  call 0x140855f40
00C5BCFA  4C 39 67 70                     cmp qword ptr [rdi + 0x70], r12
00C5BCFE  0F 84 1A FC FF FF               je 0x140c5b91e
00C5BD04  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
00C5BD0B  48 8D 55 D7                     lea rdx, [rbp - 0x29]
00C5BD0F  48 8B CB                        mov rcx, rbx
00C5BD12  74 07                           je 0x140c5bd1b
00C5BD14  E8 07 0F C0 FF                  call 0x14085cc20
00C5BD19  EB 05                           jmp 0x140c5bd20
00C5BD1B  E8 20 A2 BF FF                  call 0x140855f40
00C5BD20  0F B7 45 9F                     movzx eax, word ptr [rbp - 0x61]
00C5BD24  66 83 E8 02                     sub ax, 2
00C5BD28  66 89 47 68                     mov word ptr [rdi + 0x68], ax
00C5BD2C  66 3B 45 9F                     cmp ax, word ptr [rbp - 0x61]
00C5BD30  0F 87 E8 FB FF FF               ja 0x140c5b91e
00C5BD36  66 89 47 6A                     mov word ptr [rdi + 0x6a], ax
00C5BD3A  4C 8D 05 1F 65 02 00            lea r8, [rip + 0x2651f]
00C5BD41  49 8B D5                        mov rdx, r13
00C5BD44  48 8B CB                        mov rcx, rbx
00C5BD47  E8 D0 90 BE FF                  call 0x140844e1c
00C5BD4C  8B F0                           mov esi, eax
00C5BD4E  41 3B C7                        cmp eax, r15d
00C5BD51  75 0D                           jne 0x140c5bd60
00C5BD53  44 89 67 58                     mov dword ptr [rdi + 0x58], r12d
00C5BD57  4C 89 67 60                     mov qword ptr [rdi + 0x60], r12
00C5BD5B  E9 A1 00 00 00                  jmp 0x140c5be01
00C5BD60  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
00C5BD67  4C 8D 45 A7                     lea r8, [rbp - 0x59]
00C5BD6B  8B D6                           mov edx, esi
00C5BD6D  48 8B CB                        mov rcx, rbx
00C5BD70  74 07                           je 0x140c5bd79
00C5BD72  E8 E9 8E BF FF                  call 0x140854c60
00C5BD77  EB 05                           jmp 0x140c5bd7e
00C5BD79  E8 32 8F BF FF                  call 0x140854cb0
00C5BD7E  48 85 C0                        test rax, rax
00C5BD81  0F 84 97 FB FF FF               je 0x140c5b91e
00C5BD87  48 8D 4D DF                     lea rcx, [rbp - 0x21]
00C5BD8B  4C 8B C0                        mov r8, rax
00C5BD8E  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00C5BD93  4C 8D 4D 9F                     lea r9, [rbp - 0x61]
00C5BD97  48 8B CB                        mov rcx, rbx
00C5BD9A  8B D6                           mov edx, esi
00C5BD9C  E8 93 7B B9 FF                  call 0x1407f3934
00C5BDA1  48 89 47 60                     mov qword ptr [rdi + 0x60], rax
00C5BDA5  48 8D 55 A7                     lea rdx, [rbp - 0x59]
00C5BDA9  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
00C5BDB0  48 8B CB                        mov rcx, rbx
00C5BDB3  74 07                           je 0x140c5bdbc
00C5BDB5  E8 66 0E C0 FF                  call 0x14085cc20
00C5BDBA  EB 05                           jmp 0x140c5bdc1
00C5BDBC  E8 7F A1 BF FF                  call 0x140855f40
00C5BDC1  4C 39 67 60                     cmp qword ptr [rdi + 0x60], r12
00C5BDC5  0F 84 53 FB FF FF               je 0x140c5b91e
00C5BDCB  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
00C5BDD2  48 8D 55 DF                     lea rdx, [rbp - 0x21]
00C5BDD6  48 8B CB                        mov rcx, rbx
00C5BDD9  74 07                           je 0x140c5bde2
00C5BDDB  E8 40 0E C0 FF                  call 0x14085cc20
00C5BDE0  EB 05                           jmp 0x140c5bde7
00C5BDE2  E8 59 A1 BF FF                  call 0x140855f40
00C5BDE7  0F B7 45 9F                     movzx eax, word ptr [rbp - 0x61]
00C5BDEB  66 83 E8 02                     sub ax, 2
00C5BDEF  66 89 47 58                     mov word ptr [rdi + 0x58], ax
00C5BDF3  66 3B 45 9F                     cmp ax, word ptr [rbp - 0x61]
00C5BDF7  0F 87 21 FB FF FF               ja 0x140c5b91e
00C5BDFD  66 89 47 5A                     mov word ptr [rdi + 0x5a], ax
00C5BE01  4C 8D 05 A8 64 02 00            lea r8, [rip + 0x264a8]
00C5BE08  49 8B D5                        mov rdx, r13
00C5BE0B  48 8B CB                        mov rcx, rbx
00C5BE0E  E8 09 90 BE FF                  call 0x140844e1c
00C5BE13  41 3B C7                        cmp eax, r15d
00C5BE16  74 16                           je 0x140c5be2e
00C5BE18  44 8B 45 67                     mov r8d, dword ptr [rbp + 0x67]
00C5BE1C  4C 8D 4F 68                     lea r9, [rdi + 0x68]
00C5BE20  48 8B 4D 5F                     mov rcx, qword ptr [rbp + 0x5f]
00C5BE24  8B D0                           mov edx, eax
00C5BE26  E8 FD 07 00 00                  call 0x140c5c628
00C5BE2B  44 8B F8                        mov r15d, eax
00C5BE2E  B8 88 00 00 00                  mov eax, 0x88
00C5BE33  48 8B CF                        mov rcx, rdi
00C5BE36  41 B4 01                        mov r12b, 1
00C5BE39  44 89 3C 01                     mov dword ptr [rcx + rax], r15d
00C5BE3D  E9 DC FA FF FF                  jmp 0x140c5b91e
00C5BE42  0F B7 55 4F                     movzx edx, word ptr [rbp + 0x4f]
00C5BE46  48 8B CE                        mov rcx, rsi
00C5BE49  48 8B 43 20                     mov rax, qword ptr [rbx + 0x20]
00C5BE4D  E8 7E EC A5 FF                  call 0x1406baad0
00C5BE52  E9 C7 FA FF FF                  jmp 0x140c5b91e
00C5BE57  E8 E4 A0 BF FF                  call 0x140855f40
00C5BE5C  48 8B 9C 24 E8 00 00 00         mov rbx, qword ptr [rsp + 0xe8]
00C5BE64  41 8A C4                        mov al, r12b
00C5BE67  48 81 C4 A0 00 00 00            add rsp, 0xa0
00C5BE6E  41 5F                           pop r15
00C5BE70  41 5E                           pop r14
00C5BE72  41 5D                           pop r13
00C5BE74  41 5C                           pop r12
00C5BE76  5F                              pop rdi
00C5BE77  5E                              pop rsi
00C5BE78  5D                              pop rbp
00C5BE79  C3                              ret
00C5BE7A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpAddDriverToList(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_p10;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned int *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    v_rsp = (v_rsp) - (160);
    v_r15 = (unsigned int)((v_r15) | (0xFFFFFFFFULL));
    *(unsigned int *)(v_rsp - 71 - 73) = (unsigned int)(v_r15);
    a1 = 0;
    *(unsigned int *)(v_rsp - 71 - 33) = (unsigned int)(v_r15);
    *(unsigned int *)(v_rsp - 71 - 69) = 0;
    *(unsigned int *)(v_rsp - 71 - 29) = 0;
    *(unsigned int *)(v_rsp - 71 - 37) = 0;
    *(unsigned int *)(v_rsp - 71 - 97) = 0;
    *(unsigned int *)(v_rsp - 71 - 45) = 0;
    *(unsigned int *)(v_rsp - 71 - 77) = 0;
    *(unsigned int *)(v_rsp - 71 - 85) = 0;
    *(unsigned __int16 *)(v_rsp - 71 + 79) = 0;
    *(unsigned __int8 *)(v_rsp - 71 + 127) = 0;
    *(unsigned int *)(v_rsp - 71 - 41) = (unsigned int)(v_r15);
    *(unsigned int *)(v_rsp - 71 - 49) = (unsigned int)(v_r15);
    *(unsigned int *)(v_rsp - 71 - 81) = (unsigned int)(v_r15);
    *(unsigned __int64 *)(v_rsp - 71 - 9) = v_xmm0;
    *(unsigned int *)(v_rsp - 71 - 89) = (unsigned int)(v_r15);
    *(unsigned __int64 *)(v_rsp - 71 - 65) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 71 - 25) = v_xmm1;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_00C5B7EB;
    result = HvpGetCellFlat(0, a2, v_rsp - 71 - 73, a4);
    goto loc_00C5B7F0;
loc_00C5B7EB:
    result = HvpGetCellPaged(0, a2, v_rsp - 71 - 73, a4);
loc_00C5B7F0:
    if (result == 0) goto loc_00C5B91E;
    result = CmpGetNodeName(0, result, v_rsp - 71 + 79, a4);
    if (result == 0) goto loc_00C5B91E;
    result = RtlInitUnicodeStringEx(v_rsp - 71 - 9, result, v_rsp - 71 + 79, a4);
    if (sign_flag) goto loc_00C5BE42;
    a2 = 0;
    result = guard_dispatch_icall(144, a2, (unsigned int)(0x20314D43ULL), a4);
    if (result == 0) goto loc_00C5BE42;
    a2 = 0;
    result = memset(result, a2, 144, a4);
    *(unsigned __int64 *)(result + 64) = 0;
    result = 0;
    *(unsigned __int64 *)(result + 72) = v_xmm0;
    *(unsigned __int64 *)(result + 40) = 0;
    *(unsigned __int64 *)(result + 24) = 0;
    *(unsigned __int64 *)(result + 128) = 0;
    *(unsigned __int16 *)(result + 120) = (unsigned __int16)(*(unsigned __int16 *)(v_rsp - 71 + 79) - 2);
    *(unsigned __int16 *)(result + 122) = (unsigned __int16)(*(unsigned __int16 *)(v_rsp - 71 + 79));
    result = CmpFindValueByName(0, result, v_rip + 158368, a4);
    if (((unsigned int)(result)) != ((unsigned int)(v_r15))) goto loc_00C5B9DB;
    a2 = 0;
    a1 = (unsigned int)((*(unsigned __int16 *)(result + 120)) + (46));
    *(unsigned __int16 *)(v_rsp - 71 - 63) = (unsigned __int16)(a1);
    result = guard_dispatch_icall(a1, a2, (unsigned int)(0x20334D43ULL), a4);
    v_rsi = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 57) = result;
    if (result == 0) goto loc_00C5B9D3;
    result = RtlAppendUnicodeToString(v_rsp - 71 - 65, v_rip + 142475, (unsigned int)(0x20334D43ULL), a4);
    if (sign_flag) goto loc_00C5B91A;
    result = RtlAppendUnicodeStringToString(v_rsp - 71 - 65, result + 120, (unsigned int)(0x20334D43ULL), a4);
    if (sign_flag) goto loc_00C5B91A;
    result = RtlAppendUnicodeToString(v_rsp - 71 - 65, v_rip + 142487, (unsigned int)(0x20334D43ULL), a4);
    if (!sign_flag) goto loc_00C5BABD;
loc_00C5B91A:
loc_00C5B91E:
    if (*(unsigned __int64 *)(v_rsp - 71 - 57) != 0) {
        a2 = *(unsigned __int16 *)(v_rsp - 71 - 65);
        result = *(unsigned __int64 *)(a1 + 32);
        result = guard_dispatch_icall(*(unsigned __int64 *)(v_rsp - 71 - 57), a2, (unsigned int)(0x20334D43ULL), a4);
    }
    if (*(unsigned __int64 *)(v_rsp - 71 - 17) != 0) {
        a2 = *(unsigned __int16 *)(v_rsp - 71 - 25);
        result = *(unsigned __int64 *)(a1 + 32);
        result = guard_dispatch_icall(*(unsigned __int64 *)(v_rsp - 71 - 17), a2, (unsigned int)(0x20334D43ULL), a4);
    }
    if (result == 0) goto loc_00C5B9AC;
    v_r15 = a1 + 32;
    if (*(unsigned __int64 *)(result + 24) != 0) {
        a2 = *(unsigned __int16 *)(result + 16);
        result = *(unsigned __int64 *)(a1 + 32);
        result = guard_dispatch_icall(*(unsigned __int64 *)(result + 24), a2, (unsigned int)(0x20334D43ULL), a4);
        v_r15 = a1 + 32;
    }
    if (*(unsigned __int64 *)(result + 40) != 0) {
        a2 = *(unsigned __int16 *)(result + 32);
        result = *(unsigned __int64 *)(a1 + 32);
        result = guard_dispatch_icall(*(unsigned __int64 *)(result + 40), a2, (unsigned int)(0x20334D43ULL), a4);
    }
    if (*(unsigned __int64 *)(result + 128) != 0) {
        a2 = *(unsigned __int16 *)(result + 120);
        result = *(unsigned __int64 *)(v_r15);
        result = guard_dispatch_icall(*(unsigned __int64 *)(result + 128), a2, (unsigned int)(0x20334D43ULL), a4);
    }
    result = guard_dispatch_icall(result, 144, (unsigned int)(0x20334D43ULL), a4);
loc_00C5B9AC:
    if (result == 0) goto loc_00C5BE5C;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_00C5BE57;
    result = HvpReleaseCellFlat(a1, v_rsp - 71 - 73, (unsigned int)(0x20334D43ULL), a4);
    goto loc_00C5BE5C;
loc_00C5B9D3:
    goto loc_00C5B91E;
loc_00C5B9DB:
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_00C5B9F4;
    result = HvpGetCellFlat(a1, (unsigned int)((unsigned int)(a1 + 32)), v_rsp - 71 - 89, a4);
    goto loc_00C5B9F9;
loc_00C5B9F4:
    result = HvpGetCellPaged(a1, (unsigned int)((unsigned int)(a1 + 32)), v_rsp - 71 - 89, a4);
loc_00C5B9F9:
    if (result == 0) goto loc_00C5B91A;
    v_stack_mB8 = v_rsp - 71 - 81;
    result = CmpValueToData(a1, (unsigned int)((unsigned int)(a1 + 32)), result, v_rsp - 71 - 97);
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_00C5BA36;
    result = HvpReleaseCellFlat(a1, v_rsp - 71 - 89, result, v_rsp - 71 - 97);
    goto loc_00C5BA3B;
loc_00C5BA36:
    result = HvpReleaseCellPaged(a1, v_rsp - 71 - 89, result, v_rsp - 71 - 97);
loc_00C5BA3B:
    if (result == 0) goto loc_00C5B91A;
    a2 = 0;
    result = guard_dispatch_icall((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 97)))), a2, (unsigned int)(0x20334D43ULL), v_rsp - 71 - 97);
    *(unsigned __int64 *)(v_rsp - 71 - 57) = result;
    if (result != 0) goto loc_00C5BA87;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_00C5BA7D;
    result = HvpReleaseCellFlat(a1, v_rsp - 71 - 81, (unsigned int)(0x20334D43ULL), v_rsp - 71 - 97);
    goto loc_00C5B91A;
loc_00C5BA7D:
    result = HvpReleaseCellPaged(a1, v_rsp - 71 - 81, (unsigned int)(0x20334D43ULL), v_rsp - 71 - 97);
    goto loc_00C5B91A;
loc_00C5BA87:
    result = memcpy(result, result, (unsigned int)(*(unsigned int *)(v_rsp - 71 - 97)), v_rsp - 71 - 97);
    *(unsigned __int16 *)(v_rsp - 71 - 65) = (unsigned __int16)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 97)));
    *(unsigned __int16 *)(v_rsp - 71 - 63) = (unsigned __int16)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 97)));
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_00C5BAB4;
    result = HvpReleaseCellFlat(a1, v_rsp - 71 - 81, (unsigned int)(*(unsigned int *)(v_rsp - 71 - 97)), v_rsp - 71 - 97);
    goto loc_00C5BAB9;
loc_00C5BAB4:
    result = HvpReleaseCellPaged(a1, v_rsp - 71 - 81, (unsigned int)(*(unsigned int *)(v_rsp - 71 - 97)), v_rsp - 71 - 97);
loc_00C5BAB9:
    v_r15 = (unsigned int)((result) | (0xFFFFFFFFULL));
loc_00C5BABD:
    a2 = 0;
    a1 = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 71 + 111))) + (94));
    a1 = (unsigned __int16)((a1) + (*(unsigned __int16 *)((unsigned __int8)(a1 + 32))));
    *(unsigned __int16 *)(v_rsp - 71 - 23) = (unsigned __int16)((unsigned __int16)(a1));
    result = guard_dispatch_icall((unsigned __int16)(a1), a2, (unsigned int)(0x20344D43ULL), v_rsp - 71 - 97);
    *(unsigned __int64 *)(v_rsp - 71 - 17) = result;
    if (result == 0) goto loc_00C5B91A;
    result = RtlAppendUnicodeStringToString(v_rsp - 71 - 25, v_rip + 157311, (unsigned int)(0x20344D43ULL), v_rsp - 71 - 97);
    if (sign_flag) goto loc_00C5B91A;
    result = RtlAppendUnicodeStringToString(v_rsp - 71 - 25, *(unsigned __int64 *)(v_rsp - 71 + 111), (unsigned int)(0x20344D43ULL), v_rsp - 71 - 97);
    if (sign_flag) goto loc_00C5B91A;
    result = RtlAppendUnicodeStringToString(v_rsp - 71 - 25, v_rip + 157355, (unsigned int)(0x20344D43ULL), v_rsp - 71 - 97);
    if (sign_flag) goto loc_00C5B91A;
    result = RtlAppendUnicodeStringToString(v_rsp - 71 - 25, (unsigned __int8)(a1 + 32), (unsigned int)(0x20344D43ULL), v_rsp - 71 - 97);
    v_r12 = 0;
    if (sign_flag) goto loc_00C5B91A;
    if (*(unsigned __int64 *)(result + 24) != 0) {
        a2 = *(unsigned __int16 *)(result + 16);
        result = *(unsigned __int64 *)(a1 + 32);
        result = guard_dispatch_icall(*(unsigned __int64 *)(result + 24), a2, (unsigned int)(0x20344D43ULL), v_rsp - 71 - 97);
    }
    *(unsigned __int64 *)(result + 16) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 71 - 65) = v_xmm1;
    if (*(unsigned __int64 *)(result + 40) != 0) {
        a2 = *(unsigned __int16 *)(result + 32);
        result = *(unsigned __int64 *)(a1 + 32);
        result = guard_dispatch_icall(*(unsigned __int64 *)(result + 40), a2, (unsigned int)(0x20344D43ULL), v_rsp - 71 - 97);
    }
    *(unsigned __int64 *)(result + 32) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 71 - 25) = v_xmm1;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 119)) + 8)) != (*(unsigned __int64 *)(v_rsp - 71 + 119))) {
        a1 = 3;
    }
    *(unsigned __int64 *)(result) = a1;
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)(v_rsp - 71 + 119);
    *(unsigned __int64 *)(a1 + 8) = result;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 119)) = result;
    result = CmpFindValueByName(a1, result, v_rip + 157577, v_rsp - 71 - 97);
    if (((unsigned int)(result)) != ((unsigned int)(v_r15))) goto loc_00C5BBE6;
    *(unsigned int *)(result + 140) = 1;
    goto loc_00C5BC73;
loc_00C5BBE6:
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_00C5BBFF;
    result = HvpGetCellFlat(a1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_rsp - 71 - 89, v_rsp - 71 - 97);
    goto loc_00C5BC04;
loc_00C5BBFF:
    result = HvpGetCellPaged(a1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_rsp - 71 - 89, v_rsp - 71 - 97);
loc_00C5BC04:
    if (result == 0) goto loc_00C5B91E;
    v_stack_mB8 = v_rsp - 71 - 49;
    result = CmpValueToData(a1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), result, v_rsp - 71 - 97);
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_00C5BC41;
    result = HvpReleaseCellFlat(a1, v_rsp - 71 - 89, result, v_rsp - 71 - 97);
    goto loc_00C5BC46;
loc_00C5BC41:
    result = HvpReleaseCellPaged(a1, v_rsp - 71 - 89, result, v_rsp - 71 - 97);
loc_00C5BC46:
    if (result == 0) goto loc_00C5B91E;
    *(unsigned int *)(result + 140) = (unsigned int)((unsigned int)(*(unsigned int *)(result)));
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_00C5BC6E;
    result = HvpReleaseCellFlat(a1, v_rsp - 71 - 49, result, v_rsp - 71 - 97);
    goto loc_00C5BC73;
loc_00C5BC6E:
    result = HvpReleaseCellPaged(a1, v_rsp - 71 - 49, result, v_rsp - 71 - 97);
loc_00C5BC73:
    result = CmpFindValueByName(a1, result, v_rip + 157398, v_rsp - 71 - 97);
    if (((unsigned int)(result)) != ((unsigned int)(v_r15))) goto loc_00C5BC99;
    *(unsigned int *)(result + 104) = 0;
    *(unsigned __int64 *)(result + 112) = 0;
    goto loc_00C5BD3A;
loc_00C5BC99:
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_00C5BCB2;
    result = HvpGetCellFlat(a1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_rsp - 71 - 89, v_rsp - 71 - 97);
    goto loc_00C5BCB7;
loc_00C5BCB2:
    result = HvpGetCellPaged(a1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_rsp - 71 - 89, v_rsp - 71 - 97);
loc_00C5BCB7:
    if (result == 0) goto loc_00C5B91E;
    v_stack_mB8 = v_rsp - 71 - 41;
    result = CmpValueToData(a1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), result, v_rsp - 71 - 97);
    *(unsigned __int64 *)(result + 112) = result;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_00C5BCF5;
    result = HvpReleaseCellFlat(a1, v_rsp - 71 - 89, result, v_rsp - 71 - 97);
    goto loc_00C5BCFA;
loc_00C5BCF5:
    result = HvpReleaseCellPaged(a1, v_rsp - 71 - 89, result, v_rsp - 71 - 97);
loc_00C5BCFA:
    if ((*(unsigned __int64 *)(result + 112)) == 0) goto loc_00C5B91E;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_00C5BD1B;
    result = HvpReleaseCellFlat(a1, v_rsp - 71 - 41, result, v_rsp - 71 - 97);
    goto loc_00C5BD20;
loc_00C5BD1B:
    result = HvpReleaseCellPaged(a1, v_rsp - 71 - 41, result, v_rsp - 71 - 97);
loc_00C5BD20:
    result = (unsigned __int16)((*(unsigned __int16 *)(v_rsp - 71 - 97)) - (2));
    *(unsigned __int16 *)(result + 104) = (unsigned __int16)(result);
    if (((unsigned __int16)(result)) > (*(unsigned __int16 *)(v_rsp - 71 - 97))) goto loc_00C5B91E;
    *(unsigned __int16 *)(result + 106) = (unsigned __int16)(result);
loc_00C5BD3A:
    result = CmpFindValueByName(a1, result, v_rip + 156959, v_rsp - 71 - 97);
    if (((unsigned int)(result)) != ((unsigned int)(v_r15))) goto loc_00C5BD60;
    *(unsigned int *)(result + 88) = 0;
    *(unsigned __int64 *)(result + 96) = 0;
    goto loc_00C5BE01;
loc_00C5BD60:
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_00C5BD79;
    result = HvpGetCellFlat(a1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_rsp - 71 - 89, v_rsp - 71 - 97);
    goto loc_00C5BD7E;
loc_00C5BD79:
    result = HvpGetCellPaged(a1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_rsp - 71 - 89, v_rsp - 71 - 97);
loc_00C5BD7E:
    if (result == 0) goto loc_00C5B91E;
    v_stack_mB8 = v_rsp - 71 - 33;
    result = CmpValueToData(a1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), result, v_rsp - 71 - 97);
    *(unsigned __int64 *)(result + 96) = result;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_00C5BDBC;
    result = HvpReleaseCellFlat(a1, v_rsp - 71 - 89, result, v_rsp - 71 - 97);
    goto loc_00C5BDC1;
loc_00C5BDBC:
    result = HvpReleaseCellPaged(a1, v_rsp - 71 - 89, result, v_rsp - 71 - 97);
loc_00C5BDC1:
    if ((*(unsigned __int64 *)(result + 96)) == 0) goto loc_00C5B91E;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_00C5BDE2;
    result = HvpReleaseCellFlat(a1, v_rsp - 71 - 33, result, v_rsp - 71 - 97);
    goto loc_00C5BDE7;
loc_00C5BDE2:
    result = HvpReleaseCellPaged(a1, v_rsp - 71 - 33, result, v_rsp - 71 - 97);
loc_00C5BDE7:
    result = (unsigned __int16)((*(unsigned __int16 *)(v_rsp - 71 - 97)) - (2));
    *(unsigned __int16 *)(result + 88) = (unsigned __int16)(result);
    if (((unsigned __int16)(result)) > (*(unsigned __int16 *)(v_rsp - 71 - 97))) goto loc_00C5B91E;
    *(unsigned __int16 *)(result + 90) = (unsigned __int16)(result);
loc_00C5BE01:
    result = CmpFindValueByName(a1, result, v_rip + 156840, v_rsp - 71 - 97);
    if (((unsigned int)(result)) != ((unsigned int)(v_r15))) {
        a3 = *(unsigned int *)(v_rsp - 71 + 103);
        a4 = result + 104;
        a1 = *(unsigned __int64 *)(v_rsp - 71 + 95);
        a2 = (unsigned int)(result);
        result = CmpFindTagIndex(a1, a2, a3, a4);
        v_r15 = (unsigned int)(result);
    }
    *(unsigned int *)(result + 136 * 1) = (unsigned int)(v_r15);
    goto loc_00C5B91E;
loc_00C5BE42:
    result = guard_dispatch_icall((unsigned int)((unsigned int)(result)), *(unsigned __int16 *)(v_rsp - 71 + 79), a3, a4);
    goto loc_00C5B91E;
loc_00C5BE57:
    result = HvpReleaseCellPaged((unsigned int)((unsigned int)(result)), *(unsigned __int16 *)(v_rsp - 71 + 79), a3, a4);
loc_00C5BE5C:
    v_rsp = (v_rsp) + (160);
    return 1;
}
```

## 5. (Beta) C Style

```c
int64_t CmpAddDriverToList(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_mB8;
    uint64_t v_stack_p10;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    local_rsp = (local_rsp) - (160);
    local_r15 = (uint32_t)((local_r15) | (0xFFFFFFFFULL));
    *(uint32_t *)(local_rsp - 0x47 - 0x49) = (uint32_t)(local_r15);
    Arg1 = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x21) = (uint32_t)(local_r15);
    *(uint32_t *)(local_rsp - 0x47 - 0x45) = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x1D) = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x25) = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x61) = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x2D) = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x4D) = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x55) = 0;
    *(uint16_t *)(local_rsp - 0x47 + 0x4F) = 0;
    *(uint8_t *)(local_rsp - 0x47 + 0x7F) = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x29) = (uint32_t)(local_r15);
    *(uint32_t *)(local_rsp - 0x47 - 0x31) = (uint32_t)(local_r15);
    *(uint32_t *)(local_rsp - 0x47 - 0x51) = (uint32_t)(local_r15);
    *(uint64_t *)(local_rsp - 0x47 - 0x9) = v_xmm0;
    *(uint32_t *)(local_rsp - 0x47 - 0x59) = (uint32_t)(local_r15);
    *(uint64_t *)(local_rsp - 0x47 - 0x41) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x47 - 0x19) = v_xmm1;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_00C5B7EB;
    result = HvpGetCellFlat(0, Arg2, local_rsp - 71 - 73, Arg4);
    goto loc_00C5B7F0;
loc_00C5B7EB:
    result = HvpGetCellPaged(0, Arg2, local_rsp - 71 - 73, Arg4);
loc_00C5B7F0:
    if (result == 0) goto loc_00C5B91E;
    result = CmpGetNodeName(0, result, local_rsp - 71 + 79, Arg4);
    if (result == 0) goto loc_00C5B91E;
    result = RtlInitUnicodeStringEx(local_rsp - 71 - 9, result, local_rsp - 71 + 79, Arg4);
    if (sign_flag) goto loc_00C5BE42;
    Arg2 = 0;
    result = guard_dispatch_icall(144, Arg2, (uint32_t)(0x20314D43ULL), Arg4);
    if (result == 0) goto loc_00C5BE42;
    Arg2 = 0;
    result = memset(result, Arg2, 144, Arg4);
    *(uint64_t *)(result + 0x40) = 0;
    result = 0;
    *(uint64_t *)(result + 0x48) = v_xmm0;
    *(uint64_t *)(result + 0x28) = 0;
    *(uint64_t *)(result + 0x18) = 0;
    *(uint64_t *)(result + 0x80) = 0;
    *(uint16_t *)(result + 0x78) = (uint16_t)(*(uint16_t *)(local_rsp - 0x47 + 0x4F) - 2);
    *(uint16_t *)(result + 0x7A) = (uint16_t)(*(uint16_t *)(local_rsp - 0x47 + 0x4F));
    result = CmpFindValueByName(0, result, v_rip + 158368, Arg4);
    if (((uint32_t)(result)) != ((uint32_t)(local_r15))) goto loc_00C5B9DB;
    Arg2 = 0;
    Arg1 = (uint32_t)((*(uint16_t *)(result + 0x78)) + (46));
    *(uint16_t *)(local_rsp - 0x47 - 0x3F) = (uint16_t)(Arg1);
    result = guard_dispatch_icall(Arg1, Arg2, (uint32_t)(0x20334D43ULL), Arg4);
    local_rsi = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x39) = result;
    if (result == 0) goto loc_00C5B9D3;
    result = RtlAppendUnicodeToString(local_rsp - 71 - 65, v_rip + 142475, (uint32_t)(0x20334D43ULL), Arg4);
    if (sign_flag) goto loc_00C5B91A;
    result = RtlAppendUnicodeStringToString(local_rsp - 71 - 65, result + 120, (uint32_t)(0x20334D43ULL), Arg4);
    if (sign_flag) goto loc_00C5B91A;
    result = RtlAppendUnicodeToString(local_rsp - 71 - 65, v_rip + 142487, (uint32_t)(0x20334D43ULL), Arg4);
    if (!sign_flag) goto loc_00C5BABD;
loc_00C5B91A:
loc_00C5B91E:
    if (*(uint64_t *)(local_rsp - 0x47 - 0x39) != 0) {
        Arg2 = *(uint16_t *)(local_rsp - 0x47 - 0x41);
        result = *(uint64_t *)(arg1 + 0x20);
        result = guard_dispatch_icall(*(uint64_t *)(local_rsp - 0x47 - 0x39), Arg2, (uint32_t)(0x20334D43ULL), Arg4);
    }
    if (*(uint64_t *)(local_rsp - 0x47 - 0x11) != 0) {
        Arg2 = *(uint16_t *)(local_rsp - 0x47 - 0x19);
        result = *(uint64_t *)(arg1 + 0x20);
        result = guard_dispatch_icall(*(uint64_t *)(local_rsp - 0x47 - 0x11), Arg2, (uint32_t)(0x20334D43ULL), Arg4);
    }
    if (result == 0) goto loc_00C5B9AC;
    local_r15 = Arg1 + 32;
    if (*(uint64_t *)(result + 0x18) != 0) {
        Arg2 = *(uint16_t *)(result + 0x10);
        result = *(uint64_t *)(arg1 + 0x20);
        result = guard_dispatch_icall(*(uint64_t *)(result + 0x18), Arg2, (uint32_t)(0x20334D43ULL), Arg4);
        local_r15 = Arg1 + 32;
    }
    if (*(uint64_t *)(result + 0x28) != 0) {
        Arg2 = *(uint16_t *)(result + 0x20);
        result = *(uint64_t *)(arg1 + 0x20);
        result = guard_dispatch_icall(*(uint64_t *)(result + 0x28), Arg2, (uint32_t)(0x20334D43ULL), Arg4);
    }
    if (*(uint64_t *)(result + 0x80) != 0) {
        Arg2 = *(uint16_t *)(result + 0x78);
        result = *(uint64_t *)(local_r15);
        result = guard_dispatch_icall(*(uint64_t *)(result + 0x80), Arg2, (uint32_t)(0x20334D43ULL), Arg4);
    }
    result = guard_dispatch_icall(result, 144, (uint32_t)(0x20334D43ULL), Arg4);
loc_00C5B9AC:
    if (result == 0) goto loc_00C5BE5C;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_00C5BE57;
    result = HvpReleaseCellFlat(Arg1, local_rsp - 71 - 73, (uint32_t)(0x20334D43ULL), Arg4);
    goto loc_00C5BE5C;
loc_00C5B9D3:
    goto loc_00C5B91E;
loc_00C5B9DB:
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_00C5B9F4;
    result = HvpGetCellFlat(Arg1, (uint32_t)((uint32_t)(Arg1 + 32)), local_rsp - 71 - 89, Arg4);
    goto loc_00C5B9F9;
loc_00C5B9F4:
    result = HvpGetCellPaged(Arg1, (uint32_t)((uint32_t)(Arg1 + 32)), local_rsp - 71 - 89, Arg4);
loc_00C5B9F9:
    if (result == 0) goto loc_00C5B91A;
    v_stack_mB8 = local_rsp - 71 - 81;
    result = CmpValueToData(Arg1, (uint32_t)((uint32_t)(Arg1 + 32)), result, local_rsp - 71 - 97);
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_00C5BA36;
    result = HvpReleaseCellFlat(Arg1, local_rsp - 71 - 89, result, local_rsp - 71 - 97);
    goto loc_00C5BA3B;
loc_00C5BA36:
    result = HvpReleaseCellPaged(Arg1, local_rsp - 71 - 89, result, local_rsp - 71 - 97);
loc_00C5BA3B:
    if (result == 0) goto loc_00C5B91A;
    Arg2 = 0;
    result = guard_dispatch_icall((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x61)))), Arg2, (uint32_t)(0x20334D43ULL), local_rsp - 71 - 97);
    *(uint64_t *)(local_rsp - 0x47 - 0x39) = result;
    if (result != 0) goto loc_00C5BA87;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_00C5BA7D;
    result = HvpReleaseCellFlat(Arg1, local_rsp - 71 - 81, (uint32_t)(0x20334D43ULL), local_rsp - 71 - 97);
    goto loc_00C5B91A;
loc_00C5BA7D:
    result = HvpReleaseCellPaged(Arg1, local_rsp - 71 - 81, (uint32_t)(0x20334D43ULL), local_rsp - 71 - 97);
    goto loc_00C5B91A;
loc_00C5BA87:
    result = memcpy(result, result, (uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x61)), local_rsp - 71 - 97);
    *(uint16_t *)(local_rsp - 0x47 - 0x41) = (uint16_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x61)));
    *(uint16_t *)(local_rsp - 0x47 - 0x3F) = (uint16_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x61)));
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_00C5BAB4;
    result = HvpReleaseCellFlat(Arg1, local_rsp - 71 - 81, (uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x61)), local_rsp - 71 - 97);
    goto loc_00C5BAB9;
loc_00C5BAB4:
    result = HvpReleaseCellPaged(Arg1, local_rsp - 71 - 81, (uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x61)), local_rsp - 71 - 97);
loc_00C5BAB9:
    local_r15 = (uint32_t)((result) | (0xFFFFFFFFULL));
loc_00C5BABD:
    Arg2 = 0;
    Arg1 = (uint16_t)((*(uint16_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x6F))) + (94));
    Arg1 = (uint16_t)((Arg1) + (*(uint16_t *)((uint8_t)(arg1 + 0x20))));
    *(uint16_t *)(local_rsp - 0x47 - 0x17) = (uint16_t)((uint16_t)(Arg1));
    result = guard_dispatch_icall((uint16_t)(Arg1), Arg2, (uint32_t)(0x20344D43ULL), local_rsp - 71 - 97);
    *(uint64_t *)(local_rsp - 0x47 - 0x11) = result;
    if (result == 0) goto loc_00C5B91A;
    result = RtlAppendUnicodeStringToString(local_rsp - 71 - 25, v_rip + 157311, (uint32_t)(0x20344D43ULL), local_rsp - 71 - 97);
    if (sign_flag) goto loc_00C5B91A;
    result = RtlAppendUnicodeStringToString(local_rsp - 71 - 25, *(uint64_t *)(local_rsp - 0x47 + 0x6F), (uint32_t)(0x20344D43ULL), local_rsp - 71 - 97);
    if (sign_flag) goto loc_00C5B91A;
    result = RtlAppendUnicodeStringToString(local_rsp - 71 - 25, v_rip + 157355, (uint32_t)(0x20344D43ULL), local_rsp - 71 - 97);
    if (sign_flag) goto loc_00C5B91A;
    result = RtlAppendUnicodeStringToString(local_rsp - 71 - 25, (uint8_t)(Arg1 + 32), (uint32_t)(0x20344D43ULL), local_rsp - 71 - 97);
    local_r12 = 0;
    if (sign_flag) goto loc_00C5B91A;
    if (*(uint64_t *)(result + 0x18) != 0) {
        Arg2 = *(uint16_t *)(result + 0x10);
        result = *(uint64_t *)(arg1 + 0x20);
        result = guard_dispatch_icall(*(uint64_t *)(result + 0x18), Arg2, (uint32_t)(0x20344D43ULL), local_rsp - 71 - 97);
    }
    *(uint64_t *)(result + 0x10) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x47 - 0x41) = v_xmm1;
    if (*(uint64_t *)(result + 0x28) != 0) {
        Arg2 = *(uint16_t *)(result + 0x20);
        result = *(uint64_t *)(arg1 + 0x20);
        result = guard_dispatch_icall(*(uint64_t *)(result + 0x28), Arg2, (uint32_t)(0x20344D43ULL), local_rsp - 71 - 97);
    }
    *(uint64_t *)(result + 0x20) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x47 - 0x19) = v_xmm1;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x77)) + 0x8)) != (*(uint64_t *)(local_rsp - 0x47 + 0x77))) {
        Arg1 = 3;
    }
    *(void **)(result) = Arg1;
    *(uint64_t *)(result + 0x8) = *(uint64_t *)(local_rsp - 0x47 + 0x77);
    *(uint64_t *)(arg1 + 0x8) = result;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x77)) = result;
    result = CmpFindValueByName(Arg1, result, v_rip + 157577, local_rsp - 71 - 97);
    if (((uint32_t)(result)) != ((uint32_t)(local_r15))) goto loc_00C5BBE6;
    *(uint32_t *)(result + 0x8C) = 1;
    goto loc_00C5BC73;
loc_00C5BBE6:
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_00C5BBFF;
    result = HvpGetCellFlat(Arg1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), local_rsp - 71 - 89, local_rsp - 71 - 97);
    goto loc_00C5BC04;
loc_00C5BBFF:
    result = HvpGetCellPaged(Arg1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), local_rsp - 71 - 89, local_rsp - 71 - 97);
loc_00C5BC04:
    if (result == 0) goto loc_00C5B91E;
    v_stack_mB8 = local_rsp - 71 - 49;
    result = CmpValueToData(Arg1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), result, local_rsp - 71 - 97);
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_00C5BC41;
    result = HvpReleaseCellFlat(Arg1, local_rsp - 71 - 89, result, local_rsp - 71 - 97);
    goto loc_00C5BC46;
loc_00C5BC41:
    result = HvpReleaseCellPaged(Arg1, local_rsp - 71 - 89, result, local_rsp - 71 - 97);
loc_00C5BC46:
    if (result == 0) goto loc_00C5B91E;
    *(uint32_t *)(result + 0x8C) = (uint32_t)((uint32_t)(*(uint32_t *)(result)));
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_00C5BC6E;
    result = HvpReleaseCellFlat(Arg1, local_rsp - 71 - 49, result, local_rsp - 71 - 97);
    goto loc_00C5BC73;
loc_00C5BC6E:
    result = HvpReleaseCellPaged(Arg1, local_rsp - 71 - 49, result, local_rsp - 71 - 97);
loc_00C5BC73:
    result = CmpFindValueByName(Arg1, result, v_rip + 157398, local_rsp - 71 - 97);
    if (((uint32_t)(result)) != ((uint32_t)(local_r15))) goto loc_00C5BC99;
    *(uint32_t *)(result + 0x68) = 0;
    *(uint64_t *)(result + 0x70) = 0;
    goto loc_00C5BD3A;
loc_00C5BC99:
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_00C5BCB2;
    result = HvpGetCellFlat(Arg1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), local_rsp - 71 - 89, local_rsp - 71 - 97);
    goto loc_00C5BCB7;
loc_00C5BCB2:
    result = HvpGetCellPaged(Arg1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), local_rsp - 71 - 89, local_rsp - 71 - 97);
loc_00C5BCB7:
    if (result == 0) goto loc_00C5B91E;
    v_stack_mB8 = local_rsp - 71 - 41;
    result = CmpValueToData(Arg1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), result, local_rsp - 71 - 97);
    *(uint64_t *)(result + 0x70) = result;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_00C5BCF5;
    result = HvpReleaseCellFlat(Arg1, local_rsp - 71 - 89, result, local_rsp - 71 - 97);
    goto loc_00C5BCFA;
loc_00C5BCF5:
    result = HvpReleaseCellPaged(Arg1, local_rsp - 71 - 89, result, local_rsp - 71 - 97);
loc_00C5BCFA:
    if ((*(uint64_t *)(result + 0x70)) == 0) goto loc_00C5B91E;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_00C5BD1B;
    result = HvpReleaseCellFlat(Arg1, local_rsp - 71 - 41, result, local_rsp - 71 - 97);
    goto loc_00C5BD20;
loc_00C5BD1B:
    result = HvpReleaseCellPaged(Arg1, local_rsp - 71 - 41, result, local_rsp - 71 - 97);
loc_00C5BD20:
    result = (uint16_t)((*(uint16_t *)(local_rsp - 0x47 - 0x61)) - (2));
    *(uint16_t *)(result + 0x68) = (uint16_t)(result);
    if (((uint16_t)(result)) > (*(uint16_t *)(local_rsp - 0x47 - 0x61))) goto loc_00C5B91E;
    *(uint16_t *)(result + 0x6A) = (uint16_t)(result);
loc_00C5BD3A:
    result = CmpFindValueByName(Arg1, result, v_rip + 156959, local_rsp - 71 - 97);
    if (((uint32_t)(result)) != ((uint32_t)(local_r15))) goto loc_00C5BD60;
    *(uint32_t *)(result + 0x58) = 0;
    *(uint64_t *)(result + 0x60) = 0;
    goto loc_00C5BE01;
loc_00C5BD60:
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_00C5BD79;
    result = HvpGetCellFlat(Arg1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), local_rsp - 71 - 89, local_rsp - 71 - 97);
    goto loc_00C5BD7E;
loc_00C5BD79:
    result = HvpGetCellPaged(Arg1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), local_rsp - 71 - 89, local_rsp - 71 - 97);
loc_00C5BD7E:
    if (result == 0) goto loc_00C5B91E;
    v_stack_mB8 = local_rsp - 71 - 33;
    result = CmpValueToData(Arg1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), result, local_rsp - 71 - 97);
    *(uint64_t *)(result + 0x60) = result;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_00C5BDBC;
    result = HvpReleaseCellFlat(Arg1, local_rsp - 71 - 89, result, local_rsp - 71 - 97);
    goto loc_00C5BDC1;
loc_00C5BDBC:
    result = HvpReleaseCellPaged(Arg1, local_rsp - 71 - 89, result, local_rsp - 71 - 97);
loc_00C5BDC1:
    if ((*(uint64_t *)(result + 0x60)) == 0) goto loc_00C5B91E;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_00C5BDE2;
    result = HvpReleaseCellFlat(Arg1, local_rsp - 71 - 33, result, local_rsp - 71 - 97);
    goto loc_00C5BDE7;
loc_00C5BDE2:
    result = HvpReleaseCellPaged(Arg1, local_rsp - 71 - 33, result, local_rsp - 71 - 97);
loc_00C5BDE7:
    result = (uint16_t)((*(uint16_t *)(local_rsp - 0x47 - 0x61)) - (2));
    *(uint16_t *)(result + 0x58) = (uint16_t)(result);
    if (((uint16_t)(result)) > (*(uint16_t *)(local_rsp - 0x47 - 0x61))) goto loc_00C5B91E;
    *(uint16_t *)(result + 0x5A) = (uint16_t)(result);
loc_00C5BE01:
    result = CmpFindValueByName(Arg1, result, v_rip + 156840, local_rsp - 71 - 97);
    if (((uint32_t)(result)) != ((uint32_t)(local_r15))) {
        Arg3 = *(uint32_t *)(local_rsp - 0x47 + 0x67);
        Arg4 = result + 104;
        Arg1 = *(uint64_t *)(local_rsp - 0x47 + 0x5F);
        Arg2 = (uint32_t)(result);
        result = CmpFindTagIndex(Arg1, Arg2, Arg3, Arg4);
        local_r15 = (uint32_t)(result);
    }
    *(uint32_t *)(result + 0x88 * 1) = (uint32_t)(local_r15);
    goto loc_00C5B91E;
loc_00C5BE42:
    result = guard_dispatch_icall((uint32_t)((uint32_t)(result)), *(uint16_t *)(local_rsp - 0x47 + 0x4F), Arg3, Arg4);
    goto loc_00C5B91E;
loc_00C5BE57:
    result = HvpReleaseCellPaged((uint32_t)((uint32_t)(result)), *(uint16_t *)(local_rsp - 0x47 + 0x4F), Arg3, Arg4);
loc_00C5BE5C:
    local_rsp = (local_rsp) + (160);
    return 1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x8C` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C5B758&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
