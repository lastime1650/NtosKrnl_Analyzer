# PiDqPnPGetObjectPropertyInBestLocale

- RVA: `0x008DEE10`–`0x008DF2EE` (길이 `1,246` bytes)
- VA: `0x00000001408DEE10`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00085B8C`
- 디코드: `318`개 명령, `1,246/1,246` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **15**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x008DEF06` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008DEFA2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008DEFB5` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008DF05D` → [PiPnpRtlObjectActionCallback](../8E/PiPnpRtlObjectActionCallback_function_008E2850.md) (function, `0x008E2850`)
- `0x008DF0C4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008DF0DA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008DF10A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008DF174` → [PnpGetObjectPropertyWorker](../8E/PnpGetObjectPropertyWorker_function_008E1810.md) (function, `0x008E1810`)
- `0x008DF1B9` → [PiPnpRtlObjectActionCallback](../8E/PiPnpRtlObjectActionCallback_function_008E2850.md) (function, `0x008E2850`)
- `0x008DF202` → [PiDqPnPGetObjectProperty](PiDqPnPGetObjectProperty_function_008DFD90.md) (function, `0x008DFD90`)
- `0x008DF254` → [PnpGetGenericStoreProperty](../8E/PnpGetGenericStoreProperty_function_008EFBA0.md) (function, `0x008EFBA0`)
- `0x008DF281` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008DF2A9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008DF2D7` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008DF2E4` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [PiDqActionDataGetRequestedProperties](PiDqActionDataGetRequestedProperties_function_008DEBE4.md) at `0x008DECD6`
- [PiDqActionDataGetAllPropertiesInBestLanguage](../98/PiDqActionDataGetAllPropertiesInBestLanguage_function_0098FB7C.md) at `0x0098FC87`
- [PiDqActionDataGetChangedProperties](../A6/PiDqActionDataGetChangedProperties_function_00A61F10.md) at `0x00A62148`

