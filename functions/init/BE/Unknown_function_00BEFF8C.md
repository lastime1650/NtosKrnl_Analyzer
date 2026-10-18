# sub_00BEFF8C

- RVA: `0x00BEFF8C`–`0x00BF1284` (길이 `4,856` bytes)
- VA: `0x0000000140BEFF8C`
- 실행 섹션: `INIT`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C2BA4`
- 디코드: `1,275`개 명령, `4,856/4,856` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **24**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00BEFFC5` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BF002F` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BF0082` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BF0130` → [sub_00BE7AF8](../../initkdbg/BE/Unknown_function_00BE7AF8.md) (function, `0x00BE7AF8`)
- `0x00BF01CC` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BF01E6` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BF02D7` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BF0505` → [MmImageSectionPagable](../../page/A4/MmImageSectionPagable_function_00A4B78C.md) (function, `0x00A4B78C`)
- `0x00BF053F` → [KeInitializeGate](../../text/49/KeInitializeGate_function_004953F8.md) (function, `0x004953F8`)
- `0x00BF075C` → [MmImageSectionPagable](../../page/A4/MmImageSectionPagable_function_00A4B78C.md) (function, `0x00A4B78C`)
- `0x00BF09E1` → [sub_0051AFB0](../../text/51/Unknown_function_0051AFB0.md) (function, `0x0051AFB0`)
- `0x00BF0AF6` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BF0CF3` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BF0D6F` → [KeWaitForGate](../../text/2C/KeWaitForGate_function_002CA794.md) (function, `0x002CA794`)
- `0x00BF0D7D` → [ExQueueWorkItem](../../text/2F/ExQueueWorkItem_function_002F9520.md) (function, `0x002F9520`)
- `0x00BF0DA2` → [KeWaitForGate](../../text/2C/KeWaitForGate_function_002CA794.md) (function, `0x002CA794`)
- `0x00BF0DD4` → [KeWaitForGate](../../text/2C/KeWaitForGate_function_002CA794.md) (function, `0x002CA794`)
- `0x00BF0E84` → [KeWaitForGate](../../text/2C/KeWaitForGate_function_002CA794.md) (function, `0x002CA794`)
- `0x00BF0ED5` → [sub_00BE7AF8](../../initkdbg/BE/Unknown_function_00BE7AF8.md) (function, `0x00BE7AF8`)
- `0x00BF0F72` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BF0F8C` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BF1101` → [sub_0051AF4C](../../text/51/Unknown_function_0051AF4C.md) (function, `0x0051AF4C`)
- `0x00BF123A` → [sub_00BE8384](../../initkdbg/BE/Unknown_function_00BE8384.md) (function, `0x00BE8384`)
- `0x00BF127E` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [sub_0050C0E0](../../text/50/Unknown_function_0050C0E0.md) at `0x0051151B`
- [FsRtlMdlReadCompleteDevEx](../../initkdbg/BD/FsRtlMdlReadCompleteDevEx_function_00BD1010.md) at `0x00BD7572`
- [sub_00BE3A04](../../initkdbg/BE/Unknown_function_00BE3A04.md) at `0x00BE4074`
- [sub_00BF16D0](../BF/Unknown_function_00BF16D0.md) at `0x00BF976D`
- [sub_00BF16D0](../BF/Unknown_function_00BF16D0.md) at `0x00BFD0B5`
- [sub_00BF16D0](../BF/Unknown_function_00BF16D0.md) at `0x00C00700`
- [sub_00BF16D0](../BF/Unknown_function_00BF16D0.md) at `0x00C1123F`

