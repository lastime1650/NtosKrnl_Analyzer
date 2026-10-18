# PiDevCfgCheckDeviceNeedsUpdate

- RVA: `0x00731DDC`–`0x0073248A` (길이 `1,710` bytes)
- VA: `0x0000000140731DDC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BD468`
- 디코드: `428`개 명령, `1,710/1,710` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **27**; 고유 호출 대상: **16**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **9**

### Outgoing calls
- `0x00731E78` → [PiDevCfgFindDeviceDriver](../97/PiDevCfgFindDeviceDriver_function_0097602C.md) (function, `0x0097602C`)
- `0x00731ED8` → [CmGetDeviceRegProp](../8E/CmGetDeviceRegProp_function_008ED870.md) (function, `0x008ED870`)
- `0x00731F00` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00731F9D` → [PiDevCfgQueryObjectProperties](../97/PiDevCfgQueryObjectProperties_function_0097776C.md) (function, `0x0097776C`)
- `0x00731FB9` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00731FD5` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00731FE6` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00731FFB` → [PiDevCfgParseVersionString](PiDevCfgParseVersionString_function_00733FAC.md) (function, `0x00733FAC`)
- `0x0073200C` → [CmIsRootEnumeratedDevice](../8F/CmIsRootEnumeratedDevice_function_008F6E08.md) (function, `0x008F6E08`)
- `0x0073202B` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0073206B` → [PiDevCfgQueryObjectProperties](../97/PiDevCfgQueryObjectProperties_function_0097776C.md) (function, `0x0097776C`)
- `0x007320C8` → [PnpOpenObjectRegKey](../8E/PnpOpenObjectRegKey_function_008E15E8.md) (function, `0x008E15E8`)
- `0x007320F7` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x0073215C` → [RtlEqualUnicodeString](../93/RtlEqualUnicodeString_function_00932A20.md) (function, `0x00932A20`)
- `0x007321EA` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x0073220A` → [PiDevCfgSplitDriverConfigurationId](PiDevCfgSplitDriverConfigurationId_function_00736568.md) (function, `0x00736568`)
- `0x0073223E` → [RtlEqualUnicodeString](../93/RtlEqualUnicodeString_function_00932A20.md) (function, `0x00932A20`)
- `0x0073239F` → [PiDevCfgGetDriverPackageId](../97/PiDevCfgGetDriverPackageId_function_00977690.md) (function, `0x00977690`)
- `0x007323C3` → [PiDevCfgQueryDriverConfiguration](../97/PiDevCfgQueryDriverConfiguration_function_0097584C.md) (function, `0x0097584C`)
- `0x007323E4` → [PiDevCfgQueryDriverConfiguration](../97/PiDevCfgQueryDriverConfiguration_function_0097584C.md) (function, `0x0097584C`)
- `0x00732425` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x0073242E` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00732437` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00732440` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00732449` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00732458` → [PiDevCfgFreeDriverNode](PiDevCfgFreeDriverNode_function_00733354.md) (function, `0x00733354`)
- `0x00732469` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PiDevCfgInitDeviceCallback](PiDevCfgInitDeviceCallback_function_00733800.md) at `0x007338E6`
- [PiDevCfgProcessDeviceCallback](PiDevCfgProcessDeviceCallback_function_00734080.md) at `0x007341BB`
- [PpDevCfgCheckDeviceNeedsUpdate](PpDevCfgCheckDeviceNeedsUpdate_function_007367AC.md) at `0x007367F5`

### Static image references
- `0x00731DFB` → RVA `0x00E0A740` (`.data`; read)
- `0x00731EAA` → RVA `0x00E66398` (`.data`; read)
- `0x00731F09` → RVA `0x00012FA0` (`.rdata`; read)
- `0x00731F26` → RVA `0x00012F58` (`.rdata`; read)
- `0x00731F3E` → RVA `0x00012FB8` (`.rdata`; read)
- `0x00731F5D` → RVA `0x00027F08` (`.rdata`; read)
- `0x00732034` → RVA `0x00021140` (`.rdata`; read)
- `0x0073210E` → RVA `0x00E0A9E0` (`.data`; read)
- `0x00732384` → RVA `0x00FD8030` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **7**
  - `0x00731F00` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00731FB9` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00731FD5` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00731FE6` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x0073202B` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x007320F7` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00732469` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00731DDC  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00731DE1  55                              push rbp
