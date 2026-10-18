# KiAbDeferredProcessingWorker

- RVA: `0x0030DEB0`–`0x0030E82E` (길이 `2,430` bytes)
- VA: `0x000000014030DEB0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00073F08`
- 디코드: `600`개 명령, `2,430/2,430` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **32**; 고유 호출 대상: **18**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0030E104` → [KiDeferredReadySingleThread](../25/KiDeferredReadySingleThread_function_00252FE0.md) (function, `0x00252FE0`)
- `0x0030E12B` → [KiFlushSoftwareInterruptBatch](../25/KiFlushSoftwareInterruptBatch_function_00252200.md) (function, `0x00252200`)
- `0x0030E148` → [KiSendSoftwareInterruptAffinity](KiSendSoftwareInterruptAffinity_function_0030E834.md) (function, `0x0030E834`)
- `0x0030E1BE` → [HalpInterruptSendIpi](../25/HalpInterruptSendIpi_function_00252310.md) (function, `0x00252310`)
- `0x0030E214` → [KiAbEntryGetLockedHeadEntry](../22/KiAbEntryGetLockedHeadEntry_function_002213C0.md) (function, `0x002213C0`)
- `0x0030E241` → [KiAbOwnerComputeCpuPriorityKey](../21/KiAbOwnerComputeCpuPriorityKey_function_0021F090.md) (function, `0x0021F090`)
- `0x0030E25F` → [RtlRbRemoveNode](../2E/RtlRbRemoveNode_function_002E4C10.md) (function, `0x002E4C10`)
- `0x0030E30B` → [KiAbEntryGetLockedHeadEntry](../22/KiAbEntryGetLockedHeadEntry_function_002213C0.md) (function, `0x002213C0`)
- `0x0030E338` → [KiAbOwnerComputeCpuPriorityKey](../21/KiAbOwnerComputeCpuPriorityKey_function_0021F090.md) (function, `0x0021F090`)
- `0x0030E353` → [RtlRbRemoveNode](../2E/RtlRbRemoveNode_function_002E4C10.md) (function, `0x002E4C10`)
- `0x0030E3D2` → [RtlRbInsertNodeEx](../2E/RtlRbInsertNodeEx_function_002E4570.md) (function, `0x002E4570`)
- `0x0030E426` → [KeReleaseInStackQueuedSpinLockFromDpcLevel](../21/KeReleaseInStackQueuedSpinLockFromDpcLevel_function_002171B0.md) (function, `0x002171B0`)
- `0x0030E43C` → [KeReleaseInStackQueuedSpinLockFromDpcLevel](../21/KeReleaseInStackQueuedSpinLockFromDpcLevel_function_002171B0.md) (function, `0x002171B0`)
- `0x0030E476` → [EtwTraceAutoBoostProcessLockEntry](../22/EtwTraceAutoBoostProcessLockEntry_function_00221C7C.md) (function, `0x00221C7C`)
- `0x0030E4B4` → [RtlRbInsertNodeEx](../2E/RtlRbInsertNodeEx_function_002E4570.md) (function, `0x002E4570`)
- `0x0030E508` → [KeReleaseInStackQueuedSpinLockFromDpcLevel](../21/KeReleaseInStackQueuedSpinLockFromDpcLevel_function_002171B0.md) (function, `0x002171B0`)
- `0x0030E51E` → [KeReleaseInStackQueuedSpinLockFromDpcLevel](../21/KeReleaseInStackQueuedSpinLockFromDpcLevel_function_002171B0.md) (function, `0x002171B0`)
- `0x0030E55D` → [EtwTraceAutoBoostProcessLockEntry](../22/EtwTraceAutoBoostProcessLockEntry_function_00221C7C.md) (function, `0x00221C7C`)
- `0x0030E5A4` → [KiAbProcessThreadLocks](../22/KiAbProcessThreadLocks_function_00221D30.md) (function, `0x00221D30`)
- `0x0030E5F9` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0030E620` → [KiAbSetMinimumThreadPriority](../21/KiAbSetMinimumThreadPriority_function_0021F190.md) (function, `0x0021F190`)
- `0x0030E63C` → [KiAbEntryUpdateOwnerTreePosition](../2E/KiAbEntryUpdateOwnerTreePosition_function_002E5970.md) (function, `0x002E5970`)
- `0x0030E665` → [KiAbSetMinimumThreadPriority](../21/KiAbSetMinimumThreadPriority_function_0021F190.md) (function, `0x0021F190`)
- `0x0030E681` → [KiAbEntryUpdateOwnerTreePosition](../2E/KiAbEntryUpdateOwnerTreePosition_function_002E5970.md) (function, `0x002E5970`)
- `0x0030E734` → [ObReferenceObjectSafeWithTag](../21/ObReferenceObjectSafeWithTag_function_00210EE0.md) (function, `0x00210EE0`)
- `0x0030E751` → [IoBoostThreadIoPriority](../21/IoBoostThreadIoPriority_function_00216110.md) (function, `0x00216110`)
- `0x0030E75F` → [PsBoostThreadOutstandingIoQoS](../21/PsBoostThreadOutstandingIoQoS_function_00215C54.md) (function, `0x00215C54`)
- `0x0030E76C` → [ObDereferenceObjectDeferDeleteWithTag](../26/ObDereferenceObjectDeferDeleteWithTag_function_00263EA0.md) (function, `0x00263EA0`)
- `0x0030E798` → [ObReferenceObjectSafeWithTag](../21/ObReferenceObjectSafeWithTag_function_00210EE0.md) (function, `0x00210EE0`)
- `0x0030E7B9` → [IoBoostThreadIoPriority](../21/IoBoostThreadIoPriority_function_00216110.md) (function, `0x00216110`)
- `0x0030E7C7` → [PsBoostThreadOutstandingIoQoS](../21/PsBoostThreadOutstandingIoQoS_function_00215C54.md) (function, `0x00215C54`)
- `0x0030E7D4` → [ObDereferenceObjectDeferDeleteWithTag](../26/ObDereferenceObjectDeferDeleteWithTag_function_00263EA0.md) (function, `0x00263EA0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0030E451` → RVA `0x00FC6B14` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0030DEB0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0030DEB5  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0030DEBA  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
0030DEBF  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
0030DEC4  55                              push rbp
0030DEC5  41 54                           push r12
0030DEC7  41 55                           push r13
0030DEC9  41 56                           push r14
0030DECB  41 57                           push r15
0030DECD  48 8D 6C 24 C9                  lea rbp, [rsp - 0x37]
0030DED2  48 81 EC C0 00 00 00            sub rsp, 0xc0
0030DED9  45 33 E4                        xor r12d, r12d
0030DEDC  49 8D B0 78 91 00 00            lea rsi, [r8 + 0x9178]
0030DEE3  4D 8D 90 70 91 00 00            lea r10, [r8 + 0x9170]
0030DEEA  4C 89 65 AF                     mov qword ptr [rbp - 0x51], r12
0030DEEE  48 89 75 D7                     mov qword ptr [rbp - 0x29], rsi
0030DEF2  48 BB FC FF FF FF FF FF FF 7F   movabs rbx, 0x7ffffffffffffffc
0030DEFC  4C 89 55 DF                     mov qword ptr [rbp - 0x21], r10
0030DF00  49 BB 00 00 00 00 00 00 00 80   movabs r11, 0x8000000000000000
0030DF0A  45 8D 7C 24 01                  lea r15d, [r12 + 1]
0030DF0F  49 8B 3A                        mov rdi, qword ptr [r10]
0030DF12  48 89 7D CF                     mov qword ptr [rbp - 0x31], rdi
0030DF16  48 85 FF                        test rdi, rdi
0030DF19  0F 84 88 01 00 00               je 0x14030e0a7
0030DF1F  48 8B 07                        mov rax, qword ptr [rdi]
0030DF22  49 89 02                        mov qword ptr [r10], rax
0030DF25  4C 89 3F                        mov qword ptr [rdi], r15
0030DF28  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
0030DF2D  0F B6 47 E9                     movzx eax, byte ptr [rdi - 0x17]
0030DF31  84 C0                           test al, al
0030DF33  0F 84 3B 01 00 00               je 0x14030e074
0030DF39  48 8B 87 48 01 00 00            mov rax, qword ptr [rdi + 0x148]
0030DF40  48 85 C0                        test rax, rax
0030DF43  0F 84 62 04 00 00               je 0x14030e3ab
0030DF49  0F B6 48 0C                     movzx ecx, byte ptr [rax + 0xc]
0030DF4D  4D 8B C7                        mov r8, r15
0030DF50  49 D3 E0                        shl r8, cl
0030DF53  45 8B CC                        mov r9d, r12d
0030DF56  0F B7 48 08                     movzx ecx, word ptr [rax + 8]
0030DF5A  41 FF C8                        dec r8d
0030DF5D  0F B7 50 0A                     movzx edx, word ptr [rax + 0xa]
0030DF61  0B D1                           or edx, ecx
0030DF63  44 3B C2                        cmp r8d, edx
0030DF66  41 0F 94 C1                     sete r9b
0030DF6A  48 8B 87 40 01 00 00            mov rax, qword ptr [rdi + 0x140]
0030DF71  4D 8B C7                        mov r8, r15
0030DF74  0F B6 48 0C                     movzx ecx, byte ptr [rax + 0xc]
0030DF78  0F B7 50 08                     movzx edx, word ptr [rax + 8]
0030DF7C  49 D3 E0                        shl r8, cl
0030DF7F  0F B7 48 0A                     movzx ecx, word ptr [rax + 0xa]
0030DF83  41 FF C8                        dec r8d
0030DF86  0B CA                           or ecx, edx
0030DF88  44 3B C1                        cmp r8d, ecx
0030DF8B  0F 84 DA 00 00 00               je 0x14030e06b
0030DF91  48 8B 8F 40 01 00 00            mov rcx, qword ptr [rdi + 0x140]
0030DF98  49 8B F7                        mov rsi, r15
0030DF9B  48 89 4D E7                     mov qword ptr [rbp - 0x19], rcx
0030DF9F  0F B7 51 08                     movzx edx, word ptr [rcx + 8]
0030DFA3  0F B7 41 0A                     movzx eax, word ptr [rcx + 0xa]
0030DFA7  0F B6 49 0C                     movzx ecx, byte ptr [rcx + 0xc]
0030DFAB  0B C2                           or eax, edx
0030DFAD  48 D3 E6                        shl rsi, cl
0030DFB0  FF CE                           dec esi
0030DFB2  33 F0                           xor esi, eax
0030DFB4  0F BC CE                        bsf ecx, esi
0030DFB7  89 4D B7                        mov dword ptr [rbp - 0x49], ecx
0030DFBA  74 38                           je 0x14030dff4
0030DFBC  48 8B 7D E7                     mov rdi, qword ptr [rbp - 0x19]
0030DFC0  8D 46 FF                        lea eax, [rsi - 1]
0030DFC3  23 F0                           and esi, eax
0030DFC5  8B C1                           mov eax, ecx
0030DFC7  4C 6B F8 58                     imul r15, rax, 0x58
0030DFCB  49 83 C7 10                     add r15, 0x10
0030DFCF  4C 03 FF                        add r15, rdi
0030DFD2  49 8B 07                        mov rax, qword ptr [r15]
0030DFD5  48 85 C0                        test rax, rax
0030DFD8  0F 85 E7 01 00 00               jne 0x14030e1c5
0030DFDE  0F BC CE                        bsf ecx, esi
0030DFE1  89 4D B7                        mov dword ptr [rbp - 0x49], ecx
0030DFE4  75 DA                           jne 0x14030dfc0
0030DFE6  48 8B 7D CF                     mov rdi, qword ptr [rbp - 0x31]
0030DFEA  41 BF 01 00 00 00               mov r15d, 1
0030DFF0  4C 8B 55 DF                     mov r10, qword ptr [rbp - 0x21]
0030DFF4  4C 8B B7 48 01 00 00            mov r14, qword ptr [rdi + 0x148]
0030DFFB  4D 85 F6                        test r14, r14
0030DFFE  74 74                           je 0x14030e074
0030E000  41 0F B7 56 08                  movzx edx, word ptr [r14 + 8]
0030E005  49 8B F7                        mov rsi, r15
0030E008  41 0F B7 46 0A                  movzx eax, word ptr [r14 + 0xa]
0030E00D  41 0F B6 4E 0C                  movzx ecx, byte ptr [r14 + 0xc]
0030E012  0B C2                           or eax, edx
0030E014  48 D3 E6                        shl rsi, cl
0030E017  FF CE                           dec esi
0030E019  33 F0                           xor esi, eax
0030E01B  0F BC CE                        bsf ecx, esi
0030E01E  89 4D C7                        mov dword ptr [rbp - 0x39], ecx
0030E021  74 51                           je 0x14030e074
0030E023  48 8B 7D D7                     mov rdi, qword ptr [rbp - 0x29]
0030E027  8D 46 FF                        lea eax, [rsi - 1]
0030E02A  23 F0                           and esi, eax
0030E02C  8B C1                           mov eax, ecx
0030E02E  4C 6B F8 58                     imul r15, rax, 0x58
0030E032  49 83 C7 10                     add r15, 0x10
0030E036  4D 03 FE                        add r15, r14
0030E039  49 8B 07                        mov rax, qword ptr [r15]
0030E03C  48 85 C0                        test rax, rax
0030E03F  0F 85 76 02 00 00               jne 0x14030e2bb
0030E045  0F BC CE                        bsf ecx, esi
0030E048  48 BB FC FF FF FF FF FF FF 7F   movabs rbx, 0x7ffffffffffffffc
0030E052  49 BB 00 00 00 00 00 00 00 80   movabs r11, 0x8000000000000000
0030E05C  89 4D C7                        mov dword ptr [rbp - 0x39], ecx
0030E05F  75 C6                           jne 0x14030e027
0030E061  48 8B 7D CF                     mov rdi, qword ptr [rbp - 0x31]
0030E065  4C 8B 55 DF                     mov r10, qword ptr [rbp - 0x21]
0030E069  EB 09                           jmp 0x14030e074
0030E06B  45 85 C9                        test r9d, r9d
0030E06E  0F 84 1D FF FF FF               je 0x14030df91
0030E074  66 F0 FF 4F 34                  lock dec word ptr [rdi + 0x34]
0030E079  48 BB FC FF FF FF FF FF FF 7F   movabs rbx, 0x7ffffffffffffffc
0030E083  49 8B 3A                        mov rdi, qword ptr [r10]
0030E086  41 BF 01 00 00 00               mov r15d, 1
0030E08C  48 89 7D CF                     mov qword ptr [rbp - 0x31], rdi
0030E090  49 BB 00 00 00 00 00 00 00 80   movabs r11, 0x8000000000000000
0030E09A  48 85 FF                        test rdi, rdi
0030E09D  0F 85 7C FE FF FF               jne 0x14030df1f
0030E0A3  48 8B 75 D7                     mov rsi, qword ptr [rbp - 0x29]
0030E0A7  48 8B 0E                        mov rcx, qword ptr [rsi]
0030E0AA  48 85 C9                        test rcx, rcx
0030E0AD  0F 85 BD 04 00 00               jne 0x14030e570
0030E0B3  49 83 3A 00                     cmp qword ptr [r10], 0
0030E0B7  48 BB FC FF FF FF FF FF FF 7F   movabs rbx, 0x7ffffffffffffffc
0030E0C1  49 BB 00 00 00 00 00 00 00 80   movabs r11, 0x8000000000000000
0030E0CB  0F 85 3E FE FF FF               jne 0x14030df0f
0030E0D1  4C 8B 75 77                     mov r14, qword ptr [rbp + 0x77]
0030E0D5  41 8B F4                        mov esi, r12d
0030E0D8  48 8B 5D AF                     mov rbx, qword ptr [rbp - 0x51]
0030E0DC  4D 89 A6 A0 91 00 00            mov qword ptr [r14 + 0x91a0], r12
0030E0E3  48 85 DB                        test rbx, rbx
0030E0E6  0F 84 36 07 00 00               je 0x14030e822
0030E0EC  48 8B 03                        mov rax, qword ptr [rbx]
0030E0EF  48 89 45 AF                     mov qword ptr [rbp - 0x51], rax
0030E0F3  48 8D 93 28 FF FF FF            lea rdx, [rbx - 0xd8]
0030E0FA  45 33 C9                        xor r9d, r9d
0030E0FD  4C 8D 45 AF                     lea r8, [rbp - 0x51]
0030E101  49 8B CE                        mov rcx, r14
0030E104  E8 D7 4E F4 FF                  call 0x140252fe0
0030E109  48 8B 5D AF                     mov rbx, qword ptr [rbp - 0x51]
0030E10D  FF C6                           inc esi
0030E10F  48 85 DB                        test rbx, rbx
0030E112  74 07                           je 0x14030e11b
0030E114  48 8B 03                        mov rax, qword ptr [rbx]
0030E117  48 89 45 AF                     mov qword ptr [rbp - 0x51], rax
0030E11B  49 8D BE D8 35 00 00            lea rdi, [r14 + 0x35d8]
0030E122  40 F6 C6 0F                     test sil, 0xf
0030E126  75 08                           jne 0x14030e130
0030E128  48 8B CF                        mov rcx, rdi
0030E12B  E8 D0 40 F4 FF                  call 0x140252200
0030E130  48 85 DB                        test rbx, rbx
0030E133  75 BE                           jne 0x14030e0f3
0030E135  0F B6 47 01                     movzx eax, byte ptr [rdi + 1]
0030E139  84 C0                           test al, al
0030E13B  74 25                           je 0x14030e162
0030E13D  3C 01                           cmp al, 1
0030E13F  74 43                           je 0x14030e184
0030E141  0F B6 17                        movzx edx, byte ptr [rdi]
0030E144  48 8D 4F 08                     lea rcx, [rdi + 8]
0030E148  E8 E7 06 00 00                  call 0x14030e834
0030E14D  80 7F 01 02                     cmp byte ptr [rdi + 1], 2
0030E151  0F 84 8E 04 00 00               je 0x14030e5e5
0030E157  C6 47 01 00                     mov byte ptr [rdi + 1], 0
0030E15B  C7 47 04 FF FF 00 00            mov dword ptr [rdi + 4], 0xffff
0030E162  4C 8D 9C 24 C0 00 00 00         lea r11, [rsp + 0xc0]
0030E16A  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
0030E16E  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
0030E172  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
0030E176  49 8B E3                        mov rsp, r11
0030E179  41 5F                           pop r15
0030E17B  41 5E                           pop r14
0030E17D  41 5D                           pop r13
0030E17F  41 5C                           pop r12
0030E181  5D                              pop rbp
0030E182  C3                              ret
0030E183  CC                              int3
0030E184  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0030E18D  BA 1F 00 00 00                  mov edx, 0x1f
0030E192  8B 4F 04                        mov ecx, dword ptr [rdi + 4]
0030E195  44 0F B6 07                     movzx r8d, byte ptr [rdi]
0030E199  89 4D F7                        mov dword ptr [rbp - 9], ecx
0030E19C  48 8D 4D EF                     lea rcx, [rbp - 0x11]
0030E1A0  FF 80 D4 8E 00 00               inc dword ptr [rax + 0x8ed4]
0030E1A6  B8 2F 00 00 00                  mov eax, 0x2f
0030E1AB  41 80 F8 01                     cmp r8b, 1
0030E1AF  48 C7 45 EF 06 00 00 00         mov qword ptr [rbp - 0x11], 6
0030E1B7  4C 89 65 FB                     mov qword ptr [rbp - 5], r12
0030E1BB  0F 45 D0                        cmovne edx, eax
0030E1BE  E8 4D 41 F4 FF                  call 0x140252310
0030E1C3  EB 88                           jmp 0x14030e14d
0030E1C5  A8 02                           test al, 2
0030E1C7  0F 85 11 FE FF FF               jne 0x14030dfde
0030E1CD  48 85 C0                        test rax, rax
0030E1D0  0F 89 08 FE FF FF               jns 0x14030dfde
0030E1D6  41 80 7F 09 00                  cmp byte ptr [r15 + 9], 0
0030E1DB  0F 85 FD FD FF FF               jne 0x14030dfde
0030E1E1  4D 8B 2F                        mov r13, qword ptr [r15]
0030E1E4  33 C0                           xor eax, eax
0030E1E6  4C 23 EB                        and r13, rbx
0030E1E9  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
0030E1ED  0F 57 C0                        xorps xmm0, xmm0
0030E1F0  4C 89 6D B7                     mov qword ptr [rbp - 0x49], r13
0030E1F4  0F 11 45 07                     movups xmmword ptr [rbp + 7], xmm0
0030E1F8  44 89 65 BF                     mov dword ptr [rbp - 0x41], r12d
0030E1FC  74 0D                           je 0x14030e20b
0030E1FE  41 38 47 08                     cmp byte ptr [r15 + 8], al
0030E202  7C 07                           jl 0x14030e20b
0030E204  4D 0B EB                        or r13, r11
0030E207  4C 89 6D B7                     mov qword ptr [rbp - 0x49], r13
0030E20B  4C 8D 45 07                     lea r8, [rbp + 7]
0030E20F  33 D2                           xor edx, edx
0030E211  49 8B CF                        mov rcx, r15
0030E214  E8 A7 31 F1 FF                  call 0x1402213c0
0030E219  4C 8B F0                        mov r14, rax
0030E21C  48 85 C0                        test rax, rax
0030E21F  0F 84 69 04 00 00               je 0x14030e68e
0030E225  41 80 7F 09 00                  cmp byte ptr [r15 + 9], 0
0030E22A  0F 85 03 02 00 00               jne 0x14030e433
0030E230  BB 80 00 00 00                  mov ebx, 0x80
0030E235  4C 3B F8                        cmp r15, rax
0030E238  0F 84 9F 01 00 00               je 0x14030e3dd
0030E23E  49 8B CF                        mov rcx, r15
0030E241  E8 4A 0E F1 FF                  call 0x14021f090
0030E246  41 38 47 28                     cmp byte ptr [r15 + 0x28], al
0030E24A  0F 84 8A 01 00 00               je 0x14030e3da
0030E250  4D 8D 66 28                     lea r12, [r14 + 0x28]
0030E254  41 88 47 28                     mov byte ptr [r15 + 0x28], al
0030E258  49 8B CC                        mov rcx, r12
0030E25B  49 8D 57 10                     lea rdx, [r15 + 0x10]
0030E25F  E8 AC 69 FD FF                  call 0x1402e4c10
0030E264  49 8B 4C 24 08                  mov rcx, qword ptr [r12 + 8]
0030E269  45 0F B6 4F 28                  movzx r9d, byte ptr [r15 + 0x28]
0030E26E  49 8B 14 24                     mov rdx, qword ptr [r12]
0030E272  F6 C1 01                        test cl, 1
0030E275  0F 85 63 05 00 00               jne 0x14030e7de
0030E27B  83 E1 01                        and ecx, 1
0030E27E  45 32 C0                        xor r8b, r8b
0030E281  48 85 D2                        test rdx, rdx
0030E284  0F 84 41 01 00 00               je 0x14030e3cb
0030E28A  66 0F 1F 44 00 00               nop word ptr [rax + rax]
0030E290  44 38 4A 18                     cmp byte ptr [rdx + 0x18], r9b
0030E294  0F 8E 19 01 00 00               jle 0x14030e3b3
0030E29A  48 8B 02                        mov rax, qword ptr [rdx]
0030E29D  85 C9                           test ecx, ecx
0030E29F  74 0C                           je 0x14030e2ad
0030E2A1  48 85 C0                        test rax, rax
0030E2A4  0F 84 21 01 00 00               je 0x14030e3cb
0030E2AA  48 33 C2                        xor rax, rdx
0030E2AD  48 85 C0                        test rax, rax
0030E2B0  0F 84 15 01 00 00               je 0x14030e3cb
0030E2B6  48 8B D0                        mov rdx, rax
0030E2B9  EB D5                           jmp 0x14030e290
0030E2BB  A8 02                           test al, 2
0030E2BD  0F 85 82 FD FF FF               jne 0x14030e045
0030E2C3  48 85 C0                        test rax, rax
0030E2C6  0F 89 79 FD FF FF               jns 0x14030e045
0030E2CC  41 80 7F 09 00                  cmp byte ptr [r15 + 9], 0
0030E2D1  0F 85 6E FD FF FF               jne 0x14030e045
0030E2D7  33 C0                           xor eax, eax
0030E2D9  44 89 65 C3                     mov dword ptr [rbp - 0x3d], r12d
0030E2DD  48 89 45 2F                     mov qword ptr [rbp + 0x2f], rax
0030E2E1  0F 57 C0                        xorps xmm0, xmm0
0030E2E4  49 8B 07                        mov rax, qword ptr [r15]
0030E2E7  48 23 C3                        and rax, rbx
0030E2EA  48 89 45 C7                     mov qword ptr [rbp - 0x39], rax
0030E2EE  0F 11 45 1F                     movups xmmword ptr [rbp + 0x1f], xmm0
0030E2F2  74 0E                           je 0x14030e302
0030E2F4  41 80 7F 08 00                  cmp byte ptr [r15 + 8], 0
0030E2F9  7C 07                           jl 0x14030e302
0030E2FB  49 0B C3                        or rax, r11
0030E2FE  48 89 45 C7                     mov qword ptr [rbp - 0x39], rax
0030E302  4C 8D 45 1F                     lea r8, [rbp + 0x1f]
0030E306  33 D2                           xor edx, edx
0030E308  49 8B CF                        mov rcx, r15
0030E30B  E8 B0 30 F1 FF                  call 0x1402213c0
0030E310  4C 8B E8                        mov r13, rax
0030E313  48 85 C0                        test rax, rax
0030E316  0F 84 7C 03 00 00               je 0x14030e698
0030E31C  41 80 7F 09 00                  cmp byte ptr [r15 + 9], 0
0030E321  0F 85 EE 01 00 00               jne 0x14030e515
0030E327  BB 80 00 00 00                  mov ebx, 0x80
0030E32C  4C 3B F8                        cmp r15, rax
0030E32F  0F 84 8A 01 00 00               je 0x14030e4bf
0030E335  49 8B CF                        mov rcx, r15
0030E338  E8 53 0D F1 FF                  call 0x14021f090
0030E33D  41 38 47 28                     cmp byte ptr [r15 + 0x28], al
0030E341  0F 84 75 01 00 00               je 0x14030e4bc
0030E347  49 8D 57 10                     lea rdx, [r15 + 0x10]
0030E34B  41 88 47 28                     mov byte ptr [r15 + 0x28], al
0030E34F  49 8D 4D 28                     lea rcx, [r13 + 0x28]
0030E353  E8 B8 68 FD FF                  call 0x1402e4c10
0030E358  49 8B 4D 30                     mov rcx, qword ptr [r13 + 0x30]
0030E35C  45 0F B6 4F 28                  movzx r9d, byte ptr [r15 + 0x28]
0030E361  F6 C1 01                        test cl, 1
0030E364  0F 85 81 04 00 00               jne 0x14030e7eb
0030E36A  49 8B 45 28                     mov rax, qword ptr [r13 + 0x28]
0030E36E  83 E1 01                        and ecx, 1
0030E371  45 32 C0                        xor r8b, r8b
0030E374  48 8B D0                        mov rdx, rax
0030E377  48 85 C0                        test rax, rax
0030E37A  0F 84 2C 01 00 00               je 0x14030e4ac
0030E380  44 38 4A 18                     cmp byte ptr [rdx + 0x18], r9b
0030E384  0F 8E 0A 01 00 00               jle 0x14030e494
0030E38A  48 8B 02                        mov rax, qword ptr [rdx]
0030E38D  85 C9                           test ecx, ecx
0030E38F  74 0C                           je 0x14030e39d
0030E391  48 85 C0                        test rax, rax
0030E394  0F 84 12 01 00 00               je 0x14030e4ac
0030E39A  48 33 C2                        xor rax, rdx
0030E39D  48 85 C0                        test rax, rax
0030E3A0  0F 84 06 01 00 00               je 0x14030e4ac
0030E3A6  48 8B D0                        mov rdx, rax
0030E3A9  EB D5                           jmp 0x14030e380
0030E3AB  45 8B CF                        mov r9d, r15d
0030E3AE  E9 B7 FB FF FF                  jmp 0x14030df6a
0030E3B3  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
0030E3B7  85 C9                           test ecx, ecx
0030E3B9  0F 84 07 02 00 00               je 0x14030e5c6
0030E3BF  48 85 C0                        test rax, rax
0030E3C2  0F 85 FB 01 00 00               jne 0x14030e5c3
0030E3C8  41 B0 01                        mov r8b, 1
0030E3CB  4D 8D 4F 10                     lea r9, [r15 + 0x10]
0030E3CF  49 8B CC                        mov rcx, r12
0030E3D2  E8 99 61 FD FF                  call 0x1402e4570
0030E3D7  45 33 E4                        xor r12d, r12d
0030E3DA  83 CB 10                        or ebx, 0x10
0030E3DD  41 8B 4E 54                     mov ecx, dword ptr [r14 + 0x54]
0030E3E1  44 89 65 A7                     mov dword ptr [rbp - 0x59], r12d
0030E3E5  84 C9                           test cl, cl
0030E3E7  74 04                           je 0x14030e3ed
0030E3E9  C6 45 A8 02                     mov byte ptr [rbp - 0x58], 2
0030E3ED  F7 C1 00 7F 00 00               test ecx, 0x7f00
0030E3F3  76 04                           jbe 0x14030e3f9
0030E3F5  C6 45 A9 01                     mov byte ptr [rbp - 0x57], 1
0030E3F9  49 8B 46 40                     mov rax, qword ptr [r14 + 0x40]
0030E3FD  48 85 C0                        test rax, rax
0030E400  0F 84 FA 03 00 00               je 0x14030e800
0030E406  0F B6 50 18                     movzx edx, byte ptr [rax + 0x18]
0030E40A  88 55 A7                        mov byte ptr [rbp - 0x59], dl
0030E40D  41 80 7E 09 00                  cmp byte ptr [r14 + 9], 0
0030E412  0F 85 8A 02 00 00               jne 0x14030e6a2
0030E418  83 7D A7 00                     cmp dword ptr [rbp - 0x59], 0
0030E41C  0F 85 E1 01 00 00               jne 0x14030e603
0030E422  48 8D 4D 07                     lea rcx, [rbp + 7]
0030E426  E8 85 8D F0 FF                  call 0x1402171b0
0030E42B  83 E3 F9                        and ebx, 0xfffffff9
0030E42E  83 CB 01                        or ebx, 1
0030E431  EB 1E                           jmp 0x14030e451
0030E433  BB 88 00 00 00                  mov ebx, 0x88
0030E438  48 8D 4D 07                     lea rcx, [rbp + 7]
0030E43C  E8 6F 8D F0 FF                  call 0x1402171b0
0030E441  44 8B 65 BF                     mov r12d, dword ptr [rbp - 0x41]
0030E445  45 85 E4                        test r12d, r12d
0030E448  0F 85 C8 02 00 00               jne 0x14030e716
0030E44E  45 33 E4                        xor r12d, r12d
0030E451  F7 05 B9 86 CB 00 00 10 00 00   test dword ptr [rip + 0xcb86b9], 0x1000
0030E45B  74 1E                           je 0x14030e47b
0030E45D  41 0F B6 47 08                  movzx eax, byte ptr [r15 + 8]
0030E462  44 8B C3                        mov r8d, ebx
0030E465  83 E0 3F                        and eax, 0x3f
0030E468  49 8B D5                        mov rdx, r13
0030E46B  48 6B C8 58                     imul rcx, rax, 0x58
0030E46F  4C 2B F9                        sub r15, rcx
0030E472  49 8B 4F F0                     mov rcx, qword ptr [r15 - 0x10]
0030E476  E8 01 38 F1 FF                  call 0x140221c7c
0030E47B  49 BB 00 00 00 00 00 00 00 80   movabs r11, 0x8000000000000000
0030E485  48 BB FC FF FF FF FF FF FF 7F   movabs rbx, 0x7ffffffffffffffc
0030E48F  E9 4A FB FF FF                  jmp 0x14030dfde
0030E494  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
0030E498  85 C9                           test ecx, ecx
0030E49A  0F 84 37 01 00 00               je 0x14030e5d7
0030E4A0  48 85 C0                        test rax, rax
0030E4A3  0F 85 2B 01 00 00               jne 0x14030e5d4
0030E4A9  41 B0 01                        mov r8b, 1
0030E4AC  4D 8D 4F 10                     lea r9, [r15 + 0x10]
0030E4B0  49 8D 4D 28                     lea rcx, [r13 + 0x28]
0030E4B4  E8 B7 60 FD FF                  call 0x1402e4570
0030E4B9  45 33 E4                        xor r12d, r12d
0030E4BC  83 CB 10                        or ebx, 0x10
0030E4BF  41 8B 4D 54                     mov ecx, dword ptr [r13 + 0x54]
0030E4C3  44 89 65 AB                     mov dword ptr [rbp - 0x55], r12d
0030E4C7  84 C9                           test cl, cl
0030E4C9  74 04                           je 0x14030e4cf
0030E4CB  C6 45 AC 02                     mov byte ptr [rbp - 0x54], 2
0030E4CF  F7 C1 00 7F 00 00               test ecx, 0x7f00
0030E4D5  76 04                           jbe 0x14030e4db
0030E4D7  C6 45 AD 01                     mov byte ptr [rbp - 0x53], 1
0030E4DB  49 8B 45 40                     mov rax, qword ptr [r13 + 0x40]
0030E4DF  48 85 C0                        test rax, rax
0030E4E2  0F 84 21 03 00 00               je 0x14030e809
0030E4E8  0F B6 50 18                     movzx edx, byte ptr [rax + 0x18]
0030E4EC  88 55 AB                        mov byte ptr [rbp - 0x55], dl
0030E4EF  41 80 7D 09 00                  cmp byte ptr [r13 + 9], 0
0030E4F4  0F 85 E2 01 00 00               jne 0x14030e6dc
0030E4FA  83 7D AB 00                     cmp dword ptr [rbp - 0x55], 0
0030E4FE  0F 85 45 01 00 00               jne 0x14030e649
0030E504  48 8D 4D 1F                     lea rcx, [rbp + 0x1f]
0030E508  E8 A3 8C F0 FF                  call 0x1402171b0
0030E50D  83 E3 F9                        and ebx, 0xfffffff9
0030E510  83 CB 01                        or ebx, 1
0030E513  EB 1E                           jmp 0x14030e533
0030E515  BB 88 00 00 00                  mov ebx, 0x88
0030E51A  48 8D 4D 1F                     lea rcx, [rbp + 0x1f]
0030E51E  E8 8D 8C F0 FF                  call 0x1402171b0
0030E523  44 8B 65 C3                     mov r12d, dword ptr [rbp - 0x3d]
0030E527  45 85 E4                        test r12d, r12d
0030E52A  0F 85 4A 02 00 00               jne 0x14030e77a
0030E530  45 33 E4                        xor r12d, r12d
0030E533  F7 05 D7 85 CB 00 00 10 00 00   test dword ptr [rip + 0xcb85d7], 0x1000
0030E53D  0F 84 02 FB FF FF               je 0x14030e045
0030E543  41 0F B6 47 08                  movzx eax, byte ptr [r15 + 8]
0030E548  44 8B C3                        mov r8d, ebx
0030E54B  48 8B 55 C7                     mov rdx, qword ptr [rbp - 0x39]
0030E54F  83 E0 3F                        and eax, 0x3f
0030E552  48 6B C8 58                     imul rcx, rax, 0x58
0030E556  4C 2B F9                        sub r15, rcx
0030E559  49 8B 4F F0                     mov rcx, qword ptr [r15 - 0x10]
0030E55D  E8 1A 37 F1 FF                  call 0x140221c7c
0030E562  E9 DE FA FF FF                  jmp 0x14030e045
0030E567  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
0030E570  48 8B 01                        mov rax, qword ptr [rcx]
0030E573  48 8D 99 D8 FC FF FF            lea rbx, [rcx - 0x328]
0030E57A  48 89 06                        mov qword ptr [rsi], rax
0030E57D  4C 89 39                        mov qword ptr [rcx], r15
0030E580  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
0030E585  0F B6 83 18 03 00 00            movzx eax, byte ptr [rbx + 0x318]
0030E58C  84 C0                           test al, al
0030E58E  74 1D                           je 0x14030e5ad
0030E590  4C 8B CE                        mov r9, rsi
0030E593  4C 89 54 24 20                  mov qword ptr [rsp + 0x20], r10
0030E598  4C 8D 45 AF                     lea r8, [rbp - 0x51]
0030E59C  BA 04 00 00 00                  mov edx, 4
0030E5A1  48 8B CB                        mov rcx, rbx
0030E5A4  E8 87 37 F1 FF                  call 0x140221d30
0030E5A9  4C 8B 55 DF                     mov r10, qword ptr [rbp - 0x21]
0030E5AD  66 F0 FF 8B 64 03 00 00         lock dec word ptr [rbx + 0x364]
0030E5B5  48 8B 0E                        mov rcx, qword ptr [rsi]
0030E5B8  48 85 C9                        test rcx, rcx
0030E5BB  0F 84 F2 FA FF FF               je 0x14030e0b3
0030E5C1  EB AD                           jmp 0x14030e570
0030E5C3  48 33 C2                        xor rax, rdx
0030E5C6  48 85 C0                        test rax, rax
0030E5C9  0F 85 E7 FC FF FF               jne 0x14030e2b6
0030E5CF  E9 F4 FD FF FF                  jmp 0x14030e3c8
0030E5D4  48 33 C2                        xor rax, rdx
0030E5D7  48 85 C0                        test rax, rax
0030E5DA  0F 85 C6 FD FF FF               jne 0x14030e3a6
0030E5E0  E9 C4 FE FF FF                  jmp 0x14030e4a9
0030E5E5  48 8D 4F 10                     lea rcx, [rdi + 0x10]
0030E5E9  48 C7 47 08 01 00 20 00         mov qword ptr [rdi + 8], 0x200001
0030E5F1  33 D2                           xor edx, edx
0030E5F3  41 B8 00 01 00 00               mov r8d, 0x100
0030E5F9  E8 42 86 3B 00                  call 0x1406c6c40
0030E5FE  E9 54 FB FF FF                  jmp 0x14030e157
0030E603  4C 8B 4D D7                     mov r9, qword ptr [rbp - 0x29]
0030E607  48 8D 45 BF                     lea rax, [rbp - 0x41]
0030E60B  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0030E610  4C 8D 45 AF                     lea r8, [rbp - 0x51]
0030E614  48 8D 55 A7                     lea rdx, [rbp - 0x59]
0030E618  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
0030E61D  49 8B CF                        mov rcx, r15
0030E620  E8 6B 0B F1 FF                  call 0x14021f190
0030E625  85 C0                           test eax, eax
0030E627  0F 84 0B FE FF FF               je 0x14030e438
0030E62D  4D 3B FE                        cmp r15, r14
0030E630  0F 84 02 FE FF FF               je 0x14030e438
0030E636  49 8B D6                        mov rdx, r14
0030E639  49 8B CF                        mov rcx, r15
0030E63C  E8 2F 73 FD FF                  call 0x1402e5970
0030E641  83 CB 20                        or ebx, 0x20
0030E644  E9 EF FD FF FF                  jmp 0x14030e438
0030E649  48 8D 45 C3                     lea rax, [rbp - 0x3d]
0030E64D  4C 8B CF                        mov r9, rdi
0030E650  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0030E655  4C 8D 45 AF                     lea r8, [rbp - 0x51]
0030E659  48 8D 55 AB                     lea rdx, [rbp - 0x55]
0030E65D  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
0030E662  49 8B CF                        mov rcx, r15
0030E665  E8 26 0B F1 FF                  call 0x14021f190
0030E66A  85 C0                           test eax, eax
0030E66C  0F 84 A8 FE FF FF               je 0x14030e51a
0030E672  4D 3B FD                        cmp r15, r13
0030E675  0F 84 9F FE FF FF               je 0x14030e51a
0030E67B  49 8B D5                        mov rdx, r13
0030E67E  49 8B CF                        mov rcx, r15
0030E681  E8 EA 72 FD FF                  call 0x1402e5970
0030E686  83 CB 20                        or ebx, 0x20
0030E689  E9 8C FE FF FF                  jmp 0x14030e51a
0030E68E  BB 80 00 00 00                  mov ebx, 0x80
0030E693  E9 B9 FD FF FF                  jmp 0x14030e451
0030E698  BB 80 00 00 00                  mov ebx, 0x80
0030E69D  E9 91 FE FF FF                  jmp 0x14030e533
0030E6A2  41 0F B6 46 08                  movzx eax, byte ptr [r14 + 8]
0030E6A7  83 E0 3F                        and eax, 0x3f
0030E6AA  48 6B C8 58                     imul rcx, rax, 0x58
0030E6AE  49 8B C6                        mov rax, r14
0030E6B1  48 2B C1                        sub rax, rcx
0030E6B4  48 8B 40 F0                     mov rax, qword ptr [rax - 0x10]
0030E6B8  0F B6 88 C3 00 00 00            movzx ecx, byte ptr [rax + 0xc3]
0030E6BF  80 F9 1E                        cmp cl, 0x1e
0030E6C2  8B C1                           mov eax, ecx
0030E6C4  B9 1E 00 00 00                  mov ecx, 0x1e
0030E6C9  0F 4F C1                        cmovg eax, ecx
0030E6CC  3A C2                           cmp al, dl
0030E6CE  0F 8E 44 FD FF FF               jle 0x14030e418
0030E6D4  88 45 A7                        mov byte ptr [rbp - 0x59], al
0030E6D7  E9 3C FD FF FF                  jmp 0x14030e418
0030E6DC  41 0F B6 45 08                  movzx eax, byte ptr [r13 + 8]
0030E6E1  83 E0 3F                        and eax, 0x3f
0030E6E4  48 6B C8 58                     imul rcx, rax, 0x58
0030E6E8  49 8B C5                        mov rax, r13
0030E6EB  48 2B C1                        sub rax, rcx
0030E6EE  48 8B 40 F0                     mov rax, qword ptr [rax - 0x10]
0030E6F2  0F B6 88 C3 00 00 00            movzx ecx, byte ptr [rax + 0xc3]
0030E6F9  80 F9 1E                        cmp cl, 0x1e
0030E6FC  8B C1                           mov eax, ecx
0030E6FE  B9 1E 00 00 00                  mov ecx, 0x1e
0030E703  0F 4F C1                        cmovg eax, ecx
0030E706  3A C2                           cmp al, dl
0030E708  0F 8E EC FD FF FF               jle 0x14030e4fa
0030E70E  88 45 AB                        mov byte ptr [rbp - 0x55], al
0030E711  E9 E4 FD FF FF                  jmp 0x14030e4fa
0030E716  41 0F B6 47 08                  movzx eax, byte ptr [r15 + 8]
0030E71B  BA 44 66 6C 74                  mov edx, 0x746c6644
0030E720  83 E0 3F                        and eax, 0x3f
0030E723  48 6B C8 58                     imul rcx, rax, 0x58
0030E727  49 8B C7                        mov rax, r15
0030E72A  48 2B C1                        sub rax, rcx
0030E72D  4C 8B 68 F0                     mov r13, qword ptr [rax - 0x10]
0030E731  49 8B CD                        mov rcx, r13
0030E734  E8 A7 27 F0 FF                  call 0x140210ee0
0030E739  84 C0                           test al, al
0030E73B  74 34                           je 0x14030e771
0030E73D  41 F6 C4 01                     test r12b, 1
0030E741  74 13                           je 0x14030e756
0030E743  BA 02 00 00 00                  mov edx, 2
0030E748  41 B8 00 00 00 80               mov r8d, 0x80000000
0030E74E  49 8B CD                        mov rcx, r13
0030E751  E8 BA 79 F0 FF                  call 0x140216110
0030E756  41 F6 C4 02                     test r12b, 2
0030E75A  74 08                           je 0x14030e764
0030E75C  49 8B CD                        mov rcx, r13
0030E75F  E8 F0 74 F0 FF                  call 0x140215c54
0030E764  BA 44 66 6C 74                  mov edx, 0x746c6644
0030E769  49 8B CD                        mov rcx, r13
0030E76C  E8 2F 57 F5 FF                  call 0x140263ea0
0030E771  4C 8B 6D B7                     mov r13, qword ptr [rbp - 0x49]
0030E775  E9 D4 FC FF FF                  jmp 0x14030e44e
0030E77A  41 0F B6 47 08                  movzx eax, byte ptr [r15 + 8]
0030E77F  BA 44 66 6C 74                  mov edx, 0x746c6644
0030E784  83 E0 3F                        and eax, 0x3f
0030E787  48 6B C8 58                     imul rcx, rax, 0x58
0030E78B  49 8B C7                        mov rax, r15
0030E78E  48 2B C1                        sub rax, rcx
0030E791  4C 8B 68 F0                     mov r13, qword ptr [rax - 0x10]
0030E795  49 8B CD                        mov rcx, r13
0030E798  E8 43 27 F0 FF                  call 0x140210ee0
0030E79D  84 C0                           test al, al
0030E79F  0F 84 8B FD FF FF               je 0x14030e530
0030E7A5  41 F6 C4 01                     test r12b, 1
0030E7A9  74 13                           je 0x14030e7be
0030E7AB  BA 02 00 00 00                  mov edx, 2
0030E7B0  41 B8 00 00 00 80               mov r8d, 0x80000000
0030E7B6  49 8B CD                        mov rcx, r13
0030E7B9  E8 52 79 F0 FF                  call 0x140216110
0030E7BE  41 F6 C4 02                     test r12b, 2
0030E7C2  74 08                           je 0x14030e7cc
0030E7C4  49 8B CD                        mov rcx, r13
0030E7C7  E8 88 74 F0 FF                  call 0x140215c54
0030E7CC  BA 44 66 6C 74                  mov edx, 0x746c6644
0030E7D1  49 8B CD                        mov rcx, r13
0030E7D4  E8 C7 56 F5 FF                  call 0x140263ea0
0030E7D9  E9 52 FD FF FF                  jmp 0x14030e530
0030E7DE  48 85 D2                        test rdx, rdx
0030E7E1  74 2F                           je 0x14030e812
0030E7E3  49 33 D4                        xor rdx, r12
0030E7E6  E9 90 FA FF FF                  jmp 0x14030e27b
0030E7EB  49 8B 55 28                     mov rdx, qword ptr [r13 + 0x28]
0030E7EF  48 85 D2                        test rdx, rdx
0030E7F2  74 26                           je 0x14030e81a
0030E7F4  49 8D 45 28                     lea rax, [r13 + 0x28]
0030E7F8  48 33 C2                        xor rax, rdx
0030E7FB  E9 6E FB FF FF                  jmp 0x14030e36e
0030E800  0F B6 55 A7                     movzx edx, byte ptr [rbp - 0x59]
0030E804  E9 04 FC FF FF                  jmp 0x14030e40d
0030E809  0F B6 55 AB                     movzx edx, byte ptr [rbp - 0x55]
0030E80D  E9 DD FC FF FF                  jmp 0x14030e4ef
0030E812  45 32 C0                        xor r8b, r8b
0030E815  E9 B1 FB FF FF                  jmp 0x14030e3cb
0030E81A  45 32 C0                        xor r8b, r8b
0030E81D  E9 8A FC FF FF                  jmp 0x14030e4ac
0030E822  49 8D BE D8 35 00 00            lea rdi, [r14 + 0x35d8]
0030E829  E9 07 F9 FF FF                  jmp 0x14030e135
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiAbDeferredProcessingWorker(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m64;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m98;
    unsigned int v_stack_m9C;
    unsigned int v_stack_mA0;
    unsigned int v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int8 v_stack_mB2;
    unsigned __int8 v_stack_mB3;
    unsigned int v_stack_mB4;
    unsigned __int8 v_stack_mB6;
    unsigned __int8 v_stack_mB7;
    unsigned int v_stack_mB8;
    unsigned int v_stack_mC0;
    unsigned int v_stack_mE8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p20 = v_rdi;
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (192);
    v_r12 = 0;
    v_stack_mB0 = 0;
    v_stack_m88 = a3 + 37240;
    v_stack_m80 = a3 + 37232;
loc_0030DF0F:
    v_stack_m90 = *(unsigned __int64 *)(a3 + 37232);
    if (*(unsigned __int64 *)(a3 + 37232) == 0) goto loc_0030E0A7;
loc_0030DF1F:
    *(unsigned __int64 *)(a3 + 37232) = *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 37232));
    *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 37232)) = v_r12 + 1;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a3 + 37232) - 23)) == 0) goto loc_0030E074;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 37232) + 328) == 0) goto loc_0030E3AB;
    a3 = (v_r12 + 1) << ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 37232) + 328) + 12)));
    a3 = (unsigned int)((a3) - 1);
    a2 = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 37232) + 328) + 10)) | ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 37232) + 328) + 8))));
    a4 = (((unsigned int)(a3)) == ((unsigned int)(a2))) ? 1 : 0;
