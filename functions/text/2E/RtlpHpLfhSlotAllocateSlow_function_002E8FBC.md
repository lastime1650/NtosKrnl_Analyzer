# RtlpHpLfhSlotAllocateSlow

- RVA: `0x002E8FBC`–`0x002E9840` (길이 `2,180` bytes)
- VA: `0x00000001402E8FBC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000714BC`
- 디코드: `554`개 명령, `2,180/2,180` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **27**; 고유 호출 대상: **21**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x002E9012` → [RtlpHpEnvTlsGetValue](RtlpHpEnvTlsGetValue_function_002E9850.md) (function, `0x002E9850`)
- `0x002E9145` → [RtlpHpAcquireLockExclusive](../32/RtlpHpAcquireLockExclusive_function_003246B0.md) (function, `0x003246B0`)
- `0x002E9164` → [RtlpHpLfhOwnerGetSubsegment](RtlpHpLfhOwnerGetSubsegment_function_002E8E0C.md) (function, `0x002E8E0C`)
- `0x002E91D5` → [RtlpHpReleaseLockExclusive](../32/RtlpHpReleaseLockExclusive_function_00324230.md) (function, `0x00324230`)
- `0x002E938D` → [RtlpHpLfhSubsegmentCommitBlock](RtlpHpLfhSubsegmentCommitBlock_function_002EA630.md) (function, `0x002EA630`)
- `0x002E93BA` → [RtlHeapZero](../6B/RtlHeapZero_function_006BBC10.md) (function, `0x006BBC10`)
- `0x002E93F6` → [RtlpHpLfhBucketAddSubsegment](RtlpHpLfhBucketAddSubsegment_function_002E8CD8.md) (function, `0x002E8CD8`)
- `0x002E948E` → [RtlpHpReleaseLockShared](../32/RtlpHpReleaseLockShared_function_003245B0.md) (function, `0x003245B0`)
- `0x002E94AD` → [RtlpHpReleaseLockExclusive](../32/RtlpHpReleaseLockExclusive_function_00324230.md) (function, `0x00324230`)
- `0x002E9519` → [RtlpHpLfhOwnerRunMaintenance](RtlpHpLfhOwnerRunMaintenance_function_002E8980.md) (function, `0x002E8980`)
- `0x002E9548` → [RtlpHpReleaseLockExclusive](../32/RtlpHpReleaseLockExclusive_function_00324230.md) (function, `0x00324230`)
- `0x002E958D` → [RtlpHpLfhBucketGetSubsegment](RtlpHpLfhBucketGetSubsegment_function_002E8474.md) (function, `0x002E8474`)
- `0x002E95BE` → [RtlpHpAcquireLockExclusive](../32/RtlpHpAcquireLockExclusive_function_003246B0.md) (function, `0x003246B0`)
- `0x002E95DB` → [RtlpHpLfhOwnerMoveSubsegment](RtlpHpLfhOwnerMoveSubsegment_function_002E85CC.md) (function, `0x002E85CC`)
- `0x002E963A` → [RtlpHpReleaseLockShared](../32/RtlpHpReleaseLockShared_function_003245B0.md) (function, `0x003245B0`)
- `0x002E96A3` → [RtlpHpReleaseLockShared](../32/RtlpHpReleaseLockShared_function_003245B0.md) (function, `0x003245B0`)
- `0x002E96B7` → [RtlpHpLfhSubsegmentCreate](RtlpHpLfhSubsegmentCreate_function_002EC5A0.md) (function, `0x002EC5A0`)
- `0x002E96E7` → [RtlpHpLfhSubsegmentPrefetch](RtlpHpLfhSubsegmentPrefetch_function_002EBB18.md) (function, `0x002EBB18`)
- `0x002E96F4` → [RtlpHpLfhThreadDataInitializeSet](../4F/RtlpHpLfhThreadDataInitializeSet_function_004F6334.md) (function, `0x004F6334`)
- `0x002E974C` → [RtlpHpLfhHeatMapDecayCounts](../46/RtlpHpLfhHeatMapDecayCounts_function_00468B9C.md) (function, `0x00468B9C`)
- `0x002E975C` → [RtlpHpLfhContextMetadataAllocate](../4C/RtlpHpLfhContextMetadataAllocate_function_004C472C.md) (function, `0x004C472C`)
- `0x002E9793` → [RtlpHpLfhPrivateSlotCreate](../60/RtlpHpLfhPrivateSlotCreate_function_00604D50.md) (function, `0x00604D50`)
- `0x002E97B8` → [RtlpHpLfhPrivateSlotShutdown](../60/RtlpHpLfhPrivateSlotShutdown_function_0060502C.md) (function, `0x0060502C`)
- `0x002E97DB` → [RtlpHpLfhHeatMapQuery](RtlpHpLfhHeatMapQuery_function_002E7790.md) (function, `0x002E7790`)
- `0x002E9807` → [RtlpHpLfhHeatMapUpdate](../46/RtlpHpLfhHeatMapUpdate_function_00463854.md) (function, `0x00463854`)
- `0x002E9826` → [RtlpHpReleaseLockExclusive](../32/RtlpHpReleaseLockExclusive_function_00324230.md) (function, `0x00324230`)
- `0x002E9836` → [RtlpHpLfhBucketUpdateAffinityMapping](../4D/RtlpHpLfhBucketUpdateAffinityMapping_function_004D0008.md) (function, `0x004D0008`)

### Direct callers
- [sub_002E9C01](Unknown_function_002E9C01.md) at `0x002E9D12`
- [RtlpHpAllocateHeapSlow](RtlpHpAllocateHeapSlow_function_002E9DEC.md) at `0x002EA402`
- [RtlpHpMetadataAlloc](RtlpHpMetadataAlloc_function_002EC180.md) at `0x002EC3CA`
- [RtlpHpMetadataAlloc](RtlpHpMetadataAlloc_function_002EC180.md) at `0x002EC538`
- [ExAllocateHeapPool](../35/ExAllocateHeapPool_function_0035BA30.md) at `0x0035D8E8`
- [ExAllocateHeapPool](../35/ExAllocateHeapPool_function_0035BA30.md) at `0x0035DD61`

### Static image references
- `0x002E908C` → RVA `0x00F059A0` (`.data`; read)
- `0x002E9265` → RVA `0x00E28308` (`.data`; read)
- `0x002E92FC` → RVA `0x00E28328` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **12**
  - `0x002E9287` → [sub_006DE040 + 0x21D](../6D/Unknown_function_006DE040.md) (`tail-transfer`)
  - `0x002E9507` → [sub_006DE040 + 0x2EF](../6D/Unknown_function_006DE040.md) (`tail-transfer`)
  - `0x002E95F7` → [sub_006DE040 + 0x1F6](../6D/Unknown_function_006DE040.md) (`tail-transfer`)
  - `0x002E9605` → [sub_006DE040 + 0x216](../6D/Unknown_function_006DE040.md) (`tail-transfer`)
  - `0x002E9707` → [sub_006DE040](../6D/Unknown_function_006DE040.md) (`tail-transfer`)
  - `0x002E976E` → [sub_006DE040 + 0x6F](../6D/Unknown_function_006DE040.md) (`tail-transfer`)
  - `0x002E977B` → [sub_006DE040 + 0xCD](../6D/Unknown_function_006DE040.md) (`tail-transfer`)
  - `0x002E979E` → [sub_006DE040 + 0xD8](../6D/Unknown_function_006DE040.md) (`tail-transfer`)
  - `0x002E97A7` → [sub_006DE040 + 0xE4](../6D/Unknown_function_006DE040.md) (`tail-transfer`)
  - `0x002E97C0` → [sub_006DE040 + 0xE4](../6D/Unknown_function_006DE040.md) (`tail-transfer`)
  - `0x002E97CC` → [sub_006DE040 + 0xF0](../6D/Unknown_function_006DE040.md) (`tail-transfer`)
  - `0x002E9820` → [sub_006DE040 + 0x3E4](../6D/Unknown_function_006DE040.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002E8FBC  48 8B C4                        mov rax, rsp
002E8FBF  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
002E8FC3  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
002E8FC7  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
002E8FCB  55                              push rbp
002E8FCC  53                              push rbx
002E8FCD  56                              push rsi
002E8FCE  57                              push rdi
002E8FCF  41 54                           push r12
002E8FD1  41 55                           push r13
002E8FD3  41 56                           push r14
002E8FD5  41 57                           push r15
002E8FD7  48 8D 68 A1                     lea rbp, [rax - 0x5f]
002E8FDB  48 81 EC 88 00 00 00            sub rsp, 0x88
002E8FE2  44 0F B7 6A 02                  movzx r13d, word ptr [rdx + 2]
002E8FE7  48 8D 45 DF                     lea rax, [rbp - 0x21]
002E8FEB  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
002E8FEF  48 8B F1                        mov rsi, rcx
002E8FF2  48 8D 45 DF                     lea rax, [rbp - 0x21]
002E8FF6  49 C1 E5 06                     shl r13, 6
002E8FFA  4C 03 E9                        add r13, rcx
002E8FFD  48 89 45 DF                     mov qword ptr [rbp - 0x21], rax
002E9001  8B 49 4C                        mov ecx, dword ptr [rcx + 0x4c]
002E9004  45 33 D2                        xor r10d, r10d
002E9007  4C 89 6D CF                     mov qword ptr [rbp - 0x31], r13
002E900B  4C 8B FA                        mov r15, rdx
002E900E  44 89 55 F7                     mov dword ptr [rbp - 9], r10d
002E9012  E8 39 08 00 00                  call 0x1402e9850
002E9017  48 8B D8                        mov rbx, rax
002E901A  48 85 C0                        test rax, rax
002E901D  0F 84 CE 06 00 00               je 0x1402e96f1
002E9023  45 0F B6 5D 00                  movzx r11d, byte ptr [r13]
002E9028  48 8B C3                        mov rax, rbx
002E902B  48 C1 E8 10                     shr rax, 0x10
002E902F  48 B9 08 00 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000008
002E9039  44 0F B7 F0                     movzx r14d, ax
002E903D  49 C1 E6 06                     shl r14, 6
002E9041  4C 03 F6                        add r14, rsi
002E9044  41 D1 EB                        shr r11d, 1
002E9047  4C 89 75 EF                     mov qword ptr [rbp - 0x11], r14
002E904B  41 83 FB 7E                     cmp r11d, 0x7e
002E904F  0F 83 B8 00 00 00               jae 0x1402e910d
002E9055  41 8B 86 FC 00 00 00            mov eax, dword ptr [r14 + 0xfc]
002E905C  48 8B 09                        mov rcx, qword ptr [rcx]
002E905F  48 C1 E9 14                     shr rcx, 0x14
002E9063  8B D1                           mov edx, ecx
002E9065  2B D0                           sub edx, eax
002E9067  74 1B                           je 0x1402e9084
002E9069  F0 41 0F B1 8E FC 00 00 00      lock cmpxchg dword ptr [r14 + 0xfc], ecx
002E9072  0F 84 CD 06 00 00               je 0x1402e9745
002E9078  48 B9 08 00 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000008
002E9082  EB D8                           jmp 0x1402e905c
002E9084  43 0F B7 14 5E                  movzx edx, word ptr [r14 + r11*2]
002E9089  45 33 D2                        xor r10d, r10d
002E908C  8B 05 0E C9 C1 00               mov eax, dword ptr [rip + 0xc1c90e]
002E9092  41 B8 01 00 00 00               mov r8d, 1
002E9098  8B C8                           mov ecx, eax
002E909A  C1 E9 08                        shr ecx, 8
002E909D  45 8D 48 01                     lea r9d, [r8 + 1]
002E90A1  83 E1 03                        and ecx, 3
002E90A4  0F 85 5A 06 00 00               jne 0x1402e9704
002E90AA  41 84 C0                        test r8b, al
002E90AD  0F 84 A3 03 00 00               je 0x1402e9456
002E90B3  41 0F B7 45 4C                  movzx eax, word ptr [r13 + 0x4c]
002E90B8  3B D0                           cmp edx, eax
002E90BA  0F 82 96 03 00 00               jb 0x1402e9456
002E90C0  41 0F B7 45 4E                  movzx eax, word ptr [r13 + 0x4e]
002E90C5  3B D0                           cmp edx, eax
002E90C7  0F 82 81 03 00 00               jb 0x1402e944e
002E90CD  8A 46 48                        mov al, byte ptr [rsi + 0x48]
002E90D0  41 22 C0                        and al, r8b
002E90D3  F6 D8                           neg al
002E90D5  1B FF                           sbb edi, edi
002E90D7  F7 DF                           neg edi
002E90D9  41 03 F8                        add edi, r8d
002E90DC  4C 8D A6 C0 00 00 00            lea r12, [rsi + 0xc0]
002E90E3  4D 3B F4                        cmp r14, r12
002E90E6  75 2D                           jne 0x1402e9115
002E90E8  41 3B F8                        cmp edi, r8d
002E90EB  7C 28                           jl 0x1402e9115
002E90ED  8B 46 48                        mov eax, dword ptr [rsi + 0x48]
002E90F0  48 89 5D 67                     mov qword ptr [rbp + 0x67], rbx
002E90F4  41 84 C0                        test r8b, al
002E90F7  0F 85 59 06 00 00               jne 0x1402e9756
002E90FD  4D 8B F4                        mov r14, r12
002E9100  4C 89 65 EF                     mov qword ptr [rbp - 0x11], r12
002E9104  44 89 45 CB                     mov dword ptr [rbp - 0x35], r8d
002E9108  45 33 D2                        xor r10d, r10d
002E910B  EB 14                           jmp 0x1402e9121
002E910D  41 8B D2                        mov edx, r10d
002E9110  E9 77 FF FF FF                  jmp 0x1402e908c
002E9115  89 7D CB                        mov dword ptr [rbp - 0x35], edi
002E9118  41 3B F9                        cmp edi, r9d
002E911B  0F 84 5F 06 00 00               je 0x1402e9780
002E9121  66 45 39 57 04                  cmp word ptr [r15 + 4], r10w
002E9126  0F 85 80 06 00 00               jne 0x1402e97ac
002E912C  0F B6 56 41                     movzx edx, byte ptr [rsi + 0x41]
002E9130  49 8D 4F 10                     lea rcx, [r15 + 0x10]
002E9134  41 B8 02 00 00 00               mov r8d, 2
002E913A  4C 89 65 D7                     mov qword ptr [rbp - 0x29], r12
002E913E  45 8B E8                        mov r13d, r8d
002E9141  44 89 45 C7                     mov dword ptr [rbp - 0x39], r8d
002E9145  E8 66 B5 03 00                  call 0x1403246b0
002E914A  40 8A F8                        mov dil, al
002E914D  88 45 67                        mov byte ptr [rbp + 0x67], al
002E9150  45 33 D2                        xor r10d, r10d
002E9153  66 45 39 57 04                  cmp word ptr [r15 + 4], r10w
002E9158  0F 84 B5 02 00 00               je 0x1402e9413
002E915E  49 8B D7                        mov rdx, r15
002E9161  48 8B CE                        mov rcx, rsi
002E9164  E8 A3 FC FF FF                  call 0x1402e8e0c
002E9169  48 8B D8                        mov rbx, rax
002E916C  48 85 C0                        test rax, rax
002E916F  0F 84 97 03 00 00               je 0x1402e950c
002E9175  0F B7 40 20                     movzx eax, word ptr [rax + 0x20]
002E9179  BF 00 10 00 00                  mov edi, 0x1000
002E917E  66 3B F8                        cmp di, ax
002E9181  0F 83 C7 04 00 00               jae 0x1402e964e
002E9187  66 2B C7                        sub ax, di
002E918A  44 0F B7 E7                     movzx r12d, di
002E918E  B9 01 00 00 00                  mov ecx, 1
002E9193  66 89 43 20                     mov word ptr [rbx + 0x20], ax
002E9197  66 3B F9                        cmp di, cx
002E919A  76 1A                           jbe 0x1402e91b6
002E919C  0F B7 C7                        movzx eax, di
002E919F  48 2B C1                        sub rax, rcx
002E91A2  48 8B CB                        mov rcx, rbx
002E91A5  48 33 C8                        xor rcx, rax
002E91A8  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
002E91AF  48 33 C8                        xor rcx, rax
002E91B2  49 89 4F 38                     mov qword ptr [r15 + 0x38], rcx
002E91B6  45 85 ED                        test r13d, r13d
002E91B9  74 24                           je 0x1402e91df
002E91BB  0F B6 56 41                     movzx edx, byte ptr [rsi + 0x41]
002E91BF  49 8D 4F 10                     lea rcx, [r15 + 0x10]
002E91C3  44 8A 45 67                     mov r8b, byte ptr [rbp + 0x67]
002E91C7  B8 02 00 00 00                  mov eax, 2
002E91CC  44 3B E8                        cmp r13d, eax
002E91CF  0F 85 B9 02 00 00               jne 0x1402e948e
002E91D5  E8 56 B0 03 00                  call 0x140324230
002E91DA  33 C0                           xor eax, eax
002E91DC  44 8B E8                        mov r13d, eax
002E91DF  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
002E91E3  4C 8B 4D D7                     mov r9, qword ptr [rbp - 0x29]
002E91E7  0F B6 01                        movzx eax, byte ptr [rcx]
002E91EA  D1 E8                           shr eax, 1
002E91EC  83 F8 7E                        cmp eax, 0x7e
002E91EF  73 46                           jae 0x1402e9237
002E91F1  41 0F B7 14 41                  movzx edx, word ptr [r9 + rax*2]
002E91F6  4C 8D 96 C0 00 00 00            lea r10, [rsi + 0xc0]
002E91FD  44 8B C0                        mov r8d, eax
002E9200  41 BB FF FF 00 00               mov r11d, 0xffff
002E9206  42 8D 0C 22                     lea ecx, [rdx + r12]
002E920A  41 3B CB                        cmp ecx, r11d
002E920D  41 0F 43 CB                     cmovae ecx, r11d
002E9211  3B CA                           cmp ecx, edx
002E9213  74 1E                           je 0x1402e9233
002E9215  4D 3B CA                        cmp r9, r10
002E9218  0F 85 26 04 00 00               jne 0x1402e9644
002E921E  0F B7 C2                        movzx eax, dx
002E9221  66 F0 43 0F B1 0C 41            lock cmpxchg word ptr [r9 + r8*2], cx
002E9228  0F B7 C8                        movzx ecx, ax
002E922B  3B CA                           cmp ecx, edx
002E922D  0F 85 34 04 00 00               jne 0x1402e9667
002E9233  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
002E9237  4D 3B F1                        cmp r14, r9
002E923A  0F 85 BA 05 00 00               jne 0x1402e97fa
002E9240  45 33 D2                        xor r10d, r10d
002E9243  41 BE 02 00 00 00               mov r14d, 2
002E9249  45 85 ED                        test r13d, r13d
002E924C  0F 85 46 02 00 00               jne 0x1402e9498
002E9252  65 4C 8B 0C 25 88 01 00 00      mov r9, qword ptr gs:[0x188]
002E925B  48 8B C3                        mov rax, rbx
002E925E  48 C1 E8 0C                     shr rax, 0xc
002E9262  33 43 28                        xor eax, dword ptr [rbx + 0x28]
002E9265  33 05 9D F0 B3 00               xor eax, dword ptr [rip + 0xb3f09d]
002E926B  49 8B 89 60 07 00 00            mov rcx, qword ptr [r9 + 0x760]
002E9272  49 8B 91 68 07 00 00            mov rdx, qword ptr [r9 + 0x768]
002E9279  66 45 39 57 04                  cmp word ptr [r15 + 4], r10w
002E927E  44 0F B6 53 18                  movzx r10d, byte ptr [rbx + 0x18]
002E9283  4C 8D 04 0A                     lea r8, [rdx + rcx]
002E9287  0F 85 D0 4F 3F 00               jne 0x1406de25d
002E928D  48 33 D1                        xor rdx, rcx
002E9290  89 45 CB                        mov dword ptr [rbp - 0x35], eax
002E9293  44 0F B7 E0                     movzx r12d, ax
002E9297  48 8D 7B 40                     lea rdi, [rbx + 0x40]
002E929B  48 8B C2                        mov rax, rdx
002E929E  48 C1 C1 18                     rol rcx, 0x18
002E92A2  48 C1 E0 10                     shl rax, 0x10
002E92A6  41 83 EA 08                     sub r10d, 8
002E92AA  48 33 C8                        xor rcx, rax
002E92AD  49 C1 E8 20                     shr r8, 0x20
002E92B1  48 33 CA                        xor rcx, rdx
002E92B4  45 0F B6 D8                     movzx r11d, r8b
002E92B8  48 C1 C2 25                     rol rdx, 0x25
002E92BC  49 89 91 68 07 00 00            mov qword ptr [r9 + 0x768], rdx
002E92C3  49 89 89 60 07 00 00            mov qword ptr [r9 + 0x760], rcx
002E92CA  8A 43 27                        mov al, byte ptr [rbx + 0x27]
002E92CD  44 0F B6 4B 32                  movzx r9d, byte ptr [rbx + 0x32]
002E92D2  88 45 6F                        mov byte ptr [rbp + 0x6f], al
002E92D5  0F B6 43 24                     movzx eax, byte ptr [rbx + 0x24]
002E92D9  44 89 4D C7                     mov dword ptr [rbp - 0x39], r9d
002E92DD  48 8D 14 C7                     lea rdx, [rdi + rax*8]
002E92E1  41 8B C2                        mov eax, r10d
002E92E4  48 FF C8                        dec rax
002E92E7  4C 8D 34 C7                     lea r14, [rdi + rax*8]
002E92EB  33 C0                           xor eax, eax
002E92ED  4C 8B 02                        mov r8, qword ptr [rdx]
002E92F0  49 F7 D0                        not r8
002E92F3  4D 85 C0                        test r8, r8
002E92F6  0F 84 C1 01 00 00               je 0x1402e94bd
002E92FC  8B 05 26 F0 B3 00               mov eax, dword ptr [rip + 0xb3f026]
002E9302  A8 04                           test al, 4
002E9304  0F 85 5F 01 00 00               jne 0x1402e9469
002E930A  49 3B D6                        cmp rdx, r14
002E930D  0F 84 5B 03 00 00               je 0x1402e966e
002E9313  41 83 F9 40                     cmp r9d, 0x40
002E9317  0F 85 51 03 00 00               jne 0x1402e966e
002E931D  41 8B CB                        mov ecx, r11d
002E9320  49 D3 C8                        ror r8, cl
002E9323  F3 4D 0F BC C8                  tzcnt r9, r8
002E9328  45 03 CB                        add r9d, r11d
002E932B  41 83 E1 3F                     and r9d, 0x3f
002E932F  41 8B C9                        mov ecx, r9d
002E9332  41 BA 01 00 00 00               mov r10d, 1
002E9338  49 D3 E2                        shl r10, cl
002E933B  0F 0D 0A                        prefetchw byte ptr [rdx]
002E933E  48 8B 02                        mov rax, qword ptr [rdx]
002E9341  48 8B C8                        mov rcx, rax
002E9344  49 0B CA                        or rcx, r10
002E9347  F0 48 0F B1 0A                  lock cmpxchg qword ptr [rdx], rcx
002E934C  75 F3                           jne 0x1402e9341
002E934E  4C 8B C0                        mov r8, rax
002E9351  4C 85 D0                        test rax, r10
002E9354  0F 85 04 01 00 00               jne 0x1402e945e
002E935A  2B D7                           sub edx, edi
002E935C  41 8B FC                        mov edi, r12d
002E935F  45 8D 34 D1                     lea r14d, [r9 + rdx*8]
002E9363  41 8B C6                        mov eax, r14d
002E9366  41 0F AF FE                     imul edi, r14d
002E936A  C1 E8 06                        shr eax, 6
002E936D  88 43 24                        mov byte ptr [rbx + 0x24], al
002E9370  0F B7 45 CD                     movzx eax, word ptr [rbp - 0x33]
002E9374  03 F8                           add edi, eax
002E9376  B8 01 00 00 00                  mov eax, 1
002E937B  38 45 6F                        cmp byte ptr [rbp + 0x6f], al
002E937E  0F 86 D2 02 00 00               jbe 0x1402e9656
002E9384  44 8B C7                        mov r8d, edi
002E9387  48 8B D3                        mov rdx, rbx
002E938A  48 8B CE                        mov rcx, rsi
002E938D  E8 9E 12 00 00                  call 0x1402ea630
002E9392  45 33 E4                        xor r12d, r12d
002E9395  85 C0                           test eax, eax
002E9397  0F 88 32 01 00 00               js 0x1402e94cf
002E939D  48 03 FB                        add rdi, rbx
002E93A0  41 BE 02 00 00 00               mov r14d, 2
002E93A6  44 84 75 7F                     test byte ptr [rbp + 0x7f], r14b
002E93AA  74 13                           je 0x1402e93bf
002E93AC  8B 55 77                        mov edx, dword ptr [rbp + 0x77]
002E93AF  48 8B CF                        mov rcx, rdi
002E93B2  48 83 C2 0F                     add rdx, 0xf
002E93B6  48 83 E2 F0                     and rdx, 0xfffffffffffffff0
002E93BA  E8 51 28 3D 00                  call 0x1406bbc10
002E93BF  48 85 FF                        test rdi, rdi
002E93C2  0F 84 31 01 00 00               je 0x1402e94f9
002E93C8  45 85 ED                        test r13d, r13d
002E93CB  0F 85 40 04 00 00               jne 0x1402e9811
002E93D1  48 8B 5D CF                     mov rbx, qword ptr [rbp - 0x31]
002E93D5  44 39 65 F7                     cmp dword ptr [rbp - 9], r12d
002E93D9  0F 85 51 04 00 00               jne 0x1402e9830
002E93DF  48 8D 45 DF                     lea rax, [rbp - 0x21]
002E93E3  48 39 45 DF                     cmp qword ptr [rbp - 0x21], rax
002E93E7  74 12                           je 0x1402e93fb
002E93E9  45 33 C9                        xor r9d, r9d
002E93EC  4C 8D 45 DF                     lea r8, [rbp - 0x21]
002E93F0  48 8B D3                        mov rdx, rbx
002E93F3  48 8B CE                        mov rcx, rsi
002E93F6  E8 DD F8 FF FF                  call 0x1402e8cd8
002E93FB  48 8B C7                        mov rax, rdi
002E93FE  48 81 C4 88 00 00 00            add rsp, 0x88
002E9405  41 5F                           pop r15
002E9407  41 5E                           pop r14
002E9409  41 5D                           pop r13
002E940B  41 5C                           pop r12
002E940D  5F                              pop rdi
002E940E  5E                              pop rsi
002E940F  5B                              pop rbx
002E9410  5D                              pop rbp
002E9411  C3                              ret
002E9412  CC                              int3
002E9413  41 0F 0D 4F 38                  prefetchw byte ptr [r15 + 0x38]
002E9418  49 8B 5F 38                     mov rbx, qword ptr [r15 + 0x38]
002E941C  48 F7 C3 FF 0F 00 00            test rbx, 0xfff
002E9423  0F 84 35 FD FF FF               je 0x1402e915e
002E9429  48 8D 4B FF                     lea rcx, [rbx - 1]
002E942D  48 8B C3                        mov rax, rbx
002E9430  F0 49 0F B1 4F 38               lock cmpxchg qword ptr [r15 + 0x38], rcx
002E9436  0F 85 E7 01 00 00               jne 0x1402e9623
002E943C  48 81 E3 00 F0 FF FF            and rbx, 0xfffffffffffff000
002E9443  0F 85 FA FD FF FF               jne 0x1402e9243
002E9449  E9 10 FD FF FF                  jmp 0x1402e915e
002E944E  41 8B F8                        mov edi, r8d
002E9451  E9 86 FC FF FF                  jmp 0x1402e90dc
002E9456  41 8B FA                        mov edi, r10d
002E9459  E9 7E FC FF FF                  jmp 0x1402e90dc
002E945E  44 8B 4D C7                     mov r9d, dword ptr [rbp - 0x39]
002E9462  33 C0                           xor eax, eax
002E9464  E9 87 FE FF FF                  jmp 0x1402e92f0
002E9469  F3 49 0F B8 C0                  popcnt rax, r8
002E946E  41 0F AF C3                     imul eax, r11d
002E9472  B9 01 00 00 00                  mov ecx, 1
002E9477  C1 E8 08                        shr eax, 8
002E947A  C4 E2 F9 F7 C1                  shlx rax, rcx, rax
002E947F  C4 42 FB F5 D0                  pdep r10, rax, r8
002E9484  F3 4D 0F BC CA                  tzcnt r9, r10
002E9489  E9 AD FE FF FF                  jmp 0x1402e933b
002E948E  E8 1D B1 03 00                  call 0x1403245b0
002E9493  E9 42 FD FF FF                  jmp 0x1402e91da
002E9498  0F B6 56 41                     movzx edx, byte ptr [rsi + 0x41]
002E949C  49 8D 4F 10                     lea rcx, [r15 + 0x10]
002E94A0  44 8A 45 67                     mov r8b, byte ptr [rbp + 0x67]
002E94A4  45 3B EE                        cmp r13d, r14d
002E94A7  0F 85 8D 01 00 00               jne 0x1402e963a
002E94AD  E8 7E AD 03 00                  call 0x140324230
002E94B2  45 33 D2                        xor r10d, r10d
002E94B5  45 8B EA                        mov r13d, r10d
002E94B8  E9 95 FD FF FF                  jmp 0x1402e9252
002E94BD  49 3B D6                        cmp rdx, r14
002E94C0  0F 84 6C 01 00 00               je 0x1402e9632
002E94C6  48 83 C2 08                     add rdx, 8
002E94CA  E9 1E FE FF FF                  jmp 0x1402e92ed
002E94CF  49 8B FC                        mov rdi, r12
002E94D2  41 83 FE FF                     cmp r14d, -1
002E94D6  0F 84 39 02 00 00               je 0x1402e9715
002E94DC  41 8B CE                        mov ecx, r14d
002E94DF  41 8B C6                        mov eax, r14d
002E94E2  83 E1 3F                        and ecx, 0x3f
002E94E5  48 C7 C2 FE FF FF FF            mov rdx, 0xfffffffffffffffe
002E94EC  48 D3 C2                        rol rdx, cl
002E94EF  48 C1 E8 06                     shr rax, 6
002E94F3  F0 48 21 54 C3 40               lock and qword ptr [rbx + rax*8 + 0x40], rdx
002E94F9  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
002E94FD  41 BE 01 00 00 00               mov r14d, 1
002E9503  45 8D 46 01                     lea r8d, [r14 + 1]
002E9507  E9 23 4E 3F 00                  jmp 0x1406de32f
002E950C  45 33 C9                        xor r9d, r9d
002E950F  4C 8D 45 DF                     lea r8, [rbp - 0x21]
002E9513  49 8B D7                        mov rdx, r15
002E9516  48 8B CE                        mov rcx, rsi
002E9519  E8 62 F4 FF FF                  call 0x1402e8980
002E951E  45 33 D2                        xor r10d, r10d
002E9521  45 38 57 01                     cmp byte ptr [r15 + 1], r10b
002E9525  0F 87 28 FC FF FF               ja 0x1402e9153
002E952B  45 85 ED                        test r13d, r13d
002E952E  74 27                           je 0x1402e9557
002E9530  0F B6 56 41                     movzx edx, byte ptr [rsi + 0x41]
002E9534  41 8D 42 02                     lea eax, [r10 + 2]
002E9538  49 8D 4F 10                     lea rcx, [r15 + 0x10]
002E953C  44 8A C7                        mov r8b, dil
002E953F  44 3B E8                        cmp r13d, eax
002E9542  0F 85 5B 01 00 00               jne 0x1402e96a3
002E9548  E8 E3 AC 03 00                  call 0x140324230
002E954D  45 33 D2                        xor r10d, r10d
002E9550  45 8B EA                        mov r13d, r10d
002E9553  44 89 55 C7                     mov dword ptr [rbp - 0x39], r10d
002E9557  48 8D 45 FF                     lea rax, [rbp - 1]
002E955B  49 8B DA                        mov rbx, r10
002E955E  48 89 45 07                     mov qword ptr [rbp + 7], rax
002E9562  48 8D 45 FF                     lea rax, [rbp - 1]
002E9566  48 89 45 FF                     mov qword ptr [rbp - 1], rax
002E956A  4C 39 96 A0 00 00 00            cmp qword ptr [rsi + 0xa0], r10
002E9571  0F 85 4E 02 00 00               jne 0x1402e97c5
002E9577  4D 3B E6                        cmp r12, r14
002E957A  0F 85 51 02 00 00               jne 0x1402e97d1
002E9580  8B 7D CB                        mov edi, dword ptr [rbp - 0x35]
002E9583  48 8B 55 CF                     mov rdx, qword ptr [rbp - 0x31]
002E9587  44 8B C7                        mov r8d, edi
002E958A  48 8B CE                        mov rcx, rsi
002E958D  E8 E2 EE FF FF                  call 0x1402e8474
002E9592  48 8B D8                        mov rbx, rax
002E9595  33 C0                           xor eax, eax
002E9597  48 85 DB                        test rbx, rbx
002E959A  0F 84 0D 01 00 00               je 0x1402e96ad
002E95A0  66 41 39 47 04                  cmp word ptr [r15 + 4], ax
002E95A5  0F 85 46 02 00 00               jne 0x1402e97f1
002E95AB  0F B6 56 41                     movzx edx, byte ptr [rsi + 0x41]
002E95AF  49 8D 4F 10                     lea rcx, [r15 + 0x10]
002E95B3  B8 02 00 00 00                  mov eax, 2
002E95B8  44 8B E8                        mov r13d, eax
002E95BB  89 45 C7                        mov dword ptr [rbp - 0x39], eax
002E95BE  E8 ED B0 03 00                  call 0x1403246b0
002E95C3  40 8A F8                        mov dil, al
002E95C6  88 45 67                        mov byte ptr [rbp + 0x67], al
002E95C9  33 C0                           xor eax, eax
002E95CB  45 33 C9                        xor r9d, r9d
002E95CE  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
002E95D2  4C 8B C3                        mov r8, rbx
002E95D5  49 8B D7                        mov rdx, r15
002E95D8  48 8B CE                        mov rcx, rsi
002E95DB  E8 EC EF FF FF                  call 0x1402e85cc
002E95E0  45 33 D2                        xor r10d, r10d
002E95E3  85 C0                           test eax, eax
002E95E5  0F 85 68 FB FF FF               jne 0x1402e9153
002E95EB  0F B7 43 22                     movzx eax, word ptr [rbx + 0x22]
002E95EF  48 8D 4D DF                     lea rcx, [rbp - 0x21]
002E95F3  66 39 43 20                     cmp word ptr [rbx + 0x20], ax
002E95F7  0F 85 39 4C 3F 00               jne 0x1406de236
002E95FD  48 8B 45 DF                     mov rax, qword ptr [rbp - 0x21]
002E9601  48 39 48 08                     cmp qword ptr [rax + 8], rcx
002E9605  0F 85 4B 4C 3F 00               jne 0x1406de256
002E960B  48 89 03                        mov qword ptr [rbx], rax
002E960E  48 8D 4D DF                     lea rcx, [rbp - 0x21]
002E9612  48 89 4B 08                     mov qword ptr [rbx + 8], rcx
002E9616  48 89 58 08                     mov qword ptr [rax + 8], rbx
002E961A  48 89 5D DF                     mov qword ptr [rbp - 0x21], rbx
002E961E  E9 30 FB FF FF                  jmp 0x1402e9153
002E9623  C7 45 F7 01 00 00 00            mov dword ptr [rbp - 9], 1
002E962A  48 8B D8                        mov rbx, rax
002E962D  E9 EA FD FF FF                  jmp 0x1402e941c
002E9632  48 8B D7                        mov rdx, rdi
002E9635  E9 B3 FC FF FF                  jmp 0x1402e92ed
002E963A  E8 71 AF 03 00                  call 0x1403245b0
002E963F  E9 6E FE FF FF                  jmp 0x1402e94b2
002E9644  66 43 89 0C 41                  mov word ptr [r9 + r8*2], cx
002E9649  E9 E5 FB FF FF                  jmp 0x1402e9233
002E964E  0F B7 F8                        movzx edi, ax
002E9651  E9 31 FB FF FF                  jmp 0x1402e9187
002E9656  0F B7 43 30                     movzx eax, word ptr [rbx + 0x30]
002E965A  44 3B F0                        cmp r14d, eax
002E965D  77 7C                           ja 0x1402e96db
002E965F  45 33 E4                        xor r12d, r12d
002E9662  E9 36 FD FF FF                  jmp 0x1402e939d
002E9667  8B D1                           mov edx, ecx
002E9669  E9 98 FB FF FF                  jmp 0x1402e9206
002E966E  F3 49 0F BC C8                  tzcnt rcx, r8
002E9673  49 0F BD C0                     bsr rax, r8
002E9677  89 45 FB                        mov dword ptr [rbp - 5], eax
002E967A  2B C1                           sub eax, ecx
002E967C  FF C0                           inc eax
002E967E  44 3B C8                        cmp r9d, eax
002E9681  41 0F 42 C1                     cmovb eax, r9d
002E9685  44 0F AF D8                     imul r11d, eax
002E9689  41 C1 EB 08                     shr r11d, 8
002E968D  44 03 D9                        add r11d, ecx
002E9690  41 8B CB                        mov ecx, r11d
002E9693  49 D3 C8                        ror r8, cl
002E9696  F3 4D 0F BC C8                  tzcnt r9, r8
002E969B  45 03 CB                        add r9d, r11d
002E969E  E9 8C FC FF FF                  jmp 0x1402e932f
002E96A3  E8 08 AF 03 00                  call 0x1403245b0
002E96A8  E9 A0 FE FF FF                  jmp 0x1402e954d
002E96AD  48 8B 55 CF                     mov rdx, qword ptr [rbp - 0x31]
002E96B1  44 8B C7                        mov r8d, edi
002E96B4  48 8B CE                        mov rcx, rsi
002E96B7  E8 E4 2E 00 00                  call 0x1402ec5a0
002E96BC  48 8B D8                        mov rbx, rax
002E96BF  33 C0                           xor eax, eax
002E96C1  48 85 DB                        test rbx, rbx
002E96C4  0F 85 D6 FE FF FF               jne 0x1402e95a0
002E96CA  45 33 E4                        xor r12d, r12d
002E96CD  41 8B FC                        mov edi, r12d
002E96D0  41 BE 02 00 00 00               mov r14d, 2
002E96D6  E9 ED FC FF FF                  jmp 0x1402e93c8
002E96DB  45 8B CC                        mov r9d, r12d
002E96DE  44 8B C7                        mov r8d, edi
002E96E1  48 8B D3                        mov rdx, rbx
002E96E4  48 8B CE                        mov rcx, rsi
002E96E7  E8 2C 24 00 00                  call 0x1402ebb18
002E96EC  E9 6E FF FF FF                  jmp 0x1402e965f
002E96F1  48 8B CE                        mov rcx, rsi
002E96F4  E8 3B CC 20 00                  call 0x1404f6334
002E96F9  48 8B D8                        mov rbx, rax
002E96FC  45 33 D2                        xor r10d, r10d
002E96FF  E9 1F F9 FF FF                  jmp 0x1402e9023
002E9704  41 3B C9                        cmp ecx, r9d
002E9707  0F 85 33 49 3F 00               jne 0x1406de040
002E970D  41 8B F9                        mov edi, r9d
002E9710  E9 C7 F9 FF FF                  jmp 0x1402e90dc
002E9715  41 BE 02 00 00 00               mov r14d, 2
002E971B  E9 9F FC FF FF                  jmp 0x1402e93bf
002E9720  66 45 39 57 04                  cmp word ptr [r15 + 4], r10w
002E9725  0F 84 01 FA FF FF               je 0x1402e912c
002E972B  4D 8B E6                        mov r12, r14
002E972E  4C 89 75 D7                     mov qword ptr [rbp - 0x29], r14
002E9732  45 8B EA                        mov r13d, r10d
002E9735  44 89 55 C7                     mov dword ptr [rbp - 0x39], r10d
002E9739  41 8A FA                        mov dil, r10b
002E973C  44 88 55 67                     mov byte ptr [rbp + 0x67], r10b
002E9740  E9 0E FA FF FF                  jmp 0x1402e9153
002E9745  4D 8B C6                        mov r8, r14
002E9748  89 54 24 20                     mov dword ptr [rsp + 0x20], edx
002E974C  E8 4B F4 17 00                  call 0x140468b9c
002E9751  E9 2E F9 FF FF                  jmp 0x1402e9084
002E9756  41 8B D0                        mov edx, r8d
002E9759  48 8B CE                        mov rcx, rsi
002E975C  E8 CB AF 1D 00                  call 0x1404c472c
002E9761  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
002E9765  4C 8B F0                        mov r14, rax
002E9768  48 8B F8                        mov rdi, rax
002E976B  48 85 C0                        test rax, rax
002E976E  0F 85 3B 49 3F 00               jne 0x1406de0af
002E9774  4D 8B F4                        mov r14, r12
002E9777  4C 89 65 EF                     mov qword ptr [rbp - 0x11], r12
002E977B  E9 8D 49 3F 00                  jmp 0x1406de10d
002E9780  89 7D CB                        mov dword ptr [rbp - 0x35], edi
002E9783  66 45 39 57 04                  cmp word ptr [r15 + 4], r10w
002E9788  75 A1                           jne 0x1402e972b
002E978A  4D 8B C5                        mov r8, r13
002E978D  48 8B D3                        mov rdx, rbx
002E9790  48 8B CE                        mov rcx, rsi
002E9793  E8 B8 B5 31 00                  call 0x140604d50
002E9798  45 33 D2                        xor r10d, r10d
002E979B  48 85 C0                        test rax, rax
002E979E  0F 84 74 49 3F 00               je 0x1406de118
002E97A4  89 7D CB                        mov dword ptr [rbp - 0x35], edi
002E97A7  E9 78 49 3F 00                  jmp 0x1406de124
002E97AC  45 33 C9                        xor r9d, r9d
002E97AF  4C 8B C3                        mov r8, rbx
002E97B2  49 8B D7                        mov rdx, r15
002E97B5  48 8B CE                        mov rcx, rsi
002E97B8  E8 6F B8 31 00                  call 0x14060502c
002E97BD  45 33 D2                        xor r10d, r10d
002E97C0  E9 5F 49 3F 00                  jmp 0x1406de124
002E97C5  45 33 ED                        xor r13d, r13d
002E97C8  45 8D 75 01                     lea r14d, [r13 + 1]
002E97CC  E9 5F 49 3F 00                  jmp 0x1406de130
002E97D1  4C 8B 45 CF                     mov r8, qword ptr [rbp - 0x31]
002E97D5  49 8B D4                        mov rdx, r12
002E97D8  48 8B CE                        mov rcx, rsi
002E97DB  E8 B0 DF FF FF                  call 0x1402e7790
002E97E0  8B F8                           mov edi, eax
002E97E2  B8 01 00 00 00                  mov eax, 1
002E97E7  3B F8                           cmp edi, eax
002E97E9  0F 4D F8                        cmovge edi, eax
002E97EC  E9 92 FD FF FF                  jmp 0x1402e9583
002E97F1  40 8A 7D 67                     mov dil, byte ptr [rbp + 0x67]
002E97F5  E9 D1 FD FF FF                  jmp 0x1402e95cb
002E97FA  4C 8B C1                        mov r8, rcx
002E97FD  44 0F B7 CF                     movzx r9d, di
002E9801  48 8B CE                        mov rcx, rsi
002E9804  49 8B D6                        mov rdx, r14
002E9807  E8 48 A0 17 00                  call 0x140463854
002E980C  E9 2F FA FF FF                  jmp 0x1402e9240
002E9811  0F B6 56 41                     movzx edx, byte ptr [rsi + 0x41]
002E9815  49 8D 4F 10                     lea rcx, [r15 + 0x10]
002E9819  44 8A 45 67                     mov r8b, byte ptr [rbp + 0x67]
002E981D  45 3B EE                        cmp r13d, r14d
002E9820  0F 85 FE 4B 3F 00               jne 0x1406de424
002E9826  E8 05 AA 03 00                  call 0x140324230
002E982B  E9 A1 FB FF FF                  jmp 0x1402e93d1
002E9830  48 8B D3                        mov rdx, rbx
002E9833  48 8B CE                        mov rcx, rsi
002E9836  E8 CD 67 1E 00                  call 0x1404d0008
002E983B  E9 9F FB FF FF                  jmp 0x1402e93df
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpHpLfhSlotAllocateSlow(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned int v_stack_p20;

    *(unsigned int *)(v_rsp + 32) = a4;
    *(unsigned int *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    v_rsp = (v_rsp) - (136);
    *(unsigned __int64 *)(v_rsp - 95 - 25) = v_rsp - 95 - 33;
    v_r13 = (*(unsigned __int16 *)(a2 + 2)) << (6);
    v_r13 = (v_r13) + (a1);
    *(unsigned __int64 *)(v_rsp - 95 - 33) = v_rsp - 95 - 33;
    v_r10 = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 49) = v_r13;
    *(unsigned int *)(v_rsp - 95 - 9) = 0;
    result = RtlpHpEnvTlsGetValue((unsigned int)(*(unsigned int *)(a1 + 76)), a2, a3, a4);
    if (result == 0) goto loc_002E96F1;
loc_002E9023:
    result = (result) >> (16);
    v_r14 = ((unsigned __int16)(result)) << (6);
    v_r14 = (v_r14) + (a1);
    v_r11 = (unsigned int)((*(unsigned __int8 *)(v_r13)) >> (1));
    *(unsigned __int64 *)(v_rsp - 95 - 17) = v_r14;
    if (((unsigned int)(v_r11)) >= 126) goto loc_002E910D;
loc_002E905C:
    a1 = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a1 + 76)))) >> (20);
    a2 = (unsigned int)(((unsigned int)((unsigned int)(a1))) - ((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 252)))));
    if (condition_is_equal) goto loc_002E9084;
    if (condition_is_equal) goto loc_002E9745;
    goto loc_002E905C;
loc_002E9084:
    v_r10 = 0;
loc_002E908C:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12699918))))) >> (8));
    a1 = (unsigned int)((a1) & (3));
    if (condition_is_not_equal) goto loc_002E9704;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12699918))))) == 0) goto loc_002E9456;
    if (((unsigned int)(*(unsigned __int16 *)(v_r14 + v_r11 * 2))) < ((unsigned int)(*(unsigned __int16 *)(v_r13 + 76)))) goto loc_002E9456;
    if (((unsigned int)(*(unsigned __int16 *)(v_r14 + v_r11 * 2))) < ((unsigned int)(*(unsigned __int16 *)(v_r13 + 78)))) goto loc_002E944E;
    result = (unsigned __int8)((*(unsigned __int8 *)(a1 + 72)) & (1));
    result = (unsigned __int8)(-(result));
    v_rdi = (unsigned int)(-(v_rdi));
    v_rdi = (unsigned int)((v_rdi) + (1));
loc_002E90DC:
    if (v_r14 != (a1 + 192)) goto loc_002E9115;
    if (((unsigned int)(v_rdi)) < 1) goto loc_002E9115;
    *(unsigned __int64 *)(v_rsp - 95 + 103) = result;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 72))))) != 0) goto loc_002E9756;
    *(unsigned __int64 *)(v_rsp - 95 - 17) = a1 + 192;
    *(unsigned int *)(v_rsp - 95 - 53) = 1;
    v_r10 = 0;
    goto loc_002E9121;
loc_002E910D:
    goto loc_002E908C;
loc_002E9115:
    *(unsigned int *)(v_rsp - 95 - 53) = (unsigned int)(v_rdi);
    if (((unsigned int)(v_rdi)) == ((unsigned int)(1 + 1))) goto loc_002E9780;
loc_002E9121:
    if ((*(unsigned __int16 *)(a2 + 4)) != 0) goto loc_002E97AC;
loc_002E912C:
    *(unsigned __int64 *)(v_rsp - 95 - 41) = a1 + 192;
    *(unsigned int *)(v_rsp - 95 - 57) = 2;
    result = RtlpHpAcquireLockExclusive(a2 + 16, *(unsigned __int8 *)(a1 + 65), 2, 1 + 1);
    *(unsigned __int8 *)(v_rsp - 95 + 103) = (unsigned __int8)(result);
    v_r10 = 0;
loc_002E9153:
    if ((*(unsigned __int16 *)(a2 + 4)) == 0) goto loc_002E9413;
loc_002E915E:
    result = RtlpHpLfhOwnerGetSubsegment(a1, a2, 2, 1 + 1);
    if (result == 0) goto loc_002E950C;
    if (((unsigned __int16)((unsigned int)(0x1000ULL))) >= ((unsigned __int16)(*(unsigned __int16 *)(result + 32)))) goto loc_002E964E;
loc_002E9187:
    result = (unsigned __int16)((*(unsigned __int16 *)(result + 32)) - ((unsigned __int16)((unsigned int)(0x1000ULL))));
    *(unsigned __int16 *)(result + 32) = (unsigned __int16)(result);
    if (((unsigned __int16)((unsigned int)(0x1000ULL))) >= = 1) {
        result = (unsigned __int16)((unsigned int)(0x1000ULL));
        result = (result) - (1);
        a1 = result;
        a1 = (a1) ^ (result);
        a1 = (a1) & (0xFFFFFFFFFFFFF000ULL);
        a1 = (a1) ^ (result);
        *(unsigned __int64 *)(a2 + 56) = a1;
    }
    if (2 == 0) goto loc_002E91DF;
    if (2 != 2) goto loc_002E948E;
    result = RtlpHpReleaseLockExclusive(a2 + 16, *(unsigned __int8 *)(a1 + 65), *(unsigned __int8 *)(v_rsp - 95 + 103), 1 + 1);
loc_002E91DA:
    result = 0;
loc_002E91DF:
    result = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 95 - 49))) >> (1));
    if (((unsigned int)(result)) >= 126) goto loc_002E9237;
loc_002E9206:
    a1 = *(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 95 - 41) + result * 2) + (unsigned __int16)((unsigned int)(0x1000ULL)) * 1;
    if (((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 95 - 41) + result * 2) + (unsigned __int16)((unsigned int)(0x1000ULL)) * 1)) >= ((unsigned int)((unsigned int)(0xFFFFULL)))) { a1 = (unsigned int)((unsigned int)(0xFFFFULL)); }
    if (((unsigned int)(a1)) == ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 95 - 41) + result * 2)))) goto loc_002E9233;
    if ((*(unsigned __int64 *)(v_rsp - 95 - 41)) != (a1 + 192)) goto loc_002E9644;
    if (((unsigned int)((unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 95 - 41) + result * 2))))) != ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 95 - 41) + result * 2)))) goto loc_002E9667;
loc_002E9233:
loc_002E9237:
    if ((a1 + 192) != (*(unsigned __int64 *)(v_rsp - 95 - 41))) goto loc_002E97FA;
loc_002E9240:
    v_r10 = 0;
loc_002E9243:
    if (0 != 0) goto loc_002E9498;
loc_002E9252:
    result = (result) >> (12);
    result = (unsigned int)((result) ^ (*(unsigned int *)(result + 40)));
    result = (unsigned int)((result) ^ (*(unsigned int *)(v_rip + 11792541)));
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1896)) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1888));
    *(unsigned int *)(v_rsp - 95 - 53) = (unsigned int)(result);
    result = (a2) << (16);
    v_r10 = (unsigned int)((*(unsigned __int8 *)(result + 24)) - (8));
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1888)) ^ (result);
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1896) + *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1888) * 1) >> (32);
    a1 = (a1) ^ (a2);
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1896) = a2;
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1888) = a1;
    *(unsigned __int8 *)(v_rsp - 95 + 111) = (unsigned __int8)(*(unsigned __int8 *)(result + 39));
    *(unsigned int *)(v_rsp - 95 - 57) = (unsigned int)(*(unsigned __int8 *)(result + 50));
    result = ((unsigned int)((unsigned int)(v_r10))) - 1;
    result = 0;
loc_002E92ED:
loc_002E92F0:
    a3 = ~(*(unsigned __int64 *)(result + 64 + *(unsigned __int8 *)(result + 36) * 8));
    if (a3 == 0) goto loc_002E94BD;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11792422)))) & (4)) != 0) goto loc_002E9469;
    if ((result + 64 + *(unsigned __int8 *)(result + 36) * 8) == (result + 64 + result * 8)) goto loc_002E966E;
    if (((unsigned int)(*(unsigned __int8 *)(result + 50))) != 64) goto loc_002E966E;
    a4 = (unsigned int)((*(unsigned __int8 *)(result + 50)) + ((unsigned int)((unsigned __int8)(a3))));
    a4 = (unsigned int)((a4) & (63));
loc_002E932F:
    v_r10 = (1) << ((unsigned __int8)((unsigned int)(a4)));
loc_002E933B:
loc_002E9341:
    a1 = (*(unsigned __int64 *)(result + 64 + *(unsigned __int8 *)(result + 36) * 8)) | (v_r10);
    if (condition_is_not_equal) goto loc_002E9341;
    if (((*(unsigned __int64 *)(result + 64 + *(unsigned __int8 *)(result + 36) * 8)) & (v_r10)) != 0) goto loc_002E945E;
    a2 = (unsigned int)((result + 64 + *(unsigned __int8 *)(result + 36) * 8) - ((unsigned int)(result + 64)));
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)((unsigned __int16)(result)))) * ((unsigned int)(a4 + a2 * 8)));
    result = (unsigned int)(((unsigned int)((unsigned int)(a4 + a2 * 8))) >> (6));
    *(unsigned __int8 *)(result + 36) = (unsigned __int8)(result);
    v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(*(unsigned __int16 *)(v_rsp - 95 - 51))));
    if ((*(unsigned __int8 *)(v_rsp - 95 + 111)) <= 1) goto loc_002E9656;
    result = RtlpHpLfhSubsegmentCommitBlock(a1, result, (unsigned int)((unsigned int)(v_rdi)), a4);
    v_r12 = 0;
    if (sign_flag) goto loc_002E94CF;
loc_002E939D:
    v_rdi = (v_rdi) + (result);
    if (((*(unsigned __int8 *)(v_rsp - 95 + 127)) & (2)) != 0) {
        a2 = *(unsigned int *)(v_rsp - 95 + 119);
        a1 = v_rdi;
        a2 = (a2) + (15);
        a2 = (a2) & (-16);
        result = RtlHeapZero(a1, a2, (unsigned int)((unsigned int)(v_rdi)), a4);
    }
    if (v_rdi == 0) goto loc_002E94F9;
loc_002E93C8:
    if (0 != 0) goto loc_002E9811;
loc_002E93D1:
    if ((*(unsigned int *)(v_rsp - 95 - 9)) != 0) goto loc_002E9830;
loc_002E93DF:
    result = v_rsp - 95 - 33;
    if ((*(unsigned __int64 *)(v_rsp - 95 - 33)) != (v_rsp - 95 - 33)) {
        a4 = 0;
        a3 = v_rsp - 95 - 33;
        a2 = *(unsigned __int64 *)(v_rsp - 95 - 49);
        a1 = a1;
        result = RtlpHpLfhBucketAddSubsegment(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (136);
    return v_rdi;
loc_002E9413:
loc_002E941C:
    if (((*(unsigned __int64 *)(a2 + 56)) & (0xFFFULL)) == 0) goto loc_002E915E;
    if (((*(unsigned __int64 *)(a2 + 56)) & (0xFFFULL)) != 0) goto loc_002E9623;
    v_rbx = (*(unsigned __int64 *)(a2 + 56)) & (0xFFFFFFFFFFFFF000ULL);
    if (condition_is_not_equal) goto loc_002E9243;
    goto loc_002E915E;
loc_002E944E:
    goto loc_002E90DC;
loc_002E9456:
    goto loc_002E90DC;
loc_002E945E:
    result = 0;
    goto loc_002E92F0;
loc_002E9469:
    result = (unsigned int)((result) * ((unsigned int)((unsigned __int8)(a3))));
    result = (unsigned int)((result) >> (8));
    goto loc_002E933B;
loc_002E948E:
    result = RtlpHpReleaseLockShared(1, a2, a3, (unsigned int)(*(unsigned int *)(v_rsp - 95 - 57)));
    goto loc_002E91DA;
loc_002E9498:
    if (0 != 2) goto loc_002E963A;
    result = RtlpHpReleaseLockExclusive(a2 + 16, *(unsigned __int8 *)(a1 + 65), *(unsigned __int8 *)(v_rsp - 95 + 103), (unsigned int)(*(unsigned int *)(v_rsp - 95 - 57)));
loc_002E94B2:
    v_r10 = 0;
    goto loc_002E9252;
loc_002E94BD:
    if ((*(unsigned __int8 *)(a1 + 65)) == 2) goto loc_002E9632;
    a2 = (*(unsigned __int8 *)(a1 + 65)) + (8);
    goto loc_002E92ED;
loc_002E94CF:
    if (2 == -1) goto loc_002E9715;
    a1 = (unsigned int)((2) & (63));
    result = (2) >> (6);
loc_002E94F9:
loc_002E950C:
    a4 = 0;
    result = RtlpHpLfhOwnerRunMaintenance(a1, a2, v_rsp - 95 - 33, a4);
    v_r10 = 0;
    if ((*(unsigned __int8 *)(a2 + 1)) > 0) goto loc_002E9153;
    if (0 == 0) goto loc_002E9557;
    if (0 != ((unsigned int)(v_r10 + 2))) goto loc_002E96A3;
    result = RtlpHpReleaseLockExclusive(a2 + 16, *(unsigned __int8 *)(a1 + 65), 0, a4);
loc_002E954D:
    v_r10 = 0;
    *(unsigned int *)(v_rsp - 95 - 57) = 0;
loc_002E9557:
    *(unsigned __int64 *)(v_rsp - 95 + 7) = v_rsp - 95 - 1;
    *(unsigned __int64 *)(v_rsp - 95 - 1) = v_rsp - 95 - 1;
    if ((*(unsigned __int64 *)(a1 + 160)) != 0) goto loc_002E97C5;
    if (0 != 1) goto loc_002E97D1;
loc_002E9583:
    result = RtlpHpLfhBucketGetSubsegment(a1, *(unsigned __int64 *)(v_rsp - 95 - 49), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 53)))), a4);
    result = 0;
    if (0 == 0) goto loc_002E96AD;
loc_002E95A0:
    if ((*(unsigned __int16 *)(a2 + 4)) != 0) goto loc_002E97F1;
    *(unsigned int *)(v_rsp - 95 - 57) = 2;
    result = RtlpHpAcquireLockExclusive(a2 + 16, *(unsigned __int8 *)(a1 + 65), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 53)))), a4);
    *(unsigned __int8 *)(v_rsp - 95 + 103) = (unsigned __int8)(result);
    result = 0;
loc_002E95CB:
    a4 = 0;
    v_stack_p20 = 0;
    result = RtlpHpLfhOwnerMoveSubsegment(a1, a2, 0, a4);
    v_r10 = 0;
    if ((unsigned int)(result) != 0) goto loc_002E9153;
    *(unsigned __int64 *)(result) = *(unsigned __int64 *)(v_rsp - 95 - 33);
    *(unsigned __int64 *)(result + 8) = v_rsp - 95 - 33;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 33) + 8) = result;
    *(unsigned __int64 *)(v_rsp - 95 - 33) = result;
    goto loc_002E9153;
loc_002E9623:
    *(unsigned int *)(v_rsp - 95 - 9) = 1;
    goto loc_002E941C;
loc_002E9632:
    goto loc_002E92ED;
loc_002E963A:
    result = RtlpHpReleaseLockShared(v_rsp - 95 - 33, (unsigned __int8)(result), 0, a4);
    goto loc_002E94B2;
loc_002E9644:
    *(unsigned __int16 *)(a4 + 0 * 2) = (unsigned __int16)(v_rsp - 95 - 33);
    goto loc_002E9233;
loc_002E964E:
    goto loc_002E9187;
loc_002E9656:
    if (1 > ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 95 - 33) + 48)))) goto loc_002E96DB;
loc_002E965F:
    v_r12 = 0;
    goto loc_002E939D;
loc_002E9667:
    goto loc_002E9206;
loc_002E966E:
    *(unsigned int *)(v_rsp - 95 - 5) = (unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 95 - 33) + 48));
    result = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 95 - 33) + 48)) - ((unsigned int)(v_rsp - 95 - 33)));
    result = (unsigned int)((result) + 1);
    if (0 < ((unsigned int)(result))) { result = 0; }
    v_r11 = (unsigned int)(((unsigned __int8)(a3)) * ((unsigned int)(result)));
    v_r11 = (unsigned int)((v_r11) >> (8));
    v_r11 = (unsigned int)((v_r11) + ((unsigned int)(v_rsp - 95 - 33)));
    a4 = (unsigned int)((a4) + ((unsigned int)(v_r11)));
    goto loc_002E932F;
loc_002E96A3:
    result = RtlpHpReleaseLockShared((unsigned int)((unsigned int)(v_r11)), (unsigned int)((unsigned int)(v_rsp - 95 - 33)), 0, a4);
    goto loc_002E954D;
loc_002E96AD:
    result = RtlpHpLfhSubsegmentCreate(a1, *(unsigned __int64 *)(v_rsp - 95 - 49), (unsigned int)((unsigned int)((unsigned __int16)(result))), a4);
    result = 0;
    if (0 != 0) goto loc_002E95A0;
    v_r12 = 0;
    goto loc_002E93C8;
loc_002E96DB:
    result = RtlpHpLfhSubsegmentPrefetch(a1, 0, 0, 0);
    goto loc_002E965F;
loc_002E96F1:
    result = RtlpHpLfhThreadDataInitializeSet(a1, 0, 0, 0);
    v_r10 = 0;
    goto loc_002E9023;
loc_002E9704:
    goto loc_002E90DC;
loc_002E9715:
    goto loc_002E93BF;
loc_002E972B:
    *(unsigned __int64 *)(v_rsp - 95 - 41) = 2;
    *(unsigned int *)(v_rsp - 95 - 57) = 0;
    *(unsigned __int8 *)(v_rsp - 95 + 103) = 0;
    goto loc_002E9153;
loc_002E9745:
    v_stack_p20 = 0;
    result = RtlpHpLfhHeatMapDecayCounts(a1, 0, 2, 0);
    goto loc_002E9084;
loc_002E9756:
    result = RtlpHpLfhContextMetadataAllocate(a1, 2, 2, 0);
    *(unsigned __int64 *)(v_rsp - 95 - 17) = result;
    *(unsigned __int64 *)(v_rsp - 95 - 17) = 2;
loc_002E9780:
    *(unsigned int *)(v_rsp - 95 - 53) = (unsigned int)(result);
    if ((*(unsigned __int16 *)(a2 + 4)) != 0) goto loc_002E972B;
    result = RtlpHpLfhPrivateSlotCreate(a1, result, 0, 0);
    v_r10 = 0;
    *(unsigned int *)(v_rsp - 95 - 53) = (unsigned int)(result);
loc_002E97AC:
    a4 = 0;
    result = RtlpHpLfhPrivateSlotShutdown(a1, a2, result, a4);
    v_r10 = 0;
loc_002E97C5:
    v_r13 = 0;
loc_002E97D1:
    result = RtlpHpLfhHeatMapQuery(a1, 2, *(unsigned __int64 *)(v_rsp - 95 - 49), a4);
    v_rdi = (unsigned int)((unsigned int)(result));
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) >= 1) { v_rdi = 1; }
    goto loc_002E9583;
loc_002E97F1:
    goto loc_002E95CB;
loc_002E97FA:
    result = RtlpHpLfhHeatMapUpdate(a1, v_r13 + 1, a1, (unsigned __int16)(*(unsigned __int8 *)(v_rsp - 95 + 103)));
    goto loc_002E9240;
loc_002E9811:
    result = RtlpHpReleaseLockExclusive(a2 + 16, *(unsigned __int8 *)(a1 + 65), *(unsigned __int8 *)(v_rsp - 95 + 103), (unsigned __int16)(*(unsigned __int8 *)(v_rsp - 95 + 103)));
    goto loc_002E93D1;
loc_002E9830:
    result = RtlpHpLfhBucketUpdateAffinityMapping(a1, result, *(unsigned __int8 *)(v_rsp - 95 + 103), (unsigned __int16)(*(unsigned __int8 *)(v_rsp - 95 + 103)));
    goto loc_002E93DF;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpHpLfhSlotAllocateSlow(void *Arg1, void *Arg2, int32_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint32_t v_stack_p20;

    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    *(void **)(local_rsp + 0x10) = Arg2;
    local_rsp = (local_rsp) - (136);
    *(uint64_t *)(local_rsp - 0x5F - 0x19) = local_rsp - 95 - 33;
    local_r13 = (*(uint16_t *)(arg2 + 0x2)) << (6);
    local_r13 = (local_r13) + (Arg1);
    *(uint64_t *)(local_rsp - 0x5F - 0x21) = local_rsp - 95 - 33;
    local_r10 = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x31) = local_r13;
    *(uint32_t *)(local_rsp - 0x5F - 0x9) = 0;
    result = RtlpHpEnvTlsGetValue((uint32_t)(*(uint32_t *)(arg1 + 0x4C)), Arg2, Arg3, Arg4);
    if (result == 0) goto loc_002E96F1;
loc_002E9023:
    result = (result) >> (16);
    local_r14 = ((uint16_t)(result)) << (6);
    local_r14 = (local_r14) + (Arg1);
    local_r11 = (uint32_t)((*(uint8_t *)(local_r13)) >> (1));
    *(uint64_t *)(local_rsp - 0x5F - 0x11) = local_r14;
    if (((uint32_t)(local_r11)) >= 126) goto loc_002E910D;
loc_002E905C:
    Arg1 = (*(uint64_t *)((uint32_t)(*(uint32_t *)(arg1 + 0x4C)))) >> (20);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) - ((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0xFC)))));
    if (condition_is_equal) goto loc_002E9084;
    if (condition_is_equal) goto loc_002E9745;
    goto loc_002E905C;
loc_002E9084:
    local_r10 = 0;
loc_002E908C:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC1C90E))))) >> (8));
    Arg1 = (uint32_t)((Arg1) & (3));
    if (condition_is_not_equal) goto loc_002E9704;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC1C90E))))) == 0) goto loc_002E9456;
    if (((uint32_t)(*(uint16_t *)(local_r14 + local_r11 * 2))) < ((uint32_t)(*(uint16_t *)(local_r13 + 0x4C)))) goto loc_002E9456;
    if (((uint32_t)(*(uint16_t *)(local_r14 + local_r11 * 2))) < ((uint32_t)(*(uint16_t *)(local_r13 + 0x4E)))) goto loc_002E944E;
    result = (uint8_t)((*(uint8_t *)(arg1 + 0x48)) & (1));
    result = (uint8_t)(-(result));
    local_rdi = (uint32_t)(-(local_rdi));
    local_rdi = (uint32_t)((local_rdi) + (1));
loc_002E90DC:
    if (local_r14 != (Arg1 + 192)) goto loc_002E9115;
    if (((uint32_t)(local_rdi)) < 1) goto loc_002E9115;
    *(uint64_t *)(local_rsp - 0x5F + 0x67) = result;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x48))))) != 0) goto loc_002E9756;
    *(void **)(local_rsp - 0x5F - 0x11) = Arg1 + 192;
    *(uint32_t *)(local_rsp - 0x5F - 0x35) = 1;
    local_r10 = 0;
    goto loc_002E9121;
loc_002E910D:
    goto loc_002E908C;
loc_002E9115:
    *(uint32_t *)(local_rsp - 0x5F - 0x35) = (uint32_t)(local_rdi);
    if (((uint32_t)(local_rdi)) == ((uint32_t)(1 + 1))) goto loc_002E9780;
loc_002E9121:
    if ((*(uint16_t *)(arg2 + 0x4)) != 0) goto loc_002E97AC;
loc_002E912C:
    *(void **)(local_rsp - 0x5F - 0x29) = Arg1 + 192;
    *(uint32_t *)(local_rsp - 0x5F - 0x39) = 2;
    result = RtlpHpAcquireLockExclusive(Arg2 + 16, *(uint8_t *)(arg1 + 0x41), 2, 1 + 1);
    *(uint8_t *)(local_rsp - 0x5F + 0x67) = (uint8_t)(result);
    local_r10 = 0;
loc_002E9153:
    if ((*(uint16_t *)(arg2 + 0x4)) == 0) goto loc_002E9413;
loc_002E915E:
    result = RtlpHpLfhOwnerGetSubsegment(Arg1, Arg2, 2, 1 + 1);
    if (result == 0) goto loc_002E950C;
    if (((uint16_t)((uint32_t)(0x1000ULL))) >= ((uint16_t)(*(uint16_t *)(result + 0x20)))) goto loc_002E964E;
loc_002E9187:
    result = (uint16_t)((*(uint16_t *)(result + 0x20)) - ((uint16_t)((uint32_t)(0x1000ULL))));
    *(uint16_t *)(result + 0x20) = (uint16_t)(result);
    if (((uint16_t)((uint32_t)(0x1000ULL))) >= = 1) {
        result = (uint16_t)((uint32_t)(0x1000ULL));
        result = (result) - (1);
        Arg1 = result;
        Arg1 = (Arg1) ^ (result);
        Arg1 = (Arg1) & (0xFFFFFFFFFFFFF000ULL);
        Arg1 = (Arg1) ^ (result);
        *(void **)(arg2 + 0x38) = Arg1;
    }
    if (2 == 0) goto loc_002E91DF;
    if (2 != 2) goto loc_002E948E;
    result = RtlpHpReleaseLockExclusive(Arg2 + 16, *(uint8_t *)(arg1 + 0x41), *(uint8_t *)(local_rsp - 0x5F + 0x67), 1 + 1);
loc_002E91DA:
    result = 0;
loc_002E91DF:
    result = (uint32_t)((*(uint8_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x31))) >> (1));
    if (((uint32_t)(result)) >= 126) goto loc_002E9237;
loc_002E9206:
    Arg1 = *(uint16_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x29) + result * 2) + (uint16_t)((uint32_t)(0x1000ULL)) * 1;
    if (((uint32_t)(*(uint16_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x29) + result * 2) + (uint16_t)((uint32_t)(0x1000ULL)) * 1)) >= ((uint32_t)((uint32_t)(0xFFFFULL)))) { Arg1 = (uint32_t)((uint32_t)(0xFFFFULL)); }
    if (((uint32_t)(Arg1)) == ((uint32_t)(*(uint16_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x29) + result * 2)))) goto loc_002E9233;
    if ((*(uint64_t *)(local_rsp - 0x5F - 0x29)) != (Arg1 + 192)) goto loc_002E9644;
    if (((uint32_t)((uint16_t)((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x29) + result * 2))))) != ((uint32_t)(*(uint16_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x29) + result * 2)))) goto loc_002E9667;
loc_002E9233:
loc_002E9237:
    if ((Arg1 + 192) != (*(uint64_t *)(local_rsp - 0x5F - 0x29))) goto loc_002E97FA;
loc_002E9240:
    local_r10 = 0;
loc_002E9243:
    if (0 != 0) goto loc_002E9498;
loc_002E9252:
    result = (result) >> (12);
    result = (uint32_t)((result) ^ (*(uint32_t *)(result + 0x28)));
    result = (uint32_t)((result) ^ (*(uint32_t *)(v_rip + 0xB3F09D)));
    Arg2 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x768)) ^ (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x760));
    *(uint32_t *)(local_rsp - 0x5F - 0x35) = (uint32_t)(result);
    result = (Arg2) << (16);
    local_r10 = (uint32_t)((*(uint8_t *)(result + 0x18)) - (8));
    Arg1 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x760)) ^ (result);
    Arg3 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x768) + *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x760) * 1) >> (32);
    Arg1 = (Arg1) ^ (Arg2);
    *(void **)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x768) = Arg2;
    *(void **)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x760) = Arg1;
    *(uint8_t *)(local_rsp - 0x5F + 0x6F) = (uint8_t)(*(uint8_t *)(result + 0x27));
    *(uint32_t *)(local_rsp - 0x5F - 0x39) = (uint32_t)(*(uint8_t *)(result + 0x32));
    result = ((uint32_t)((uint32_t)(local_r10))) - 1;
    result = 0;
loc_002E92ED:
loc_002E92F0:
    Arg3 = ~(*(uint64_t *)(result + 0x40 + *(uint8_t *)(result + 0x24) * 8));
    if (Arg3 == 0) goto loc_002E94BD;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB3F026)))) & (4)) != 0) goto loc_002E9469;
    if ((result + 64 + *(uint8_t *)(result + 0x24) * 8) == (result + 64 + result * 8)) goto loc_002E966E;
    if (((uint32_t)(*(uint8_t *)(result + 0x32))) != 64) goto loc_002E966E;
    Arg4 = (uint32_t)((*(uint8_t *)(result + 0x32)) + ((uint32_t)((uint8_t)(Arg3))));
    Arg4 = (uint32_t)((Arg4) & (63));
loc_002E932F:
    local_r10 = (1) << ((uint8_t)((uint32_t)(Arg4)));
loc_002E933B:
loc_002E9341:
    Arg1 = (*(uint64_t *)(result + 0x40 + *(uint8_t *)(result + 0x24) * 8)) | (local_r10);
    if (condition_is_not_equal) goto loc_002E9341;
    if (((*(uint64_t *)(result + 0x40 + *(uint8_t *)(result + 0x24) * 8)) & (local_r10)) != 0) goto loc_002E945E;
    Arg2 = (uint32_t)((result + 64 + *(uint8_t *)(result + 0x24) * 8) - ((uint32_t)(result + 64)));
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)((uint16_t)(result)))) * ((uint32_t)(Arg4 + Arg2 * 8)));
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg4 + Arg2 * 8))) >> (6));
    *(uint8_t *)(result + 0x24) = (uint8_t)(result);
    local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(*(uint16_t *)(local_rsp - 0x5F - 0x33))));
    if ((*(uint8_t *)(local_rsp - 0x5F + 0x6F)) <= 1) goto loc_002E9656;
    result = RtlpHpLfhSubsegmentCommitBlock(Arg1, result, (uint32_t)((uint32_t)(local_rdi)), Arg4);
    local_r12 = 0;
    if (sign_flag) goto loc_002E94CF;
loc_002E939D:
    local_rdi = (local_rdi) + (result);
    if (((*(uint8_t *)(local_rsp - 0x5F + 0x7F)) & (2)) != 0) {
        Arg2 = *(uint32_t *)(local_rsp - 0x5F + 0x77);
        Arg1 = local_rdi;
        Arg2 = (Arg2) + (15);
        Arg2 = (Arg2) & (-16);
        result = RtlHeapZero(Arg1, Arg2, (uint32_t)((uint32_t)(local_rdi)), Arg4);
    }
    if (local_rdi == 0) goto loc_002E94F9;
loc_002E93C8:
    if (0 != 0) goto loc_002E9811;
loc_002E93D1:
    if ((*(uint32_t *)(local_rsp - 0x5F - 0x9)) != 0) goto loc_002E9830;
loc_002E93DF:
    result = local_rsp - 95 - 33;
    if ((*(uint64_t *)(local_rsp - 0x5F - 0x21)) != (local_rsp - 95 - 33)) {
        Arg4 = 0;
        Arg3 = local_rsp - 95 - 33;
        Arg2 = *(uint64_t *)(local_rsp - 0x5F - 0x31);
        Arg1 = Arg1;
        result = RtlpHpLfhBucketAddSubsegment(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (136);
    return local_rdi;
loc_002E9413:
loc_002E941C:
    if (((*(uint64_t *)(arg2 + 0x38)) & (0xFFFULL)) == 0) goto loc_002E915E;
    if (((*(uint64_t *)(arg2 + 0x38)) & (0xFFFULL)) != 0) goto loc_002E9623;
    local_rbx = (*(uint64_t *)(arg2 + 0x38)) & (0xFFFFFFFFFFFFF000ULL);
    if (condition_is_not_equal) goto loc_002E9243;
    goto loc_002E915E;
loc_002E944E:
    goto loc_002E90DC;
loc_002E9456:
    goto loc_002E90DC;
loc_002E945E:
    result = 0;
    goto loc_002E92F0;
loc_002E9469:
    result = (uint32_t)((result) * ((uint32_t)((uint8_t)(Arg3))));
    result = (uint32_t)((result) >> (8));
    goto loc_002E933B;
loc_002E948E:
    result = RtlpHpReleaseLockShared(1, Arg2, Arg3, (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x39)));
    goto loc_002E91DA;
loc_002E9498:
    if (0 != 2) goto loc_002E963A;
    result = RtlpHpReleaseLockExclusive(Arg2 + 16, *(uint8_t *)(arg1 + 0x41), *(uint8_t *)(local_rsp - 0x5F + 0x67), (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x39)));
loc_002E94B2:
    local_r10 = 0;
    goto loc_002E9252;
loc_002E94BD:
    if ((*(uint8_t *)(arg1 + 0x41)) == 2) goto loc_002E9632;
    Arg2 = (*(uint8_t *)(arg1 + 0x41)) + (8);
    goto loc_002E92ED;
loc_002E94CF:
    if (2 == -1) goto loc_002E9715;
    Arg1 = (uint32_t)((2) & (63));
    result = (2) >> (6);
loc_002E94F9:
loc_002E950C:
    Arg4 = 0;
    result = RtlpHpLfhOwnerRunMaintenance(Arg1, Arg2, local_rsp - 95 - 33, Arg4);
    local_r10 = 0;
    if ((*(uint8_t *)(arg2 + 0x1)) > 0) goto loc_002E9153;
    if (0 == 0) goto loc_002E9557;
    if (0 != ((uint32_t)(local_r10 + 2))) goto loc_002E96A3;
    result = RtlpHpReleaseLockExclusive(Arg2 + 16, *(uint8_t *)(arg1 + 0x41), 0, Arg4);
loc_002E954D:
    local_r10 = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x39) = 0;
loc_002E9557:
    *(uint64_t *)(local_rsp - 0x5F + 0x7) = local_rsp - 95 - 1;
    *(uint64_t *)(local_rsp - 0x5F - 0x1) = local_rsp - 95 - 1;
    if ((*(uint64_t *)(arg1 + 0xA0)) != 0) goto loc_002E97C5;
    if (0 != 1) goto loc_002E97D1;
loc_002E9583:
    result = RtlpHpLfhBucketGetSubsegment(Arg1, *(uint64_t *)(local_rsp - 0x5F - 0x31), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x35)))), Arg4);
    result = 0;
    if (0 == 0) goto loc_002E96AD;
loc_002E95A0:
    if ((*(uint16_t *)(arg2 + 0x4)) != 0) goto loc_002E97F1;
    *(uint32_t *)(local_rsp - 0x5F - 0x39) = 2;
    result = RtlpHpAcquireLockExclusive(Arg2 + 16, *(uint8_t *)(arg1 + 0x41), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x35)))), Arg4);
    *(uint8_t *)(local_rsp - 0x5F + 0x67) = (uint8_t)(result);
    result = 0;
loc_002E95CB:
    Arg4 = 0;
    v_stack_p20 = 0;
    result = RtlpHpLfhOwnerMoveSubsegment(Arg1, Arg2, 0, Arg4);
    local_r10 = 0;
    if ((uint32_t)(result) != 0) goto loc_002E9153;
    *(uint64_t *)(result) = *(uint64_t *)(local_rsp - 0x5F - 0x21);
    *(uint64_t *)(result + 0x8) = local_rsp - 95 - 33;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x21) + 0x8) = result;
    *(uint64_t *)(local_rsp - 0x5F - 0x21) = result;
    goto loc_002E9153;
loc_002E9623:
    *(uint32_t *)(local_rsp - 0x5F - 0x9) = 1;
    goto loc_002E941C;
loc_002E9632:
    goto loc_002E92ED;
loc_002E963A:
    result = RtlpHpReleaseLockShared(local_rsp - 95 - 33, (uint8_t)(result), 0, Arg4);
    goto loc_002E94B2;
loc_002E9644:
    *(uint16_t *)(Arg4 + 0x0 * 2) = (uint16_t)(local_rsp - 95 - 33);
    goto loc_002E9233;
loc_002E964E:
    goto loc_002E9187;
loc_002E9656:
    if (1 > ((uint32_t)(*(uint16_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x21) + 0x30)))) goto loc_002E96DB;
loc_002E965F:
    local_r12 = 0;
    goto loc_002E939D;
loc_002E9667:
    goto loc_002E9206;
loc_002E966E:
    *(uint32_t *)(local_rsp - 0x5F - 0x5) = (uint32_t)(*(uint16_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x21) + 0x30));
    result = (uint32_t)((*(uint16_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x21) + 0x30)) - ((uint32_t)(local_rsp - 95 - 33)));
    result = (uint32_t)((result) + 1);
    if (0 < ((uint32_t)(result))) { result = 0; }
    local_r11 = (uint32_t)(((uint8_t)(Arg3)) * ((uint32_t)(result)));
    local_r11 = (uint32_t)((local_r11) >> (8));
    local_r11 = (uint32_t)((local_r11) + ((uint32_t)(local_rsp - 95 - 33)));
    Arg4 = (uint32_t)((Arg4) + ((uint32_t)(local_r11)));
    goto loc_002E932F;
loc_002E96A3:
    result = RtlpHpReleaseLockShared((uint32_t)((uint32_t)(local_r11)), (uint32_t)((uint32_t)(local_rsp - 95 - 33)), 0, Arg4);
    goto loc_002E954D;
loc_002E96AD:
    result = RtlpHpLfhSubsegmentCreate(Arg1, *(uint64_t *)(local_rsp - 0x5F - 0x31), (uint32_t)((uint32_t)((uint16_t)(result))), Arg4);
    result = 0;
    if (0 != 0) goto loc_002E95A0;
    local_r12 = 0;
    goto loc_002E93C8;
loc_002E96DB:
    result = RtlpHpLfhSubsegmentPrefetch(Arg1, 0, 0, 0);
    goto loc_002E965F;
loc_002E96F1:
    result = RtlpHpLfhThreadDataInitializeSet(Arg1, 0, 0, 0);
    local_r10 = 0;
    goto loc_002E9023;
loc_002E9704:
    goto loc_002E90DC;
loc_002E9715:
    goto loc_002E93BF;
loc_002E972B:
    *(uint64_t *)(local_rsp - 0x5F - 0x29) = 2;
    *(uint32_t *)(local_rsp - 0x5F - 0x39) = 0;
    *(uint8_t *)(local_rsp - 0x5F + 0x67) = 0;
    goto loc_002E9153;
loc_002E9745:
    v_stack_p20 = 0;
    result = RtlpHpLfhHeatMapDecayCounts(Arg1, 0, 2, 0);
    goto loc_002E9084;
loc_002E9756:
    result = RtlpHpLfhContextMetadataAllocate(Arg1, 2, 2, 0);
    *(uint64_t *)(local_rsp - 0x5F - 0x11) = result;
    *(uint64_t *)(local_rsp - 0x5F - 0x11) = 2;
loc_002E9780:
    *(uint32_t *)(local_rsp - 0x5F - 0x35) = (uint32_t)(result);
    if ((*(uint16_t *)(arg2 + 0x4)) != 0) goto loc_002E972B;
    result = RtlpHpLfhPrivateSlotCreate(Arg1, result, 0, 0);
    local_r10 = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x35) = (uint32_t)(result);
loc_002E97AC:
    Arg4 = 0;
    result = RtlpHpLfhPrivateSlotShutdown(Arg1, Arg2, result, Arg4);
    local_r10 = 0;
loc_002E97C5:
    local_r13 = 0;
loc_002E97D1:
    result = RtlpHpLfhHeatMapQuery(Arg1, 2, *(uint64_t *)(local_rsp - 0x5F - 0x31), Arg4);
    local_rdi = (uint32_t)((uint32_t)(result));
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) >= 1) { local_rdi = 1; }
    goto loc_002E9583;
loc_002E97F1:
    goto loc_002E95CB;
loc_002E97FA:
    result = RtlpHpLfhHeatMapUpdate(Arg1, local_r13 + 1, Arg1, (uint16_t)(*(uint8_t *)(local_rsp - 0x5F + 0x67)));
    goto loc_002E9240;
loc_002E9811:
    result = RtlpHpReleaseLockExclusive(Arg2 + 16, *(uint8_t *)(arg1 + 0x41), *(uint8_t *)(local_rsp - 0x5F + 0x67), (uint16_t)(*(uint8_t *)(local_rsp - 0x5F + 0x67)));
    goto loc_002E93D1;
loc_002E9830:
    result = RtlpHpLfhBucketUpdateAffinityMapping(Arg1, result, *(uint8_t *)(local_rsp - 0x5F + 0x67), (uint16_t)(*(uint8_t *)(local_rsp - 0x5F + 0x67)));
    goto loc_002E93DF;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x41` | `8` | `R` |
| `Arg1` | `+ 0x48` | `8` | `R` |
| `Arg1` | `+ 0x48` | `32` | `R` |
| `Arg1` | `+ 0x4C` | `32` | `R` |
| `Arg1` | `+ 0xA0` | `64` | `R` |
| `Arg1` | `+ 0xC0` | `64` | `R` |
| `Arg2` | `+ 0x1` | `8` | `R` |
| `Arg2` | `+ 0x2` | `16` | `R` |
| `Arg2` | `+ 0x4` | `16` | `R` |
| `Arg2` | `+ 0x10` | `64` | `R` |
| `Arg2` | `+ 0x38` | `8` | `R` |
| `Arg2` | `+ 0x38` | `64` | `R` |
| `Arg2` | `+ 0x38` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002E8FBC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
