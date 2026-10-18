# _CmGetDeviceMappedPropertyFromComposite

- RVA: `0x009D1684`–`0x009D2A53` (길이 `5,071` bytes)
- VA: `0x00000001409D1684`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000A1438`
- 디코드: `1,167`개 명령, `5,071/5,071` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **42**; 고유 호출 대상: **20**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **68**

### Outgoing calls
- `0x009D189D` → [_CmGetDeviceCompoundFilters](_CmGetDeviceCompoundFilters_function_009D31C0.md) (function, `0x009D31C0`)
- `0x009D196D` → [RtlStringCbCopyExW](../../text/45/RtlStringCbCopyExW_function_0045488C.md) (function, `0x0045488C`)
- `0x009D1A26` → [PnpGetObjectProperty](../8E/PnpGetObjectProperty_function_008E2180.md) (function, `0x008E2180`)
- `0x009D1A82` → [PnpGetObjectProperty](../8E/PnpGetObjectProperty_function_008E2180.md) (function, `0x008E2180`)
- `0x009D1AAB` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x009D1B1A` → [PnpGetObjectProperty](../8E/PnpGetObjectProperty_function_008E2180.md) (function, `0x008E2180`)
- `0x009D1B7D` → [PnpGetObjectProperty](../8E/PnpGetObjectProperty_function_008E2180.md) (function, `0x008E2180`)
- `0x009D1C05` → [CmGetDeviceParent](../93/CmGetDeviceParent_function_00932368.md) (function, `0x00932368`)
- `0x009D1C9A` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (function, `0x00463960`)
- `0x009D1CD9` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x009D1D44` → [CmGetDeviceStatus](CmGetDeviceStatus_function_009D154C.md) (function, `0x009D154C`)
- `0x009D1E21` → [CmIsDeviceSafeRemovalRequired](CmIsDeviceSafeRemovalRequired_function_009D1040.md) (function, `0x009D1040`)
- `0x009D1E5F` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (function, `0x00463960`)
- `0x009D1E9F` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x009D1EF8` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (function, `0x00463960`)
- `0x009D1F3F` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x009D1FB9` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (function, `0x00463960`)
- `0x009D1FF8` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x009D208A` → [PnpGetObjectProperty](../8E/PnpGetObjectProperty_function_008E2180.md) (function, `0x008E2180`)
- `0x009D213A` → [PnpGetObjectProperty](../8E/PnpGetObjectProperty_function_008E2180.md) (function, `0x008E2180`)
- `0x009D21A0` → [PnpGetObjectProperty](../8E/PnpGetObjectProperty_function_008E2180.md) (function, `0x008E2180`)
- `0x009D2207` → [_CmOpenDeviceRegKey](../8E/_CmOpenDeviceRegKey_function_008EE540.md) (function, `0x008EE540`)
- `0x009D221A` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x009D225A` → [CmGetDeviceChildren](CmGetDeviceChildren_function_009D08DC.md) (function, `0x009D08DC`)
- `0x009D2295` → [CmGetDeviceRelationsList](CmGetDeviceRelationsList_function_009D0660.md) (function, `0x009D0660`)
- `0x009D2322` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (function, `0x00463960`)
- `0x009D2361` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x009D23E3` → [PnpGetObjectProperty](../8E/PnpGetObjectProperty_function_008E2180.md) (function, `0x008E2180`)
- `0x009D2446` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (function, `0x00463960`)
- `0x009D2485` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x009D2593` → [CmGetDeviceSiblings](CmGetDeviceSiblings_function_009D0734.md) (function, `0x009D0734`)
- `0x009D25E9` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (function, `0x00463960`)
- `0x009D2634` → [PnpMultiSzGetLen](PnpMultiSzGetLen_function_009D3180.md) (function, `0x009D3180`)
- `0x009D2744` → [PnpGetObjectProperty](../8E/PnpGetObjectProperty_function_008E2180.md) (function, `0x008E2180`)
- `0x009D27A4` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (function, `0x00463960`)
- `0x009D2873` → [PnpGetObjectProperty](../8E/PnpGetObjectProperty_function_008E2180.md) (function, `0x008E2180`)
- `0x009D290C` → [CmGetDeviceRegProp](../8E/CmGetDeviceRegProp_function_008ED870.md) (function, `0x008ED870`)
- `0x009D2926` → [wcscmp](../../text/50/wcscmp_function_00501AF0.md) (function, `0x00501AF0`)
- `0x009D2961` → [_CmGetDeviceContainerIdFromBase](../8F/_CmGetDeviceContainerIdFromBase_function_008FD2B4.md) (function, `0x008FD2B4`)
- `0x009D2978` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (function, `0x00463960`)
- `0x009D298E` → [RtlGUIDFromString](../8F/RtlGUIDFromString_function_008F1EF0.md) (function, `0x008F1EF0`)
- `0x009D2A33` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [sub_008E1E60](../8E/Unknown_function_008E1E60.md) at `0x008E1EA9`
- [_CmGetDeviceMappedPropertyKeys](_CmGetDeviceMappedPropertyKeys_function_009D0D78.md) at `0x009D0F33`

### Static image references
- `0x009D16A3` → RVA `0x00E0A740` (`.data`; read)
- `0x009D1864` → RVA `0x000140B0` (`.rdata`; read)
- `0x009D1871` → RVA `0x000140B8` (`.rdata`; read)
- `0x009D18CF` → RVA `0x00011490` (`.rdata`; read)
- `0x009D18DC` → RVA `0x00011498` (`.rdata`; read)
- `0x009D1991` → RVA `0x00014050` (`.rdata`; read)
- `0x009D199E` → RVA `0x00014058` (`.rdata`; read)
- `0x009D19B3` → RVA `0x000140F8` (`.rdata`; read)
- `0x009D19C0` → RVA `0x00014100` (`.rdata`; read)
- `0x009D19FF` → RVA `0x00011568` (`.rdata`; read)
- `0x009D1A43` → RVA `0x00AFFD10` (` ?? ::NNGAKEGL::`string'`; read)
- `0x009D1A6D` → RVA `0x00014110` (`.rdata`; read)
- `0x009D1AC3` → RVA `0x00014080` (`.rdata`; read)
- `0x009D1AD0` → RVA `0x00014088` (`.rdata`; read)
- `0x009D1AF5` → RVA `0x00014098` (`.rdata`; read)
- `0x009D1B6C` → RVA `0x00014128` (`.rdata`; read)
- `0x009D1B9A` → RVA `0x000140C8` (`.rdata`; read)
- `0x009D1BA7` → RVA `0x000140D0` (`.rdata`; read)
- `0x009D1BD4` → RVA `0x000141A0` (`.rdata`; read)
- `0x009D1BE1` → RVA `0x000141A8` (`.rdata`; read)
- `0x009D1C43` → RVA `0x00014200` (`.rdata`; read)
- `0x009D1C50` → RVA `0x00014208` (`.rdata`; read)
- `0x009D1C63` → RVA `0x000141B8` (`.rdata`; read)
- `0x009D1C70` → RVA `0x000141C0` (`.rdata`; read)
- `0x009D1D06` → RVA `0x000142C0` (`.rdata`; read)
- `0x009D1D13` → RVA `0x000142C8` (`.rdata`; read)
- `0x009D1DE6` → RVA `0x00014218` (`.rdata`; read)
- `0x009D1DF3` → RVA `0x00014220` (`.rdata`; read)
- `0x009D1E32` → RVA `0x000141E8` (`.rdata`; read)
- `0x009D1E3F` → RVA `0x000141F0` (`.rdata`; read)
- `0x009D1ECC` → RVA `0x000141D0` (`.rdata`; read)
- `0x009D1ED9` → RVA `0x000141D8` (`.rdata`; read)
- `0x009D1F5D` → RVA `0x00014278` (`.rdata`; read)
- `0x009D1F6A` → RVA `0x00014280` (`.rdata`; read)
- `0x009D1F7D` → RVA `0x00014260` (`.rdata`; read)
- `0x009D1F8A` → RVA `0x00014268` (`.rdata`; read)
- `0x009D2079` → RVA `0x000142D8` (`.rdata`; read)
- `0x009D20BC` → RVA `0x00014230` (`.rdata`; read)
- `0x009D20C9` → RVA `0x00014238` (`.rdata`; read)
- `0x009D2129` → RVA `0x00014290` (`.rdata`; read)
- `0x009D218F` → RVA `0x000142A8` (`.rdata`; read)
- `0x009D2227` → RVA `0x00014248` (`.rdata`; read)
- `0x009D2234` → RVA `0x00014250` (`.rdata`; read)
- `0x009D22E6` → RVA `0x000142F0` (`.rdata`; read)
- `0x009D22F3` → RVA `0x000142F8` (`.rdata`; read)
- `0x009D23CE` → RVA `0x00014320` (`.rdata`; read)
- `0x009D240A` → RVA `0x00014308` (`.rdata`; read)
- `0x009D2417` → RVA `0x00014310` (`.rdata`; read)
- `0x009D24DF` → RVA `0x0001BF58` (`.rdata`; read)
- `0x009D24EC` → RVA `0x0001BF60` (`.rdata`; read)
- `0x009D2537` → RVA `0x00014338` (`.rdata`; read)
- `0x009D2544` → RVA `0x00014340` (`.rdata`; read)
- `0x009D2560` → RVA `0x000143B0` (`.rdata`; read)
- `0x009D256D` → RVA `0x000143B8` (`.rdata`; read)
- `0x009D25BC` → RVA `0x00014368` (`.rdata`; read)
- `0x009D25C9` → RVA `0x00014370` (`.rdata`; read)
- `0x009D2641` → RVA `0x00014440` (`.rdata`; read)
- `0x009D264E` → RVA `0x00014448` (`.rdata`; read)
- `0x009D26E8` → RVA `0x00011478` (`.rdata`; read)
- `0x009D26F5` → RVA `0x00011480` (`.rdata`; read)
- `0x009D2733` → RVA `0x00011728` (`.rdata`; read)
- `0x009D2777` → RVA `0x00014458` (`.rdata`; read)
- `0x009D2784` → RVA `0x00014460` (`.rdata`; read)
- `0x009D27E9` → RVA `0x00014470` (`.rdata`; read)
- `0x009D27F6` → RVA `0x00014478` (`.rdata`; read)
- `0x009D2862` → RVA `0x000115B8` (`.rdata`; read)
- `0x009D28C3` → RVA `0x00011570` (`.rdata`; read)
- `0x009D291F` → RVA `0x00AFDCF0` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **20**
  - `0x009D196D` → [RtlStringCbCopyExW](../../text/45/RtlStringCbCopyExW_function_0045488C.md) (`PAGE` → `.text`)
  - `0x009D1AAB` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x009D1C9A` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (`PAGE` → `.text`)
  - `0x009D1CD9` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x009D1E5F` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (`PAGE` → `.text`)
  - `0x009D1E9F` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x009D1EF8` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (`PAGE` → `.text`)
  - `0x009D1F3F` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x009D1FB9` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (`PAGE` → `.text`)
  - `0x009D1FF8` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x009D221A` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x009D2322` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (`PAGE` → `.text`)
  - `0x009D2361` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x009D2446` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (`PAGE` → `.text`)
  - `0x009D2485` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x009D25E9` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (`PAGE` → `.text`)
  - `0x009D27A4` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (`PAGE` → `.text`)
  - `0x009D2926` → [wcscmp](../../text/50/wcscmp_function_00501AF0.md) (`PAGE` → `.text`)
  - `0x009D2978` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (`PAGE` → `.text`)
  - `0x009D2A33` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x009D289B` → [sub_00B2F56A](../B2/Unknown_function_00B2F56A.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
009D1684  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
009D1689  55                              push rbp
009D168A  56                              push rsi
009D168B  57                              push rdi
009D168C  41 54                           push r12
009D168E  41 55                           push r13
009D1690  41 56                           push r14
009D1692  41 57                           push r15
009D1694  48 8D AC 24 70 FF FF FF         lea rbp, [rsp - 0x90]
009D169C  48 81 EC 90 01 00 00            sub rsp, 0x190
009D16A3  48 8B 05 96 90 43 00            mov rax, qword ptr [rip + 0x439096]
009D16AA  48 33 C4                        xor rax, rsp
009D16AD  48 89 85 80 00 00 00            mov qword ptr [rbp + 0x80], rax
009D16B4  44 8B 95 10 01 00 00            mov r10d, dword ptr [rbp + 0x110]
009D16BB  0F 57 C0                        xorps xmm0, xmm0
009D16BE  4C 8B B5 F8 00 00 00            mov r14, qword ptr [rbp + 0xf8]
009D16C5  49 8B F9                        mov rdi, r9
009D16C8  48 8B B5 08 01 00 00            mov rsi, qword ptr [rbp + 0x108]
009D16CF  4C 8B E9                        mov r13, rcx
009D16D2  33 C9                           xor ecx, ecx
009D16D4  4C 89 45 90                     mov qword ptr [rbp - 0x70], r8
009D16D8  48 89 54 24 68                  mov qword ptr [rsp + 0x68], rdx
009D16DD  4D 8B C8                        mov r9, r8
009D16E0  4C 8B 85 F0 00 00 00            mov r8, qword ptr [rbp + 0xf0]
009D16E7  0F 57 C9                        xorps xmm1, xmm1
009D16EA  4C 89 45 98                     mov qword ptr [rbp - 0x68], r8
009D16EE  4C 8B DA                        mov r11, rdx
009D16F1  89 4D 84                        mov dword ptr [rbp - 0x7c], ecx
009D16F4  8B D9                           mov ebx, ecx
009D16F6  89 4C 24 70                     mov dword ptr [rsp + 0x70], ecx
009D16FA  89 4C 24 78                     mov dword ptr [rsp + 0x78], ecx
009D16FE  89 4C 24 7C                     mov dword ptr [rsp + 0x7c], ecx
009D1702  89 4D 80                        mov dword ptr [rbp - 0x80], ecx
009D1705  89 4D B0                        mov dword ptr [rbp - 0x50], ecx
009D1708  48 89 4D B8                     mov qword ptr [rbp - 0x48], rcx
009D170C  89 4C 24 74                     mov dword ptr [rsp + 0x74], ecx
009D1710  89 4D B4                        mov dword ptr [rbp - 0x4c], ecx
009D1713  88 4C 24 60                     mov byte ptr [rsp + 0x60], cl
009D1717  0F 11 45 A0                     movups xmmword ptr [rbp - 0x60], xmm0
009D171B  0F 11 4D C0                     movups xmmword ptr [rbp - 0x40], xmm1
009D171F  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
009D1723  66 45 85 D2                     test r10w, r10w
009D1727  0F 85 8F 04 00 00               jne 0x1409d1bbc
009D172D  45 8B E2                        mov r12d, r10d
009D1730  41 89 08                        mov dword ptr [r8], ecx
009D1733  41 81 E4 00 00 FF FF            and r12d, 0xffff0000
009D173A  89 0E                           mov dword ptr [rsi], ecx
009D173C  44 89 65 88                     mov dword ptr [rbp - 0x78], r12d
009D1740  4D 85 F6                        test r14, r14
009D1743  0F 84 76 01 00 00               je 0x1409d18bf
009D1749  8B 95 00 01 00 00               mov edx, dword ptr [rbp + 0x100]
009D174F  8B C2                           mov eax, edx
009D1751  F7 D8                           neg eax
009D1753  48 1B C9                        sbb rcx, rcx
009D1756  4C 23 F1                        and r14, rcx
009D1759  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
009D175C  83 F8 02                        cmp eax, 2
009D175F  0F 82 67 10 00 00               jb 0x1409d27cc
009D1765  41 BF 25 02 00 C0               mov r15d, 0xc0000225
009D176B  83 F8 0A                        cmp eax, 0xa
009D176E  0F 84 4C 03 00 00               je 0x1409d1ac0
009D1774  3D 00 01 00 00                  cmp eax, 0x100
009D1779  0F 84 4D 01 00 00               je 0x1409d18cc
009D177F  83 F8 02                        cmp eax, 2
009D1782  0F 84 7B 05 00 00               je 0x1409d1d03
009D1788  83 F8 03                        cmp eax, 3
009D178B  0F 84 7E 0D 00 00               je 0x1409d250f
009D1791  83 F8 0C                        cmp eax, 0xc
009D1794  0F 84 4C 10 00 00               je 0x1409d27e6
009D179A  41 BC 04 00 00 00               mov r12d, 4
009D17A0  41 3B C4                        cmp eax, r12d
009D17A3  0F 84 E5 01 00 00               je 0x1409d198e
009D17A9  83 F8 05                        cmp eax, 5
009D17AC  0F 84 8E 04 00 00               je 0x1409d1c40
009D17B2  83 F8 06                        cmp eax, 6
009D17B5  0F 84 9F 07 00 00               je 0x1409d1f5a
009D17BB  45 8D 4C 24 03                  lea r9d, [r12 + 3]
009D17C0  41 3B C1                        cmp eax, r9d
009D17C3  0F 84 6B 0D 00 00               je 0x1409d2534
009D17C9  83 F8 0B                        cmp eax, 0xb
009D17CC  0F 84 6C 0E 00 00               je 0x1409d263e
009D17D2  83 F8 08                        cmp eax, 8
009D17D5  0F 84 F6 03 00 00               je 0x1409d1bd1
009D17DB  83 F8 09                        cmp eax, 9
009D17DE  0F 84 40 0A 00 00               je 0x1409d2224
009D17E4  83 F8 0A                        cmp eax, 0xa
009D17E7  0F 84 70 0D 00 00               je 0x1409d255d
009D17ED  83 F8 02                        cmp eax, 2
009D17F0  0F 84 E9 05 00 00               je 0x1409d1ddf
009D17F6  83 F8 05                        cmp eax, 5
009D17F9  0F 84 61 04 00 00               je 0x1409d1c60
009D17FF  83 F8 06                        cmp eax, 6
009D1802  0F 84 72 07 00 00               je 0x1409d1f7a
009D1808  83 F8 0F                        cmp eax, 0xf
009D180B  0F 84 D2 0A 00 00               je 0x1409d22e3
009D1811  83 F8 10                        cmp eax, 0x10
009D1814  0F 84 ED 0B 00 00               je 0x1409d2407
009D181A  41 3B C4                        cmp eax, r12d
009D181D  0F 84 A3 03 00 00               je 0x1409d1bc6
009D1823  83 F8 0E                        cmp eax, 0xe
009D1826  0F 84 03 06 00 00               je 0x1409d1e2f
009D182C  44 8B 65 88                     mov r12d, dword ptr [rbp - 0x78]
009D1830  4C 8B 4D 90                     mov r9, qword ptr [rbp - 0x70]
009D1834  83 F8 14                        cmp eax, 0x14
009D1837  0F 84 37 0F 00 00               je 0x1409d2774
009D183D  83 F8 15                        cmp eax, 0x15
009D1840  0F 84 73 0D 00 00               je 0x1409d25b9
009D1846  83 F8 1A                        cmp eax, 0x1a
009D1849  0F 84 6A 08 00 00               je 0x1409d20b9
009D184F  83 F8 16                        cmp eax, 0x16
009D1852  0F 84 3F 03 00 00               je 0x1409d1b97
009D1858  83 F8 17                        cmp eax, 0x17
009D185B  0F 85 7B 0E 00 00               jne 0x1409d26dc
009D1861  48 8B 07                        mov rax, qword ptr [rdi]
009D1864  48 2B 05 45 28 64 FF            sub rax, qword ptr [rip - 0x9bd7bb]
009D186B  75 0B                           jne 0x1409d1878
009D186D  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
009D1871  48 2B 05 40 28 64 FF            sub rax, qword ptr [rip - 0x9bd7c0]
009D1878  48 85 C0                        test rax, rax
009D187B  75 3A                           jne 0x1409d18b7
009D187D  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
009D1882  4C 8B CF                        mov r9, rdi
009D1885  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
009D1889  49 8B CD                        mov rcx, r13
009D188C  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
009D1891  49 8B D3                        mov rdx, r11
009D1894  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
009D1899  4C 8B 45 90                     mov r8, qword ptr [rbp - 0x70]
009D189D  E8 1E 19 00 00                  call 0x1409d31c0
009D18A2  8B D8                           mov ebx, eax
009D18A4  33 FF                           xor edi, edi
009D18A6  4C 8B 5C 24 68                  mov r11, qword ptr [rsp + 0x68]
009D18AB  81 FB 0E 00 00 C0               cmp ebx, 0xc000000e
009D18B1  0F 84 28 09 00 00               je 0x1409d21df
009D18B7  8B C3                           mov eax, ebx
009D18B9  E9 6B 11 00 00                  jmp 0x1409d2a29
009D18BE  CC                              int3
009D18BF  8B D1                           mov edx, ecx
009D18C1  89 8D 00 01 00 00               mov dword ptr [rbp + 0x100], ecx
009D18C7  E9 8D FE FF FF                  jmp 0x1409d1759
009D18CC  48 8B 0F                        mov rcx, qword ptr [rdi]
009D18CF  48 2B 0D BA FB 63 FF            sub rcx, qword ptr [rip - 0x9c0446]
009D18D6  75 0B                           jne 0x1409d18e3
009D18D8  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
009D18DC  48 2B 0D B5 FB 63 FF            sub rcx, qword ptr [rip - 0x9c044b]
009D18E3  48 85 C9                        test rcx, rcx
009D18E6  0F 85 48 FF FF FF               jne 0x1409d1834
009D18EC  33 FF                           xor edi, edi
009D18EE  4D 85 DB                        test r11, r11
009D18F1  0F 84 A3 10 00 00               je 0x1409d299a
009D18F7  41 BA C8 00 00 00               mov r10d, 0xc8
009D18FD  49 8B C3                        mov rax, r11
009D1900  45 8B CA                        mov r9d, r10d
009D1903  66 39 38                        cmp word ptr [rax], di
009D1906  74 0A                           je 0x1409d1912
009D1908  48 83 C0 02                     add rax, 2
009D190C  49 83 E9 01                     sub r9, 1
009D1910  75 F1                           jne 0x1409d1903
009D1912  49 8B C1                        mov rax, r9
009D1915  BB 0D 00 00 C0                  mov ebx, 0xc000000d
009D191A  48 F7 D8                        neg rax
009D191D  49 8B C1                        mov rax, r9
009D1920  1B C9                           sbb ecx, ecx
009D1922  4D 2B D1                        sub r10, r9
009D1925  F7 D1                           not ecx
009D1927  23 D9                           and ebx, ecx
009D1929  48 F7 D8                        neg rax
009D192C  48 1B C0                        sbb rax, rax
009D192F  49 23 C2                        and rax, r10
009D1932  4D 85 C9                        test r9, r9
009D1935  0F 84 70 FF FF FF               je 0x1409d18ab
009D193B  8D 04 45 02 00 00 00            lea eax, [rax*2 + 2]
009D1942  89 06                           mov dword ptr [rsi], eax
009D1944  41 C7 00 12 00 00 00            mov dword ptr [r8], 0x12
009D194B  8B 06                           mov eax, dword ptr [rsi]
009D194D  3B D0                           cmp edx, eax
009D194F  0F 82 E1 02 00 00               jb 0x1409d1c36
009D1955  8B D0                           mov edx, eax
009D1957  C7 44 24 28 00 09 00 00         mov dword ptr [rsp + 0x28], 0x900
009D195F  45 33 C9                        xor r9d, r9d
009D1962  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
009D1967  4D 8B C3                        mov r8, r11
009D196A  49 8B CE                        mov rcx, r14
009D196D  E8 1A 2F A8 FF                  call 0x14045488c
009D1972  4C 8B 5C 24 68                  mov r11, qword ptr [rsp + 0x68]
009D1977  8B D8                           mov ebx, eax
009D1979  85 C0                           test eax, eax
009D197B  0F 89 2A FF FF FF               jns 0x1409d18ab
009D1981  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
009D1985  89 3E                           mov dword ptr [rsi], edi
009D1987  89 38                           mov dword ptr [rax], edi
009D1989  E9 1D FF FF FF                  jmp 0x1409d18ab
009D198E  48 8B 07                        mov rax, qword ptr [rdi]
009D1991  48 2B 05 B8 26 64 FF            sub rax, qword ptr [rip - 0x9bd948]
009D1998  75 0B                           jne 0x1409d19a5
009D199A  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
009D199E  48 2B 05 B3 26 64 FF            sub rax, qword ptr [rip - 0x9bd94d]
009D19A5  33 C9                           xor ecx, ecx
009D19A7  48 85 C0                        test rax, rax
009D19AA  0F 84 C9 08 00 00               je 0x1409d2279
009D19B0  48 8B 07                        mov rax, qword ptr [rdi]
009D19B3  48 2B 05 3E 27 64 FF            sub rax, qword ptr [rip - 0x9bd8c2]
009D19BA  75 0B                           jne 0x1409d19c7
009D19BC  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
009D19C0  48 2B 05 39 27 64 FF            sub rax, qword ptr [rip - 0x9bd8c7]
009D19C7  48 85 C0                        test rax, rax
009D19CA  0F 85 E7 FE FF FF               jne 0x1409d18b7
009D19D0  8B 7D 88                        mov edi, dword ptr [rbp - 0x78]
009D19D3  48 8D 44 24 70                  lea rax, [rsp + 0x70]
009D19D8  89 7C 24 50                     mov dword ptr [rsp + 0x50], edi
009D19DC  49 8B D3                        mov rdx, r11
009D19DF  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
009D19E4  48 8D 45 C0                     lea rax, [rbp - 0x40]
009D19E8  C7 44 24 40 10 00 00 00         mov dword ptr [rsp + 0x40], 0x10
009D19F0  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
009D19F5  48 8D 44 24 74                  lea rax, [rsp + 0x74]
009D19FA  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009D19FF  48 8D 05 62 FB 63 FF            lea rax, [rip - 0x9c049e]
009D1A06  41 C7 00 11 00 00 00            mov dword ptr [r8], 0x11
009D1A0D  41 B8 01 00 00 00               mov r8d, 1
009D1A13  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009D1A18  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
009D1A1D  49 8B CD                        mov rcx, r13
009D1A20  C7 06 01 00 00 00               mov dword ptr [rsi], 1
009D1A26  E8 55 07 F1 FF                  call 0x1408e2180
009D1A2B  8B D8                           mov ebx, eax
009D1A2D  85 C0                           test eax, eax
009D1A2F  0F 88 6F FE FF FF               js 0x1409d18a4
009D1A35  89 7C 24 50                     mov dword ptr [rsp + 0x50], edi
009D1A39  48 8D 44 24 70                  lea rax, [rsp + 0x70]
009D1A3E  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
009D1A43  48 8D 15 C6 E2 12 00            lea rdx, [rip + 0x12e2c6]
009D1A4A  C7 44 24 40 10 00 00 00         mov dword ptr [rsp + 0x40], 0x10
009D1A52  48 8D 45 D0                     lea rax, [rbp - 0x30]
009D1A56  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
009D1A5B  33 FF                           xor edi, edi
009D1A5D  48 8D 44 24 74                  lea rax, [rsp + 0x74]
009D1A62  45 33 C9                        xor r9d, r9d
009D1A65  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009D1A6A  49 8B CD                        mov rcx, r13
009D1A6D  48 8D 05 9C 26 64 FF            lea rax, [rip - 0x9bd964]
009D1A74  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009D1A79  44 8D 47 01                     lea r8d, [rdi + 1]
009D1A7D  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
009D1A82  E8 F9 06 F1 FF                  call 0x1408e2180
009D1A87  8B D8                           mov ebx, eax
009D1A89  85 C0                           test eax, eax
009D1A8B  0F 88 15 FE FF FF               js 0x1409d18a6
009D1A91  8B 06                           mov eax, dword ptr [rsi]
009D1A93  39 85 00 01 00 00               cmp dword ptr [rbp + 0x100], eax
009D1A99  0F 82 97 01 00 00               jb 0x1409d1c36
009D1A9F  44 8D 47 10                     lea r8d, [rdi + 0x10]
009D1AA3  48 8D 55 C0                     lea rdx, [rbp - 0x40]
009D1AA7  48 8D 4D D0                     lea rcx, [rbp - 0x30]
009D1AAB  E8 60 50 CF FF                  call 0x1406c6b10
009D1AB0  F7 D8                           neg eax
009D1AB2  1A C9                           sbb cl, cl
009D1AB4  F6 D9                           neg cl
009D1AB6  FE C9                           dec cl
009D1AB8  41 88 0E                        mov byte ptr [r14], cl
009D1ABB  E9 F7 FD FF FF                  jmp 0x1409d18b7
009D1AC0  48 8B 07                        mov rax, qword ptr [rdi]
009D1AC3  48 2B 05 B6 25 64 FF            sub rax, qword ptr [rip - 0x9bda4a]
009D1ACA  75 0B                           jne 0x1409d1ad7
009D1ACC  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
009D1AD0  48 2B 05 B1 25 64 FF            sub rax, qword ptr [rip - 0x9bda4f]
009D1AD7  48 85 C0                        test rax, rax
009D1ADA  0F 85 7D 0A 00 00               jne 0x1409d255d
009D1AE0  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
009D1AE5  48 8D 44 24 70                  lea rax, [rsp + 0x70]
009D1AEA  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
009D1AEF  33 FF                           xor edi, edi
009D1AF1  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
009D1AF5  48 8D 05 9C 25 64 FF            lea rax, [rip - 0x9bda64]
009D1AFC  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
009D1B01  49 8B D3                        mov rdx, r11
009D1B04  4C 89 44 24 30                  mov qword ptr [rsp + 0x30], r8
009D1B09  49 8B CD                        mov rcx, r13
009D1B0C  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009D1B11  44 8D 47 01                     lea r8d, [rdi + 1]
009D1B15  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
009D1B1A  E8 61 06 F1 FF                  call 0x1408e2180
009D1B1F  8B D8                           mov ebx, eax
009D1B21  85 C0                           test eax, eax
009D1B23  74 67                           je 0x1409d1b8c
009D1B25  3D 23 00 00 C0                  cmp eax, 0xc0000023
009D1B2A  74 60                           je 0x1409d1b8c
009D1B2C  41 3B C7                        cmp eax, r15d
009D1B2F  0F 85 71 FD FF FF               jne 0x1409d18a6
009D1B35  4C 8B 4D 90                     mov r9, qword ptr [rbp - 0x70]
009D1B39  48 8D 44 24 70                  lea rax, [rsp + 0x70]
009D1B3E  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
009D1B43  44 8D 47 01                     lea r8d, [rdi + 1]
009D1B47  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
009D1B4C  49 8B CD                        mov rcx, r13
009D1B4F  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
009D1B54  8B 85 00 01 00 00               mov eax, dword ptr [rbp + 0x100]
009D1B5A  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
009D1B5E  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
009D1B62  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
009D1B67  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009D1B6C  48 8D 05 B5 25 64 FF            lea rax, [rip - 0x9bda4b]
009D1B73  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009D1B78  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
009D1B7D  E8 FE 05 F1 FF                  call 0x1408e2180
009D1B82  8B D8                           mov ebx, eax
009D1B84  85 C0                           test eax, eax
009D1B86  0F 85 3A 06 00 00               jne 0x1409d21c6
009D1B8C  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
009D1B90  89 06                           mov dword ptr [rsi], eax
009D1B92  E9 0F FD FF FF                  jmp 0x1409d18a6
009D1B97  48 8B 0F                        mov rcx, qword ptr [rdi]
009D1B9A  48 2B 0D 27 25 64 FF            sub rcx, qword ptr [rip - 0x9bdad9]
009D1BA1  75 0B                           jne 0x1409d1bae
009D1BA3  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
009D1BA7  48 2B 0D 22 25 64 FF            sub rcx, qword ptr [rip - 0x9bdade]
009D1BAE  48 85 C9                        test rcx, rcx
009D1BB1  0F 84 C6 FC FF FF               je 0x1409d187d
009D1BB7  E9 9C FC FF FF                  jmp 0x1409d1858
009D1BBC  BB 0D 00 00 C0                  mov ebx, 0xc000000d
009D1BC1  E9 F1 FC FF FF                  jmp 0x1409d18b7
009D1BC6  4C 8B 4D 90                     mov r9, qword ptr [rbp - 0x70]
009D1BCA  33 C9                           xor ecx, ecx
009D1BCC  E9 DF FD FF FF                  jmp 0x1409d19b0
009D1BD1  48 8B 07                        mov rax, qword ptr [rdi]
009D1BD4  48 2B 05 C5 25 64 FF            sub rax, qword ptr [rip - 0x9bda3b]
009D1BDB  75 0B                           jne 0x1409d1be8
009D1BDD  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
009D1BE1  48 2B 05 C0 25 64 FF            sub rax, qword ptr [rip - 0x9bda40]
009D1BE8  48 85 C0                        test rax, rax
009D1BEB  0F 85 D8 02 00 00               jne 0x1409d1ec9
009D1BF1  D1 EA                           shr edx, 1
009D1BF3  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
009D1BF8  89 54 24 78                     mov dword ptr [rsp + 0x78], edx
009D1BFC  4D 8B C6                        mov r8, r14
009D1BFF  49 8B D3                        mov rdx, r11
009D1C02  49 8B CD                        mov rcx, r13
009D1C05  E8 5E 07 F6 FF                  call 0x140932368
009D1C0A  33 FF                           xor edi, edi
009D1C0C  8B D8                           mov ebx, eax
009D1C0E  85 C0                           test eax, eax
009D1C10  0F 85 A4 0D 00 00               jne 0x1409d29ba
009D1C16  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
009D1C1A  03 C0                           add eax, eax
009D1C1C  89 06                           mov dword ptr [rsi], eax
009D1C1E  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
009D1C22  C7 00 12 00 00 00               mov dword ptr [rax], 0x12
009D1C28  8B 06                           mov eax, dword ptr [rsi]
009D1C2A  39 85 00 01 00 00               cmp dword ptr [rbp + 0x100], eax
009D1C30  0F 83 70 FC FF FF               jae 0x1409d18a6
009D1C36  BB 23 00 00 C0                  mov ebx, 0xc0000023
009D1C3B  E9 77 FC FF FF                  jmp 0x1409d18b7
009D1C40  48 8B 07                        mov rax, qword ptr [rdi]
009D1C43  48 2B 05 B6 25 64 FF            sub rax, qword ptr [rip - 0x9bda4a]
009D1C4A  75 0B                           jne 0x1409d1c57
009D1C4C  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
009D1C50  48 2B 05 B1 25 64 FF            sub rax, qword ptr [rip - 0x9bda4f]
009D1C57  48 85 C0                        test rax, rax
009D1C5A  0F 84 44 0D 00 00               je 0x1409d29a4
009D1C60  48 8B 07                        mov rax, qword ptr [rdi]
009D1C63  48 2B 05 4E 25 64 FF            sub rax, qword ptr [rip - 0x9bdab2]
009D1C6A  75 0B                           jne 0x1409d1c77
009D1C6C  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
009D1C70  48 2B 05 49 25 64 FF            sub rax, qword ptr [rip - 0x9bdab7]
009D1C77  33 FF                           xor edi, edi
009D1C79  48 85 C0                        test rax, rax
009D1C7C  0F 85 35 FC FF FF               jne 0x1409d18b7
009D1C82  C7 06 01 00 00 00               mov dword ptr [rsi], 1
009D1C88  41 C7 00 11 00 00 00            mov dword ptr [r8], 0x11
009D1C8F  3B 16                           cmp edx, dword ptr [rsi]
009D1C91  72 A3                           jb 0x1409d1c36
009D1C93  49 8B D3                        mov rdx, r11
009D1C96  48 8D 4D A0                     lea rcx, [rbp - 0x60]
009D1C9A  E8 C1 1C A9 FF                  call 0x140463960
009D1C9F  8B D8                           mov ebx, eax
009D1CA1  85 C0                           test eax, eax
009D1CA3  0F 88 FD FB FF FF               js 0x1409d18a6
009D1CA9  41 88 3E                        mov byte ptr [r14], dil
009D1CAC  49 8B 85 08 01 00 00            mov rax, qword ptr [r13 + 0x108]
009D1CB3  48 85 C0                        test rax, rax
009D1CB6  0F 84 F5 09 00 00               je 0x1409d26b1
009D1CBC  48 8D 4D 84                     lea rcx, [rbp - 0x7c]
009D1CC0  89 7C 24 28                     mov dword ptr [rsp + 0x28], edi
009D1CC4  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
009D1CC9  4C 8D 4D 80                     lea r9, [rbp - 0x80]
009D1CCD  49 8B CD                        mov rcx, r13
009D1CD0  4C 8D 44 24 7C                  lea r8, [rsp + 0x7c]
009D1CD5  48 8D 55 A0                     lea rdx, [rbp - 0x60]
009D1CD9  E8 F2 8D CE FF                  call 0x1406baad0
009D1CDE  3D 05 00 00 80                  cmp eax, 0x80000005
009D1CE3  0F 84 4D FF FF FF               je 0x1409d1c36
009D1CE9  3D 0E 00 00 C0                  cmp eax, 0xc000000e
009D1CEE  0F 84 CB 04 00 00               je 0x1409d21bf
009D1CF4  8B D8                           mov ebx, eax
009D1CF6  85 C0                           test eax, eax
009D1CF8  0F 88 B9 FB FF FF               js 0x1409d18b7
009D1CFE  E9 AD 03 00 00                  jmp 0x1409d20b0
009D1D03  48 8B 07                        mov rax, qword ptr [rdi]
009D1D06  48 2B 05 B3 25 64 FF            sub rax, qword ptr [rip - 0x9bda4d]
009D1D0D  75 0B                           jne 0x1409d1d1a
009D1D0F  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
009D1D13  48 2B 05 AE 25 64 FF            sub rax, qword ptr [rip - 0x9bda52]
009D1D1A  48 85 C0                        test rax, rax
009D1D1D  0F 85 C0 00 00 00               jne 0x1409d1de3
009D1D23  4C 8B 45 90                     mov r8, qword ptr [rbp - 0x70]
009D1D27  48 8D 45 84                     lea rax, [rbp - 0x7c]
009D1D2B  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009D1D30  4C 8D 4C 24 7C                  lea r9, [rsp + 0x7c]
009D1D35  48 8D 45 80                     lea rax, [rbp - 0x80]
009D1D39  49 8B D3                        mov rdx, r11
009D1D3C  49 8B CD                        mov rcx, r13
009D1D3F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009D1D44  E8 03 F8 FF FF                  call 0x1409d154c
009D1D49  8B D8                           mov ebx, eax
009D1D4B  85 C0                           test eax, eax
009D1D4D  0F 88 51 FB FF FF               js 0x1409d18a4
009D1D53  44 8B 47 10                     mov r8d, dword ptr [rdi + 0x10]
009D1D57  BA 00 04 00 00                  mov edx, 0x400
009D1D5C  8B 4C 24 7C                     mov ecx, dword ptr [rsp + 0x7c]
009D1D60  41 83 F8 02                     cmp r8d, 2
009D1D64  0F 85 6C 07 00 00               jne 0x1409d24d6
009D1D6A  48 8B 07                        mov rax, qword ptr [rdi]
009D1D6D  48 2B 05 4C 25 64 FF            sub rax, qword ptr [rip - 0x9bdab4]
009D1D74  75 0B                           jne 0x1409d1d81
009D1D76  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
009D1D7A  48 2B 05 47 25 64 FF            sub rax, qword ptr [rip - 0x9bdab9]
009D1D81  48 85 C0                        test rax, rax
009D1D84  0F 85 4C 07 00 00               jne 0x1409d24d6
009D1D8A  41 B9 07 00 00 00               mov r9d, 7
009D1D90  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
009D1D94  C7 06 04 00 00 00               mov dword ptr [rsi], 4
009D1D9A  44 89 08                        mov dword ptr [rax], r9d
009D1D9D  8B 06                           mov eax, dword ptr [rsi]
009D1D9F  39 85 00 01 00 00               cmp dword ptr [rbp + 0x100], eax
009D1DA5  0F 82 8B FE FF FF               jb 0x1409d1c36
009D1DAB  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
009D1DAE  83 F8 02                        cmp eax, 2
009D1DB1  0F 85 C0 08 00 00               jne 0x1409d2677
009D1DB7  48 8B 07                        mov rax, qword ptr [rdi]
009D1DBA  48 2B 05 FF 24 64 FF            sub rax, qword ptr [rip - 0x9bdb01]
009D1DC1  75 0B                           jne 0x1409d1dce
009D1DC3  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
009D1DC7  48 2B 05 FA 24 64 FF            sub rax, qword ptr [rip - 0x9bdb06]
009D1DCE  48 85 C0                        test rax, rax
009D1DD1  0F 85 34 0A 00 00               jne 0x1409d280b
009D1DD7  41 89 0E                        mov dword ptr [r14], ecx
009D1DDA  E9 D8 FA FF FF                  jmp 0x1409d18b7
009D1DDF  4C 8B 4D 90                     mov r9, qword ptr [rbp - 0x70]
009D1DE3  48 8B 07                        mov rax, qword ptr [rdi]
009D1DE6  48 2B 05 2B 24 64 FF            sub rax, qword ptr [rip - 0x9bdbd5]
009D1DED  75 0B                           jne 0x1409d1dfa
009D1DEF  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
009D1DF3  48 2B 05 26 24 64 FF            sub rax, qword ptr [rip - 0x9bdbda]
009D1DFA  48 85 C0                        test rax, rax
009D1DFD  0F 85 B0 0A 00 00               jne 0x1409d28b3
009D1E03  C7 06 01 00 00 00               mov dword ptr [rsi], 1
009D1E09  41 C7 00 11 00 00 00            mov dword ptr [r8], 0x11
009D1E10  3B 16                           cmp edx, dword ptr [rsi]
009D1E12  0F 82 1E FE FF FF               jb 0x1409d1c36
009D1E18  4D 8B C1                        mov r8, r9
009D1E1B  49 8B D3                        mov rdx, r11
009D1E1E  49 8B CD                        mov rcx, r13
009D1E21  E8 1A F2 FF FF                  call 0x1409d1040
009D1E26  F6 D8                           neg al
009D1E28  1A C9                           sbb cl, cl
009D1E2A  E9 89 FC FF FF                  jmp 0x1409d1ab8
009D1E2F  48 8B 07                        mov rax, qword ptr [rdi]
009D1E32  48 2B 05 AF 23 64 FF            sub rax, qword ptr [rip - 0x9bdc51]
009D1E39  75 0B                           jne 0x1409d1e46
009D1E3B  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
009D1E3F  48 2B 05 AA 23 64 FF            sub rax, qword ptr [rip - 0x9bdc56]
009D1E46  33 FF                           xor edi, edi
009D1E48  48 85 C0                        test rax, rax
009D1E4B  0F 85 66 FA FF FF               jne 0x1409d18b7
009D1E51  49 8B D3                        mov rdx, r11
009D1E54  41 C7 00 12 20 00 00            mov dword ptr [r8], 0x2012
009D1E5B  48 8D 4D A0                     lea rcx, [rbp - 0x60]
009D1E5F  E8 FC 1A A9 FF                  call 0x140463960
009D1E64  8B D8                           mov ebx, eax
009D1E66  85 C0                           test eax, eax
009D1E68  0F 88 38 FA FF FF               js 0x1409d18a6
009D1E6E  49 8B 85 00 01 00 00            mov rax, qword ptr [r13 + 0x100]
009D1E75  48 85 C0                        test rax, rax
009D1E78  0F 84 33 08 00 00               je 0x1409d26b1
009D1E7E  44 8D 47 0E                     lea r8d, [rdi + 0xe]
009D1E82  8B 8D 00 01 00 00               mov ecx, dword ptr [rbp + 0x100]
009D1E88  48 8D 55 A0                     lea rdx, [rbp - 0x60]
009D1E8C  89 7C 24 30                     mov dword ptr [rsp + 0x30], edi
009D1E90  4D 8B CE                        mov r9, r14
009D1E93  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
009D1E98  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
009D1E9C  49 8B CD                        mov rcx, r13
009D1E9F  E8 2C 8C CE FF                  call 0x1406baad0
009D1EA4  3D 05 00 00 80                  cmp eax, 0x80000005
009D1EA9  0F 84 87 FD FF FF               je 0x1409d1c36
009D1EAF  3D 34 00 00 C0                  cmp eax, 0xc0000034
009D1EB4  0F 84 98 00 00 00               je 0x1409d1f52
009D1EBA  8B D8                           mov ebx, eax
009D1EBC  85 C0                           test eax, eax
009D1EBE  0F 88 E2 F9 FF FF               js 0x1409d18a6
009D1EC4  E9 EE F9 FF FF                  jmp 0x1409d18b7
009D1EC9  48 8B 07                        mov rax, qword ptr [rdi]
009D1ECC  48 2B 05 FD 22 64 FF            sub rax, qword ptr [rip - 0x9bdd03]
009D1ED3  75 0B                           jne 0x1409d1ee0
009D1ED5  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
009D1ED9  48 2B 05 F8 22 64 FF            sub rax, qword ptr [rip - 0x9bdd08]
009D1EE0  33 FF                           xor edi, edi
009D1EE2  48 85 C0                        test rax, rax
009D1EE5  0F 85 CC F9 FF FF               jne 0x1409d18b7
009D1EEB  45 89 08                        mov dword ptr [r8], r9d
009D1EEE  48 8D 4D A0                     lea rcx, [rbp - 0x60]
009D1EF2  49 8B D3                        mov rdx, r11
009D1EF5  44 89 26                        mov dword ptr [rsi], r12d
009D1EF8  E8 63 1A A9 FF                  call 0x140463960
009D1EFD  8B D8                           mov ebx, eax
009D1EFF  85 C0                           test eax, eax
009D1F01  0F 88 9F F9 FF FF               js 0x1409d18a6
009D1F07  49 8B 85 00 01 00 00            mov rax, qword ptr [r13 + 0x100]
009D1F0E  48 85 C0                        test rax, rax
009D1F11  0F 84 9A 07 00 00               je 0x1409d26b1
009D1F17  48 8D 8D 00 01 00 00            lea rcx, [rbp + 0x100]
009D1F1E  89 7C 24 30                     mov dword ptr [rsp + 0x30], edi
009D1F22  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
009D1F27  44 8D 47 0D                     lea r8d, [rdi + 0xd]
009D1F2B  8B 8D 00 01 00 00               mov ecx, dword ptr [rbp + 0x100]
009D1F31  48 8D 55 A0                     lea rdx, [rbp - 0x60]
009D1F35  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
009D1F39  4D 8B CE                        mov r9, r14
009D1F3C  49 8B CD                        mov rcx, r13
009D1F3F  E8 8C 8B CE FF                  call 0x1406baad0
009D1F44  48 8B D8                        mov rbx, rax
009D1F47  3D 34 00 00 C0                  cmp eax, 0xc0000034
009D1F4C  0F 85 78 0A 00 00               jne 0x1409d29ca
009D1F52  41 8B DF                        mov ebx, r15d
009D1F55  E9 5D F9 FF FF                  jmp 0x1409d18b7
009D1F5A  48 8B 07                        mov rax, qword ptr [rdi]
009D1F5D  48 2B 05 14 23 64 FF            sub rax, qword ptr [rip - 0x9bdcec]
009D1F64  75 0B                           jne 0x1409d1f71
009D1F66  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
009D1F6A  48 2B 05 0F 23 64 FF            sub rax, qword ptr [rip - 0x9bdcf1]
009D1F71  48 85 C0                        test rax, rax
009D1F74  0F 84 35 0A 00 00               je 0x1409d29af
009D1F7A  48 8B 07                        mov rax, qword ptr [rdi]
009D1F7D  48 2B 05 DC 22 64 FF            sub rax, qword ptr [rip - 0x9bdd24]
009D1F84  75 0B                           jne 0x1409d1f91
009D1F86  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
009D1F8A  48 2B 05 D7 22 64 FF            sub rax, qword ptr [rip - 0x9bdd29]
009D1F91  33 FF                           xor edi, edi
009D1F93  48 85 C0                        test rax, rax
009D1F96  0F 85 1B F9 FF FF               jne 0x1409d18b7
009D1F9C  41 C7 00 11 00 00 00            mov dword ptr [r8], 0x11
009D1FA3  C7 06 01 00 00 00               mov dword ptr [rsi], 1
009D1FA9  83 FA 01                        cmp edx, 1
009D1FAC  0F 82 84 FC FF FF               jb 0x1409d1c36
009D1FB2  49 8B D3                        mov rdx, r11
009D1FB5  48 8D 4D A0                     lea rcx, [rbp - 0x60]
009D1FB9  E8 A2 19 A9 FF                  call 0x140463960
009D1FBE  8B D8                           mov ebx, eax
009D1FC0  85 C0                           test eax, eax
009D1FC2  0F 88 DE F8 FF FF               js 0x1409d18a6
009D1FC8  41 88 3E                        mov byte ptr [r14], dil
009D1FCB  49 8B 85 08 01 00 00            mov rax, qword ptr [r13 + 0x108]
009D1FD2  48 85 C0                        test rax, rax
009D1FD5  0F 84 D6 06 00 00               je 0x1409d26b1
009D1FDB  48 8D 4D 84                     lea rcx, [rbp - 0x7c]
009D1FDF  89 7C 24 28                     mov dword ptr [rsp + 0x28], edi
009D1FE3  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
009D1FE8  4C 8D 4D 80                     lea r9, [rbp - 0x80]
009D1FEC  49 8B CD                        mov rcx, r13
009D1FEF  4C 8D 44 24 7C                  lea r8, [rsp + 0x7c]
009D1FF4  48 8D 55 A0                     lea rdx, [rbp - 0x60]
009D1FF8  E8 D3 8A CE FF                  call 0x1406baad0
009D1FFD  3D 05 00 00 80                  cmp eax, 0x80000005
009D2002  0F 84 2E FC FF FF               je 0x1409d1c36
009D2008  3D 0E 00 00 C0                  cmp eax, 0xc000000e
009D200D  0F 84 AC 01 00 00               je 0x1409d21bf
009D2013  8B D8                           mov ebx, eax
009D2015  85 C0                           test eax, eax
009D2017  0F 88 9A F8 FF FF               js 0x1409d18b7
009D201D  8B 4C 24 7C                     mov ecx, dword ptr [rsp + 0x7c]
009D2021  0F BA E1 0F                     bt ecx, 0xf
009D2025  0F 82 85 00 00 00               jb 0x1409d20b0
009D202B  0F BA E1 0A                     bt ecx, 0xa
009D202F  0F 82 86 06 00 00               jb 0x1409d26bb
009D2035  F6 C1 08                        test cl, 8
009D2038  0F 85 79 F8 FF FF               jne 0x1409d18b7
009D203E  8B 7D 88                        mov edi, dword ptr [rbp - 0x78]
009D2041  48 8D 44 24 70                  lea rax, [rsp + 0x70]
009D2046  4C 8B 4D 90                     mov r9, qword ptr [rbp - 0x70]
009D204A  49 8B CD                        mov rcx, r13
009D204D  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
009D2052  89 7C 24 50                     mov dword ptr [rsp + 0x50], edi
009D2056  33 FF                           xor edi, edi
009D2058  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
009D205D  48 8D 45 B0                     lea rax, [rbp - 0x50]
009D2061  44 89 64 24 40                  mov dword ptr [rsp + 0x40], r12d
009D2066  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
009D206B  48 8D 44 24 74                  lea rax, [rsp + 0x74]
009D2070  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009D2075  44 8D 47 01                     lea r8d, [rdi + 1]
009D2079  48 8D 05 58 22 64 FF            lea rax, [rip - 0x9bdda8]
009D2080  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009D2085  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
009D208A  E8 F1 00 F1 FF                  call 0x1408e2180
009D208F  8B D8                           mov ebx, eax
009D2091  41 3B C7                        cmp eax, r15d
009D2094  0F 84 25 01 00 00               je 0x1409d21bf
009D209A  85 C0                           test eax, eax
009D209C  0F 88 04 F8 FF FF               js 0x1409d18a6
009D20A2  44 8D 67 40                     lea r12d, [rdi + 0x40]
009D20A6  44 84 65 B0                     test byte ptr [rbp - 0x50], r12b
009D20AA  0F 84 07 F8 FF FF               je 0x1409d18b7
009D20B0  41 C6 06 FF                     mov byte ptr [r14], 0xff
009D20B4  E9 FE F7 FF FF                  jmp 0x1409d18b7
009D20B9  48 8B 07                        mov rax, qword ptr [rdi]
009D20BC  48 2B 05 6D 21 64 FF            sub rax, qword ptr [rip - 0x9bde93]
009D20C3  75 0B                           jne 0x1409d20d0
009D20C5  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
009D20C9  48 2B 05 68 21 64 FF            sub rax, qword ptr [rip - 0x9bde98]
009D20D0  33 FF                           xor edi, edi
009D20D2  48 85 C0                        test rax, rax
009D20D5  0F 85 DC F7 FF FF               jne 0x1409d18b7
009D20DB  41 C7 00 11 00 00 00            mov dword ptr [r8], 0x11
009D20E2  C7 06 01 00 00 00               mov dword ptr [rsi], 1
009D20E8  83 FA 01                        cmp edx, 1
009D20EB  0F 82 45 FB FF FF               jb 0x1409d1c36
009D20F1  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
009D20F6  48 8D 44 24 70                  lea rax, [rsp + 0x70]
009D20FB  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
009D2100  44 8D 47 01                     lea r8d, [rdi + 1]
009D2104  C7 44 24 40 01 00 00 00         mov dword ptr [rsp + 0x40], 1
009D210C  48 8D 44 24 60                  lea rax, [rsp + 0x60]
009D2111  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
009D2116  49 8B D3                        mov rdx, r11
009D2119  48 8D 44 24 74                  lea rax, [rsp + 0x74]
009D211E  41 88 3E                        mov byte ptr [r14], dil
009D2121  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009D2126  49 8B CD                        mov rcx, r13
009D2129  48 8D 05 60 21 64 FF            lea rax, [rip - 0x9bdea0]
009D2130  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009D2135  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
009D213A  E8 41 00 F1 FF                  call 0x1408e2180
009D213F  8B D8                           mov ebx, eax
009D2141  85 C0                           test eax, eax
009D2143  0F 89 C8 04 00 00               jns 0x1409d2611
009D2149  41 3B C7                        cmp eax, r15d
009D214C  0F 85 15 05 00 00               jne 0x1409d2667
009D2152  4C 8B 4D 90                     mov r9, qword ptr [rbp - 0x70]
009D2156  48 8D 44 24 70                  lea rax, [rsp + 0x70]
009D215B  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
009D2160  41 B8 01 00 00 00               mov r8d, 1
009D2166  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
009D216B  49 8B CD                        mov rcx, r13
009D216E  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
009D2173  48 8D 44 24 60                  lea rax, [rsp + 0x60]
009D2178  C7 44 24 40 01 00 00 00         mov dword ptr [rsp + 0x40], 1
009D2180  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
009D2185  48 8D 44 24 74                  lea rax, [rsp + 0x74]
009D218A  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009D218F  48 8D 05 12 21 64 FF            lea rax, [rip - 0x9bdeee]
009D2196  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009D219B  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
009D21A0  E8 DB FF F0 FF                  call 0x1408e2180
009D21A5  8B D8                           mov ebx, eax
009D21A7  85 C0                           test eax, eax
009D21A9  0F 89 3B 08 00 00               jns 0x1409d29ea
009D21AF  41 3B C7                        cmp eax, r15d
009D21B2  74 0B                           je 0x1409d21bf
009D21B4  3D 23 00 00 C0                  cmp eax, 0xc0000023
009D21B9  0F 85 E7 F6 FF FF               jne 0x1409d18a6
009D21BF  8B DF                           mov ebx, edi
009D21C1  E9 F1 F6 FF FF                  jmp 0x1409d18b7
009D21C6  3D 23 00 00 C0                  cmp eax, 0xc0000023
009D21CB  0F 84 BB F9 FF FF               je 0x1409d1b8c
009D21D1  41 3B C7                        cmp eax, r15d
009D21D4  0F 85 CC F6 FF FF               jne 0x1409d18a6
009D21DA  E9 D8 F6 FF FF                  jmp 0x1409d18b7
009D21DF  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
009D21E4  48 8D 45 B8                     lea rax, [rbp - 0x48]
009D21E8  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009D21ED  45 33 C9                        xor r9d, r9d
009D21F0  40 88 7C 24 28                  mov byte ptr [rsp + 0x28], dil
009D21F5  49 8B D3                        mov rdx, r11
009D21F8  49 8B CD                        mov rcx, r13
009D21FB  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
009D2203  45 8D 41 10                     lea r8d, [r9 + 0x10]
009D2207  E8 34 C3 F1 FF                  call 0x1408ee540
009D220C  8B D8                           mov ebx, eax
009D220E  85 C0                           test eax, eax
009D2210  0F 85 F4 07 00 00               jne 0x1409d2a0a
009D2216  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
009D221A  E8 91 B0 CD FF                  call 0x1406ad2b0
009D221F  E9 2E FD FF FF                  jmp 0x1409d1f52
009D2224  48 8B 07                        mov rax, qword ptr [rdi]
009D2227  48 2B 05 1A 20 64 FF            sub rax, qword ptr [rip - 0x9bdfe6]
009D222E  75 0B                           jne 0x1409d223b
009D2230  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
009D2234  48 2B 05 15 20 64 FF            sub rax, qword ptr [rip - 0x9bdfeb]
009D223B  33 FF                           xor edi, edi
009D223D  48 85 C0                        test rax, rax
009D2240  0F 85 71 F6 FF FF               jne 0x1409d18b7
009D2246  D1 EA                           shr edx, 1
009D2248  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
009D224D  89 54 24 78                     mov dword ptr [rsp + 0x78], edx
009D2251  4D 8B C6                        mov r8, r14
009D2254  49 8B D3                        mov rdx, r11
009D2257  49 8B CD                        mov rcx, r13
009D225A  E8 7D E6 FF FF                  call 0x1409d08dc
009D225F  8B D8                           mov ebx, eax
009D2261  3D 23 00 00 C0                  cmp eax, 0xc0000023
009D2266  0F 84 36 03 00 00               je 0x1409d25a2
009D226C  85 C0                           test eax, eax
009D226E  0F 85 32 F6 FF FF               jne 0x1409d18a6
009D2274  E9 29 03 00 00                  jmp 0x1409d25a2
009D2279  D1 EA                           shr edx, 1
009D227B  48 8D 44 24 78                  lea rax, [rsp + 0x78]
009D2280  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009D2285  4D 8B CE                        mov r9, r14
009D2288  89 54 24 20                     mov dword ptr [rsp + 0x20], edx
009D228C  45 8B C4                        mov r8d, r12d
009D228F  49 8B D3                        mov rdx, r11
009D2292  49 8B CD                        mov rcx, r13
009D2295  E8 C6 E3 FF FF                  call 0x1409d0660
009D229A  8B D8                           mov ebx, eax
009D229C  3D 34 00 00 C0                  cmp eax, 0xc0000034
009D22A1  0F 84 AB FC FF FF               je 0x1409d1f52
009D22A7  33 FF                           xor edi, edi
009D22A9  85 C0                           test eax, eax
009D22AB  74 0B                           je 0x1409d22b8
009D22AD  3D 23 00 00 C0                  cmp eax, 0xc0000023
009D22B2  0F 85 EE F5 FF FF               jne 0x1409d18a6
009D22B8  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
009D22BC  C7 00 12 20 00 00               mov dword ptr [rax], 0x2012
009D22C2  85 DB                           test ebx, ebx
009D22C4  0F 84 67 03 00 00               je 0x1409d2631
009D22CA  81 FB 23 00 00 C0               cmp ebx, 0xc0000023
009D22D0  0F 85 D0 F5 FF FF               jne 0x1409d18a6
009D22D6  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
009D22DA  03 C0                           add eax, eax
009D22DC  89 06                           mov dword ptr [rsi], eax
009D22DE  E9 D4 F5 FF FF                  jmp 0x1409d18b7
009D22E3  48 8B 07                        mov rax, qword ptr [rdi]
009D22E6  48 2B 05 03 20 64 FF            sub rax, qword ptr [rip - 0x9bdffd]
009D22ED  75 0B                           jne 0x1409d22fa
009D22EF  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
009D22F3  48 2B 05 FE 1F 64 FF            sub rax, qword ptr [rip - 0x9be002]
009D22FA  33 FF                           xor edi, edi
009D22FC  48 85 C0                        test rax, rax
009D22FF  0F 85 B2 F5 FF FF               jne 0x1409d18b7
009D2305  41 C7 00 11 00 00 00            mov dword ptr [r8], 0x11
009D230C  C7 06 01 00 00 00               mov dword ptr [rsi], 1
009D2312  83 FA 01                        cmp edx, 1
009D2315  0F 82 1B F9 FF FF               jb 0x1409d1c36
009D231B  49 8B D3                        mov rdx, r11
009D231E  48 8D 4D A0                     lea rcx, [rbp - 0x60]
009D2322  E8 39 16 A9 FF                  call 0x140463960
009D2327  8B D8                           mov ebx, eax
009D2329  85 C0                           test eax, eax
009D232B  0F 88 75 F5 FF FF               js 0x1409d18a6
009D2331  41 88 3E                        mov byte ptr [r14], dil
009D2334  49 8B 85 08 01 00 00            mov rax, qword ptr [r13 + 0x108]
009D233B  48 85 C0                        test rax, rax
009D233E  0F 84 6D 03 00 00               je 0x1409d26b1
009D2344  48 8D 4D 84                     lea rcx, [rbp - 0x7c]
009D2348  89 7C 24 28                     mov dword ptr [rsp + 0x28], edi
009D234C  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
009D2351  4C 8D 4D 80                     lea r9, [rbp - 0x80]
009D2355  49 8B CD                        mov rcx, r13
009D2358  4C 8D 44 24 7C                  lea r8, [rsp + 0x7c]
009D235D  48 8D 55 A0                     lea rdx, [rbp - 0x60]
009D2361  E8 6A 87 CE FF                  call 0x1406baad0
009D2366  3D 05 00 00 80                  cmp eax, 0x80000005
009D236B  0F 84 C5 F8 FF FF               je 0x1409d1c36
009D2371  3D 0E 00 00 C0                  cmp eax, 0xc000000e
009D2376  0F 84 43 FE FF FF               je 0x1409d21bf
009D237C  8B D8                           mov ebx, eax
009D237E  85 C0                           test eax, eax
009D2380  0F 88 31 F5 FF FF               js 0x1409d18b7
009D2386  F7 44 24 7C 00 00 00 02         test dword ptr [rsp + 0x7c], 0x2000000
009D238E  0F 85 23 F5 FF FF               jne 0x1409d18b7
009D2394  8B 7D 88                        mov edi, dword ptr [rbp - 0x78]
009D2397  48 8D 44 24 70                  lea rax, [rsp + 0x70]
009D239C  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
009D23A1  45 33 C9                        xor r9d, r9d
009D23A4  89 7C 24 50                     mov dword ptr [rsp + 0x50], edi
009D23A8  49 8B CD                        mov rcx, r13
009D23AB  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
009D23B0  33 FF                           xor edi, edi
009D23B2  C7 44 24 40 01 00 00 00         mov dword ptr [rsp + 0x40], 1
009D23BA  48 8D 44 24 60                  lea rax, [rsp + 0x60]
009D23BF  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
009D23C4  48 8D 44 24 74                  lea rax, [rsp + 0x74]
009D23C9  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009D23CE  48 8D 05 4B 1F 64 FF            lea rax, [rip - 0x9be0b5]
009D23D5  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009D23DA  44 8D 47 01                     lea r8d, [rdi + 1]
009D23DE  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
009D23E3  E8 98 FD F0 FF                  call 0x1408e2180
009D23E8  8B D8                           mov ebx, eax
009D23EA  85 C0                           test eax, eax
009D23EC  0F 88 E4 03 00 00               js 0x1409d27d6
009D23F2  83 7C 24 74 11                  cmp dword ptr [rsp + 0x74], 0x11
009D23F7  0F 85 B3 FC FF FF               jne 0x1409d20b0
009D23FD  80 7C 24 60 FF                  cmp byte ptr [rsp + 0x60], 0xff
009D2402  E9 A3 FC FF FF                  jmp 0x1409d20aa
009D2407  48 8B 07                        mov rax, qword ptr [rdi]
009D240A  48 2B 05 F7 1E 64 FF            sub rax, qword ptr [rip - 0x9be109]
009D2411  75 0B                           jne 0x1409d241e
009D2413  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
009D2417  48 2B 05 F2 1E 64 FF            sub rax, qword ptr [rip - 0x9be10e]
009D241E  33 FF                           xor edi, edi
009D2420  48 85 C0                        test rax, rax
009D2423  0F 85 8E F4 FF FF               jne 0x1409d18b7
009D2429  41 C7 00 11 00 00 00            mov dword ptr [r8], 0x11
009D2430  C7 06 01 00 00 00               mov dword ptr [rsi], 1
009D2436  83 FA 01                        cmp edx, 1
009D2439  0F 82 F7 F7 FF FF               jb 0x1409d1c36
009D243F  49 8B D3                        mov rdx, r11
009D2442  48 8D 4D A0                     lea rcx, [rbp - 0x60]
009D2446  E8 15 15 A9 FF                  call 0x140463960
009D244B  8B D8                           mov ebx, eax
009D244D  85 C0                           test eax, eax
009D244F  0F 88 51 F4 FF FF               js 0x1409d18a6
009D2455  41 88 3E                        mov byte ptr [r14], dil
009D2458  49 8B 85 08 01 00 00            mov rax, qword ptr [r13 + 0x108]
009D245F  48 85 C0                        test rax, rax
009D2462  0F 84 49 02 00 00               je 0x1409d26b1
009D2468  48 8D 4D 84                     lea rcx, [rbp - 0x7c]
009D246C  89 7C 24 28                     mov dword ptr [rsp + 0x28], edi
009D2470  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
009D2475  4C 8D 4D 80                     lea r9, [rbp - 0x80]
009D2479  49 8B CD                        mov rcx, r13
009D247C  4C 8D 44 24 7C                  lea r8, [rsp + 0x7c]
009D2481  48 8D 55 A0                     lea rdx, [rbp - 0x60]
009D2485  E8 46 86 CE FF                  call 0x1406baad0
009D248A  3D 0E 00 00 C0                  cmp eax, 0xc000000e
009D248F  0F 84 2A FD FF FF               je 0x1409d21bf
009D2495  3D 05 00 00 80                  cmp eax, 0x80000005
009D249A  0F 84 96 F7 FF FF               je 0x1409d1c36
009D24A0  8B D8                           mov ebx, eax
009D24A2  85 C0                           test eax, eax
009D24A4  0F 88 0D F4 FF FF               js 0x1409d18b7
009D24AA  F7 44 24 7C 00 01 00 00         test dword ptr [rsp + 0x7c], 0x100
009D24B2  0F 85 F8 FB FF FF               jne 0x1409d20b0
009D24B8  BA 00 04 00 00                  mov edx, 0x400
009D24BD  85 54 24 7C                     test dword ptr [rsp + 0x7c], edx
009D24C1  0F 84 F0 F3 FF FF               je 0x1409d18b7
009D24C7  83 7D 80 0E                     cmp dword ptr [rbp - 0x80], 0xe
009D24CB  0F 85 E6 F3 FF FF               jne 0x1409d18b7
009D24D1  E9 DA FB FF FF                  jmp 0x1409d20b0
009D24D6  41 83 F8 03                     cmp r8d, 3
009D24DA  75 20                           jne 0x1409d24fc
009D24DC  48 8B 07                        mov rax, qword ptr [rdi]
009D24DF  48 2B 05 72 9A 64 FF            sub rax, qword ptr [rip - 0x9b658e]
009D24E6  75 0B                           jne 0x1409d24f3
009D24E8  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
009D24EC  48 2B 05 6D 9A 64 FF            sub rax, qword ptr [rip - 0x9b6593]
009D24F3  48 85 C0                        test rax, rax
009D24F6  0F 84 8E F8 FF FF               je 0x1409d1d8a
009D24FC  85 CA                           test edx, ecx
009D24FE  0F 84 4E FA FF FF               je 0x1409d1f52
009D2504  41 B9 18 00 00 00               mov r9d, 0x18
009D250A  E9 81 F8 FF FF                  jmp 0x1409d1d90
009D250F  48 8B 0F                        mov rcx, qword ptr [rdi]
009D2512  48 2B 0D 3F 9A 64 FF            sub rcx, qword ptr [rip - 0x9b65c1]
009D2519  75 0B                           jne 0x1409d2526
009D251B  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
009D251F  48 2B 0D 3A 9A 64 FF            sub rcx, qword ptr [rip - 0x9b65c6]
009D2526  48 85 C9                        test rcx, rcx
009D2529  0F 85 62 F2 FF FF               jne 0x1409d1791
009D252F  E9 EF F7 FF FF                  jmp 0x1409d1d23
009D2534  48 8B 0F                        mov rcx, qword ptr [rdi]
009D2537  48 2B 0D FA 1D 64 FF            sub rcx, qword ptr [rip - 0x9be206]
009D253E  75 0B                           jne 0x1409d254b
009D2540  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
009D2544  48 2B 0D F5 1D 64 FF            sub rcx, qword ptr [rip - 0x9be20b]
009D254B  48 85 C9                        test rcx, rcx
009D254E  0F 85 D8 F2 FF FF               jne 0x1409d182c
009D2554  44 8D 61 20                     lea r12d, [rcx + 0x20]
009D2558  E9 1C FD FF FF                  jmp 0x1409d2279
009D255D  48 8B 07                        mov rax, qword ptr [rdi]
009D2560  48 2B 05 49 1E 64 FF            sub rax, qword ptr [rip - 0x9be1b7]
009D2567  75 0B                           jne 0x1409d2574
009D2569  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
009D256D  48 2B 05 44 1E 64 FF            sub rax, qword ptr [rip - 0x9be1bc]
009D2574  33 FF                           xor edi, edi
009D2576  48 85 C0                        test rax, rax
009D2579  0F 85 38 F3 FF FF               jne 0x1409d18b7
009D257F  D1 EA                           shr edx, 1
009D2581  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
009D2586  89 54 24 78                     mov dword ptr [rsp + 0x78], edx
009D258A  4D 8B C6                        mov r8, r14
009D258D  49 8B D3                        mov rdx, r11
009D2590  49 8B CD                        mov rcx, r13
009D2593  E8 9C E1 FF FF                  call 0x1409d0734
009D2598  8B D8                           mov ebx, eax
009D259A  85 C0                           test eax, eax
009D259C  0F 85 07 03 00 00               jne 0x1409d28a9
009D25A2  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
009D25A6  03 C0                           add eax, eax
009D25A8  89 06                           mov dword ptr [rsi], eax
009D25AA  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
009D25AE  C7 00 12 20 00 00               mov dword ptr [rax], 0x2012
009D25B4  E9 6F F6 FF FF                  jmp 0x1409d1c28
009D25B9  48 8B 07                        mov rax, qword ptr [rdi]
009D25BC  48 2B 05 A5 1D 64 FF            sub rax, qword ptr [rip - 0x9be25b]
009D25C3  75 0B                           jne 0x1409d25d0
009D25C5  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
009D25C9  48 2B 05 A0 1D 64 FF            sub rax, qword ptr [rip - 0x9be260]
009D25D0  33 FF                           xor edi, edi
009D25D2  48 85 C0                        test rax, rax
009D25D5  0F 85 DC F2 FF FF               jne 0x1409d18b7
009D25DB  49 8B D3                        mov rdx, r11
009D25DE  41 C7 00 12 20 00 00            mov dword ptr [r8], 0x2012
009D25E5  48 8D 4D A0                     lea rcx, [rbp - 0x60]
009D25E9  E8 72 13 A9 FF                  call 0x140463960
009D25EE  8B D8                           mov ebx, eax
009D25F0  85 C0                           test eax, eax
009D25F2  0F 88 AE F2 FF FF               js 0x1409d18a6
009D25F8  49 8B 85 00 01 00 00            mov rax, qword ptr [r13 + 0x100]
009D25FF  48 85 C0                        test rax, rax
009D2602  0F 84 A9 00 00 00               je 0x1409d26b1
009D2608  44 8D 47 10                     lea r8d, [rdi + 0x10]
009D260C  E9 71 F8 FF FF                  jmp 0x1409d1e82
009D2611  83 7C 24 74 11                  cmp dword ptr [rsp + 0x74], 0x11
009D2616  0F 85 36 FB FF FF               jne 0x1409d2152
009D261C  83 7C 24 70 01                  cmp dword ptr [rsp + 0x70], 1
009D2621  0F 85 2B FB FF FF               jne 0x1409d2152
009D2627  40 38 7C 24 60                  cmp byte ptr [rsp + 0x60], dil
009D262C  E9 9A FE FF FF                  jmp 0x1409d24cb
009D2631  49 8B CE                        mov rcx, r14
009D2634  E8 47 0B 00 00                  call 0x1409d3180
009D2639  E9 9C FC FF FF                  jmp 0x1409d22da
009D263E  48 8B 0F                        mov rcx, qword ptr [rdi]
009D2641  48 2B 0D F8 1D 64 FF            sub rcx, qword ptr [rip - 0x9be208]
009D2648  75 0B                           jne 0x1409d2655
009D264A  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
009D264E  48 2B 0D F3 1D 64 FF            sub rcx, qword ptr [rip - 0x9be20d]
009D2655  48 85 C9                        test rcx, rcx
009D2658  0F 85 CE F1 FF FF               jne 0x1409d182c
009D265E  44 8D 61 40                     lea r12d, [rcx + 0x40]
009D2662  E9 12 FC FF FF                  jmp 0x1409d2279
009D2667  3D 23 00 00 C0                  cmp eax, 0xc0000023
009D266C  0F 85 34 F2 FF FF               jne 0x1409d18a6
009D2672  E9 DB FA FF FF                  jmp 0x1409d2152
009D2677  83 F8 03                        cmp eax, 3
009D267A  0F 85 8B 01 00 00               jne 0x1409d280b
009D2680  48 8B 07                        mov rax, qword ptr [rdi]
009D2683  48 2B 05 CE 98 64 FF            sub rax, qword ptr [rip - 0x9b6732]
009D268A  75 0B                           jne 0x1409d2697
009D268C  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
009D2690  48 2B 05 C9 98 64 FF            sub rax, qword ptr [rip - 0x9b6737]
009D2697  48 85 C0                        test rax, rax
009D269A  0F 85 6B 01 00 00               jne 0x1409d280b
009D26A0  23 CA                           and ecx, edx
009D26A2  F7 D9                           neg ecx
009D26A4  1B C0                           sbb eax, eax
009D26A6  23 45 80                        and eax, dword ptr [rbp - 0x80]
009D26A9  41 89 06                        mov dword ptr [r14], eax
009D26AC  E9 06 F2 FF FF                  jmp 0x1409d18b7
009D26B1  BB 02 00 00 C0                  mov ebx, 0xc0000002
009D26B6  E9 FC F1 FF FF                  jmp 0x1409d18b7
009D26BB  8B 55 80                        mov edx, dword ptr [rbp - 0x80]
009D26BE  83 FA 1D                        cmp edx, 0x1d
009D26C1  0F 87 E9 F9 FF FF               ja 0x1409d20b0
009D26C7  41 B8 00 00 40 23               mov r8d, 0x23400000
009D26CD  41 0F A3 D0                     bt r8d, edx
009D26D1  0F 82 5E F9 FF FF               jb 0x1409d2035
009D26D7  E9 D4 F9 FF FF                  jmp 0x1409d20b0
009D26DC  83 F8 66                        cmp eax, 0x66
009D26DF  0F 85 D2 F1 FF FF               jne 0x1409d18b7
009D26E5  48 8B 07                        mov rax, qword ptr [rdi]
009D26E8  48 2B 05 89 ED 63 FF            sub rax, qword ptr [rip - 0x9c1277]
009D26EF  75 0B                           jne 0x1409d26fc
009D26F1  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
009D26F5  48 2B 05 84 ED 63 FF            sub rax, qword ptr [rip - 0x9c127c]
009D26FC  33 FF                           xor edi, edi
009D26FE  48 85 C0                        test rax, rax
009D2701  0F 85 B0 F1 FF FF               jne 0x1409d18b7
009D2707  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
009D270C  48 8D 44 24 70                  lea rax, [rsp + 0x70]
009D2711  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
009D2716  44 8D 47 01                     lea r8d, [rdi + 1]
009D271A  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
009D271E  48 8D 44 24 74                  lea rax, [rsp + 0x74]
009D2723  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
009D2728  49 8B D3                        mov rdx, r11
009D272B  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009D2730  49 8B CD                        mov rcx, r13
009D2733  48 8D 05 EE EF 63 FF            lea rax, [rip - 0x9c1012]
009D273A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009D273F  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
009D2744  E8 37 FA F0 FF                  call 0x1408e2180
009D2749  B9 00 00 00 80                  mov ecx, 0x80000000
009D274E  8B D8                           mov ebx, eax
009D2750  03 C1                           add eax, ecx
009D2752  85 C1                           test ecx, eax
009D2754  0F 84 B9 00 00 00               je 0x1409d2813
009D275A  83 7C 24 74 13                  cmp dword ptr [rsp + 0x74], 0x13
009D275F  0F 85 C3 00 00 00               jne 0x1409d2828
009D2765  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
009D2769  C7 00 13 00 00 00               mov dword ptr [rax], 0x13
009D276F  E9 18 F4 FF FF                  jmp 0x1409d1b8c
009D2774  48 8B 07                        mov rax, qword ptr [rdi]
009D2777  48 2B 05 DA 1C 64 FF            sub rax, qword ptr [rip - 0x9be326]
009D277E  75 0B                           jne 0x1409d278b
009D2780  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
009D2784  48 2B 05 D5 1C 64 FF            sub rax, qword ptr [rip - 0x9be32b]
009D278B  33 FF                           xor edi, edi
009D278D  48 85 C0                        test rax, rax
009D2790  0F 85 21 F1 FF FF               jne 0x1409d18b7
009D2796  49 8B D3                        mov rdx, r11
009D2799  41 C7 00 12 20 00 00            mov dword ptr [r8], 0x2012
009D27A0  48 8D 4D A0                     lea rcx, [rbp - 0x60]
009D27A4  E8 B7 11 A9 FF                  call 0x140463960
009D27A9  8B D8                           mov ebx, eax
009D27AB  85 C0                           test eax, eax
009D27AD  0F 88 F3 F0 FF FF               js 0x1409d18a6
009D27B3  49 8B 85 00 01 00 00            mov rax, qword ptr [r13 + 0x100]
009D27BA  48 85 C0                        test rax, rax
009D27BD  0F 84 EE FE FF FF               je 0x1409d26b1
009D27C3  44 8D 47 0F                     lea r8d, [rdi + 0xf]
009D27C7  E9 B6 F6 FF FF                  jmp 0x1409d1e82
009D27CC  BB 30 02 00 C0                  mov ebx, 0xc0000230
009D27D1  E9 E1 F0 FF FF                  jmp 0x1409d18b7
009D27D6  41 3B C7                        cmp eax, r15d
009D27D9  0F 85 FB 01 00 00               jne 0x1409d29da
009D27DF  8B DF                           mov ebx, edi
009D27E1  E9 CA F8 FF FF                  jmp 0x1409d20b0
009D27E6  48 8B 0F                        mov rcx, qword ptr [rdi]
009D27E9  48 2B 0D 80 1C 64 FF            sub rcx, qword ptr [rip - 0x9be380]
009D27F0  75 0B                           jne 0x1409d27fd
009D27F2  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
009D27F6  48 2B 0D 7B 1C 64 FF            sub rcx, qword ptr [rip - 0x9be385]
009D27FD  48 85 C9                        test rcx, rcx
009D2800  0F 85 2E F0 FF FF               jne 0x1409d1834
009D2806  E9 18 F5 FF FF                  jmp 0x1409d1d23
009D280B  8B 45 84                        mov eax, dword ptr [rbp - 0x7c]
009D280E  E9 96 FE FF FF                  jmp 0x1409d26a9
009D2813  81 FB 23 00 00 C0               cmp ebx, 0xc0000023
009D2819  0F 84 3B FF FF FF               je 0x1409d275a
009D281F  41 3B DF                        cmp ebx, r15d
009D2822  0F 85 7E F0 FF FF               jne 0x1409d18a6
009D2828  4C 8B 4D 90                     mov r9, qword ptr [rbp - 0x70]
009D282C  48 8D 44 24 70                  lea rax, [rsp + 0x70]
009D2831  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
009D2836  41 B8 01 00 00 00               mov r8d, 1
009D283C  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
009D2841  49 8B CD                        mov rcx, r13
009D2844  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
009D2849  8B 85 00 01 00 00               mov eax, dword ptr [rbp + 0x100]
009D284F  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
009D2853  48 8D 44 24 74                  lea rax, [rsp + 0x74]
009D2858  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
009D285D  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009D2862  48 8D 05 4F ED 63 FF            lea rax, [rip - 0x9c12b1]
009D2869  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009D286E  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
009D2873  E8 08 F9 F0 FF                  call 0x1408e2180
009D2878  B9 00 00 00 80                  mov ecx, 0x80000000
009D287D  8B D8                           mov ebx, eax
009D287F  03 C1                           add eax, ecx
009D2881  85 C1                           test ecx, eax
009D2883  75 0C                           jne 0x1409d2891
009D2885  81 FB 23 00 00 C0               cmp ebx, 0xc0000023
009D288B  0F 85 15 F0 FF FF               jne 0x1409d18a6
009D2891  83 7C 24 74 13                  cmp dword ptr [rsp + 0x74], 0x13
009D2896  4C 8B 5C 24 68                  mov r11, qword ptr [rsp + 0x68]
009D289B  0F 84 C9 CC 15 00               je 0x140b2f56a
009D28A1  41 8B DF                        mov ebx, r15d
009D28A4  E9 02 F0 FF FF                  jmp 0x1409d18ab
009D28A9  3D 23 00 00 C0                  cmp eax, 0xc0000023
009D28AE  E9 BB F9 FF FF                  jmp 0x1409d226e
009D28B3  48 8B 07                        mov rax, qword ptr [rdi]
009D28B6  48 2B 05 AB EC 63 FF            sub rax, qword ptr [rip - 0x9c1355]
009D28BD  75 0B                           jne 0x1409d28ca
009D28BF  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
009D28C3  48 2B 05 A6 EC 63 FF            sub rax, qword ptr [rip - 0x9c135a]
009D28CA  33 FF                           xor edi, edi
009D28CC  48 85 C0                        test rax, rax
009D28CF  0F 85 E2 EF FF FF               jne 0x1409d18b7
009D28D5  4C 8B 45 90                     mov r8, qword ptr [rbp - 0x70]
009D28D9  48 8D 44 24 70                  lea rax, [rsp + 0x70]
009D28DE  44 89 54 24 38                  mov dword ptr [rsp + 0x38], r10d
009D28E3  44 8D 4F 25                     lea r9d, [rdi + 0x25]
009D28E7  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009D28EC  49 8B D3                        mov rdx, r11
009D28EF  48 8D 45 E0                     lea rax, [rbp - 0x20]
009D28F3  C7 44 24 70 4E 00 00 00         mov dword ptr [rsp + 0x70], 0x4e
009D28FB  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009D2900  49 8B CD                        mov rcx, r13
009D2903  48 8D 45 B4                     lea rax, [rbp - 0x4c]
009D2907  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009D290C  E8 5F AF F1 FF                  call 0x1408ed870
009D2911  8B D8                           mov ebx, eax
009D2913  85 C0                           test eax, eax
009D2915  0F 88 8B EF FF FF               js 0x1409d18a6
009D291B  48 8D 55 E0                     lea rdx, [rbp - 0x20]
009D291F  48 8D 0D CA B3 12 00            lea rcx, [rip + 0x12b3ca]
009D2926  E8 C5 F1 B2 FF                  call 0x140501af0
009D292B  85 C0                           test eax, eax
009D292D  0F 84 1F F6 FF FF               je 0x1409d1f52
009D2933  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
009D2937  C7 06 10 00 00 00               mov dword ptr [rsi], 0x10
009D293D  C7 00 0D 00 00 00               mov dword ptr [rax], 0xd
009D2943  8B 06                           mov eax, dword ptr [rsi]
009D2945  39 85 00 01 00 00               cmp dword ptr [rbp + 0x100], eax
009D294B  0F 82 E5 F2 FF FF               jb 0x1409d1c36
009D2951  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
009D2956  4C 8D 4D 30                     lea r9, [rbp + 0x30]
009D295A  4C 8D 45 E0                     lea r8, [rbp - 0x20]
009D295E  49 8B CD                        mov rcx, r13
009D2961  E8 4E A9 F2 FF                  call 0x1408fd2b4
009D2966  8B D8                           mov ebx, eax
009D2968  85 C0                           test eax, eax
009D296A  0F 88 36 EF FF FF               js 0x1409d18a6
009D2970  48 8D 55 30                     lea rdx, [rbp + 0x30]
009D2974  48 8D 4D A0                     lea rcx, [rbp - 0x60]
009D2978  E8 E3 0F A9 FF                  call 0x140463960
009D297D  8B D8                           mov ebx, eax
009D297F  85 C0                           test eax, eax
009D2981  0F 88 1F EF FF FF               js 0x1409d18a6
009D2987  49 8B D6                        mov rdx, r14
009D298A  48 8D 4D A0                     lea rcx, [rbp - 0x60]
009D298E  E8 5D F5 F1 FF                  call 0x1408f1ef0
009D2993  8B D8                           mov ebx, eax
009D2995  E9 0C EF FF FF                  jmp 0x1409d18a6
009D299A  BB 0D 00 00 C0                  mov ebx, 0xc000000d
009D299F  E9 07 EF FF FF                  jmp 0x1409d18ab
009D29A4  41 BC 08 00 00 00               mov r12d, 8
009D29AA  E9 CA F8 FF FF                  jmp 0x1409d2279
009D29AF  41 BC 10 00 00 00               mov r12d, 0x10
009D29B5  E9 BF F8 FF FF                  jmp 0x1409d2279
009D29BA  3D 23 00 00 C0                  cmp eax, 0xc0000023
009D29BF  0F 85 E1 EE FF FF               jne 0x1409d18a6
009D29C5  E9 4C F2 FF FF                  jmp 0x1409d1c16
009D29CA  3D 05 00 00 80                  cmp eax, 0x80000005
009D29CF  0F 84 61 F2 FF FF               je 0x1409d1c36
009D29D5  E9 E2 F4 FF FF                  jmp 0x1409d1ebc
009D29DA  3D 23 00 00 C0                  cmp eax, 0xc0000023
009D29DF  0F 85 C1 EE FF FF               jne 0x1409d18a6
009D29E5  E9 F5 FD FF FF                  jmp 0x1409d27df
009D29EA  83 7C 24 74 11                  cmp dword ptr [rsp + 0x74], 0x11
009D29EF  0F 85 C2 EE FF FF               jne 0x1409d18b7
009D29F5  83 7C 24 70 01                  cmp dword ptr [rsp + 0x70], 1
009D29FA  0F 85 B7 EE FF FF               jne 0x1409d18b7
009D2A00  80 7C 24 60 FF                  cmp byte ptr [rsp + 0x60], 0xff
009D2A05  E9 C1 FA FF FF                  jmp 0x1409d24cb
009D2A0A  81 FB 0E 00 00 C0               cmp ebx, 0xc000000e
009D2A10  0F 84 A1 EE FF FF               je 0x1409d18b7
009D2A16  81 FB C0 00 00 C0               cmp ebx, 0xc00000c0
009D2A1C  B8 01 00 00 C0                  mov eax, 0xc0000001
009D2A21  0F 45 D8                        cmovne ebx, eax
009D2A24  E9 8E EE FF FF                  jmp 0x1409d18b7
009D2A29  48 8B 8D 80 00 00 00            mov rcx, qword ptr [rbp + 0x80]
009D2A30  48 33 CC                        xor rcx, rsp
009D2A33  E8 08 9C CD FF                  call 0x1406ac640
009D2A38  48 8B 9C 24 E8 01 00 00         mov rbx, qword ptr [rsp + 0x1e8]
009D2A40  48 81 C4 90 01 00 00            add rsp, 0x190
009D2A47  41 5F                           pop r15
009D2A49  41 5E                           pop r14
009D2A4B  41 5D                           pop r13
009D2A4D  41 5C                           pop r12
009D2A4F  5F                              pop rdi
009D2A50  5E                              pop rsi
009D2A51  5D                              pop rbp
009D2A52  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall _CmGetDeviceMappedPropertyFromComposite(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, unsigned int a7, __int64 a8, unsigned int a9)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned int v_stack_m114;
    unsigned int v_stack_m118;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned int v_stack_m140;
    unsigned int v_stack_m144;
    unsigned int v_stack_m148;
    unsigned int v_stack_m14C;
    unsigned int v_stack_m150;
    unsigned int v_stack_m154;
    unsigned int v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int8 v_stack_m168;
    unsigned int v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned int v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned int v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p38;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (400);
    result = (*(unsigned __int64 *)(v_rip + 4427926)) ^ (v_rsp);
    v_stack_m48 = result;
    a1 = 0;
    v_stack_m138 = a3;
    v_stack_m160 = a2;
    v_stack_m130 = a5;
    v_stack_m144 = 0;
    v_stack_m158 = 0;
    v_stack_m150 = 0;
    v_stack_m14C = 0;
    v_stack_m148 = 0;
    v_stack_m118 = 0;
    v_stack_m110 = 0;
    v_stack_m154 = 0;
    v_stack_m114 = 0;
    v_stack_m168 = 0;
    v_stack_m128 = v_xmm0;
    v_stack_m108 = v_xmm1;
    v_stack_mF8 = v_xmm0;
    if ((unsigned __int16)((unsigned int)(a9)) != 0) goto loc_009D1BBC;
    *(unsigned int *)(a5) = 0;
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a9)))) & (0xFFFF0000ULL));
    *(unsigned int *)(a8) = 0;
    v_stack_m140 = (unsigned int)(v_r12);
    if (a6 == 0) goto loc_009D18BF;
    result = (unsigned int)(-((unsigned int)((unsigned int)((unsigned int)(a7)))));
    v_r14 = (a6) & (0);
loc_009D1759:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) < 2) goto loc_009D27CC;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == 10) goto loc_009D1AC0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == 256) goto loc_009D18CC;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == 2) goto loc_009D1D03;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == 3) goto loc_009D250F;
loc_009D1791:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == 12) goto loc_009D27E6;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == 4) goto loc_009D198E;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == 5) goto loc_009D1C40;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == 6) goto loc_009D1F5A;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == ((unsigned int)(4 + 3))) goto loc_009D2534;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == 11) goto loc_009D263E;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == 8) goto loc_009D1BD1;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == 9) goto loc_009D2224;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == 10) goto loc_009D255D;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == 2) goto loc_009D1DDF;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == 5) goto loc_009D1C60;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == 6) goto loc_009D1F7A;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == 15) goto loc_009D22E3;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == 16) goto loc_009D2407;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == 4) goto loc_009D1BC6;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == 14) goto loc_009D1E2F;
loc_009D182C:
loc_009D1834:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == 20) goto loc_009D2774;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == 21) goto loc_009D25B9;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == 26) goto loc_009D20B9;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == 22) goto loc_009D1B97;
loc_009D1858:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) != 23) goto loc_009D26DC;
    result = (*(unsigned __int64 *)(a4)) - (*(unsigned __int64 *)(v_rip - 10213307));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(a4 + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 10213312));
    }
    if (result != 0) goto loc_009D18B7;
loc_009D187D:
    v_stack_m190 = a8;
    v_stack_m198 = (unsigned int)((unsigned int)(a7));
    v_stack_m1A0 = v_r14;
    v_stack_m1A8 = a5;
    result = _CmGetDeviceCompoundFilters(0, a2, v_stack_m138, a4);
loc_009D18A4:
    v_rdi = 0;
loc_009D18A6:
loc_009D18AB:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 0xC000000EULL) goto loc_009D21DF;
loc_009D18B7:
    goto loc_009D2A29;
loc_009D18BF:
    v_stack_p38 = 0;
    goto loc_009D1759;
loc_009D18CC:
    a1 = (*(unsigned __int64 *)(v_rdi)) - (*(unsigned __int64 *)(v_rip - 10224710));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int64 *)(v_rdi + 8);
        a1 = (a1) - (*(unsigned __int64 *)(v_rip - 10224715));
    }
    if (a1 != 0) goto loc_009D1834;
    v_rdi = 0;
    if (v_stack_m160 == 0) goto loc_009D299A;
loc_009D1903:
    if ((*(unsigned __int16 *)(v_stack_m160)) == 0) goto loc_009D1912;
    result = (v_stack_m160) + (2);
    a4 = (200) - (1);
    if (condition_is_not_equal) goto loc_009D1903;
loc_009D1912:
    result = -(a4);
    v_r10 = (200) - (a4);
    a1 = (unsigned int)(~(a1));
    v_rbx = (unsigned int)(((unsigned int)(0xC000000DULL)) & ((unsigned int)(a1)));
    result = -(a4);
    result = (result) & (v_r10);
    if (a4 == 0) goto loc_009D18AB;
    *(unsigned int *)(a8) = (unsigned int)(result * 2 + 2);
    *(unsigned int *)(v_stack_m138) = 18;
    if (0 < ((unsigned int)((unsigned int)(*(unsigned int *)(a8))))) goto loc_009D1C36;
    v_stack_m1A0 = 0x900ULL;
    a4 = 0;
    v_stack_m1A8 = 0;
    result = RtlStringCbCopyExW(v_r14, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a8)))), v_stack_m160, a4);
    if (!sign_flag) goto loc_009D18AB;
    *(unsigned int *)(a8) = 0;
    *(unsigned int *)(v_stack_m130) = 0;
    goto loc_009D18AB;
loc_009D198E:
    result = (*(unsigned __int64 *)(v_rdi)) - (*(unsigned __int64 *)(v_rip - 10213704));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(v_rdi + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 10213709));
    }
    a1 = 0;
    if (result == 0) goto loc_009D2279;
loc_009D19B0:
    result = (*(unsigned __int64 *)(v_rdi)) - (*(unsigned __int64 *)(v_rip - 10213570));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(v_rdi + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 10213575));
    }
    if (result != 0) goto loc_009D18B7;
    v_stack_m178 = (unsigned int)((unsigned int)(v_stack_m140));
    v_stack_m180 = v_stack_m158;
    v_stack_m188 = 16;
    v_stack_m190 = v_stack_m108;
    v_stack_m198 = v_stack_m154;
    *(unsigned int *)(v_stack_m160) = 17;
    v_stack_m1A0 = v_rip - 10224798;
    v_stack_m1A8 = 0;
    *(unsigned int *)(a8) = 1;
    result = PnpGetObjectProperty(0, v_stack_m160, 1, a4);
    if (sign_flag) goto loc_009D18A4;
    v_stack_m178 = (unsigned int)((unsigned int)(v_stack_m140));
    v_stack_m180 = v_stack_m158;
    v_stack_m188 = 16;
    v_stack_m190 = v_stack_mF8;
    v_rdi = 0;
    a4 = 0;
    v_stack_m198 = v_stack_m154;
    v_stack_m1A0 = v_rip - 10213732;
    v_stack_m1A8 = 0;
    result = PnpGetObjectProperty(0, v_rip + 1237702, v_rdi + 1, a4);
    if (sign_flag) goto loc_009D18A6;
    if (a7 < ((unsigned int)((unsigned int)(*(unsigned int *)(a8))))) goto loc_009D1C36;
    result = memcmp(v_stack_mF8, v_stack_m108, v_rdi + 16, a4);
    result = (unsigned int)(-(result));
    a1 = (unsigned __int8)(-(v_stack_mF8));
    a1 = (unsigned __int8)((a1) - 1);
loc_009D1AB8:
    *(unsigned __int8 *)(v_r14) = (unsigned __int8)(a1);
    goto loc_009D18B7;
loc_009D1AC0:
    result = (*(unsigned __int64 *)(v_rdi)) - (*(unsigned __int64 *)(v_rip - 10213962));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(v_rdi + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 10213967));
    }
    if (result != 0) goto loc_009D255D;
    v_stack_m178 = (unsigned int)((unsigned int)(v_stack_m140));
    v_stack_m180 = v_stack_m158;
    v_rdi = 0;
    v_stack_m188 = (unsigned int)(v_stack_m108);
    v_stack_m190 = v_r14;
    v_stack_m198 = v_rdi + 16;
    v_stack_m1A0 = v_rip - 10213988;
    v_stack_m1A8 = 0;
    result = PnpGetObjectProperty(a1, v_stack_m160, v_rdi + 1, a4);
    if ((unsigned int)(result) == 0) goto loc_009D1B8C;
    if (((unsigned int)(result)) == 0xC0000023ULL) goto loc_009D1B8C;
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0xC0000225ULL)))) goto loc_009D18A6;
    v_stack_m178 = (unsigned int)((unsigned int)(v_stack_m140));
    v_stack_m180 = v_stack_m158;
    v_stack_m188 = (unsigned int)((unsigned int)(a7));
    v_stack_m190 = v_r14;
    v_stack_m198 = v_stack_m130;
    v_stack_m1A0 = v_rip - 10213963;
    v_stack_m1A8 = 0;
    result = PnpGetObjectProperty(a1, v_stack_m160, v_rdi + 1, v_stack_m138);
    if ((unsigned int)(result) != 0) goto loc_009D21C6;
loc_009D1B8C:
    *(unsigned int *)(a8) = (unsigned int)((unsigned int)(v_stack_m158));
    goto loc_009D18A6;
loc_009D1B97:
    a1 = (*(unsigned __int64 *)(v_rdi)) - (*(unsigned __int64 *)(v_rip - 10214105));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int64 *)(v_rdi + 8);
        a1 = (a1) - (*(unsigned __int64 *)(v_rip - 10214110));
    }
    if (a1 == 0) goto loc_009D187D;
    goto loc_009D1858;
loc_009D1BBC:
    goto loc_009D18B7;
loc_009D1BC6:
    a1 = 0;
    goto loc_009D19B0;
loc_009D1BD1:
    result = (*(unsigned __int64 *)(v_rdi)) - (*(unsigned __int64 *)(v_rip - 10213947));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(v_rdi + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 10213952));
    }
    if (result != 0) goto loc_009D1EC9;
    a2 = (unsigned int)((v_stack_m160) >> (1));
    v_stack_m150 = (unsigned int)(a2);
    result = CmGetDeviceParent(0, v_stack_m160, v_r14, v_stack_m150);
    v_rdi = 0;
    if ((unsigned int)(result) != 0) goto loc_009D29BA;
loc_009D1C16:
    result = (unsigned int)(((unsigned int)(v_stack_m150)) + ((unsigned int)((unsigned int)(v_stack_m150))));
    *(unsigned int *)(a8) = (unsigned int)(result);
    *(unsigned int *)(v_stack_m130) = 18;
loc_009D1C28:
    if (a7 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a8))))) goto loc_009D18A6;
loc_009D1C36:
    goto loc_009D18B7;
loc_009D1C40:
    result = (*(unsigned __int64 *)(v_rdi)) - (*(unsigned __int64 *)(v_rip - 10213962));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(v_rdi + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 10213967));
    }
    if (result == 0) goto loc_009D29A4;
loc_009D1C60:
    result = (*(unsigned __int64 *)(v_rdi)) - (*(unsigned __int64 *)(v_rip - 10214066));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(v_rdi + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 10214071));
    }
    v_rdi = 0;
    if (result != 0) goto loc_009D18B7;
    *(unsigned int *)(a8) = 1;
    *(unsigned int *)(v_r14) = 17;
    if (((unsigned int)(v_stack_m160)) < (*(unsigned int *)(a8))) goto loc_009D1C36;
    result = RtlInitUnicodeStringEx(v_stack_m128, v_stack_m160, v_r14, v_stack_m150);
    if (sign_flag) goto loc_009D18A6;
    *(unsigned __int8 *)(v_r14) = 0;
    if (*(unsigned __int64 *)(a1 + 264) == 0) goto loc_009D26B1;
    v_stack_m1A0 = 0;
    v_stack_m1A8 = v_stack_m144;
    result = guard_dispatch_icall(0, v_stack_m128, v_stack_m14C, v_stack_m148);
    if (((unsigned int)(result)) == 0x80000005ULL) goto loc_009D1C36;
    if (((unsigned int)(result)) == 0xC000000EULL) goto loc_009D21BF;
    if (sign_flag) goto loc_009D18B7;
    goto loc_009D20B0;
loc_009D1D03:
    result = (*(unsigned __int64 *)(v_rdi)) - (*(unsigned __int64 *)(v_rip - 10213965));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(v_rdi + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 10213970));
    }
    if (result != 0) goto loc_009D1DE3;
loc_009D1D23:
    v_stack_m1A0 = v_stack_m144;
    v_stack_m1A8 = v_stack_m148;
    result = CmGetDeviceStatus(0, v_stack_m160, v_stack_m138, v_stack_m14C);
    if (sign_flag) goto loc_009D18A4;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 16)))) != 2) goto loc_009D24D6;
    result = (*(unsigned __int64 *)(v_rdi)) - (*(unsigned __int64 *)(v_rip - 10214068));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(v_rdi + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 10214073));
    }
    if (result != 0) goto loc_009D24D6;
loc_009D1D8A:
loc_009D1D90:
    *(unsigned int *)(a8) = 4;
    *(unsigned int *)(v_stack_m130) = 7;
    if (a7 < ((unsigned int)((unsigned int)(*(unsigned int *)(a8))))) goto loc_009D1C36;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 16)))) != 2) goto loc_009D2677;
    result = (*(unsigned __int64 *)(v_rdi)) - (*(unsigned __int64 *)(v_rip - 10214145));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(v_rdi + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 10214150));
    }
    if (result != 0) goto loc_009D280B;
    *(unsigned int *)(v_r14) = (unsigned int)((unsigned int)(v_stack_m14C));
    goto loc_009D18B7;
loc_009D1DDF:
loc_009D1DE3:
    result = (*(unsigned __int64 *)(v_rdi)) - (*(unsigned __int64 *)(v_rip - 10214357));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(v_rdi + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 10214362));
    }
    if (result != 0) goto loc_009D28B3;
    *(unsigned int *)(a8) = 1;
    *(unsigned int *)((unsigned int)(*(unsigned int *)(v_rdi + 16))) = 17;
    if (((unsigned int)((unsigned int)(0x400ULL))) < (*(unsigned int *)(a8))) goto loc_009D1C36;
    result = CmIsDeviceSafeRemovalRequired(0, v_stack_m160, v_stack_m138, v_stack_m138);
    result = (unsigned __int8)(-(result));
    goto loc_009D1AB8;
loc_009D1E2F:
    result = (*(unsigned __int64 *)(v_rdi)) - (*(unsigned __int64 *)(v_rip - 10214481));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(v_rdi + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 10214486));
    }
    v_rdi = 0;
    if (result != 0) goto loc_009D18B7;
    *(unsigned int *)(v_stack_m138) = 0x2012ULL;
    result = RtlInitUnicodeStringEx(v_stack_m128, v_stack_m160, v_stack_m138, v_stack_m138);
    if (sign_flag) goto loc_009D18A6;
    if (*(unsigned __int64 *)(a1 + 256) == 0) goto loc_009D26B1;
loc_009D1E82:
    v_stack_m198 = 0;
    v_stack_m1A0 = a8;
    v_stack_m1A8 = (unsigned int)((unsigned int)(a7));
    result = guard_dispatch_icall(0, v_stack_m128, v_rdi + 14, v_r14);
    if (((unsigned int)(result)) == 0x80000005ULL) goto loc_009D1C36;
    if (((unsigned int)(result)) == 0xC0000034ULL) goto loc_009D1F52;
loc_009D1EBC:
    if (sign_flag) goto loc_009D18A6;
    goto loc_009D18B7;
loc_009D1EC9:
    result = (*(unsigned __int64 *)(v_rdi)) - (*(unsigned __int64 *)(v_rip - 10214659));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(v_rdi + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 10214664));
    }
    v_rdi = 0;
    if (result != 0) goto loc_009D18B7;
    *(unsigned int *)(v_rdi + 14) = (unsigned int)(v_r14);
    *(unsigned int *)(a8) = (unsigned int)((unsigned int)(v_stack_m140));
    result = RtlInitUnicodeStringEx(v_stack_m128, v_stack_m160, v_rdi + 14, v_r14);
    if (sign_flag) goto loc_009D18A6;
    if (*(unsigned __int64 *)(a1 + 256) == 0) goto loc_009D26B1;
    v_stack_m198 = 0;
    v_stack_m1A0 = a7;
    v_stack_m1A8 = (unsigned int)((unsigned int)(a7));
    result = guard_dispatch_icall(0, v_stack_m128, v_rdi + 13, v_r14);
    if (((unsigned int)(result)) != 0xC0000034ULL) goto loc_009D29CA;
loc_009D1F52:
    goto loc_009D18B7;
loc_009D1F5A:
    result = (*(unsigned __int64 *)(v_rdi)) - (*(unsigned __int64 *)(v_rip - 10214636));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(v_rdi + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 10214641));
    }
    if (result == 0) goto loc_009D29AF;
loc_009D1F7A:
    result = (*(unsigned __int64 *)(v_rdi)) - (*(unsigned __int64 *)(v_rip - 10214692));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(v_rdi + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 10214697));
    }
    v_rdi = 0;
    if (result != 0) goto loc_009D18B7;
    *(unsigned int *)(v_rdi + 13) = 17;
    *(unsigned int *)(a8) = 1;
    if (((unsigned int)(v_stack_m128)) < 1) goto loc_009D1C36;
    result = RtlInitUnicodeStringEx(v_stack_m128, v_stack_m160, v_rdi + 13, v_r14);
    if (sign_flag) goto loc_009D18A6;
    *(unsigned __int8 *)(v_r14) = 0;
    if (*(unsigned __int64 *)(a1 + 264) == 0) goto loc_009D26B1;
    v_stack_m1A0 = 0;
    v_stack_m1A8 = v_stack_m144;
    result = guard_dispatch_icall(0, v_stack_m128, v_stack_m14C, v_stack_m148);
    if (((unsigned int)(result)) == 0x80000005ULL) goto loc_009D1C36;
    if (((unsigned int)(result)) == 0xC000000EULL) goto loc_009D21BF;
    if (sign_flag) goto loc_009D18B7;
    if (condition_is_below) goto loc_009D20B0;
    if (condition_is_below) goto loc_009D26BB;
loc_009D2035:
    if ((((unsigned __int8)((unsigned int)(v_stack_m14C))) & (8)) != 0) goto loc_009D18B7;
    v_stack_m178 = (unsigned int)((unsigned int)(v_stack_m140));
    v_rdi = 0;
    v_stack_m180 = v_stack_m158;
    v_stack_m188 = (unsigned int)((unsigned int)(v_stack_m140));
    v_stack_m190 = v_stack_m118;
    v_stack_m198 = v_stack_m154;
    v_stack_m1A0 = v_rip - 10214824;
    v_stack_m1A8 = 0;
    result = PnpGetObjectProperty(0, v_stack_m160, v_rdi + 1, v_stack_m138);
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC0000225ULL)))) goto loc_009D21BF;
    if (sign_flag) goto loc_009D18A6;
loc_009D20AA:
    if (((v_stack_m118) & ((unsigned __int8)(v_rdi + 64))) == 0) goto loc_009D18B7;
loc_009D20B0:
    *(unsigned __int8 *)(v_r14) = 255;
    goto loc_009D18B7;
loc_009D20B9:
    result = (*(unsigned __int64 *)(v_rdi)) - (*(unsigned __int64 *)(v_rip - 10215059));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(v_rdi + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 10215064));
    }
    v_rdi = 0;
    if (result != 0) goto loc_009D18B7;
    *(unsigned int *)(v_rdi + 1) = 17;
    *(unsigned int *)(a8) = 1;
    if (((unsigned int)(v_stack_m160)) < 1) goto loc_009D1C36;
    v_stack_m178 = (unsigned int)(v_rdi + 64);
    v_stack_m180 = v_stack_m158;
    v_stack_m188 = 1;
    v_stack_m190 = v_stack_m168;
    *(unsigned __int8 *)(v_r14) = 0;
    v_stack_m198 = v_stack_m154;
    v_stack_m1A0 = v_rip - 10215072;
    v_stack_m1A8 = 0;
    result = PnpGetObjectProperty(0, v_stack_m160, v_rdi + 1, v_stack_m138);
    if (!sign_flag) goto loc_009D2611;
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0xC0000225ULL)))) goto loc_009D2667;
loc_009D2152:
    v_stack_m178 = (unsigned int)(v_rdi + 64);
    v_stack_m180 = v_stack_m158;
    v_stack_m188 = 1;
    v_stack_m190 = v_stack_m168;
    v_stack_m198 = v_stack_m154;
    v_stack_m1A0 = v_rip - 10215150;
    v_stack_m1A8 = 0;
    result = PnpGetObjectProperty(0, v_stack_m160, 1, v_stack_m138);
    if (!sign_flag) goto loc_009D29EA;
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC0000225ULL)))) goto loc_009D21BF;
    if (((unsigned int)(result)) != 0xC0000023ULL) goto loc_009D18A6;
loc_009D21BF:
    goto loc_009D18B7;
loc_009D21C6:
    if (((unsigned int)(result)) == 0xC0000023ULL) goto loc_009D1B8C;
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0xC0000225ULL)))) goto loc_009D18A6;
    goto loc_009D18B7;
loc_009D21DF:
    v_stack_m190 = 0;
    v_stack_m198 = v_stack_m110;
    a4 = 0;
    v_stack_m1A0 = 0;
    v_stack_m1A8 = 1;
    result = _CmOpenDeviceRegKey(0, v_stack_m160, a4 + 16, a4);
    if ((unsigned int)(result) != 0) goto loc_009D2A0A;
    result = ZwClose(v_stack_m110, v_stack_m160, a4 + 16, a4);
    goto loc_009D1F52;
loc_009D2224:
    result = (*(unsigned __int64 *)(v_rdi)) - (*(unsigned __int64 *)(v_rip - 10215398));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(v_rdi + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 10215403));
    }
    v_rdi = 0;
    if (result != 0) goto loc_009D18B7;
    a2 = (unsigned int)((v_stack_m160) >> (1));
    v_stack_m150 = (unsigned int)(a2);
    result = CmGetDeviceChildren(0, v_stack_m160, v_r14, v_stack_m150);
    if (((unsigned int)(result)) == 0xC0000023ULL) goto loc_009D25A2;
loc_009D226E:
    if ((unsigned int)(result) != 0) goto loc_009D18A6;
    goto loc_009D25A2;
loc_009D2279:
    a2 = (unsigned int)((v_stack_m160) >> (1));
    v_stack_m1A0 = v_stack_m150;
    v_stack_m1A8 = (unsigned int)(a2);
    result = CmGetDeviceRelationsList(0, v_stack_m160, (unsigned int)((unsigned int)(v_rdi + 64)), v_r14);
    if (((unsigned int)(result)) == 0xC0000034ULL) goto loc_009D1F52;
    v_rdi = 0;
    if ((unsigned int)(result) == 0) goto loc_009D22B8;
    if (((unsigned int)(result)) != 0xC0000023ULL) goto loc_009D18A6;
loc_009D22B8:
    *(unsigned int *)(v_stack_m130) = 0x2012ULL;
    if ((unsigned int)((unsigned int)((unsigned int)(result))) == 0) goto loc_009D2631;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 0xC0000023ULL) goto loc_009D18A6;
loc_009D22DA:
    result = (unsigned int)(((unsigned int)(v_stack_m150)) + ((unsigned int)((unsigned int)(v_stack_m150))));
    *(unsigned int *)(a8) = (unsigned int)(result);
    goto loc_009D18B7;
loc_009D22E3:
    result = (*(unsigned __int64 *)(v_rdi)) - (*(unsigned __int64 *)(v_rip - 10215421));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(v_rdi + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 10215426));
    }
    v_rdi = 0;
    if (result != 0) goto loc_009D18B7;
    *(unsigned int *)((unsigned int)((unsigned int)(v_rdi + 64))) = 17;
    *(unsigned int *)(a8) = 1;
    if (((unsigned int)(v_stack_m160)) < 1) goto loc_009D1C36;
    result = RtlInitUnicodeStringEx(v_stack_m128, v_stack_m160, (unsigned int)((unsigned int)(v_rdi + 64)), v_r14);
    if (sign_flag) goto loc_009D18A6;
    *(unsigned __int8 *)(v_r14) = 0;
    if (*(unsigned __int64 *)(a1 + 264) == 0) goto loc_009D26B1;
    v_stack_m1A0 = 0;
    v_stack_m1A8 = v_stack_m144;
    result = guard_dispatch_icall(0, v_stack_m128, v_stack_m14C, v_stack_m148);
    if (((unsigned int)(result)) == 0x80000005ULL) goto loc_009D1C36;
    if (((unsigned int)(result)) == 0xC000000EULL) goto loc_009D21BF;
    if (sign_flag) goto loc_009D18B7;
    if (((v_stack_m14C) & (0x2000000ULL)) != 0) goto loc_009D18B7;
    a4 = 0;
    v_stack_m178 = (unsigned int)((unsigned int)(v_stack_m140));
    v_stack_m180 = v_stack_m158;
    v_rdi = 0;
    v_stack_m188 = 1;
    v_stack_m190 = v_stack_m168;
    v_stack_m198 = v_stack_m154;
    v_stack_m1A0 = v_rip - 10215605;
    v_stack_m1A8 = 0;
    result = PnpGetObjectProperty(0, v_stack_m160, v_rdi + 1, a4);
    if (sign_flag) goto loc_009D27D6;
    if (v_stack_m154 != 17) goto loc_009D20B0;
    goto loc_009D20AA;
loc_009D2407:
    result = (*(unsigned __int64 *)(v_rdi)) - (*(unsigned __int64 *)(v_rip - 10215689));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(v_rdi + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 10215694));
    }
    v_rdi = 0;
    if (result != 0) goto loc_009D18B7;
    *(unsigned int *)(v_rdi + 1) = 17;
    *(unsigned int *)(a8) = 1;
    if (((unsigned int)(v_stack_m160)) < 1) goto loc_009D1C36;
    result = RtlInitUnicodeStringEx(v_stack_m128, v_stack_m160, v_rdi + 1, a4);
    if (sign_flag) goto loc_009D18A6;
    *(unsigned __int8 *)(v_r14) = 0;
    if (*(unsigned __int64 *)(a1 + 264) == 0) goto loc_009D26B1;
    v_stack_m1A0 = 0;
    v_stack_m1A8 = v_stack_m144;
    result = guard_dispatch_icall(0, v_stack_m128, v_stack_m14C, v_stack_m148);
    if (((unsigned int)(result)) == 0xC000000EULL) goto loc_009D21BF;
    if (((unsigned int)(result)) == 0x80000005ULL) goto loc_009D1C36;
    if (sign_flag) goto loc_009D18B7;
    if (((v_stack_m14C) & (256)) != 0) goto loc_009D20B0;
    if (((v_stack_m14C) & ((unsigned int)((unsigned int)(0x400ULL)))) == 0) goto loc_009D18B7;
loc_009D24CB:
    if (v_stack_m148 != 14) goto loc_009D18B7;
    goto loc_009D20B0;
loc_009D24D6:
    if (((unsigned int)(v_stack_m14C)) != 3) goto loc_009D24FC;
    result = (*(unsigned __int64 *)(v_rdi)) - (*(unsigned __int64 *)(v_rip - 10184078));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(v_rdi + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 10184083));
    }
    if (result == 0) goto loc_009D1D8A;
loc_009D24FC:
    if ((((unsigned int)((unsigned int)(0x400ULL))) & (0)) == 0) goto loc_009D1F52;
    goto loc_009D1D90;
loc_009D250F:
    a1 = (*(unsigned __int64 *)(v_rdi)) - (*(unsigned __int64 *)(v_rip - 10184129));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int64 *)(v_rdi + 8);
        a1 = (a1) - (*(unsigned __int64 *)(v_rip - 10184134));
    }
    if (a1 != 0) goto loc_009D1791;
    goto loc_009D1D23;
loc_009D2534:
    a1 = (*(unsigned __int64 *)(v_rdi)) - (*(unsigned __int64 *)(v_rip - 10215942));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int64 *)(v_rdi + 8);
        a1 = (a1) - (*(unsigned __int64 *)(v_rip - 10215947));
    }
    if (a1 != 0) goto loc_009D182C;
    goto loc_009D2279;
loc_009D255D:
    result = (*(unsigned __int64 *)(v_rdi)) - (*(unsigned __int64 *)(v_rip - 10215863));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(v_rdi + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 10215868));
    }
    v_rdi = 0;
    if (result != 0) goto loc_009D18B7;
    a2 = (unsigned int)(((unsigned int)(0x400ULL)) >> (1));
    v_stack_m150 = (unsigned int)(a2);
    result = CmGetDeviceSiblings(a1, v_stack_m160, v_r14, v_stack_m150);
    if ((unsigned int)(result) != 0) goto loc_009D28A9;
loc_009D25A2:
    result = (unsigned int)(((unsigned int)(v_stack_m150)) + ((unsigned int)((unsigned int)(v_stack_m150))));
    *(unsigned int *)(a8) = (unsigned int)(result);
    *(unsigned int *)(v_stack_m130) = 0x2012ULL;
    goto loc_009D1C28;
loc_009D25B9:
    result = (*(unsigned __int64 *)(v_rdi)) - (*(unsigned __int64 *)(v_rip - 10216027));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(v_rdi + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 10216032));
    }
    v_rdi = 0;
    if (result != 0) goto loc_009D18B7;
    *(unsigned int *)(v_r14) = 0x2012ULL;
    result = RtlInitUnicodeStringEx(v_stack_m128, v_stack_m160, v_r14, v_stack_m150);
    if (sign_flag) goto loc_009D18A6;
    if (*(unsigned __int64 *)(a1 + 256) == 0) goto loc_009D26B1;
    goto loc_009D1E82;
loc_009D2611:
    if (v_stack_m154 != 17) goto loc_009D2152;
    if (v_stack_m158 != 1) goto loc_009D2152;
    goto loc_009D24CB;
loc_009D2631:
    result = PnpMultiSzGetLen(v_r14, v_stack_m160, v_rdi + 16, v_stack_m150);
    goto loc_009D22DA;
loc_009D263E:
    a1 = (*(unsigned __int64 *)(v_rdi)) - (*(unsigned __int64 *)(v_rip - 10215944));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int64 *)(v_rdi + 8);
        a1 = (a1) - (*(unsigned __int64 *)(v_rip - 10215949));
    }
    if (a1 != 0) goto loc_009D182C;
    goto loc_009D2279;
loc_009D2667:
    if (((unsigned int)(result)) != 0xC0000023ULL) goto loc_009D18A6;
    goto loc_009D2152;
loc_009D2677:
    if (((unsigned int)(result)) != 3) goto loc_009D280B;
    result = (*(unsigned __int64 *)(v_rdi)) - (*(unsigned __int64 *)(v_rip - 10184498));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(v_rdi + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 10184503));
    }
    if (result != 0) goto loc_009D280B;
    a1 = (unsigned int)((a1) & ((unsigned int)(v_stack_m160)));
    a1 = (unsigned int)(-(a1));
    result = (unsigned int)((result) & (v_stack_m148));
loc_009D26A9:
    *(unsigned int *)(v_r14) = (unsigned int)(result);
    goto loc_009D18B7;
loc_009D26B1:
    goto loc_009D18B7;
loc_009D26BB:
    if (((unsigned int)((unsigned int)(v_stack_m148))) > 29) goto loc_009D20B0;
    if (((unsigned int)((unsigned int)(v_stack_m148))) < 29) goto loc_009D2035;
    goto loc_009D20B0;
loc_009D26DC:
    if (((unsigned int)(result)) != 102) goto loc_009D18B7;
    result = (*(unsigned __int64 *)(v_rdi)) - (*(unsigned __int64 *)(v_rip - 10228343));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(v_rdi + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 10228348));
    }
    v_rdi = 0;
    if (result != 0) goto loc_009D18B7;
    v_stack_m178 = (unsigned int)(a1 + 64);
    v_stack_m180 = v_stack_m158;
    v_stack_m188 = (unsigned int)((unsigned int)(v_stack_m148));
    v_stack_m190 = v_r14;
    v_stack_m198 = v_stack_m154;
    v_stack_m1A0 = v_rip - 10227730;
    v_stack_m1A8 = 0;
    result = PnpGetObjectProperty(a1, v_stack_m160, v_rdi + 1, v_stack_m150);
    result = (unsigned int)((result) + ((unsigned int)((unsigned int)(0x80000000ULL))));
    if ((((unsigned int)((unsigned int)(0x80000000ULL))) & ((unsigned int)(result))) == 0) goto loc_009D2813;
loc_009D275A:
    if (v_stack_m154 != 19) goto loc_009D2828;
    *(unsigned int *)(v_stack_m130) = 19;
    goto loc_009D1B8C;
loc_009D2774:
    result = (*(unsigned __int64 *)(v_rdi)) - (*(unsigned __int64 *)(v_rip - 10216230));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(v_rdi + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 10216235));
    }
    v_rdi = 0;
    if (result != 0) goto loc_009D18B7;
    *(unsigned int *)(v_rdi + 1) = 0x2012ULL;
    result = RtlInitUnicodeStringEx(v_stack_m128, v_stack_m160, v_rdi + 1, v_stack_m150);
    if (sign_flag) goto loc_009D18A6;
    if (*(unsigned __int64 *)(a1 + 256) == 0) goto loc_009D26B1;
    goto loc_009D1E82;
loc_009D27CC:
    goto loc_009D18B7;
loc_009D27D6:
    if (((unsigned int)(*(unsigned __int64 *)(a1 + 256))) != ((unsigned int)((unsigned int)(0xC0000225ULL)))) goto loc_009D29DA;
loc_009D27DF:
    goto loc_009D20B0;
loc_009D27E6:
    a1 = (*(unsigned __int64 *)(v_rdi)) - (*(unsigned __int64 *)(v_rip - 10216320));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int64 *)(v_rdi + 8);
        a1 = (a1) - (*(unsigned __int64 *)(v_rip - 10216325));
    }
    if (a1 != 0) goto loc_009D1834;
    goto loc_009D1D23;
loc_009D280B:
    goto loc_009D26A9;
loc_009D2813:
    if (0 == 0xC0000023ULL) goto loc_009D275A;
    if (0 != ((unsigned int)((unsigned int)(0xC0000225ULL)))) goto loc_009D18A6;
loc_009D2828:
    v_stack_m178 = (unsigned int)(a1 + 64);
    v_stack_m180 = v_stack_m158;
    v_stack_m188 = (unsigned int)((unsigned int)(a7));
    v_stack_m190 = v_r14;
    v_stack_m198 = v_stack_m154;
    v_stack_m1A0 = v_rip - 10228401;
    v_stack_m1A8 = 0;
    result = PnpGetObjectProperty(a1, v_stack_m160, 1, v_stack_m138);
    result = (unsigned int)((result) + ((unsigned int)((unsigned int)(0x80000000ULL))));
    if ((((unsigned int)((unsigned int)(0x80000000ULL))) & ((unsigned int)(result))) != 0) goto loc_009D2891;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 0xC0000023ULL) goto loc_009D18A6;
loc_009D2891:
    goto loc_009D18AB;
loc_009D28A9:
    goto loc_009D226E;
loc_009D28B3:
    result = (*(unsigned __int64 *)(v_rdi)) - (*(unsigned __int64 *)(v_rip - 10228565));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(v_rdi + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 10228570));
    }
    v_rdi = 0;
    if (result != 0) goto loc_009D18B7;
    v_stack_m190 = (unsigned int)(v_r10);
    v_stack_m198 = v_stack_m158;
    v_stack_m158 = 78;
    v_stack_m1A0 = v_stack_mE8;
    v_stack_m1A8 = v_stack_m114;
    result = CmGetDeviceRegProp(a1, v_stack_m160, v_stack_m138, v_rdi + 37);
    if (sign_flag) goto loc_009D18A6;
    result = wcscmp(v_rip + 1225674, v_stack_mE8, v_stack_m138, v_rdi + 37);
    if ((unsigned int)(result) == 0) goto loc_009D1F52;
    *(unsigned int *)(a8) = 16;
    *(unsigned int *)(v_stack_m130) = 13;
    if (a7 < ((unsigned int)((unsigned int)(*(unsigned int *)(a8))))) goto loc_009D1C36;
    result = _CmGetDeviceContainerIdFromBase(a1, v_stack_m160, v_stack_mE8, v_stack_m98);
    if (sign_flag) goto loc_009D18A6;
    result = RtlInitUnicodeStringEx(v_stack_m128, v_stack_m98, v_stack_mE8, v_stack_m98);
    if (sign_flag) goto loc_009D18A6;
    result = RtlGUIDFromString(v_stack_m128, v_r14, v_stack_mE8, v_stack_m98);
    goto loc_009D18A6;
loc_009D299A:
    goto loc_009D18AB;
loc_009D29A4:
    goto loc_009D2279;
loc_009D29AF:
    goto loc_009D2279;
loc_009D29BA:
    if (((unsigned int)(result)) != 0xC0000023ULL) goto loc_009D18A6;
    goto loc_009D1C16;
loc_009D29CA:
    if (((unsigned int)(result)) == 0x80000005ULL) goto loc_009D1C36;
    goto loc_009D1EBC;
loc_009D29DA:
    if (((unsigned int)(result)) != 0xC0000023ULL) goto loc_009D18A6;
    goto loc_009D27DF;
loc_009D29EA:
    if (v_stack_m154 != 17) goto loc_009D18B7;
    if (v_stack_m158 != 1) goto loc_009D18B7;
    goto loc_009D24CB;
loc_009D2A0A:
    if (((unsigned int)((unsigned int)(0xC000000DULL))) == 0xC000000EULL) goto loc_009D18B7;
    v_rbx = (unsigned int)(0xC000000DULL);
    if (((unsigned int)((unsigned int)(0xC000000DULL))) != 0xC00000C0ULL) { v_rbx = (unsigned int)((unsigned int)(0xC0000001ULL)); }
    goto loc_009D18B7;
loc_009D2A29:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, v_r14, v_stack_mE8, v_stack_m98);
    v_rsp = (v_rsp) + (400);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t _CmGetDeviceMappedPropertyFromComposite(void *Arg1, int64_t Arg2, int64_t Arg3, void *Arg4, void *Arg5, int64_t Arg6, uint32_t Arg7, void *Arg8, uint32_t Arg9)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg5 = (uint8_t *)Arg5;
    uint8_t *arg8 = (uint8_t *)Arg8;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint32_t v_stack_m114;
    uint32_t v_stack_m118;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint32_t v_stack_m140;
    uint32_t v_stack_m144;
    uint32_t v_stack_m148;
    uint32_t v_stack_m14C;
    uint32_t v_stack_m150;
    uint32_t v_stack_m154;
    uint32_t v_stack_m158;
    uint64_t v_stack_m160;
    uint8_t v_stack_m168;
    uint32_t v_stack_m178;
    uint64_t v_stack_m180;
    uint32_t v_stack_m188;
    uint64_t v_stack_m190;
    uint32_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m48;
    uint64_t v_stack_m98;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p20;
    uint32_t v_stack_p38;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (400);
    result = (*(uint64_t *)(v_rip + 0x439096)) ^ (local_rsp);
    v_stack_m48 = result;
    Arg1 = 0;
    v_stack_m138 = Arg3;
    v_stack_m160 = Arg2;
    v_stack_m130 = Arg5;
    v_stack_m144 = 0;
    v_stack_m158 = 0;
    v_stack_m150 = 0;
    v_stack_m14C = 0;
    v_stack_m148 = 0;
    v_stack_m118 = 0;
    v_stack_m110 = 0;
    v_stack_m154 = 0;
    v_stack_m114 = 0;
    v_stack_m168 = 0;
    v_stack_m128 = v_xmm0;
    v_stack_m108 = v_xmm1;
    v_stack_mF8 = v_xmm0;
    if ((uint16_t)((uint32_t)(Arg9)) != 0) goto loc_009D1BBC;
    *(uint32_t *)(arg5) = 0;
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg9)))) & (0xFFFF0000ULL));
    *(uint32_t *)(arg8) = 0;
    v_stack_m140 = (uint32_t)(local_r12);
    if (Arg6 == 0) goto loc_009D18BF;
    result = (uint32_t)(-((uint32_t)((uint32_t)((uint32_t)(Arg7)))));
    local_r14 = (Arg6) & (0);
loc_009D1759:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) < 2) goto loc_009D27CC;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == 10) goto loc_009D1AC0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == 256) goto loc_009D18CC;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == 2) goto loc_009D1D03;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == 3) goto loc_009D250F;
loc_009D1791:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == 12) goto loc_009D27E6;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == 4) goto loc_009D198E;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == 5) goto loc_009D1C40;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == 6) goto loc_009D1F5A;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == ((uint32_t)(4 + 3))) goto loc_009D2534;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == 11) goto loc_009D263E;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == 8) goto loc_009D1BD1;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == 9) goto loc_009D2224;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == 10) goto loc_009D255D;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == 2) goto loc_009D1DDF;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == 5) goto loc_009D1C60;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == 6) goto loc_009D1F7A;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == 15) goto loc_009D22E3;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == 16) goto loc_009D2407;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == 4) goto loc_009D1BC6;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == 14) goto loc_009D1E2F;
loc_009D182C:
loc_009D1834:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == 20) goto loc_009D2774;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == 21) goto loc_009D25B9;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == 26) goto loc_009D20B9;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == 22) goto loc_009D1B97;
loc_009D1858:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) != 23) goto loc_009D26DC;
    result = (*(uint64_t *)(arg4)) - (*(uint64_t *)(v_rip - 0x9BD7BB));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(arg4 + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x9BD7C0));
    }
    if (result != 0) goto loc_009D18B7;
loc_009D187D:
    v_stack_m190 = Arg8;
    v_stack_m198 = (uint32_t)((uint32_t)(Arg7));
    v_stack_m1A0 = local_r14;
    v_stack_m1A8 = Arg5;
    result = _CmGetDeviceCompoundFilters(0, Arg2, v_stack_m138, Arg4);
loc_009D18A4:
    local_rdi = 0;
loc_009D18A6:
loc_009D18AB:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 0xC000000EULL) goto loc_009D21DF;
loc_009D18B7:
    goto loc_009D2A29;
loc_009D18BF:
    v_stack_p38 = 0;
    goto loc_009D1759;
loc_009D18CC:
    Arg1 = (*(uint64_t *)(local_rdi)) - (*(uint64_t *)(v_rip - 0x9C0446));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint64_t *)(local_rdi + 0x8);
        Arg1 = (Arg1) - (*(uint64_t *)(v_rip - 0x9C044B));
    }
    if (Arg1 != NULL) goto loc_009D1834;
    local_rdi = 0;
    if (v_stack_m160 == 0) goto loc_009D299A;
loc_009D1903:
    if ((*(uint16_t *)(v_stack_m160)) == 0) goto loc_009D1912;
    result = (v_stack_m160) + (2);
    Arg4 = (200) - (1);
    if (condition_is_not_equal) goto loc_009D1903;
loc_009D1912:
    result = -(Arg4);
    local_r10 = (200) - (Arg4);
    Arg1 = (uint32_t)(~(Arg1));
    local_rbx = (uint32_t)(((uint32_t)(0xC000000DULL)) & ((uint32_t)(Arg1)));
    result = -(Arg4);
    result = (result) & (local_r10);
    if (Arg4 == NULL) goto loc_009D18AB;
    *(uint32_t *)(arg8) = (uint32_t)(result * 2 + 2);
    *(uint32_t *)(v_stack_m138) = 18;
    if (0 < ((uint32_t)((uint32_t)(*(uint32_t *)(arg8))))) goto loc_009D1C36;
    v_stack_m1A0 = 0x900ULL;
    Arg4 = 0;
    v_stack_m1A8 = 0;
    result = RtlStringCbCopyExW(local_r14, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg8)))), v_stack_m160, Arg4);
    if (!sign_flag) goto loc_009D18AB;
    *(uint32_t *)(arg8) = 0;
    *(uint32_t *)(v_stack_m130) = 0;
    goto loc_009D18AB;
loc_009D198E:
    result = (*(uint64_t *)(local_rdi)) - (*(uint64_t *)(v_rip - 0x9BD948));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(local_rdi + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x9BD94D));
    }
    Arg1 = 0;
    if (result == 0) goto loc_009D2279;
loc_009D19B0:
    result = (*(uint64_t *)(local_rdi)) - (*(uint64_t *)(v_rip - 0x9BD8C2));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(local_rdi + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x9BD8C7));
    }
    if (result != 0) goto loc_009D18B7;
    v_stack_m178 = (uint32_t)((uint32_t)(v_stack_m140));
    v_stack_m180 = v_stack_m158;
    v_stack_m188 = 16;
    v_stack_m190 = v_stack_m108;
    v_stack_m198 = v_stack_m154;
    *(uint32_t *)(v_stack_m160) = 17;
    v_stack_m1A0 = v_rip - 10224798;
    v_stack_m1A8 = 0;
    *(uint32_t *)(arg8) = 1;
    result = PnpGetObjectProperty(0, v_stack_m160, 1, Arg4);
    if (sign_flag) goto loc_009D18A4;
    v_stack_m178 = (uint32_t)((uint32_t)(v_stack_m140));
    v_stack_m180 = v_stack_m158;
    v_stack_m188 = 16;
    v_stack_m190 = v_stack_mF8;
    local_rdi = 0;
    Arg4 = 0;
    v_stack_m198 = v_stack_m154;
    v_stack_m1A0 = v_rip - 10213732;
    v_stack_m1A8 = 0;
    result = PnpGetObjectProperty(0, v_rip + 1237702, local_rdi + 1, Arg4);
    if (sign_flag) goto loc_009D18A6;
    if (Arg7 < ((uint32_t)((uint32_t)(*(uint32_t *)(arg8))))) goto loc_009D1C36;
    result = memcmp(v_stack_mF8, v_stack_m108, local_rdi + 16, Arg4);
    result = (uint32_t)(-(result));
    Arg1 = (uint8_t)(-(v_stack_mF8));
    Arg1 = (uint8_t)((Arg1) - 1);
loc_009D1AB8:
    *(uint8_t *)(local_r14) = (uint8_t)(Arg1);
    goto loc_009D18B7;
loc_009D1AC0:
    result = (*(uint64_t *)(local_rdi)) - (*(uint64_t *)(v_rip - 0x9BDA4A));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(local_rdi + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x9BDA4F));
    }
    if (result != 0) goto loc_009D255D;
    v_stack_m178 = (uint32_t)((uint32_t)(v_stack_m140));
    v_stack_m180 = v_stack_m158;
    local_rdi = 0;
    v_stack_m188 = (uint32_t)(v_stack_m108);
    v_stack_m190 = local_r14;
    v_stack_m198 = local_rdi + 16;
    v_stack_m1A0 = v_rip - 10213988;
    v_stack_m1A8 = 0;
    result = PnpGetObjectProperty(Arg1, v_stack_m160, local_rdi + 1, Arg4);
    if ((uint32_t)(result) == 0) goto loc_009D1B8C;
    if (((uint32_t)(result)) == 0xC0000023ULL) goto loc_009D1B8C;
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0xC0000225ULL)))) goto loc_009D18A6;
    v_stack_m178 = (uint32_t)((uint32_t)(v_stack_m140));
    v_stack_m180 = v_stack_m158;
    v_stack_m188 = (uint32_t)((uint32_t)(Arg7));
    v_stack_m190 = local_r14;
    v_stack_m198 = v_stack_m130;
    v_stack_m1A0 = v_rip - 10213963;
    v_stack_m1A8 = 0;
    result = PnpGetObjectProperty(Arg1, v_stack_m160, local_rdi + 1, v_stack_m138);
    if ((uint32_t)(result) != 0) goto loc_009D21C6;
loc_009D1B8C:
    *(uint32_t *)(arg8) = (uint32_t)((uint32_t)(v_stack_m158));
    goto loc_009D18A6;
loc_009D1B97:
    Arg1 = (*(uint64_t *)(local_rdi)) - (*(uint64_t *)(v_rip - 0x9BDAD9));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint64_t *)(local_rdi + 0x8);
        Arg1 = (Arg1) - (*(uint64_t *)(v_rip - 0x9BDADE));
    }
    if (Arg1 == NULL) goto loc_009D187D;
    goto loc_009D1858;
loc_009D1BBC:
    goto loc_009D18B7;
loc_009D1BC6:
    Arg1 = 0;
    goto loc_009D19B0;
loc_009D1BD1:
    result = (*(uint64_t *)(local_rdi)) - (*(uint64_t *)(v_rip - 0x9BDA3B));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(local_rdi + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x9BDA40));
    }
    if (result != 0) goto loc_009D1EC9;
    Arg2 = (uint32_t)((v_stack_m160) >> (1));
    v_stack_m150 = (uint32_t)(Arg2);
    result = CmGetDeviceParent(0, v_stack_m160, local_r14, v_stack_m150);
    local_rdi = 0;
    if ((uint32_t)(result) != 0) goto loc_009D29BA;
loc_009D1C16:
    result = (uint32_t)(((uint32_t)(v_stack_m150)) + ((uint32_t)((uint32_t)(v_stack_m150))));
    *(uint32_t *)(arg8) = (uint32_t)(result);
    *(uint32_t *)(v_stack_m130) = 18;
loc_009D1C28:
    if (Arg7 >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg8))))) goto loc_009D18A6;
loc_009D1C36:
    goto loc_009D18B7;
loc_009D1C40:
    result = (*(uint64_t *)(local_rdi)) - (*(uint64_t *)(v_rip - 0x9BDA4A));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(local_rdi + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x9BDA4F));
    }
    if (result == 0) goto loc_009D29A4;
loc_009D1C60:
    result = (*(uint64_t *)(local_rdi)) - (*(uint64_t *)(v_rip - 0x9BDAB2));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(local_rdi + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x9BDAB7));
    }
    local_rdi = 0;
    if (result != 0) goto loc_009D18B7;
    *(uint32_t *)(arg8) = 1;
    *(uint32_t *)(local_r14) = 17;
    if (((uint32_t)(v_stack_m160)) < (*(uint32_t *)(arg8))) goto loc_009D1C36;
    result = RtlInitUnicodeStringEx(v_stack_m128, v_stack_m160, local_r14, v_stack_m150);
    if (sign_flag) goto loc_009D18A6;
    *(uint8_t *)(local_r14) = 0;
    if (*(uint64_t *)(arg1 + 0x108) == 0) goto loc_009D26B1;
    v_stack_m1A0 = 0;
    v_stack_m1A8 = v_stack_m144;
    result = guard_dispatch_icall(0, v_stack_m128, v_stack_m14C, v_stack_m148);
    if (((uint32_t)(result)) == 0x80000005ULL) goto loc_009D1C36;
    if (((uint32_t)(result)) == 0xC000000EULL) goto loc_009D21BF;
    if (sign_flag) goto loc_009D18B7;
    goto loc_009D20B0;
loc_009D1D03:
    result = (*(uint64_t *)(local_rdi)) - (*(uint64_t *)(v_rip - 0x9BDA4D));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(local_rdi + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x9BDA52));
    }
    if (result != 0) goto loc_009D1DE3;
loc_009D1D23:
    v_stack_m1A0 = v_stack_m144;
    v_stack_m1A8 = v_stack_m148;
    result = CmGetDeviceStatus(0, v_stack_m160, v_stack_m138, v_stack_m14C);
    if (sign_flag) goto loc_009D18A4;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x10)))) != 2) goto loc_009D24D6;
    result = (*(uint64_t *)(local_rdi)) - (*(uint64_t *)(v_rip - 0x9BDAB4));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(local_rdi + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x9BDAB9));
    }
    if (result != 0) goto loc_009D24D6;
loc_009D1D8A:
loc_009D1D90:
    *(uint32_t *)(arg8) = 4;
    *(uint32_t *)(v_stack_m130) = 7;
    if (Arg7 < ((uint32_t)((uint32_t)(*(uint32_t *)(arg8))))) goto loc_009D1C36;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x10)))) != 2) goto loc_009D2677;
    result = (*(uint64_t *)(local_rdi)) - (*(uint64_t *)(v_rip - 0x9BDB01));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(local_rdi + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x9BDB06));
    }
    if (result != 0) goto loc_009D280B;
    *(uint32_t *)(local_r14) = (uint32_t)((uint32_t)(v_stack_m14C));
    goto loc_009D18B7;
loc_009D1DDF:
loc_009D1DE3:
    result = (*(uint64_t *)(local_rdi)) - (*(uint64_t *)(v_rip - 0x9BDBD5));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(local_rdi + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x9BDBDA));
    }
    if (result != 0) goto loc_009D28B3;
    *(uint32_t *)(arg8) = 1;
    *(uint32_t *)((uint32_t)(*(uint32_t *)(local_rdi + 0x10))) = 17;
    if (((uint32_t)((uint32_t)(0x400ULL))) < (*(uint32_t *)(arg8))) goto loc_009D1C36;
    result = CmIsDeviceSafeRemovalRequired(0, v_stack_m160, v_stack_m138, v_stack_m138);
    result = (uint8_t)(-(result));
    goto loc_009D1AB8;
loc_009D1E2F:
    result = (*(uint64_t *)(local_rdi)) - (*(uint64_t *)(v_rip - 0x9BDC51));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(local_rdi + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x9BDC56));
    }
    local_rdi = 0;
    if (result != 0) goto loc_009D18B7;
    *(uint32_t *)(v_stack_m138) = 0x2012ULL;
    result = RtlInitUnicodeStringEx(v_stack_m128, v_stack_m160, v_stack_m138, v_stack_m138);
    if (sign_flag) goto loc_009D18A6;
    if (*(uint64_t *)(arg1 + 0x100) == 0) goto loc_009D26B1;
loc_009D1E82:
    v_stack_m198 = 0;
    v_stack_m1A0 = Arg8;
    v_stack_m1A8 = (uint32_t)((uint32_t)(Arg7));
    result = guard_dispatch_icall(0, v_stack_m128, local_rdi + 14, local_r14);
    if (((uint32_t)(result)) == 0x80000005ULL) goto loc_009D1C36;
    if (((uint32_t)(result)) == 0xC0000034ULL) goto loc_009D1F52;
loc_009D1EBC:
    if (sign_flag) goto loc_009D18A6;
    goto loc_009D18B7;
loc_009D1EC9:
    result = (*(uint64_t *)(local_rdi)) - (*(uint64_t *)(v_rip - 0x9BDD03));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(local_rdi + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x9BDD08));
    }
    local_rdi = 0;
    if (result != 0) goto loc_009D18B7;
    *(uint32_t *)(local_rdi + 0xE) = (uint32_t)(local_r14);
    *(uint32_t *)(arg8) = (uint32_t)((uint32_t)(v_stack_m140));
    result = RtlInitUnicodeStringEx(v_stack_m128, v_stack_m160, local_rdi + 14, local_r14);
    if (sign_flag) goto loc_009D18A6;
    if (*(uint64_t *)(arg1 + 0x100) == 0) goto loc_009D26B1;
    v_stack_m198 = 0;
    v_stack_m1A0 = Arg7;
    v_stack_m1A8 = (uint32_t)((uint32_t)(Arg7));
    result = guard_dispatch_icall(0, v_stack_m128, local_rdi + 13, local_r14);
    if (((uint32_t)(result)) != 0xC0000034ULL) goto loc_009D29CA;
loc_009D1F52:
    goto loc_009D18B7;
loc_009D1F5A:
    result = (*(uint64_t *)(local_rdi)) - (*(uint64_t *)(v_rip - 0x9BDCEC));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(local_rdi + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x9BDCF1));
    }
    if (result == 0) goto loc_009D29AF;
loc_009D1F7A:
    result = (*(uint64_t *)(local_rdi)) - (*(uint64_t *)(v_rip - 0x9BDD24));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(local_rdi + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x9BDD29));
    }
    local_rdi = 0;
    if (result != 0) goto loc_009D18B7;
    *(uint32_t *)(local_rdi + 0xD) = 17;
    *(uint32_t *)(arg8) = 1;
    if (((uint32_t)(v_stack_m128)) < 1) goto loc_009D1C36;
    result = RtlInitUnicodeStringEx(v_stack_m128, v_stack_m160, local_rdi + 13, local_r14);
    if (sign_flag) goto loc_009D18A6;
    *(uint8_t *)(local_r14) = 0;
    if (*(uint64_t *)(arg1 + 0x108) == 0) goto loc_009D26B1;
    v_stack_m1A0 = 0;
    v_stack_m1A8 = v_stack_m144;
    result = guard_dispatch_icall(0, v_stack_m128, v_stack_m14C, v_stack_m148);
    if (((uint32_t)(result)) == 0x80000005ULL) goto loc_009D1C36;
    if (((uint32_t)(result)) == 0xC000000EULL) goto loc_009D21BF;
    if (sign_flag) goto loc_009D18B7;
    if (condition_is_below) goto loc_009D20B0;
    if (condition_is_below) goto loc_009D26BB;
loc_009D2035:
    if ((((uint8_t)((uint32_t)(v_stack_m14C))) & (8)) != 0) goto loc_009D18B7;
    v_stack_m178 = (uint32_t)((uint32_t)(v_stack_m140));
    local_rdi = 0;
    v_stack_m180 = v_stack_m158;
    v_stack_m188 = (uint32_t)((uint32_t)(v_stack_m140));
    v_stack_m190 = v_stack_m118;
    v_stack_m198 = v_stack_m154;
    v_stack_m1A0 = v_rip - 10214824;
    v_stack_m1A8 = 0;
    result = PnpGetObjectProperty(0, v_stack_m160, local_rdi + 1, v_stack_m138);
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC0000225ULL)))) goto loc_009D21BF;
    if (sign_flag) goto loc_009D18A6;
loc_009D20AA:
    if (((v_stack_m118) & ((uint8_t)(local_rdi + 64))) == 0) goto loc_009D18B7;
loc_009D20B0:
    *(uint8_t *)(local_r14) = 255;
    goto loc_009D18B7;
loc_009D20B9:
    result = (*(uint64_t *)(local_rdi)) - (*(uint64_t *)(v_rip - 0x9BDE93));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(local_rdi + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x9BDE98));
    }
    local_rdi = 0;
    if (result != 0) goto loc_009D18B7;
    *(uint32_t *)(local_rdi + 0x1) = 17;
    *(uint32_t *)(arg8) = 1;
    if (((uint32_t)(v_stack_m160)) < 1) goto loc_009D1C36;
    v_stack_m178 = (uint32_t)(local_rdi + 64);
    v_stack_m180 = v_stack_m158;
    v_stack_m188 = 1;
    v_stack_m190 = v_stack_m168;
    *(uint8_t *)(local_r14) = 0;
    v_stack_m198 = v_stack_m154;
    v_stack_m1A0 = v_rip - 10215072;
    v_stack_m1A8 = 0;
    result = PnpGetObjectProperty(0, v_stack_m160, local_rdi + 1, v_stack_m138);
    if (!sign_flag) goto loc_009D2611;
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0xC0000225ULL)))) goto loc_009D2667;
loc_009D2152:
    v_stack_m178 = (uint32_t)(local_rdi + 64);
    v_stack_m180 = v_stack_m158;
    v_stack_m188 = 1;
    v_stack_m190 = v_stack_m168;
    v_stack_m198 = v_stack_m154;
    v_stack_m1A0 = v_rip - 10215150;
    v_stack_m1A8 = 0;
    result = PnpGetObjectProperty(0, v_stack_m160, 1, v_stack_m138);
    if (!sign_flag) goto loc_009D29EA;
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC0000225ULL)))) goto loc_009D21BF;
    if (((uint32_t)(result)) != 0xC0000023ULL) goto loc_009D18A6;
loc_009D21BF:
    goto loc_009D18B7;
loc_009D21C6:
    if (((uint32_t)(result)) == 0xC0000023ULL) goto loc_009D1B8C;
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0xC0000225ULL)))) goto loc_009D18A6;
    goto loc_009D18B7;
loc_009D21DF:
    v_stack_m190 = 0;
    v_stack_m198 = v_stack_m110;
    Arg4 = 0;
    v_stack_m1A0 = 0;
    v_stack_m1A8 = 1;
    result = _CmOpenDeviceRegKey(0, v_stack_m160, Arg4 + 16, Arg4);
    if ((uint32_t)(result) != 0) goto loc_009D2A0A;
    result = ZwClose(v_stack_m110, v_stack_m160, Arg4 + 16, Arg4);
    goto loc_009D1F52;
loc_009D2224:
    result = (*(uint64_t *)(local_rdi)) - (*(uint64_t *)(v_rip - 0x9BDFE6));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(local_rdi + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x9BDFEB));
    }
    local_rdi = 0;
    if (result != 0) goto loc_009D18B7;
    Arg2 = (uint32_t)((v_stack_m160) >> (1));
    v_stack_m150 = (uint32_t)(Arg2);
    result = CmGetDeviceChildren(0, v_stack_m160, local_r14, v_stack_m150);
    if (((uint32_t)(result)) == 0xC0000023ULL) goto loc_009D25A2;
loc_009D226E:
    if ((uint32_t)(result) != 0) goto loc_009D18A6;
    goto loc_009D25A2;
loc_009D2279:
    Arg2 = (uint32_t)((v_stack_m160) >> (1));
    v_stack_m1A0 = v_stack_m150;
    v_stack_m1A8 = (uint32_t)(Arg2);
    result = CmGetDeviceRelationsList(0, v_stack_m160, (uint32_t)((uint32_t)(local_rdi + 64)), local_r14);
    if (((uint32_t)(result)) == 0xC0000034ULL) goto loc_009D1F52;
    local_rdi = 0;
    if ((uint32_t)(result) == 0) goto loc_009D22B8;
    if (((uint32_t)(result)) != 0xC0000023ULL) goto loc_009D18A6;
loc_009D22B8:
    *(uint32_t *)(v_stack_m130) = 0x2012ULL;
    if ((uint32_t)((uint32_t)((uint32_t)(result))) == 0) goto loc_009D2631;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 0xC0000023ULL) goto loc_009D18A6;
loc_009D22DA:
    result = (uint32_t)(((uint32_t)(v_stack_m150)) + ((uint32_t)((uint32_t)(v_stack_m150))));
    *(uint32_t *)(arg8) = (uint32_t)(result);
    goto loc_009D18B7;
loc_009D22E3:
    result = (*(uint64_t *)(local_rdi)) - (*(uint64_t *)(v_rip - 0x9BDFFD));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(local_rdi + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x9BE002));
    }
    local_rdi = 0;
    if (result != 0) goto loc_009D18B7;
    *(uint32_t *)((uint32_t)((uint32_t)(local_rdi + 0x40))) = 17;
    *(uint32_t *)(arg8) = 1;
    if (((uint32_t)(v_stack_m160)) < 1) goto loc_009D1C36;
    result = RtlInitUnicodeStringEx(v_stack_m128, v_stack_m160, (uint32_t)((uint32_t)(local_rdi + 64)), local_r14);
    if (sign_flag) goto loc_009D18A6;
    *(uint8_t *)(local_r14) = 0;
    if (*(uint64_t *)(arg1 + 0x108) == 0) goto loc_009D26B1;
    v_stack_m1A0 = 0;
    v_stack_m1A8 = v_stack_m144;
    result = guard_dispatch_icall(0, v_stack_m128, v_stack_m14C, v_stack_m148);
    if (((uint32_t)(result)) == 0x80000005ULL) goto loc_009D1C36;
    if (((uint32_t)(result)) == 0xC000000EULL) goto loc_009D21BF;
    if (sign_flag) goto loc_009D18B7;
    if (((v_stack_m14C) & (0x2000000ULL)) != 0) goto loc_009D18B7;
    Arg4 = 0;
    v_stack_m178 = (uint32_t)((uint32_t)(v_stack_m140));
    v_stack_m180 = v_stack_m158;
    local_rdi = 0;
    v_stack_m188 = 1;
    v_stack_m190 = v_stack_m168;
    v_stack_m198 = v_stack_m154;
    v_stack_m1A0 = v_rip - 10215605;
    v_stack_m1A8 = 0;
    result = PnpGetObjectProperty(0, v_stack_m160, local_rdi + 1, Arg4);
    if (sign_flag) goto loc_009D27D6;
    if (v_stack_m154 != 17) goto loc_009D20B0;
    goto loc_009D20AA;
loc_009D2407:
    result = (*(uint64_t *)(local_rdi)) - (*(uint64_t *)(v_rip - 0x9BE109));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(local_rdi + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x9BE10E));
    }
    local_rdi = 0;
    if (result != 0) goto loc_009D18B7;
    *(uint32_t *)(local_rdi + 0x1) = 17;
    *(uint32_t *)(arg8) = 1;
    if (((uint32_t)(v_stack_m160)) < 1) goto loc_009D1C36;
    result = RtlInitUnicodeStringEx(v_stack_m128, v_stack_m160, local_rdi + 1, Arg4);
    if (sign_flag) goto loc_009D18A6;
    *(uint8_t *)(local_r14) = 0;
    if (*(uint64_t *)(arg1 + 0x108) == 0) goto loc_009D26B1;
    v_stack_m1A0 = 0;
    v_stack_m1A8 = v_stack_m144;
    result = guard_dispatch_icall(0, v_stack_m128, v_stack_m14C, v_stack_m148);
    if (((uint32_t)(result)) == 0xC000000EULL) goto loc_009D21BF;
    if (((uint32_t)(result)) == 0x80000005ULL) goto loc_009D1C36;
    if (sign_flag) goto loc_009D18B7;
    if (((v_stack_m14C) & (256)) != 0) goto loc_009D20B0;
    if (((v_stack_m14C) & ((uint32_t)((uint32_t)(0x400ULL)))) == 0) goto loc_009D18B7;
loc_009D24CB:
    if (v_stack_m148 != 14) goto loc_009D18B7;
    goto loc_009D20B0;
loc_009D24D6:
    if (((uint32_t)(v_stack_m14C)) != 3) goto loc_009D24FC;
    result = (*(uint64_t *)(local_rdi)) - (*(uint64_t *)(v_rip - 0x9B658E));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(local_rdi + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x9B6593));
    }
    if (result == 0) goto loc_009D1D8A;
loc_009D24FC:
    if ((((uint32_t)((uint32_t)(0x400ULL))) & (0)) == 0) goto loc_009D1F52;
    goto loc_009D1D90;
loc_009D250F:
    Arg1 = (*(uint64_t *)(local_rdi)) - (*(uint64_t *)(v_rip - 0x9B65C1));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint64_t *)(local_rdi + 0x8);
        Arg1 = (Arg1) - (*(uint64_t *)(v_rip - 0x9B65C6));
    }
    if (Arg1 != NULL) goto loc_009D1791;
    goto loc_009D1D23;
loc_009D2534:
    Arg1 = (*(uint64_t *)(local_rdi)) - (*(uint64_t *)(v_rip - 0x9BE206));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint64_t *)(local_rdi + 0x8);
        Arg1 = (Arg1) - (*(uint64_t *)(v_rip - 0x9BE20B));
    }
    if (Arg1 != NULL) goto loc_009D182C;
    goto loc_009D2279;
loc_009D255D:
    result = (*(uint64_t *)(local_rdi)) - (*(uint64_t *)(v_rip - 0x9BE1B7));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(local_rdi + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x9BE1BC));
    }
    local_rdi = 0;
    if (result != 0) goto loc_009D18B7;
    Arg2 = (uint32_t)(((uint32_t)(0x400ULL)) >> (1));
    v_stack_m150 = (uint32_t)(Arg2);
    result = CmGetDeviceSiblings(Arg1, v_stack_m160, local_r14, v_stack_m150);
    if ((uint32_t)(result) != 0) goto loc_009D28A9;
loc_009D25A2:
    result = (uint32_t)(((uint32_t)(v_stack_m150)) + ((uint32_t)((uint32_t)(v_stack_m150))));
    *(uint32_t *)(arg8) = (uint32_t)(result);
    *(uint32_t *)(v_stack_m130) = 0x2012ULL;
    goto loc_009D1C28;
loc_009D25B9:
    result = (*(uint64_t *)(local_rdi)) - (*(uint64_t *)(v_rip - 0x9BE25B));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(local_rdi + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x9BE260));
    }
    local_rdi = 0;
    if (result != 0) goto loc_009D18B7;
    *(uint32_t *)(local_r14) = 0x2012ULL;
    result = RtlInitUnicodeStringEx(v_stack_m128, v_stack_m160, local_r14, v_stack_m150);
    if (sign_flag) goto loc_009D18A6;
    if (*(uint64_t *)(arg1 + 0x100) == 0) goto loc_009D26B1;
    goto loc_009D1E82;
loc_009D2611:
    if (v_stack_m154 != 17) goto loc_009D2152;
    if (v_stack_m158 != 1) goto loc_009D2152;
    goto loc_009D24CB;
loc_009D2631:
    result = PnpMultiSzGetLen(local_r14, v_stack_m160, local_rdi + 16, v_stack_m150);
    goto loc_009D22DA;
loc_009D263E:
    Arg1 = (*(uint64_t *)(local_rdi)) - (*(uint64_t *)(v_rip - 0x9BE208));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint64_t *)(local_rdi + 0x8);
        Arg1 = (Arg1) - (*(uint64_t *)(v_rip - 0x9BE20D));
    }
    if (Arg1 != NULL) goto loc_009D182C;
    goto loc_009D2279;
loc_009D2667:
    if (((uint32_t)(result)) != 0xC0000023ULL) goto loc_009D18A6;
    goto loc_009D2152;
loc_009D2677:
    if (((uint32_t)(result)) != 3) goto loc_009D280B;
    result = (*(uint64_t *)(local_rdi)) - (*(uint64_t *)(v_rip - 0x9B6732));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(local_rdi + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x9B6737));
    }
    if (result != 0) goto loc_009D280B;
    Arg1 = (uint32_t)((Arg1) & ((uint32_t)(v_stack_m160)));
    Arg1 = (uint32_t)(-(Arg1));
    result = (uint32_t)((result) & (v_stack_m148));
loc_009D26A9:
    *(uint32_t *)(local_r14) = (uint32_t)(result);
    goto loc_009D18B7;
loc_009D26B1:
    goto loc_009D18B7;
loc_009D26BB:
    if (((uint32_t)((uint32_t)(v_stack_m148))) > 29) goto loc_009D20B0;
    if (((uint32_t)((uint32_t)(v_stack_m148))) < 29) goto loc_009D2035;
    goto loc_009D20B0;
loc_009D26DC:
    if (((uint32_t)(result)) != 102) goto loc_009D18B7;
    result = (*(uint64_t *)(local_rdi)) - (*(uint64_t *)(v_rip - 0x9C1277));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(local_rdi + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x9C127C));
    }
    local_rdi = 0;
    if (result != 0) goto loc_009D18B7;
    v_stack_m178 = (uint32_t)(Arg1 + 64);
    v_stack_m180 = v_stack_m158;
    v_stack_m188 = (uint32_t)((uint32_t)(v_stack_m148));
    v_stack_m190 = local_r14;
    v_stack_m198 = v_stack_m154;
    v_stack_m1A0 = v_rip - 10227730;
    v_stack_m1A8 = 0;
    result = PnpGetObjectProperty(Arg1, v_stack_m160, local_rdi + 1, v_stack_m150);
    result = (uint32_t)((result) + ((uint32_t)((uint32_t)(0x80000000ULL))));
    if ((((uint32_t)((uint32_t)(0x80000000ULL))) & ((uint32_t)(result))) == 0) goto loc_009D2813;
loc_009D275A:
    if (v_stack_m154 != 19) goto loc_009D2828;
    *(uint32_t *)(v_stack_m130) = 19;
    goto loc_009D1B8C;
loc_009D2774:
    result = (*(uint64_t *)(local_rdi)) - (*(uint64_t *)(v_rip - 0x9BE326));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(local_rdi + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x9BE32B));
    }
    local_rdi = 0;
    if (result != 0) goto loc_009D18B7;
    *(uint32_t *)(local_rdi + 0x1) = 0x2012ULL;
    result = RtlInitUnicodeStringEx(v_stack_m128, v_stack_m160, local_rdi + 1, v_stack_m150);
    if (sign_flag) goto loc_009D18A6;
    if (*(uint64_t *)(arg1 + 0x100) == 0) goto loc_009D26B1;
    goto loc_009D1E82;
loc_009D27CC:
    goto loc_009D18B7;
loc_009D27D6:
    if (((uint32_t)(*(uint64_t *)(arg1 + 0x100))) != ((uint32_t)((uint32_t)(0xC0000225ULL)))) goto loc_009D29DA;
loc_009D27DF:
    goto loc_009D20B0;
loc_009D27E6:
    Arg1 = (*(uint64_t *)(local_rdi)) - (*(uint64_t *)(v_rip - 0x9BE380));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint64_t *)(local_rdi + 0x8);
        Arg1 = (Arg1) - (*(uint64_t *)(v_rip - 0x9BE385));
    }
    if (Arg1 != NULL) goto loc_009D1834;
    goto loc_009D1D23;
loc_009D280B:
    goto loc_009D26A9;
loc_009D2813:
    if (0 == 0xC0000023ULL) goto loc_009D275A;
    if (0 != ((uint32_t)((uint32_t)(0xC0000225ULL)))) goto loc_009D18A6;
loc_009D2828:
    v_stack_m178 = (uint32_t)(Arg1 + 64);
    v_stack_m180 = v_stack_m158;
    v_stack_m188 = (uint32_t)((uint32_t)(Arg7));
    v_stack_m190 = local_r14;
    v_stack_m198 = v_stack_m154;
    v_stack_m1A0 = v_rip - 10228401;
    v_stack_m1A8 = 0;
    result = PnpGetObjectProperty(Arg1, v_stack_m160, 1, v_stack_m138);
    result = (uint32_t)((result) + ((uint32_t)((uint32_t)(0x80000000ULL))));
    if ((((uint32_t)((uint32_t)(0x80000000ULL))) & ((uint32_t)(result))) != 0) goto loc_009D2891;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 0xC0000023ULL) goto loc_009D18A6;
loc_009D2891:
    goto loc_009D18AB;
loc_009D28A9:
    goto loc_009D226E;
loc_009D28B3:
    result = (*(uint64_t *)(local_rdi)) - (*(uint64_t *)(v_rip - 0x9C1355));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(local_rdi + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x9C135A));
    }
    local_rdi = 0;
    if (result != 0) goto loc_009D18B7;
    v_stack_m190 = (uint32_t)(local_r10);
    v_stack_m198 = v_stack_m158;
    v_stack_m158 = 78;
    v_stack_m1A0 = v_stack_mE8;
    v_stack_m1A8 = v_stack_m114;
    result = CmGetDeviceRegProp(Arg1, v_stack_m160, v_stack_m138, local_rdi + 37);
    if (sign_flag) goto loc_009D18A6;
    result = wcscmp(v_rip + 1225674, v_stack_mE8, v_stack_m138, local_rdi + 37);
    if ((uint32_t)(result) == 0) goto loc_009D1F52;
    *(uint32_t *)(arg8) = 16;
    *(uint32_t *)(v_stack_m130) = 13;
    if (Arg7 < ((uint32_t)((uint32_t)(*(uint32_t *)(arg8))))) goto loc_009D1C36;
    result = _CmGetDeviceContainerIdFromBase(Arg1, v_stack_m160, v_stack_mE8, v_stack_m98);
    if (sign_flag) goto loc_009D18A6;
    result = RtlInitUnicodeStringEx(v_stack_m128, v_stack_m98, v_stack_mE8, v_stack_m98);
    if (sign_flag) goto loc_009D18A6;
    result = RtlGUIDFromString(v_stack_m128, local_r14, v_stack_mE8, v_stack_m98);
    goto loc_009D18A6;
loc_009D299A:
    goto loc_009D18AB;
loc_009D29A4:
    goto loc_009D2279;
loc_009D29AF:
    goto loc_009D2279;
loc_009D29BA:
    if (((uint32_t)(result)) != 0xC0000023ULL) goto loc_009D18A6;
    goto loc_009D1C16;
loc_009D29CA:
    if (((uint32_t)(result)) == 0x80000005ULL) goto loc_009D1C36;
    goto loc_009D1EBC;
loc_009D29DA:
    if (((uint32_t)(result)) != 0xC0000023ULL) goto loc_009D18A6;
    goto loc_009D27DF;
loc_009D29EA:
    if (v_stack_m154 != 17) goto loc_009D18B7;
    if (v_stack_m158 != 1) goto loc_009D18B7;
    goto loc_009D24CB;
loc_009D2A0A:
    if (((uint32_t)((uint32_t)(0xC000000DULL))) == 0xC000000EULL) goto loc_009D18B7;
    local_rbx = (uint32_t)(0xC000000DULL);
    if (((uint32_t)((uint32_t)(0xC000000DULL))) != 0xC00000C0ULL) { local_rbx = (uint32_t)((uint32_t)(0xC0000001ULL)); }
    goto loc_009D18B7;
loc_009D2A29:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, local_r14, v_stack_mE8, v_stack_m98);
    local_rsp = (local_rsp) + (400);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x100` | `64` | `R` |
| `Arg1` | `+ 0x108` | `64` | `R` |
| `Arg4` | `+ 0x0` | `64` | `R` |
| `Arg4` | `+ 0x8` | `64` | `R` |
| `Arg4` | `+ 0x10` | `32` | `R` |
| `Arg5` | `+ 0x0` | `32` | `W` |
| `Arg8` | `+ 0x0` | `32` | `R` |
| `Arg8` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009D1684&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