00731DE2  56                              push rsi
00731DE3  57                              push rdi
00731DE4  41 54                           push r12
00731DE6  41 55                           push r13
00731DE8  41 56                           push r14
00731DEA  41 57                           push r15
00731DEC  48 8D AC 24 70 FF FF FF         lea rbp, [rsp - 0x90]
00731DF4  48 81 EC 90 01 00 00            sub rsp, 0x190
00731DFB  48 8B 05 3E 89 6D 00            mov rax, qword ptr [rip + 0x6d893e]
00731E02  48 33 C4                        xor rax, rsp
00731E05  48 89 85 80 00 00 00            mov qword ptr [rbp + 0x80], rax
00731E0C  45 33 ED                        xor r13d, r13d
00731E0F  C7 44 24 70 01 00 00 00         mov dword ptr [rsp + 0x70], 1
00731E17  44 89 2A                        mov dword ptr [rdx], r13d
00731E1A  4C 8D 44 24 40                  lea r8, [rsp + 0x40]
00731E1F  4C 8B E2                        mov r12, rdx
00731E22  44 89 6C 24 4C                  mov dword ptr [rsp + 0x4c], r13d
00731E27  0F 57 C0                        xorps xmm0, xmm0
00731E2A  4C 89 6C 24 60                  mov qword ptr [rsp + 0x60], r13
00731E2F  33 D2                           xor edx, edx
00731E31  4C 89 6C 24 68                  mov qword ptr [rsp + 0x68], r13
00731E36  48 8B F1                        mov rsi, rcx
00731E39  4C 89 6C 24 78                  mov qword ptr [rsp + 0x78], r13
00731E3E  41 8B DD                        mov ebx, r13d
00731E41  4C 89 6D 88                     mov qword ptr [rbp - 0x78], r13
00731E45  4C 89 6D 90                     mov qword ptr [rbp - 0x70], r13
00731E49  4C 89 6D 80                     mov qword ptr [rbp - 0x80], r13
00731E4D  4C 89 6D 98                     mov qword ptr [rbp - 0x68], r13
00731E51  4C 89 6D A0                     mov qword ptr [rbp - 0x60], r13
00731E55  0F 11 44 24 50                  movups xmmword ptr [rsp + 0x50], xmm0
00731E5A  4C 89 6D A8                     mov qword ptr [rbp - 0x58], r13
00731E5E  4C 89 6D B0                     mov qword ptr [rbp - 0x50], r13
00731E62  4C 89 6D B8                     mov qword ptr [rbp - 0x48], r13
00731E66  4C 89 6C 24 40                  mov qword ptr [rsp + 0x40], r13
00731E6B  44 89 6C 24 48                  mov dword ptr [rsp + 0x48], r13d
00731E70  4C 89 6D C0                     mov qword ptr [rbp - 0x40], r13
00731E74  4C 89 6D C8                     mov qword ptr [rbp - 0x38], r13
00731E78  E8 AF 41 24 00                  call 0x14097602c
00731E7D  8B F8                           mov edi, eax
00731E7F  B8 00 00 00 80                  mov eax, 0x80000000
00731E84  8D 0C 07                        lea ecx, [rdi + rax]
00731E87  85 C8                           test eax, ecx
00731E89  75 0C                           jne 0x140731e97
00731E8B  81 FF 90 04 00 C0               cmp edi, 0xc0000490
00731E91  0F 85 89 05 00 00               jne 0x140732420
00731E97  4C 8B 46 10                     mov r8, qword ptr [rsi + 0x10]
00731E9B  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00731EA0  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
00731EA4  41 BE 04 00 00 00               mov r14d, 4
00731EAA  48 8B 0D E7 44 73 00            mov rcx, qword ptr [rip + 0x7344e7]
00731EB1  44 89 6C 24 38                  mov dword ptr [rsp + 0x38], r13d
00731EB6  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00731EBB  48 8D 44 24 4C                  lea rax, [rsp + 0x4c]
00731EC0  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00731EC5  45 8D 4E 07                     lea r9d, [r14 + 7]
00731EC9  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00731ECE  44 89 74 24 48                  mov dword ptr [rsp + 0x48], r14d
00731ED3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00731ED8  E8 93 B9 1B 00                  call 0x1408ed870
00731EDD  85 C0                           test eax, eax
00731EDF  78 0E                           js 0x140731eef
00731EE1  44 39 74 24 70                  cmp dword ptr [rsp + 0x70], r14d
00731EE6  75 07                           jne 0x140731eef
00731EE8  44 39 74 24 48                  cmp dword ptr [rsp + 0x48], r14d
00731EED  74 05                           je 0x140731ef4
00731EEF  44 89 6C 24 4C                  mov dword ptr [rsp + 0x4c], r13d
00731EF4  33 D2                           xor edx, edx
00731EF6  48 8D 4D E0                     lea rcx, [rbp - 0x20]
00731EFA  41 B8 A0 00 00 00               mov r8d, 0xa0
00731F00  E8 3B 4D F9 FF                  call 0x1406c6c40
00731F05  4C 8B 4E 10                     mov r9, qword ptr [rsi + 0x10]
00731F09  48 8D 05 90 10 8E FF            lea rax, [rip - 0x71ef70]
00731F10  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
00731F14  B9 12 00 00 00                  mov ecx, 0x12
00731F19  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00731F1D  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00731F22  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00731F26  48 8D 05 2B 10 8E FF            lea rax, [rip - 0x71efd5]
00731F2D  48 89 45 08                     mov qword ptr [rbp + 8], rax
00731F31  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00731F36  48 89 45 18                     mov qword ptr [rbp + 0x18], rax
00731F3A  44 8D 79 F4                     lea r15d, [rcx - 0xc]
00731F3E  48 8D 05 73 10 8E FF            lea rax, [rip - 0x71ef8d]
00731F45  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
00731F4A  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
00731F4E  44 8D 41 EF                     lea r8d, [rcx - 0x11]
00731F52  48 8D 45 88                     lea rax, [rbp - 0x78]
00731F56  89 4D E8                        mov dword ptr [rbp - 0x18], ecx
00731F59  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
00731F5D  48 8D 05 A4 5F 8F FF            lea rax, [rip - 0x70a05c]
00731F64  48 89 45 58                     mov qword ptr [rbp + 0x58], rax
00731F68  48 8D 45 98                     lea rax, [rbp - 0x68]
00731F6C  48 89 45 68                     mov qword ptr [rbp + 0x68], rax
00731F70  48 8D 45 E0                     lea rax, [rbp - 0x20]
00731F74  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00731F79  44 89 7D FC                     mov dword ptr [rbp - 4], r15d
00731F7D  C7 45 10 10 00 00 00            mov dword ptr [rbp + 0x10], 0x10
00731F84  C7 45 20 08 00 00 00            mov dword ptr [rbp + 0x20], 8
00731F8B  89 4D 38                        mov dword ptr [rbp + 0x38], ecx
00731F8E  44 89 7D 4C                     mov dword ptr [rbp + 0x4c], r15d
00731F92  C7 45 60 12 20 00 00            mov dword ptr [rbp + 0x60], 0x2012
00731F99  44 89 7D 74                     mov dword ptr [rbp + 0x74], r15d
00731F9D  E8 CA 57 24 00                  call 0x14097776c
00731FA2  8B F8                           mov edi, eax
00731FA4  85 C0                           test eax, eax
00731FA6  0F 88 74 04 00 00               js 0x140732420
00731FAC  44 39 6D 00                     cmp dword ptr [rbp], r13d
00731FB0  7D 0C                           jge 0x140731fbe
00731FB2  33 D2                           xor edx, edx
00731FB4  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
00731FB9  E8 C2 87 CF FF                  call 0x14042a780
00731FBE  44 39 6D 28                     cmp dword ptr [rbp + 0x28], r13d
00731FC2  7D 05                           jge 0x140731fc9
00731FC4  4C 89 6C 24 78                  mov qword ptr [rsp + 0x78], r13
00731FC9  44 39 6D 50                     cmp dword ptr [rbp + 0x50], r13d
00731FCD  7D 0B                           jge 0x140731fda
00731FCF  33 D2                           xor edx, edx
00731FD1  48 8D 4D 88                     lea rcx, [rbp - 0x78]
00731FD5  E8 A6 87 CF FF                  call 0x14042a780
00731FDA  44 39 6D 78                     cmp dword ptr [rbp + 0x78], r13d
00731FDE  7D 0B                           jge 0x140731feb
00731FE0  33 D2                           xor edx, edx
00731FE2  48 8D 4D 98                     lea rcx, [rbp - 0x68]
00731FE6  E8 95 87 CF FF                  call 0x14042a780
00731FEB  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
00731FEF  48 85 C9                        test rcx, rcx
00731FF2  74 10                           je 0x140732004
00731FF4  4C 8D 45 80                     lea r8, [rbp - 0x80]
00731FF8  41 8B D6                        mov edx, r14d
00731FFB  E8 AC 1F 00 00                  call 0x140733fac
00732000  84 C0                           test al, al
00732002  75 04                           jne 0x140732008
00732004  4C 89 6D 80                     mov qword ptr [rbp - 0x80], r13
00732008  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
0073200C  E8 F7 4D 1C 00                  call 0x1408f6e08
00732011  41 BE 02 00 00 00               mov r14d, 2
00732017  84 C0                           test al, al
00732019  0F 84 04 01 00 00               je 0x140732123
0073201F  33 D2                           xor edx, edx
00732021  48 8D 4D E0                     lea rcx, [rbp - 0x20]
00732025  41 B8 A0 00 00 00               mov r8d, 0xa0
0073202B  E8 10 4C F9 FF                  call 0x1406c6c40
00732030  4C 8B 4E 10                     mov r9, qword ptr [rsi + 0x10]
00732034  48 8D 05 05 F1 8E FF            lea rax, [rip - 0x710efb]
0073203B  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
0073203F  45 8D 46 FF                     lea r8d, [r14 - 1]
00732043  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00732047  48 8D 45 A8                     lea rax, [rbp - 0x58]
0073204B  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0073204F  48 8D 45 E0                     lea rax, [rbp - 0x20]
00732053  C7 44 24 28 01 00 00 00         mov dword ptr [rsp + 0x28], 1
0073205B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00732060  C7 45 E8 12 20 00 00            mov dword ptr [rbp - 0x18], 0x2012
00732067  44 89 7D FC                     mov dword ptr [rbp - 4], r15d
0073206B  E8 FC 56 24 00                  call 0x14097776c
00732070  8B F8                           mov edi, eax
00732072  85 C0                           test eax, eax
00732074  0F 88 A6 03 00 00               js 0x140732420
0073207A  44 39 6D 00                     cmp dword ptr [rbp], r13d
0073207E  0F 8C 9F 00 00 00               jl 0x140732123
00732084  48 8B 75 B0                     mov rsi, qword ptr [rbp - 0x50]
00732088  48 85 F6                        test rsi, rsi
0073208B  0F 84 92 00 00 00               je 0x140732123
00732091  66 44 39 75 A8                  cmp word ptr [rbp - 0x58], r14w
00732096  0F 86 87 00 00 00               jbe 0x140732123
0073209C  0F B7 06                        movzx eax, word ptr [rsi]
0073209F  66 85 C0                        test ax, ax
007320A2  74 60                           je 0x140732104
007320A4  48 8B 0D ED 42 73 00            mov rcx, qword ptr [rip + 0x7342ed]
007320AB  48 8D 45 B8                     lea rax, [rbp - 0x48]
007320AF  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007320B4  41 B9 19 00 02 00               mov r9d, 0x20019
007320BA  41 B8 09 00 00 00               mov r8d, 9
007320C0  44 88 6C 24 20                  mov byte ptr [rsp + 0x20], r13b
007320C5  48 8B D6                        mov rdx, rsi
007320C8  E8 1B F5 1A 00                  call 0x1408e15e8
007320CD  8B F8                           mov edi, eax
007320CF  85 C0                           test eax, eax
007320D1  79 20                           jns 0x1407320f3
007320D3  41 8B FD                        mov edi, r13d
007320D6  48 83 C8 FF                     or rax, 0xffffffffffffffff
007320DA  48 FF C0                        inc rax
007320DD  66 44 39 2C 46                  cmp word ptr [rsi + rax*2], r13w
007320E2  75 F6                           jne 0x1407320da
007320E4  48 8D 34 46                     lea rsi, [rsi + rax*2]
007320E8  49 03 F6                        add rsi, r14
007320EB  66 44 39 2E                     cmp word ptr [rsi], r13w
007320EF  75 B3                           jne 0x1407320a4
007320F1  EB 11                           jmp 0x140732104
007320F3  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
007320F7  E8 B4 B1 F7 FF                  call 0x1406ad2b0
007320FC  0F B7 06                        movzx eax, word ptr [rsi]
007320FF  66 85 C0                        test ax, ax
00732102  75 1F                           jne 0x140732123
00732104  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00732109  48 85 C9                        test rcx, rcx
0073210C  75 1A                           jne 0x140732128
0073210E  8A 05 CC 88 6D 00               mov al, byte ptr [rip + 0x6d88cc]
00732114  F6 D8                           neg al
00732116  1B DB                           sbb ebx, ebx
00732118  81 E3 FE FF 03 00               and ebx, 0x3fffe
0073211E  41 03 DE                        add ebx, r14d
00732121  EB 05                           jmp 0x140732128
00732123  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00732128  F6 44 24 4C 40                  test byte ptr [rsp + 0x4c], 0x40
0073212D  74 0E                           je 0x14073213d
0073212F  48 85 C9                        test rcx, rcx
00732132  0F 84 78 02 00 00               je 0x1407323b0
00732138  E9 70 02 00 00                  jmp 0x1407323ad
0073213D  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
00732142  4D 85 C0                        test r8, r8
00732145  74 E8                           je 0x14073212f
00732147  48 85 C9                        test rcx, rcx
0073214A  0F 84 2B 02 00 00               je 0x14073237b
00732150  48 83 C1 28                     add rcx, 0x28
00732154  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
00732159  41 B0 01                        mov r8b, 1
0073215C  E8 BF 08 20 00                  call 0x140932a20
00732161  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00732166  84 C0                           test al, al
00732168  0F 84 08 02 00 00               je 0x140732376
0073216E  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
00732173  48 39 41 70                     cmp qword ptr [rcx + 0x70], rax
00732177  0F 85 30 02 00 00               jne 0x1407323ad
0073217D  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
00732181  48 39 41 78                     cmp qword ptr [rcx + 0x78], rax
00732185  0F 85 22 02 00 00               jne 0x1407323ad
0073218B  4C 8B 75 A0                     mov r14, qword ptr [rbp - 0x60]
0073218F  48 8D 81 D0 00 00 00            lea rax, [rcx + 0xd0]
00732196  4D 85 F6                        test r14, r14
00732199  74 0A                           je 0x1407321a5
0073219B  48 39 00                        cmp qword ptr [rax], rax
0073219E  75 17                           jne 0x1407321b7
007321A0  E9 08 02 00 00                  jmp 0x1407323ad
007321A5  48 39 00                        cmp qword ptr [rax], rax
007321A8  0F 85 FF 01 00 00               jne 0x1407323ad
007321AE  4D 85 F6                        test r14, r14
007321B1  0F 84 AC 01 00 00               je 0x140732363
007321B7  48 8D 44 24 50                  lea rax, [rsp + 0x50]
007321BC  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
007321C1  48 8D 44 24 50                  lea rax, [rsp + 0x50]
007321C6  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
007321CB  66 45 39 2E                     cmp word ptr [r14], r13w
007321CF  0F 84 1A 01 00 00               je 0x1407322ef
007321D5  48 8D 81 D0 00 00 00            lea rax, [rcx + 0xd0]
007321DC  48 39 00                        cmp qword ptr [rax], rax
007321DF  0F 84 04 01 00 00               je 0x1407322e9
007321E5  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
007321EA  E8 11 E6 28 00                  call 0x1409c0800
007321EF  48 8D 45 80                     lea rax, [rbp - 0x80]
007321F3  49 8B CE                        mov rcx, r14
007321F6  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007321FB  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
00732200  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00732205  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0073220A  E8 59 43 00 00                  call 0x140736568
0073220F  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00732214  85 C0                           test eax, eax
00732216  0F 88 CD 00 00 00               js 0x1407322e9
0073221C  48 8D 81 D0 00 00 00            lea rax, [rcx + 0xd0]
00732223  4C 8B 38                        mov r15, qword ptr [rax]
00732226  4C 3B F8                        cmp r15, rax
00732229  0F 84 BA 00 00 00               je 0x1407322e9
0073222F  49 8D 4F 28                     lea rcx, [r15 + 0x28]
00732233  41 B0 01                        mov r8b, 1
00732236  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
0073223B  49 8B F7                        mov rsi, r15
0073223E  E8 DD 07 20 00                  call 0x140932a20
00732243  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00732248  84 C0                           test al, al
0073224A  75 12                           jne 0x14073225e
0073224C  4D 8B 3F                        mov r15, qword ptr [r15]
0073224F  48 8D 81 D0 00 00 00            lea rax, [rcx + 0xd0]
00732256  49 8B F5                        mov rsi, r13
00732259  4C 3B F8                        cmp r15, rax
0073225C  75 D1                           jne 0x14073222f
0073225E  48 85 F6                        test rsi, rsi
00732261  0F 84 82 00 00 00               je 0x1407322e9
00732267  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
0073226C  48 39 46 70                     cmp qword ptr [rsi + 0x70], rax
00732270  75 77                           jne 0x1407322e9
00732272  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
00732276  48 39 46 78                     cmp qword ptr [rsi + 0x78], rax
0073227A  75 6D                           jne 0x1407322e9
0073227C  48 8B 06                        mov rax, qword ptr [rsi]
0073227F  48 39 70 08                     cmp qword ptr [rax + 8], rsi
00732283  0F 85 D3 00 00 00               jne 0x14073235c
00732289  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
0073228D  48 39 31                        cmp qword ptr [rcx], rsi
00732290  0F 85 C6 00 00 00               jne 0x14073235c
00732296  48 89 01                        mov qword ptr [rcx], rax
00732299  48 89 48 08                     mov qword ptr [rax + 8], rcx
0073229D  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
007322A2  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
007322A7  48 39 08                        cmp qword ptr [rax], rcx
007322AA  0F 85 AC 00 00 00               jne 0x14073235c
007322B0  48 89 46 08                     mov qword ptr [rsi + 8], rax
007322B4  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
007322B9  48 89 0E                        mov qword ptr [rsi], rcx
007322BC  48 89 30                        mov qword ptr [rax], rsi
007322BF  48 83 C8 FF                     or rax, 0xffffffffffffffff
007322C3  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
007322C8  48 FF C0                        inc rax
007322CB  66 45 39 2C 46                  cmp word ptr [r14 + rax*2], r13w
007322D0  75 F6                           jne 0x1407322c8
007322D2  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
007322D7  4D 8D 34 46                     lea r14, [r14 + rax*2]
007322DB  49 83 C6 02                     add r14, 2
007322DF  66 45 39 2E                     cmp word ptr [r14], r13w
007322E3  0F 85 EC FE FF FF               jne 0x1407321d5
007322E9  66 45 39 2E                     cmp word ptr [r14], r13w
007322ED  75 0C                           jne 0x1407322fb
007322EF  48 8D 81 D0 00 00 00            lea rax, [rcx + 0xd0]
007322F6  48 39 00                        cmp qword ptr [rax], rax
007322F9  74 03                           je 0x1407322fe
007322FB  83 CB 20                        or ebx, 0x20
007322FE  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
00732303  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00732308  48 3B D0                        cmp rdx, rax
0073230B  0F 84 9F 00 00 00               je 0x1407323b0
00732311  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00732316  48 39 42 08                     cmp qword ptr [rdx + 8], rax
0073231A  75 40                           jne 0x14073235c
0073231C  48 8B 02                        mov rax, qword ptr [rdx]
0073231F  48 39 50 08                     cmp qword ptr [rax + 8], rdx
00732323  75 37                           jne 0x14073235c
00732325  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0073232A  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
0073232F  48 89 48 08                     mov qword ptr [rax + 8], rcx
00732333  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00732338  48 05 D0 00 00 00               add rax, 0xd0
0073233E  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00732342  48 39 01                        cmp qword ptr [rcx], rax
00732345  75 15                           jne 0x14073235c
00732347  48 89 02                        mov qword ptr [rdx], rax
0073234A  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
0073234E  48 89 11                        mov qword ptr [rcx], rdx
00732351  48 89 50 08                     mov qword ptr [rax + 8], rdx
00732355  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
0073235A  EB A2                           jmp 0x1407322fe
0073235C  B9 03 00 00 00                  mov ecx, 3
00732361  CD 29                           int 0x29
00732363  44 38 2D 76 86 6D 00            cmp byte ptr [rip + 0x6d8676], r13b
0073236A  0F 84 AC 00 00 00               je 0x14073241c
00732370  0F BA EB 12                     bts ebx, 0x12
00732374  EB 3A                           jmp 0x1407323b0
00732376  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
0073237B  44 38 2D 5E 86 6D 00            cmp byte ptr [rip + 0x6d865e], r13b
00732382  74 29                           je 0x1407323ad
00732384  8B 05 A6 5C 8A 00               mov eax, dword ptr [rip + 0x8a5ca6]
0073238A  41 84 C6                        test r14b, al
0073238D  74 1E                           je 0x1407323ad
0073238F  0F BA EB 12                     bts ebx, 0x12
00732393  48 85 C9                        test rcx, rcx
00732396  74 18                           je 0x1407323b0
00732398  48 8D 55 C0                     lea rdx, [rbp - 0x40]
0073239C  49 8B C8                        mov rcx, r8
0073239F  E8 EC 52 24 00                  call 0x140977690
007323A4  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
007323A9  85 C0                           test eax, eax
007323AB  79 03                           jns 0x1407323b0
007323AD  83 CB 20                        or ebx, 0x20
007323B0  44 38 2D 29 86 6D 00            cmp byte ptr [rip + 0x6d8629], r13b
007323B7  74 63                           je 0x14073241c
007323B9  48 85 C9                        test rcx, rcx
007323BC  74 5E                           je 0x14073241c
007323BE  F6 C3 20                        test bl, 0x20
007323C1  74 59                           je 0x14073241c
007323C3  E8 84 34 24 00                  call 0x14097584c
007323C8  8B F8                           mov edi, eax
007323CA  85 C0                           test eax, eax
007323CC  78 34                           js 0x140732402
007323CE  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
007323D3  48 05 D0 00 00 00               add rax, 0xd0
007323D9  48 8B 30                        mov rsi, qword ptr [rax]
007323DC  48 3B F0                        cmp rsi, rax
007323DF  74 3B                           je 0x14073241c
007323E1  48 8B CE                        mov rcx, rsi
007323E4  E8 63 34 24 00                  call 0x14097584c
007323E9  8B F8                           mov edi, eax
007323EB  85 C0                           test eax, eax
007323ED  78 13                           js 0x140732402
007323EF  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
007323F4  48 8B 36                        mov rsi, qword ptr [rsi]
007323F7  48 05 D0 00 00 00               add rax, 0xd0
007323FD  48 3B F0                        cmp rsi, rax
00732400  75 DF                           jne 0x1407323e1
00732402  8B C7                           mov eax, edi
00732404  81 FF 93 04 00 C0               cmp edi, 0xc0000493
0073240A  75 0C                           jne 0x140732418
0073240C  83 E3 DF                        and ebx, 0xffffffdf
0073240F  41 8B FD                        mov edi, r13d
00732412  0F BA EB 12                     bts ebx, 0x12
00732416  EB 04                           jmp 0x14073241c
00732418  85 C0                           test eax, eax
0073241A  78 04                           js 0x140732420
0073241C  41 89 1C 24                     mov dword ptr [r12], ebx
00732420  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
00732425  E8 D6 E3 28 00                  call 0x1409c0800
0073242A  48 8D 4D 88                     lea rcx, [rbp - 0x78]
0073242E  E8 CD E3 28 00                  call 0x1409c0800
00732433  48 8D 4D 98                     lea rcx, [rbp - 0x68]
00732437  E8 C4 E3 28 00                  call 0x1409c0800
0073243C  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00732440  E8 BB E3 28 00                  call 0x1409c0800
00732445  48 8D 4D A8                     lea rcx, [rbp - 0x58]
00732449  E8 B2 E3 28 00                  call 0x1409c0800
0073244E  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00732453  48 85 C9                        test rcx, rcx
00732456  74 05                           je 0x14073245d
00732458  E8 F7 0E 00 00                  call 0x140733354
0073245D  8B C7                           mov eax, edi
0073245F  48 8B 8D 80 00 00 00            mov rcx, qword ptr [rbp + 0x80]
00732466  48 33 CC                        xor rcx, rsp
00732469  E8 D2 A1 F7 FF                  call 0x1406ac640
0073246E  48 8B 9C 24 E0 01 00 00         mov rbx, qword ptr [rsp + 0x1e0]
00732476  48 81 C4 90 01 00 00            add rsp, 0x190
0073247D  41 5F                           pop r15
0073247F  41 5E                           pop r14
00732481  41 5D                           pop r13
00732483  41 5C                           pop r12
00732485  5F                              pop rdi
00732486  5E                              pop rsi
00732487  5D                              pop rbp
00732488  C3                              ret
00732489  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiDevCfgCheckDeviceNeedsUpdate(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned int v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned int v_stack_m17C;
    unsigned int v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned int v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m50;
    unsigned int v_stack_m54;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned int v_stack_m7C;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_mA0;
    unsigned int v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned int v_stack_mCC;
    unsigned __int64 v_stack_mD8;
    unsigned int v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_p18;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (400);
    result = (*(unsigned __int64 *)(v_rip + 7178558)) ^ (v_rsp);
    v_stack_m48 = result;
    v_r13 = 0;
    v_stack_m158 = 1;
    *(unsigned int *)(a2) = 0;
    v_stack_m17C = 0;
    v_stack_m168 = 0;
    a2 = 0;
    v_stack_m160 = 0;
    v_stack_m150 = 0;
    v_stack_m140 = 0;
    v_stack_m138 = 0;
    v_stack_m148 = 0;
    v_stack_m130 = 0;
    v_stack_m128 = 0;
    v_stack_m178 = v_xmm0;
    v_stack_m120 = 0;
    v_stack_m118 = 0;
    v_stack_m110 = 0;
    v_stack_m188 = 0;
    v_stack_m180 = 0;
    v_stack_m108 = 0;
    v_stack_m100 = 0;
    result = PiDevCfgFindDeviceDriver(a1, a2, v_stack_m188, a4);
    if ((((unsigned int)((unsigned int)(0x80000000ULL))) & ((unsigned int)((unsigned int)((unsigned int)(result)) + (unsigned int)(0x80000000ULL) * 1))) != 0) goto loc_00731E97;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 0xC0000490ULL) goto loc_00732420;
