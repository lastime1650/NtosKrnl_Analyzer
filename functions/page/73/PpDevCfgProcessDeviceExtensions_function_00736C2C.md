# PpDevCfgProcessDeviceExtensions

- RVA: `0x00736C2C`–`0x007373BA` (길이 `1,934` bytes)
- VA: `0x0000000140736C2C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C8D18`
- 디코드: `457`개 명령, `1,934/1,934` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **40**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x00736C70` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00736D28` → [PiDevCfgInitDeviceContext](../97/PiDevCfgInitDeviceContext_function_00977518.md) (function, `0x00977518`)
- `0x00736D80` → [PiDevCfgQueryObjectProperties](../97/PiDevCfgQueryObjectProperties_function_0097776C.md) (function, `0x0097776C`)
- `0x00736D9A` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00736DAC` → [PiDevCfgFindDeviceDriver](../97/PiDevCfgFindDeviceDriver_function_0097602C.md) (function, `0x0097602C`)
- `0x00736DDB` → [PiDevCfgQueryDriverConfiguration](../97/PiDevCfgQueryDriverConfiguration_function_0097584C.md) (function, `0x0097584C`)
- `0x00736E2C` → [PiDevCfgAppendMultiSz](PiDevCfgAppendMultiSz_function_00731B28.md) (function, `0x00731B28`)
- `0x00736E54` → [PiDevCfgAppendMultiSz](PiDevCfgAppendMultiSz_function_00731B28.md) (function, `0x00731B28`)
- `0x00736E7C` → [PiDevCfgAppendMultiSz](PiDevCfgAppendMultiSz_function_00731B28.md) (function, `0x00731B28`)
- `0x00736EA4` → [PiDevCfgAppendMultiSz](PiDevCfgAppendMultiSz_function_00731B28.md) (function, `0x00731B28`)
- `0x00736ECC` → [PiDevCfgAppendMultiSz](PiDevCfgAppendMultiSz_function_00731B28.md) (function, `0x00731B28`)
- `0x00736EF0` → [PiDevCfgAppendMultiSz](PiDevCfgAppendMultiSz_function_00731B28.md) (function, `0x00731B28`)
- `0x00736F10` → [PiDevCfgAppendMultiSz](PiDevCfgAppendMultiSz_function_00731B28.md) (function, `0x00731B28`)
- `0x00736F86` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x0073703B` → [PiDevCfgQueryObjectProperties](../97/PiDevCfgQueryObjectProperties_function_0097776C.md) (function, `0x0097776C`)
- `0x00737057` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00737069` → [PiDevCfgAppendMultiSz](PiDevCfgAppendMultiSz_function_00731B28.md) (function, `0x00731B28`)
- `0x007370C1` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x007370D5` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x0073711B` → [PiDevCfgConfigureDeviceDriver](../96/PiDevCfgConfigureDeviceDriver_function_00963ABC.md) (function, `0x00963ABC`)
- `0x00737188` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x007371D4` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x0073720C` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x00737252` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x00737281` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x007372D2` → [CmGetDeviceRegProp](../8E/CmGetDeviceRegProp_function_008ED870.md) (function, `0x008ED870`)
- `0x0073730F` → [PiDevCfgSetDeviceRegProp](../96/PiDevCfgSetDeviceRegProp_function_009635C0.md) (function, `0x009635C0`)
- `0x0073731E` → [PiDevCfgFreeDriverNode](PiDevCfgFreeDriverNode_function_00733354.md) (function, `0x00733354`)
- `0x00737327` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00737330` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00737339` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00737342` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x0073734B` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00737354` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x0073735D` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00737366` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00737370` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00737379` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00737382` → [PiDevCfgFreeDeviceContext](../70/PiDevCfgFreeDeviceContext_function_00704A00.md) (function, `0x00704A00`)
- `0x00737393` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PiConfigureDevice](../72/PiConfigureDevice_function_0072D38C.md) at `0x0072D3FB`

