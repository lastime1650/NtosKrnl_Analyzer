# RtlApplyHotPatch

- RVA: `0x00B7528C`–`0x00B757E7` (길이 `1,371` bytes)
- VA: `0x0000000140B7528C`
- 실행 섹션: `PAGELK`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB640`
- 디코드: `328`개 명령, `1,371/1,371` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **12**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B7534A` → [RtlGetHotPatchSize](../../text/6A/RtlGetHotPatchSize_function_006AA1D0.md) (function, `0x006AA1D0`)
- `0x00B75496` → [RtlIsCodeInEcRanges](RtlIsCodeInEcRanges_function_00B757F0.md) (function, `0x00B757F0`)
- `0x00B754CF` → [RtlpDetermineHotPatchExtent](RtlpDetermineHotPatchExtent_function_00B75844.md) (function, `0x00B75844`)
- `0x00B754FC` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00B7563A` → [RtlpCheckFunctionPatchAppliedInOriginalImage](../../text/6A/RtlpCheckFunctionPatchAppliedInOriginalImage_function_006AA408.md) (function, `0x006AA408`)
- `0x00B7566F` → [RtlGetHpatEntryAddress](../../text/6A/RtlGetHpatEntryAddress_function_006AA1E8.md) (function, `0x006AA1E8`)
- `0x00B756A5` → [RtlPopulateHpatEntry](../../text/6A/RtlPopulateHpatEntry_function_006AA388.md) (function, `0x006AA388`)
- `0x00B756DA` → [RtlpApplyFunctionPatch](../../text/6A/RtlpApplyFunctionPatch_function_006AA3EC.md) (function, `0x006AA3EC`)
- `0x00B756F4` → [RtlGetHpatEntryAddress](../../text/6A/RtlGetHpatEntryAddress_function_006AA1E8.md) (function, `0x006AA1E8`)
- `0x00B75791` → [RtlFindClearBitsAndSet](../../text/3E/RtlFindClearBitsAndSet_function_003E0CD0.md) (function, `0x003E0CD0`)
- `0x00B757B6` → [RtlpRevertFunctionPatchFromUndoEntry](../../text/6A/RtlpRevertFunctionPatchFromUndoEntry_function_006AA20C.md) (function, `0x006AA20C`)
- `0x00B757C3` → [RtlFindClearBitsAndSet](../../text/3E/RtlFindClearBitsAndSet_function_003E0CD0.md) (function, `0x003E0CD0`)

### Direct callers
- [MiApplyHotPatchToDriverDataPages](../../page/80/MiApplyHotPatchToDriverDataPages_function_00801F18.md) at `0x00801FE2`
- [MiApplyImageHotPatch](../../page/80/MiApplyImageHotPatch_function_00802330.md) at `0x00802529`
- [MiApplyImageHotPatchRequest](../../page/80/MiApplyImageHotPatchRequest_function_008025AC.md) at `0x00802E16`
- [MiApplyImageHotPatchDpc](MiApplyImageHotPatchDpc_function_00B74A20.md) at `0x00B74B09`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **10**
  - `0x00B7534A` → [RtlGetHotPatchSize](../../text/6A/RtlGetHotPatchSize_function_006AA1D0.md) (`PAGELK` → `.text`)
  - `0x00B754FC` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGELK` → `.text`)
  - `0x00B7563A` → [RtlpCheckFunctionPatchAppliedInOriginalImage](../../text/6A/RtlpCheckFunctionPatchAppliedInOriginalImage_function_006AA408.md) (`PAGELK` → `.text`)
  - `0x00B7566F` → [RtlGetHpatEntryAddress](../../text/6A/RtlGetHpatEntryAddress_function_006AA1E8.md) (`PAGELK` → `.text`)
  - `0x00B756A5` → [RtlPopulateHpatEntry](../../text/6A/RtlPopulateHpatEntry_function_006AA388.md) (`PAGELK` → `.text`)
  - `0x00B756DA` → [RtlpApplyFunctionPatch](../../text/6A/RtlpApplyFunctionPatch_function_006AA3EC.md) (`PAGELK` → `.text`)
  - `0x00B756F4` → [RtlGetHpatEntryAddress](../../text/6A/RtlGetHpatEntryAddress_function_006AA1E8.md) (`PAGELK` → `.text`)
  - `0x00B75791` → [RtlFindClearBitsAndSet](../../text/3E/RtlFindClearBitsAndSet_function_003E0CD0.md) (`PAGELK` → `.text`)
  - `0x00B757B6` → [RtlpRevertFunctionPatchFromUndoEntry](../../text/6A/RtlpRevertFunctionPatchFromUndoEntry_function_006AA20C.md) (`PAGELK` → `.text`)
  - `0x00B757C3` → [RtlFindClearBitsAndSet](../../text/3E/RtlFindClearBitsAndSet_function_003E0CD0.md) (`PAGELK` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B7528C  48 8B C4                        mov rax, rsp
00B7528F  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
00B75293  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
00B75297  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
00B7529B  48 89 48 08                     mov qword ptr [rax + 8], rcx
00B7529F  55                              push rbp
00B752A0  53                              push rbx
00B752A1  56                              push rsi
00B752A2  57                              push rdi
00B752A3  41 54                           push r12
00B752A5  41 55                           push r13
00B752A7  41 56                           push r14
00B752A9  41 57                           push r15
00B752AB  48 8D 68 B9                     lea rbp, [rax - 0x47]
00B752AF  48 81 EC A8 00 00 00            sub rsp, 0xa8
00B752B6  83 A5 17 01 00 00 00            and dword ptr [rbp + 0x117], 0
00B752BD  48 8D 75 E7                     lea rsi, [rbp - 0x19]
00B752C1  48 8B 9D E7 00 00 00            mov rbx, qword ptr [rbp + 0xe7]
00B752C8  33 C0                           xor eax, eax
00B752CA  21 85 97 00 00 00               and dword ptr [rbp + 0x97], eax
00B752D0  45 8B D9                        mov r11d, r9d
00B752D3  48 21 45 CF                     and qword ptr [rbp - 0x31], rax
00B752D7  45 33 C9                        xor r9d, r9d
00B752DA  48 21 45 B7                     and qword ptr [rbp - 0x49], rax
00B752DE  4D 8B F0                        mov r14, r8
00B752E1  21 85 2F 01 00 00               and dword ptr [rbp + 0x12f], eax
00B752E7  45 33 C0                        xor r8d, r8d
00B752EA  48 21 45 AF                     and qword ptr [rbp - 0x51], rax
00B752EE  4C 8B D2                        mov r10, rdx
00B752F1  48 21 45 BF                     and qword ptr [rbp - 0x41], rax
00B752F5  0F 57 C0                        xorps xmm0, xmm0
00B752F8  48 21 85 27 01 00 00            and qword ptr [rbp + 0x127], rax
00B752FF  48 8B F9                        mov rdi, rcx
00B75302  48 21 45 DF                     and qword ptr [rbp - 0x21], rax
00B75306  48 89 45 F7                     mov qword ptr [rbp - 9], rax
00B7530A  48 8B 85 0F 01 00 00            mov rax, qword ptr [rbp + 0x10f]
00B75311  48 85 C0                        test rax, rax
00B75314  C6 45 77 00                     mov byte ptr [rbp + 0x77], 0
00B75318  0F 11 45 E7                     movups xmmword ptr [rbp - 0x19], xmm0
00B7531C  48 0F 45 F0                     cmovne rsi, rax
00B75320  4C 89 8D 1F 01 00 00            mov qword ptr [rbp + 0x11f], r9
00B75327  33 D2                           xor edx, edx
00B75329  44 89 85 C7 00 00 00            mov dword ptr [rbp + 0xc7], r8d
00B75330  48 89 75 C7                     mov qword ptr [rbp - 0x39], rsi
00B75334  89 95 0F 01 00 00               mov dword ptr [rbp + 0x10f], edx
00B7533A  48 85 DB                        test rbx, rbx
00B7533D  0F 84 38 04 00 00               je 0x140b7577b
00B75343  48 8B 8D DF 00 00 00            mov rcx, qword ptr [rbp + 0xdf]
00B7534A  E8 81 4E B3 FF                  call 0x1406aa1d0
00B7534F  8B D0                           mov edx, eax
00B75351  89 85 0F 01 00 00               mov dword ptr [rbp + 0x10f], eax
00B75357  48 85 DB                        test rbx, rbx
00B7535A  0F 84 1B 04 00 00               je 0x140b7577b
00B75360  44 8B 23                        mov r12d, dword ptr [rbx]
00B75363  45 85 E4                        test r12d, r12d
00B75366  0F 84 0F 04 00 00               je 0x140b7577b
00B7536C  45 33 FF                        xor r15d, r15d
00B7536F  4C 89 7D D7                     mov qword ptr [rbp - 0x29], r15
00B75373  44 88 BD E7 00 00 00            mov byte ptr [rbp + 0xe7], r15b
00B7537A  45 85 E4                        test r12d, r12d
00B7537D  78 6E                           js 0x140b753ed
00B7537F  8B 8D EF 00 00 00               mov ecx, dword ptr [rbp + 0xef]
00B75385  83 E1 01                        and ecx, 1
00B75388  89 8D E7 00 00 00               mov dword ptr [rbp + 0xe7], ecx
00B7538E  74 51                           je 0x140b753e1
00B75390  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
00B75394  4C 8B 4D 7F                     mov r9, qword ptr [rbp + 0x7f]
00B75398  44 8B 85 87 00 00 00            mov r8d, dword ptr [rbp + 0x87]
00B7539F  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
00B753A3  48 8B 45 6F                     mov rax, qword ptr [rbp + 0x6f]
00B753A7  48 89 45 AF                     mov qword ptr [rbp - 0x51], rax
00B753AB  48 8B 85 9F 00 00 00            mov rax, qword ptr [rbp + 0x9f]
00B753B2  48 89 85 27 01 00 00            mov qword ptr [rbp + 0x127], rax
00B753B9  48 8B 85 A7 00 00 00            mov rax, qword ptr [rbp + 0xa7]
00B753C0  48 89 45 DF                     mov qword ptr [rbp - 0x21], rax
00B753C4  4C 89 8D 1F 01 00 00            mov qword ptr [rbp + 0x11f], r9
00B753CB  44 89 85 C7 00 00 00            mov dword ptr [rbp + 0xc7], r8d
00B753D2  4C 89 75 B7                     mov qword ptr [rbp - 0x49], r14
00B753D6  44 89 9D 2F 01 00 00            mov dword ptr [rbp + 0x12f], r11d
00B753DD  4C 89 55 BF                     mov qword ptr [rbp - 0x41], r10
00B753E1  8B C1                           mov eax, ecx
00B753E3  F7 D8                           neg eax
00B753E5  4D 1B FF                        sbb r15, r15
00B753E8  4C 23 FF                        and r15, rdi
00B753EB  EB 6C                           jmp 0x140b75459
00B753ED  F6 85 EF 00 00 00 02            test byte ptr [rbp + 0xef], 2
00B753F4  74 67                           je 0x140b7545d
00B753F6  48 8B 46 10                     mov rax, qword ptr [rsi + 0x10]
00B753FA  4C 8B 8D CF 00 00 00            mov r9, qword ptr [rbp + 0xcf]
00B75401  44 8B 85 D7 00 00 00            mov r8d, dword ptr [rbp + 0xd7]
00B75408  4C 8B BD 9F 00 00 00            mov r15, qword ptr [rbp + 0x9f]
00B7540F  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
00B75413  48 8B 85 AF 00 00 00            mov rax, qword ptr [rbp + 0xaf]
00B7541A  48 89 45 B7                     mov qword ptr [rbp - 0x49], rax
00B7541E  8B 85 B7 00 00 00               mov eax, dword ptr [rbp + 0xb7]
00B75424  89 85 2F 01 00 00               mov dword ptr [rbp + 0x12f], eax
00B7542A  48 8B 85 BF 00 00 00            mov rax, qword ptr [rbp + 0xbf]
00B75431  48 89 45 AF                     mov qword ptr [rbp - 0x51], rax
00B75435  48 8B 85 A7 00 00 00            mov rax, qword ptr [rbp + 0xa7]
00B7543C  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
00B75440  4C 89 8D 1F 01 00 00            mov qword ptr [rbp + 0x11f], r9
00B75447  44 89 85 C7 00 00 00            mov dword ptr [rbp + 0xc7], r8d
00B7544E  48 89 BD 27 01 00 00            mov qword ptr [rbp + 0x127], rdi
00B75455  4C 89 55 DF                     mov qword ptr [rbp - 0x21], r10
00B75459  4C 89 7D D7                     mov qword ptr [rbp - 0x29], r15
00B7545D  45 8B EC                        mov r13d, r12d
00B75460  48 83 C3 04                     add rbx, 4
00B75464  41 81 E5 00 C0 0F 00            and r13d, 0xfc000
00B7546B  41 81 E4 FF 0F 00 00            and r12d, 0xfff
00B75472  4D 85 FF                        test r15, r15
00B75475  75 0F                           jne 0x140b75486
00B75477  8B C2                           mov eax, edx
00B75479  41 0F AF C4                     imul eax, r12d
00B7547D  48 8D 1C 83                     lea rbx, [rbx + rax*4]
00B75481  E9 D1 FE FF FF                  jmp 0x140b75357
00B75486  45 85 E4                        test r12d, r12d
00B75489  0F 84 C2 02 00 00               je 0x140b75751
00B7548F  8B 3B                           mov edi, dword ptr [rbx]
00B75491  49 8B D1                        mov rdx, r9
00B75494  8B CF                           mov ecx, edi
00B75496  E8 55 03 00 00                  call 0x140b757f0
00B7549B  4C 8B 3E                        mov r15, qword ptr [rsi]
00B7549E  84 C0                           test al, al
00B754A0  BA 64 AA 00 00                  mov edx, 0xaa64
00B754A5  44 8B F2                        mov r14d, edx
00B754A8  66 44 0F 44 B5 F7 00 00 00      cmove r14w, word ptr [rbp + 0xf7]
00B754B1  4D 85 FF                        test r15, r15
00B754B4  0F 84 9A 00 00 00               je 0x140b75554
00B754BA  4C 8D 8D 17 01 00 00            lea r9, [rbp + 0x117]
00B754C1  41 0F B7 D6                     movzx edx, r14w
00B754C5  4C 8D 85 97 00 00 00            lea r8, [rbp + 0x97]
00B754CC  41 8B CD                        mov ecx, r13d
00B754CF  E8 70 03 00 00                  call 0x140b75844
00B754D4  8B 95 97 00 00 00               mov edx, dword ptr [rbp + 0x97]
00B754DA  48 8D 45 77                     lea rax, [rbp + 0x77]
00B754DE  44 8B 8D 17 01 00 00            mov r9d, dword ptr [rbp + 0x117]
00B754E5  03 D7                           add edx, edi
00B754E7  44 8B 43 04                     mov r8d, dword ptr [rbx + 4]
00B754EB  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
00B754EF  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B754F4  49 8B C7                        mov rax, r15
00B754F7  44 89 6C 24 20                  mov dword ptr [rsp + 0x20], r13d
00B754FC  E8 CF 55 B4 FF                  call 0x1406baad0
00B75501  85 C0                           test eax, eax
00B75503  0F 88 C9 02 00 00               js 0x140b757d2
00B75509  80 7D 77 00                     cmp byte ptr [rbp + 0x77], 0
00B7550D  75 40                           jne 0x140b7554f
00B7550F  8B 95 0F 01 00 00               mov edx, dword ptr [rbp + 0x10f]
00B75515  41 FF CC                        dec r12d
00B75518  48 8B 75 C7                     mov rsi, qword ptr [rbp - 0x39]
00B7551C  4C 8B 8D 1F 01 00 00            mov r9, qword ptr [rbp + 0x11f]
00B75523  44 8B 85 C7 00 00 00            mov r8d, dword ptr [rbp + 0xc7]
00B7552A  48 8D 1C 93                     lea rbx, [rbx + rdx*4]
00B7552E  41 81 FD 00 C0 01 00            cmp r13d, 0x1c000
00B75535  0F 85 4B FF FF FF               jne 0x140b75486
00B7553B  48 8B 4D AF                     mov rcx, qword ptr [rbp - 0x51]
00B7553F  48 85 C9                        test rcx, rcx
00B75542  0F 84 3E FF FF FF               je 0x140b75486
00B75548  FF 01                           inc dword ptr [rcx]
00B7554A  E9 37 FF FF FF                  jmp 0x140b75486
00B7554F  BA 64 AA 00 00                  mov edx, 0xaa64
00B75554  8B 3B                           mov edi, dword ptr [rbx]
00B75556  4C 8B 7D D7                     mov r15, qword ptr [rbp - 0x29]
00B7555A  8B 43 04                        mov eax, dword ptr [rbx + 4]
00B7555D  49 03 FF                        add rdi, r15
00B75560  4C 8B 55 DF                     mov r10, qword ptr [rbp - 0x21]
00B75564  4C 03 D0                        add r10, rax
00B75567  41 81 FD 00 C0 01 00            cmp r13d, 0x1c000
00B7556E  0F 84 A9 00 00 00               je 0x140b7561d
00B75574  41 81 FD 00 C0 02 00            cmp r13d, 0x2c000
00B7557B  74 7F                           je 0x140b755fc
00B7557D  41 81 FD 00 C0 05 00            cmp r13d, 0x5c000
00B75584  74 41                           je 0x140b755c7
00B75586  41 81 FD 00 80 07 00            cmp r13d, 0x78000
00B7558D  0F 85 9A 01 00 00               jne 0x140b7572d
00B75593  48 8B 8D 8F 00 00 00            mov rcx, qword ptr [rbp + 0x8f]
00B7559A  48 83 F9 FF                     cmp rcx, -1
00B7559E  0F 84 C2 01 00 00               je 0x140b75766
00B755A4  48 85 C9                        test rcx, rcx
00B755A7  0F 84 80 01 00 00               je 0x140b7572d
00B755AD  80 3C 08 FF                     cmp byte ptr [rax + rcx], 0xff
00B755B1  0F 85 76 01 00 00               jne 0x140b7572d
00B755B7  48 8B 0C C5 00 00 00 00         mov rcx, qword ptr [rax*8]
00B755BF  48 01 0F                        add qword ptr [rdi], rcx
00B755C2  E9 66 01 00 00                  jmp 0x140b7572d
00B755C7  B9 64 86 00 00                  mov ecx, 0x8664
00B755CC  66 44 3B F1                     cmp r14w, cx
00B755D0  74 17                           je 0x140b755e9
00B755D2  66 44 3B F2                     cmp r14w, dx
00B755D6  74 11                           je 0x140b755e9
00B755D8  48 8B 8D 27 01 00 00            mov rcx, qword ptr [rbp + 0x127]
00B755DF  8B 04 08                        mov eax, dword ptr [rax + rcx]
00B755E2  89 07                           mov dword ptr [rdi], eax
00B755E4  E9 44 01 00 00                  jmp 0x140b7572d
00B755E9  48 8B 8D 27 01 00 00            mov rcx, qword ptr [rbp + 0x127]
00B755F0  48 8B 04 08                     mov rax, qword ptr [rax + rcx]
00B755F4  48 89 07                        mov qword ptr [rdi], rax
00B755F7  E9 31 01 00 00                  jmp 0x140b7572d
00B755FC  B8 64 86 00 00                  mov eax, 0x8664
00B75601  66 44 3B F0                     cmp r14w, ax
00B75605  74 0E                           je 0x140b75615
00B75607  66 44 3B F2                     cmp r14w, dx
00B7560B  74 08                           je 0x140b75615
00B7560D  44 89 17                        mov dword ptr [rdi], r10d
00B75610  E9 18 01 00 00                  jmp 0x140b7572d
00B75615  4C 89 17                        mov qword ptr [rdi], r10
00B75618  E9 10 01 00 00                  jmp 0x140b7572d
00B7561D  83 BD 0F 01 00 00 02            cmp dword ptr [rbp + 0x10f], 2
00B75624  75 04                           jne 0x140b7562a
00B75626  33 D2                           xor edx, edx
00B75628  EB 04                           jmp 0x140b7562e
00B7562A  48 8D 53 08                     lea rdx, [rbx + 8]
00B7562E  48 8B 75 B7                     mov rsi, qword ptr [rbp - 0x49]
00B75632  48 8B CF                        mov rcx, rdi
00B75635  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00B7563A  E8 C9 4D B3 FF                  call 0x1406aa408
00B7563F  44 8B D8                        mov r11d, eax
00B75642  83 F8 FF                        cmp eax, -1
00B75645  0F 84 29 01 00 00               je 0x140b75774
00B7564B  83 F8 FE                        cmp eax, -2
00B7564E  0F 85 8F 00 00 00               jne 0x140b756e3
00B75654  48 8B 75 AF                     mov rsi, qword ptr [rbp - 0x51]
00B75658  44 8B 1E                        mov r11d, dword ptr [rsi]
00B7565B  44 3B 9D 2F 01 00 00            cmp r11d, dword ptr [rbp + 0x12f]
00B75662  0F 83 05 01 00 00               jae 0x140b7576d
00B75668  48 8B 4D B7                     mov rcx, qword ptr [rbp - 0x49]
00B7566C  41 8B D3                        mov edx, r11d
00B7566F  E8 74 4B B3 FF                  call 0x1406aa1e8
00B75674  8B 8D EF 00 00 00               mov ecx, dword ptr [rbp + 0xef]
00B7567A  4D 8B C2                        mov r8, r10
00B7567D  4C 8B 4D BF                     mov r9, qword ptr [rbp - 0x41]
00B75681  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
00B75685  4D 2B CF                        sub r9, r15
00B75688  66 44 89 74 24 38               mov word ptr [rsp + 0x38], r14w
00B7568E  48 8D 90 00 10 00 00            lea rdx, [rax + 0x1000]
00B75695  83 64 24 28 00                  and dword ptr [rsp + 0x28], 0
00B7569A  4C 03 C8                        add r9, rax
00B7569D  48 8B C8                        mov rcx, rax
00B756A0  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00B756A5  E8 DE 4C B3 FF                  call 0x1406aa388
00B756AA  48 8B 8D 07 01 00 00            mov rcx, qword ptr [rbp + 0x107]
00B756B1  48 85 C9                        test rcx, rcx
00B756B4  74 16                           je 0x140b756cc
00B756B6  80 BD E7 00 00 00 00            cmp byte ptr [rbp + 0xe7], 0
00B756BD  74 0D                           je 0x140b756cc
00B756BF  8B 03                           mov eax, dword ptr [rbx]
00B756C1  42 89 04 D9                     mov dword ptr [rcx + r11*8], eax
00B756C5  8B 07                           mov eax, dword ptr [rdi]
00B756C7  42 89 44 D9 04                  mov dword ptr [rcx + r11*8 + 4], eax
00B756CC  8B 13                           mov edx, dword ptr [rbx]
00B756CE  48 8B CF                        mov rcx, rdi
00B756D1  48 03 55 BF                     add rdx, qword ptr [rbp - 0x41]
00B756D5  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
00B756DA  E8 0D 4D B3 FF                  call 0x1406aa3ec
00B756DF  FF 06                           inc dword ptr [rsi]
00B756E1  EB 1D                           jmp 0x140b75700
00B756E3  3B 85 2F 01 00 00               cmp eax, dword ptr [rbp + 0x12f]
00B756E9  0F 83 85 00 00 00               jae 0x140b75774
00B756EF  8B D0                           mov edx, eax
00B756F1  48 8B CE                        mov rcx, rsi
00B756F4  E8 EF 4A B3 FF                  call 0x1406aa1e8
00B756F9  4C 89 90 00 10 00 00            mov qword ptr [rax + 0x1000], r10
00B75700  48 8B 85 FF 00 00 00            mov rax, qword ptr [rbp + 0xff]
00B75707  48 85 C0                        test rax, rax
00B7570A  74 21                           je 0x140b7572d
00B7570C  80 BD E7 00 00 00 00            cmp byte ptr [rbp + 0xe7], 0
00B75713  74 18                           je 0x140b7572d
00B75715  41 8B CB                        mov ecx, r11d
00B75718  41 83 E3 07                     and r11d, 7
00B7571C  48 C1 E9 03                     shr rcx, 3
00B75720  48 03 48 08                     add rcx, qword ptr [rax + 8]
00B75724  0F BE 01                        movsx eax, byte ptr [rcx]
00B75727  44 0F AB D8                     bts eax, r11d
00B7572B  88 01                           mov byte ptr [rcx], al
00B7572D  8B 95 0F 01 00 00               mov edx, dword ptr [rbp + 0x10f]
00B75733  41 FF CC                        dec r12d
00B75736  48 8B 75 C7                     mov rsi, qword ptr [rbp - 0x39]
00B7573A  4C 8B 8D 1F 01 00 00            mov r9, qword ptr [rbp + 0x11f]
00B75741  44 8B 85 C7 00 00 00            mov r8d, dword ptr [rbp + 0xc7]
00B75748  48 8D 1C 93                     lea rbx, [rbx + rdx*4]
00B7574C  E9 35 FD FF FF                  jmp 0x140b75486
00B75751  48 8B 7D 4F                     mov rdi, qword ptr [rbp + 0x4f]
00B75755  4C 8B 55 57                     mov r10, qword ptr [rbp + 0x57]
00B75759  44 8B 5D 67                     mov r11d, dword ptr [rbp + 0x67]
00B7575D  4C 8B 75 5F                     mov r14, qword ptr [rbp + 0x5f]
00B75761  E9 F1 FB FF FF                  jmp 0x140b75357
00B75766  B8 30 00 00 C0                  mov eax, 0xc0000030
00B7576B  EB 65                           jmp 0x140b757d2
00B7576D  B8 AC 04 00 C0                  mov eax, 0xc00004ac
00B75772  EB 5E                           jmp 0x140b757d2
00B75774  B8 18 00 00 C0                  mov eax, 0xc0000018
00B75779  EB 57                           jmp 0x140b757d2
00B7577B  48 8B 9D FF 00 00 00            mov rbx, qword ptr [rbp + 0xff]
00B75782  48 85 DB                        test rbx, rbx
00B75785  74 49                           je 0x140b757d0
00B75787  45 33 C0                        xor r8d, r8d
00B7578A  48 8B CB                        mov rcx, rbx
00B7578D  41 8D 50 01                     lea edx, [r8 + 1]
00B75791  E8 3A B5 86 FF                  call 0x1403e0cd0
00B75796  44 8B C0                        mov r8d, eax
00B75799  83 F8 FF                        cmp eax, -1
00B7579C  74 32                           je 0x140b757d0
00B7579E  48 8B B5 07 01 00 00            mov rsi, qword ptr [rbp + 0x107]
00B757A5  41 8B C8                        mov ecx, r8d
00B757A8  48 8D 14 CE                     lea rdx, [rsi + rcx*8]
00B757AC  8B 02                           mov eax, dword ptr [rdx]
00B757AE  85 C0                           test eax, eax
00B757B0  74 09                           je 0x140b757bb
00B757B2  48 8D 0C 07                     lea rcx, [rdi + rax]
00B757B6  E8 51 4A B3 FF                  call 0x1406aa20c
00B757BB  BA 01 00 00 00                  mov edx, 1
00B757C0  48 8B CB                        mov rcx, rbx
00B757C3  E8 08 B5 86 FF                  call 0x1403e0cd0
00B757C8  44 8B C0                        mov r8d, eax
00B757CB  83 F8 FF                        cmp eax, -1
00B757CE  75 D5                           jne 0x140b757a5
00B757D0  33 C0                           xor eax, eax
00B757D2  48 81 C4 A8 00 00 00            add rsp, 0xa8
00B757D9  41 5F                           pop r15
00B757DB  41 5E                           pop r14
00B757DD  41 5D                           pop r13
00B757DF  41 5C                           pop r12
00B757E1  5F                              pop rdi
00B757E2  5E                              pop rsi
00B757E3  5B                              pop rbx
00B757E4  5D                              pop rbp
00B757E5  C3                              ret
00B757E6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlApplyHotPatch(__int64 a1, __int64 a2, __int64 a3, int a4)
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
    unsigned int v_stack_mA8;
    unsigned __int16 v_stack_mB0;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC8;

    *(unsigned int *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (168);
    result = 0;
    a4 = 0;
    a3 = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 9) = 0;
    *(unsigned __int8 *)(v_rsp - 71 + 119) = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 25) = v_xmm0;
    v_rsi = v_rsp - 71 - 25;
    if (*(unsigned __int64 *)(v_rsp - 71 + 271) != 0) { v_rsi = *(unsigned __int64 *)(v_rsp - 71 + 271); }
    *(unsigned __int64 *)(v_rsp - 71 + 287) = 0;
    a2 = 0;
    *(unsigned int *)(v_rsp - 71 + 199) = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 57) = v_rsi;
    *(unsigned int *)(v_rsp - 71 + 271) = 0;
    if (*(unsigned __int64 *)(v_rsp - 71 + 231) == 0) goto loc_00B7577B;
    result = RtlGetHotPatchSize(*(unsigned __int64 *)(v_rsp - 71 + 223), a2, a3, a4);
    *(unsigned int *)(v_rsp - 71 + 271) = (unsigned int)(result);