### Static image references
- `0x008DEFDC` → RVA `0x00E66398` (`.data`; read)
- `0x008DF030` → RVA `0x008E2850` (`PiPnpRtlObjectActionCallback`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **10**
  - `0x008DEF06` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008DEFA2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008DEFB5` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008DF0C4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008DF0DA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008DF10A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008DF281` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008DF2A9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008DF2D7` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008DF2E4` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008DEE10  48 8B C4                        mov rax, rsp
008DEE13  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
008DEE17  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
008DEE1B  89 50 10                        mov dword ptr [rax + 0x10], edx
008DEE1E  48 89 48 08                     mov qword ptr [rax + 8], rcx
008DEE22  55                              push rbp
008DEE23  53                              push rbx
008DEE24  56                              push rsi
008DEE25  57                              push rdi
008DEE26  41 54                           push r12
008DEE28  41 55                           push r13
008DEE2A  41 56                           push r14
008DEE2C  41 57                           push r15
008DEE2E  48 8D 68 B9                     lea rbp, [rax - 0x47]
008DEE32  48 81 EC C8 00 00 00            sub rsp, 0xc8
008DEE39  48 8B 75 7F                     mov rsi, qword ptr [rbp + 0x7f]
008DEE3D  0F 57 C0                        xorps xmm0, xmm0
008DEE40  4C 8B 65 77                     mov r12, qword ptr [rbp + 0x77]
008DEE44  4D 8B F1                        mov r14, r9
008DEE47  45 33 C9                        xor r9d, r9d
008DEE4A  0F 11 06                        movups xmmword ptr [rsi], xmm0
008DEE4D  0F 11 46 10                     movups xmmword ptr [rsi + 0x10], xmm0
008DEE51  0F 11 46 20                     movups xmmword ptr [rsi + 0x20], xmm0
008DEE55  66 45 39 0C 24                  cmp word ptr [r12], r9w
008DEE5A  0F 84 83 03 00 00               je 0x1408df1e3
008DEE60  41 0F 10 06                     movups xmm0, xmmword ptr [r14]
008DEE64  4D 8B F9                        mov r15, r9
008DEE67  C7 45 77 00 02 00 00            mov dword ptr [rbp + 0x77], 0x200
008DEE6E  45 8B E9                        mov r13d, r9d
008DEE71  44 89 4D 9F                     mov dword ptr [rbp - 0x61], r9d
008DEE75  0F 11 06                        movups xmmword ptr [rsi], xmm0
008DEE78  41 8B 46 10                     mov eax, dword ptr [r14 + 0x10]
008DEE7C  BA FF FF FF 7F                  mov edx, 0x7fffffff
008DEE81  48 83 66 20 00                  and qword ptr [rsi + 0x20], 0
008DEE86  89 46 10                        mov dword ptr [rsi + 0x10], eax
008DEE89  8B 45 6F                        mov eax, dword ptr [rbp + 0x6f]
008DEE8C  89 46 14                        mov dword ptr [rsi + 0x14], eax
008DEE8F  49 8B C4                        mov rax, r12
008DEE92  4C 89 4E 28                     mov qword ptr [rsi + 0x28], r9
008DEE96  4C 89 4E 18                     mov qword ptr [rsi + 0x18], r9
008DEE9A  66 44 39 08                     cmp word ptr [rax], r9w
008DEE9E  74 0A                           je 0x1408deeaa
008DEEA0  48 83 C0 02                     add rax, 2
008DEEA4  48 83 EA 01                     sub rdx, 1
008DEEA8  75 F0                           jne 0x1408dee9a
008DEEAA  48 8B C2                        mov rax, rdx
008DEEAD  B9 FF FF FF 7F                  mov ecx, 0x7fffffff
008DEEB2  48 F7 D8                        neg rax
008DEEB5  48 8B C2                        mov rax, rdx
008DEEB8  1B DB                           sbb ebx, ebx
008DEEBA  48 2B CA                        sub rcx, rdx
008DEEBD  F7 D3                           not ebx
008DEEBF  81 E3 0D 00 00 C0               and ebx, 0xc000000d
008DEEC5  48 F7 D8                        neg rax
008DEEC8  4D 1B C0                        sbb r8, r8
008DEECB  4C 23 C1                        and r8, rcx
008DEECE  48 85 D2                        test rdx, rdx
008DEED1  0F 84 98 03 00 00               je 0x1408df26f
008DEED7  4D 85 C0                        test r8, r8
008DEEDA  0F 84 A3 00 00 00               je 0x1408def83
008DEEE0  49 8D 48 01                     lea rcx, [r8 + 1]
008DEEE4  B8 02 00 00 00                  mov eax, 2
008DEEE9  48 F7 E1                        mul rcx
008DEEEC  48 8B F8                        mov rdi, rax
008DEEEF  48 85 D2                        test rdx, rdx
008DEEF2  0F 85 72 03 00 00               jne 0x1408df26a
008DEEF8  41 B8 50 6E 70 58               mov r8d, 0x58706e50
008DEEFE  48 8B D0                        mov rdx, rax
008DEF01  B9 00 01 00 00                  mov ecx, 0x100
008DEF06  E8 E5 31 2A 00                  call 0x140b820f0
008DEF0B  45 33 C9                        xor r9d, r9d
008DEF0E  48 89 46 18                     mov qword ptr [rsi + 0x18], rax
008DEF12  48 8B C8                        mov rcx, rax
008DEF15  48 85 C0                        test rax, rax
008DEF18  0F 84 98 03 00 00               je 0x1408df2b6
008DEF1E  48 D1 EF                        shr rdi, 1
008DEF21  48 8D 47 FF                     lea rax, [rdi - 1]
008DEF25  48 3D FE FF FF 7F               cmp rax, 0x7ffffffe
008DEF2B  0F 87 8C 03 00 00               ja 0x1408df2bd
008DEF31  BA FE FF FF 7F                  mov edx, 0x7ffffffe
008DEF36  4D 8B C4                        mov r8, r12
008DEF39  48 2B D7                        sub rdx, rdi
008DEF3C  4C 2B C1                        sub r8, rcx
008DEF3F  48 8D 04 3A                     lea rax, [rdx + rdi]
008DEF43  48 85 C0                        test rax, rax
008DEF46  74 17                           je 0x1408def5f
008DEF48  41 0F B7 04 08                  movzx eax, word ptr [r8 + rcx]
008DEF4D  66 85 C0                        test ax, ax
008DEF50  74 0D                           je 0x1408def5f
008DEF52  66 89 01                        mov word ptr [rcx], ax
008DEF55  48 83 C1 02                     add rcx, 2
008DEF59  48 83 EF 01                     sub rdi, 1
008DEF5D  75 E0                           jne 0x1408def3f
008DEF5F  48 85 FF                        test rdi, rdi
008DEF62  48 8D 41 FE                     lea rax, [rcx - 2]
008DEF66  48 0F 45 C1                     cmovne rax, rcx
008DEF6A  48 F7 DF                        neg rdi
008DEF6D  1B DB                           sbb ebx, ebx
008DEF6F  F7 D3                           not ebx
008DEF71  81 E3 05 00 00 80               and ebx, 0x80000005
008DEF77  66 44 89 08                     mov word ptr [rax], r9w
008DEF7B  85 DB                           test ebx, ebx
008DEF7D  0F 88 EC 02 00 00               js 0x1408df26f
008DEF83  85 DB                           test ebx, ebx
008DEF85  0F 88 87 01 00 00               js 0x1408df112
008DEF8B  44 39 6D 77                     cmp dword ptr [rbp + 0x77], r13d
008DEF8F  76 38                           jbe 0x1408defc9
008DEF91  44 8B 6D 77                     mov r13d, dword ptr [rbp + 0x77]
008DEF95  4D 85 FF                        test r15, r15
008DEF98  74 0D                           je 0x1408defa7
008DEF9A  BA 50 6E 70 58                  mov edx, 0x58706e50
008DEF9F  49 8B CF                        mov rcx, r15
008DEFA2  E8 C9 38 2A 00                  call 0x140b82870
008DEFA7  49 8B D5                        mov rdx, r13
008DEFAA  B9 00 01 00 00                  mov ecx, 0x100
008DEFAF  41 B8 50 6E 70 58               mov r8d, 0x58706e50
008DEFB5  E8 36 31 2A 00                  call 0x140b820f0
008DEFBA  45 33 C9                        xor r9d, r9d
008DEFBD  4C 8B F8                        mov r15, rax
008DEFC0  48 85 C0                        test rax, rax
008DEFC3  0F 84 C9 02 00 00               je 0x1408df292
008DEFC9  8B 5D 57                        mov ebx, dword ptr [rbp + 0x57]
008DEFCC  44 89 4D 77                     mov dword ptr [rbp + 0x77], r9d
008DEFD0  85 DB                           test ebx, ebx
008DEFD2  0F 84 4F 02 00 00               je 0x1408df227
008DEFD8  48 8B 45 5F                     mov rax, qword ptr [rbp + 0x5f]
008DEFDC  4C 8B 35 B5 73 58 00            mov r14, qword ptr [rip + 0x5873b5]
008DEFE3  48 83 65 F7 00                  and qword ptr [rbp - 9], 0
008DEFE8  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
008DEFEC  48 8B 45 67                     mov rax, qword ptr [rbp + 0x67]
008DEFF0  49 8B BE E8 01 00 00            mov rdi, qword ptr [r14 + 0x1e8]
008DEFF7  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
008DEFFB  48 8D 45 9F                     lea rax, [rbp - 0x61]
008DEFFF  48 89 45 D7                     mov qword ptr [rbp - 0x29], rax
008DF003  48 8D 45 77                     lea rax, [rbp + 0x77]
008DF007  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
008DF00B  4C 89 4D AF                     mov qword ptr [rbp - 0x51], r9
008DF00F  4C 89 4D B7                     mov qword ptr [rbp - 0x49], r9
008DF013  44 89 4D EB                     mov dword ptr [rbp - 0x15], r9d
008DF017  4C 89 65 C7                     mov qword ptr [rbp - 0x39], r12
008DF01B  4C 89 7D DF                     mov qword ptr [rbp - 0x21], r15
008DF01F  44 89 6D E7                     mov dword ptr [rbp - 0x19], r13d
008DF023  48 85 FF                        test rdi, rdi
008DF026  0F 84 FF 00 00 00               je 0x1408df12b
008DF02C  48 8B 55 4F                     mov rdx, qword ptr [rbp + 0x4f]
008DF030  48 8D 05 19 38 00 00            lea rax, [rip + 0x3819]
008DF037  48 3B F8                        cmp rdi, rax
008DF03A  41 B9 08 00 00 00               mov r9d, 8
008DF040  48 8D 45 AF                     lea rax, [rbp - 0x51]
008DF044  44 8B C3                        mov r8d, ebx
008DF047  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008DF04C  49 8B CE                        mov rcx, r14
008DF04F  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
008DF057  0F 85 77 02 00 00               jne 0x1408df2d4
008DF05D  E8 EE 37 00 00                  call 0x1408e2850
008DF062  3D 02 00 00 C0                  cmp eax, 0xc0000002
008DF067  0F 84 B3 01 00 00               je 0x1408df220
008DF06D  3D 20 01 00 C0                  cmp eax, 0xc0000120
008DF072  0F 85 AB 00 00 00               jne 0x1408df123
008DF078  8B 5D AF                        mov ebx, dword ptr [rbp - 0x51]
008DF07B  4C 8B 75 67                     mov r14, qword ptr [rbp + 0x67]
008DF07F  45 33 C9                        xor r9d, r9d
008DF082  81 FB 23 00 00 C0               cmp ebx, 0xc0000023
008DF088  0F 84 FD FE FF FF               je 0x1408def8b
008DF08E  85 DB                           test ebx, ebx
008DF090  78 6B                           js 0x1408df0fd
008DF092  8B 45 9F                        mov eax, dword ptr [rbp - 0x61]
008DF095  89 46 20                        mov dword ptr [rsi + 0x20], eax
008DF098  8B 45 77                        mov eax, dword ptr [rbp + 0x77]
008DF09B  89 46 24                        mov dword ptr [rsi + 0x24], eax
008DF09E  4C 89 7E 28                     mov qword ptr [rsi + 0x28], r15
008DF0A2  EB 08                           jmp 0x1408df0ac
008DF0A4  85 DB                           test ebx, ebx
008DF0A6  0F 88 5D 01 00 00               js 0x1408df209
008DF0AC  44 39 4E 20                     cmp dword ptr [rsi + 0x20], r9d
008DF0B0  0F 85 53 01 00 00               jne 0x1408df209
008DF0B6  48 8B 4E 18                     mov rcx, qword ptr [rsi + 0x18]
008DF0BA  48 85 C9                        test rcx, rcx
008DF0BD  74 0D                           je 0x1408df0cc
008DF0BF  BA 50 6E 70 58                  mov edx, 0x58706e50
008DF0C4  E8 A7 37 2A 00                  call 0x140b82870
008DF0C9  45 33 C9                        xor r9d, r9d
008DF0CC  48 8B 4E 28                     mov rcx, qword ptr [rsi + 0x28]
008DF0D0  48 85 C9                        test rcx, rcx
008DF0D3  74 0D                           je 0x1408df0e2
008DF0D5  BA 50 6E 70 58                  mov edx, 0x58706e50
008DF0DA  E8 91 37 2A 00                  call 0x140b82870
008DF0DF  45 33 C9                        xor r9d, r9d
008DF0E2  48 83 C8 FF                     or rax, 0xffffffffffffffff
008DF0E6  48 FF C0                        inc rax
008DF0E9  66 45 39 0C 44                  cmp word ptr [r12 + rax*2], r9w
008DF0EE  75 F6                           jne 0x1408df0e6
008DF0F0  4D 8D 24 44                     lea r12, [r12 + rax*2]
008DF0F4  49 83 C4 02                     add r12, 2
008DF0F8  E9 58 FD FF FF                  jmp 0x1408dee55
008DF0FD  4D 85 FF                        test r15, r15
008DF100  74 10                           je 0x1408df112
008DF102  BA 50 6E 70 58                  mov edx, 0x58706e50
008DF107  49 8B CF                        mov rcx, r15
008DF10A  E8 61 37 2A 00                  call 0x140b82870
008DF10F  45 33 C9                        xor r9d, r9d
008DF112  81 FB 25 02 00 C0               cmp ebx, 0xc0000225
008DF118  0F 85 79 01 00 00               jne 0x1408df297
008DF11E  41 8B D9                        mov ebx, r9d
008DF121  EB 89                           jmp 0x1408df0ac
008DF123  85 C0                           test eax, eax
008DF125  0F 85 35 01 00 00               jne 0x1408df260
008DF12B  8B 45 F7                        mov eax, dword ptr [rbp - 9]
008DF12E  44 8B C3                        mov r8d, ebx
008DF131  4C 8B 4D BF                     mov r9, qword ptr [rbp - 0x41]
008DF135  49 8B CE                        mov rcx, r14
008DF138  48 8B 55 4F                     mov rdx, qword ptr [rbp + 0x4f]
008DF13C  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
008DF140  48 8B 45 EF                     mov rax, qword ptr [rbp - 0x11]
008DF144  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
008DF149  8B 45 E7                        mov eax, dword ptr [rbp - 0x19]
008DF14C  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
008DF150  48 8B 45 DF                     mov rax, qword ptr [rbp - 0x21]
008DF154  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008DF159  48 8B 45 D7                     mov rax, qword ptr [rbp - 0x29]
008DF15D  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008DF162  48 8B 45 CF                     mov rax, qword ptr [rbp - 0x31]
008DF166  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008DF16B  48 8B 45 C7                     mov rax, qword ptr [rbp - 0x39]
008DF16F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008DF174  E8 97 26 00 00                  call 0x1408e1810
008DF179  8B D8                           mov ebx, eax
008DF17B  48 85 FF                        test rdi, rdi
008DF17E  0F 84 F7 FE FF FF               je 0x1408df07b
008DF184  44 8B 45 57                     mov r8d, dword ptr [rbp + 0x57]
008DF188  41 B9 08 00 00 00               mov r9d, 8
008DF18E  48 8B 55 4F                     mov rdx, qword ptr [rbp + 0x4f]
008DF192  49 8B CE                        mov rcx, r14
008DF195  89 45 AF                        mov dword ptr [rbp - 0x51], eax
008DF198  48 8D 05 B1 36 00 00            lea rax, [rip + 0x36b1]
008DF19F  48 3B F8                        cmp rdi, rax
008DF1A2  48 8D 45 AF                     lea rax, [rbp - 0x51]
008DF1A6  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008DF1AB  C7 44 24 20 02 00 00 00         mov dword ptr [rsp + 0x20], 2
008DF1B3  0F 85 28 01 00 00               jne 0x1408df2e1
008DF1B9  E8 92 36 00 00                  call 0x1408e2850
008DF1BE  3D 02 00 00 C0                  cmp eax, 0xc0000002
008DF1C3  0F 84 B2 FE FF FF               je 0x1408df07b
008DF1C9  3D 20 01 00 C0                  cmp eax, 0xc0000120
008DF1CE  0F 84 A4 FE FF FF               je 0x1408df078
008DF1D4  85 C0                           test eax, eax
008DF1D6  B8 E5 00 00 C0                  mov eax, 0xc00000e5
008DF1DB  0F 45 D8                        cmovne ebx, eax
008DF1DE  E9 98 FE FF FF                  jmp 0x1408df07b
008DF1E3  8B 45 6F                        mov eax, dword ptr [rbp + 0x6f]
008DF1E6  4C 8B 45 5F                     mov r8, qword ptr [rbp + 0x5f]
008DF1EA  8B 55 57                        mov edx, dword ptr [rbp + 0x57]
008DF1ED  48 8B 4D 4F                     mov rcx, qword ptr [rbp + 0x4f]
008DF1F1  48 89 74 24 30                  mov qword ptr [rsp + 0x30], rsi
008DF1F6  4C 89 4C 24 28                  mov qword ptr [rsp + 0x28], r9
008DF1FB  4D 8B CE                        mov r9, r14
008DF1FE  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008DF202  E8 89 0B 00 00                  call 0x1408dfd90
008DF207  8B D8                           mov ebx, eax
008DF209  8B C3                           mov eax, ebx
008DF20B  48 81 C4 C8 00 00 00            add rsp, 0xc8
008DF212  41 5F                           pop r15
008DF214  41 5E                           pop r14
008DF216  41 5D                           pop r13
008DF218  41 5C                           pop r12
008DF21A  5F                              pop rdi
008DF21B  5E                              pop rsi
008DF21C  5B                              pop rbx
008DF21D  5D                              pop rbp
008DF21E  C3                              ret
008DF21F  CC                              int3
008DF220  33 FF                           xor edi, edi
008DF222  E9 04 FF FF FF                  jmp 0x1408df12b
008DF227  48 8B 55 5F                     mov rdx, qword ptr [rbp + 0x5f]
008DF22B  48 8D 45 77                     lea rax, [rbp + 0x77]
008DF22F  48 8B 0D 62 71 58 00            mov rcx, qword ptr [rip + 0x587162]
008DF236  4D 8B CE                        mov r9, r14
008DF239  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008DF23E  4D 8B C4                        mov r8, r12
008DF241  44 89 6C 24 30                  mov dword ptr [rsp + 0x30], r13d
008DF246  48 8D 45 9F                     lea rax, [rbp - 0x61]
008DF24A  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
008DF24F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008DF254  E8 47 09 01 00                  call 0x1408efba0
008DF259  8B D8                           mov ebx, eax
008DF25B  E9 1F FE FF FF                  jmp 0x1408df07f
008DF260  BB E5 00 00 C0                  mov ebx, 0xc00000e5
008DF265  E9 11 FE FF FF                  jmp 0x1408df07b
008DF26A  BB 95 00 00 C0                  mov ebx, 0xc0000095
008DF26F  48 8B 4E 18                     mov rcx, qword ptr [rsi + 0x18]
008DF273  48 85 C9                        test rcx, rcx
008DF276  0F 84 07 FD FF FF               je 0x1408def83
008DF27C  BA 50 6E 70 58                  mov edx, 0x58706e50
008DF281  E8 EA 35 2A 00                  call 0x140b82870
008DF286  45 33 C9                        xor r9d, r9d
008DF289  4C 89 4E 18                     mov qword ptr [rsi + 0x18], r9
008DF28D  E9 F1 FC FF FF                  jmp 0x1408def83
008DF292  BB 9A 00 00 C0                  mov ebx, 0xc000009a
008DF297  48 8B 4E 18                     mov rcx, qword ptr [rsi + 0x18]
008DF29B  48 85 C9                        test rcx, rcx
008DF29E  0F 84 00 FE FF FF               je 0x1408df0a4
008DF2A4  BA 50 6E 70 58                  mov edx, 0x58706e50
008DF2A9  E8 C2 35 2A 00                  call 0x140b82870
008DF2AE  45 33 C9                        xor r9d, r9d
008DF2B1  E9 EE FD FF FF                  jmp 0x1408df0a4
008DF2B6  BB 9A 00 00 C0                  mov ebx, 0xc000009a
008DF2BB  EB B2                           jmp 0x1408df26f
008DF2BD  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008DF2C2  48 85 FF                        test rdi, rdi
008DF2C5  0F 84 B0 FC FF FF               je 0x1408def7b
008DF2CB  66 44 89 09                     mov word ptr [rcx], r9w
008DF2CF  E9 A7 FC FF FF                  jmp 0x1408def7b
008DF2D4  48 8B C7                        mov rax, rdi
008DF2D7  E8 F4 B7 DD FF                  call 0x1406baad0
008DF2DC  E9 81 FD FF FF                  jmp 0x1408df062
008DF2E1  48 8B C7                        mov rax, rdi
008DF2E4  E8 E7 B7 DD FF                  call 0x1406baad0
008DF2E9  E9 D0 FE FF FF                  jmp 0x1408df1be
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiDqPnPGetObjectPropertyInBestLocale(__int64 a1, int a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned int v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned int v_stack_mE8;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p38;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned int *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (200);
    a4 = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 127)) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 127) + 16) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 127) + 32) = v_xmm0;