### Static image references
- `0x00BF0D4B` → RVA `0x00BF1290` (`INIT`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **24**
  - `0x00BEFFC5` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (`INIT` → `INITKDBG`)
  - `0x00BF002F` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (`INIT` → `INITKDBG`)
  - `0x00BF0082` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (`INIT` → `INITKDBG`)
  - `0x00BF0130` → [sub_00BE7AF8](../../initkdbg/BE/Unknown_function_00BE7AF8.md) (`INIT` → `INITKDBG`)
  - `0x00BF01CC` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (`INIT` → `INITKDBG`)
  - `0x00BF01E6` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (`INIT` → `INITKDBG`)
  - `0x00BF02D7` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (`INIT` → `INITKDBG`)
  - `0x00BF0505` → [MmImageSectionPagable](../../page/A4/MmImageSectionPagable_function_00A4B78C.md) (`INIT` → `PAGE`)
  - `0x00BF053F` → [KeInitializeGate](../../text/49/KeInitializeGate_function_004953F8.md) (`INIT` → `.text`)
  - `0x00BF075C` → [MmImageSectionPagable](../../page/A4/MmImageSectionPagable_function_00A4B78C.md) (`INIT` → `PAGE`)
  - `0x00BF09E1` → [sub_0051AFB0](../../text/51/Unknown_function_0051AFB0.md) (`INIT` → `.text`)
  - `0x00BF0AF6` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (`INIT` → `INITKDBG`)
  - `0x00BF0CF3` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (`INIT` → `INITKDBG`)
  - `0x00BF0D6F` → [KeWaitForGate](../../text/2C/KeWaitForGate_function_002CA794.md) (`INIT` → `.text`)
  - `0x00BF0D7D` → [ExQueueWorkItem](../../text/2F/ExQueueWorkItem_function_002F9520.md) (`INIT` → `.text`)
  - `0x00BF0DA2` → [KeWaitForGate](../../text/2C/KeWaitForGate_function_002CA794.md) (`INIT` → `.text`)
  - `0x00BF0DD4` → [KeWaitForGate](../../text/2C/KeWaitForGate_function_002CA794.md) (`INIT` → `.text`)
  - `0x00BF0E84` → [KeWaitForGate](../../text/2C/KeWaitForGate_function_002CA794.md) (`INIT` → `.text`)
  - `0x00BF0ED5` → [sub_00BE7AF8](../../initkdbg/BE/Unknown_function_00BE7AF8.md) (`INIT` → `INITKDBG`)
  - `0x00BF0F72` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (`INIT` → `INITKDBG`)
  - `0x00BF0F8C` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (`INIT` → `INITKDBG`)
  - `0x00BF1101` → [sub_0051AF4C](../../text/51/Unknown_function_0051AF4C.md) (`INIT` → `.text`)
  - `0x00BF123A` → [sub_00BE8384](../../initkdbg/BE/Unknown_function_00BE8384.md) (`INIT` → `INITKDBG`)
  - `0x00BF127E` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BEFF8C  48 8B C4                        mov rax, rsp
00BEFF8F  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
00BEFF93  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
00BEFF97  48 89 48 08                     mov qword ptr [rax + 8], rcx
00BEFF9B  55                              push rbp
00BEFF9C  53                              push rbx
00BEFF9D  56                              push rsi
00BEFF9E  57                              push rdi
00BEFF9F  41 54                           push r12
00BEFFA1  41 55                           push r13
00BEFFA3  41 56                           push r14
00BEFFA5  41 57                           push r15
00BEFFA7  48 8D A8 E8 FE FF FF            lea rbp, [rax - 0x118]
00BEFFAE  48 81 EC D8 01 00 00            sub rsp, 0x1d8
00BEFFB5  48 8B 19                        mov rbx, qword ptr [rcx]
00BEFFB8  4C 8B F2                        mov r14, rdx
00BEFFBB  48 8B CA                        mov rcx, rdx
00BEFFBE  48 8B 83 08 02 00 00            mov rax, qword ptr [rbx + 0x208]
00BEFFC5  E8 96 AA FF FF                  call 0x140beaa60
00BEFFCA  45 33 FF                        xor r15d, r15d
00BEFFCD  4C 8B E8                        mov r13, rax
00BEFFD0  48 85 C0                        test rax, rax
00BEFFD3  0F 84 66 12 00 00               je 0x140bf123f
00BEFFD9  0F B7 40 06                     movzx eax, word ptr [rax + 6]
00BEFFDD  66 89 85 38 01 00 00            mov word ptr [rbp + 0x138], ax
00BEFFE4  66 85 C0                        test ax, ax
00BEFFE7  0F 84 2D 11 00 00               je 0x140bf111a
00BEFFED  41 81 7D 38 00 10 00 00         cmp dword ptr [r13 + 0x38], 0x1000
00BEFFF5  0F 82 1F 11 00 00               jb 0x140bf111a
00BEFFFB  49 F7 C6 FF 0F 00 00            test r14, 0xfff
00BF0002  0F 85 12 11 00 00               jne 0x140bf111a
00BF0008  41 8B 45 54                     mov eax, dword ptr [r13 + 0x54]
00BF000C  BE 25 02 00 C0                  mov esi, 0xc0000225
00BF0011  48 8B 8B 38 05 00 00            mov rcx, qword ptr [rbx + 0x538]
00BF0018  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
00BF001C  44 0F 20 C7                     mov rdi, cr8
00BF0020  41 8D 47 0F                     lea eax, [r15 + 0xf]
00BF0024  44 0F 22 C0                     mov cr8, rax
00BF0028  48 8B 83 60 01 00 00            mov rax, qword ptr [rbx + 0x160]
00BF002F  E8 2C AA FF FF                  call 0x140beaa60
00BF0034  48 8B 83 20 06 00 00            mov rax, qword ptr [rbx + 0x620]
00BF003B  45 8D 67 18                     lea r12d, [r15 + 0x18]
00BF003F  48 8B 08                        mov rcx, qword ptr [rax]
00BF0042  8B 01                           mov eax, dword ptr [rcx]
00BF0044  48 8D 51 10                     lea rdx, [rcx + 0x10]
00BF0048  48 8D 0C 40                     lea rcx, [rax + rax*2]
00BF004C  48 8D 04 CA                     lea rax, [rdx + rcx*8]
00BF0050  4C 39 72 08                     cmp qword ptr [rdx + 8], r14
00BF0054  74 0A                           je 0x140bf0060
00BF0056  49 03 D4                        add rdx, r12
00BF0059  48 3B D0                        cmp rdx, rax
00BF005C  72 F2                           jb 0x140bf0050
00BF005E  EB 14                           jmp 0x140bf0074
00BF0060  0F 10 02                        movups xmm0, xmmword ptr [rdx]
00BF0063  41 8B F7                        mov esi, r15d
00BF0066  F2 0F 10 4A 10                  movsd xmm1, qword ptr [rdx + 0x10]
00BF006B  0F 11 45 B0                     movups xmmword ptr [rbp - 0x50], xmm0
00BF006F  F2 0F 11 4D C0                  movsd qword ptr [rbp - 0x40], xmm1
00BF0074  48 8B 8B 38 05 00 00            mov rcx, qword ptr [rbx + 0x538]
00BF007B  48 8B 83 A0 01 00 00            mov rax, qword ptr [rbx + 0x1a0]
00BF0082  E8 D9 A9 FF FF                  call 0x140beaa60
00BF0087  40 0F B6 C7                     movzx eax, dil
00BF008B  44 0F 22 C0                     mov cr8, rax
00BF008F  BF 01 00 00 00                  mov edi, 1
00BF0094  41 83 CA FF                     or r10d, 0xffffffff
00BF0098  45 33 C9                        xor r9d, r9d
00BF009B  41 BB F8 FF FF FF               mov r11d, 0xfffffff8
00BF00A1  44 8D 7F 07                     lea r15d, [rdi + 7]
00BF00A5  85 F6                           test esi, esi
00BF00A7  79 38                           jns 0x140bf00e1
00BF00A9  41 8B CC                        mov ecx, r12d
00BF00AC  48 8D 45 B0                     lea rax, [rbp - 0x50]
00BF00B0  8D 57 02                        lea edx, [rdi + 2]
00BF00B3  4C 89 08                        mov qword ptr [rax], r9
00BF00B6  41 03 CB                        add ecx, r11d
00BF00B9  49 03 C7                        add rax, r15
00BF00BC  48 2B D7                        sub rdx, rdi
00BF00BF  75 F2                           jne 0x140bf00b3
00BF00C1  85 C9                           test ecx, ecx
00BF00C3  74 0B                           je 0x140bf00d0
00BF00C5  44 88 08                        mov byte ptr [rax], r9b
00BF00C8  48 03 C7                        add rax, rdi
00BF00CB  41 03 CA                        add ecx, r10d
00BF00CE  75 F5                           jne 0x140bf00c5
00BF00D0  41 8B 45 50                     mov eax, dword ptr [r13 + 0x50]
00BF00D4  89 45 C0                        mov dword ptr [rbp - 0x40], eax
00BF00D7  4C 89 75 B8                     mov qword ptr [rbp - 0x48], r14
00BF00DB  48 89 7D B0                     mov qword ptr [rbp - 0x50], rdi
00BF00DF  EB 03                           jmp 0x140bf00e4
00BF00E1  8B 45 C0                        mov eax, dword ptr [rbp - 0x40]
00BF00E4  44 8B 83 44 09 00 00            mov r8d, dword ptr [rbx + 0x944]
00BF00EB  49 8B CE                        mov rcx, r14
00BF00EE  81 E1 FF 0F 00 00               and ecx, 0xfff
00BF00F4  48 81 C1 FF 0F 00 00            add rcx, 0xfff
00BF00FB  48 03 C1                        add rax, rcx
00BF00FE  48 C1 E8 0C                     shr rax, 0xc
00BF0102  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00BF0107  44 8D 34 80                     lea r14d, [rax + rax*4]
00BF010B  8B 83 04 08 00 00               mov eax, dword ptr [rbx + 0x804]
00BF0111  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00BF0115  83 C0 30                        add eax, 0x30
00BF0118  41 C1 E6 02                     shl r14d, 2
00BF011C  41 03 C6                        add eax, r14d
00BF011F  3B 83 64 0A 00 00               cmp eax, dword ptr [rbx + 0xa64]
00BF0125  0F 86 DC 00 00 00               jbe 0x140bf0207
00BF012B  8B D0                           mov edx, eax
00BF012D  48 8B CB                        mov rcx, rbx
00BF0130  E8 C3 79 FF FF                  call 0x140be7af8
00BF0135  45 33 C9                        xor r9d, r9d
00BF0138  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00BF013D  48 8B F0                        mov rsi, rax
00BF0140  48 85 C0                        test rax, rax
00BF0143  0F 84 9C 0D 00 00               je 0x140bf0ee5
00BF0149  8B 8B D8 09 00 00               mov ecx, dword ptr [rbx + 0x9d8]
00BF014F  F6 C1 02                        test cl, 2
00BF0152  0F 85 9C 00 00 00               jne 0x140bf01f4
00BF0158  8B 83 04 08 00 00               mov eax, dword ptr [rbx + 0x804]
00BF015E  81 E1 00 00 00 10               and ecx, 0x10000000
00BF0164  4C 8B 83 E8 07 00 00            mov r8, qword ptr [rbx + 0x7e8]
00BF016B  F7 D9                           neg ecx
00BF016D  1B C9                           sbb ecx, ecx
00BF016F  23 8B 44 09 00 00               and ecx, dword ptr [rbx + 0x944]
00BF0175  41 3B C7                        cmp eax, r15d
00BF0178  72 14                           jb 0x140bf018e
00BF017A  8B D0                           mov edx, eax
00BF017C  48 C1 EA 03                     shr rdx, 3
00BF0180  4C 89 0B                        mov qword ptr [rbx], r9
00BF0183  83 C0 F8                        add eax, -8
00BF0186  49 03 DF                        add rbx, r15
00BF0189  48 2B D7                        sub rdx, rdi
00BF018C  75 F2                           jne 0x140bf0180
00BF018E  85 C0                           test eax, eax
00BF0190  74 0B                           je 0x140bf019d
00BF0192  44 88 0B                        mov byte ptr [rbx], r9b
00BF0195  48 03 DF                        add rbx, rdi
00BF0198  83 C0 FF                        add eax, -1
00BF019B  75 F5                           jne 0x140bf0192
00BF019D  8B 9E 44 09 00 00               mov ebx, dword ptr [rsi + 0x944]
00BF01A3  89 8E 44 09 00 00               mov dword ptr [rsi + 0x944], ecx
00BF01A9  83 F9 03                        cmp ecx, 3
00BF01AC  74 2E                           je 0x140bf01dc
00BF01AE  F7 86 D8 09 00 00 00 00 00 08   test dword ptr [rsi + 0x9d8], 0x8000000
00BF01B8  75 19                           jne 0x140bf01d3
00BF01BA  85 C9                           test ecx, ecx
00BF01BC  74 15                           je 0x140bf01d3
00BF01BE  48 8B 86 38 02 00 00            mov rax, qword ptr [rsi + 0x238]
00BF01C5  49 8D 48 F8                     lea rcx, [r8 - 8]
00BF01C9  48 8B 11                        mov rdx, qword ptr [rcx]
00BF01CC  E8 8F A8 FF FF                  call 0x140beaa60
00BF01D1  EB 18                           jmp 0x140bf01eb
00BF01D3  48 8B 86 08 01 00 00            mov rax, qword ptr [rsi + 0x108]
00BF01DA  EB 07                           jmp 0x140bf01e3
00BF01DC  48 8B 86 68 03 00 00            mov rax, qword ptr [rsi + 0x368]
00BF01E3  49 8B C8                        mov rcx, r8
00BF01E6  E8 75 A8 FF FF                  call 0x140beaa60
00BF01EB  89 9E 44 09 00 00               mov dword ptr [rsi + 0x944], ebx
00BF01F1  45 33 C9                        xor r9d, r9d
00BF01F4  83 A6 D8 09 00 00 FD            and dword ptr [rsi + 0x9d8], 0xfffffffd
00BF01FB  41 BB F8 FF FF FF               mov r11d, 0xfffffff8
00BF0201  41 83 CA FF                     or r10d, 0xffffffff
00BF0205  EB 0E                           jmp 0x140bf0215
00BF0207  48 8B F3                        mov rsi, rbx
00BF020A  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
00BF020F  89 83 04 08 00 00               mov dword ptr [rbx + 0x804], eax
00BF0215  01 BE 2C 08 00 00               add dword ptr [rsi + 0x82c], edi
00BF021B  B9 30 00 00 00                  mov ecx, 0x30
00BF0220  8B 5C 24 30                     mov ebx, dword ptr [rsp + 0x30]
00BF0224  48 03 DE                        add rbx, rsi
00BF0227  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
00BF022C  48 8B C3                        mov rax, rbx
00BF022F  8D 51 D6                        lea edx, [rcx - 0x2a]
00BF0232  4C 89 08                        mov qword ptr [rax], r9
00BF0235  41 03 CB                        add ecx, r11d
00BF0238  49 03 C7                        add rax, r15
00BF023B  48 2B D7                        sub rdx, rdi
00BF023E  75 F2                           jne 0x140bf0232
00BF0240  85 C9                           test ecx, ecx
00BF0242  74 0B                           je 0x140bf024f
00BF0244  44 88 08                        mov byte ptr [rax], r9b
00BF0247  48 03 C7                        add rax, rdi
00BF024A  41 03 CA                        add ecx, r10d
00BF024D  75 F5                           jne 0x140bf0244
00BF024F  C7 03 21 00 00 00               mov dword ptr [rbx], 0x21
00BF0255  4C 89 4B 08                     mov qword ptr [rbx + 8], r9
00BF0259  44 89 4B 10                     mov dword ptr [rbx + 0x10], r9d
00BF025D  48 8B 8E 38 08 00 00            mov rcx, qword ptr [rsi + 0x838]
00BF0264  48 8B C1                        mov rax, rcx
00BF0267  EB 02                           jmp 0x140bf026b
00BF0269  33 C8                           xor ecx, eax
00BF026B  48 C1 E8 1F                     shr rax, 0x1f
00BF026F  48 85 C0                        test rax, rax
00BF0272  75 F5                           jne 0x140bf0269
00BF0274  48 8B 85 20 01 00 00            mov rax, qword ptr [rbp + 0x120]
00BF027B  48 8D 53 18                     lea rdx, [rbx + 0x18]
00BF027F  0F BA F1 1F                     btr ecx, 0x1f
00BF0283  41 B8 03 00 00 00               mov r8d, 3
00BF0289  89 4B 14                        mov dword ptr [rbx + 0x14], ecx
00BF028C  48 8D 4D B0                     lea rcx, [rbp - 0x50]
00BF0290  48 89 30                        mov qword ptr [rax], rsi
00BF0293  48 8B 01                        mov rax, qword ptr [rcx]
00BF0296  45 03 E3                        add r12d, r11d
00BF0299  48 89 02                        mov qword ptr [rdx], rax
00BF029C  49 03 CF                        add rcx, r15
00BF029F  49 03 D7                        add rdx, r15
00BF02A2  4C 2B C7                        sub r8, rdi
00BF02A5  75 EC                           jne 0x140bf0293
00BF02A7  45 85 E4                        test r12d, r12d
00BF02AA  74 0F                           je 0x140bf02bb
00BF02AC  8A 01                           mov al, byte ptr [rcx]
00BF02AE  48 03 CF                        add rcx, rdi
00BF02B1  88 02                           mov byte ptr [rdx], al
00BF02B3  48 03 D7                        add rdx, rdi
00BF02B6  45 03 E2                        add r12d, r10d
00BF02B9  75 F1                           jne 0x140bf02ac
00BF02BB  48 8B 86 00 02 00 00            mov rax, qword ptr [rsi + 0x200]
00BF02C2  4C 8D 4C 24 50                  lea r9, [rsp + 0x50]
00BF02C7  48 8B 8D 28 01 00 00            mov rcx, qword ptr [rbp + 0x128]
00BF02CE  41 B8 0C 00 00 00               mov r8d, 0xc
00BF02D4  40 8A D7                        mov dl, dil
00BF02D7  E8 84 A7 FF FF                  call 0x140beaa60
00BF02DC  45 33 C0                        xor r8d, r8d
00BF02DF  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00BF02E4  48 85 C0                        test rax, rax
00BF02E7  75 05                           jne 0x140bf02ee
00BF02E9  44 89 44 24 50                  mov dword ptr [rsp + 0x50], r8d
00BF02EE  40 84 BD 30 01 00 00            test byte ptr [rbp + 0x130], dil
00BF02F5  75 0A                           jne 0x140bf0301
00BF02F7  4C 89 44 24 78                  mov qword ptr [rsp + 0x78], r8
00BF02FC  44 89 44 24 50                  mov dword ptr [rsp + 0x50], r8d
00BF0301  8B 44 24 68                     mov eax, dword ptr [rsp + 0x68]
00BF0305  48 8D 53 30                     lea rdx, [rbx + 0x30]
00BF0309  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
00BF030E  48 8D 0C 80                     lea rcx, [rax + rax*4]
00BF0312  48 8D 04 8A                     lea rax, [rdx + rcx*4]
00BF0316  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00BF031B  48 8B C2                        mov rax, rdx
00BF031E  45 3B F7                        cmp r14d, r15d
00BF0321  72 1A                           jb 0x140bf033d
00BF0323  41 8B CE                        mov ecx, r14d
00BF0326  48 C1 E9 03                     shr rcx, 3
00BF032A  48 C7 00 FF FF FF FF            mov qword ptr [rax], 0xffffffffffffffff
00BF0331  41 83 C6 F8                     add r14d, -8
00BF0335  49 03 C7                        add rax, r15
00BF0338  48 2B CF                        sub rcx, rdi
00BF033B  75 ED                           jne 0x140bf032a
00BF033D  45 85 F6                        test r14d, r14d
00BF0340  74 0C                           je 0x140bf034e
00BF0342  C6 00 FF                        mov byte ptr [rax], 0xff
00BF0345  48 03 C7                        add rax, rdi
00BF0348  41 83 C6 FF                     add r14d, -1
00BF034C  75 F4                           jne 0x140bf0342
00BF034E  0F B7 85 38 01 00 00            movzx eax, word ptr [rbp + 0x138]
00BF0355  41 8B D0                        mov edx, r8d
00BF0358  41 0F B7 5D 14                  movzx ebx, word ptr [r13 + 0x14]
00BF035D  41 BE 77 78 00 00               mov r14d, 0x7877
00BF0363  48 83 C3 18                     add rbx, 0x18
00BF0367  41 BA 77 72 00 00               mov r10d, 0x7277
00BF036D  49 03 DD                        add rbx, r13
00BF0370  41 BB 77 77 00 00               mov r11d, 0x7777
00BF0376  48 8D 0C 80                     lea rcx, [rax + rax*4]
00BF037A  41 B9 54 41 00 00               mov r9d, 0x4154
00BF0380  F7 43 24 00 00 00 02            test dword ptr [rbx + 0x24], 0x2000000
00BF0387  48 8D 04 CB                     lea rax, [rbx + rcx*8]
00BF038B  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00BF0390  75 33                           jne 0x140bf03c5
00BF0392  8B 0B                           mov ecx, dword ptr [rbx]
00BF0394  48 8D 43 04                     lea rax, [rbx + 4]
00BF0398  81 F9 49 4E 49 54               cmp ecx, 0x54494e49
00BF039E  75 08                           jne 0x140bf03a8
00BF03A0  81 38 4B 44 42 47               cmp dword ptr [rax], 0x4742444b
00BF03A6  74 1D                           je 0x140bf03c5
00BF03A8  81 F9 50 41 47 45               cmp ecx, 0x45474150
00BF03AE  75 28                           jne 0x140bf03d8
00BF03B0  0F B7 08                        movzx ecx, word ptr [rax]
00BF03B3  66 41 3B CE                     cmp cx, r14w
00BF03B7  74 0C                           je 0x140bf03c5
00BF03B9  66 41 3B CA                     cmp cx, r10w
00BF03BD  74 06                           je 0x140bf03c5
00BF03BF  66 41 3B CB                     cmp cx, r11w
00BF03C3  75 21                           jne 0x140bf03e6
00BF03C5  8B D7                           mov edx, edi
00BF03C7  44 39 43 24                     cmp dword ptr [rbx + 0x24], r8d
00BF03CB  0F 8D E2 00 00 00               jge 0x140bf04b3
00BF03D1  8B D7                           mov edx, edi
00BF03D3  E9 DF 00 00 00                  jmp 0x140bf04b7
00BF03D8  81 F9 45 52 52 41               cmp ecx, 0x41525245
00BF03DE  75 06                           jne 0x140bf03e6
00BF03E0  66 44 39 08                     cmp word ptr [rax], r9w
00BF03E4  74 DF                           je 0x140bf03c5
00BF03E6  4C 8B 86 50 09 00 00            mov r8, qword ptr [rsi + 0x950]
00BF03ED  4C 8B CB                        mov r9, rbx
00BF03F0  4C 8B 96 58 09 00 00            mov r10, qword ptr [rsi + 0x958]
00BF03F7  4D 2B C8                        sub r9, r8
00BF03FA  4C 8B 9E 60 09 00 00            mov r11, qword ptr [rsi + 0x960]
00BF0401  41 83 CD FF                     or r13d, 0xffffffff
00BF0405  4C 8B B6 68 09 00 00            mov r14, qword ptr [rsi + 0x968]
00BF040C  41 BC 07 00 00 00               mov r12d, 7
00BF0412  43 8A 0C 08                     mov cl, byte ptr [r8 + r9]
00BF0416  41 8A 00                        mov al, byte ptr [r8]
00BF0419  4C 03 C7                        add r8, rdi
00BF041C  3A C8                           cmp cl, al
00BF041E  75 07                           jne 0x140bf0427
00BF0420  45 03 E5                        add r12d, r13d
00BF0423  75 ED                           jne 0x140bf0412
00BF0425  EB 7C                           jmp 0x140bf04a3
00BF0427  45 8B C7                        mov r8d, r15d
00BF042A  4C 8B CB                        mov r9, rbx
00BF042D  49 8B 09                        mov rcx, qword ptr [r9]
00BF0430  4D 03 CF                        add r9, r15
00BF0433  49 8B 02                        mov rax, qword ptr [r10]
00BF0436  4D 03 D7                        add r10, r15
00BF0439  48 3B C8                        cmp rcx, rax
00BF043C  75 25                           jne 0x140bf0463
00BF043E  41 83 C0 F8                     add r8d, -8
00BF0442  45 3B C7                        cmp r8d, r15d
00BF0445  73 E6                           jae 0x140bf042d
00BF0447  45 85 C0                        test r8d, r8d
00BF044A  74 57                           je 0x140bf04a3
00BF044C  41 8A 09                        mov cl, byte ptr [r9]
00BF044F  4C 03 CF                        add r9, rdi
00BF0452  41 8A 02                        mov al, byte ptr [r10]
00BF0455  4C 03 D7                        add r10, rdi
00BF0458  3A C8                           cmp cl, al
00BF045A  75 07                           jne 0x140bf0463
00BF045C  45 03 C5                        add r8d, r13d
00BF045F  75 EB                           jne 0x140bf044c
00BF0461  EB 40                           jmp 0x140bf04a3
00BF0463  4C 8B C3                        mov r8, rbx
00BF0466  41 B9 04 00 00 00               mov r9d, 4
00BF046C  4D 2B C3                        sub r8, r11
00BF046F  43 8A 0C 03                     mov cl, byte ptr [r11 + r8]
00BF0473  41 8A 03                        mov al, byte ptr [r11]
00BF0476  4C 03 DF                        add r11, rdi
00BF0479  3A C8                           cmp cl, al
00BF047B  75 07                           jne 0x140bf0484
00BF047D  45 03 CD                        add r9d, r13d
00BF0480  75 ED                           jne 0x140bf046f
00BF0482  EB 1F                           jmp 0x140bf04a3
00BF0484  4C 8B C3                        mov r8, rbx
00BF0487  41 B9 06 00 00 00               mov r9d, 6
00BF048D  4D 2B C6                        sub r8, r14
00BF0490  43 8A 0C 06                     mov cl, byte ptr [r14 + r8]
00BF0494  41 8A 06                        mov al, byte ptr [r14]
00BF0497  4C 03 F7                        add r14, rdi
00BF049A  3A C8                           cmp cl, al
00BF049C  75 0D                           jne 0x140bf04ab
00BF049E  45 03 CD                        add r9d, r13d
00BF04A1  75 ED                           jne 0x140bf0490
00BF04A3  45 33 C0                        xor r8d, r8d
00BF04A6  E9 1A FF FF FF                  jmp 0x140bf03c5
00BF04AB  45 33 C0                        xor r8d, r8d
00BF04AE  E9 14 FF FF FF                  jmp 0x140bf03c7
00BF04B3  85 D2                           test edx, edx
00BF04B5  74 1F                           je 0x140bf04d6
00BF04B7  81 3B 49 4E 49 54               cmp dword ptr [rbx], 0x54494e49
00BF04BD  75 17                           jne 0x140bf04d6
00BF04BF  81 7B 04 4B 44 42 47            cmp dword ptr [rbx + 4], 0x4742444b
00BF04C6  75 0E                           jne 0x140bf04d6
00BF04C8  F7 86 DC 09 00 00 00 20 00 00   test dword ptr [rsi + 0x9dc], 0x2000
00BF04D2  41 0F 45 D0                     cmovne edx, r8d
00BF04D6  8B 4B 10                        mov ecx, dword ptr [rbx + 0x10]
00BF04D9  85 D2                           test edx, edx
00BF04DB  8B 53 0C                        mov edx, dword ptr [rbx + 0xc]
00BF04DE  45 8B E0                        mov r12d, r8d
00BF04E1  8B 43 08                        mov eax, dword ptr [rbx + 8]
00BF04E4  41 0F 94 C4                     sete r12b
00BF04E8  3B C8                           cmp ecx, eax
00BF04EA  89 54 24 58                     mov dword ptr [rsp + 0x58], edx
00BF04EE  0F 46 C8                        cmovbe ecx, eax
00BF04F1  44 8D B2 FF 0F 00 00            lea r14d, [rdx + 0xfff]
00BF04F8  44 03 F1                        add r14d, ecx
00BF04FB  48 8B CB                        mov rcx, rbx
00BF04FE  41 81 E6 00 F0 FF FF            and r14d, 0xfffff000
00BF0505  E8 82 B2 E5 FF                  call 0x140a4b78c
00BF050A  45 33 D2                        xor r10d, r10d
00BF050D  85 C0                           test eax, eax
00BF050F  45 8B DA                        mov r11d, r10d
00BF0512  41 0F 95 C3                     setne r11b
00BF0516  F7 86 D8 09 00 00 00 00 10 00   test dword ptr [rsi + 0x9d8], 0x100000
00BF0520  44 89 5C 24 30                  mov dword ptr [rsp + 0x30], r11d
00BF0525  75 27                           jne 0x140bf054e
00BF0527  33 D2                           xor edx, edx
00BF0529  C7 85 38 01 00 00 80 00 00 00   mov dword ptr [rbp + 0x138], 0x80
00BF0533  48 8D 4D D8                     lea rcx, [rbp - 0x28]
00BF0537  48 89 75 D0                     mov qword ptr [rbp - 0x30], rsi
00BF053B  4C 89 55 F0                     mov qword ptr [rbp - 0x10], r10
00BF053F  E8 B4 4E 8A FF                  call 0x1404953f8
00BF0544  44 8B 5C 24 30                  mov r11d, dword ptr [rsp + 0x30]
00BF0549  45 33 D2                        xor r10d, r10d
00BF054C  EB 30                           jmp 0x140bf057e
00BF054E  B9 78 00 00 00                  mov ecx, 0x78
00BF0553  44 89 95 38 01 00 00            mov dword ptr [rbp + 0x138], r10d
00BF055A  48 8D 45 D0                     lea rax, [rbp - 0x30]
00BF055E  8D 51 97                        lea edx, [rcx - 0x69]
00BF0561  4C 89 10                        mov qword ptr [rax], r10
00BF0564  83 C1 F8                        add ecx, -8
00BF0567  49 03 C7                        add rax, r15
00BF056A  48 2B D7                        sub rdx, rdi
00BF056D  75 F2                           jne 0x140bf0561
00BF056F  85 C9                           test ecx, ecx
00BF0571  74 0B                           je 0x140bf057e
00BF0573  44 88 10                        mov byte ptr [rax], r10b
00BF0576  48 03 C7                        add rax, rdi
00BF0579  83 C1 FF                        add ecx, -1
00BF057C  75 F5                           jne 0x140bf0573
00BF057E  48 8B 95 28 01 00 00            mov rdx, qword ptr [rbp + 0x128]
00BF0585  45 8B EA                        mov r13d, r10d
00BF0588  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
00BF058D  48 8B C2                        mov rax, rdx
00BF0590  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
00BF0595  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
00BF059A  49 3B C8                        cmp rcx, r8
00BF059D  0F 84 8A 02 00 00               je 0x140bf082d
00BF05A3  48 83 C3 04                     add rbx, 4
00BF05A7  44 3B 6C 24 58                  cmp r13d, dword ptr [rsp + 0x58]
00BF05AC  0F 82 D1 01 00 00               jb 0x140bf0783
00BF05B2  45 3B EE                        cmp r13d, r14d
00BF05B5  0F 82 C1 01 00 00               jb 0x140bf077c
00BF05BB  48 8D 43 24                     lea rax, [rbx + 0x24]
00BF05BF  48 3B 44 24 68                  cmp rax, qword ptr [rsp + 0x68]
00BF05C4  0F 84 2D 02 00 00               je 0x140bf07f7
00BF05CA  44 3B 6B 30                     cmp r13d, dword ptr [rbx + 0x30]
00BF05CE  0F 82 23 02 00 00               jb 0x140bf07f7
00BF05D4  48 83 C3 28                     add rbx, 0x28
00BF05D8  41 8B D2                        mov edx, r10d
00BF05DB  F7 43 20 00 00 00 02            test dword ptr [rbx + 0x20], 0x2000000
00BF05E2  75 12                           jne 0x140bf05f6
00BF05E4  8B 43 FC                        mov eax, dword ptr [rbx - 4]
00BF05E7  3D 49 4E 49 54                  cmp eax, 0x54494e49
00BF05EC  75 0F                           jne 0x140bf05fd
00BF05EE  81 3B 4B 44 42 47               cmp dword ptr [rbx], 0x4742444b
00BF05F4  75 31                           jne 0x140bf0627
00BF05F6  8B D7                           mov edx, edi
00BF05F8  E9 06 01 00 00                  jmp 0x140bf0703
00BF05FD  3D 50 41 47 45                  cmp eax, 0x45474150
00BF0602  75 23                           jne 0x140bf0627
00BF0604  0F B7 03                        movzx eax, word ptr [rbx]
00BF0607  B9 77 78 00 00                  mov ecx, 0x7877
00BF060C  66 3B C1                        cmp ax, cx
00BF060F  74 E5                           je 0x140bf05f6
00BF0611  B9 77 72 00 00                  mov ecx, 0x7277
00BF0616  66 3B C1                        cmp ax, cx
00BF0619  74 DB                           je 0x140bf05f6
00BF061B  B9 77 77 00 00                  mov ecx, 0x7777
00BF0620  66 3B C1                        cmp ax, cx
00BF0623  75 13                           jne 0x140bf0638
00BF0625  EB CF                           jmp 0x140bf05f6
00BF0627  3D 45 52 52 41                  cmp eax, 0x41525245
00BF062C  75 0A                           jne 0x140bf0638
00BF062E  B8 54 41 00 00                  mov eax, 0x4154
00BF0633  66 39 03                        cmp word ptr [rbx], ax
00BF0636  74 BE                           je 0x140bf05f6
00BF0638  4C 8B 86 50 09 00 00            mov r8, qword ptr [rsi + 0x950]
00BF063F  4C 8B CB                        mov r9, rbx
00BF0642  4C 8B 96 58 09 00 00            mov r10, qword ptr [rsi + 0x958]
00BF0649  4D 2B C8                        sub r9, r8
00BF064C  4C 8B 9E 60 09 00 00            mov r11, qword ptr [rsi + 0x960]
00BF0653  41 BC 07 00 00 00               mov r12d, 7
00BF0659  4C 8B B6 68 09 00 00            mov r14, qword ptr [rsi + 0x968]
00BF0660  43 8A 4C 08 FC                  mov cl, byte ptr [r8 + r9 - 4]
00BF0665  41 8A 00                        mov al, byte ptr [r8]
00BF0668  4C 03 C7                        add r8, rdi
00BF066B  3A C8                           cmp cl, al
00BF066D  75 0B                           jne 0x140bf067a
00BF066F  41 83 C4 FF                     add r12d, -1
00BF0673  75 EB                           jne 0x140bf0660
00BF0675  E9 84 00 00 00                  jmp 0x140bf06fe
00BF067A  45 8B C7                        mov r8d, r15d
00BF067D  4C 8D 4B FC                     lea r9, [rbx - 4]
00BF0681  49 8B 09                        mov rcx, qword ptr [r9]
00BF0684  4D 03 CF                        add r9, r15
00BF0687  49 8B 02                        mov rax, qword ptr [r10]
00BF068A  4D 03 D7                        add r10, r15
00BF068D  48 3B C8                        cmp rcx, rax
00BF0690  75 26                           jne 0x140bf06b8
00BF0692  41 83 C0 F8                     add r8d, -8
00BF0696  45 3B C7                        cmp r8d, r15d
00BF0699  73 E6                           jae 0x140bf0681
00BF069B  45 85 C0                        test r8d, r8d
00BF069E  74 5E                           je 0x140bf06fe
00BF06A0  41 8A 09                        mov cl, byte ptr [r9]
00BF06A3  4C 03 CF                        add r9, rdi
00BF06A6  41 8A 02                        mov al, byte ptr [r10]
00BF06A9  4C 03 D7                        add r10, rdi
00BF06AC  3A C8                           cmp cl, al
00BF06AE  75 08                           jne 0x140bf06b8
00BF06B0  41 83 C0 FF                     add r8d, -1
00BF06B4  75 EA                           jne 0x140bf06a0
00BF06B6  EB 46                           jmp 0x140bf06fe
00BF06B8  4C 8B C3                        mov r8, rbx
00BF06BB  41 B9 04 00 00 00               mov r9d, 4
00BF06C1  4D 2B C3                        sub r8, r11
00BF06C4  41 83 CA FF                     or r10d, 0xffffffff
00BF06C8  43 8A 4C 03 FC                  mov cl, byte ptr [r11 + r8 - 4]
00BF06CD  41 8A 03                        mov al, byte ptr [r11]
00BF06D0  4C 03 DF                        add r11, rdi
00BF06D3  3A C8                           cmp cl, al
00BF06D5  75 07                           jne 0x140bf06de
00BF06D7  45 03 CA                        add r9d, r10d
00BF06DA  75 EC                           jne 0x140bf06c8
00BF06DC  EB 20                           jmp 0x140bf06fe
00BF06DE  4C 8B C3                        mov r8, rbx
00BF06E1  41 B9 06 00 00 00               mov r9d, 6
00BF06E7  4D 2B C6                        sub r8, r14
00BF06EA  43 8A 4C 06 FC                  mov cl, byte ptr [r14 + r8 - 4]
00BF06EF  41 8A 06                        mov al, byte ptr [r14]
00BF06F2  4C 03 F7                        add r14, rdi
00BF06F5  3A C8                           cmp cl, al
00BF06F7  75 07                           jne 0x140bf0700
00BF06F9  45 03 CA                        add r9d, r10d
00BF06FC  75 EC                           jne 0x140bf06ea
00BF06FE  8B D7                           mov edx, edi
00BF0700  45 33 D2                        xor r10d, r10d
00BF0703  44 39 53 20                     cmp dword ptr [rbx + 0x20], r10d
00BF0707  7D 04                           jge 0x140bf070d
00BF0709  8B D7                           mov edx, edi
00BF070B  EB 04                           jmp 0x140bf0711
00BF070D  85 D2                           test edx, edx
00BF070F  74 1F                           je 0x140bf0730
00BF0711  81 7B FC 49 4E 49 54            cmp dword ptr [rbx - 4], 0x54494e49
00BF0718  75 16                           jne 0x140bf0730
00BF071A  81 3B 4B 44 42 47               cmp dword ptr [rbx], 0x4742444b
00BF0720  75 0E                           jne 0x140bf0730
00BF0722  F7 86 DC 09 00 00 00 20 00 00   test dword ptr [rsi + 0x9dc], 0x2000
00BF072C  41 0F 45 D2                     cmovne edx, r10d
00BF0730  8B 4B 0C                        mov ecx, dword ptr [rbx + 0xc]
00BF0733  85 D2                           test edx, edx
00BF0735  8B 43 04                        mov eax, dword ptr [rbx + 4]
00BF0738  45 8B E2                        mov r12d, r10d
00BF073B  44 8B 73 08                     mov r14d, dword ptr [rbx + 8]
00BF073F  41 0F 94 C4                     sete r12b
00BF0743  3B C8                           cmp ecx, eax
00BF0745  0F 46 C8                        cmovbe ecx, eax
00BF0748  81 C1 FF 0F 00 00               add ecx, 0xfff
00BF074E  44 03 F1                        add r14d, ecx
00BF0751  48 8D 4B FC                     lea rcx, [rbx - 4]
00BF0755  41 81 E6 00 F0 FF FF            and r14d, 0xfffff000
00BF075C  E8 2B B0 E5 FF                  call 0x140a4b78c
00BF0761  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
00BF0766  45 33 D2                        xor r10d, r10d
00BF0769  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
00BF076E  85 C0                           test eax, eax
00BF0770  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00BF0775  45 8B DA                        mov r11d, r10d
00BF0778  41 0F 95 C3                     setne r11b
00BF077C  45 85 E4                        test r12d, r12d
00BF077F  74 7B                           je 0x140bf07fc
00BF0781  EB 07                           jmp 0x140bf078a
00BF0783  44 3B 6C 24 54                  cmp r13d, dword ptr [rsp + 0x54]
00BF0788  73 72                           jae 0x140bf07fc
00BF078A  41 8B D2                        mov edx, r10d
00BF078D  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00BF0792  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00BF0797  44 8B 01                        mov r8d, dword ptr [rcx]
00BF079A  4C 8B 08                        mov r9, qword ptr [rax]
00BF079D  4D 85 C0                        test r8, r8
00BF07A0  74 1D                           je 0x140bf07bf
00BF07A2  4D 8D 50 FF                     lea r10, [r8 - 1]
00BF07A6  4C 8B 44 24 40                  mov r8, qword ptr [rsp + 0x40]
00BF07AB  4D 03 D1                        add r10, r9
00BF07AE  4D 3B C1                        cmp r8, r9
00BF07B1  72 09                           jb 0x140bf07bc
00BF07B3  4D 3B C2                        cmp r8, r10
00BF07B6  0F 86 89 00 00 00               jbe 0x140bf0845
00BF07BC  45 33 D2                        xor r10d, r10d
00BF07BF  03 D7                           add edx, edi
00BF07C1  48 83 C1 04                     add rcx, 4
00BF07C5  49 03 C7                        add rax, r15
00BF07C8  3B D7                           cmp edx, edi
00BF07CA  72 CB                           jb 0x140bf0797
00BF07CC  44 3B 6C 24 58                  cmp r13d, dword ptr [rsp + 0x58]
00BF07D1  72 05                           jb 0x140bf07d8
00BF07D3  45 85 DB                        test r11d, r11d
00BF07D6  75 0C                           jne 0x140bf07e4
00BF07D8  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
00BF07DD  0F BA 70 10 1F                  btr dword ptr [rax + 0x10], 0x1f
00BF07E2  EB 05                           jmp 0x140bf07e9
00BF07E4  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
00BF07E9  80 60 0F 7F                     and byte ptr [rax + 0xf], 0x7f
00BF07ED  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
00BF07F2  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
00BF07F7  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00BF07FC  48 05 00 10 00 00               add rax, 0x1000
00BF0802  48 83 C1 14                     add rcx, 0x14
00BF0806  41 81 C5 00 10 00 00            add r13d, 0x1000
00BF080D  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00BF0812  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00BF0817  41 BA 00 00 00 00               mov r10d, 0
00BF081D  49 3B C8                        cmp rcx, r8
00BF0820  0F 85 81 FD FF FF               jne 0x140bf05a7
00BF0826  48 8B 95 28 01 00 00            mov rdx, qword ptr [rbp + 0x128]
00BF082D  4C 8B 6C 24 48                  mov r13, qword ptr [rsp + 0x48]
00BF0832  48 BB 01 20 00 04 80 00 10 70   movabs rbx, 0x7010008004002001
00BF083C  49 83 C5 30                     add r13, 0x30
00BF0840  E9 16 06 00 00                  jmp 0x140bf0e5b
00BF0845  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
00BF084A  49 8B C0                        mov rax, r8
00BF084D  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
00BF0852  EB A8                           jmp 0x140bf07fc
00BF0854  45 8B F2                        mov r14d, r10d
00BF0857  49 8B C5                        mov rax, r13
00BF085A  44 38 50 0F                     cmp byte ptr [rax + 0xf], r10b
00BF085E  7C 17                           jl 0x140bf0877
00BF0860  44 03 F7                        add r14d, edi
00BF0863  4B 8D 0C B6                     lea rcx, [r14 + r14*4]
00BF0867  48 8D 04 8D 00 00 00 00         lea rax, [rcx*4]
00BF086F  49 03 C5                        add rax, r13
00BF0872  49 3B C0                        cmp rax, r8
00BF0875  75 E3                           jne 0x140bf085a
00BF0877  44 89 74 24 30                  mov dword ptr [rsp + 0x30], r14d
00BF087C  45 85 F6                        test r14d, r14d
00BF087F  0F 84 8D 05 00 00               je 0x140bf0e12
00BF0885  8B 85 38 01 00 00               mov eax, dword ptr [rbp + 0x138]
00BF088B  85 C0                           test eax, eax
00BF088D  0F 85 30 02 00 00               jne 0x140bf0ac3
00BF0893  41 8B C6                        mov eax, r14d
00BF0896  4C 89 6C 24 40                  mov qword ptr [rsp + 0x40], r13
00BF089B  4C 8B B6 D0 0A 00 00            mov r14, qword ptr [rsi + 0xad0]
00BF08A2  4C 89 75 A8                     mov qword ptr [rbp - 0x58], r14
00BF08A6  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
00BF08AA  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
00BF08AF  41 3B C7                        cmp eax, r15d
00BF08B2  41 8B DF                        mov ebx, r15d
00BF08B5  45 8B E2                        mov r12d, r10d
00BF08B8  0F 42 D8                        cmovb ebx, eax
00BF08BB  85 DB                           test ebx, ebx
00BF08BD  0F 84 15 01 00 00               je 0x140bf09d8
00BF08C3  48 8D 45 68                     lea rax, [rbp + 0x68]
00BF08C7  4D 8B EE                        mov r13, r14
00BF08CA  4C 8B 74 24 38                  mov r14, qword ptr [rsp + 0x38]
00BF08CF  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00BF08D4  49 C7 45 08 00 10 00 00         mov qword ptr [r13 + 8], 0x1000
00BF08DC  45 8B DC                        mov r11d, r12d
00BF08DF  41 C1 E3 0C                     shl r11d, 0xc
00BF08E3  4D 03 DE                        add r11, r14
00BF08E6  4D 89 5D 00                     mov qword ptr [r13], r11
00BF08EA  4D 8B D3                        mov r10, r11
00BF08ED  48 8B 86 38 08 00 00            mov rax, qword ptr [rsi + 0x838]
00BF08F4  81 86 48 08 00 00 00 10 00 00   add dword ptr [rsi + 0x848], 0x1000
00BF08FE  44 8B 8E 34 08 00 00            mov r9d, dword ptr [rsi + 0x834]
00BF0905  49 8D 8B 00 10 00 00            lea rcx, [r11 + 0x1000]
00BF090C  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00BF0911  49 8B C3                        mov rax, r11
00BF0914  4C 3B D9                        cmp r11, rcx
00BF0917  73 0C                           jae 0x140bf0925
00BF0919  0F 18 00                        prefetchnta byte ptr [rax]
00BF091C  48 83 C0 40                     add rax, 0x40
00BF0920  48 3B C1                        cmp rax, rcx
00BF0923  72 F4                           jb 0x140bf0919
00BF0925  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
00BF092A  49 BE 01 20 00 04 80 00 10 70   movabs r14, 0x7010008004002001
00BF0934  4C 8B C6                        mov r8, rsi
00BF0937  C7 44 24 58 20 00 00 00         mov dword ptr [rsp + 0x58], 0x20
00BF093F  49 8B C7                        mov rax, r15
00BF0942  4D 33 02                        xor r8, qword ptr [r10]
00BF0945  41 8B C9                        mov ecx, r9d
00BF0948  4D 03 D7                        add r10, r15
00BF094B  49 D3 C0                        rol r8, cl
00BF094E  4D 33 02                        xor r8, qword ptr [r10]
00BF0951  4D 03 D7                        add r10, r15
00BF0954  49 D3 C0                        rol r8, cl
00BF0957  48 2B C7                        sub rax, rdi
00BF095A  75 E6                           jne 0x140bf0942
00BF095C  49 8B CA                        mov rcx, r10
00BF095F  49 2B CB                        sub rcx, r11
00BF0962  48 33 CE                        xor rcx, rsi
00BF0965  48 8B C1                        mov rax, rcx
00BF0968  48 C1 C0 11                     rol rax, 0x11
00BF096C  48 33 C8                        xor rcx, rax
00BF096F  49 8B C6                        mov rax, r14
00BF0972  48 F7 E1                        mul rcx
00BF0975  44 33 CA                        xor r9d, edx
00BF0978  48 89 55 50                     mov qword ptr [rbp + 0x50], rdx
00BF097C  44 33 C8                        xor r9d, eax
00BF097F  41 83 E1 3F                     and r9d, 0x3f
00BF0983  44 0F 44 CF                     cmove r9d, edi
00BF0987  83 44 24 58 FF                  add dword ptr [rsp + 0x58], -1
00BF098C  75 B1                           jne 0x140bf093f
00BF098E  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
00BF0993  49 8B C0                        mov rax, r8
00BF0996  4C 8B 74 24 38                  mov r14, qword ptr [rsp + 0x38]
00BF099B  EB 03                           jmp 0x140bf09a0
00BF099D  44 33 C0                        xor r8d, eax
00BF09A0  48 C1 E8 1F                     shr rax, 0x1f
00BF09A4  48 85 C0                        test rax, rax
00BF09A7  75 F4                           jne 0x140bf099d
00BF09A9  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
00BF09AE  41 0F BA F0 1F                  btr r8d, 0x1f
00BF09B3  44 03 E7                        add r12d, edi
00BF09B6  49 83 C5 30                     add r13, 0x30
00BF09BA  44 89 02                        mov dword ptr [rdx], r8d
00BF09BD  48 83 C2 04                     add rdx, 4
00BF09C1  48 89 54 24 48                  mov qword ptr [rsp + 0x48], rdx
00BF09C6  44 3B E3                        cmp r12d, ebx
00BF09C9  0F 82 05 FF FF FF               jb 0x140bf08d4
00BF09CF  4C 8B 6C 24 40                  mov r13, qword ptr [rsp + 0x40]
00BF09D4  4C 8B 75 A8                     mov r14, qword ptr [rbp - 0x58]
00BF09D8  44 8B C3                        mov r8d, ebx
00BF09DB  49 8B D6                        mov rdx, r14
00BF09DE  48 8B CE                        mov rcx, rsi
00BF09E1  E8 CA A5 92 FF                  call 0x14051afb0
00BF09E6  45 33 D2                        xor r10d, r10d
00BF09E9  85 DB                           test ebx, ebx
00BF09EB  0F 84 86 00 00 00               je 0x140bf0a77
00BF09F1  8B C3                           mov eax, ebx
00BF09F3  4C 8D 65 68                     lea r12, [rbp + 0x68]
00BF09F7  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00BF09FC  4D 8D 4D 10                     lea r9, [r13 + 0x10]
00BF0A00  4D 8B D5                        mov r10, r13
00BF0A03  4D 8D 5E 10                     lea r11, [r14 + 0x10]
00BF0A07  41 B8 10 00 00 00               mov r8d, 0x10
00BF0A0D  49 8B CB                        mov rcx, r11
00BF0A10  49 8B D2                        mov rdx, r10
00BF0A13  45 8D 68 F2                     lea r13d, [r8 - 0xe]
00BF0A17  48 8B 01                        mov rax, qword ptr [rcx]
00BF0A1A  41 83 C0 F8                     add r8d, -8
00BF0A1E  48 89 02                        mov qword ptr [rdx], rax
00BF0A21  49 03 CF                        add rcx, r15
00BF0A24  49 03 D7                        add rdx, r15
00BF0A27  4C 2B EF                        sub r13, rdi
00BF0A2A  75 EB                           jne 0x140bf0a17
00BF0A2C  45 85 C0                        test r8d, r8d
00BF0A2F  74 10                           je 0x140bf0a41
00BF0A31  8A 01                           mov al, byte ptr [rcx]
00BF0A33  48 03 CF                        add rcx, rdi
00BF0A36  88 02                           mov byte ptr [rdx], al
00BF0A38  48 03 D7                        add rdx, rdi
00BF0A3B  41 83 C0 FF                     add r8d, -1
00BF0A3F  75 F0                           jne 0x140bf0a31
00BF0A41  41 8B 01                        mov eax, dword ptr [r9]
00BF0A44  49 83 C3 30                     add r11, 0x30
00BF0A48  8B C8                           mov ecx, eax
00BF0A4A  49 83 C2 14                     add r10, 0x14
00BF0A4E  41 33 0C 24                     xor ecx, dword ptr [r12]
00BF0A52  49 83 C4 04                     add r12, 4
00BF0A56  0F BA F1 1F                     btr ecx, 0x1f
00BF0A5A  33 C8                           xor ecx, eax
00BF0A5C  41 89 09                        mov dword ptr [r9], ecx
00BF0A5F  49 83 C1 14                     add r9, 0x14
00BF0A63  48 29 7C 24 48                  sub qword ptr [rsp + 0x48], rdi
00BF0A68  75 9D                           jne 0x140bf0a07
00BF0A6A  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
00BF0A6F  45 33 D2                        xor r10d, r10d
00BF0A72  4C 8B 6C 24 40                  mov r13, qword ptr [rsp + 0x40]
00BF0A77  8B C3                           mov eax, ebx
00BF0A79  48 8D 0C 9B                     lea rcx, [rbx + rbx*4]
00BF0A7D  C1 E0 0C                        shl eax, 0xc
00BF0A80  4D 8D 6C 8D 00                  lea r13, [r13 + rcx*4]
00BF0A85  48 01 44 24 38                  add qword ptr [rsp + 0x38], rax
00BF0A8A  8B 44 24 54                     mov eax, dword ptr [rsp + 0x54]
00BF0A8E  2B C3                           sub eax, ebx
00BF0A90  4C 89 6C 24 40                  mov qword ptr [rsp + 0x40], r13
00BF0A95  C1 E3 0F                        shl ebx, 0xf
00BF0A98  01 9E 48 08 00 00               add dword ptr [rsi + 0x848], ebx
00BF0A9E  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
00BF0AA2  85 C0                           test eax, eax
00BF0AA4  0F 85 05 FE FF FF               jne 0x140bf08af
00BF0AAA  44 8B 74 24 30                  mov r14d, dword ptr [rsp + 0x30]
00BF0AAF  48 BB 01 20 00 04 80 00 10 70   movabs rbx, 0x7010008004002001
00BF0AB9  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
00BF0ABE  E9 4A 03 00 00                  jmp 0x140bf0e0d
00BF0AC3  45 85 F6                        test r14d, r14d
00BF0AC6  0F 84 46 03 00 00               je 0x140bf0e12
00BF0ACC  45 8B FA                        mov r15d, r10d
00BF0ACF  44 8B 86 30 08 00 00            mov r8d, dword ptr [rsi + 0x830]
00BF0AD6  45 8B E6                        mov r12d, r14d
00BF0AD9  48 8B 96 D8 0A 00 00            mov rdx, qword ptr [rsi + 0xad8]
00BF0AE0  45 2B E7                        sub r12d, r15d
00BF0AE3  44 3B E0                        cmp r12d, eax
00BF0AE6  B9 40 00 00 00                  mov ecx, 0x40
00BF0AEB  44 0F 47 E0                     cmova r12d, eax
00BF0AEF  48 8B 86 00 01 00 00            mov rax, qword ptr [rsi + 0x100]
00BF0AF6  E8 65 9F FF FF                  call 0x140beaa60
00BF0AFB  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00BF0B00  0F 31                           rdtsc
00BF0B02  48 C1 E2 20                     shl rdx, 0x20
00BF0B06  48 0B C2                        or rax, rdx
00BF0B09  48 8B C8                        mov rcx, rax
00BF0B0C  48 8B D0                        mov rdx, rax
00BF0B0F  48 C1 C9 03                     ror rcx, 3
00BF0B13  48 8B C3                        mov rax, rbx
00BF0B16  48 33 D1                        xor rdx, rcx
00BF0B19  48 F7 E2                        mul rdx
00BF0B1C  48 8B CA                        mov rcx, rdx
00BF0B1F  48 89 55 58                     mov qword ptr [rbp + 0x58], rdx
00BF0B23  48 33 C8                        xor rcx, rax
00BF0B26  48 B8 A3 8B 2E BA E8 A2 8B 2E   movabs rax, 0x2e8ba2e8ba2e8ba3
00BF0B30  48 F7 E1                        mul rcx
00BF0B33  48 D1 EA                        shr rdx, 1
00BF0B36  48 6B C2 0B                     imul rax, rdx, 0xb
00BF0B3A  48 2B C8                        sub rcx, rax
00BF0B3D  83 F9 05                        cmp ecx, 5
00BF0B40  0F 87 8D 00 00 00               ja 0x140bf0bd3
00BF0B46  74 77                           je 0x140bf0bbf
00BF0B48  85 C9                           test ecx, ecx
00BF0B4A  74 5F                           je 0x140bf0bab
00BF0B4C  2B CF                           sub ecx, edi
00BF0B4E  74 48                           je 0x140bf0b98
00BF0B50  2B CF                           sub ecx, edi
00BF0B52  74 30                           je 0x140bf0b84
00BF0B54  3B CF                           cmp ecx, edi
00BF0B56  74 14                           je 0x140bf0b6c
00BF0B58  C7 45 80 94 64 07 67            mov dword ptr [rbp - 0x80], 0x67076494
00BF0B5F  44 8B 4D 80                     mov r9d, dword ptr [rbp - 0x80]
00BF0B63  41 C1 C1 04                     rol r9d, 4
00BF0B67  E9 75 01 00 00                  jmp 0x140bf0ce1
00BF0B6C  C7 45 84 38 39 22 A8            mov dword ptr [rbp - 0x7c], 0xa8223938
00BF0B73  44 8B 4D 84                     mov r9d, dword ptr [rbp - 0x7c]
00BF0B77  41 83 F1 03                     xor r9d, 3
00BF0B7B  41 C1 C9 0F                     ror r9d, 0xf
00BF0B7F  E9 5D 01 00 00                  jmp 0x140bf0ce1
00BF0B84  C7 45 88 0D 91 B5 85            mov dword ptr [rbp - 0x78], 0x85b5910d
00BF0B8B  44 8B 4D 88                     mov r9d, dword ptr [rbp - 0x78]
00BF0B8F  41 C1 C9 02                     ror r9d, 2
00BF0B93  E9 49 01 00 00                  jmp 0x140bf0ce1
00BF0B98  C7 45 8C A1 31 AD B2            mov dword ptr [rbp - 0x74], 0xb2ad31a1
00BF0B9F  44 8B 4D 8C                     mov r9d, dword ptr [rbp - 0x74]
00BF0BA3  41 D1 C1                        rol r9d, 1
00BF0BA6  E9 36 01 00 00                  jmp 0x140bf0ce1
00BF0BAB  C7 45 90 D8 D0 98 D0            mov dword ptr [rbp - 0x70], 0xd098d0d8
00BF0BB2  44 8B 4D 90                     mov r9d, dword ptr [rbp - 0x70]
00BF0BB6  41 C1 C9 06                     ror r9d, 6
00BF0BBA  E9 22 01 00 00                  jmp 0x140bf0ce1
00BF0BBF  C7 45 94 ED 49 8C 28            mov dword ptr [rbp - 0x6c], 0x288c49ed
00BF0BC6  44 8B 4D 94                     mov r9d, dword ptr [rbp - 0x6c]
00BF0BCA  41 C1 C9 05                     ror r9d, 5
00BF0BCE  E9 0E 01 00 00                  jmp 0x140bf0ce1
00BF0BD3  BA 06 00 00 00                  mov edx, 6
00BF0BD8  2B CA                           sub ecx, edx
00BF0BDA  0F 84 EF 00 00 00               je 0x140bf0ccf
00BF0BE0  2B CF                           sub ecx, edi
00BF0BE2  0F 84 D6 00 00 00               je 0x140bf0cbe
00BF0BE8  2B CF                           sub ecx, edi
00BF0BEA  0F 84 BD 00 00 00               je 0x140bf0cad
00BF0BF0  3B CF                           cmp ecx, edi
00BF0BF2  0F 84 A0 00 00 00               je 0x140bf0c98
00BF0BF8  0F 31                           rdtsc
00BF0BFA  48 C1 E2 20                     shl rdx, 0x20
00BF0BFE  48 0B C2                        or rax, rdx
00BF0C01  48 8B C8                        mov rcx, rax
00BF0C04  48 8B D0                        mov rdx, rax
00BF0C07  48 C1 C9 03                     ror rcx, 3
00BF0C0B  48 8B C3                        mov rax, rbx
00BF0C0E  48 33 D1                        xor rdx, rcx
00BF0C11  48 F7 E2                        mul rdx
00BF0C14  4C 8B CA                        mov r9, rdx
00BF0C17  48 89 55 60                     mov qword ptr [rbp + 0x60], rdx
00BF0C1B  44 33 C8                        xor r9d, eax
00BF0C1E  B8 4F EC C4 4E                  mov eax, 0x4ec4ec4f
00BF0C23  41 F7 E1                        mul r9d
00BF0C26  41 8B C9                        mov ecx, r9d
00BF0C29  41 C1 E9 05                     shr r9d, 5
00BF0C2D  C1 EA 03                        shr edx, 3
00BF0C30  45 8B C1                        mov r8d, r9d
00BF0C33  6B C2 1A                        imul eax, edx, 0x1a
00BF0C36  2B C8                           sub ecx, eax
00BF0C38  B8 4F EC C4 4E                  mov eax, 0x4ec4ec4f
00BF0C3D  41 F7 E1                        mul r9d
00BF0C40  83 C1 61                        add ecx, 0x61
00BF0C43  41 C1 E9 05                     shr r9d, 5
00BF0C47  C1 E1 08                        shl ecx, 8
00BF0C4A  C1 EA 03                        shr edx, 3
00BF0C4D  6B C2 1A                        imul eax, edx, 0x1a
00BF0C50  44 2B C0                        sub r8d, eax
00BF0C53  B8 4F EC C4 4E                  mov eax, 0x4ec4ec4f
00BF0C58  41 F7 E1                        mul r9d
00BF0C5B  41 83 C0 41                     add r8d, 0x41
00BF0C5F  44 0B C1                        or r8d, ecx
00BF0C62  C1 EA 03                        shr edx, 3
00BF0C65  6B C2 1A                        imul eax, edx, 0x1a
00BF0C68  41 8B C9                        mov ecx, r9d
00BF0C6B  41 C1 E9 05                     shr r9d, 5
00BF0C6F  41 C1 E0 08                     shl r8d, 8
00BF0C73  2B C8                           sub ecx, eax
00BF0C75  B8 4F EC C4 4E                  mov eax, 0x4ec4ec4f
00BF0C7A  41 F7 E1                        mul r9d
00BF0C7D  83 C1 61                        add ecx, 0x61
00BF0C80  C1 EA 03                        shr edx, 3
00BF0C83  41 0B C8                        or ecx, r8d
00BF0C86  6B C2 1A                        imul eax, edx, 0x1a
00BF0C89  C1 E1 08                        shl ecx, 8
00BF0C8C  44 2B C8                        sub r9d, eax
00BF0C8F  41 83 C1 41                     add r9d, 0x41
00BF0C93  44 0B C9                        or r9d, ecx
00BF0C96  EB 49                           jmp 0x140bf0ce1
00BF0C98  C7 45 98 85 9E 86 B0            mov dword ptr [rbp - 0x68], 0xb0869e85
00BF0C9F  44 8B 4D 98                     mov r9d, dword ptr [rbp - 0x68]
00BF0CA3  41 83 F1 09                     xor r9d, 9
00BF0CA7  41 C1 C9 21                     ror r9d, 0x21
00BF0CAB  EB 34                           jmp 0x140bf0ce1
00BF0CAD  C7 45 9C 42 41 66 64            mov dword ptr [rbp - 0x64], 0x64664142
00BF0CB4  44 8B 4D 9C                     mov r9d, dword ptr [rbp - 0x64]
00BF0CB8  41 C1 C9 08                     ror r9d, 8
00BF0CBC  EB 23                           jmp 0x140bf0ce1
00BF0CBE  C7 45 A0 D8 A6 C6 82            mov dword ptr [rbp - 0x60], 0x82c6a6d8
00BF0CC5  44 8B 4D A0                     mov r9d, dword ptr [rbp - 0x60]
00BF0CC9  41 C1 C1 07                     rol r9d, 7
00BF0CCD  EB 12                           jmp 0x140bf0ce1
00BF0CCF  C7 45 A4 72 46 57 4E            mov dword ptr [rbp - 0x5c], 0x4e574672
00BF0CD6  44 8B 4D A4                     mov r9d, dword ptr [rbp - 0x5c]
00BF0CDA  44 33 CA                        xor r9d, edx
00BF0CDD  41 C1 C9 18                     ror r9d, 0x18
00BF0CE1  48 8B 86 00 01 00 00            mov rax, qword ptr [rsi + 0x100]
00BF0CE8  BA 50 00 00 00                  mov edx, 0x50
00BF0CED  45 8B C1                        mov r8d, r9d
00BF0CF0  8D 4A F0                        lea ecx, [rdx - 0x10]
00BF0CF3  E8 68 9D FF FF                  call 0x140beaa60
00BF0CF8  33 D2                           xor edx, edx
00BF0CFA  48 8D 5D F8                     lea rbx, [rbp - 8]
00BF0CFE  48 85 C0                        test rax, rax
00BF0D01  41 8B CF                        mov ecx, r15d
00BF0D04  48 0F 45 D8                     cmovne rbx, rax
00BF0D08  C1 E1 0C                        shl ecx, 0xc
00BF0D0B  48 03 8D 28 01 00 00            add rcx, qword ptr [rbp + 0x128]
00BF0D12  48 8D 45 D0                     lea rax, [rbp - 0x30]
00BF0D16  48 89 03                        mov qword ptr [rbx], rax
00BF0D19  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00BF0D1E  48 89 43 08                     mov qword ptr [rbx + 8], rax
00BF0D22  41 8B C7                        mov eax, r15d
00BF0D25  48 89 4B 10                     mov qword ptr [rbx + 0x10], rcx
00BF0D29  44 89 63 20                     mov dword ptr [rbx + 0x20], r12d
00BF0D2D  89 7B 28                        mov dword ptr [rbx + 0x28], edi
00BF0D30  48 8D 0C 80                     lea rcx, [rax + rax*4]
00BF0D34  48 89 5B 48                     mov qword ptr [rbx + 0x48], rbx
00BF0D38  48 8D 04 8D 00 00 00 00         lea rax, [rcx*4]
00BF0D40  48 89 53 30                     mov qword ptr [rbx + 0x30], rdx
00BF0D44  49 03 C5                        add rax, r13
00BF0D47  48 89 43 18                     mov qword ptr [rbx + 0x18], rax
00BF0D4B  48 8D 05 3E 05 00 00            lea rax, [rip + 0x53e]
00BF0D52  48 89 43 40                     mov qword ptr [rbx + 0x40], rax
00BF0D56  8B C7                           mov eax, edi
00BF0D58  F0 0F C1 45 F0                  lock xadd dword ptr [rbp - 0x10], eax
00BF0D5D  03 C7                           add eax, edi
00BF0D5F  3B C7                           cmp eax, edi
00BF0D61  75 11                           jne 0x140bf0d74
00BF0D63  39 55 F4                        cmp dword ptr [rbp - 0xc], edx
00BF0D66  74 0C                           je 0x140bf0d74
00BF0D68  45 33 C0                        xor r8d, r8d
00BF0D6B  48 8D 4D D8                     lea rcx, [rbp - 0x28]
00BF0D6F  E8 20 9A 6D FF                  call 0x1402ca794
00BF0D74  33 D2                           xor edx, edx
00BF0D76  89 7D F4                        mov dword ptr [rbp - 0xc], edi
00BF0D79  48 8D 4B 30                     lea rcx, [rbx + 0x30]
00BF0D7D  E8 9E 87 70 FF                  call 0x1402f9520
00BF0D82  48 8D 45 F8                     lea rax, [rbp - 8]
00BF0D86  45 33 D2                        xor r10d, r10d
00BF0D89  48 3B D8                        cmp rbx, rax
00BF0D8C  75 2B                           jne 0x140bf0db9
00BF0D8E  44 39 55 F4                     cmp dword ptr [rbp - 0xc], r10d
00BF0D92  74 25                           je 0x140bf0db9
00BF0D94  33 F6                           xor esi, esi
00BF0D96  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
00BF0D99  48 8D 4D D8                     lea rcx, [rbp - 0x28]
00BF0D9D  45 33 C0                        xor r8d, r8d
00BF0DA0  33 D2                           xor edx, edx
00BF0DA2  E8 ED 99 6D FF                  call 0x1402ca794
00BF0DA7  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
00BF0DAA  85 C0                           test eax, eax
00BF0DAC  75 E8                           jne 0x140bf0d96
00BF0DAE  89 75 F4                        mov dword ptr [rbp - 0xc], esi
00BF0DB1  45 33 D2                        xor r10d, r10d
00BF0DB4  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
00BF0DB9  4C 39 54 24 48                  cmp qword ptr [rsp + 0x48], r10
00BF0DBE  75 2B                           jne 0x140bf0deb
00BF0DC0  44 39 55 F4                     cmp dword ptr [rbp - 0xc], r10d
00BF0DC4  74 25                           je 0x140bf0deb
00BF0DC6  33 F6                           xor esi, esi
00BF0DC8  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
00BF0DCB  48 8D 4D D8                     lea rcx, [rbp - 0x28]
00BF0DCF  45 33 C0                        xor r8d, r8d
00BF0DD2  33 D2                           xor edx, edx
00BF0DD4  E8 BB 99 6D FF                  call 0x1402ca794
00BF0DD9  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
00BF0DDC  85 C0                           test eax, eax
00BF0DDE  75 E8                           jne 0x140bf0dc8
00BF0DE0  89 75 F4                        mov dword ptr [rbp - 0xc], esi
00BF0DE3  45 33 D2                        xor r10d, r10d
00BF0DE6  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
00BF0DEB  8B 85 38 01 00 00               mov eax, dword ptr [rbp + 0x138]
00BF0DF1  48 BB 01 20 00 04 80 00 10 70   movabs rbx, 0x7010008004002001
00BF0DFB  44 03 F8                        add r15d, eax
00BF0DFE  45 3B FE                        cmp r15d, r14d
00BF0E01  0F 82 C8 FC FF FF               jb 0x140bf0acf
00BF0E07  41 BF 08 00 00 00               mov r15d, 8
00BF0E0D  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
00BF0E12  41 8B C6                        mov eax, r14d
00BF0E15  48 8D 0C 80                     lea rcx, [rax + rax*4]
00BF0E19  EB 0D                           jmp 0x140bf0e28
00BF0E1B  44 38 50 0F                     cmp byte ptr [rax + 0xf], r10b
00BF0E1F  7D 17                           jge 0x140bf0e38
00BF0E21  44 03 F7                        add r14d, edi
00BF0E24  4B 8D 0C B6                     lea rcx, [r14 + r14*4]
00BF0E28  48 8D 04 8D 00 00 00 00         lea rax, [rcx*4]
00BF0E30  49 03 C5                        add rax, r13
00BF0E33  49 3B C0                        cmp rax, r8
00BF0E36  75 E3                           jne 0x140bf0e1b
00BF0E38  48 8B 95 28 01 00 00            mov rdx, qword ptr [rbp + 0x128]
00BF0E3F  41 8B C6                        mov eax, r14d
00BF0E42  C1 E0 0C                        shl eax, 0xc
00BF0E45  48 03 D0                        add rdx, rax
00BF0E48  41 8B C6                        mov eax, r14d
00BF0E4B  48 89 95 28 01 00 00            mov qword ptr [rbp + 0x128], rdx
00BF0E52  48 8D 0C 80                     lea rcx, [rax + rax*4]
00BF0E56  4D 8D 6C 8D 00                  lea r13, [r13 + rcx*4]
00BF0E5B  4C 89 6C 24 68                  mov qword ptr [rsp + 0x68], r13
00BF0E60  4D 3B E8                        cmp r13, r8
00BF0E63  0F 85 EB F9 FF FF               jne 0x140bf0854
00BF0E69  44 39 95 38 01 00 00            cmp dword ptr [rbp + 0x138], r10d
00BF0E70  74 25                           je 0x140bf0e97
00BF0E72  44 39 55 F4                     cmp dword ptr [rbp - 0xc], r10d
00BF0E76  74 1F                           je 0x140bf0e97
00BF0E78  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
00BF0E7B  48 8D 4D D8                     lea rcx, [rbp - 0x28]
00BF0E7F  45 33 C0                        xor r8d, r8d
00BF0E82  33 D2                           xor edx, edx
00BF0E84  E8 0B 99 6D FF                  call 0x1402ca794
00BF0E89  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
00BF0E8C  45 33 D2                        xor r10d, r10d
00BF0E8F  85 C0                           test eax, eax
00BF0E91  75 E5                           jne 0x140bf0e78
00BF0E93  44 89 55 F4                     mov dword ptr [rbp - 0xc], r10d
00BF0E97  40 84 BD 30 01 00 00            test byte ptr [rbp + 0x130], dil
00BF0E9E  0F 84 6F 02 00 00               je 0x140bf1113
00BF0EA4  44 8B 74 24 50                  mov r14d, dword ptr [rsp + 0x50]
00BF0EA9  45 85 F6                        test r14d, r14d
00BF0EAC  0F 84 61 02 00 00               je 0x140bf1113
00BF0EB2  44 8B AE 04 08 00 00            mov r13d, dword ptr [rsi + 0x804]
00BF0EB9  44 8B 86 44 09 00 00            mov r8d, dword ptr [rsi + 0x944]
00BF0EC0  41 8D 45 30                     lea eax, [r13 + 0x30]
00BF0EC4  3B 86 64 0A 00 00               cmp eax, dword ptr [rsi + 0xa64]
00BF0ECA  0F 86 D3 00 00 00               jbe 0x140bf0fa3
00BF0ED0  8B D0                           mov edx, eax
00BF0ED2  48 8B CE                        mov rcx, rsi
00BF0ED5  E8 1E 6C FF FF                  call 0x140be7af8
00BF0EDA  45 33 D2                        xor r10d, r10d
00BF0EDD  48 8B D8                        mov rbx, rax
00BF0EE0  48 85 C0                        test rax, rax
00BF0EE3  75 0A                           jne 0x140bf0eef
00BF0EE5  B8 9A 00 00 C0                  mov eax, 0xc000009a
00BF0EEA  E9 55 03 00 00                  jmp 0x140bf1244
00BF0EEF  8B 8E D8 09 00 00               mov ecx, dword ptr [rsi + 0x9d8]
00BF0EF5  F6 C1 02                        test cl, 2
00BF0EF8  0F 85 9C 00 00 00               jne 0x140bf0f9a
00BF0EFE  8B 86 04 08 00 00               mov eax, dword ptr [rsi + 0x804]
00BF0F04  81 E1 00 00 00 10               and ecx, 0x10000000
00BF0F0A  4C 8B 86 E8 07 00 00            mov r8, qword ptr [rsi + 0x7e8]
00BF0F11  F7 D9                           neg ecx
00BF0F13  1B C9                           sbb ecx, ecx
00BF0F15  23 8E 44 09 00 00               and ecx, dword ptr [rsi + 0x944]
00BF0F1B  41 3B C7                        cmp eax, r15d
00BF0F1E  72 14                           jb 0x140bf0f34
00BF0F20  8B D0                           mov edx, eax
00BF0F22  48 C1 EA 03                     shr rdx, 3
00BF0F26  4C 89 16                        mov qword ptr [rsi], r10
00BF0F29  83 C0 F8                        add eax, -8
00BF0F2C  49 03 F7                        add rsi, r15
00BF0F2F  48 2B D7                        sub rdx, rdi
00BF0F32  75 F2                           jne 0x140bf0f26
00BF0F34  85 C0                           test eax, eax
00BF0F36  74 0B                           je 0x140bf0f43
00BF0F38  44 88 16                        mov byte ptr [rsi], r10b
00BF0F3B  48 03 F7                        add rsi, rdi
00BF0F3E  83 C0 FF                        add eax, -1
00BF0F41  75 F5                           jne 0x140bf0f38
00BF0F43  8B B3 44 09 00 00               mov esi, dword ptr [rbx + 0x944]
00BF0F49  89 8B 44 09 00 00               mov dword ptr [rbx + 0x944], ecx
00BF0F4F  83 F9 03                        cmp ecx, 3
00BF0F52  74 2E                           je 0x140bf0f82
00BF0F54  F7 83 D8 09 00 00 00 00 00 08   test dword ptr [rbx + 0x9d8], 0x8000000
00BF0F5E  75 19                           jne 0x140bf0f79
00BF0F60  85 C9                           test ecx, ecx
00BF0F62  74 15                           je 0x140bf0f79
00BF0F64  48 8B 83 38 02 00 00            mov rax, qword ptr [rbx + 0x238]
00BF0F6B  49 8D 48 F8                     lea rcx, [r8 - 8]
00BF0F6F  48 8B 11                        mov rdx, qword ptr [rcx]
00BF0F72  E8 E9 9A FF FF                  call 0x140beaa60
00BF0F77  EB 18                           jmp 0x140bf0f91
00BF0F79  48 8B 83 08 01 00 00            mov rax, qword ptr [rbx + 0x108]
00BF0F80  EB 07                           jmp 0x140bf0f89
00BF0F82  48 8B 83 68 03 00 00            mov rax, qword ptr [rbx + 0x368]
00BF0F89  49 8B C8                        mov rcx, r8
00BF0F8C  E8 CF 9A FF FF                  call 0x140beaa60
00BF0F91  89 B3 44 09 00 00               mov dword ptr [rbx + 0x944], esi
00BF0F97  45 33 D2                        xor r10d, r10d
00BF0F9A  83 A3 D8 09 00 00 FD            and dword ptr [rbx + 0x9d8], 0xfffffffd
00BF0FA1  EB 09                           jmp 0x140bf0fac
00BF0FA3  48 8B DE                        mov rbx, rsi
00BF0FA6  89 86 04 08 00 00               mov dword ptr [rsi + 0x804], eax
00BF0FAC  01 BB 2C 08 00 00               add dword ptr [rbx + 0x82c], edi
00BF0FB2  4A 8D 34 2B                     lea rsi, [rbx + r13]
00BF0FB6  B9 30 00 00 00                  mov ecx, 0x30
00BF0FBB  48 8B C6                        mov rax, rsi
00BF0FBE  8D 51 D6                        lea edx, [rcx - 0x2a]
00BF0FC1  4C 89 10                        mov qword ptr [rax], r10
00BF0FC4  83 C1 F8                        add ecx, -8
00BF0FC7  49 03 C7                        add rax, r15
00BF0FCA  48 2B D7                        sub rdx, rdi
00BF0FCD  75 F2                           jne 0x140bf0fc1
00BF0FCF  85 C9                           test ecx, ecx
00BF0FD1  74 0B                           je 0x140bf0fde
00BF0FD3  44 88 10                        mov byte ptr [rax], r10b
00BF0FD6  48 03 C7                        add rax, rdi
00BF0FD9  83 C1 FF                        add ecx, -1
00BF0FDC  75 F5                           jne 0x140bf0fd3
00BF0FDE  4C 8B 4C 24 78                  mov r9, qword ptr [rsp + 0x78]
00BF0FE3  C7 06 0D 00 00 00               mov dword ptr [rsi], 0xd
00BF0FE9  4C 89 4E 08                     mov qword ptr [rsi + 8], r9
00BF0FED  44 89 76 10                     mov dword ptr [rsi + 0x10], r14d
00BF0FF1  44 01 B3 48 08 00 00            add dword ptr [rbx + 0x848], r14d
00BF0FF8  4B 8D 0C 31                     lea rcx, [r9 + r14]
00BF0FFC  44 8B 93 34 08 00 00            mov r10d, dword ptr [rbx + 0x834]
00BF1003  4C 8B A3 38 08 00 00            mov r12, qword ptr [rbx + 0x838]
00BF100A  4C 3B C9                        cmp r9, rcx
00BF100D  73 0F                           jae 0x140bf101e
00BF100F  49 8B C1                        mov rax, r9
00BF1012  0F 18 00                        prefetchnta byte ptr [rax]
00BF1015  48 83 C0 40                     add rax, 0x40
00BF1019  48 3B C1                        cmp rax, rcx
00BF101C  72 F4                           jb 0x140bf1012
00BF101E  45 8B DE                        mov r11d, r14d
00BF1021  4D 8B C4                        mov r8, r12
00BF1024  41 C1 EB 07                     shr r11d, 7
00BF1028  45 85 DB                        test r11d, r11d
00BF102B  74 55                           je 0x140bf1082
00BF102D  49 BD 01 20 00 04 80 00 10 70   movabs r13, 0x7010008004002001
00BF1037  49 8B C7                        mov rax, r15
00BF103A  4D 33 01                        xor r8, qword ptr [r9]
00BF103D  41 8B CA                        mov ecx, r10d
00BF1040  4D 03 CF                        add r9, r15
00BF1043  49 D3 C0                        rol r8, cl
00BF1046  4D 33 01                        xor r8, qword ptr [r9]
00BF1049  4D 03 CF                        add r9, r15
00BF104C  49 D3 C0                        rol r8, cl
00BF104F  48 2B C7                        sub rax, rdi
00BF1052  75 E6                           jne 0x140bf103a
00BF1054  49 8B C9                        mov rcx, r9
00BF1057  48 2B 4C 24 78                  sub rcx, qword ptr [rsp + 0x78]
00BF105C  49 33 CC                        xor rcx, r12
00BF105F  48 8B C1                        mov rax, rcx
00BF1062  48 C1 C0 11                     rol rax, 0x11
00BF1066  48 33 C8                        xor rcx, rax
00BF1069  49 8B C5                        mov rax, r13
00BF106C  48 F7 E1                        mul rcx
00BF106F  33 D0                           xor edx, eax
00BF1071  44 33 D2                        xor r10d, edx
00BF1074  41 83 E2 3F                     and r10d, 0x3f
00BF1078  44 0F 44 D7                     cmove r10d, edi
00BF107C  41 83 C3 FF                     add r11d, -1
00BF1080  75 B5                           jne 0x140bf1037
00BF1082  41 8B D6                        mov edx, r14d
00BF1085  83 E2 7F                        and edx, 0x7f
00BF1088  41 3B D7                        cmp edx, r15d
00BF108B  72 1A                           jb 0x140bf10a7
00BF108D  8B C2                           mov eax, edx
00BF108F  48 C1 E8 03                     shr rax, 3
00BF1093  4D 33 01                        xor r8, qword ptr [r9]
00BF1096  41 8B CA                        mov ecx, r10d
00BF1099  49 D3 C0                        rol r8, cl
00BF109C  4D 03 CF                        add r9, r15
00BF109F  83 C2 F8                        add edx, -8
00BF10A2  48 2B C7                        sub rax, rdi
00BF10A5  75 EC                           jne 0x140bf1093
00BF10A7  85 D2                           test edx, edx
00BF10A9  74 15                           je 0x140bf10c0
00BF10AB  41 0F B6 01                     movzx eax, byte ptr [r9]
00BF10AF  41 8B CA                        mov ecx, r10d
00BF10B2  4C 33 C0                        xor r8, rax
00BF10B5  4C 03 CF                        add r9, rdi
00BF10B8  49 D3 C0                        rol r8, cl
00BF10BB  83 C2 FF                        add edx, -1
00BF10BE  75 EB                           jne 0x140bf10ab
00BF10C0  49 8B C0                        mov rax, r8
00BF10C3  EB 03                           jmp 0x140bf10c8
00BF10C5  44 33 C0                        xor r8d, eax
00BF10C8  48 C1 E8 1F                     shr rax, 0x1f
00BF10CC  48 85 C0                        test rax, rax
00BF10CF  75 F4                           jne 0x140bf10c5
00BF10D1  41 0F BA F0 1F                  btr r8d, 0x1f
00BF10D6  44 89 46 14                     mov dword ptr [rsi + 0x14], r8d
00BF10DA  44 01 B3 48 08 00 00            add dword ptr [rbx + 0x848], r14d
00BF10E1  F7 83 D8 09 00 00 00 00 00 20   test dword ptr [rbx + 0x9d8], 0x20000000
00BF10EB  74 19                           je 0x140bf1106
00BF10ED  45 85 F6                        test r14d, r14d
00BF10F0  74 14                           je 0x140bf1106
00BF10F2  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
00BF10F7  4C 8D 4E 1C                     lea r9, [rsi + 0x1c]
00BF10FB  45 8B C6                        mov r8d, r14d
00BF10FE  48 8B CB                        mov rcx, rbx
00BF1101  E8 46 9E 92 FF                  call 0x14051af4c
00BF1106  48 8B 85 20 01 00 00            mov rax, qword ptr [rbp + 0x120]
00BF110D  89 7E 18                        mov dword ptr [rsi + 0x18], edi
00BF1110  48 89 18                        mov qword ptr [rax], rbx
00BF1113  33 C0                           xor eax, eax
00BF1115  E9 2A 01 00 00                  jmp 0x140bf1244
00BF111A  8B 8B D8 09 00 00               mov ecx, dword ptr [rbx + 0x9d8]
00BF1120  0F BA E1 14                     bt ecx, 0x14
00BF1124  0F 83 2F 01 00 00               jae 0x140bf1259
00BF112A  44 39 BB 18 09 00 00            cmp dword ptr [rbx + 0x918], r15d
00BF1131  0F 85 08 01 00 00               jne 0x140bf123f
00BF1137  48 B8 E8 B4 C8 91 58 3F A0 A3   movabs rax, 0xa3a03f5891c8b4e8
00BF1141  4C 89 BB 28 09 00 00            mov qword ptr [rbx + 0x928], r15
00BF1148  48 03 C3                        add rax, rbx
00BF114B  48 C7 83 30 09 00 00 0F 01 00 00  mov qword ptr [rbx + 0x930], 0x10f
00BF1156  48 89 83 20 09 00 00            mov qword ptr [rbx + 0x920], rax
00BF115D  BF 01 00 00 00                  mov edi, 1
00BF1162  4C 89 B3 38 09 00 00            mov qword ptr [rbx + 0x938], r14
00BF1169  89 BB 18 09 00 00               mov dword ptr [rbx + 0x918], edi
00BF116F  0F BA E1 1D                     bt ecx, 0x1d
00BF1173  0F 82 C6 00 00 00               jb 0x140bf123f
00BF1179  F7 83 DC 09 00 00 00 00 20 00   test dword ptr [rbx + 0x9dc], 0x200000
00BF1183  0F 84 B6 00 00 00               je 0x140bf123f
00BF1189  40 84 CF                        test dil, cl
00BF118C  0F 84 AD 00 00 00               je 0x140bf123f
00BF1192  8B 8B 74 0A 00 00               mov ecx, dword ptr [rbx + 0xa74]
00BF1198  8B 83 04 08 00 00               mov eax, dword ptr [rbx + 0x804]
00BF119E  4C 8B 93 38 08 00 00            mov r10, qword ptr [rbx + 0x838]
00BF11A5  2B C1                           sub eax, ecx
00BF11A7  4C 8B 83 78 0A 00 00            mov r8, qword ptr [rbx + 0xa78]
00BF11AE  48 8D 14 19                     lea rdx, [rcx + rbx]
00BF11B2  8B C8                           mov ecx, eax
00BF11B4  48 C1 E9 03                     shr rcx, 3
00BF11B8  4C 8D 0C CA                     lea r9, [rdx + rcx*8]
00BF11BC  49 3B D1                        cmp rdx, r9
00BF11BF  74 2C                           je 0x140bf11ed
00BF11C1  44 8D 7F 07                     lea r15d, [rdi + 7]
00BF11C5  4C 31 02                        xor qword ptr [rdx], r8
00BF11C8  48 8B 02                        mov rax, qword ptr [rdx]
00BF11CB  49 03 D7                        add rdx, r15
00BF11CE  41 0F B6 C8                     movzx ecx, r8b
00BF11D2  49 33 C2                        xor rax, r10
00BF11D5  83 E1 3F                        and ecx, 0x3f
00BF11D8  49 D3 C8                        ror r8, cl
00BF11DB  4C 03 C0                        add r8, rax
00BF11DE  49 81 F0 FA 0E 00 00            xor r8, 0xefa
00BF11E5  49 3B D1                        cmp rdx, r9
00BF11E8  75 DB                           jne 0x140bf11c5
00BF11EA  45 33 FF                        xor r15d, r15d
00BF11ED  0F BA B3 DC 09 00 00 15         btr dword ptr [rbx + 0x9dc], 0x15
00BF11F5  4C 3B 83 80 0A 00 00            cmp r8, qword ptr [rbx + 0xa80]
00BF11FC  74 41                           je 0x140bf123f
00BF11FE  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
00BF1205  8B 93 04 08 00 00               mov edx, dword ptr [rbx + 0x804]
00BF120B  48 89 18                        mov qword ptr [rax], rbx
00BF120E  89 50 10                        mov dword ptr [rax + 0x10], edx
00BF1211  48 8B 8B 80 0A 00 00            mov rcx, qword ptr [rbx + 0xa80]
00BF1218  44 39 BB 18 09 00 00            cmp dword ptr [rbx + 0x918], r15d
00BF121F  75 0E                           jne 0x140bf122f
00BF1221  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
00BF1228  49 33 C8                        xor rcx, r8
00BF122B  48 89 48 18                     mov qword ptr [rax + 0x18], rcx
00BF122F  33 D2                           xor edx, edx
00BF1231  41 B9 00 01 00 00               mov r9d, 0x100
00BF1237  48 8B CB                        mov rcx, rbx
00BF123A  E8 45 71 FF FF                  call 0x140be8384
00BF123F  B8 7B 00 00 C0                  mov eax, 0xc000007b
00BF1244  48 81 C4 D8 01 00 00            add rsp, 0x1d8
00BF124B  41 5F                           pop r15
00BF124D  41 5E                           pop r14
00BF124F  41 5D                           pop r13
00BF1251  41 5C                           pop r12
00BF1253  5F                              pop rdi
00BF1254  5E                              pop rsi
00BF1255  5B                              pop rbx
00BF1256  5D                              pop rbp
00BF1257  C3                              ret
00BF1258  CC                              int3
00BF1259  41 B9 04 00 00 00               mov r9d, 4
00BF125F  C7 85 20 01 00 00 09 00 00 E8   mov dword ptr [rbp + 0x120], 0xe8000009
00BF1269  8B 8D 20 01 00 00               mov ecx, dword ptr [rbp + 0x120]
00BF126F  4D 8B C6                        mov r8, r14
00BF1272  C1 C1 65                        rol ecx, 0x65
00BF1275  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00BF127A  41 8D 51 06                     lea edx, [r9 + 6]
00BF127E  E8 DD C3 90 FF                  call 0x1404fd660
00BF1283  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00BEFF8C(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned int v_stack_m1C0;
    unsigned int v_stack_m1C4;
    unsigned __int64 v_stack_m1C8;
    unsigned __int64 v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned int v_stack_m1E8;
    unsigned __int64 v_stack_p20;

    *(unsigned int *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (472);
    result = KeGuardDispatchICall(a2, a2, a3, a4);
    v_r15 = 0;
    if (result == 0) goto loc_00BF123F;
    *(unsigned __int16 *)(v_rsp - 280 + 312) = (unsigned __int16)(*(unsigned __int16 *)(result + 6));
    if ((unsigned __int16)(*(unsigned __int16 *)(result + 6)) == 0) goto loc_00BF111A;
    if ((*(unsigned int *)(result + 56)) < 0x1000ULL) goto loc_00BF111A;
    if (((a2) & (0xFFFULL)) != 0) goto loc_00BF111A;
    v_stack_m1C4 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 84)));
    result = KeGuardDispatchICall(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 1336), a2, a3, a4);