loc_00B75357:
    if (*(unsigned __int64 *)(v_rsp - 71 + 231) == 0) goto loc_00B7577B;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 231)))) == 0) goto loc_00B7577B;
    v_r15 = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 41) = 0;
    *(unsigned __int8 *)(v_rsp - 71 + 231) = 0;
    if (sign_flag) goto loc_00B753ED;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 71 + 239))) & (1));
    *(unsigned int *)(v_rsp - 71 + 231) = (unsigned int)(a1);
    if (!(condition_is_equal)) {
        result = *(unsigned __int64 *)(v_rsi + 8);
        a4 = *(unsigned __int64 *)(v_rsp - 71 + 127);
        a3 = *(unsigned int *)(v_rsp - 71 + 135);
        *(unsigned __int64 *)(v_rsp - 71 - 49) = result;
        result = *(unsigned __int64 *)(v_rsp - 71 + 111);
        *(unsigned __int64 *)(v_rsp - 71 - 81) = result;
        result = *(unsigned __int64 *)(v_rsp - 71 + 159);
        *(unsigned __int64 *)(v_rsp - 71 + 295) = result;
        result = *(unsigned __int64 *)(v_rsp - 71 + 167);
        *(unsigned __int64 *)(v_rsp - 71 - 33) = result;
        *(unsigned __int64 *)(v_rsp - 71 + 287) = a4;
        *(unsigned int *)(v_rsp - 71 + 199) = (unsigned int)(a3);
        *(unsigned __int64 *)(v_rsp - 71 - 73) = a3;
        *(unsigned int *)(v_rsp - 71 + 303) = (unsigned int)((unsigned int)(a4));
        *(unsigned __int64 *)(v_rsp - 71 - 65) = 0;
    }
    result = (unsigned int)(-((unsigned int)((unsigned int)(a1))));
    v_r15 = (v_r15) & (a1);
    goto loc_00B75459;