loc_008DEE55:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 71 + 119))) == 0) goto loc_008DF1E3;
    *(unsigned int *)(v_rsp - 71 + 119) = 512;
    *(unsigned int *)(v_rsp - 71 - 97) = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 127)) = v_xmm0;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 127) + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)));
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 127) + 20) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 111)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 127) + 40) = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 127) + 24) = 0;
loc_008DEE9A:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 71 + 119))) == 0) goto loc_008DEEAA;
    result = (*(unsigned __int64 *)(v_rsp - 71 + 119)) + (2);
    a2 = ((unsigned int)(0x7FFFFFFFULL)) - (1);
    if (condition_is_not_equal) goto loc_008DEE9A;
loc_008DEEAA:
    result = -(a2);
    a1 = ((unsigned int)(0x7FFFFFFFULL)) - (a2);
    v_rbx = (unsigned int)(~(v_rbx));
    v_rbx = (unsigned int)((v_rbx) & (0xC000000DULL));
    result = -(a2);
    a3 = (a3) & (a1);
    if (a2 == 0) goto loc_008DF26F;
    if (a3 == 0) goto loc_008DEF83;
    if (a2 != 0) goto loc_008DF26A;
    result = ExAllocatePool2(256, 2, (unsigned int)(0x58706E50ULL), a4);
    a4 = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 127) + 24) = result;
    if (result == 0) goto loc_008DF2B6;
    v_rdi = (2) >> (1);
    if ((v_rdi - 1) > 0x7FFFFFFEULL) goto loc_008DF2BD;
    a2 = ((unsigned int)(0x7FFFFFFEULL)) - (v_rdi);
    a3 = (*(unsigned __int64 *)(v_rsp - 71 + 119)) - (result);
