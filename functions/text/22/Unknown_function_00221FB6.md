# sub_00221FB6

- RVA: `0x00221FB6`–`0x00222DBC` (길이 `3,590` bytes)
- VA: `0x0000000140221FB6`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005F6C0`
- 디코드: `891`개 명령, `3,590/3,590` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **47**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00221FD1` → [KiAbOwnerComputeCpuPriorityKey](../21/KiAbOwnerComputeCpuPriorityKey_function_0021F090.md) (function, `0x0021F090`)
- `0x00222021` → [KiAbEntryGetLockedHeadEntry](KiAbEntryGetLockedHeadEntry_function_002213C0.md) (function, `0x002213C0`)
- `0x002220C2` → [RtlRbRemoveNode](../2E/RtlRbRemoveNode_function_002E4C10.md) (function, `0x002E4C10`)
- `0x00222134` → [KiAbOwnerComputeCpuPriorityKey](../21/KiAbOwnerComputeCpuPriorityKey_function_0021F090.md) (function, `0x0021F090`)
- `0x00222182` → [KiAbEntryGetLockedHeadEntry](KiAbEntryGetLockedHeadEntry_function_002213C0.md) (function, `0x002213C0`)
- `0x00222219` → [RtlRbRemoveNode](../2E/RtlRbRemoveNode_function_002E4C10.md) (function, `0x002E4C10`)
- `0x00222292` → [RtlRbInsertNodeEx](../2E/RtlRbInsertNodeEx_function_002E4570.md) (function, `0x002E4570`)
- `0x002222E3` → [KeReleaseInStackQueuedSpinLockFromDpcLevel](../21/KeReleaseInStackQueuedSpinLockFromDpcLevel_function_002171B0.md) (function, `0x002171B0`)
- `0x00222310` → [RtlRbInsertNodeEx](../2E/RtlRbInsertNodeEx_function_002E4570.md) (function, `0x002E4570`)
- `0x00222360` → [KeReleaseInStackQueuedSpinLockFromDpcLevel](../21/KeReleaseInStackQueuedSpinLockFromDpcLevel_function_002171B0.md) (function, `0x002171B0`)
- `0x00222389` → [KiAbIoBoostOwners](../21/KiAbIoBoostOwners_function_0021FCB0.md) (function, `0x0021FCB0`)
- `0x002223A6` → [KiAbCpuBoostOwners](KiAbCpuBoostOwners_function_00220680.md) (function, `0x00220680`)
- `0x002223AF` → [KeReleaseInStackQueuedSpinLockFromDpcLevel](../21/KeReleaseInStackQueuedSpinLockFromDpcLevel_function_002171B0.md) (function, `0x002171B0`)
- `0x002223ED` → [EtwTraceAutoBoostProcessLockEntry](EtwTraceAutoBoostProcessLockEntry_function_00221C7C.md) (function, `0x00221C7C`)
- `0x00222437` → [KiAbIoBoostOwners](../21/KiAbIoBoostOwners_function_0021FCB0.md) (function, `0x0021FCB0`)
- `0x00222454` → [KiAbCpuBoostOwners](KiAbCpuBoostOwners_function_00220680.md) (function, `0x00220680`)
- `0x0022245D` → [KeReleaseInStackQueuedSpinLockFromDpcLevel](../21/KeReleaseInStackQueuedSpinLockFromDpcLevel_function_002171B0.md) (function, `0x002171B0`)
- `0x00222495` → [EtwTraceAutoBoostProcessLockEntry](EtwTraceAutoBoostProcessLockEntry_function_00221C7C.md) (function, `0x00221C7C`)
- `0x00222508` → [RtlRbRemoveNode](../2E/RtlRbRemoveNode_function_002E4C10.md) (function, `0x002E4C10`)
- `0x00222572` → [RtlRbInsertNodeEx](../2E/RtlRbInsertNodeEx_function_002E4570.md) (function, `0x002E4570`)
- `0x002225DA` → [PsGetIoPriorityThread](../34/PsGetIoPriorityThread_function_00343930.md) (function, `0x00343930`)
- `0x00222664` → [KiAbEntryGetCpuPriorityKey](KiAbEntryGetCpuPriorityKey_function_00222DD0.md) (function, `0x00222DD0`)
- `0x00222683` → [KeReleaseInStackQueuedSpinLockFromDpcLevel](../21/KeReleaseInStackQueuedSpinLockFromDpcLevel_function_002171B0.md) (function, `0x002171B0`)
- `0x002226E4` → [RtlRbRemoveNode](../2E/RtlRbRemoveNode_function_002E4C10.md) (function, `0x002E4C10`)
- `0x00222754` → [RtlRbInsertNodeEx](../2E/RtlRbInsertNodeEx_function_002E4570.md) (function, `0x002E4570`)
- `0x002227E1` → [KiAbSetMinimumThreadPriority](../21/KiAbSetMinimumThreadPriority_function_0021F190.md) (function, `0x0021F190`)
- `0x002227FA` → [KiAbOwnerComputeCpuPriorityKey](../21/KiAbOwnerComputeCpuPriorityKey_function_0021F090.md) (function, `0x0021F090`)
- `0x0022281B` → [RtlRbRemoveNode](../2E/RtlRbRemoveNode_function_002E4C10.md) (function, `0x002E4C10`)
- `0x0022289C` → [KiAbSetMinimumThreadPriority](../21/KiAbSetMinimumThreadPriority_function_0021F190.md) (function, `0x0021F190`)
- `0x002228B5` → [KiAbOwnerComputeCpuPriorityKey](../21/KiAbOwnerComputeCpuPriorityKey_function_0021F090.md) (function, `0x0021F090`)
- `0x002228D4` → [RtlRbRemoveNode](../2E/RtlRbRemoveNode_function_002E4C10.md) (function, `0x002E4C10`)
- `0x00222976` → [KiAbEntryGetCpuPriorityKey](KiAbEntryGetCpuPriorityKey_function_00222DD0.md) (function, `0x00222DD0`)
- `0x00222995` → [KeReleaseInStackQueuedSpinLockFromDpcLevel](../21/KeReleaseInStackQueuedSpinLockFromDpcLevel_function_002171B0.md) (function, `0x002171B0`)
- `0x002229C3` → [RtlRbInsertNodeEx](../2E/RtlRbInsertNodeEx_function_002E4570.md) (function, `0x002E4570`)
- `0x002229F0` → [RtlRbInsertNodeEx](../2E/RtlRbInsertNodeEx_function_002E4570.md) (function, `0x002E4570`)
- `0x00222A00` → [KiAbOwnerComputeCpuPriorityKey](../21/KiAbOwnerComputeCpuPriorityKey_function_0021F090.md) (function, `0x0021F090`)
- `0x00222A21` → [KiAbOwnerComputeCpuPriorityKey](../21/KiAbOwnerComputeCpuPriorityKey_function_0021F090.md) (function, `0x0021F090`)
- `0x00222A96` → [PsGetIoPriorityThread](../34/PsGetIoPriorityThread_function_00343930.md) (function, `0x00343930`)
- `0x00222C69` → [ObReferenceObjectSafeWithTag](../21/ObReferenceObjectSafeWithTag_function_00210EE0.md) (function, `0x00210EE0`)
- `0x00222C8A` → [IoBoostThreadIoPriority](../21/IoBoostThreadIoPriority_function_00216110.md) (function, `0x00216110`)
- `0x00222C98` → [PsBoostThreadOutstandingIoQoS](../21/PsBoostThreadOutstandingIoQoS_function_00215C54.md) (function, `0x00215C54`)
- `0x00222CA5` → [ObDereferenceObjectDeferDeleteWithTag](../26/ObDereferenceObjectDeferDeleteWithTag_function_00263EA0.md) (function, `0x00263EA0`)
- `0x00222CCD` → [ObReferenceObjectSafeWithTag](../21/ObReferenceObjectSafeWithTag_function_00210EE0.md) (function, `0x00210EE0`)
- `0x00222CEE` → [IoBoostThreadIoPriority](../21/IoBoostThreadIoPriority_function_00216110.md) (function, `0x00216110`)
- `0x00222CFC` → [PsBoostThreadOutstandingIoQoS](../21/PsBoostThreadOutstandingIoQoS_function_00215C54.md) (function, `0x00215C54`)
- `0x00222D09` → [ObDereferenceObjectDeferDeleteWithTag](../26/ObDereferenceObjectDeferDeleteWithTag_function_00263EA0.md) (function, `0x00263EA0`)
- `0x00222DAF` → [RtlRbInsertNodeEx](../2E/RtlRbInsertNodeEx_function_002E4570.md) (function, `0x002E4570`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x002223C5` → RVA `0x00FC6B14` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **8**
  - `0x00221FBC` → [sub_00221DC6 + 0xB8](Unknown_function_00221DC6.md) (`tail-transfer`)
  - `0x00222120` → [sub_00221DC6 + 0x154](Unknown_function_00221DC6.md) (`tail-transfer`)
  - `0x00222416` → [sub_00221DC6 + 0xB8](Unknown_function_00221DC6.md) (`tail-transfer`)
  - `0x002224A9` → [sub_00221DC6 + 0x154](Unknown_function_00221DC6.md) (`tail-transfer`)
  - `0x00222BA3` → [sub_00221DC6 + 0xB8](Unknown_function_00221DC6.md) (`tail-transfer`)
  - `0x00222BB1` → [sub_00221DC6 + 0x154](Unknown_function_00221DC6.md) (`tail-transfer`)
  - `0x00222BE7` → [sub_00221DC6 + 0xB8](Unknown_function_00221DC6.md) (`tail-transfer`)
  - `0x00222C1B` → [sub_00221DC6 + 0x154](Unknown_function_00221DC6.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00221FB6  41 F6 44 24 0B 01               test byte ptr [r12 + 0xb], 1
00221FBC  0F 85 BC FE FF FF               jne 0x140221e7e
00221FC2  41 80 7C 24 09 00               cmp byte ptr [r12 + 9], 0
00221FC8  0F 85 EE 0B 00 00               jne 0x140222bbc
00221FCE  49 8B CC                        mov rcx, r12
00221FD1  E8 BA D0 FF FF                  call 0x14021f090
00221FD6  41 3A 44 24 28                  cmp al, byte ptr [r12 + 0x28]
00221FDB  0F 84 2E 04 00 00               je 0x14022240f
00221FE1  33 C0                           xor eax, eax
00221FE3  8B DF                           mov ebx, edi
00221FE5  83 E3 07                        and ebx, 7
00221FE8  48 89 45 F7                     mov qword ptr [rbp - 9], rax
00221FEC  89 45 9F                        mov dword ptr [rbp - 0x61], eax
00221FEF  0F 57 C0                        xorps xmm0, xmm0
00221FF2  89 45 BF                        mov dword ptr [rbp - 0x41], eax
00221FF5  49 8B 04 24                     mov rax, qword ptr [r12]
00221FF9  C1 E3 06                        shl ebx, 6
00221FFC  49 23 C3                        and rax, r11
00221FFF  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
00222003  0F 11 45 E7                     movups xmmword ptr [rbp - 0x19], xmm0
00222007  74 0F                           je 0x140222018
00222009  41 80 7C 24 08 00               cmp byte ptr [r12 + 8], 0
0022200F  7C 07                           jl 0x140222018
00222011  49 0B C2                        or rax, r10
00222014  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
00222018  4C 8D 45 E7                     lea r8, [rbp - 0x19]
0022201C  8B D6                           mov edx, esi
0022201E  49 8B CC                        mov rcx, r12
00222021  E8 9A F3 FF FF                  call 0x1402213c0
00222026  48 89 45 DF                     mov qword ptr [rbp - 0x21], rax
0022202A  4C 8B F8                        mov r15, rax
0022202D  48 85 C0                        test rax, rax
00222030  0F 84 8F 03 00 00               je 0x1402223c5
00222036  41 0F B6 54 24 09               movzx edx, byte ptr [r12 + 9]
0022203C  0F B6 C2                        movzx eax, dl
0022203F  F6 D8                           neg al
00222041  1B C9                           sbb ecx, ecx
00222043  83 E1 08                        and ecx, 8
00222046  0B D9                           or ebx, ecx
00222048  84 D2                           test dl, dl
0022204A  0F 85 5E 04 00 00               jne 0x1402224ae
00222050  83 7D A3 00                     cmp dword ptr [rbp - 0x5d], 0
00222054  0F 84 51 03 00 00               je 0x1402223ab
0022205A  4D 3B E7                        cmp r12, r15
0022205D  0F 84 3B 02 00 00               je 0x14022229e
00222063  41 8B 44 24 50                  mov eax, dword ptr [r12 + 0x50]
00222068  C7 45 D7 00 00 00 00            mov dword ptr [rbp - 0x29], 0
0022206F  25 FF FF FF 3F                  and eax, 0x3fffffff
00222074  0F 87 75 0A 00 00               ja 0x140222aef
0022207A  41 0F B6 44 24 08               movzx eax, byte ptr [r12 + 8]
00222080  83 E0 3F                        and eax, 0x3f
00222083  48 6B C8 58                     imul rcx, rax, 0x58
00222087  49 8B C4                        mov rax, r12
0022208A  48 2B C1                        sub rax, rcx
0022208D  48 8B 40 F0                     mov rax, qword ptr [rax - 0x10]
00222091  0F B6 88 33 02 00 00            movzx ecx, byte ptr [rax + 0x233]
00222098  3A CA                           cmp cl, dl
0022209A  7E 0A                           jle 0x1402220a6
0022209C  0F B6 D1                        movzx edx, cl
0022209F  80 F9 1E                        cmp cl, 0x1e
002220A2  7E 02                           jle 0x1402220a6
002220A4  B2 1E                           mov dl, 0x1e
002220A6  41 38 54 24 28                  cmp byte ptr [r12 + 0x28], dl
002220AB  0F 84 EA 01 00 00               je 0x14022229b
002220B1  41 88 54 24 28                  mov byte ptr [r12 + 0x28], dl
002220B6  49 83 C7 28                     add r15, 0x28
002220BA  49 8B CF                        mov rcx, r15
002220BD  49 8D 54 24 10                  lea rdx, [r12 + 0x10]
002220C2  E8 49 2B 0C 00                  call 0x1402e4c10
002220C7  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
002220CB  41 0F B6 4C 24 28               movzx ecx, byte ptr [r12 + 0x28]
002220D1  49 8B 17                        mov rdx, qword ptr [r15]
002220D4  A8 01                           test al, 1
002220D6  0F 85 37 0C 00 00               jne 0x140222d13
002220DC  44 0F B6 C8                     movzx r9d, al
002220E0  45 32 C0                        xor r8b, r8b
002220E3  41 83 E1 01                     and r9d, 1
002220E7  48 85 D2                        test rdx, rdx
002220EA  0F 84 9A 01 00 00               je 0x14022228a
002220F0  38 4A 18                        cmp byte ptr [rdx + 0x18], cl
002220F3  0F 8E 78 01 00 00               jle 0x140222271
002220F9  48 8B 02                        mov rax, qword ptr [rdx]
002220FC  45 85 C9                        test r9d, r9d
002220FF  74 0C                           je 0x14022210d
00222101  48 85 C0                        test rax, rax
00222104  0F 84 80 01 00 00               je 0x14022228a
0022210A  48 33 C2                        xor rax, rdx
0022210D  48 85 C0                        test rax, rax
00222110  0F 84 74 01 00 00               je 0x14022228a
00222116  48 8B D0                        mov rdx, rax
00222119  EB D5                           jmp 0x1402220f0
0022211B  41 F6 46 0B 01                  test byte ptr [r14 + 0xb], 1
00222120  0F 85 F4 FD FF FF               jne 0x140221f1a
00222126  41 80 7E 09 00                  cmp byte ptr [r14 + 9], 0
0022212B  0F 85 C1 0A 00 00               jne 0x140222bf2
00222131  49 8B CE                        mov rcx, r14
00222134  E8 57 CF FF FF                  call 0x14021f090
00222139  8B 55 A3                        mov edx, dword ptr [rbp - 0x5d]
0022213C  41 3A 46 28                     cmp al, byte ptr [r14 + 0x28]
00222140  0F 84 5F 03 00 00               je 0x1402224a5
00222146  33 C0                           xor eax, eax
00222148  8B DF                           mov ebx, edi
0022214A  83 E3 07                        and ebx, 7
0022214D  48 89 45 0F                     mov qword ptr [rbp + 0xf], rax
00222151  89 45 5F                        mov dword ptr [rbp + 0x5f], eax
00222154  0F 57 C0                        xorps xmm0, xmm0
00222157  89 45 C7                        mov dword ptr [rbp - 0x39], eax
0022215A  49 8B 06                        mov rax, qword ptr [r14]
0022215D  C1 E3 06                        shl ebx, 6
00222160  49 23 C3                        and rax, r11
00222163  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
00222167  0F 11 45 FF                     movups xmmword ptr [rbp - 1], xmm0
0022216B  74 0E                           je 0x14022217b
0022216D  41 80 7E 08 00                  cmp byte ptr [r14 + 8], 0
00222172  7C 07                           jl 0x14022217b
00222174  49 0B C2                        or rax, r10
00222177  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
0022217B  4C 8D 45 FF                     lea r8, [rbp - 1]
0022217F  49 8B CE                        mov rcx, r14
00222182  E8 39 F2 FF FF                  call 0x1402213c0
00222187  4C 8B E0                        mov r12, rax
0022218A  48 85 C0                        test rax, rax
0022218D  0F 84 DC 02 00 00               je 0x14022246f
00222193  41 0F B6 56 09                  movzx edx, byte ptr [r14 + 9]
00222198  0F B6 C2                        movzx eax, dl
0022219B  F6 D8                           neg al
0022219D  1B C9                           sbb ecx, ecx
0022219F  83 E1 08                        and ecx, 8
002221A2  0B D9                           or ebx, ecx
002221A4  84 D2                           test dl, dl
002221A6  0F 85 E4 04 00 00               jne 0x140222690
002221AC  45 85 FF                        test r15d, r15d
002221AF  0F 84 A4 02 00 00               je 0x140222459
002221B5  4D 3B F4                        cmp r14, r12
002221B8  0F 84 5A 01 00 00               je 0x140222318
002221BE  41 8B 46 50                     mov eax, dword ptr [r14 + 0x50]
002221C2  C7 45 DB 00 00 00 00            mov dword ptr [rbp - 0x25], 0
002221C9  25 FF FF FF 3F                  and eax, 0x3fffffff
002221CE  0F 87 28 09 00 00               ja 0x140222afc
002221D4  41 0F B6 46 08                  movzx eax, byte ptr [r14 + 8]
002221D9  83 E0 3F                        and eax, 0x3f
002221DC  48 6B C8 58                     imul rcx, rax, 0x58
002221E0  49 8B C6                        mov rax, r14
002221E3  48 2B C1                        sub rax, rcx
002221E6  48 8B 40 F0                     mov rax, qword ptr [rax - 0x10]
002221EA  0F B6 88 33 02 00 00            movzx ecx, byte ptr [rax + 0x233]
002221F1  3A CA                           cmp cl, dl
002221F3  7E 0A                           jle 0x1402221ff
002221F5  0F B6 D1                        movzx edx, cl
002221F8  80 F9 1E                        cmp cl, 0x1e
002221FB  7E 02                           jle 0x1402221ff
002221FD  B2 1E                           mov dl, 0x1e
002221FF  41 38 56 28                     cmp byte ptr [r14 + 0x28], dl
00222203  0F 84 0C 01 00 00               je 0x140222315
00222209  41 88 56 28                     mov byte ptr [r14 + 0x28], dl
0022220D  4D 8D 7C 24 28                  lea r15, [r12 + 0x28]
00222212  49 8B CF                        mov rcx, r15
00222215  49 8D 56 10                     lea rdx, [r14 + 0x10]
00222219  E8 F2 29 0C 00                  call 0x1402e4c10
0022221E  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
00222222  41 0F B6 4E 28                  movzx ecx, byte ptr [r14 + 0x28]
00222227  49 8B 17                        mov rdx, qword ptr [r15]
0022222A  A8 01                           test al, 1
0022222C  0F 85 EE 0A 00 00               jne 0x140222d20
00222232  44 0F B6 C8                     movzx r9d, al
00222236  45 32 C0                        xor r8b, r8b
00222239  41 83 E1 01                     and r9d, 1
0022223D  48 85 D2                        test rdx, rdx
00222240  0F 84 C3 00 00 00               je 0x140222309
00222246  38 4A 18                        cmp byte ptr [rdx + 0x18], cl
00222249  0F 8E A1 00 00 00               jle 0x1402222f0
0022224F  48 8B 02                        mov rax, qword ptr [rdx]
00222252  45 85 C9                        test r9d, r9d
00222255  74 0C                           je 0x140222263
00222257  48 85 C0                        test rax, rax
0022225A  0F 84 A9 00 00 00               je 0x140222309
00222260  48 33 C2                        xor rax, rdx
00222263  48 85 C0                        test rax, rax
00222266  0F 84 9D 00 00 00               je 0x140222309
0022226C  48 8B D0                        mov rdx, rax
0022226F  EB D5                           jmp 0x140222246
00222271  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
00222275  45 85 C9                        test r9d, r9d
00222278  0F 84 23 05 00 00               je 0x1402227a1
0022227E  48 85 C0                        test rax, rax
00222281  0F 85 17 05 00 00               jne 0x14022279e
00222287  41 B0 01                        mov r8b, 1
0022228A  4D 8D 4C 24 10                  lea r9, [r12 + 0x10]
0022228F  49 8B CF                        mov rcx, r15
00222292  E8 D9 22 0C 00                  call 0x1402e4570
00222297  4C 8B 7D DF                     mov r15, qword ptr [rbp - 0x21]
0022229B  83 CB 10                        or ebx, 0x10
0022229E  41 8B 4F 54                     mov ecx, dword ptr [r15 + 0x54]
002222A2  84 C9                           test cl, cl
002222A4  74 04                           je 0x1402222aa
002222A6  C6 45 A0 02                     mov byte ptr [rbp - 0x60], 2
002222AA  F7 C1 00 7F 00 00               test ecx, 0x7f00
002222B0  76 04                           jbe 0x1402222b6
002222B2  C6 45 A1 01                     mov byte ptr [rbp - 0x5f], 1
002222B6  49 8B 47 40                     mov rax, qword ptr [r15 + 0x40]
002222BA  48 85 C0                        test rax, rax
002222BD  0F 84 6A 0A 00 00               je 0x140222d2d
002222C3  0F B6 50 18                     movzx edx, byte ptr [rax + 0x18]
002222C7  88 55 9F                        mov byte ptr [rbp - 0x61], dl
002222CA  41 80 7F 09 00                  cmp byte ptr [r15 + 9], 0
002222CF  0F 85 56 08 00 00               jne 0x140222b2b
002222D5  83 7D 9F 00                     cmp dword ptr [rbp - 0x61], 0
002222D9  0F 85 E1 04 00 00               jne 0x1402227c0
002222DF  48 8D 4D E7                     lea rcx, [rbp - 0x19]
002222E3  E8 C8 4E FF FF                  call 0x1402171b0
002222E8  83 CB 01                        or ebx, 1
002222EB  E9 D5 00 00 00                  jmp 0x1402223c5
002222F0  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
002222F4  45 85 C9                        test r9d, r9d
002222F7  0F 84 B5 04 00 00               je 0x1402227b2
002222FD  48 85 C0                        test rax, rax
00222300  0F 85 A9 04 00 00               jne 0x1402227af
00222306  41 B0 01                        mov r8b, 1
00222309  4D 8D 4E 10                     lea r9, [r14 + 0x10]
0022230D  49 8B CF                        mov rcx, r15
00222310  E8 5B 22 0C 00                  call 0x1402e4570
00222315  83 CB 10                        or ebx, 0x10
00222318  41 8B 4C 24 54                  mov ecx, dword ptr [r12 + 0x54]
0022231D  84 C9                           test cl, cl
0022231F  74 04                           je 0x140222325
00222321  C6 45 60 02                     mov byte ptr [rbp + 0x60], 2
00222325  F7 C1 00 7F 00 00               test ecx, 0x7f00
0022232B  76 04                           jbe 0x140222331
0022232D  C6 45 61 01                     mov byte ptr [rbp + 0x61], 1
00222331  49 8B 44 24 40                  mov rax, qword ptr [r12 + 0x40]
00222336  48 85 C0                        test rax, rax
00222339  0F 84 F7 09 00 00               je 0x140222d36
0022233F  0F B6 50 18                     movzx edx, byte ptr [rax + 0x18]
00222343  88 55 5F                        mov byte ptr [rbp + 0x5f], dl
00222346  41 80 7C 24 09 00               cmp byte ptr [r12 + 9], 0
0022234C  0F 85 13 08 00 00               jne 0x140222b65
00222352  83 7D 5F 00                     cmp dword ptr [rbp + 0x5f], 0
00222356  0F 85 1F 05 00 00               jne 0x14022287b
0022235C  48 8D 4D FF                     lea rcx, [rbp - 1]
00222360  E8 4B 4E FF FF                  call 0x1402171b0
00222365  83 CB 01                        or ebx, 1
00222368  E9 02 01 00 00                  jmp 0x14022246f
0022236D  45 85 D2                        test r10d, r10d
00222370  74 1C                           je 0x14022238e
00222372  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
00222376  41 8B D2                        mov edx, r10d
00222379  4C 8B 4D 77                     mov r9, qword ptr [rbp + 0x77]
0022237D  49 8B CF                        mov rcx, r15
00222380  4C 8B 45 6F                     mov r8, qword ptr [rbp + 0x6f]
00222384  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00222389  E8 22 D9 FF FF                  call 0x14021fcb0
0022238E  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
00222392  41 0F B6 D6                     movzx edx, r14b
00222396  4C 8B 4D 77                     mov r9, qword ptr [rbp + 0x77]
0022239A  49 8B CF                        mov rcx, r15
0022239D  4C 8B 45 6F                     mov r8, qword ptr [rbp + 0x6f]
002223A1  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
002223A6  E8 D5 E2 FF FF                  call 0x140220680
002223AB  48 8D 4D E7                     lea rcx, [rbp - 0x19]
002223AF  E8 FC 4D FF FF                  call 0x1402171b0
002223B4  44 8B 75 BF                     mov r14d, dword ptr [rbp - 0x41]
002223B8  45 85 F6                        test r14d, r14d
002223BB  0F 85 89 08 00 00               jne 0x140222c4a
002223C1  4C 8B 75 AF                     mov r14, qword ptr [rbp - 0x51]
002223C5  F7 05 45 47 DA 00 00 10 00 00   test dword ptr [rip + 0xda4745], 0x1000
002223CF  74 21                           je 0x1402223f2
002223D1  41 0F B6 44 24 08               movzx eax, byte ptr [r12 + 8]
002223D7  48 8B 55 CF                     mov rdx, qword ptr [rbp - 0x31]
002223DB  83 E0 3F                        and eax, 0x3f
002223DE  4C 6B C0 58                     imul r8, rax, 0x58
002223E2  4D 2B E0                        sub r12, r8
002223E5  44 8B C3                        mov r8d, ebx
002223E8  49 8B 4C 24 F0                  mov rcx, qword ptr [r12 - 0x10]
002223ED  E8 8A F8 FF FF                  call 0x140221c7c
002223F2  44 8B 4D A7                     mov r9d, dword ptr [rbp - 0x59]
002223F6  49 BB FC FF FF FF FF FF FF 7F   movabs r11, 0x7ffffffffffffffc
00222400  49 BA 00 00 00 00 00 00 00 80   movabs r10, 0x8000000000000000
0022240A  BB 1E 00 00 00                  mov ebx, 0x1e
0022240F  8B 55 A3                        mov edx, dword ptr [rbp - 0x5d]
00222412  4C 8B 45 B7                     mov r8, qword ptr [rbp - 0x49]
00222416  E9 63 FA FF FF                  jmp 0x140221e7e
0022241B  45 85 D2                        test r10d, r10d
0022241E  74 1C                           je 0x14022243c
00222420  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
00222424  41 8B D2                        mov edx, r10d
00222427  4C 8B 4D 77                     mov r9, qword ptr [rbp + 0x77]
0022242B  49 8B CC                        mov rcx, r12
0022242E  4C 8B 45 6F                     mov r8, qword ptr [rbp + 0x6f]
00222432  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00222437  E8 74 D8 FF FF                  call 0x14021fcb0
0022243C  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
00222440  41 0F B6 D7                     movzx edx, r15b
00222444  4C 8B 4D 77                     mov r9, qword ptr [rbp + 0x77]
00222448  49 8B CC                        mov rcx, r12
0022244B  4C 8B 45 6F                     mov r8, qword ptr [rbp + 0x6f]
0022244F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00222454  E8 27 E2 FF FF                  call 0x140220680
00222459  48 8D 4D FF                     lea rcx, [rbp - 1]
0022245D  E8 4E 4D FF FF                  call 0x1402171b0
00222462  44 8B 7D C7                     mov r15d, dword ptr [rbp - 0x39]
00222466  45 85 FF                        test r15d, r15d
00222469  0F 85 40 08 00 00               jne 0x140222caf
0022246F  F7 05 9B 46 DA 00 00 10 00 00   test dword ptr [rip + 0xda469b], 0x1000
00222479  74 1F                           je 0x14022249a
0022247B  41 0F B6 46 08                  movzx eax, byte ptr [r14 + 8]
00222480  48 8B 55 CF                     mov rdx, qword ptr [rbp - 0x31]
00222484  83 E0 3F                        and eax, 0x3f
00222487  4C 6B C0 58                     imul r8, rax, 0x58
0022248B  4D 2B F0                        sub r14, r8
0022248E  44 8B C3                        mov r8d, ebx
00222491  49 8B 4E F0                     mov rcx, qword ptr [r14 - 0x10]
00222495  E8 E2 F7 FF FF                  call 0x140221c7c
0022249A  44 8B 4D A7                     mov r9d, dword ptr [rbp - 0x59]
0022249E  44 8B 7D AF                     mov r15d, dword ptr [rbp - 0x51]
002224A2  8B 55 A3                        mov edx, dword ptr [rbp - 0x5d]
002224A5  4C 8B 45 B7                     mov r8, qword ptr [rbp - 0x49]
002224A9  E9 6C FA FF FF                  jmp 0x140221f1a
002224AE  83 7D A7 00                     cmp dword ptr [rbp - 0x59], 0
002224B2  0F 84 F3 FE FF FF               je 0x1402223ab
002224B8  4D 3B E7                        cmp r12, r15
002224BB  0F 84 B9 00 00 00               je 0x14022257a
002224C1  41 0F B6 44 24 08               movzx eax, byte ptr [r12 + 8]
002224C7  83 E0 3F                        and eax, 0x3f
002224CA  48 6B C8 58                     imul rcx, rax, 0x58
002224CE  49 8B C4                        mov rax, r12
002224D1  48 2B C1                        sub rax, rcx
002224D4  48 8B 40 F0                     mov rax, qword ptr [rax - 0x10]
002224D8  0F B6 88 C3 00 00 00            movzx ecx, byte ptr [rax + 0xc3]
002224DF  80 F9 1E                        cmp cl, 0x1e
002224E2  8B C1                           mov eax, ecx
002224E4  B9 1E 00 00 00                  mov ecx, 0x1e
002224E9  0F 4F C1                        cmovg eax, ecx
002224EC  41 38 44 24 28                  cmp byte ptr [r12 + 0x28], al
002224F1  0F 84 80 00 00 00               je 0x140222577
002224F7  4D 8D 77 38                     lea r14, [r15 + 0x38]
002224FB  41 88 44 24 28                  mov byte ptr [r12 + 0x28], al
00222500  49 8B CE                        mov rcx, r14
00222503  49 8D 54 24 10                  lea rdx, [r12 + 0x10]
00222508  E8 03 27 0C 00                  call 0x1402e4c10
0022250D  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00222511  41 0F B6 4C 24 28               movzx ecx, byte ptr [r12 + 0x28]
00222517  49 8B 16                        mov rdx, qword ptr [r14]
0022251A  A8 01                           test al, 1
0022251C  0F 85 1D 08 00 00               jne 0x140222d3f
00222522  44 0F B6 C8                     movzx r9d, al
00222526  45 32 C0                        xor r8b, r8b
00222529  41 83 E1 01                     and r9d, 1
0022252D  48 85 D2                        test rdx, rdx
00222530  74 38                           je 0x14022256a
00222532  38 4A 18                        cmp byte ptr [rdx + 0x18], cl
00222535  7D 1A                           jge 0x140222551
00222537  48 8B 02                        mov rax, qword ptr [rdx]
0022253A  45 85 C9                        test r9d, r9d
0022253D  74 08                           je 0x140222547
0022253F  48 85 C0                        test rax, rax
00222542  74 26                           je 0x14022256a
00222544  48 33 C2                        xor rax, rdx
00222547  48 85 C0                        test rax, rax
0022254A  74 1E                           je 0x14022256a
0022254C  48 8B D0                        mov rdx, rax
0022254F  EB E1                           jmp 0x140222532
00222551  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
00222555  45 85 C9                        test r9d, r9d
00222558  0F 84 F8 04 00 00               je 0x140222a56
0022255E  48 85 C0                        test rax, rax
00222561  0F 85 EC 04 00 00               jne 0x140222a53
00222567  41 B0 01                        mov r8b, 1
0022256A  4D 8D 4C 24 10                  lea r9, [r12 + 0x10]
0022256F  49 8B CE                        mov rcx, r14
00222572  E8 F9 1F 0C 00                  call 0x1402e4570
00222577  83 CB 20                        or ebx, 0x20
0022257A  49 8B 47 30                     mov rax, qword ptr [r15 + 0x30]
0022257E  48 85 C0                        test rax, rax
00222581  0F 85 B8 04 00 00               jne 0x140222a3f
00222587  41 B1 1E                        mov r9b, 0x1e
0022258A  41 80 7F 09 00                  cmp byte ptr [r15 + 9], 0
0022258F  44 88 4D 9F                     mov byte ptr [rbp - 0x61], r9b
00222593  0F 84 64 04 00 00               je 0x1402229fd
00222599  41 80 7C 24 09 00               cmp byte ptr [r12 + 9], 0
0022259F  0F 84 87 03 00 00               je 0x14022292c
002225A5  41 0F B6 54 24 0B               movzx edx, byte ptr [r12 + 0xb]
002225AB  0F B6 C2                        movzx eax, dl
002225AE  24 06                           and al, 6
002225B0  3C 06                           cmp al, 6
002225B2  0F 84 74 03 00 00               je 0x14022292c
002225B8  41 0F B6 44 24 08               movzx eax, byte ptr [r12 + 8]
002225BE  45 33 D2                        xor r10d, r10d
002225C1  83 E0 3F                        and eax, 0x3f
002225C4  48 6B C8 58                     imul rcx, rax, 0x58
002225C8  49 8B C4                        mov rax, r12
002225CB  48 2B C1                        sub rax, rcx
002225CE  4C 8B 58 F0                     mov r11, qword ptr [rax - 0x10]
002225D2  F6 C2 02                        test dl, 2
002225D5  75 30                           jne 0x140222607
002225D7  49 8B CB                        mov rcx, r11
002225DA  E8 51 13 12 00                  call 0x140343930
002225DF  83 F8 02                        cmp eax, 2
002225E2  0F 8C 3E 06 00 00               jl 0x140222c26
002225E8  41 FE 47 54                     inc byte ptr [r15 + 0x54]
002225EC  41 0F B6 44 24 0B               movzx eax, byte ptr [r12 + 0xb]
002225F2  44 0F B6 4D 9F                  movzx r9d, byte ptr [rbp - 0x61]
002225F7  0C 02                           or al, 2
002225F9  41 88 44 24 0B                  mov byte ptr [r12 + 0xb], al
002225FE  41 80 7F 54 01                  cmp byte ptr [r15 + 0x54], 1
00222603  45 0F 44 D5                     cmove r10d, r13d
00222607  41 F6 44 24 0B 04               test byte ptr [r12 + 0xb], 4
0022260D  75 52                           jne 0x140222661
0022260F  41 83 BB E8 05 00 00 00         cmp dword ptr [r11 + 0x5e8], 0
00222617  74 0A                           je 0x140222623
00222619  41 83 BB E4 05 00 00 00         cmp dword ptr [r11 + 0x5e4], 0
00222621  74 3E                           je 0x140222661
00222623  41 8B 47 54                     mov eax, dword ptr [r15 + 0x54]
00222627  8D 88 00 01 00 00               lea ecx, [rax + 0x100]
0022262D  33 C8                           xor ecx, eax
0022262F  81 E1 00 7F 00 00               and ecx, 0x7f00
00222635  33 C8                           xor ecx, eax
00222637  41 89 4F 54                     mov dword ptr [r15 + 0x54], ecx
0022263B  41 0F B6 44 24 0B               movzx eax, byte ptr [r12 + 0xb]
00222641  44 0F B6 4D 9F                  movzx r9d, byte ptr [rbp - 0x61]
00222646  0C 04                           or al, 4
00222648  41 88 44 24 0B                  mov byte ptr [r12 + 0xb], al
0022264D  41 8B 47 54                     mov eax, dword ptr [r15 + 0x54]
00222651  25 00 7F 00 00                  and eax, 0x7f00
00222656  3D 00 01 00 00                  cmp eax, 0x100
0022265B  75 04                           jne 0x140222661
0022265D  41 83 CA 02                     or r10d, 2
00222661  49 8B CC                        mov rcx, r12
00222664  E8 67 07 00 00                  call 0x140222dd0
00222669  44 0F B6 F0                     movzx r14d, al
0022266D  44 3A C8                        cmp r9b, al
00222670  0F 8C F7 FC FF FF               jl 0x14022236d
00222676  45 85 D2                        test r10d, r10d
00222679  0F 85 F3 FC FF FF               jne 0x140222372
0022267F  48 8D 4D E7                     lea rcx, [rbp - 0x19]
00222683  E8 28 4B FF FF                  call 0x1402171b0
00222688  83 CB 02                        or ebx, 2
0022268B  E9 31 FD FF FF                  jmp 0x1402223c1
00222690  83 7D A7 00                     cmp dword ptr [rbp - 0x59], 0
00222694  0F 84 BF FD FF FF               je 0x140222459
0022269A  4D 3B F4                        cmp r14, r12
0022269D  0F 84 B9 00 00 00               je 0x14022275c
002226A3  41 0F B6 46 08                  movzx eax, byte ptr [r14 + 8]
002226A8  83 E0 3F                        and eax, 0x3f
002226AB  48 6B C8 58                     imul rcx, rax, 0x58
002226AF  49 8B C6                        mov rax, r14
002226B2  48 2B C1                        sub rax, rcx
002226B5  48 8B 40 F0                     mov rax, qword ptr [rax - 0x10]
002226B9  0F B6 88 C3 00 00 00            movzx ecx, byte ptr [rax + 0xc3]
002226C0  80 F9 1E                        cmp cl, 0x1e
002226C3  8B C1                           mov eax, ecx
002226C5  B9 1E 00 00 00                  mov ecx, 0x1e
002226CA  0F 4F C1                        cmovg eax, ecx
002226CD  41 38 46 28                     cmp byte ptr [r14 + 0x28], al
002226D1  0F 84 82 00 00 00               je 0x140222759
002226D7  49 8D 56 10                     lea rdx, [r14 + 0x10]
002226DB  41 88 46 28                     mov byte ptr [r14 + 0x28], al
002226DF  49 8D 4C 24 38                  lea rcx, [r12 + 0x38]
002226E4  E8 27 25 0C 00                  call 0x1402e4c10
002226E9  49 8B 44 24 40                  mov rax, qword ptr [r12 + 0x40]
002226EE  41 0F B6 4E 28                  movzx ecx, byte ptr [r14 + 0x28]
002226F3  A8 01                           test al, 1
002226F5  0F 85 51 06 00 00               jne 0x140222d4c
002226FB  4D 8B 4C 24 38                  mov r9, qword ptr [r12 + 0x38]
00222700  44 0F B6 D0                     movzx r10d, al
00222704  45 32 C0                        xor r8b, r8b
00222707  41 83 E2 01                     and r10d, 1
0022270B  49 8B D1                        mov rdx, r9
0022270E  4D 85 C9                        test r9, r9
00222711  74 38                           je 0x14022274b
00222713  38 4A 18                        cmp byte ptr [rdx + 0x18], cl
00222716  7D 1A                           jge 0x140222732
00222718  48 8B 02                        mov rax, qword ptr [rdx]
0022271B  45 85 D2                        test r10d, r10d
0022271E  74 08                           je 0x140222728
00222720  48 85 C0                        test rax, rax
00222723  74 26                           je 0x14022274b
00222725  48 33 C2                        xor rax, rdx
00222728  48 85 C0                        test rax, rax
0022272B  74 1E                           je 0x14022274b
0022272D  48 8B D0                        mov rdx, rax
00222730  EB E1                           jmp 0x140222713
00222732  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
00222736  45 85 D2                        test r10d, r10d
00222739  0F 84 28 03 00 00               je 0x140222a67
0022273F  48 85 C0                        test rax, rax
00222742  0F 85 1C 03 00 00               jne 0x140222a64
00222748  41 B0 01                        mov r8b, 1
0022274B  4D 8D 4E 10                     lea r9, [r14 + 0x10]
0022274F  49 8D 4C 24 38                  lea rcx, [r12 + 0x38]
00222754  E8 17 1E 0C 00                  call 0x1402e4570
00222759  83 CB 20                        or ebx, 0x20
0022275C  49 8B 44 24 30                  mov rax, qword ptr [r12 + 0x30]
00222761  48 85 C0                        test rax, rax
00222764  0F 85 DF 02 00 00               jne 0x140222a49
0022276A  41 B1 1E                        mov r9b, 0x1e
0022276D  41 80 7C 24 09 00               cmp byte ptr [r12 + 9], 0
00222773  44 88 4D 5F                     mov byte ptr [rbp + 0x5f], r9b
00222777  0F 84 A1 02 00 00               je 0x140222a1e
0022277D  41 80 7E 09 00                  cmp byte ptr [r14 + 9], 0
00222782  74 12                           je 0x140222796
00222784  41 0F B6 56 0B                  movzx edx, byte ptr [r14 + 0xb]
00222789  0F B6 C2                        movzx eax, dl
0022278C  24 06                           and al, 6
0022278E  3C 06                           cmp al, 6
00222790  0F 85 DF 02 00 00               jne 0x140222a75
00222796  45 33 D2                        xor r10d, r10d
00222799  E9 D5 01 00 00                  jmp 0x140222973
0022279E  48 33 C2                        xor rax, rdx
002227A1  48 85 C0                        test rax, rax
002227A4  0F 85 6C F9 FF FF               jne 0x140222116
002227AA  E9 D8 FA FF FF                  jmp 0x140222287
002227AF  48 33 C2                        xor rax, rdx
002227B2  48 85 C0                        test rax, rax
002227B5  0F 85 B1 FA FF FF               jne 0x14022226c
002227BB  E9 46 FB FF FF                  jmp 0x140222306
002227C0  4C 8B 4D 77                     mov r9, qword ptr [rbp + 0x77]
002227C4  48 8D 45 BF                     lea rax, [rbp - 0x41]
002227C8  4C 8B 45 6F                     mov r8, qword ptr [rbp + 0x6f]
002227CC  48 8D 55 9F                     lea rdx, [rbp - 0x61]
002227D0  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
002227D5  49 8B CC                        mov rcx, r12
002227D8  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
002227DC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
002227E1  E8 AA C9 FF FF                  call 0x14021f190
002227E6  85 C0                           test eax, eax
002227E8  0F 84 BD FB FF FF               je 0x1402223ab
002227EE  4D 3B E7                        cmp r12, r15
002227F1  0F 84 B4 FB FF FF               je 0x1402223ab
002227F7  49 8B CC                        mov rcx, r12
002227FA  E8 91 C8 FF FF                  call 0x14021f090
002227FF  41 38 44 24 28                  cmp byte ptr [r12 + 0x28], al
00222804  0F 84 BE 01 00 00               je 0x1402229c8
0022280A  4D 8D 77 28                     lea r14, [r15 + 0x28]
0022280E  41 88 44 24 28                  mov byte ptr [r12 + 0x28], al
00222813  49 8B CE                        mov rcx, r14
00222816  49 8D 54 24 10                  lea rdx, [r12 + 0x10]
0022281B  E8 F0 23 0C 00                  call 0x1402e4c10
00222820  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00222824  41 0F B6 4C 24 28               movzx ecx, byte ptr [r12 + 0x28]
0022282A  49 8B 16                        mov rdx, qword ptr [r14]
0022282D  A8 01                           test al, 1
0022282F  0F 85 4E 05 00 00               jne 0x140222d83
00222835  44 0F B6 C8                     movzx r9d, al
00222839  45 32 C0                        xor r8b, r8b
0022283C  41 83 E1 01                     and r9d, 1
00222840  48 85 D2                        test rdx, rdx
00222843  0F 84 72 01 00 00               je 0x1402229bb
00222849  0F 1F 80 00 00 00 00            nop dword ptr [rax]
00222850  38 4A 18                        cmp byte ptr [rdx + 0x18], cl
00222853  0F 8E 49 01 00 00               jle 0x1402229a2
00222859  48 8B 02                        mov rax, qword ptr [rdx]
0022285C  45 85 C9                        test r9d, r9d
0022285F  74 0C                           je 0x14022286d
00222861  48 85 C0                        test rax, rax
00222864  0F 84 51 01 00 00               je 0x1402229bb
0022286A  48 33 C2                        xor rax, rdx
0022286D  48 85 C0                        test rax, rax
00222870  0F 84 45 01 00 00               je 0x1402229bb
00222876  48 8B D0                        mov rdx, rax
00222879  EB D5                           jmp 0x140222850
0022287B  4C 8B 4D 77                     mov r9, qword ptr [rbp + 0x77]
0022287F  48 8D 45 C7                     lea rax, [rbp - 0x39]
00222883  4C 8B 45 6F                     mov r8, qword ptr [rbp + 0x6f]
00222887  48 8D 55 5F                     lea rdx, [rbp + 0x5f]
0022288B  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00222890  49 8B CE                        mov rcx, r14
00222893  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
00222897  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0022289C  E8 EF C8 FF FF                  call 0x14021f190
002228A1  85 C0                           test eax, eax
002228A3  0F 84 B0 FB FF FF               je 0x140222459
002228A9  4D 3B F4                        cmp r14, r12
002228AC  0F 84 A7 FB FF FF               je 0x140222459
002228B2  49 8B CE                        mov rcx, r14
002228B5  E8 D6 C7 FF FF                  call 0x14021f090
002228BA  41 38 46 28                     cmp byte ptr [r14 + 0x28], al
002228BE  0F 84 31 01 00 00               je 0x1402229f5
002228C4  4D 8D 7C 24 28                  lea r15, [r12 + 0x28]
002228C9  41 88 46 28                     mov byte ptr [r14 + 0x28], al
002228CD  49 8B CF                        mov rcx, r15
002228D0  49 8D 56 10                     lea rdx, [r14 + 0x10]
002228D4  E8 37 23 0C 00                  call 0x1402e4c10
002228D9  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
002228DD  41 0F B6 4E 28                  movzx ecx, byte ptr [r14 + 0x28]
002228E2  49 8B 17                        mov rdx, qword ptr [r15]
002228E5  A8 01                           test al, 1
002228E7  0F 85 A3 04 00 00               jne 0x140222d90
002228ED  44 0F B6 C8                     movzx r9d, al
002228F1  45 32 C0                        xor r8b, r8b
002228F4  41 83 E1 01                     and r9d, 1
002228F8  48 85 D2                        test rdx, rdx
002228FB  0F 84 E8 00 00 00               je 0x1402229e9
00222901  38 4A 18                        cmp byte ptr [rdx + 0x18], cl
00222904  0F 8E C6 00 00 00               jle 0x1402229d0
0022290A  48 8B 02                        mov rax, qword ptr [rdx]
0022290D  45 85 C9                        test r9d, r9d
00222910  74 0C                           je 0x14022291e
00222912  48 85 C0                        test rax, rax
00222915  0F 84 CE 00 00 00               je 0x1402229e9
0022291B  48 33 C2                        xor rax, rdx
0022291E  48 85 C0                        test rax, rax
00222921  0F 84 C2 00 00 00               je 0x1402229e9
00222927  48 8B D0                        mov rdx, rax
0022292A  EB D5                           jmp 0x140222901
0022292C  45 33 D2                        xor r10d, r10d
0022292F  E9 2D FD FF FF                  jmp 0x140222661
00222934  41 8B 44 24 54                  mov eax, dword ptr [r12 + 0x54]
00222939  8D 88 00 01 00 00               lea ecx, [rax + 0x100]
0022293F  33 C8                           xor ecx, eax
00222941  81 E1 00 7F 00 00               and ecx, 0x7f00
00222947  33 C8                           xor ecx, eax
00222949  41 89 4C 24 54                  mov dword ptr [r12 + 0x54], ecx
0022294E  41 0F B6 46 0B                  movzx eax, byte ptr [r14 + 0xb]
00222953  44 0F B6 4D 5F                  movzx r9d, byte ptr [rbp + 0x5f]
00222958  0C 04                           or al, 4
0022295A  41 88 46 0B                     mov byte ptr [r14 + 0xb], al
0022295E  41 8B 44 24 54                  mov eax, dword ptr [r12 + 0x54]
00222963  25 00 7F 00 00                  and eax, 0x7f00
00222968  3D 00 01 00 00                  cmp eax, 0x100
0022296D  75 04                           jne 0x140222973
0022296F  41 83 CA 02                     or r10d, 2
00222973  49 8B CE                        mov rcx, r14
00222976  E8 55 04 00 00                  call 0x140222dd0
0022297B  44 0F B6 F8                     movzx r15d, al
0022297F  44 3A C8                        cmp r9b, al
00222982  0F 8C 93 FA FF FF               jl 0x14022241b
00222988  45 85 D2                        test r10d, r10d
0022298B  0F 85 8F FA FF FF               jne 0x140222420
00222991  48 8D 4D FF                     lea rcx, [rbp - 1]
00222995  E8 16 48 FF FF                  call 0x1402171b0
0022299A  83 CB 02                        or ebx, 2
0022299D  E9 CD FA FF FF                  jmp 0x14022246f
002229A2  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
002229A6  45 85 C9                        test r9d, r9d
002229A9  0F 84 5D 01 00 00               je 0x140222b0c
002229AF  48 85 C0                        test rax, rax
002229B2  0F 85 51 01 00 00               jne 0x140222b09
002229B8  41 B0 01                        mov r8b, 1
002229BB  4D 8D 4C 24 10                  lea r9, [r12 + 0x10]
002229C0  49 8B CE                        mov rcx, r14
002229C3  E8 A8 1B 0C 00                  call 0x1402e4570
002229C8  83 CB 20                        or ebx, 0x20
002229CB  E9 DB F9 FF FF                  jmp 0x1402223ab
002229D0  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
002229D4  45 85 C9                        test r9d, r9d
002229D7  0F 84 40 01 00 00               je 0x140222b1d
002229DD  48 85 C0                        test rax, rax
002229E0  0F 85 34 01 00 00               jne 0x140222b1a
002229E6  41 B0 01                        mov r8b, 1
002229E9  4D 8D 4E 10                     lea r9, [r14 + 0x10]
002229ED  49 8B CF                        mov rcx, r15
002229F0  E8 7B 1B 0C 00                  call 0x1402e4570
002229F5  83 CB 20                        or ebx, 0x20
002229F8  E9 5C FA FF FF                  jmp 0x140222459
002229FD  49 8B CF                        mov rcx, r15
00222A00  E8 8B C6 FF FF                  call 0x14021f090
00222A05  41 3A C1                        cmp al, r9b
00222A08  41 0F B6 D1                     movzx edx, r9b
00222A0C  0F B6 C8                        movzx ecx, al
00222A0F  0F 4C D1                        cmovl edx, ecx
00222A12  44 0F B6 CA                     movzx r9d, dl
00222A16  88 55 9F                        mov byte ptr [rbp - 0x61], dl
00222A19  E9 7B FB FF FF                  jmp 0x140222599
00222A1E  49 8B CC                        mov rcx, r12
00222A21  E8 6A C6 FF FF                  call 0x14021f090
00222A26  41 3A C1                        cmp al, r9b
00222A29  41 0F B6 D1                     movzx edx, r9b
00222A2D  0F B6 C8                        movzx ecx, al
00222A30  0F 4C D1                        cmovl edx, ecx
00222A33  44 0F B6 CA                     movzx r9d, dl
00222A37  88 55 5F                        mov byte ptr [rbp + 0x5f], dl
00222A3A  E9 3E FD FF FF                  jmp 0x14022277d
00222A3F  44 0F B6 48 18                  movzx r9d, byte ptr [rax + 0x18]
00222A44  E9 41 FB FF FF                  jmp 0x14022258a
00222A49  44 0F B6 48 18                  movzx r9d, byte ptr [rax + 0x18]
00222A4E  E9 1A FD FF FF                  jmp 0x14022276d
00222A53  48 33 C2                        xor rax, rdx
00222A56  48 85 C0                        test rax, rax
00222A59  0F 85 ED FA FF FF               jne 0x14022254c
00222A5F  E9 03 FB FF FF                  jmp 0x140222567
00222A64  48 33 C2                        xor rax, rdx
00222A67  48 85 C0                        test rax, rax
00222A6A  0F 85 BD FC FF FF               jne 0x14022272d
00222A70  E9 D3 FC FF FF                  jmp 0x140222748
00222A75  41 0F B6 46 08                  movzx eax, byte ptr [r14 + 8]
00222A7A  45 33 D2                        xor r10d, r10d
00222A7D  83 E0 3F                        and eax, 0x3f
00222A80  48 6B C8 58                     imul rcx, rax, 0x58
00222A84  49 8B C6                        mov rax, r14
00222A87  48 2B C1                        sub rax, rcx
00222A8A  4C 8B 58 F0                     mov r11, qword ptr [rax - 0x10]
00222A8E  F6 C2 02                        test dl, 2
00222A91  75 30                           jne 0x140222ac3
00222A93  49 8B CB                        mov rcx, r11
00222A96  E8 95 0E 12 00                  call 0x140343930
00222A9B  83 F8 02                        cmp eax, 2
00222A9E  0F 8C 94 01 00 00               jl 0x140222c38
00222AA4  41 FE 44 24 54                  inc byte ptr [r12 + 0x54]
00222AA9  41 0F B6 46 0B                  movzx eax, byte ptr [r14 + 0xb]
00222AAE  44 0F B6 4D 5F                  movzx r9d, byte ptr [rbp + 0x5f]
00222AB3  0C 02                           or al, 2
00222AB5  41 88 46 0B                     mov byte ptr [r14 + 0xb], al
00222AB9  41 80 7C 24 54 01               cmp byte ptr [r12 + 0x54], 1
00222ABF  45 0F 44 D5                     cmove r10d, r13d
00222AC3  41 F6 46 0B 04                  test byte ptr [r14 + 0xb], 4
00222AC8  0F 85 A5 FE FF FF               jne 0x140222973
00222ACE  41 83 BB E8 05 00 00 00         cmp dword ptr [r11 + 0x5e8], 0
00222AD6  0F 84 58 FE FF FF               je 0x140222934
00222ADC  41 83 BB E4 05 00 00 00         cmp dword ptr [r11 + 0x5e4], 0
00222AE4  0F 85 4A FE FF FF               jne 0x140222934
00222AEA  E9 84 FE FF FF                  jmp 0x140222973
00222AEF  0F BD D0                        bsr edx, eax
00222AF2  89 55 D7                        mov dword ptr [rbp - 0x29], edx
00222AF5  FE C2                           inc dl
00222AF7  E9 7E F5 FF FF                  jmp 0x14022207a
00222AFC  0F BD D0                        bsr edx, eax
00222AFF  89 55 DB                        mov dword ptr [rbp - 0x25], edx
00222B02  FE C2                           inc dl
00222B04  E9 CB F6 FF FF                  jmp 0x1402221d4
00222B09  48 33 C2                        xor rax, rdx
00222B0C  48 85 C0                        test rax, rax
00222B0F  0F 85 61 FD FF FF               jne 0x140222876
00222B15  E9 9E FE FF FF                  jmp 0x1402229b8
00222B1A  48 33 C2                        xor rax, rdx
00222B1D  48 85 C0                        test rax, rax
00222B20  0F 85 01 FE FF FF               jne 0x140222927
00222B26  E9 BB FE FF FF                  jmp 0x1402229e6
00222B2B  41 0F B6 47 08                  movzx eax, byte ptr [r15 + 8]
00222B30  83 E0 3F                        and eax, 0x3f
00222B33  48 6B C8 58                     imul rcx, rax, 0x58
00222B37  49 8B C7                        mov rax, r15
00222B3A  48 2B C1                        sub rax, rcx
00222B3D  48 8B 40 F0                     mov rax, qword ptr [rax - 0x10]
00222B41  0F B6 88 C3 00 00 00            movzx ecx, byte ptr [rax + 0xc3]
00222B48  80 F9 1E                        cmp cl, 0x1e
00222B4B  8B C1                           mov eax, ecx
00222B4D  B9 1E 00 00 00                  mov ecx, 0x1e
00222B52  0F 4F C1                        cmovg eax, ecx
00222B55  3A C2                           cmp al, dl
00222B57  0F 8E 78 F7 FF FF               jle 0x1402222d5
00222B5D  88 45 9F                        mov byte ptr [rbp - 0x61], al
00222B60  E9 70 F7 FF FF                  jmp 0x1402222d5
00222B65  41 0F B6 44 24 08               movzx eax, byte ptr [r12 + 8]
00222B6B  83 E0 3F                        and eax, 0x3f
00222B6E  48 6B C8 58                     imul rcx, rax, 0x58
00222B72  49 8B C4                        mov rax, r12
00222B75  48 2B C1                        sub rax, rcx
00222B78  48 8B 40 F0                     mov rax, qword ptr [rax - 0x10]
00222B7C  0F B6 88 C3 00 00 00            movzx ecx, byte ptr [rax + 0xc3]
00222B83  80 F9 1E                        cmp cl, 0x1e
00222B86  8B C1                           mov eax, ecx
00222B88  B9 1E 00 00 00                  mov ecx, 0x1e
00222B8D  0F 4F C1                        cmovg eax, ecx
00222B90  3A C2                           cmp al, dl
00222B92  0F 8E BA F7 FF FF               jle 0x140222352
00222B98  88 45 5F                        mov byte ptr [rbp + 0x5f], al
00222B9B  E9 B2 F7 FF FF                  jmp 0x140222352
00222BA0  45 85 C9                        test r9d, r9d
00222BA3  0F 84 D5 F2 FF FF               je 0x140221e7e
00222BA9  E9 33 F4 FF FF                  jmp 0x140221fe1
00222BAE  45 85 C9                        test r9d, r9d
00222BB1  0F 84 63 F3 FF FF               je 0x140221f1a
00222BB7  E9 8A F5 FF FF                  jmp 0x140222146
00222BBC  41 0F B6 44 24 08               movzx eax, byte ptr [r12 + 8]
00222BC2  83 E0 3F                        and eax, 0x3f
00222BC5  48 6B C8 58                     imul rcx, rax, 0x58
00222BC9  49 8B C4                        mov rax, r12
00222BCC  48 2B C1                        sub rax, rcx
00222BCF  48 8B 40 F0                     mov rax, qword ptr [rax - 0x10]
00222BD3  0F B6 88 C3 00 00 00            movzx ecx, byte ptr [rax + 0xc3]
00222BDA  80 F9 1E                        cmp cl, 0x1e
00222BDD  8B C1                           mov eax, ecx
00222BDF  0F 4F C3                        cmovg eax, ebx
00222BE2  41 3A 44 24 28                  cmp al, byte ptr [r12 + 0x28]
00222BE7  0F 84 91 F2 FF FF               je 0x140221e7e
00222BED  E9 EF F3 FF FF                  jmp 0x140221fe1
00222BF2  41 0F B6 46 08                  movzx eax, byte ptr [r14 + 8]
00222BF7  83 E0 3F                        and eax, 0x3f
00222BFA  48 6B C8 58                     imul rcx, rax, 0x58
00222BFE  49 8B C6                        mov rax, r14
00222C01  48 2B C1                        sub rax, rcx
00222C04  48 8B 40 F0                     mov rax, qword ptr [rax - 0x10]
00222C08  0F B6 88 C3 00 00 00            movzx ecx, byte ptr [rax + 0xc3]
00222C0F  80 F9 1E                        cmp cl, 0x1e
00222C12  8B C1                           mov eax, ecx
00222C14  0F 4F C3                        cmovg eax, ebx
00222C17  41 3A 46 28                     cmp al, byte ptr [r14 + 0x28]
00222C1B  0F 84 F9 F2 FF FF               je 0x140221f1a
00222C21  E9 20 F5 FF FF                  jmp 0x140222146
00222C26  45 39 93 E0 05 00 00            cmp dword ptr [r11 + 0x5e0], r10d
00222C2D  0F 84 D4 F9 FF FF               je 0x140222607
00222C33  E9 B0 F9 FF FF                  jmp 0x1402225e8
00222C38  45 39 93 E0 05 00 00            cmp dword ptr [r11 + 0x5e0], r10d
00222C3F  0F 84 7E FE FF FF               je 0x140222ac3
00222C45  E9 5A FE FF FF                  jmp 0x140222aa4
00222C4A  41 0F B6 44 24 08               movzx eax, byte ptr [r12 + 8]
00222C50  BA 44 66 6C 74                  mov edx, 0x746c6644
00222C55  83 E0 3F                        and eax, 0x3f
00222C58  48 6B C8 58                     imul rcx, rax, 0x58
00222C5C  49 8B C4                        mov rax, r12
00222C5F  48 2B C1                        sub rax, rcx
00222C62  4C 8B 78 F0                     mov r15, qword ptr [rax - 0x10]
00222C66  49 8B CF                        mov rcx, r15
00222C69  E8 72 E2 FE FF                  call 0x140210ee0
00222C6E  84 C0                           test al, al
00222C70  0F 84 4B F7 FF FF               je 0x1402223c1
00222C76  41 F6 C6 01                     test r14b, 1
00222C7A  74 13                           je 0x140222c8f
00222C7C  BA 02 00 00 00                  mov edx, 2
00222C81  41 B8 00 00 00 80               mov r8d, 0x80000000
00222C87  49 8B CF                        mov rcx, r15
00222C8A  E8 81 34 FF FF                  call 0x140216110
00222C8F  41 F6 C6 02                     test r14b, 2
00222C93  74 08                           je 0x140222c9d
00222C95  49 8B CF                        mov rcx, r15
00222C98  E8 B7 2F FF FF                  call 0x140215c54
00222C9D  BA 44 66 6C 74                  mov edx, 0x746c6644
00222CA2  49 8B CF                        mov rcx, r15
00222CA5  E8 F6 11 04 00                  call 0x140263ea0
00222CAA  E9 12 F7 FF FF                  jmp 0x1402223c1
00222CAF  41 0F B6 46 08                  movzx eax, byte ptr [r14 + 8]
00222CB4  BA 44 66 6C 74                  mov edx, 0x746c6644
00222CB9  83 E0 3F                        and eax, 0x3f
00222CBC  48 6B C8 58                     imul rcx, rax, 0x58
00222CC0  49 8B C6                        mov rax, r14
00222CC3  48 2B C1                        sub rax, rcx
00222CC6  4C 8B 60 F0                     mov r12, qword ptr [rax - 0x10]
00222CCA  49 8B CC                        mov rcx, r12
00222CCD  E8 0E E2 FE FF                  call 0x140210ee0
00222CD2  84 C0                           test al, al
00222CD4  0F 84 95 F7 FF FF               je 0x14022246f
00222CDA  41 F6 C7 01                     test r15b, 1
00222CDE  74 13                           je 0x140222cf3
00222CE0  BA 02 00 00 00                  mov edx, 2
00222CE5  41 B8 00 00 00 80               mov r8d, 0x80000000
00222CEB  49 8B CC                        mov rcx, r12
00222CEE  E8 1D 34 FF FF                  call 0x140216110
00222CF3  41 F6 C7 02                     test r15b, 2
00222CF7  74 08                           je 0x140222d01
00222CF9  49 8B CC                        mov rcx, r12
00222CFC  E8 53 2F FF FF                  call 0x140215c54
00222D01  BA 44 66 6C 74                  mov edx, 0x746c6644
00222D06  49 8B CC                        mov rcx, r12
00222D09  E8 92 11 04 00                  call 0x140263ea0
00222D0E  E9 5C F7 FF FF                  jmp 0x14022246f
00222D13  48 85 D2                        test rdx, rdx
00222D16  74 4B                           je 0x140222d63
00222D18  49 33 D7                        xor rdx, r15
00222D1B  E9 BC F3 FF FF                  jmp 0x1402220dc
00222D20  48 85 D2                        test rdx, rdx
00222D23  74 46                           je 0x140222d6b
00222D25  49 33 D7                        xor rdx, r15
00222D28  E9 05 F5 FF FF                  jmp 0x140222232
00222D2D  0F B6 55 9F                     movzx edx, byte ptr [rbp - 0x61]
00222D31  E9 94 F5 FF FF                  jmp 0x1402222ca
00222D36  0F B6 55 5F                     movzx edx, byte ptr [rbp + 0x5f]
00222D3A  E9 07 F6 FF FF                  jmp 0x140222346
00222D3F  48 85 D2                        test rdx, rdx
00222D42  74 2F                           je 0x140222d73
00222D44  49 33 D6                        xor rdx, r14
00222D47  E9 D6 F7 FF FF                  jmp 0x140222522
00222D4C  49 8B 54 24 38                  mov rdx, qword ptr [r12 + 0x38]
00222D51  48 85 D2                        test rdx, rdx
00222D54  74 25                           je 0x140222d7b
00222D56  4D 8D 4C 24 38                  lea r9, [r12 + 0x38]
00222D5B  4C 33 CA                        xor r9, rdx
00222D5E  E9 9D F9 FF FF                  jmp 0x140222700
00222D63  45 32 C0                        xor r8b, r8b
00222D66  E9 1F F5 FF FF                  jmp 0x14022228a
00222D6B  45 32 C0                        xor r8b, r8b
00222D6E  E9 96 F5 FF FF                  jmp 0x140222309
00222D73  45 32 C0                        xor r8b, r8b
00222D76  E9 EF F7 FF FF                  jmp 0x14022256a
00222D7B  45 32 C0                        xor r8b, r8b
00222D7E  E9 C8 F9 FF FF                  jmp 0x14022274b
00222D83  48 85 D2                        test rdx, rdx
00222D86  74 15                           je 0x140222d9d
00222D88  49 33 D6                        xor rdx, r14
00222D8B  E9 A5 FA FF FF                  jmp 0x140222835
00222D90  48 85 D2                        test rdx, rdx
00222D93  74 10                           je 0x140222da5
00222D95  49 33 D7                        xor rdx, r15
00222D98  E9 50 FB FF FF                  jmp 0x1402228ed
00222D9D  45 32 C0                        xor r8b, r8b
00222DA0  E9 16 FC FF FF                  jmp 0x1402229bb
00222DA5  45 32 C0                        xor r8b, r8b
00222DA8  4D 8D 4E 10                     lea r9, [r14 + 0x10]
00222DAC  49 8B CF                        mov rcx, r15
00222DAF  E8 BC 17 0C 00                  call 0x1402e4570
00222DB4  83 CB 20                        or ebx, 0x20
00222DB7  E9 9D F6 FF FF                  jmp 0x140222459
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00221FB6(void)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbx;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;

    if ((*(unsigned __int8 *)(v_r12 + 9)) != 0) goto loc_00222BBC;
    result = KiAbOwnerComputeCpuPriorityKey(v_r12, a2, a3, a4);
    if (((unsigned __int8)(result)) == (*(unsigned __int8 *)(v_r12 + 40))) goto loc_0022240F;
loc_00221FE1:
    result = 0;
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) & (7));
    *(unsigned __int64 *)(v_rbp - 9) = 0;
    *(unsigned int *)(v_rbp - 97) = 0;
    *(unsigned int *)(v_rbp - 65) = 0;
    v_rbx = (unsigned int)((v_rbx) << (6));
    result = (*(unsigned __int64 *)(v_r12)) & (v_r11);
    *(unsigned __int64 *)(v_rbp - 49) = result;
    *(unsigned __int64 *)(v_rbp - 25) = v_xmm0;
    if (condition_is_equal) goto loc_00222018;
    if ((*(unsigned __int8 *)(v_r12 + 8)) >= 0) {
        result = (result) | (v_r10);
        *(unsigned __int64 *)(v_rbp - 49) = result;
    }
    result = KiAbEntryGetLockedHeadEntry(v_r12, (unsigned int)((unsigned int)(v_rsi)), v_rbp - 25, a4);
    *(unsigned __int64 *)(v_rbp - 33) = result;
    if (result == 0) goto loc_002223C5;
    result = (unsigned __int8)(-((unsigned __int8)(*(unsigned __int8 *)(v_r12 + 9))));
    a1 = (unsigned int)((v_r12) & (8));
    v_rbx = (unsigned int)((v_rbx) | ((unsigned int)(a1)));
    if ((unsigned __int8)(*(unsigned __int8 *)(v_r12 + 9)) != 0) goto loc_002224AE;
    if ((*(unsigned int *)(v_rbp - 93)) == 0) goto loc_002223AB;
    if (v_r12 == result) goto loc_0022229E;
    *(unsigned int *)(v_rbp - 41) = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r12 + 80))) & (0x3FFFFFFFULL));
    if (condition_is_above) goto loc_00222AEF;
loc_0022207A:
    result = (unsigned int)((*(unsigned __int8 *)(v_r12 + 8)) & (63));
    a1 = (a1) * (result);
    result = (v_r12) - (a1);
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(result - 16) + 563))) <= ((unsigned __int8)(*(unsigned __int8 *)(v_r12 + 9)))) goto loc_002220A6;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(result - 16) + 563))) >= = 30) {
        a2 = 30;
    }
    if ((*(unsigned __int8 *)(v_r12 + 40)) == ((unsigned __int8)(a2))) goto loc_0022229B;
    *(unsigned __int8 *)(v_r12 + 40) = (unsigned __int8)(a2);
    v_r15 = (result) + (40);
    result = RtlRbRemoveNode(v_r15, v_r12 + 16, v_rbp - 25, a4);
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r15 + 8))) & (1)) != 0) goto loc_00222D13;
loc_002220DC:
    a3 = 0;
    a4 = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)(v_r15 + 8))) & (1));
    if (*(unsigned __int64 *)(v_r15) == 0) goto loc_0022228A;
loc_002220F0:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_r15) + 24)) <= ((unsigned __int8)(*(unsigned __int8 *)(v_r12 + 40)))) goto loc_00222271;
    if ((unsigned int)(a4) == 0) goto loc_0022210D;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15)) == 0) goto loc_0022228A;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15))) ^ (*(unsigned __int64 *)(v_r15));
loc_0022210D:
    if (result == 0) goto loc_0022228A;
loc_00222116:
    goto loc_002220F0;
loc_00222271:
    if ((unsigned int)(a4) == 0) goto loc_002227A1;
    if (*(unsigned __int64 *)(result + 8) != 0) goto loc_0022279E;
loc_00222287:
loc_0022228A:
    result = RtlRbInsertNodeEx(v_r15, result, 1, v_r12 + 16);
loc_0022229B:
    v_rbx = (unsigned int)((v_rbx) | (16));
loc_0022229E:
    if ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbp - 33) + 84))) != 0) {
        *(unsigned __int8 *)(v_rbp - 96) = 2;
    }
    if (!(condition_is_below_or_equal)) {
        *(unsigned __int8 *)(v_rbp - 95) = 1;
    }
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 33) + 64) == 0) goto loc_00222D2D;
    *(unsigned __int8 *)(v_rbp - 97) = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 33) + 64) + 24));
loc_002222CA:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 33) + 9)) != 0) goto loc_00222B2B;
loc_002222D5:
    if ((*(unsigned int *)(v_rbp - 97)) != 0) goto loc_002227C0;
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(v_rbp - 25, *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 33) + 64) + 24), 1, v_r12 + 16);
    v_rbx = (unsigned int)((v_rbx) | (1));
    goto loc_002223C5;
loc_0022236D:
    if ((unsigned int)(v_r10) != 0) {
        result = *(unsigned __int64 *)(v_rbp + 127);
        a2 = (unsigned int)(v_r10);
        a4 = *(unsigned __int64 *)(v_rbp + 119);
        a1 = *(unsigned __int64 *)(v_rbp - 33);
        a3 = *(unsigned __int64 *)(v_rbp + 111);
        v_stack_p20 = result;
        result = KiAbIoBoostOwners(a1, a2, a3, a4);
    }
    v_stack_p20 = *(unsigned __int64 *)(v_rbp + 127);
    result = KiAbCpuBoostOwners(*(unsigned __int64 *)(v_rbp - 33), (unsigned __int8)(v_r14), *(unsigned __int64 *)(v_rbp + 111), *(unsigned __int64 *)(v_rbp + 119));
loc_002223AB:
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(v_rbp - 25, (unsigned __int8)(v_r14), *(unsigned __int64 *)(v_rbp + 111), *(unsigned __int64 *)(v_rbp + 119));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbp - 65))) != 0) goto loc_00222C4A;
loc_002223C1:
loc_002223C5:
    if (((*(unsigned int *)(v_rip + 14305093)) & (0x1000ULL)) != 0) {
        result = *(unsigned __int8 *)(v_r12 + 8);
        a2 = *(unsigned __int64 *)(v_rbp - 49);
        result = (unsigned int)((result) & (63));
        a3 = (*(unsigned __int64 *)(v_rbp + 111)) * (result);
        v_r12 = (v_r12) - (a3);
        a3 = (unsigned int)(v_rbx);
        a1 = *(unsigned __int64 *)(v_r12 - 16);
        result = EtwTraceAutoBoostProcessLockEntry(a1, a2, a3, *(unsigned __int64 *)(v_rbp + 119));
    }
loc_0022240F:
loc_002224AE:
    if ((*(unsigned int *)(v_rbp - 89)) == 0) goto loc_002223AB;
    if (v_r12 == (*(unsigned __int64 *)(v_rbp - 33))) goto loc_0022257A;
    result = (unsigned int)((*(unsigned __int8 *)(v_r12 + 8)) & (63));
    a1 = (a1) * (result);
    result = (v_r12) - (a1);
    result = (unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(result - 16) + 195)));
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(result - 16) + 195))) > 30) { result = 30; }
    if ((*(unsigned __int8 *)(v_r12 + 40)) == ((unsigned __int8)(result))) goto loc_00222577;
    *(unsigned __int8 *)(v_r12 + 40) = (unsigned __int8)(result);
    result = RtlRbRemoveNode(*(unsigned __int64 *)(v_rbp - 33) + 56, v_r12 + 16, *(unsigned __int64 *)(v_rbp - 73), (unsigned int)(*(unsigned int *)(v_rbp - 89)));
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 33) + 56 + 8))) & (1)) != 0) goto loc_00222D3F;
loc_00222522:
    a3 = 0;
    a4 = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 33) + 56 + 8))) & (1));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 33) + 56) == 0) goto loc_0022256A;
loc_00222532:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 33) + 56) + 24)) >= ((unsigned __int8)(*(unsigned __int8 *)(v_r12 + 40)))) goto loc_00222551;
    if ((unsigned int)(a4) == 0) goto loc_00222547;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 33) + 56)) == 0) goto loc_0022256A;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 33) + 56))) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 33) + 56));
loc_00222547:
    if (result == 0) goto loc_0022256A;
loc_0022254C:
    goto loc_00222532;
loc_00222551:
    if ((unsigned int)(a4) == 0) goto loc_00222A56;
    if (*(unsigned __int64 *)(result + 8) != 0) goto loc_00222A53;
loc_00222567:
loc_0022256A:
    result = RtlRbInsertNodeEx(*(unsigned __int64 *)(v_rbp - 33) + 56, result, 1, v_r12 + 16);
loc_00222577:
    v_rbx = (unsigned int)((30) | (32));
loc_0022257A:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 33) + 48) != 0) goto loc_00222A3F;
loc_0022258A:
    *(unsigned __int8 *)(v_rbp - 97) = 30;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 33) + 9)) == 0) goto loc_002229FD;
loc_00222599:
    if ((*(unsigned __int8 *)(v_r12 + 9)) == 0) goto loc_0022292C;
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(v_r12 + 11))) & (6));
    if (((unsigned __int8)(result)) == 6) goto loc_0022292C;
    v_r10 = 0;
    result = (unsigned int)((*(unsigned __int8 *)(v_r12 + 8)) & (63));
    a1 = (*(unsigned __int64 *)(v_rbp - 33) + 56) * (result);
    result = (v_r12) - (a1);
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_r12 + 11))) & (2)) != 0) goto loc_00222607;
    result = PsGetIoPriorityThread(*(unsigned __int64 *)(result - 16), *(unsigned __int8 *)(v_r12 + 11), 1, 30);
    if (((unsigned int)(result)) < 2) goto loc_00222C26;
loc_002225E8:
    result = (unsigned __int8)((*(unsigned __int8 *)(v_r12 + 11)) | (2));
    *(unsigned __int8 *)(v_r12 + 11) = (unsigned __int8)(result);
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 33) + 84)) == 1) { v_r10 = (unsigned int)(v_r13); }
loc_00222607:
    if (((*(unsigned __int8 *)(v_r12 + 11)) & (4)) != 0) goto loc_00222661;
    if ((*(unsigned int *)(*(unsigned __int64 *)(result - 16) + 1512)) == 0) goto loc_00222623;
    if ((*(unsigned int *)(*(unsigned __int64 *)(result - 16) + 1508)) == 0) goto loc_00222661;
loc_00222623:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbp - 33) + 84)) + 256) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbp - 33) + 84)))));
    a1 = (unsigned int)((a1) & (0x7F00ULL));
    a1 = (unsigned int)((a1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbp - 33) + 84)))));
    *(unsigned int *)(*(unsigned __int64 *)(v_rbp - 33) + 84) = (unsigned int)(a1);
    result = (unsigned __int8)((*(unsigned __int8 *)(v_r12 + 11)) | (4));
    *(unsigned __int8 *)(v_r12 + 11) = (unsigned __int8)(result);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbp - 33) + 84))) & (0x7F00ULL));
    if (((unsigned int)(result)) == 256) {
        v_r10 = (unsigned int)((v_r10) | (2));
    }
    result = KiAbEntryGetCpuPriorityKey(v_r12, *(unsigned __int8 *)(v_r12 + 11), 1, *(unsigned __int8 *)(v_rbp - 97));
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rbp - 97))) < ((unsigned __int8)(result))) goto loc_0022236D;
    if ((unsigned int)(v_r10) != 0) goto loc_00222372;
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(v_rbp - 25, *(unsigned __int8 *)(v_r12 + 11), 1, *(unsigned __int8 *)(v_rbp - 97));
    v_rbx = (unsigned int)((v_rbx) | (2));
    goto loc_002223C1;
loc_0022279E:
    result = (result) ^ (*(unsigned __int8 *)(v_r12 + 11));
loc_002227A1:
    if (result != 0) goto loc_00222116;
    goto loc_00222287;
loc_002227C0:
    v_stack_p28 = v_rbp - 65;
    v_stack_p20 = *(unsigned __int64 *)(v_rbp + 127);
    result = KiAbSetMinimumThreadPriority(v_r12, v_rbp - 97, *(unsigned __int64 *)(v_rbp + 111), *(unsigned __int64 *)(v_rbp + 119));
    if ((unsigned int)(result) == 0) goto loc_002223AB;
    if (v_r12 == (*(unsigned __int64 *)(v_rbp - 33))) goto loc_002223AB;
    result = KiAbOwnerComputeCpuPriorityKey(v_r12, v_rbp - 97, *(unsigned __int64 *)(v_rbp + 111), *(unsigned __int64 *)(v_rbp + 119));
    if ((*(unsigned __int8 *)(v_r12 + 40)) == ((unsigned __int8)(result))) goto loc_002229C8;
    *(unsigned __int8 *)(v_r12 + 40) = (unsigned __int8)(result);
    result = RtlRbRemoveNode(*(unsigned __int64 *)(v_rbp - 33) + 40, v_r12 + 16, *(unsigned __int64 *)(v_rbp + 111), *(unsigned __int64 *)(v_rbp + 119));
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 33) + 40 + 8))) & (1)) != 0) goto loc_00222D83;
loc_00222835:
    a3 = 0;
    a4 = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 33) + 40 + 8))) & (1));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 33) + 40) == 0) goto loc_002229BB;
loc_00222850:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 33) + 40) + 24)) <= ((unsigned __int8)(*(unsigned __int8 *)(v_r12 + 40)))) goto loc_002229A2;
    if ((unsigned int)(a4) == 0) goto loc_0022286D;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 33) + 40)) == 0) goto loc_002229BB;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 33) + 40))) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 33) + 40));
loc_0022286D:
    if (result == 0) goto loc_002229BB;
loc_00222876:
    goto loc_00222850;
loc_0022292C:
    v_r10 = 0;
    goto loc_00222661;
loc_002229A2:
    if ((unsigned int)(a4) == 0) goto loc_00222B0C;
    if (*(unsigned __int64 *)(result + 8) != 0) goto loc_00222B09;
loc_002229B8:
loc_002229BB:
    result = RtlRbInsertNodeEx(*(unsigned __int64 *)(v_rbp - 33) + 40, result, 1, v_r12 + 16);
loc_002229C8:
    v_rbx = (unsigned int)((v_rbx) | (32));
    goto loc_002223AB;
loc_002229FD:
    result = KiAbOwnerComputeCpuPriorityKey(*(unsigned __int64 *)(v_rbp - 33), result, 1, v_r12 + 16);
    a2 = (unsigned __int8)(v_r12 + 16);
    if (((unsigned __int8)(result)) < ((unsigned __int8)(v_r12 + 16))) { a2 = (unsigned int)((unsigned __int8)(result)); }
    *(unsigned __int8 *)(v_rbp - 97) = (unsigned __int8)(a2);
    goto loc_00222599;
loc_00222A3F:
    goto loc_0022258A;
loc_00222A53:
    result = (result) ^ (a2);
loc_00222A56:
    if (result != 0) goto loc_0022254C;
    goto loc_00222567;
loc_00222AEF:
    *(unsigned int *)(v_rbp - 41) = (unsigned int)(a2);
    a2 = (unsigned __int8)((a2) + 1);
    goto loc_0022207A;
loc_00222B09:
    result = (result) ^ (a2);
loc_00222B0C:
    if (result != 0) goto loc_00222876;
    goto loc_002229B8;
loc_00222B2B:
    result = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 33) + 8)) & (63));
    a1 = ((unsigned __int8)(result)) * (result);
    result = (*(unsigned __int64 *)(v_rbp - 33)) - (a1);
    result = (unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(result - 16) + 195)));
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(result - 16) + 195))) > 30) { result = 30; }
    if (((unsigned __int8)(result)) <= ((unsigned __int8)(a2))) goto loc_002222D5;
    *(unsigned __int8 *)(v_rbp - 97) = (unsigned __int8)(result);
    goto loc_002222D5;
loc_00222BBC:
    result = (unsigned int)((*(unsigned __int8 *)(v_r12 + 8)) & (63));
    a1 = (30) * (result);
    result = (v_r12) - (a1);
    result = (unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(result - 16) + 195)));
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(result - 16) + 195))) > 30) { result = (unsigned int)(v_rbx); }
    goto loc_00221FE1;
loc_00222C26:
    if ((*(unsigned int *)(*(unsigned __int64 *)(result - 16) + 1504)) == 0) goto loc_00222607;
    goto loc_002225E8;
loc_00222C4A:
    result = (unsigned int)((*(unsigned __int8 *)(v_r12 + 8)) & (63));
    a1 = (*(unsigned __int8 *)(*(unsigned __int64 *)(result - 16) + 195)) * (result);
    result = (v_r12) - (a1);
    result = ObReferenceObjectSafeWithTag(*(unsigned __int64 *)(result - 16), (unsigned int)(0x746C6644ULL), 1, *(unsigned __int8 *)(result + 24));
    if ((unsigned __int8)(result) == 0) goto loc_002223C1;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rbp - 33) + 40)) & (1)) != 0) {
        a2 = 2;
        a3 = 0x80000000ULL;
        a1 = *(unsigned __int64 *)(result - 16);
        result = IoBoostThreadIoPriority(a1, a2, a3, *(unsigned __int8 *)(result + 24));
    }
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rbp - 33) + 40)) & (2)) != 0) {
        a1 = *(unsigned __int64 *)(result - 16);
        result = PsBoostThreadOutstandingIoQoS(a1, a2, a3, *(unsigned __int8 *)(result + 24));
    }
    result = ObDereferenceObjectDeferDeleteWithTag(*(unsigned __int64 *)(result - 16), (unsigned int)(0x746C6644ULL), a3, *(unsigned __int8 *)(result + 24));
    goto loc_002223C1;
loc_00222D13:
    if ((unsigned int)(0x746C6644ULL) == 0) goto loc_00222D63;
    a2 = ((unsigned int)(0x746C6644ULL)) ^ (*(unsigned __int64 *)(result - 16));
    goto loc_002220DC;
loc_00222D2D:
    goto loc_002222CA;
loc_00222D3F:
    if (*(unsigned __int8 *)(v_rbp - 97) == 0) goto loc_00222D73;
    a2 = (*(unsigned __int8 *)(v_rbp - 97)) ^ (*(unsigned __int64 *)(v_rbp - 33) + 40);
    goto loc_00222522;
loc_00222D63:
    a3 = 0;
    goto loc_0022228A;
loc_00222D73:
    a3 = 0;
    goto loc_0022256A;
loc_00222D83:
    if (a2 == 0) goto loc_00222D9D;
    a2 = (a2) ^ (*(unsigned __int64 *)(v_rbp - 33) + 40);
    goto loc_00222835;
loc_00222D9D:
    a3 = 0;
    goto loc_002229BB;
}
```

## 5. (Beta) C Style

```c
void sub_00221FB6(void)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbx;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;

    if ((*(uint8_t *)(local_r12 + 0x9)) != 0) goto loc_00222BBC;
    result = KiAbOwnerComputeCpuPriorityKey(local_r12, a2, a3, a4);
    if (((uint8_t)(result)) == (*(uint8_t *)(local_r12 + 0x28))) goto loc_0022240F;
loc_00221FE1:
    result = 0;
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) & (7));
    *(uint64_t *)(local_rbp - 0x9) = 0;
    *(uint32_t *)(local_rbp - 0x61) = 0;
    *(uint32_t *)(local_rbp - 0x41) = 0;
    local_rbx = (uint32_t)((local_rbx) << (6));
    result = (*(uint64_t *)(local_r12)) & (local_r11);
    *(uint64_t *)(local_rbp - 0x31) = result;
    *(uint64_t *)(local_rbp - 0x19) = v_xmm0;
    if (condition_is_equal) goto loc_00222018;
    if ((*(uint8_t *)(local_r12 + 0x8)) >= 0) {
        result = (result) | (local_r10);
        *(uint64_t *)(local_rbp - 0x31) = result;
    }
    result = KiAbEntryGetLockedHeadEntry(local_r12, (uint32_t)((uint32_t)(local_rsi)), local_rbp - 25, a4);
    *(uint64_t *)(local_rbp - 0x21) = result;
    if (result == 0) goto loc_002223C5;
    result = (uint8_t)(-((uint8_t)(*(uint8_t *)(local_r12 + 0x9))));
    a1 = (uint32_t)((local_r12) & (8));
    local_rbx = (uint32_t)((local_rbx) | ((uint32_t)(a1)));
    if ((uint8_t)(*(uint8_t *)(local_r12 + 0x9)) != 0) goto loc_002224AE;
    if ((*(uint32_t *)(local_rbp - 0x5D)) == 0) goto loc_002223AB;
    if (local_r12 == result) goto loc_0022229E;
    *(uint32_t *)(local_rbp - 0x29) = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r12 + 0x50))) & (0x3FFFFFFFULL));
    if (condition_is_above) goto loc_00222AEF;
loc_0022207A:
    result = (uint32_t)((*(uint8_t *)(local_r12 + 0x8)) & (63));
    a1 = (a1) * (result);
    result = (local_r12) - (a1);
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(result - 0x10) + 0x233))) <= ((uint8_t)(*(uint8_t *)(local_r12 + 0x9)))) goto loc_002220A6;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(result - 0x10) + 0x233))) >= = 30) {
        a2 = 30;
    }
    if ((*(uint8_t *)(local_r12 + 0x28)) == ((uint8_t)(a2))) goto loc_0022229B;
    *(uint8_t *)(local_r12 + 0x28) = (uint8_t)(a2);
    local_r15 = (result) + (40);
    result = RtlRbRemoveNode(local_r15, local_r12 + 16, local_rbp - 25, a4);
    if ((((uint8_t)(*(uint64_t *)(local_r15 + 0x8))) & (1)) != 0) goto loc_00222D13;
loc_002220DC:
    a3 = 0;
    a4 = (uint32_t)(((uint8_t)(*(uint64_t *)(local_r15 + 0x8))) & (1));
    if (*(uint64_t *)(local_r15) == 0) goto loc_0022228A;
loc_002220F0:
    if ((*(uint8_t *)(*(uint64_t *)(local_r15) + 0x18)) <= ((uint8_t)(*(uint8_t *)(local_r12 + 0x28)))) goto loc_00222271;
    if ((uint32_t)(a4) == 0) goto loc_0022210D;
    if (*(uint64_t *)(*(uint64_t *)(local_r15)) == 0) goto loc_0022228A;
    result = (*(uint64_t *)(*(uint64_t *)(local_r15))) ^ (*(uint64_t *)(local_r15));
loc_0022210D:
    if (result == 0) goto loc_0022228A;
loc_00222116:
    goto loc_002220F0;
loc_00222271:
    if ((uint32_t)(a4) == 0) goto loc_002227A1;
    if (*(uint64_t *)(result + 0x8) != 0) goto loc_0022279E;
loc_00222287:
loc_0022228A:
    result = RtlRbInsertNodeEx(local_r15, result, 1, local_r12 + 16);
loc_0022229B:
    local_rbx = (uint32_t)((local_rbx) | (16));
loc_0022229E:
    if ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbp - 0x21) + 0x54))) != 0) {
        *(uint8_t *)(local_rbp - 0x60) = 2;
    }
    if (!(condition_is_below_or_equal)) {
        *(uint8_t *)(local_rbp - 0x5F) = 1;
    }
    if (*(uint64_t *)(*(uint64_t *)(local_rbp - 0x21) + 0x40) == 0) goto loc_00222D2D;
    *(uint8_t *)(local_rbp - 0x61) = (uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x21) + 0x40) + 0x18));
loc_002222CA:
    if ((*(uint8_t *)(*(uint64_t *)(local_rbp - 0x21) + 0x9)) != 0) goto loc_00222B2B;
loc_002222D5:
    if ((*(uint32_t *)(local_rbp - 0x61)) != 0) goto loc_002227C0;
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(local_rbp - 25, *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x21) + 0x40) + 0x18), 1, local_r12 + 16);
    local_rbx = (uint32_t)((local_rbx) | (1));
    goto loc_002223C5;
loc_0022236D:
    if ((uint32_t)(local_r10) != 0) {
        result = *(uint64_t *)(local_rbp + 0x7F);
        a2 = (uint32_t)(local_r10);
        a4 = *(uint64_t *)(local_rbp + 0x77);
        a1 = *(uint64_t *)(local_rbp - 0x21);
        a3 = *(uint64_t *)(local_rbp + 0x6F);
        v_stack_p20 = result;
        result = KiAbIoBoostOwners(a1, a2, a3, a4);
    }
    v_stack_p20 = *(uint64_t *)(local_rbp + 0x7F);
    result = KiAbCpuBoostOwners(*(uint64_t *)(local_rbp - 0x21), (uint8_t)(local_r14), *(uint64_t *)(local_rbp + 0x6F), *(uint64_t *)(local_rbp + 0x77));
loc_002223AB:
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(local_rbp - 25, (uint8_t)(local_r14), *(uint64_t *)(local_rbp + 0x6F), *(uint64_t *)(local_rbp + 0x77));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbp - 0x41))) != 0) goto loc_00222C4A;
loc_002223C1:
loc_002223C5:
    if (((*(uint32_t *)(v_rip + 0xDA4745)) & (0x1000ULL)) != 0) {
        result = *(uint8_t *)(local_r12 + 0x8);
        a2 = *(uint64_t *)(local_rbp - 0x31);
        result = (uint32_t)((result) & (63));
        a3 = (*(uint64_t *)(local_rbp + 0x6F)) * (result);
        local_r12 = (local_r12) - (a3);
        a3 = (uint32_t)(local_rbx);
        a1 = *(uint64_t *)(local_r12 - 0x10);
        result = EtwTraceAutoBoostProcessLockEntry(a1, a2, a3, *(uint64_t *)(local_rbp + 0x77));
    }
loc_0022240F:
loc_002224AE:
    if ((*(uint32_t *)(local_rbp - 0x59)) == 0) goto loc_002223AB;
    if (local_r12 == (*(uint64_t *)(local_rbp - 0x21))) goto loc_0022257A;
    result = (uint32_t)((*(uint8_t *)(local_r12 + 0x8)) & (63));
    a1 = (a1) * (result);
    result = (local_r12) - (a1);
    result = (uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(result - 0x10) + 0xC3)));
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(result - 0x10) + 0xC3))) > 30) { result = 30; }
    if ((*(uint8_t *)(local_r12 + 0x28)) == ((uint8_t)(result))) goto loc_00222577;
    *(uint8_t *)(local_r12 + 0x28) = (uint8_t)(result);
    result = RtlRbRemoveNode(*(uint64_t *)(local_rbp - 0x21) + 56, local_r12 + 16, *(uint64_t *)(local_rbp - 0x49), (uint32_t)(*(uint32_t *)(local_rbp - 0x59)));
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x21) + 0x38 + 0x8))) & (1)) != 0) goto loc_00222D3F;
loc_00222522:
    a3 = 0;
    a4 = (uint32_t)(((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x21) + 0x38 + 0x8))) & (1));
    if (*(uint64_t *)(*(uint64_t *)(local_rbp - 0x21) + 0x38) == 0) goto loc_0022256A;
loc_00222532:
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x21) + 0x38) + 0x18)) >= ((uint8_t)(*(uint8_t *)(local_r12 + 0x28)))) goto loc_00222551;
    if ((uint32_t)(a4) == 0) goto loc_00222547;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x21) + 0x38)) == 0) goto loc_0022256A;
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x21) + 0x38))) ^ (*(uint64_t *)(*(uint64_t *)(local_rbp - 0x21) + 0x38));
loc_00222547:
    if (result == 0) goto loc_0022256A;
loc_0022254C:
    goto loc_00222532;
loc_00222551:
    if ((uint32_t)(a4) == 0) goto loc_00222A56;
    if (*(uint64_t *)(result + 0x8) != 0) goto loc_00222A53;
loc_00222567:
loc_0022256A:
    result = RtlRbInsertNodeEx(*(uint64_t *)(local_rbp - 0x21) + 56, result, 1, local_r12 + 16);
loc_00222577:
    local_rbx = (uint32_t)((30) | (32));
loc_0022257A:
    if (*(uint64_t *)(*(uint64_t *)(local_rbp - 0x21) + 0x30) != 0) goto loc_00222A3F;
loc_0022258A:
    *(uint8_t *)(local_rbp - 0x61) = 30;
    if ((*(uint8_t *)(*(uint64_t *)(local_rbp - 0x21) + 0x9)) == 0) goto loc_002229FD;
loc_00222599:
    if ((*(uint8_t *)(local_r12 + 0x9)) == 0) goto loc_0022292C;
    result = (uint8_t)(((uint8_t)(*(uint8_t *)(local_r12 + 0xB))) & (6));
    if (((uint8_t)(result)) == 6) goto loc_0022292C;
    local_r10 = 0;
    result = (uint32_t)((*(uint8_t *)(local_r12 + 0x8)) & (63));
    a1 = (*(uint64_t *)(local_rbp - 0x21) + 56) * (result);
    result = (local_r12) - (a1);
    if ((((uint8_t)(*(uint8_t *)(local_r12 + 0xB))) & (2)) != 0) goto loc_00222607;
    result = PsGetIoPriorityThread(*(uint64_t *)(result - 0x10), *(uint8_t *)(local_r12 + 0xB), 1, 30);
    if (((uint32_t)(result)) < 2) goto loc_00222C26;
loc_002225E8:
    result = (uint8_t)((*(uint8_t *)(local_r12 + 0xB)) | (2));
    *(uint8_t *)(local_r12 + 0xB) = (uint8_t)(result);
    if ((*(uint8_t *)(*(uint64_t *)(local_rbp - 0x21) + 0x54)) == 1) { local_r10 = (uint32_t)(local_r13); }
loc_00222607:
    if (((*(uint8_t *)(local_r12 + 0xB)) & (4)) != 0) goto loc_00222661;
    if ((*(uint32_t *)(*(uint64_t *)(result - 0x10) + 0x5E8)) == 0) goto loc_00222623;
    if ((*(uint32_t *)(*(uint64_t *)(result - 0x10) + 0x5E4)) == 0) goto loc_00222661;
loc_00222623:
    a1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbp - 0x21) + 0x54)) + 256) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbp - 0x21) + 0x54)))));
    a1 = (uint32_t)((a1) & (0x7F00ULL));
    a1 = (uint32_t)((a1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbp - 0x21) + 0x54)))));
    *(uint32_t *)(*(uint64_t *)(local_rbp - 0x21) + 0x54) = (uint32_t)(a1);
    result = (uint8_t)((*(uint8_t *)(local_r12 + 0xB)) | (4));
    *(uint8_t *)(local_r12 + 0xB) = (uint8_t)(result);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbp - 0x21) + 0x54))) & (0x7F00ULL));
    if (((uint32_t)(result)) == 256) {
        local_r10 = (uint32_t)((local_r10) | (2));
    }
    result = KiAbEntryGetCpuPriorityKey(local_r12, *(uint8_t *)(local_r12 + 0xB), 1, *(uint8_t *)(local_rbp - 0x61));
    if (((uint8_t)(*(uint8_t *)(local_rbp - 0x61))) < ((uint8_t)(result))) goto loc_0022236D;
    if ((uint32_t)(local_r10) != 0) goto loc_00222372;
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(local_rbp - 25, *(uint8_t *)(local_r12 + 0xB), 1, *(uint8_t *)(local_rbp - 0x61));
    local_rbx = (uint32_t)((local_rbx) | (2));
    goto loc_002223C1;
loc_0022279E:
    result = (result) ^ (*(uint8_t *)(local_r12 + 0xB));
loc_002227A1:
    if (result != 0) goto loc_00222116;
    goto loc_00222287;
loc_002227C0:
    v_stack_p28 = local_rbp - 65;
    v_stack_p20 = *(uint64_t *)(local_rbp + 0x7F);
    result = KiAbSetMinimumThreadPriority(local_r12, local_rbp - 97, *(uint64_t *)(local_rbp + 0x6F), *(uint64_t *)(local_rbp + 0x77));
    if ((uint32_t)(result) == 0) goto loc_002223AB;
    if (local_r12 == (*(uint64_t *)(local_rbp - 0x21))) goto loc_002223AB;
    result = KiAbOwnerComputeCpuPriorityKey(local_r12, local_rbp - 97, *(uint64_t *)(local_rbp + 0x6F), *(uint64_t *)(local_rbp + 0x77));
    if ((*(uint8_t *)(local_r12 + 0x28)) == ((uint8_t)(result))) goto loc_002229C8;
    *(uint8_t *)(local_r12 + 0x28) = (uint8_t)(result);
    result = RtlRbRemoveNode(*(uint64_t *)(local_rbp - 0x21) + 40, local_r12 + 16, *(uint64_t *)(local_rbp + 0x6F), *(uint64_t *)(local_rbp + 0x77));
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x21) + 0x28 + 0x8))) & (1)) != 0) goto loc_00222D83;
loc_00222835:
    a3 = 0;
    a4 = (uint32_t)(((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x21) + 0x28 + 0x8))) & (1));
    if (*(uint64_t *)(*(uint64_t *)(local_rbp - 0x21) + 0x28) == 0) goto loc_002229BB;
loc_00222850:
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x21) + 0x28) + 0x18)) <= ((uint8_t)(*(uint8_t *)(local_r12 + 0x28)))) goto loc_002229A2;
    if ((uint32_t)(a4) == 0) goto loc_0022286D;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x21) + 0x28)) == 0) goto loc_002229BB;
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x21) + 0x28))) ^ (*(uint64_t *)(*(uint64_t *)(local_rbp - 0x21) + 0x28));
loc_0022286D:
    if (result == 0) goto loc_002229BB;
loc_00222876:
    goto loc_00222850;
loc_0022292C:
    local_r10 = 0;
    goto loc_00222661;
loc_002229A2:
    if ((uint32_t)(a4) == 0) goto loc_00222B0C;
    if (*(uint64_t *)(result + 0x8) != 0) goto loc_00222B09;
loc_002229B8:
loc_002229BB:
    result = RtlRbInsertNodeEx(*(uint64_t *)(local_rbp - 0x21) + 40, result, 1, local_r12 + 16);
loc_002229C8:
    local_rbx = (uint32_t)((local_rbx) | (32));
    goto loc_002223AB;
loc_002229FD:
    result = KiAbOwnerComputeCpuPriorityKey(*(uint64_t *)(local_rbp - 0x21), result, 1, local_r12 + 16);
    a2 = (uint8_t)(local_r12 + 16);
    if (((uint8_t)(result)) < ((uint8_t)(local_r12 + 16))) { a2 = (uint32_t)((uint8_t)(result)); }
    *(uint8_t *)(local_rbp - 0x61) = (uint8_t)(a2);
    goto loc_00222599;
loc_00222A3F:
    goto loc_0022258A;
loc_00222A53:
    result = (result) ^ (a2);
loc_00222A56:
    if (result != 0) goto loc_0022254C;
    goto loc_00222567;
loc_00222AEF:
    *(uint32_t *)(local_rbp - 0x29) = (uint32_t)(a2);
    a2 = (uint8_t)((a2) + 1);
    goto loc_0022207A;
loc_00222B09:
    result = (result) ^ (a2);
loc_00222B0C:
    if (result != 0) goto loc_00222876;
    goto loc_002229B8;
loc_00222B2B:
    result = (uint32_t)((*(uint8_t *)(*(uint64_t *)(local_rbp - 0x21) + 0x8)) & (63));
    a1 = ((uint8_t)(result)) * (result);
    result = (*(uint64_t *)(local_rbp - 0x21)) - (a1);
    result = (uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(result - 0x10) + 0xC3)));
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(result - 0x10) + 0xC3))) > 30) { result = 30; }
    if (((uint8_t)(result)) <= ((uint8_t)(a2))) goto loc_002222D5;
    *(uint8_t *)(local_rbp - 0x61) = (uint8_t)(result);
    goto loc_002222D5;
loc_00222BBC:
    result = (uint32_t)((*(uint8_t *)(local_r12 + 0x8)) & (63));
    a1 = (30) * (result);
    result = (local_r12) - (a1);
    result = (uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(result - 0x10) + 0xC3)));
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(result - 0x10) + 0xC3))) > 30) { result = (uint32_t)(local_rbx); }
    goto loc_00221FE1;
loc_00222C26:
    if ((*(uint32_t *)(*(uint64_t *)(result - 0x10) + 0x5E0)) == 0) goto loc_00222607;
    goto loc_002225E8;
loc_00222C4A:
    result = (uint32_t)((*(uint8_t *)(local_r12 + 0x8)) & (63));
    a1 = (*(uint8_t *)(*(uint64_t *)(result - 0x10) + 0xC3)) * (result);
    result = (local_r12) - (a1);
    result = ObReferenceObjectSafeWithTag(*(uint64_t *)(result - 0x10), (uint32_t)(0x746C6644ULL), 1, *(uint8_t *)(result + 0x18));
    if ((uint8_t)(result) == 0) goto loc_002223C1;
    if ((((uint8_t)(*(uint64_t *)(local_rbp - 0x21) + 40)) & (1)) != 0) {
        a2 = 2;
        a3 = 0x80000000ULL;
        a1 = *(uint64_t *)(result - 0x10);
        result = IoBoostThreadIoPriority(a1, a2, a3, *(uint8_t *)(result + 0x18));
    }
    if ((((uint8_t)(*(uint64_t *)(local_rbp - 0x21) + 40)) & (2)) != 0) {
        a1 = *(uint64_t *)(result - 0x10);
        result = PsBoostThreadOutstandingIoQoS(a1, a2, a3, *(uint8_t *)(result + 0x18));
    }
    result = ObDereferenceObjectDeferDeleteWithTag(*(uint64_t *)(result - 0x10), (uint32_t)(0x746C6644ULL), a3, *(uint8_t *)(result + 0x18));
    goto loc_002223C1;
loc_00222D13:
    if ((uint32_t)(0x746C6644ULL) == 0) goto loc_00222D63;
    a2 = ((uint32_t)(0x746C6644ULL)) ^ (*(uint64_t *)(result - 0x10));
    goto loc_002220DC;
loc_00222D2D:
    goto loc_002222CA;
loc_00222D3F:
    if (*(uint8_t *)(local_rbp - 0x61) == 0) goto loc_00222D73;
    a2 = (*(uint8_t *)(local_rbp - 0x61)) ^ (*(uint64_t *)(local_rbp - 0x21) + 40);
    goto loc_00222522;
loc_00222D63:
    a3 = 0;
    goto loc_0022228A;
loc_00222D73:
    a3 = 0;
    goto loc_0022256A;
loc_00222D83:
    if (a2 == 0) goto loc_00222D9D;
    a2 = (a2) ^ (*(uint64_t *)(local_rbp - 0x21) + 40);
    goto loc_00222835;
loc_00222D9D:
    a3 = 0;
    goto loc_002229BB;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00221FB6&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
