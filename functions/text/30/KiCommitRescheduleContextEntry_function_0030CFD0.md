# KiCommitRescheduleContextEntry

- RVA: `0x0030CFD0`–`0x0030D4C6` (길이 `1,270` bytes)
- VA: `0x000000014030CFD0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00073E68`
- 디코드: `330`개 명령, `1,270/1,270` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **11**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **11**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0030D040` → [KiIsPrcbThread](../35/KiIsPrcbThread_function_00353230.md) (function, `0x00353230`)
- `0x0030D17B` → [KiSetProcessorIdle](../41/KiSetProcessorIdle_function_00416950.md) (function, `0x00416950`)
- `0x0030D188` → [KiUpdateThreadQosGroupingSummaries](../25/KiUpdateThreadQosGroupingSummaries_function_00257AEC.md) (function, `0x00257AEC`)
- `0x0030D190` → [KiUpdateStandbyStealSummaryForStandbyChange](../25/KiUpdateStandbyStealSummaryForStandbyChange_function_00257A80.md) (function, `0x00257A80`)
- `0x0030D2A4` → [KiSetProcessorIdle](../41/KiSetProcessorIdle_function_00416950.md) (function, `0x00416950`)
- `0x0030D2C4` → [KiIsPrcbThread](../35/KiIsPrcbThread_function_00353230.md) (function, `0x00353230`)
- `0x0030D316` → [KiSetProcessorIdle](../41/KiSetProcessorIdle_function_00416950.md) (function, `0x00416950`)
- `0x0030D35A` → [KiInsertDeferredReadyList](../20/KiInsertDeferredReadyList_function_00201310.md) (function, `0x00201310`)
- `0x0030D387` → [KiQueryEffectivePriorityThread](../25/KiQueryEffectivePriorityThread_function_00257BA0.md) (function, `0x00257BA0`)
- `0x0030D3BC` → [KiQueryEffectivePriorityThread](../25/KiQueryEffectivePriorityThread_function_00257BA0.md) (function, `0x00257BA0`)
- `0x0030D47D` → [KiSetProcessorIdle](../41/KiSetProcessorIdle_function_00416950.md) (function, `0x00416950`)

### Direct callers
- [sub_0021D7F8](../21/Unknown_function_0021D7F8.md) at `0x0021DF13`
- [sub_002546EC](../25/Unknown_function_002546EC.md) at `0x00254CC2`
- [KiAttemptToScheduleThreadToBusyIsolationUnit](../25/KiAttemptToScheduleThreadToBusyIsolationUnit_function_00259B00.md) at `0x0025A8CE`
- [KiExecuteAllDpcs](../25/KiExecuteAllDpcs_function_0025B740.md) at `0x0025C8AD`
- [KiGroupSchedulingGenerationEnd](KiGroupSchedulingGenerationEnd_function_0030A9B4.md) at `0x0030AA8E`
- [KiSoftParkElectionUnparkProcessor](KiSoftParkElectionUnparkProcessor_function_0030B818.md) at `0x0030B996`
- [KiEnterLongDpcProcessing](KiEnterLongDpcProcessing_function_0030BE54.md) at `0x0030C021`
- [KiRescheduleThreadAfterAffinityChange](KiRescheduleThreadAfterAffinityChange_function_0030C9E8.md) at `0x0030CB74`
- [KiCommitRescheduleContext](KiCommitRescheduleContext_function_0030CF20.md) at `0x0030CF76`
- [KiAttemptToStealStandbyThread](KiAttemptToStealStandbyThread_function_0030D790.md) at `0x0030DA42`
- [KiAttemptToStealStandbyThread](KiAttemptToStealStandbyThread_function_0030D790.md) at `0x0030DB5A`
- [KiSearchForNewThreadsOnTarget](KiSearchForNewThreadsOnTarget_function_0030F500.md) at `0x003100C5`
- [KiSearchForNewThreadsOnTarget](KiSearchForNewThreadsOnTarget_function_0030F500.md) at `0x0031048E`

### Static image references
- `0x0030D0F9` → RVA `0x00FC537C` (`ALMOSTRO`; read)
- `0x0030D41F` → RVA `0x00FC504C` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x0030D451` → [sub_006E0CEA](../6E/Unknown_function_006E0CEA.md) (`tail-transfer`)
  - `0x0030D45D` → [sub_006E0CEA + 0xD](../6E/Unknown_function_006E0CEA.md) (`tail-transfer`)
  - `0x0030D48B` → [sub_006E0CEA + 0x9F](../6E/Unknown_function_006E0CEA.md) (`tail-transfer`)
  - `0x0030D497` → [sub_006E0CEA + 0xB5](../6E/Unknown_function_006E0CEA.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0030CFD0  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0030CFD5  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
0030CFDA  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
0030CFDF  55                              push rbp
0030CFE0  56                              push rsi
0030CFE1  57                              push rdi
0030CFE2  41 54                           push r12
0030CFE4  41 55                           push r13
0030CFE6  41 56                           push r14
0030CFE8  41 57                           push r15
0030CFEA  48 83 EC 30                     sub rsp, 0x30
0030CFEE  48 8B 79 18                     mov rdi, qword ptr [rcx + 0x18]
0030CFF2  45 33 DB                        xor r11d, r11d
0030CFF5  48 8B 19                        mov rbx, qword ptr [rcx]
0030CFF8  45 8B D0                        mov r10d, r8d
0030CFFB  48 8B 71 10                     mov rsi, qword ptr [rcx + 0x10]
0030CFFF  4C 8B E2                        mov r12, rdx
0030D002  44 88 5C 24 70                  mov byte ptr [rsp + 0x70], r11b
0030D007  4C 8B F1                        mov r14, rcx
0030D00A  45 8A EB                        mov r13b, r11b
0030D00D  48 83 FF FF                     cmp rdi, -1
0030D011  0F 84 97 02 00 00               je 0x14030d2ae
0030D017  48 83 FF FE                     cmp rdi, -2
0030D01B  0F 84 28 04 00 00               je 0x14030d449
0030D021  48 8B 4B 10                     mov rcx, qword ptr [rbx + 0x10]
0030D025  41 8D 6B 01                     lea ebp, [r11 + 1]
0030D029  44 89 5C 24 20                  mov dword ptr [rsp + 0x20], r11d
0030D02E  45 8B FB                        mov r15d, r11d
0030D031  B2 02                           mov dl, 2
0030D033  48 85 C9                        test rcx, rcx
0030D036  0F 85 88 02 00 00               jne 0x14030d2c4
0030D03C  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
0030D040  E8 EB 61 04 00                  call 0x140353230
0030D045  84 C0                           test al, al
0030D047  75 0E                           jne 0x14030d057
0030D049  8A 81 84 01 00 00               mov al, byte ptr [rcx + 0x184]
0030D04F  3A C2                           cmp al, dl
0030D051  0F 84 47 03 00 00               je 0x14030d39e
0030D057  48 3B 4B 18                     cmp rcx, qword ptr [rbx + 0x18]
0030D05B  89 6C 24 20                     mov dword ptr [rsp + 0x20], ebp
0030D05F  41 0F 94 C7                     sete r15b
0030D063  8A 43 23                        mov al, byte ptr [rbx + 0x23]
0030D066  F6 D0                           not al
0030D068  23 C5                           and eax, ebp
0030D06A  44 3B F8                        cmp r15d, eax
0030D06D  0F 85 EF 03 00 00               jne 0x14030d462
0030D073  48 85 FF                        test rdi, rdi
0030D076  0F 84 58 01 00 00               je 0x14030d1d4
0030D07C  45 0F B6 66 21                  movzx r12d, byte ptr [r14 + 0x21]
0030D081  48 8B AB 80 8E 00 00            mov rbp, qword ptr [rbx + 0x8e80]
0030D088  45 03 E4                        add r12d, r12d
0030D08B  4C 8B 6B 38                     mov r13, qword ptr [rbx + 0x38]
0030D08F  48 3B FD                        cmp rdi, rbp
0030D092  0F 84 EF 03 00 00               je 0x14030d487
0030D098  F6 47 02 04                     test byte ptr [rdi + 2], 4
0030D09C  0F 85 DF 02 00 00               jne 0x14030d381
0030D0A2  8A 8F C3 00 00 00               mov cl, byte ptr [rdi + 0xc3]
0030D0A8  8B 47 78                        mov eax, dword ptr [rdi + 0x78]
0030D0AB  80 E1 7F                        and cl, 0x7f
0030D0AE  D1 E8                           shr eax, 1
0030D0B0  C0 E0 07                        shl al, 7
0030D0B3  0A C1                           or al, cl
0030D0B5  41 88 45 00                     mov byte ptr [r13], al
0030D0B9  4C 8B 83 B8 8E 00 00            mov r8, qword ptr [rbx + 0x8eb8]
0030D0C0  4D 85 C0                        test r8, r8
0030D0C3  0F 85 29 03 00 00               jne 0x14030d3f2
0030D0C9  8B 57 50                        mov edx, dword ptr [rdi + 0x50]
0030D0CC  4C 8B 43 38                     mov r8, qword ptr [rbx + 0x38]
0030D0D0  41 8A 40 40                     mov al, byte ptr [r8 + 0x40]
0030D0D4  8A C8                           mov cl, al
0030D0D6  32 8F 04 02 00 00               xor cl, byte ptr [rdi + 0x204]
0030D0DC  80 E1 07                        and cl, 7
0030D0DF  32 C1                           xor al, cl
0030D0E1  8A 8F 05 02 00 00               mov cl, byte ptr [rdi + 0x205]
0030D0E7  C0 E1 03                        shl cl, 3
0030D0EA  32 C8                           xor cl, al
0030D0EC  80 E1 38                        and cl, 0x38
0030D0EF  32 C1                           xor al, cl
0030D0F1  8B 4F 54                        mov ecx, dword ptr [rdi + 0x54]
0030D0F4  3B D1                           cmp edx, ecx
0030D0F6  0F 46 D1                        cmovbe edx, ecx
0030D0F9  3B 15 7D 82 CB 00               cmp edx, dword ptr [rip + 0xcb827d]
0030D0FF  1A C9                           sbb cl, cl
0030D101  24 BF                           and al, 0xbf
0030D103  F6 D1                           not cl
0030D105  80 E1 40                        and cl, 0x40
0030D108  0A C1                           or al, cl
0030D10A  41 88 40 40                     mov byte ptr [r8 + 0x40], al
0030D10E  48 8B 8B B8 8E 00 00            mov rcx, qword ptr [rbx + 0x8eb8]
0030D115  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
0030D119  48 89 7B 10                     mov qword ptr [rbx + 0x10], rdi
0030D11D  48 85 C9                        test rcx, rcx
0030D120  74 09                           je 0x14030d12b
0030D122  48 3B F8                        cmp rdi, rax
0030D125  0F 94 C0                        sete al
0030D128  88 41 10                        mov byte ptr [rcx + 0x10], al
0030D12B  8A 87 84 01 00 00               mov al, byte ptr [rdi + 0x184]
0030D131  BE 01 00 00 00                  mov esi, 1
0030D136  40 3A C6                        cmp al, sil
0030D139  0F 84 25 02 00 00               je 0x14030d364
0030D13F  41 F6 C4 02                     test r12b, 2
0030D143  0F 85 1B 02 00 00               jne 0x14030d364
0030D149  C6 87 84 01 00 00 03            mov byte ptr [rdi + 0x184], 3
0030D150  B8 18 00 00 00                  mov eax, 0x18
0030D155  48 8B CB                        mov rcx, rbx
0030D158  48 3B 3C 03                     cmp rdi, qword ptr [rbx + rax]
0030D15C  0F 85 53 01 00 00               jne 0x14030d2b5
0030D162  4C 8B 64 24 78                  mov r12, qword ptr [rsp + 0x78]
0030D167  45 8B C7                        mov r8d, r15d
0030D16A  44 33 C6                        xor r8d, esi
0030D16D  4C 3B E3                        cmp r12, rbx
0030D170  0F 84 26 03 00 00               je 0x14030d49c
0030D176  8B D6                           mov edx, esi
0030D178  48 8B CB                        mov rcx, rbx
0030D17B  E8 D0 97 10 00                  call 0x140416950
0030D180  44 8A 6C 24 70                  mov r13b, byte ptr [rsp + 0x70]
0030D185  48 8B CB                        mov rcx, rbx
0030D188  E8 5F A9 F4 FF                  call 0x140257aec
0030D18D  48 8B CB                        mov rcx, rbx
0030D190  E8 EB A8 F4 FF                  call 0x140257a80
0030D195  83 7C 24 20 00                  cmp dword ptr [rsp + 0x20], 0
0030D19A  0F 85 7D 01 00 00               jne 0x14030d31d
0030D1A0  48 3B 7B 18                     cmp rdi, qword ptr [rbx + 0x18]
0030D1A4  0F 85 35 01 00 00               jne 0x14030d2df
0030D1AA  F6 84 24 80 00 00 00 02         test byte ptr [rsp + 0x80], 2
0030D1B2  0F 85 F0 02 00 00               jne 0x14030d4a8
0030D1B8  41 8A C5                        mov al, r13b
0030D1BB  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
0030D1C3  48 83 C4 30                     add rsp, 0x30
0030D1C7  41 5F                           pop r15
0030D1C9  41 5E                           pop r14
0030D1CB  41 5D                           pop r13
0030D1CD  41 5C                           pop r12
0030D1CF  5F                              pop rdi
0030D1D0  5E                              pop rsi
0030D1D1  5D                              pop rbp
0030D1D2  C3                              ret
0030D1D3  CC                              int3
0030D1D4  48 8B 6B 38                     mov rbp, qword ptr [rbx + 0x38]
0030D1D8  4C 89 5B 10                     mov qword ptr [rbx + 0x10], r11
0030D1DC  49 8B 76 10                     mov rsi, qword ptr [r14 + 0x10]
0030D1E0  F6 46 02 04                     test byte ptr [rsi + 2], 4
0030D1E4  0F 85 CC 01 00 00               jne 0x14030d3b6
0030D1EA  8A 8E C3 00 00 00               mov cl, byte ptr [rsi + 0xc3]
0030D1F0  8B 46 78                        mov eax, dword ptr [rsi + 0x78]
0030D1F3  80 E1 7F                        and cl, 0x7f
0030D1F6  D1 E8                           shr eax, 1
0030D1F8  C0 E0 07                        shl al, 7
0030D1FB  0A C1                           or al, cl
0030D1FD  88 45 00                        mov byte ptr [rbp], al
0030D200  4C 8B 83 B8 8E 00 00            mov r8, qword ptr [rbx + 0x8eb8]
0030D207  4D 85 C0                        test r8, r8
0030D20A  74 2C                           je 0x14030d238
0030D20C  48 3B 73 18                     cmp rsi, qword ptr [rbx + 0x18]
0030D210  0F 84 11 02 00 00               je 0x14030d427
0030D216  0F B6 C8                        movzx ecx, al
0030D219  83 E1 7F                        and ecx, 0x7f
0030D21C  41 8B 00                        mov eax, dword ptr [r8]
0030D21F  C1 E8 08                        shr eax, 8
0030D222  0F B6 D0                        movzx edx, al
0030D225  3B CA                           cmp ecx, edx
0030D227  74 0F                           je 0x14030d238
0030D229  0F 8E 03 02 00 00               jle 0x14030d432
0030D22F  2B CA                           sub ecx, edx
0030D231  C1 E1 08                        shl ecx, 8
0030D234  F0 41 01 08                     lock add dword ptr [r8], ecx
0030D238  8B 56 50                        mov edx, dword ptr [rsi + 0x50]
0030D23B  4C 8B 43 38                     mov r8, qword ptr [rbx + 0x38]
0030D23F  41 8A 40 40                     mov al, byte ptr [r8 + 0x40]
0030D243  8A C8                           mov cl, al
0030D245  32 8E 04 02 00 00               xor cl, byte ptr [rsi + 0x204]
0030D24B  80 E1 07                        and cl, 7
0030D24E  32 C1                           xor al, cl
0030D250  8A 8E 05 02 00 00               mov cl, byte ptr [rsi + 0x205]
0030D256  C0 E1 03                        shl cl, 3
0030D259  32 C8                           xor cl, al
0030D25B  80 E1 38                        and cl, 0x38
0030D25E  32 C1                           xor al, cl
0030D260  8B 4E 54                        mov ecx, dword ptr [rsi + 0x54]
0030D263  3B D1                           cmp edx, ecx
0030D265  0F 46 D1                        cmovbe edx, ecx
0030D268  3B 15 0E 81 CB 00               cmp edx, dword ptr [rip + 0xcb810e]
0030D26E  1A C9                           sbb cl, cl
0030D270  24 BF                           and al, 0xbf
0030D272  F6 D1                           not cl
0030D274  80 E1 40                        and cl, 0x40
0030D277  0A C1                           or al, cl
0030D279  41 88 40 40                     mov byte ptr [r8 + 0x40], al
0030D27D  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
0030D281  49 39 46 10                     cmp qword ptr [r14 + 0x10], rax
0030D285  0F 85 54 01 00 00               jne 0x14030d3df
0030D28B  45 8B C7                        mov r8d, r15d
0030D28E  BE 01 00 00 00                  mov esi, 1
0030D293  44 33 C6                        xor r8d, esi
0030D296  4C 3B E3                        cmp r12, rbx
0030D299  0F 84 CA 01 00 00               je 0x14030d469
0030D29F  8B D6                           mov edx, esi
0030D2A1  48 8B CB                        mov rcx, rbx
0030D2A4  E8 A7 96 10 00                  call 0x140416950
0030D2A9  E9 D7 FE FF FF                  jmp 0x14030d185
0030D2AE  32 C0                           xor al, al
0030D2B0  E9 06 FF FF FF                  jmp 0x14030d1bb
0030D2B5  45 85 FF                        test r15d, r15d
0030D2B8  75 54                           jne 0x14030d30e
0030D2BA  4C 8B 64 24 78                  mov r12, qword ptr [rsp + 0x78]
0030D2BF  E9 BC FE FF FF                  jmp 0x14030d180
0030D2C4  E8 67 5F 04 00                  call 0x140353230
0030D2C9  84 C0                           test al, al
0030D2CB  74 6E                           je 0x14030d33b
0030D2CD  48 3B 4B 18                     cmp rcx, qword ptr [rbx + 0x18]
0030D2D1  0F 85 8C FD FF FF               jne 0x14030d063
0030D2D7  44 8B FD                        mov r15d, ebp
0030D2DA  E9 84 FD FF FF                  jmp 0x14030d063
0030D2DF  4C 3B E3                        cmp r12, rbx
0030D2E2  0F 84 C2 FE FF FF               je 0x14030d1aa
0030D2E8  49 83 BC 24 B8 8E 00 00 00      cmp qword ptr [r12 + 0x8eb8], 0
0030D2F1  0F 84 B3 FE FF FF               je 0x14030d1aa
0030D2F7  8A 87 C3 00 00 00               mov al, byte ptr [rdi + 0xc3]
0030D2FD  44 8A EE                        mov r13b, sil
0030D300  41 80 4E 23 04                  or byte ptr [r14 + 0x23], 4
0030D305  41 88 46 24                     mov byte ptr [r14 + 0x24], al
0030D309  E9 9C FE FF FF                  jmp 0x14030d1aa
0030D30E  45 33 C0                        xor r8d, r8d
0030D311  33 D2                           xor edx, edx
0030D313  48 8B CB                        mov rcx, rbx
0030D316  E8 35 96 10 00                  call 0x140416950
0030D31B  EB 9D                           jmp 0x14030d2ba
0030D31D  4C 3B E3                        cmp r12, rbx
0030D320  0F 84 7A FE FF FF               je 0x14030d1a0
0030D326  41 F7 DF                        neg r15d
0030D329  44 8A EE                        mov r13b, sil
0030D32C  1A C0                           sbb al, al
0030D32E  24 F8                           and al, 0xf8
0030D330  04 10                           add al, 0x10
0030D332  41 08 46 23                     or byte ptr [r14 + 0x23], al
0030D336  E9 65 FE FF FF                  jmp 0x14030d1a0
0030D33B  41 8A 46 22                     mov al, byte ptr [r14 + 0x22]
0030D33F  84 C2                           test dl, al
0030D341  0F 84 8C 00 00 00               je 0x14030d3d3
0030D347  41 8A 46 22                     mov al, byte ptr [r14 + 0x22]
0030D34B  40 84 C5                        test bpl, al
0030D34E  0F 85 0F FD FF FF               jne 0x14030d063
0030D354  48 8B D1                        mov rdx, rcx
0030D357  49 8B C9                        mov rcx, r9
0030D35A  E8 B1 3F EF FF                  call 0x140201310
0030D35F  E9 FF FC FF FF                  jmp 0x14030d063
0030D364  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
0030D36E  8B 00                           mov eax, dword ptr [rax]
0030D370  2B 87 B4 01 00 00               sub eax, dword ptr [rdi + 0x1b4]
0030D376  01 87 84 00 00 00               add dword ptr [rdi + 0x84], eax
0030D37C  E9 C8 FD FF FF                  jmp 0x14030d149
0030D381  48 8B D3                        mov rdx, rbx
0030D384  48 8B CF                        mov rcx, rdi
0030D387  E8 14 A8 F4 FF                  call 0x140257ba0
0030D38C  44 8B 94 24 80 00 00 00         mov r10d, dword ptr [rsp + 0x80]
0030D394  8B C8                           mov ecx, eax
0030D396  45 33 DB                        xor r11d, r11d
0030D399  E9 0A FD FF FF                  jmp 0x14030d0a8
0030D39E  41 8A 46 22                     mov al, byte ptr [r14 + 0x22]
0030D3A2  84 C2                           test dl, al
0030D3A4  0F 85 AD FC FF FF               jne 0x14030d057
0030D3AA  40 88 A9 35 02 00 00            mov byte ptr [rcx + 0x235], bpl
0030D3B1  E9 A1 FC FF FF                  jmp 0x14030d057
0030D3B6  48 8B D3                        mov rdx, rbx
0030D3B9  48 8B CE                        mov rcx, rsi
0030D3BC  E8 DF A7 F4 FF                  call 0x140257ba0
0030D3C1  44 8B 94 24 80 00 00 00         mov r10d, dword ptr [rsp + 0x80]
0030D3C9  8B C8                           mov ecx, eax
0030D3CB  45 33 DB                        xor r11d, r11d
0030D3CE  E9 1D FE FF FF                  jmp 0x14030d1f0
0030D3D3  40 88 A9 35 02 00 00            mov byte ptr [rcx + 0x235], bpl
0030D3DA  E9 68 FF FF FF                  jmp 0x14030d347
0030D3DF  45 85 FF                        test r15d, r15d
0030D3E2  0F 85 8D 00 00 00               jne 0x14030d475
0030D3E8  BE 01 00 00 00                  mov esi, 1
0030D3ED  E9 93 FD FF FF                  jmp 0x14030d185
0030D3F2  48 3B 7B 18                     cmp rdi, qword ptr [rbx + 0x18]
0030D3F6  74 27                           je 0x14030d41f
0030D3F8  0F B6 C8                        movzx ecx, al
0030D3FB  83 E1 7F                        and ecx, 0x7f
0030D3FE  41 8B 00                        mov eax, dword ptr [r8]
0030D401  C1 E8 08                        shr eax, 8
0030D404  0F B6 D0                        movzx edx, al
0030D407  3B CA                           cmp ecx, edx
0030D409  0F 84 BA FC FF FF               je 0x14030d0c9
0030D40F  7E 2E                           jle 0x14030d43f
0030D411  2B CA                           sub ecx, edx
0030D413  C1 E1 08                        shl ecx, 8
0030D416  F0 41 01 08                     lock add dword ptr [r8], ecx
0030D41A  E9 AA FC FF FF                  jmp 0x14030d0c9
0030D41F  8B 0D 27 7C CB 00               mov ecx, dword ptr [rip + 0xcb7c27]
0030D425  EB D7                           jmp 0x14030d3fe
0030D427  8B 0D 1F 7C CB 00               mov ecx, dword ptr [rip + 0xcb7c1f]
0030D42D  E9 EA FD FF FF                  jmp 0x14030d21c
0030D432  C1 E1 08                        shl ecx, 8
0030D435  C1 E2 08                        shl edx, 8
0030D438  2B CA                           sub ecx, edx
0030D43A  E9 F5 FD FF FF                  jmp 0x14030d234
0030D43F  C1 E1 08                        shl ecx, 8
0030D442  C1 E2 08                        shl edx, 8
0030D445  2B CA                           sub ecx, edx
0030D447  EB CD                           jmp 0x14030d416
0030D449  F6 46 02 04                     test byte ptr [rsi + 2], 4
0030D44D  48 8B 7B 38                     mov rdi, qword ptr [rbx + 0x38]
0030D451  0F 85 93 38 3D 00               jne 0x1406e0cea
0030D457  8A 8E C3 00 00 00               mov cl, byte ptr [rsi + 0xc3]
0030D45D  E9 95 38 3D 00                  jmp 0x1406e0cf7
0030D462  B9 21 00 00 00                  mov ecx, 0x21
0030D467  CD 29                           int 0x29
0030D469  44 84 D6                        test sil, r10b
0030D46C  45 0F 45 C3                     cmovne r8d, r11d
0030D470  E9 2A FE FF FF                  jmp 0x14030d29f
0030D475  45 33 C0                        xor r8d, r8d
0030D478  33 D2                           xor edx, edx
0030D47A  48 8B CB                        mov rcx, rbx
0030D47D  E8 CE 94 10 00                  call 0x140416950
0030D482  E9 61 FF FF FF                  jmp 0x14030d3e8
0030D487  F6 46 02 04                     test byte ptr [rsi + 2], 4
0030D48B  0F 85 F8 38 3D 00               jne 0x1406e0d89
0030D491  8A 86 C3 00 00 00               mov al, byte ptr [rsi + 0xc3]
0030D497  E9 03 39 3D 00                  jmp 0x1406e0d9f
0030D49C  44 84 D6                        test sil, r10b
0030D49F  45 0F 45 C3                     cmovne r8d, r11d
0030D4A3  E9 CE FC FF FF                  jmp 0x14030d176
0030D4A8  48 85 FF                        test rdi, rdi
0030D4AB  0F 84 07 FD FF FF               je 0x14030d1b8
0030D4B1  66 F0 01 B7 64 03 00 00         lock add word ptr [rdi + 0x364], si
0030D4B9  41 80 4E 23 03                  or byte ptr [r14 + 0x23], 3
0030D4BE  44 8A EE                        mov r13b, sil
0030D4C1  E9 F2 FC FF FF                  jmp 0x14030d1b8
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiCommitRescheduleContextEntry(__int64 a1, __int64 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rsp;
    unsigned int v_stack_m48;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p78;
    unsigned __int8 v_stack_p8;
    unsigned int v_stack_p80;

    v_stack_p20 = v_rbx;
    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (48);
    v_r11 = 0;
    v_stack_p8 = 0;
    if ((*(unsigned __int64 *)(a1 + 24)) == -1) goto loc_0030D2AE;
    if ((*(unsigned __int64 *)(a1 + 24)) == -2) goto loc_0030D449;
    v_stack_m48 = 0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 16) != 0) goto loc_0030D2C4;
    result = KiIsPrcbThread(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8), 2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_0030D057;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8) + 388))) == 2) goto loc_0030D39E;