loc_008DEF3F:
    if (a2 + v_rdi * 1 == 0) goto loc_008DEF5F;
    if ((unsigned __int16)(*(unsigned __int16 *)(a3 + result * 1)) == 0) goto loc_008DEF5F;
    *(unsigned __int16 *)(result) = (unsigned __int16)(*(unsigned __int16 *)(a3 + result * 1));
    a1 = (result) + (2);
    v_rdi = (v_rdi) - (1);
    if (condition_is_not_equal) goto loc_008DEF3F;
loc_008DEF5F:
    result = a1 - 2;
    if (v_rdi != 0) { result = a1; }
    v_rdi = -(v_rdi);
    v_rbx = (unsigned int)(~(v_rbx));
    v_rbx = (unsigned int)((v_rbx) & (0x80000005ULL));
    *(unsigned __int16 *)(result) = 0;
loc_008DEF7B:
    if (sign_flag) goto loc_008DF26F;
loc_008DEF83:
    if (sign_flag) goto loc_008DF112;
loc_008DEF8B:
    if ((*(unsigned int *)(v_rsp - 71 + 119)) <= 0) goto loc_008DEFC9;
    if (0 != 0) {
        a2 = 0x58706E50ULL;
        a1 = 0;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    result = ExAllocatePool2(256, (unsigned int)(*(unsigned int *)(v_rsp - 71 + 119)), (unsigned int)(0x58706E50ULL), a4);
    a4 = 0;
    if (result == 0) goto loc_008DF292;
loc_008DEFC9:
    *(unsigned int *)(v_rsp - 71 + 119) = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 87))) == 0) goto loc_008DF227;
    *(unsigned __int64 *)(v_rsp - 71 - 65) = *(unsigned __int64 *)(v_rsp - 71 + 95);
    *(unsigned __int64 *)(v_rsp - 71 - 49) = *(unsigned __int64 *)(v_rsp - 71 + 103);
    *(unsigned __int64 *)(v_rsp - 71 - 41) = v_rsp - 71 - 97;
    *(unsigned __int64 *)(v_rsp - 71 - 17) = v_rsp - 71 + 119;
    *(unsigned __int64 *)(v_rsp - 71 - 81) = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 73) = 0;
    *(unsigned int *)(v_rsp - 71 - 21) = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 57) = *(unsigned __int64 *)(v_rsp - 71 + 119);
    *(unsigned __int64 *)(v_rsp - 71 - 33) = result;
    *(unsigned int *)(v_rsp - 71 - 25) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 119)));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5796789) + 488) == 0) goto loc_008DF12B;
    v_stack_mE0 = v_rsp - 71 - 81;
    v_stack_mE8 = 1;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5796789) + 488)) != (v_rip + 14361)) goto loc_008DF2D4;
    result = PiPnpRtlObjectActionCallback(*(unsigned __int64 *)(v_rip + 5796789), *(unsigned __int64 *)(v_rsp - 71 + 79), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 87)))), 8);
