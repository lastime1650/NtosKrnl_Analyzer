# CcCanIWrite

- RVA: `0x00388250`–`0x0038878E` (길이 `1,342` bytes)
- VA: `0x0000000140388250`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0007FE50`
- 디코드: `308`개 명령, `1,342/1,342` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **22**; 고유 호출 대상: **22**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x003882E0` → [KeRcuReadLock](KeRcuReadLock_function_0038A1A0.md) (function, `0x0038A1A0`)
- `0x003882E8` → [CcReferencePartitionFromFileObject](CcReferencePartitionFromFileObject_function_00388200.md) (function, `0x00388200`)
- `0x003882F6` → [CcGetPrivateVolumeCacheMapFromFileObject](CcGetPrivateVolumeCacheMapFromFileObject_function_00388794.md) (function, `0x00388794`)
- `0x00388301` → [CcReferencePrivateVolumeCacheMap](../35/CcReferencePrivateVolumeCacheMap_function_00357210.md) (function, `0x00357210`)
- `0x00388352` → [CcIsFileObjectDirectMapped](CcIsFileObjectDirectMapped_function_00388D10.md) (function, `0x00388D10`)
- `0x00388399` → [KeRcuReadUnlock](KeRcuReadUnlock_function_0038A070.md) (function, `0x0038A070`)
- `0x00388411` → [CcCanIWriteStreamEx](CcCanIWriteStreamEx_function_0038993C.md) (function, `0x0038993C`)
- `0x0038844A` → [CcDecrementVolumeUseCountWithDelete](CcDecrementVolumeUseCountWithDelete_function_0038B888.md) (function, `0x0038B888`)
- `0x0038845C` → [CcDereferencePartitionAndPrivateVolumeCacheMap](CcDereferencePartitionAndPrivateVolumeCacheMap_function_0038B94C.md) (function, `0x0038B94C`)
- `0x003884A2` → [CcAdjustWriteBehindThreadPoolIfNeeded](CcAdjustWriteBehindThreadPoolIfNeeded_function_00386D94.md) (function, `0x00386D94`)
- `0x003884F3` → [DbgPrintEx](../35/DbgPrintEx_function_00359290.md) (function, `0x00359290`)
- `0x0038850A` → [KeDelayExecutionThread](../20/KeDelayExecutionThread_function_00209550.md) (function, `0x00209550`)
- `0x00388561` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x003885D4` → [ExInterlockedInsertHeadList](ExInterlockedInsertHeadList_function_00386680.md) (function, `0x00386680`)
- `0x003885E7` → [KeAcquireInStackQueuedSpinLock](../27/KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)
- `0x0038860F` → [CcNotifyWriteBehindVolume](../3C/CcNotifyWriteBehindVolume_function_003CC134.md) (function, `0x003CC134`)
- `0x00388627` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x00388632` → [CcPostDeferredWrites](../35/CcPostDeferredWrites_function_003590FC.md) (function, `0x003590FC`)
- `0x00388650` → [KeWaitForSingleObject](../20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x00388681` → [ExInterlockedInsertTailList](ExInterlockedInsertTailList_function_00386700.md) (function, `0x00386700`)
- `0x003886AA` → [CcNotifyWriteBehindInternal](../3C/CcNotifyWriteBehindInternal_function_003CC224.md) (function, `0x003CC224`)
- `0x0038874A` → [CcPerfLogCanWriteFail](../57/CcPerfLogCanWriteFail_function_0057F21C.md) (function, `0x0057F21C`)

### Direct callers
- [FsRtlPrepareMdlWriteDev](../../page/71/FsRtlPrepareMdlWriteDev_function_00713BB0.md) at `0x00713C23`
- [FsRtlCopyWrite](../../page/A4/FsRtlCopyWrite_function_00A48210.md) at `0x00A4827D`

### Static image references
- `0x00388306` → RVA `0x00E65B88` (`.data`; read)
- `0x00388357` → RVA `0x00F8F2A1` (`.data`; read)
- `0x0038847F` → RVA `0x00E65B54` (`.data`; read)
- `0x0038848D` → RVA `0x00FC6B10` (`ALMOSTRO`; read)
- `0x003884CD` → RVA `0x00E65B6C` (`.data`; read)
- `0x003884D4` → RVA `0x006C7CC0` (` ?? ::FNODOBFM::`string'`; read)
- `0x00388637` → RVA `0x00E0A880` (`.data`; read)
- `0x003886D3` → RVA `0x00FC6EA0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **5**
  - `0x0038866C` → [sub_006E4F4E + 0x8](../6E/Unknown_function_006E4F4E.md) (`tail-transfer`)
  - `0x00388676` → [sub_006E4F4E + 0x8](../6E/Unknown_function_006E4F4E.md) (`tail-transfer`)
  - `0x0038867C` → [sub_006E4F4E + 0x38](../6E/Unknown_function_006E4F4E.md) (`tail-transfer`)
  - `0x0038876A` → [sub_006E4F4E](../6E/Unknown_function_006E4F4E.md) (`tail-transfer`)
  - `0x00388777` → [sub_006E4F4E](../6E/Unknown_function_006E4F4E.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00388250  48 8B C4                        mov rax, rsp
00388253  48 89 58 08                     mov qword ptr [rax + 8], rbx
00388257  44 88 48 20                     mov byte ptr [rax + 0x20], r9b
0038825B  44 88 40 18                     mov byte ptr [rax + 0x18], r8b
0038825F  89 50 10                        mov dword ptr [rax + 0x10], edx
00388262  55                              push rbp
00388263  56                              push rsi
00388264  57                              push rdi
00388265  41 54                           push r12
00388267  41 55                           push r13
00388269  41 56                           push r14
0038826B  41 57                           push r15
0038826D  48 8D 68 B8                     lea rbp, [rax - 0x48]
00388271  48 81 EC 10 01 00 00            sub rsp, 0x110
00388278  33 C0                           xor eax, eax
0038827A  33 F6                           xor esi, esi
0038827C  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
00388280  45 33 C0                        xor r8d, r8d
00388283  45 33 F6                        xor r14d, r14d
00388286  88 44 24 42                     mov byte ptr [rsp + 0x42], al
0038828A  0F 57 C0                        xorps xmm0, xmm0
0038828D  88 44 24 41                     mov byte ptr [rsp + 0x41], al
00388291  0F 11 45 88                     movups xmmword ptr [rbp - 0x78], xmm0
00388295  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0038829E  8D 5E 01                        lea ebx, [rsi + 1]
003882A1  45 8A D1                        mov r10b, r9b
003882A4  44 89 44 24 44                  mov dword ptr [rsp + 0x44], r8d
003882A9  44 8B CA                        mov r9d, edx
003882AC  4C 89 75 80                     mov qword ptr [rbp - 0x80], r14
003882B0  4C 8B E9                        mov r13, rcx
003882B3  8B 90 A4 05 00 00               mov edx, dword ptr [rax + 0x5a4]
003882B9  F6 C2 02                        test dl, 2
003882BC  0F 85 9F 01 00 00               jne 0x140388461
003882C2  48 85 C9                        test rcx, rcx
003882C5  0F 84 08 04 00 00               je 0x1403886d3
003882CB  8B 41 50                        mov eax, dword ptr [rcx + 0x50]
003882CE  A8 10                           test al, 0x10
003882D0  0F 85 8B 01 00 00               jne 0x140388461
003882D6  0F BA E0 18                     bt eax, 0x18
003882DA  0F 82 81 01 00 00               jb 0x140388461
003882E0  E8 BB 1E 00 00                  call 0x14038a1a0
003882E5  49 8B CD                        mov rcx, r13
003882E8  E8 13 FF FF FF                  call 0x140388200
003882ED  48 8B D0                        mov rdx, rax
003882F0  49 8B CD                        mov rcx, r13
003882F3  48 8B F8                        mov rdi, rax
003882F6  E8 99 04 00 00                  call 0x140388794
003882FB  48 8B C8                        mov rcx, rax
003882FE  48 8B F0                        mov rsi, rax
00388301  E8 0A EF FC FF                  call 0x140357210
00388306  8A 15 7C D8 AD 00               mov dl, byte ptr [rip + 0xadd87c]
0038830C  48 8D 8E 50 04 00 00            lea rcx, [rsi + 0x450]
00388313  84 D2                           test dl, dl
00388315  0F 84 AC 03 00 00               je 0x1403886c7
0038831B  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
00388320  4C 8D A6 C4 02 00 00            lea r12, [rsi + 0x2c4]
00388327  84 D2                           test dl, dl
00388329  75 07                           jne 0x140388332
0038832B  4C 8D A7 0C 03 00 00            lea r12, [rdi + 0x30c]
00388332  4C 89 64 24 50                  mov qword ptr [rsp + 0x50], r12
00388337  4C 8D A6 94 04 00 00            lea r12, [rsi + 0x494]
0038833E  84 D2                           test dl, dl
00388340  0F 84 E0 01 00 00               je 0x140388526
00388346  49 8B CD                        mov rcx, r13
00388349  4C 89 64 24 58                  mov qword ptr [rsp + 0x58], r12
0038834E  88 5C 24 42                     mov byte ptr [rsp + 0x42], bl
00388352  E8 B9 09 00 00                  call 0x140388d10
00388357  44 38 35 43 6F C0 00            cmp byte ptr [rip + 0xc06f43], r14b
0038835E  44 8A F8                        mov r15b, al
00388361  75 36                           jne 0x140388399
00388363  49 8B 4D 28                     mov rcx, qword ptr [r13 + 0x28]
00388367  48 85 C9                        test rcx, rcx
0038836A  74 2D                           je 0x140388399
0038836C  48 8B 51 08                     mov rdx, qword ptr [rcx + 8]
00388370  48 85 D2                        test rdx, rdx
00388373  74 24                           je 0x140388399
00388375  4C 8B B2 00 02 00 00            mov r14, qword ptr [rdx + 0x200]
0038837C  48 8B CB                        mov rcx, rbx
0038837F  4C 89 75 80                     mov qword ptr [rbp - 0x80], r14
00388383  F0 49 0F C1 4E 08               lock xadd qword ptr [r14 + 8], rcx
00388389  48 03 CB                        add rcx, rbx
0038838C  48 3B CB                        cmp rcx, rbx
0038838F  0F 8E F6 02 00 00               jle 0x14038868b
00388395  88 5C 24 41                     mov byte ptr [rsp + 0x41], bl
00388399  E8 D2 1C 00 00                  call 0x14038a070
0038839E  45 84 FF                        test r15b, r15b
003883A1  0F 85 88 00 00 00               jne 0x14038842f
003883A7  44 38 3D DA D7 AD 00            cmp byte ptr [rip + 0xadd7da], r15b
003883AE  0F 85 8C 01 00 00               jne 0x140388540
003883B4  44 8A 55 68                     mov r10b, byte ptr [rbp + 0x68]
003883B8  44 8B 4D 58                     mov r9d, dword ptr [rbp + 0x58]
003883BC  44 8B 44 24 44                  mov r8d, dword ptr [rsp + 0x44]
003883C1  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
003883C6  80 3D BB D7 AD 00 00            cmp byte ptr [rip + 0xadd7bb], 0
003883CD  0F 85 5F 01 00 00               jne 0x140388532
003883D3  44 03 C3                        add r8d, ebx
003883D6  45 32 E4                        xor r12b, r12b
003883D9  45 32 FF                        xor r15b, r15b
003883DC  44 89 44 24 44                  mov dword ptr [rsp + 0x44], r8d
003883E1  44 88 64 24 40                  mov byte ptr [rsp + 0x40], r12b
003883E6  45 84 D2                        test r10b, r10b
003883E9  75 09                           jne 0x1403883f4
003883EB  48 39 00                        cmp qword ptr [rax], rax
003883EE  0F 85 8B 00 00 00               jne 0x14038847f
003883F4  48 8D 44 24 40                  lea rax, [rsp + 0x40]
003883F9  4D 8B C5                        mov r8, r13
003883FC  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00388401  48 8B D6                        mov rdx, rsi
00388404  83 64 24 28 00                  and dword ptr [rsp + 0x28], 0
00388409  48 8B CF                        mov rcx, rdi
0038840C  83 64 24 20 00                  and dword ptr [rsp + 0x20], 0
00388411  E8 26 15 00 00                  call 0x14038993c
00388416  44 8A 64 24 40                  mov r12b, byte ptr [rsp + 0x40]
0038841B  44 8A F8                        mov r15b, al
0038841E  84 C0                           test al, al
00388420  0F 84 F8 02 00 00               je 0x14038871e
00388426  45 84 E4                        test r12b, r12b
00388429  0F 85 EF 02 00 00               jne 0x14038871e
0038842F  80 7C 24 41 00                  cmp byte ptr [rsp + 0x41], 0
00388434  74 19                           je 0x14038844f
00388436  49 8B 96 88 01 00 00            mov rdx, qword ptr [r14 + 0x188]
0038843D  49 8B CE                        mov rcx, r14
00388440  48 FF C2                        inc rdx
00388443  49 89 96 88 01 00 00            mov qword ptr [r14 + 0x188], rdx
0038844A  E8 39 34 00 00                  call 0x14038b888
0038844F  80 7C 24 42 00                  cmp byte ptr [rsp + 0x42], 0
00388454  74 0B                           je 0x140388461
00388456  48 8B D6                        mov rdx, rsi
00388459  48 8B CF                        mov rcx, rdi
0038845C  E8 EB 34 00 00                  call 0x14038b94c
00388461  8A C3                           mov al, bl
00388463  48 8B 9C 24 50 01 00 00         mov rbx, qword ptr [rsp + 0x150]
0038846B  48 81 C4 10 01 00 00            add rsp, 0x110
00388472  41 5F                           pop r15
00388474  41 5E                           pop r14
00388476  41 5D                           pop r13
00388478  41 5C                           pop r12
0038847A  5F                              pop rdi
0038847B  5E                              pop rsi
0038847C  5D                              pop rbp
0038847D  C3                              ret
0038847E  CC                              int3
0038847F  8B 05 CF D6 AD 00               mov eax, dword ptr [rip + 0xadd6cf]
00388485  85 C0                           test eax, eax
00388487  0F 85 7A 02 00 00               jne 0x140388707
0038848D  F7 05 79 E6 C3 00 00 00 02 00   test dword ptr [rip + 0xc3e679], 0x20000
00388497  0F 85 99 02 00 00               jne 0x140388736
0038849D  8A D3                           mov dl, bl
0038849F  48 8B CF                        mov rcx, rdi
003884A2  E8 ED E8 FF FF                  call 0x140386d94
003884A7  80 7D 60 00                     cmp byte ptr [rbp + 0x60], 0
003884AB  0F 85 9D 00 00 00               jne 0x14038854e
003884B1  39 5C 24 44                     cmp dword ptr [rsp + 0x44], ebx
003884B5  0F 85 AC 02 00 00               jne 0x140388767
003884BB  45 84 FF                        test r15b, r15b
003884BE  0F 84 9C 02 00 00               je 0x140388760
003884C4  45 84 E4                        test r12b, r12b
003884C7  0F 84 62 FF FF FF               je 0x14038842f
003884CD  44 8B 0D 98 D6 AD 00            mov r9d, dword ptr [rip + 0xadd698]
003884D4  4C 8D 05 E5 F7 33 00            lea r8, [rip + 0x33f7e5]
003884DB  83 4C 24 7C FF                  or dword ptr [rsp + 0x7c], 0xffffffff
003884E0  BA 02 00 00 00                  mov edx, 2
003884E5  41 69 C1 F0 D8 FF FF            imul eax, r9d, 0xffffd8f0
003884EC  8D 4A 7D                        lea ecx, [rdx + 0x7d]
003884EF  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
003884F3  E8 98 0D FD FF                  call 0x140359290
003884F8  4D 85 F6                        test r14, r14
003884FB  0F 85 53 02 00 00               jne 0x140388754
00388501  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
00388506  33 D2                           xor edx, edx
00388508  33 C9                           xor ecx, ecx
0038850A  E8 41 10 E8 FF                  call 0x140209550
0038850F  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00388514  44 8B 44 24 44                  mov r8d, dword ptr [rsp + 0x44]
00388519  44 8B 4D 58                     mov r9d, dword ptr [rbp + 0x58]
0038851D  44 8A 55 68                     mov r10b, byte ptr [rbp + 0x68]
00388521  E9 AD FE FF FF                  jmp 0x1403883d3
00388526  4C 8D A7 0C 05 00 00            lea r12, [rdi + 0x50c]
0038852D  E9 14 FE FF FF                  jmp 0x140388346
00388532  4D 85 ED                        test r13, r13
00388535  0F 85 98 FE FF FF               jne 0x1403883d3
0038853B  E9 EF FE FF FF                  jmp 0x14038842f
00388540  48 85 F6                        test rsi, rsi
00388543  0F 85 6B FE FF FF               jne 0x1403883b4
00388549  E9 E1 FE FF FF                  jmp 0x14038842f
0038854E  33 D2                           xor edx, edx
00388550  48 C7 44 24 60 00 00 06 00      mov qword ptr [rsp + 0x60], 0x60000
00388559  48 8D 4D A0                     lea rcx, [rbp - 0x60]
0038855D  44 8D 42 68                     lea r8d, [rdx + 0x68]
00388561  E8 DA E6 33 00                  call 0x1406c6c40
00388566  48 8D 44 24 68                  lea rax, [rsp + 0x68]
0038856B  48 89 7D E8                     mov qword ptr [rbp - 0x18], rdi
0038856F  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00388574  33 C9                           xor ecx, ecx
00388576  48 89 75 F0                     mov qword ptr [rbp - 0x10], rsi
0038857A  48 8D 44 24 68                  lea rax, [rsp + 0x68]
0038857F  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00388584  8B 45 58                        mov eax, dword ptr [rbp + 0x58]
00388587  89 45 B0                        mov dword ptr [rbp - 0x50], eax
0038858A  48 8D 44 24 60                  lea rax, [rsp + 0x60]
0038858F  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
00388593  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
0038859D  C7 45 A0 FC 02 68 00            mov dword ptr [rbp - 0x60], 0x6802fc
003885A4  4C 89 6D A8                     mov qword ptr [rbp - 0x58], r13
003885A8  48 8B 00                        mov rax, qword ptr [rax]
003885AB  48 89 45 00                     mov qword ptr [rbp], rax
003885AF  45 84 FF                        test r15b, r15b
003885B2  0F 85 C4 01 00 00               jne 0x14038877c
003885B8  88 4D F8                        mov byte ptr [rbp - 8], cl
003885BB  38 4D 68                        cmp byte ptr [rbp + 0x68], cl
003885BE  4C 8D 87 C0 04 00 00            lea r8, [rdi + 0x4c0]
003885C5  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
003885CA  48 8D 55 B8                     lea rdx, [rbp - 0x48]
003885CE  0F 84 AD 00 00 00               je 0x140388681
003885D4  E8 A7 E0 FF FF                  call 0x140386680
003885D9  4C 8D BF 00 03 00 00            lea r15, [rdi + 0x300]
003885E0  49 8B CF                        mov rcx, r15
003885E3  48 8D 55 88                     lea rdx, [rbp - 0x78]
003885E7  E8 B4 D1 EE FF                  call 0x1402757a0
003885EC  45 33 E4                        xor r12d, r12d
003885EF  44 38 25 92 D5 AD 00            cmp byte ptr [rip + 0xadd592], r12b
003885F6  0F 84 9B 00 00 00               je 0x140388697
003885FC  8A 86 94 04 00 00               mov al, byte ptr [rsi + 0x494]
00388602  48 8B CE                        mov rcx, rsi
00388605  F6 D8                           neg al
00388607  1B D2                           sbb edx, edx
00388609  83 E2 0C                        and edx, 0xc
0038860C  83 C2 04                        add edx, 4
0038860F  E8 20 3B 04 00                  call 0x1403cc134
00388614  44 38 A6 94 04 00 00            cmp byte ptr [rsi + 0x494], r12b
0038861B  75 06                           jne 0x140388623
0038861D  88 9E D9 03 00 00               mov byte ptr [rsi + 0x3d9], bl
00388623  48 8D 4D 88                     lea rcx, [rbp - 0x78]
00388627  E8 B4 A6 FB FF                  call 0x140342ce0
0038862C  48 8B D6                        mov rdx, rsi
0038862F  48 8B CF                        mov rcx, rdi
00388632  E8 C5 0A FD FF                  call 0x1403590fc
00388637  4C 8D 2D 42 22 A8 00            lea r13, [rip + 0xa82242]
0038863E  45 33 C9                        xor r9d, r9d
00388641  45 33 C0                        xor r8d, r8d
00388644  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00388649  33 D2                           xor edx, edx
0038864B  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
00388650  E8 5B 60 E8 FF                  call 0x14020e6b0
00388655  85 C0                           test eax, eax
00388657  0F 84 D2 FD FF FF               je 0x14038842f
0038865D  4C 8B 74 24 50                  mov r14, qword ptr [rsp + 0x50]
00388662  4C 8B 64 24 58                  mov r12, qword ptr [rsp + 0x58]
00388667  41 80 3C 24 00                  cmp byte ptr [r12], 0
0038866C  0F 85 E4 C8 35 00               jne 0x1406e4f56
00388672  41 80 3E 00                     cmp byte ptr [r14], 0
00388676  0F 85 DA C8 35 00               jne 0x1406e4f56
0038867C  E9 05 C9 35 00                  jmp 0x1406e4f86
00388681  E8 7A E0 FF FF                  call 0x140386700
00388686  E9 4E FF FF FF                  jmp 0x1403885d9
0038868B  B9 0E 00 00 00                  mov ecx, 0xe
00388690  CD 29                           int 0x29
00388692  E9 FE FC FF FF                  jmp 0x140388395
00388697  8A 87 0C 05 00 00               mov al, byte ptr [rdi + 0x50c]
0038869D  48 8B CF                        mov rcx, rdi
003886A0  F6 D8                           neg al
003886A2  1B D2                           sbb edx, edx
003886A4  83 E2 0C                        and edx, 0xc
003886A7  83 C2 04                        add edx, 4
003886AA  E8 75 3B 04 00                  call 0x1403cc224
003886AF  44 38 A7 0C 05 00 00            cmp byte ptr [rdi + 0x50c], r12b
003886B6  0F 85 67 FF FF FF               jne 0x140388623
003886BC  88 9F 19 04 00 00               mov byte ptr [rdi + 0x419], bl
003886C2  E9 5C FF FF FF                  jmp 0x140388623
003886C7  48 8D 8F 90 04 00 00            lea rcx, [rdi + 0x490]
003886CE  E9 48 FC FF FF                  jmp 0x14038831b
003886D3  48 8B 05 C6 E7 C3 00            mov rax, qword ptr [rip + 0xc3e7c6]
003886DA  48 8B 78 08                     mov rdi, qword ptr [rax + 8]
003886DE  48 8D 8F 0C 03 00 00            lea rcx, [rdi + 0x30c]
003886E5  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
003886EA  48 8D 87 90 04 00 00            lea rax, [rdi + 0x490]
003886F1  48 8D 8F 0C 05 00 00            lea rcx, [rdi + 0x50c]
003886F8  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
003886FD  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
00388702  E9 BF FC FF FF                  jmp 0x1403883c6
00388707  45 85 C9                        test r9d, r9d
0038870A  0F 84 7D FD FF FF               je 0x14038848d
00388710  44 3B C8                        cmp r9d, eax
00388713  0F 82 74 FD FF FF               jb 0x14038848d
00388719  E9 D6 FC FF FF                  jmp 0x1403883f4
0038871E  83 7C 24 44 02                  cmp dword ptr [rsp + 0x44], 2
00388723  0F 85 64 FD FF FF               jne 0x14038848d
00388729  84 C0                           test al, al
0038872B  0F 85 FE FC FF FF               jne 0x14038842f
00388731  E9 57 FD FF FF                  jmp 0x14038848d
00388736  4C 8B 8F 38 04 00 00            mov r9, qword ptr [rdi + 0x438]
0038873D  49 8B CD                        mov rcx, r13
00388740  4C 8B 87 20 04 00 00            mov r8, qword ptr [rdi + 0x420]
00388747  8B 55 58                        mov edx, dword ptr [rbp + 0x58]
0038874A  E8 CD 6A 1F 00                  call 0x14057f21c
0038874F  E9 49 FD FF FF                  jmp 0x14038849d
00388754  49 01 9E 98 01 00 00            add qword ptr [r14 + 0x198], rbx
0038875B  E9 A1 FD FF FF                  jmp 0x140388501
00388760  32 DB                           xor bl, bl
00388762  E9 C8 FC FF FF                  jmp 0x14038842f
00388767  4D 85 F6                        test r14, r14
0038876A  0F 84 DE C7 35 00               je 0x1406e4f4e
00388770  49 01 9E 90 01 00 00            add qword ptr [r14 + 0x190], rbx
00388777  E9 D2 C7 35 00                  jmp 0x1406e4f4e
0038877C  88 5D F8                        mov byte ptr [rbp - 8], bl
0038877F  38 4C 24 40                     cmp byte ptr [rsp + 0x40], cl
00388783  0F 85 32 FE FF FF               jne 0x1403885bb
00388789  E9 2A FE FF FF                  jmp 0x1403885b8
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CcCanIWrite(__int64 a1, int a2, int a3, unsigned __int8 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned int v_stack_m104;
    unsigned __int8 v_stack_m106;
    unsigned __int8 v_stack_m107;
    unsigned __int8 v_stack_m108;
    unsigned __int64 v_stack_m118;
    unsigned int v_stack_m120;
    unsigned int v_stack_m128;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p40;
    unsigned int v_stack_p44;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned int v_stack_p78;
    unsigned int v_stack_p7C;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int8 *)(v_rsp + 32) = a4;
    *(unsigned __int8 *)(v_rsp + 24) = (unsigned __int8)(a3);
    *(unsigned int *)(v_rsp + 16) = a2;
    v_rsp = (v_rsp) - (272);
    result = 0;
    v_rsi = 0;
    *(unsigned __int64 *)(v_rsp - 72 - 104) = 0;
    a3 = 0;
    v_r14 = 0;
    v_stack_m106 = 0;
    v_stack_m107 = 0;
    *(unsigned __int64 *)(v_rsp - 72 - 120) = v_xmm0;
    v_stack_m104 = 0;
    *(unsigned __int64 *)(v_rsp - 72 - 128) = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1444)))) & (2)) != 0) goto loc_00388461;
    if (a1 == 0) goto loc_003886D3;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 80)))) & (16)) != 0) goto loc_00388461;
    if (condition_is_below) goto loc_00388461;
    result = KeRcuReadLock(a1, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1444)), a3, (unsigned int)(a2));
    result = CcReferencePartitionFromFileObject(a1, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1444)), a3, (unsigned int)(a2));
    result = CcGetPrivateVolumeCacheMapFromFileObject(a1, result, a3, (unsigned int)(a2));
    result = CcReferencePrivateVolumeCacheMap(result, result, a3, (unsigned int)(a2));
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 11393148)) == 0) goto loc_003886C7;
loc_0038831B:
    v_stack_m100 = result + 1104;
    v_r12 = result + 708;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 11393148)) == 0) {
        v_r12 = result + 780;
    }
    v_stack_mF8 = v_r12;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 11393148)) == 0) goto loc_00388526;
loc_00388346:
    v_stack_mF0 = result + 1172;
    v_stack_m106 = (unsigned __int8)(v_rsi + 1);
    result = CcIsFileObjectDirectMapped(a1, *(unsigned __int8 *)(v_rip + 11393148), a3, (unsigned int)(a2));
    if ((*(unsigned __int8 *)(v_rip + 12611395)) != 0) goto loc_00388399;
    if (*(unsigned __int64 *)(a1 + 40) == 0) goto loc_00388399;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) == 0) goto loc_00388399;
    *(unsigned __int64 *)(v_rsp - 72 - 128) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 512);
    a1 = (v_rsi + 1) + (v_rsi + 1);
    if (a1 <= (v_rsi + 1)) goto loc_0038868B;
loc_00388395:
    v_stack_m107 = (unsigned __int8)(v_rsi + 1);
loc_00388399:
    result = KeRcuReadUnlock(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8), a3, (unsigned int)(a2));
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) goto loc_0038842F;
    if ((*(unsigned __int8 *)(v_rip + 11392986)) != ((unsigned __int8)((unsigned __int8)(result)))) goto loc_00388540;
loc_003883B4:
loc_003883C6:
    if ((*(unsigned __int8 *)(v_rip + 11392955)) != 0) goto loc_00388532;
loc_003883D3:
    a3 = (unsigned int)(((unsigned int)(v_stack_m104)) + ((unsigned int)(v_rsi + 1)));
    v_r12 = 0;
    v_r15 = 0;
    v_stack_m104 = a3;
    v_stack_m108 = 0;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 72 + 104)) != 0) goto loc_003883F4;
    if ((*(unsigned __int64 *)(v_stack_m100)) != v_stack_m100) goto loc_0038847F;
loc_003883F4:
    v_stack_m118 = v_stack_m108;
    result = CcCanIWriteStreamEx(result, result, a1, (unsigned int)(*(unsigned int *)(v_rsp - 72 + 88)));
    if ((unsigned __int8)(result) == 0) goto loc_0038871E;
    if ((unsigned __int8)(v_stack_m108) != 0) goto loc_0038871E;
loc_0038842F:
    if (v_stack_m107 != 0) {
        a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 512) + 392);
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 512);
        a2 = (a2) + 1;
        *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 512) + 392) = a2;
        result = CcDecrementVolumeUseCountWithDelete(a1, a2, a1, (unsigned int)(*(unsigned int *)(v_rsp - 72 + 88)));
    }
    if (v_stack_m106 != 0) {
        a2 = result;
        a1 = result;
        result = CcDereferencePartitionAndPrivateVolumeCacheMap(a1, a2, a1, (unsigned int)(*(unsigned int *)(v_rsp - 72 + 88)));
    }
    v_rsp = (v_rsp) + (272);
    return (unsigned __int8)(v_rsi + 1);
loc_0038847F:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11392719))) != 0) goto loc_00388707;
loc_0038848D:
    if (((*(unsigned int *)(v_rip + 12838521)) & (0x20000ULL)) != 0) goto loc_00388736;
loc_0038849D:
    result = CcAdjustWriteBehindThreadPoolIfNeeded(result, (unsigned __int8)(v_stack_p8), a1, (unsigned int)(*(unsigned int *)(v_rsp - 72 + 88)));
    if ((*(unsigned __int8 *)(v_rsp - 72 + 96)) != 0) goto loc_0038854E;
    if (v_stack_p44 != ((unsigned int)(v_stack_p8))) goto loc_00388767;
    if ((unsigned __int8)((unsigned __int8)(result)) == 0) goto loc_00388760;
    if ((unsigned __int8)(v_stack_m108) == 0) goto loc_0038842F;
    result = (unsigned int)((result) * ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11392664)))));
    v_stack_p78 = (unsigned int)(result);
    result = DbgPrintEx(2 + 125, 2, v_rip + 3405797, (unsigned int)(*(unsigned int *)(v_rip + 11392664)));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 512) != 0) goto loc_00388754;
loc_00388501:
    a2 = 0;
    a1 = 0;
    result = KeDelayExecutionThread(a1, a2, v_stack_p78, (unsigned int)(*(unsigned int *)(v_rip + 11392664)));
    goto loc_003883D3;
loc_00388526:
    goto loc_00388346;
loc_00388532:
    if (0 != 0) goto loc_003883D3;
    goto loc_0038842F;
loc_00388540:
    if (result != 0) goto loc_003883B4;
    goto loc_0038842F;
loc_0038854E:
    a2 = 0;
    v_stack_p60 = 0x60000ULL;
    result = memset(v_rsp - 72 - 96, a2, a2 + 104, (unsigned int)(*(unsigned int *)(v_rsp - 72 + 88)));
    *(unsigned __int64 *)(v_rsp - 72 - 24) = result;
    v_stack_p70 = v_stack_p68;
    a1 = 0;
    *(unsigned __int64 *)(v_rsp - 72 - 16) = result;
    v_stack_p68 = v_stack_p68;
    *(unsigned int *)(v_rsp - 72 - 80) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 72 + 88)));
    *(unsigned __int64 *)(v_rsp - 72 - 56) = v_stack_p60;
    *(unsigned int *)(v_rsp - 72 - 96) = 0x6802FCULL;
    *(unsigned __int64 *)(v_rsp - 72 - 88) = 0;
    *(unsigned __int64 *)(v_rsp - 72) = *(unsigned __int64 *)(v_stack_p60);
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) goto loc_0038877C;
loc_003885B8:
    *(unsigned __int8 *)(v_rsp - 72 - 8) = 0;
loc_003885BB:
    if ((*(unsigned __int8 *)(v_rsp - 72 + 104)) == 0) goto loc_00388681;
    result = ExInterlockedInsertHeadList(v_stack_p48, v_rsp - 72 - 72, result + 1216, (unsigned int)(*(unsigned int *)(v_rsp - 72 + 88)));
loc_003885D9:
    result = KeAcquireInStackQueuedSpinLock(result + 768, v_rsp - 72 - 120, result + 1216, (unsigned int)(*(unsigned int *)(v_rsp - 72 + 88)));
    v_r12 = 0;
    if ((*(unsigned __int8 *)(v_rip + 11392402)) == 0) goto loc_00388697;
    result = (unsigned __int8)(-(*(unsigned __int8 *)(result + 1172)));
    a2 = (unsigned int)((v_rsp - 72 - 120) & (12));
    a2 = (unsigned int)((a2) + (4));
    result = CcNotifyWriteBehindVolume(result, a2, result + 1216, (unsigned int)(*(unsigned int *)(v_rsp - 72 + 88)));
    if ((*(unsigned __int8 *)(result + 1172)) == 0) {
        *(unsigned __int8 *)(result + 985) = (unsigned __int8)(v_stack_p8);
    }
    result = KeReleaseInStackQueuedSpinLock(v_rsp - 72 - 120, a2, result + 1216, (unsigned int)(*(unsigned int *)(v_rsp - 72 + 88)));
    result = CcPostDeferredWrites(result, result, result + 1216, (unsigned int)(*(unsigned int *)(v_rsp - 72 + 88)));
    a4 = 0;
    a3 = 0;
    v_stack_p20 = v_rip + 11018818;
    a2 = 0;
    result = KeWaitForSingleObject(v_stack_p60, a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_0038842F;
loc_00388681:
    result = ExInterlockedInsertTailList(v_stack_p60, a2, a3, a4);
    goto loc_003885D9;
loc_0038868B:
    goto loc_00388395;
loc_00388697:
    result = (unsigned __int8)(-(*(unsigned __int8 *)(result + 1292)));
    a2 = (unsigned int)((a2) & (12));
    a2 = (unsigned int)((a2) + (4));
    result = CcNotifyWriteBehindInternal(result, a2, a3, a4);
    if ((*(unsigned __int8 *)(result + 1292)) != ((unsigned __int8)(v_stack_p58))) goto loc_00388623;
    *(unsigned __int8 *)(result + 1049) = (unsigned __int8)(v_stack_p8);
    goto loc_00388623;
loc_003886C7:
    goto loc_0038831B;
loc_003886D3:
    v_stack_p50 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12838854) + 8) + 780;
    v_stack_p48 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12838854) + 8) + 1168;
    v_stack_p58 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12838854) + 8) + 1292;
    goto loc_003883C6;
loc_00388707:
    if (0 == 0) goto loc_0038848D;
    if (0 < ((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12838854) + 8) + 1168))) goto loc_0038848D;
    goto loc_003883F4;
loc_0038871E:
    if (v_stack_p44 != 2) goto loc_0038848D;
    if ((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12838854) + 8) + 1168) != 0) goto loc_0038842F;
    goto loc_0038848D;
loc_00388736:
    result = CcPerfLogCanWriteFail(v_rip + 11018818, (unsigned int)(*(unsigned int *)(v_rsp - 72 + 88)), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12838854) + 8) + 1056), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12838854) + 8) + 1080));
    goto loc_0038849D;
loc_00388754:
    goto loc_00388501;
loc_00388760:
    v_rbx = 0;
    goto loc_0038842F;
loc_00388767:
loc_0038877C:
    *(unsigned __int8 *)(v_rsp - 72 - 8) = 0;
    if (v_stack_p40 != ((unsigned __int8)(v_rip + 11018818))) goto loc_003885BB;
    goto loc_003885B8;
}
```