loc_0030D057:
    v_stack_m48 = (unsigned int)(v_r11 + 1);
    v_r15 = ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24))) ? 1 : 0;
loc_0030D063:
    result = (unsigned __int8)(~(*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 35)));
    result = (unsigned int)((result) & ((unsigned int)(v_r11 + 1)));
    if (((unsigned int)(v_r15)) != ((unsigned int)(result))) goto loc_0030D462;
    if (*(unsigned __int64 *)(a1 + 24) == 0) goto loc_0030D1D4;
    v_r12 = (unsigned int)((*(unsigned __int8 *)(a1 + 33)) + ((unsigned int)(*(unsigned __int8 *)(a1 + 33))));
    if ((*(unsigned __int64 *)(a1 + 24)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 36480))) goto loc_0030D487;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 24) + 2)) & (4)) != 0) goto loc_0030D381;
loc_0030D0A8:
    a1 = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 24) + 195)) & (127));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 24) + 120))) >> (1));
    result = (unsigned __int8)((result) << (7));
    result = (unsigned __int8)((result) | ((unsigned __int8)(a1)));
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 56)) = (unsigned __int8)(result);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 36536) != 0) goto loc_0030D3F2;
loc_0030D0C9:
    a1 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 56) + 64))) ^ (*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 24) + 516)));
    a1 = (unsigned __int8)((a1) & (7));
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 56) + 64)) ^ ((unsigned __int8)(a1)));
    a1 = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 24) + 517)) << (3));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(result)));
    a1 = (unsigned __int8)((a1) & (56));
    result = (unsigned __int8)((result) ^ ((unsigned __int8)(a1)));
    a2 = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 24) + 80));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 24) + 80)))) <= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 24) + 84))))) { a2 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 24) + 84))); }
    result = (unsigned __int8)((result) & (191));
    a1 = (unsigned __int8)(~((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 24) + 84))));
    a1 = (unsigned __int8)((a1) & (64));
    result = (unsigned __int8)((result) | ((unsigned __int8)(a1)));
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 56) + 64) = (unsigned __int8)(result);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 16) = *(unsigned __int64 *)(a1 + 24);
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 36536) != 0) {
        result = ((*(unsigned __int64 *)(a1 + 24)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24))) ? 1 : 0;
        *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 36536) + 16) = (unsigned __int8)(result);
    }
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 24) + 388))) == 1) goto loc_0030D364;
    if ((((unsigned __int8)(v_r12)) & (2)) != 0) goto loc_0030D364;
