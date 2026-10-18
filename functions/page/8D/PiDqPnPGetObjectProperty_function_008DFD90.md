# PiDqPnPGetObjectProperty

- RVA: `0x008DFD90`–`0x008E01BB` (길이 `1,067` bytes)
- VA: `0x00000001408DFD90`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00085C98`
- 디코드: `270`개 명령, `1,067/1,067` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **12**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x008DFE5F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008DFEF5` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008DFF08` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008DFFB0` → [PiPnpRtlObjectActionCallback](../8E/PiPnpRtlObjectActionCallback_function_008E2850.md) (function, `0x008E2850`)
- `0x008E001D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008E0083` → [PnpGetObjectPropertyWorker](../8E/PnpGetObjectPropertyWorker_function_008E1810.md) (function, `0x008E1810`)
- `0x008E00C7` → [PiPnpRtlObjectActionCallback](../8E/PiPnpRtlObjectActionCallback_function_008E2850.md) (function, `0x008E2850`)
- `0x008E0126` → [PnpGetGenericStoreProperty](../8E/PnpGetGenericStoreProperty_function_008EFBA0.md) (function, `0x008EFBA0`)
- `0x008E0153` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008E0178` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008E01A4` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008E01B1` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [PiDqActionDataGetRequestedProperties](PiDqActionDataGetRequestedProperties_function_008DEBE4.md) at `0x008DED79`
- [PiDqPnPGetObjectPropertyInBestLocale](PiDqPnPGetObjectPropertyInBestLocale_function_008DEE10.md) at `0x008DF202`
- [PiDqPropertyCallback](PiDqPropertyCallback_function_008DF580.md) at `0x008DF6BF`
- [PiDqActionDataGetAllPropertiesInAllLanguages](../99/PiDqActionDataGetAllPropertiesInAllLanguages_function_0099569C.md) at `0x00995808`
- [PiDqActionDataGetChangedProperties](../A6/PiDqActionDataGetChangedProperties_function_00A61F10.md) at `0x00A62044`
- [sub_00B2C164](../B2/Unknown_function_00B2C164.md) at `0x00B2C195`

### Static image references
- `0x008DFED9` → RVA `0x008E2850` (`PiPnpRtlObjectActionCallback`; read)
- `0x008DFF32` → RVA `0x00E66398` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **8**
  - `0x008DFE5F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008DFEF5` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008DFF08` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008E001D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008E0153` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008E0178` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008E01A4` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008E01B1` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x008E0191` → [sub_00B1CF96](../B1/Unknown_function_00B1CF96.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008DFD90  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
008DFD95  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
008DFD9A  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
008DFD9F  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
008DFDA4  55                              push rbp
008DFDA5  56                              push rsi
008DFDA6  57                              push rdi
008DFDA7  41 54                           push r12
008DFDA9  41 55                           push r13
008DFDAB  41 56                           push r14
008DFDAD  41 57                           push r15
008DFDAF  48 8D 6C 24 F1                  lea rbp, [rsp - 0xf]
008DFDB4  48 81 EC C0 00 00 00            sub rsp, 0xc0
008DFDBB  4C 8B 75 7F                     mov r14, qword ptr [rbp + 0x7f]
008DFDBF  33 DB                           xor ebx, ebx
008DFDC1  41 0F 10 01                     movups xmm0, xmmword ptr [r9]
008DFDC5  48 8B 7D 77                     mov rdi, qword ptr [rbp + 0x77]
008DFDC9  44 8B EA                        mov r13d, edx
008DFDCC  C7 45 AF 00 02 00 00            mov dword ptr [rbp - 0x51], 0x200
008DFDD3  44 8B FB                        mov r15d, ebx
008DFDD6  89 5D B3                        mov dword ptr [rbp - 0x4d], ebx
008DFDD9  44 8B E3                        mov r12d, ebx
008DFDDC  8B F3                           mov esi, ebx
008DFDDE  41 0F 11 06                     movups xmmword ptr [r14], xmm0
008DFDE2  41 8B 41 10                     mov eax, dword ptr [r9 + 0x10]
008DFDE6  41 89 46 10                     mov dword ptr [r14 + 0x10], eax
008DFDEA  8B 45 6F                        mov eax, dword ptr [rbp + 0x6f]
008DFDED  41 89 46 14                     mov dword ptr [r14 + 0x14], eax
008DFDF1  49 89 5E 20                     mov qword ptr [r14 + 0x20], rbx
008DFDF5  49 89 5E 28                     mov qword ptr [r14 + 0x28], rbx
008DFDF9  49 89 5E 18                     mov qword ptr [r14 + 0x18], rbx
008DFDFD  48 85 FF                        test rdi, rdi
008DFE00  0F 84 C8 00 00 00               je 0x1408dfece
008DFE06  BA FF FF FF 7F                  mov edx, 0x7fffffff
008DFE0B  48 8B C7                        mov rax, rdi
008DFE0E  8B CA                           mov ecx, edx
008DFE10  66 39 18                        cmp word ptr [rax], bx
008DFE13  74 0A                           je 0x1408dfe1f
008DFE15  48 83 C0 02                     add rax, 2
008DFE19  48 83 E9 01                     sub rcx, 1
008DFE1D  75 F1                           jne 0x1408dfe10
008DFE1F  48 85 C9                        test rcx, rcx
008DFE22  BE 0D 00 00 C0                  mov esi, 0xc000000d
008DFE27  0F 45 F3                        cmovne esi, ebx
008DFE2A  0F 84 11 03 00 00               je 0x1408e0141
008DFE30  48 2B D1                        sub rdx, rcx
008DFE33  0F 84 95 00 00 00               je 0x1408dfece
008DFE39  48 8D 4A 01                     lea rcx, [rdx + 1]
008DFE3D  B8 02 00 00 00                  mov eax, 2
008DFE42  48 F7 E1                        mul rcx
008DFE45  48 8B D8                        mov rbx, rax
008DFE48  48 85 D2                        test rdx, rdx
008DFE4B  0F 85 E9 02 00 00               jne 0x1408e013a
008DFE51  41 B8 50 6E 70 58               mov r8d, 0x58706e50
008DFE57  48 8B D0                        mov rdx, rax
008DFE5A  B9 00 01 00 00                  mov ecx, 0x100
008DFE5F  E8 8C 22 2A 00                  call 0x140b820f0
008DFE64  49 89 46 18                     mov qword ptr [r14 + 0x18], rax
008DFE68  48 85 C0                        test rax, rax
008DFE6B  0F 84 11 03 00 00               je 0x1408e0182
008DFE71  48 D1 EB                        shr rbx, 1
008DFE74  BA FE FF FF 7F                  mov edx, 0x7ffffffe
008DFE79  48 8D 4B FF                     lea rcx, [rbx - 1]
008DFE7D  48 3B CA                        cmp rcx, rdx
008DFE80  0F 87 03 03 00 00               ja 0x1408e0189
008DFE86  33 F6                           xor esi, esi
008DFE88  48 2B D3                        sub rdx, rbx
008DFE8B  4C 8B C7                        mov r8, rdi
008DFE8E  4C 2B C0                        sub r8, rax
008DFE91  48 8D 0C 1A                     lea rcx, [rdx + rbx]
008DFE95  48 85 C9                        test rcx, rcx
008DFE98  74 27                           je 0x1408dfec1
008DFE9A  41 0F B7 0C 00                  movzx ecx, word ptr [r8 + rax]
008DFE9F  66 85 C9                        test cx, cx
008DFEA2  74 18                           je 0x1408dfebc
008DFEA4  66 89 08                        mov word ptr [rax], cx
008DFEA7  48 83 C0 02                     add rax, 2
008DFEAB  48 83 EB 01                     sub rbx, 1
008DFEAF  75 E0                           jne 0x1408dfe91
008DFEB1  48 83 E8 02                     sub rax, 2
008DFEB5  BE 05 00 00 80                  mov esi, 0x80000005
008DFEBA  EB 05                           jmp 0x1408dfec1
008DFEBC  48 85 DB                        test rbx, rbx
008DFEBF  74 F0                           je 0x1408dfeb1
008DFEC1  33 DB                           xor ebx, ebx
008DFEC3  66 89 18                        mov word ptr [rax], bx
008DFEC6  85 F6                           test esi, esi
008DFEC8  0F 88 73 02 00 00               js 0x1408e0141
008DFECE  85 F6                           test esi, esi
008DFED0  0F 88 4C 01 00 00               js 0x1408e0022
008DFED6  8B 45 AF                        mov eax, dword ptr [rbp - 0x51]
008DFED9  48 8D 0D 70 29 00 00            lea rcx, [rip + 0x2970]
008DFEE0  41 3B C4                        cmp eax, r12d
008DFEE3  76 3B                           jbe 0x1408dff20
008DFEE5  44 8B E0                        mov r12d, eax
008DFEE8  4D 85 FF                        test r15, r15
008DFEEB  74 0D                           je 0x1408dfefa
008DFEED  BA 50 6E 70 58                  mov edx, 0x58706e50
008DFEF2  49 8B CF                        mov rcx, r15
008DFEF5  E8 76 29 2A 00                  call 0x140b82870
008DFEFA  49 8B D4                        mov rdx, r12
008DFEFD  B9 00 01 00 00                  mov ecx, 0x100
008DFF02  41 B8 50 6E 70 58               mov r8d, 0x58706e50
008DFF08  E8 E3 21 2A 00                  call 0x140b820f0
008DFF0D  4C 8B F8                        mov r15, rax
008DFF10  48 85 C0                        test rax, rax
008DFF13  0F 84 48 02 00 00               je 0x1408e0161
008DFF19  48 8D 0D 30 29 00 00            lea rcx, [rip + 0x2930]
008DFF20  89 5D AF                        mov dword ptr [rbp - 0x51], ebx
008DFF23  45 85 ED                        test r13d, r13d
008DFF26  0F 84 CC 01 00 00               je 0x1408e00f8
008DFF2C  48 8B 45 5F                     mov rax, qword ptr [rbp + 0x5f]
008DFF30  33 F6                           xor esi, esi
008DFF32  48 8B 3D 5F 64 58 00            mov rdi, qword ptr [rip + 0x58645f]
008DFF39  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
008DFF3D  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
008DFF41  48 89 45 D7                     mov qword ptr [rbp - 0x29], rax
008DFF45  48 8B 45 67                     mov rax, qword ptr [rbp + 0x67]
008DFF49  48 89 45 DF                     mov qword ptr [rbp - 0x21], rax
008DFF4D  48 8D 45 B3                     lea rax, [rbp - 0x4d]
008DFF51  48 89 5D BF                     mov qword ptr [rbp - 0x41], rbx
008DFF55  48 89 5D C7                     mov qword ptr [rbp - 0x39], rbx
008DFF59  89 5D FB                        mov dword ptr [rbp - 5], ebx
008DFF5C  48 8B 9F E8 01 00 00            mov rbx, qword ptr [rdi + 0x1e8]
008DFF63  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
008DFF67  48 8D 45 AF                     lea rax, [rbp - 0x51]
008DFF6B  48 89 45 FF                     mov qword ptr [rbp - 1], rax
008DFF6F  48 C7 45 07 00 00 00 00         mov qword ptr [rbp + 7], 0
008DFF77  4C 89 7D EF                     mov qword ptr [rbp - 0x11], r15
008DFF7B  44 89 65 F7                     mov dword ptr [rbp - 9], r12d
008DFF7F  48 85 DB                        test rbx, rbx
008DFF82  0F 84 B2 00 00 00               je 0x1408e003a
008DFF88  48 8B 55 4F                     mov rdx, qword ptr [rbp + 0x4f]
008DFF8C  48 8D 45 BF                     lea rax, [rbp - 0x41]
008DFF90  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008DFF95  44 8D 4E 08                     lea r9d, [rsi + 8]
008DFF99  48 3B D9                        cmp rbx, rcx
008DFF9C  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
008DFFA4  45 8B C5                        mov r8d, r13d
008DFFA7  48 8B CF                        mov rcx, rdi
008DFFAA  0F 85 F1 01 00 00               jne 0x1408e01a1
008DFFB0  E8 9B 28 00 00                  call 0x1408e2850
008DFFB5  3D 02 00 00 C0                  cmp eax, 0xc0000002
008DFFBA  0F 84 30 01 00 00               je 0x1408e00f0
008DFFC0  3D 20 01 00 C0                  cmp eax, 0xc0000120
008DFFC5  75 6B                           jne 0x1408e0032
008DFFC7  8B 75 BF                        mov esi, dword ptr [rbp - 0x41]
008DFFCA  48 8B 7D 77                     mov rdi, qword ptr [rbp + 0x77]
008DFFCE  33 DB                           xor ebx, ebx
008DFFD0  81 FE 23 00 00 C0               cmp esi, 0xc0000023
008DFFD6  0F 84 FA FE FF FF               je 0x1408dfed6
008DFFDC  85 F6                           test esi, esi
008DFFDE  78 30                           js 0x1408e0010
008DFFE0  8B 45 B3                        mov eax, dword ptr [rbp - 0x4d]
008DFFE3  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
008DFFE7  8B 45 AF                        mov eax, dword ptr [rbp - 0x51]
008DFFEA  41 89 46 24                     mov dword ptr [r14 + 0x24], eax
008DFFEE  4D 89 7E 28                     mov qword ptr [r14 + 0x28], r15
008DFFF2  8B C6                           mov eax, esi
008DFFF4  48 8B 9C 24 08 01 00 00         mov rbx, qword ptr [rsp + 0x108]
008DFFFC  48 81 C4 C0 00 00 00            add rsp, 0xc0
008E0003  41 5F                           pop r15
008E0005  41 5E                           pop r14
008E0007  41 5D                           pop r13
008E0009  41 5C                           pop r12
008E000B  5F                              pop rdi
008E000C  5E                              pop rsi
008E000D  5D                              pop rbp
008E000E  C3                              ret
008E000F  CC                              int3
008E0010  4D 85 FF                        test r15, r15
008E0013  74 0D                           je 0x1408e0022
008E0015  BA 50 6E 70 58                  mov edx, 0x58706e50
008E001A  49 8B CF                        mov rcx, r15
008E001D  E8 4E 28 2A 00                  call 0x140b82870
008E0022  81 FE 25 02 00 C0               cmp esi, 0xc0000225
008E0028  0F 85 38 01 00 00               jne 0x1408e0166
008E002E  8B C3                           mov eax, ebx
008E0030  EB C2                           jmp 0x1408dfff4
008E0032  85 C0                           test eax, eax
008E0034  0F 85 AC 00 00 00               jne 0x1408e00e6
008E003A  8B 45 07                        mov eax, dword ptr [rbp + 7]
008E003D  45 8B C5                        mov r8d, r13d
008E0040  4C 8B 4D CF                     mov r9, qword ptr [rbp - 0x31]
008E0044  48 8B CF                        mov rcx, rdi
008E0047  48 8B 55 4F                     mov rdx, qword ptr [rbp + 0x4f]
008E004B  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
008E004F  48 8B 45 FF                     mov rax, qword ptr [rbp - 1]
008E0053  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
008E0058  8B 45 F7                        mov eax, dword ptr [rbp - 9]
008E005B  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
008E005F  48 8B 45 EF                     mov rax, qword ptr [rbp - 0x11]
008E0063  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008E0068  48 8B 45 E7                     mov rax, qword ptr [rbp - 0x19]
008E006C  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008E0071  48 8B 45 DF                     mov rax, qword ptr [rbp - 0x21]
008E0075  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008E007A  48 8B 45 D7                     mov rax, qword ptr [rbp - 0x29]
008E007E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008E0083  E8 88 17 00 00                  call 0x1408e1810
008E0088  8B F0                           mov esi, eax
008E008A  48 85 DB                        test rbx, rbx
008E008D  0F 84 37 FF FF FF               je 0x1408dffca
008E0093  48 8B 55 4F                     mov rdx, qword ptr [rbp + 0x4f]
008E0097  41 B9 08 00 00 00               mov r9d, 8
008E009D  89 45 BF                        mov dword ptr [rbp - 0x41], eax
008E00A0  45 8B C5                        mov r8d, r13d
008E00A3  48 8D 05 A6 27 00 00            lea rax, [rip + 0x27a6]
008E00AA  48 8B CF                        mov rcx, rdi
008E00AD  48 3B D8                        cmp rbx, rax
008E00B0  48 8D 45 BF                     lea rax, [rbp - 0x41]
008E00B4  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008E00B9  C7 44 24 20 02 00 00 00         mov dword ptr [rsp + 0x20], 2
008E00C1  0F 85 E7 00 00 00               jne 0x1408e01ae
008E00C7  E8 84 27 00 00                  call 0x1408e2850
008E00CC  3D 02 00 00 C0                  cmp eax, 0xc0000002
008E00D1  0F 84 F3 FE FF FF               je 0x1408dffca
008E00D7  3D 20 01 00 C0                  cmp eax, 0xc0000120
008E00DC  74 54                           je 0x1408e0132
008E00DE  85 C0                           test eax, eax
008E00E0  0F 84 E4 FE FF FF               je 0x1408dffca
008E00E6  BE E5 00 00 C0                  mov esi, 0xc00000e5
008E00EB  E9 DA FE FF FF                  jmp 0x1408dffca
008E00F0  48 8B DE                        mov rbx, rsi
008E00F3  E9 42 FF FF FF                  jmp 0x1408e003a
008E00F8  4C 8B 4D 67                     mov r9, qword ptr [rbp + 0x67]
008E00FC  48 8D 45 AF                     lea rax, [rbp - 0x51]
008E0100  48 8B 55 5F                     mov rdx, qword ptr [rbp + 0x5f]
008E0104  4C 8B C7                        mov r8, rdi
008E0107  48 8B 0D 8A 62 58 00            mov rcx, qword ptr [rip + 0x58628a]
008E010E  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008E0113  48 8D 45 B3                     lea rax, [rbp - 0x4d]
008E0117  44 89 64 24 30                  mov dword ptr [rsp + 0x30], r12d
008E011C  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
008E0121  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008E0126  E8 75 FA 00 00                  call 0x1408efba0
008E012B  8B F0                           mov esi, eax
008E012D  E9 9E FE FF FF                  jmp 0x1408dffd0
008E0132  8B 75 BF                        mov esi, dword ptr [rbp - 0x41]
008E0135  E9 90 FE FF FF                  jmp 0x1408dffca
008E013A  BE 95 00 00 C0                  mov esi, 0xc0000095
008E013F  33 DB                           xor ebx, ebx
008E0141  49 8B 4E 18                     mov rcx, qword ptr [r14 + 0x18]
008E0145  48 85 C9                        test rcx, rcx
008E0148  0F 84 80 FD FF FF               je 0x1408dfece
008E014E  BA 50 6E 70 58                  mov edx, 0x58706e50
008E0153  E8 18 27 2A 00                  call 0x140b82870
008E0158  49 89 5E 18                     mov qword ptr [r14 + 0x18], rbx
008E015C  E9 6D FD FF FF                  jmp 0x1408dfece
008E0161  BE 9A 00 00 C0                  mov esi, 0xc000009a
008E0166  49 8B 4E 18                     mov rcx, qword ptr [r14 + 0x18]
008E016A  48 85 C9                        test rcx, rcx
008E016D  0F 84 7F FE FF FF               je 0x1408dfff2
008E0173  BA 50 6E 70 58                  mov edx, 0x58706e50
008E0178  E8 F3 26 2A 00                  call 0x140b82870
008E017D  E9 70 FE FF FF                  jmp 0x1408dfff2
008E0182  BE 9A 00 00 C0                  mov esi, 0xc000009a
008E0187  EB B6                           jmp 0x1408e013f
008E0189  BE 0D 00 00 C0                  mov esi, 0xc000000d
008E018E  48 85 DB                        test rbx, rbx
008E0191  0F 84 FF CD 23 00               je 0x140b1cf96
008E0197  33 DB                           xor ebx, ebx
008E0199  66 89 18                        mov word ptr [rax], bx
008E019C  E9 25 FD FF FF                  jmp 0x1408dfec6
008E01A1  48 8B C3                        mov rax, rbx
008E01A4  E8 27 A9 DD FF                  call 0x1406baad0
008E01A9  E9 07 FE FF FF                  jmp 0x1408dffb5
008E01AE  48 8B C3                        mov rax, rbx
008E01B1  E8 1A A9 DD FF                  call 0x1406baad0
008E01B6  E9 11 FF FF FF                  jmp 0x1408e00cc
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiDqPnPGetObjectProperty(__int64 a1, int a2, __int64 a3, __int64 a4, unsigned int a5, __int64 a6, __int64 a7)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m47;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m94;
    unsigned int v_stack_m98;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned int v_stack_p50;
    unsigned __int64 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (192);
    v_rbx = 0;
    v_stack_m98 = 512;
    v_stack_m94 = 0;
    *(unsigned __int64 *)(a7) = v_xmm0;
    *(unsigned int *)(a7 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)));
    *(unsigned int *)(a7 + 20) = (unsigned int)((unsigned int)(a5));
    *(unsigned __int64 *)(a7 + 32) = 0;
    *(unsigned __int64 *)(a7 + 40) = 0;
    *(unsigned __int64 *)(a7 + 24) = 0;
    if (a6 == 0) goto loc_008DFECE;
loc_008DFE10:
    if ((*(unsigned __int16 *)(a6)) == 0) goto loc_008DFE1F;
    result = (a6) + (2);
    a1 = ((unsigned int)((unsigned int)((unsigned int)(0x7FFFFFFFULL)))) - (1);
    if (condition_is_not_equal) goto loc_008DFE10;
loc_008DFE1F:
    v_rsi = (unsigned int)(0xC000000DULL);
    if (a1 != 0) { v_rsi = 0; }
    if (a1 == 0) goto loc_008E0141;
    a2 = ((unsigned int)(0x7FFFFFFFULL)) - (a1);
    if (condition_is_equal) goto loc_008DFECE;
    if (a2 != 0) goto loc_008E013A;
    result = ExAllocatePool2(256, 2, (unsigned int)(0x58706E50ULL), a4);
    *(unsigned __int64 *)(a7 + 24) = result;
    if (result == 0) goto loc_008E0182;
    v_rbx = (2) >> (1);
    if ((v_rbx - 1) > ((unsigned int)(0x7FFFFFFEULL))) goto loc_008E0189;
    v_rsi = 0;
    a2 = ((unsigned int)(0x7FFFFFFEULL)) - (v_rbx);
    a3 = (a6) - (result);
loc_008DFE91:
    if (a2 + v_rbx * 1 == 0) goto loc_008DFEC1;
    if ((unsigned __int16)(*(unsigned __int16 *)(a3 + result * 1)) == 0) goto loc_008DFEBC;
    *(unsigned __int16 *)(result) = (unsigned __int16)(*(unsigned __int16 *)(a3 + result * 1));
    result = (result) + (2);
    v_rbx = (v_rbx) - (1);
    if (condition_is_not_equal) goto loc_008DFE91;
loc_008DFEB1:
    result = (result) - (2);
    goto loc_008DFEC1;
loc_008DFEBC:
    if (v_rbx == 0) goto loc_008DFEB1;
loc_008DFEC1:
    v_rbx = 0;
    *(unsigned __int16 *)(result) = 0;
loc_008DFEC6:
    if (sign_flag) goto loc_008E0141;
loc_008DFECE:
    if (sign_flag) goto loc_008E0022;
loc_008DFED6:
    if (((unsigned int)((unsigned int)(v_stack_m98))) <= 0) goto loc_008DFF20;
    result = (unsigned int)(v_stack_m98);
    if (0 != 0) {
        a2 = 0x58706E50ULL;
        a1 = 0;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(v_stack_m98))), (unsigned int)(0x58706E50ULL), a4);
    if (result == 0) goto loc_008E0161;
loc_008DFF20:
    v_stack_m98 = 0;
    if ((unsigned int)((unsigned int)(a2)) == 0) goto loc_008E00F8;
    v_rsi = 0;
    v_stack_m78 = v_stack_p18;
    v_stack_m70 = a6;
    v_stack_m68 = v_stack_p20;
    v_stack_m88 = 0;
    v_stack_m80 = 0;
    v_stack_m4C = 0;
    v_stack_m60 = v_stack_m94;
    v_stack_m48 = v_stack_m98;
    v_stack_m40 = 0;
    v_stack_m58 = result;
    v_stack_m50 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m98))));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5792863) + 488) == 0) goto loc_008E003A;
    v_stack_mD0 = v_stack_m88;
    v_stack_mD8 = 1;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5792863) + 488)) != (v_rip + 10544)) goto loc_008E01A1;
    result = PiPnpRtlObjectActionCallback(*(unsigned __int64 *)(v_rip + 5792863), v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), v_rsi + 8);
loc_008DFFB5:
    if (((unsigned int)(result)) == 0xC0000002ULL) goto loc_008E00F0;
    if (((unsigned int)(result)) != 0xC0000120ULL) goto loc_008E0032;
loc_008DFFCA:
    v_rbx = 0;
loc_008DFFD0:
    if (((unsigned int)((unsigned int)(v_stack_m88))) == 0xC0000023ULL) goto loc_008DFED6;
    if (sign_flag) goto loc_008E0010;
    *(unsigned int *)(a7 + 32) = (unsigned int)((unsigned int)(v_stack_m94));
    *(unsigned int *)(a7 + 36) = (unsigned int)((unsigned int)(v_stack_m98));
    *(unsigned __int64 *)(a7 + 40) = result;
loc_008DFFF2:
loc_008DFFF4:
    v_rsp = (v_rsp) + (192);
    return (unsigned int)((unsigned int)((unsigned int)(v_stack_m88)));
loc_008E0010:
    result = (unsigned int)((unsigned int)((unsigned int)(v_stack_m88)));
    if (result != 0) {
        a2 = 0x58706E50ULL;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a2))), v_rsi + 8);
    }
    if (((unsigned int)((unsigned int)(v_stack_m88))) != 0xC0000225ULL) goto loc_008E0166;
    goto loc_008DFFF4;
loc_008E0032:
    if ((unsigned int)((unsigned int)((unsigned int)(v_stack_p10))) != 0) goto loc_008E00E6;
loc_008E003A:
    v_stack_p50 = (unsigned int)((unsigned int)(v_stack_m40));
    v_stack_p48 = v_stack_m48;
    v_stack_p40 = (unsigned int)((unsigned int)(v_stack_m50));
    v_stack_p38 = v_stack_m58;
    v_stack_p30 = v_stack_m60;
    v_stack_p28 = v_stack_m68;
    v_stack_p20 = v_stack_m70;
    result = PnpGetObjectPropertyWorker(a6, v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), v_stack_m78);
    if (v_stack_p10 == 0) goto loc_008DFFCA;
    v_stack_m88 = (unsigned int)(result);
    v_stack_p28 = v_stack_m88;
    v_stack_p20 = 2;
    if (v_stack_p10 != (v_rip + 10150)) goto loc_008E01AE;
    result = PiPnpRtlObjectActionCallback(a6, v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), 8);
loc_008E00CC:
    if (((unsigned int)(result)) == 0xC0000002ULL) goto loc_008DFFCA;
    if (((unsigned int)(result)) == 0xC0000120ULL) goto loc_008E0132;
    if ((unsigned int)(result) == 0) goto loc_008DFFCA;
loc_008E00E6:
    goto loc_008DFFCA;
loc_008E00F0:
    goto loc_008E003A;
loc_008E00F8:
    v_stack_p38 = v_stack_m98;
    v_stack_p30 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m98))));
    v_stack_p28 = result;
    v_stack_p20 = v_stack_m94;
    result = PnpGetGenericStoreProperty(*(unsigned __int64 *)(v_rip + 5792394), v_stack_p18, a6, v_stack_p20);
    goto loc_008DFFD0;
loc_008E0132:
    goto loc_008DFFCA;
loc_008E013A:
loc_008E013F:
    v_rbx = 0;
loc_008E0141:
    if (*(unsigned __int64 *)(a7 + 24) == 0) goto loc_008DFECE;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(a7 + 24), (unsigned int)(0x58706E50ULL), a6, v_stack_p20);
    *(unsigned __int64 *)(a7 + 24) = 0;
    goto loc_008DFECE;
loc_008E0161:
loc_008E0166:
    if (*(unsigned __int64 *)(a7 + 24) == 0) goto loc_008DFFF2;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(a7 + 24), (unsigned int)(0x58706E50ULL), a6, v_stack_p20);
    goto loc_008DFFF2;
loc_008E0182:
    goto loc_008E013F;
loc_008E0189:
    v_rbx = 0;
    *(unsigned __int16 *)(result) = 0;
    goto loc_008DFEC6;
loc_008E01A1:
    result = guard_dispatch_icall(*(unsigned __int64 *)(a7 + 24), (unsigned int)(0x58706E50ULL), a6, v_stack_p20);
    goto loc_008DFFB5;
loc_008E01AE:
    result = guard_dispatch_icall(*(unsigned __int64 *)(a7 + 24), (unsigned int)(0x58706E50ULL), a6, v_stack_p20);
    goto loc_008E00CC;
}
```

