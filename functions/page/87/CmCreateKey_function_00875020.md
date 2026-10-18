# CmCreateKey

- RVA: `0x00875020`–`0x008755F0` (길이 `1,488` bytes)
- VA: `0x0000000140875020`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0006C960`
- 디코드: `342`개 명령, `1,488/1,488` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **19**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x008750E9` → [CmpAcquireShutdownRundown](../../pagecmrc/BC/CmpAcquireShutdownRundown_function_00BC9400.md) (function, `0x00BC9400`)
- `0x008751B8` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00875203` → [CmpAllocateTransientPoolWithQuota](../../text/46/CmpAllocateTransientPoolWithQuota_function_00461190.md) (function, `0x00461190`)
- `0x0087522A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008752B7` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x008752E2` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x0087537B` → [CmpAllocateParseContext](CmpAllocateParseContext_function_008767B4.md) (function, `0x008767B4`)
- `0x008753C9` → [PsGetCurrentSilo](../../text/40/PsGetCurrentSilo_function_004094A0.md) (function, `0x004094A0`)
- `0x008753F5` → [ObOpenObjectByNameEx](../89/ObOpenObjectByNameEx_function_0089A8A0.md) (function, `0x0089A8A0`)
- `0x00875441` → [ObCloseHandle](../8A/ObCloseHandle_function_008A1870.md) (function, `0x008A1870`)
- `0x00875475` → [CmpFreeParseContext](CmpFreeParseContext_function_008768E0.md) (function, `0x008768E0`)
- `0x0087547F` → [CmpReleaseShutdownRundown](../../pagecmrc/BC/CmpReleaseShutdownRundown_function_00BC9880.md) (function, `0x00BC9880`)
- `0x00875491` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x008754DD` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x008754F1` → [EtwGetKernelTraceTimestamp](../../text/39/EtwGetKernelTraceTimestamp_function_0039FC50.md) (function, `0x0039FC50`)
- `0x00875536` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x00875554` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00875588` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008755C2` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [CmCreateKeyCallout](../A6/CmCreateKeyCallout_function_00A629A0.md) at `0x00A629D6`