### Static image references
- `0x00736C52` → RVA `0x00E0A740` (`.data`; read)
- `0x00736C85` → RVA `0x00FD8054` (`PAGEDATA`; read)
- `0x00736D3B` → RVA `0x00012E80` (`.rdata`; read)
- `0x00736F61` → RVA `0x00012E50` (`.rdata`; read)
- `0x00736F6D` → RVA `0x00E66398` (`.data`; read)
- `0x00736FEE` → RVA `0x00FD86A8` (`PAGEDATA`; read)
- `0x007371AD` → RVA `0x000219F0` (`.rdata`; read)
- `0x00737234` → RVA `0x00027F08` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x00736C70` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00736D9A` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00737057` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00737393` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00736C2C  48 8B C4                        mov rax, rsp
00736C2F  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00736C33  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00736C37  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00736C3B  55                              push rbp
00736C3C  41 54                           push r12
00736C3E  41 55                           push r13
00736C40  41 56                           push r14
00736C42  41 57                           push r15
00736C44  48 8D A8 F8 FE FF FF            lea rbp, [rax - 0x108]
00736C4B  48 81 EC E0 01 00 00            sub rsp, 0x1e0
00736C52  48 8B 05 E7 3A 6D 00            mov rax, qword ptr [rip + 0x6d3ae7]
00736C59  48 33 C4                        xor rax, rsp
00736C5C  48 89 85 D8 00 00 00            mov qword ptr [rbp + 0xd8], rax
00736C63  33 D2                           xor edx, edx
00736C65  4C 8B F1                        mov r14, rcx
00736C68  48 8D 4D 50                     lea rcx, [rbp + 0x50]
00736C6C  44 8D 42 58                     lea r8d, [rdx + 0x58]
00736C70  E8 CB FF F8 FF                  call 0x1406c6c40
00736C75  33 FF                           xor edi, edi
00736C77  C7 44 24 70 01 00 00 00         mov dword ptr [rsp + 0x70], 1
00736C7F  33 C0                           xor eax, eax
00736C81  48 89 7D 88                     mov qword ptr [rbp - 0x78], rdi
00736C85  39 3D C9 13 8A 00               cmp dword ptr [rip + 0x8a13c9], edi
00736C8B  0F 57 C0                        xorps xmm0, xmm0
00736C8E  48 89 7D 90                     mov qword ptr [rbp - 0x70], rdi
00736C92  44 8B E7                        mov r12d, edi
00736C95  48 89 7C 24 68                  mov qword ptr [rsp + 0x68], rdi
00736C9A  44 8B EF                        mov r13d, edi
00736C9D  48 89 7D B8                     mov qword ptr [rbp - 0x48], rdi
00736CA1  44 8B FF                        mov r15d, edi
00736CA4  48 89 7D C0                     mov qword ptr [rbp - 0x40], rdi
00736CA8  48 89 7D F0                     mov qword ptr [rbp - 0x10], rdi
00736CAC  48 89 7D F8                     mov qword ptr [rbp - 8], rdi
00736CB0  48 89 7D 00                     mov qword ptr [rbp], rdi
00736CB4  48 89 7D 08                     mov qword ptr [rbp + 8], rdi
00736CB8  48 89 7D 10                     mov qword ptr [rbp + 0x10], rdi
00736CBC  48 89 7D 18                     mov qword ptr [rbp + 0x18], rdi
00736CC0  48 89 7D 20                     mov qword ptr [rbp + 0x20], rdi
00736CC4  48 89 7D 28                     mov qword ptr [rbp + 0x28], rdi
00736CC8  48 89 7D 30                     mov qword ptr [rbp + 0x30], rdi
00736CCC  48 89 7D 38                     mov qword ptr [rbp + 0x38], rdi
00736CD0  48 89 7D 98                     mov qword ptr [rbp - 0x68], rdi
00736CD4  48 89 7D A0                     mov qword ptr [rbp - 0x60], rdi
00736CD8  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
00736CDC  48 89 7D B0                     mov qword ptr [rbp - 0x50], rdi
00736CE0  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
00736CE5  48 89 7D 80                     mov qword ptr [rbp - 0x80], rdi
00736CE9  0F 11 85 B0 00 00 00            movups xmmword ptr [rbp + 0xb0], xmm0
00736CF0  48 89 85 D0 00 00 00            mov qword ptr [rbp + 0xd0], rax
00736CF7  0F 11 85 C0 00 00 00            movups xmmword ptr [rbp + 0xc0], xmm0
00736CFE  89 7C 24 60                     mov dword ptr [rsp + 0x60], edi
00736D02  89 7C 24 64                     mov dword ptr [rsp + 0x64], edi
00736D06  75 07                           jne 0x140736d0f
00736D08  8B DF                           mov ebx, edi
00736D0A  E9 14 06 00 00                  jmp 0x140737323
00736D0F  49 8B 4E 30                     mov rcx, qword ptr [r14 + 0x30]
00736D13  48 85 C9                        test rcx, rcx
00736D16  75 0A                           jne 0x140736d22
00736D18  BB 10 00 00 C0                  mov ebx, 0xc0000010
00736D1D  E9 01 06 00 00                  jmp 0x140737323
00736D22  4C 8D 45 50                     lea r8, [rbp + 0x50]
00736D26  33 D2                           xor edx, edx
00736D28  E8 EB 07 24 00                  call 0x140977518
00736D2D  8B D8                           mov ebx, eax
00736D2F  85 C0                           test eax, eax
00736D31  0F 88 DD 05 00 00               js 0x140737314
00736D37  48 8B 75 60                     mov rsi, qword ptr [rbp + 0x60]
00736D3B  48 8D 05 3E C1 8D FF            lea rax, [rip - 0x723ec2]
00736D42  49 8B 56 30                     mov rdx, qword ptr [r14 + 0x30]
00736D46  B9 01 00 00 00                  mov ecx, 1
00736D4B  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
00736D4F  4C 8B CE                        mov r9, rsi
00736D52  48 8D 45 88                     lea rax, [rbp - 0x78]
00736D56  89 4C 24 28                     mov dword ptr [rsp + 0x28], ecx
00736D5A  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
00736D5E  44 8B C1                        mov r8d, ecx
00736D61  48 8D 45 C8                     lea rax, [rbp - 0x38]
00736D65  48 C7 45 D0 12 20 00 00         mov qword ptr [rbp - 0x30], 0x2012
00736D6D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00736D72  89 7D E0                        mov dword ptr [rbp - 0x20], edi
00736D75  48 89 7D E8                     mov qword ptr [rbp - 0x18], rdi
00736D79  C7 45 E4 06 00 00 00            mov dword ptr [rbp - 0x1c], 6
00736D80  E8 E7 09 24 00                  call 0x14097776c
00736D85  8B D8                           mov ebx, eax
00736D87  85 C0                           test eax, eax
00736D89  0F 88 85 05 00 00               js 0x140737314
00736D8F  39 7D E8                        cmp dword ptr [rbp - 0x18], edi
00736D92  7D 0B                           jge 0x140736d9f
00736D94  33 D2                           xor edx, edx
00736D96  48 8D 4D 88                     lea rcx, [rbp - 0x78]
00736D9A  E8 E1 39 CF FF                  call 0x14042a780
00736D9F  48 8B 55 90                     mov rdx, qword ptr [rbp - 0x70]
00736DA3  4C 8D 44 24 68                  lea r8, [rsp + 0x68]
00736DA8  48 8D 4D 50                     lea rcx, [rbp + 0x50]
00736DAC  E8 7B F2 23 00                  call 0x14097602c
00736DB1  8B D8                           mov ebx, eax
00736DB3  85 C0                           test eax, eax
00736DB5  0F 88 59 05 00 00               js 0x140737314
00736DBB  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00736DC0  48 05 D0 00 00 00               add rax, 0xd0
00736DC6  48 8B 38                        mov rdi, qword ptr [rax]
00736DC9  48 3B F8                        cmp rdi, rax
00736DCC  0F 84 79 03 00 00               je 0x14073714b
00736DD2  41 BD 93 04 00 C0               mov r13d, 0xc0000493
00736DD8  48 8B CF                        mov rcx, rdi
00736DDB  E8 6C EA 23 00                  call 0x14097584c
00736DE0  8B D8                           mov ebx, eax
00736DE2  41 3B C5                        cmp eax, r13d
00736DE5  75 0C                           jne 0x140736df3
00736DE7  41 B1 01                        mov r9b, 1
00736DEA  48 8D 4D B8                     lea rcx, [rbp - 0x48]
00736DEE  E9 13 01 00 00                  jmp 0x140736f06
00736DF3  45 33 E4                        xor r12d, r12d
00736DF6  85 C0                           test eax, eax
00736DF8  0F 88 16 05 00 00               js 0x140737314
00736DFE  4C 39 A7 28 01 00 00            cmp qword ptr [rdi + 0x128], r12
00736E05  74 0C                           je 0x140736e13
00736E07  83 A7 B8 00 00 00 FE            and dword ptr [rdi + 0xb8], 0xfffffffe
00736E0E  E9 0C 01 00 00                  jmp 0x140736f1f
00736E13  4C 39 A7 38 01 00 00            cmp qword ptr [rdi + 0x138], r12
00736E1A  74 1F                           je 0x140736e3b
00736E1C  4C 8D 87 30 01 00 00            lea r8, [rdi + 0x130]
00736E23  45 33 C9                        xor r9d, r9d
00736E26  33 D2                           xor edx, edx
00736E28  48 8D 4D F0                     lea rcx, [rbp - 0x10]
00736E2C  E8 F7 AC FF FF                  call 0x140731b28
00736E31  8B D8                           mov ebx, eax
00736E33  85 C0                           test eax, eax
00736E35  0F 88 D9 04 00 00               js 0x140737314
00736E3B  4C 39 A7 48 01 00 00            cmp qword ptr [rdi + 0x148], r12
00736E42  74 1F                           je 0x140736e63
00736E44  4C 8D 87 40 01 00 00            lea r8, [rdi + 0x140]
00736E4B  45 33 C9                        xor r9d, r9d
00736E4E  33 D2                           xor edx, edx
00736E50  48 8D 4D 00                     lea rcx, [rbp]
00736E54  E8 CF AC FF FF                  call 0x140731b28
00736E59  8B D8                           mov ebx, eax
00736E5B  85 C0                           test eax, eax
00736E5D  0F 88 B1 04 00 00               js 0x140737314
00736E63  4C 39 A7 58 01 00 00            cmp qword ptr [rdi + 0x158], r12
00736E6A  74 1F                           je 0x140736e8b
00736E6C  4C 8D 87 50 01 00 00            lea r8, [rdi + 0x150]
00736E73  45 33 C9                        xor r9d, r9d
00736E76  33 D2                           xor edx, edx
00736E78  48 8D 4D 10                     lea rcx, [rbp + 0x10]
00736E7C  E8 A7 AC FF FF                  call 0x140731b28
00736E81  8B D8                           mov ebx, eax
00736E83  85 C0                           test eax, eax
00736E85  0F 88 89 04 00 00               js 0x140737314
00736E8B  4C 39 A7 68 01 00 00            cmp qword ptr [rdi + 0x168], r12
00736E92  74 1F                           je 0x140736eb3
00736E94  4C 8D 87 60 01 00 00            lea r8, [rdi + 0x160]
00736E9B  45 33 C9                        xor r9d, r9d
00736E9E  33 D2                           xor edx, edx
00736EA0  48 8D 4D 20                     lea rcx, [rbp + 0x20]
00736EA4  E8 7F AC FF FF                  call 0x140731b28
00736EA9  8B D8                           mov ebx, eax
00736EAB  85 C0                           test eax, eax
00736EAD  0F 88 61 04 00 00               js 0x140737314
00736EB3  4C 39 A7 78 01 00 00            cmp qword ptr [rdi + 0x178], r12
00736EBA  74 1F                           je 0x140736edb
00736EBC  4C 8D 87 70 01 00 00            lea r8, [rdi + 0x170]
00736EC3  45 33 C9                        xor r9d, r9d
00736EC6  33 D2                           xor edx, edx
00736EC8  48 8D 4D 30                     lea rcx, [rbp + 0x30]
00736ECC  E8 57 AC FF FF                  call 0x140731b28
00736ED1  8B D8                           mov ebx, eax
00736ED3  85 C0                           test eax, eax
00736ED5  0F 88 39 04 00 00               js 0x140737314
00736EDB  44 0B BF A0 01 00 00            or r15d, dword ptr [rdi + 0x1a0]
00736EE2  48 8D 57 28                     lea rdx, [rdi + 0x28]
00736EE6  45 33 C9                        xor r9d, r9d
00736EE9  48 8D 4D 98                     lea rcx, [rbp - 0x68]
00736EED  45 33 C0                        xor r8d, r8d
00736EF0  E8 33 AC FF FF                  call 0x140731b28
00736EF5  8B D8                           mov ebx, eax
00736EF7  85 C0                           test eax, eax
00736EF9  0F 88 15 04 00 00               js 0x140737314
00736EFF  45 33 C9                        xor r9d, r9d
00736F02  48 8D 4D A8                     lea rcx, [rbp - 0x58]
00736F06  45 33 C0                        xor r8d, r8d
00736F09  48 8D 97 A8 01 00 00            lea rdx, [rdi + 0x1a8]
00736F10  E8 13 AC FF FF                  call 0x140731b28
00736F15  8B D8                           mov ebx, eax
00736F17  85 C0                           test eax, eax
00736F19  0F 88 F5 03 00 00               js 0x140737314
00736F1F  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00736F24  48 8B 3F                        mov rdi, qword ptr [rdi]
00736F27  48 05 D0 00 00 00               add rax, 0xd0
00736F2D  48 3B F8                        cmp rdi, rax
00736F30  0F 85 A2 FE FF FF               jne 0x140736dd8
00736F36  33 FF                           xor edi, edi
00736F38  85 DB                           test ebx, ebx
00736F3A  0F 88 D4 03 00 00               js 0x140737314
00736F40  48 8B 4D C0                     mov rcx, qword ptr [rbp - 0x40]
00736F44  48 85 C9                        test rcx, rcx
00736F47  74 54                           je 0x140736f9d
00736F49  0F B7 45 B8                     movzx eax, word ptr [rbp - 0x48]
00736F4D  44 8D 4F 01                     lea r9d, [rdi + 1]
00736F51  4D 8B 46 30                     mov r8, qword ptr [r14 + 0x30]
00736F55  48 8D 55 50                     lea rdx, [rbp + 0x50]
00736F59  89 7C 24 50                     mov dword ptr [rsp + 0x50], edi
00736F5D  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00736F61  48 8D 05 E8 BE 8D FF            lea rax, [rip - 0x724118]
00736F68  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
00736F6D  48 8B 0D 24 F4 72 00            mov rcx, qword ptr [rip + 0x72f424]
00736F74  C7 44 24 38 12 20 00 00         mov dword ptr [rsp + 0x38], 0x2012
00736F7C  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00736F81  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00736F86  E8 C5 6B 35 00                  call 0x140a8db50
00736F8B  8B D8                           mov ebx, eax
00736F8D  85 C0                           test eax, eax
00736F8F  0F 88 7F 03 00 00               js 0x140737314
00736F95  41 8B DD                        mov ebx, r13d
00736F98  E9 77 03 00 00                  jmp 0x140737314
00736F9D  48 8D 45 F0                     lea rax, [rbp - 0x10]
00736FA1  44 8B E7                        mov r12d, edi
00736FA4  48 89 85 B0 00 00 00            mov qword ptr [rbp + 0xb0], rax
00736FAB  48 8D 45 00                     lea rax, [rbp]
00736FAF  48 89 85 B8 00 00 00            mov qword ptr [rbp + 0xb8], rax
00736FB6  48 8D 45 10                     lea rax, [rbp + 0x10]
00736FBA  48 89 85 C0 00 00 00            mov qword ptr [rbp + 0xc0], rax
00736FC1  48 8D 45 20                     lea rax, [rbp + 0x20]
00736FC5  48 89 85 C8 00 00 00            mov qword ptr [rbp + 0xc8], rax
00736FCC  48 8D 45 30                     lea rax, [rbp + 0x30]
00736FD0  48 89 85 D0 00 00 00            mov qword ptr [rbp + 0xd0], rax
00736FD7  4C 8B AC 3D B0 00 00 00         mov r13, qword ptr [rbp + rdi + 0xb0]
00736FDF  49 83 7D 08 00                  cmp qword ptr [r13 + 8], 0
00736FE4  0F 84 F0 00 00 00               je 0x1407370da
00736FEA  49 8B 56 30                     mov rdx, qword ptr [r14 + 0x30]
00736FEE  48 8D 05 B3 16 8A 00            lea rax, [rip + 0x8a16b3]
00736FF5  48 8B 04 07                     mov rax, qword ptr [rdi + rax]
00736FF9  4C 8B CE                        mov r9, rsi
00736FFC  83 65 D4 00                     and dword ptr [rbp - 0x2c], 0
00737000  41 B8 01 00 00 00               mov r8d, 1
00737006  83 65 E0 00                     and dword ptr [rbp - 0x20], 0
0073700A  48 83 65 E8 00                  and qword ptr [rbp - 0x18], 0
0073700F  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
00737013  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00737018  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
0073701C  48 8D 45 C8                     lea rax, [rbp - 0x38]
00737020  C7 44 24 28 01 00 00 00         mov dword ptr [rsp + 0x28], 1
00737028  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0073702D  C7 45 D0 12 20 00 00            mov dword ptr [rbp - 0x30], 0x2012
00737034  C7 45 E4 06 00 00 00            mov dword ptr [rbp - 0x1c], 6
0073703B  E8 2C 07 24 00                  call 0x14097776c
00737040  8B D8                           mov ebx, eax
00737042  85 C0                           test eax, eax
00737044  0F 88 CA 02 00 00               js 0x140737314
0073704A  83 7D E8 00                     cmp dword ptr [rbp - 0x18], 0
0073704E  7D 0C                           jge 0x14073705c
00737050  33 D2                           xor edx, edx
00737052  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
00737057  E8 24 37 CF FF                  call 0x14042a780
0073705C  45 33 C9                        xor r9d, r9d
0073705F  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
00737064  4D 8B C5                        mov r8, r13
00737067  33 D2                           xor edx, edx
00737069  E8 BA AA FF FF                  call 0x140731b28
0073706E  8B D8                           mov ebx, eax
00737070  85 C0                           test eax, eax
00737072  0F 88 9C 02 00 00               js 0x140737314
00737078  83 64 24 50 00                  and dword ptr [rsp + 0x50], 0
0073707D  48 8D 55 50                     lea rdx, [rbp + 0x50]
00737081  0F B7 44 24 78                  movzx eax, word ptr [rsp + 0x78]
00737086  41 B9 01 00 00 00               mov r9d, 1
0073708C  4D 8B 46 30                     mov r8, qword ptr [r14 + 0x30]
00737090  48 8B 0D 01 F3 72 00            mov rcx, qword ptr [rip + 0x72f301]
00737097  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
0073709B  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
0073709F  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
007370A4  48 8D 05 FD 15 8A 00            lea rax, [rip + 0x8a15fd]
007370AB  48 8B 04 07                     mov rax, qword ptr [rdi + rax]
007370AF  C7 44 24 38 12 20 00 00         mov dword ptr [rsp + 0x38], 0x2012
007370B7  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
007370BC  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
007370C1  E8 8A 6A 35 00                  call 0x140a8db50
007370C6  8B D8                           mov ebx, eax
007370C8  85 C0                           test eax, eax
007370CA  0F 88 44 02 00 00               js 0x140737314
007370D0  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
007370D5  E8 26 97 28 00                  call 0x1409c0800
007370DA  41 FF C4                        inc r12d
007370DD  48 83 C7 08                     add rdi, 8
007370E1  41 83 FC 05                     cmp r12d, 5
007370E5  0F 82 EC FE FF FF               jb 0x140736fd7
007370EB  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
007370F0  48 8D 81 D0 00 00 00            lea rax, [rcx + 0xd0]
007370F7  48 8B 38                        mov rdi, qword ptr [rax]
007370FA  EB 42                           jmp 0x14073713e
007370FC  8B 87 B8 00 00 00               mov eax, dword ptr [rdi + 0xb8]
00737102  A8 01                           test al, 1
00737104  74 2E                           je 0x140737134
00737106  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
0073710C  4C 8D 4C 24 60                  lea r9, [rsp + 0x60]
00737111  4C 8B C7                        mov r8, rdi
00737114  48 8D 55 50                     lea rdx, [rbp + 0x50]
00737118  49 8B CE                        mov rcx, r14
0073711B  E8 9C C9 22 00                  call 0x140963abc
00737120  8B D8                           mov ebx, eax
00737122  85 C0                           test eax, eax
00737124  0F 88 EA 01 00 00               js 0x140737314
0073712A  44 0B 7C 24 60                  or r15d, dword ptr [rsp + 0x60]
0073712F  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00737134  48 8B 3F                        mov rdi, qword ptr [rdi]
00737137  48 8D 81 D0 00 00 00            lea rax, [rcx + 0xd0]
0073713E  48 3B F8                        cmp rdi, rax
00737141  75 B9                           jne 0x1407370fc
00737143  4C 8B 65 A0                     mov r12, qword ptr [rbp - 0x60]
00737147  4C 8B 6D B0                     mov r13, qword ptr [rbp - 0x50]
0073714B  33 FF                           xor edi, edi
0073714D  48 39 7D 90                     cmp qword ptr [rbp - 0x70], rdi
00737151  74 3A                           je 0x14073718d
00737153  4D 8B 46 30                     mov r8, qword ptr [r14 + 0x30]
00737157  48 8D 05 22 BD 8D FF            lea rax, [rip - 0x7242de]
0073715E  48 8B 0D 33 F2 72 00            mov rcx, qword ptr [rip + 0x72f233]
00737165  44 8D 4F 01                     lea r9d, [rdi + 1]
00737169  89 7C 24 50                     mov dword ptr [rsp + 0x50], edi
0073716D  48 8D 55 50                     lea rdx, [rbp + 0x50]
00737171  89 7C 24 48                     mov dword ptr [rsp + 0x48], edi
00737175  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
0073717A  89 7C 24 38                     mov dword ptr [rsp + 0x38], edi
0073717E  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00737183  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00737188  E8 C3 69 35 00                  call 0x140a8db50
0073718D  4D 8B 46 30                     mov r8, qword ptr [r14 + 0x30]
00737191  48 8D 55 50                     lea rdx, [rbp + 0x50]
00737195  48 8B 0D FC F1 72 00            mov rcx, qword ptr [rip + 0x72f1fc]
0073719C  89 7C 24 50                     mov dword ptr [rsp + 0x50], edi
007371A0  4D 85 E4                        test r12, r12
007371A3  74 40                           je 0x1407371e5
007371A5  0F B7 45 98                     movzx eax, word ptr [rbp - 0x68]
007371A9  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
007371AD  48 8D 05 3C A8 8E FF            lea rax, [rip - 0x7157c4]
007371B4  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
007371B9  41 BC 01 00 00 00               mov r12d, 1
007371BF  C7 44 24 38 12 20 00 00         mov dword ptr [rsp + 0x38], 0x2012
007371C7  45 8B CC                        mov r9d, r12d
007371CA  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
007371CF  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
007371D4  E8 77 69 35 00                  call 0x140a8db50
007371D9  8B D8                           mov ebx, eax
007371DB  85 C0                           test eax, eax
007371DD  0F 88 31 01 00 00               js 0x140737314
007371E3  EB 2C                           jmp 0x140737211
007371E5  89 7C 24 48                     mov dword ptr [rsp + 0x48], edi
007371E9  48 8D 05 00 A8 8E FF            lea rax, [rip - 0x715800]
007371F0  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
007371F5  41 BC 01 00 00 00               mov r12d, 1
007371FB  89 7C 24 38                     mov dword ptr [rsp + 0x38], edi
007371FF  45 8B CC                        mov r9d, r12d
00737202  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00737207  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0073720C  E8 3F 69 35 00                  call 0x140a8db50
00737211  4D 8B 46 30                     mov r8, qword ptr [r14 + 0x30]
00737215  45 8B CC                        mov r9d, r12d
00737218  48 8B 0D 79 F1 72 00            mov rcx, qword ptr [rip + 0x72f179]
0073721F  48 8D 55 50                     lea rdx, [rbp + 0x50]
00737223  89 7C 24 50                     mov dword ptr [rsp + 0x50], edi
00737227  4D 85 ED                        test r13, r13
0073722A  74 37                           je 0x140737263
0073722C  0F B7 45 A8                     movzx eax, word ptr [rbp - 0x58]
00737230  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00737234  48 8D 05 CD 0C 8F FF            lea rax, [rip - 0x70f333]
0073723B  4C 89 6C 24 40                  mov qword ptr [rsp + 0x40], r13
00737240  C7 44 24 38 12 20 00 00         mov dword ptr [rsp + 0x38], 0x2012
00737248  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0073724D  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00737252  E8 F9 68 35 00                  call 0x140a8db50
00737257  8B D8                           mov ebx, eax
00737259  85 C0                           test eax, eax
0073725B  0F 88 B3 00 00 00               js 0x140737314
00737261  EB 23                           jmp 0x140737286
00737263  89 7C 24 48                     mov dword ptr [rsp + 0x48], edi
00737267  48 8D 05 9A 0C 8F FF            lea rax, [rip - 0x70f366]
0073726E  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
00737273  89 7C 24 38                     mov dword ptr [rsp + 0x38], edi
00737277  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0073727C  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00737281  E8 CA 68 35 00                  call 0x140a8db50
00737286  45 85 FF                        test r15d, r15d
00737289  0F 84 85 00 00 00               je 0x140737314
0073728F  49 8B 56 30                     mov rdx, qword ptr [r14 + 0x30]
00737293  48 8D 44 24 64                  lea rax, [rsp + 0x64]
00737298  48 8B 0D F9 F0 72 00            mov rcx, qword ptr [rip + 0x72f0f9]
0073729F  41 BC 04 00 00 00               mov r12d, 4
007372A5  89 7C 24 38                     mov dword ptr [rsp + 0x38], edi
007372A9  4C 8B C6                        mov r8, rsi
007372AC  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
007372B1  48 8D 44 24 60                  lea rax, [rsp + 0x60]
007372B6  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007372BB  48 8D 44 24 70                  lea rax, [rsp + 0x70]
007372C0  45 8D 6C 24 07                  lea r13d, [r12 + 7]
007372C5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007372CA  45 8B CD                        mov r9d, r13d
007372CD  44 89 64 24 64                  mov dword ptr [rsp + 0x64], r12d
007372D2  E8 99 65 1B 00                  call 0x1408ed870
007372D7  85 C0                           test eax, eax
007372D9  78 12                           js 0x1407372ed
007372DB  44 39 64 24 70                  cmp dword ptr [rsp + 0x70], r12d
007372E0  75 0B                           jne 0x1407372ed
007372E2  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
007372E6  44 39 64 24 64                  cmp dword ptr [rsp + 0x64], r12d
007372EB  74 02                           je 0x1407372ef
007372ED  8B C7                           mov eax, edi
007372EF  41 0B C7                        or eax, r15d
007372F2  44 89 64 24 28                  mov dword ptr [rsp + 0x28], r12d
007372F7  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
007372FB  48 8D 55 50                     lea rdx, [rbp + 0x50]
007372FF  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00737304  45 8B CC                        mov r9d, r12d
00737307  45 8B C5                        mov r8d, r13d
0073730A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0073730F  E8 AC C2 22 00                  call 0x1409635c0
00737314  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00737319  48 85 C9                        test rcx, rcx
0073731C  74 05                           je 0x140737323
0073731E  E8 31 C0 FF FF                  call 0x140733354
00737323  48 8D 4D 88                     lea rcx, [rbp - 0x78]
00737327  E8 D4 94 28 00                  call 0x1409c0800
0073732C  48 8D 4D F0                     lea rcx, [rbp - 0x10]
00737330  E8 CB 94 28 00                  call 0x1409c0800
00737335  48 8D 4D 00                     lea rcx, [rbp]
00737339  E8 C2 94 28 00                  call 0x1409c0800
0073733E  48 8D 4D 10                     lea rcx, [rbp + 0x10]
00737342  E8 B9 94 28 00                  call 0x1409c0800
00737347  48 8D 4D 20                     lea rcx, [rbp + 0x20]
0073734B  E8 B0 94 28 00                  call 0x1409c0800
00737350  48 8D 4D 30                     lea rcx, [rbp + 0x30]
00737354  E8 A7 94 28 00                  call 0x1409c0800
00737359  48 8D 4D 98                     lea rcx, [rbp - 0x68]
0073735D  E8 9E 94 28 00                  call 0x1409c0800
00737362  48 8D 4D A8                     lea rcx, [rbp - 0x58]
00737366  E8 95 94 28 00                  call 0x1409c0800
0073736B  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
00737370  E8 8B 94 28 00                  call 0x1409c0800
00737375  48 8D 4D B8                     lea rcx, [rbp - 0x48]
00737379  E8 82 94 28 00                  call 0x1409c0800
0073737E  48 8D 4D 50                     lea rcx, [rbp + 0x50]
00737382  E8 79 D6 FC FF                  call 0x140704a00
00737387  8B C3                           mov eax, ebx
00737389  48 8B 8D D8 00 00 00            mov rcx, qword ptr [rbp + 0xd8]
00737390  48 33 CC                        xor rcx, rsp
00737393  E8 A8 52 F7 FF                  call 0x1406ac640
00737398  4C 8D 9C 24 E0 01 00 00         lea r11, [rsp + 0x1e0]
007373A0  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
007373A4  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
007373A8  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
007373AC  49 8B E3                        mov rsp, r11
007373AF  41 5F                           pop r15
007373B1  41 5E                           pop r14
007373B3  41 5D                           pop r13
007373B5  41 5C                           pop r12
007373B7  5D                              pop rbp
007373B8  C3                              ret
007373B9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpDevCfgProcessDeviceExtensions(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m190;
    unsigned int v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned int v_stack_m1A4;
    unsigned int v_stack_m1A8;
    unsigned int v_stack_m1B8;
    unsigned int v_stack_m1C0;
    unsigned __int64 v_stack_m1C8;
    unsigned int v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned int v_stack_m1E0;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m28;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (480);
    result = (*(unsigned __int64 *)(v_rip + 7158503)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 264 + 216) = result;
    a2 = 0;
    result = memset(v_rsp - 264 + 80, a2, a2 + 88, a4);
    v_rdi = 0;
    v_stack_m198 = 1;
    result = 0;
    *(unsigned __int64 *)(v_rsp - 264 - 120) = 0;
    *(unsigned __int64 *)(v_rsp - 264 - 112) = 0;
    v_stack_m1A0 = 0;
    *(unsigned __int64 *)(v_rsp - 264 - 72) = 0;
    *(unsigned __int64 *)(v_rsp - 264 - 64) = 0;
    *(unsigned __int64 *)(v_rsp - 264 - 16) = 0;
    *(unsigned __int64 *)(v_rsp - 264 - 8) = 0;
    *(unsigned __int64 *)(v_rsp - 264) = 0;
    *(unsigned __int64 *)(v_rsp - 264 + 8) = 0;
    *(unsigned __int64 *)(v_rsp - 264 + 16) = 0;
    *(unsigned __int64 *)(v_rsp - 264 + 24) = 0;
    *(unsigned __int64 *)(v_rsp - 264 + 32) = 0;
    *(unsigned __int64 *)(v_rsp - 264 + 40) = 0;
    *(unsigned __int64 *)(v_rsp - 264 + 48) = 0;
    *(unsigned __int64 *)(v_rsp - 264 + 56) = 0;
    *(unsigned __int64 *)(v_rsp - 264 - 104) = 0;
    *(unsigned __int64 *)(v_rsp - 264 - 96) = 0;
    *(unsigned __int64 *)(v_rsp - 264 - 88) = 0;
    *(unsigned __int64 *)(v_rsp - 264 - 80) = 0;
    v_stack_m190 = 0;
    *(unsigned __int64 *)(v_rsp - 264 - 128) = 0;
    *(unsigned __int64 *)(v_rsp - 264 + 176) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 264 + 208) = 0;
    *(unsigned __int64 *)(v_rsp - 264 + 192) = v_xmm0;
    v_stack_m1A8 = 0;
    v_stack_m1A4 = 0;
    if ((*(unsigned int *)(v_rip + 9049033)) != 0) goto loc_00736D0F;
    goto loc_00737323;