loc_008DF062:
    if (((unsigned int)(result)) == 0xC0000002ULL) goto loc_008DF220;
    if (((unsigned int)(result)) != 0xC0000120ULL) goto loc_008DF123;
loc_008DF078:
loc_008DF07B:
loc_008DF07F:
    a4 = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 81)))) == 0xC0000023ULL) goto loc_008DEF8B;
    if (sign_flag) goto loc_008DF0FD;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 127) + 32) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 97)));
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 127) + 36) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 119)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 127) + 40) = result;
    goto loc_008DF0AC;
loc_008DF0A4:
    if (sign_flag) goto loc_008DF209;
loc_008DF0AC:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 127) + 32)) != 0) goto loc_008DF209;
    result = (unsigned int)(*(unsigned int *)(v_rsp - 71 + 119));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 127) + 24) != 0) {
        a2 = 0x58706E50ULL;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 127) + 24), a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 87)))), a4);
        a4 = 0;
    }
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 127) + 40) != 0) {
        a2 = 0x58706E50ULL;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 127) + 40), a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 87)))), a4);
        a4 = 0;
    }
    result = (result) | (-1);
loc_008DF0E6:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 71 + 119) + result * 2)) != 0) goto loc_008DF0E6;
    v_r12 = (*(unsigned __int64 *)(v_rsp - 71 + 119) + result * 2) + (2);
    goto loc_008DEE55;