### Static image references
- `0x00875035` → RVA `0x00E0A740` (`.data`; read)
- `0x008750C4` → RVA `0x00FD8008` (`PAGEDATA`; read)
- `0x008753C2` → RVA `0x00FC6AC0` (`ALMOSTRO`; read)
- `0x00875592` → RVA `0x00FD9A67` (`PAGEDATA`; read)
- `0x008755A0` → RVA `0x00F0C8B0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **11**
  - `0x008750E9` → [CmpAcquireShutdownRundown](../../pagecmrc/BC/CmpAcquireShutdownRundown_function_00BC9400.md) (`PAGE` → `PAGECMRC`)
  - `0x00875203` → [CmpAllocateTransientPoolWithQuota](../../text/46/CmpAllocateTransientPoolWithQuota_function_00461190.md) (`PAGE` → `.text`)
  - `0x0087522A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008753C9` → [PsGetCurrentSilo](../../text/40/PsGetCurrentSilo_function_004094A0.md) (`PAGE` → `.text`)
  - `0x0087547F` → [CmpReleaseShutdownRundown](../../pagecmrc/BC/CmpReleaseShutdownRundown_function_00BC9880.md) (`PAGE` → `PAGECMRC`)
  - `0x00875491` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x008754DD` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x008754F1` → [EtwGetKernelTraceTimestamp](../../text/39/EtwGetKernelTraceTimestamp_function_0039FC50.md) (`PAGE` → `.text`)
  - `0x00875554` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00875588` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008755C2` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0087559A` → [sub_00B1796C](../B1/Unknown_function_00B1796C.md) (`tail-transfer`)
  - `0x008755A8` → [sub_00B1796C](../B1/Unknown_function_00B1796C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00875020  4C 8B DC                        mov r11, rsp
00875023  53                              push rbx
00875024  56                              push rsi
00875025  57                              push rdi
00875026  41 54                           push r12
00875028  41 55                           push r13
0087502A  41 56                           push r14
0087502C  41 57                           push r15
0087502E  48 81 EC 10 01 00 00            sub rsp, 0x110
00875035  48 8B 05 04 57 59 00            mov rax, qword ptr [rip + 0x595704]
0087503C  48 33 C4                        xor rax, rsp
0087503F  48 89 84 24 08 01 00 00         mov qword ptr [rsp + 0x108], rax
00875047  4D 8B E8                        mov r13, r8
0087504A  8B DA                           mov ebx, edx
0087504C  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
00875051  4C 8B A4 24 80 01 00 00         mov r12, qword ptr [rsp + 0x180]
00875059  4C 89 64 24 60                  mov qword ptr [rsp + 0x60], r12
0087505E  4C 8B B4 24 70 01 00 00         mov r14, qword ptr [rsp + 0x170]
00875066  48 89 8C 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rcx
0087506E  4C 89 84 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], r8
00875076  4C 89 A4 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], r12
0087507E  33 FF                           xor edi, edi
00875080  89 7C 24 44                     mov dword ptr [rsp + 0x44], edi
00875084  48 89 7C 24 50                  mov qword ptr [rsp + 0x50], rdi
00875089  0F 57 C0                        xorps xmm0, xmm0
0087508C  0F 11 84 24 B0 00 00 00         movups xmmword ptr [rsp + 0xb0], xmm0
00875094  0F 57 C9                        xorps xmm1, xmm1
00875097  0F 11 8C 24 A0 00 00 00         movups xmmword ptr [rsp + 0xa0], xmm1
0087509F  40 88 7C 24 41                  mov byte ptr [rsp + 0x41], dil
008750A4  49 89 BB 38 FF FF FF            mov qword ptr [r11 - 0xc8], rdi
008750AB  89 BC 24 C0 00 00 00            mov dword ptr [rsp + 0xc0], edi
008750B2  41 0F 11 43 A0                  movups xmmword ptr [r11 - 0x60], xmm0
008750B7  41 0F 11 43 B0                  movups xmmword ptr [r11 - 0x50], xmm0
008750BC  48 89 BC 24 88 00 00 00         mov qword ptr [rsp + 0x88], rdi
008750C4  48 39 3D 3D 2F 76 00            cmp qword ptr [rip + 0x762f3d], rdi
008750CB  0F 85 13 04 00 00               jne 0x1408754e4
008750D1  48 8B F7                        mov rsi, rdi
008750D4  8B C3                           mov eax, ebx
008750D6  25 00 03 00 00                  and eax, 0x300
008750DB  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
008750DF  81 E3 FF FC FF FF               and ebx, 0xfffffcff
008750E5  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
008750E9  E8 12 43 35 00                  call 0x140bc9400
008750EE  44 8A F8                        mov r15b, al
008750F1  88 44 24 40                     mov byte ptr [rsp + 0x40], al
008750F5  84 C0                           test al, al
008750F7  0F 84 95 04 00 00               je 0x140875592
008750FD  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00875106  8A 90 32 02 00 00               mov dl, byte ptr [rax + 0x232]
0087510C  88 54 24 42                     mov byte ptr [rsp + 0x42], dl
00875110  88 54 24 43                     mov byte ptr [rsp + 0x43], dl
00875114  41 BF 01 00 00 00               mov r15d, 1
0087511A  41 3A D7                        cmp dl, r15b
0087511D  0F 85 87 03 00 00               jne 0x1408754aa
00875123  48 BB 00 00 FF FF FF 7F 00 00   movabs rbx, 0x7fffffff0000
0087512D  4D 85 F6                        test r14, r14
00875130  74 58                           je 0x14087518a
00875132  0F 57 C0                        xorps xmm0, xmm0
00875135  0F 11 84 24 90 00 00 00         movups xmmword ptr [rsp + 0x90], xmm0
0087513D  48 8B CB                        mov rcx, rbx
00875140  4C 3B F3                        cmp r14, rbx
00875143  49 0F 42 CE                     cmovb rcx, r14
00875147  90                              nop
00875148  8B 01                           mov eax, dword ptr [rcx]
0087514A  89 84 24 90 00 00 00            mov dword ptr [rsp + 0x90], eax
00875151  4C 8B 61 08                     mov r12, qword ptr [rcx + 8]
00875155  4C 89 A4 24 98 00 00 00         mov qword ptr [rsp + 0x98], r12
0087515D  0F 28 84 24 90 00 00 00         movaps xmm0, xmmword ptr [rsp + 0x90]
00875165  66 0F 7F 84 24 A0 00 00 00      movdqa xmmword ptr [rsp + 0xa0], xmm0
0087516E  66 0F 7E C2                     movd edx, xmm0
00875172  66 85 D2                        test dx, dx
00875175  75 47                           jne 0x1408751be
00875177  41 84 D7                        test r15b, dl
0087517A  0F 85 3C 01 00 00               jne 0x1408752bc
00875180  66 85 D2                        test dx, dx
00875183  75 6B                           jne 0x1408751f0
00875185  4C 8B 64 24 60                  mov r12, qword ptr [rsp + 0x60]
0087518A  48 8B C3                        mov rax, rbx
0087518D  48 39 5C 24 70                  cmp qword ptr [rsp + 0x70], rbx
00875192  48 0F 42 44 24 70               cmovb rax, qword ptr [rsp + 0x70]
00875198  48 89 38                        mov qword ptr [rax], rdi
0087519B  4D 85 E4                        test r12, r12
0087519E  74 0E                           je 0x1408751ae
008751A0  48 8B CB                        mov rcx, rbx
008751A3  4C 3B E3                        cmp r12, rbx
008751A6  49 0F 42 CC                     cmovb rcx, r12
008751AA  8B 01                           mov eax, dword ptr [rcx]
008751AC  89 01                           mov dword ptr [rcx], eax
008751AE  41 F6 C5 03                     test r13b, 3
008751B2  0F 84 84 00 00 00               je 0x14087523c
008751B8  E8 13 4E 02 00                  call 0x140899fd0
008751BD  CC                              int3
008751BE  45 84 E7                        test r15b, r12b
008751C1  0F 85 F0 00 00 00               jne 0x1408752b7
008751C7  0F B7 C2                        movzx eax, dx
008751CA  4E 8D 04 20                     lea r8, [rax + r12]
008751CE  4A 8D 0C 20                     lea rcx, [rax + r12]
008751D2  48 3B CB                        cmp rcx, rbx
008751D5  77 05                           ja 0x1408751dc
008751D7  4D 3B C4                        cmp r8, r12
008751DA  73 9B                           jae 0x140875177
008751DC  8A 03                           mov al, byte ptr [rbx]
008751DE  4C 8B A4 24 98 00 00 00         mov r12, qword ptr [rsp + 0x98]
008751E6  0F B7 94 24 90 00 00 00         movzx edx, word ptr [rsp + 0x90]
008751EE  EB 87                           jmp 0x140875177
008751F0  0F B7 C2                        movzx eax, dx
008751F3  48 89 84 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rax
008751FB  41 B8 43 4D 63 78               mov r8d, 0x78634d43
00875201  8B D0                           mov edx, eax
00875203  E8 88 BF BE FF                  call 0x140461190
00875208  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
00875210  48 85 C0                        test rax, rax
00875213  0F 84 B6 00 00 00               je 0x1408752cf
00875219  4C 8B 84 24 C8 00 00 00         mov r8, qword ptr [rsp + 0xc8]
00875221  49 8B D4                        mov rdx, r12
00875224  4C 8B F0                        mov r14, rax
00875227  48 8B C8                        mov rcx, rax
0087522A  E8 11 16 E5 FF                  call 0x1406c6840
0087522F  4C 89 B4 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], r14
00875237  E9 49 FF FF FF                  jmp 0x140875185
0087523C  48 8B C3                        mov rax, rbx
0087523F  4C 3B EB                        cmp r13, rbx
00875242  49 0F 42 C5                     cmovb rax, r13
00875246  90                              nop
00875247  8A 00                           mov al, byte ptr [rax]
00875249  49 8B 4D 10                     mov rcx, qword ptr [r13 + 0x10]
0087524D  0F 57 C0                        xorps xmm0, xmm0
00875250  0F 11 44 24 60                  movups xmmword ptr [rsp + 0x60], xmm0
00875255  48 3B CB                        cmp rcx, rbx
00875258  48 0F 43 CB                     cmovae rcx, rbx
0087525C  90                              nop
0087525D  8B 01                           mov eax, dword ptr [rcx]
0087525F  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
00875263  48 8B 51 08                     mov rdx, qword ptr [rcx + 8]
00875267  48 89 54 24 68                  mov qword ptr [rsp + 0x68], rdx
0087526C  0F 28 44 24 60                  movaps xmm0, xmmword ptr [rsp + 0x60]
00875271  66 0F 7F 84 24 B0 00 00 00      movdqa xmmword ptr [rsp + 0xb0], xmm0
0087527A  66 0F 7E C0                     movd eax, xmm0
0087527E  66 85 C0                        test ax, ax
00875281  74 1A                           je 0x14087529d
00875283  41 84 D7                        test r15b, dl
00875286  75 5A                           jne 0x1408752e2
00875288  0F B7 C0                        movzx eax, ax
0087528B  4C 8D 04 10                     lea r8, [rax + rdx]
0087528F  48 8D 0C 10                     lea rcx, [rax + rdx]
00875293  48 3B CB                        cmp rcx, rbx
00875296  77 4F                           ja 0x1408752e7
00875298  4C 3B C2                        cmp r8, rdx
0087529B  72 4A                           jb 0x1408752e7
0087529D  44 84 7C 24 60                  test byte ptr [rsp + 0x60], r15b
008752A2  74 47                           je 0x1408752eb
008752A4  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008752A9  89 5C 24 44                     mov dword ptr [rsp + 0x44], ebx
008752AD  44 8A 7C 24 40                  mov r15b, byte ptr [rsp + 0x40]
008752B2  E9 99 01 00 00                  jmp 0x140875450
008752B7  E8 14 4D 02 00                  call 0x140899fd0
008752BC  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008752C1  89 5C 24 44                     mov dword ptr [rsp + 0x44], ebx
008752C5  44 8A 7C 24 40                  mov r15b, byte ptr [rsp + 0x40]
008752CA  E9 81 01 00 00                  jmp 0x140875450
008752CF  BB 9A 00 00 C0                  mov ebx, 0xc000009a
008752D4  89 5C 24 44                     mov dword ptr [rsp + 0x44], ebx
008752D8  44 8A 7C 24 40                  mov r15b, byte ptr [rsp + 0x40]
008752DD  E9 6E 01 00 00                  jmp 0x140875450
008752E2  E8 E9 4C 02 00                  call 0x140899fd0
008752E7  8A 03                           mov al, byte ptr [rbx]
008752E9  EB B2                           jmp 0x14087529d
008752EB  49 8B 4D 08                     mov rcx, qword ptr [r13 + 8]
008752EF  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
008752F4  8B 5C 24 44                     mov ebx, dword ptr [rsp + 0x44]
008752F8  44 8B 74 24 48                  mov r14d, dword ptr [rsp + 0x48]
008752FD  EB 50                           jmp 0x14087534f
008752FF  8B D8                           mov ebx, eax
00875301  48 83 A4 24 B8 00 00 00 00      and qword ptr [rsp + 0xb8], 0
0087530A  33 C0                           xor eax, eax
0087530C  66 89 84 24 B0 00 00 00         mov word ptr [rsp + 0xb0], ax
00875314  89 5C 24 44                     mov dword ptr [rsp + 0x44], ebx
00875318  33 FF                           xor edi, edi
0087531A  44 8D 78 01                     lea r15d, [rax + 1]
0087531E  8A 44 24 43                     mov al, byte ptr [rsp + 0x43]
00875322  88 44 24 42                     mov byte ptr [rsp + 0x42], al
00875326  8B F7                           mov esi, edi
00875328  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
0087532D  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
00875335  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0087533A  44 8B 74 24 48                  mov r14d, dword ptr [rsp + 0x48]
0087533F  4C 8B AC 24 D8 00 00 00         mov r13, qword ptr [rsp + 0xd8]
00875347  4C 8B A4 24 E0 00 00 00         mov r12, qword ptr [rsp + 0xe0]
0087534F  85 DB                           test ebx, ebx
00875351  0F 88 8F 02 00 00               js 0x1408755e6
00875357  48 83 3D A9 2C 76 00 00         cmp qword ptr [rip + 0x762ca9], 0
0087535F  0F 85 96 01 00 00               jne 0x1408754fb
00875365  8B 9C 24 78 01 00 00            mov ebx, dword ptr [rsp + 0x178]
0087536C  8B C3                           mov eax, ebx
0087536E  25 1F 00 00 01                  and eax, 0x100001f
00875373  3B C3                           cmp eax, ebx
00875375  0F 85 5F 02 00 00               jne 0x1408755da
0087537B  E8 34 14 00 00                  call 0x1408767b4
00875380  48 8B F0                        mov rsi, rax
00875383  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00875388  48 85 C0                        test rax, rax
0087538B  0F 84 50 02 00 00               je 0x1408755e1
00875391  8B 44 24 58                     mov eax, dword ptr [rsp + 0x58]
00875395  89 46 1C                        mov dword ptr [rsi + 0x1c], eax
00875398  89 5E 18                        mov dword ptr [rsi + 0x18], ebx
0087539B  44 89 3E                        mov dword ptr [rsi], r15d
0087539E  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
008753A6  48 89 46 08                     mov qword ptr [rsi + 8], rax
008753AA  0F B7 84 24 A0 00 00 00         movzx eax, word ptr [rsp + 0xa0]
008753B2  66 89 46 04                     mov word ptr [rsi + 4], ax
008753B6  48 8B 84 24 88 01 00 00         mov rax, qword ptr [rsp + 0x188]
008753BE  48 89 46 48                     mov qword ptr [rsi + 0x48], rax
008753C2  48 8B 1D F7 16 75 00            mov rbx, qword ptr [rip + 0x7516f7]
008753C9  E8 D2 40 B9 FF                  call 0x1404094a0
008753CE  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
008753D3  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
008753D8  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008753DD  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
008753E2  44 89 74 24 20                  mov dword ptr [rsp + 0x20], r14d
008753E7  45 33 C9                        xor r9d, r9d
008753EA  44 8A 44 24 42                  mov r8b, byte ptr [rsp + 0x42]
008753EF  48 8B D3                        mov rdx, rbx
008753F2  49 8B CD                        mov rcx, r13
008753F5  E8 A6 54 02 00                  call 0x14089a8a0
008753FA  8B D8                           mov ebx, eax
008753FC  0F B6 4C 24 41                  movzx ecx, byte ptr [rsp + 0x41]
00875401  85 C0                           test eax, eax
00875403  41 0F 49 CF                     cmovns ecx, r15d
00875407  88 4C 24 41                     mov byte ptr [rsp + 0x41], cl
0087540B  85 C0                           test eax, eax
0087540D  78 19                           js 0x140875428
0087540F  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
00875414  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00875419  48 89 01                        mov qword ptr [rcx], rax
0087541C  4D 85 E4                        test r12, r12
0087541F  74 07                           je 0x140875428
00875421  8B 46 20                        mov eax, dword ptr [rsi + 0x20]
00875424  41 89 04 24                     mov dword ptr [r12], eax
00875428  44 8A 7C 24 40                  mov r15b, byte ptr [rsp + 0x40]
0087542D  EB 21                           jmp 0x140875450
0087542F  8B D8                           mov ebx, eax
00875431  80 7C 24 41 00                  cmp byte ptr [rsp + 0x41], 0
00875436  74 0E                           je 0x140875446
00875438  8A 54 24 43                     mov dl, byte ptr [rsp + 0x43]
0087543C  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00875441  E8 2A C4 02 00                  call 0x1408a1870
00875446  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
0087544B  44 8A 7C 24 40                  mov r15b, byte ptr [rsp + 0x40]
00875450  48 8B 05 B1 2B 76 00            mov rax, qword ptr [rip + 0x762bb1]
00875457  48 85 C0                        test rax, rax
0087545A  0F 85 FE 00 00 00               jne 0x14087555e
00875460  4C 8B B4 24 80 00 00 00         mov r14, qword ptr [rsp + 0x80]
00875468  4D 85 F6                        test r14, r14
0087546B  75 6D                           jne 0x1408754da
0087546D  48 85 F6                        test rsi, rsi
00875470  74 08                           je 0x14087547a
00875472  48 8B CE                        mov rcx, rsi
00875475  E8 66 14 00 00                  call 0x1408768e0
0087547A  45 84 FF                        test r15b, r15b
0087547D  74 05                           je 0x140875484
0087547F  E8 FC 43 35 00                  call 0x140bc9880
00875484  8B C3                           mov eax, ebx
00875486  48 8B 8C 24 08 01 00 00         mov rcx, qword ptr [rsp + 0x108]
0087548E  48 33 CC                        xor rcx, rsp
00875491  E8 AA 71 E3 FF                  call 0x1406ac640
00875496  48 81 C4 10 01 00 00            add rsp, 0x110
0087549D  41 5F                           pop r15
0087549F  41 5E                           pop r14
008754A1  41 5D                           pop r13
008754A3  41 5C                           pop r12
008754A5  5F                              pop rdi
008754A6  5E                              pop rsi
008754A7  5B                              pop rbx
008754A8  C3                              ret
008754A9  CC                              int3
008754AA  4D 85 F6                        test r14, r14
008754AD  0F 85 15 01 00 00               jne 0x1408755c8
008754B3  49 8B 45 10                     mov rax, qword ptr [r13 + 0x10]
008754B7  0F 10 00                        movups xmm0, xmmword ptr [rax]
008754BA  F3 0F 7F 84 24 B0 00 00 00      movdqu xmmword ptr [rsp + 0xb0], xmm0
008754C3  49 8B 4D 08                     mov rcx, qword ptr [r13 + 8]
008754C7  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
008754CC  8B 5C 24 44                     mov ebx, dword ptr [rsp + 0x44]
008754D0  44 8B 74 24 48                  mov r14d, dword ptr [rsp + 0x48]
008754D5  E9 75 FE FF FF                  jmp 0x14087534f
008754DA  49 8B CE                        mov rcx, r14
008754DD  E8 9E 08 C0 FF                  call 0x140475d80
008754E2  EB 89                           jmp 0x14087546d
008754E4  BA 00 00 02 00                  mov edx, 0x20000
008754E9  48 8D 8C 24 E8 00 00 00         lea rcx, [rsp + 0xe8]
008754F1  E8 5A A7 B2 FF                  call 0x14039fc50
008754F6  E9 D6 FB FF FF                  jmp 0x1408750d1
008754FB  48 85 C9                        test rcx, rcx
008754FE  0F 84 61 FE FF FF               je 0x140875365
00875504  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0087550D  44 8A 88 32 02 00 00            mov r9b, byte ptr [rax + 0x232]
00875514  4C 8B 05 A5 15 75 00            mov r8, qword ptr [rip + 0x7515a5]
0087551B  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
00875520  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
00875525  48 8D 44 24 60                  lea rax, [rsp + 0x60]
0087552A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0087552F  33 D2                           xor edx, edx
00875531  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00875536  E8 75 38 FF FF                  call 0x140868db0
0087553B  85 C0                           test eax, eax
0087553D  0F 88 22 FE FF FF               js 0x140875365
00875543  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00875548  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
0087554C  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
00875554  E8 F7 3D A8 FF                  call 0x1402f9350
00875559  E9 07 FE FF FF                  jmp 0x140875365
0087555E  48 8D 8C 24 B0 00 00 00         lea rcx, [rsp + 0xb0]
00875566  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
0087556B  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00875573  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00875578  45 33 C9                        xor r9d, r9d
0087557B  44 8B C3                        mov r8d, ebx
0087557E  48 8D 94 24 E8 00 00 00         lea rdx, [rsp + 0xe8]
00875586  B1 0A                           mov cl, 0xa
00875588  E8 43 55 E4 FF                  call 0x1406baad0
0087558D  E9 CE FE FF FF                  jmp 0x140875460
00875592  8A 05 CF 44 76 00               mov al, byte ptr [rip + 0x7644cf]
00875598  84 C0                           test al, al
0087559A  0F 84 CC 23 2A 00               je 0x140b1796c
008755A0  8B 05 0A 73 69 00               mov eax, dword ptr [rip + 0x69730a]
008755A6  A8 08                           test al, 8
008755A8  0F 84 BE 23 2A 00               je 0x140b1796c
008755AE  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
008755B3  4D 8B CD                        mov r9, r13
008755B6  BA 0E 00 00 00                  mov edx, 0xe
008755BB  8D 4A 43                        lea ecx, [rdx + 0x43]
008755BE  44 8D 42 F3                     lea r8d, [rdx - 0xd]
008755C2  E8 99 80 C8 FF                  call 0x1404fd660
008755C7  CC                              int3
008755C8  41 0F 10 06                     movups xmm0, xmmword ptr [r14]
008755CC  F3 0F 7F 84 24 A0 00 00 00      movdqu xmmword ptr [rsp + 0xa0], xmm0
008755D5  E9 D9 FE FF FF                  jmp 0x1408754b3
008755DA  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008755DF  EB 05                           jmp 0x1408755e6
008755E1  BB 9A 00 00 C0                  mov ebx, 0xc000009a
008755E6  44 8A 7C 24 40                  mov r15b, byte ptr [rsp + 0x40]
008755EB  E9 60 FE FF FF                  jmp 0x140875450
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmCreateKey(__int64 a1, int a2, __int64 a3, int a4, __int64 a5, unsigned int a6, __int64 a7, __int64 a8)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned int v_stack_m100;
    unsigned int v_stack_m104;
    unsigned __int8 v_stack_m105;
    unsigned __int8 v_stack_m106;
    unsigned __int8 v_stack_m107;
    unsigned __int8 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned int v_stack_m128;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned int v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int8 v_stack_p40;
    unsigned int v_stack_p44;
    unsigned int v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p88;
    unsigned __int64 v_stack_pA0;
    unsigned __int64 v_stack_pB0;
    unsigned __int64 v_stack_pE8;

    v_rsp = (v_rsp) - (272);
    result = (*(unsigned __int64 *)(v_rip + 5854980)) ^ (v_rsp);
    v_stack_m40 = result;
    v_stack_mD8 = a1;
    v_stack_mE8 = a7;
    v_stack_m78 = a1;
    v_stack_m70 = a3;
    v_stack_m68 = a7;
    v_rdi = 0;
    v_stack_m104 = 0;
    v_stack_mF8 = 0;
    v_stack_m98 = v_xmm0;
    v_stack_mA8 = v_xmm1;
    v_stack_m107 = 0;
    *(unsigned __int64 *)(v_rsp - 200) = 0;
    v_stack_m88 = 0;
    *(unsigned __int64 *)(v_rsp - 96) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 80) = v_xmm0;
    v_stack_mC0 = 0;
    if ((*(unsigned __int64 *)(v_rip + 7745341)) != 0) goto loc_008754E4;