loc_00731E97:
    v_stack_m190 = 0;
    v_stack_m198 = v_stack_m180;
    v_stack_m1A0 = v_stack_m17C;
    v_stack_m180 = 4;
    v_stack_m1A8 = v_stack_m158;
    result = CmGetDeviceRegProp(*(unsigned __int64 *)(v_rip + 7554279), *(unsigned __int64 *)(a1 + 8), *(unsigned __int64 *)(a1 + 16), 4 + 7);
    if (sign_flag) goto loc_00731EEF;
    if (v_stack_m158 != 4) goto loc_00731EEF;
    if (v_stack_m180 != 4) {
        v_stack_m17C = 0;
    }
    a2 = 0;
    result = memset(v_stack_mE8, a2, 160, 4 + 7);
    v_stack_mE8 = v_rip - 7466864;
    v_stack_mD8 = v_stack_m168;
    v_stack_mC0 = v_rip - 7466965;
    v_stack_mB0 = v_stack_m150;
    v_stack_m1A0 = 4;
    v_stack_m98 = v_rip - 7466893;
    v_stack_mE0 = 18;
    v_stack_m88 = v_stack_m140;
    v_stack_m70 = v_rip - 7381084;
    v_stack_m60 = v_stack_m130;
    v_stack_m1A8 = v_stack_mE8;
    v_stack_mCC = (unsigned int)(18 - 12);
    v_stack_mB8 = 16;
    v_stack_mA8 = 8;
    v_stack_m90 = 18;
    v_stack_m7C = (unsigned int)(18 - 12);
    v_stack_m68 = 0x2012ULL;
    v_stack_m54 = (unsigned int)(18 - 12);
    result = PiDevCfgQueryObjectProperties(18, *(unsigned __int64 *)(a1 + 8), 18 - 17, *(unsigned __int64 *)(a1 + 16));
    if (sign_flag) goto loc_00732420;
    if (v_stack_mC8 < 0) {
        a2 = 0;
        a1 = v_stack_m168;
        result = RtlInitUnicodeString(a1, a2, 18 - 17, *(unsigned __int64 *)(a1 + 16));
    }
    if (v_stack_mA0 < 0) {
        v_stack_m150 = 0;
    }
    if (v_stack_m78 < 0) {
        a2 = 0;
        a1 = v_stack_m140;
        result = RtlInitUnicodeString(a1, a2, 18 - 17, *(unsigned __int64 *)(a1 + 16));
    }
    if (v_stack_m50 < 0) {
        a2 = 0;
        a1 = v_stack_m130;
        result = RtlInitUnicodeString(a1, a2, 18 - 17, *(unsigned __int64 *)(a1 + 16));
    }
    if (v_stack_m138 == 0) goto loc_00732004;
    result = PiDevCfgParseVersionString(v_stack_m138, 4, v_stack_m148, *(unsigned __int64 *)(a1 + 16));
    if ((unsigned __int8)(result) == 0) {
        v_stack_m148 = 0;
    }
    result = CmIsRootEnumeratedDevice(*(unsigned __int64 *)(a1 + 8), 4, v_stack_m148, *(unsigned __int64 *)(a1 + 16));
    if ((unsigned __int8)(result) == 0) goto loc_00732123;
    a2 = 0;
    result = memset(v_stack_mE8, a2, 160, *(unsigned __int64 *)(a1 + 16));
    v_stack_mE8 = v_rip - 7409403;
    v_stack_mD8 = v_stack_m120;
    v_stack_m1A0 = 1;
    v_stack_m1A8 = v_stack_mE8;
    v_stack_mE0 = 0x2012ULL;
    v_stack_mCC = (unsigned int)(18 - 12);
    result = PiDevCfgQueryObjectProperties(v_stack_mE8, *(unsigned __int64 *)(a1 + 8), 2 - 1, *(unsigned __int64 *)(a1 + 16));
    if (sign_flag) goto loc_00732420;
    if (v_stack_mC8 < 0) goto loc_00732123;
    if (v_stack_m118 == 0) goto loc_00732123;
    if (v_stack_m120 <= 2) goto loc_00732123;
    if ((unsigned __int16)(*(unsigned __int16 *)(v_stack_m118)) == 0) goto loc_00732104;