loc_00B753ED:
    if (((*(unsigned __int8 *)(v_rsp - 71 + 239)) & (2)) == 0) goto loc_00B7545D;
    *(unsigned __int64 *)(v_rsp - 71 - 49) = *(unsigned __int64 *)(v_rsi + 16);
    *(unsigned __int64 *)(v_rsp - 71 - 73) = *(unsigned __int64 *)(v_rsp - 71 + 175);
    *(unsigned int *)(v_rsp - 71 + 303) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 183)));
    *(unsigned __int64 *)(v_rsp - 71 - 81) = *(unsigned __int64 *)(v_rsp - 71 + 191);
    *(unsigned __int64 *)(v_rsp - 71 - 65) = *(unsigned __int64 *)(v_rsp - 71 + 167);
    *(unsigned __int64 *)(v_rsp - 71 + 287) = *(unsigned __int64 *)(v_rsp - 71 + 207);
    *(unsigned int *)(v_rsp - 71 + 199) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 215)));
    *(unsigned __int64 *)(v_rsp - 71 + 295) = a1;
    *(unsigned __int64 *)(v_rsp - 71 - 33) = 0;
loc_00B75459:
    *(unsigned __int64 *)(v_rsp - 71 - 41) = *(unsigned __int64 *)(v_rsp - 71 + 159);