## 5. (Beta) C Style

```c
int64_t CcCanIWrite(void *Arg1, int32_t Arg2, int32_t Arg3, uint8_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint32_t v_stack_m104;
    uint8_t v_stack_m106;
    uint8_t v_stack_m107;
    uint8_t v_stack_m108;
    uint64_t v_stack_m118;
    uint32_t v_stack_m120;
    uint32_t v_stack_m128;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p20;
    uint8_t v_stack_p40;
    uint32_t v_stack_p44;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint32_t v_stack_p78;
    uint32_t v_stack_p7C;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint8_t *)(local_rsp + 0x20) = Arg4;
    *(uint8_t *)(local_rsp + 0x18) = (uint8_t)(Arg3);
    *(uint32_t *)(local_rsp + 0x10) = Arg2;
    local_rsp = (local_rsp) - (272);
    result = 0;
    local_rsi = 0;
    *(uint64_t *)(local_rsp - 0x48 - 0x68) = 0;
    Arg3 = 0;
    local_r14 = 0;
    v_stack_m106 = 0;
    v_stack_m107 = 0;
    *(uint64_t *)(local_rsp - 0x48 - 0x78) = v_xmm0;
    v_stack_m104 = 0;
    *(uint64_t *)(local_rsp - 0x48 - 0x80) = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A4)))) & (2)) != 0) goto loc_00388461;
    if (Arg1 == NULL) goto loc_003886D3;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x50)))) & (16)) != 0) goto loc_00388461;
    if (condition_is_below) goto loc_00388461;
    result = KeRcuReadLock(Arg1, (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A4)), Arg3, (uint32_t)(Arg2));
    result = CcReferencePartitionFromFileObject(Arg1, (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A4)), Arg3, (uint32_t)(Arg2));
    result = CcGetPrivateVolumeCacheMapFromFileObject(Arg1, result, Arg3, (uint32_t)(Arg2));
    result = CcReferencePrivateVolumeCacheMap(result, result, Arg3, (uint32_t)(Arg2));
    if ((uint8_t)(*(uint8_t *)(v_rip + 0xADD87C)) == 0) goto loc_003886C7;
loc_0038831B:
    v_stack_m100 = result + 1104;
    local_r12 = result + 708;
    if ((uint8_t)(*(uint8_t *)(v_rip + 0xADD87C)) == 0) {
        local_r12 = result + 780;
    }
    v_stack_mF8 = local_r12;
    if ((uint8_t)(*(uint8_t *)(v_rip + 0xADD87C)) == 0) goto loc_00388526;
loc_00388346:
    v_stack_mF0 = result + 1172;
    v_stack_m106 = (uint8_t)(local_rsi + 1);
    result = CcIsFileObjectDirectMapped(Arg1, *(uint8_t *)(v_rip + 0xADD87C), Arg3, (uint32_t)(Arg2));
    if ((*(uint8_t *)(v_rip + 0xC06F43)) != 0) goto loc_00388399;
    if (*(uint64_t *)(arg1 + 0x28) == 0) goto loc_00388399;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) == 0) goto loc_00388399;
    *(uint64_t *)(local_rsp - 0x48 - 0x80) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 0x200);
    Arg1 = (local_rsi + 1) + (local_rsi + 1);
    if (Arg1 <= (local_rsi + 1)) goto loc_0038868B;
loc_00388395:
    v_stack_m107 = (uint8_t)(local_rsi + 1);
loc_00388399:
    result = KeRcuReadUnlock(Arg1, *(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8), Arg3, (uint32_t)(Arg2));
    if ((uint8_t)((uint8_t)(result)) != 0) goto loc_0038842F;
    if ((*(uint8_t *)(v_rip + 0xADD7DA)) != ((uint8_t)((uint8_t)(result)))) goto loc_00388540;
loc_003883B4:
loc_003883C6:
    if ((*(uint8_t *)(v_rip + 0xADD7BB)) != 0) goto loc_00388532;
loc_003883D3:
    Arg3 = (uint32_t)(((uint32_t)(v_stack_m104)) + ((uint32_t)(local_rsi + 1)));
    local_r12 = 0;
    local_r15 = 0;
    v_stack_m104 = Arg3;
    v_stack_m108 = 0;
    if ((uint8_t)(*(uint8_t *)(local_rsp - 0x48 + 0x68)) != 0) goto loc_003883F4;
    if ((*(uint64_t *)(v_stack_m100)) != v_stack_m100) goto loc_0038847F;
loc_003883F4:
    v_stack_m118 = v_stack_m108;
    result = CcCanIWriteStreamEx(result, result, Arg1, (uint32_t)(*(uint32_t *)(local_rsp - 0x48 + 0x58)));
    if ((uint8_t)(result) == 0) goto loc_0038871E;
    if ((uint8_t)(v_stack_m108) != 0) goto loc_0038871E;
loc_0038842F:
    if (v_stack_m107 != 0) {
        Arg2 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 0x200) + 0x188);
        Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 0x200);
        Arg2 = (Arg2) + 1;
        *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 0x200) + 0x188) = Arg2;
        result = CcDecrementVolumeUseCountWithDelete(Arg1, Arg2, Arg1, (uint32_t)(*(uint32_t *)(local_rsp - 0x48 + 0x58)));
    }
    if (v_stack_m106 != 0) {
        Arg2 = result;
        Arg1 = result;
        result = CcDereferencePartitionAndPrivateVolumeCacheMap(Arg1, Arg2, Arg1, (uint32_t)(*(uint32_t *)(local_rsp - 0x48 + 0x58)));
    }
    local_rsp = (local_rsp) + (272);
    return (uint8_t)(local_rsi + 1);
loc_0038847F:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xADD6CF))) != 0) goto loc_00388707;
loc_0038848D:
    if (((*(uint32_t *)(v_rip + 0xC3E679)) & (0x20000ULL)) != 0) goto loc_00388736;
loc_0038849D:
    result = CcAdjustWriteBehindThreadPoolIfNeeded(result, (uint8_t)(v_stack_p8), Arg1, (uint32_t)(*(uint32_t *)(local_rsp - 0x48 + 0x58)));
    if ((*(uint8_t *)(local_rsp - 0x48 + 0x60)) != 0) goto loc_0038854E;
    if (v_stack_p44 != ((uint32_t)(v_stack_p8))) goto loc_00388767;
    if ((uint8_t)((uint8_t)(result)) == 0) goto loc_00388760;
    if ((uint8_t)(v_stack_m108) == 0) goto loc_0038842F;
    result = (uint32_t)((result) * ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xADD698)))));
    v_stack_p78 = (uint32_t)(result);
    result = DbgPrintEx(2 + 125, 2, v_rip + 3405797, (uint32_t)(*(uint32_t *)(v_rip + 0xADD698)));
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 0x200) != 0) goto loc_00388754;
loc_00388501:
    Arg2 = 0;
    Arg1 = 0;
    result = KeDelayExecutionThread(Arg1, Arg2, v_stack_p78, (uint32_t)(*(uint32_t *)(v_rip + 0xADD698)));
    goto loc_003883D3;
loc_00388526:
    goto loc_00388346;
loc_00388532:
    if (0 != 0) goto loc_003883D3;
    goto loc_0038842F;
loc_00388540:
    if (result != 0) goto loc_003883B4;
    goto loc_0038842F;
loc_0038854E:
    Arg2 = 0;
    v_stack_p60 = 0x60000ULL;
    result = memset(local_rsp - 72 - 96, Arg2, Arg2 + 104, (uint32_t)(*(uint32_t *)(local_rsp - 0x48 + 0x58)));
    *(uint64_t *)(local_rsp - 0x48 - 0x18) = result;
    v_stack_p70 = v_stack_p68;
    Arg1 = 0;
    *(uint64_t *)(local_rsp - 0x48 - 0x10) = result;
    v_stack_p68 = v_stack_p68;
    *(uint32_t *)(local_rsp - 0x48 - 0x50) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x48 + 0x58)));
    *(uint64_t *)(local_rsp - 0x48 - 0x38) = v_stack_p60;
    *(uint32_t *)(local_rsp - 0x48 - 0x60) = 0x6802FCULL;
    *(uint64_t *)(local_rsp - 0x48 - 0x58) = 0;
    *(uint64_t *)(local_rsp - 0x48) = *(uint64_t *)(v_stack_p60);
    if ((uint8_t)((uint8_t)(result)) != 0) goto loc_0038877C;
loc_003885B8:
    *(uint8_t *)(local_rsp - 0x48 - 0x8) = 0;
loc_003885BB:
    if ((*(uint8_t *)(local_rsp - 0x48 + 0x68)) == 0) goto loc_00388681;
    result = ExInterlockedInsertHeadList(v_stack_p48, local_rsp - 72 - 72, result + 1216, (uint32_t)(*(uint32_t *)(local_rsp - 0x48 + 0x58)));
loc_003885D9:
    result = KeAcquireInStackQueuedSpinLock(result + 768, local_rsp - 72 - 120, result + 1216, (uint32_t)(*(uint32_t *)(local_rsp - 0x48 + 0x58)));
    local_r12 = 0;
    if ((*(uint8_t *)(v_rip + 0xADD592)) == 0) goto loc_00388697;
    result = (uint8_t)(-(*(uint8_t *)(result + 0x494)));
    Arg2 = (uint32_t)((local_rsp - 72 - 120) & (12));
    Arg2 = (uint32_t)((Arg2) + (4));
    result = CcNotifyWriteBehindVolume(result, Arg2, result + 1216, (uint32_t)(*(uint32_t *)(local_rsp - 0x48 + 0x58)));
    if ((*(uint8_t *)(result + 0x494)) == 0) {
        *(uint8_t *)(result + 0x3D9) = (uint8_t)(v_stack_p8);
    }
    result = KeReleaseInStackQueuedSpinLock(local_rsp - 72 - 120, Arg2, result + 1216, (uint32_t)(*(uint32_t *)(local_rsp - 0x48 + 0x58)));
    result = CcPostDeferredWrites(result, result, result + 1216, (uint32_t)(*(uint32_t *)(local_rsp - 0x48 + 0x58)));
    Arg4 = 0;
    Arg3 = 0;
    v_stack_p20 = v_rip + 11018818;
    Arg2 = 0;
    result = KeWaitForSingleObject(v_stack_p60, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_0038842F;
loc_00388681:
    result = ExInterlockedInsertTailList(v_stack_p60, Arg2, Arg3, Arg4);
    goto loc_003885D9;
loc_0038868B:
    goto loc_00388395;
loc_00388697:
    result = (uint8_t)(-(*(uint8_t *)(result + 0x50C)));
    Arg2 = (uint32_t)((Arg2) & (12));
    Arg2 = (uint32_t)((Arg2) + (4));
    result = CcNotifyWriteBehindInternal(result, Arg2, Arg3, Arg4);
    if ((*(uint8_t *)(result + 0x50C)) != ((uint8_t)(v_stack_p58))) goto loc_00388623;
    *(uint8_t *)(result + 0x419) = (uint8_t)(v_stack_p8);
    goto loc_00388623;
loc_003886C7:
    goto loc_0038831B;
loc_003886D3:
    v_stack_p50 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xC3E7C6) + 0x8) + 780;
    v_stack_p48 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xC3E7C6) + 0x8) + 1168;
    v_stack_p58 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xC3E7C6) + 0x8) + 1292;
    goto loc_003883C6;
loc_00388707:
    if (0 == 0) goto loc_0038848D;
    if (0 < ((uint32_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xC3E7C6) + 0x8) + 1168))) goto loc_0038848D;
    goto loc_003883F4;
loc_0038871E:
    if (v_stack_p44 != 2) goto loc_0038848D;
    if ((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xC3E7C6) + 0x8) + 1168) != 0) goto loc_0038842F;
    goto loc_0038848D;
loc_00388736:
    result = CcPerfLogCanWriteFail(v_rip + 11018818, (uint32_t)(*(uint32_t *)(local_rsp - 0x48 + 0x58)), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xC3E7C6) + 0x8) + 0x420), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xC3E7C6) + 0x8) + 0x438));
    goto loc_0038849D;
loc_00388754:
    goto loc_00388501;
loc_00388760:
    local_rbx = 0;
    goto loc_0038842F;
loc_00388767:
loc_0038877C:
    *(uint8_t *)(local_rsp - 0x48 - 0x8) = 0;
    if (v_stack_p40 != ((uint8_t)(v_rip + 11018818))) goto loc_003885BB;
    goto loc_003885B8;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x28` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00388250&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
