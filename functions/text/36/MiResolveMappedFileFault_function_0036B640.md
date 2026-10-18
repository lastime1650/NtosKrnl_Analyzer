# MiResolveMappedFileFault

- RVA: `0x0036B640`–`0x0036C02B` (길이 `2,539` bytes)
- VA: `0x000000014036B640`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007A398`
- 디코드: `630`개 명령, `2,539/2,539` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **39**; 고유 호출 대상: **28**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x0036B7BD` → [MiComputeFaultNode](../2B/MiComputeFaultNode_function_002B60C0.md) (function, `0x002B60C0`)
- `0x0036B80A` → [MiLockVadTree](../27/MiLockVadTree_function_0027C0F0.md) (function, `0x0027C0F0`)
- `0x0036B813` → [MiLocateAddress](../31/MiLocateAddress_function_003168D0.md) (function, `0x003168D0`)
- `0x0036B825` → [MiUnlockVadTree](../29/MiUnlockVadTree_function_00297020.md) (function, `0x00297020`)
- `0x0036B855` → [MiGetInPageSupportBlock](MiGetInPageSupportBlock_function_00362500.md) (function, `0x00362500`)
- `0x0036B868` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x0036B874` → [MiGetInPageSupportBlock](MiGetInPageSupportBlock_function_00362500.md) (function, `0x00362500`)
- `0x0036B88B` → [MiLockProtoPoolPage](../2B/MiLockProtoPoolPage_function_002B8B80.md) (function, `0x002B8B80`)
- `0x0036B8EE` → [MiSanitizePfnProtection](MiSanitizePfnProtection_function_0036C040.md) (function, `0x0036C040`)
- `0x0036B904` → [MiInitializePageColorBase](../32/MiInitializePageColorBase_function_00320410.md) (function, `0x00320410`)
- `0x0036B964` → [MiObtainFaultCharges](../28/MiObtainFaultCharges_function_0028AEB0.md) (function, `0x0028AEB0`)
- `0x0036B9C4` → [MiUseSlabAllocator](MiUseSlabAllocator_function_00365C68.md) (function, `0x00365C68`)
- `0x0036B9DC` → [MiGetPage](../28/MiGetPage_function_002884C0.md) (function, `0x002884C0`)
- `0x0036BA1F` → [MiCopyDataPageToImagePage](../2A/MiCopyDataPageToImagePage_function_002AE818.md) (function, `0x002AE818`)
- `0x0036BA84` → [MiPickClusterForMappedFileFault](MiPickClusterForMappedFileFault_function_0036C0C0.md) (function, `0x0036C0C0`)
- `0x0036BAC2` → [MiBuildMdlForMappedFileFault](MiBuildMdlForMappedFileFault_function_0036380C.md) (function, `0x0036380C`)
- `0x0036BAEC` → [MiFinishMdlForMappedFileFault](../2A/MiFinishMdlForMappedFileFault_function_002AC974.md) (function, `0x002AC974`)
- `0x0036BB27` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x0036BB2F` → [MiFreeInPageSupportBlock](../2B/MiFreeInPageSupportBlock_function_002B5900.md) (function, `0x002B5900`)
- `0x0036BB43` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x0036BB59` → [MiReturnFaultCharges](MiReturnFaultCharges_function_0036D928.md) (function, `0x0036D928`)
- `0x0036BB92` → [MiGetSlabPage](../37/MiGetSlabPage_function_00376FBC.md) (function, `0x00376FBC`)
- `0x0036BBA5` → [MiReturnResident](../28/MiReturnResident_function_00286890.md) (function, `0x00286890`)
- `0x0036BBB3` → [MiReturnCommit](../24/MiReturnCommit_function_00248410.md) (function, `0x00248410`)
- `0x0036BBDA` → [MiComputeFaultCluster](MiComputeFaultCluster_function_003635B4.md) (function, `0x003635B4`)
- `0x0036BC1D` → [MiCopyFileOnlyGlobalSubsectionPage](MiCopyFileOnlyGlobalSubsectionPage_function_0036A9EC.md) (function, `0x0036A9EC`)
- `0x0036BC4B` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x0036BCC1` → [MiGetAvailablePagesBelowPriority](../34/MiGetAvailablePagesBelowPriority_function_0034D340.md) (function, `0x0034D340`)
- `0x0036BCE5` → [MiSetInPagePrefetchPriority](MiSetInPagePrefetchPriority_function_0036A974.md) (function, `0x0036A974`)
- `0x0036BE39` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x0036BE41` → [MiFreeInPageSupportBlock](../2B/MiFreeInPageSupportBlock_function_002B5900.md) (function, `0x002B5900`)
- `0x0036BE87` → [MiGetSessionIdForVa](../34/MiGetSessionIdForVa_function_00346C60.md) (function, `0x00346C60`)
- `0x0036BED5` → [MiGetSharedProtos](../34/MiGetSharedProtos_function_00348D58.md) (function, `0x00348D58`)
- `0x0036BF4B` → [MiLockVadTree](../27/MiLockVadTree_function_0027C0F0.md) (function, `0x0027C0F0`)
- `0x0036BF54` → [MiLocateAddress](../31/MiLocateAddress_function_003168D0.md) (function, `0x003168D0`)
- `0x0036BF67` → [MiUnlockVadTree](../29/MiUnlockVadTree_function_00297020.md) (function, `0x00297020`)
- `0x0036BFAF` → [MiFreeInPageSupportBlock](../2B/MiFreeInPageSupportBlock_function_002B5900.md) (function, `0x002B5900`)
- `0x0036BFC4` → [KeInvalidAccessAllowed](../34/KeInvalidAccessAllowed_function_0034B3F0.md) (function, `0x0034B3F0`)
- `0x0036C010` → [MiGetInPageSupportBlock](MiGetInPageSupportBlock_function_00362500.md) (function, `0x00362500`)

### Direct callers
- [MiResolveProtoPteFault](../32/MiResolveProtoPteFault_function_00321750.md) at `0x00322244`
- [MiIssueFlowThroughFault](MiIssueFlowThroughFault_function_00369D64.md) at `0x00369E8A`

### Static image references
- `0x0036B6F5` → RVA `0x00E2DC80` (`.data`; read)
- `0x0036B77B` → RVA `0x00E30088` (`.data`; read)
- `0x0036B942` → RVA `0x00E37398` (`.data`; read)
- `0x0036B983` → RVA `0x00E2DCC0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0036B640  48 8B C4                        mov rax, rsp
0036B643  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
0036B647  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
0036B64B  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
0036B64F  48 89 48 08                     mov qword ptr [rax + 8], rcx
0036B653  55                              push rbp
0036B654  53                              push rbx
0036B655  56                              push rsi
0036B656  57                              push rdi
0036B657  41 54                           push r12
0036B659  41 55                           push r13
0036B65B  41 56                           push r14
0036B65D  41 57                           push r15
0036B65F  48 8D 68 A1                     lea rbp, [rax - 0x5f]
0036B663  48 81 EC E8 00 00 00            sub rsp, 0xe8
0036B66A  48 8B 01                        mov rax, qword ptr [rcx]
0036B66D  33 F6                           xor esi, esi
0036B66F  4C 8B F2                        mov r14, rdx
0036B672  48 89 45 9F                     mov qword ptr [rbp - 0x61], rax
0036B676  48 8B 41 38                     mov rax, qword ptr [rcx + 0x38]
0036B67A  4D 8B D1                        mov r10, r9
0036B67D  48 8B 51 10                     mov rdx, qword ptr [rcx + 0x10]
0036B681  0F 57 C0                        xorps xmm0, xmm0
0036B684  48 89 45 DF                     mov qword ptr [rbp - 0x21], rax
0036B688  44 8D 66 02                     lea r12d, [rsi + 2]
0036B68C  49 8B 1E                        mov rbx, qword ptr [r14]
0036B68F  4D 8B D8                        mov r11, r8
0036B692  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0036B69B  48 8B F9                        mov rdi, rcx
0036B69E  48 89 75 F7                     mov qword ptr [rbp - 9], rsi
0036B6A2  44 8B CE                        mov r9d, esi
0036B6A5  48 89 75 EF                     mov qword ptr [rbp - 0x11], rsi
0036B6A9  44 8B EE                        mov r13d, esi
0036B6AC  89 75 87                        mov dword ptr [rbp - 0x79], esi
0036B6AF  F6 80 A8 05 00 00 04            test byte ptr [rax + 0x5a8], 4
0036B6B6  0F 11 45 FF                     movups xmmword ptr [rbp - 1], xmm0
0036B6BA  89 75 A7                        mov dword ptr [rbp - 0x59], esi
0036B6BD  48 89 55 B7                     mov qword ptr [rbp - 0x49], rdx
0036B6C1  49 89 32                        mov qword ptr [r10], rsi
0036B6C4  48 89 75 BF                     mov qword ptr [rbp - 0x41], rsi
0036B6C8  0F 85 9C 04 00 00               jne 0x14036bb6a
0036B6CE  4C 8B C2                        mov r8, rdx
0036B6D1  B9 00 01 00 00                  mov ecx, 0x100
0036B6D6  41 83 E0 01                     and r8d, 1
0036B6DA  89 4D 8B                        mov dword ptr [rbp - 0x75], ecx
0036B6DD  48 83 E2 FE                     and rdx, 0xfffffffffffffffe
0036B6E1  4D 85 C0                        test r8, r8
0036B6E4  0F 85 FD 04 00 00               jne 0x14036bbe7
0036B6EA  48 0F BA E3 0A                  bt rbx, 0xa
0036B6EF  0F 83 B3 06 00 00               jae 0x14036bda8
0036B6F5  48 8B 05 84 25 AC 00            mov rax, qword ptr [rip + 0xac2584]
0036B6FC  4C 8B FB                        mov r15, rbx
0036B6FF  48 85 C0                        test rax, rax
0036B702  74 12                           je 0x14036b716
0036B704  F6 C3 10                        test bl, 0x10
0036B707  0F 85 05 04 00 00               jne 0x14036bb12
0036B70D  4C 8B F8                        mov r15, rax
0036B710  49 F7 D7                        not r15
0036B713  4C 23 FB                        and r15, rbx
0036B716  48 89 75 D7                     mov qword ptr [rbp - 0x29], rsi
0036B71A  49 C1 FF 10                     sar r15, 0x10
0036B71E  4D 8B 17                        mov r10, qword ptr [r15]
0036B721  4C 89 55 C7                     mov qword ptr [rbp - 0x39], r10
0036B725  41 8B 42 38                     mov eax, dword ptr [r10 + 0x38]
0036B729  A8 10                           test al, 0x10
0036B72B  0F 85 08 04 00 00               jne 0x14036bb39
0036B731  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
0036B735  83 4D 93 FF                     or dword ptr [rbp - 0x6d], 0xffffffff
0036B739  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
0036B73D  41 8B 47 20                     mov eax, dword ptr [r15 + 0x20]
0036B741  48 89 75 E7                     mov qword ptr [rbp - 0x19], rsi
0036B745  0F BA E0 11                     bt eax, 0x11
0036B749  0F 82 26 07 00 00               jb 0x14036be75
0036B74F  48 8B D6                        mov rdx, rsi
0036B752  41 8B 47 34                     mov eax, dword ptr [r15 + 0x34]
0036B756  41 8B 4F 2C                     mov ecx, dword ptr [r15 + 0x2c]
0036B75A  25 FF FF FF 3F                  and eax, 0x3fffffff
0036B75F  48 6B C0 F8                     imul rax, rax, -8
0036B763  48 03 45 CF                     add rax, qword ptr [rbp - 0x31]
0036B767  48 8D 0C C8                     lea rcx, [rax + rcx*8]
0036B76B  4C 3B F1                        cmp r14, rcx
0036B76E  0F 83 76 08 00 00               jae 0x14036bfea
0036B774  41 0F B7 4A 3C                  movzx ecx, word ptr [r10 + 0x3c]
0036B779  8B FE                           mov edi, esi
0036B77B  48 8B 05 06 49 AC 00            mov rax, qword ptr [rip + 0xac4906]
0036B782  81 E1 FF 03 00 00               and ecx, 0x3ff
0036B788  44 8B F6                        mov r14d, esi
0036B78B  89 75 8F                        mov dword ptr [rbp - 0x71], esi
0036B78E  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
0036B792  48 89 45 97                     mov qword ptr [rbp - 0x69], rax
0036B796  41 8A 42 3E                     mov al, byte ptr [r10 + 0x3e]
0036B79A  24 0C                           and al, 0xc
0036B79C  3C 04                           cmp al, 4
0036B79E  0F 84 6B 07 00 00               je 0x14036bf0f
0036B7A4  41 83 FE 02                     cmp r14d, 2
0036B7A8  0F 84 8C 00 00 00               je 0x14036b83a
0036B7AE  48 8B 4D 67                     mov rcx, qword ptr [rbp + 0x67]
0036B7B2  4C 8D 45 AF                     lea r8, [rbp - 0x51]
0036B7B6  49 8B D2                        mov rdx, r10
0036B7B9  48 89 75 AF                     mov qword ptr [rbp - 0x51], rsi
0036B7BD  E8 FE A8 F4 FF                  call 0x1402b60c0
0036B7C2  89 75 87                        mov dword ptr [rbp - 0x79], esi
0036B7C5  8B F8                           mov edi, eax
0036B7C7  44 8B CE                        mov r9d, esi
0036B7CA  41 83 FE 01                     cmp r14d, 1
0036B7CE  0F 84 82 06 00 00               je 0x14036be56
0036B7D4  4D 85 ED                        test r13, r13
0036B7D7  0F 85 E0 03 00 00               jne 0x14036bbbd
0036B7DD  48 0F BA E3 0A                  bt rbx, 0xa
0036B7E2  73 56                           jae 0x14036b83a
0036B7E4  48 8B 45 C7                     mov rax, qword ptr [rbp - 0x39]
0036B7E8  8B 40 38                        mov eax, dword ptr [rax + 0x38]
0036B7EB  A8 20                           test al, 0x20
0036B7ED  75 4B                           jne 0x14036b83a
0036B7EF  48 8B 45 DF                     mov rax, qword ptr [rbp - 0x21]
0036B7F3  8B 80 B8 00 00 00               mov eax, dword ptr [rax + 0xb8]
0036B7F9  A8 0F                           test al, 0xf
0036B7FB  75 3D                           jne 0x14036b83a
0036B7FD  4C 8B 75 AF                     mov r14, qword ptr [rbp - 0x51]
0036B801  4D 85 F6                        test r14, r14
0036B804  75 27                           jne 0x14036b82d
0036B806  41 8D 4D 01                     lea ecx, [r13 + 1]
0036B80A  E8 E1 08 F1 FF                  call 0x14027c0f0
0036B80F  48 8B 4D 9F                     mov rcx, qword ptr [rbp - 0x61]
0036B813  E8 B8 B0 FA FF                  call 0x1403168d0
0036B818  B2 11                           mov dl, 0x11
0036B81A  48 89 45 AF                     mov qword ptr [rbp - 0x51], rax
0036B81E  41 8D 4D 01                     lea ecx, [r13 + 1]
0036B822  4C 8B F0                        mov r14, rax
0036B825  E8 F6 B7 F2 FF                  call 0x140297020
0036B82A  44 8B CE                        mov r9d, esi
0036B82D  49 8B 4E 78                     mov rcx, qword ptr [r14 + 0x78]
0036B831  48 85 C9                        test rcx, rcx
0036B834  0F 89 B5 04 00 00               jns 0x14036bcef
0036B83A  41 81 F9 00 01 00 00            cmp r9d, 0x100
0036B841  0F 86 1B 06 00 00               jbe 0x14036be62
0036B847  41 83 CC 01                     or r12d, 1
0036B84B  48 8B 55 BF                     mov rdx, qword ptr [rbp - 0x41]
0036B84F  41 8B CC                        mov ecx, r12d
0036B852  83 C9 04                        or ecx, 4
0036B855  E8 A6 6C FF FF                  call 0x140362500
0036B85A  4C 8B F0                        mov r14, rax
0036B85D  48 85 C0                        test rax, rax
0036B860  75 44                           jne 0x14036b8a6
0036B862  48 8B 4D 77                     mov rcx, qword ptr [rbp + 0x77]
0036B866  B2 11                           mov dl, 0x11
0036B868  E8 23 A8 ED FF                  call 0x140246090
0036B86D  48 8B 55 BF                     mov rdx, qword ptr [rbp - 0x41]
0036B871  41 8B CC                        mov ecx, r12d
0036B874  E8 87 6C FF FF                  call 0x140362500
0036B879  4C 8B F0                        mov r14, rax
0036B87C  48 85 C0                        test rax, rax
0036B87F  0F 84 6F 07 00 00               je 0x14036bff4
0036B885  48 8B 4D 6F                     mov rcx, qword ptr [rbp + 0x6f]
0036B889  33 D2                           xor edx, edx
0036B88B  E8 F0 D2 F4 FF                  call 0x1402b8b80
0036B890  48 89 45 77                     mov qword ptr [rbp + 0x77], rax
0036B894  48 85 C0                        test rax, rax
0036B897  0F 84 0F 07 00 00               je 0x14036bfac
0036B89D  4D 85 F6                        test r14, r14
0036B8A0  0F 84 0E 07 00 00               je 0x14036bfb4
0036B8A6  48 8B 45 6F                     mov rax, qword ptr [rbp + 0x6f]
0036B8AA  48 8B 00                        mov rax, qword ptr [rax]
0036B8AD  48 3B C3                        cmp rax, rbx
0036B8B0  0F 85 78 05 00 00               jne 0x14036be2e
0036B8B6  48 0F BA E3 0A                  bt rbx, 0xa
0036B8BB  0F 83 52 05 00 00               jae 0x14036be13
0036B8C1  44 8B 65 8F                     mov r12d, dword ptr [rbp - 0x71]
0036B8C5  41 83 FC 02                     cmp r12d, 2
0036B8C9  0F 84 76 03 00 00               je 0x14036bc45
0036B8CF  4D 85 ED                        test r13, r13
0036B8D2  0F 85 FC 03 00 00               jne 0x14036bcd4
0036B8D8  41 8B 57 20                     mov edx, dword ptr [r15 + 0x20]
0036B8DC  4C 8B C3                        mov r8, rbx
0036B8DF  49 C1 E8 05                     shr r8, 5
0036B8E3  33 C9                           xor ecx, ecx
0036B8E5  D1 EA                           shr edx, 1
0036B8E7  41 83 E0 1F                     and r8d, 0x1f
0036B8EB  83 E2 1F                        and edx, 0x1f
0036B8EE  E8 4D 07 00 00                  call 0x14036c040
0036B8F3  8D 51 03                        lea edx, [rcx + 3]
0036B8F6  89 45 87                        mov dword ptr [rbp - 0x79], eax
0036B8F9  48 8B 4D DF                     mov rcx, qword ptr [rbp - 0x21]
0036B8FD  4C 8D 4D FF                     lea r9, [rbp - 1]
0036B901  44 8B C7                        mov r8d, edi
0036B904  E8 07 4B FB FF                  call 0x140320410
0036B909  48 83 CF FF                     or rdi, 0xffffffffffffffff
0036B90D  44 8D 4F 02                     lea r9d, [rdi + 2]
0036B911  45 3B E1                        cmp r12d, r9d
0036B914  74 41                           je 0x14036b957
0036B916  48 8B 45 C7                     mov rax, qword ptr [rbp - 0x39]
0036B91A  8B 48 38                        mov ecx, dword ptr [rax + 0x38]
0036B91D  81 E1 20 00 04 00               and ecx, 0x40020
0036B923  83 F9 20                        cmp ecx, 0x20
0036B926  0F 94 C1                        sete cl
0036B929  F6 40 3E 0C                     test byte ptr [rax + 0x3e], 0xc
0036B92D  0F 94 C0                        sete al
0036B930  22 C8                           and cl, al
0036B932  48 0F BA E3 0A                  bt rbx, 0xa
0036B937  0F 92 C0                        setb al
0036B93A  84 C8                           test al, cl
0036B93C  0F 84 EC 00 00 00               je 0x14036ba2e
0036B942  39 35 50 BA AC 00               cmp dword ptr [rip + 0xacba50], esi
0036B948  0F 85 E0 00 00 00               jne 0x14036ba2e
0036B94E  4D 85 ED                        test r13, r13
0036B951  0F 85 4C 03 00 00               jne 0x14036bca3
0036B957  4C 8B 65 97                     mov r12, qword ptr [rbp - 0x69]
0036B95B  45 8B C1                        mov r8d, r9d
0036B95E  49 8B D1                        mov rdx, r9
0036B961  49 8B CC                        mov rcx, r12
0036B964  E8 47 F5 F1 FF                  call 0x14028aeb0
0036B969  48 85 C0                        test rax, rax
0036B96C  0F 84 EC 01 00 00               je 0x14036bb5e
0036B972  48 8B 4D FF                     mov rcx, qword ptr [rbp - 1]
0036B976  B8 01 00 00 00                  mov eax, 1
0036B97B  F0 0F C1 01                     lock xadd dword ptr [rcx], eax
0036B97F  4C 8B 4D 07                     mov r9, qword ptr [rbp + 7]
0036B983  4C 8D 05 36 23 AC 00            lea r8, [rip + 0xac2336]
0036B98A  49 8B C9                        mov rcx, r9
0036B98D  33 D2                           xor edx, edx
0036B98F  48 C1 E9 10                     shr rcx, 0x10
0036B993  83 E1 03                        and ecx, 3
0036B996  41 F7 34 88                     div dword ptr [r8 + rcx*4]
0036B99A  41 33 D1                        xor edx, r9d
0036B99D  0F B6 FA                        movzx edi, dl
0036B9A0  41 33 F9                        xor edi, r9d
0036B9A3  41 C1 E9 09                     shr r9d, 9
0036B9A7  41 83 E1 3F                     and r9d, 0x3f
0036B9AB  48 0F BA E3 0A                  bt rbx, 0xa
0036B9B0  73 1F                           jae 0x14036b9d1
0036B9B2  48 8D 45 A7                     lea rax, [rbp - 0x59]
0036B9B6  4C 8B C3                        mov r8, rbx
0036B9B9  49 8B D7                        mov rdx, r15
0036B9BC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0036B9C1  49 8B CC                        mov rcx, r12
0036B9C4  E8 9F A2 FF FF                  call 0x140365c68
0036B9C9  85 C0                           test eax, eax
0036B9CB  0F 85 A0 01 00 00               jne 0x14036bb71
0036B9D1  41 B8 01 00 00 00               mov r8d, 1
0036B9D7  8B D7                           mov edx, edi
0036B9D9  49 8B CC                        mov rcx, r12
0036B9DC  E8 DF CA F1 FF                  call 0x1402884c0
0036B9E1  48 8B F8                        mov rdi, rax
0036B9E4  48 83 F8 FF                     cmp rax, -1
0036B9E8  0F 84 5E 01 00 00               je 0x14036bb4c
0036B9EE  83 7D 8F 01                     cmp dword ptr [rbp - 0x71], 1
0036B9F2  49 8B D7                        mov rdx, r15
0036B9F5  4C 8B 4D B7                     mov r9, qword ptr [rbp - 0x49]
0036B9F9  49 8B CE                        mov rcx, r14
0036B9FC  4C 8B 45 6F                     mov r8, qword ptr [rbp + 0x6f]
0036BA00  0F 84 00 02 00 00               je 0x14036bc06
0036BA06  48 8B 45 9F                     mov rax, qword ptr [rbp - 0x61]
0036BA0A  49 89 86 E0 00 00 00            mov qword ptr [r14 + 0xe0], rax
0036BA11  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
0036BA15  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0036BA1A  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
0036BA1F  E8 F4 2D F4 FF                  call 0x1402ae818
0036BA24  85 C0                           test eax, eax
0036BA26  0F 85 C5 00 00 00               jne 0x14036baf1
0036BA2C  EB 04                           jmp 0x14036ba32
0036BA2E  4C 8B 65 97                     mov r12, qword ptr [rbp - 0x69]
0036BA32  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
0036BA36  4D 8B C5                        mov r8, r13
0036BA39  4C 8B 4D CF                     mov r9, qword ptr [rbp - 0x31]
0036BA3D  49 8B D6                        mov rdx, r14
0036BA40  49 89 86 A0 00 00 00            mov qword ptr [r14 + 0xa0], rax
0036BA47  49 8B CC                        mov rcx, r12
0036BA4A  48 8B 45 6F                     mov rax, qword ptr [rbp + 0x6f]
0036BA4E  49 89 86 E8 00 00 00            mov qword ptr [r14 + 0xe8], rax
0036BA55  8B 45 8B                        mov eax, dword ptr [rbp - 0x75]
0036BA58  41 89 86 B8 00 00 00            mov dword ptr [r14 + 0xb8], eax
0036BA5F  48 8D 45 EF                     lea rax, [rbp - 0x11]
0036BA63  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0036BA68  48 8D 45 F7                     lea rax, [rbp - 9]
0036BA6C  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0036BA71  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
0036BA76  49 89 9E A8 00 00 00            mov qword ptr [r14 + 0xa8], rbx
0036BA7D  4D 89 BE D0 00 00 00            mov qword ptr [r14 + 0xd0], r15
0036BA84  E8 37 06 00 00                  call 0x14036c0c0
0036BA89  4C 8B 45 EF                     mov r8, qword ptr [rbp - 0x11]
0036BA8D  48 8B D8                        mov rbx, rax
0036BA90  48 8B 55 F7                     mov rdx, qword ptr [rbp - 9]
0036BA94  48 8D 45 FF                     lea rax, [rbp - 1]
0036BA98  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0036BA9D  4D 8B CC                        mov r9, r12
0036BAA0  48 8B 45 67                     mov rax, qword ptr [rbp + 0x67]
0036BAA4  49 8B CE                        mov rcx, r14
0036BAA7  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0036BAAC  8B 45 87                        mov eax, dword ptr [rbp - 0x79]
0036BAAF  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
0036BAB4  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0036BAB8  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
0036BABD  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0036BAC2  E8 45 7D FF FF                  call 0x14036380c
0036BAC7  8B F8                           mov edi, eax
0036BAC9  48 3B FB                        cmp rdi, rbx
0036BACC  0F 85 CA 00 00 00               jne 0x14036bb9c
0036BAD2  48 85 FF                        test rdi, rdi
0036BAD5  74 44                           je 0x14036bb1b
0036BAD7  8B 45 93                        mov eax, dword ptr [rbp - 0x6d]
0036BADA  4C 8B C7                        mov r8, rdi
0036BADD  4C 8B 4D D7                     mov r9, qword ptr [rbp - 0x29]
0036BAE1  49 8B CE                        mov rcx, r14
0036BAE4  48 8B 55 B7                     mov rdx, qword ptr [rbp - 0x49]
0036BAE8  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0036BAEC  E8 83 0E F4 FF                  call 0x1402ac974
0036BAF1  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
0036BAF5  4C 89 30                        mov qword ptr [rax], r14
0036BAF8  B8 33 33 03 C0                  mov eax, 0xc0033333
0036BAFD  48 81 C4 E8 00 00 00            add rsp, 0xe8
0036BB04  41 5F                           pop r15
0036BB06  41 5E                           pop r14
0036BB08  41 5D                           pop r13
0036BB0A  41 5C                           pop r12
0036BB0C  5F                              pop rdi
0036BB0D  5E                              pop rsi
0036BB0E  5B                              pop rbx
0036BB0F  5D                              pop rbp
0036BB10  C3                              ret
0036BB11  CC                              int3
0036BB12  49 83 E7 EF                     and r15, 0xffffffffffffffef
0036BB16  E9 FB FB FF FF                  jmp 0x14036b716
0036BB1B  41 BC 17 00 00 C0               mov r12d, 0xc0000017
0036BB21  48 8B 4D 77                     mov rcx, qword ptr [rbp + 0x77]
0036BB25  B2 11                           mov dl, 0x11
0036BB27  E8 64 A5 ED FF                  call 0x140246090
0036BB2C  49 8B CE                        mov rcx, r14
0036BB2F  E8 CC 9D F4 FF                  call 0x1402b5900
0036BB34  41 8B C4                        mov eax, r12d
0036BB37  EB C4                           jmp 0x14036bafd
0036BB39  BE 06 00 00 C0                  mov esi, 0xc0000006
0036BB3E  B2 11                           mov dl, 0x11
0036BB40  49 8B CB                        mov rcx, r11
0036BB43  E8 48 A5 ED FF                  call 0x140246090
0036BB48  8B C6                           mov eax, esi
0036BB4A  EB B1                           jmp 0x14036bafd
0036BB4C  B8 01 00 00 00                  mov eax, 1
0036BB51  49 8B CC                        mov rcx, r12
0036BB54  44 8B C0                        mov r8d, eax
0036BB57  8B D0                           mov edx, eax
0036BB59  E8 CA 1D 00 00                  call 0x14036d928
0036BB5E  83 7D 8F 01                     cmp dword ptr [rbp - 0x71], 1
0036BB62  0F 85 CA FE FF FF               jne 0x14036ba32
0036BB68  EB B1                           jmp 0x14036bb1b
0036BB6A  BE A1 00 00 C0                  mov esi, 0xc00000a1
0036BB6F  EB CD                           jmp 0x14036bb3e
0036BB71  8B 55 A7                        mov edx, dword ptr [rbp - 0x59]
0036BB74  83 FA 04                        cmp edx, 4
0036BB77  0F 87 54 FE FF FF               ja 0x14036b9d1
0036BB7D  89 74 24 28                     mov dword ptr [rsp + 0x28], esi
0036BB81  41 B9 10 00 00 00               mov r9d, 0x10
0036BB87  44 8B C7                        mov r8d, edi
0036BB8A  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0036BB8F  49 8B CC                        mov rcx, r12
0036BB92  E8 25 B4 00 00                  call 0x140376fbc
0036BB97  E9 45 FE FF FF                  jmp 0x14036b9e1
0036BB9C  48 2B DF                        sub rbx, rdi
0036BB9F  49 8B CC                        mov rcx, r12
0036BBA2  48 8B D3                        mov rdx, rbx
0036BBA5  E8 E6 AC F1 FF                  call 0x140286890
0036BBAA  45 33 C0                        xor r8d, r8d
0036BBAD  48 8B D3                        mov rdx, rbx
0036BBB0  49 8B CC                        mov rcx, r12
0036BBB3  E8 58 C8 ED FF                  call 0x140248410
0036BBB8  E9 15 FF FF FF                  jmp 0x14036bad2
0036BBBD  4C 8B 75 AF                     mov r14, qword ptr [rbp - 0x51]
0036BBC1  4D 85 F6                        test r14, r14
0036BBC4  0F 84 68 03 00 00               je 0x14036bf32
0036BBCA  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
0036BBCE  41 B9 02 00 00 00               mov r9d, 2
0036BBD4  4D 8B C6                        mov r8, r14
0036BBD7  49 8B D5                        mov rdx, r13
0036BBDA  E8 D5 79 FF FF                  call 0x1403635b4
0036BBDF  44 8B C8                        mov r9d, eax
0036BBE2  E9 53 FC FF FF                  jmp 0x14036b83a
0036BBE7  80 3A 05                        cmp byte ptr [rdx], 5
0036BBEA  0F 84 0A 03 00 00               je 0x14036befa
0036BBF0  8A 02                           mov al, byte ptr [rdx]
0036BBF2  3C 01                           cmp al, 1
0036BBF4  0F 84 92 01 00 00               je 0x14036bd8c
0036BBFA  41 3A C4                        cmp al, r12b
0036BBFD  4C 0F 44 EA                     cmove r13, rdx
0036BC01  E9 E4 FA FF FF                  jmp 0x14036b6ea
0036BC06  48 8B 45 E7                     mov rax, qword ptr [rbp - 0x19]
0036BC0A  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0036BC0F  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
0036BC13  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0036BC18  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
0036BC1D  E8 CA ED FF FF                  call 0x14036a9ec
0036BC22  44 8B E0                        mov r12d, eax
0036BC25  85 C0                           test eax, eax
0036BC27  0F 89 C4 FE FF FF               jns 0x14036baf1
0036BC2D  3D 55 00 00 C0                  cmp eax, 0xc0000055
0036BC32  0F 84 EB 03 00 00               je 0x14036c023
0036BC38  BF 34 04 00 C0                  mov edi, 0xc0000434
0036BC3D  3B C7                           cmp eax, edi
0036BC3F  0F 85 40 03 00 00               jne 0x14036bf85
0036BC45  48 8B 4D 77                     mov rcx, qword ptr [rbp + 0x77]
0036BC49  B2 11                           mov dl, 0x11
0036BC4B  E8 40 A4 ED FF                  call 0x140246090
0036BC50  48 8B 45 6F                     mov rax, qword ptr [rbp + 0x6f]
0036BC54  49 89 86 E8 00 00 00            mov qword ptr [r14 + 0xe8], rax
0036BC5B  41 89 B6 38 01 00 00            mov dword ptr [r14 + 0x138], esi
0036BC62  4D 89 BE D0 00 00 00            mov qword ptr [r14 + 0xd0], r15
0036BC69  41 89 B6 B8 00 00 00            mov dword ptr [r14 + 0xb8], esi
0036BC70  49 89 9E A8 00 00 00            mov qword ptr [r14 + 0xa8], rbx
0036BC77  49 89 B6 A0 00 00 00            mov qword ptr [r14 + 0xa0], rsi
0036BC7E  49 89 B6 00 01 00 00            mov qword ptr [r14 + 0x100], rsi
0036BC85  41 8B 86 C0 00 00 00            mov eax, dword ptr [r14 + 0xc0]
0036BC8C  0F BA F0 13                     btr eax, 0x13
0036BC90  83 C8 01                        or eax, 1
0036BC93  41 89 86 C0 00 00 00            mov dword ptr [r14 + 0xc0], eax
0036BC9A  41 89 76 50                     mov dword ptr [r14 + 0x50], esi
0036BC9E  E9 4E FE FF FF                  jmp 0x14036baf1
0036BCA3  4C 8B 65 97                     mov r12, qword ptr [rbp - 0x69]
0036BCA7  45 38 4D 00                     cmp byte ptr [r13], r9b
0036BCAB  0F 85 AA FC FF FF               jne 0x14036b95b
0036BCB1  41 8B 55 50                     mov edx, dword ptr [r13 + 0x50]
0036BCB5  49 8B CC                        mov rcx, r12
0036BCB8  C1 EA 03                        shr edx, 3
0036BCBB  83 E2 07                        and edx, 7
0036BCBE  41 03 D1                        add edx, r9d
0036BCC1  E8 7A 16 FE FF                  call 0x14034d340
0036BCC6  48 85 C0                        test rax, rax
0036BCC9  0F 84 63 FD FF FF               je 0x14036ba32
0036BCCF  E9 87 FC FF FF                  jmp 0x14036b95b
0036BCD4  41 80 7D 00 01                  cmp byte ptr [r13], 1
0036BCD9  0F 85 F9 FB FF FF               jne 0x14036b8d8
0036BCDF  49 8B D6                        mov rdx, r14
0036BCE2  49 8B CD                        mov rcx, r13
0036BCE5  E8 8A EC FF FF                  call 0x14036a974
0036BCEA  E9 E9 FB FF FF                  jmp 0x14036b8d8
0036BCEF  48 8B C1                        mov rax, rcx
0036BCF2  41 BA FF 0F 00 00               mov r10d, 0xfff
0036BCF8  49 23 C2                        and rax, r10
0036BCFB  48 83 F8 11                     cmp rax, 0x11
0036BCFF  0F 82 35 FB FF FF               jb 0x14036b83a
0036BD05  48 B8 FF FF FF FF FF FF 07 00   movabs rax, 0x7ffffffffffff
0036BD0F  48 8B D1                        mov rdx, rcx
0036BD12  48 C1 EA 0C                     shr rdx, 0xc
0036BD16  48 23 D0                        and rdx, rax
0036BD19  48 8B C1                        mov rax, rcx
0036BD1C  49 23 C2                        and rax, r10
0036BD1F  48 FF C8                        dec rax
0036BD22  48 03 D0                        add rdx, rax
0036BD25  48 8B 45 9F                     mov rax, qword ptr [rbp - 0x61]
0036BD29  48 25 00 F0 FF FF               and rax, 0xfffffffffffff000
0036BD2F  48 C1 E2 0C                     shl rdx, 0xc
0036BD33  48 3B C2                        cmp rax, rdx
0036BD36  0F 85 FE FA FF FF               jne 0x14036b83a
0036BD3C  4C 8B 4D 6F                     mov r9, qword ptr [rbp + 0x6f]
0036BD40  49 83 C1 08                     add r9, 8
0036BD44  45 85 CA                        test r10d, r9d
0036BD47  0F 84 56 02 00 00               je 0x14036bfa3
0036BD4D  41 8B 47 34                     mov eax, dword ptr [r15 + 0x34]
0036BD51  45 8B 47 2C                     mov r8d, dword ptr [r15 + 0x2c]
0036BD55  25 FF FF FF 3F                  and eax, 0x3fffffff
0036BD5A  48 6B D0 F8                     imul rdx, rax, -8
0036BD5E  48 8B 45 CF                     mov rax, qword ptr [rbp - 0x31]
0036BD62  48 03 C2                        add rax, rdx
0036BD65  4A 8D 14 C0                     lea rdx, [rax + r8*8]
0036BD69  4C 3B CA                        cmp r9, rdx
0036BD6C  0F 83 31 02 00 00               jae 0x14036bfa3
0036BD72  49 8B 01                        mov rax, qword ptr [r9]
0036BD75  48 3B C3                        cmp rax, rbx
0036BD78  0F 85 25 02 00 00               jne 0x14036bfa3
0036BD7E  44 8B C9                        mov r9d, ecx
0036BD81  45 23 CA                        and r9d, r10d
0036BD84  41 FF C9                        dec r9d
0036BD87  E9 AE FA FF FF                  jmp 0x14036b83a
0036BD8C  4C 8B EA                        mov r13, rdx
0036BD8F  85 4A 50                        test dword ptr [rdx + 0x50], ecx
0036BD92  0F 85 A6 FD FF FF               jne 0x14036bb3e
0036BD98  48 8B 42 70                     mov rax, qword ptr [rdx + 0x70]
0036BD9C  44 8B E6                        mov r12d, esi
0036BD9F  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
0036BDA3  E9 42 F9 FF FF                  jmp 0x14036b6ea
0036BDA8  48 8B 0D D1 1E AC 00            mov rcx, qword ptr [rip + 0xac1ed1]
0036BDAF  48 8B C3                        mov rax, rbx
0036BDB2  48 85 C9                        test rcx, rcx
0036BDB5  74 0E                           je 0x14036bdc5
0036BDB7  F6 C3 10                        test bl, 0x10
0036BDBA  75 51                           jne 0x14036be0d
0036BDBC  48 8B C1                        mov rax, rcx
0036BDBF  48 F7 D0                        not rax
0036BDC2  48 23 C3                        and rax, rbx
0036BDC5  48 C1 E8 0C                     shr rax, 0xc
0036BDC9  49 BA FF FF FF FF FF 00 00 00   movabs r10, 0xffffffffff
0036BDD3  49 23 C2                        and rax, r10
0036BDD6  48 8D 3C 40                     lea rdi, [rax + rax*2]
0036BDDA  48 C1 E7 04                     shl rdi, 4
0036BDDE  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0036BDE8  48 03 F8                        add rdi, rax
0036BDEB  48 89 7D D7                     mov qword ptr [rbp - 0x29], rdi
0036BDEF  4C 8B 7F 10                     mov r15, qword ptr [rdi + 0x10]
0036BDF3  48 85 C9                        test rcx, rcx
0036BDF6  74 0C                           je 0x14036be04
0036BDF8  41 F6 C7 10                     test r15b, 0x10
0036BDFC  75 06                           jne 0x14036be04
0036BDFE  48 F7 D1                        not rcx
0036BE01  4C 23 F9                        and r15, rcx
0036BE04  48 8B 7D 67                     mov rdi, qword ptr [rbp + 0x67]
0036BE08  E9 0D F9 FF FF                  jmp 0x14036b71a
0036BE0D  48 83 E0 EF                     and rax, 0xffffffffffffffef
0036BE11  EB B2                           jmp 0x14036bdc5
0036BE13  48 8B 4D D7                     mov rcx, qword ptr [rbp - 0x29]
0036BE17  F6 41 22 20                     test byte ptr [rcx + 0x22], 0x20
0036BE1B  74 11                           je 0x14036be2e
0036BE1D  48 8B 01                        mov rax, qword ptr [rcx]
0036BE20  8B 80 A0 00 00 00               mov eax, dword ptr [rax + 0xa0]
0036BE26  84 C0                           test al, al
0036BE28  0F 89 93 FA FF FF               jns 0x14036b8c1
0036BE2E  48 8B 4D 77                     mov rcx, qword ptr [rbp + 0x77]
0036BE32  B2 11                           mov dl, 0x11
0036BE34  BF 34 04 00 C0                  mov edi, 0xc0000434
0036BE39  E8 52 A2 ED FF                  call 0x140246090
0036BE3E  49 8B CE                        mov rcx, r14
0036BE41  E8 BA 9A F4 FF                  call 0x1402b5900
0036BE46  4D 85 ED                        test r13, r13
0036BE49  0F 85 22 01 00 00               jne 0x14036bf71
0036BE4F  8B C7                           mov eax, edi
0036BE51  E9 A7 FC FF FF                  jmp 0x14036bafd
0036BE56  C7 45 8B 01 00 00 00            mov dword ptr [rbp - 0x75], 1
0036BE5D  E9 E9 F9 FF FF                  jmp 0x14036b84b
0036BE62  44 89 4D 8B                     mov dword ptr [rbp - 0x75], r9d
0036BE66  41 83 F9 10                     cmp r9d, 0x10
0036BE6A  0F 86 DB F9 FF FF               jbe 0x14036b84b
0036BE70  E9 D2 F9 FF FF                  jmp 0x14036b847
0036BE75  41 F7 42 38 00 00 00 08         test dword ptr [r10 + 0x38], 0x8000000
0036BE7D  0F 84 CC F8 FF FF               je 0x14036b74f
0036BE83  48 8B 4D 9F                     mov rcx, qword ptr [rbp - 0x61]
0036BE87  E8 D4 AD FD FF                  call 0x140346c60
0036BE8C  89 45 93                        mov dword ptr [rbp - 0x6d], eax
0036BE8F  48 B8 00 00 00 00 00 80 FF FF   movabs rax, 0xffff800000000000
0036BE99  48 39 45 9F                     cmp qword ptr [rbp - 0x61], rax
0036BE9D  72 2C                           jb 0x14036becb
0036BE9F  4D 85 C0                        test r8, r8
0036BEA2  0F 84 16 01 00 00               je 0x14036bfbe
0036BEA8  80 3A 01                        cmp byte ptr [rdx], 1
0036BEAB  0F 84 24 01 00 00               je 0x14036bfd5
0036BEB1  80 3A 03                        cmp byte ptr [rdx], 3
0036BEB4  0F 84 1B 01 00 00               je 0x14036bfd5
0036BEBA  48 8B 45 B7                     mov rax, qword ptr [rbp - 0x49]
0036BEBE  48 83 E0 FE                     and rax, 0xfffffffffffffffe
0036BEC2  80 38 06                        cmp byte ptr [rax], 6
0036BEC5  0F 84 0A 01 00 00               je 0x14036bfd5
0036BECB  8B 55 93                        mov edx, dword ptr [rbp - 0x6d]
0036BECE  4D 8B C7                        mov r8, r15
0036BED1  48 8B 4D C7                     mov rcx, qword ptr [rbp - 0x39]
0036BED5  E8 7E CE FD FF                  call 0x140348d58
0036BEDA  44 8B 4D 87                     mov r9d, dword ptr [rbp - 0x79]
0036BEDE  48 8B D0                        mov rdx, rax
0036BEE1  4C 8B 55 C7                     mov r10, qword ptr [rbp - 0x39]
0036BEE5  4C 8B 5D 77                     mov r11, qword ptr [rbp + 0x77]
0036BEE9  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
0036BEED  48 8B 40 48                     mov rax, qword ptr [rax + 0x48]
0036BEF1  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
0036BEF5  E9 58 F8 FF FF                  jmp 0x14036b752
0036BEFA  8B 42 38                        mov eax, dword ptr [rdx + 0x38]
0036BEFD  A8 04                           test al, 4
0036BEFF  0F 84 E5 F7 FF FF               je 0x14036b6ea
0036BF05  BE 17 00 00 C0                  mov esi, 0xc0000017
0036BF0A  E9 2F FC FF FF                  jmp 0x14036bb3e
0036BF0F  48 8B C2                        mov rax, rdx
0036BF12  44 8B CE                        mov r9d, esi
0036BF15  48 F7 D8                        neg rax
0036BF18  44 8B E6                        mov r12d, esi
0036BF1B  45 1B F6                        sbb r14d, r14d
0036BF1E  41 83 C6 02                     add r14d, 2
0036BF22  48 85 D2                        test rdx, rdx
0036BF25  44 89 75 8F                     mov dword ptr [rbp - 0x71], r14d
0036BF29  41 0F 94 C1                     sete r9b
0036BF2D  E9 72 F8 FF FF                  jmp 0x14036b7a4
0036BF32  48 B8 FF FF FE FF FF 7F 00 00   movabs rax, 0x7ffffffeffff
0036BF3C  48 39 45 9F                     cmp qword ptr [rbp - 0x61], rax
0036BF40  0F 87 84 FC FF FF               ja 0x14036bbca
0036BF46  B9 01 00 00 00                  mov ecx, 1
0036BF4B  E8 A0 01 F1 FF                  call 0x14027c0f0
0036BF50  48 8B 4D 9F                     mov rcx, qword ptr [rbp - 0x61]
0036BF54  E8 77 A9 FA FF                  call 0x1403168d0
0036BF59  B2 11                           mov dl, 0x11
0036BF5B  48 89 45 AF                     mov qword ptr [rbp - 0x51], rax
0036BF5F  B9 01 00 00 00                  mov ecx, 1
0036BF64  4C 8B F0                        mov r14, rax
0036BF67  E8 B4 B0 F2 FF                  call 0x140297020
0036BF6C  E9 59 FC FF FF                  jmp 0x14036bbca
0036BF71  81 FF 9A 00 00 C0               cmp edi, 0xc000009a
0036BF77  0F 94 C1                        sete cl
0036BF7A  FE C1                           inc cl
0036BF7C  41 88 4D 01                     mov byte ptr [r13 + 1], cl
0036BF80  E9 CA FE FF FF                  jmp 0x14036be4f
0036BF85  3D 33 33 03 C0                  cmp eax, 0xc0033333
0036BF8A  0F 85 91 FB FF FF               jne 0x14036bb21
0036BF90  48 8B 45 67                     mov rax, qword ptr [rbp + 0x67]
0036BF94  41 BC 16 00 00 C0               mov r12d, 0xc0000016
0036BF9A  83 48 50 08                     or dword ptr [rax + 0x50], 8
0036BF9E  E9 7E FB FF FF                  jmp 0x14036bb21
0036BFA3  44 8B 4D 87                     mov r9d, dword ptr [rbp - 0x79]
0036BFA7  E9 8E F8 FF FF                  jmp 0x14036b83a
0036BFAC  49 8B CE                        mov rcx, r14
0036BFAF  E8 4C 99 F4 FF                  call 0x1402b5900
0036BFB4  BF 9A 00 00 C0                  mov edi, 0xc000009a
0036BFB9  E9 88 FE FF FF                  jmp 0x14036be46
0036BFBE  48 8B 4D B7                     mov rcx, qword ptr [rbp - 0x49]
0036BFC2  33 D2                           xor edx, edx
0036BFC4  E8 27 F4 FD FF                  call 0x14034b3f0
0036BFC9  84 C0                           test al, al
0036BFCB  0F 84 FA FE FF FF               je 0x14036becb
0036BFD1  4C 8B 5D 77                     mov r11, qword ptr [rbp + 0x77]
0036BFD5  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
0036BFD9  A8 01                           test al, 1
0036BFDB  74 0D                           je 0x14036bfea
0036BFDD  48 83 E0 FE                     and rax, 0xfffffffffffffffe
0036BFE1  80 38 06                        cmp byte ptr [rax], 6
0036BFE4  0F 84 E1 FE FF FF               je 0x14036becb
0036BFEA  BE 05 00 00 C0                  mov esi, 0xc0000005
0036BFEF  E9 4A FB FF FF                  jmp 0x14036bb3e
0036BFF4  41 F6 C4 01                     test r12b, 1
0036BFF8  0F 84 9F F8 FF FF               je 0x14036b89d
0036BFFE  48 8B 55 BF                     mov rdx, qword ptr [rbp - 0x41]
0036C002  41 83 E4 FE                     and r12d, 0xfffffffe
0036C006  41 8B CC                        mov ecx, r12d
0036C009  C7 45 8B 10 00 00 00            mov dword ptr [rbp - 0x75], 0x10
0036C010  E8 EB 64 FF FF                  call 0x140362500
0036C015  4C 8B F0                        mov r14, rax
0036C018  48 85 C0                        test rax, rax
0036C01B  0F 85 64 F8 FF FF               jne 0x14036b885
0036C021  EB 91                           jmp 0x14036bfb4
0036C023  44 8B E6                        mov r12d, esi
0036C026  E9 F6 FA FF FF                  jmp 0x14036bb21
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiResolveMappedFileFault(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p30;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (232);
    v_rsi = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 97) = *(unsigned __int64 *)(a1);
    *(unsigned __int64 *)(v_rsp - 95 - 33) = *(unsigned __int64 *)(a1 + 56);
    *(unsigned __int64 *)(v_rsp - 95 - 9) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 17) = 0;
    *(unsigned int *)(v_rsp - 95 - 121) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 1) = v_xmm0;
    *(unsigned int *)(v_rsp - 95 - 89) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 73) = *(unsigned __int64 *)(a1 + 16);
    *(unsigned __int64 *)(a4) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 65) = 0;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1448)) & (4)) != 0) goto loc_0036BB6A;
    a3 = (unsigned int)((*(unsigned __int64 *)(a1 + 16)) & (1));
    *(unsigned int *)(v_rsp - 95 - 117) = 256;
    a2 = (*(unsigned __int64 *)(a1 + 16)) & (-2);
    if (a3 != 0) goto loc_0036BBE7;