loc_00B7545D:
    v_rbx = (*(unsigned __int64 *)(v_rsp - 71 + 231)) + (4);
    v_r13 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 231)))))) & (0xFC000ULL));
    v_r12 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 231)))) & (0xFFFULL));
    if (*(unsigned __int64 *)(v_rsp - 71 + 159) != 0) goto loc_00B75486;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))) * ((unsigned int)(v_r12)));
    goto loc_00B75357;
loc_00B75486:
    if ((unsigned int)(v_r12) == 0) goto loc_00B75751;
    result = RtlIsCodeInEcRanges((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + result * 4)))), *(unsigned __int64 *)(v_rsp - 71 + 207), (unsigned int)(*(unsigned int *)(v_rsp - 71 + 215)), *(unsigned __int64 *)(v_rsp - 71 + 207));
    v_r14 = (unsigned int)((unsigned int)((unsigned int)(0xAA64ULL)));
    if ((unsigned __int8)(result) == 0) { v_r14 = *(unsigned __int16 *)(v_rsp - 71 + 247); }
    if (*(unsigned __int64 *)(v_rsi) == 0) goto loc_00B75554;
    result = RtlpDetermineHotPatchExtent((unsigned int)((unsigned int)(v_r13)), (unsigned __int16)(v_r14), v_rsp - 71 + 151, v_rsp - 71 + 279);
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 71 + 151))) + ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + result * 4)))));
    v_stack_mC0 = v_rsp - 71 + 119;
    v_stack_mC8 = (unsigned int)(v_r13);
    result = guard_dispatch_icall(*(unsigned __int64 *)(v_rsp - 71 - 49), a2, (unsigned int)(*(unsigned int *)(v_rbx + result * 4 + 4)), (unsigned int)(*(unsigned int *)(v_rsp - 71 + 279)));
    if (sign_flag) goto loc_00B757D2;
    if ((*(unsigned __int8 *)(v_rsp - 71 + 119)) != 0) goto loc_00B7554F;
    v_r12 = (unsigned int)((v_r12) - 1);
    if (((unsigned int)(v_r13)) != 0x1C000ULL) goto loc_00B75486;
    if (*(unsigned __int64 *)(v_rsp - 71 - 81) == 0) goto loc_00B75486;
    goto loc_00B75486;