loc_007320A4:
    v_stack_m1A0 = v_stack_m110;
    v_stack_m1A8 = 0;
    result = PnpOpenObjectRegKey(*(unsigned __int64 *)(v_rip + 7553773), v_stack_m118, 9, (unsigned int)(0x20019ULL));
    if (!sign_flag) goto loc_007320F3;
    result = (result) | (-1);
loc_007320DA:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(v_stack_m118 + result * 2)) != 0) goto loc_007320DA;
    v_rsi = (v_stack_m118 + result * 2) + (2);
    if ((*(unsigned __int16 *)(v_rsi)) != 0) goto loc_007320A4;
    goto loc_00732104;
loc_007320F3:
    result = ZwClose(v_stack_m110, v_stack_m118, 9, (unsigned int)(0x20019ULL));
    if ((unsigned __int16)(*(unsigned __int16 *)(v_rsi)) != 0) goto loc_00732123;
loc_00732104:
    if (v_stack_m188 != 0) goto loc_00732128;
    result = (unsigned __int8)(-(*(unsigned __int8 *)(v_rip + 7178444)));
    v_rbx = (unsigned int)((0) & (0x3FFFEULL));
    v_rbx = (unsigned int)((v_rbx) + (2));
    goto loc_00732128;
loc_00732123:
loc_00732128:
    if (((v_stack_m17C) & (64)) == 0) goto loc_0073213D;