## 5. (Beta) C Style

```c
int64_t PiDqPnPGetObjectProperty(int64_t Arg1, int32_t Arg2, int64_t Arg3, void *Arg4, uint32_t Arg5, int64_t Arg6, void *Arg7)
{
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg7 = (uint8_t *)Arg7;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m47;
    uint64_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint32_t v_stack_m94;
    uint32_t v_stack_m98;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint32_t v_stack_p40;
    uint64_t v_stack_p48;
    uint32_t v_stack_p50;
    uint64_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (192);
    local_rbx = 0;
    v_stack_m98 = 512;
    v_stack_m94 = 0;
    *(uint64_t *)(arg7) = v_xmm0;
    *(uint32_t *)(arg7 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)));
    *(uint32_t *)(arg7 + 0x14) = (uint32_t)((uint32_t)(Arg5));
    *(uint64_t *)(arg7 + 0x20) = 0;
    *(uint64_t *)(arg7 + 0x28) = 0;
    *(uint64_t *)(arg7 + 0x18) = 0;
    if (Arg6 == 0) goto loc_008DFECE;
loc_008DFE10:
    if ((*(uint16_t *)(Arg6)) == 0) goto loc_008DFE1F;
    result = (Arg6) + (2);
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(0x7FFFFFFFULL)))) - (1);
    if (condition_is_not_equal) goto loc_008DFE10;
loc_008DFE1F:
    local_rsi = (uint32_t)(0xC000000DULL);
    if (Arg1 != 0) { local_rsi = 0; }
    if (Arg1 == 0) goto loc_008E0141;
    Arg2 = ((uint32_t)(0x7FFFFFFFULL)) - (Arg1);
    if (condition_is_equal) goto loc_008DFECE;
    if (Arg2 != 0) goto loc_008E013A;
    result = ExAllocatePool2(256, 2, (uint32_t)(0x58706E50ULL), Arg4);
    *(uint64_t *)(arg7 + 0x18) = result;
    if (result == 0) goto loc_008E0182;
    local_rbx = (2) >> (1);
    if ((local_rbx - 1) > ((uint32_t)(0x7FFFFFFEULL))) goto loc_008E0189;
    local_rsi = 0;
    Arg2 = ((uint32_t)(0x7FFFFFFEULL)) - (local_rbx);
    Arg3 = (Arg6) - (result);
loc_008DFE91:
    if (Arg2 + local_rbx * 1 == 0) goto loc_008DFEC1;
    if ((uint16_t)(*(uint16_t *)(Arg3 + result * 1)) == 0) goto loc_008DFEBC;
    *(uint16_t *)(result) = (uint16_t)(*(uint16_t *)(Arg3 + result * 1));
    result = (result) + (2);
    local_rbx = (local_rbx) - (1);
    if (condition_is_not_equal) goto loc_008DFE91;
loc_008DFEB1:
    result = (result) - (2);
    goto loc_008DFEC1;
loc_008DFEBC:
    if (local_rbx == 0) goto loc_008DFEB1;
loc_008DFEC1:
    local_rbx = 0;
    *(uint16_t *)(result) = 0;
loc_008DFEC6:
    if (sign_flag) goto loc_008E0141;
loc_008DFECE:
    if (sign_flag) goto loc_008E0022;
loc_008DFED6:
    if (((uint32_t)((uint32_t)(v_stack_m98))) <= 0) goto loc_008DFF20;
    result = (uint32_t)(v_stack_m98);
    if (0 != 0) {
        Arg2 = 0x58706E50ULL;
        Arg1 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(v_stack_m98))), (uint32_t)(0x58706E50ULL), Arg4);
    if (result == 0) goto loc_008E0161;
loc_008DFF20:
    v_stack_m98 = 0;
    if ((uint32_t)((uint32_t)(Arg2)) == 0) goto loc_008E00F8;
    local_rsi = 0;
    v_stack_m78 = v_stack_p18;
    v_stack_m70 = Arg6;
    v_stack_m68 = v_stack_p20;
    v_stack_m88 = 0;
    v_stack_m80 = 0;
    v_stack_m4C = 0;
    v_stack_m60 = v_stack_m94;
    v_stack_m48 = v_stack_m98;
    v_stack_m40 = 0;
    v_stack_m58 = result;
    v_stack_m50 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m98))));
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x58645F) + 0x1E8) == 0) goto loc_008E003A;
    v_stack_mD0 = v_stack_m88;
    v_stack_mD8 = 1;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x58645F) + 0x1E8)) != (v_rip + 10544)) goto loc_008E01A1;
    result = PiPnpRtlObjectActionCallback(*(uint64_t *)(v_rip + 0x58645F), v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), local_rsi + 8);
loc_008DFFB5:
    if (((uint32_t)(result)) == 0xC0000002ULL) goto loc_008E00F0;
    if (((uint32_t)(result)) != 0xC0000120ULL) goto loc_008E0032;
loc_008DFFCA:
    local_rbx = 0;
loc_008DFFD0:
    if (((uint32_t)((uint32_t)(v_stack_m88))) == 0xC0000023ULL) goto loc_008DFED6;
    if (sign_flag) goto loc_008E0010;
    *(uint32_t *)(arg7 + 0x20) = (uint32_t)((uint32_t)(v_stack_m94));
    *(uint32_t *)(arg7 + 0x24) = (uint32_t)((uint32_t)(v_stack_m98));
    *(uint64_t *)(arg7 + 0x28) = result;
loc_008DFFF2:
loc_008DFFF4:
    local_rsp = (local_rsp) + (192);
    return (uint32_t)((uint32_t)((uint32_t)(v_stack_m88)));
loc_008E0010:
    result = (uint32_t)((uint32_t)((uint32_t)(v_stack_m88)));
    if (result != 0) {
        Arg2 = 0x58706E50ULL;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg2))), local_rsi + 8);
    }
    if (((uint32_t)((uint32_t)(v_stack_m88))) != 0xC0000225ULL) goto loc_008E0166;
    goto loc_008DFFF4;
loc_008E0032:
    if ((uint32_t)((uint32_t)((uint32_t)(v_stack_p10))) != 0) goto loc_008E00E6;
loc_008E003A:
    v_stack_p50 = (uint32_t)((uint32_t)(v_stack_m40));
    v_stack_p48 = v_stack_m48;
    v_stack_p40 = (uint32_t)((uint32_t)(v_stack_m50));
    v_stack_p38 = v_stack_m58;
    v_stack_p30 = v_stack_m60;
    v_stack_p28 = v_stack_m68;
    v_stack_p20 = v_stack_m70;
    result = PnpGetObjectPropertyWorker(Arg6, v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), v_stack_m78);
    if (v_stack_p10 == 0) goto loc_008DFFCA;
    v_stack_m88 = (uint32_t)(result);
    v_stack_p28 = v_stack_m88;
    v_stack_p20 = 2;
    if (v_stack_p10 != (v_rip + 10150)) goto loc_008E01AE;
    result = PiPnpRtlObjectActionCallback(Arg6, v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), 8);
loc_008E00CC:
    if (((uint32_t)(result)) == 0xC0000002ULL) goto loc_008DFFCA;
    if (((uint32_t)(result)) == 0xC0000120ULL) goto loc_008E0132;
    if ((uint32_t)(result) == 0) goto loc_008DFFCA;
loc_008E00E6:
    goto loc_008DFFCA;
loc_008E00F0:
    goto loc_008E003A;
loc_008E00F8:
    v_stack_p38 = v_stack_m98;
    v_stack_p30 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m98))));
    v_stack_p28 = result;
    v_stack_p20 = v_stack_m94;
    result = PnpGetGenericStoreProperty(*(uint64_t *)(v_rip + 0x58628A), v_stack_p18, Arg6, v_stack_p20);
    goto loc_008DFFD0;
loc_008E0132:
    goto loc_008DFFCA;
loc_008E013A:
loc_008E013F:
    local_rbx = 0;
loc_008E0141:
    if (*(uint64_t *)(arg7 + 0x18) == 0) goto loc_008DFECE;
    result = ExFreePoolWithTag(*(uint64_t *)(arg7 + 0x18), (uint32_t)(0x58706E50ULL), Arg6, v_stack_p20);
    *(uint64_t *)(arg7 + 0x18) = 0;
    goto loc_008DFECE;
loc_008E0161:
loc_008E0166:
    if (*(uint64_t *)(arg7 + 0x18) == 0) goto loc_008DFFF2;
    result = ExFreePoolWithTag(*(uint64_t *)(arg7 + 0x18), (uint32_t)(0x58706E50ULL), Arg6, v_stack_p20);
    goto loc_008DFFF2;
loc_008E0182:
    goto loc_008E013F;
loc_008E0189:
    local_rbx = 0;
    *(uint16_t *)(result) = 0;
    goto loc_008DFEC6;
loc_008E01A1:
    result = guard_dispatch_icall(*(uint64_t *)(arg7 + 0x18), (uint32_t)(0x58706E50ULL), Arg6, v_stack_p20);
    goto loc_008DFFB5;
loc_008E01AE:
    result = guard_dispatch_icall(*(uint64_t *)(arg7 + 0x18), (uint32_t)(0x58706E50ULL), Arg6, v_stack_p20);
    goto loc_008E00CC;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x0` | `128` | `R` |
| `Arg4` | `+ 0x10` | `32` | `R` |
| `Arg7` | `+ 0x0` | `128` | `R` |
| `Arg7` | `+ 0x10` | `32` | `W` |
| `Arg7` | `+ 0x14` | `32` | `W` |
| `Arg7` | `+ 0x18` | `64` | `R` |
| `Arg7` | `+ 0x18` | `64` | `W` |
| `Arg7` | `+ 0x20` | `32` | `W` |
| `Arg7` | `+ 0x20` | `64` | `W` |
| `Arg7` | `+ 0x24` | `32` | `W` |
| `Arg7` | `+ 0x28` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008DFD90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