loc_00B7554F:
loc_00B75554:
    v_rdi = ((unsigned int)(*(unsigned int *)(v_rbx + result * 4 + (unsigned int)(*(unsigned int *)(v_rsp - 71 + 271)) * 4))) + (*(unsigned __int64 *)(v_rsp - 71 - 41));
    v_r10 = (*(unsigned __int64 *)(v_rsp - 71 - 33)) + ((unsigned int)(*(unsigned int *)(v_rbx + result * 4 + (unsigned int)(*(unsigned int *)(v_rsp - 71 + 271)) * 4 + 4)));
    if (((unsigned int)(v_r13)) == 0x1C000ULL) goto loc_00B7561D;
    if (((unsigned int)(v_r13)) == 0x2C000ULL) goto loc_00B755FC;
    if (((unsigned int)(v_r13)) == 0x5C000ULL) goto loc_00B755C7;
    if (((unsigned int)(v_r13)) != 0x78000ULL) goto loc_00B7572D;
    if ((*(unsigned __int64 *)(v_rsp - 71 + 143)) == -1) goto loc_00B75766;
    if (*(unsigned __int64 *)(v_rsp - 71 + 143) == 0) goto loc_00B7572D;
    if ((*(unsigned __int8 *)((unsigned int)(*(unsigned int *)(v_rbx + result * 4 + (unsigned int)(*(unsigned int *)(v_rsp - 71 + 271)) * 4 + 4)) + *(unsigned __int64 *)(v_rsp - 71 + 143) * 1)) != 255) goto loc_00B7572D;
    goto loc_00B7572D;