loc_0030D149:
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 24) + 388) = 3;
    if ((*(unsigned __int64 *)(a1 + 24)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24 * 1))) goto loc_0030D2B5;
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) ^ (1));
    if (v_stack_p10 == (*(unsigned __int64 *)(a1))) goto loc_0030D49C;
loc_0030D176:
    result = KiSetProcessorIdle(*(unsigned __int64 *)(a1), 1, a3, a4);
loc_0030D180:
loc_0030D185:
    result = KiUpdateThreadQosGroupingSummaries(*(unsigned __int64 *)(a1), 1, a3, a4);
    result = KiUpdateStandbyStealSummaryForStandbyChange(*(unsigned __int64 *)(a1), 1, a3, a4);
    if (v_stack_m48 != 0) goto loc_0030D31D;
loc_0030D1A0:
    if ((*(unsigned __int64 *)(a1 + 24)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24))) goto loc_0030D2DF;
loc_0030D1AA:
    if (((v_stack_p18) & (2)) != 0) goto loc_0030D4A8;
loc_0030D1B8:
loc_0030D1BB:
    v_rsp = (v_rsp) + (48);
    return (unsigned __int8)(v_stack_p8);
loc_0030D1D4:
    *(unsigned __int64 *)(v_stack_p20 + 16) = 0;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 16) + 2)) & (4)) != 0) goto loc_0030D3B6;