loc_0030DF6A:
    a3 = (v_r12 + 1) << ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 37232) + 320) + 12)));
    a3 = (unsigned int)((a3) - 1);
    a1 = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 37232) + 320) + 10)) | ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 37232) + 320) + 8))));
    if (((unsigned int)(a3)) == ((unsigned int)(a1))) goto loc_0030E06B;
loc_0030DF91:
    v_stack_m78 = *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 37232) + 320);
    result = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 37232) + 320) + 10)) | ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 37232) + 320) + 8))));
    v_rsi = (v_r12 + 1) << ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 37232) + 320) + 12)));
    v_rsi = (unsigned int)((v_rsi) - 1);
    v_rsi = (unsigned int)((v_rsi) ^ ((unsigned int)(result)));
    v_stack_mA8 = (unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 37232) + 320) + 12));
    if (condition_is_equal) goto loc_0030DFF4;
loc_0030DFC0:
    v_rsi = (unsigned int)((v_rsi) & ((unsigned int)(v_rsi - 1)));
    v_r15 = (v_r12 + 1) * ((unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 37232) + 320) + 12))));
    v_r15 = (v_r15) + (16);
    v_r15 = (v_r15) + (v_stack_m78);
    if (*(unsigned __int64 *)(v_r15) != 0) goto loc_0030E1C5;