loc_00B755C7:
    if (((unsigned __int16)(v_r14)) == ((unsigned __int16)((unsigned int)(0x8664ULL)))) goto loc_00B755E9;
    if (((unsigned __int16)(v_r14)) == ((unsigned __int16)((unsigned int)(0xAA64ULL)))) goto loc_00B755E9;
    *(unsigned int *)(v_rdi) = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_rbx + result * 4 + (unsigned int)(*(unsigned int *)(v_rsp - 71 + 271)) * 4 + 4)) + *(unsigned __int64 *)(v_rsp - 71 + 295) * 1)));
    goto loc_00B7572D;
loc_00B755E9:
    *(unsigned __int64 *)(v_rdi) = *(unsigned __int64 *)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_rbx + result * 4 + (unsigned int)(*(unsigned int *)(v_rsp - 71 + 271)) * 4 + 4)) + *(unsigned __int64 *)(v_rsp - 71 + 295) * 1)) + *(unsigned __int64 *)(v_rsp - 71 + 295) * 1);
    goto loc_00B7572D;
loc_00B755FC:
    if (((unsigned __int16)(v_r14)) == ((unsigned __int16)((unsigned int)(0x8664ULL)))) goto loc_00B75615;
    if (((unsigned __int16)(v_r14)) == ((unsigned __int16)((unsigned int)(0xAA64ULL)))) goto loc_00B75615;
    *(unsigned int *)(v_rdi) = (unsigned int)(v_r10);
    goto loc_00B7572D;
loc_00B75615:
    *(unsigned __int64 *)(v_rdi) = v_r10;
    goto loc_00B7572D;
loc_00B7561D:
    if ((*(unsigned int *)(v_rsp - 71 + 271)) != 2) goto loc_00B7562A;
    a2 = 0;
    goto loc_00B7562E;
loc_00B7562A:
loc_00B7562E:
    v_stack_mC8 = *(unsigned __int64 *)(v_rsp - 71 - 73);
    result = RtlpCheckFunctionPatchAppliedInOriginalImage(v_rdi, v_rbx + result * 4 + (unsigned int)(*(unsigned int *)(v_rsp - 71 + 271)) * 4 + 8, (unsigned int)(*(unsigned int *)(v_rsp - 71 + 199)), *(unsigned __int64 *)(v_rsp - 71 + 287));
    if (((unsigned int)(result)) == -1) goto loc_00B75774;
    if (((unsigned int)(result)) != -2) goto loc_00B756E3;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 81))))) >= (*(unsigned int *)(v_rsp - 71 + 303))) goto loc_00B7576D;
    result = RtlGetHpatEntryAddress(*(unsigned __int64 *)(v_rsp - 71 - 73), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 81))))), (unsigned int)(*(unsigned int *)(v_rsp - 71 + 199)), *(unsigned __int64 *)(v_rsp - 71 + 287));
    v_stack_mA8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 239)));
    a4 = (*(unsigned __int64 *)(v_rsp - 71 - 65)) - (*(unsigned __int64 *)(v_rsp - 71 - 41));
    v_stack_mB0 = (unsigned __int16)(v_r14);
    a4 = (a4) + (result);
    v_stack_mC8 = *(unsigned __int64 *)(v_rsp - 71 - 41);
    result = RtlPopulateHpatEntry(result, result + 4096, v_r10, a4);
    if (*(unsigned __int64 *)(v_rsp - 71 + 263) == 0) goto loc_00B756CC;
    if ((*(unsigned __int8 *)(v_rsp - 71 + 231)) != 0) {
        result = *(unsigned int *)(v_rbx + result * 4 + (unsigned int)(*(unsigned int *)(v_rsp - 71 + 271)) * 4);
        *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 263) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 81))) * 8) = (unsigned int)(result);
        result = *(unsigned int *)(v_rdi);
        *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 263) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 81))) * 8 + 4) = (unsigned int)(result);
    }
    a2 = ((unsigned int)(*(unsigned int *)(v_rbx + result * 4 + (unsigned int)(*(unsigned int *)(v_rsp - 71 + 271)) * 4))) + (*(unsigned __int64 *)(v_rsp - 71 - 65));
    v_stack_mC8 = a4;
    result = RtlpApplyFunctionPatch(v_rdi, a2, v_r10, a4);
    goto loc_00B75700;
loc_00B756E3:
    if (((unsigned int)(result)) >= (*(unsigned int *)(v_rsp - 71 + 303))) goto loc_00B75774;
    result = RtlGetHpatEntryAddress(*(unsigned __int64 *)(v_rsp - 71 - 81), (unsigned int)((unsigned int)(result)), v_r10, a4);
    *(unsigned __int64 *)(result + 4096) = v_r10;
loc_00B75700:
    if (*(unsigned __int64 *)(v_rsp - 71 + 255) == 0) goto loc_00B7572D;
    result = *(unsigned __int64 *)(v_rsp - 71 + 255);
    v_r11 = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 81)));
    if ((*(unsigned __int8 *)(v_rsp - 71 + 231)) != 0) {
        a1 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 81))));
        v_r11 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 81)))) & (7));
        a1 = (a1) >> (3);
        a1 = (a1) + (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 255) + 8));
        result = (__int8)(*(unsigned __int8 *)(a1));
        *(unsigned __int8 *)(a1) = (unsigned __int8)(result);
    }
    v_r12 = (unsigned int)((v_r12) - 1);
    goto loc_00B75486;
loc_00B75751:
    goto loc_00B75357;
loc_00B75766:
    goto loc_00B757D2;
loc_00B7576D:
    goto loc_00B757D2;
loc_00B75774:
    goto loc_00B757D2;
loc_00B7577B:
    if (*(unsigned __int64 *)(v_rsp - 71 + 255) == 0) goto loc_00B757D0;
    a3 = 0;
    result = RtlFindClearBitsAndSet(*(unsigned __int64 *)(v_rsp - 71 + 255), a3 + 1, a3, *(unsigned __int64 *)(v_rsp - 71 + 287));
    if (((unsigned int)(result)) == -1) goto loc_00B757D0;
loc_00B757A5:
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 263) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))) * 8));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 263) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))) * 8))) != 0) {
        a1 = *(unsigned __int64 *)(v_rsp - 71 + 79) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 263) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))) * 8)) * 1;
        result = RtlpRevertFunctionPatchFromUndoEntry(a1, *(unsigned __int64 *)(v_rsp - 71 + 263) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))) * 8, (unsigned int)((unsigned int)(result)), *(unsigned __int64 *)(v_rsp - 71 + 287));
    }
    result = RtlFindClearBitsAndSet(*(unsigned __int64 *)(v_rsp - 71 + 255), 1, (unsigned int)((unsigned int)(result)), *(unsigned __int64 *)(v_rsp - 71 + 287));
    if (((unsigned int)(result)) != -1) goto loc_00B757A5;
loc_00B757D0:
    result = 0;