loc_00736D0F:
    if (*(unsigned __int64 *)(a1 + 48) != 0) goto loc_00736D22;
    goto loc_00737323;
loc_00736D22:
    a2 = 0;
    result = PiDevCfgInitDeviceContext(*(unsigned __int64 *)(a1 + 48), a2, v_rsp - 264 + 80, a4);
    if (sign_flag) goto loc_00737314;
    *(unsigned __int64 *)(v_rsp - 264 - 56) = v_rip - 7487170;
    v_stack_m1E0 = 1;
    *(unsigned __int64 *)(v_rsp - 264 - 40) = v_rsp - 264 - 120;
    *(unsigned __int64 *)(v_rsp - 264 - 48) = 0x2012ULL;
    v_stack_m1E8 = v_rsp - 264 - 56;
    *(unsigned int *)(v_rsp - 264 - 32) = 0;
    *(unsigned __int64 *)(v_rsp - 264 - 24) = 0;
    *(unsigned int *)(v_rsp - 264 - 28) = 6;
    result = PiDevCfgQueryObjectProperties(1, *(unsigned __int64 *)(a1 + 48), 1, *(unsigned __int64 *)(v_rsp - 264 + 96));
    if (sign_flag) goto loc_00737314;
    if ((*(unsigned int *)(v_rsp - 264 - 24)) < 0) {
        a2 = 0;
        a1 = v_rsp - 264 - 120;
        result = RtlInitUnicodeString(a1, a2, 1, *(unsigned __int64 *)(v_rsp - 264 + 96));
    }
    result = PiDevCfgFindDeviceDriver(v_rsp - 264 + 80, *(unsigned __int64 *)(v_rsp - 264 - 112), v_stack_m1A0, *(unsigned __int64 *)(v_rsp - 264 + 96));
    if (sign_flag) goto loc_00737314;
    result = (v_stack_m1A0) + (208);
    if ((*(unsigned __int64 *)(result)) == result) goto loc_0073714B;