loc_0073212F:
    if (v_stack_m188 == 0) goto loc_007323B0;
    goto loc_007323AD;
loc_0073213D:
    if (v_stack_m160 == 0) goto loc_0073212F;
    if (v_stack_m188 == 0) goto loc_0073237B;
    a1 = (v_stack_m188) + (40);
    result = RtlEqualUnicodeString(a1, v_stack_m168, 1, (unsigned int)(0x20019ULL));
    if ((unsigned __int8)(result) == 0) goto loc_00732376;
    if ((*(unsigned __int64 *)(v_stack_m188 + 112)) != v_stack_m150) goto loc_007323AD;
    if ((*(unsigned __int64 *)(v_stack_m188 + 120)) != v_stack_m148) goto loc_007323AD;
    if (v_stack_m128 == 0) goto loc_007321A5;
    if ((*(unsigned __int64 *)(v_stack_m188 + 208)) != (v_stack_m188 + 208)) goto loc_007321B7;
    goto loc_007323AD;
loc_007321A5:
    if ((*(unsigned __int64 *)(v_stack_m188 + 208)) != (v_stack_m188 + 208)) goto loc_007323AD;
    if (v_stack_m128 == 0) goto loc_00732363;
loc_007321B7:
    v_stack_m170 = v_stack_m178;
    v_stack_m178 = v_stack_m178;
    if ((*(unsigned __int16 *)(v_stack_m128)) == 0) goto loc_007322EF;