loc_008DF0FD:
    if (result != 0) {
        a2 = 0x58706E50ULL;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 87)))), a4);
        a4 = 0;
    }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 81)))) != 0xC0000225ULL) goto loc_008DF297;
    goto loc_008DF0AC;
loc_008DF123:
    if ((unsigned int)(result) != 0) goto loc_008DF260;
loc_008DF12B:
    v_stack_mB8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 9)));
    v_stack_mC0 = *(unsigned __int64 *)(v_rsp - 71 - 17);
    v_stack_mC8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 25)));
    v_stack_mD0 = *(unsigned __int64 *)(v_rsp - 71 - 33);
    v_stack_mD8 = *(unsigned __int64 *)(v_rsp - 71 - 41);
    v_stack_mE0 = *(unsigned __int64 *)(v_rsp - 71 - 49);
    v_stack_mE8 = *(unsigned __int64 *)(v_rsp - 71 - 57);
    result = PnpGetObjectPropertyWorker(*(unsigned __int64 *)(v_rsp - 71 + 103), *(unsigned __int64 *)(v_rsp - 71 + 79), 0, *(unsigned __int64 *)(v_rsp - 71 - 65));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5796789) + 488) == 0) goto loc_008DF07B;
    *(unsigned int *)(v_rsp - 71 - 81) = (unsigned int)(result);
    v_stack_mE0 = v_rsp - 71 - 81;
    v_stack_mE8 = 2;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5796789) + 488)) != (v_rip + 14001)) goto loc_008DF2E1;
    result = PiPnpRtlObjectActionCallback(*(unsigned __int64 *)(v_rsp - 71 + 103), *(unsigned __int64 *)(v_rsp - 71 + 79), (unsigned int)(*(unsigned int *)(v_rsp - 71 + 87)), 8);
loc_008DF1BE:
    if (((unsigned int)(result)) == 0xC0000002ULL) goto loc_008DF07B;
    if (((unsigned int)(result)) == 0xC0000120ULL) goto loc_008DF078;
    v_rbx = (unsigned int)((unsigned int)(result));
    if ((unsigned int)(result) != 0) { v_rbx = (unsigned int)((unsigned int)(0xC00000E5ULL)); }
    goto loc_008DF07B;
loc_008DF1E3:
    v_stack_mD8 = *(unsigned __int64 *)(v_rsp - 71 + 127);
    v_stack_mE0 = 8;
    v_stack_mE8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 111)));
    result = PiDqPnPGetObjectProperty(*(unsigned __int64 *)(v_rsp - 71 + 79), (unsigned int)(*(unsigned int *)(v_rsp - 71 + 87)), *(unsigned __int64 *)(v_rsp - 71 + 95), *(unsigned __int64 *)(v_rsp - 71 + 103));
loc_008DF209:
    v_rsp = (v_rsp) + (200);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_008DF220:
    v_rdi = 0;
    goto loc_008DF12B;
loc_008DF227:
    v_stack_p38 = v_rsp - 71 + 119;
    v_stack_p30 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 119)));
    v_stack_p28 = result;
    v_stack_p20 = v_rsp - 71 - 97;
    result = PnpGetGenericStoreProperty(*(unsigned __int64 *)(v_rip + 5796194), *(unsigned __int64 *)(v_rsp - 71 + 95), v_r12, *(unsigned __int64 *)(v_rsp - 71 + 103));
    goto loc_008DF07F;
loc_008DF260:
    goto loc_008DF07B;
loc_008DF26A:
loc_008DF26F:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 127) + 24) == 0) goto loc_008DEF83;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 127) + 24), (unsigned int)(0x58706E50ULL), v_r12, *(unsigned __int64 *)(v_rsp - 71 + 103));
    a4 = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 127) + 24) = 0;
    goto loc_008DEF83;
loc_008DF292:
loc_008DF297:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 127) + 24) == 0) goto loc_008DF0A4;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 127) + 24), (unsigned int)(0x58706E50ULL), v_r12, a4);
    a4 = 0;
    goto loc_008DF0A4;
loc_008DF2B6:
    goto loc_008DF26F;
loc_008DF2BD:
    if (0 == 0) goto loc_008DEF7B;
    *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 127) + 24)) = 0;
    goto loc_008DEF7B;
loc_008DF2D4:
    result = guard_dispatch_icall(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 127) + 24), (unsigned int)(0x58706E50ULL), v_r12, a4);
    goto loc_008DF062;