loc_0030D1F0:
    a1 = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 16) + 195)) & (127));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 16) + 120))) >> (1));
    result = (unsigned __int8)((result) << (7));
    result = (unsigned __int8)((result) | ((unsigned __int8)(a1)));
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p20 + 56)) = (unsigned __int8)(result);
    if (*(unsigned __int64 *)(v_stack_p20 + 36536) == 0) goto loc_0030D238;
    if ((*(unsigned __int64 *)(a1 + 16)) == (*(unsigned __int64 *)(v_stack_p20 + 24))) goto loc_0030D427;
    a1 = (unsigned int)(((unsigned __int8)(result)) & (127));
loc_0030D21C:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p20 + 36536)))) >> (8));
    if (((unsigned int)(a1)) == ((unsigned int)((unsigned __int8)(result)))) goto loc_0030D238;
    if (((unsigned int)(a1)) <= ((unsigned int)((unsigned __int8)(result)))) goto loc_0030D432;
    a1 = (unsigned int)((a1) - ((unsigned int)((unsigned __int8)(result))));
    a1 = (unsigned int)((a1) << (8));
loc_0030D234:
loc_0030D238:
    a1 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p20 + 56) + 64))) ^ (*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 16) + 516)));
    a1 = (unsigned __int8)((a1) & (7));
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p20 + 56) + 64)) ^ ((unsigned __int8)(a1)));
    a1 = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 16) + 517)) << (3));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(result)));
    a1 = (unsigned __int8)((a1) & (56));
    result = (unsigned __int8)((result) ^ ((unsigned __int8)(a1)));
    a2 = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 16) + 80));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 16) + 80)))) <= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 16) + 84))))) { a2 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 16) + 84))); }
    result = (unsigned __int8)((result) & (191));
    a1 = (unsigned __int8)(~((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 16) + 84))));
    a1 = (unsigned __int8)((a1) & (64));
    result = (unsigned __int8)((result) | ((unsigned __int8)(a1)));
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p20 + 56) + 64) = (unsigned __int8)(result);
    if ((*(unsigned __int64 *)(a1 + 16)) != (*(unsigned __int64 *)(v_stack_p20 + 24))) goto loc_0030D3DF;
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) ^ (1));
    if (v_stack_p10 == v_stack_p20) goto loc_0030D469;