loc_007321D5:
    if ((*(unsigned __int64 *)(v_stack_m188 + 208)) == (v_stack_m188 + 208)) goto loc_007322E9;
    result = RtlFreeAnsiString(v_stack_m168, v_stack_m168, 1, (unsigned int)(0x20019ULL));
    v_stack_m1A0 = v_stack_m148;
    v_stack_m1A8 = v_stack_m150;
    result = PiDevCfgSplitDriverConfigurationId(v_stack_m128, v_stack_m168, 1, (unsigned int)(0x20019ULL));
    if (sign_flag) goto loc_007322E9;
    if ((*(unsigned __int64 *)(v_stack_m188 + 208)) == (v_stack_m188 + 208)) goto loc_007322E9;
loc_0073222F:
    result = RtlEqualUnicodeString(*(unsigned __int64 *)(v_stack_m188 + 208) + 40, v_stack_m168, 1, (unsigned int)(0x20019ULL));
    if ((unsigned __int8)(result) != 0) goto loc_0073225E;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m188 + 208))) != (v_stack_m188 + 208)) goto loc_0073222F;
loc_0073225E:
    if (0 == 0) goto loc_007322E9;
    if ((*(unsigned __int64 *)(0 + 112)) != v_stack_m150) goto loc_007322E9;
    if ((*(unsigned __int64 *)(0 + 120)) != v_stack_m148) goto loc_007322E9;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(0) + 8)) != 0) goto loc_0073235C;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(0 + 8))) != 0) goto loc_0073235C;
    *(unsigned __int64 *)(*(unsigned __int64 *)(0 + 8)) = *(unsigned __int64 *)(0);
    *(unsigned __int64 *)(*(unsigned __int64 *)(0) + 8) = *(unsigned __int64 *)(0 + 8);
    if ((*(unsigned __int64 *)(v_stack_m170)) != v_stack_m178) goto loc_0073235C;
    *(unsigned __int64 *)(0 + 8) = v_stack_m170;
    *(unsigned __int64 *)(0) = v_stack_m178;
    *(unsigned __int64 *)(v_stack_m170) = 0;
    result = (v_stack_m170) | (-1);
    v_stack_m170 = 0;
loc_007322C8:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(v_stack_m128 + result * 2)) != 0) goto loc_007322C8;
    v_r14 = (v_stack_m128 + result * 2) + (2);
    if ((*(unsigned __int16 *)(v_r14)) != 0) goto loc_007321D5;
loc_007322E9:
    if ((*(unsigned __int16 *)(v_r14)) != 0) goto loc_007322FB;
loc_007322EF:
    if ((*(unsigned __int64 *)(v_stack_m188 + 208)) != (v_stack_m188 + 208)) {
        v_rbx = (unsigned int)((v_rbx) | (32));
    }
    if (v_stack_m178 == v_stack_m178) goto loc_007323B0;
    if ((*(unsigned __int64 *)(v_stack_m178 + 8)) != v_stack_m178) goto loc_0073235C;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m178) + 8)) != v_stack_m178) goto loc_0073235C;
    v_stack_m178 = *(unsigned __int64 *)(v_stack_m178);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m178) + 8) = v_stack_m178;
    result = (v_stack_m188) + (208);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8))) != result) goto loc_0073235C;
    *(unsigned __int64 *)(v_stack_m178) = result;
    *(unsigned __int64 *)(v_stack_m178 + 8) = *(unsigned __int64 *)(result + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 8)) = v_stack_m178;
    *(unsigned __int64 *)(result + 8) = v_stack_m178;
    goto loc_007322FE;
loc_0073235C:
loc_00732363:
    if ((*(unsigned __int8 *)(v_rip + 7177846)) == 0) goto loc_0073241C;
    goto loc_007323B0;
loc_00732376:
loc_0073237B:
    if ((*(unsigned __int8 *)(v_rip + 7177822)) == 0) goto loc_007323AD;
    if ((((unsigned __int8)(v_r14)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9067686))))) == 0) goto loc_007323AD;
    if (3 == 0) goto loc_007323B0;
    result = PiDevCfgGetDriverPackageId(v_stack_m160, v_stack_m108, v_stack_m160, (unsigned int)(0x20019ULL));
    if (sign_flag) {
        v_rbx = (unsigned int)((v_rbx) | (32));
    }
    if ((*(unsigned __int8 *)(v_rip + 7177769)) == 0) goto loc_0073241C;
    if (v_stack_m188 == 0) goto loc_0073241C;
    if ((((unsigned __int8)(v_rbx)) & (32)) == 0) goto loc_0073241C;
    result = PiDevCfgQueryDriverConfiguration(v_stack_m188, v_stack_m108, v_stack_m160, (unsigned int)(0x20019ULL));
    if (sign_flag) goto loc_00732402;
    result = (v_stack_m188) + (208);
    if ((*(unsigned __int64 *)(result)) == result) goto loc_0073241C;
loc_007323E1:
    result = PiDevCfgQueryDriverConfiguration(*(unsigned __int64 *)(result), v_stack_m108, v_stack_m160, (unsigned int)(0x20019ULL));
    if (sign_flag) goto loc_00732402;
    result = (v_stack_m188) + (208);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result))) != result) goto loc_007323E1;
loc_00732402:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 0xC0000493ULL) goto loc_00732418;
    v_rbx = (unsigned int)((v_rbx) & (0xFFFFFFDFULL));
    goto loc_0073241C;
loc_00732418:
    if (!(sign_flag)) {
        *(unsigned int *)(a2) = (unsigned int)(v_rbx);
    }
    result = RtlFreeAnsiString(v_stack_m168, v_stack_m108, v_stack_m160, (unsigned int)(0x20019ULL));
    result = RtlFreeAnsiString(v_stack_m140, v_stack_m108, v_stack_m160, (unsigned int)(0x20019ULL));
    result = RtlFreeAnsiString(v_stack_m130, v_stack_m108, v_stack_m160, (unsigned int)(0x20019ULL));
    result = RtlFreeAnsiString(v_stack_m108, v_stack_m108, v_stack_m160, (unsigned int)(0x20019ULL));
    result = RtlFreeAnsiString(v_stack_m120, v_stack_m108, v_stack_m160, (unsigned int)(0x20019ULL));
    if (v_stack_m188 != 0) {
        result = PiDevCfgFreeDriverNode(v_stack_m188, v_stack_m108, v_stack_m160, (unsigned int)(0x20019ULL));
    }
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m108, v_stack_m160, (unsigned int)(0x20019ULL));
    v_rsp = (v_rsp) + (400);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PiDevCfgCheckDeviceNeedsUpdate(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint32_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint32_t v_stack_m17C;
    uint32_t v_stack_m180;
    uint64_t v_stack_m188;
    uint32_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m48;
    uint32_t v_stack_m50;
    uint32_t v_stack_m54;
    uint64_t v_stack_m60;
    uint32_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;
    uint32_t v_stack_m7C;
    uint64_t v_stack_m88;
    uint32_t v_stack_m90;
    uint64_t v_stack_m98;
    uint32_t v_stack_mA0;
    uint32_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint32_t v_stack_mCC;
    uint64_t v_stack_mD8;
    uint32_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_p18;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (400);
    result = (*(uint64_t *)(v_rip + 0x6D893E)) ^ (local_rsp);
    v_stack_m48 = result;
    local_r13 = 0;
    v_stack_m158 = 1;
    *(uint32_t *)(arg2) = 0;
    v_stack_m17C = 0;
    v_stack_m168 = 0;
    Arg2 = 0;
    v_stack_m160 = 0;
    v_stack_m150 = 0;
    v_stack_m140 = 0;
    v_stack_m138 = 0;
    v_stack_m148 = 0;
    v_stack_m130 = 0;
    v_stack_m128 = 0;
    v_stack_m178 = v_xmm0;
    v_stack_m120 = 0;
    v_stack_m118 = 0;
    v_stack_m110 = 0;
    v_stack_m188 = 0;
    v_stack_m180 = 0;
    v_stack_m108 = 0;
    v_stack_m100 = 0;
    result = PiDevCfgFindDeviceDriver(Arg1, Arg2, v_stack_m188, a4);
    if ((((uint32_t)((uint32_t)(0x80000000ULL))) & ((uint32_t)((uint32_t)((uint32_t)(result)) + (uint32_t)(0x80000000ULL) * 1))) != 0) goto loc_00731E97;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 0xC0000490ULL) goto loc_00732420;