loc_0036B6EA:
    if (condition_is_above_or_equal) goto loc_0036BDA8;
    if (*(unsigned __int64 *)(v_rip + 11281796) == 0) goto loc_0036B716;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a2))) & (16)) != 0) goto loc_0036BB12;
    v_r15 = ~(*(unsigned __int64 *)(v_rip + 11281796));
    v_r15 = (v_r15) & (*(unsigned __int64 *)(a2));
loc_0036B716:
    *(unsigned __int64 *)(v_rsp - 95 - 41) = 0;
loc_0036B71A:
    v_r15 = (v_r15) >> (16);
    *(unsigned __int64 *)(v_rsp - 95 - 57) = *(unsigned __int64 *)(v_r15);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r15) + 56)))) & (16)) != 0) goto loc_0036BB39;
    *(unsigned __int64 *)(v_rsp - 95 - 49) = *(unsigned __int64 *)(v_r15 + 8);
    *(unsigned __int64 *)(v_rsp - 95 - 25) = 0;
    if (condition_is_below) goto loc_0036BE75;
loc_0036B74F:
loc_0036B752:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r15 + 52))) & (0x3FFFFFFFULL));
    result = (result) * (result);
    result = (result) + (*(unsigned __int64 *)(v_rsp - 95 - 49));
    if (a2 >= (result + (unsigned int)(*(unsigned int *)(v_r15 + 44)) * 8)) goto loc_0036BFEA;
    a1 = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_r15) + 60)) & (0x3FFULL));
    *(unsigned int *)(v_rsp - 95 - 113) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 105) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11290886) + a1 * 8);
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_r15) + 62)) & (12));
    if (((unsigned __int8)(result)) == 4) goto loc_0036BF0F;