loc_0030D29F:
    result = KiSetProcessorIdle(v_stack_p20, 1, a3, a4);
    goto loc_0030D185;
loc_0030D2AE:
    result = 0;
    goto loc_0030D1BB;
loc_0030D2B5:
    if ((unsigned int)(v_r15) != 0) goto loc_0030D30E;
loc_0030D2BA:
    goto loc_0030D180;
loc_0030D2C4:
    result = KiIsPrcbThread(v_stack_p20, 1, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0030D33B;
    if (v_stack_p20 != (*(unsigned __int64 *)(v_stack_p20 + 24))) goto loc_0030D063;
    goto loc_0030D063;
loc_0030D2DF:
    if (v_stack_p78 == v_stack_p20) goto loc_0030D1AA;
    if ((*(unsigned __int64 *)(v_stack_p78 + 36536)) == 0) goto loc_0030D1AA;
    *(unsigned __int8 *)(a1 + 36) = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 24) + 195));
    goto loc_0030D1AA;
loc_0030D30E:
    a3 = 0;
    a2 = 0;
    result = KiSetProcessorIdle(v_stack_p20, a2, a3, a4);
    goto loc_0030D2BA;
loc_0030D31D:
    if (v_stack_p78 == v_stack_p20) goto loc_0030D1A0;
    v_r15 = (unsigned int)(-((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_p20 + 56)))));
    result = (unsigned __int8)((result) & (248));
    result = (unsigned __int8)((result) + (16));
    goto loc_0030D1A0;