loc_00731E97:
    v_stack_m190 = 0;
    v_stack_m198 = v_stack_m180;
    v_stack_m1A0 = v_stack_m17C;
    v_stack_m180 = 4;
    v_stack_m1A8 = v_stack_m158;
    result = CmGetDeviceRegProp(*(uint64_t *)(v_rip + 0x7344E7), *(uint64_t *)(arg1 + 0x8), *(uint64_t *)(arg1 + 0x10), 4 + 7);
    if (sign_flag) goto loc_00731EEF;
    if (v_stack_m158 != 4) goto loc_00731EEF;
    if (v_stack_m180 != 4) {
        v_stack_m17C = 0;
    }
    Arg2 = 0;
    result = memset(v_stack_mE8, Arg2, 160, 4 + 7);
    v_stack_mE8 = v_rip - 7466864;
    v_stack_mD8 = v_stack_m168;
    v_stack_mC0 = v_rip - 7466965;
    v_stack_mB0 = v_stack_m150;
    v_stack_m1A0 = 4;
    v_stack_m98 = v_rip - 7466893;
    v_stack_mE0 = 18;
    v_stack_m88 = v_stack_m140;
    v_stack_m70 = v_rip - 7381084;
    v_stack_m60 = v_stack_m130;
    v_stack_m1A8 = v_stack_mE8;
    v_stack_mCC = (uint32_t)(18 - 12);
    v_stack_mB8 = 16;
    v_stack_mA8 = 8;
    v_stack_m90 = 18;
    v_stack_m7C = (uint32_t)(18 - 12);
    v_stack_m68 = 0x2012ULL;
    v_stack_m54 = (uint32_t)(18 - 12);
    result = PiDevCfgQueryObjectProperties(18, *(uint64_t *)(arg1 + 0x8), 18 - 17, *(uint64_t *)(arg1 + 0x10));
    if (sign_flag) goto loc_00732420;
    if (v_stack_mC8 < 0) {
        Arg2 = 0;
        Arg1 = v_stack_m168;
        result = RtlInitUnicodeString(Arg1, Arg2, 18 - 17, *(uint64_t *)(arg1 + 0x10));
    }
    if (v_stack_mA0 < 0) {
        v_stack_m150 = 0;
    }
    if (v_stack_m78 < 0) {
        Arg2 = 0;
        Arg1 = v_stack_m140;
        result = RtlInitUnicodeString(Arg1, Arg2, 18 - 17, *(uint64_t *)(arg1 + 0x10));
    }
    if (v_stack_m50 < 0) {
        Arg2 = 0;
        Arg1 = v_stack_m130;
        result = RtlInitUnicodeString(Arg1, Arg2, 18 - 17, *(uint64_t *)(arg1 + 0x10));
    }
    if (v_stack_m138 == 0) goto loc_00732004;
    result = PiDevCfgParseVersionString(v_stack_m138, 4, v_stack_m148, *(uint64_t *)(arg1 + 0x10));
    if ((uint8_t)(result) == 0) {
        v_stack_m148 = 0;
    }
    result = CmIsRootEnumeratedDevice(*(uint64_t *)(arg1 + 0x8), 4, v_stack_m148, *(uint64_t *)(arg1 + 0x10));
    if ((uint8_t)(result) == 0) goto loc_00732123;
    Arg2 = 0;
    result = memset(v_stack_mE8, Arg2, 160, *(uint64_t *)(arg1 + 0x10));
    v_stack_mE8 = v_rip - 7409403;
    v_stack_mD8 = v_stack_m120;
    v_stack_m1A0 = 1;
    v_stack_m1A8 = v_stack_mE8;
    v_stack_mE0 = 0x2012ULL;
    v_stack_mCC = (uint32_t)(18 - 12);
    result = PiDevCfgQueryObjectProperties(v_stack_mE8, *(uint64_t *)(arg1 + 0x8), 2 - 1, *(uint64_t *)(arg1 + 0x10));
    if (sign_flag) goto loc_00732420;
    if (v_stack_mC8 < 0) goto loc_00732123;
    if (v_stack_m118 == 0) goto loc_00732123;
    if (v_stack_m120 <= 2) goto loc_00732123;
    if ((uint16_t)(*(uint16_t *)(v_stack_m118)) == 0) goto loc_00732104;
loc_007320A4:
    v_stack_m1A0 = v_stack_m110;
    v_stack_m1A8 = 0;
    result = PnpOpenObjectRegKey(*(uint64_t *)(v_rip + 0x7342ED), v_stack_m118, 9, (uint32_t)(0x20019ULL));
    if (!sign_flag) goto loc_007320F3;
    result = (result) | (-1);
loc_007320DA:
    result = (result) + 1;
    if ((*(uint16_t *)(v_stack_m118 + result * 2)) != 0) goto loc_007320DA;
    local_rsi = (v_stack_m118 + result * 2) + (2);
    if ((*(uint16_t *)(local_rsi)) != 0) goto loc_007320A4;
    goto loc_00732104;
loc_007320F3:
    result = ZwClose(v_stack_m110, v_stack_m118, 9, (uint32_t)(0x20019ULL));
    if ((uint16_t)(*(uint16_t *)(local_rsi)) != 0) goto loc_00732123;
loc_00732104:
    if (v_stack_m188 != 0) goto loc_00732128;
    result = (uint8_t)(-(*(uint8_t *)(v_rip + 0x6D88CC)));
    local_rbx = (uint32_t)((0) & (0x3FFFEULL));
    local_rbx = (uint32_t)((local_rbx) + (2));
    goto loc_00732128;
loc_00732123:
loc_00732128:
    if (((v_stack_m17C) & (64)) == 0) goto loc_0073213D;
loc_0073212F:
    if (v_stack_m188 == 0) goto loc_007323B0;
    goto loc_007323AD;
loc_0073213D:
    if (v_stack_m160 == 0) goto loc_0073212F;
    if (v_stack_m188 == 0) goto loc_0073237B;
    Arg1 = (v_stack_m188) + (40);
    result = RtlEqualUnicodeString(Arg1, v_stack_m168, 1, (uint32_t)(0x20019ULL));
    if ((uint8_t)(result) == 0) goto loc_00732376;
    if ((*(uint64_t *)(v_stack_m188 + 0x70)) != v_stack_m150) goto loc_007323AD;
    if ((*(uint64_t *)(v_stack_m188 + 0x78)) != v_stack_m148) goto loc_007323AD;
    if (v_stack_m128 == 0) goto loc_007321A5;
    if ((*(uint64_t *)(v_stack_m188 + 0xD0)) != (v_stack_m188 + 208)) goto loc_007321B7;
    goto loc_007323AD;