loc_008750D1:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) & (768));
    v_stack_mF0 = (unsigned int)(result);
    v_rbx = (unsigned int)(((unsigned int)(a2)) & (0xFFFFFCFFULL));
    v_stack_m100 = (unsigned int)(v_rbx);
    result = CmpAcquireShutdownRundown(a1, a2, a3, a4);
    v_stack_m108 = (unsigned __int8)(result);
    if ((unsigned __int8)(result) == 0) goto loc_00875592;
    v_stack_m106 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_stack_m105 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562))) != 1) goto loc_008754AA;
    if (a5 == 0) goto loc_0087518A;
    v_stack_mB8 = v_xmm0;
    a1 = v_rbx;
    if (a5 < v_rbx) { a1 = a5; }
    v_stack_mB8 = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    v_stack_mB0 = *(unsigned __int64 *)(a1 + 8);
    v_stack_mA8 = v_xmm0;
    if ((unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) != 0) goto loc_008751BE;
loc_00875177:
    if (((1) & ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)))) != 0) goto loc_008752BC;
    if ((unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) != 0) goto loc_008751F0;
loc_00875185:
loc_0087518A:
    result = v_rbx;
    if (v_stack_mD8 < v_rbx) { result = v_stack_mD8; }
    *(unsigned __int64 *)(result) = 0;
    if (v_stack_mE8 != 0) {
        a1 = v_rbx;
        if (v_stack_mE8 < v_rbx) { a1 = v_stack_mE8; }
        result = *(unsigned int *)(a1);
        *(unsigned int *)(a1) = (unsigned int)(result);
    }
    if ((((unsigned __int8)(a3)) & (3)) == 0) goto loc_0087523C;
    result = ExRaiseDatatypeMisalignment(a1, *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562), a3, a4);