loc_00736DD8:
    result = PiDevCfgQueryDriverConfiguration(*(unsigned __int64 *)(result), *(unsigned __int64 *)(v_rsp - 264 - 112), v_stack_m1A0, *(unsigned __int64 *)(v_rsp - 264 + 96));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0xC0000493ULL)))) goto loc_00736DF3;
    goto loc_00736F06;
loc_00736DF3:
    v_r12 = 0;
    if (sign_flag) goto loc_00737314;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 296)) == 0) goto loc_00736E13;
    goto loc_00736F1F;
loc_00736E13:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 312)) == 0) goto loc_00736E3B;
    a4 = 0;
    a2 = 0;
    result = PiDevCfgAppendMultiSz(v_rsp - 264 - 16, a2, *(unsigned __int64 *)(result) + 304, a4);
    if (sign_flag) goto loc_00737314;
loc_00736E3B:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 328)) == 0) goto loc_00736E63;
    a4 = 0;
    a2 = 0;
    result = PiDevCfgAppendMultiSz(v_rsp - 264, a2, *(unsigned __int64 *)(result) + 320, a4);
    if (sign_flag) goto loc_00737314;
loc_00736E63:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 344)) == 0) goto loc_00736E8B;
    a4 = 0;
    a2 = 0;
    result = PiDevCfgAppendMultiSz(v_rsp - 264 + 16, a2, *(unsigned __int64 *)(result) + 336, a4);
    if (sign_flag) goto loc_00737314;