loc_0030D33B:
    if (((0) & ((unsigned __int8)(*(unsigned __int8 *)(a1 + 34)))) == 0) goto loc_0030D3D3;
loc_0030D347:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_p20 + 56))) & ((unsigned __int8)(*(unsigned __int8 *)(a1 + 34)))) != 0) goto loc_0030D063;
    result = KiInsertDeferredReadyList(a4, v_stack_p20, a3, a4);
    goto loc_0030D063;
loc_0030D364:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result))) - (*(unsigned int *)(*(unsigned __int64 *)(a1 + 24) + 436)));
    goto loc_0030D149;
loc_0030D381:
    result = KiQueryEffectivePriorityThread(*(unsigned __int64 *)(a1 + 24), v_stack_p20, a3, a4);
    v_r11 = 0;
    goto loc_0030D0A8;
loc_0030D39E:
    if ((((unsigned __int8)(v_stack_p20)) & ((unsigned __int8)(*(unsigned __int8 *)(a1 + 34)))) != 0) goto loc_0030D057;
    *(unsigned __int8 *)((unsigned int)((unsigned int)(result)) + 565) = (unsigned __int8)(*(unsigned __int64 *)(v_stack_p20 + 56));
    goto loc_0030D057;
loc_0030D3B6:
    result = KiQueryEffectivePriorityThread(1, v_stack_p20, a3, a4);
    v_r11 = 0;
    goto loc_0030D1F0;
loc_0030D3D3:
    *(unsigned __int8 *)((unsigned int)((unsigned int)(result)) + 565) = (unsigned __int8)(*(unsigned __int64 *)(v_stack_p20 + 56));
    goto loc_0030D347;
loc_0030D3DF:
    if ((unsigned int)(v_r15) != 0) goto loc_0030D475;
loc_0030D3E8:
    goto loc_0030D185;
loc_0030D3F2:
    if ((*(unsigned __int64 *)(a1 + 24)) == (*(unsigned __int64 *)(v_stack_p20 + 24))) goto loc_0030D41F;
    a1 = (unsigned int)(((unsigned __int8)(result)) & (127));
loc_0030D3FE:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a3))) >> (8));
    if (((unsigned int)(a1)) == ((unsigned int)((unsigned __int8)(result)))) goto loc_0030D0C9;
    if (((unsigned int)(a1)) <= ((unsigned int)((unsigned __int8)(result)))) goto loc_0030D43F;
    a1 = (unsigned int)((a1) - ((unsigned int)((unsigned __int8)(result))));
    a1 = (unsigned int)((a1) << (8));
loc_0030D416:
    goto loc_0030D0C9;
loc_0030D41F:
    goto loc_0030D3FE;
loc_0030D427:
    goto loc_0030D21C;
loc_0030D432:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 13335583))) << (8));
    a2 = (unsigned int)(((unsigned __int8)(result)) << (8));
    a1 = (unsigned int)((a1) - ((unsigned int)(a2)));
    goto loc_0030D234;
loc_0030D43F:
    a1 = (unsigned int)((a1) << (8));
    a2 = (unsigned int)((a2) << (8));
    a1 = (unsigned int)((a1) - ((unsigned int)(a2)));
    goto loc_0030D416;
loc_0030D449:
loc_0030D462:
loc_0030D469:
    if (((1) & ((unsigned __int8)((unsigned int)(v_stack_p80)))) != 0) { a3 = 0; }
    goto loc_0030D29F;
loc_0030D475:
    a3 = 0;
    a2 = 0;
    result = KiSetProcessorIdle(v_stack_p20, a2, a3, a4);
    goto loc_0030D3E8;
loc_0030D487:
loc_0030D49C:
    if (((1) & ((unsigned __int8)((unsigned int)(v_stack_p80)))) != 0) { a3 = 0; }
    goto loc_0030D176;
loc_0030D4A8:
    if (*(unsigned __int64 *)(v_stack_p20 + 56) == 0) goto loc_0030D1B8;
    goto loc_0030D1B8;
}
```

## 5. (Beta) C Style

```c
int64_t KiCommitRescheduleContextEntry(void *Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rsp;
    uint32_t v_stack_m48;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p78;
    uint8_t v_stack_p8;
    uint32_t v_stack_p80;

    v_stack_p20 = local_rbx;
    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (48);
    local_r11 = 0;
    v_stack_p8 = 0;
    if ((*(uint64_t *)(arg1 + 0x18)) == -1) goto loc_0030D2AE;
    if ((*(uint64_t *)(arg1 + 0x18)) == -2) goto loc_0030D449;
    v_stack_m48 = 0;
    if (*(uint64_t *)(*(uint64_t *)(arg1) + 0x10) != 0) goto loc_0030D2C4;
    result = KiIsPrcbThread(*(uint64_t *)(*(uint64_t *)(arg1) + 0x8), 2, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_0030D057;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x8) + 0x184))) == 2) goto loc_0030D39E;