loc_0036B7A4:
    if (0 == 2) goto loc_0036B83A;
    *(unsigned __int64 *)(v_rsp - 95 - 81) = 0;
    result = MiComputeFaultNode(*(unsigned __int64 *)(v_rsp - 95 + 103), *(unsigned __int64 *)(v_r15), v_rsp - 95 - 81, 0);
    *(unsigned int *)(v_rsp - 95 - 121) = 0;
    if (0 == 1) goto loc_0036BE56;
    if (0 != 0) goto loc_0036BBBD;
    if (condition_is_above_or_equal) goto loc_0036B83A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 - 57) + 56)))) & (32)) != 0) goto loc_0036B83A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 - 33) + 184)))) & (15)) != 0) goto loc_0036B83A;
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 - 33) + 184));
    v_r14 = *(unsigned __int64 *)(v_rsp - 95 - 81);
    if (*(unsigned __int64 *)(v_rsp - 95 - 81) == 0) {
        a1 = 0 + 1;
        result = MiLockVadTree(a1, *(unsigned __int64 *)(v_r15), v_rsp - 95 - 81, 0);
        a1 = *(unsigned __int64 *)(v_rsp - 95 - 97);
        result = MiLocateAddress(a1, *(unsigned __int64 *)(v_r15), v_rsp - 95 - 81, 0);
        a2 = 17;
        *(unsigned __int64 *)(v_rsp - 95 - 81) = result;
        a1 = 0 + 1;
        v_r14 = result;
        result = MiUnlockVadTree(a1, a2, v_rsp - 95 - 81, 0);
        a4 = 0;
    }
    if (!sign_flag) goto loc_0036BCEF;