loc_00736E8B:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 360)) == 0) goto loc_00736EB3;
    a4 = 0;
    a2 = 0;
    result = PiDevCfgAppendMultiSz(v_rsp - 264 + 32, a2, *(unsigned __int64 *)(result) + 352, a4);
    if (sign_flag) goto loc_00737314;
loc_00736EB3:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 376)) == 0) goto loc_00736EDB;
    a4 = 0;
    a2 = 0;
    result = PiDevCfgAppendMultiSz(v_rsp - 264 + 48, a2, *(unsigned __int64 *)(result) + 368, a4);
    if (sign_flag) goto loc_00737314;
loc_00736EDB:
    v_r15 = (unsigned int)((0) | (*(unsigned int *)(*(unsigned __int64 *)(result) + 416)));
    a4 = 0;
    a3 = 0;
    result = PiDevCfgAppendMultiSz(v_rsp - 264 - 104, *(unsigned __int64 *)(result) + 40, a3, a4);
    if (sign_flag) goto loc_00737314;
    a4 = 0;
loc_00736F06:
    a3 = 0;
    result = PiDevCfgAppendMultiSz(v_rsp - 264 - 88, *(unsigned __int64 *)(result) + 424, a3, a4);
    if (sign_flag) goto loc_00737314;
loc_00736F1F:
    result = (v_stack_m1A0) + (208);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result))) != result) goto loc_00736DD8;
    v_rdi = 0;
    if (sign_flag) goto loc_00737314;
    if (*(unsigned __int64 *)(v_rsp - 264 - 64) == 0) goto loc_00736F9D;
    v_stack_m1B8 = 0;
    v_stack_m1C0 = (unsigned int)(*(unsigned __int16 *)(v_rsp - 264 - 72));
    v_stack_m1C8 = *(unsigned __int64 *)(v_rsp - 264 - 64);
    v_stack_m1D0 = 0x2012ULL;
    v_stack_m1D8 = v_rip - 7487768;
    v_stack_m1E8 = *(unsigned __int64 *)(v_rsp - 264 + 96);
    result = PiDevCfgSetObjectProperty(*(unsigned __int64 *)(v_rip + 7533604), v_rsp - 264 + 80, *(unsigned __int64 *)(a1 + 48), v_rdi + 1);
    if (sign_flag) goto loc_00737314;
    goto loc_00737314;
loc_00736F9D:
    *(unsigned __int64 *)(v_rsp - 264 + 176) = v_rsp - 264 - 16;
    *(unsigned __int64 *)(v_rsp - 264 + 184) = v_rsp - 264;
    *(unsigned __int64 *)(v_rsp - 264 + 192) = v_rsp - 264 + 16;
    *(unsigned __int64 *)(v_rsp - 264 + 200) = v_rsp - 264 + 32;
    *(unsigned __int64 *)(v_rsp - 264 + 208) = v_rsp - 264 + 48;
loc_00736FD7:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 264 + v_rdi * 1 + 176) + 8)) == 0) goto loc_007370DA;
    *(unsigned __int64 *)(v_rsp - 264 - 56) = *(unsigned __int64 *)(v_rdi + v_rip + 9049779 * 1);
    *(unsigned __int64 *)(v_rsp - 264 - 40) = v_stack_m190;
    v_stack_m1E0 = 1;
    v_stack_m1E8 = v_rsp - 264 - 56;
    *(unsigned int *)(v_rsp - 264 - 48) = 0x2012ULL;
    *(unsigned int *)(v_rsp - 264 - 28) = 6;
    result = PiDevCfgQueryObjectProperties(*(unsigned __int64 *)(v_rip + 7533604), *(unsigned __int64 *)(a1 + 48), 1, *(unsigned __int64 *)(v_rsp - 264 + 96));
    if (sign_flag) goto loc_00737314;
    if ((*(unsigned int *)(v_rsp - 264 - 24)) < 0) {
        a2 = 0;
        a1 = v_stack_m190;
        result = RtlInitUnicodeString(a1, a2, 1, *(unsigned __int64 *)(v_rsp - 264 + 96));
    }
    a4 = 0;
    a2 = 0;
    result = PiDevCfgAppendMultiSz(v_stack_m190, a2, *(unsigned __int64 *)(v_rsp - 264 + v_rdi * 1 + 176), a4);
    if (sign_flag) goto loc_00737314;
    v_stack_m1C0 = (unsigned int)(v_stack_m190);
    v_stack_m1C8 = *(unsigned __int64 *)(v_rsp - 264 - 128);
    v_stack_m1D0 = 0x2012ULL;
    v_stack_m1D8 = *(unsigned __int64 *)(v_rdi + v_rip + 9049597 * 1);
    v_stack_m1E8 = *(unsigned __int64 *)(v_rsp - 264 + 96);
    result = PiDevCfgSetObjectProperty(*(unsigned __int64 *)(v_rip + 7533313), v_rsp - 264 + 80, *(unsigned __int64 *)(a1 + 48), 1);
    if (sign_flag) goto loc_00737314;
    result = RtlFreeAnsiString(v_stack_m190, v_rsp - 264 + 80, *(unsigned __int64 *)(a1 + 48), 1);
loc_007370DA:
    v_r12 = (unsigned int)((0) + 1);
    v_rdi = (v_rdi) + (8);
    if (((unsigned int)(v_r12)) < 5) goto loc_00736FD7;
    goto loc_0073713E;