loc_008751BE:
    if (((1) & ((unsigned __int8)(v_stack_mE8))) != 0) goto loc_008752B7;
    if (((unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) + v_stack_mE8 * 1) > v_rbx) goto loc_008751DC;
    if (((unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) + v_stack_mE8 * 1) >= v_stack_mE8) goto loc_00875177;
loc_008751DC:
    goto loc_00875177;
loc_008751F0:
    v_stack_m80 = (unsigned __int16)(v_stack_mB8);
    result = CmpAllocateTransientPoolWithQuota((unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) + v_stack_mE8 * 1, (unsigned int)((unsigned int)((unsigned __int16)(v_stack_mB8))), (unsigned int)(0x78634D43ULL), a4);
    v_stack_mC8 = result;
    if (result == 0) goto loc_008752CF;
    result = memcpy(result, v_stack_mB0, v_stack_m80, a4);
    v_stack_mA0 = result;
    goto loc_00875185;
loc_0087523C:
    result = v_rbx;
    if (a3 < v_rbx) { result = a3; }
    v_stack_mE8 = v_xmm0;
    a1 = *(unsigned __int64 *)(a3 + 16);
    if ((*(unsigned __int64 *)(a3 + 16)) >= v_rbx) { a1 = v_rbx; }
    v_stack_mE8 = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    v_stack_mE0 = *(unsigned __int64 *)(a1 + 8);
    v_stack_m98 = v_xmm0;
    if ((unsigned __int16)((unsigned int)(*(unsigned int *)(a1))) == 0) goto loc_0087529D;
    if (((1) & ((unsigned __int8)(*(unsigned __int64 *)(a1 + 8)))) != 0) goto loc_008752E2;
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(a1))) + *(unsigned __int64 *)(a1 + 8) * 1) > v_rbx) goto loc_008752E7;
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(a1))) + *(unsigned __int64 *)(a1 + 8) * 1) < (*(unsigned __int64 *)(a1 + 8))) goto loc_008752E7;
loc_0087529D:
    if (((v_stack_mE8) & (1)) == 0) goto loc_008752EB;
    v_stack_m104 = (unsigned int)((unsigned int)(0xC000000DULL));
    goto loc_00875450;