loc_0036B83A:
    if (((unsigned int)(a4)) <= 256) goto loc_0036BE62;
loc_0036B847:
    v_r12 = (unsigned int)((v_rsi + 2) | (1));
loc_0036B84B:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) | (4));
    result = MiGetInPageSupportBlock(a1, *(unsigned __int64 *)(v_rsp - 95 - 65), v_rsp - 95 - 81, a4);
    if (result != 0) goto loc_0036B8A6;
    result = MiUnlockProtoPoolPage(*(unsigned __int64 *)(v_rsp - 95 + 119), 17, v_rsp - 95 - 81, a4);
    result = MiGetInPageSupportBlock((unsigned int)((unsigned int)(v_r12)), *(unsigned __int64 *)(v_rsp - 95 - 65), v_rsp - 95 - 81, a4);
    if (result == 0) goto loc_0036BFF4;
loc_0036B885:
    a2 = 0;
    result = MiLockProtoPoolPage(*(unsigned __int64 *)(v_rsp - 95 + 111), a2, v_rsp - 95 - 81, a4);
    *(unsigned __int64 *)(v_rsp - 95 + 119) = result;
    if (result == 0) goto loc_0036BFAC;
loc_0036B89D:
    if (result == 0) goto loc_0036BFB4;
loc_0036B8A6:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 + 111))) != (*(unsigned __int64 *)(a2))) goto loc_0036BE2E;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 + 111))) >= (*(unsigned __int64 *)(a2))) goto loc_0036BE13;
loc_0036B8C1:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 113)))) == 2) goto loc_0036BC45;
    if (0 != 0) goto loc_0036BCD4;