loc_007370FC:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m1A0 + 208) + 184)))) & (1)) == 0) goto loc_00737134;
    result = PiDevCfgConfigureDeviceDriver(a1, v_rsp - 264 + 80, *(unsigned __int64 *)(v_stack_m1A0 + 208), v_stack_m1A8);
    if (sign_flag) goto loc_00737314;
    v_r15 = (unsigned int)((v_r15) | (v_stack_m1A8));
loc_00737134:
loc_0073713E:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m1A0 + 208))) != (v_stack_m1A0 + 208)) goto loc_007370FC;
loc_0073714B:
    v_rdi = 0;
    result = v_stack_m1A0 + 208;
    if ((*(unsigned __int64 *)(v_rsp - 264 - 112)) != 0) {
        a3 = *(unsigned __int64 *)(a1 + 48);
        result = v_rip - 7488222;
        a1 = *(unsigned __int64 *)(v_rip + 7533107);
        a4 = v_rdi + 1;
        v_stack_m1B8 = 0;
        a2 = v_rsp - 264 + 80;
        v_stack_m1C0 = 0;
        v_stack_m1C8 = 0;
        v_stack_m1D0 = 0;
        v_stack_m1D8 = result;
        v_stack_m1E8 = *(unsigned __int64 *)(v_rsp - 264 + 96);
        result = PiDevCfgSetObjectProperty(a1, a2, a3, a4);
    }
    v_stack_m1B8 = 0;
    if (*(unsigned __int64 *)(v_rsp - 264 - 96) == 0) goto loc_007371E5;
    v_stack_m1C0 = (unsigned int)(*(unsigned __int16 *)(v_rsp - 264 - 104));
    v_stack_m1C8 = *(unsigned __int64 *)(v_rsp - 264 - 96);
    v_stack_m1D0 = 0x2012ULL;
    v_stack_m1D8 = v_rip - 7428036;
    v_stack_m1E8 = *(unsigned __int64 *)(v_rsp - 264 + 96);
    result = PiDevCfgSetObjectProperty(*(unsigned __int64 *)(v_rip + 7533052), v_rsp - 264 + 80, *(unsigned __int64 *)(a1 + 48), 1);
    if (sign_flag) goto loc_00737314;
    goto loc_00737211;
loc_007371E5:
    v_stack_m1C0 = 0;
    v_stack_m1C8 = 0;
    v_stack_m1D0 = 0;
    v_stack_m1D8 = v_rip - 7428096;
    v_stack_m1E8 = *(unsigned __int64 *)(v_rsp - 264 + 96);
    result = PiDevCfgSetObjectProperty(*(unsigned __int64 *)(v_rip + 7533052), v_rsp - 264 + 80, *(unsigned __int64 *)(a1 + 48), 1);
loc_00737211:
    v_stack_m1B8 = 0;
    if (*(unsigned __int64 *)(v_rsp - 264 - 80) == 0) goto loc_00737263;
    v_stack_m1C0 = (unsigned int)(*(unsigned __int16 *)(v_rsp - 264 - 88));
    v_stack_m1C8 = *(unsigned __int64 *)(v_rsp - 264 - 80);
    v_stack_m1D0 = 0x2012ULL;
    v_stack_m1D8 = v_rip - 7402291;
    v_stack_m1E8 = *(unsigned __int64 *)(v_rsp - 264 + 96);
    result = PiDevCfgSetObjectProperty(*(unsigned __int64 *)(v_rip + 7532921), v_rsp - 264 + 80, *(unsigned __int64 *)(a1 + 48), 1);
    if (sign_flag) goto loc_00737314;
    goto loc_00737286;
loc_00737263:
    v_stack_m1C0 = 0;
    v_stack_m1C8 = 0;
    v_stack_m1D0 = 0;
    v_stack_m1D8 = v_rip - 7402342;
    v_stack_m1E8 = *(unsigned __int64 *)(v_rsp - 264 + 96);
    result = PiDevCfgSetObjectProperty(*(unsigned __int64 *)(v_rip + 7532921), v_rsp - 264 + 80, *(unsigned __int64 *)(a1 + 48), 1);
loc_00737286:
    if ((unsigned int)(v_r15) == 0) goto loc_00737314;
    v_stack_m1D0 = 0;
    v_stack_m1D8 = v_stack_m1A4;
    v_stack_m1E0 = v_stack_m1A8;
    v_stack_m1E8 = v_stack_m198;
    v_stack_m1A4 = 4;
    result = CmGetDeviceRegProp(*(unsigned __int64 *)(v_rip + 7532793), *(unsigned __int64 *)(a1 + 48), *(unsigned __int64 *)(v_rsp - 264 + 96), (unsigned int)((unsigned int)(4 + 7)));
    if (sign_flag) goto loc_007372ED;
    if (v_stack_m198 != 4) goto loc_007372ED;
    result = (unsigned int)(v_stack_m1A8);
    if (v_stack_m1A4 != 4) {
        result = 0;
    }
    result = (unsigned int)((result) | ((unsigned int)(v_r15)));
    v_stack_m1E0 = 4;
    v_stack_m1A8 = (unsigned int)(result);
    v_stack_m1E8 = v_stack_m1A8;
    result = PiDevCfgSetDeviceRegProp(*(unsigned __int64 *)(v_rip + 7532793), v_rsp - 264 + 80, (unsigned int)((unsigned int)(4 + 7)), 4);
loc_00737314:
    if (v_stack_m1A0 != 0) {
        result = PiDevCfgFreeDriverNode(v_stack_m1A0, v_rsp - 264 + 80, (unsigned int)((unsigned int)(4 + 7)), 4);
    }
    result = RtlFreeAnsiString(v_rsp - 264 - 120, v_rsp - 264 + 80, (unsigned int)((unsigned int)(4 + 7)), 4);
    result = RtlFreeAnsiString(v_rsp - 264 - 16, v_rsp - 264 + 80, (unsigned int)((unsigned int)(4 + 7)), 4);
    result = RtlFreeAnsiString(v_rsp - 264, v_rsp - 264 + 80, (unsigned int)((unsigned int)(4 + 7)), 4);
    result = RtlFreeAnsiString(v_rsp - 264 + 16, v_rsp - 264 + 80, (unsigned int)((unsigned int)(4 + 7)), 4);
    result = RtlFreeAnsiString(v_rsp - 264 + 32, v_rsp - 264 + 80, (unsigned int)((unsigned int)(4 + 7)), 4);
    result = RtlFreeAnsiString(v_rsp - 264 + 48, v_rsp - 264 + 80, (unsigned int)((unsigned int)(4 + 7)), 4);
    result = RtlFreeAnsiString(v_rsp - 264 - 104, v_rsp - 264 + 80, (unsigned int)((unsigned int)(4 + 7)), 4);
    result = RtlFreeAnsiString(v_rsp - 264 - 88, v_rsp - 264 + 80, (unsigned int)((unsigned int)(4 + 7)), 4);
    result = RtlFreeAnsiString(v_stack_m190, v_rsp - 264 + 80, (unsigned int)((unsigned int)(4 + 7)), 4);
    result = RtlFreeAnsiString(v_rsp - 264 - 72, v_rsp - 264 + 80, (unsigned int)((unsigned int)(4 + 7)), 4);
    result = PiDevCfgFreeDeviceContext(v_rsp - 264 + 80, v_rsp - 264 + 80, (unsigned int)((unsigned int)(4 + 7)), 4);
    a1 = (*(unsigned __int64 *)(v_rsp - 264 + 216)) ^ (v_rsp);
    result = _security_check_cookie(a1, v_rsp - 264 + 80, (unsigned int)((unsigned int)(4 + 7)), 4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PpDevCfgProcessDeviceExtensions(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m190;
    uint32_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint32_t v_stack_m1A4;
    uint32_t v_stack_m1A8;
    uint32_t v_stack_m1B8;
    uint32_t v_stack_m1C0;
    uint64_t v_stack_m1C8;
    uint32_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint32_t v_stack_m1E0;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m28;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (480);
    result = (*(uint64_t *)(v_rip + 0x6D3AE7)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x108 + 0xD8) = result;
    Arg2 = 0;
    result = memset(local_rsp - 264 + 80, Arg2, Arg2 + 88, a4);
    local_rdi = 0;
    v_stack_m198 = 1;
    result = 0;
    *(uint64_t *)(local_rsp - 0x108 - 0x78) = 0;
    *(uint64_t *)(local_rsp - 0x108 - 0x70) = 0;
    v_stack_m1A0 = 0;
    *(uint64_t *)(local_rsp - 0x108 - 0x48) = 0;
    *(uint64_t *)(local_rsp - 0x108 - 0x40) = 0;
    *(uint64_t *)(local_rsp - 0x108 - 0x10) = 0;
    *(uint64_t *)(local_rsp - 0x108 - 0x8) = 0;
    *(uint64_t *)(local_rsp - 0x108) = 0;
    *(uint64_t *)(local_rsp - 0x108 + 0x8) = 0;
    *(uint64_t *)(local_rsp - 0x108 + 0x10) = 0;
    *(uint64_t *)(local_rsp - 0x108 + 0x18) = 0;
    *(uint64_t *)(local_rsp - 0x108 + 0x20) = 0;
    *(uint64_t *)(local_rsp - 0x108 + 0x28) = 0;
    *(uint64_t *)(local_rsp - 0x108 + 0x30) = 0;
    *(uint64_t *)(local_rsp - 0x108 + 0x38) = 0;
    *(uint64_t *)(local_rsp - 0x108 - 0x68) = 0;
    *(uint64_t *)(local_rsp - 0x108 - 0x60) = 0;
    *(uint64_t *)(local_rsp - 0x108 - 0x58) = 0;
    *(uint64_t *)(local_rsp - 0x108 - 0x50) = 0;
    v_stack_m190 = 0;
    *(uint64_t *)(local_rsp - 0x108 - 0x80) = 0;
    *(uint64_t *)(local_rsp - 0x108 + 0xB0) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x108 + 0xD0) = 0;
    *(uint64_t *)(local_rsp - 0x108 + 0xC0) = v_xmm0;
    v_stack_m1A8 = 0;
    v_stack_m1A4 = 0;
    if ((*(uint32_t *)(v_rip + 0x8A13C9)) != 0) goto loc_00736D0F;
    goto loc_00737323;
loc_00736D0F:
    if (*(uint64_t *)(arg1 + 0x30) != 0) goto loc_00736D22;
    goto loc_00737323;
loc_00736D22:
    Arg2 = 0;
    result = PiDevCfgInitDeviceContext(*(uint64_t *)(arg1 + 0x30), Arg2, local_rsp - 264 + 80, a4);
    if (sign_flag) goto loc_00737314;
    *(uint64_t *)(local_rsp - 0x108 - 0x38) = v_rip - 7487170;
    v_stack_m1E0 = 1;
    *(uint64_t *)(local_rsp - 0x108 - 0x28) = local_rsp - 264 - 120;
    *(uint64_t *)(local_rsp - 0x108 - 0x30) = 0x2012ULL;
    v_stack_m1E8 = local_rsp - 264 - 56;
    *(uint32_t *)(local_rsp - 0x108 - 0x20) = 0;
    *(uint64_t *)(local_rsp - 0x108 - 0x18) = 0;
    *(uint32_t *)(local_rsp - 0x108 - 0x1C) = 6;
    result = PiDevCfgQueryObjectProperties(1, *(uint64_t *)(arg1 + 0x30), 1, *(uint64_t *)(local_rsp - 0x108 + 0x60));
    if (sign_flag) goto loc_00737314;
    if ((*(uint32_t *)(local_rsp - 0x108 - 0x18)) < 0) {
        Arg2 = 0;
        Arg1 = local_rsp - 264 - 120;
        result = RtlInitUnicodeString(Arg1, Arg2, 1, *(uint64_t *)(local_rsp - 0x108 + 0x60));
    }
    result = PiDevCfgFindDeviceDriver(local_rsp - 264 + 80, *(uint64_t *)(local_rsp - 0x108 - 0x70), v_stack_m1A0, *(uint64_t *)(local_rsp - 0x108 + 0x60));
    if (sign_flag) goto loc_00737314;
    result = (v_stack_m1A0) + (208);
    if ((*(uint64_t *)(result)) == result) goto loc_0073714B;
loc_00736DD8:
    result = PiDevCfgQueryDriverConfiguration(*(uint64_t *)(result), *(uint64_t *)(local_rsp - 0x108 - 0x70), v_stack_m1A0, *(uint64_t *)(local_rsp - 0x108 + 0x60));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0xC0000493ULL)))) goto loc_00736DF3;
    goto loc_00736F06;