loc_0030DFDE:
    v_stack_mA8 = (unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 37232) + 320) + 12));
    if (*(unsigned __int64 *)(v_r15) != 0) goto loc_0030DFC0;
loc_0030DFF4:
    if (*(unsigned __int64 *)(v_stack_m90 + 328) == 0) goto loc_0030E074;
    result = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m90 + 328) + 10)) | ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m90 + 328) + 8))));
    v_rsi = (1) << ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m90 + 328) + 12)));
    v_rsi = (unsigned int)((v_rsi) - 1);
    v_rsi = (unsigned int)((v_rsi) ^ ((unsigned int)(result)));
    v_stack_m98 = (unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m90 + 328) + 12));
    if (condition_is_equal) goto loc_0030E074;
loc_0030E027:
    v_rsi = (unsigned int)((v_rsi) & ((unsigned int)(v_rsi - 1)));
    v_r15 = (1) * ((unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m90 + 328) + 12))));
    v_r15 = (v_r15) + (16);
    v_r15 = (v_r15) + (*(unsigned __int64 *)(v_stack_m90 + 328));
    if (*(unsigned __int64 *)(v_r15) != 0) goto loc_0030E2BB;
loc_0030E045:
    v_stack_m98 = (unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m90 + 328) + 12));
    if (*(unsigned __int64 *)(v_r15) != 0) goto loc_0030E027;
    goto loc_0030E074;