loc_008752B7:
    result = ExRaiseDatatypeMisalignment((unsigned __int16)((unsigned int)(*(unsigned int *)(a1))) + *(unsigned __int64 *)(a1 + 8) * 1, *(unsigned __int64 *)(a1 + 8), (unsigned __int16)((unsigned int)(*(unsigned int *)(a1))) + *(unsigned __int64 *)(a1 + 8) * 1, a4);
loc_008752BC:
    v_stack_m104 = (unsigned int)((unsigned int)(0xC000000DULL));
    goto loc_00875450;
loc_008752CF:
    v_stack_m104 = (unsigned int)((unsigned int)(0xC000009AULL));
    goto loc_00875450;
loc_008752E2:
    result = ExRaiseDatatypeMisalignment((unsigned __int16)((unsigned int)(*(unsigned int *)(a1))) + *(unsigned __int64 *)(a1 + 8) * 1, *(unsigned __int64 *)(a1 + 8), (unsigned __int16)((unsigned int)(*(unsigned int *)(a1))) + *(unsigned __int64 *)(a1 + 8) * 1, a4);
loc_008752E7:
    goto loc_0087529D;
loc_008752EB:
    v_stack_mF8 = *(unsigned __int64 *)(a3 + 8);
    goto loc_0087534F;