loc_0030D057:
    v_stack_m48 = (uint32_t)(local_r11 + 1);
    local_r15 = ((*(uint64_t *)(*(uint64_t *)(arg1) + 0x8)) == (*(uint64_t *)(*(uint64_t *)(arg1) + 0x18))) ? 1 : 0;
loc_0030D063:
    result = (uint8_t)(~(*(uint8_t *)(*(uint64_t *)(arg1) + 0x23)));
    result = (uint32_t)((result) & ((uint32_t)(local_r11 + 1)));
    if (((uint32_t)(local_r15)) != ((uint32_t)(result))) goto loc_0030D462;
    if (*(uint64_t *)(arg1 + 0x18) == 0) goto loc_0030D1D4;
    local_r12 = (uint32_t)((*(uint8_t *)(arg1 + 0x21)) + ((uint32_t)(*(uint8_t *)(arg1 + 0x21))));
    if ((*(uint64_t *)(arg1 + 0x18)) == (*(uint64_t *)(*(uint64_t *)(arg1) + 0x8E80))) goto loc_0030D487;
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x18) + 0x2)) & (4)) != 0) goto loc_0030D381;
loc_0030D0A8:
    Arg1 = (uint8_t)((*(uint8_t *)(*(uint64_t *)(arg1 + 0x18) + 0xC3)) & (127));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x18) + 0x78))) >> (1));
    result = (uint8_t)((result) << (7));
    result = (uint8_t)((result) | ((uint8_t)(Arg1)));
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x38)) = (uint8_t)(result);
    if (*(uint64_t *)(*(uint64_t *)(arg1) + 0x8EB8) != 0) goto loc_0030D3F2;
loc_0030D0C9:
    Arg1 = (uint8_t)(((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x38) + 0x40))) ^ (*(uint8_t *)(*(uint64_t *)(arg1 + 0x18) + 0x204)));
    Arg1 = (uint8_t)((Arg1) & (7));
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x38) + 0x40)) ^ ((uint8_t)(Arg1)));
    Arg1 = (uint8_t)((*(uint8_t *)(*(uint64_t *)(arg1 + 0x18) + 0x205)) << (3));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(result)));
    Arg1 = (uint8_t)((Arg1) & (56));
    result = (uint8_t)((result) ^ ((uint8_t)(Arg1)));
    Arg2 = (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x18) + 0x50));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x18) + 0x50)))) <= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x18) + 0x54))))) { Arg2 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x18) + 0x54))); }
    result = (uint8_t)((result) & (191));
    Arg1 = (uint8_t)(~((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x18) + 0x54))));
    Arg1 = (uint8_t)((Arg1) & (64));
    result = (uint8_t)((result) | ((uint8_t)(Arg1)));
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x38) + 0x40) = (uint8_t)(result);
    *(uint64_t *)(*(uint64_t *)(arg1) + 0x10) = *(uint64_t *)(arg1 + 0x18);
    result = *(uint64_t *)(*(uint64_t *)(arg1) + 0x18);
    if (*(uint64_t *)(*(uint64_t *)(arg1) + 0x8EB8) != 0) {
        result = ((*(uint64_t *)(arg1 + 0x18)) == (*(uint64_t *)(*(uint64_t *)(arg1) + 0x18))) ? 1 : 0;
        *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x8EB8) + 0x10) = (uint8_t)(result);
    }
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x18) + 0x184))) == 1) goto loc_0030D364;
    if ((((uint8_t)(local_r12)) & (2)) != 0) goto loc_0030D364;
loc_0030D149:
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x18) + 0x184) = 3;
    if ((*(uint64_t *)(arg1 + 0x18)) != (*(uint64_t *)(*(uint64_t *)(arg1) + 0x18 * 1))) goto loc_0030D2B5;
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) ^ (1));
    if (v_stack_p10 == (*(uint64_t *)(arg1))) goto loc_0030D49C;
loc_0030D176:
    result = KiSetProcessorIdle(*(uint64_t *)(arg1), 1, Arg3, Arg4);
loc_0030D180:
loc_0030D185:
    result = KiUpdateThreadQosGroupingSummaries(*(uint64_t *)(arg1), 1, Arg3, Arg4);
    result = KiUpdateStandbyStealSummaryForStandbyChange(*(uint64_t *)(arg1), 1, Arg3, Arg4);
    if (v_stack_m48 != 0) goto loc_0030D31D;
loc_0030D1A0:
    if ((*(uint64_t *)(arg1 + 0x18)) != (*(uint64_t *)(*(uint64_t *)(arg1) + 0x18))) goto loc_0030D2DF;
loc_0030D1AA:
    if (((v_stack_p18) & (2)) != 0) goto loc_0030D4A8;
loc_0030D1B8:
loc_0030D1BB:
    local_rsp = (local_rsp) + (48);
    return (uint8_t)(v_stack_p8);
loc_0030D1D4:
    *(uint64_t *)(v_stack_p20 + 0x10) = 0;
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x10) + 0x2)) & (4)) != 0) goto loc_0030D3B6;
loc_0030D1F0:
    Arg1 = (uint8_t)((*(uint8_t *)(*(uint64_t *)(arg1 + 0x10) + 0xC3)) & (127));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x10) + 0x78))) >> (1));
    result = (uint8_t)((result) << (7));
    result = (uint8_t)((result) | ((uint8_t)(Arg1)));
    *(uint8_t *)(*(uint64_t *)(v_stack_p20 + 0x38)) = (uint8_t)(result);
    if (*(uint64_t *)(v_stack_p20 + 0x8EB8) == 0) goto loc_0030D238;
    if ((*(uint64_t *)(arg1 + 0x10)) == (*(uint64_t *)(v_stack_p20 + 0x18))) goto loc_0030D427;
    Arg1 = (uint32_t)(((uint8_t)(result)) & (127));
loc_0030D21C:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p20 + 0x8EB8)))) >> (8));
    if (((uint32_t)(Arg1)) == ((uint32_t)((uint8_t)(result)))) goto loc_0030D238;
    if (((uint32_t)(Arg1)) <= ((uint32_t)((uint8_t)(result)))) goto loc_0030D432;
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)((uint8_t)(result))));
    Arg1 = (uint32_t)((Arg1) << (8));