loc_00BF0050:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 1568)) + 16 + 8)) == a2) goto loc_00BF0060;
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 1568)) + 16) + (v_r15 + 24);
    if (a2 < (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 1568)) + 16 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 1568)))) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 1568)))) * 2 * 8)) goto loc_00BF0050;
    goto loc_00BF0074;
loc_00BF0060:
    *(unsigned __int64 *)(v_rsp - 280 - 80) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 280 - 64) = v_xmm1;
loc_00BF0074:
    result = KeGuardDispatchICall(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 1336), a2, a3, a4);
    v_r10 = (unsigned int)((v_r10) | (0xFFFFFFFFULL));
    a4 = 0;
    if (!sign_flag) goto loc_00BF00E1;
loc_00BF00B3:
    *(unsigned __int64 *)(v_rsp - 280 - 80) = 0;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r15 + 24))) + ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
    result = (v_rsp - 280 - 80) + (1 + 7);
    a2 = (1 + 2) - (1);
    if (condition_is_not_equal) goto loc_00BF00B3;
    if ((unsigned int)(a1) == 0) goto loc_00BF00D0;
loc_00BF00C5:
    *(unsigned __int8 *)(result) = 0;
    result = (result) + (1);
    a1 = (unsigned int)((a1) + ((unsigned int)(v_r10)));
    if (condition_is_not_equal) goto loc_00BF00C5;
