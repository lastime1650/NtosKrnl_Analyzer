# HalpReportResourceUsage

- RVA: `0x00C1F034`–`0x00C1F63B` (길이 `1,543` bytes)
- VA: `0x0000000140C1F034`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C3DB8`
- 디코드: `388`개 명령, `1,543/1,543` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **18**; 고유 호출 대상: **11**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **12**

### Outgoing calls
- `0x00C1F07B` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00C1F0C0` → [HalpClaimDebugResource](../../text/54/HalpClaimDebugResource_function_00547AC4.md) (function, `0x00547AC4`)
- `0x00C1F0DD` → [HalpClaimDebugResource](../../text/54/HalpClaimDebugResource_function_00547AC4.md) (function, `0x00547AC4`)
- `0x00C1F0F9` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C1F10C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C1F1F6` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00C1F20A` → [KiCopyAffinityEx](../../text/2C/KiCopyAffinityEx_function_002CE860.md) (function, `0x002CE860`)
- `0x00C1F31F` → [RtlCmEncodeMemIoResource](../../text/5E/RtlCmEncodeMemIoResource_function_005E7BF0.md) (function, `0x005E7BF0`)
- `0x00C1F38F` → [HalTranslateBusAddress](../../text/46/HalTranslateBusAddress_function_004610B0.md) (function, `0x004610B0`)
- `0x00C1F47D` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C1F4C7` → [HalpGetResourceSortValue](HalpGetResourceSortValue_function_00C1EFE4.md) (function, `0x00C1EFE4`)
- `0x00C1F4EE` → [HalpGetResourceSortValue](HalpGetResourceSortValue_function_00C1EFE4.md) (function, `0x00C1EFE4`)
- `0x00C1F561` → [HalpGetResourceSortValue](HalpGetResourceSortValue_function_00C1EFE4.md) (function, `0x00C1EFE4`)
- `0x00C1F5CB` → [IoReportHalResourceUsage](../C3/IoReportHalResourceUsage_function_00C32FB0.md) (function, `0x00C32FB0`)
- `0x00C1F5D5` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C1F5DF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C1F5EE` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00C1F635` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [HalReportResourceUsage](HalReportResourceUsage_function_00C1DDC0.md) at `0x00C1DE03`

### Static image references
- `0x00C1F05A` → RVA `0x00E0A740` (`.data`; read)
- `0x00C1F080` → RVA `0x00E10320` (`.data`; read)
- `0x00C1F0B9` → RVA `0x00E0A798` (`.data`; read)
- `0x00C1F0C5` → RVA `0x00E10318` (`.data`; read)
- `0x00C1F0D6` → RVA `0x00E0A7C8` (`.data`; read)
- `0x00C1F13D` → RVA `0x010088D0` (`INITDATA`; read)
- `0x00C1F152` → RVA `0x01008AD1` (`INITDATA`; read)
- `0x00C1F193` → RVA `0x010086A8` (`INITDATA`; read)
- `0x00C1F1FF` → RVA `0x00FC7120` (`ALMOSTRO`; read)
- `0x00C1F20F` → RVA `0x00FC6A80` (`ALMOSTRO`; read)
- `0x00C1F244` → RVA `0x01008AD0` (`INITDATA`; read)
- `0x00C1F615` → RVA `0x00023DC8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **14**
  - `0x00C1F07B` → [memset](../../text/6C/memset_function_006C6C40.md) (`INIT` → `.text`)
  - `0x00C1F0C0` → [HalpClaimDebugResource](../../text/54/HalpClaimDebugResource_function_00547AC4.md) (`INIT` → `.text`)
  - `0x00C1F0DD` → [HalpClaimDebugResource](../../text/54/HalpClaimDebugResource_function_00547AC4.md) (`INIT` → `.text`)
  - `0x00C1F0F9` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C1F10C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C1F1F6` → [memset](../../text/6C/memset_function_006C6C40.md) (`INIT` → `.text`)
  - `0x00C1F20A` → [KiCopyAffinityEx](../../text/2C/KiCopyAffinityEx_function_002CE860.md) (`INIT` → `.text`)
  - `0x00C1F31F` → [RtlCmEncodeMemIoResource](../../text/5E/RtlCmEncodeMemIoResource_function_005E7BF0.md) (`INIT` → `.text`)
  - `0x00C1F38F` → [HalTranslateBusAddress](../../text/46/HalTranslateBusAddress_function_004610B0.md) (`INIT` → `.text`)
  - `0x00C1F47D` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C1F5D5` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C1F5DF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C1F5EE` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`INIT` → `.text`)
  - `0x00C1F635` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C1F034  48 8B C4                        mov rax, rsp
00C1F037  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00C1F03B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00C1F03F  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00C1F043  55                              push rbp
00C1F044  41 54                           push r12
00C1F046  41 55                           push r13
00C1F048  41 56                           push r14
00C1F04A  41 57                           push r15
00C1F04C  48 8D A8 E8 FE FF FF            lea rbp, [rax - 0x118]
00C1F053  48 81 EC F0 01 00 00            sub rsp, 0x1f0
00C1F05A  48 8B 05 DF B6 1E 00            mov rax, qword ptr [rip + 0x1eb6df]
00C1F061  48 33 C4                        xor rax, rsp
00C1F064  48 89 85 E0 00 00 00            mov qword ptr [rbp + 0xe0], rax
00C1F06B  48 89 4D C8                     mov qword ptr [rbp - 0x38], rcx
00C1F06F  33 D2                           xor edx, edx
00C1F071  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00C1F075  41 B8 08 01 00 00               mov r8d, 0x108
00C1F07B  E8 C0 7B AA FF                  call 0x1406c6c40
00C1F080  4C 8B 1D 99 12 1F 00            mov r11, qword ptr [rip + 0x1f1299]
00C1F087  33 DB                           xor ebx, ebx
00C1F089  33 C0                           xor eax, eax
00C1F08B  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
00C1F08F  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
00C1F094  0F 57 C0                        xorps xmm0, xmm0
00C1F097  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00C1F09B  89 5C 24 60                     mov dword ptr [rsp + 0x60], ebx
00C1F09F  48 89 5C 24 78                  mov qword ptr [rsp + 0x78], rbx
00C1F0A4  48 89 5D A8                     mov qword ptr [rbp - 0x58], rbx
00C1F0A8  89 5C 24 3C                     mov dword ptr [rsp + 0x3c], ebx
00C1F0AC  0F 11 44 24 48                  movups xmmword ptr [rsp + 0x48], xmm0
00C1F0B1  4D 85 DB                        test r11, r11
00C1F0B4  74 0F                           je 0x140c1f0c5
00C1F0B6  49 8B D3                        mov rdx, r11
00C1F0B9  48 8D 0D D8 B6 1E 00            lea rcx, [rip + 0x1eb6d8]
00C1F0C0  E8 FF 89 92 FF                  call 0x140547ac4
00C1F0C5  48 8B 15 4C 12 1F 00            mov rdx, qword ptr [rip + 0x1f124c]
00C1F0CC  48 85 D2                        test rdx, rdx
00C1F0CF  74 11                           je 0x140c1f0e2
00C1F0D1  49 3B D3                        cmp rdx, r11
00C1F0D4  74 0C                           je 0x140c1f0e2
00C1F0D6  48 8D 0D EB B6 1E 00            lea rcx, [rip + 0x1eb6eb]
00C1F0DD  E8 E2 89 92 FF                  call 0x140547ac4
00C1F0E2  41 BE 48 61 6C 6D               mov r14d, 0x6d6c6148
00C1F0E8  BF 00 20 00 00                  mov edi, 0x2000
00C1F0ED  BB 40 00 00 00                  mov ebx, 0x40
00C1F0F2  45 8B C6                        mov r8d, r14d
00C1F0F5  8B D7                           mov edx, edi
00C1F0F7  8B CB                           mov ecx, ebx
00C1F0F9  E8 F2 2F F6 FF                  call 0x140b820f0
00C1F0FE  45 8B C6                        mov r8d, r14d
00C1F101  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00C1F105  8B D7                           mov edx, edi
00C1F107  8B CB                           mov ecx, ebx
00C1F109  48 8B F0                        mov rsi, rax
00C1F10C  E8 DF 2F F6 FF                  call 0x140b820f0
00C1F111  45 33 D2                        xor r10d, r10d
00C1F114  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00C1F119  4C 8B E8                        mov r13, rax
00C1F11C  48 85 F6                        test rsi, rsi
00C1F11F  0F 84 F0 04 00 00               je 0x140c1f615
00C1F125  48 85 C0                        test rax, rax
00C1F128  0F 84 E7 04 00 00               je 0x140c1f615
00C1F12E  4C 8D 7E 04                     lea r15, [rsi + 4]
00C1F132  41 8B D2                        mov edx, r10d
00C1F135  41 83 0F FF                     or dword ptr [r15], 0xffffffff
00C1F139  4C 8D 60 04                     lea r12, [rax + 4]
00C1F13D  4C 8D 0D 8C 97 3E 00            lea r9, [rip + 0x3e978c]
00C1F144  4C 89 7D B0                     mov qword ptr [rbp - 0x50], r15
00C1F148  4D 8B F7                        mov r14, r15
00C1F14B  4C 89 65 A0                     mov qword ptr [rbp - 0x60], r12
00C1F14F  49 8B C9                        mov rcx, r9
00C1F152  4C 8D 05 78 99 3E 00            lea r8, [rip + 0x3e9978]
00C1F159  41 8D 5A 01                     lea ebx, [r10 + 1]
00C1F15D  84 19                           test byte ptr [rcx], bl
00C1F15F  75 06                           jne 0x140c1f167
00C1F161  C6 01 11                        mov byte ptr [rcx], 0x11
00C1F164  41 89 10                        mov dword ptr [r8], edx
00C1F167  03 D3                           add edx, ebx
00C1F169  48 03 CB                        add rcx, rbx
00C1F16C  49 83 C0 05                     add r8, 5
00C1F170  83 FA 30                        cmp edx, 0x30
00C1F173  72 E8                           jb 0x140c1f15d
00C1F175  4C 89 55 B8                     mov qword ptr [rbp - 0x48], r10
00C1F179  41 8A D2                        mov dl, r10b
00C1F17C  4C 89 55 80                     mov qword ptr [rbp - 0x80], r10
00C1F180  41 BB 20 00 00 00               mov r11d, 0x20
00C1F186  88 54 24 31                     mov byte ptr [rsp + 0x31], dl
00C1F18A  80 FA 02                        cmp dl, 2
00C1F18D  0F 83 F0 02 00 00               jae 0x140c1f483
00C1F193  48 8B 3D 0E 95 3E 00            mov rdi, qword ptr [rip + 0x3e950e]
00C1F19A  8A C2                           mov al, dl
00C1F19C  F6 D8                           neg al
00C1F19E  44 89 54 24 34                  mov dword ptr [rsp + 0x34], r10d
00C1F1A3  45 8B C2                        mov r8d, r10d
00C1F1A6  1A C9                           sbb cl, cl
00C1F1A8  80 E1 F0                        and cl, 0xf0
00C1F1AB  41 02 CB                        add cl, r11b
00C1F1AE  88 4C 24 30                     mov byte ptr [rsp + 0x30], cl
00C1F1B2  41 8B C2                        mov eax, r10d
00C1F1B5  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00C1F1B9  41 81 F8 FF 00 00 00            cmp r8d, 0xff
00C1F1C0  0F 87 EB 00 00 00               ja 0x140c1f2b1
00C1F1C6  45 8B E8                        mov r13d, r8d
00C1F1C9  43 84 0C 29                     test byte ptr [r9 + r13], cl
00C1F1CD  75 13                           jne 0x140c1f1e2
00C1F1CF  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
00C1F1D3  44 03 C3                        add r8d, ebx
00C1F1D6  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
00C1F1DB  44 89 44 24 34                  mov dword ptr [rsp + 0x34], r8d
00C1F1E0  EB D7                           jmp 0x140c1f1b9
00C1F1E2  33 D2                           xor edx, edx
00C1F1E4  48 C7 45 D0 01 00 20 00         mov qword ptr [rbp - 0x30], 0x200001
00C1F1EC  41 B8 00 01 00 00               mov r8d, 0x100
00C1F1F2  48 8D 4D D8                     lea rcx, [rbp - 0x28]
00C1F1F6  E8 45 7A AA FF                  call 0x1406c6c40
00C1F1FB  0F B7 55 D2                     movzx edx, word ptr [rbp - 0x2e]
00C1F1FF  4C 8D 05 1A 7F 3A 00            lea r8, [rip + 0x3a7f1a]
00C1F206  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00C1F20A  E8 51 F6 6A FF                  call 0x1402ce860
00C1F20F  8B 05 6B 78 3A 00               mov eax, dword ptr [rip + 0x3a786b]
00C1F215  4C 8D 05 B4 96 3E 00            lea r8, [rip + 0x3e96b4]
00C1F21C  47 8A 04 28                     mov r8b, byte ptr [r8 + r13]
00C1F220  66 C7 44 24 48 02 02            mov word ptr [rsp + 0x48], 0x202
00C1F227  41 80 E0 02                     and r8b, 2
00C1F22B  74 0A                           je 0x140c1f237
00C1F22D  66 89 5C 24 4A                  mov word ptr [rsp + 0x4a], bx
00C1F232  45 33 D2                        xor r10d, r10d
00C1F235  EB 09                           jmp 0x140c1f240
00C1F237  45 33 D2                        xor r10d, r10d
00C1F23A  66 44 89 54 24 4A               mov word ptr [rsp + 0x4a], r10w
00C1F240  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
00C1F244  4C 8D 0D 85 98 3E 00            lea r9, [rip + 0x3e9885]
00C1F24B  4A 8D 14 AD 00 00 00 00         lea rdx, [r13*4]
00C1F253  48 89 4D 94                     mov qword ptr [rbp - 0x6c], rcx
00C1F257  49 03 D5                        add rdx, r13
00C1F25A  66 44 89 54 24 4E               mov word ptr [rsp + 0x4e], r10w
00C1F260  45 84 C0                        test r8b, r8b
00C1F263  48 89 4C 24 54                  mov qword ptr [rsp + 0x54], rcx
00C1F268  44 8B 44 24 34                  mov r8d, dword ptr [rsp + 0x34]
00C1F26D  44 89 45 90                     mov dword ptr [rbp - 0x70], r8d
00C1F271  42 8B 44 0A 01                  mov eax, dword ptr [rdx + r9 + 1]
00C1F276  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00C1F27A  66 89 44 24 4C                  mov word ptr [rsp + 0x4c], ax
00C1F27F  41 8B C2                        mov eax, r10d
00C1F282  0F 95 C0                        setne al
00C1F285  66 C7 45 88 02 02               mov word ptr [rbp - 0x78], 0x202
00C1F28B  66 89 45 8A                     mov word ptr [rbp - 0x76], ax
00C1F28F  44 03 C3                        add r8d, ebx
00C1F292  42 0F B6 04 0A                  movzx eax, byte ptr [rdx + r9]
00C1F297  8B 55 98                        mov edx, dword ptr [rbp - 0x68]
00C1F29A  66 89 45 8C                     mov word ptr [rbp - 0x74], ax
00C1F29E  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
00C1F2A2  66 44 89 55 8E                  mov word ptr [rbp - 0x72], r10w
00C1F2A7  44 89 44 24 34                  mov dword ptr [rsp + 0x34], r8d
00C1F2AC  E9 13 01 00 00                  jmp 0x140c1f3c4
00C1F2B1  48 85 FF                        test rdi, rdi
00C1F2B4  0F 84 A3 01 00 00               je 0x140c1f45d
00C1F2BA  84 4F 0C                        test byte ptr [rdi + 0xc], cl
00C1F2BD  75 08                           jne 0x140c1f2c7
00C1F2BF  48 8B 3F                        mov rdi, qword ptr [rdi]
00C1F2C2  E9 EB FE FF FF                  jmp 0x140c1f1b2
00C1F2C7  44 8B C8                        mov r9d, eax
00C1F2CA  4D 03 C9                        add r9, r9
00C1F2CD  44 8B E8                        mov r13d, eax
00C1F2D0  4E 8B 44 CF 15                  mov r8, qword ptr [rdi + r9*8 + 0x15]
00C1F2D5  4D 85 C0                        test r8, r8
00C1F2D8  75 19                           jne 0x140c1f2f3
00C1F2DA  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
00C1F2DF  4C 8D 0D EA 95 3E 00            lea r9, [rip + 0x3e95ea]
00C1F2E6  48 8B 3F                        mov rdi, qword ptr [rdi]
00C1F2E9  44 8B 44 24 34                  mov r8d, dword ptr [rsp + 0x34]
00C1F2EE  E9 BF FE FF FF                  jmp 0x140c1f1b2
00C1F2F3  8B 4F 08                        mov ecx, dword ptr [rdi + 8]
00C1F2F6  8D 41 FF                        lea eax, [rcx - 1]
00C1F2F9  A9 F9 FF FF FF                  test eax, 0xfffffff9
00C1F2FE  0F 85 50 01 00 00               jne 0x140c1f454
00C1F304  83 F9 05                        cmp ecx, 5
00C1F307  0F 84 47 01 00 00               je 0x140c1f454
00C1F30D  4E 8B 4C CF 0D                  mov r9, qword ptr [rdi + r9*8 + 0xd]
00C1F312  8A D1                           mov dl, cl
00C1F314  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00C1F319  66 44 89 54 24 4A               mov word ptr [rsp + 0x4a], r10w
00C1F31F  E8 CC 88 9C FF                  call 0x1405e7bf0
00C1F324  45 33 DB                        xor r11d, r11d
00C1F327  85 C0                           test eax, eax
00C1F329  0F 88 39 01 00 00               js 0x140c1f468
00C1F32F  0F B6 4C 24 48                  movzx ecx, byte ptr [rsp + 0x48]
00C1F334  C6 44 24 49 02                  mov byte ptr [rsp + 0x49], 2
00C1F339  2B CB                           sub ecx, ebx
00C1F33B  74 1C                           je 0x140c1f359
00C1F33D  83 E9 02                        sub ecx, 2
00C1F340  74 05                           je 0x140c1f347
00C1F342  83 F9 04                        cmp ecx, 4
00C1F345  75 20                           jne 0x140c1f367
00C1F347  44 89 5C 24 3C                  mov dword ptr [rsp + 0x3c], r11d
00C1F34C  F6 47 0C 04                     test byte ptr [rdi + 0xc], 4
00C1F350  74 15                           je 0x140c1f367
00C1F352  66 09 5C 24 4A                  or word ptr [rsp + 0x4a], bx
00C1F357  EB 0E                           jmp 0x140c1f367
00C1F359  B8 11 00 00 00                  mov eax, 0x11
00C1F35E  89 5C 24 3C                     mov dword ptr [rsp + 0x3c], ebx
00C1F362  66 89 44 24 4A                  mov word ptr [rsp + 0x4a], ax
00C1F367  0F 10 44 24 48                  movups xmm0, xmmword ptr [rsp + 0x48]
00C1F36C  8B 44 24 58                     mov eax, dword ptr [rsp + 0x58]
00C1F370  4C 8D 4C 24 3C                  lea r9, [rsp + 0x3c]
00C1F375  4C 8B 44 24 4C                  mov r8, qword ptr [rsp + 0x4c]
00C1F37A  33 D2                           xor edx, edx
00C1F37C  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
00C1F380  33 C9                           xor ecx, ecx
00C1F382  48 8D 45 A8                     lea rax, [rbp - 0x58]
00C1F386  0F 11 45 88                     movups xmmword ptr [rbp - 0x78], xmm0
00C1F38A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C1F38F  E8 1C 1D 84 FF                  call 0x1404610b0
00C1F394  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
00C1F398  45 33 D2                        xor r10d, r10d
00C1F39B  48 89 45 8C                     mov qword ptr [rbp - 0x74], rax
00C1F39F  38 5C 24 48                     cmp byte ptr [rsp + 0x48], bl
00C1F3A3  75 0C                           jne 0x140c1f3b1
00C1F3A5  44 39 54 24 3C                  cmp dword ptr [rsp + 0x3c], r10d
00C1F3AA  75 05                           jne 0x140c1f3b1
00C1F3AC  66 44 89 55 8A                  mov word ptr [rbp - 0x76], r10w
00C1F3B1  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
00C1F3B5  44 8B 44 24 34                  mov r8d, dword ptr [rsp + 0x34]
00C1F3BA  03 C3                           add eax, ebx
00C1F3BC  8B 54 24 64                     mov edx, dword ptr [rsp + 0x64]
00C1F3C0  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00C1F3C4  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
00C1F3C8  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
00C1F3CD  4C 8B 4D A0                     mov r9, qword ptr [rbp - 0x60]
00C1F3D1  44 39 11                        cmp dword ptr [rcx], r10d
00C1F3D4  74 30                           je 0x140c1f406
00C1F3D6  01 1E                           add dword ptr [rsi], ebx
00C1F3D8  49 8D 49 08                     lea rcx, [r9 + 8]
00C1F3DC  41 01 5D 00                     add dword ptr [r13], ebx
00C1F3E0  45 33 DB                        xor r11d, r11d
00C1F3E3  45 89 1E                        mov dword ptr [r14], r11d
00C1F3E6  45 89 19                        mov dword ptr [r9], r11d
00C1F3E9  4D 8D 5E 08                     lea r11, [r14 + 8]
00C1F3ED  4C 89 75 B0                     mov qword ptr [rbp - 0x50], r14
00C1F3F1  49 83 C1 10                     add r9, 0x10
00C1F3F5  49 83 C6 10                     add r14, 0x10
00C1F3F9  4C 89 5D B8                     mov qword ptr [rbp - 0x48], r11
00C1F3FD  45 33 D2                        xor r10d, r10d
00C1F400  48 89 4D 80                     mov qword ptr [rbp - 0x80], rcx
00C1F404  EB 08                           jmp 0x140c1f40e
00C1F406  4C 8B 5D B8                     mov r11, qword ptr [rbp - 0x48]
00C1F40A  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
00C1F40E  41 01 5B 04                     add dword ptr [r11 + 4], ebx
00C1F412  41 BB 20 00 00 00               mov r11d, 0x20
00C1F418  01 59 04                        add dword ptr [rcx + 4], ebx
00C1F41B  0F 10 44 24 48                  movups xmm0, xmmword ptr [rsp + 0x48]
00C1F420  8B 4C 24 58                     mov ecx, dword ptr [rsp + 0x58]
00C1F424  41 0F 11 06                     movups xmmword ptr [r14], xmm0
00C1F428  41 89 4E 10                     mov dword ptr [r14 + 0x10], ecx
00C1F42C  49 83 C6 14                     add r14, 0x14
00C1F430  0F 10 45 88                     movups xmm0, xmmword ptr [rbp - 0x78]
00C1F434  8A 4C 24 30                     mov cl, byte ptr [rsp + 0x30]
00C1F438  41 0F 11 01                     movups xmmword ptr [r9], xmm0
00C1F43C  41 89 51 10                     mov dword ptr [r9 + 0x10], edx
00C1F440  49 83 C1 14                     add r9, 0x14
00C1F444  4C 89 4D A0                     mov qword ptr [rbp - 0x60], r9
00C1F448  4C 8D 0D 81 94 3E 00            lea r9, [rip + 0x3e9481]
00C1F44F  E9 65 FD FF FF                  jmp 0x140c1f1b9
00C1F454  8A 4C 24 30                     mov cl, byte ptr [rsp + 0x30]
00C1F458  E9 7D FE FF FF                  jmp 0x140c1f2da
00C1F45D  8A 54 24 31                     mov dl, byte ptr [rsp + 0x31]
00C1F461  02 D3                           add dl, bl
00C1F463  E9 1E FD FF FF                  jmp 0x140c1f186
00C1F468  4C 63 C0                        movsxd r8, eax
00C1F46B  4C 8B CF                        mov r9, rdi
00C1F46E  BA 0F 01 00 00                  mov edx, 0x10f
00C1F473  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00C1F478  B9 5C 00 00 00                  mov ecx, 0x5c
00C1F47D  E8 DE E1 8D FF                  call 0x1404fd660
00C1F482  CC                              int3
00C1F483  44 2B F6                        sub r14d, esi
00C1F486  44 89 54 24 34                  mov dword ptr [rsp + 0x34], r10d
00C1F48B  4C 89 75 80                     mov qword ptr [rbp - 0x80], r14
00C1F48F  45 8B F2                        mov r14d, r10d
00C1F492  44 39 16                        cmp dword ptr [rsi], r10d
00C1F495  0F 86 22 01 00 00               jbe 0x140c1f5bd
00C1F49B  33 C0                           xor eax, eax
00C1F49D  4D 8D 57 10                     lea r10, [r15 + 0x10]
00C1F4A1  49 83 C4 10                     add r12, 0x10
00C1F4A5  45 8B 7F 0C                     mov r15d, dword ptr [r15 + 0xc]
00C1F4A9  44 8B D8                        mov r11d, eax
00C1F4AC  44 89 7C 24 64                  mov dword ptr [rsp + 0x64], r15d
00C1F4B1  45 85 FF                        test r15d, r15d
00C1F4B4  0F 84 EA 00 00 00               je 0x140c1f5a4
00C1F4BA  4C 8D 44 24 70                  lea r8, [rsp + 0x70]
00C1F4BF  49 8B CA                        mov rcx, r10
00C1F4C2  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
00C1F4C7  E8 18 FB FF FF                  call 0x140c1efe4
00C1F4CC  8B 74 24 74                     mov esi, dword ptr [rsp + 0x74]
00C1F4D0  45 8B F7                        mov r14d, r15d
00C1F4D3  44 8B 7C 24 40                  mov r15d, dword ptr [rsp + 0x40]
00C1F4D8  45 2B F3                        sub r14d, r11d
00C1F4DB  49 8B FA                        mov rdi, r10
00C1F4DE  4D 8B EC                        mov r13, r12
00C1F4E1  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
00C1F4E6  48 8B CF                        mov rcx, rdi
00C1F4E9  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
00C1F4EE  E8 F1 FA FF FF                  call 0x140c1efe4
00C1F4F3  44 39 7C 24 60                  cmp dword ptr [rsp + 0x60], r15d
00C1F4F8  72 18                           jb 0x140c1f512
00C1F4FA  75 73                           jne 0x140c1f56f
00C1F4FC  39 74 24 7C                     cmp dword ptr [rsp + 0x7c], esi
00C1F500  75 0E                           jne 0x140c1f510
00C1F502  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
00C1F506  39 44 24 78                     cmp dword ptr [rsp + 0x78], eax
00C1F50A  72 06                           jb 0x140c1f512
00C1F50C  39 74 24 7C                     cmp dword ptr [rsp + 0x7c], esi
00C1F510  7D 5D                           jge 0x140c1f56f
00C1F512  41 8B 4A 10                     mov ecx, dword ptr [r10 + 0x10]
00C1F516  4C 8D 44 24 70                  lea r8, [rsp + 0x70]
00C1F51B  0F 10 07                        movups xmm0, xmmword ptr [rdi]
00C1F51E  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
00C1F523  41 0F 10 0A                     movups xmm1, xmmword ptr [r10]
00C1F527  41 0F 11 02                     movups xmmword ptr [r10], xmm0
00C1F52B  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
00C1F52E  41 89 42 10                     mov dword ptr [r10 + 0x10], eax
00C1F532  0F 11 0F                        movups xmmword ptr [rdi], xmm1
00C1F535  89 4F 10                        mov dword ptr [rdi + 0x10], ecx
00C1F538  41 8B 4C 24 10                  mov ecx, dword ptr [r12 + 0x10]
00C1F53D  41 0F 10 45 00                  movups xmm0, xmmword ptr [r13]
00C1F542  41 0F 10 0C 24                  movups xmm1, xmmword ptr [r12]
00C1F547  41 0F 11 04 24                  movups xmmword ptr [r12], xmm0
00C1F54C  41 8B 45 10                     mov eax, dword ptr [r13 + 0x10]
00C1F550  41 89 44 24 10                  mov dword ptr [r12 + 0x10], eax
00C1F555  41 0F 11 4D 00                  movups xmmword ptr [r13], xmm1
00C1F55A  41 89 4D 10                     mov dword ptr [r13 + 0x10], ecx
00C1F55E  49 8B CA                        mov rcx, r10
00C1F561  E8 7E FA FF FF                  call 0x140c1efe4
00C1F566  8B 74 24 74                     mov esi, dword ptr [rsp + 0x74]
00C1F56A  44 8B 7C 24 40                  mov r15d, dword ptr [rsp + 0x40]
00C1F56F  48 83 C7 14                     add rdi, 0x14
00C1F573  49 83 C5 14                     add r13, 0x14
00C1F577  4C 2B F3                        sub r14, rbx
00C1F57A  0F 85 61 FF FF FF               jne 0x140c1f4e1
00C1F580  44 8B 7C 24 64                  mov r15d, dword ptr [rsp + 0x64]
00C1F585  49 83 C2 14                     add r10, 0x14
00C1F589  49 83 C4 14                     add r12, 0x14
00C1F58D  44 03 DB                        add r11d, ebx
00C1F590  45 3B DF                        cmp r11d, r15d
00C1F593  0F 82 21 FF FF FF               jb 0x140c1f4ba
00C1F599  48 8B 75 C0                     mov rsi, qword ptr [rbp - 0x40]
00C1F59D  33 C0                           xor eax, eax
00C1F59F  44 8B 74 24 34                  mov r14d, dword ptr [rsp + 0x34]
00C1F5A4  44 03 F3                        add r14d, ebx
00C1F5A7  4D 8B FA                        mov r15, r10
00C1F5AA  44 89 74 24 34                  mov dword ptr [rsp + 0x34], r14d
00C1F5AF  44 3B 36                        cmp r14d, dword ptr [rsi]
00C1F5B2  0F 82 E5 FE FF FF               jb 0x140c1f49d
00C1F5B8  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
00C1F5BD  44 8B 4D 80                     mov r9d, dword ptr [rbp - 0x80]
00C1F5C1  4D 8B C5                        mov r8, r13
00C1F5C4  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
00C1F5C8  48 8B D6                        mov rdx, rsi
00C1F5CB  E8 E0 39 01 00                  call 0x140c32fb0
00C1F5D0  33 D2                           xor edx, edx
00C1F5D2  48 8B CE                        mov rcx, rsi
00C1F5D5  E8 96 32 F6 FF                  call 0x140b82870
00C1F5DA  33 D2                           xor edx, edx
00C1F5DC  49 8B CD                        mov rcx, r13
00C1F5DF  E8 8C 32 F6 FF                  call 0x140b82870
00C1F5E4  48 8B 8D E0 00 00 00            mov rcx, qword ptr [rbp + 0xe0]
00C1F5EB  48 33 CC                        xor rcx, rsp
00C1F5EE  E8 4D D0 A8 FF                  call 0x1406ac640
00C1F5F3  4C 8D 9C 24 F0 01 00 00         lea r11, [rsp + 0x1f0]
00C1F5FB  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00C1F5FF  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00C1F603  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00C1F607  49 8B E3                        mov rsp, r11
00C1F60A  41 5F                           pop r15
00C1F60C  41 5E                           pop r14
00C1F60E  41 5D                           pop r13
00C1F610  41 5C                           pop r12
00C1F612  5D                              pop rbp
00C1F613  C3                              ret
00C1F614  CC                              int3
00C1F615  4C 8D 0D AC 47 40 FF            lea r9, [rip - 0xbfb854]
00C1F61C  48 C7 44 24 20 8E 01 00 00      mov qword ptr [rsp + 0x20], 0x18e
00C1F625  BA 00 40 00 00                  mov edx, 0x4000
00C1F62A  B9 AC 00 00 00                  mov ecx, 0xac
00C1F62F  41 B8 01 00 00 00               mov r8d, 1
00C1F635  E8 26 E0 8D FF                  call 0x1404fd660
00C1F63A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpReportResourceUsage(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m19C;
    unsigned __int64 v_stack_m1A0;
    unsigned int v_stack_m1A4;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned int v_stack_m1B4;
    unsigned int v_stack_m1B8;
    unsigned int v_stack_m1C0;
    unsigned __int64 v_stack_m1C4;
    unsigned int v_stack_m1C8;
    unsigned __int16 v_stack_m1CA;
    unsigned __int16 v_stack_m1CC;
    unsigned __int16 v_stack_m1CE;
    unsigned __int8 v_stack_m1CF;
    unsigned __int64 v_stack_m1D0;
    unsigned int v_stack_m1D8;
    unsigned int v_stack_m1DC;
    unsigned int v_stack_m1E0;
    unsigned int v_stack_m1E4;
    unsigned __int8 v_stack_m1E7;
    unsigned __int8 v_stack_m1E8;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m28;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (496);
    result = (*(unsigned __int64 *)(v_rip + 2012895)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 280 + 224) = result;
    *(unsigned __int64 *)(v_rsp - 280 - 56) = a1;
    a2 = 0;
    result = memset(v_rsp - 280 - 48, a2, 264, a4);
    v_rbx = 0;
    result = 0;
    v_stack_m1D8 = 0;
    v_stack_m1A8 = 0;
    v_stack_m1C0 = 0;
    v_stack_m1B8 = 0;
    v_stack_m1A0 = 0;
    *(unsigned __int64 *)(v_rsp - 280 - 88) = 0;
    v_stack_m1DC = 0;
    v_stack_m1D0 = v_xmm0;
    if (*(unsigned __int64 *)(v_rip + 2036377) != 0) {
        a2 = *(unsigned __int64 *)(v_rip + 2036377);
        a1 = v_rip + 2012888;
        result = HalpClaimDebugResource(a1, a2, 264, a4);
    }
    if (*(unsigned __int64 *)(v_rip + 2036300) == 0) goto loc_00C1F0E2;
    if ((*(unsigned __int64 *)(v_rip + 2036300)) != (*(unsigned __int64 *)(v_rip + 2036377))) {
        a1 = v_rip + 2012907;
        result = HalpClaimDebugResource(a1, *(unsigned __int64 *)(v_rip + 2036300), 264, a4);
    }
    result = ExAllocatePool2(64, (unsigned int)((unsigned int)((unsigned int)(0x2000ULL))), (unsigned int)((unsigned int)((unsigned int)(0x6D6C6148ULL))), a4);
    *(unsigned __int64 *)(v_rsp - 280 - 64) = result;
    result = ExAllocatePool2(64, (unsigned int)((unsigned int)((unsigned int)(0x2000ULL))), (unsigned int)((unsigned int)((unsigned int)(0x6D6C6148ULL))), a4);
    v_r10 = 0;
    v_stack_m1B0 = result;
    if (result == 0) goto loc_00C1F615;
    if (result == 0) goto loc_00C1F615;
    *(unsigned __int64 *)(v_rsp - 280 - 80) = result + 4;
    *(unsigned __int64 *)(v_rsp - 280 - 96) = result + 4;
loc_00C1F15D:
    if (((*(unsigned __int8 *)(v_rip + 4102028)) & ((unsigned __int8)(v_r10 + 1))) == 0) {
        *(unsigned __int8 *)(v_rip + 4102028) = 17;
        *(unsigned int *)(v_rip + 4102520) = 0;
    }
    a2 = (unsigned int)((0) + ((unsigned int)(v_r10 + 1)));
    a1 = (v_rip + 4102028) + (v_r10 + 1);
    a3 = (v_rip + 4102520) + (5);
    if (a2 < 48) goto loc_00C1F15D;
    *(unsigned __int64 *)(v_rsp - 280 - 72) = 0;
    *(unsigned __int64 *)(v_rsp - 280 - 128) = 0;
loc_00C1F186:
    v_stack_m1E7 = 0;
    if (0 >= 2) goto loc_00C1F483;
    result = (unsigned __int8)(-(0));
    v_stack_m1E4 = 0;
    a1 = (unsigned __int8)((a1) & (240));
    a1 = (unsigned __int8)((a1) + (32));
    v_stack_m1E8 = (unsigned __int8)(a1);
loc_00C1F1B2:
    v_stack_m1E0 = 0;
loc_00C1F1B9:
    if (0 > 255) goto loc_00C1F2B1;
    if (((*(unsigned __int8 *)(v_rip + 4102028 + 0 * 1)) & ((unsigned __int8)(a1))) != 0) goto loc_00C1F1E2;
    a3 = (unsigned int)((0) + ((unsigned int)(v_r10 + 1)));
    v_stack_m1E4 = (unsigned int)(a3);
    goto loc_00C1F1B9;
loc_00C1F1E2:
    a2 = 0;
    *(unsigned __int64 *)(v_rsp - 280 - 48) = 0x200001ULL;
    result = memset(v_rsp - 280 - 40, a2, 256, v_rip + 4102028);
    result = KiCopyAffinityEx(v_rsp - 280 - 48, *(unsigned __int16 *)(v_rsp - 280 - 46), v_rip + 3833626, v_rip + 4102028);
    v_stack_m1D0 = 514;
    a3 = (unsigned __int8)((*(unsigned __int8 *)(v_rip + 4101812 + v_stack_m1B0 * 1)) & (2));
    if (condition_is_equal) goto loc_00C1F237;
    v_stack_m1CE = (unsigned __int16)(v_r10 + 1);
    v_r10 = 0;
    goto loc_00C1F240;
loc_00C1F237:
    v_r10 = 0;
    v_stack_m1CE = 0;
loc_00C1F240:
    *(unsigned __int64 *)(v_rsp - 280 - 108) = *(unsigned __int64 *)(v_rsp - 280 - 40);
    a2 = (v_stack_m1B0 * 4) + (v_stack_m1B0);
    v_stack_m1CA = 0;
    v_stack_m1C4 = *(unsigned __int64 *)(v_rsp - 280 - 40);
    *(unsigned int *)(v_rsp - 280 - 112) = (unsigned int)((unsigned int)(v_stack_m1E4));
    v_stack_m1C8 = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + v_rip + 4102277 * 1 + 1)));
    v_stack_m1CC = (unsigned __int16)((unsigned int)(*(unsigned int *)(a2 + v_rip + 4102277 * 1 + 1)));
    result = ((unsigned __int8)(a3) != 0) ? 1 : 0;
    *(unsigned __int16 *)(v_rsp - 280 - 120) = 514;
    *(unsigned __int16 *)(v_rsp - 280 - 118) = (unsigned __int16)(result);
    a3 = (unsigned int)(((unsigned int)(v_stack_m1E4)) + ((unsigned int)(v_r10 + 1)));
    *(unsigned __int16 *)(v_rsp - 280 - 116) = (unsigned __int16)(*(unsigned __int8 *)(a2 + v_rip + 4102277 * 1));
    *(unsigned __int16 *)(v_rsp - 280 - 114) = 0;
    v_stack_m1E4 = (unsigned int)(a3);
    goto loc_00C1F3C4;
loc_00C1F2B1:
    if (*(unsigned __int64 *)(v_rip + 4101390) == 0) goto loc_00C1F45D;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 4101390) + 12)) & ((unsigned __int8)(*(unsigned __int64 *)(v_rsp - 280 - 40)))) != 0) goto loc_00C1F2C7;
    goto loc_00C1F1B2;
loc_00C1F2C7:
    a4 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_m1E0)))) + ((unsigned int)((unsigned int)((unsigned int)(v_stack_m1E0))));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4101390)) + a4 * 8 + 21) != 0) goto loc_00C1F2F3;
loc_00C1F2DA:
    goto loc_00C1F1B2;
loc_00C1F2F3:
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4101390))) + 8)) - 1)) & (0xFFFFFFF9ULL)) != 0) goto loc_00C1F454;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4101390))) + 8)))) == 5) goto loc_00C1F454;
    v_stack_m1CE = 0;
    result = RtlCmEncodeMemIoResource(v_stack_m1D0, (unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4101390))) + 8))), (unsigned int)(v_stack_m1E4), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4101390))) + v_rip + 4101610 * 8 + 13));
    v_r11 = 0;
    if (sign_flag) goto loc_00C1F468;
    v_stack_m1CF = 2;
    a1 = (unsigned int)((v_stack_m1D0) - ((unsigned int)(v_r10 + 1)));
    if (condition_is_equal) goto loc_00C1F359;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_00C1F347;
    if (((unsigned int)(a1)) != 4) goto loc_00C1F367;
loc_00C1F347:
    v_stack_m1DC = 0;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4101390))) + 12)) & (4)) == 0) goto loc_00C1F367;
    goto loc_00C1F367;
loc_00C1F359:
    v_stack_m1DC = (unsigned int)(v_r10 + 1);
    v_stack_m1CE = 17;
loc_00C1F367:
    a2 = 0;
    v_stack_m1B4 = (unsigned int)((unsigned int)(v_stack_m1C0));
    a1 = 0;
    *(unsigned __int64 *)(v_rsp - 280 - 120) = v_xmm0;
    v_stack_m1F8 = v_rsp - 280 - 88;
    result = HalTranslateBusAddress(a1, a2, v_stack_m1CC, v_stack_m1DC);
    v_r10 = 0;
    *(unsigned __int64 *)(v_rsp - 280 - 116) = *(unsigned __int64 *)(v_rsp - 280 - 88);
    if (v_stack_m1D0 != ((unsigned __int8)(v_r10 + 1))) goto loc_00C1F3B1;
    if (v_stack_m1DC == 0) {
        *(unsigned __int16 *)(v_rsp - 280 - 118) = 0;
    }
    result = (unsigned int)(((unsigned int)(v_stack_m1E0)) + ((unsigned int)(v_r10 + 1)));
    v_stack_m1E0 = (unsigned int)(result);
loc_00C1F3C4:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 280 - 80))) == 0) goto loc_00C1F406;
    v_r11 = 0;
    *(unsigned int *)(result + 4) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 280 - 96)) = 0;
    *(unsigned __int64 *)(v_rsp - 280 - 80) = result + 4;
    a4 = (*(unsigned __int64 *)(v_rsp - 280 - 96)) + (16);
    v_r14 = (result + 4) + (16);
    *(unsigned __int64 *)(v_rsp - 280 - 72) = result + 4 + 8;
    v_r10 = 0;
    *(unsigned __int64 *)(v_rsp - 280 - 128) = *(unsigned __int64 *)(v_rsp - 280 - 96) + 8;
    goto loc_00C1F40E;
loc_00C1F406:
loc_00C1F40E:
    *(unsigned __int64 *)(v_r14) = v_xmm0;
    *(unsigned int *)(v_r14 + 16) = (unsigned int)((unsigned int)(v_stack_m1C0));
    v_r14 = (v_r14) + (20);
    *(unsigned __int64 *)(a4) = v_xmm0;
    *(unsigned int *)(a4 + 16) = (unsigned int)((unsigned int)(v_stack_m1B4));
    a4 = (a4) + (20);
    *(unsigned __int64 *)(v_rsp - 280 - 96) = a4;
    goto loc_00C1F1B9;
loc_00C1F454:
    goto loc_00C1F2DA;
loc_00C1F45D:
    a2 = (unsigned __int8)((v_stack_m1E7) + ((unsigned __int8)(v_r10 + 1)));
    goto loc_00C1F186;
loc_00C1F468:
    v_stack_m1F8 = v_stack_m1B0;
    result = KeBugCheckEx(92, 271, (int)((unsigned int)(result)), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4101390))));
loc_00C1F483:
    v_r14 = (unsigned int)((v_r14) - ((unsigned int)(result)));
    v_stack_m1E4 = 0;
    *(unsigned __int64 *)(v_rsp - 280 - 128) = v_r14;
    if ((*(unsigned int *)(result)) <= 0) goto loc_00C1F5BD;
    result = 0;
loc_00C1F49D:
    v_r12 = (result + 4) + (16);
    v_stack_m1B4 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 4 + 12)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result + 4 + 12))) == 0) goto loc_00C1F5A4;
loc_00C1F4BA:
    result = HalpGetResourceSortValue(result + 4 + 16, v_stack_m1D8, v_stack_m1A8, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4101390))));
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 4 + 12))))) - (0));
loc_00C1F4E1:
    result = HalpGetResourceSortValue(result + 4 + 16, v_stack_m1B8, v_stack_m1A0, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4101390))));
    if (v_stack_m1B8 < ((unsigned int)((unsigned int)(v_stack_m1D8)))) goto loc_00C1F512;
    if (v_stack_m1B8 != ((unsigned int)((unsigned int)(v_stack_m1D8)))) goto loc_00C1F56F;
    if (v_stack_m19C != ((unsigned int)((unsigned int)(v_stack_m1A4)))) goto loc_00C1F510;
    if (v_stack_m1A0 < ((unsigned int)((unsigned int)(v_stack_m1A8)))) goto loc_00C1F512;
loc_00C1F510:
    result = (unsigned int)(v_stack_m1A8);
    v_rsi = (unsigned int)(v_stack_m1A4);
    v_r15 = (unsigned int)(v_stack_m1D8);
    if (v_stack_m19C < ((unsigned int)((unsigned int)(v_stack_m1A4)))) {
        a1 = *(unsigned int *)(result + 4 + 16 + 16);
        a3 = v_stack_m1A8;
        a2 = v_stack_m1D8;
        *(unsigned __int64 *)(result + 4 + 16) = v_xmm0;
        result = *(unsigned int *)(result + 4 + 16 + 16);
        *(unsigned int *)(result + 4 + 16 + 16) = (unsigned int)(result);
        *(unsigned __int64 *)(result + 4 + 16) = v_xmm1;
        *(unsigned int *)(result + 4 + 16 + 16) = (unsigned int)(a1);
        a1 = *(unsigned int *)(v_r12 + 16);
        *(unsigned __int64 *)(v_r12) = v_xmm0;
        result = *(unsigned int *)(v_r12 + 16);
        *(unsigned int *)(v_r12 + 16) = (unsigned int)(result);
        *(unsigned __int64 *)(v_r12) = v_xmm1;
        *(unsigned int *)(v_r12 + 16) = (unsigned int)(a1);
        a1 = result + 4 + 16;
        result = HalpGetResourceSortValue(a1, a2, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4101390))));
        v_rsi = v_stack_m1A4;
        v_r15 = v_stack_m1D8;
    }
    v_rdi = (result + 4 + 16) + (20);
    v_r13 = (v_r12) + (20);
    v_r14 = (v_r14) - (v_r10 + 1);
    if (condition_is_not_equal) goto loc_00C1F4E1;
    v_r10 = (result + 4 + 16) + (20);
    v_r12 = (v_r12) + (20);
    v_r11 = (unsigned int)((0) + ((unsigned int)(v_r10 + 1)));
    if (((unsigned int)(v_r11)) < ((unsigned int)((unsigned int)(v_stack_m1B4)))) goto loc_00C1F4BA;
    result = 0;
loc_00C1F5A4:
    v_r14 = (unsigned int)(((unsigned int)(v_stack_m1E4)) + ((unsigned int)(v_r10 + 1)));
    v_stack_m1E4 = (unsigned int)(v_r14);
    if (((unsigned int)(v_r14)) < (*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 280 - 64)))) goto loc_00C1F49D;
loc_00C1F5BD:
    result = IoReportHalResourceUsage(*(unsigned __int64 *)(v_rsp - 280 - 56), *(unsigned __int64 *)(v_rsp - 280 - 64), v_stack_m1B0, (unsigned int)(*(unsigned int *)(v_rsp - 280 - 128)));
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rsp - 280 - 64), a2, v_stack_m1B0, (unsigned int)(*(unsigned int *)(v_rsp - 280 - 128)));
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m1B0, a2, v_stack_m1B0, (unsigned int)(*(unsigned int *)(v_rsp - 280 - 128)));
    a1 = (*(unsigned __int64 *)(v_rsp - 280 + 224)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, v_stack_m1B0, (unsigned int)(*(unsigned int *)(v_rsp - 280 - 128)));
    return result;
loc_00C1F615:
    v_stack_m1D0 = 398;
    result = KeBugCheckEx(172, (unsigned int)(0x4000ULL), 1, v_rip - 12564564);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpReportResourceUsage(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m19C;
    uint64_t v_stack_m1A0;
    uint32_t v_stack_m1A4;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint32_t v_stack_m1B4;
    uint32_t v_stack_m1B8;
    uint32_t v_stack_m1C0;
    uint64_t v_stack_m1C4;
    uint32_t v_stack_m1C8;
    uint16_t v_stack_m1CA;
    uint16_t v_stack_m1CC;
    uint16_t v_stack_m1CE;
    uint8_t v_stack_m1CF;
    uint64_t v_stack_m1D0;
    uint32_t v_stack_m1D8;
    uint32_t v_stack_m1DC;
    uint32_t v_stack_m1E0;
    uint32_t v_stack_m1E4;
    uint8_t v_stack_m1E7;
    uint8_t v_stack_m1E8;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m28;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (496);
    result = (*(uint64_t *)(v_rip + 0x1EB6DF)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x118 + 0xE0) = result;
    *(uint64_t *)(local_rsp - 0x118 - 0x38) = Arg1;
    Arg2 = 0;
    result = memset(local_rsp - 280 - 48, Arg2, 264, a4);
    local_rbx = 0;
    result = 0;
    v_stack_m1D8 = 0;
    v_stack_m1A8 = 0;
    v_stack_m1C0 = 0;
    v_stack_m1B8 = 0;
    v_stack_m1A0 = 0;
    *(uint64_t *)(local_rsp - 0x118 - 0x58) = 0;
    v_stack_m1DC = 0;
    v_stack_m1D0 = v_xmm0;
    if (*(uint64_t *)(v_rip + 0x1F1299) != 0) {
        Arg2 = *(uint64_t *)(v_rip + 0x1F1299);
        Arg1 = v_rip + 2012888;
        result = HalpClaimDebugResource(Arg1, Arg2, 264, a4);
    }
    if (*(uint64_t *)(v_rip + 0x1F124C) == 0) goto loc_00C1F0E2;
    if ((*(uint64_t *)(v_rip + 0x1F124C)) != (*(uint64_t *)(v_rip + 0x1F1299))) {
        Arg1 = v_rip + 2012907;
        result = HalpClaimDebugResource(Arg1, *(uint64_t *)(v_rip + 0x1F124C), 264, a4);
    }
    result = ExAllocatePool2(64, (uint32_t)((uint32_t)((uint32_t)(0x2000ULL))), (uint32_t)((uint32_t)((uint32_t)(0x6D6C6148ULL))), a4);
    *(uint64_t *)(local_rsp - 0x118 - 0x40) = result;
    result = ExAllocatePool2(64, (uint32_t)((uint32_t)((uint32_t)(0x2000ULL))), (uint32_t)((uint32_t)((uint32_t)(0x6D6C6148ULL))), a4);
    local_r10 = 0;
    v_stack_m1B0 = result;
    if (result == 0) goto loc_00C1F615;
    if (result == 0) goto loc_00C1F615;
    *(uint64_t *)(local_rsp - 0x118 - 0x50) = result + 4;
    *(uint64_t *)(local_rsp - 0x118 - 0x60) = result + 4;
loc_00C1F15D:
    if (((*(uint8_t *)(v_rip + 0x3E978C)) & ((uint8_t)(local_r10 + 1))) == 0) {
        *(uint8_t *)(v_rip + 0x3E978C) = 17;
        *(uint32_t *)(v_rip + 0x3E9978) = 0;
    }
    Arg2 = (uint32_t)((0) + ((uint32_t)(local_r10 + 1)));
    Arg1 = (v_rip + 4102028) + (local_r10 + 1);
    a3 = (v_rip + 4102520) + (5);
    if (Arg2 < 48) goto loc_00C1F15D;
    *(uint64_t *)(local_rsp - 0x118 - 0x48) = 0;
    *(uint64_t *)(local_rsp - 0x118 - 0x80) = 0;
loc_00C1F186:
    v_stack_m1E7 = 0;
    if (0 >= 2) goto loc_00C1F483;
    result = (uint8_t)(-(0));
    v_stack_m1E4 = 0;
    Arg1 = (uint8_t)((Arg1) & (240));
    Arg1 = (uint8_t)((Arg1) + (32));
    v_stack_m1E8 = (uint8_t)(Arg1);
loc_00C1F1B2:
    v_stack_m1E0 = 0;
loc_00C1F1B9:
    if (0 > 255) goto loc_00C1F2B1;
    if (((*(uint8_t *)(v_rip + 0x3E978C + 0x0 * 1)) & ((uint8_t)(Arg1))) != 0) goto loc_00C1F1E2;
    a3 = (uint32_t)((0) + ((uint32_t)(local_r10 + 1)));
    v_stack_m1E4 = (uint32_t)(a3);
    goto loc_00C1F1B9;
loc_00C1F1E2:
    Arg2 = 0;
    *(uint64_t *)(local_rsp - 0x118 - 0x30) = 0x200001ULL;
    result = memset(local_rsp - 280 - 40, Arg2, 256, v_rip + 4102028);
    result = KiCopyAffinityEx(local_rsp - 280 - 48, *(uint16_t *)(local_rsp - 0x118 - 0x2E), v_rip + 3833626, v_rip + 4102028);
    v_stack_m1D0 = 514;
    a3 = (uint8_t)((*(uint8_t *)(v_rip + 0x3E96B4 + v_stack_m1B0 * 1)) & (2));
    if (condition_is_equal) goto loc_00C1F237;
    v_stack_m1CE = (uint16_t)(local_r10 + 1);
    local_r10 = 0;
    goto loc_00C1F240;
loc_00C1F237:
    local_r10 = 0;
    v_stack_m1CE = 0;
loc_00C1F240:
    *(uint64_t *)(local_rsp - 0x118 - 0x6C) = *(uint64_t *)(local_rsp - 0x118 - 0x28);
    Arg2 = (v_stack_m1B0 * 4) + (v_stack_m1B0);
    v_stack_m1CA = 0;
    v_stack_m1C4 = *(uint64_t *)(local_rsp - 0x118 - 0x28);
    *(uint32_t *)(local_rsp - 0x118 - 0x70) = (uint32_t)((uint32_t)(v_stack_m1E4));
    v_stack_m1C8 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + v_rip + 0x3E9885 * 1 + 0x1)));
    v_stack_m1CC = (uint16_t)((uint32_t)(*(uint32_t *)(Arg2 + v_rip + 0x3E9885 * 1 + 0x1)));
    result = ((uint8_t)(a3) != 0) ? 1 : 0;
    *(uint16_t *)(local_rsp - 0x118 - 0x78) = 514;
    *(uint16_t *)(local_rsp - 0x118 - 0x76) = (uint16_t)(result);
    a3 = (uint32_t)(((uint32_t)(v_stack_m1E4)) + ((uint32_t)(local_r10 + 1)));
    *(uint16_t *)(local_rsp - 0x118 - 0x74) = (uint16_t)(*(uint8_t *)(Arg2 + v_rip + 0x3E9885 * 1));
    *(uint16_t *)(local_rsp - 0x118 - 0x72) = 0;
    v_stack_m1E4 = (uint32_t)(a3);
    goto loc_00C1F3C4;
loc_00C1F2B1:
    if (*(uint64_t *)(v_rip + 0x3E950E) == 0) goto loc_00C1F45D;
    if (((*(uint8_t *)(*(uint64_t *)(v_rip + 0x3E950E) + 0xC)) & ((uint8_t)(*(uint64_t *)(local_rsp - 0x118 - 0x28)))) != 0) goto loc_00C1F2C7;
    goto loc_00C1F1B2;
loc_00C1F2C7:
    a4 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_m1E0)))) + ((uint32_t)((uint32_t)((uint32_t)(v_stack_m1E0))));
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x3E950E)) + a4 * 8 + 0x15) != 0) goto loc_00C1F2F3;
loc_00C1F2DA:
    goto loc_00C1F1B2;
loc_00C1F2F3:
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x3E950E))) + 0x8)) - 1)) & (0xFFFFFFF9ULL)) != 0) goto loc_00C1F454;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x3E950E))) + 0x8)))) == 5) goto loc_00C1F454;
    v_stack_m1CE = 0;
    result = RtlCmEncodeMemIoResource(v_stack_m1D0, (uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x3E950E))) + 0x8))), (uint32_t)(v_stack_m1E4), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x3E950E))) + v_rip + 0x3E95EA * 8 + 0xD));
    local_r11 = 0;
    if (sign_flag) goto loc_00C1F468;
    v_stack_m1CF = 2;
    Arg1 = (uint32_t)((v_stack_m1D0) - ((uint32_t)(local_r10 + 1)));
    if (condition_is_equal) goto loc_00C1F359;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_00C1F347;
    if (((uint32_t)(Arg1)) != 4) goto loc_00C1F367;
loc_00C1F347:
    v_stack_m1DC = 0;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x3E950E))) + 0xC)) & (4)) == 0) goto loc_00C1F367;
    goto loc_00C1F367;
loc_00C1F359:
    v_stack_m1DC = (uint32_t)(local_r10 + 1);
    v_stack_m1CE = 17;
loc_00C1F367:
    Arg2 = 0;
    v_stack_m1B4 = (uint32_t)((uint32_t)(v_stack_m1C0));
    Arg1 = 0;
    *(uint64_t *)(local_rsp - 0x118 - 0x78) = v_xmm0;
    v_stack_m1F8 = local_rsp - 280 - 88;
    result = HalTranslateBusAddress(Arg1, Arg2, v_stack_m1CC, v_stack_m1DC);
    local_r10 = 0;
    *(uint64_t *)(local_rsp - 0x118 - 0x74) = *(uint64_t *)(local_rsp - 0x118 - 0x58);
    if (v_stack_m1D0 != ((uint8_t)(local_r10 + 1))) goto loc_00C1F3B1;
    if (v_stack_m1DC == 0) {
        *(uint16_t *)(local_rsp - 0x118 - 0x76) = 0;
    }
    result = (uint32_t)(((uint32_t)(v_stack_m1E0)) + ((uint32_t)(local_r10 + 1)));
    v_stack_m1E0 = (uint32_t)(result);
loc_00C1F3C4:
    if ((*(uint32_t *)(*(uint64_t *)(local_rsp - 0x118 - 0x50))) == 0) goto loc_00C1F406;
    local_r11 = 0;
    *(uint32_t *)(result + 0x4) = 0;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x118 - 0x60)) = 0;
    *(uint64_t *)(local_rsp - 0x118 - 0x50) = result + 4;
    a4 = (*(uint64_t *)(local_rsp - 0x118 - 0x60)) + (16);
    local_r14 = (result + 4) + (16);
    *(uint64_t *)(local_rsp - 0x118 - 0x48) = result + 4 + 8;
    local_r10 = 0;
    *(uint64_t *)(local_rsp - 0x118 - 0x80) = *(uint64_t *)(local_rsp - 0x118 - 0x60) + 8;
    goto loc_00C1F40E;
loc_00C1F406:
loc_00C1F40E:
    *(uint64_t *)(local_r14) = v_xmm0;
    *(uint32_t *)(local_r14 + 0x10) = (uint32_t)((uint32_t)(v_stack_m1C0));
    local_r14 = (local_r14) + (20);
    *(uint64_t *)(a4) = v_xmm0;
    *(uint32_t *)(a4 + 0x10) = (uint32_t)((uint32_t)(v_stack_m1B4));
    a4 = (a4) + (20);
    *(uint64_t *)(local_rsp - 0x118 - 0x60) = a4;
    goto loc_00C1F1B9;
loc_00C1F454:
    goto loc_00C1F2DA;
loc_00C1F45D:
    Arg2 = (uint8_t)((v_stack_m1E7) + ((uint8_t)(local_r10 + 1)));
    goto loc_00C1F186;
loc_00C1F468:
    v_stack_m1F8 = v_stack_m1B0;
    result = KeBugCheckEx(92, 271, (int32_t)((uint32_t)(result)), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x3E950E))));
loc_00C1F483:
    local_r14 = (uint32_t)((local_r14) - ((uint32_t)(result)));
    v_stack_m1E4 = 0;
    *(uint64_t *)(local_rsp - 0x118 - 0x80) = local_r14;
    if ((*(uint32_t *)(result)) <= 0) goto loc_00C1F5BD;
    result = 0;
loc_00C1F49D:
    local_r12 = (result + 4) + (16);
    v_stack_m1B4 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4 + 0xC)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4 + 0xC))) == 0) goto loc_00C1F5A4;
loc_00C1F4BA:
    result = HalpGetResourceSortValue(result + 4 + 16, v_stack_m1D8, v_stack_m1A8, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x3E950E))));
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4 + 0xC))))) - (0));
loc_00C1F4E1:
    result = HalpGetResourceSortValue(result + 4 + 16, v_stack_m1B8, v_stack_m1A0, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x3E950E))));
    if (v_stack_m1B8 < ((uint32_t)((uint32_t)(v_stack_m1D8)))) goto loc_00C1F512;
    if (v_stack_m1B8 != ((uint32_t)((uint32_t)(v_stack_m1D8)))) goto loc_00C1F56F;
    if (v_stack_m19C != ((uint32_t)((uint32_t)(v_stack_m1A4)))) goto loc_00C1F510;
    if (v_stack_m1A0 < ((uint32_t)((uint32_t)(v_stack_m1A8)))) goto loc_00C1F512;
loc_00C1F510:
    result = (uint32_t)(v_stack_m1A8);
    local_rsi = (uint32_t)(v_stack_m1A4);
    local_r15 = (uint32_t)(v_stack_m1D8);
    if (v_stack_m19C < ((uint32_t)((uint32_t)(v_stack_m1A4)))) {
        Arg1 = *(uint32_t *)(result + 0x4 + 0x10 + 0x10);
        a3 = v_stack_m1A8;
        Arg2 = v_stack_m1D8;
        *(uint64_t *)(result + 0x4 + 0x10) = v_xmm0;
        result = *(uint32_t *)(result + 0x4 + 0x10 + 0x10);
        *(uint32_t *)(result + 0x4 + 0x10 + 0x10) = (uint32_t)(result);
        *(uint64_t *)(result + 0x4 + 0x10) = v_xmm1;
        *(uint32_t *)(result + 0x4 + 0x10 + 0x10) = (uint32_t)(Arg1);
        Arg1 = *(uint32_t *)(local_r12 + 0x10);
        *(uint64_t *)(local_r12) = v_xmm0;
        result = *(uint32_t *)(local_r12 + 0x10);
        *(uint32_t *)(local_r12 + 0x10) = (uint32_t)(result);
        *(uint64_t *)(local_r12) = v_xmm1;
        *(uint32_t *)(local_r12 + 0x10) = (uint32_t)(Arg1);
        Arg1 = result + 4 + 16;
        result = HalpGetResourceSortValue(Arg1, Arg2, a3, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x3E950E))));
        local_rsi = v_stack_m1A4;
        local_r15 = v_stack_m1D8;
    }
    local_rdi = (result + 4 + 16) + (20);
    local_r13 = (local_r12) + (20);
    local_r14 = (local_r14) - (local_r10 + 1);
    if (condition_is_not_equal) goto loc_00C1F4E1;
    local_r10 = (result + 4 + 16) + (20);
    local_r12 = (local_r12) + (20);
    local_r11 = (uint32_t)((0) + ((uint32_t)(local_r10 + 1)));
    if (((uint32_t)(local_r11)) < ((uint32_t)((uint32_t)(v_stack_m1B4)))) goto loc_00C1F4BA;
    result = 0;
loc_00C1F5A4:
    local_r14 = (uint32_t)(((uint32_t)(v_stack_m1E4)) + ((uint32_t)(local_r10 + 1)));
    v_stack_m1E4 = (uint32_t)(local_r14);
    if (((uint32_t)(local_r14)) < (*(uint32_t *)(*(uint64_t *)(local_rsp - 0x118 - 0x40)))) goto loc_00C1F49D;
loc_00C1F5BD:
    result = IoReportHalResourceUsage(*(uint64_t *)(local_rsp - 0x118 - 0x38), *(uint64_t *)(local_rsp - 0x118 - 0x40), v_stack_m1B0, (uint32_t)(*(uint32_t *)(local_rsp - 0x118 - 0x80)));
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(local_rsp - 0x118 - 0x40), Arg2, v_stack_m1B0, (uint32_t)(*(uint32_t *)(local_rsp - 0x118 - 0x80)));
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m1B0, Arg2, v_stack_m1B0, (uint32_t)(*(uint32_t *)(local_rsp - 0x118 - 0x80)));
    Arg1 = (*(uint64_t *)(local_rsp - 0x118 + 0xE0)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, v_stack_m1B0, (uint32_t)(*(uint32_t *)(local_rsp - 0x118 - 0x80)));
    return result;
loc_00C1F615:
    v_stack_m1D0 = 398;
    result = KeBugCheckEx(172, (uint32_t)(0x4000ULL), 1, v_rip - 12564564);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C1F034&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