loc_0036B8D8:
    a3 = (*(unsigned __int64 *)(a2)) >> (5);
    a1 = 0;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r15 + 32))) >> (1));
    a3 = (unsigned int)((a3) & (31));
    a2 = (unsigned int)((a2) & (31));
    result = MiSanitizePfnProtection(a1, a2, a3, a4);
    *(unsigned int *)(v_rsp - 95 - 121) = (unsigned int)(result);
    result = MiInitializePageColorBase(*(unsigned __int64 *)(v_rsp - 95 - 33), a1 + 3, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_rsp - 95 - 1);
    v_rdi = ((unsigned int)((unsigned int)(result))) | (-1);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 113)))) == ((unsigned int)(v_rdi + 2))) goto loc_0036B957;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 - 57) + 56))) & (0x40020ULL));
    a1 = (((unsigned int)(a1)) == 32) ? 1 : 0;
    result = (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 95 - 57) + 62)) & (12)) == 0) ? 1 : 0;
    a1 = (unsigned __int8)((a1) & ((unsigned __int8)(result)));
    result = (condition_is_below) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_0036BA2E;
    if ((*(unsigned int *)(v_rip + 11319888)) != 0) goto loc_0036BA2E;
    if (0 != 0) goto loc_0036BCA3;
loc_0036B957:
loc_0036B95B:
    result = MiObtainFaultCharges(*(unsigned __int64 *)(v_rsp - 95 - 105), v_rdi + 2, (unsigned int)((unsigned int)(v_rdi + 2)), v_rdi + 2);
    if (result == 0) goto loc_0036BB5E;
    a2 = 0;
    a1 = (*(unsigned __int64 *)(v_rsp - 95 + 7)) >> (16);
    a1 = (unsigned int)((a1) & (3));
    a2 = (unsigned int)((a2) ^ ((unsigned int)(*(unsigned __int64 *)(v_rsp - 95 + 7))));
    v_rdi = (unsigned int)(((unsigned __int8)(a2)) ^ ((unsigned int)(*(unsigned __int64 *)(v_rsp - 95 + 7))));
    a4 = (unsigned int)((*(unsigned __int64 *)(v_rsp - 95 + 7)) >> (9));
    a4 = (unsigned int)((a4) & (63));
    if (condition_is_above_or_equal) goto loc_0036B9D1;
    v_stack_m108 = v_rsp - 95 - 89;
    result = MiUseSlabAllocator(*(unsigned __int64 *)(v_rsp - 95 - 105), v_r15, *(unsigned __int64 *)(a2), a4);
    if ((unsigned int)(result) != 0) goto loc_0036BB71;
loc_0036B9D1:
    result = MiGetPage(*(unsigned __int64 *)(v_rsp - 95 - 105), (unsigned int)((unsigned int)(v_rdi)), 1, a4);
loc_0036B9E1:
    if (result == -1) goto loc_0036BB4C;
    if ((*(unsigned int *)(v_rsp - 95 - 113)) == 1) goto loc_0036BC06;
    *(unsigned __int64 *)(result + 224) = *(unsigned __int64 *)(v_rsp - 95 - 97);
    v_stack_m100 = *(unsigned __int64 *)(v_rsp - 95 + 119);
    v_stack_m108 = result;
    result = MiCopyDataPageToImagePage(result, v_r15, *(unsigned __int64 *)(v_rsp - 95 + 111), *(unsigned __int64 *)(v_rsp - 95 - 73));
    if ((unsigned int)(result) != 0) goto loc_0036BAF1;
    goto loc_0036BA32;
loc_0036BA2E:
loc_0036BA32:
    *(unsigned __int64 *)(result + 160) = *(unsigned __int64 *)(v_rsp - 95 + 119);
    *(unsigned __int64 *)(result + 232) = *(unsigned __int64 *)(v_rsp - 95 + 111);
    *(unsigned int *)(result + 184) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 117)));
    v_stack_mF8 = v_rsp - 95 - 17;
    v_stack_m100 = v_rsp - 95 - 9;
    v_stack_m108 = result;
    *(unsigned __int64 *)(result + 168) = *(unsigned __int64 *)(a2);
    *(unsigned __int64 *)(result + 208) = v_r15;
    result = MiPickClusterForMappedFileFault(*(unsigned __int64 *)(v_rsp - 95 - 105), result, 0, *(unsigned __int64 *)(v_rsp - 95 - 49));
    v_stack_mE0 = v_rsp - 95 - 1;
    v_stack_mE8 = *(unsigned __int64 *)(v_rsp - 95 + 103);
    v_stack_mF0 = 0;
    v_stack_mF8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 121)));
    v_stack_m100 = result;
    v_stack_m108 = result;
    result = MiBuildMdlForMappedFileFault(result, *(unsigned __int64 *)(v_rsp - 95 - 9), *(unsigned __int64 *)(v_rsp - 95 - 17), *(unsigned __int64 *)(v_rsp - 95 - 105));
    if (((unsigned int)((unsigned int)(result))) != result) goto loc_0036BB9C;
loc_0036BAD2:
    if ((unsigned int)((unsigned int)(result)) == 0) goto loc_0036BB1B;
    v_stack_m108 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 109)));
    result = MiFinishMdlForMappedFileFault(result, *(unsigned __int64 *)(v_rsp - 95 - 73), (unsigned int)((unsigned int)(result)), *(unsigned __int64 *)(v_rsp - 95 - 41));
loc_0036BAF1:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 + 127)) = result;
loc_0036BAFD:
    v_rsp = (v_rsp) + (232);
    return (unsigned int)(0xC0033333ULL);
loc_0036BB12:
    v_r15 = (v_r15) & (-17);
    goto loc_0036B716;
loc_0036BB1B:
loc_0036BB21:
    result = MiUnlockProtoPoolPage(*(unsigned __int64 *)(v_rsp - 95 + 119), 17, (unsigned int)((unsigned int)(result)), *(unsigned __int64 *)(v_rsp - 95 - 41));
    result = MiFreeInPageSupportBlock(result, 17, (unsigned int)((unsigned int)(result)), *(unsigned __int64 *)(v_rsp - 95 - 41));
    goto loc_0036BAFD;
loc_0036BB39:
loc_0036BB3E:
    result = MiUnlockProtoPoolPage(a3, 17, (unsigned int)((unsigned int)(result)), *(unsigned __int64 *)(v_rsp - 95 - 41));
    goto loc_0036BAFD;
loc_0036BB4C:
    result = MiReturnFaultCharges((unsigned int)(0xC0000017ULL), 1, 1, *(unsigned __int64 *)(v_rsp - 95 - 41));
loc_0036BB5E:
    if ((*(unsigned int *)(v_rsp - 95 - 113)) != 1) goto loc_0036BA32;
    goto loc_0036BB1B;
loc_0036BB6A:
    goto loc_0036BB3E;
loc_0036BB71:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 89)))) > 4) goto loc_0036B9D1;
    v_stack_p28 = (unsigned int)((unsigned int)(0xC00000A1ULL));
    v_stack_p20 = (unsigned int)(0xC00000A1ULL);
    result = MiGetSlabPage((unsigned int)(0xC0000017ULL), (unsigned int)(*(unsigned int *)(v_rsp - 95 - 89)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), 16);
    goto loc_0036B9E1;
loc_0036BB9C:
    v_rbx = (result) - ((unsigned int)((unsigned int)(result)));
    result = MiReturnResident((unsigned int)(0xC0000017ULL), v_rbx, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), 16);
    a3 = 0;
    result = MiReturnCommit((unsigned int)(0xC0000017ULL), v_rbx, a3, 16);
    goto loc_0036BAD2;
loc_0036BBBD:
    if (*(unsigned __int64 *)(v_rsp - 95 - 81) == 0) goto loc_0036BF32;
loc_0036BBCA:
    result = MiComputeFaultCluster(*(unsigned __int64 *)(v_rsp - 95 - 105), 0, *(unsigned __int64 *)(v_rsp - 95 - 81), 2);
    goto loc_0036B83A;
loc_0036BBE7:
    if ((*(unsigned __int8 *)(0)) == 5) goto loc_0036BEFA;
    if (((unsigned __int8)(*(unsigned __int8 *)(0))) == 1) goto loc_0036BD8C;
    v_r13 = 0;
    if (((unsigned __int8)(*(unsigned __int8 *)(0))) == ((unsigned __int8)((unsigned int)(0xC0000017ULL)))) { v_r13 = 0; }
    goto loc_0036B6EA;