loc_00BF00D0:
    *(unsigned int *)(v_rsp - 280 - 64) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 80)));
    *(unsigned __int64 *)(v_rsp - 280 - 72) = a2;
    *(unsigned __int64 *)(v_rsp - 280 - 80) = 1;
    goto loc_00BF00E4;
loc_00BF00E1:
loc_00BF00E4:
    a1 = (unsigned int)((a2) & (0xFFFULL));
    a1 = (a1) + (0xFFFULL);
    result = ((unsigned int)(*(unsigned int *)(v_rsp - 280 - 64))) + (a1);
    result = (result) >> (12);
    v_stack_m1B0 = result;
    v_stack_m1E8 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 2052)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 2052))) + (48));
    v_r14 = (unsigned int)((result + result * 4) << (2));
    result = (unsigned int)((result) + ((unsigned int)(v_r14)));
    if (((unsigned int)(result)) <= (*(unsigned int *)(*(unsigned __int64 *)(a1) + 2660))) goto loc_00BF0207;
    result = sub_00BE7AF8(*(unsigned __int64 *)(a1), (unsigned int)((unsigned int)(result)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 2372)), a4);
    a4 = 0;
    v_stack_m1A8 = result;
    if (result == 0) goto loc_00BF0EE5;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 2520)))) & (2)) != 0) goto loc_00BF01F4;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 2520))) & (0x10000000ULL));
    a1 = (unsigned int)(-(a1));
    a1 = (unsigned int)((a1) & (*(unsigned int *)(*(unsigned __int64 *)(a1) + 2372)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 2052)))) < ((unsigned int)(1 + 7))) goto loc_00BF018E;
    a2 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 2052))))) >> (3);