loc_00736DF3:
    local_r12 = 0;
    if (sign_flag) goto loc_00737314;
    if ((*(uint64_t *)(*(uint64_t *)(result) + 0x128)) == 0) goto loc_00736E13;
    goto loc_00736F1F;
loc_00736E13:
    if ((*(uint64_t *)(*(uint64_t *)(result) + 0x138)) == 0) goto loc_00736E3B;
    a4 = 0;
    Arg2 = 0;
    result = PiDevCfgAppendMultiSz(local_rsp - 264 - 16, Arg2, *(uint64_t *)(result) + 304, a4);
    if (sign_flag) goto loc_00737314;
loc_00736E3B:
    if ((*(uint64_t *)(*(uint64_t *)(result) + 0x148)) == 0) goto loc_00736E63;
    a4 = 0;
    Arg2 = 0;
    result = PiDevCfgAppendMultiSz(local_rsp - 264, Arg2, *(uint64_t *)(result) + 320, a4);
    if (sign_flag) goto loc_00737314;
loc_00736E63:
    if ((*(uint64_t *)(*(uint64_t *)(result) + 0x158)) == 0) goto loc_00736E8B;
    a4 = 0;
    Arg2 = 0;
    result = PiDevCfgAppendMultiSz(local_rsp - 264 + 16, Arg2, *(uint64_t *)(result) + 336, a4);
    if (sign_flag) goto loc_00737314;
loc_00736E8B:
    if ((*(uint64_t *)(*(uint64_t *)(result) + 0x168)) == 0) goto loc_00736EB3;
    a4 = 0;
    Arg2 = 0;
    result = PiDevCfgAppendMultiSz(local_rsp - 264 + 32, Arg2, *(uint64_t *)(result) + 352, a4);
    if (sign_flag) goto loc_00737314;
loc_00736EB3:
    if ((*(uint64_t *)(*(uint64_t *)(result) + 0x178)) == 0) goto loc_00736EDB;
    a4 = 0;
    Arg2 = 0;
    result = PiDevCfgAppendMultiSz(local_rsp - 264 + 48, Arg2, *(uint64_t *)(result) + 368, a4);
    if (sign_flag) goto loc_00737314;
loc_00736EDB:
    local_r15 = (uint32_t)((0) | (*(uint32_t *)(*(uint64_t *)(result) + 0x1A0)));
    a4 = 0;
    a3 = 0;
    result = PiDevCfgAppendMultiSz(local_rsp - 264 - 104, *(uint64_t *)(result) + 40, a3, a4);
    if (sign_flag) goto loc_00737314;
    a4 = 0;
loc_00736F06:
    a3 = 0;
    result = PiDevCfgAppendMultiSz(local_rsp - 264 - 88, *(uint64_t *)(result) + 424, a3, a4);
    if (sign_flag) goto loc_00737314;
loc_00736F1F:
    result = (v_stack_m1A0) + (208);
    if ((*(uint64_t *)(*(uint64_t *)(result))) != result) goto loc_00736DD8;
    local_rdi = 0;
    if (sign_flag) goto loc_00737314;
    if (*(uint64_t *)(local_rsp - 0x108 - 0x40) == 0) goto loc_00736F9D;
    v_stack_m1B8 = 0;
    v_stack_m1C0 = (uint32_t)(*(uint16_t *)(local_rsp - 0x108 - 0x48));
    v_stack_m1C8 = *(uint64_t *)(local_rsp - 0x108 - 0x40);
    v_stack_m1D0 = 0x2012ULL;
    v_stack_m1D8 = v_rip - 7487768;
    v_stack_m1E8 = *(uint64_t *)(local_rsp - 0x108 + 0x60);
    result = PiDevCfgSetObjectProperty(*(uint64_t *)(v_rip + 0x72F424), local_rsp - 264 + 80, *(uint64_t *)(arg1 + 0x30), local_rdi + 1);
    if (sign_flag) goto loc_00737314;
    goto loc_00737314;
loc_00736F9D:
    *(uint64_t *)(local_rsp - 0x108 + 0xB0) = local_rsp - 264 - 16;
    *(uint64_t *)(local_rsp - 0x108 + 0xB8) = local_rsp - 264;
    *(uint64_t *)(local_rsp - 0x108 + 0xC0) = local_rsp - 264 + 16;
    *(uint64_t *)(local_rsp - 0x108 + 0xC8) = local_rsp - 264 + 32;
    *(uint64_t *)(local_rsp - 0x108 + 0xD0) = local_rsp - 264 + 48;