loc_0087534F:
    if (sign_flag) goto loc_008755E6;
    if ((*(unsigned __int64 *)(v_rip + 7744681)) != 0) goto loc_008754FB;
loc_00875365:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a6)))) & (0x100001FULL));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(a6)))) goto loc_008755DA;
    result = CmpAllocateParseContext(*(unsigned __int64 *)(a3 + 8), *(unsigned __int64 *)(a1 + 8), (unsigned __int16)((unsigned int)(*(unsigned int *)(a1))) + *(unsigned __int64 *)(a1 + 8) * 1, a4);
    v_stack_mD0 = result;
    if (result == 0) goto loc_008755E1;
    *(unsigned int *)(result + 28) = (unsigned int)((unsigned int)(v_stack_mF0));
    *(unsigned int *)(result + 24) = (unsigned int)((unsigned int)(a6));
    *(unsigned int *)(result) = (unsigned int)(v_stack_m108);
    *(unsigned __int64 *)(result + 8) = v_stack_mA0;
    *(unsigned __int16 *)(result + 4) = (unsigned __int16)(v_stack_mA8);
    *(unsigned __int64 *)(result + 72) = a8;
    result = PsGetCurrentSilo(*(unsigned __int64 *)(a3 + 8), *(unsigned __int64 *)(a1 + 8), (unsigned __int16)((unsigned int)(*(unsigned int *)(a1))) + *(unsigned __int64 *)(a1 + 8) * 1, a4);
    v_stack_m110 = v_stack_mF8;
    v_stack_m118 = result;
    v_stack_m120 = result;
    v_stack_m128 = (unsigned int)((unsigned int)(v_stack_m100));
    a4 = 0;
    result = ObOpenObjectByNameEx(a3, *(unsigned __int64 *)(v_rip + 7673591), v_stack_m106, a4);
    a1 = v_stack_m107;
    if (!sign_flag) { a1 = (unsigned int)(v_stack_m108); }
    v_stack_m107 = (unsigned __int8)(a1);
    if (sign_flag) goto loc_00875428;
    *(unsigned __int64 *)(v_stack_mD8) = v_stack_mF8;
    result = v_stack_mF8;
    if (v_stack_mB0 != 0) {
        result = *(unsigned int *)(result + 32);
        *(unsigned int *)(v_stack_mB0) = (unsigned int)(result);
    }
    goto loc_00875450;
loc_00875450:
    if (*(unsigned __int64 *)(v_rip + 7744433) != 0) goto loc_0087555E;
loc_00875460:
    if (v_stack_mC8 != 0) goto loc_008754DA;
loc_0087546D:
    result = *(unsigned __int64 *)(v_rip + 7744433);
    if (result != 0) {
        a1 = result;
        result = CmpFreeParseContext(a1, *(unsigned __int64 *)(v_rip + 7673591), v_stack_m106, a4);
    }
    if ((unsigned __int8)(v_stack_m108) != 0) {
        result = CmpReleaseShutdownRundown(a1, *(unsigned __int64 *)(v_rip + 7673591), v_stack_m106, a4);
    }
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, *(unsigned __int64 *)(v_rip + 7673591), v_stack_m106, a4);
    v_rsp = (v_rsp) + (272);
    return result;
loc_008754AA:
    if (v_stack_mC8 != 0) goto loc_008755C8;
loc_008754B3:
    v_stack_pB0 = v_xmm0;
    v_stack_p50 = *(unsigned __int64 *)(a3 + 8);
    goto loc_0087534F;
loc_008754DA:
    result = CmSiFreeMemory((unsigned int)(v_stack_p48), *(unsigned __int64 *)(v_rip + 7673591), v_stack_m106, a4);
    goto loc_0087546D;
loc_008754E4:
    result = EtwGetKernelTraceTimestamp(v_stack_pE8, (unsigned int)(0x20000ULL), v_stack_m106, a4);
    goto loc_008750D1;