loc_0030E06B:
    if ((unsigned int)(a4) == 0) goto loc_0030DF91;
loc_0030E074:
    v_stack_m90 = *(unsigned __int64 *)(v_stack_m80);
    if (*(unsigned __int64 *)(v_stack_m80) != 0) goto loc_0030DF1F;
loc_0030E0A7:
    if (*(unsigned __int64 *)(v_stack_m88) != 0) goto loc_0030E570;
loc_0030E0B3:
    if ((*(unsigned __int64 *)(v_stack_m80)) != 0) goto loc_0030DF0F;
    *(unsigned __int64 *)(v_stack_p18 + 37280) = 0;
    if (v_stack_mB0 == 0) goto loc_0030E822;
    v_stack_mB0 = *(unsigned __int64 *)(v_stack_mB0);
loc_0030E0F3:
    a4 = 0;
    result = KiDeferredReadySingleThread(v_stack_p18, v_stack_mB0 - 216, v_stack_mB0, a4);
    v_rsi = (unsigned int)((0) + 1);
    if (v_stack_mB0 != 0) {
        result = *(unsigned __int64 *)(v_stack_mB0);
        v_stack_mB0 = result;
    }
    if ((((unsigned __int8)(v_rsi)) & (15)) == 0) {
        a1 = v_stack_p18 + 13784;
        result = KiFlushSoftwareInterruptBatch(a1, v_stack_mB0 - 216, v_stack_mB0, a4);
    }
    if (v_stack_mB0 != 0) goto loc_0030E0F3;