loc_00BF0180:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1)) = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 2052))) + (-8));
    v_rbx = (*(unsigned __int64 *)(a1)) + (1 + 7);
    a2 = (a2) - (1);
    if (condition_is_not_equal) goto loc_00BF0180;
loc_00BF018E:
    if ((unsigned int)(result) == 0) goto loc_00BF019D;
loc_00BF0192:
    *(unsigned __int8 *)(v_rbx) = 0;
    v_rbx = (v_rbx) + (1);
    result = (unsigned int)((result) + (-1));
    if (condition_is_not_equal) goto loc_00BF0192;
loc_00BF019D:
    *(unsigned int *)(result + 2372) = (unsigned int)(a1);
    if (((unsigned int)(a1)) == 3) goto loc_00BF01DC;
    if (((*(unsigned int *)(result + 2520)) & (0x8000000ULL)) != 0) goto loc_00BF01D3;
    if ((unsigned int)(a1) == 0) goto loc_00BF01D3;
    result = KeGuardDispatchICall(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 2024) - 8, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 2024) - 8), *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 2024), a4);
    goto loc_00BF01EB;
loc_00BF01D3:
    goto loc_00BF01E3;
loc_00BF01DC:
loc_00BF01E3:
    result = KeGuardDispatchICall(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 2024), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 2024) - 8), *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 2024), a4);
loc_00BF01EB:
    *(unsigned int *)(result + 2372) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 2372)));
    a4 = 0;
loc_00BF01F4:
    v_r10 = (unsigned int)((v_r10) | (0xFFFFFFFFULL));
    goto loc_00BF0215;
loc_00BF0207:
    v_stack_m1A8 = (unsigned int)(*(unsigned int *)(result + 2372));
    *(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2052) = (unsigned int)(result);
loc_00BF0215:
    v_rbx = ((unsigned int)(v_stack_m1E8)) + ((unsigned int)(*(unsigned int *)(result + 2372)));
    v_stack_m1D0 = v_rbx;
loc_00BF0232:
    *(unsigned __int64 *)(v_rbx) = 0;
    a1 = (unsigned int)((48) + ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
    result = (v_rbx) + (1 + 7);
    a2 = (48 - 42) - (1);
    if (condition_is_not_equal) goto loc_00BF0232;
    if ((unsigned int)(a1) == 0) goto loc_00BF024F;
loc_00BF0244:
    *(unsigned __int8 *)(result) = 0;
    result = (result) + (1);
    a1 = (unsigned int)((a1) + ((unsigned int)(v_r10)));
    if (condition_is_not_equal) goto loc_00BF0244;
loc_00BF024F:
    *(unsigned int *)(v_rbx) = 33;
    *(unsigned __int64 *)(v_rbx + 8) = 0;
    *(unsigned int *)(v_rbx + 16) = 0;
    goto loc_00BF026B;
loc_00BF0269:
    a1 = (unsigned int)((*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2104)) ^ ((unsigned int)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2104))));
loc_00BF026B:
    result = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2104)) >> (31);
    if (result != 0) goto loc_00BF0269;
    *(unsigned int *)(v_rbx + 20) = (unsigned int)(a1);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 280 + 288)) = (unsigned int)(*(unsigned int *)(result + 2372));
loc_00BF0293:
    v_r12 = (unsigned int)((v_r15 + 24) + ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
    *(unsigned __int64 *)(v_rbx + 24) = *(unsigned __int64 *)(v_rsp - 280 - 80);
    a1 = (v_rsp - 280 - 80) + (1 + 7);
    a2 = (v_rbx + 24) + (1 + 7);
    a3 = (3) - (1);
    if (condition_is_not_equal) goto loc_00BF0293;
    if ((unsigned int)(v_r12) == 0) goto loc_00BF02BB;
loc_00BF02AC:
    a1 = (a1) + (1);
    *(unsigned __int8 *)(a2) = (unsigned __int8)(*(unsigned __int8 *)(a1));
    a2 = (a2) + (1);
    v_r12 = (unsigned int)((v_r12) + ((unsigned int)(v_r10)));
    if (condition_is_not_equal) goto loc_00BF02AC;
loc_00BF02BB:
    result = KeGuardDispatchICall(*(unsigned __int64 *)(v_rsp - 280 + 296), 1, 12, v_stack_m1C8);
    a3 = 0;
    v_stack_m1A0 = result;
    if (result == 0) {
        v_stack_m1C8 = 0;
    }
    if (((*(unsigned __int8 *)(v_rsp - 280 + 304)) & (1)) == 0) {
        v_stack_m1A0 = 0;
        v_stack_m1C8 = 0;
    }
    v_stack_m1E0 = v_rbx + 48;
    v_stack_m1B8 = v_rbx + 48 + (unsigned int)(v_stack_m1B0) + (unsigned int)(v_stack_m1B0) * 4 * 4;
    if (((unsigned int)(v_r14)) < ((unsigned int)(1 + 7))) goto loc_00BF033D;
    a1 = ((unsigned int)((unsigned int)(v_r14))) >> (3);
loc_00BF032A:
    *(unsigned __int64 *)(v_rbx + 48) = -1;
    v_r14 = (unsigned int)((v_r14) + (-8));
    result = (v_rbx + 48) + (1 + 7);
    a1 = (a1) - (1);
    if (condition_is_not_equal) goto loc_00BF032A;
loc_00BF033D:
    if ((unsigned int)(v_r14) == 0) goto loc_00BF034E;
loc_00BF0342:
    *(unsigned __int8 *)(result) = 255;
    result = (result) + (1);
    v_r14 = (unsigned int)((v_r14) + (-1));
    if (condition_is_not_equal) goto loc_00BF0342;
loc_00BF034E:
    v_rbx = (*(unsigned __int16 *)(result + 20)) + (24);
    v_rbx = (v_rbx) + (result);
    v_stack_m1B0 = v_rbx + *(unsigned __int16 *)(v_rsp - 280 + 312) + *(unsigned __int16 *)(v_rsp - 280 + 312) * 4 * 8;
    if (((*(unsigned int *)(v_rbx + 36)) & (0x2000000ULL)) != 0) goto loc_00BF03C5;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx)))) != 0x54494E49ULL) goto loc_00BF03A8;
    if ((*(unsigned int *)(v_rbx + 4)) == 0x4742444BULL) goto loc_00BF03C5;
loc_00BF03A8:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx)))) != 0x45474150ULL) goto loc_00BF03D8;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rbx + 4))) == ((unsigned __int16)((unsigned int)(0x7877ULL)))) goto loc_00BF03C5;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rbx + 4))) == ((unsigned __int16)((unsigned int)(0x7277ULL)))) goto loc_00BF03C5;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rbx + 4))) != ((unsigned __int16)((unsigned int)(0x7777ULL)))) goto loc_00BF03E6;
loc_00BF03C5:
loc_00BF03C7:
    if ((*(unsigned int *)(v_rbx + 36)) >= 0) goto loc_00BF04B3;
    goto loc_00BF04B7;
loc_00BF03D8:
    if (((unsigned int)(*(unsigned __int16 *)(v_rbx + 4))) != 0x41525245ULL) goto loc_00BF03E6;
    if ((*(unsigned __int16 *)(v_rbx + 4)) == ((unsigned __int16)((unsigned int)(0x4154ULL)))) goto loc_00BF03C5;
loc_00BF03E6:
    a4 = (v_rbx) - (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2384));
    v_r13 = (unsigned int)((result) | (0xFFFFFFFFULL));
loc_00BF0412:
    a3 = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2384)) + (1);
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2384) + a4 * 1))) != ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2384))))) goto loc_00BF0427;
    v_r12 = (unsigned int)((7) + ((unsigned int)(v_r13)));
    if (condition_is_not_equal) goto loc_00BF0412;
    goto loc_00BF04A3;
loc_00BF0427:
loc_00BF042D:
    a4 = (v_rbx) + (1 + 7);
    v_r10 = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2392)) + (1 + 7);
    if ((*(unsigned __int64 *)(v_rbx)) != (*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2392)))) goto loc_00BF0463;
    a3 = (unsigned int)(((unsigned int)((unsigned int)(1 + 7))) + (-8));
    if (a3 >= ((unsigned int)(1 + 7))) goto loc_00BF042D;
    if (a3 == 0) goto loc_00BF04A3;
loc_00BF044C:
    a4 = (a4) + (1);
    v_r10 = (v_r10) + (1);
    if (((unsigned __int8)(*(unsigned __int8 *)(a4))) != ((unsigned __int8)(*(unsigned __int8 *)(v_r10)))) goto loc_00BF0463;
    a3 = (unsigned int)((a3) + ((unsigned int)(v_r13)));
    if (condition_is_not_equal) goto loc_00BF044C;
    goto loc_00BF04A3;
loc_00BF0463:
    a3 = (v_rbx) - (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2400));
loc_00BF046F:
    v_r11 = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2400)) + (1);
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2400) + a3 * 1))) != ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2400))))) goto loc_00BF0484;
    a4 = (unsigned int)((4) + ((unsigned int)(v_r13)));
    if (condition_is_not_equal) goto loc_00BF046F;
    goto loc_00BF04A3;
loc_00BF0484:
    a3 = (v_rbx) - (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2408));
loc_00BF0490:
    v_r14 = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2408)) + (1);
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2408) + a3 * 1))) != ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2408))))) goto loc_00BF04AB;
    a4 = (unsigned int)((6) + ((unsigned int)(v_r13)));
    if (condition_is_not_equal) goto loc_00BF0490;
loc_00BF04A3:
    a3 = 0;
    goto loc_00BF03C5;
loc_00BF04AB:
    a3 = 0;
    goto loc_00BF03C7;
loc_00BF04B3:
    if (1 == 0) goto loc_00BF04D6;
loc_00BF04B7:
    if ((*(unsigned int *)(v_rbx)) != 0x54494E49ULL) goto loc_00BF04D6;
    if ((*(unsigned int *)(v_rbx + 4)) == 0x4742444BULL) {
        a2 = 1;
        if (((*(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2524)) & (0x2000ULL)) != 0) { a2 = 0; }
    }
    v_r12 = ((unsigned int)(a2) == 0) ? 1 : 0;
    v_stack_m1C0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 12)));
    a1 = (unsigned int)(*(unsigned int *)(v_rbx + 16));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 16)))) <= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 8))))) { a1 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 8))); }
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 12)) + 4095) + ((unsigned int)(a1)));
    v_r14 = (unsigned int)((v_r14) & (0xFFFFF000ULL));
    result = MmImageSectionPagable(v_rbx, (unsigned int)(*(unsigned int *)(v_rbx + 12)), a3, a4);
    v_r10 = 0;
    v_r11 = ((unsigned int)(result) != 0) ? 1 : 0;
    v_stack_m1E8 = (unsigned int)(v_r11);
    if (((*(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2520)) & (0x100000ULL)) != 0) goto loc_00BF054E;
    a2 = 0;
    *(unsigned int *)(v_rsp - 280 + 312) = 128;
    *(unsigned __int64 *)(v_rsp - 280 - 48) = (unsigned int)(*(unsigned int *)(result + 2372));
    *(unsigned __int64 *)(v_rsp - 280 - 16) = 0;
    result = KeInitializeGate(v_rsp - 280 - 40, a2, a3, a4);
    v_r10 = 0;
    goto loc_00BF057E;
loc_00BF054E:
    *(unsigned int *)(v_rsp - 280 + 312) = 0;
loc_00BF0561:
    *(unsigned __int64 *)(v_rsp - 280 - 48) = 0;
    a1 = (unsigned int)((120) + (-8));
    result = (v_rsp - 280 - 48) + (1 + 7);
    a2 = (120 - 105) - (1);
    if (condition_is_not_equal) goto loc_00BF0561;
    if ((unsigned int)(a1) == 0) goto loc_00BF057E;
loc_00BF0573:
    *(unsigned __int8 *)(result) = 0;
    result = (result) + (1);
    a1 = (unsigned int)((a1) + (-1));
    if (condition_is_not_equal) goto loc_00BF0573;
loc_00BF057E:
    v_stack_m1D8 = *(unsigned __int64 *)(v_rsp - 280 + 296);
    if (v_stack_m1E0 == v_stack_m1B8) goto loc_00BF082D;
    v_rbx = (v_rbx) + (4);
loc_00BF05A7:
    if (0 < v_stack_m1C0) goto loc_00BF0783;
    if (0 < ((unsigned int)(v_r14))) goto loc_00BF077C;
    if ((v_rbx + 36) == v_stack_m1B0) goto loc_00BF07F7;
    if (0 < (*(unsigned int *)(v_rbx + 48))) goto loc_00BF07F7;
    v_rbx = (v_rbx) + (40);
    if (((*(unsigned int *)(v_rbx + 32)) & (0x2000000ULL)) != 0) goto loc_00BF05F6;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx - 4)))) != 0x54494E49ULL) goto loc_00BF05FD;
    if ((*(unsigned int *)(v_rbx)) != 0x4742444BULL) goto loc_00BF0627;
loc_00BF05F6:
    goto loc_00BF0703;
loc_00BF05FD:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx - 4)))) != 0x45474150ULL) goto loc_00BF0627;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rbx))) == ((unsigned __int16)((unsigned int)(0x7877ULL)))) goto loc_00BF05F6;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rbx))) == ((unsigned __int16)((unsigned int)(0x7277ULL)))) goto loc_00BF05F6;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rbx))) != ((unsigned __int16)((unsigned int)(0x7777ULL)))) goto loc_00BF0638;
    goto loc_00BF05F6;
loc_00BF0627:
    if (((unsigned int)(*(unsigned __int16 *)(v_rbx))) != 0x41525245ULL) goto loc_00BF0638;
    if ((*(unsigned __int16 *)(v_rbx)) == ((unsigned __int16)((unsigned int)(0x4154ULL)))) goto loc_00BF05F6;
loc_00BF0638:
    a4 = (v_rbx) - (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2384));
loc_00BF0660:
    a3 = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2384)) + (1);
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2384) + a4 * 1 - 4))) != ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2384))))) goto loc_00BF067A;
    v_r12 = (unsigned int)((7) + (-1));
    if (condition_is_not_equal) goto loc_00BF0660;
    goto loc_00BF06FE;
loc_00BF067A:
loc_00BF0681:
    a4 = (v_rbx - 4) + (1 + 7);
    v_r10 = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2392)) + (1 + 7);
    if ((*(unsigned __int64 *)(v_rbx - 4)) != (*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2392)))) goto loc_00BF06B8;
    a3 = (unsigned int)(((unsigned int)((unsigned int)(1 + 7))) + (-8));
    if (a3 >= ((unsigned int)(1 + 7))) goto loc_00BF0681;
    if (a3 == 0) goto loc_00BF06FE;
loc_00BF06A0:
    a4 = (a4) + (1);
    v_r10 = (v_r10) + (1);
    if (((unsigned __int8)(*(unsigned __int8 *)(a4))) != ((unsigned __int8)(*(unsigned __int8 *)(v_r10)))) goto loc_00BF06B8;
    a3 = (unsigned int)((a3) + (-1));
    if (condition_is_not_equal) goto loc_00BF06A0;
    goto loc_00BF06FE;
loc_00BF06B8:
    a3 = (v_rbx) - (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2400));
    v_r10 = (unsigned int)((v_r10) | (0xFFFFFFFFULL));
loc_00BF06C8:
    v_r11 = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2400)) + (1);
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2400) + a3 * 1 - 4))) != ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2400))))) goto loc_00BF06DE;
    a4 = (unsigned int)((4) + ((unsigned int)(v_r10)));
    if (condition_is_not_equal) goto loc_00BF06C8;
    goto loc_00BF06FE;
loc_00BF06DE:
    a3 = (v_rbx) - (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2408));
loc_00BF06EA:
    v_r14 = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2408)) + (1);
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2408) + a3 * 1 - 4))) != ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2408))))) goto loc_00BF0700;
    a4 = (unsigned int)((6) + ((unsigned int)(v_r10)));
    if (condition_is_not_equal) goto loc_00BF06EA;
loc_00BF06FE:
loc_00BF0700:
    v_r10 = 0;
loc_00BF0703:
    if ((*(unsigned int *)(v_rbx + 32)) >= 0) goto loc_00BF070D;
    goto loc_00BF0711;
loc_00BF070D:
    if (1 == 0) goto loc_00BF0730;
loc_00BF0711:
    if ((*(unsigned int *)(v_rbx - 4)) != 0x54494E49ULL) goto loc_00BF0730;
    if ((*(unsigned int *)(v_rbx)) == 0x4742444BULL) {
        a2 = 1;
        if (((*(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2524)) & (0x2000ULL)) != 0) { a2 = 0; }
    }
    v_r12 = ((unsigned int)(a2) == 0) ? 1 : 0;
    a1 = (unsigned int)(*(unsigned int *)(v_rbx + 12));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 12)))) <= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 4))))) { a1 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 4))); }
    a1 = (unsigned int)((a1) + (0xFFFULL));
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 8))) + ((unsigned int)(a1)));
    v_r14 = (unsigned int)((v_r14) & (0xFFFFF000ULL));
    result = MmImageSectionPagable(v_rbx - 4, a2, a3, a4);
    v_r10 = 0;
    v_r11 = ((unsigned int)(result) != 0) ? 1 : 0;
loc_00BF077C:
    if ((unsigned int)(v_r12) == 0) goto loc_00BF07FC;
    goto loc_00BF078A;
loc_00BF0783:
    if (0 >= v_stack_m1C4) goto loc_00BF07FC;
loc_00BF078A:
loc_00BF0797:
    if ((unsigned int)(*(unsigned int *)(v_stack_m1C8)) == 0) goto loc_00BF07BF;
    v_r10 = ((unsigned int)(*(unsigned int *)(v_stack_m1C8)) - 1) + (*(unsigned __int64 *)(v_stack_m1A0));
    if (v_stack_m1D8 < (*(unsigned __int64 *)(v_stack_m1A0))) goto loc_00BF07BC;
    if (v_stack_m1D8 <= v_r10) goto loc_00BF0845;
loc_00BF07BC:
    v_r10 = 0;
loc_00BF07BF:
    a2 = (unsigned int)((0) + (1));
    a1 = (v_stack_m1C8) + (4);
    result = (v_stack_m1A0) + (1 + 7);
    if (((unsigned int)(a2)) < 1) goto loc_00BF0797;
    if (0 < v_stack_m1C0) goto loc_00BF07D8;
    if ((unsigned int)(v_r11) != 0) goto loc_00BF07E4;
loc_00BF07D8:
    goto loc_00BF07E9;
loc_00BF07E4:
loc_00BF07E9:
loc_00BF07F7:
loc_00BF07FC:
    result = (v_stack_m1D8) + (0x1000ULL);
    a1 = (v_stack_m1E0) + (20);
    v_r13 = (unsigned int)((0) + (0x1000ULL));
    v_stack_m1D8 = result;
    v_stack_m1E0 = a1;
    if (a1 != v_stack_m1B8) goto loc_00BF05A7;
loc_00BF082D:
    v_r13 = (v_stack_m1D0) + (48);
    goto loc_00BF0E5B;
loc_00BF0845:
    goto loc_00BF07FC;
loc_00BF0854:
loc_00BF085A:
    if ((*(unsigned __int8 *)(v_r13 + 15)) < 0) goto loc_00BF0877;
    v_r14 = (unsigned int)((0) + (1));
    result = (v_r14 + v_r14 * 4 * 4) + (v_r13);
    if (result != v_stack_m1B8) goto loc_00BF085A;
loc_00BF0877:
    v_stack_m1E8 = (unsigned int)(v_r14);
    if ((unsigned int)(v_r14) == 0) goto loc_00BF0E12;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 280 + 312))) != 0) goto loc_00BF0AC3;
    v_stack_m1D8 = v_r13;
    *(unsigned __int64 *)(v_rsp - 280 - 88) = *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2768);
    v_stack_m1C4 = (unsigned int)((unsigned int)((unsigned int)(v_r14)));
    v_stack_m1E0 = *(unsigned __int64 *)(v_rsp - 280 + 296);
loc_00BF08AF:
    v_rbx = (unsigned int)((unsigned int)(1 + 7));
    if (((unsigned int)((unsigned int)((unsigned int)(v_r14)))) < ((unsigned int)(1 + 7))) { v_rbx = (unsigned int)((unsigned int)((unsigned int)(v_r14))); }
    if ((unsigned int)(v_rbx) == 0) goto loc_00BF09D8;
    v_stack_m1D0 = v_rsp - 280 + 104;
loc_00BF08D4:
    *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2768) + 8) = 0x1000ULL;
    v_r11 = (unsigned int)((0) << (12));
    v_r11 = (v_r11) + (v_stack_m1E0);
    *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2768)) = v_r11;
    v_stack_m1C0 = *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2104);
    if (v_r11 >= (v_r11 + 4096)) goto loc_00BF0925;
loc_00BF0919:
    result = (v_r11) + (64);
    if (result < (v_r11 + 4096)) goto loc_00BF0919;
loc_00BF0925:
    v_stack_m1C0 = 32;
loc_00BF093F:
loc_00BF0942:
    a3 = (v_stack_m1C0) ^ (*(unsigned __int64 *)(v_r11));
    v_r10 = (v_r11) + (1 + 7);
    a3 = (a3) ^ (*(unsigned __int64 *)(v_r10));
    v_r10 = (v_r10) + (1 + 7);
    result = (1 + 7) - (1);
    if (condition_is_not_equal) goto loc_00BF0942;
    a1 = (v_r10) - (v_r11);
    a1 = (a1) ^ (v_stack_m1C0);
    a1 = (a1) ^ (a1);
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2100))) ^ ((unsigned int)(*(unsigned __int64 *)(v_rsp - 280 + 296))));
    *(unsigned __int64 *)(v_rsp - 280 + 80) = *(unsigned __int64 *)(v_rsp - 280 + 296);
    a4 = (unsigned int)((a4) ^ ((unsigned int)(v_stack_m1E0)));
    a4 = (unsigned int)((a4) & (63));
    if (condition_is_equal) { a4 = 1; }
    if (condition_is_not_equal) goto loc_00BF093F;
    goto loc_00BF09A0;
loc_00BF099D:
    a3 = (unsigned int)((a3) ^ (a3));
loc_00BF09A0:
    result = (a3) >> (31);
    if (result != 0) goto loc_00BF099D;
    v_r12 = (unsigned int)((0) + (1));
    v_r13 = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2768)) + (48);
    *(unsigned int *)(v_stack_m1D0) = a3;
    a2 = (v_stack_m1D0) + (4);
    v_stack_m1D0 = a2;
    if (((unsigned int)(v_r12)) < ((unsigned int)(v_rbx))) goto loc_00BF08D4;
loc_00BF09D8:
    result = sub_0051AFB0(v_stack_m1A8, *(unsigned __int64 *)(v_rsp - 280 - 88), (unsigned int)((unsigned int)(v_rbx)), a4);
    v_r10 = 0;
    if ((unsigned int)(v_rbx) == 0) goto loc_00BF0A77;
    v_stack_m1D0 = (unsigned int)((unsigned int)(v_rbx));
loc_00BF0A07:
loc_00BF0A17:
    a3 = (unsigned int)((16) + (-8));
    *(unsigned __int64 *)(v_stack_m1D8) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 280 - 88) + 16);
    a1 = (*(unsigned __int64 *)(v_rsp - 280 - 88) + 16) + (1 + 7);
    a2 = (v_stack_m1D8) + (1 + 7);
    v_r13 = (16 - 14) - (1);
    if (condition_is_not_equal) goto loc_00BF0A17;
    if (a3 == 0) goto loc_00BF0A41;
loc_00BF0A31:
    a1 = (a1) + (1);
    *(unsigned __int8 *)(a2) = (unsigned __int8)(*(unsigned __int8 *)(a1));
    a2 = (a2) + (1);
    a3 = (unsigned int)((a3) + (-1));
    if (condition_is_not_equal) goto loc_00BF0A31;
loc_00BF0A41:
    v_r11 = (*(unsigned __int64 *)(v_rsp - 280 - 88) + 16) + (48);
    v_r10 = (v_stack_m1D8) + (20);
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1D8 + 16))))) ^ (*(unsigned int *)(v_rsp - 280 + 104)));
    v_r12 = (v_rsp - 280 + 104) + (4);
    a1 = (unsigned int)((a1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1D8 + 16)))));
    *(unsigned int *)(v_stack_m1D8 + 16) = (unsigned int)(a1);
    a4 = (v_stack_m1D8 + 16) + (20);
    if (condition_is_not_equal) goto loc_00BF0A07;
    v_r10 = 0;