loc_008754FB:
    if (v_stack_pE8 == 0) goto loc_00875365;
    v_stack_p60 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_p60;
    a2 = 0;
    result = ObReferenceObjectByHandle(v_stack_p50, a2, *(unsigned __int64 *)(v_rip + 7673253), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if (sign_flag) goto loc_00875365;
    v_stack_p88 = *(unsigned __int64 *)(v_stack_p60 + 8);
    result = ObfDereferenceObject(v_stack_p60, a2, *(unsigned __int64 *)(v_rip + 7673253), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    goto loc_00875365;
loc_0087555E:
    v_stack_p28 = v_stack_pB0;
    v_stack_p20 = v_stack_p88;
    a4 = 0;
    result = guard_dispatch_icall(10, v_stack_pE8, (unsigned int)((unsigned int)((unsigned int)(v_stack_p44))), a4);
    goto loc_00875460;
loc_00875592:
    v_stack_p20 = 0;
    result = KeBugCheckEx(14 + 67, 14, 14 - 13, a3);
loc_008755C8:
    v_stack_pA0 = v_xmm0;
    goto loc_008754B3;
loc_008755DA:
    goto loc_008755E6;
loc_008755E1:
loc_008755E6:
    goto loc_00875450;
}
```

## 5. (Beta) C Style

```c
int64_t CmCreateKey(int64_t Arg1, int32_t Arg2, void *Arg3, int32_t Arg4, int64_t Arg5, uint32_t Arg6, int64_t Arg7, int64_t Arg8)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint32_t v_stack_m100;
    uint32_t v_stack_m104;
    uint8_t v_stack_m105;
    uint8_t v_stack_m106;
    uint8_t v_stack_m107;
    uint8_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint32_t v_stack_m128;
    uint64_t v_stack_m40;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint32_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint32_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint8_t v_stack_p40;
    uint32_t v_stack_p44;
    uint32_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p60;
    uint64_t v_stack_p88;
    uint64_t v_stack_pA0;
    uint64_t v_stack_pB0;
    uint64_t v_stack_pE8;

    local_rsp = (local_rsp) - (272);
    result = (*(uint64_t *)(v_rip + 0x595704)) ^ (local_rsp);
    v_stack_m40 = result;
    v_stack_mD8 = Arg1;
    v_stack_mE8 = Arg7;
    v_stack_m78 = Arg1;
    v_stack_m70 = Arg3;
    v_stack_m68 = Arg7;
    local_rdi = 0;
    v_stack_m104 = 0;
    v_stack_mF8 = 0;
    v_stack_m98 = v_xmm0;
    v_stack_mA8 = v_xmm1;
    v_stack_m107 = 0;
    *(uint64_t *)(local_rsp - 0xC8) = 0;
    v_stack_m88 = 0;
    *(uint64_t *)(local_rsp - 0x60) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x50) = v_xmm0;
    v_stack_mC0 = 0;
    if ((*(uint64_t *)(v_rip + 0x762F3D)) != 0) goto loc_008754E4;
loc_008750D1:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) & (768));
    v_stack_mF0 = (uint32_t)(result);
    local_rbx = (uint32_t)(((uint32_t)(Arg2)) & (0xFFFFFCFFULL));
    v_stack_m100 = (uint32_t)(local_rbx);
    result = CmpAcquireShutdownRundown(Arg1, Arg2, Arg3, Arg4);
    v_stack_m108 = (uint8_t)(result);
    if ((uint8_t)(result) == 0) goto loc_00875592;
    v_stack_m106 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    v_stack_m105 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232))) != 1) goto loc_008754AA;
    if (Arg5 == 0) goto loc_0087518A;
    v_stack_mB8 = v_xmm0;
    Arg1 = local_rbx;
    if (Arg5 < local_rbx) { Arg1 = Arg5; }
    v_stack_mB8 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1)));
    v_stack_mB0 = *(uint64_t *)(Arg1 + 0x8);
    v_stack_mA8 = v_xmm0;
    if ((uint16_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) != 0) goto loc_008751BE;
loc_00875177:
    if (((1) & ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)))) != 0) goto loc_008752BC;
    if ((uint16_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) != 0) goto loc_008751F0;
loc_00875185:
loc_0087518A:
    result = local_rbx;
    if (v_stack_mD8 < local_rbx) { result = v_stack_mD8; }
    *(uint64_t *)(result) = 0;
    if (v_stack_mE8 != 0) {
        Arg1 = local_rbx;
        if (v_stack_mE8 < local_rbx) { Arg1 = v_stack_mE8; }
        result = *(uint32_t *)(Arg1);
        *(uint32_t *)(Arg1) = (uint32_t)(result);
    }
    if ((((uint8_t)(Arg3)) & (3)) == 0) goto loc_0087523C;
    result = ExRaiseDatatypeMisalignment(Arg1, *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232), Arg3, Arg4);
loc_008751BE:
    if (((1) & ((uint8_t)(v_stack_mE8))) != 0) goto loc_008752B7;
    if (((uint16_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) + v_stack_mE8 * 1) > local_rbx) goto loc_008751DC;
    if (((uint16_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) + v_stack_mE8 * 1) >= v_stack_mE8) goto loc_00875177;
loc_008751DC:
    goto loc_00875177;
loc_008751F0:
    v_stack_m80 = (uint16_t)(v_stack_mB8);
    result = CmpAllocateTransientPoolWithQuota((uint16_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) + v_stack_mE8 * 1, (uint32_t)((uint32_t)((uint16_t)(v_stack_mB8))), (uint32_t)(0x78634D43ULL), Arg4);
    v_stack_mC8 = result;
    if (result == 0) goto loc_008752CF;
    result = memcpy(result, v_stack_mB0, v_stack_m80, Arg4);
    v_stack_mA0 = result;
    goto loc_00875185;
loc_0087523C:
    result = local_rbx;
    if (Arg3 < local_rbx) { result = Arg3; }
    v_stack_mE8 = v_xmm0;
    Arg1 = *(uint64_t *)(arg3 + 0x10);
    if ((*(uint64_t *)(arg3 + 0x10)) >= local_rbx) { Arg1 = local_rbx; }
    v_stack_mE8 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1)));
    v_stack_mE0 = *(uint64_t *)(Arg1 + 0x8);
    v_stack_m98 = v_xmm0;
    if ((uint16_t)((uint32_t)(*(uint32_t *)(Arg1))) == 0) goto loc_0087529D;
    if (((1) & ((uint8_t)(*(uint64_t *)(Arg1 + 0x8)))) != 0) goto loc_008752E2;
    if (((uint16_t)((uint32_t)(*(uint32_t *)(Arg1))) + *(uint64_t *)(Arg1 + 0x8) * 1) > local_rbx) goto loc_008752E7;
    if (((uint16_t)((uint32_t)(*(uint32_t *)(Arg1))) + *(uint64_t *)(Arg1 + 0x8) * 1) < (*(uint64_t *)(Arg1 + 0x8))) goto loc_008752E7;
loc_0087529D:
    if (((v_stack_mE8) & (1)) == 0) goto loc_008752EB;
    v_stack_m104 = (uint32_t)((uint32_t)(0xC000000DULL));
    goto loc_00875450;
loc_008752B7:
    result = ExRaiseDatatypeMisalignment((uint16_t)((uint32_t)(*(uint32_t *)(Arg1))) + *(uint64_t *)(Arg1 + 0x8) * 1, *(uint64_t *)(Arg1 + 0x8), (uint16_t)((uint32_t)(*(uint32_t *)(Arg1))) + *(uint64_t *)(Arg1 + 0x8) * 1, Arg4);