loc_0030E135:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_stack_p18 + 13784 + 1)) == 0) goto loc_0030E162;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_stack_p18 + 13784 + 1))) == 1) goto loc_0030E184;
    result = KiSendSoftwareInterruptAffinity(v_stack_p18 + 13784 + 8, *(unsigned __int8 *)(v_stack_p18 + 13784), v_stack_mB0, a4);
loc_0030E14D:
    if ((*(unsigned __int8 *)(v_stack_p18 + 13784 + 1)) == 2) goto loc_0030E5E5;
loc_0030E157:
    *(unsigned __int8 *)(v_stack_p18 + 13784 + 1) = 0;
    *(unsigned int *)(v_stack_p18 + 13784 + 4) = 0xFFFFULL;
loc_0030E162:
    return result;
loc_0030E184:
    v_stack_m68 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 4)));
    v_stack_m70 = 6;
    v_stack_m64 = 0;
    a2 = 31;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 72)))) != 1) { a2 = 47; }
    result = HalpInterruptSendIpi(v_stack_m70, a2, *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 72)), a4);
    goto loc_0030E14D;
loc_0030E1C5:
    if ((((unsigned __int8)(result)) & (2)) != 0) goto loc_0030DFDE;
    if (!sign_flag) goto loc_0030DFDE;
    if ((*(unsigned __int8 *)(1 + 9)) != 0) goto loc_0030DFDE;
    result = 0;
    v_r13 = (*(unsigned __int64 *)(1)) & (*(unsigned __int64 *)(v_stack_m28 + 48));
    v_stack_m48 = 0;
    v_stack_mA8 = v_r13;
    v_stack_m58 = v_xmm0;
    v_stack_mA0 = 0;
    if (condition_is_equal) goto loc_0030E20B;
    if ((*(unsigned __int8 *)(1 + 8)) >= 0) {
        v_r13 = (v_r13) | (v_stack_m28);
        v_stack_mA8 = v_r13;
    }
    a2 = 0;
    result = KiAbEntryGetLockedHeadEntry(1, a2, v_stack_m58, a4);
    if (result == 0) goto loc_0030E68E;
    if ((*(unsigned __int8 *)(1 + 9)) != 0) goto loc_0030E433;
    if (1 == result) goto loc_0030E3DD;
    result = KiAbOwnerComputeCpuPriorityKey(1, a2, v_stack_m58, a4);
    if ((*(unsigned __int8 *)(1 + 40)) == ((unsigned __int8)(result))) goto loc_0030E3DA;
    *(unsigned __int8 *)(1 + 40) = (unsigned __int8)(result);
    result = RtlRbRemoveNode(result + 40, 1 + 16, v_stack_m58, a4);
    if ((((unsigned __int8)(*(unsigned __int64 *)(result + 40 + 8))) & (1)) != 0) goto loc_0030E7DE;
loc_0030E27B:
    a1 = (unsigned int)((*(unsigned __int64 *)(result + 40 + 8)) & (1));
    a3 = 0;
    if (*(unsigned __int64 *)(result + 40) == 0) goto loc_0030E3CB;
loc_0030E290:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(result + 40) + 24)) <= ((unsigned __int8)(*(unsigned __int8 *)(1 + 40)))) goto loc_0030E3B3;
    if ((unsigned int)(a1) == 0) goto loc_0030E2AD;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 40)) == 0) goto loc_0030E3CB;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 40))) ^ (*(unsigned __int64 *)(result + 40));
loc_0030E2AD:
    if (result == 0) goto loc_0030E3CB;
loc_0030E2B6:
    goto loc_0030E290;
loc_0030E2BB:
    if ((((unsigned __int8)(result)) & (2)) != 0) goto loc_0030E045;
    if (!sign_flag) goto loc_0030E045;
    if ((*(unsigned __int8 *)(1 + 9)) != 0) goto loc_0030E045;
    result = 0;
    v_stack_m9C = (unsigned int)(result + 40);
    v_stack_m30 = 0;
    result = (*(unsigned __int64 *)(1)) & (128);
    v_stack_m98 = result;
    v_stack_m40 = v_xmm0;
    if (condition_is_equal) goto loc_0030E302;
    if ((*(unsigned __int8 *)(1 + 8)) >= 0) {
        result = (result) | (v_stack_m28);
        v_stack_m98 = result;
    }
    a2 = 0;
    result = KiAbEntryGetLockedHeadEntry(1, a2, v_stack_m40, *(unsigned __int8 *)(1 + 40));
    if (result == 0) goto loc_0030E698;
    if ((*(unsigned __int8 *)(1 + 9)) != 0) goto loc_0030E515;
    if (1 == result) goto loc_0030E4BF;
    result = KiAbOwnerComputeCpuPriorityKey(1, a2, v_stack_m40, *(unsigned __int8 *)(1 + 40));
    if ((*(unsigned __int8 *)(1 + 40)) == ((unsigned __int8)(result))) goto loc_0030E4BC;
    *(unsigned __int8 *)(1 + 40) = (unsigned __int8)(result);
    result = RtlRbRemoveNode(result + 40, 1 + 16, v_stack_m40, *(unsigned __int8 *)(1 + 40));
    if ((((unsigned __int8)(*(unsigned __int64 *)(result + 48))) & (1)) != 0) goto loc_0030E7EB;
loc_0030E36E:
    a1 = (unsigned int)((*(unsigned __int64 *)(result + 48)) & (1));
    a3 = 0;
    if (*(unsigned __int64 *)(result + 40) == 0) goto loc_0030E4AC;
loc_0030E380:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(result + 40) + 24)) <= ((unsigned __int8)(*(unsigned __int8 *)(1 + 40)))) goto loc_0030E494;
    if ((unsigned int)(a1) == 0) goto loc_0030E39D;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 40)) == 0) goto loc_0030E4AC;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 40))) ^ (*(unsigned __int64 *)(result + 40));
loc_0030E39D:
    if (result == 0) goto loc_0030E4AC;
loc_0030E3A6:
    goto loc_0030E380;
loc_0030E3AB:
    goto loc_0030DF6A;
loc_0030E3B3:
    if ((unsigned int)(a1) == 0) goto loc_0030E5C6;
    if (*(unsigned __int64 *)(result + 8) != 0) goto loc_0030E5C3;
loc_0030E3C8:
loc_0030E3CB:
    result = RtlRbInsertNodeEx(result + 40, result, 1, 1 + 16);
    v_r12 = 0;
loc_0030E3DA:
    v_rbx = (unsigned int)((128) | (16));
loc_0030E3DD:
    v_stack_mB8 = 0;
    if ((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 84))) != 0) {
        v_stack_mB7 = 2;
    }
    if (!(condition_is_below_or_equal)) {
        v_stack_mB6 = 1;
    }
    if (*(unsigned __int64 *)(result + 64) == 0) goto loc_0030E800;
    v_stack_mB8 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(result + 64) + 24));