loc_0030D234:
loc_0030D238:
    Arg1 = (uint8_t)(((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_stack_p20 + 0x38) + 0x40))) ^ (*(uint8_t *)(*(uint64_t *)(arg1 + 0x10) + 0x204)));
    Arg1 = (uint8_t)((Arg1) & (7));
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(v_stack_p20 + 0x38) + 0x40)) ^ ((uint8_t)(Arg1)));
    Arg1 = (uint8_t)((*(uint8_t *)(*(uint64_t *)(arg1 + 0x10) + 0x205)) << (3));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(result)));
    Arg1 = (uint8_t)((Arg1) & (56));
    result = (uint8_t)((result) ^ ((uint8_t)(Arg1)));
    Arg2 = (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x10) + 0x50));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x10) + 0x50)))) <= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x10) + 0x54))))) { Arg2 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x10) + 0x54))); }
    result = (uint8_t)((result) & (191));
    Arg1 = (uint8_t)(~((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x10) + 0x54))));
    Arg1 = (uint8_t)((Arg1) & (64));
    result = (uint8_t)((result) | ((uint8_t)(Arg1)));
    *(uint8_t *)(*(uint64_t *)(v_stack_p20 + 0x38) + 0x40) = (uint8_t)(result);
    if ((*(uint64_t *)(arg1 + 0x10)) != (*(uint64_t *)(v_stack_p20 + 0x18))) goto loc_0030D3DF;
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) ^ (1));
    if (v_stack_p10 == v_stack_p20) goto loc_0030D469;
loc_0030D29F:
    result = KiSetProcessorIdle(v_stack_p20, 1, Arg3, Arg4);
    goto loc_0030D185;
loc_0030D2AE:
    result = 0;
    goto loc_0030D1BB;
loc_0030D2B5:
    if ((uint32_t)(local_r15) != 0) goto loc_0030D30E;
loc_0030D2BA:
    goto loc_0030D180;
loc_0030D2C4:
    result = KiIsPrcbThread(v_stack_p20, 1, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0030D33B;
    if (v_stack_p20 != (*(uint64_t *)(v_stack_p20 + 0x18))) goto loc_0030D063;
    goto loc_0030D063;
loc_0030D2DF:
    if (v_stack_p78 == v_stack_p20) goto loc_0030D1AA;
    if ((*(uint64_t *)(v_stack_p78 + 0x8EB8)) == 0) goto loc_0030D1AA;
    *(uint8_t *)(arg1 + 0x24) = (uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x18) + 0xC3));
    goto loc_0030D1AA;
loc_0030D30E:
    Arg3 = 0;
    Arg2 = 0;
    result = KiSetProcessorIdle(v_stack_p20, Arg2, Arg3, Arg4);
    goto loc_0030D2BA;
loc_0030D31D:
    if (v_stack_p78 == v_stack_p20) goto loc_0030D1A0;
    local_r15 = (uint32_t)(-((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_p20 + 0x38)))));
    result = (uint8_t)((result) & (248));
    result = (uint8_t)((result) + (16));
    goto loc_0030D1A0;
loc_0030D33B:
    if (((0) & ((uint8_t)(*(uint8_t *)(arg1 + 0x22)))) == 0) goto loc_0030D3D3;
loc_0030D347:
    if ((((uint8_t)(*(uint64_t *)(v_stack_p20 + 0x38))) & ((uint8_t)(*(uint8_t *)(arg1 + 0x22)))) != 0) goto loc_0030D063;
    result = KiInsertDeferredReadyList(Arg4, v_stack_p20, Arg3, Arg4);
    goto loc_0030D063;
loc_0030D364:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result))) - (*(uint32_t *)(*(uint64_t *)(arg1 + 0x18) + 0x1B4)));
    goto loc_0030D149;
loc_0030D381:
    result = KiQueryEffectivePriorityThread(*(uint64_t *)(arg1 + 0x18), v_stack_p20, Arg3, Arg4);
    local_r11 = 0;
    goto loc_0030D0A8;
loc_0030D39E:
    if ((((uint8_t)(v_stack_p20)) & ((uint8_t)(*(uint8_t *)(arg1 + 0x22)))) != 0) goto loc_0030D057;
    *(uint8_t *)((uint32_t)((uint32_t)(result)) + 0x235) = (uint8_t)(*(uint64_t *)(v_stack_p20 + 0x38));
    goto loc_0030D057;
loc_0030D3B6:
    result = KiQueryEffectivePriorityThread(1, v_stack_p20, Arg3, Arg4);
    local_r11 = 0;
    goto loc_0030D1F0;
loc_0030D3D3:
    *(uint8_t *)((uint32_t)((uint32_t)(result)) + 0x235) = (uint8_t)(*(uint64_t *)(v_stack_p20 + 0x38));
    goto loc_0030D347;
loc_0030D3DF:
    if ((uint32_t)(local_r15) != 0) goto loc_0030D475;
loc_0030D3E8:
    goto loc_0030D185;
loc_0030D3F2:
    if ((*(uint64_t *)(arg1 + 0x18)) == (*(uint64_t *)(v_stack_p20 + 0x18))) goto loc_0030D41F;
    Arg1 = (uint32_t)(((uint8_t)(result)) & (127));
loc_0030D3FE:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg3))) >> (8));
    if (((uint32_t)(Arg1)) == ((uint32_t)((uint8_t)(result)))) goto loc_0030D0C9;
    if (((uint32_t)(Arg1)) <= ((uint32_t)((uint8_t)(result)))) goto loc_0030D43F;
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)((uint8_t)(result))));
    Arg1 = (uint32_t)((Arg1) << (8));
loc_0030D416:
    goto loc_0030D0C9;
loc_0030D41F:
    goto loc_0030D3FE;
loc_0030D427:
    goto loc_0030D21C;
loc_0030D432:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xCB7C1F))) << (8));
    Arg2 = (uint32_t)(((uint8_t)(result)) << (8));
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(Arg2)));
    goto loc_0030D234;
loc_0030D43F:
    Arg1 = (uint32_t)((Arg1) << (8));
    Arg2 = (uint32_t)((Arg2) << (8));
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(Arg2)));
    goto loc_0030D416;
loc_0030D449:
loc_0030D462:
loc_0030D469:
    if (((1) & ((uint8_t)((uint32_t)(v_stack_p80)))) != 0) { Arg3 = 0; }
    goto loc_0030D29F;
loc_0030D475:
    Arg3 = 0;
    Arg2 = 0;
    result = KiSetProcessorIdle(v_stack_p20, Arg2, Arg3, Arg4);
    goto loc_0030D3E8;
loc_0030D487:
loc_0030D49C:
    if (((1) & ((uint8_t)((uint32_t)(v_stack_p80)))) != 0) { Arg3 = 0; }
    goto loc_0030D176;
loc_0030D4A8:
    if (*(uint64_t *)(v_stack_p20 + 0x38) == 0) goto loc_0030D1B8;
    goto loc_0030D1B8;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x21` | `8` | `R` |
| `Arg1` | `+ 0x22` | `8` | `R` |
| `Arg1` | `+ 0x23` | `8` | `R/W` |
| `Arg1` | `+ 0x24` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0030CFD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