loc_008DF2E1:
    result = guard_dispatch_icall(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 127) + 24), (unsigned int)(0x58706E50ULL), v_r12, a4);
    goto loc_008DF1BE;
}
```

## 5. (Beta) C Style

```c
int64_t PiDqPnPGetObjectPropertyInBestLocale(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint32_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint32_t v_stack_mE8;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p30;
    uint64_t v_stack_p38;

    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint32_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (200);
    Arg4 = 0;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x7F)) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x7F) + 0x10) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x7F) + 0x20) = v_xmm0;
loc_008DEE55:
    if ((*(uint16_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x77))) == 0) goto loc_008DF1E3;
    *(uint32_t *)(local_rsp - 0x47 + 0x77) = 512;
    *(uint32_t *)(local_rsp - 0x47 - 0x61) = 0;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x7F)) = v_xmm0;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x7F) + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x10)));
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x7F) + 0x14) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x6F)));
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x7F) + 0x28) = 0;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x7F) + 0x18) = 0;
loc_008DEE9A:
    if ((*(uint16_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x77))) == 0) goto loc_008DEEAA;
    result = (*(uint64_t *)(local_rsp - 0x47 + 0x77)) + (2);
    Arg2 = ((uint32_t)(0x7FFFFFFFULL)) - (1);
    if (condition_is_not_equal) goto loc_008DEE9A;
loc_008DEEAA:
    result = -(Arg2);
    Arg1 = ((uint32_t)(0x7FFFFFFFULL)) - (Arg2);
    local_rbx = (uint32_t)(~(local_rbx));
    local_rbx = (uint32_t)((local_rbx) & (0xC000000DULL));
    result = -(Arg2);
    Arg3 = (Arg3) & (Arg1);
    if (Arg2 == 0) goto loc_008DF26F;
    if (Arg3 == 0) goto loc_008DEF83;
    if (Arg2 != 0) goto loc_008DF26A;
    result = ExAllocatePool2(256, 2, (uint32_t)(0x58706E50ULL), Arg4);
    Arg4 = 0;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x7F) + 0x18) = result;
    if (result == 0) goto loc_008DF2B6;
    local_rdi = (2) >> (1);
    if ((local_rdi - 1) > 0x7FFFFFFEULL) goto loc_008DF2BD;
    Arg2 = ((uint32_t)(0x7FFFFFFEULL)) - (local_rdi);
    Arg3 = (*(uint64_t *)(local_rsp - 0x47 + 0x77)) - (result);
loc_008DEF3F:
    if (Arg2 + local_rdi * 1 == 0) goto loc_008DEF5F;
    if ((uint16_t)(*(uint16_t *)(Arg3 + result * 1)) == 0) goto loc_008DEF5F;
    *(uint16_t *)(result) = (uint16_t)(*(uint16_t *)(Arg3 + result * 1));
    Arg1 = (result) + (2);
    local_rdi = (local_rdi) - (1);
    if (condition_is_not_equal) goto loc_008DEF3F;
loc_008DEF5F:
    result = Arg1 - 2;
    if (local_rdi != 0) { result = Arg1; }
    local_rdi = -(local_rdi);
    local_rbx = (uint32_t)(~(local_rbx));
    local_rbx = (uint32_t)((local_rbx) & (0x80000005ULL));
    *(uint16_t *)(result) = 0;
loc_008DEF7B:
    if (sign_flag) goto loc_008DF26F;
loc_008DEF83:
    if (sign_flag) goto loc_008DF112;
loc_008DEF8B:
    if ((*(uint32_t *)(local_rsp - 0x47 + 0x77)) <= 0) goto loc_008DEFC9;
    if (0 != 0) {
        Arg2 = 0x58706E50ULL;
        Arg1 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    result = ExAllocatePool2(256, (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x77)), (uint32_t)(0x58706E50ULL), Arg4);
    Arg4 = 0;
    if (result == 0) goto loc_008DF292;
loc_008DEFC9:
    *(uint32_t *)(local_rsp - 0x47 + 0x77) = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x57))) == 0) goto loc_008DF227;
    *(uint64_t *)(local_rsp - 0x47 - 0x41) = *(uint64_t *)(local_rsp - 0x47 + 0x5F);
    *(uint64_t *)(local_rsp - 0x47 - 0x31) = *(uint64_t *)(local_rsp - 0x47 + 0x67);
    *(uint64_t *)(local_rsp - 0x47 - 0x29) = local_rsp - 71 - 97;
    *(uint64_t *)(local_rsp - 0x47 - 0x11) = local_rsp - 71 + 119;
    *(uint64_t *)(local_rsp - 0x47 - 0x51) = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x49) = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x15) = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x39) = *(uint64_t *)(local_rsp - 0x47 + 0x77);
    *(uint64_t *)(local_rsp - 0x47 - 0x21) = result;
    *(uint32_t *)(local_rsp - 0x47 - 0x19) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x77)));
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x5873B5) + 0x1E8) == 0) goto loc_008DF12B;
    v_stack_mE0 = local_rsp - 71 - 81;
    v_stack_mE8 = 1;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x5873B5) + 0x1E8)) != (v_rip + 14361)) goto loc_008DF2D4;
    result = PiPnpRtlObjectActionCallback(*(uint64_t *)(v_rip + 0x5873B5), *(uint64_t *)(local_rsp - 0x47 + 0x4F), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x57)))), 8);
loc_008DF062:
    if (((uint32_t)(result)) == 0xC0000002ULL) goto loc_008DF220;
    if (((uint32_t)(result)) != 0xC0000120ULL) goto loc_008DF123;