loc_0030E40D:
    if ((*(unsigned __int8 *)(result + 9)) != 0) goto loc_0030E6A2;
loc_0030E418:
    if (v_stack_mB8 != 0) goto loc_0030E603;
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(v_stack_m58, *(unsigned __int8 *)(*(unsigned __int64 *)(result + 64) + 24), 1, 1 + 16);
    v_rbx = (unsigned int)((v_rbx) & (0xFFFFFFF9ULL));
    v_rbx = (unsigned int)((v_rbx) | (1));
    goto loc_0030E451;
loc_0030E433:
loc_0030E438:
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(v_stack_m58, *(unsigned __int8 *)(*(unsigned __int64 *)(result + 64) + 24), 1, 1 + 16);
    if ((unsigned int)((unsigned int)(v_stack_mA0)) != 0) goto loc_0030E716;
loc_0030E44E:
    v_r12 = 0;
loc_0030E451:
    v_r15 = 1;
    if (((*(unsigned int *)(v_rip + 13338297)) & (0x1000ULL)) != 0) {
        result = *(unsigned __int8 *)(1 + 8);
        a3 = 136;
        result = (unsigned int)((result) & (63));
        a2 = result;
        a1 = (v_stack_m58) * (result);
        v_r15 = (1) - (a1);
        a1 = *(unsigned __int64 *)(v_r15 - 16);
        result = EtwTraceAutoBoostProcessLockEntry(a1, a2, a3, 1 + 16);
    }
    goto loc_0030DFDE;
loc_0030E494:
    if ((unsigned int)(a1) == 0) goto loc_0030E5D7;
    if (*(unsigned __int64 *)(a2 + 8) != 0) goto loc_0030E5D4;
loc_0030E4A9:
loc_0030E4AC:
    result = RtlRbInsertNodeEx(result + 40, a2, 1, v_r15 + 16);
    v_r12 = 0;
loc_0030E4BC:
    v_rbx = (unsigned int)((136) | (16));
loc_0030E4BF:
    v_stack_mB4 = 0;
    if ((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 84))) != 0) {
        v_stack_mB3 = 2;
    }
    if (!(condition_is_below_or_equal)) {
        v_stack_mB2 = 1;
    }
    if (*(unsigned __int64 *)(result + 64) == 0) goto loc_0030E809;
    v_stack_mB4 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(result + 64) + 24));
loc_0030E4EF:
    if ((*(unsigned __int8 *)(result + 9)) != 0) goto loc_0030E6DC;
loc_0030E4FA:
    if (v_stack_mB4 != 0) goto loc_0030E649;
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(v_stack_m40, *(unsigned __int8 *)(*(unsigned __int64 *)(result + 64) + 24), 1, v_r15 + 16);
    v_rbx = (unsigned int)((v_rbx) & (0xFFFFFFF9ULL));
    v_rbx = (unsigned int)((v_rbx) | (1));
    goto loc_0030E533;
loc_0030E515:
loc_0030E51A:
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(v_stack_m40, *(unsigned __int8 *)(*(unsigned __int64 *)(result + 64) + 24), 1, v_r15 + 16);
    if ((unsigned int)((unsigned int)(v_stack_m9C)) != 0) goto loc_0030E77A;
loc_0030E530:
    v_r12 = 0;
loc_0030E533:
    if (((*(unsigned int *)(v_rip + 13338071)) & (0x1000ULL)) == 0) goto loc_0030E045;
    result = (unsigned int)((*(unsigned __int8 *)(v_r15 + 8)) & (63));
    a1 = (v_stack_m40) * (result);
    v_r15 = (v_r15) - (a1);
    result = EtwTraceAutoBoostProcessLockEntry(*(unsigned __int64 *)(v_r15 - 16), v_stack_m98, 136, v_r15 + 16);
    goto loc_0030E045;
loc_0030E570:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56)) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 - 16));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 - 16)) = v_r15;
    result = *(unsigned __int8 *)(*(unsigned __int64 *)(v_r15 - 16) - 808 + 792);
    v_r10 = v_stack_m80;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_r15 - 16) - 808 + 792)) != 0) {
        a4 = *(unsigned __int64 *)(v_stack_m28 + 56);
        v_stack_mA0 = v_stack_m80;
        a3 = v_stack_mB0;
        a2 = 4;
        a1 = *(unsigned __int64 *)(v_r15 - 16) - 808;
        result = KiAbProcessThreadLocks(a1, a2, a3, a4);
        v_r10 = v_stack_m80;
    }
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56)) == 0) goto loc_0030E0B3;
    goto loc_0030E570;
loc_0030E5C3:
    result = (result) ^ (a2);
loc_0030E5C6:
    if (result != 0) goto loc_0030E2B6;
    goto loc_0030E3C8;
loc_0030E5D4:
    result = (result) ^ (a2);
loc_0030E5D7:
    if (result != 0) goto loc_0030E3A6;
    goto loc_0030E4A9;
loc_0030E5E5:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 8) = 0x200001ULL;
    a2 = 0;
    result = memset(*(unsigned __int64 *)(v_stack_m28 + 72) + 16, a2, 256, a4);
    goto loc_0030E157;
loc_0030E603:
    v_stack_m98 = v_stack_mA0;
    v_stack_mA0 = 0;
    result = KiAbSetMinimumThreadPriority(v_r15, v_stack_mB8, v_stack_mB0, v_stack_m88);
    if ((unsigned int)(result) == 0) goto loc_0030E438;
    if (v_r15 == result) goto loc_0030E438;
    result = KiAbEntryUpdateOwnerTreePosition(v_r15, result, v_stack_mB0, v_stack_m88);
    v_rbx = (unsigned int)((*(unsigned __int64 *)(v_r15 - 16) - 808) | (32));
    goto loc_0030E438;
loc_0030E649:
    v_stack_m98 = v_stack_m9C;
    v_stack_mA0 = 0;
    result = KiAbSetMinimumThreadPriority(v_r15, v_stack_mB4, v_stack_mB0, *(unsigned __int64 *)(v_stack_m28 + 72));
    if ((unsigned int)(result) == 0) goto loc_0030E51A;
    if (v_r15 == result) goto loc_0030E51A;
    result = KiAbEntryUpdateOwnerTreePosition(v_r15, result, v_stack_mB0, *(unsigned __int64 *)(v_stack_m28 + 72));
    v_rbx = (unsigned int)((v_rbx) | (32));
    goto loc_0030E51A;
loc_0030E68E:
    goto loc_0030E451;
loc_0030E698:
    goto loc_0030E533;
loc_0030E6A2:
    result = (unsigned int)((*(unsigned __int8 *)(result + 8)) & (63));
    a1 = (v_r15) * (result);
    result = (result) - (a1);
    result = (unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(result - 16) + 195)));
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(result - 16) + 195))) > 30) { result = 30; }
    if (((unsigned __int8)(result)) <= ((unsigned __int8)(result))) goto loc_0030E418;
    v_stack_mB8 = (unsigned __int8)(result);
    goto loc_0030E418;
loc_0030E6DC:
    result = (unsigned int)((*(unsigned __int8 *)(result + 8)) & (63));
    a1 = (30) * (result);
    result = (result) - (a1);
    result = (unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(result - 16) + 195)));
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(result - 16) + 195))) > 30) { result = 30; }
    if (((unsigned __int8)(result)) <= ((unsigned __int8)(result))) goto loc_0030E4FA;
    v_stack_mB4 = (unsigned __int8)(result);
    goto loc_0030E4FA;
loc_0030E716:
    result = (unsigned int)((*(unsigned __int8 *)(v_r15 + 8)) & (63));
    a1 = (30) * (result);
    result = (v_r15) - (a1);
    result = ObReferenceObjectSafeWithTag(*(unsigned __int64 *)(result - 16), (unsigned int)(0x746C6644ULL), v_stack_mB0, *(unsigned __int64 *)(v_stack_m28 + 72));
    if ((unsigned __int8)(result) == 0) goto loc_0030E771;
    if (((0) & (1)) != 0) {
        a2 = 2;
        a3 = 0x80000000ULL;
        a1 = *(unsigned __int64 *)(result - 16);
        result = IoBoostThreadIoPriority(a1, a2, a3, *(unsigned __int64 *)(v_stack_m28 + 72));
    }
    if (((0) & (2)) != 0) {
        a1 = *(unsigned __int64 *)(result - 16);
        result = PsBoostThreadOutstandingIoQoS(a1, a2, a3, *(unsigned __int64 *)(v_stack_m28 + 72));
    }
    result = ObDereferenceObjectDeferDeleteWithTag(*(unsigned __int64 *)(result - 16), (unsigned int)(0x746C6644ULL), a3, *(unsigned __int64 *)(v_stack_m28 + 72));
loc_0030E771:
    goto loc_0030E44E;
loc_0030E77A:
    result = (unsigned int)((*(unsigned __int8 *)(v_r15 + 8)) & (63));
    a1 = (*(unsigned __int64 *)(result - 16)) * (result);
    result = (v_r15) - (a1);
    result = ObReferenceObjectSafeWithTag(*(unsigned __int64 *)(result - 16), (unsigned int)(0x746C6644ULL), a3, *(unsigned __int64 *)(v_stack_m28 + 72));
    if ((unsigned __int8)(result) == 0) goto loc_0030E530;
    if (((0) & (1)) != 0) {
        a2 = 2;
        a3 = 0x80000000ULL;
        a1 = *(unsigned __int64 *)(result - 16);
        result = IoBoostThreadIoPriority(a1, a2, a3, *(unsigned __int64 *)(v_stack_m28 + 72));
    }
    if (((0) & (2)) != 0) {
        a1 = *(unsigned __int64 *)(result - 16);
        result = PsBoostThreadOutstandingIoQoS(a1, a2, a3, *(unsigned __int64 *)(v_stack_m28 + 72));
    }
    result = ObDereferenceObjectDeferDeleteWithTag(*(unsigned __int64 *)(result - 16), (unsigned int)(0x746C6644ULL), a3, *(unsigned __int64 *)(v_stack_m28 + 72));
    goto loc_0030E530;
loc_0030E7DE:
    if ((unsigned int)(0x746C6644ULL) == 0) goto loc_0030E812;
    a2 = ((unsigned int)(0x746C6644ULL)) ^ (0);
    goto loc_0030E27B;
loc_0030E7EB:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(result - 16) + 40) == 0) goto loc_0030E81A;
    result = (*(unsigned __int64 *)(result - 16) + 40) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(result - 16) + 40));
    goto loc_0030E36E;
loc_0030E800:
    goto loc_0030E40D;
loc_0030E809:
    goto loc_0030E4EF;
loc_0030E812:
    a3 = 0;
    goto loc_0030E3CB;
loc_0030E81A:
    a3 = 0;
    goto loc_0030E4AC;
loc_0030E822:
    goto loc_0030E135;
}
```

## 5. (Beta) C Style

```c
int64_t KiAbDeferredProcessingWorker(int64_t Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m64;
    uint32_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint32_t v_stack_m98;
    uint32_t v_stack_m9C;
    uint32_t v_stack_mA0;
    uint32_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint8_t v_stack_mB2;
    uint8_t v_stack_mB3;
    uint32_t v_stack_mB4;
    uint8_t v_stack_mB6;
    uint8_t v_stack_mB7;
    uint32_t v_stack_mB8;
    uint32_t v_stack_mC0;
    uint32_t v_stack_mE8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p20 = local_rdi;
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (192);
    local_r12 = 0;
    v_stack_mB0 = 0;
    v_stack_m88 = Arg3 + 37240;
    v_stack_m80 = Arg3 + 37232;
loc_0030DF0F:
    v_stack_m90 = *(uint64_t *)(arg3 + 0x9170);
    if (*(uint64_t *)(arg3 + 0x9170) == 0) goto loc_0030E0A7;
loc_0030DF1F:
    *(uint64_t *)(arg3 + 0x9170) = *(uint64_t *)(*(uint64_t *)(arg3 + 0x9170));
    *(uint64_t *)(*(uint64_t *)(arg3 + 0x9170)) = local_r12 + 1;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg3 + 0x9170) - 0x17)) == 0) goto loc_0030E074;
    if (*(uint64_t *)(*(uint64_t *)(arg3 + 0x9170) + 0x148) == 0) goto loc_0030E3AB;
    Arg3 = (local_r12 + 1) << ((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg3 + 0x9170) + 0x148) + 0xC)));
    Arg3 = (uint32_t)((Arg3) - 1);
    Arg2 = (uint32_t)((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg3 + 0x9170) + 0x148) + 0xA)) | ((uint32_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg3 + 0x9170) + 0x148) + 0x8))));
    a4 = (((uint32_t)(Arg3)) == ((uint32_t)(Arg2))) ? 1 : 0;
