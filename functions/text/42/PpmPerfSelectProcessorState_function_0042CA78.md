# PpmPerfSelectProcessorState

- RVA: `0x0042CA78`–`0x0042CF4E` (길이 `1,238` bytes)
- VA: `0x000000014042CA78`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000A19D4`
- 디코드: `288`개 명령, `1,238/1,238` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x0042CB04` → [PpmGetPerfPolicyClass](PpmGetPerfPolicyClass_function_0042CF54.md) (function, `0x0042CF54`)
- `0x0042CC0E` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0042CC2A` → [PpmEventPerfSelectProcessorState](PpmEventPerfSelectProcessorState_function_0042CFA0.md) (function, `0x0042CFA0`)

### Direct callers
- [sub_0042CA0D](Unknown_function_0042CA0D.md) at `0x0042CA48`

### Static image references
- `0x0042CAA3` → RVA `0x00F0CE0C` (`.data`; read)
- `0x0042CABB` → RVA `0x00FC6E40` (`ALMOSTRO`; read)
- `0x0042CAD6` → RVA `0x00E08380` (`.data`; read)
- `0x0042CAF0` → RVA `0x00F07778` (`.data`; read)
- `0x0042CC4F` → RVA `0x00FC5178` (`ALMOSTRO`; read)
- `0x0042CC6F` → RVA `0x00FC517C` (`ALMOSTRO`; read)
- `0x0042CDAB` → RVA `0x00FC50E0` (`ALMOSTRO`; read)
- `0x0042CDC0` → RVA `0x00F0CE4C` (`.data`; read)
- `0x0042CDDA` → RVA `0x00F077E8` (`.data`; read)
- `0x0042CE30` → RVA `0x00FC6CC8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x0042CE92` → [sub_006EE448 + 0x9](../6E/Unknown_function_006EE448.md) (`tail-transfer`)
  - `0x0042CE9B` → [sub_006EE448](../6E/Unknown_function_006EE448.md) (`tail-transfer`)
  - `0x0042CF07` → [sub_006EE448 + 0x39](../6E/Unknown_function_006EE448.md) (`tail-transfer`)
  - `0x0042CF18` → [sub_006EE448 + 0x48](../6E/Unknown_function_006EE448.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0042CA78  40 53                           push rbx
0042CA7A  55                              push rbp
0042CA7B  56                              push rsi
0042CA7C  57                              push rdi
0042CA7D  41 54                           push r12
0042CA7F  41 55                           push r13
0042CA81  41 56                           push r14
0042CA83  41 57                           push r15
0042CA85  48 81 EC 88 00 00 00            sub rsp, 0x88
0042CA8C  48 8B 01                        mov rax, qword ptr [rcx]
0042CA8F  33 FF                           xor edi, edi
0042CA91  48 8B 71 08                     mov rsi, qword ptr [rcx + 8]
0042CA95  4C 8B F1                        mov r14, rcx
0042CA98  4C 8B 59 10                     mov r11, qword ptr [rcx + 0x10]
0042CA9C  21 BC 24 E0 00 00 00            and dword ptr [rsp + 0xe0], edi
0042CAA3  48 63 15 62 03 AE 00            movsxd rdx, dword ptr [rip + 0xae0362]
0042CAAA  8D 4F 64                        lea ecx, [rdi + 0x64]
0042CAAD  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
0042CAB2  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
0042CAB6  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
0042CABB  8B 05 7F A3 B9 00               mov eax, dword ptr [rip + 0xb9a37f]
0042CAC1  3B C1                           cmp eax, ecx
0042CAC3  44 0F B6 C0                     movzx r8d, al
0042CAC7  44 0F 47 C1                     cmova r8d, ecx
0042CACB  C7 84 24 E8 00 00 00 01 00 00 00  mov dword ptr [rsp + 0xe8], 1
0042CAD6  48 8B 0D A3 B8 9D 00            mov rcx, qword ptr [rip + 0x9db8a3]
0042CADD  48 69 D2 E8 01 00 00            imul rdx, rdx, 0x1e8
0042CAE4  48 8D 69 28                     lea rbp, [rcx + 0x28]
0042CAE8  48 03 EA                        add rbp, rdx
0042CAEB  4D 85 DB                        test r11, r11
0042CAEE  74 0D                           je 0x14042cafd
0042CAF0  48 3B 0D 81 AC AD 00            cmp rcx, qword ptr [rip + 0xadac81]
0042CAF7  0F 84 C3 02 00 00               je 0x14042cdc0
0042CAFD  44 8B 4D 48                     mov r9d, dword ptr [rbp + 0x48]
0042CB01  49 8B CE                        mov rcx, r14
0042CB04  E8 4B 04 00 00                  call 0x14042cf54
0042CB09  0F B6 D8                        movzx ebx, al
0042CB0C  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
0042CB11  0F B6 44 2B 2E                  movzx eax, byte ptr [rbx + rbp + 0x2e]
0042CB16  44 0F B6 64 2B 38               movzx r12d, byte ptr [rbx + rbp + 0x38]
0042CB1C  8A 4C 2B 32                     mov cl, byte ptr [rbx + rbp + 0x32]
0042CB20  44 0F B6 7C 2B 34               movzx r15d, byte ptr [rbx + rbp + 0x34]
0042CB26  44 8A 94 2B 89 00 00 00         mov r10b, byte ptr [rbx + rbp + 0x89]
0042CB2E  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
0042CB32  0F B6 44 2B 30                  movzx eax, byte ptr [rbx + rbp + 0x30]
0042CB37  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
0042CB3B  0F B6 44 2B 36                  movzx eax, byte ptr [rbx + rbp + 0x36]
0042CB40  88 8C 24 D0 00 00 00            mov byte ptr [rsp + 0xd0], cl
0042CB47  89 84 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], eax
0042CB4E  46 8D 2C 20                     lea r13d, [rax + r12]
0042CB52  41 D1 ED                        shr r13d, 1
0042CB55  4D 85 DB                        test r11, r11
0042CB58  74 14                           je 0x14042cb6e
0042CB5A  8B 44 9D 6C                     mov eax, dword ptr [rbp + rbx*4 + 0x6c]
0042CB5E  8B 54 9D 64                     mov edx, dword ptr [rbp + rbx*4 + 0x64]
0042CB62  3B C2                           cmp eax, edx
0042CB64  0F 85 1C 03 00 00               jne 0x14042ce86
0042CB6A  C6 46 3C 00                     mov byte ptr [rsi + 0x3c], 0
0042CB6E  41 8D 41 FF                     lea eax, [r9 - 1]
0042CB72  BA 01 00 00 00                  mov edx, 1
0042CB77  A9 FD FF FF FF                  test eax, 0xfffffffd
0042CB7C  0F 85 AE 02 00 00               jne 0x14042ce30
0042CB82  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
0042CB87  44 8B 88 C4 01 00 00            mov r9d, dword ptr [rax + 0x1c4]
0042CB8E  41 B8 64 00 00 00               mov r8d, 0x64
0042CB94  80 B8 0A 02 00 00 00            cmp byte ptr [rax + 0x20a], 0
0042CB9B  0F 85 A3 00 00 00               jne 0x14042cc44
0042CBA1  C7 84 24 E8 00 00 00 05 00 00 00  mov dword ptr [rsp + 0xe8], 5
0042CBAC  41 8B D9                        mov ebx, r9d
0042CBAF  0F BA EF 12                     bts edi, 0x12
0042CBB3  48 83 64 24 50 00               and qword ptr [rsp + 0x50], 0
0042CBB9  48 83 64 24 48 00               and qword ptr [rsp + 0x48], 0
0042CBBF  48 83 64 24 40 00               and qword ptr [rsp + 0x40], 0
0042CBC5  4C 8B 54 24 70                  mov r10, qword ptr [rsp + 0x70]
0042CBCA  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0042CBCF  44 8B 9C 24 E8 00 00 00         mov r11d, dword ptr [rsp + 0xe8]
0042CBD7  44 89 5C 24 38                  mov dword ptr [rsp + 0x38], r11d
0042CBDC  41 0F B6 94 2A AF 00 00 00      movzx edx, byte ptr [r10 + rbp + 0xaf]
0042CBE5  48 8B 81 78 01 00 00            mov rax, qword ptr [rcx + 0x178]
0042CBEC  44 8B 81 CC 01 00 00            mov r8d, dword ptr [rcx + 0x1cc]
0042CBF3  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
0042CBF8  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
0042CBFC  8B 55 58                        mov edx, dword ptr [rbp + 0x58]
0042CBFF  89 54 24 28                     mov dword ptr [rsp + 0x28], edx
0042CC03  42 8B 54 95 50                  mov edx, dword ptr [rbp + r10*4 + 0x50]
0042CC08  89 54 24 20                     mov dword ptr [rsp + 0x20], edx
0042CC0C  8B D3                           mov edx, ebx
0042CC0E  E8 BD DE 28 00                  call 0x1406baad0
0042CC13  8B 94 24 E0 00 00 00            mov edx, dword ptr [rsp + 0xe0]
0042CC1A  44 8B C8                        mov r9d, eax
0042CC1D  44 8B C3                        mov r8d, ebx
0042CC20  89 46 38                        mov dword ptr [rsi + 0x38], eax
0042CC23  49 8B CE                        mov rcx, r14
0042CC26  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
0042CC2A  E8 71 03 00 00                  call 0x14042cfa0
0042CC2F  48 81 C4 88 00 00 00            add rsp, 0x88
0042CC36  41 5F                           pop r15
0042CC38  41 5E                           pop r14
0042CC3A  41 5D                           pop r13
0042CC3C  41 5C                           pop r12
0042CC3E  5F                              pop rdi
0042CC3F  5E                              pop rsi
0042CC40  5D                              pop rbp
0042CC41  5B                              pop rbx
0042CC42  C3                              ret
0042CC43  CC                              int3
0042CC44  41 80 7E 44 00                  cmp byte ptr [r14 + 0x44], 0
0042CC49  0F 85 13 02 00 00               jne 0x14042ce62
0042CC4F  0F B6 05 22 85 B9 00            movzx eax, byte ptr [rip + 0xb98522]
0042CC56  41 3A C0                        cmp al, r8b
0042CC59  44 8B D0                        mov r10d, eax
0042CC5C  45 0F 47 D0                     cmova r10d, r8d
0042CC60  45 84 ED                        test r13b, r13b
0042CC63  0F 84 67 02 00 00               je 0x14042ced0
0042CC69  45 8B 46 28                     mov r8d, dword ptr [r14 + 0x28]
0042CC6D  33 D2                           xor edx, edx
0042CC6F  39 15 07 85 B9 00               cmp dword ptr [rip + 0xb98507], edx
0042CC75  41 8B C0                        mov eax, r8d
0042CC78  8B 5E 38                        mov ebx, dword ptr [rsi + 0x38]
0042CC7B  0F 84 94 01 00 00               je 0x14042ce15
0042CC81  41 0F B7 4E 3E                  movzx ecx, word ptr [r14 + 0x3e]
0042CC86  F7 F1                           div ecx
0042CC88  89 84 24 E0 00 00 00            mov dword ptr [rsp + 0xe0], eax
0042CC8F  8B D0                           mov edx, eax
0042CC91  41 3B C4                        cmp eax, r12d
0042CC94  77 5C                           ja 0x14042ccf2
0042CC96  83 A6 A0 04 00 00 00            and dword ptr [rsi + 0x4a0], 0
0042CC9D  8B 8C 24 D8 00 00 00            mov ecx, dword ptr [rsp + 0xd8]
0042CCA4  3B D1                           cmp edx, ecx
0042CCA6  0F 82 9E 00 00 00               jb 0x14042cd4a
0042CCAC  83 A6 A4 04 00 00 00            and dword ptr [rsi + 0x4a4], 0
0042CCB3  4D 85 DB                        test r11, r11
0042CCB6  0F 84 F7 FE FF FF               je 0x14042cbb3
0042CCBC  41 0F B6 83 EE 00 00 00         movzx eax, byte ptr [r11 + 0xee]
0042CCC4  84 C0                           test al, al
0042CCC6  0F 85 6C 02 00 00               jne 0x14042cf38
0042CCCC  41 0F B6 83 EF 00 00 00         movzx eax, byte ptr [r11 + 0xef]
0042CCD4  84 C0                           test al, al
0042CCD6  0F 84 D7 FE FF FF               je 0x14042cbb3
0042CCDC  0F BA EF 11                     bts edi, 0x11
0042CCE0  41 C6 83 EF 00 00 00 00         mov byte ptr [r11 + 0xef], 0
0042CCE8  3B D8                           cmp ebx, eax
0042CCEA  0F 46 D8                        cmovbe ebx, eax
0042CCED  E9 C1 FE FF FF                  jmp 0x14042cbb3
0042CCF2  8B 86 A0 04 00 00               mov eax, dword ptr [rsi + 0x4a0]
0042CCF8  FF C0                           inc eax
0042CCFA  89 86 A0 04 00 00               mov dword ptr [rsi + 0x4a0], eax
0042CD00  41 3B D9                        cmp ebx, r9d
0042CD03  73 98                           jae 0x14042cc9d
0042CD05  3B 44 24 60                     cmp eax, dword ptr [rsp + 0x60]
0042CD09  72 92                           jb 0x14042cc9d
0042CD0B  83 A6 A0 04 00 00 00            and dword ptr [rsi + 0x4a0], 0
0042CD12  41 0F B6 CF                     movzx ecx, r15b
0042CD16  45 84 FF                        test r15b, r15b
0042CD19  0F 84 DA 00 00 00               je 0x14042cdf9
0042CD1F  83 E9 01                        sub ecx, 1
0042CD22  0F 84 F5 01 00 00               je 0x14042cf1d
0042CD28  83 E9 01                        sub ecx, 1
0042CD2B  0F 85 C4 01 00 00               jne 0x14042cef5
0042CD31  41 8B D9                        mov ebx, r9d
0042CD34  83 CF 40                        or edi, 0x40
0042CD37  8B 8C 24 D8 00 00 00            mov ecx, dword ptr [rsp + 0xd8]
0042CD3E  41 3B D9                        cmp ebx, r9d
0042CD41  41 0F 43 D9                     cmovae ebx, r9d
0042CD45  E9 5A FF FF FF                  jmp 0x14042cca4
0042CD4A  8B 86 A4 04 00 00               mov eax, dword ptr [rsi + 0x4a4]
0042CD50  BA 01 00 00 00                  mov edx, 1
0042CD55  FF C0                           inc eax
0042CD57  89 86 A4 04 00 00               mov dword ptr [rsi + 0x4a4], eax
0042CD5D  3B DA                           cmp ebx, edx
0042CD5F  0F 86 4E FF FF FF               jbe 0x14042ccb3
0042CD65  3B 44 24 64                     cmp eax, dword ptr [rsp + 0x64]
0042CD69  0F 82 44 FF FF FF               jb 0x14042ccb3
0042CD6F  83 A6 A4 04 00 00 00            and dword ptr [rsi + 0x4a4], 0
0042CD76  0F B6 8C 24 D0 00 00 00         movzx ecx, byte ptr [rsp + 0xd0]
0042CD7E  C7 84 24 E8 00 00 00 03 00 00 00  mov dword ptr [rsp + 0xe8], 3
0042CD89  85 C9                           test ecx, ecx
0042CD8B  75 16                           jne 0x14042cda3
0042CD8D  33 D2                           xor edx, edx
0042CD8F  41 0F B6 CD                     movzx ecx, r13b
0042CD93  41 8B C0                        mov eax, r8d
0042CD96  F7 F1                           div ecx
0042CD98  0F BA EF 08                     bts edi, 8
0042CD9C  8B D8                           mov ebx, eax
0042CD9E  E9 10 FF FF FF                  jmp 0x14042ccb3
0042CDA3  2B CA                           sub ecx, edx
0042CDA5  0F 85 80 01 00 00               jne 0x14042cf2b
0042CDAB  8B 05 2F 83 B9 00               mov eax, dword ptr [rip + 0xb9832f]
0042CDB1  0F BA EF 09                     bts edi, 9
0042CDB5  3B D8                           cmp ebx, eax
0042CDB7  76 35                           jbe 0x14042cdee
0042CDB9  2B D8                           sub ebx, eax
0042CDBB  E9 F3 FE FF FF                  jmp 0x14042ccb3
0042CDC0  40 38 3D 85 00 AE 00            cmp byte ptr [rip + 0xae0085], dil
0042CDC7  0F 84 30 FD FF FF               je 0x14042cafd
0042CDCD  45 38 83 E9 00 00 00            cmp byte ptr [r11 + 0xe9], r8b
0042CDD4  0F 83 23 FD FF FF               jae 0x14042cafd
0042CDDA  48 8D 2D 07 AA AD 00            lea rbp, [rip + 0xadaa07]
0042CDE1  BF 00 10 00 00                  mov edi, 0x1000
0042CDE6  48 03 EA                        add rbp, rdx
0042CDE9  E9 0F FD FF FF                  jmp 0x14042cafd
0042CDEE  8B DA                           mov ebx, edx
0042CDF0  0F BA EF 0A                     bts edi, 0xa
0042CDF4  E9 BA FE FF FF                  jmp 0x14042ccb3
0042CDF9  33 D2                           xor edx, edx
0042CDFB  41 0F B6 CD                     movzx ecx, r13b
0042CDFF  41 8B C0                        mov eax, r8d
0042CE02  F7 F1                           div ecx
0042CE04  8B 94 24 E0 00 00 00            mov edx, dword ptr [rsp + 0xe0]
0042CE0B  83 CF 10                        or edi, 0x10
0042CE0E  8B D8                           mov ebx, eax
0042CE10  E9 22 FF FF FF                  jmp 0x14042cd37
0042CE15  F7 F3                           div ebx
0042CE17  E9 6C FE FF FF                  jmp 0x14042cc88
0042CE1C  84 C9                           test cl, cl
0042CE1E  0F 85 A3 00 00 00               jne 0x14042cec7
0042CE24  8A 8C 24 D0 00 00 00            mov cl, byte ptr [rsp + 0xd0]
0042CE2B  E9 3E FD FF FF                  jmp 0x14042cb6e
0042CE30  83 3D 91 9E B9 00 00            cmp dword ptr [rip + 0xb99e91], 0
0042CE37  41 8D 41 FB                     lea eax, [r9 - 5]
0042CE3B  75 17                           jne 0x14042ce54
0042CE3D  3B C2                           cmp eax, edx
0042CE3F  76 13                           jbe 0x14042ce54
0042CE41  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
0042CE46  41 B8 64 00 00 00               mov r8d, 0x64
0042CE4C  45 8B C8                        mov r9d, r8d
0042CE4F  E9 40 FD FF FF                  jmp 0x14042cb94
0042CE54  44 8B 4E 18                     mov r9d, dword ptr [rsi + 0x18]
0042CE58  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
0042CE5D  E9 2C FD FF FF                  jmp 0x14042cb8e
0042CE62  41 80 7E 5C 00                  cmp byte ptr [r14 + 0x5c], 0
0042CE67  0F 84 E2 FD FF FF               je 0x14042cc4f
0042CE6D  45 84 D2                        test r10b, r10b
0042CE70  0F 84 D9 FD FF FF               je 0x14042cc4f
0042CE76  0B FA                           or edi, edx
0042CE78  41 8B D9                        mov ebx, r9d
0042CE7B  44 3A D2                        cmp r10b, dl
0042CE7E  0F 44 DA                        cmove ebx, edx
0042CE81  E9 2D FD FF FF                  jmp 0x14042cbb3
0042CE86  8A 4E 3C                        mov cl, byte ptr [rsi + 0x3c]
0042CE89  45 8B 83 F0 00 00 00            mov r8d, dword ptr [r11 + 0xf0]
0042CE90  84 C9                           test cl, cl
0042CE92  0F 85 B9 15 2C 00               jne 0x1406ee451
0042CE98  44 3B C0                        cmp r8d, eax
0042CE9B  0F 82 A7 15 2C 00               jb 0x1406ee448
0042CEA1  8A 46 3D                        mov al, byte ptr [rsi + 0x3d]
0042CEA4  BA 01 00 00 00                  mov edx, 1
0042CEA9  02 C2                           add al, dl
0042CEAB  0F BA EF 14                     bts edi, 0x14
0042CEAF  88 46 3D                        mov byte ptr [rsi + 0x3d], al
0042CEB2  3A 44 2B 76                     cmp al, byte ptr [rbx + rbp + 0x76]
0042CEB6  0F 82 60 FF FF FF               jb 0x14042ce1c
0042CEBC  66 89 56 3C                     mov word ptr [rsi + 0x3c], dx
0042CEC0  8A CA                           mov cl, dl
0042CEC2  E9 55 FF FF FF                  jmp 0x14042ce1c
0042CEC7  0F BA EF 15                     bts edi, 0x15
0042CECB  E9 54 FF FF FF                  jmp 0x14042ce24
0042CED0  45 84 FF                        test r15b, r15b
0042CED3  41 8B C7                        mov eax, r15d
0042CED6  BA 02 00 00 00                  mov edx, 2
0042CEDB  0F 44 C2                        cmove eax, edx
0042CEDE  84 C9                           test cl, cl
0042CEE0  44 8A F8                        mov r15b, al
0042CEE3  0F B6 C1                        movzx eax, cl
0042CEE6  0F 44 C2                        cmove eax, edx
0042CEE9  88 84 24 D0 00 00 00            mov byte ptr [rsp + 0xd0], al
0042CEF0  E9 74 FD FF FF                  jmp 0x14042cc69
0042CEF5  83 F9 01                        cmp ecx, 1
0042CEF8  0F 85 39 FE FF FF               jne 0x14042cd37
0042CEFE  41 0F B6 C2                     movzx eax, r10b
0042CF02  3B D0                           cmp edx, eax
0042CF04  41 8B C0                        mov eax, r8d
0042CF07  0F 82 74 15 2C 00               jb 0x1406ee481
0042CF0D  8B 8C 24 D8 00 00 00            mov ecx, dword ptr [rsp + 0xd8]
0042CF14  33 D2                           xor edx, edx
0042CF16  F7 F1                           div ecx
0042CF18  E9 73 15 2C 00                  jmp 0x1406ee490
0042CF1D  03 1D BD 81 B9 00               add ebx, dword ptr [rip + 0xb981bd]
0042CF23  83 CF 20                        or edi, 0x20
0042CF26  E9 0C FE FF FF                  jmp 0x14042cd37
0042CF2B  3B CA                           cmp ecx, edx
0042CF2D  0F 84 BB FE FF FF               je 0x14042cdee
0042CF33  E9 7B FD FF FF                  jmp 0x14042ccb3
0042CF38  0F BA EF 10                     bts edi, 0x10
0042CF3C  41 C6 83 EE 00 00 00 00         mov byte ptr [r11 + 0xee], 0
0042CF44  3B D8                           cmp ebx, eax
0042CF46  0F 46 D8                        cmovbe ebx, eax
0042CF49  E9 7E FD FF FF                  jmp 0x14042cccc
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmPerfSelectProcessorState(__int64 a1)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r13;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m64;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m90;
    unsigned int v_stack_m98;
    unsigned int v_stack_mA0;
    unsigned int v_stack_mA8;
    unsigned int v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned int v_stack_p60;
    unsigned int v_stack_p64;
    unsigned __int64 v_stack_p68;
    unsigned __int8 v_stack_p8;
    unsigned __int8 v_stack_pD0;
    unsigned int v_stack_pD8;
    unsigned int v_stack_pE0;
    unsigned int v_stack_pE8;

    v_rsp = (v_rsp) - (136);
    v_rdi = 0;
    v_stack_m60 = *(unsigned __int64 *)(a1);
    v_stack_m50 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 8);
    a3 = (unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12166015)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12166015)))) > ((unsigned int)(v_rdi + 100))) { a3 = (unsigned int)(v_rdi + 100); }
    v_stack_p20 = 1;
    a2 = ((int)(*(unsigned int *)(v_rip + 11404130))) * ((int)(*(unsigned int *)(v_rip + 11404130)));
    v_rbp = (*(unsigned __int64 *)(v_rip + 10336419) + 40) + (a2);
    if (*(unsigned __int64 *)(a1 + 16) == 0) goto loc_0042CAFD;
    if ((*(unsigned __int64 *)(v_rip + 10336419)) == (*(unsigned __int64 *)(v_rip + 11381889))) goto loc_0042CDC0;
loc_0042CAFD:
    result = PpmGetPerfPolicyClass(a1, a2, a3, (unsigned int)(*(unsigned int *)(v_rbp + 72)));
    v_stack_m58 = (unsigned __int8)(result);
    v_stack_m64 = (unsigned int)(*(unsigned __int8 *)((unsigned __int8)(result) + v_rbp * 1 + 46));
    v_stack_m68 = (unsigned int)(*(unsigned __int8 *)((unsigned __int8)(result) + v_rbp * 1 + 48));
    v_stack_p8 = (unsigned __int8)(*(unsigned __int8 *)((unsigned __int8)(result) + v_rbp * 1 + 50));
    v_stack_p10 = (unsigned int)(*(unsigned __int8 *)((unsigned __int8)(result) + v_rbp * 1 + 54));
    v_r13 = (unsigned int)((*(unsigned __int8 *)((unsigned __int8)(result) + v_rbp * 1 + 54) + *(unsigned __int8 *)((unsigned __int8)(result) + v_rbp * 1 + 56) * 1) >> (1));
    if (*(unsigned __int64 *)(a1 + 16) == 0) goto loc_0042CB6E;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rbp + (unsigned __int8)(result) * 4 + 108)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbp + (unsigned __int8)(result) * 4 + 100))))) goto loc_0042CE86;
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 60) = 0;
loc_0042CB6E:
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(v_rbp + 72)) - 1)) & (0xFFFFFFFDULL)) != 0) goto loc_0042CE30;
loc_0042CB8E:
loc_0042CB94:
    if ((*(unsigned __int8 *)(v_stack_m60 + 522)) != 0) goto loc_0042CC44;
    v_stack_p20 = 5;
loc_0042CBB3:
    v_stack_m90 = (unsigned int)((unsigned int)(v_stack_p20));
    v_stack_m98 = (unsigned int)(*(unsigned __int8 *)(v_stack_m58 + v_rbp * 1 + 175));
    v_stack_mA0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbp + 88)));
    v_stack_mA8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbp + v_stack_m58 * 4 + 80)));
    result = guard_dispatch_icall(v_stack_m50, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m60 + 452)))))), (unsigned int)(*(unsigned int *)(v_stack_m60 + 460)), (unsigned int)(*(unsigned int *)(v_stack_m60 + 452)));
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 56) = (unsigned int)(result);
    v_stack_mA8 = 0;
    result = PpmEventPerfSelectProcessorState(a1, (unsigned int)(v_stack_p18), (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m60 + 452)))))), (unsigned int)((unsigned int)(result)));
    v_rsp = (v_rsp) + (136);
    return result;
loc_0042CC44:
    if ((*(unsigned __int8 *)(a1 + 68)) != 0) goto loc_0042CE62;
loc_0042CC4F:
    v_r10 = (unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rip + 12158242)));
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rip + 12158242))) > ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m60 + 452))))))))) { v_r10 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m60 + 452))))))); }
    if ((unsigned __int8)(v_r13) == 0) goto loc_0042CED0;
loc_0042CC69:
    a2 = 0;
    if ((*(unsigned int *)(v_rip + 12158215)) == 0) goto loc_0042CE15;
loc_0042CC88:
    v_stack_pE0 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 40)))));
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 40)))))) > ((unsigned int)(*(unsigned __int8 *)((unsigned __int8)(result) + v_rbp * 1 + 56)))) goto loc_0042CCF2;
loc_0042CC9D:
loc_0042CCA4:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 40)))))))) < ((unsigned int)((unsigned int)(v_stack_pD8)))) goto loc_0042CD4A;
loc_0042CCB3:
    if ((unsigned int)(v_stack_p20) == 0) goto loc_0042CBB3;
    if ((unsigned __int8)(*(unsigned __int8 *)((unsigned int)(v_stack_p20) + 238)) != 0) goto loc_0042CF38;
loc_0042CCCC:
    if ((unsigned __int8)(*(unsigned __int8 *)((unsigned int)(v_stack_p20) + 239)) == 0) goto loc_0042CBB3;
    *(unsigned __int8 *)((unsigned int)(v_stack_p20) + 239) = 0;
    v_rbx = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 56));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 56)))) <= ((unsigned int)(*(unsigned __int8 *)((unsigned int)(v_stack_p20) + 239)))) { v_rbx = (unsigned int)(*(unsigned __int8 *)((unsigned int)(v_stack_p20) + 239)); }
    goto loc_0042CBB3;
loc_0042CCF2:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 1184))) + 1);
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 1184) = (unsigned int)(result);
    if (((unsigned int)(v_rbx)) >= ((unsigned int)((unsigned int)((unsigned int)(result))))) goto loc_0042CC9D;
    if (((unsigned int)(result)) < v_stack_p60) goto loc_0042CC9D;
    if ((unsigned __int8)(*(unsigned __int8 *)((unsigned __int8)(result) + v_rbp * 1 + 52)) == 0) goto loc_0042CDF9;
    a1 = (unsigned int)(((unsigned __int8)(*(unsigned __int8 *)((unsigned __int8)(result) + v_rbp * 1 + 52))) - (1));
    if (condition_is_equal) goto loc_0042CF1D;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_not_equal) goto loc_0042CEF5;
    v_rdi = (unsigned int)((v_rdi) | (64));
loc_0042CD37:
    v_rbx = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))))) >= ((unsigned int)((unsigned int)((unsigned int)(result))))) { v_rbx = (unsigned int)((unsigned int)((unsigned int)(result))); }
    goto loc_0042CCA4;
loc_0042CD4A:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 1188))) + 1);
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 1188) = (unsigned int)(result);
    if (((unsigned int)(v_rbx)) <= 1) goto loc_0042CCB3;
    if (((unsigned int)(result)) < v_stack_p64) goto loc_0042CCB3;
    v_stack_pE8 = 3;
    if ((unsigned int)(v_stack_pD0) != 0) goto loc_0042CDA3;
    a2 = 0;
    goto loc_0042CCB3;
loc_0042CDA3:
    a1 = (unsigned int)(((unsigned __int8)(v_r13)) - (0));
    if (condition_is_not_equal) goto loc_0042CF2B;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 40)))))))) <= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12157743))))) goto loc_0042CDEE;
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 40))))))) - ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12157743)))));
    goto loc_0042CCB3;
loc_0042CDC0:
    if ((*(unsigned __int8 *)(v_rip + 11403397)) == ((unsigned __int8)(v_rdi))) goto loc_0042CAFD;
    if ((*(unsigned __int8 *)((unsigned int)(v_stack_p20) + 233)) >= ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 40))))) goto loc_0042CAFD;
    v_rbp = (v_rip + 11381255) + (0);
    goto loc_0042CAFD;
loc_0042CDEE:
    goto loc_0042CCB3;
loc_0042CDF9:
    a2 = 0;
    v_rdi = (unsigned int)(((unsigned int)(0x1000ULL)) | (16));
    goto loc_0042CD37;
loc_0042CE15:
    goto loc_0042CC88;
loc_0042CE1C:
    if ((unsigned __int8)((unsigned __int8)(v_r13)) != 0) goto loc_0042CEC7;
loc_0042CE24:
    goto loc_0042CB6E;
loc_0042CE30:
    if ((*(unsigned int *)(v_rip + 12164753)) != 0) goto loc_0042CE54;
    if (((unsigned int)((unsigned int)((unsigned int)(result)) - 5)) <= ((unsigned int)((unsigned int)(v_stack_pE0)))) goto loc_0042CE54;
    goto loc_0042CB94;
loc_0042CE54:
    goto loc_0042CB8E;
loc_0042CE62:
    if ((*(unsigned __int8 *)(a1 + 92)) == 0) goto loc_0042CC4F;
    if ((unsigned __int8)(v_r10) == 0) goto loc_0042CC4F;
    v_rdi = (unsigned int)((v_rdi) | ((unsigned int)((unsigned int)(v_stack_pE0))));
    v_rbx = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 24))));
    if (((unsigned __int8)(v_r10)) == ((unsigned __int8)((unsigned int)(v_stack_pE0)))) { v_rbx = (unsigned int)((unsigned int)(v_stack_pE0)); }
    goto loc_0042CBB3;
loc_0042CE86:
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 61)) + (1));
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 61) = (unsigned __int8)(result);
    if (((unsigned __int8)(result)) < (*(unsigned __int8 *)(v_rbx + v_rbp * 1 + 118))) goto loc_0042CE1C;
    *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 60) = 1;
    goto loc_0042CE1C;
loc_0042CEC7:
    goto loc_0042CE24;
loc_0042CED0:
    result = (unsigned int)((unsigned int)(*(unsigned __int8 *)((unsigned __int8)(result) + v_rbp * 1 + 52)));
    if ((unsigned __int8)(*(unsigned __int8 *)((unsigned __int8)(result) + v_rbp * 1 + 52)) == 0) { result = 2; }
    result = 1;
    if (1 == 0) { result = 2; }
    v_stack_pD0 = (unsigned __int8)(result);
    goto loc_0042CC69;
loc_0042CEF5:
    if (1 != 1) goto loc_0042CD37;
    a2 = 0;
loc_0042CF1D:
    v_rbx = (unsigned int)((v_rbx) + (*(unsigned int *)(v_rip + 12157373)));
    v_rdi = (unsigned int)((v_rdi) | (32));
    goto loc_0042CD37;
loc_0042CF2B:
    if (((unsigned int)((unsigned int)(v_stack_pD8))) == 0) goto loc_0042CDEE;
    goto loc_0042CCB3;
loc_0042CF38:
    *(unsigned __int8 *)((unsigned int)(v_stack_p20) + 238) = 0;
    if (((unsigned int)(v_rbx)) <= ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_p20) + 240))))))) { v_rbx = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_p20) + 240))))); }
    goto loc_0042CCCC;
}
```

