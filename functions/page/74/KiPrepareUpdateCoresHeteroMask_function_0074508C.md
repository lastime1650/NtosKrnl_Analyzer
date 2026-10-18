# KiPrepareUpdateCoresHeteroMask

- RVA: `0x0074508C`–`0x007455FB` (길이 `1,391` bytes)
- VA: `0x000000014074508C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BDC68`
- 디코드: `347`개 명령, `1,391/1,391` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **30**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00745132` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00745148` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x007451AC` → [KeAddProcessorAffinityEx](../../text/25/KeAddProcessorAffinityEx_function_0025B6F0.md) (function, `0x0025B6F0`)
- `0x007451F3` → [KeAddProcessorAffinityEx](../../text/25/KeAddProcessorAffinityEx_function_0025B6F0.md) (function, `0x0025B6F0`)
- `0x0074521C` → [KeAddProcessorAffinityEx](../../text/25/KeAddProcessorAffinityEx_function_0025B6F0.md) (function, `0x0025B6F0`)
- `0x00745282` → [KeIsEmptyAffinityEx](../../text/2D/KeIsEmptyAffinityEx_function_002D1580.md) (function, `0x002D1580`)
- `0x00745299` → [KiCopyAffinityEx](../../text/2C/KiCopyAffinityEx_function_002CE860.md) (function, `0x002CE860`)
- `0x007452C0` → [KeEnumerateNextProcessor](../../text/41/KeEnumerateNextProcessor_function_00415480.md) (function, `0x00415480`)
- `0x00745301` → [KeEnumerateNextProcessor](../../text/41/KeEnumerateNextProcessor_function_00415480.md) (function, `0x00415480`)
- `0x00745328` → [KeEnumerateNextProcessor](../../text/41/KeEnumerateNextProcessor_function_00415480.md) (function, `0x00415480`)
- `0x0074535F` → [KeAddProcessorAffinityEx](../../text/25/KeAddProcessorAffinityEx_function_0025B6F0.md) (function, `0x0025B6F0`)
- `0x00745377` → [KeAddProcessorAffinityEx](../../text/25/KeAddProcessorAffinityEx_function_0025B6F0.md) (function, `0x0025B6F0`)
- `0x00745388` → [KeAddProcessorAffinityEx](../../text/25/KeAddProcessorAffinityEx_function_0025B6F0.md) (function, `0x0025B6F0`)
- `0x00745397` → [KeEnumerateNextProcessor](../../text/41/KeEnumerateNextProcessor_function_00415480.md) (function, `0x00415480`)
- `0x007453A8` → [KeIsEmptyAffinityEx](../../text/2D/KeIsEmptyAffinityEx_function_002D1580.md) (function, `0x002D1580`)
- `0x007453BE` → [KiCopyAffinityEx](../../text/2C/KiCopyAffinityEx_function_002CE860.md) (function, `0x002CE860`)
- `0x007453E4` → [KeEnumerateNextProcessor](../../text/41/KeEnumerateNextProcessor_function_00415480.md) (function, `0x00415480`)
- `0x00745425` → [KeEnumerateNextProcessor](../../text/41/KeEnumerateNextProcessor_function_00415480.md) (function, `0x00415480`)
- `0x00745452` → [KeEnumerateNextProcessor](../../text/41/KeEnumerateNextProcessor_function_00415480.md) (function, `0x00415480`)
- `0x0074548F` → [KeAddProcessorAffinityEx](../../text/25/KeAddProcessorAffinityEx_function_0025B6F0.md) (function, `0x0025B6F0`)
- `0x007454A1` → [KeAddProcessorAffinityEx](../../text/25/KeAddProcessorAffinityEx_function_0025B6F0.md) (function, `0x0025B6F0`)
- `0x007454BC` → [KeAddProcessorAffinityEx](../../text/25/KeAddProcessorAffinityEx_function_0025B6F0.md) (function, `0x0025B6F0`)
- `0x007454C8` → [KeAddProcessorAffinityEx](../../text/25/KeAddProcessorAffinityEx_function_0025B6F0.md) (function, `0x0025B6F0`)
- `0x007454D7` → [KeEnumerateNextProcessor](../../text/41/KeEnumerateNextProcessor_function_00415480.md) (function, `0x00415480`)
- `0x00745537` → [KiCopyAffinityEx](../../text/2C/KiCopyAffinityEx_function_002CE860.md) (function, `0x002CE860`)
- `0x00745557` → [KiCopyAffinityEx](../../text/2C/KiCopyAffinityEx_function_002CE860.md) (function, `0x002CE860`)
- `0x0074558C` → [KiCopyAffinityEx](../../text/2C/KiCopyAffinityEx_function_002CE860.md) (function, `0x002CE860`)
- `0x007455AC` → [KiCopyAffinityEx](../../text/2C/KiCopyAffinityEx_function_002CE860.md) (function, `0x002CE860`)
- `0x007455CB` → [KiCopyAffinityEx](../../text/2C/KiCopyAffinityEx_function_002CE860.md) (function, `0x002CE860`)
- `0x007455DA` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [KiConfigureHeteroMultiCoreProcessors](../AA/KiConfigureHeteroMultiCoreProcessors_function_00AA7938.md) at `0x00AA7C09`

### Static image references
- `0x007450AB` → RVA `0x00E0A740` (`.data`; read)
- `0x00745156` → RVA `0x00FC6A80` (`ALMOSTRO`; read)
- `0x007451C5` → RVA `0x00000000` (`image boundary/outside`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **30**
  - `0x00745132` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00745148` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x007451AC` → [KeAddProcessorAffinityEx](../../text/25/KeAddProcessorAffinityEx_function_0025B6F0.md) (`PAGE` → `.text`)
  - `0x007451F3` → [KeAddProcessorAffinityEx](../../text/25/KeAddProcessorAffinityEx_function_0025B6F0.md) (`PAGE` → `.text`)
  - `0x0074521C` → [KeAddProcessorAffinityEx](../../text/25/KeAddProcessorAffinityEx_function_0025B6F0.md) (`PAGE` → `.text`)
  - `0x00745282` → [KeIsEmptyAffinityEx](../../text/2D/KeIsEmptyAffinityEx_function_002D1580.md) (`PAGE` → `.text`)
  - `0x00745299` → [KiCopyAffinityEx](../../text/2C/KiCopyAffinityEx_function_002CE860.md) (`PAGE` → `.text`)
  - `0x007452C0` → [KeEnumerateNextProcessor](../../text/41/KeEnumerateNextProcessor_function_00415480.md) (`PAGE` → `.text`)
  - `0x00745301` → [KeEnumerateNextProcessor](../../text/41/KeEnumerateNextProcessor_function_00415480.md) (`PAGE` → `.text`)
  - `0x00745328` → [KeEnumerateNextProcessor](../../text/41/KeEnumerateNextProcessor_function_00415480.md) (`PAGE` → `.text`)
  - `0x0074535F` → [KeAddProcessorAffinityEx](../../text/25/KeAddProcessorAffinityEx_function_0025B6F0.md) (`PAGE` → `.text`)
  - `0x00745377` → [KeAddProcessorAffinityEx](../../text/25/KeAddProcessorAffinityEx_function_0025B6F0.md) (`PAGE` → `.text`)
  - `0x00745388` → [KeAddProcessorAffinityEx](../../text/25/KeAddProcessorAffinityEx_function_0025B6F0.md) (`PAGE` → `.text`)
  - `0x00745397` → [KeEnumerateNextProcessor](../../text/41/KeEnumerateNextProcessor_function_00415480.md) (`PAGE` → `.text`)
  - `0x007453A8` → [KeIsEmptyAffinityEx](../../text/2D/KeIsEmptyAffinityEx_function_002D1580.md) (`PAGE` → `.text`)
  - `0x007453BE` → [KiCopyAffinityEx](../../text/2C/KiCopyAffinityEx_function_002CE860.md) (`PAGE` → `.text`)
  - `0x007453E4` → [KeEnumerateNextProcessor](../../text/41/KeEnumerateNextProcessor_function_00415480.md) (`PAGE` → `.text`)
  - `0x00745425` → [KeEnumerateNextProcessor](../../text/41/KeEnumerateNextProcessor_function_00415480.md) (`PAGE` → `.text`)
  - `0x00745452` → [KeEnumerateNextProcessor](../../text/41/KeEnumerateNextProcessor_function_00415480.md) (`PAGE` → `.text`)
  - `0x0074548F` → [KeAddProcessorAffinityEx](../../text/25/KeAddProcessorAffinityEx_function_0025B6F0.md) (`PAGE` → `.text`)
  - `0x007454A1` → [KeAddProcessorAffinityEx](../../text/25/KeAddProcessorAffinityEx_function_0025B6F0.md) (`PAGE` → `.text`)
  - `0x007454BC` → [KeAddProcessorAffinityEx](../../text/25/KeAddProcessorAffinityEx_function_0025B6F0.md) (`PAGE` → `.text`)
  - `0x007454C8` → [KeAddProcessorAffinityEx](../../text/25/KeAddProcessorAffinityEx_function_0025B6F0.md) (`PAGE` → `.text`)
  - `0x007454D7` → [KeEnumerateNextProcessor](../../text/41/KeEnumerateNextProcessor_function_00415480.md) (`PAGE` → `.text`)
  - `0x00745537` → [KiCopyAffinityEx](../../text/2C/KiCopyAffinityEx_function_002CE860.md) (`PAGE` → `.text`)
  - `0x00745557` → [KiCopyAffinityEx](../../text/2C/KiCopyAffinityEx_function_002CE860.md) (`PAGE` → `.text`)
  - `0x0074558C` → [KiCopyAffinityEx](../../text/2C/KiCopyAffinityEx_function_002CE860.md) (`PAGE` → `.text`)
  - `0x007455AC` → [KiCopyAffinityEx](../../text/2C/KiCopyAffinityEx_function_002CE860.md) (`PAGE` → `.text`)
  - `0x007455CB` → [KiCopyAffinityEx](../../text/2C/KiCopyAffinityEx_function_002CE860.md) (`PAGE` → `.text`)
  - `0x007455DA` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0074508C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00745091  55                              push rbp
00745092  56                              push rsi
00745093  57                              push rdi
00745094  41 54                           push r12
00745096  41 55                           push r13
00745098  41 56                           push r14
0074509A  41 57                           push r15
0074509C  48 8D AC 24 50 FF FF FF         lea rbp, [rsp - 0xb0]
007450A4  48 81 EC B0 01 00 00            sub rsp, 0x1b0
007450AB  48 8B 05 8E 56 6C 00            mov rax, qword ptr [rip + 0x6c568e]
007450B2  48 33 C4                        xor rax, rsp
007450B5  48 89 85 A0 00 00 00            mov qword ptr [rbp + 0xa0], rax
007450BC  48 8B 85 28 01 00 00            mov rax, qword ptr [rbp + 0x128]
007450C3  4C 8B FA                        mov r15, rdx
007450C6  48 8B 9D 30 01 00 00            mov rbx, qword ptr [rbp + 0x130]
007450CD  33 F6                           xor esi, esi
007450CF  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
007450D4  BF 00 01 00 00                  mov edi, 0x100
007450D9  48 8B 85 38 01 00 00            mov rax, qword ptr [rbp + 0x138]
007450E0  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
007450E5  48 8B 85 40 01 00 00            mov rax, qword ptr [rbp + 0x140]
007450EC  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
007450F1  48 8B 85 48 01 00 00            mov rax, qword ptr [rbp + 0x148]
007450F8  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
007450FD  48 8B 85 50 01 00 00            mov rax, qword ptr [rbp + 0x150]
00745104  44 89 44 24 4C                  mov dword ptr [rsp + 0x4c], r8d
00745109  44 8B C7                        mov r8d, edi
0074510C  48 89 54 24 68                  mov qword ptr [rsp + 0x68], rdx
00745111  33 D2                           xor edx, edx
00745113  88 4C 24 20                     mov byte ptr [rsp + 0x20], cl
00745117  48 8D 4D 98                     lea rcx, [rbp - 0x68]
0074511B  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
0074511F  44 89 4C 24 48                  mov dword ptr [rsp + 0x48], r9d
00745124  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
00745129  89 74 24 42                     mov dword ptr [rsp + 0x42], esi
0074512D  66 89 74 24 46                  mov word ptr [rsp + 0x46], si
00745132  E8 09 1B F8 FF                  call 0x1406c6c40
00745137  44 8B C7                        mov r8d, edi
0074513A  48 C7 45 90 01 00 20 00         mov qword ptr [rbp - 0x70], 0x200001
00745142  33 D2                           xor edx, edx
00745144  48 8D 4D 98                     lea rcx, [rbp - 0x68]
00745148  E8 F3 1A F8 FF                  call 0x1406c6c40
0074514D  4C 8B AD 18 01 00 00            mov r13, qword ptr [rbp + 0x118]
00745154  33 D2                           xor edx, edx
00745156  8B 05 24 19 88 00               mov eax, dword ptr [rip + 0x881924]
0074515C  41 B4 FF                        mov r12b, 0xff
0074515F  89 54 24 24                     mov dword ptr [rsp + 0x24], edx
00745163  40 8A FA                        mov dil, dl
00745166  45 8A F4                        mov r14b, r12b
00745169  41 8B 4D 04                     mov ecx, dword ptr [r13 + 4]
0074516D  89 4C 24 28                     mov dword ptr [rsp + 0x28], ecx
00745171  85 C0                           test eax, eax
00745173  0F 84 F7 00 00 00               je 0x140745270
00745179  8B 5C 24 24                     mov ebx, dword ptr [rsp + 0x24]
0074517D  4D 8B FD                        mov r15, r13
00745180  8B C3                           mov eax, ebx
00745182  0F AF C1                        imul eax, ecx
00745185  03 85 10 01 00 00               add eax, dword ptr [rbp + 0x110]
0074518B  44 8B E8                        mov r13d, eax
0074518E  38 54 24 20                     cmp byte ptr [rsp + 0x20], dl
00745192  74 07                           je 0x14074519b
00745194  41 38 54 87 1B                  cmp byte ptr [r15 + rax*4 + 0x1b], dl
00745199  EB 05                           jmp 0x1407451a0
0074519B  41 38 54 87 1A                  cmp byte ptr [r15 + rax*4 + 0x1a], dl
007451A0  0F 85 A1 00 00 00               jne 0x140745247
007451A6  8B D3                           mov edx, ebx
007451A8  48 8D 4D 90                     lea rcx, [rbp - 0x70]
007451AC  E8 3F 65 B1 FF                  call 0x14025b6f0
007451B1  4C 63 4C 24 48                  movsxd r9, dword ptr [rsp + 0x48]
007451B6  4C 63 44 24 4C                  movsxd r8, dword ptr [rsp + 0x4c]
007451BB  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
007451BF  8B CB                           mov ecx, ebx
007451C1  4B 8D 14 48                     lea rdx, [r8 + r9*2]
007451C5  4C 8D 0D 34 AE 8B FF            lea r9, [rip - 0x7451cc]
007451CC  44 8A 04 01                     mov r8b, byte ptr [rcx + rax]
007451D0  46 3A 84 0A F8 70 FC 00         cmp r8b, byte ptr [rdx + r9 + 0xfc70f8]
007451D8  72 67                           jb 0x140745241
007451DA  46 3A 84 0A E8 70 FC 00         cmp r8b, byte ptr [rdx + r9 + 0xfc70e8]
007451E2  77 5D                           ja 0x140745241
007451E4  33 C9                           xor ecx, ecx
007451E6  8B D3                           mov edx, ebx
007451E8  38 4C 24 20                     cmp byte ptr [rsp + 0x20], cl
007451EC  74 29                           je 0x140745217
007451EE  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
007451F3  E8 F8 64 B1 FF                  call 0x14025b6f0
007451F8  43 0F B6 4C AF 19               movzx ecx, byte ptr [r15 + r13*4 + 0x19]
007451FE  44 3A F1                        cmp r14b, cl
00745201  41 0F B6 C6                     movzx eax, r14b
00745205  0F 43 C1                        cmovae eax, ecx
00745208  33 D2                           xor edx, edx
0074520A  44 8A F0                        mov r14b, al
0074520D  40 3A F1                        cmp sil, cl
00745210  77 31                           ja 0x140745243
00745212  40 8A F1                        mov sil, cl
00745215  EB 2C                           jmp 0x140745243
00745217  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
0074521C  E8 CF 64 B1 FF                  call 0x14025b6f0
00745221  43 0F B6 4C AF 18               movzx ecx, byte ptr [r15 + r13*4 + 0x18]
00745227  44 3A E1                        cmp r12b, cl
0074522A  41 0F B6 C4                     movzx eax, r12b
0074522E  0F 43 C1                        cmovae eax, ecx
00745231  40 3A F9                        cmp dil, cl
00745234  44 8A E0                        mov r12b, al
00745237  40 0F B6 C7                     movzx eax, dil
0074523B  0F 46 C1                        cmovbe eax, ecx
0074523E  40 8A F8                        mov dil, al
00745241  33 D2                           xor edx, edx
00745243  8B 4C 24 28                     mov ecx, dword ptr [rsp + 0x28]
00745247  8B 05 33 18 88 00               mov eax, dword ptr [rip + 0x881833]
0074524D  FF C3                           inc ebx
0074524F  89 5C 24 24                     mov dword ptr [rsp + 0x24], ebx
00745253  8B 5C 24 24                     mov ebx, dword ptr [rsp + 0x24]
00745257  3B D8                           cmp ebx, eax
00745259  0F 82 21 FF FF FF               jb 0x140745180
0074525F  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
00745264  4C 8B AD 18 01 00 00            mov r13, qword ptr [rbp + 0x118]
0074526B  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
00745270  38 54 24 20                     cmp byte ptr [rsp + 0x20], dl
00745274  0F 85 2B 01 00 00               jne 0x1407453a5
0074527A  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
0074527F  48 8B CE                        mov rcx, rsi
00745282  E8 F9 C2 B8 FF                  call 0x1402d1580
00745287  45 33 F6                        xor r14d, r14d
0074528A  85 C0                           test eax, eax
0074528C  74 7C                           je 0x14074530a
0074528E  0F B7 56 02                     movzx edx, word ptr [rsi + 2]
00745292  4C 8D 45 90                     lea r8, [rbp - 0x70]
00745296  48 8B CE                        mov rcx, rsi
00745299  E8 C2 95 B8 FF                  call 0x1402ce860
0074529E  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
007452A2  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
007452A7  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
007452AC  48 8D 4C 24 24                  lea rcx, [rsp + 0x24]
007452B1  48 8D 45 90                     lea rax, [rbp - 0x70]
007452B5  66 44 89 74 24 40               mov word ptr [rsp + 0x40], r14w
007452BB  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
007452C0  E8 BB 01 CD FF                  call 0x140415480
007452C5  85 C0                           test eax, eax
007452C7  75 41                           jne 0x14074530a
007452C9  8B 5C 24 28                     mov ebx, dword ptr [rsp + 0x28]
007452CD  8B 44 24 24                     mov eax, dword ptr [rsp + 0x24]
007452D1  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
007452D6  0F AF C3                        imul eax, ebx
007452D9  40 0F B6 CF                     movzx ecx, dil
007452DD  03 85 10 01 00 00               add eax, dword ptr [rbp + 0x110]
007452E3  41 0F B6 7C 85 18               movzx edi, byte ptr [r13 + rax*4 + 0x18]
007452E9  44 3A E7                        cmp r12b, dil
007452EC  41 0F B6 C4                     movzx eax, r12b
007452F0  0F 43 C7                        cmovae eax, edi
007452F3  40 3A CF                        cmp cl, dil
007452F6  44 8A E0                        mov r12b, al
007452F9  0F 47 F9                        cmova edi, ecx
007452FC  48 8D 4C 24 24                  lea rcx, [rsp + 0x24]
00745301  E8 7A 01 CD FF                  call 0x140415480
00745306  85 C0                           test eax, eax
00745308  74 C3                           je 0x1407452cd
0074530A  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
0074530E  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
00745313  48 8D 4C 24 24                  lea rcx, [rsp + 0x24]
00745318  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0074531D  66 44 89 74 24 40               mov word ptr [rsp + 0x40], r14w
00745323  48 89 74 24 30                  mov qword ptr [rsp + 0x30], rsi
00745328  E8 53 01 CD FF                  call 0x140415480
0074532D  85 C0                           test eax, eax
0074532F  0F 85 B5 01 00 00               jne 0x1407454ea
00745335  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
0074533A  4C 8B 7C 24 60                  mov r15, qword ptr [rsp + 0x60]
0074533F  8B 5C 24 24                     mov ebx, dword ptr [rsp + 0x24]
00745343  33 C0                           xor eax, eax
00745345  8B F3                           mov esi, ebx
00745347  0F AF 74 24 28                  imul esi, dword ptr [rsp + 0x28]
0074534C  03 B5 10 01 00 00               add esi, dword ptr [rbp + 0x110]
00745352  38 85 20 01 00 00               cmp byte ptr [rbp + 0x120], al
00745358  75 0C                           jne 0x140745366
0074535A  8B D3                           mov edx, ebx
0074535C  49 8B CE                        mov rcx, r14
0074535F  E8 8C 63 B1 FF                  call 0x14025b6f0
00745364  EB 1D                           jmp 0x140745383
00745366  44 3A E7                        cmp r12b, dil
00745369  74 07                           je 0x140745372
0074536B  45 38 64 B5 18                  cmp byte ptr [r13 + rsi*4 + 0x18], r12b
00745370  76 0A                           jbe 0x14074537c
00745372  8B D3                           mov edx, ebx
00745374  49 8B CE                        mov rcx, r14
00745377  E8 74 63 B1 FF                  call 0x14025b6f0
0074537C  41 38 7C B5 18                  cmp byte ptr [r13 + rsi*4 + 0x18], dil
00745381  75 0A                           jne 0x14074538d
00745383  8B D3                           mov edx, ebx
00745385  49 8B CF                        mov rcx, r15
00745388  E8 63 63 B1 FF                  call 0x14025b6f0
0074538D  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
00745392  48 8D 4C 24 24                  lea rcx, [rsp + 0x24]
00745397  E8 E4 00 CD FF                  call 0x140415480
0074539C  85 C0                           test eax, eax
0074539E  74 9F                           je 0x14074533f
007453A0  E9 3B 01 00 00                  jmp 0x1407454e0
007453A5  48 8B CB                        mov rcx, rbx
007453A8  E8 D3 C1 B8 FF                  call 0x1402d1580
007453AD  33 FF                           xor edi, edi
007453AF  85 C0                           test eax, eax
007453B1  74 7D                           je 0x140745430
007453B3  0F B7 53 02                     movzx edx, word ptr [rbx + 2]
007453B7  4C 8D 45 90                     lea r8, [rbp - 0x70]
007453BB  48 8B CB                        mov rcx, rbx
007453BE  E8 9D 94 B8 FF                  call 0x1402ce860
007453C3  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
007453C7  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
007453CC  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
007453D1  48 8D 4C 24 24                  lea rcx, [rsp + 0x24]
007453D6  48 8D 45 90                     lea rax, [rbp - 0x70]
007453DA  66 89 7C 24 40                  mov word ptr [rsp + 0x40], di
007453DF  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
007453E4  E8 97 00 CD FF                  call 0x140415480
007453E9  44 8B 64 24 28                  mov r12d, dword ptr [rsp + 0x28]
007453EE  EB 3A                           jmp 0x14074542a
007453F0  8B 44 24 24                     mov eax, dword ptr [rsp + 0x24]
007453F4  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
007453F9  41 0F AF C4                     imul eax, r12d
007453FD  40 0F B6 CE                     movzx ecx, sil
00745401  03 85 10 01 00 00               add eax, dword ptr [rbp + 0x110]
00745407  41 0F B6 74 85 19               movzx esi, byte ptr [r13 + rax*4 + 0x19]
0074540D  44 3A F6                        cmp r14b, sil
00745410  41 0F B6 C6                     movzx eax, r14b
00745414  0F 43 C6                        cmovae eax, esi
00745417  40 3A CE                        cmp cl, sil
0074541A  44 8A F0                        mov r14b, al
0074541D  0F 47 F1                        cmova esi, ecx
00745420  48 8D 4C 24 24                  lea rcx, [rsp + 0x24]
00745425  E8 56 00 CD FF                  call 0x140415480
0074542A  85 C0                           test eax, eax
0074542C  74 C2                           je 0x1407453f0
0074542E  EB 05                           jmp 0x140745435
00745430  44 8B 64 24 28                  mov r12d, dword ptr [rsp + 0x28]
00745435  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00745439  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
0074543E  48 8D 4C 24 24                  lea rcx, [rsp + 0x24]
00745443  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00745448  66 89 7C 24 40                  mov word ptr [rsp + 0x40], di
0074544D  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
00745452  E8 29 00 CD FF                  call 0x140415480
00745457  85 C0                           test eax, eax
00745459  0F 85 86 00 00 00               jne 0x1407454e5
0074545F  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
00745464  8B 7C 24 24                     mov edi, dword ptr [rsp + 0x24]
00745468  8B C7                           mov eax, edi
0074546A  41 0F AF C4                     imul eax, r12d
0074546E  03 85 10 01 00 00               add eax, dword ptr [rbp + 0x110]
00745474  48 8D 1C 85 00 00 00 00         lea rbx, [rax*4]
0074547C  44 3A F6                        cmp r14b, sil
0074547F  74 07                           je 0x140745488
00745481  46 38 74 2B 19                  cmp byte ptr [rbx + r13 + 0x19], r14b
00745486  76 0C                           jbe 0x140745494
00745488  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
0074548D  8B D7                           mov edx, edi
0074548F  E8 5C 62 B1 FF                  call 0x14025b6f0
00745494  42 38 74 2B 19                  cmp byte ptr [rbx + r13 + 0x19], sil
00745499  75 0B                           jne 0x1407454a6
0074549B  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
0074549F  8B D7                           mov edx, edi
007454A1  E8 4A 62 B1 FF                  call 0x14025b6f0
007454A6  33 C0                           xor eax, eax
007454A8  38 85 20 01 00 00               cmp byte ptr [rbp + 0x120], al
007454AE  75 1D                           jne 0x1407454cd
007454B0  46 38 74 2B 19                  cmp byte ptr [rbx + r13 + 0x19], r14b
007454B5  75 16                           jne 0x1407454cd
007454B7  8B D7                           mov edx, edi
007454B9  49 8B CF                        mov rcx, r15
007454BC  E8 2F 62 B1 FF                  call 0x14025b6f0
007454C1  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
007454C6  8B D7                           mov edx, edi
007454C8  E8 23 62 B1 FF                  call 0x14025b6f0
007454CD  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
007454D2  48 8D 4C 24 24                  lea rcx, [rsp + 0x24]
007454D7  E8 A4 FF CC FF                  call 0x140415480
007454DC  85 C0                           test eax, eax
007454DE  74 84                           je 0x140745464
007454E0  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
007454E5  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
007454EA  48 63 5C 24 48                  movsxd rbx, dword ptr [rsp + 0x48]
007454EF  48 8D 15 0A AB 8B FF            lea rdx, [rip - 0x7454f6]
007454F6  48 63 7C 24 4C                  movsxd rdi, dword ptr [rsp + 0x4c]
007454FB  48 8D 0C 5F                     lea rcx, [rdi + rbx*2]
007454FF  8B 94 8A 60 54 FC 00            mov edx, dword ptr [rdx + rcx*4 + 0xfc5460]
00745506  83 EA 01                        sub edx, 1
00745509  74 66                           je 0x140745571
0074550B  83 EA 01                        sub edx, 1
0074550E  74 5A                           je 0x14074556a
00745510  83 EA 01                        sub edx, 1
00745513  74 4E                           je 0x140745563
00745515  83 FA 01                        cmp edx, 1
00745518  0F 85 B2 00 00 00               jne 0x1407455d0
0074551E  4C 8B C6                        mov r8, rsi
00745521  48 8D 43 03                     lea rax, [rbx + 3]
00745525  48 8D 04 47                     lea rax, [rdi + rax*2]
00745529  48 69 C8 08 01 00 00            imul rcx, rax, 0x108
00745530  49 03 CF                        add rcx, r15
00745533  0F B7 51 02                     movzx edx, word ptr [rcx + 2]
00745537  E8 24 93 B8 FF                  call 0x1402ce860
0074553C  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
00745541  48 8D 43 0A                     lea rax, [rbx + 0xa]
00745545  48 8D 04 47                     lea rax, [rdi + rax*2]
00745549  48 69 C8 08 01 00 00            imul rcx, rax, 0x108
00745550  49 03 CF                        add rcx, r15
00745553  0F B7 51 02                     movzx edx, word ptr [rcx + 2]
00745557  E8 04 93 B8 FF                  call 0x1402ce860
0074555C  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
00745561  EB 52                           jmp 0x1407455b5
00745563  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
00745568  EB B7                           jmp 0x140745521
0074556A  4C 8B 44 24 70                  mov r8, qword ptr [rsp + 0x70]
0074556F  EB 05                           jmp 0x140745576
00745571  4C 8B 44 24 78                  mov r8, qword ptr [rsp + 0x78]
00745576  48 8D 43 03                     lea rax, [rbx + 3]
0074557A  48 8D 04 47                     lea rax, [rdi + rax*2]
0074557E  48 69 C8 08 01 00 00            imul rcx, rax, 0x108
00745585  49 03 CF                        add rcx, r15
00745588  0F B7 51 02                     movzx edx, word ptr [rcx + 2]
0074558C  E8 CF 92 B8 FF                  call 0x1402ce860
00745591  4C 8B 44 24 78                  mov r8, qword ptr [rsp + 0x78]
00745596  48 8D 43 0A                     lea rax, [rbx + 0xa]
0074559A  48 8D 04 47                     lea rax, [rdi + rax*2]
0074559E  48 69 C8 08 01 00 00            imul rcx, rax, 0x108
007455A5  49 03 CF                        add rcx, r15
007455A8  0F B7 51 02                     movzx edx, word ptr [rcx + 2]
007455AC  E8 AF 92 B8 FF                  call 0x1402ce860
007455B1  4C 8B 45 80                     mov r8, qword ptr [rbp - 0x80]
007455B5  48 8D 43 11                     lea rax, [rbx + 0x11]
007455B9  48 8D 04 47                     lea rax, [rdi + rax*2]
007455BD  48 69 C8 08 01 00 00            imul rcx, rax, 0x108
007455C4  49 03 CF                        add rcx, r15
007455C7  0F B7 51 02                     movzx edx, word ptr [rcx + 2]
007455CB  E8 90 92 B8 FF                  call 0x1402ce860
007455D0  48 8B 8D A0 00 00 00            mov rcx, qword ptr [rbp + 0xa0]
007455D7  48 33 CC                        xor rcx, rsp
007455DA  E8 61 70 F6 FF                  call 0x1406ac640
007455DF  48 8B 9C 24 F0 01 00 00         mov rbx, qword ptr [rsp + 0x1f0]
007455E7  48 81 C4 B0 01 00 00            add rsp, 0x1b0
007455EE  41 5F                           pop r15
007455F0  41 5E                           pop r14
007455F2  41 5D                           pop r13
007455F4  41 5C                           pop r12
007455F6  5F                              pop rdi
007455F7  5E                              pop rsi
007455F8  5D                              pop rbp
007455F9  C3                              ret
007455FA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiPrepareUpdateCoresHeteroMask(unsigned __int8 a1, __int64 a2, int a3, int a4, unsigned int a5, __int64 a6, unsigned __int8 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned int v_stack_m19C;
    unsigned int v_stack_m1A0;
    unsigned __int16 v_stack_m1A2;
    unsigned int v_stack_m1A6;
    unsigned __int16 v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned int v_stack_m1C0;
    unsigned int v_stack_m1C4;
    unsigned __int8 v_stack_m1C8;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (432);
    result = (*(unsigned __int64 *)(v_rip + 7100046)) ^ (v_rsp);
    v_stack_m48 = result;
    v_rsi = 0;
    v_stack_m198 = a8;
    v_stack_m190 = a10;
    v_stack_m188 = a11;
    v_stack_m170 = a12;
    v_stack_m19C = a3;
    v_stack_m180 = a2;
    a2 = 0;
    v_stack_m1C8 = a1;
    v_stack_m168 = a13;
    v_stack_m1A0 = a4;
    v_stack_m178 = a9;
    v_stack_m1A6 = 0;
    v_stack_m1A2 = 0;
    result = memset(v_stack_m150, a2, 256, a4);
    v_stack_m158 = 0x200001ULL;
    a2 = 0;
    result = memset(v_stack_m150, a2, 256, a4);
    a2 = 0;
    v_stack_m1C4 = 0;
    v_stack_m1C0 = (unsigned int)((unsigned int)(*(unsigned int *)(a6 + 4)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 8919332))) == 0) goto loc_00745270;
loc_00745180:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m1C4)))) * ((unsigned int)((unsigned int)(*(unsigned int *)(a6 + 4)))));
    result = (unsigned int)((result) + (a5));
    if (v_stack_m1C8 == 0) goto loc_0074519B;
    goto loc_007451A0;
loc_0074519B:
loc_007451A0:
    if ((*(unsigned __int8 *)(a6 + result * 4 + 26)) != 0) goto loc_00745247;
    result = KeAddProcessorAffinityEx(v_stack_m158, (unsigned int)((unsigned int)((unsigned int)(v_stack_m1C4))), 256, a4);
    if (((unsigned __int8)(*(unsigned __int8 *)((unsigned int)((unsigned int)((unsigned int)(v_stack_m1C4))) + *(unsigned __int64 *)(a6 + 8) * 1))) < (*(unsigned __int8 *)((int)(v_stack_m19C) + (int)(v_stack_m1A0) * 2 + v_rip - 7623116 * 1 + 16543992))) goto loc_00745241;
    if (((unsigned __int8)(*(unsigned __int8 *)((unsigned int)((unsigned int)((unsigned int)(v_stack_m1C4))) + *(unsigned __int64 *)(a6 + 8) * 1))) > (*(unsigned __int8 *)((int)(v_stack_m19C) + (int)(v_stack_m1A0) * 2 + v_rip - 7623116 * 1 + 16543976))) goto loc_00745241;
    a1 = 0;
    if (v_stack_m1C8 == 0) goto loc_00745217;
    result = KeAddProcessorAffinityEx(v_stack_m178, (unsigned int)((unsigned int)((unsigned int)(v_stack_m1C4))), *(unsigned __int8 *)((unsigned int)((unsigned int)((unsigned int)(v_stack_m1C4))) + *(unsigned __int64 *)(a6 + 8) * 1), v_rip - 7623116);
    result = 255;
    if (255 >= ((unsigned __int8)(*(unsigned __int8 *)(a6 + (unsigned int)((unsigned int)(result)) * 4 + 25)))) { result = (unsigned int)(*(unsigned __int8 *)(a6 + (unsigned int)((unsigned int)(result)) * 4 + 25)); }
    a2 = 0;
    if (0 > ((unsigned __int8)(*(unsigned __int8 *)(a6 + (unsigned int)((unsigned int)(result)) * 4 + 25)))) goto loc_00745243;
    goto loc_00745243;
loc_00745217:
    result = KeAddProcessorAffinityEx(v_stack_m198, a2, *(unsigned __int8 *)((unsigned int)((unsigned int)((unsigned int)(v_stack_m1C4))) + *(unsigned __int64 *)(a6 + 8) * 1), v_rip - 7623116);
    result = 255;
    if (255 >= ((unsigned __int8)(*(unsigned __int8 *)(a6 + (unsigned int)((unsigned int)(result)) * 4 + 24)))) { result = (unsigned int)(*(unsigned __int8 *)(a6 + (unsigned int)((unsigned int)(result)) * 4 + 24)); }
    result = 0;
    if (0 <= ((unsigned __int8)(*(unsigned __int8 *)(a6 + (unsigned int)((unsigned int)(result)) * 4 + 24)))) { result = (unsigned int)(*(unsigned __int8 *)(a6 + (unsigned int)((unsigned int)(result)) * 4 + 24)); }
loc_00745241:
    a2 = 0;
loc_00745243:
loc_00745247:
    v_rbx = (unsigned int)(((unsigned int)(v_stack_m1C4)) + 1);
    v_stack_m1C4 = (unsigned int)(v_rbx);
    if (((unsigned int)((unsigned int)(v_stack_m1C4))) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 8919091))))) goto loc_00745180;
loc_00745270:
    if (v_stack_m1C8 != 0) goto loc_007453A5;
    result = KeIsEmptyAffinityEx(v_stack_m198, a2, *(unsigned __int8 *)((unsigned int)((unsigned int)((unsigned int)(v_stack_m1C4))) + *(unsigned __int64 *)(a6 + 8) * 1), v_rip - 7623116);
    v_r14 = 0;
    if ((unsigned int)(result) == 0) goto loc_0074530A;
    result = KiCopyAffinityEx(v_stack_m198, *(unsigned __int16 *)(v_stack_m198 + 2), v_stack_m158, v_rip - 7623116);
    v_stack_m1B0 = v_stack_m150;
    v_stack_m1A8 = 0;
    v_stack_m1B8 = v_stack_m158;
    result = KeEnumerateNextProcessor(v_stack_m1C4, v_stack_m1B8, v_stack_m158, v_rip - 7623116);
    if ((unsigned int)(result) != 0) goto loc_0074530A;
loc_007452CD:
    result = (unsigned int)(((unsigned int)(v_stack_m1C4)) * ((unsigned int)((unsigned int)(v_stack_m1C0))));
    result = (unsigned int)((result) + (a5));
    result = (unsigned __int8)((unsigned __int8)(result));
    if (((unsigned __int8)((unsigned __int8)(result))) >= ((unsigned __int8)(*(unsigned __int8 *)(a6 + result * 4 + 24)))) { result = (unsigned int)(*(unsigned __int8 *)(a6 + result * 4 + 24)); }
    v_rdi = *(unsigned __int8 *)(a6 + result * 4 + 24);
    if (((unsigned __int8)((unsigned __int8)((unsigned __int8)(result)))) > ((unsigned __int8)(*(unsigned __int8 *)(a6 + result * 4 + 24)))) { v_rdi = (unsigned int)((unsigned __int8)((unsigned __int8)(result))); }
    result = KeEnumerateNextProcessor(v_stack_m1C4, v_stack_m1B8, v_stack_m158, v_rip - 7623116);
    if ((unsigned int)(result) == 0) goto loc_007452CD;
loc_0074530A:
    v_stack_m1B0 = *(unsigned __int64 *)(v_stack_m198 + 8);
    v_stack_m1A8 = 0;
    v_stack_m1B8 = v_stack_m198;
    result = KeEnumerateNextProcessor(v_stack_m1C4, v_stack_m1B8, v_stack_m158, v_rip - 7623116);
    if ((unsigned int)(result) != 0) goto loc_007454EA;
loc_0074533F:
    result = 0;
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m1C4)))) * (v_stack_m1C0));
    v_rsi = (unsigned int)((v_rsi) + (a5));
    if (a7 != 0) goto loc_00745366;
    result = KeAddProcessorAffinityEx(v_stack_m190, (unsigned int)((unsigned int)((unsigned int)(v_stack_m1C4))), v_stack_m158, v_rip - 7623116);
    goto loc_00745383;
loc_00745366:
    if (((unsigned __int8)((unsigned __int8)(result))) == ((unsigned __int8)(v_rdi))) goto loc_00745372;
    if ((*(unsigned __int8 *)(a6 + v_rsi * 4 + 24)) >= = ((unsigned __int8)((unsigned __int8)(result)))) {
        a2 = (unsigned int)((unsigned int)(v_stack_m1C4));
        a1 = v_stack_m190;
        result = KeAddProcessorAffinityEx(a1, a2, v_stack_m158, v_rip - 7623116);
    }
    if ((*(unsigned __int8 *)(a6 + v_rsi * 4 + 24)) == ((unsigned __int8)(v_rdi))) {
        a2 = (unsigned int)((unsigned int)(v_stack_m1C4));
        a1 = v_stack_m188;
        result = KeAddProcessorAffinityEx(a1, a2, v_stack_m158, v_rip - 7623116);
    }
    result = KeEnumerateNextProcessor(v_stack_m1C4, v_stack_m1B8, v_stack_m158, v_rip - 7623116);
    if ((unsigned int)(result) == 0) goto loc_0074533F;
    goto loc_007454E0;
loc_007453A5:
    result = KeIsEmptyAffinityEx((unsigned int)(v_stack_m1C4), v_stack_m1B8, v_stack_m158, v_rip - 7623116);
    v_rdi = 0;
    if ((unsigned int)(result) == 0) goto loc_00745430;
    result = KiCopyAffinityEx((unsigned int)(v_stack_m1C4), *(unsigned __int16 *)((unsigned int)(v_stack_m1C4) + 2), v_stack_m158, v_rip - 7623116);
    v_stack_m1B0 = v_stack_m150;
    v_stack_m1A8 = 0;
    v_stack_m1B8 = v_stack_m158;
    result = KeEnumerateNextProcessor(v_stack_m1C4, v_stack_m1B8, v_stack_m158, v_rip - 7623116);
    goto loc_0074542A;
loc_007453F0:
    result = (unsigned int)(((unsigned int)(v_stack_m1C4)) * ((unsigned int)((unsigned int)(v_stack_m1C0))));
    result = (unsigned int)((result) + (a5));
    result = (unsigned __int8)(v_stack_m190);
    if (((unsigned __int8)(v_stack_m190)) >= ((unsigned __int8)(*(unsigned __int8 *)(a6 + result * 4 + 25)))) { result = (unsigned int)(*(unsigned __int8 *)(a6 + result * 4 + 25)); }
    v_rsi = *(unsigned __int8 *)(a6 + result * 4 + 25);
    if (((unsigned __int8)((unsigned __int8)(v_rsi))) > ((unsigned __int8)(*(unsigned __int8 *)(a6 + result * 4 + 25)))) { v_rsi = (unsigned int)((unsigned __int8)(v_rsi)); }
    result = KeEnumerateNextProcessor(v_stack_m1C4, v_stack_m1B8, v_stack_m158, v_rip - 7623116);
loc_0074542A:
    if ((unsigned int)(result) == 0) goto loc_007453F0;
    goto loc_00745435;
loc_00745430:
loc_00745435:
    v_stack_m1B0 = *(unsigned __int64 *)((unsigned int)(v_stack_m1C4) + 8);
    v_stack_m1A8 = 0;
    v_stack_m1B8 = (unsigned int)(v_stack_m1C4);
    result = KeEnumerateNextProcessor(v_stack_m1C4, v_stack_m1B8, v_stack_m158, v_rip - 7623116);
    if ((unsigned int)(result) != 0) goto loc_007454E5;
loc_00745464:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m1C4)))) * ((unsigned int)((unsigned int)(v_stack_m1C0))));
    result = (unsigned int)((result) + (a5));
    if (((unsigned __int8)((unsigned __int8)(result))) == ((unsigned __int8)(v_rsi))) goto loc_00745488;
    if ((*(unsigned __int8 *)(result * 4 + a6 * 1 + 25)) >= = ((unsigned __int8)((unsigned __int8)(result)))) {
        a1 = v_stack_m170;
        a2 = (unsigned int)((unsigned int)(v_stack_m1C4));
        result = KeAddProcessorAffinityEx(a1, a2, v_stack_m158, v_rip - 7623116);
    }
    if ((*(unsigned __int8 *)(result * 4 + a6 * 1 + 25)) == ((unsigned __int8)(v_rsi))) {
        a1 = v_stack_m168;
        a2 = (unsigned int)((unsigned int)(v_stack_m1C4));
        result = KeAddProcessorAffinityEx(a1, a2, v_stack_m158, v_rip - 7623116);
    }
    result = 0;
    if (a7 != 0) goto loc_007454CD;
    if ((*(unsigned __int8 *)(result * 4 + a6 * 1 + 25)) == ((unsigned __int8)((unsigned __int8)(result)))) {
        a2 = (unsigned int)((unsigned int)(v_stack_m1C4));
        a1 = v_stack_m190;
        result = KeAddProcessorAffinityEx(a1, a2, v_stack_m158, v_rip - 7623116);
        a1 = v_stack_m188;
        a2 = (unsigned int)((unsigned int)(v_stack_m1C4));
        result = KeAddProcessorAffinityEx(a1, a2, v_stack_m158, v_rip - 7623116);
    }
    result = KeEnumerateNextProcessor(v_stack_m1C4, v_stack_m1B8, v_stack_m158, v_rip - 7623116);
    if ((unsigned int)(result) == 0) goto loc_00745464;
loc_007454E0:
loc_007454E5:
loc_007454EA:
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip - 7623926 + (int)(v_stack_m19C) + (int)(v_stack_m1A0) * 2 * 4 + 16536672))) - (1));
    if (condition_is_equal) goto loc_00745571;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_0074556A;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_00745563;
    if (((unsigned int)(a2)) != 1) goto loc_007455D0;
loc_00745521:
    a1 = ((int)(v_stack_m19C) + (int)(v_stack_m1A0) * 2) * ((int)(v_stack_m19C) + (int)(v_stack_m1A0) + 3 * 2);
    a1 = (a1) + (v_stack_m180);
    result = KiCopyAffinityEx(a1, *(unsigned __int16 *)(a1 + 2), v_stack_m198, v_rip - 7623116);
    a1 = (a1) * ((int)(v_stack_m19C) + (int)(v_stack_m1A0) + 10 * 2);
    a1 = (a1) + (v_stack_m180);
    result = KiCopyAffinityEx(a1, *(unsigned __int16 *)(a1 + 2), v_stack_m190, v_rip - 7623116);
    goto loc_007455B5;
loc_00745563:
    goto loc_00745521;
loc_0074556A:
    goto loc_00745576;
loc_00745571:
loc_00745576:
    a1 = (a1) * ((int)(v_stack_m19C) + (int)(v_stack_m1A0) + 3 * 2);
    a1 = (a1) + (v_stack_m180);
    result = KiCopyAffinityEx(a1, *(unsigned __int16 *)(a1 + 2), v_stack_m170, v_rip - 7623116);
    a1 = (a1) * ((int)(v_stack_m19C) + (int)(v_stack_m1A0) + 10 * 2);
    a1 = (a1) + (v_stack_m180);
    result = KiCopyAffinityEx(a1, *(unsigned __int16 *)(a1 + 2), v_stack_m170, v_rip - 7623116);
loc_007455B5:
    a1 = (a1) * ((int)(v_stack_m19C) + (int)(v_stack_m1A0) + 17 * 2);
    a1 = (a1) + (v_stack_m180);
    result = KiCopyAffinityEx(a1, *(unsigned __int16 *)(a1 + 2), v_stack_m168, v_rip - 7623116);
loc_007455D0:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, *(unsigned __int16 *)(a1 + 2), v_stack_m168, v_rip - 7623116);
    v_rsp = (v_rsp) + (432);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiPrepareUpdateCoresHeteroMask(uint8_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4, uint32_t Arg5, void *Arg6, uint8_t Arg7, int64_t Arg8, int64_t Arg9, int64_t Arg10, int64_t Arg11, int64_t Arg12, int64_t Arg13)
{
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint32_t v_stack_m19C;
    uint32_t v_stack_m1A0;
    uint16_t v_stack_m1A2;
    uint32_t v_stack_m1A6;
    uint16_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint32_t v_stack_m1C0;
    uint32_t v_stack_m1C4;
    uint8_t v_stack_m1C8;
    uint64_t v_stack_m48;
    uint64_t v_stack_mE8;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (432);
    result = (*(uint64_t *)(v_rip + 0x6C568E)) ^ (local_rsp);
    v_stack_m48 = result;
    local_rsi = 0;
    v_stack_m198 = Arg8;
    v_stack_m190 = Arg10;
    v_stack_m188 = Arg11;
    v_stack_m170 = Arg12;
    v_stack_m19C = Arg3;
    v_stack_m180 = Arg2;
    Arg2 = 0;
    v_stack_m1C8 = Arg1;
    v_stack_m168 = Arg13;
    v_stack_m1A0 = Arg4;
    v_stack_m178 = Arg9;
    v_stack_m1A6 = 0;
    v_stack_m1A2 = 0;
    result = memset(v_stack_m150, Arg2, 256, Arg4);
    v_stack_m158 = 0x200001ULL;
    Arg2 = 0;
    result = memset(v_stack_m150, Arg2, 256, Arg4);
    Arg2 = 0;
    v_stack_m1C4 = 0;
    v_stack_m1C0 = (uint32_t)((uint32_t)(*(uint32_t *)(arg6 + 0x4)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x881924))) == 0) goto loc_00745270;
loc_00745180:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m1C4)))) * ((uint32_t)((uint32_t)(*(uint32_t *)(arg6 + 0x4)))));
    result = (uint32_t)((result) + (Arg5));
    if (v_stack_m1C8 == 0) goto loc_0074519B;
    goto loc_007451A0;
loc_0074519B:
loc_007451A0:
    if ((*(uint8_t *)(arg6 + result * 4 + 0x1A)) != 0) goto loc_00745247;
    result = KeAddProcessorAffinityEx(v_stack_m158, (uint32_t)((uint32_t)((uint32_t)(v_stack_m1C4))), 256, Arg4);
    if (((uint8_t)(*(uint8_t *)((uint32_t)((uint32_t)((uint32_t)(v_stack_m1C4))) + *(uint64_t *)(arg6 + 0x8) * 1))) < (*(uint8_t *)((int32_t)(v_stack_m19C) + (int32_t)(v_stack_m1A0) * 2 + v_rip - 0x7451CC * 1 + 0xFC70F8))) goto loc_00745241;
    if (((uint8_t)(*(uint8_t *)((uint32_t)((uint32_t)((uint32_t)(v_stack_m1C4))) + *(uint64_t *)(arg6 + 0x8) * 1))) > (*(uint8_t *)((int32_t)(v_stack_m19C) + (int32_t)(v_stack_m1A0) * 2 + v_rip - 0x7451CC * 1 + 0xFC70E8))) goto loc_00745241;
    Arg1 = 0;
    if (v_stack_m1C8 == 0) goto loc_00745217;
    result = KeAddProcessorAffinityEx(v_stack_m178, (uint32_t)((uint32_t)((uint32_t)(v_stack_m1C4))), *(uint8_t *)((uint32_t)((uint32_t)((uint32_t)(v_stack_m1C4))) + *(uint64_t *)(arg6 + 0x8) * 1), v_rip - 7623116);
    result = 255;
    if (255 >= ((uint8_t)(*(uint8_t *)(arg6 + (uint32_t)((uint32_t)(result)) * 4 + 0x19)))) { result = (uint32_t)(*(uint8_t *)(arg6 + (uint32_t)((uint32_t)(result)) * 4 + 0x19)); }
    Arg2 = 0;
    if (0 > ((uint8_t)(*(uint8_t *)(arg6 + (uint32_t)((uint32_t)(result)) * 4 + 0x19)))) goto loc_00745243;
    goto loc_00745243;
loc_00745217:
    result = KeAddProcessorAffinityEx(v_stack_m198, Arg2, *(uint8_t *)((uint32_t)((uint32_t)((uint32_t)(v_stack_m1C4))) + *(uint64_t *)(arg6 + 0x8) * 1), v_rip - 7623116);
    result = 255;
    if (255 >= ((uint8_t)(*(uint8_t *)(arg6 + (uint32_t)((uint32_t)(result)) * 4 + 0x18)))) { result = (uint32_t)(*(uint8_t *)(arg6 + (uint32_t)((uint32_t)(result)) * 4 + 0x18)); }
    result = 0;
    if (0 <= ((uint8_t)(*(uint8_t *)(arg6 + (uint32_t)((uint32_t)(result)) * 4 + 0x18)))) { result = (uint32_t)(*(uint8_t *)(arg6 + (uint32_t)((uint32_t)(result)) * 4 + 0x18)); }
loc_00745241:
    Arg2 = 0;
loc_00745243:
loc_00745247:
    local_rbx = (uint32_t)(((uint32_t)(v_stack_m1C4)) + 1);
    v_stack_m1C4 = (uint32_t)(local_rbx);
    if (((uint32_t)((uint32_t)(v_stack_m1C4))) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x881833))))) goto loc_00745180;
loc_00745270:
    if (v_stack_m1C8 != 0) goto loc_007453A5;
    result = KeIsEmptyAffinityEx(v_stack_m198, Arg2, *(uint8_t *)((uint32_t)((uint32_t)((uint32_t)(v_stack_m1C4))) + *(uint64_t *)(arg6 + 0x8) * 1), v_rip - 7623116);
    local_r14 = 0;
    if ((uint32_t)(result) == 0) goto loc_0074530A;
    result = KiCopyAffinityEx(v_stack_m198, *(uint16_t *)(v_stack_m198 + 0x2), v_stack_m158, v_rip - 7623116);
    v_stack_m1B0 = v_stack_m150;
    v_stack_m1A8 = 0;
    v_stack_m1B8 = v_stack_m158;
    result = KeEnumerateNextProcessor(v_stack_m1C4, v_stack_m1B8, v_stack_m158, v_rip - 7623116);
    if ((uint32_t)(result) != 0) goto loc_0074530A;
loc_007452CD:
    result = (uint32_t)(((uint32_t)(v_stack_m1C4)) * ((uint32_t)((uint32_t)(v_stack_m1C0))));
    result = (uint32_t)((result) + (Arg5));
    result = (uint8_t)((uint8_t)(result));
    if (((uint8_t)((uint8_t)(result))) >= ((uint8_t)(*(uint8_t *)(arg6 + result * 4 + 0x18)))) { result = (uint32_t)(*(uint8_t *)(arg6 + result * 4 + 0x18)); }
    local_rdi = *(uint8_t *)(arg6 + result * 4 + 0x18);
    if (((uint8_t)((uint8_t)((uint8_t)(result)))) > ((uint8_t)(*(uint8_t *)(arg6 + result * 4 + 0x18)))) { local_rdi = (uint32_t)((uint8_t)((uint8_t)(result))); }
    result = KeEnumerateNextProcessor(v_stack_m1C4, v_stack_m1B8, v_stack_m158, v_rip - 7623116);
    if ((uint32_t)(result) == 0) goto loc_007452CD;
loc_0074530A:
    v_stack_m1B0 = *(uint64_t *)(v_stack_m198 + 0x8);
    v_stack_m1A8 = 0;
    v_stack_m1B8 = v_stack_m198;
    result = KeEnumerateNextProcessor(v_stack_m1C4, v_stack_m1B8, v_stack_m158, v_rip - 7623116);
    if ((uint32_t)(result) != 0) goto loc_007454EA;
loc_0074533F:
    result = 0;
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m1C4)))) * (v_stack_m1C0));
    local_rsi = (uint32_t)((local_rsi) + (Arg5));
    if (Arg7 != 0) goto loc_00745366;
    result = KeAddProcessorAffinityEx(v_stack_m190, (uint32_t)((uint32_t)((uint32_t)(v_stack_m1C4))), v_stack_m158, v_rip - 7623116);
    goto loc_00745383;
loc_00745366:
    if (((uint8_t)((uint8_t)(result))) == ((uint8_t)(local_rdi))) goto loc_00745372;
    if ((*(uint8_t *)(arg6 + local_rsi * 4 + 0x18)) >= = ((uint8_t)((uint8_t)(result)))) {
        Arg2 = (uint32_t)((uint32_t)(v_stack_m1C4));
        Arg1 = v_stack_m190;
        result = KeAddProcessorAffinityEx(Arg1, Arg2, v_stack_m158, v_rip - 7623116);
    }
    if ((*(uint8_t *)(arg6 + local_rsi * 4 + 0x18)) == ((uint8_t)(local_rdi))) {
        Arg2 = (uint32_t)((uint32_t)(v_stack_m1C4));
        Arg1 = v_stack_m188;
        result = KeAddProcessorAffinityEx(Arg1, Arg2, v_stack_m158, v_rip - 7623116);
    }
    result = KeEnumerateNextProcessor(v_stack_m1C4, v_stack_m1B8, v_stack_m158, v_rip - 7623116);
    if ((uint32_t)(result) == 0) goto loc_0074533F;
    goto loc_007454E0;
loc_007453A5:
    result = KeIsEmptyAffinityEx((uint32_t)(v_stack_m1C4), v_stack_m1B8, v_stack_m158, v_rip - 7623116);
    local_rdi = 0;
    if ((uint32_t)(result) == 0) goto loc_00745430;
    result = KiCopyAffinityEx((uint32_t)(v_stack_m1C4), *(uint16_t *)((uint32_t)(v_stack_m1C4) + 0x2), v_stack_m158, v_rip - 7623116);
    v_stack_m1B0 = v_stack_m150;
    v_stack_m1A8 = 0;
    v_stack_m1B8 = v_stack_m158;
    result = KeEnumerateNextProcessor(v_stack_m1C4, v_stack_m1B8, v_stack_m158, v_rip - 7623116);
    goto loc_0074542A;
loc_007453F0:
    result = (uint32_t)(((uint32_t)(v_stack_m1C4)) * ((uint32_t)((uint32_t)(v_stack_m1C0))));
    result = (uint32_t)((result) + (Arg5));
    result = (uint8_t)(v_stack_m190);
    if (((uint8_t)(v_stack_m190)) >= ((uint8_t)(*(uint8_t *)(arg6 + result * 4 + 0x19)))) { result = (uint32_t)(*(uint8_t *)(arg6 + result * 4 + 0x19)); }
    local_rsi = *(uint8_t *)(arg6 + result * 4 + 0x19);
    if (((uint8_t)((uint8_t)(local_rsi))) > ((uint8_t)(*(uint8_t *)(arg6 + result * 4 + 0x19)))) { local_rsi = (uint32_t)((uint8_t)(local_rsi)); }
    result = KeEnumerateNextProcessor(v_stack_m1C4, v_stack_m1B8, v_stack_m158, v_rip - 7623116);
loc_0074542A:
    if ((uint32_t)(result) == 0) goto loc_007453F0;
    goto loc_00745435;
loc_00745430:
loc_00745435:
    v_stack_m1B0 = *(uint64_t *)((uint32_t)(v_stack_m1C4) + 0x8);
    v_stack_m1A8 = 0;
    v_stack_m1B8 = (uint32_t)(v_stack_m1C4);
    result = KeEnumerateNextProcessor(v_stack_m1C4, v_stack_m1B8, v_stack_m158, v_rip - 7623116);
    if ((uint32_t)(result) != 0) goto loc_007454E5;
loc_00745464:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m1C4)))) * ((uint32_t)((uint32_t)(v_stack_m1C0))));
    result = (uint32_t)((result) + (Arg5));
    if (((uint8_t)((uint8_t)(result))) == ((uint8_t)(local_rsi))) goto loc_00745488;
    if ((*(uint8_t *)(result * 4 + arg6 * 1 + 0x19)) >= = ((uint8_t)((uint8_t)(result)))) {
        Arg1 = v_stack_m170;
        Arg2 = (uint32_t)((uint32_t)(v_stack_m1C4));
        result = KeAddProcessorAffinityEx(Arg1, Arg2, v_stack_m158, v_rip - 7623116);
    }
    if ((*(uint8_t *)(result * 4 + arg6 * 1 + 0x19)) == ((uint8_t)(local_rsi))) {
        Arg1 = v_stack_m168;
        Arg2 = (uint32_t)((uint32_t)(v_stack_m1C4));
        result = KeAddProcessorAffinityEx(Arg1, Arg2, v_stack_m158, v_rip - 7623116);
    }
    result = 0;
    if (Arg7 != 0) goto loc_007454CD;
    if ((*(uint8_t *)(result * 4 + arg6 * 1 + 0x19)) == ((uint8_t)((uint8_t)(result)))) {
        Arg2 = (uint32_t)((uint32_t)(v_stack_m1C4));
        Arg1 = v_stack_m190;
        result = KeAddProcessorAffinityEx(Arg1, Arg2, v_stack_m158, v_rip - 7623116);
        Arg1 = v_stack_m188;
        Arg2 = (uint32_t)((uint32_t)(v_stack_m1C4));
        result = KeAddProcessorAffinityEx(Arg1, Arg2, v_stack_m158, v_rip - 7623116);
    }
    result = KeEnumerateNextProcessor(v_stack_m1C4, v_stack_m1B8, v_stack_m158, v_rip - 7623116);
    if ((uint32_t)(result) == 0) goto loc_00745464;
loc_007454E0:
loc_007454E5:
loc_007454EA:
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip - 0x7454F6 + (int32_t)(v_stack_m19C) + (int32_t)(v_stack_m1A0) * 2 * 4 + 0xFC5460))) - (1));
    if (condition_is_equal) goto loc_00745571;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_0074556A;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_00745563;
    if (((uint32_t)(Arg2)) != 1) goto loc_007455D0;
loc_00745521:
    Arg1 = ((int32_t)(v_stack_m19C) + (int32_t)(v_stack_m1A0) * 2) * ((int32_t)(v_stack_m19C) + (int32_t)(v_stack_m1A0) + 3 * 2);
    Arg1 = (Arg1) + (v_stack_m180);
    result = KiCopyAffinityEx(Arg1, *(uint16_t *)(Arg1 + 0x2), v_stack_m198, v_rip - 7623116);
    Arg1 = (Arg1) * ((int32_t)(v_stack_m19C) + (int32_t)(v_stack_m1A0) + 10 * 2);
    Arg1 = (Arg1) + (v_stack_m180);
    result = KiCopyAffinityEx(Arg1, *(uint16_t *)(Arg1 + 0x2), v_stack_m190, v_rip - 7623116);
    goto loc_007455B5;
loc_00745563:
    goto loc_00745521;
loc_0074556A:
    goto loc_00745576;
loc_00745571:
loc_00745576:
    Arg1 = (Arg1) * ((int32_t)(v_stack_m19C) + (int32_t)(v_stack_m1A0) + 3 * 2);
    Arg1 = (Arg1) + (v_stack_m180);
    result = KiCopyAffinityEx(Arg1, *(uint16_t *)(Arg1 + 0x2), v_stack_m170, v_rip - 7623116);
    Arg1 = (Arg1) * ((int32_t)(v_stack_m19C) + (int32_t)(v_stack_m1A0) + 10 * 2);
    Arg1 = (Arg1) + (v_stack_m180);
    result = KiCopyAffinityEx(Arg1, *(uint16_t *)(Arg1 + 0x2), v_stack_m170, v_rip - 7623116);
loc_007455B5:
    Arg1 = (Arg1) * ((int32_t)(v_stack_m19C) + (int32_t)(v_stack_m1A0) + 17 * 2);
    Arg1 = (Arg1) + (v_stack_m180);
    result = KiCopyAffinityEx(Arg1, *(uint16_t *)(Arg1 + 0x2), v_stack_m168, v_rip - 7623116);
loc_007455D0:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, *(uint16_t *)(Arg1 + 0x2), v_stack_m168, v_rip - 7623116);
    local_rsp = (local_rsp) + (432);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg6` | `+ 0x4` | `32` | `R` |
| `Arg6` | `+ 0x8` | `64` | `R` |
| `Arg6` | `+ 0x18 + r13*4` | `8` | `R` |
| `Arg6` | `+ 0x18 + rax*4` | `8` | `R` |
| `Arg6` | `+ 0x18 + rsi*4` | `8` | `R` |
| `Arg6` | `+ 0x19 + r13*4` | `8` | `R` |
| `Arg6` | `+ 0x19 + rax*4` | `8` | `R` |
| `Arg6` | `+ 0x1A + rax*4` | `8` | `R` |
| `Arg6` | `+ 0x1B + rax*4` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0074508C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