loc_008752BC:
    v_stack_m104 = (uint32_t)((uint32_t)(0xC000000DULL));
    goto loc_00875450;
loc_008752CF:
    v_stack_m104 = (uint32_t)((uint32_t)(0xC000009AULL));
    goto loc_00875450;
loc_008752E2:
    result = ExRaiseDatatypeMisalignment((uint16_t)((uint32_t)(*(uint32_t *)(Arg1))) + *(uint64_t *)(Arg1 + 0x8) * 1, *(uint64_t *)(Arg1 + 0x8), (uint16_t)((uint32_t)(*(uint32_t *)(Arg1))) + *(uint64_t *)(Arg1 + 0x8) * 1, Arg4);
loc_008752E7:
    goto loc_0087529D;
loc_008752EB:
    v_stack_mF8 = *(uint64_t *)(arg3 + 0x8);
    goto loc_0087534F;
loc_0087534F:
    if (sign_flag) goto loc_008755E6;
    if ((*(uint64_t *)(v_rip + 0x762CA9)) != 0) goto loc_008754FB;
loc_00875365:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg6)))) & (0x100001FULL));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(Arg6)))) goto loc_008755DA;
    result = CmpAllocateParseContext(*(uint64_t *)(arg3 + 0x8), *(uint64_t *)(Arg1 + 0x8), (uint16_t)((uint32_t)(*(uint32_t *)(Arg1))) + *(uint64_t *)(Arg1 + 0x8) * 1, Arg4);
    v_stack_mD0 = result;
    if (result == 0) goto loc_008755E1;
    *(uint32_t *)(result + 0x1C) = (uint32_t)((uint32_t)(v_stack_mF0));
    *(uint32_t *)(result + 0x18) = (uint32_t)((uint32_t)(Arg6));
    *(uint32_t *)(result) = (uint32_t)(v_stack_m108);
    *(uint64_t *)(result + 0x8) = v_stack_mA0;
    *(uint16_t *)(result + 0x4) = (uint16_t)(v_stack_mA8);
    *(uint64_t *)(result + 0x48) = Arg8;
    result = PsGetCurrentSilo(*(uint64_t *)(arg3 + 0x8), *(uint64_t *)(Arg1 + 0x8), (uint16_t)((uint32_t)(*(uint32_t *)(Arg1))) + *(uint64_t *)(Arg1 + 0x8) * 1, Arg4);
    v_stack_m110 = v_stack_mF8;
    v_stack_m118 = result;
    v_stack_m120 = result;
    v_stack_m128 = (uint32_t)((uint32_t)(v_stack_m100));
    Arg4 = 0;
    result = ObOpenObjectByNameEx(Arg3, *(uint64_t *)(v_rip + 0x7516F7), v_stack_m106, Arg4);
    Arg1 = v_stack_m107;
    if (!sign_flag) { Arg1 = (uint32_t)(v_stack_m108); }
    v_stack_m107 = (uint8_t)(Arg1);
    if (sign_flag) goto loc_00875428;
    *(uint64_t *)(v_stack_mD8) = v_stack_mF8;
    result = v_stack_mF8;
    if (v_stack_mB0 != 0) {
        result = *(uint32_t *)(result + 0x20);
        *(uint32_t *)(v_stack_mB0) = (uint32_t)(result);
    }
    goto loc_00875450;
loc_00875450:
    if (*(uint64_t *)(v_rip + 0x762BB1) != 0) goto loc_0087555E;
loc_00875460:
    if (v_stack_mC8 != 0) goto loc_008754DA;
loc_0087546D:
    result = *(uint64_t *)(v_rip + 0x762BB1);
    if (result != 0) {
        Arg1 = result;
        result = CmpFreeParseContext(Arg1, *(uint64_t *)(v_rip + 0x7516F7), v_stack_m106, Arg4);
    }
    if ((uint8_t)(v_stack_m108) != 0) {
        result = CmpReleaseShutdownRundown(Arg1, *(uint64_t *)(v_rip + 0x7516F7), v_stack_m106, Arg4);
    }
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, *(uint64_t *)(v_rip + 0x7516F7), v_stack_m106, Arg4);
    local_rsp = (local_rsp) + (272);
    return result;
loc_008754AA:
    if (v_stack_mC8 != 0) goto loc_008755C8;
loc_008754B3:
    v_stack_pB0 = v_xmm0;
    v_stack_p50 = *(uint64_t *)(arg3 + 0x8);
    goto loc_0087534F;
loc_008754DA:
    result = CmSiFreeMemory((uint32_t)(v_stack_p48), *(uint64_t *)(v_rip + 0x7516F7), v_stack_m106, Arg4);
    goto loc_0087546D;
loc_008754E4:
    result = EtwGetKernelTraceTimestamp(v_stack_pE8, (uint32_t)(0x20000ULL), v_stack_m106, Arg4);
    goto loc_008750D1;
loc_008754FB:
    if (v_stack_pE8 == 0) goto loc_00875365;
    v_stack_p60 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_p60;
    Arg2 = 0;
    result = ObReferenceObjectByHandle(v_stack_p50, Arg2, *(uint64_t *)(v_rip + 0x7515A5), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if (sign_flag) goto loc_00875365;
    v_stack_p88 = *(uint64_t *)(v_stack_p60 + 0x8);
    result = ObfDereferenceObject(v_stack_p60, Arg2, *(uint64_t *)(v_rip + 0x7515A5), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    goto loc_00875365;
loc_0087555E:
    v_stack_p28 = v_stack_pB0;
    v_stack_p20 = v_stack_p88;
    Arg4 = 0;
    result = guard_dispatch_icall(10, v_stack_pE8, (uint32_t)((uint32_t)((uint32_t)(v_stack_p44))), Arg4);
    goto loc_00875460;
loc_00875592:
    v_stack_p20 = 0;
    result = KeBugCheckEx(14 + 67, 14, 14 - 13, Arg3);
loc_008755C8:
    v_stack_pA0 = v_xmm0;
    goto loc_008754B3;
loc_008755DA:
    goto loc_008755E6;
loc_008755E1:
loc_008755E6:
    goto loc_00875450;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x8` | `64` | `R` |
| `Arg3` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00875020&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