loc_0030DF6A:
    Arg3 = (local_r12 + 1) << ((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg3 + 0x9170) + 0x140) + 0xC)));
    Arg3 = (uint32_t)((Arg3) - 1);
    Arg1 = (uint32_t)((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg3 + 0x9170) + 0x140) + 0xA)) | ((uint32_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg3 + 0x9170) + 0x140) + 0x8))));
    if (((uint32_t)(Arg3)) == ((uint32_t)(Arg1))) goto loc_0030E06B;
loc_0030DF91:
    v_stack_m78 = *(uint64_t *)(*(uint64_t *)(arg3 + 0x9170) + 0x140);
    result = (uint32_t)((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg3 + 0x9170) + 0x140) + 0xA)) | ((uint32_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg3 + 0x9170) + 0x140) + 0x8))));
    local_rsi = (local_r12 + 1) << ((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg3 + 0x9170) + 0x140) + 0xC)));
    local_rsi = (uint32_t)((local_rsi) - 1);
    local_rsi = (uint32_t)((local_rsi) ^ ((uint32_t)(result)));
    v_stack_mA8 = (uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg3 + 0x9170) + 0x140) + 0xC));
    if (condition_is_equal) goto loc_0030DFF4;
loc_0030DFC0:
    local_rsi = (uint32_t)((local_rsi) & ((uint32_t)(local_rsi - 1)));
    local_r15 = (local_r12 + 1) * ((uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg3 + 0x9170) + 0x140) + 0xC))));
    local_r15 = (local_r15) + (16);
    local_r15 = (local_r15) + (v_stack_m78);
    if (*(uint64_t *)(local_r15) != 0) goto loc_0030E1C5;
loc_0030DFDE:
    v_stack_mA8 = (uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg3 + 0x9170) + 0x140) + 0xC));
    if (*(uint64_t *)(local_r15) != 0) goto loc_0030DFC0;
loc_0030DFF4:
    if (*(uint64_t *)(v_stack_m90 + 0x148) == 0) goto loc_0030E074;
    result = (uint32_t)((*(uint16_t *)(*(uint64_t *)(v_stack_m90 + 0x148) + 0xA)) | ((uint32_t)(*(uint16_t *)(*(uint64_t *)(v_stack_m90 + 0x148) + 0x8))));
    local_rsi = (1) << ((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_stack_m90 + 0x148) + 0xC)));
    local_rsi = (uint32_t)((local_rsi) - 1);
    local_rsi = (uint32_t)((local_rsi) ^ ((uint32_t)(result)));
    v_stack_m98 = (uint32_t)(*(uint8_t *)(*(uint64_t *)(v_stack_m90 + 0x148) + 0xC));
    if (condition_is_equal) goto loc_0030E074;
loc_0030E027:
    local_rsi = (uint32_t)((local_rsi) & ((uint32_t)(local_rsi - 1)));
    local_r15 = (1) * ((uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(v_stack_m90 + 0x148) + 0xC))));
    local_r15 = (local_r15) + (16);
    local_r15 = (local_r15) + (*(uint64_t *)(v_stack_m90 + 0x148));
    if (*(uint64_t *)(local_r15) != 0) goto loc_0030E2BB;
loc_0030E045:
    v_stack_m98 = (uint32_t)(*(uint8_t *)(*(uint64_t *)(v_stack_m90 + 0x148) + 0xC));
    if (*(uint64_t *)(local_r15) != 0) goto loc_0030E027;
    goto loc_0030E074;
loc_0030E06B:
    if ((uint32_t)(a4) == 0) goto loc_0030DF91;
loc_0030E074:
    v_stack_m90 = *(uint64_t *)(v_stack_m80);
    if (*(uint64_t *)(v_stack_m80) != 0) goto loc_0030DF1F;
loc_0030E0A7:
    if (*(uint64_t *)(v_stack_m88) != 0) goto loc_0030E570;
loc_0030E0B3:
    if ((*(uint64_t *)(v_stack_m80)) != 0) goto loc_0030DF0F;
    *(uint64_t *)(v_stack_p18 + 0x91A0) = 0;
    if (v_stack_mB0 == 0) goto loc_0030E822;
    v_stack_mB0 = *(uint64_t *)(v_stack_mB0);
loc_0030E0F3:
    a4 = 0;
    result = KiDeferredReadySingleThread(v_stack_p18, v_stack_mB0 - 216, v_stack_mB0, a4);
    local_rsi = (uint32_t)((0) + 1);
    if (v_stack_mB0 != 0) {
        result = *(uint64_t *)(v_stack_mB0);
        v_stack_mB0 = result;
    }
    if ((((uint8_t)(local_rsi)) & (15)) == 0) {
        Arg1 = v_stack_p18 + 13784;
        result = KiFlushSoftwareInterruptBatch(Arg1, v_stack_mB0 - 216, v_stack_mB0, a4);
    }
    if (v_stack_mB0 != 0) goto loc_0030E0F3;
loc_0030E135:
    if ((uint8_t)(*(uint8_t *)(v_stack_p18 + 0x35D8 + 0x1)) == 0) goto loc_0030E162;
    if (((uint8_t)(*(uint8_t *)(v_stack_p18 + 0x35D8 + 0x1))) == 1) goto loc_0030E184;
    result = KiSendSoftwareInterruptAffinity(v_stack_p18 + 13784 + 8, *(uint8_t *)(v_stack_p18 + 0x35D8), v_stack_mB0, a4);
loc_0030E14D:
    if ((*(uint8_t *)(v_stack_p18 + 0x35D8 + 0x1)) == 2) goto loc_0030E5E5;
loc_0030E157:
    *(uint8_t *)(v_stack_p18 + 0x35D8 + 0x1) = 0;
    *(uint32_t *)(v_stack_p18 + 0x35D8 + 0x4) = 0xFFFFULL;
loc_0030E162:
    return result;
loc_0030E184:
    v_stack_m68 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x4)));
    v_stack_m70 = 6;
    v_stack_m64 = 0;
    Arg2 = 31;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x48)))) != 1) { Arg2 = 47; }
    result = HalpInterruptSendIpi(v_stack_m70, Arg2, *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x48)), a4);
    goto loc_0030E14D;
loc_0030E1C5:
    if ((((uint8_t)(result)) & (2)) != 0) goto loc_0030DFDE;
    if (!sign_flag) goto loc_0030DFDE;
    if ((*(uint8_t *)(1 + 0x9)) != 0) goto loc_0030DFDE;
    result = 0;
    local_r13 = (*(uint64_t *)(1)) & (*(uint64_t *)(v_stack_m28 + 0x30));
    v_stack_m48 = 0;
    v_stack_mA8 = local_r13;
    v_stack_m58 = v_xmm0;
    v_stack_mA0 = 0;
    if (condition_is_equal) goto loc_0030E20B;
    if ((*(uint8_t *)(1 + 0x8)) >= 0) {
        local_r13 = (local_r13) | (v_stack_m28);
        v_stack_mA8 = local_r13;
    }
    Arg2 = 0;
    result = KiAbEntryGetLockedHeadEntry(1, Arg2, v_stack_m58, a4);
    if (result == 0) goto loc_0030E68E;
    if ((*(uint8_t *)(1 + 0x9)) != 0) goto loc_0030E433;
    if (1 == result) goto loc_0030E3DD;
    result = KiAbOwnerComputeCpuPriorityKey(1, Arg2, v_stack_m58, a4);
    if ((*(uint8_t *)(1 + 0x28)) == ((uint8_t)(result))) goto loc_0030E3DA;
    *(uint8_t *)(1 + 0x28) = (uint8_t)(result);
    result = RtlRbRemoveNode(result + 40, 1 + 16, v_stack_m58, a4);
    if ((((uint8_t)(*(uint64_t *)(result + 0x28 + 0x8))) & (1)) != 0) goto loc_0030E7DE;
loc_0030E27B:
    Arg1 = (uint32_t)((*(uint64_t *)(result + 0x28 + 0x8)) & (1));
    Arg3 = 0;
    if (*(uint64_t *)(result + 0x28) == 0) goto loc_0030E3CB;
loc_0030E290:
    if ((*(uint8_t *)(*(uint64_t *)(result + 0x28) + 0x18)) <= ((uint8_t)(*(uint8_t *)(1 + 0x28)))) goto loc_0030E3B3;
    if ((uint32_t)(Arg1) == 0) goto loc_0030E2AD;
    if (*(uint64_t *)(*(uint64_t *)(result + 0x28)) == 0) goto loc_0030E3CB;
    result = (*(uint64_t *)(*(uint64_t *)(result + 0x28))) ^ (*(uint64_t *)(result + 0x28));
loc_0030E2AD:
    if (result == 0) goto loc_0030E3CB;
loc_0030E2B6:
    goto loc_0030E290;
loc_0030E2BB:
    if ((((uint8_t)(result)) & (2)) != 0) goto loc_0030E045;
    if (!sign_flag) goto loc_0030E045;
    if ((*(uint8_t *)(1 + 0x9)) != 0) goto loc_0030E045;
    result = 0;
    v_stack_m9C = (uint32_t)(result + 40);
    v_stack_m30 = 0;
    result = (*(uint64_t *)(1)) & (128);
    v_stack_m98 = result;
    v_stack_m40 = v_xmm0;
    if (condition_is_equal) goto loc_0030E302;
    if ((*(uint8_t *)(1 + 0x8)) >= 0) {
        result = (result) | (v_stack_m28);
        v_stack_m98 = result;
    }
    Arg2 = 0;
    result = KiAbEntryGetLockedHeadEntry(1, Arg2, v_stack_m40, *(uint8_t *)(1 + 0x28));
    if (result == 0) goto loc_0030E698;
    if ((*(uint8_t *)(1 + 0x9)) != 0) goto loc_0030E515;
    if (1 == result) goto loc_0030E4BF;
    result = KiAbOwnerComputeCpuPriorityKey(1, Arg2, v_stack_m40, *(uint8_t *)(1 + 0x28));
    if ((*(uint8_t *)(1 + 0x28)) == ((uint8_t)(result))) goto loc_0030E4BC;
    *(uint8_t *)(1 + 0x28) = (uint8_t)(result);
    result = RtlRbRemoveNode(result + 40, 1 + 16, v_stack_m40, *(uint8_t *)(1 + 0x28));
    if ((((uint8_t)(*(uint64_t *)(result + 0x30))) & (1)) != 0) goto loc_0030E7EB;
loc_0030E36E:
    Arg1 = (uint32_t)((*(uint64_t *)(result + 0x30)) & (1));
    Arg3 = 0;
    if (*(uint64_t *)(result + 0x28) == 0) goto loc_0030E4AC;
loc_0030E380:
    if ((*(uint8_t *)(*(uint64_t *)(result + 0x28) + 0x18)) <= ((uint8_t)(*(uint8_t *)(1 + 0x28)))) goto loc_0030E494;
    if ((uint32_t)(Arg1) == 0) goto loc_0030E39D;
    if (*(uint64_t *)(*(uint64_t *)(result + 0x28)) == 0) goto loc_0030E4AC;
    result = (*(uint64_t *)(*(uint64_t *)(result + 0x28))) ^ (*(uint64_t *)(result + 0x28));
loc_0030E39D:
    if (result == 0) goto loc_0030E4AC;
loc_0030E3A6:
    goto loc_0030E380;
loc_0030E3AB:
    goto loc_0030DF6A;