## 5. (Beta) C Style

```c
int64_t PpmPerfSelectProcessorState(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r13;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint32_t v_stack_m64;
    uint32_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint32_t v_stack_m90;
    uint32_t v_stack_m98;
    uint32_t v_stack_mA0;
    uint32_t v_stack_mA8;
    uint32_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint32_t v_stack_p60;
    uint32_t v_stack_p64;
    uint64_t v_stack_p68;
    uint8_t v_stack_p8;
    uint8_t v_stack_pD0;
    uint32_t v_stack_pD8;
    uint32_t v_stack_pE0;
    uint32_t v_stack_pE8;

    local_rsp = (local_rsp) - (136);
    local_rdi = 0;
    v_stack_m60 = *(uint64_t *)(arg1);
    v_stack_m50 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x8);
    a3 = (uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB9A37F)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB9A37F)))) > ((uint32_t)(local_rdi + 100))) { a3 = (uint32_t)(local_rdi + 100); }
    v_stack_p20 = 1;
    a2 = ((int32_t)(*(uint32_t *)(v_rip + 0xAE0362))) * ((int32_t)(*(uint32_t *)(v_rip + 0xAE0362)));
    local_rbp = (*(uint64_t *)(v_rip + 0x9DB8A3) + 40) + (a2);
    if (*(uint64_t *)(arg1 + 0x10) == 0) goto loc_0042CAFD;
    if ((*(uint64_t *)(v_rip + 0x9DB8A3)) == (*(uint64_t *)(v_rip + 0xADAC81))) goto loc_0042CDC0;
loc_0042CAFD:
    result = PpmGetPerfPolicyClass(Arg1, a2, a3, (uint32_t)(*(uint32_t *)(local_rbp + 0x48)));
    v_stack_m58 = (uint8_t)(result);
    v_stack_m64 = (uint32_t)(*(uint8_t *)((uint8_t)(result) + local_rbp * 1 + 0x2E));
    v_stack_m68 = (uint32_t)(*(uint8_t *)((uint8_t)(result) + local_rbp * 1 + 0x30));
    v_stack_p8 = (uint8_t)(*(uint8_t *)((uint8_t)(result) + local_rbp * 1 + 0x32));
    v_stack_p10 = (uint32_t)(*(uint8_t *)((uint8_t)(result) + local_rbp * 1 + 0x36));
    local_r13 = (uint32_t)((*(uint8_t *)((uint8_t)(result) + local_rbp * 1 + 0x36) + *(uint8_t *)((uint8_t)(result) + local_rbp * 1 + 0x38) * 1) >> (1));
    if (*(uint64_t *)(arg1 + 0x10) == 0) goto loc_0042CB6E;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rbp + (uint8_t)(result) * 4 + 0x6C)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbp + (uint8_t)(result) * 4 + 0x64))))) goto loc_0042CE86;
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x3C) = 0;
loc_0042CB6E:
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(local_rbp + 0x48)) - 1)) & (0xFFFFFFFDULL)) != 0) goto loc_0042CE30;
loc_0042CB8E:
loc_0042CB94:
    if ((*(uint8_t *)(v_stack_m60 + 0x20A)) != 0) goto loc_0042CC44;
    v_stack_p20 = 5;
loc_0042CBB3:
    v_stack_m90 = (uint32_t)((uint32_t)(v_stack_p20));
    v_stack_m98 = (uint32_t)(*(uint8_t *)(v_stack_m58 + local_rbp * 1 + 0xAF));
    v_stack_mA0 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbp + 0x58)));
    v_stack_mA8 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbp + v_stack_m58 * 4 + 0x50)));
    result = guard_dispatch_icall(v_stack_m50, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m60 + 0x1C4)))))), (uint32_t)(*(uint32_t *)(v_stack_m60 + 0x1CC)), (uint32_t)(*(uint32_t *)(v_stack_m60 + 0x1C4)));
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x38) = (uint32_t)(result);
    v_stack_mA8 = 0;
    result = PpmEventPerfSelectProcessorState(Arg1, (uint32_t)(v_stack_p18), (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m60 + 0x1C4)))))), (uint32_t)((uint32_t)(result)));
    local_rsp = (local_rsp) + (136);
    return result;
loc_0042CC44:
    if ((*(uint8_t *)(arg1 + 0x44)) != 0) goto loc_0042CE62;
loc_0042CC4F:
    local_r10 = (uint32_t)((uint32_t)(*(uint8_t *)(v_rip + 0xB98522)));
    if (((uint8_t)(*(uint8_t *)(v_rip + 0xB98522))) > ((uint8_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m60 + 0x1C4))))))))) { local_r10 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m60 + 0x1C4))))))); }
    if ((uint8_t)(local_r13) == 0) goto loc_0042CED0;
loc_0042CC69:
    a2 = 0;
    if ((*(uint32_t *)(v_rip + 0xB98507)) == 0) goto loc_0042CE15;
loc_0042CC88:
    v_stack_pE0 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)))));
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)))))) > ((uint32_t)(*(uint8_t *)((uint8_t)(result) + local_rbp * 1 + 0x38)))) goto loc_0042CCF2;
loc_0042CC9D:
loc_0042CCA4:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)))))))) < ((uint32_t)((uint32_t)(v_stack_pD8)))) goto loc_0042CD4A;
loc_0042CCB3:
    if ((uint32_t)(v_stack_p20) == 0) goto loc_0042CBB3;
    if ((uint8_t)(*(uint8_t *)((uint32_t)(v_stack_p20) + 0xEE)) != 0) goto loc_0042CF38;
loc_0042CCCC:
    if ((uint8_t)(*(uint8_t *)((uint32_t)(v_stack_p20) + 0xEF)) == 0) goto loc_0042CBB3;
    *(uint8_t *)((uint32_t)(v_stack_p20) + 0xEF) = 0;
    local_rbx = (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x38));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x38)))) <= ((uint32_t)(*(uint8_t *)((uint32_t)(v_stack_p20) + 0xEF)))) { local_rbx = (uint32_t)(*(uint8_t *)((uint32_t)(v_stack_p20) + 0xEF)); }
    goto loc_0042CBB3;
loc_0042CCF2:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x4A0))) + 1);
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x4A0) = (uint32_t)(result);
    if (((uint32_t)(local_rbx)) >= ((uint32_t)((uint32_t)((uint32_t)(result))))) goto loc_0042CC9D;
    if (((uint32_t)(result)) < v_stack_p60) goto loc_0042CC9D;
    if ((uint8_t)(*(uint8_t *)((uint8_t)(result) + local_rbp * 1 + 0x34)) == 0) goto loc_0042CDF9;
    Arg1 = (uint32_t)(((uint8_t)(*(uint8_t *)((uint8_t)(result) + local_rbp * 1 + 0x34))) - (1));
    if (condition_is_equal) goto loc_0042CF1D;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_not_equal) goto loc_0042CEF5;
    local_rdi = (uint32_t)((local_rdi) | (64));
loc_0042CD37:
    local_rbx = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))))) >= ((uint32_t)((uint32_t)((uint32_t)(result))))) { local_rbx = (uint32_t)((uint32_t)((uint32_t)(result))); }
    goto loc_0042CCA4;
loc_0042CD4A:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x4A4))) + 1);
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x4A4) = (uint32_t)(result);
    if (((uint32_t)(local_rbx)) <= 1) goto loc_0042CCB3;
    if (((uint32_t)(result)) < v_stack_p64) goto loc_0042CCB3;
    v_stack_pE8 = 3;
    if ((uint32_t)(v_stack_pD0) != 0) goto loc_0042CDA3;
    a2 = 0;
    goto loc_0042CCB3;
loc_0042CDA3:
    Arg1 = (uint32_t)(((uint8_t)(local_r13)) - (0));
    if (condition_is_not_equal) goto loc_0042CF2B;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)))))))) <= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB9832F))))) goto loc_0042CDEE;
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28))))))) - ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB9832F)))));
    goto loc_0042CCB3;
loc_0042CDC0:
    if ((*(uint8_t *)(v_rip + 0xAE0085)) == ((uint8_t)(local_rdi))) goto loc_0042CAFD;
    if ((*(uint8_t *)((uint32_t)(v_stack_p20) + 0xE9)) >= ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28))))) goto loc_0042CAFD;
    local_rbp = (v_rip + 11381255) + (0);
    goto loc_0042CAFD;
loc_0042CDEE:
    goto loc_0042CCB3;
loc_0042CDF9:
    a2 = 0;
    local_rdi = (uint32_t)(((uint32_t)(0x1000ULL)) | (16));
    goto loc_0042CD37;
loc_0042CE15:
    goto loc_0042CC88;
loc_0042CE1C:
    if ((uint8_t)((uint8_t)(local_r13)) != 0) goto loc_0042CEC7;
loc_0042CE24:
    goto loc_0042CB6E;
loc_0042CE30:
    if ((*(uint32_t *)(v_rip + 0xB99E91)) != 0) goto loc_0042CE54;
    if (((uint32_t)((uint32_t)((uint32_t)(result)) - 5)) <= ((uint32_t)((uint32_t)(v_stack_pE0)))) goto loc_0042CE54;
    goto loc_0042CB94;
loc_0042CE54:
    goto loc_0042CB8E;
loc_0042CE62:
    if ((*(uint8_t *)(arg1 + 0x5C)) == 0) goto loc_0042CC4F;
    if ((uint8_t)(local_r10) == 0) goto loc_0042CC4F;
    local_rdi = (uint32_t)((local_rdi) | ((uint32_t)((uint32_t)(v_stack_pE0))));
    local_rbx = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18))));
    if (((uint8_t)(local_r10)) == ((uint8_t)((uint32_t)(v_stack_pE0)))) { local_rbx = (uint32_t)((uint32_t)(v_stack_pE0)); }
    goto loc_0042CBB3;
loc_0042CE86:
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x3D)) + (1));
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x3D) = (uint8_t)(result);
    if (((uint8_t)(result)) < (*(uint8_t *)(local_rbx + local_rbp * 1 + 0x76))) goto loc_0042CE1C;
    *(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x3C) = 1;
    goto loc_0042CE1C;
loc_0042CEC7:
    goto loc_0042CE24;
loc_0042CED0:
    result = (uint32_t)((uint32_t)(*(uint8_t *)((uint8_t)(result) + local_rbp * 1 + 0x34)));
    if ((uint8_t)(*(uint8_t *)((uint8_t)(result) + local_rbp * 1 + 0x34)) == 0) { result = 2; }
    result = 1;
    if (1 == 0) { result = 2; }
    v_stack_pD0 = (uint8_t)(result);
    goto loc_0042CC69;
loc_0042CEF5:
    if (1 != 1) goto loc_0042CD37;
    a2 = 0;
loc_0042CF1D:
    local_rbx = (uint32_t)((local_rbx) + (*(uint32_t *)(v_rip + 0xB981BD)));
    local_rdi = (uint32_t)((local_rdi) | (32));
    goto loc_0042CD37;
loc_0042CF2B:
    if (((uint32_t)((uint32_t)(v_stack_pD8))) == 0) goto loc_0042CDEE;
    goto loc_0042CCB3;
loc_0042CF38:
    *(uint8_t *)((uint32_t)(v_stack_p20) + 0xEE) = 0;
    if (((uint32_t)(local_rbx)) <= ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_p20) + 0xF0))))))) { local_rbx = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_p20) + 0xF0))))); }
    goto loc_0042CCCC;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x28` | `32` | `R` |
| `Arg1` | `+ 0x3E` | `16` | `R` |
| `Arg1` | `+ 0x44` | `8` | `R` |
| `Arg1` | `+ 0x5C` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0042CA78&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