loc_008DF078:
loc_008DF07B:
loc_008DF07F:
    Arg4 = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x51)))) == 0xC0000023ULL) goto loc_008DEF8B;
    if (sign_flag) goto loc_008DF0FD;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x7F) + 0x20) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x61)));
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x7F) + 0x24) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x77)));
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x7F) + 0x28) = result;
    goto loc_008DF0AC;
loc_008DF0A4:
    if (sign_flag) goto loc_008DF209;
loc_008DF0AC:
    if ((*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x7F) + 0x20)) != 0) goto loc_008DF209;
    result = (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x77));
    if (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x7F) + 0x18) != 0) {
        Arg2 = 0x58706E50ULL;
        result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x7F) + 0x18), Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x57)))), Arg4);
        Arg4 = 0;
    }
    if (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x7F) + 0x28) != 0) {
        Arg2 = 0x58706E50ULL;
        result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x7F) + 0x28), Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x57)))), Arg4);
        Arg4 = 0;
    }
    result = (result) | (-1);
loc_008DF0E6:
    result = (result) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x77) + result * 2)) != 0) goto loc_008DF0E6;
    local_r12 = (*(uint64_t *)(local_rsp - 0x47 + 0x77) + result * 2) + (2);
    goto loc_008DEE55;
loc_008DF0FD:
    if (result != 0) {
        Arg2 = 0x58706E50ULL;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x57)))), Arg4);
        Arg4 = 0;
    }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x51)))) != 0xC0000225ULL) goto loc_008DF297;
    goto loc_008DF0AC;
loc_008DF123:
    if ((uint32_t)(result) != 0) goto loc_008DF260;
loc_008DF12B:
    v_stack_mB8 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x9)));
    v_stack_mC0 = *(uint64_t *)(local_rsp - 0x47 - 0x11);
    v_stack_mC8 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x19)));
    v_stack_mD0 = *(uint64_t *)(local_rsp - 0x47 - 0x21);
    v_stack_mD8 = *(uint64_t *)(local_rsp - 0x47 - 0x29);
    v_stack_mE0 = *(uint64_t *)(local_rsp - 0x47 - 0x31);
    v_stack_mE8 = *(uint64_t *)(local_rsp - 0x47 - 0x39);
    result = PnpGetObjectPropertyWorker(*(uint64_t *)(local_rsp - 0x47 + 0x67), *(uint64_t *)(local_rsp - 0x47 + 0x4F), 0, *(uint64_t *)(local_rsp - 0x47 - 0x41));
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x5873B5) + 0x1E8) == 0) goto loc_008DF07B;
    *(uint32_t *)(local_rsp - 0x47 - 0x51) = (uint32_t)(result);
    v_stack_mE0 = local_rsp - 71 - 81;
    v_stack_mE8 = 2;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x5873B5) + 0x1E8)) != (v_rip + 14001)) goto loc_008DF2E1;
    result = PiPnpRtlObjectActionCallback(*(uint64_t *)(local_rsp - 0x47 + 0x67), *(uint64_t *)(local_rsp - 0x47 + 0x4F), (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x57)), 8);
loc_008DF1BE:
    if (((uint32_t)(result)) == 0xC0000002ULL) goto loc_008DF07B;
    if (((uint32_t)(result)) == 0xC0000120ULL) goto loc_008DF078;
    local_rbx = (uint32_t)((uint32_t)(result));
    if ((uint32_t)(result) != 0) { local_rbx = (uint32_t)((uint32_t)(0xC00000E5ULL)); }
    goto loc_008DF07B;
loc_008DF1E3:
    v_stack_mD8 = *(uint64_t *)(local_rsp - 0x47 + 0x7F);
    v_stack_mE0 = 8;
    v_stack_mE8 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x6F)));
    result = PiDqPnPGetObjectProperty(*(uint64_t *)(local_rsp - 0x47 + 0x4F), (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x57)), *(uint64_t *)(local_rsp - 0x47 + 0x5F), *(uint64_t *)(local_rsp - 0x47 + 0x67));
loc_008DF209:
    local_rsp = (local_rsp) + (200);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_008DF220:
    local_rdi = 0;
    goto loc_008DF12B;
loc_008DF227:
    v_stack_p38 = local_rsp - 71 + 119;
    v_stack_p30 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x77)));
    v_stack_p28 = result;
    v_stack_p20 = local_rsp - 71 - 97;
    result = PnpGetGenericStoreProperty(*(uint64_t *)(v_rip + 0x587162), *(uint64_t *)(local_rsp - 0x47 + 0x5F), local_r12, *(uint64_t *)(local_rsp - 0x47 + 0x67));
    goto loc_008DF07F;
loc_008DF260:
    goto loc_008DF07B;
loc_008DF26A:
loc_008DF26F:
    if (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x7F) + 0x18) == 0) goto loc_008DEF83;
    result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x7F) + 0x18), (uint32_t)(0x58706E50ULL), local_r12, *(uint64_t *)(local_rsp - 0x47 + 0x67));
    Arg4 = 0;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x7F) + 0x18) = 0;
    goto loc_008DEF83;
loc_008DF292:
loc_008DF297:
    if (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x7F) + 0x18) == 0) goto loc_008DF0A4;
    result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x7F) + 0x18), (uint32_t)(0x58706E50ULL), local_r12, Arg4);
    Arg4 = 0;
    goto loc_008DF0A4;
loc_008DF2B6:
    goto loc_008DF26F;
loc_008DF2BD:
    if (0 == 0) goto loc_008DEF7B;
    *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x7F) + 0x18)) = 0;
    goto loc_008DEF7B;
loc_008DF2D4:
    result = guard_dispatch_icall(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x7F) + 0x18), (uint32_t)(0x58706E50ULL), local_r12, Arg4);
    goto loc_008DF062;
loc_008DF2E1:
    result = guard_dispatch_icall(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x7F) + 0x18), (uint32_t)(0x58706E50ULL), local_r12, Arg4);
    goto loc_008DF1BE;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008DEE10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