loc_0036BC06:
    v_stack_p30 = *(unsigned __int64 *)(v_rsp - 95 - 25);
    v_stack_p28 = *(unsigned __int64 *)(v_rsp - 95 + 119);
    v_stack_p20 = (unsigned int)((unsigned int)(result));
    result = MiCopyFileOnlyGlobalSubsectionPage(*(unsigned __int64 *)(v_rsp - 95 - 105), 0, *(unsigned __int64 *)(v_rsp - 95 - 81), (unsigned int)((unsigned int)(result)));
    if (!sign_flag) goto loc_0036BAF1;
    if (((unsigned int)(result)) == 0xC0000055ULL) goto loc_0036C023;
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0xC0000434ULL)))) goto loc_0036BF85;
loc_0036BC45:
    result = MiUnlockProtoPoolPage(*(unsigned __int64 *)(v_rsp - 95 + 119), 17, *(unsigned __int64 *)(v_rsp - 95 - 81), (unsigned int)((unsigned int)(result)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 81) + 232) = *(unsigned __int64 *)(v_rsp - 95 + 111);
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 - 81) + 312) = (unsigned int)((unsigned int)(0xC00000A1ULL));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 81) + 208) = v_r15;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 - 81) + 184) = (unsigned int)((unsigned int)(0xC00000A1ULL));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 81) + 168) = v_rbx;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 81) + 160) = (unsigned int)(0xC00000A1ULL);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 81) + 256) = (unsigned int)(0xC00000A1ULL);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 - 81) + 192))) | (1));
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 - 81) + 192) = (unsigned int)(result);
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 - 81) + 80) = (unsigned int)((unsigned int)(0xC00000A1ULL));
    goto loc_0036BAF1;
loc_0036BCA3:
    if ((*(unsigned __int8 *)(v_r13)) != ((unsigned __int8)((unsigned int)((unsigned int)(result))))) goto loc_0036B95B;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r13 + 80))) >> (3));
    a2 = (unsigned int)((a2) & (7));
    a2 = (unsigned int)((a2) + ((unsigned int)((unsigned int)((unsigned int)(result)))));
    result = MiGetAvailablePagesBelowPriority(*(unsigned __int64 *)(v_rsp - 95 - 105), a2, *(unsigned __int64 *)(v_rsp - 95 - 81), (unsigned int)((unsigned int)(result)));
    if (result == 0) goto loc_0036BA32;
    goto loc_0036B95B;
loc_0036BCD4:
    if ((*(unsigned __int8 *)(v_r13)) != 1) goto loc_0036B8D8;
    result = MiSetInPagePrefetchPriority(v_r13, *(unsigned __int64 *)(v_rsp - 95 - 81), *(unsigned __int64 *)(v_rsp - 95 - 81), (unsigned int)((unsigned int)(result)));
    goto loc_0036B8D8;
loc_0036BCEF:
    result = (v_r13) & ((unsigned int)(0xFFFULL));
    if (result < 17) goto loc_0036B83A;
    a2 = (v_r13) >> (12);
    a2 = (a2) & (result);
    result = (v_r13) & ((unsigned int)(0xFFFULL));
    result = (result) - 1;
    a2 = (a2) + (result);
    result = (*(unsigned __int64 *)(v_rsp - 95 - 97)) & (0xFFFFFFFFFFFFF000ULL);
    a2 = (a2) << (12);
    if (result != a2) goto loc_0036B83A;
    a4 = (*(unsigned __int64 *)(v_rsp - 95 + 111)) + (8);
    if ((((unsigned int)((unsigned int)(0xFFFULL))) & ((unsigned int)(a4))) == 0) goto loc_0036BFA3;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r15 + 52))) & (0x3FFFFFFFULL));
    a2 = (a2) * (result);
    result = (*(unsigned __int64 *)(v_rsp - 95 - 49)) + (a2);
    if (a4 >= (result + (unsigned int)(*(unsigned int *)(v_r15 + 44)) * 8)) goto loc_0036BFA3;
    if ((*(unsigned __int64 *)(a4)) != v_rbx) goto loc_0036BFA3;
    a4 = (unsigned int)(((unsigned int)((unsigned int)(v_r13))) & ((unsigned int)((unsigned int)(0xFFFULL))));
    a4 = (unsigned int)((a4) - 1);
    goto loc_0036B83A;
loc_0036BD8C:
    if (((*(unsigned int *)(result + (unsigned int)(*(unsigned int *)(v_r15 + 44)) * 8 + 80)) & ((unsigned int)(v_r13))) != 0) goto loc_0036BB3E;
    *(unsigned __int64 *)(v_rsp - 95 - 65) = *(unsigned __int64 *)(result + (unsigned int)(*(unsigned int *)(v_r15 + 44)) * 8 + 112);
    goto loc_0036B6EA;
loc_0036BDA8:
    if (*(unsigned __int64 *)(v_rip + 11280081) == 0) goto loc_0036BDC5;
    if ((((unsigned __int8)(v_rbx)) & (16)) != 0) goto loc_0036BE0D;
    result = ~(*(unsigned __int64 *)(v_rip + 11280081));
    result = (result) & (v_rbx);
loc_0036BDC5:
    result = (result) >> (12);
    result = (result) & ((unsigned int)(0xFFFULL));
    v_rdi = (result + result * 2) << (4);
    v_rdi = (v_rdi) + (result);
    *(unsigned __int64 *)(v_rsp - 95 - 41) = v_rdi;
    if (*(unsigned __int64 *)(v_rip + 11280081) == 0) goto loc_0036BE04;
    v_r15 = *(unsigned __int64 *)(v_rdi + 16);
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rdi + 16))) & (16)) == 0) {
        a1 = ~(*(unsigned __int64 *)(v_rip + 11280081));
        v_r15 = (*(unsigned __int64 *)(v_rdi + 16)) & (a1);
    }
    goto loc_0036B71A;
loc_0036BE0D:
    result = (result) & (-17);
    goto loc_0036BDC5;
loc_0036BE13:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 95 - 41) + 34)) & (32)) == 0) goto loc_0036BE2E;
    if (!sign_flag) goto loc_0036B8C1;
loc_0036BE2E:
    result = MiUnlockProtoPoolPage(*(unsigned __int64 *)(v_rsp - 95 + 119), 17, (unsigned int)(*(unsigned int *)(v_r15 + 44)), a4);
    result = MiFreeInPageSupportBlock(*(unsigned __int64 *)(v_rsp - 95 - 81), 17, (unsigned int)(*(unsigned int *)(v_r15 + 44)), a4);
loc_0036BE46:
    if (result + (unsigned int)(*(unsigned int *)(v_r15 + 44)) * 8 != 0) goto loc_0036BF71;
loc_0036BE4F:
    goto loc_0036BAFD;
loc_0036BE56:
    *(unsigned int *)(v_rsp - 95 - 117) = 1;
    goto loc_0036B84B;
loc_0036BE62:
    *(unsigned int *)(v_rsp - 95 - 117) = (unsigned int)(a4);
    if (((unsigned int)(a4)) <= 16) goto loc_0036B84B;
    goto loc_0036B847;
loc_0036BE75:
    if (((*(unsigned int *)((unsigned int)(0xFFFULL) + 56)) & (0x8000000ULL)) == 0) goto loc_0036B74F;
    result = MiGetSessionIdForVa(*(unsigned __int64 *)(v_rsp - 95 - 97), 17, (unsigned int)(*(unsigned int *)(v_r15 + 44)), a4);
    *(unsigned int *)(v_rsp - 95 - 109) = (unsigned int)(result);
    if ((*(unsigned __int64 *)(v_rsp - 95 - 97)) < result) goto loc_0036BECB;
    if ((unsigned int)(*(unsigned int *)(v_r15 + 44)) == 0) goto loc_0036BFBE;
    if ((*(unsigned __int8 *)(17)) == 1) goto loc_0036BFD5;
    if ((*(unsigned __int8 *)(17)) == 3) goto loc_0036BFD5;
    result = (*(unsigned __int64 *)(v_rsp - 95 - 73)) & (-2);
    if ((*(unsigned __int8 *)(result)) == 6) goto loc_0036BFD5;
loc_0036BECB:
    result = MiGetSharedProtos(*(unsigned __int64 *)(v_rsp - 95 - 57), (unsigned int)(*(unsigned int *)(v_rsp - 95 - 109)), v_r15, a4);
    *(unsigned __int64 *)(v_rsp - 95 - 25) = result;
    *(unsigned __int64 *)(v_rsp - 95 - 49) = *(unsigned __int64 *)(result + 72);
    goto loc_0036B752;
loc_0036BEFA:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 56)))) & (4)) == 0) goto loc_0036B6EA;
    goto loc_0036BB3E;
loc_0036BF0F:
    result = -(result);
    v_r14 = (unsigned int)((*(unsigned __int64 *)(v_rsp - 95 - 81)) + (2));
    *(unsigned int *)(v_rsp - 95 - 113) = (unsigned int)(v_r14);
    a4 = (result == 0) ? 1 : 0;
    goto loc_0036B7A4;
loc_0036BF32:
    if ((*(unsigned __int64 *)(v_rsp - 95 - 97)) > result) goto loc_0036BBCA;
    result = MiLockVadTree(1, result, v_r15, a4);
    result = MiLocateAddress(*(unsigned __int64 *)(v_rsp - 95 - 97), result, v_r15, a4);
    *(unsigned __int64 *)(v_rsp - 95 - 81) = result;
    result = MiUnlockVadTree(1, 17, v_r15, a4);
    goto loc_0036BBCA;
loc_0036BF71:
    a1 = (((unsigned int)((unsigned int)(0xC0000434ULL))) == 0xC000009AULL) ? 1 : 0;
    a1 = (unsigned __int8)((a1) + 1);
    *(unsigned __int8 *)(result + (unsigned int)(*(unsigned int *)(v_r15 + 44)) * 8 + 1) = (unsigned __int8)(a1);
    goto loc_0036BE4F;
loc_0036BF85:
    if (((unsigned int)(result)) != 0xC0033333ULL) goto loc_0036BB21;
    goto loc_0036BB21;
loc_0036BFA3:
    goto loc_0036B83A;
loc_0036BFAC:
    result = MiFreeInPageSupportBlock(result, 17, v_r15, (unsigned int)(*(unsigned int *)(v_rsp - 95 - 121)));
loc_0036BFB4:
    goto loc_0036BE46;
loc_0036BFBE:
    a2 = 0;
    result = KeInvalidAccessAllowed(*(unsigned __int64 *)(v_rsp - 95 - 73), a2, v_r15, (unsigned int)(*(unsigned int *)(v_rsp - 95 - 121)));
    if ((unsigned __int8)(result) == 0) goto loc_0036BECB;
loc_0036BFD5:
    if ((((unsigned __int8)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL) + 16))) & (1)) == 0) goto loc_0036BFEA;
    result = (*(unsigned __int64 *)((unsigned int)(0xC000009AULL) + 16)) & (-2);
    if ((*(unsigned __int8 *)(result)) == 6) goto loc_0036BECB;
loc_0036BFEA:
    goto loc_0036BB3E;
loc_0036BFF4:
    if ((((unsigned __int8)((unsigned int)(0xC0000016ULL))) & (1)) == 0) goto loc_0036B89D;
    v_r12 = (unsigned int)(((unsigned int)(0xC0000016ULL)) & (0xFFFFFFFEULL));
    *(unsigned int *)(v_rsp - 95 - 117) = 16;
    result = MiGetInPageSupportBlock((unsigned int)((unsigned int)(v_r12)), *(unsigned __int64 *)(v_rsp - 95 - 65), v_r15, (unsigned int)(*(unsigned int *)(v_rsp - 95 - 121)));
    if (result != 0) goto loc_0036B885;
    goto loc_0036BFB4;
loc_0036C023:
    goto loc_0036BB21;
}
```

## 5. (Beta) C Style

```c
int64_t MiResolveMappedFileFault(void *Arg1, void *Arg2, int64_t Arg3, void *Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint64_t v_stack_p30;

    *(void **)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(void **)(local_rsp + 0x10) = Arg2;
    *(void **)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (232);
    local_rsi = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x61) = *(uint64_t *)(arg1);
    *(uint64_t *)(local_rsp - 0x5F - 0x21) = *(uint64_t *)(arg1 + 0x38);
    *(uint64_t *)(local_rsp - 0x5F - 0x9) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x11) = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x79) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x1) = v_xmm0;
    *(uint32_t *)(local_rsp - 0x5F - 0x59) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x49) = *(uint64_t *)(arg1 + 0x10);
    *(uint64_t *)(arg4) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x41) = 0;
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A8)) & (4)) != 0) goto loc_0036BB6A;
    Arg3 = (uint32_t)((*(uint64_t *)(arg1 + 0x10)) & (1));
    *(uint32_t *)(local_rsp - 0x5F - 0x75) = 256;
    Arg2 = (*(uint64_t *)(arg1 + 0x10)) & (-2);
    if (Arg3 != 0) goto loc_0036BBE7;