loc_007321A5:
    if ((*(uint64_t *)(v_stack_m188 + 0xD0)) != (v_stack_m188 + 208)) goto loc_007323AD;
    if (v_stack_m128 == 0) goto loc_00732363;
loc_007321B7:
    v_stack_m170 = v_stack_m178;
    v_stack_m178 = v_stack_m178;
    if ((*(uint16_t *)(v_stack_m128)) == 0) goto loc_007322EF;
loc_007321D5:
    if ((*(uint64_t *)(v_stack_m188 + 0xD0)) == (v_stack_m188 + 208)) goto loc_007322E9;
    result = RtlFreeAnsiString(v_stack_m168, v_stack_m168, 1, (uint32_t)(0x20019ULL));
    v_stack_m1A0 = v_stack_m148;
    v_stack_m1A8 = v_stack_m150;
    result = PiDevCfgSplitDriverConfigurationId(v_stack_m128, v_stack_m168, 1, (uint32_t)(0x20019ULL));
    if (sign_flag) goto loc_007322E9;
    if ((*(uint64_t *)(v_stack_m188 + 0xD0)) == (v_stack_m188 + 208)) goto loc_007322E9;
loc_0073222F:
    result = RtlEqualUnicodeString(*(uint64_t *)(v_stack_m188 + 0xD0) + 40, v_stack_m168, 1, (uint32_t)(0x20019ULL));
    if ((uint8_t)(result) != 0) goto loc_0073225E;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m188 + 0xD0))) != (v_stack_m188 + 208)) goto loc_0073222F;
loc_0073225E:
    if (0 == 0) goto loc_007322E9;
    if ((*(uint64_t *)(0 + 0x70)) != v_stack_m150) goto loc_007322E9;
    if ((*(uint64_t *)(0 + 0x78)) != v_stack_m148) goto loc_007322E9;
    if ((*(uint64_t *)(*(uint64_t *)(0) + 0x8)) != 0) goto loc_0073235C;
    if ((*(uint64_t *)(*(uint64_t *)(0 + 0x8))) != 0) goto loc_0073235C;
    *(uint64_t *)(*(uint64_t *)(0 + 0x8)) = *(uint64_t *)(0);
    *(uint64_t *)(*(uint64_t *)(0) + 0x8) = *(uint64_t *)(0 + 0x8);
    if ((*(uint64_t *)(v_stack_m170)) != v_stack_m178) goto loc_0073235C;
    *(uint64_t *)(0 + 0x8) = v_stack_m170;
    *(uint64_t *)(0) = v_stack_m178;
    *(uint64_t *)(v_stack_m170) = 0;
    result = (v_stack_m170) | (-1);
    v_stack_m170 = 0;
loc_007322C8:
    result = (result) + 1;
    if ((*(uint16_t *)(v_stack_m128 + result * 2)) != 0) goto loc_007322C8;
    local_r14 = (v_stack_m128 + result * 2) + (2);
    if ((*(uint16_t *)(local_r14)) != 0) goto loc_007321D5;
loc_007322E9:
    if ((*(uint16_t *)(local_r14)) != 0) goto loc_007322FB;
loc_007322EF:
    if ((*(uint64_t *)(v_stack_m188 + 0xD0)) != (v_stack_m188 + 208)) {
        local_rbx = (uint32_t)((local_rbx) | (32));
    }
    if (v_stack_m178 == v_stack_m178) goto loc_007323B0;
    if ((*(uint64_t *)(v_stack_m178 + 0x8)) != v_stack_m178) goto loc_0073235C;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m178) + 0x8)) != v_stack_m178) goto loc_0073235C;
    v_stack_m178 = *(uint64_t *)(v_stack_m178);
    *(uint64_t *)(*(uint64_t *)(v_stack_m178) + 0x8) = v_stack_m178;
    result = (v_stack_m188) + (208);
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x8))) != result) goto loc_0073235C;
    *(uint64_t *)(v_stack_m178) = result;
    *(uint64_t *)(v_stack_m178 + 0x8) = *(uint64_t *)(result + 0x8);
    *(uint64_t *)(*(uint64_t *)(result + 0x8)) = v_stack_m178;
    *(uint64_t *)(result + 0x8) = v_stack_m178;
    goto loc_007322FE;
loc_0073235C:
loc_00732363:
    if ((*(uint8_t *)(v_rip + 0x6D8676)) == 0) goto loc_0073241C;
    goto loc_007323B0;
loc_00732376:
loc_0073237B:
    if ((*(uint8_t *)(v_rip + 0x6D865E)) == 0) goto loc_007323AD;
    if ((((uint8_t)(local_r14)) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x8A5CA6))))) == 0) goto loc_007323AD;
    if (3 == 0) goto loc_007323B0;
    result = PiDevCfgGetDriverPackageId(v_stack_m160, v_stack_m108, v_stack_m160, (uint32_t)(0x20019ULL));
    if (sign_flag) {
        local_rbx = (uint32_t)((local_rbx) | (32));
    }
    if ((*(uint8_t *)(v_rip + 0x6D8629)) == 0) goto loc_0073241C;
    if (v_stack_m188 == 0) goto loc_0073241C;
    if ((((uint8_t)(local_rbx)) & (32)) == 0) goto loc_0073241C;
    result = PiDevCfgQueryDriverConfiguration(v_stack_m188, v_stack_m108, v_stack_m160, (uint32_t)(0x20019ULL));
    if (sign_flag) goto loc_00732402;
    result = (v_stack_m188) + (208);
    if ((*(uint64_t *)(result)) == result) goto loc_0073241C;
loc_007323E1:
    result = PiDevCfgQueryDriverConfiguration(*(uint64_t *)(result), v_stack_m108, v_stack_m160, (uint32_t)(0x20019ULL));
    if (sign_flag) goto loc_00732402;
    result = (v_stack_m188) + (208);
    if ((*(uint64_t *)(*(uint64_t *)(result))) != result) goto loc_007323E1;
loc_00732402:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 0xC0000493ULL) goto loc_00732418;
    local_rbx = (uint32_t)((local_rbx) & (0xFFFFFFDFULL));
    goto loc_0073241C;
loc_00732418:
    if (!(sign_flag)) {
        *(uint32_t *)(arg2) = (uint32_t)(local_rbx);
    }
    result = RtlFreeAnsiString(v_stack_m168, v_stack_m108, v_stack_m160, (uint32_t)(0x20019ULL));
    result = RtlFreeAnsiString(v_stack_m140, v_stack_m108, v_stack_m160, (uint32_t)(0x20019ULL));
    result = RtlFreeAnsiString(v_stack_m130, v_stack_m108, v_stack_m160, (uint32_t)(0x20019ULL));
    result = RtlFreeAnsiString(v_stack_m108, v_stack_m108, v_stack_m160, (uint32_t)(0x20019ULL));
    result = RtlFreeAnsiString(v_stack_m120, v_stack_m108, v_stack_m160, (uint32_t)(0x20019ULL));
    if (v_stack_m188 != 0) {
        result = PiDevCfgFreeDriverNode(v_stack_m188, v_stack_m108, v_stack_m160, (uint32_t)(0x20019ULL));
    }
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m108, v_stack_m160, (uint32_t)(0x20019ULL));
    local_rsp = (local_rsp) + (400);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg2` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00731DDC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