loc_00BF0A77:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) << (12));
    result = (unsigned int)(((unsigned int)(v_stack_m1C4)) - ((unsigned int)(v_rbx)));
    v_stack_m1D8 = v_stack_m1D8 + v_rbx + v_rbx * 4 * 4;
    v_rbx = (unsigned int)((v_rbx) << (15));
    v_stack_m1C4 = (unsigned int)(result);
    if ((unsigned int)(result) != 0) goto loc_00BF08AF;
    goto loc_00BF0E0D;
loc_00BF0AC3:
    if ((unsigned int)((unsigned int)(v_stack_m1E8)) == 0) goto loc_00BF0E12;
loc_00BF0ACF:
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m1E8)))) - (0));
    if (((unsigned int)(v_r12)) > ((unsigned int)(result))) { v_r12 = (unsigned int)(result); }
    result = KeGuardDispatchICall(64, *(unsigned __int64 *)(v_stack_m1A8 + 2776), (unsigned int)(*(unsigned int *)(v_stack_m1A8 + 2096)), a4);
    v_stack_m1D0 = result;
    a2 = (*(unsigned __int64 *)(v_stack_m1A8 + 2776)) << (32);
    result = (result) | (a2);
    a2 = (result) ^ (result);
    *(unsigned __int64 *)(v_rsp - 280 + 88) = a2;
    a1 = (a2) ^ (v_rbx);
    a2 = (a2) >> (1);
    result = (v_rbx) * (a2);
    a1 = (a1) - (result);
    if (((unsigned int)(a1)) > 5) goto loc_00BF0BD3;
    if (((unsigned int)(a1)) == 5) goto loc_00BF0BBF;
    if ((unsigned int)(a1) == 0) goto loc_00BF0BAB;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00BF0B98;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00BF0B84;
    if (((unsigned int)(a1)) == 1) goto loc_00BF0B6C;
    *(unsigned int *)(v_rsp - 280 - 128) = 0x67076494ULL;
    goto loc_00BF0CE1;
loc_00BF0B6C:
    *(unsigned int *)(v_rsp - 280 - 124) = 0xA8223938ULL;
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 280 - 124))) ^ (3));
    goto loc_00BF0CE1;
loc_00BF0B84:
    *(unsigned int *)(v_rsp - 280 - 120) = 0x85B5910DULL;
    goto loc_00BF0CE1;
loc_00BF0B98:
    *(unsigned int *)(v_rsp - 280 - 116) = 0xB2AD31A1ULL;
    goto loc_00BF0CE1;
loc_00BF0BAB:
    *(unsigned int *)(v_rsp - 280 - 112) = 0xD098D0D8ULL;
    goto loc_00BF0CE1;
loc_00BF0BBF:
    *(unsigned int *)(v_rsp - 280 - 108) = 0x288C49EDULL;
    goto loc_00BF0CE1;
loc_00BF0BD3:
    a1 = (unsigned int)((a1) - (6));
    if (condition_is_equal) goto loc_00BF0CCF;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00BF0CBE;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00BF0CAD;
    if (((unsigned int)(a1)) == 1) goto loc_00BF0C98;
    a2 = (6) << (32);
    result = (result) | (a2);
    a2 = (result) ^ (result);
    *(unsigned __int64 *)(v_rsp - 280 + 96) = a2;
    a4 = (unsigned int)((a2) ^ ((unsigned int)(v_rbx)));
    a4 = (unsigned int)((a4) >> (5));
    a2 = (unsigned int)((a2) >> (3));
    result = (unsigned int)(((unsigned int)(0x4EC4EC4FULL)) * ((unsigned int)(a2)));
    a1 = (unsigned int)(((unsigned int)(a4)) - ((unsigned int)(result)));
    a1 = (unsigned int)((a1) + (97));
    a4 = (unsigned int)((a4) >> (5));
    a1 = (unsigned int)((a1) << (8));
    a2 = (unsigned int)((a2) >> (3));
    result = (unsigned int)(((unsigned int)(0x4EC4EC4FULL)) * ((unsigned int)(a2)));
    a3 = (unsigned int)(((unsigned int)(a4)) - ((unsigned int)(result)));
    a3 = (unsigned int)((a3) + (65));
    a3 = (unsigned int)((a3) | ((unsigned int)(a1)));
    a2 = (unsigned int)((a2) >> (3));
    result = (unsigned int)(((unsigned int)(0x4EC4EC4FULL)) * ((unsigned int)(a2)));
    a4 = (unsigned int)((a4) >> (5));
    a3 = (unsigned int)((a3) << (8));
    a1 = (unsigned int)(((unsigned int)(a4)) - ((unsigned int)(result)));
    a1 = (unsigned int)((a1) + (97));
    a2 = (unsigned int)((a2) >> (3));
    a1 = (unsigned int)((a1) | (a3));
    result = (unsigned int)(((unsigned int)(0x4EC4EC4FULL)) * ((unsigned int)(a2)));
    a1 = (unsigned int)((a1) << (8));
    a4 = (unsigned int)((a4) - ((unsigned int)(result)));
    a4 = (unsigned int)((a4) + (65));
    a4 = (unsigned int)((a4) | ((unsigned int)(a1)));
    goto loc_00BF0CE1;
loc_00BF0C98:
    *(unsigned int *)(v_rsp - 280 - 104) = 0xB0869E85ULL;
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 280 - 104))) ^ (9));
    goto loc_00BF0CE1;
loc_00BF0CAD:
    *(unsigned int *)(v_rsp - 280 - 100) = 0x64664142ULL;
    goto loc_00BF0CE1;
loc_00BF0CBE:
    *(unsigned int *)(v_rsp - 280 - 96) = 0x82C6A6D8ULL;
    goto loc_00BF0CE1;
loc_00BF0CCF:
    *(unsigned int *)(v_rsp - 280 - 92) = 0x4E574672ULL;
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 280 - 92))) ^ ((unsigned int)(a2)));
loc_00BF0CE1:
    result = KeGuardDispatchICall(80 - 16, 80, (unsigned int)(a4), a4);
    a2 = 0;
    v_rbx = v_rsp - 280 - 8;
    if (result != 0) { v_rbx = result; }
    a1 = (unsigned int)((0) << (12));
    a1 = (a1) + (*(unsigned __int64 *)(v_rsp - 280 + 296));
    *(unsigned __int64 *)(v_rbx) = v_rsp - 280 - 48;
    *(unsigned __int64 *)(v_rbx + 8) = v_stack_m1D0;
    *(unsigned __int64 *)(v_rbx + 16) = a1;
    *(unsigned int *)(v_rbx + 32) = (unsigned int)(v_r12);
    *(unsigned int *)(v_rbx + 40) = 1;
    *(unsigned __int64 *)(v_rbx + 72) = v_rbx;
    *(unsigned __int64 *)(v_rbx + 48) = 0;
    result = (0 + 0 * 4 * 4) + (v_stack_m1B0);
    *(unsigned __int64 *)(v_rbx + 24) = result;
    *(unsigned __int64 *)(v_rbx + 64) = v_rip + 1342;
    result = (unsigned int)((1) + (1));
    if (((unsigned int)(result)) != 1) goto loc_00BF0D74;
    if ((*(unsigned int *)(v_rsp - 280 - 12)) != 0) {
        a3 = 0;
        a1 = v_rsp - 280 - 40;
        result = KeWaitForGate(a1, a2, a3, a4);
    }
    a2 = 0;
    *(unsigned int *)(v_rsp - 280 - 12) = 1;
    result = ExQueueWorkItem(v_rbx + 48, a2, a3, a4);
    v_r10 = 0;
    if (v_rbx != (v_rsp - 280 - 8)) goto loc_00BF0DB9;
    if ((*(unsigned int *)(v_rsp - 280 - 12)) == 0) goto loc_00BF0DB9;
    v_rsi = 0;
loc_00BF0D96:
    a3 = 0;
    a2 = 0;
    result = KeWaitForGate(v_rsp - 280 - 40, a2, a3, a4);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 280 - 16))) != 0) goto loc_00BF0D96;
    *(unsigned int *)(v_rsp - 280 - 12) = 0;
    v_r10 = 0;
loc_00BF0DB9:
    if (v_stack_m1D0 != 0) goto loc_00BF0DEB;
    if ((*(unsigned int *)(v_rsp - 280 - 12)) == 0) goto loc_00BF0DEB;
    v_rsi = 0;
loc_00BF0DC8:
    a3 = 0;
    a2 = 0;
    result = KeWaitForGate(v_rsp - 280 - 40, a2, a3, a4);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 280 - 16))) != 0) goto loc_00BF0DC8;
    *(unsigned int *)(v_rsp - 280 - 12) = 0;
    v_r10 = 0;
loc_00BF0DEB:
    v_r15 = (unsigned int)((0) + ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 280 + 312)))));
    if (((unsigned int)(v_r15)) < ((unsigned int)((unsigned int)(v_stack_m1E8)))) goto loc_00BF0ACF;
loc_00BF0E0D:
loc_00BF0E12:
    goto loc_00BF0E28;
loc_00BF0E1B:
    if ((*(unsigned __int8 *)((unsigned int)((unsigned int)((unsigned int)(v_stack_m1E8))) + 15)) >= 0) goto loc_00BF0E38;
    v_r14 = (unsigned int)(((unsigned int)(v_stack_m1E8)) + (1));
loc_00BF0E28:
    result = (v_r14 + v_r14 * 4 * 4) + (v_stack_m1B0);
    if (result != v_stack_m1B8) goto loc_00BF0E1B;
loc_00BF0E38:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) << (12));
    a2 = (*(unsigned __int64 *)(v_rsp - 280 + 296)) + (result);
    *(unsigned __int64 *)(v_rsp - 280 + 296) = a2;
loc_00BF0E5B:
    v_stack_m1B0 = v_stack_m1B0 + (unsigned int)((unsigned int)(v_r14)) + (unsigned int)((unsigned int)(v_r14)) * 4 * 4;
    if ((v_stack_m1B0 + (unsigned int)((unsigned int)(v_r14)) + (unsigned int)((unsigned int)(v_r14)) * 4 * 4) != v_stack_m1B8) goto loc_00BF0854;
    if ((*(unsigned int *)(v_rsp - 280 + 312)) == 0) goto loc_00BF0E97;
    if ((*(unsigned int *)(v_rsp - 280 - 12)) == 0) goto loc_00BF0E97;
loc_00BF0E78:
    a3 = 0;
    a2 = 0;
    result = KeWaitForGate(v_rsp - 280 - 40, a2, a3, a4);
    v_r10 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 280 - 16))) != 0) goto loc_00BF0E78;
    *(unsigned int *)(v_rsp - 280 - 12) = 0;
loc_00BF0E97:
    if (((*(unsigned __int8 *)(v_rsp - 280 + 304)) & (1)) == 0) goto loc_00BF1113;
    if ((unsigned int)((unsigned int)(v_stack_m1C8)) == 0) goto loc_00BF1113;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1A8 + 2052)) + 48)) <= (*(unsigned int *)(v_stack_m1A8 + 2660))) goto loc_00BF0FA3;
    result = sub_00BE7AF8(v_stack_m1A8, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1A8 + 2052)) + 48)), (unsigned int)(*(unsigned int *)(v_stack_m1A8 + 2372)), a4);
    v_r10 = 0;
    if (result != 0) goto loc_00BF0EEF;
loc_00BF0EE5:
    goto loc_00BF1244;
loc_00BF0EEF:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m1A8 + 2520)))) & (2)) != 0) goto loc_00BF0F9A;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m1A8 + 2520))) & (0x10000000ULL));
    a1 = (unsigned int)(-(a1));
    a1 = (unsigned int)((a1) & (*(unsigned int *)(v_stack_m1A8 + 2372)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1A8 + 2052)))) < 8) goto loc_00BF0F34;
    a2 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1A8 + 2052))))) >> (3);
loc_00BF0F26:
    *(unsigned __int64 *)(v_stack_m1A8) = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m1A8 + 2052))) + (-8));
    v_rsi = (v_stack_m1A8) + (8);
    a2 = (a2) - (1);
    if (condition_is_not_equal) goto loc_00BF0F26;
loc_00BF0F34:
    if ((unsigned int)(result) == 0) goto loc_00BF0F43;
loc_00BF0F38:
    *(unsigned __int8 *)(v_rsi) = 0;
    v_rsi = (v_rsi) + (1);
    result = (unsigned int)((result) + (-1));
    if (condition_is_not_equal) goto loc_00BF0F38;
loc_00BF0F43:
    *(unsigned int *)(result + 2372) = (unsigned int)(a1);
    if (((unsigned int)(a1)) == 3) goto loc_00BF0F82;
    if (((*(unsigned int *)(result + 2520)) & (0x8000000ULL)) != 0) goto loc_00BF0F79;
    if ((unsigned int)(a1) == 0) goto loc_00BF0F79;
    result = KeGuardDispatchICall(*(unsigned __int64 *)(v_stack_m1A8 + 2024) - 8, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m1A8 + 2024) - 8), *(unsigned __int64 *)(v_stack_m1A8 + 2024), a4);
    goto loc_00BF0F91;
loc_00BF0F79:
    goto loc_00BF0F89;
loc_00BF0F82:
loc_00BF0F89:
    result = KeGuardDispatchICall(*(unsigned __int64 *)(v_stack_m1A8 + 2024), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m1A8 + 2024) - 8), *(unsigned __int64 *)(v_stack_m1A8 + 2024), a4);
loc_00BF0F91:
    *(unsigned int *)(result + 2372) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 2372)));
    v_r10 = 0;
loc_00BF0F9A:
    goto loc_00BF0FAC;
loc_00BF0FA3:
    *(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2052) = (unsigned int)(result);
loc_00BF0FAC:
loc_00BF0FC1:
    *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + (unsigned int)(*(unsigned int *)(v_stack_m1A8 + 2052)) * 1) = 0;
    a1 = (unsigned int)((48) + (-8));
    result = ((unsigned int)(*(unsigned int *)(result + 2372)) + (unsigned int)(*(unsigned int *)(v_stack_m1A8 + 2052)) * 1) + (8);
    a2 = (48 - 42) - (1);
    if (condition_is_not_equal) goto loc_00BF0FC1;
    if ((unsigned int)(a1) == 0) goto loc_00BF0FDE;
loc_00BF0FD3:
    *(unsigned __int8 *)(result) = 0;
    result = (result) + (1);
    a1 = (unsigned int)((a1) + (-1));
    if (condition_is_not_equal) goto loc_00BF0FD3;
loc_00BF0FDE:
    *(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + (unsigned int)(*(unsigned int *)(v_stack_m1A8 + 2052)) * 1) = 13;
    *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + (unsigned int)(*(unsigned int *)(v_stack_m1A8 + 2052)) * 1 + 8) = v_stack_m1A0;
    *(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + (unsigned int)(*(unsigned int *)(v_stack_m1A8 + 2052)) * 1 + 16) = (unsigned int)((unsigned int)(v_stack_m1C8));
    if (v_stack_m1A0 >= (v_stack_m1A0 + (unsigned int)(v_stack_m1C8) * 1)) goto loc_00BF101E;
loc_00BF1012:
    result = (v_stack_m1A0) + (64);
    if (result < (v_stack_m1A0 + (unsigned int)(v_stack_m1C8) * 1)) goto loc_00BF1012;
loc_00BF101E:
    v_r11 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m1C8)))) >> (7));
    if ((unsigned int)(v_r11) == 0) goto loc_00BF1082;
loc_00BF1037:
loc_00BF103A:
    a3 = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2104)) ^ (*(unsigned __int64 *)(v_stack_m1A0));
    a4 = (v_stack_m1A0) + (8);
    a3 = (a3) ^ (*(unsigned __int64 *)(a4));
    a4 = (a4) + (8);
    result = (8) - (1);
    if (condition_is_not_equal) goto loc_00BF103A;
    a1 = (a4) - (v_stack_m1A0);
    a1 = (a1) ^ (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2104));
    a1 = (a1) ^ (a1);
    a2 = (unsigned int)((a2) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1A8 + 2052)))));
    v_r10 = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2100))) ^ ((unsigned int)(a2)));
    v_r10 = (unsigned int)((v_r10) & (63));
    if (condition_is_equal) { v_r10 = 1; }
    v_r11 = (unsigned int)((v_r11) + (-1));
    if (condition_is_not_equal) goto loc_00BF1037;
loc_00BF1082:
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m1C8)))) & (127));
    if (((unsigned int)(a2)) < 8) goto loc_00BF10A7;
    result = ((unsigned int)((unsigned int)(a2))) >> (3);
loc_00BF1093:
    a3 = (a3) ^ (*(unsigned __int64 *)(a4));
    a4 = (a4) + (8);
    a2 = (unsigned int)((a2) + (-8));
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_00BF1093;
loc_00BF10A7:
    if ((unsigned int)(a2) == 0) goto loc_00BF10C0;
loc_00BF10AB:
    a3 = (a3) ^ (*(unsigned __int8 *)(a4));
    a4 = (a4) + (1);
    a2 = (unsigned int)((a2) + (-1));
    if (condition_is_not_equal) goto loc_00BF10AB;
loc_00BF10C0:
    goto loc_00BF10C8;
loc_00BF10C5:
    a3 = (unsigned int)((a3) ^ (a3));
loc_00BF10C8:
    result = (a3) >> (31);
    if (result != 0) goto loc_00BF10C5;
    *(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + (unsigned int)(*(unsigned int *)(v_stack_m1A8 + 2052)) * 1 + 20) = a3;
    if (((*(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2520)) & (0x20000000ULL)) == 0) goto loc_00BF1106;
    if ((unsigned int)((unsigned int)(v_stack_m1C8)) != 0) {
        a2 = v_stack_m1A0;
        a4 = (unsigned int)(*(unsigned int *)(result + 2372)) + (unsigned int)(*(unsigned int *)(v_stack_m1A8 + 2052)) * 1 + 28;
        a3 = (unsigned int)((unsigned int)(v_stack_m1C8));
        a1 = (unsigned int)(*(unsigned int *)(result + 2372));
        result = sub_0051AF4C(a1, a2, a3, a4);
    }
    *(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + (unsigned int)(*(unsigned int *)(v_stack_m1A8 + 2052)) * 1 + 24) = 1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 280 + 288)) = (unsigned int)(*(unsigned int *)(result + 2372));
loc_00BF1113:
    result = 0;
    goto loc_00BF1244;
loc_00BF111A:
    if (condition_is_above_or_equal) goto loc_00BF1259;
    if ((*(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2328)) != 8) goto loc_00BF123F;
    *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2344) = 8;
    result = (result) + ((unsigned int)(*(unsigned int *)(result + 2372)));
    *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2352) = 271;
    *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2336) = result;
    *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2360) = (unsigned int)(v_stack_m1C8);
    *(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2328) = 1;
    if (condition_is_below) goto loc_00BF123F;
    if (((*(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2524)) & (0x200000ULL)) == 0) goto loc_00BF123F;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2520))))) == 0) goto loc_00BF123F;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2052))) - ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2676)))));
    a1 = ((unsigned int)((unsigned int)(result))) >> (3);
    if (((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2676)) + (unsigned int)(*(unsigned int *)(result + 2372)) * 1) == ((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2676)) + (unsigned int)(*(unsigned int *)(result + 2372)) * 1 + a1 * 8)) goto loc_00BF11ED;
loc_00BF11C5:
    a2 = ((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2676)) + (unsigned int)(*(unsigned int *)(result + 2372)) * 1) + (1 + 7);
    result = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2676)) + (unsigned int)(*(unsigned int *)(result + 2372)) * 1)) ^ (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2104));
    a1 = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2680))) & (63));
    a3 = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2680)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    if (a2 != ((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2676)) + (unsigned int)(*(unsigned int *)(result + 2372)) * 1 + a1 * 8)) goto loc_00BF11C5;
    v_r15 = 0;
loc_00BF11ED:
    if (a3 == (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2688))) goto loc_00BF123F;
    *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 1416)) = (unsigned int)(*(unsigned int *)(result + 2372));
    *(unsigned int *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 1416) + 16) = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2052)));
    result = *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 1416);
    if ((*(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2328)) == 0) {
        result = *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 1416);
        a1 = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2688)) ^ (a3);
        *(unsigned __int64 *)(result + 24) = a1;
    }
    a2 = 0;
    result = sub_00BE8384((unsigned int)(*(unsigned int *)(result + 2372)), a2, a3, 256);
loc_00BF123F:
loc_00BF1244:
    v_rsp = (v_rsp) + (472);
    return (unsigned int)(0xC000007BULL);
loc_00BF1259:
    *(unsigned int *)(v_rsp - 280 + 288) = 0xE8000009ULL;
    v_stack_p20 = 0;
    result = KeBugCheckEx((unsigned int)(*(unsigned int *)(v_rsp - 280 + 288)), 4 + 6, (unsigned int)(v_stack_m1C8), 4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00BEFF8C(void *Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint32_t v_stack_m1C0;
    uint32_t v_stack_m1C4;
    uint64_t v_stack_m1C8;
    uint64_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint32_t v_stack_m1E8;
    uint64_t v_stack_p20;

    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(void **)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (472);
    result = KeGuardDispatchICall(Arg2, Arg2, Arg3, Arg4);
    local_r15 = 0;
    if (result == 0) goto loc_00BF123F;
    *(uint16_t *)(local_rsp - 0x118 + 0x138) = (uint16_t)(*(uint16_t *)(result + 0x6));
    if ((uint16_t)(*(uint16_t *)(result + 0x6)) == 0) goto loc_00BF111A;
    if ((*(uint32_t *)(result + 0x38)) < 0x1000ULL) goto loc_00BF111A;
    if (((Arg2) & (0xFFFULL)) != 0) goto loc_00BF111A;
    v_stack_m1C4 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x54)));
    result = KeGuardDispatchICall(*(uint64_t *)(*(uint64_t *)(arg1) + 0x538), Arg2, Arg3, Arg4);
loc_00BF0050:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x620)) + 0x10 + 0x8)) == Arg2) goto loc_00BF0060;
    Arg2 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x620)) + 16) + (local_r15 + 24);
    if (Arg2 < (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x620)) + 16 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x620)))) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x620)))) * 2 * 8)) goto loc_00BF0050;
    goto loc_00BF0074;
loc_00BF0060:
    *(uint64_t *)(local_rsp - 0x118 - 0x50) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x118 - 0x40) = v_xmm1;
loc_00BF0074:
    result = KeGuardDispatchICall(*(uint64_t *)(*(uint64_t *)(arg1) + 0x538), Arg2, Arg3, Arg4);
    local_r10 = (uint32_t)((local_r10) | (0xFFFFFFFFULL));
    Arg4 = 0;
    if (!sign_flag) goto loc_00BF00E1;
loc_00BF00B3:
    *(uint64_t *)(local_rsp - 0x118 - 0x50) = 0;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r15 + 24))) + ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
    result = (local_rsp - 280 - 80) + (1 + 7);
    Arg2 = (1 + 2) - (1);
    if (condition_is_not_equal) goto loc_00BF00B3;
    if ((uint32_t)(Arg1) == 0) goto loc_00BF00D0;
loc_00BF00C5:
    *(uint8_t *)(result) = 0;
    result = (result) + (1);
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(local_r10)));
    if (condition_is_not_equal) goto loc_00BF00C5;
loc_00BF00D0:
    *(uint32_t *)(local_rsp - 0x118 - 0x40) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x50)));
    *(uint64_t *)(local_rsp - 0x118 - 0x48) = Arg2;
    *(uint64_t *)(local_rsp - 0x118 - 0x50) = 1;
    goto loc_00BF00E4;