loc_0030E3B3:
    if ((uint32_t)(Arg1) == 0) goto loc_0030E5C6;
    if (*(uint64_t *)(result + 0x8) != 0) goto loc_0030E5C3;
loc_0030E3C8:
loc_0030E3CB:
    result = RtlRbInsertNodeEx(result + 40, result, 1, 1 + 16);
    local_r12 = 0;
loc_0030E3DA:
    local_rbx = (uint32_t)((128) | (16));
loc_0030E3DD:
    v_stack_mB8 = 0;
    if ((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x54))) != 0) {
        v_stack_mB7 = 2;
    }
    if (!(condition_is_below_or_equal)) {
        v_stack_mB6 = 1;
    }
    if (*(uint64_t *)(result + 0x40) == 0) goto loc_0030E800;
    v_stack_mB8 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(result + 0x40) + 0x18));
loc_0030E40D:
    if ((*(uint8_t *)(result + 0x9)) != 0) goto loc_0030E6A2;
loc_0030E418:
    if (v_stack_mB8 != 0) goto loc_0030E603;
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(v_stack_m58, *(uint8_t *)(*(uint64_t *)(result + 0x40) + 0x18), 1, 1 + 16);
    local_rbx = (uint32_t)((local_rbx) & (0xFFFFFFF9ULL));
    local_rbx = (uint32_t)((local_rbx) | (1));
    goto loc_0030E451;
loc_0030E433:
loc_0030E438:
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(v_stack_m58, *(uint8_t *)(*(uint64_t *)(result + 0x40) + 0x18), 1, 1 + 16);
    if ((uint32_t)((uint32_t)(v_stack_mA0)) != 0) goto loc_0030E716;
loc_0030E44E:
    local_r12 = 0;
loc_0030E451:
    local_r15 = 1;
    if (((*(uint32_t *)(v_rip + 0xCB86B9)) & (0x1000ULL)) != 0) {
        result = *(uint8_t *)(1 + 0x8);
        Arg3 = 136;
        result = (uint32_t)((result) & (63));
        Arg2 = result;
        Arg1 = (v_stack_m58) * (result);
        local_r15 = (1) - (Arg1);
        Arg1 = *(uint64_t *)(local_r15 - 0x10);
        result = EtwTraceAutoBoostProcessLockEntry(Arg1, Arg2, Arg3, 1 + 16);
    }
    goto loc_0030DFDE;
loc_0030E494:
    if ((uint32_t)(Arg1) == 0) goto loc_0030E5D7;
    if (*(uint64_t *)(Arg2 + 0x8) != 0) goto loc_0030E5D4;
loc_0030E4A9:
loc_0030E4AC:
    result = RtlRbInsertNodeEx(result + 40, Arg2, 1, local_r15 + 16);
    local_r12 = 0;
loc_0030E4BC:
    local_rbx = (uint32_t)((136) | (16));
loc_0030E4BF:
    v_stack_mB4 = 0;
    if ((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x54))) != 0) {
        v_stack_mB3 = 2;
    }
    if (!(condition_is_below_or_equal)) {
        v_stack_mB2 = 1;
    }
    if (*(uint64_t *)(result + 0x40) == 0) goto loc_0030E809;
    v_stack_mB4 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(result + 0x40) + 0x18));
loc_0030E4EF:
    if ((*(uint8_t *)(result + 0x9)) != 0) goto loc_0030E6DC;
loc_0030E4FA:
    if (v_stack_mB4 != 0) goto loc_0030E649;
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(v_stack_m40, *(uint8_t *)(*(uint64_t *)(result + 0x40) + 0x18), 1, local_r15 + 16);
    local_rbx = (uint32_t)((local_rbx) & (0xFFFFFFF9ULL));
    local_rbx = (uint32_t)((local_rbx) | (1));
    goto loc_0030E533;
loc_0030E515:
loc_0030E51A:
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(v_stack_m40, *(uint8_t *)(*(uint64_t *)(result + 0x40) + 0x18), 1, local_r15 + 16);
    if ((uint32_t)((uint32_t)(v_stack_m9C)) != 0) goto loc_0030E77A;
loc_0030E530:
    local_r12 = 0;
loc_0030E533:
    if (((*(uint32_t *)(v_rip + 0xCB85D7)) & (0x1000ULL)) == 0) goto loc_0030E045;
    result = (uint32_t)((*(uint8_t *)(local_r15 + 0x8)) & (63));
    Arg1 = (v_stack_m40) * (result);
    local_r15 = (local_r15) - (Arg1);
    result = EtwTraceAutoBoostProcessLockEntry(*(uint64_t *)(local_r15 - 0x10), v_stack_m98, 136, local_r15 + 16);
    goto loc_0030E045;
loc_0030E570:
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38)) = *(uint64_t *)(*(uint64_t *)(local_r15 - 0x10));
    *(uint64_t *)(*(uint64_t *)(local_r15 - 0x10)) = local_r15;
    result = *(uint8_t *)(*(uint64_t *)(local_r15 - 0x10) - 0x328 + 0x318);
    local_r10 = v_stack_m80;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(local_r15 - 0x10) - 0x328 + 0x318)) != 0) {
        a4 = *(uint64_t *)(v_stack_m28 + 0x38);
        v_stack_mA0 = v_stack_m80;
        Arg3 = v_stack_mB0;
        Arg2 = 4;
        Arg1 = *(uint64_t *)(local_r15 - 0x10) - 808;
        result = KiAbProcessThreadLocks(Arg1, Arg2, Arg3, a4);
        local_r10 = v_stack_m80;
    }
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38)) == 0) goto loc_0030E0B3;
    goto loc_0030E570;
loc_0030E5C3:
    result = (result) ^ (Arg2);
loc_0030E5C6:
    if (result != 0) goto loc_0030E2B6;
    goto loc_0030E3C8;
loc_0030E5D4:
    result = (result) ^ (Arg2);
loc_0030E5D7:
    if (result != 0) goto loc_0030E3A6;
    goto loc_0030E4A9;
loc_0030E5E5:
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x8) = 0x200001ULL;
    Arg2 = 0;
    result = memset(*(uint64_t *)(v_stack_m28 + 0x48) + 16, Arg2, 256, a4);
    goto loc_0030E157;
loc_0030E603:
    v_stack_m98 = v_stack_mA0;
    v_stack_mA0 = 0;
    result = KiAbSetMinimumThreadPriority(local_r15, v_stack_mB8, v_stack_mB0, v_stack_m88);
    if ((uint32_t)(result) == 0) goto loc_0030E438;
    if (local_r15 == result) goto loc_0030E438;
    result = KiAbEntryUpdateOwnerTreePosition(local_r15, result, v_stack_mB0, v_stack_m88);
    local_rbx = (uint32_t)((*(uint64_t *)(local_r15 - 0x10) - 808) | (32));
    goto loc_0030E438;
loc_0030E649:
    v_stack_m98 = v_stack_m9C;
    v_stack_mA0 = 0;
    result = KiAbSetMinimumThreadPriority(local_r15, v_stack_mB4, v_stack_mB0, *(uint64_t *)(v_stack_m28 + 0x48));
    if ((uint32_t)(result) == 0) goto loc_0030E51A;
    if (local_r15 == result) goto loc_0030E51A;
    result = KiAbEntryUpdateOwnerTreePosition(local_r15, result, v_stack_mB0, *(uint64_t *)(v_stack_m28 + 0x48));
    local_rbx = (uint32_t)((local_rbx) | (32));
    goto loc_0030E51A;
loc_0030E68E:
    goto loc_0030E451;
loc_0030E698:
    goto loc_0030E533;
loc_0030E6A2:
    result = (uint32_t)((*(uint8_t *)(result + 0x8)) & (63));
    Arg1 = (local_r15) * (result);
    result = (result) - (Arg1);
    result = (uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(result - 0x10) + 0xC3)));
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(result - 0x10) + 0xC3))) > 30) { result = 30; }
    if (((uint8_t)(result)) <= ((uint8_t)(result))) goto loc_0030E418;
    v_stack_mB8 = (uint8_t)(result);
    goto loc_0030E418;
loc_0030E6DC:
    result = (uint32_t)((*(uint8_t *)(result + 0x8)) & (63));
    Arg1 = (30) * (result);
    result = (result) - (Arg1);
    result = (uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(result - 0x10) + 0xC3)));
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(result - 0x10) + 0xC3))) > 30) { result = 30; }
    if (((uint8_t)(result)) <= ((uint8_t)(result))) goto loc_0030E4FA;
    v_stack_mB4 = (uint8_t)(result);
    goto loc_0030E4FA;
loc_0030E716:
    result = (uint32_t)((*(uint8_t *)(local_r15 + 0x8)) & (63));
    Arg1 = (30) * (result);
    result = (local_r15) - (Arg1);
    result = ObReferenceObjectSafeWithTag(*(uint64_t *)(result - 0x10), (uint32_t)(0x746C6644ULL), v_stack_mB0, *(uint64_t *)(v_stack_m28 + 0x48));
    if ((uint8_t)(result) == 0) goto loc_0030E771;
    if (((0) & (1)) != 0) {
        Arg2 = 2;
        Arg3 = 0x80000000ULL;
        Arg1 = *(uint64_t *)(result - 0x10);
        result = IoBoostThreadIoPriority(Arg1, Arg2, Arg3, *(uint64_t *)(v_stack_m28 + 0x48));
    }
    if (((0) & (2)) != 0) {
        Arg1 = *(uint64_t *)(result - 0x10);
        result = PsBoostThreadOutstandingIoQoS(Arg1, Arg2, Arg3, *(uint64_t *)(v_stack_m28 + 0x48));
    }
    result = ObDereferenceObjectDeferDeleteWithTag(*(uint64_t *)(result - 0x10), (uint32_t)(0x746C6644ULL), Arg3, *(uint64_t *)(v_stack_m28 + 0x48));
loc_0030E771:
    goto loc_0030E44E;
loc_0030E77A:
    result = (uint32_t)((*(uint8_t *)(local_r15 + 0x8)) & (63));
    Arg1 = (*(uint64_t *)(result - 0x10)) * (result);
    result = (local_r15) - (Arg1);
    result = ObReferenceObjectSafeWithTag(*(uint64_t *)(result - 0x10), (uint32_t)(0x746C6644ULL), Arg3, *(uint64_t *)(v_stack_m28 + 0x48));
    if ((uint8_t)(result) == 0) goto loc_0030E530;
    if (((0) & (1)) != 0) {
        Arg2 = 2;
        Arg3 = 0x80000000ULL;
        Arg1 = *(uint64_t *)(result - 0x10);
        result = IoBoostThreadIoPriority(Arg1, Arg2, Arg3, *(uint64_t *)(v_stack_m28 + 0x48));
    }
    if (((0) & (2)) != 0) {
        Arg1 = *(uint64_t *)(result - 0x10);
        result = PsBoostThreadOutstandingIoQoS(Arg1, Arg2, Arg3, *(uint64_t *)(v_stack_m28 + 0x48));
    }
    result = ObDereferenceObjectDeferDeleteWithTag(*(uint64_t *)(result - 0x10), (uint32_t)(0x746C6644ULL), Arg3, *(uint64_t *)(v_stack_m28 + 0x48));
    goto loc_0030E530;
loc_0030E7DE:
    if ((uint32_t)(0x746C6644ULL) == 0) goto loc_0030E812;
    Arg2 = ((uint32_t)(0x746C6644ULL)) ^ (0);
    goto loc_0030E27B;
loc_0030E7EB:
    if (*(uint64_t *)(*(uint64_t *)(result - 0x10) + 0x28) == 0) goto loc_0030E81A;
    result = (*(uint64_t *)(result - 0x10) + 40) ^ (*(uint64_t *)(*(uint64_t *)(result - 0x10) + 0x28));
    goto loc_0030E36E;
loc_0030E800:
    goto loc_0030E40D;
loc_0030E809:
    goto loc_0030E4EF;
loc_0030E812:
    Arg3 = 0;
    goto loc_0030E3CB;
loc_0030E81A:
    Arg3 = 0;
    goto loc_0030E4AC;
loc_0030E822:
    goto loc_0030E135;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x9170` | `64` | `R` |
| `Arg3` | `+ 0x9178` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0030DEB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