loc_0036B6EA:
    if (condition_is_above_or_equal) goto loc_0036BDA8;
    if (*(uint64_t *)(v_rip + 0xAC2584) == 0) goto loc_0036B716;
    if ((((uint8_t)(*(uint64_t *)(arg2))) & (16)) != 0) goto loc_0036BB12;
    local_r15 = ~(*(uint64_t *)(v_rip + 0xAC2584));
    local_r15 = (local_r15) & (*(uint64_t *)(arg2));
loc_0036B716:
    *(uint64_t *)(local_rsp - 0x5F - 0x29) = 0;
loc_0036B71A:
    local_r15 = (local_r15) >> (16);
    *(uint64_t *)(local_rsp - 0x5F - 0x39) = *(uint64_t *)(local_r15);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r15) + 0x38)))) & (16)) != 0) goto loc_0036BB39;
    *(uint64_t *)(local_rsp - 0x5F - 0x31) = *(uint64_t *)(local_r15 + 0x8);
    *(uint64_t *)(local_rsp - 0x5F - 0x19) = 0;
    if (condition_is_below) goto loc_0036BE75;
loc_0036B74F:
loc_0036B752:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r15 + 0x34))) & (0x3FFFFFFFULL));
    result = (result) * (result);
    result = (result) + (*(uint64_t *)(local_rsp - 0x5F - 0x31));
    if (Arg2 >= (result + (uint32_t)(*(uint32_t *)(local_r15 + 0x2C)) * 8)) goto loc_0036BFEA;
    Arg1 = (uint32_t)((*(uint16_t *)(*(uint64_t *)(local_r15) + 0x3C)) & (0x3FFULL));
    *(uint32_t *)(local_rsp - 0x5F - 0x71) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x69) = *(uint64_t *)(*(uint64_t *)(v_rip + 0xAC4906) + arg1 * 8);
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(local_r15) + 0x3E)) & (12));
    if (((uint8_t)(result)) == 4) goto loc_0036BF0F;
loc_0036B7A4:
    if (0 == 2) goto loc_0036B83A;
    *(uint64_t *)(local_rsp - 0x5F - 0x51) = 0;
    result = MiComputeFaultNode(*(uint64_t *)(local_rsp - 0x5F + 0x67), *(uint64_t *)(local_r15), local_rsp - 95 - 81, 0);
    *(uint32_t *)(local_rsp - 0x5F - 0x79) = 0;
    if (0 == 1) goto loc_0036BE56;
    if (0 != 0) goto loc_0036BBBD;
    if (condition_is_above_or_equal) goto loc_0036B83A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x39) + 0x38)))) & (32)) != 0) goto loc_0036B83A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x21) + 0xB8)))) & (15)) != 0) goto loc_0036B83A;
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x21) + 0xB8));
    local_r14 = *(uint64_t *)(local_rsp - 0x5F - 0x51);
    if (*(uint64_t *)(local_rsp - 0x5F - 0x51) == 0) {
        Arg1 = 0 + 1;
        result = MiLockVadTree(Arg1, *(uint64_t *)(local_r15), local_rsp - 95 - 81, 0);
        Arg1 = *(uint64_t *)(local_rsp - 0x5F - 0x61);
        result = MiLocateAddress(Arg1, *(uint64_t *)(local_r15), local_rsp - 95 - 81, 0);
        Arg2 = 17;
        *(uint64_t *)(local_rsp - 0x5F - 0x51) = result;
        Arg1 = 0 + 1;
        local_r14 = result;
        result = MiUnlockVadTree(Arg1, Arg2, local_rsp - 95 - 81, 0);
        Arg4 = 0;
    }
    if (!sign_flag) goto loc_0036BCEF;
loc_0036B83A:
    if (((uint32_t)(Arg4)) <= 256) goto loc_0036BE62;
loc_0036B847:
    local_r12 = (uint32_t)((local_rsi + 2) | (1));
loc_0036B84B:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) | (4));
    result = MiGetInPageSupportBlock(Arg1, *(uint64_t *)(local_rsp - 0x5F - 0x41), local_rsp - 95 - 81, Arg4);
    if (result != 0) goto loc_0036B8A6;
    result = MiUnlockProtoPoolPage(*(uint64_t *)(local_rsp - 0x5F + 0x77), 17, local_rsp - 95 - 81, Arg4);
    result = MiGetInPageSupportBlock((uint32_t)((uint32_t)(local_r12)), *(uint64_t *)(local_rsp - 0x5F - 0x41), local_rsp - 95 - 81, Arg4);
    if (result == 0) goto loc_0036BFF4;
loc_0036B885:
    Arg2 = 0;
    result = MiLockProtoPoolPage(*(uint64_t *)(local_rsp - 0x5F + 0x6F), Arg2, local_rsp - 95 - 81, Arg4);
    *(uint64_t *)(local_rsp - 0x5F + 0x77) = result;
    if (result == 0) goto loc_0036BFAC;
loc_0036B89D:
    if (result == 0) goto loc_0036BFB4;
loc_0036B8A6:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x6F))) != (*(uint64_t *)(arg2))) goto loc_0036BE2E;
    if ((*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x6F))) >= (*(uint64_t *)(arg2))) goto loc_0036BE13;
loc_0036B8C1:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x71)))) == 2) goto loc_0036BC45;
    if (0 != 0) goto loc_0036BCD4;
loc_0036B8D8:
    Arg3 = (*(uint64_t *)(arg2)) >> (5);
    Arg1 = 0;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r15 + 0x20))) >> (1));
    Arg3 = (uint32_t)((Arg3) & (31));
    Arg2 = (uint32_t)((Arg2) & (31));
    result = MiSanitizePfnProtection(Arg1, Arg2, Arg3, Arg4);
    *(uint32_t *)(local_rsp - 0x5F - 0x79) = (uint32_t)(result);
    result = MiInitializePageColorBase(*(uint64_t *)(local_rsp - 0x5F - 0x21), Arg1 + 3, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), local_rsp - 95 - 1);
    local_rdi = ((uint32_t)((uint32_t)(result))) | (-1);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x71)))) == ((uint32_t)(local_rdi + 2))) goto loc_0036B957;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x39) + 0x38))) & (0x40020ULL));
    Arg1 = (((uint32_t)(Arg1)) == 32) ? 1 : 0;
    result = (((*(uint8_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x39) + 0x3E)) & (12)) == 0) ? 1 : 0;
    Arg1 = (uint8_t)((Arg1) & ((uint8_t)(result)));
    result = (condition_is_below) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_0036BA2E;
    if ((*(uint32_t *)(v_rip + 0xACBA50)) != 0) goto loc_0036BA2E;
    if (0 != 0) goto loc_0036BCA3;
loc_0036B957:
loc_0036B95B:
    result = MiObtainFaultCharges(*(uint64_t *)(local_rsp - 0x5F - 0x69), local_rdi + 2, (uint32_t)((uint32_t)(local_rdi + 2)), local_rdi + 2);
    if (result == 0) goto loc_0036BB5E;
    Arg2 = 0;
    Arg1 = (*(uint64_t *)(local_rsp - 0x5F + 0x7)) >> (16);
    Arg1 = (uint32_t)((Arg1) & (3));
    Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)(*(uint64_t *)(local_rsp - 0x5F + 0x7))));
    local_rdi = (uint32_t)(((uint8_t)(Arg2)) ^ ((uint32_t)(*(uint64_t *)(local_rsp - 0x5F + 0x7))));
    Arg4 = (uint32_t)((*(uint64_t *)(local_rsp - 0x5F + 0x7)) >> (9));
    Arg4 = (uint32_t)((Arg4) & (63));
    if (condition_is_above_or_equal) goto loc_0036B9D1;
    v_stack_m108 = local_rsp - 95 - 89;
    result = MiUseSlabAllocator(*(uint64_t *)(local_rsp - 0x5F - 0x69), local_r15, *(uint64_t *)(arg2), Arg4);
    if ((uint32_t)(result) != 0) goto loc_0036BB71;
loc_0036B9D1:
    result = MiGetPage(*(uint64_t *)(local_rsp - 0x5F - 0x69), (uint32_t)((uint32_t)(local_rdi)), 1, Arg4);
loc_0036B9E1:
    if (result == -1) goto loc_0036BB4C;
    if ((*(uint32_t *)(local_rsp - 0x5F - 0x71)) == 1) goto loc_0036BC06;
    *(uint64_t *)(result + 0xE0) = *(uint64_t *)(local_rsp - 0x5F - 0x61);
    v_stack_m100 = *(uint64_t *)(local_rsp - 0x5F + 0x77);
    v_stack_m108 = result;
    result = MiCopyDataPageToImagePage(result, local_r15, *(uint64_t *)(local_rsp - 0x5F + 0x6F), *(uint64_t *)(local_rsp - 0x5F - 0x49));
    if ((uint32_t)(result) != 0) goto loc_0036BAF1;
    goto loc_0036BA32;
loc_0036BA2E:
loc_0036BA32:
    *(uint64_t *)(result + 0xA0) = *(uint64_t *)(local_rsp - 0x5F + 0x77);
    *(uint64_t *)(result + 0xE8) = *(uint64_t *)(local_rsp - 0x5F + 0x6F);
    *(uint32_t *)(result + 0xB8) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x75)));
    v_stack_mF8 = local_rsp - 95 - 17;
    v_stack_m100 = local_rsp - 95 - 9;
    v_stack_m108 = result;
    *(uint64_t *)(result + 0xA8) = *(uint64_t *)(arg2);
    *(uint64_t *)(result + 0xD0) = local_r15;
    result = MiPickClusterForMappedFileFault(*(uint64_t *)(local_rsp - 0x5F - 0x69), result, 0, *(uint64_t *)(local_rsp - 0x5F - 0x31));
    v_stack_mE0 = local_rsp - 95 - 1;
    v_stack_mE8 = *(uint64_t *)(local_rsp - 0x5F + 0x67);
    v_stack_mF0 = 0;
    v_stack_mF8 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x79)));
    v_stack_m100 = result;
    v_stack_m108 = result;
    result = MiBuildMdlForMappedFileFault(result, *(uint64_t *)(local_rsp - 0x5F - 0x9), *(uint64_t *)(local_rsp - 0x5F - 0x11), *(uint64_t *)(local_rsp - 0x5F - 0x69));
    if (((uint32_t)((uint32_t)(result))) != result) goto loc_0036BB9C;
loc_0036BAD2:
    if ((uint32_t)((uint32_t)(result)) == 0) goto loc_0036BB1B;
    v_stack_m108 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x6D)));
    result = MiFinishMdlForMappedFileFault(result, *(uint64_t *)(local_rsp - 0x5F - 0x49), (uint32_t)((uint32_t)(result)), *(uint64_t *)(local_rsp - 0x5F - 0x29));
loc_0036BAF1:
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x7F)) = result;
loc_0036BAFD:
    local_rsp = (local_rsp) + (232);
    return (uint32_t)(0xC0033333ULL);
loc_0036BB12:
    local_r15 = (local_r15) & (-17);
    goto loc_0036B716;
loc_0036BB1B:
loc_0036BB21:
    result = MiUnlockProtoPoolPage(*(uint64_t *)(local_rsp - 0x5F + 0x77), 17, (uint32_t)((uint32_t)(result)), *(uint64_t *)(local_rsp - 0x5F - 0x29));
    result = MiFreeInPageSupportBlock(result, 17, (uint32_t)((uint32_t)(result)), *(uint64_t *)(local_rsp - 0x5F - 0x29));
    goto loc_0036BAFD;
loc_0036BB39:
loc_0036BB3E:
    result = MiUnlockProtoPoolPage(Arg3, 17, (uint32_t)((uint32_t)(result)), *(uint64_t *)(local_rsp - 0x5F - 0x29));
    goto loc_0036BAFD;
loc_0036BB4C:
    result = MiReturnFaultCharges((uint32_t)(0xC0000017ULL), 1, 1, *(uint64_t *)(local_rsp - 0x5F - 0x29));
loc_0036BB5E:
    if ((*(uint32_t *)(local_rsp - 0x5F - 0x71)) != 1) goto loc_0036BA32;
    goto loc_0036BB1B;
loc_0036BB6A:
    goto loc_0036BB3E;
loc_0036BB71:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x59)))) > 4) goto loc_0036B9D1;
    v_stack_p28 = (uint32_t)((uint32_t)(0xC00000A1ULL));
    v_stack_p20 = (uint32_t)(0xC00000A1ULL);
    result = MiGetSlabPage((uint32_t)(0xC0000017ULL), (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x59)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), 16);
    goto loc_0036B9E1;
loc_0036BB9C:
    local_rbx = (result) - ((uint32_t)((uint32_t)(result)));
    result = MiReturnResident((uint32_t)(0xC0000017ULL), local_rbx, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), 16);
    Arg3 = 0;
    result = MiReturnCommit((uint32_t)(0xC0000017ULL), local_rbx, Arg3, 16);
    goto loc_0036BAD2;