loc_00BF00E1:
loc_00BF00E4:
    Arg1 = (uint32_t)((Arg2) & (0xFFFULL));
    Arg1 = (Arg1) + (0xFFFULL);
    result = ((uint32_t)(*(uint32_t *)(local_rsp - 0x118 - 0x40))) + (Arg1);
    result = (result) >> (12);
    v_stack_m1B0 = result;
    v_stack_m1E8 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x804)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x804))) + (48));
    local_r14 = (uint32_t)((result + result * 4) << (2));
    result = (uint32_t)((result) + ((uint32_t)(local_r14)));
    if (((uint32_t)(result)) <= (*(uint32_t *)(*(uint64_t *)(arg1) + 0xA64))) goto loc_00BF0207;
    result = sub_00BE7AF8(*(uint64_t *)(arg1), (uint32_t)((uint32_t)(result)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x944)), Arg4);
    Arg4 = 0;
    v_stack_m1A8 = result;
    if (result == 0) goto loc_00BF0EE5;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x9D8)))) & (2)) != 0) goto loc_00BF01F4;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x9D8))) & (0x10000000ULL));
    Arg1 = (uint32_t)(-(Arg1));
    Arg1 = (uint32_t)((Arg1) & (*(uint32_t *)(*(uint64_t *)(arg1) + 0x944)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x804)))) < ((uint32_t)(1 + 7))) goto loc_00BF018E;
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x804))))) >> (3);
loc_00BF0180:
    *(uint64_t *)(*(uint64_t *)(arg1)) = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x804))) + (-8));
    local_rbx = (*(uint64_t *)(arg1)) + (1 + 7);
    Arg2 = (Arg2) - (1);
    if (condition_is_not_equal) goto loc_00BF0180;
loc_00BF018E:
    if ((uint32_t)(result) == 0) goto loc_00BF019D;
loc_00BF0192:
    *(uint8_t *)(local_rbx) = 0;
    local_rbx = (local_rbx) + (1);
    result = (uint32_t)((result) + (-1));
    if (condition_is_not_equal) goto loc_00BF0192;
loc_00BF019D:
    *(uint32_t *)(result + 0x944) = (uint32_t)(Arg1);
    if (((uint32_t)(Arg1)) == 3) goto loc_00BF01DC;
    if (((*(uint32_t *)(result + 0x9D8)) & (0x8000000ULL)) != 0) goto loc_00BF01D3;
    if ((uint32_t)(Arg1) == 0) goto loc_00BF01D3;
    result = KeGuardDispatchICall(*(uint64_t *)(*(uint64_t *)(arg1) + 0x7E8) - 8, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x7E8) - 0x8), *(uint64_t *)(*(uint64_t *)(arg1) + 0x7E8), Arg4);
    goto loc_00BF01EB;
loc_00BF01D3:
    goto loc_00BF01E3;
loc_00BF01DC:
loc_00BF01E3:
    result = KeGuardDispatchICall(*(uint64_t *)(*(uint64_t *)(arg1) + 0x7E8), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x7E8) - 0x8), *(uint64_t *)(*(uint64_t *)(arg1) + 0x7E8), Arg4);
loc_00BF01EB:
    *(uint32_t *)(result + 0x944) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x944)));
    Arg4 = 0;
loc_00BF01F4:
    local_r10 = (uint32_t)((local_r10) | (0xFFFFFFFFULL));
    goto loc_00BF0215;
loc_00BF0207:
    v_stack_m1A8 = (uint32_t)(*(uint32_t *)(result + 0x944));
    *(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x804) = (uint32_t)(result);
loc_00BF0215:
    local_rbx = ((uint32_t)(v_stack_m1E8)) + ((uint32_t)(*(uint32_t *)(result + 0x944)));
    v_stack_m1D0 = local_rbx;
loc_00BF0232:
    *(uint64_t *)(local_rbx) = 0;
    Arg1 = (uint32_t)((48) + ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
    result = (local_rbx) + (1 + 7);
    Arg2 = (48 - 42) - (1);
    if (condition_is_not_equal) goto loc_00BF0232;
    if ((uint32_t)(Arg1) == 0) goto loc_00BF024F;
loc_00BF0244:
    *(uint8_t *)(result) = 0;
    result = (result) + (1);
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(local_r10)));
    if (condition_is_not_equal) goto loc_00BF0244;
loc_00BF024F:
    *(uint32_t *)(local_rbx) = 33;
    *(uint64_t *)(local_rbx + 0x8) = 0;
    *(uint32_t *)(local_rbx + 0x10) = 0;
    goto loc_00BF026B;
loc_00BF0269:
    Arg1 = (uint32_t)((*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x838)) ^ ((uint32_t)(*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x838))));
loc_00BF026B:
    result = (*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x838)) >> (31);
    if (result != 0) goto loc_00BF0269;
    *(uint32_t *)(local_rbx + 0x14) = (uint32_t)(Arg1);
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x118 + 0x120)) = (uint32_t)(*(uint32_t *)(result + 0x944));
loc_00BF0293:
    local_r12 = (uint32_t)((local_r15 + 24) + ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
    *(uint64_t *)(local_rbx + 0x18) = *(uint64_t *)(local_rsp - 0x118 - 0x50);
    Arg1 = (local_rsp - 280 - 80) + (1 + 7);
    Arg2 = (local_rbx + 24) + (1 + 7);
    Arg3 = (3) - (1);
    if (condition_is_not_equal) goto loc_00BF0293;
    if ((uint32_t)(local_r12) == 0) goto loc_00BF02BB;
loc_00BF02AC:
    Arg1 = (Arg1) + (1);
    *(uint8_t *)(Arg2) = (uint8_t)(*(uint8_t *)(arg1));
    Arg2 = (Arg2) + (1);
    local_r12 = (uint32_t)((local_r12) + ((uint32_t)(local_r10)));
    if (condition_is_not_equal) goto loc_00BF02AC;
loc_00BF02BB:
    result = KeGuardDispatchICall(*(uint64_t *)(local_rsp - 0x118 + 0x128), 1, 12, v_stack_m1C8);
    Arg3 = 0;
    v_stack_m1A0 = result;
    if (result == 0) {
        v_stack_m1C8 = 0;
    }
    if (((*(uint8_t *)(local_rsp - 0x118 + 0x130)) & (1)) == 0) {
        v_stack_m1A0 = 0;
        v_stack_m1C8 = 0;
    }
    v_stack_m1E0 = local_rbx + 48;
    v_stack_m1B8 = local_rbx + 48 + (uint32_t)(v_stack_m1B0) + (uint32_t)(v_stack_m1B0) * 4 * 4;
    if (((uint32_t)(local_r14)) < ((uint32_t)(1 + 7))) goto loc_00BF033D;
    Arg1 = ((uint32_t)((uint32_t)(local_r14))) >> (3);
loc_00BF032A:
    *(uint64_t *)(local_rbx + 0x30) = -1;
    local_r14 = (uint32_t)((local_r14) + (-8));
    result = (local_rbx + 48) + (1 + 7);
    Arg1 = (Arg1) - (1);
    if (condition_is_not_equal) goto loc_00BF032A;
loc_00BF033D:
    if ((uint32_t)(local_r14) == 0) goto loc_00BF034E;
loc_00BF0342:
    *(uint8_t *)(result) = 255;
    result = (result) + (1);
    local_r14 = (uint32_t)((local_r14) + (-1));
    if (condition_is_not_equal) goto loc_00BF0342;
loc_00BF034E:
    local_rbx = (*(uint16_t *)(result + 0x14)) + (24);
    local_rbx = (local_rbx) + (result);
    v_stack_m1B0 = local_rbx + *(uint16_t *)(local_rsp - 0x118 + 0x138) + *(uint16_t *)(local_rsp - 0x118 + 0x138) * 4 * 8;
    if (((*(uint32_t *)(local_rbx + 0x24)) & (0x2000000ULL)) != 0) goto loc_00BF03C5;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx)))) != 0x54494E49ULL) goto loc_00BF03A8;
    if ((*(uint32_t *)(local_rbx + 0x4)) == 0x4742444BULL) goto loc_00BF03C5;
loc_00BF03A8:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx)))) != 0x45474150ULL) goto loc_00BF03D8;
    if (((uint16_t)(*(uint16_t *)(local_rbx + 0x4))) == ((uint16_t)((uint32_t)(0x7877ULL)))) goto loc_00BF03C5;
    if (((uint16_t)(*(uint16_t *)(local_rbx + 0x4))) == ((uint16_t)((uint32_t)(0x7277ULL)))) goto loc_00BF03C5;
    if (((uint16_t)(*(uint16_t *)(local_rbx + 0x4))) != ((uint16_t)((uint32_t)(0x7777ULL)))) goto loc_00BF03E6;
loc_00BF03C5:
loc_00BF03C7:
    if ((*(uint32_t *)(local_rbx + 0x24)) >= 0) goto loc_00BF04B3;
    goto loc_00BF04B7;
loc_00BF03D8:
    if (((uint32_t)(*(uint16_t *)(local_rbx + 0x4))) != 0x41525245ULL) goto loc_00BF03E6;
    if ((*(uint16_t *)(local_rbx + 0x4)) == ((uint16_t)((uint32_t)(0x4154ULL)))) goto loc_00BF03C5;
loc_00BF03E6:
    Arg4 = (local_rbx) - (*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x950));
    local_r13 = (uint32_t)((result) | (0xFFFFFFFFULL));
loc_00BF0412:
    Arg3 = (*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x950)) + (1);
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x950) + Arg4 * 1))) != ((uint8_t)(*(uint8_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x950))))) goto loc_00BF0427;
    local_r12 = (uint32_t)((7) + ((uint32_t)(local_r13)));
    if (condition_is_not_equal) goto loc_00BF0412;
    goto loc_00BF04A3;
loc_00BF0427:
loc_00BF042D:
    Arg4 = (local_rbx) + (1 + 7);
    local_r10 = (*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x958)) + (1 + 7);
    if ((*(uint64_t *)(local_rbx)) != (*(uint64_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x958)))) goto loc_00BF0463;
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(1 + 7))) + (-8));
    if (Arg3 >= ((uint32_t)(1 + 7))) goto loc_00BF042D;
    if (Arg3 == 0) goto loc_00BF04A3;
loc_00BF044C:
    Arg4 = (Arg4) + (1);
    local_r10 = (local_r10) + (1);
    if (((uint8_t)(*(uint8_t *)(Arg4))) != ((uint8_t)(*(uint8_t *)(local_r10)))) goto loc_00BF0463;
    Arg3 = (uint32_t)((Arg3) + ((uint32_t)(local_r13)));
    if (condition_is_not_equal) goto loc_00BF044C;
    goto loc_00BF04A3;
loc_00BF0463:
    Arg3 = (local_rbx) - (*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x960));
loc_00BF046F:
    local_r11 = (*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x960)) + (1);
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x960) + Arg3 * 1))) != ((uint8_t)(*(uint8_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x960))))) goto loc_00BF0484;
    Arg4 = (uint32_t)((4) + ((uint32_t)(local_r13)));
    if (condition_is_not_equal) goto loc_00BF046F;
    goto loc_00BF04A3;
loc_00BF0484:
    Arg3 = (local_rbx) - (*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x968));
loc_00BF0490:
    local_r14 = (*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x968)) + (1);
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x968) + Arg3 * 1))) != ((uint8_t)(*(uint8_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x968))))) goto loc_00BF04AB;
    Arg4 = (uint32_t)((6) + ((uint32_t)(local_r13)));
    if (condition_is_not_equal) goto loc_00BF0490;
loc_00BF04A3:
    Arg3 = 0;
    goto loc_00BF03C5;
loc_00BF04AB:
    Arg3 = 0;
    goto loc_00BF03C7;
loc_00BF04B3:
    if (1 == 0) goto loc_00BF04D6;
loc_00BF04B7:
    if ((*(uint32_t *)(local_rbx)) != 0x54494E49ULL) goto loc_00BF04D6;
    if ((*(uint32_t *)(local_rbx + 0x4)) == 0x4742444BULL) {
        Arg2 = 1;
        if (((*(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x9DC)) & (0x2000ULL)) != 0) { Arg2 = 0; }
    }
    local_r12 = ((uint32_t)(Arg2) == 0) ? 1 : 0;
    v_stack_m1C0 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0xC)));
    Arg1 = (uint32_t)(*(uint32_t *)(local_rbx + 0x10));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x10)))) <= ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x8))))) { Arg1 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x8))); }
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0xC)) + 4095) + ((uint32_t)(Arg1)));
    local_r14 = (uint32_t)((local_r14) & (0xFFFFF000ULL));
    result = MmImageSectionPagable(local_rbx, (uint32_t)(*(uint32_t *)(local_rbx + 0xC)), Arg3, Arg4);
    local_r10 = 0;
    local_r11 = ((uint32_t)(result) != 0) ? 1 : 0;
    v_stack_m1E8 = (uint32_t)(local_r11);
    if (((*(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x9D8)) & (0x100000ULL)) != 0) goto loc_00BF054E;
    Arg2 = 0;
    *(uint32_t *)(local_rsp - 0x118 + 0x138) = 128;
    *(uint64_t *)(local_rsp - 0x118 - 0x30) = (uint32_t)(*(uint32_t *)(result + 0x944));
    *(uint64_t *)(local_rsp - 0x118 - 0x10) = 0;
    result = KeInitializeGate(local_rsp - 280 - 40, Arg2, Arg3, Arg4);
    local_r10 = 0;
    goto loc_00BF057E;
loc_00BF054E:
    *(uint32_t *)(local_rsp - 0x118 + 0x138) = 0;
loc_00BF0561:
    *(uint64_t *)(local_rsp - 0x118 - 0x30) = 0;
    Arg1 = (uint32_t)((120) + (-8));
    result = (local_rsp - 280 - 48) + (1 + 7);
    Arg2 = (120 - 105) - (1);
    if (condition_is_not_equal) goto loc_00BF0561;
    if ((uint32_t)(Arg1) == 0) goto loc_00BF057E;
loc_00BF0573:
    *(uint8_t *)(result) = 0;
    result = (result) + (1);
    Arg1 = (uint32_t)((Arg1) + (-1));
    if (condition_is_not_equal) goto loc_00BF0573;
loc_00BF057E:
    v_stack_m1D8 = *(uint64_t *)(local_rsp - 0x118 + 0x128);
    if (v_stack_m1E0 == v_stack_m1B8) goto loc_00BF082D;
    local_rbx = (local_rbx) + (4);
loc_00BF05A7:
    if (0 < v_stack_m1C0) goto loc_00BF0783;
    if (0 < ((uint32_t)(local_r14))) goto loc_00BF077C;
    if ((local_rbx + 36) == v_stack_m1B0) goto loc_00BF07F7;
    if (0 < (*(uint32_t *)(local_rbx + 0x30))) goto loc_00BF07F7;
    local_rbx = (local_rbx) + (40);
    if (((*(uint32_t *)(local_rbx + 0x20)) & (0x2000000ULL)) != 0) goto loc_00BF05F6;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx - 0x4)))) != 0x54494E49ULL) goto loc_00BF05FD;
    if ((*(uint32_t *)(local_rbx)) != 0x4742444BULL) goto loc_00BF0627;
loc_00BF05F6:
    goto loc_00BF0703;
loc_00BF05FD:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx - 0x4)))) != 0x45474150ULL) goto loc_00BF0627;
    if (((uint16_t)(*(uint16_t *)(local_rbx))) == ((uint16_t)((uint32_t)(0x7877ULL)))) goto loc_00BF05F6;
    if (((uint16_t)(*(uint16_t *)(local_rbx))) == ((uint16_t)((uint32_t)(0x7277ULL)))) goto loc_00BF05F6;
    if (((uint16_t)(*(uint16_t *)(local_rbx))) != ((uint16_t)((uint32_t)(0x7777ULL)))) goto loc_00BF0638;
    goto loc_00BF05F6;
loc_00BF0627:
    if (((uint32_t)(*(uint16_t *)(local_rbx))) != 0x41525245ULL) goto loc_00BF0638;
    if ((*(uint16_t *)(local_rbx)) == ((uint16_t)((uint32_t)(0x4154ULL)))) goto loc_00BF05F6;
loc_00BF0638:
    Arg4 = (local_rbx) - (*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x950));
loc_00BF0660:
    Arg3 = (*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x950)) + (1);
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x950) + Arg4 * 1 - 0x4))) != ((uint8_t)(*(uint8_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x950))))) goto loc_00BF067A;
    local_r12 = (uint32_t)((7) + (-1));
    if (condition_is_not_equal) goto loc_00BF0660;
    goto loc_00BF06FE;
loc_00BF067A:
loc_00BF0681:
    Arg4 = (local_rbx - 4) + (1 + 7);
    local_r10 = (*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x958)) + (1 + 7);
    if ((*(uint64_t *)(local_rbx - 0x4)) != (*(uint64_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x958)))) goto loc_00BF06B8;
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(1 + 7))) + (-8));
    if (Arg3 >= ((uint32_t)(1 + 7))) goto loc_00BF0681;
    if (Arg3 == 0) goto loc_00BF06FE;
loc_00BF06A0:
    Arg4 = (Arg4) + (1);
    local_r10 = (local_r10) + (1);
    if (((uint8_t)(*(uint8_t *)(Arg4))) != ((uint8_t)(*(uint8_t *)(local_r10)))) goto loc_00BF06B8;
    Arg3 = (uint32_t)((Arg3) + (-1));
    if (condition_is_not_equal) goto loc_00BF06A0;
    goto loc_00BF06FE;
loc_00BF06B8:
    Arg3 = (local_rbx) - (*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x960));
    local_r10 = (uint32_t)((local_r10) | (0xFFFFFFFFULL));
loc_00BF06C8:
    local_r11 = (*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x960)) + (1);
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x960) + Arg3 * 1 - 0x4))) != ((uint8_t)(*(uint8_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x960))))) goto loc_00BF06DE;
    Arg4 = (uint32_t)((4) + ((uint32_t)(local_r10)));
    if (condition_is_not_equal) goto loc_00BF06C8;
    goto loc_00BF06FE;
loc_00BF06DE:
    Arg3 = (local_rbx) - (*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x968));
loc_00BF06EA:
    local_r14 = (*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x968)) + (1);
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x968) + Arg3 * 1 - 0x4))) != ((uint8_t)(*(uint8_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x968))))) goto loc_00BF0700;
    Arg4 = (uint32_t)((6) + ((uint32_t)(local_r10)));
    if (condition_is_not_equal) goto loc_00BF06EA;
loc_00BF06FE:
loc_00BF0700:
    local_r10 = 0;
loc_00BF0703:
    if ((*(uint32_t *)(local_rbx + 0x20)) >= 0) goto loc_00BF070D;
    goto loc_00BF0711;
loc_00BF070D:
    if (1 == 0) goto loc_00BF0730;
loc_00BF0711:
    if ((*(uint32_t *)(local_rbx - 0x4)) != 0x54494E49ULL) goto loc_00BF0730;
    if ((*(uint32_t *)(local_rbx)) == 0x4742444BULL) {
        Arg2 = 1;
        if (((*(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x9DC)) & (0x2000ULL)) != 0) { Arg2 = 0; }
    }
    local_r12 = ((uint32_t)(Arg2) == 0) ? 1 : 0;
    Arg1 = (uint32_t)(*(uint32_t *)(local_rbx + 0xC));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0xC)))) <= ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x4))))) { Arg1 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x4))); }
    Arg1 = (uint32_t)((Arg1) + (0xFFFULL));
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0x8))) + ((uint32_t)(Arg1)));
    local_r14 = (uint32_t)((local_r14) & (0xFFFFF000ULL));
    result = MmImageSectionPagable(local_rbx - 4, Arg2, Arg3, Arg4);
    local_r10 = 0;
    local_r11 = ((uint32_t)(result) != 0) ? 1 : 0;
loc_00BF077C:
    if ((uint32_t)(local_r12) == 0) goto loc_00BF07FC;
    goto loc_00BF078A;
loc_00BF0783:
    if (0 >= v_stack_m1C4) goto loc_00BF07FC;
loc_00BF078A:
loc_00BF0797:
    if ((uint32_t)(*(uint32_t *)(v_stack_m1C8)) == 0) goto loc_00BF07BF;
    local_r10 = ((uint32_t)(*(uint32_t *)(v_stack_m1C8)) - 1) + (*(uint64_t *)(v_stack_m1A0));
    if (v_stack_m1D8 < (*(uint64_t *)(v_stack_m1A0))) goto loc_00BF07BC;
    if (v_stack_m1D8 <= local_r10) goto loc_00BF0845;
loc_00BF07BC:
    local_r10 = 0;
loc_00BF07BF:
    Arg2 = (uint32_t)((0) + (1));
    Arg1 = (v_stack_m1C8) + (4);
    result = (v_stack_m1A0) + (1 + 7);
    if (((uint32_t)(Arg2)) < 1) goto loc_00BF0797;
    if (0 < v_stack_m1C0) goto loc_00BF07D8;
    if ((uint32_t)(local_r11) != 0) goto loc_00BF07E4;
loc_00BF07D8:
    goto loc_00BF07E9;
loc_00BF07E4:
loc_00BF07E9:
loc_00BF07F7:
loc_00BF07FC:
    result = (v_stack_m1D8) + (0x1000ULL);
    Arg1 = (v_stack_m1E0) + (20);
    local_r13 = (uint32_t)((0) + (0x1000ULL));
    v_stack_m1D8 = result;
    v_stack_m1E0 = Arg1;
    if (Arg1 != v_stack_m1B8) goto loc_00BF05A7;
loc_00BF082D:
    local_r13 = (v_stack_m1D0) + (48);
    goto loc_00BF0E5B;
loc_00BF0845:
    goto loc_00BF07FC;
loc_00BF0854:
loc_00BF085A:
    if ((*(uint8_t *)(local_r13 + 0xF)) < 0) goto loc_00BF0877;
    local_r14 = (uint32_t)((0) + (1));
    result = (local_r14 + local_r14 * 4 * 4) + (local_r13);
    if (result != v_stack_m1B8) goto loc_00BF085A;
loc_00BF0877:
    v_stack_m1E8 = (uint32_t)(local_r14);
    if ((uint32_t)(local_r14) == 0) goto loc_00BF0E12;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x118 + 0x138))) != 0) goto loc_00BF0AC3;
    v_stack_m1D8 = local_r13;
    *(uint64_t *)(local_rsp - 0x118 - 0x58) = *(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0xAD0);
    v_stack_m1C4 = (uint32_t)((uint32_t)((uint32_t)(local_r14)));
    v_stack_m1E0 = *(uint64_t *)(local_rsp - 0x118 + 0x128);
loc_00BF08AF:
    local_rbx = (uint32_t)((uint32_t)(1 + 7));
    if (((uint32_t)((uint32_t)((uint32_t)(local_r14)))) < ((uint32_t)(1 + 7))) { local_rbx = (uint32_t)((uint32_t)((uint32_t)(local_r14))); }
    if ((uint32_t)(local_rbx) == 0) goto loc_00BF09D8;
    v_stack_m1D0 = local_rsp - 280 + 104;
loc_00BF08D4:
    *(uint64_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0xAD0) + 0x8) = 0x1000ULL;
    local_r11 = (uint32_t)((0) << (12));
    local_r11 = (local_r11) + (v_stack_m1E0);
    *(uint64_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0xAD0)) = local_r11;
    v_stack_m1C0 = *(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x838);
    if (local_r11 >= (local_r11 + 4096)) goto loc_00BF0925;
loc_00BF0919:
    result = (local_r11) + (64);
    if (result < (local_r11 + 4096)) goto loc_00BF0919;
loc_00BF0925:
    v_stack_m1C0 = 32;
loc_00BF093F:
loc_00BF0942:
    Arg3 = (v_stack_m1C0) ^ (*(uint64_t *)(local_r11));
    local_r10 = (local_r11) + (1 + 7);
    Arg3 = (Arg3) ^ (*(uint64_t *)(local_r10));
    local_r10 = (local_r10) + (1 + 7);
    result = (1 + 7) - (1);
    if (condition_is_not_equal) goto loc_00BF0942;
    Arg1 = (local_r10) - (local_r11);
    Arg1 = (Arg1) ^ (v_stack_m1C0);
    Arg1 = (Arg1) ^ (Arg1);
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x834))) ^ ((uint32_t)(*(uint64_t *)(local_rsp - 0x118 + 0x128))));
    *(uint64_t *)(local_rsp - 0x118 + 0x50) = *(uint64_t *)(local_rsp - 0x118 + 0x128);
    Arg4 = (uint32_t)((Arg4) ^ ((uint32_t)(v_stack_m1E0)));
    Arg4 = (uint32_t)((Arg4) & (63));
    if (condition_is_equal) { Arg4 = 1; }
    if (condition_is_not_equal) goto loc_00BF093F;
    goto loc_00BF09A0;
loc_00BF099D:
    Arg3 = (uint32_t)((Arg3) ^ (Arg3));
loc_00BF09A0:
    result = (Arg3) >> (31);
    if (result != 0) goto loc_00BF099D;
    local_r12 = (uint32_t)((0) + (1));
    local_r13 = (*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0xAD0)) + (48);
    *(uint32_t *)(v_stack_m1D0) = Arg3;
    Arg2 = (v_stack_m1D0) + (4);
    v_stack_m1D0 = Arg2;
    if (((uint32_t)(local_r12)) < ((uint32_t)(local_rbx))) goto loc_00BF08D4;