loc_00B757D2:
    v_rsp = (v_rsp) + (168);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlApplyHotPatch(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
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
    uint32_t v_stack_mA8;
    uint16_t v_stack_mB0;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC8;

    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (168);
    result = 0;
    Arg4 = 0;
    Arg3 = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x9) = 0;
    *(uint8_t *)(local_rsp - 0x47 + 0x77) = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x19) = v_xmm0;
    local_rsi = local_rsp - 71 - 25;
    if (*(uint64_t *)(local_rsp - 0x47 + 0x10F) != 0) { local_rsi = *(uint64_t *)(local_rsp - 0x47 + 0x10F); }
    *(uint64_t *)(local_rsp - 0x47 + 0x11F) = 0;
    Arg2 = 0;
    *(uint32_t *)(local_rsp - 0x47 + 0xC7) = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x39) = local_rsi;
    *(uint32_t *)(local_rsp - 0x47 + 0x10F) = 0;
    if (*(uint64_t *)(local_rsp - 0x47 + 0xE7) == 0) goto loc_00B7577B;
    result = RtlGetHotPatchSize(*(uint64_t *)(local_rsp - 0x47 + 0xDF), Arg2, Arg3, Arg4);
    *(uint32_t *)(local_rsp - 0x47 + 0x10F) = (uint32_t)(result);
loc_00B75357:
    if (*(uint64_t *)(local_rsp - 0x47 + 0xE7) == 0) goto loc_00B7577B;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0xE7)))) == 0) goto loc_00B7577B;
    local_r15 = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x29) = 0;
    *(uint8_t *)(local_rsp - 0x47 + 0xE7) = 0;
    if (sign_flag) goto loc_00B753ED;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0xEF))) & (1));
    *(uint32_t *)(local_rsp - 0x47 + 0xE7) = (uint32_t)(Arg1);
    if (!(condition_is_equal)) {
        result = *(uint64_t *)(local_rsi + 0x8);
        Arg4 = *(uint64_t *)(local_rsp - 0x47 + 0x7F);
        Arg3 = *(uint32_t *)(local_rsp - 0x47 + 0x87);
        *(uint64_t *)(local_rsp - 0x47 - 0x31) = result;
        result = *(uint64_t *)(local_rsp - 0x47 + 0x6F);
        *(uint64_t *)(local_rsp - 0x47 - 0x51) = result;
        result = *(uint64_t *)(local_rsp - 0x47 + 0x9F);
        *(uint64_t *)(local_rsp - 0x47 + 0x127) = result;
        result = *(uint64_t *)(local_rsp - 0x47 + 0xA7);
        *(uint64_t *)(local_rsp - 0x47 - 0x21) = result;
        *(uint64_t *)(local_rsp - 0x47 + 0x11F) = Arg4;
        *(uint32_t *)(local_rsp - 0x47 + 0xC7) = (uint32_t)(Arg3);
        *(uint64_t *)(local_rsp - 0x47 - 0x49) = Arg3;
        *(uint32_t *)(local_rsp - 0x47 + 0x12F) = (uint32_t)((uint32_t)(Arg4));
        *(uint64_t *)(local_rsp - 0x47 - 0x41) = 0;
    }
    result = (uint32_t)(-((uint32_t)((uint32_t)(Arg1))));
    local_r15 = (local_r15) & (Arg1);
    goto loc_00B75459;
loc_00B753ED:
    if (((*(uint8_t *)(local_rsp - 0x47 + 0xEF)) & (2)) == 0) goto loc_00B7545D;
    *(uint64_t *)(local_rsp - 0x47 - 0x31) = *(uint64_t *)(local_rsi + 0x10);
    *(uint64_t *)(local_rsp - 0x47 - 0x49) = *(uint64_t *)(local_rsp - 0x47 + 0xAF);
    *(uint32_t *)(local_rsp - 0x47 + 0x12F) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0xB7)));
    *(uint64_t *)(local_rsp - 0x47 - 0x51) = *(uint64_t *)(local_rsp - 0x47 + 0xBF);
    *(uint64_t *)(local_rsp - 0x47 - 0x41) = *(uint64_t *)(local_rsp - 0x47 + 0xA7);
    *(uint64_t *)(local_rsp - 0x47 + 0x11F) = *(uint64_t *)(local_rsp - 0x47 + 0xCF);
    *(uint32_t *)(local_rsp - 0x47 + 0xC7) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0xD7)));
    *(uint64_t *)(local_rsp - 0x47 + 0x127) = Arg1;
    *(uint64_t *)(local_rsp - 0x47 - 0x21) = 0;
loc_00B75459:
    *(uint64_t *)(local_rsp - 0x47 - 0x29) = *(uint64_t *)(local_rsp - 0x47 + 0x9F);
loc_00B7545D:
    local_rbx = (*(uint64_t *)(local_rsp - 0x47 + 0xE7)) + (4);
    local_r13 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0xE7)))))) & (0xFC000ULL));
    local_r12 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0xE7)))) & (0xFFFULL));
    if (*(uint64_t *)(local_rsp - 0x47 + 0x9F) != 0) goto loc_00B75486;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))) * ((uint32_t)(local_r12)));
    goto loc_00B75357;
loc_00B75486:
    if ((uint32_t)(local_r12) == 0) goto loc_00B75751;
    result = RtlIsCodeInEcRanges((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + result * 4)))), *(uint64_t *)(local_rsp - 0x47 + 0xCF), (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0xD7)), *(uint64_t *)(local_rsp - 0x47 + 0xCF));
    local_r14 = (uint32_t)((uint32_t)((uint32_t)(0xAA64ULL)));
    if ((uint8_t)(result) == 0) { local_r14 = *(uint16_t *)(local_rsp - 0x47 + 0xF7); }
    if (*(uint64_t *)(local_rsi) == 0) goto loc_00B75554;
    result = RtlpDetermineHotPatchExtent((uint32_t)((uint32_t)(local_r13)), (uint16_t)(local_r14), local_rsp - 71 + 151, local_rsp - 71 + 279);
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x97))) + ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + result * 4)))));
    v_stack_mC0 = local_rsp - 71 + 119;
    v_stack_mC8 = (uint32_t)(local_r13);
    result = guard_dispatch_icall(*(uint64_t *)(local_rsp - 0x47 - 0x31), Arg2, (uint32_t)(*(uint32_t *)(local_rbx + result * 4 + 0x4)), (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x117)));
    if (sign_flag) goto loc_00B757D2;
    if ((*(uint8_t *)(local_rsp - 0x47 + 0x77)) != 0) goto loc_00B7554F;
    local_r12 = (uint32_t)((local_r12) - 1);
    if (((uint32_t)(local_r13)) != 0x1C000ULL) goto loc_00B75486;
    if (*(uint64_t *)(local_rsp - 0x47 - 0x51) == 0) goto loc_00B75486;
    goto loc_00B75486;
loc_00B7554F:
loc_00B75554:
    local_rdi = ((uint32_t)(*(uint32_t *)(local_rbx + result * 4 + (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x10F)) * 4))) + (*(uint64_t *)(local_rsp - 0x47 - 0x29));
    local_r10 = (*(uint64_t *)(local_rsp - 0x47 - 0x21)) + ((uint32_t)(*(uint32_t *)(local_rbx + result * 4 + (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x10F)) * 4 + 0x4)));
    if (((uint32_t)(local_r13)) == 0x1C000ULL) goto loc_00B7561D;
    if (((uint32_t)(local_r13)) == 0x2C000ULL) goto loc_00B755FC;
    if (((uint32_t)(local_r13)) == 0x5C000ULL) goto loc_00B755C7;
    if (((uint32_t)(local_r13)) != 0x78000ULL) goto loc_00B7572D;
    if ((*(uint64_t *)(local_rsp - 0x47 + 0x8F)) == -1) goto loc_00B75766;
    if (*(uint64_t *)(local_rsp - 0x47 + 0x8F) == 0) goto loc_00B7572D;
    if ((*(uint8_t *)((uint32_t)(*(uint32_t *)(local_rbx + result * 4 + (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x10F)) * 4 + 0x4)) + *(uint64_t *)(local_rsp - 0x47 + 0x8F) * 1)) != 255) goto loc_00B7572D;
    goto loc_00B7572D;