loc_0036BBBD:
    if (*(uint64_t *)(local_rsp - 0x5F - 0x51) == 0) goto loc_0036BF32;
loc_0036BBCA:
    result = MiComputeFaultCluster(*(uint64_t *)(local_rsp - 0x5F - 0x69), 0, *(uint64_t *)(local_rsp - 0x5F - 0x51), 2);
    goto loc_0036B83A;
loc_0036BBE7:
    if ((*(uint8_t *)(0)) == 5) goto loc_0036BEFA;
    if (((uint8_t)(*(uint8_t *)(0))) == 1) goto loc_0036BD8C;
    local_r13 = 0;
    if (((uint8_t)(*(uint8_t *)(0))) == ((uint8_t)((uint32_t)(0xC0000017ULL)))) { local_r13 = 0; }
    goto loc_0036B6EA;
loc_0036BC06:
    v_stack_p30 = *(uint64_t *)(local_rsp - 0x5F - 0x19);
    v_stack_p28 = *(uint64_t *)(local_rsp - 0x5F + 0x77);
    v_stack_p20 = (uint32_t)((uint32_t)(result));
    result = MiCopyFileOnlyGlobalSubsectionPage(*(uint64_t *)(local_rsp - 0x5F - 0x69), 0, *(uint64_t *)(local_rsp - 0x5F - 0x51), (uint32_t)((uint32_t)(result)));
    if (!sign_flag) goto loc_0036BAF1;
    if (((uint32_t)(result)) == 0xC0000055ULL) goto loc_0036C023;
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0xC0000434ULL)))) goto loc_0036BF85;
loc_0036BC45:
    result = MiUnlockProtoPoolPage(*(uint64_t *)(local_rsp - 0x5F + 0x77), 17, *(uint64_t *)(local_rsp - 0x5F - 0x51), (uint32_t)((uint32_t)(result)));
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x51) + 0xE8) = *(uint64_t *)(local_rsp - 0x5F + 0x6F);
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x51) + 0x138) = (uint32_t)((uint32_t)(0xC00000A1ULL));
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x51) + 0xD0) = local_r15;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x51) + 0xB8) = (uint32_t)((uint32_t)(0xC00000A1ULL));
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x51) + 0xA8) = local_rbx;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x51) + 0xA0) = (uint32_t)(0xC00000A1ULL);
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x51) + 0x100) = (uint32_t)(0xC00000A1ULL);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x51) + 0xC0))) | (1));
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x51) + 0xC0) = (uint32_t)(result);
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x51) + 0x50) = (uint32_t)((uint32_t)(0xC00000A1ULL));
    goto loc_0036BAF1;
loc_0036BCA3:
    if ((*(uint8_t *)(local_r13)) != ((uint8_t)((uint32_t)((uint32_t)(result))))) goto loc_0036B95B;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r13 + 0x50))) >> (3));
    Arg2 = (uint32_t)((Arg2) & (7));
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)((uint32_t)((uint32_t)(result)))));
    result = MiGetAvailablePagesBelowPriority(*(uint64_t *)(local_rsp - 0x5F - 0x69), Arg2, *(uint64_t *)(local_rsp - 0x5F - 0x51), (uint32_t)((uint32_t)(result)));
    if (result == 0) goto loc_0036BA32;
    goto loc_0036B95B;
loc_0036BCD4:
    if ((*(uint8_t *)(local_r13)) != 1) goto loc_0036B8D8;
    result = MiSetInPagePrefetchPriority(local_r13, *(uint64_t *)(local_rsp - 0x5F - 0x51), *(uint64_t *)(local_rsp - 0x5F - 0x51), (uint32_t)((uint32_t)(result)));
    goto loc_0036B8D8;
loc_0036BCEF:
    result = (local_r13) & ((uint32_t)(0xFFFULL));
    if (result < 17) goto loc_0036B83A;
    Arg2 = (local_r13) >> (12);
    Arg2 = (Arg2) & (result);
    result = (local_r13) & ((uint32_t)(0xFFFULL));
    result = (result) - 1;
    Arg2 = (Arg2) + (result);
    result = (*(uint64_t *)(local_rsp - 0x5F - 0x61)) & (0xFFFFFFFFFFFFF000ULL);
    Arg2 = (Arg2) << (12);
    if (result != Arg2) goto loc_0036B83A;
    Arg4 = (*(uint64_t *)(local_rsp - 0x5F + 0x6F)) + (8);
    if ((((uint32_t)((uint32_t)(0xFFFULL))) & ((uint32_t)(Arg4))) == 0) goto loc_0036BFA3;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r15 + 0x34))) & (0x3FFFFFFFULL));
    Arg2 = (Arg2) * (result);
    result = (*(uint64_t *)(local_rsp - 0x5F - 0x31)) + (Arg2);
    if (Arg4 >= (result + (uint32_t)(*(uint32_t *)(local_r15 + 0x2C)) * 8)) goto loc_0036BFA3;
    if ((*(uint64_t *)(arg4)) != local_rbx) goto loc_0036BFA3;
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)(local_r13))) & ((uint32_t)((uint32_t)(0xFFFULL))));
    Arg4 = (uint32_t)((Arg4) - 1);
    goto loc_0036B83A;
loc_0036BD8C:
    if (((*(uint32_t *)(result + (uint32_t)(*(uint32_t *)(local_r15 + 0x2C)) * 8 + 0x50)) & ((uint32_t)(local_r13))) != 0) goto loc_0036BB3E;
    *(uint64_t *)(local_rsp - 0x5F - 0x41) = *(uint64_t *)(result + (uint32_t)(*(uint32_t *)(local_r15 + 0x2C)) * 8 + 0x70);
    goto loc_0036B6EA;
loc_0036BDA8:
    if (*(uint64_t *)(v_rip + 0xAC1ED1) == 0) goto loc_0036BDC5;
    if ((((uint8_t)(local_rbx)) & (16)) != 0) goto loc_0036BE0D;
    result = ~(*(uint64_t *)(v_rip + 0xAC1ED1));
    result = (result) & (local_rbx);
loc_0036BDC5:
    result = (result) >> (12);
    result = (result) & ((uint32_t)(0xFFFULL));
    local_rdi = (result + result * 2) << (4);
    local_rdi = (local_rdi) + (result);
    *(uint64_t *)(local_rsp - 0x5F - 0x29) = local_rdi;
    if (*(uint64_t *)(v_rip + 0xAC1ED1) == 0) goto loc_0036BE04;
    local_r15 = *(uint64_t *)(local_rdi + 0x10);
    if ((((uint8_t)(*(uint64_t *)(local_rdi + 0x10))) & (16)) == 0) {
        Arg1 = ~(*(uint64_t *)(v_rip + 0xAC1ED1));
        local_r15 = (*(uint64_t *)(local_rdi + 0x10)) & (Arg1);
    }
    goto loc_0036B71A;
loc_0036BE0D:
    result = (result) & (-17);
    goto loc_0036BDC5;
loc_0036BE13:
    if (((*(uint8_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x29) + 0x22)) & (32)) == 0) goto loc_0036BE2E;
    if (!sign_flag) goto loc_0036B8C1;
loc_0036BE2E:
    result = MiUnlockProtoPoolPage(*(uint64_t *)(local_rsp - 0x5F + 0x77), 17, (uint32_t)(*(uint32_t *)(local_r15 + 0x2C)), Arg4);
    result = MiFreeInPageSupportBlock(*(uint64_t *)(local_rsp - 0x5F - 0x51), 17, (uint32_t)(*(uint32_t *)(local_r15 + 0x2C)), Arg4);
loc_0036BE46:
    if (result + (uint32_t)(*(uint32_t *)(local_r15 + 0x2C)) * 8 != 0) goto loc_0036BF71;
loc_0036BE4F:
    goto loc_0036BAFD;
loc_0036BE56:
    *(uint32_t *)(local_rsp - 0x5F - 0x75) = 1;
    goto loc_0036B84B;
loc_0036BE62:
    *(uint32_t *)(local_rsp - 0x5F - 0x75) = (uint32_t)(Arg4);
    if (((uint32_t)(Arg4)) <= 16) goto loc_0036B84B;
    goto loc_0036B847;
loc_0036BE75:
    if (((*(uint32_t *)((uint32_t)(0xFFFULL) + 0x38)) & (0x8000000ULL)) == 0) goto loc_0036B74F;
    result = MiGetSessionIdForVa(*(uint64_t *)(local_rsp - 0x5F - 0x61), 17, (uint32_t)(*(uint32_t *)(local_r15 + 0x2C)), Arg4);
    *(uint32_t *)(local_rsp - 0x5F - 0x6D) = (uint32_t)(result);
    if ((*(uint64_t *)(local_rsp - 0x5F - 0x61)) < result) goto loc_0036BECB;
    if ((uint32_t)(*(uint32_t *)(local_r15 + 0x2C)) == 0) goto loc_0036BFBE;
    if ((*(uint8_t *)(17)) == 1) goto loc_0036BFD5;
    if ((*(uint8_t *)(17)) == 3) goto loc_0036BFD5;
    result = (*(uint64_t *)(local_rsp - 0x5F - 0x49)) & (-2);
    if ((*(uint8_t *)(result)) == 6) goto loc_0036BFD5;
loc_0036BECB:
    result = MiGetSharedProtos(*(uint64_t *)(local_rsp - 0x5F - 0x39), (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x6D)), local_r15, Arg4);
    *(uint64_t *)(local_rsp - 0x5F - 0x19) = result;
    *(uint64_t *)(local_rsp - 0x5F - 0x31) = *(uint64_t *)(result + 0x48);
    goto loc_0036B752;
loc_0036BEFA:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x38)))) & (4)) == 0) goto loc_0036B6EA;
    goto loc_0036BB3E;
loc_0036BF0F:
    result = -(result);
    local_r14 = (uint32_t)((*(uint64_t *)(local_rsp - 0x5F - 0x51)) + (2));
    *(uint32_t *)(local_rsp - 0x5F - 0x71) = (uint32_t)(local_r14);
    Arg4 = (result == 0) ? 1 : 0;
    goto loc_0036B7A4;
loc_0036BF32:
    if ((*(uint64_t *)(local_rsp - 0x5F - 0x61)) > result) goto loc_0036BBCA;
    result = MiLockVadTree(1, result, local_r15, Arg4);
    result = MiLocateAddress(*(uint64_t *)(local_rsp - 0x5F - 0x61), result, local_r15, Arg4);
    *(uint64_t *)(local_rsp - 0x5F - 0x51) = result;
    result = MiUnlockVadTree(1, 17, local_r15, Arg4);
    goto loc_0036BBCA;
loc_0036BF71:
    Arg1 = (((uint32_t)((uint32_t)(0xC0000434ULL))) == 0xC000009AULL) ? 1 : 0;
    Arg1 = (uint8_t)((Arg1) + 1);
    *(uint8_t *)(result + (uint32_t)(*(uint32_t *)(local_r15 + 0x2C)) * 8 + 0x1) = (uint8_t)(Arg1);
    goto loc_0036BE4F;
loc_0036BF85:
    if (((uint32_t)(result)) != 0xC0033333ULL) goto loc_0036BB21;
    goto loc_0036BB21;
loc_0036BFA3:
    goto loc_0036B83A;
loc_0036BFAC:
    result = MiFreeInPageSupportBlock(result, 17, local_r15, (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x79)));
loc_0036BFB4:
    goto loc_0036BE46;
loc_0036BFBE:
    Arg2 = 0;
    result = KeInvalidAccessAllowed(*(uint64_t *)(local_rsp - 0x5F - 0x49), Arg2, local_r15, (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x79)));
    if ((uint8_t)(result) == 0) goto loc_0036BECB;
loc_0036BFD5:
    if ((((uint8_t)(*(uint64_t *)((uint32_t)(0xC000009AULL) + 0x10))) & (1)) == 0) goto loc_0036BFEA;
    result = (*(uint64_t *)((uint32_t)(0xC000009AULL) + 0x10)) & (-2);
    if ((*(uint8_t *)(result)) == 6) goto loc_0036BECB;
loc_0036BFEA:
    goto loc_0036BB3E;
loc_0036BFF4:
    if ((((uint8_t)((uint32_t)(0xC0000016ULL))) & (1)) == 0) goto loc_0036B89D;
    local_r12 = (uint32_t)(((uint32_t)(0xC0000016ULL)) & (0xFFFFFFFEULL));
    *(uint32_t *)(local_rsp - 0x5F - 0x75) = 16;
    result = MiGetInPageSupportBlock((uint32_t)((uint32_t)(local_r12)), *(uint64_t *)(local_rsp - 0x5F - 0x41), local_r15, (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x79)));
    if (result != 0) goto loc_0036B885;
    goto loc_0036BFB4;
loc_0036C023:
    goto loc_0036BB21;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg4` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0036B640&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