loc_00736FD7:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsp - 0x108 + local_rdi * 1 + 0xB0) + 0x8)) == 0) goto loc_007370DA;
    *(uint64_t *)(local_rsp - 0x108 - 0x38) = *(uint64_t *)(local_rdi + v_rip + 0x8A16B3 * 1);
    *(uint64_t *)(local_rsp - 0x108 - 0x28) = v_stack_m190;
    v_stack_m1E0 = 1;
    v_stack_m1E8 = local_rsp - 264 - 56;
    *(uint32_t *)(local_rsp - 0x108 - 0x30) = 0x2012ULL;
    *(uint32_t *)(local_rsp - 0x108 - 0x1C) = 6;
    result = PiDevCfgQueryObjectProperties(*(uint64_t *)(v_rip + 0x72F424), *(uint64_t *)(arg1 + 0x30), 1, *(uint64_t *)(local_rsp - 0x108 + 0x60));
    if (sign_flag) goto loc_00737314;
    if ((*(uint32_t *)(local_rsp - 0x108 - 0x18)) < 0) {
        Arg2 = 0;
        Arg1 = v_stack_m190;
        result = RtlInitUnicodeString(Arg1, Arg2, 1, *(uint64_t *)(local_rsp - 0x108 + 0x60));
    }
    a4 = 0;
    Arg2 = 0;
    result = PiDevCfgAppendMultiSz(v_stack_m190, Arg2, *(uint64_t *)(local_rsp - 0x108 + local_rdi * 1 + 0xB0), a4);
    if (sign_flag) goto loc_00737314;
    v_stack_m1C0 = (uint32_t)(v_stack_m190);
    v_stack_m1C8 = *(uint64_t *)(local_rsp - 0x108 - 0x80);
    v_stack_m1D0 = 0x2012ULL;
    v_stack_m1D8 = *(uint64_t *)(local_rdi + v_rip + 0x8A15FD * 1);
    v_stack_m1E8 = *(uint64_t *)(local_rsp - 0x108 + 0x60);
    result = PiDevCfgSetObjectProperty(*(uint64_t *)(v_rip + 0x72F301), local_rsp - 264 + 80, *(uint64_t *)(arg1 + 0x30), 1);
    if (sign_flag) goto loc_00737314;
    result = RtlFreeAnsiString(v_stack_m190, local_rsp - 264 + 80, *(uint64_t *)(arg1 + 0x30), 1);
loc_007370DA:
    local_r12 = (uint32_t)((0) + 1);
    local_rdi = (local_rdi) + (8);
    if (((uint32_t)(local_r12)) < 5) goto loc_00736FD7;
    goto loc_0073713E;
loc_007370FC:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m1A0 + 0xD0) + 0xB8)))) & (1)) == 0) goto loc_00737134;
    result = PiDevCfgConfigureDeviceDriver(Arg1, local_rsp - 264 + 80, *(uint64_t *)(v_stack_m1A0 + 0xD0), v_stack_m1A8);
    if (sign_flag) goto loc_00737314;
    local_r15 = (uint32_t)((local_r15) | (v_stack_m1A8));
loc_00737134:
loc_0073713E:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m1A0 + 0xD0))) != (v_stack_m1A0 + 208)) goto loc_007370FC;
loc_0073714B:
    local_rdi = 0;
    result = v_stack_m1A0 + 208;
    if ((*(uint64_t *)(local_rsp - 0x108 - 0x70)) != 0) {
        a3 = *(uint64_t *)(arg1 + 0x30);
        result = v_rip - 7488222;
        Arg1 = *(uint64_t *)(v_rip + 0x72F233);
        a4 = local_rdi + 1;
        v_stack_m1B8 = 0;
        Arg2 = local_rsp - 264 + 80;
        v_stack_m1C0 = 0;
        v_stack_m1C8 = 0;
        v_stack_m1D0 = 0;
        v_stack_m1D8 = result;
        v_stack_m1E8 = *(uint64_t *)(local_rsp - 0x108 + 0x60);
        result = PiDevCfgSetObjectProperty(Arg1, Arg2, a3, a4);
    }
    v_stack_m1B8 = 0;
    if (*(uint64_t *)(local_rsp - 0x108 - 0x60) == 0) goto loc_007371E5;
    v_stack_m1C0 = (uint32_t)(*(uint16_t *)(local_rsp - 0x108 - 0x68));
    v_stack_m1C8 = *(uint64_t *)(local_rsp - 0x108 - 0x60);
    v_stack_m1D0 = 0x2012ULL;
    v_stack_m1D8 = v_rip - 7428036;
    v_stack_m1E8 = *(uint64_t *)(local_rsp - 0x108 + 0x60);
    result = PiDevCfgSetObjectProperty(*(uint64_t *)(v_rip + 0x72F1FC), local_rsp - 264 + 80, *(uint64_t *)(arg1 + 0x30), 1);
    if (sign_flag) goto loc_00737314;
    goto loc_00737211;
loc_007371E5:
    v_stack_m1C0 = 0;
    v_stack_m1C8 = 0;
    v_stack_m1D0 = 0;
    v_stack_m1D8 = v_rip - 7428096;
    v_stack_m1E8 = *(uint64_t *)(local_rsp - 0x108 + 0x60);
    result = PiDevCfgSetObjectProperty(*(uint64_t *)(v_rip + 0x72F1FC), local_rsp - 264 + 80, *(uint64_t *)(arg1 + 0x30), 1);
loc_00737211:
    v_stack_m1B8 = 0;
    if (*(uint64_t *)(local_rsp - 0x108 - 0x50) == 0) goto loc_00737263;
    v_stack_m1C0 = (uint32_t)(*(uint16_t *)(local_rsp - 0x108 - 0x58));
    v_stack_m1C8 = *(uint64_t *)(local_rsp - 0x108 - 0x50);
    v_stack_m1D0 = 0x2012ULL;
    v_stack_m1D8 = v_rip - 7402291;
    v_stack_m1E8 = *(uint64_t *)(local_rsp - 0x108 + 0x60);
    result = PiDevCfgSetObjectProperty(*(uint64_t *)(v_rip + 0x72F179), local_rsp - 264 + 80, *(uint64_t *)(arg1 + 0x30), 1);
    if (sign_flag) goto loc_00737314;
    goto loc_00737286;
loc_00737263:
    v_stack_m1C0 = 0;
    v_stack_m1C8 = 0;
    v_stack_m1D0 = 0;
    v_stack_m1D8 = v_rip - 7402342;
    v_stack_m1E8 = *(uint64_t *)(local_rsp - 0x108 + 0x60);
    result = PiDevCfgSetObjectProperty(*(uint64_t *)(v_rip + 0x72F179), local_rsp - 264 + 80, *(uint64_t *)(arg1 + 0x30), 1);
loc_00737286:
    if ((uint32_t)(local_r15) == 0) goto loc_00737314;
    v_stack_m1D0 = 0;
    v_stack_m1D8 = v_stack_m1A4;
    v_stack_m1E0 = v_stack_m1A8;
    v_stack_m1E8 = v_stack_m198;
    v_stack_m1A4 = 4;
    result = CmGetDeviceRegProp(*(uint64_t *)(v_rip + 0x72F0F9), *(uint64_t *)(arg1 + 0x30), *(uint64_t *)(local_rsp - 0x108 + 0x60), (uint32_t)((uint32_t)(4 + 7)));
    if (sign_flag) goto loc_007372ED;
    if (v_stack_m198 != 4) goto loc_007372ED;
    result = (uint32_t)(v_stack_m1A8);
    if (v_stack_m1A4 != 4) {
        result = 0;
    }
    result = (uint32_t)((result) | ((uint32_t)(local_r15)));
    v_stack_m1E0 = 4;
    v_stack_m1A8 = (uint32_t)(result);
    v_stack_m1E8 = v_stack_m1A8;
    result = PiDevCfgSetDeviceRegProp(*(uint64_t *)(v_rip + 0x72F0F9), local_rsp - 264 + 80, (uint32_t)((uint32_t)(4 + 7)), 4);
loc_00737314:
    if (v_stack_m1A0 != 0) {
        result = PiDevCfgFreeDriverNode(v_stack_m1A0, local_rsp - 264 + 80, (uint32_t)((uint32_t)(4 + 7)), 4);
    }
    result = RtlFreeAnsiString(local_rsp - 264 - 120, local_rsp - 264 + 80, (uint32_t)((uint32_t)(4 + 7)), 4);
    result = RtlFreeAnsiString(local_rsp - 264 - 16, local_rsp - 264 + 80, (uint32_t)((uint32_t)(4 + 7)), 4);
    result = RtlFreeAnsiString(local_rsp - 264, local_rsp - 264 + 80, (uint32_t)((uint32_t)(4 + 7)), 4);
    result = RtlFreeAnsiString(local_rsp - 264 + 16, local_rsp - 264 + 80, (uint32_t)((uint32_t)(4 + 7)), 4);
    result = RtlFreeAnsiString(local_rsp - 264 + 32, local_rsp - 264 + 80, (uint32_t)((uint32_t)(4 + 7)), 4);
    result = RtlFreeAnsiString(local_rsp - 264 + 48, local_rsp - 264 + 80, (uint32_t)((uint32_t)(4 + 7)), 4);
    result = RtlFreeAnsiString(local_rsp - 264 - 104, local_rsp - 264 + 80, (uint32_t)((uint32_t)(4 + 7)), 4);
    result = RtlFreeAnsiString(local_rsp - 264 - 88, local_rsp - 264 + 80, (uint32_t)((uint32_t)(4 + 7)), 4);
    result = RtlFreeAnsiString(v_stack_m190, local_rsp - 264 + 80, (uint32_t)((uint32_t)(4 + 7)), 4);
    result = RtlFreeAnsiString(local_rsp - 264 - 72, local_rsp - 264 + 80, (uint32_t)((uint32_t)(4 + 7)), 4);
    result = PiDevCfgFreeDeviceContext(local_rsp - 264 + 80, local_rsp - 264 + 80, (uint32_t)((uint32_t)(4 + 7)), 4);
    Arg1 = (*(uint64_t *)(local_rsp - 0x108 + 0xD8)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, local_rsp - 264 + 80, (uint32_t)((uint32_t)(4 + 7)), 4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x30` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00736C2C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