loc_00B755C7:
    if (((uint16_t)(local_r14)) == ((uint16_t)((uint32_t)(0x8664ULL)))) goto loc_00B755E9;
    if (((uint16_t)(local_r14)) == ((uint16_t)((uint32_t)(0xAA64ULL)))) goto loc_00B755E9;
    *(uint32_t *)(local_rdi) = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(local_rbx + result * 4 + (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x10F)) * 4 + 0x4)) + *(uint64_t *)(local_rsp - 0x47 + 0x127) * 1)));
    goto loc_00B7572D;
loc_00B755E9:
    *(uint64_t *)(local_rdi) = *(uint64_t *)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(local_rbx + result * 4 + (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x10F)) * 4 + 0x4)) + *(uint64_t *)(local_rsp - 0x47 + 0x127) * 1)) + *(uint64_t *)(local_rsp - 0x47 + 0x127) * 1);
    goto loc_00B7572D;
loc_00B755FC:
    if (((uint16_t)(local_r14)) == ((uint16_t)((uint32_t)(0x8664ULL)))) goto loc_00B75615;
    if (((uint16_t)(local_r14)) == ((uint16_t)((uint32_t)(0xAA64ULL)))) goto loc_00B75615;
    *(uint32_t *)(local_rdi) = (uint32_t)(local_r10);
    goto loc_00B7572D;
loc_00B75615:
    *(uint64_t *)(local_rdi) = local_r10;
    goto loc_00B7572D;
loc_00B7561D:
    if ((*(uint32_t *)(local_rsp - 0x47 + 0x10F)) != 2) goto loc_00B7562A;
    Arg2 = 0;
    goto loc_00B7562E;
loc_00B7562A:
loc_00B7562E:
    v_stack_mC8 = *(uint64_t *)(local_rsp - 0x47 - 0x49);
    result = RtlpCheckFunctionPatchAppliedInOriginalImage(local_rdi, local_rbx + result * 4 + (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x10F)) * 4 + 8, (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0xC7)), *(uint64_t *)(local_rsp - 0x47 + 0x11F));
    if (((uint32_t)(result)) == -1) goto loc_00B75774;
    if (((uint32_t)(result)) != -2) goto loc_00B756E3;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x51))))) >= (*(uint32_t *)(local_rsp - 0x47 + 0x12F))) goto loc_00B7576D;
    result = RtlGetHpatEntryAddress(*(uint64_t *)(local_rsp - 0x47 - 0x49), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x51))))), (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0xC7)), *(uint64_t *)(local_rsp - 0x47 + 0x11F));
    v_stack_mA8 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0xEF)));
    Arg4 = (*(uint64_t *)(local_rsp - 0x47 - 0x41)) - (*(uint64_t *)(local_rsp - 0x47 - 0x29));
    v_stack_mB0 = (uint16_t)(local_r14);
    Arg4 = (Arg4) + (result);
    v_stack_mC8 = *(uint64_t *)(local_rsp - 0x47 - 0x29);
    result = RtlPopulateHpatEntry(result, result + 4096, local_r10, Arg4);
    if (*(uint64_t *)(local_rsp - 0x47 + 0x107) == 0) goto loc_00B756CC;
    if ((*(uint8_t *)(local_rsp - 0x47 + 0xE7)) != 0) {
        result = *(uint32_t *)(local_rbx + result * 4 + (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x10F)) * 4);
        *(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x107) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x51))) * 8) = (uint32_t)(result);
        result = *(uint32_t *)(local_rdi);
        *(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x107) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x51))) * 8 + 0x4) = (uint32_t)(result);
    }
    Arg2 = ((uint32_t)(*(uint32_t *)(local_rbx + result * 4 + (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x10F)) * 4))) + (*(uint64_t *)(local_rsp - 0x47 - 0x41));
    v_stack_mC8 = Arg4;
    result = RtlpApplyFunctionPatch(local_rdi, Arg2, local_r10, Arg4);
    goto loc_00B75700;
loc_00B756E3:
    if (((uint32_t)(result)) >= (*(uint32_t *)(local_rsp - 0x47 + 0x12F))) goto loc_00B75774;
    result = RtlGetHpatEntryAddress(*(uint64_t *)(local_rsp - 0x47 - 0x51), (uint32_t)((uint32_t)(result)), local_r10, Arg4);
    *(uint64_t *)(result + 0x1000) = local_r10;
loc_00B75700:
    if (*(uint64_t *)(local_rsp - 0x47 + 0xFF) == 0) goto loc_00B7572D;
    result = *(uint64_t *)(local_rsp - 0x47 + 0xFF);
    local_r11 = (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x51)));
    if ((*(uint8_t *)(local_rsp - 0x47 + 0xE7)) != 0) {
        Arg1 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x51))));
        local_r11 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x51)))) & (7));
        Arg1 = (Arg1) >> (3);
        Arg1 = (Arg1) + (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0xFF) + 0x8));
        result = (int8_t)(*(uint8_t *)(Arg1));
        *(uint8_t *)(Arg1) = (uint8_t)(result);
    }
    local_r12 = (uint32_t)((local_r12) - 1);
    goto loc_00B75486;
loc_00B75751:
    goto loc_00B75357;
loc_00B75766:
    goto loc_00B757D2;
loc_00B7576D:
    goto loc_00B757D2;
loc_00B75774:
    goto loc_00B757D2;
loc_00B7577B:
    if (*(uint64_t *)(local_rsp - 0x47 + 0xFF) == 0) goto loc_00B757D0;
    Arg3 = 0;
    result = RtlFindClearBitsAndSet(*(uint64_t *)(local_rsp - 0x47 + 0xFF), Arg3 + 1, Arg3, *(uint64_t *)(local_rsp - 0x47 + 0x11F));
    if (((uint32_t)(result)) == -1) goto loc_00B757D0;
loc_00B757A5:
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x107) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))) * 8));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x107) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))) * 8))) != 0) {
        Arg1 = *(uint64_t *)(local_rsp - 0x47 + 0x4F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x107) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))) * 8)) * 1;
        result = RtlpRevertFunctionPatchFromUndoEntry(Arg1, *(uint64_t *)(local_rsp - 0x47 + 0x107) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))) * 8, (uint32_t)((uint32_t)(result)), *(uint64_t *)(local_rsp - 0x47 + 0x11F));
    }
    result = RtlFindClearBitsAndSet(*(uint64_t *)(local_rsp - 0x47 + 0xFF), 1, (uint32_t)((uint32_t)(result)), *(uint64_t *)(local_rsp - 0x47 + 0x11F));
    if (((uint32_t)(result)) != -1) goto loc_00B757A5;
loc_00B757D0:
    result = 0;
loc_00B757D2:
    local_rsp = (local_rsp) + (168);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B7528C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