loc_00BF09D8:
    result = sub_0051AFB0(v_stack_m1A8, *(uint64_t *)(local_rsp - 0x118 - 0x58), (uint32_t)((uint32_t)(local_rbx)), Arg4);
    local_r10 = 0;
    if ((uint32_t)(local_rbx) == 0) goto loc_00BF0A77;
    v_stack_m1D0 = (uint32_t)((uint32_t)(local_rbx));
loc_00BF0A07:
loc_00BF0A17:
    Arg3 = (uint32_t)((16) + (-8));
    *(uint64_t *)(v_stack_m1D8) = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x118 - 0x58) + 0x10);
    Arg1 = (*(uint64_t *)(local_rsp - 0x118 - 0x58) + 16) + (1 + 7);
    Arg2 = (v_stack_m1D8) + (1 + 7);
    local_r13 = (16 - 14) - (1);
    if (condition_is_not_equal) goto loc_00BF0A17;
    if (Arg3 == 0) goto loc_00BF0A41;
loc_00BF0A31:
    Arg1 = (Arg1) + (1);
    *(uint8_t *)(Arg2) = (uint8_t)(*(uint8_t *)(arg1));
    Arg2 = (Arg2) + (1);
    Arg3 = (uint32_t)((Arg3) + (-1));
    if (condition_is_not_equal) goto loc_00BF0A31;
loc_00BF0A41:
    local_r11 = (*(uint64_t *)(local_rsp - 0x118 - 0x58) + 16) + (48);
    local_r10 = (v_stack_m1D8) + (20);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1D8 + 0x10))))) ^ (*(uint32_t *)(local_rsp - 0x118 + 0x68)));
    local_r12 = (local_rsp - 280 + 104) + (4);
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1D8 + 0x10)))));
    *(uint32_t *)(v_stack_m1D8 + 0x10) = (uint32_t)(Arg1);
    Arg4 = (v_stack_m1D8 + 16) + (20);
    if (condition_is_not_equal) goto loc_00BF0A07;
    local_r10 = 0;
loc_00BF0A77:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) << (12));
    result = (uint32_t)(((uint32_t)(v_stack_m1C4)) - ((uint32_t)(local_rbx)));
    v_stack_m1D8 = v_stack_m1D8 + local_rbx + local_rbx * 4 * 4;
    local_rbx = (uint32_t)((local_rbx) << (15));
    v_stack_m1C4 = (uint32_t)(result);
    if ((uint32_t)(result) != 0) goto loc_00BF08AF;
    goto loc_00BF0E0D;
loc_00BF0AC3:
    if ((uint32_t)((uint32_t)(v_stack_m1E8)) == 0) goto loc_00BF0E12;
loc_00BF0ACF:
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m1E8)))) - (0));
    if (((uint32_t)(local_r12)) > ((uint32_t)(result))) { local_r12 = (uint32_t)(result); }
    result = KeGuardDispatchICall(64, *(uint64_t *)(v_stack_m1A8 + 0xAD8), (uint32_t)(*(uint32_t *)(v_stack_m1A8 + 0x830)), Arg4);
    v_stack_m1D0 = result;
    Arg2 = (*(uint64_t *)(v_stack_m1A8 + 0xAD8)) << (32);
    result = (result) | (Arg2);
    Arg2 = (result) ^ (result);
    *(uint64_t *)(local_rsp - 0x118 + 0x58) = Arg2;
    Arg1 = (Arg2) ^ (local_rbx);
    Arg2 = (Arg2) >> (1);
    result = (local_rbx) * (Arg2);
    Arg1 = (Arg1) - (result);
    if (((uint32_t)(Arg1)) > 5) goto loc_00BF0BD3;
    if (((uint32_t)(Arg1)) == 5) goto loc_00BF0BBF;
    if ((uint32_t)(Arg1) == 0) goto loc_00BF0BAB;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00BF0B98;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00BF0B84;
    if (((uint32_t)(Arg1)) == 1) goto loc_00BF0B6C;
    *(uint32_t *)(local_rsp - 0x118 - 0x80) = 0x67076494ULL;
    goto loc_00BF0CE1;
loc_00BF0B6C:
    *(uint32_t *)(local_rsp - 0x118 - 0x7C) = 0xA8223938ULL;
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x118 - 0x7C))) ^ (3));
    goto loc_00BF0CE1;
loc_00BF0B84:
    *(uint32_t *)(local_rsp - 0x118 - 0x78) = 0x85B5910DULL;
    goto loc_00BF0CE1;
loc_00BF0B98:
    *(uint32_t *)(local_rsp - 0x118 - 0x74) = 0xB2AD31A1ULL;
    goto loc_00BF0CE1;
loc_00BF0BAB:
    *(uint32_t *)(local_rsp - 0x118 - 0x70) = 0xD098D0D8ULL;
    goto loc_00BF0CE1;
loc_00BF0BBF:
    *(uint32_t *)(local_rsp - 0x118 - 0x6C) = 0x288C49EDULL;
    goto loc_00BF0CE1;
loc_00BF0BD3:
    Arg1 = (uint32_t)((Arg1) - (6));
    if (condition_is_equal) goto loc_00BF0CCF;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00BF0CBE;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00BF0CAD;
    if (((uint32_t)(Arg1)) == 1) goto loc_00BF0C98;
    Arg2 = (6) << (32);
    result = (result) | (Arg2);
    Arg2 = (result) ^ (result);
    *(uint64_t *)(local_rsp - 0x118 + 0x60) = Arg2;
    Arg4 = (uint32_t)((Arg2) ^ ((uint32_t)(local_rbx)));
    Arg4 = (uint32_t)((Arg4) >> (5));
    Arg2 = (uint32_t)((Arg2) >> (3));
    result = (uint32_t)(((uint32_t)(0x4EC4EC4FULL)) * ((uint32_t)(Arg2)));
    Arg1 = (uint32_t)(((uint32_t)(Arg4)) - ((uint32_t)(result)));
    Arg1 = (uint32_t)((Arg1) + (97));
    Arg4 = (uint32_t)((Arg4) >> (5));
    Arg1 = (uint32_t)((Arg1) << (8));
    Arg2 = (uint32_t)((Arg2) >> (3));
    result = (uint32_t)(((uint32_t)(0x4EC4EC4FULL)) * ((uint32_t)(Arg2)));
    Arg3 = (uint32_t)(((uint32_t)(Arg4)) - ((uint32_t)(result)));
    Arg3 = (uint32_t)((Arg3) + (65));
    Arg3 = (uint32_t)((Arg3) | ((uint32_t)(Arg1)));
    Arg2 = (uint32_t)((Arg2) >> (3));
    result = (uint32_t)(((uint32_t)(0x4EC4EC4FULL)) * ((uint32_t)(Arg2)));
    Arg4 = (uint32_t)((Arg4) >> (5));
    Arg3 = (uint32_t)((Arg3) << (8));
    Arg1 = (uint32_t)(((uint32_t)(Arg4)) - ((uint32_t)(result)));
    Arg1 = (uint32_t)((Arg1) + (97));
    Arg2 = (uint32_t)((Arg2) >> (3));
    Arg1 = (uint32_t)((Arg1) | (Arg3));
    result = (uint32_t)(((uint32_t)(0x4EC4EC4FULL)) * ((uint32_t)(Arg2)));
    Arg1 = (uint32_t)((Arg1) << (8));
    Arg4 = (uint32_t)((Arg4) - ((uint32_t)(result)));
    Arg4 = (uint32_t)((Arg4) + (65));
    Arg4 = (uint32_t)((Arg4) | ((uint32_t)(Arg1)));
    goto loc_00BF0CE1;
loc_00BF0C98:
    *(uint32_t *)(local_rsp - 0x118 - 0x68) = 0xB0869E85ULL;
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x118 - 0x68))) ^ (9));
    goto loc_00BF0CE1;
loc_00BF0CAD:
    *(uint32_t *)(local_rsp - 0x118 - 0x64) = 0x64664142ULL;
    goto loc_00BF0CE1;
loc_00BF0CBE:
    *(uint32_t *)(local_rsp - 0x118 - 0x60) = 0x82C6A6D8ULL;
    goto loc_00BF0CE1;
loc_00BF0CCF:
    *(uint32_t *)(local_rsp - 0x118 - 0x5C) = 0x4E574672ULL;
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x118 - 0x5C))) ^ ((uint32_t)(Arg2)));
loc_00BF0CE1:
    result = KeGuardDispatchICall(80 - 16, 80, (uint32_t)(Arg4), Arg4);
    Arg2 = 0;
    local_rbx = local_rsp - 280 - 8;
    if (result != 0) { local_rbx = result; }
    Arg1 = (uint32_t)((0) << (12));
    Arg1 = (Arg1) + (*(uint64_t *)(local_rsp - 0x118 + 0x128));
    *(uint64_t *)(local_rbx) = local_rsp - 280 - 48;
    *(uint64_t *)(local_rbx + 0x8) = v_stack_m1D0;
    *(void **)(local_rbx + 0x10) = Arg1;
    *(uint32_t *)(local_rbx + 0x20) = (uint32_t)(local_r12);
    *(uint32_t *)(local_rbx + 0x28) = 1;
    *(uint64_t *)(local_rbx + 0x48) = local_rbx;
    *(uint64_t *)(local_rbx + 0x30) = 0;
    result = (0 + 0 * 4 * 4) + (v_stack_m1B0);
    *(uint64_t *)(local_rbx + 0x18) = result;
    *(uint64_t *)(local_rbx + 0x40) = v_rip + 1342;
    result = (uint32_t)((1) + (1));
    if (((uint32_t)(result)) != 1) goto loc_00BF0D74;
    if ((*(uint32_t *)(local_rsp - 0x118 - 0xC)) != 0) {
        Arg3 = 0;
        Arg1 = local_rsp - 280 - 40;
        result = KeWaitForGate(Arg1, Arg2, Arg3, Arg4);
    }
    Arg2 = 0;
    *(uint32_t *)(local_rsp - 0x118 - 0xC) = 1;
    result = ExQueueWorkItem(local_rbx + 48, Arg2, Arg3, Arg4);
    local_r10 = 0;
    if (local_rbx != (local_rsp - 280 - 8)) goto loc_00BF0DB9;
    if ((*(uint32_t *)(local_rsp - 0x118 - 0xC)) == 0) goto loc_00BF0DB9;
    local_rsi = 0;
loc_00BF0D96:
    Arg3 = 0;
    Arg2 = 0;
    result = KeWaitForGate(local_rsp - 280 - 40, Arg2, Arg3, Arg4);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x118 - 0x10))) != 0) goto loc_00BF0D96;
    *(uint32_t *)(local_rsp - 0x118 - 0xC) = 0;
    local_r10 = 0;
loc_00BF0DB9:
    if (v_stack_m1D0 != 0) goto loc_00BF0DEB;
    if ((*(uint32_t *)(local_rsp - 0x118 - 0xC)) == 0) goto loc_00BF0DEB;
    local_rsi = 0;
loc_00BF0DC8:
    Arg3 = 0;
    Arg2 = 0;
    result = KeWaitForGate(local_rsp - 280 - 40, Arg2, Arg3, Arg4);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x118 - 0x10))) != 0) goto loc_00BF0DC8;
    *(uint32_t *)(local_rsp - 0x118 - 0xC) = 0;
    local_r10 = 0;
loc_00BF0DEB:
    local_r15 = (uint32_t)((0) + ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x118 + 0x138)))));
    if (((uint32_t)(local_r15)) < ((uint32_t)((uint32_t)(v_stack_m1E8)))) goto loc_00BF0ACF;
loc_00BF0E0D:
loc_00BF0E12:
    goto loc_00BF0E28;
loc_00BF0E1B:
    if ((*(uint8_t *)((uint32_t)((uint32_t)((uint32_t)(v_stack_m1E8))) + 0xF)) >= 0) goto loc_00BF0E38;
    local_r14 = (uint32_t)(((uint32_t)(v_stack_m1E8)) + (1));
loc_00BF0E28:
    result = (local_r14 + local_r14 * 4 * 4) + (v_stack_m1B0);
    if (result != v_stack_m1B8) goto loc_00BF0E1B;
loc_00BF0E38:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) << (12));
    Arg2 = (*(uint64_t *)(local_rsp - 0x118 + 0x128)) + (result);
    *(uint64_t *)(local_rsp - 0x118 + 0x128) = Arg2;
loc_00BF0E5B:
    v_stack_m1B0 = v_stack_m1B0 + (uint32_t)((uint32_t)(local_r14)) + (uint32_t)((uint32_t)(local_r14)) * 4 * 4;
    if ((v_stack_m1B0 + (uint32_t)((uint32_t)(local_r14)) + (uint32_t)((uint32_t)(local_r14)) * 4 * 4) != v_stack_m1B8) goto loc_00BF0854;
    if ((*(uint32_t *)(local_rsp - 0x118 + 0x138)) == 0) goto loc_00BF0E97;
    if ((*(uint32_t *)(local_rsp - 0x118 - 0xC)) == 0) goto loc_00BF0E97;
loc_00BF0E78:
    Arg3 = 0;
    Arg2 = 0;
    result = KeWaitForGate(local_rsp - 280 - 40, Arg2, Arg3, Arg4);
    local_r10 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x118 - 0x10))) != 0) goto loc_00BF0E78;
    *(uint32_t *)(local_rsp - 0x118 - 0xC) = 0;
loc_00BF0E97:
    if (((*(uint8_t *)(local_rsp - 0x118 + 0x130)) & (1)) == 0) goto loc_00BF1113;
    if ((uint32_t)((uint32_t)(v_stack_m1C8)) == 0) goto loc_00BF1113;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1A8 + 0x804)) + 48)) <= (*(uint32_t *)(v_stack_m1A8 + 0xA64))) goto loc_00BF0FA3;
    result = sub_00BE7AF8(v_stack_m1A8, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1A8 + 0x804)) + 48)), (uint32_t)(*(uint32_t *)(v_stack_m1A8 + 0x944)), Arg4);
    local_r10 = 0;
    if (result != 0) goto loc_00BF0EEF;
loc_00BF0EE5:
    goto loc_00BF1244;
loc_00BF0EEF:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m1A8 + 0x9D8)))) & (2)) != 0) goto loc_00BF0F9A;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m1A8 + 0x9D8))) & (0x10000000ULL));
    Arg1 = (uint32_t)(-(Arg1));
    Arg1 = (uint32_t)((Arg1) & (*(uint32_t *)(v_stack_m1A8 + 0x944)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1A8 + 0x804)))) < 8) goto loc_00BF0F34;
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1A8 + 0x804))))) >> (3);
loc_00BF0F26:
    *(uint64_t *)(v_stack_m1A8) = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m1A8 + 0x804))) + (-8));
    local_rsi = (v_stack_m1A8) + (8);
    Arg2 = (Arg2) - (1);
    if (condition_is_not_equal) goto loc_00BF0F26;
loc_00BF0F34:
    if ((uint32_t)(result) == 0) goto loc_00BF0F43;
loc_00BF0F38:
    *(uint8_t *)(local_rsi) = 0;
    local_rsi = (local_rsi) + (1);
    result = (uint32_t)((result) + (-1));
    if (condition_is_not_equal) goto loc_00BF0F38;
loc_00BF0F43:
    *(uint32_t *)(result + 0x944) = (uint32_t)(Arg1);
    if (((uint32_t)(Arg1)) == 3) goto loc_00BF0F82;
    if (((*(uint32_t *)(result + 0x9D8)) & (0x8000000ULL)) != 0) goto loc_00BF0F79;
    if ((uint32_t)(Arg1) == 0) goto loc_00BF0F79;
    result = KeGuardDispatchICall(*(uint64_t *)(v_stack_m1A8 + 0x7E8) - 8, *(uint64_t *)(*(uint64_t *)(v_stack_m1A8 + 0x7E8) - 0x8), *(uint64_t *)(v_stack_m1A8 + 0x7E8), Arg4);
    goto loc_00BF0F91;
loc_00BF0F79:
    goto loc_00BF0F89;
loc_00BF0F82:
loc_00BF0F89:
    result = KeGuardDispatchICall(*(uint64_t *)(v_stack_m1A8 + 0x7E8), *(uint64_t *)(*(uint64_t *)(v_stack_m1A8 + 0x7E8) - 0x8), *(uint64_t *)(v_stack_m1A8 + 0x7E8), Arg4);
loc_00BF0F91:
    *(uint32_t *)(result + 0x944) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x944)));
    local_r10 = 0;
loc_00BF0F9A:
    goto loc_00BF0FAC;
loc_00BF0FA3:
    *(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x804) = (uint32_t)(result);
loc_00BF0FAC:
loc_00BF0FC1:
    *(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + (uint32_t)(*(uint32_t *)(v_stack_m1A8 + 0x804)) * 1) = 0;
    Arg1 = (uint32_t)((48) + (-8));
    result = ((uint32_t)(*(uint32_t *)(result + 0x944)) + (uint32_t)(*(uint32_t *)(v_stack_m1A8 + 0x804)) * 1) + (8);
    Arg2 = (48 - 42) - (1);
    if (condition_is_not_equal) goto loc_00BF0FC1;
    if ((uint32_t)(Arg1) == 0) goto loc_00BF0FDE;
loc_00BF0FD3:
    *(uint8_t *)(result) = 0;
    result = (result) + (1);
    Arg1 = (uint32_t)((Arg1) + (-1));
    if (condition_is_not_equal) goto loc_00BF0FD3;
loc_00BF0FDE:
    *(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + (uint32_t)(*(uint32_t *)(v_stack_m1A8 + 0x804)) * 1) = 13;
    *(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + (uint32_t)(*(uint32_t *)(v_stack_m1A8 + 0x804)) * 1 + 0x8) = v_stack_m1A0;
    *(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + (uint32_t)(*(uint32_t *)(v_stack_m1A8 + 0x804)) * 1 + 0x10) = (uint32_t)((uint32_t)(v_stack_m1C8));
    if (v_stack_m1A0 >= (v_stack_m1A0 + (uint32_t)(v_stack_m1C8) * 1)) goto loc_00BF101E;
loc_00BF1012:
    result = (v_stack_m1A0) + (64);
    if (result < (v_stack_m1A0 + (uint32_t)(v_stack_m1C8) * 1)) goto loc_00BF1012;
loc_00BF101E:
    local_r11 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m1C8)))) >> (7));
    if ((uint32_t)(local_r11) == 0) goto loc_00BF1082;
loc_00BF1037:
loc_00BF103A:
    Arg3 = (*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x838)) ^ (*(uint64_t *)(v_stack_m1A0));
    Arg4 = (v_stack_m1A0) + (8);
    Arg3 = (Arg3) ^ (*(uint64_t *)(Arg4));
    Arg4 = (Arg4) + (8);
    result = (8) - (1);
    if (condition_is_not_equal) goto loc_00BF103A;
    Arg1 = (Arg4) - (v_stack_m1A0);
    Arg1 = (Arg1) ^ (*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x838));
    Arg1 = (Arg1) ^ (Arg1);
    Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1A8 + 0x804)))));
    local_r10 = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x834))) ^ ((uint32_t)(Arg2)));
    local_r10 = (uint32_t)((local_r10) & (63));
    if (condition_is_equal) { local_r10 = 1; }
    local_r11 = (uint32_t)((local_r11) + (-1));
    if (condition_is_not_equal) goto loc_00BF1037;
loc_00BF1082:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m1C8)))) & (127));
    if (((uint32_t)(Arg2)) < 8) goto loc_00BF10A7;
    result = ((uint32_t)((uint32_t)(Arg2))) >> (3);
loc_00BF1093:
    Arg3 = (Arg3) ^ (*(uint64_t *)(Arg4));
    Arg4 = (Arg4) + (8);
    Arg2 = (uint32_t)((Arg2) + (-8));
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_00BF1093;
loc_00BF10A7:
    if ((uint32_t)(Arg2) == 0) goto loc_00BF10C0;
loc_00BF10AB:
    Arg3 = (Arg3) ^ (*(uint8_t *)(Arg4));
    Arg4 = (Arg4) + (1);
    Arg2 = (uint32_t)((Arg2) + (-1));
    if (condition_is_not_equal) goto loc_00BF10AB;
loc_00BF10C0:
    goto loc_00BF10C8;
loc_00BF10C5:
    Arg3 = (uint32_t)((Arg3) ^ (Arg3));
loc_00BF10C8:
    result = (Arg3) >> (31);
    if (result != 0) goto loc_00BF10C5;
    *(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + (uint32_t)(*(uint32_t *)(v_stack_m1A8 + 0x804)) * 1 + 0x14) = Arg3;
    if (((*(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x9D8)) & (0x20000000ULL)) == 0) goto loc_00BF1106;
    if ((uint32_t)((uint32_t)(v_stack_m1C8)) != 0) {
        Arg2 = v_stack_m1A0;
        Arg4 = (uint32_t)(*(uint32_t *)(result + 0x944)) + (uint32_t)(*(uint32_t *)(v_stack_m1A8 + 0x804)) * 1 + 28;
        Arg3 = (uint32_t)((uint32_t)(v_stack_m1C8));
        Arg1 = (uint32_t)(*(uint32_t *)(result + 0x944));
        result = sub_0051AF4C(Arg1, Arg2, Arg3, Arg4);
    }
    *(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + (uint32_t)(*(uint32_t *)(v_stack_m1A8 + 0x804)) * 1 + 0x18) = 1;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x118 + 0x120)) = (uint32_t)(*(uint32_t *)(result + 0x944));
loc_00BF1113:
    result = 0;
    goto loc_00BF1244;
loc_00BF111A:
    if (condition_is_above_or_equal) goto loc_00BF1259;
    if ((*(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x918)) != 8) goto loc_00BF123F;
    *(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x928) = 8;
    result = (result) + ((uint32_t)(*(uint32_t *)(result + 0x944)));
    *(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x930) = 271;
    *(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x920) = result;
    *(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x938) = (uint32_t)(v_stack_m1C8);
    *(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x918) = 1;
    if (condition_is_below) goto loc_00BF123F;
    if (((*(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x9DC)) & (0x200000ULL)) == 0) goto loc_00BF123F;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x9D8))))) == 0) goto loc_00BF123F;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x804))) - ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0xA74)))));
    Arg1 = ((uint32_t)((uint32_t)(result))) >> (3);
    if (((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0xA74)) + (uint32_t)(*(uint32_t *)(result + 0x944)) * 1) == ((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0xA74)) + (uint32_t)(*(uint32_t *)(result + 0x944)) * 1 + Arg1 * 8)) goto loc_00BF11ED;
loc_00BF11C5:
    Arg2 = ((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0xA74)) + (uint32_t)(*(uint32_t *)(result + 0x944)) * 1) + (1 + 7);
    result = (*(uint64_t *)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0xA74)) + (uint32_t)(*(uint32_t *)(result + 0x944)) * 1)) ^ (*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x838));
    Arg1 = (uint32_t)(((uint8_t)(*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0xA78))) & (63));
    Arg3 = (*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0xA78)) + (result);
    Arg3 = (Arg3) ^ (0xEFAULL);
    if (Arg2 != ((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0xA74)) + (uint32_t)(*(uint32_t *)(result + 0x944)) * 1 + Arg1 * 8)) goto loc_00BF11C5;
    local_r15 = 0;
loc_00BF11ED:
    if (Arg3 == (*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0xA80))) goto loc_00BF123F;
    *(uint64_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x588)) = (uint32_t)(*(uint32_t *)(result + 0x944));
    *(uint32_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x588) + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x804)));
    result = *(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x588);
    if ((*(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x918)) == 0) {
        result = *(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x588);
        Arg1 = (*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0xA80)) ^ (Arg3);
        *(void **)(result + 0x18) = Arg1;
    }
    Arg2 = 0;
    result = sub_00BE8384((uint32_t)(*(uint32_t *)(result + 0x944)), Arg2, Arg3, 256);
loc_00BF123F:
loc_00BF1244:
    local_rsp = (local_rsp) + (472);
    return (uint32_t)(0xC000007BULL);
loc_00BF1259:
    *(uint32_t *)(local_rsp - 0x118 + 0x120) = 0xE8000009ULL;
    v_stack_p20 = 0;
    result = KeBugCheckEx((uint32_t)(*(uint32_t *)(local_rsp - 0x118 + 0x120)), 4 + 6, (uint32_t)(v_stack_m1C8), 4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00BEFF8C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
