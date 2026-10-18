# MiMakePageAvoidRead

- RVA: `0x002B7DE0`–`0x002B8529` (길이 `1,865` bytes)
- VA: `0x00000001402B7DE0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006DB6C`
- 디코드: `396`개 명령, `1,865/1,865` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **31**; 고유 호출 대상: **27**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **9**

### Outgoing calls
- `0x002B7F05` → [MiAssignDefaultChannel](../31/MiAssignDefaultChannel_function_0031E5B0.md) (function, `0x0031E5B0`)
- `0x002B7F47` → [MiProtectionToCacheAttribute](MiProtectionToCacheAttribute_function_002B8530.md) (function, `0x002B8530`)
- `0x002B7F90` → [MiGetPage](../28/MiGetPage_function_002884C0.md) (function, `0x002884C0`)
- `0x002B8005` → [MiChangePageAttribute](../33/MiChangePageAttribute_function_00332ECC.md) (function, `0x00332ECC`)
- `0x002B8049` → [MiReservePtes](../31/MiReservePtes_function_00318D20.md) (function, `0x00318D20`)
- `0x002B8064` → [MiMapFrame](../2C/MiMapFrame_function_002C7190.md) (function, `0x002C7190`)
- `0x002B80A5` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x002B810A` → [MiReleasePtes](../24/MiReleasePtes_function_00247240.md) (function, `0x00247240`)
- `0x002B8135` → [MiLockProtoPoolPage](MiLockProtoPoolPage_function_002B8B80.md) (function, `0x002B8B80`)
- `0x002B819E` → [MiInitializePfn](../33/MiInitializePfn_function_00331E60.md) (function, `0x00331E60`)
- `0x002B81BF` → [MiReferenceControlAreaPfn](../36/MiReferenceControlAreaPfn_function_00364084.md) (function, `0x00364084`)
- `0x002B81D2` → [MiMakeValidPte](../2C/MiMakeValidPte_function_002C5590.md) (function, `0x002C5590`)
- `0x002B823E` → [MiDecrementShareCountEx](../33/MiDecrementShareCountEx_function_00333F70.md) (function, `0x00333F70`)
- `0x002B825E` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x002B828A` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x002B82A5` → [MiLockAndInsertPageInFreeList](../47/MiLockAndInsertPageInFreeList_function_00470FA8.md) (function, `0x00470FA8`)
- `0x002B8319` → [MiGetPfnPriority](../32/MiGetPfnPriority_function_003226F0.md) (function, `0x003226F0`)
- `0x002B8352` → [MiPfnZeroingNeeded](../29/MiPfnZeroingNeeded_function_0029FA80.md) (function, `0x0029FA80`)
- `0x002B838B` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x002B83C3` → [MiCheckLinearProtectedPteAccessedBit](../29/MiCheckLinearProtectedPteAccessedBit_function_00292D80.md) (function, `0x00292D80`)
- `0x002B83F6` → [MiCheckLinearProtectedPteAccessedBit](../29/MiCheckLinearProtectedPteAccessedBit_function_00292D80.md) (function, `0x00292D80`)
- `0x002B840E` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002B841E` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002B842D` → [MiWaitForFreePage](../2A/MiWaitForFreePage_function_002A3324.md) (function, `0x002A3324`)
- `0x002B843A` → [MiReleaseFreshPage](../33/MiReleaseFreshPage_function_00334AE0.md) (function, `0x00334AE0`)
- `0x002B846F` → [MiZeroPhysicalPage](../33/MiZeroPhysicalPage_function_00332590.md) (function, `0x00332590`)
- `0x002B847B` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x002B848D` → [MiLockAndInsertPageInFreeList](../47/MiLockAndInsertPageInFreeList_function_00470FA8.md) (function, `0x00470FA8`)
- `0x002B84B3` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x002B84CA` → [MiIdentifyPfn](../31/MiIdentifyPfn_function_0031CAC0.md) (function, `0x0031CAC0`)
- `0x002B851F` → [EtwTraceKernelEvent](../23/EtwTraceKernelEvent_function_00235350.md) (function, `0x00235350`)

### Direct callers
- [MmCopyToCachedPage](../34/MmCopyToCachedPage_function_00347B44.md) at `0x00347D01`

### Static image references
- `0x002B7DF2` → RVA `0x00E0A740` (`.data`; read)
- `0x002B7E6F` → RVA `0x00E2DC80` (`.data`; read)
- `0x002B7EBB` → RVA `0x00E30088` (`.data`; read)
- `0x002B7ECF` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x002B8042` → RVA `0x00E37668` (`.data`; read)
- `0x002B8118` → RVA `0x00FC6B04` (`ALMOSTRO`; read)
- `0x002B81F1` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x002B82D7` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x002B8400` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002B7DE0  40 53                           push rbx
002B7DE2  56                              push rsi
002B7DE3  41 54                           push r12
002B7DE5  41 55                           push r13
002B7DE7  41 56                           push r14
002B7DE9  41 57                           push r15
002B7DEB  48 81 EC 48 01 00 00            sub rsp, 0x148
002B7DF2  48 8B 05 47 29 B5 00            mov rax, qword ptr [rip + 0xb52947]
002B7DF9  48 33 C4                        xor rax, rsp
002B7DFC  48 89 84 24 30 01 00 00         mov qword ptr [rsp + 0x130], rax
002B7E04  4C 89 4C 24 60                  mov qword ptr [rsp + 0x60], r9
002B7E09  44 89 44 24 58                  mov dword ptr [rsp + 0x58], r8d
002B7E0E  48 89 94 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rdx
002B7E16  48 89 8C 24 80 00 00 00         mov qword ptr [rsp + 0x80], rcx
002B7E1E  48 89 8C 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rcx
002B7E26  48 8B 84 24 A8 01 00 00         mov rax, qword ptr [rsp + 0x1a8]
002B7E2E  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
002B7E33  48 8B 8C 24 B0 01 00 00         mov rcx, qword ptr [rsp + 0x1b0]
002B7E3B  48 89 8C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rcx
002B7E43  C6 44 24 30 00                  mov byte ptr [rsp + 0x30], 0
002B7E48  0F 57 C0                        xorps xmm0, xmm0
002B7E4B  0F 11 84 24 D8 00 00 00         movups xmmword ptr [rsp + 0xd8], xmm0
002B7E53  0F 57 C9                        xorps xmm1, xmm1
002B7E56  0F 11 8C 24 E8 00 00 00         movups xmmword ptr [rsp + 0xe8], xmm1
002B7E5E  0F 11 8C 24 F8 00 00 00         movups xmmword ptr [rsp + 0xf8], xmm1
002B7E66  83 21 00                        and dword ptr [rcx], 0
002B7E69  48 8B 18                        mov rbx, qword ptr [rax]
002B7E6C  4C 8B F3                        mov r14, rbx
002B7E6F  48 8B 05 0A 5E B7 00            mov rax, qword ptr [rip + 0xb75e0a]
002B7E76  48 85 C0                        test rax, rax
002B7E79  74 12                           je 0x1402b7e8d
002B7E7B  F6 C3 10                        test bl, 0x10
002B7E7E  0F 85 3D 04 00 00               jne 0x1402b82c1
002B7E84  4C 8B F0                        mov r14, rax
002B7E87  49 F7 D6                        not r14
002B7E8A  4C 23 F3                        and r14, rbx
002B7E8D  49 C1 FE 10                     sar r14, 0x10
002B7E91  4C 89 B4 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], r14
002B7E99  49 8B 16                        mov rdx, qword ptr [r14]
002B7E9C  48 89 94 24 98 00 00 00         mov qword ptr [rsp + 0x98], rdx
002B7EA4  48 89 94 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rdx
002B7EAC  0F B7 42 3C                     movzx eax, word ptr [rdx + 0x3c]
002B7EB0  B9 FF 03 00 00                  mov ecx, 0x3ff
002B7EB5  66 23 C1                        and ax, cx
002B7EB8  0F B7 C8                        movzx ecx, ax
002B7EBB  48 8B 05 C6 81 B7 00            mov rax, qword ptr [rip + 0xb781c6]
002B7EC2  48 8B 34 C8                     mov rsi, qword ptr [rax + rcx*8]
002B7EC6  8B 42 38                        mov eax, dword ptr [rdx + 0x38]
002B7EC9  C1 E8 14                        shr eax, 0x14
002B7ECC  83 E0 7F                        and eax, 0x7f
002B7ECF  4C 8D 1D 2A 81 D4 FF            lea r11, [rip - 0x2b7ed6]
002B7ED6  0F 85 D3 03 00 00               jne 0x1402b82af
002B7EDC  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002B7EE5  8B 88 4C 02 00 00               mov ecx, dword ptr [rax + 0x24c]
002B7EEB  4D 8B 94 CB 40 8C FC 00         mov r10, qword ptr [r11 + rcx*8 + 0xfc8c40]
002B7EF3  45 8B 8A 54 87 00 00            mov r9d, dword ptr [r10 + 0x8754]
002B7EFA  4C 89 94 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], r10
002B7F02  41 8B C9                        mov ecx, r9d
002B7F05  E8 A6 66 06 00                  call 0x14031e5b0
002B7F0A  41 83 E1 3F                     and r9d, 0x3f
002B7F0E  41 81 C9 80 01 00 00            or r9d, 0x180
002B7F15  45 03 C9                        add r9d, r9d
002B7F18  0F B6 C0                        movzx eax, al
002B7F1B  41 BF 01 00 00 00               mov r15d, 1
002B7F21  41 23 C7                        and eax, r15d
002B7F24  44 0B C8                        or r9d, eax
002B7F27  41 C1 E1 08                     shl r9d, 8
002B7F2B  4D 8D 82 50 87 00 00            lea r8, [r10 + 0x8750]
002B7F32  4C 89 84 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], r8
002B7F3A  48 C1 EB 05                     shr rbx, 5
002B7F3E  83 E3 1F                        and ebx, 0x1f
002B7F41  89 5C 24 38                     mov dword ptr [rsp + 0x38], ebx
002B7F45  8B CB                           mov ecx, ebx
002B7F47  E8 E4 05 00 00                  call 0x1402b8530
002B7F4C  44 8B E0                        mov r12d, eax
002B7F4F  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
002B7F53  44 8B D0                        mov r10d, eax
002B7F56  41 83 E2 03                     and r10d, 3
002B7F5A  41 C1 E2 12                     shl r10d, 0x12
002B7F5E  45 0B D1                        or r10d, r9d
002B7F61  44 89 94 24 E0 00 00 00         mov dword ptr [rsp + 0xe0], r10d
002B7F69  41 8B C7                        mov eax, r15d
002B7F6C  F0 41 0F C1 00                  lock xadd dword ptr [r8], eax
002B7F71  41 8B CA                        mov ecx, r10d
002B7F74  C1 E9 10                        shr ecx, 0x10
002B7F77  83 E1 03                        and ecx, 3
002B7F7A  33 D2                           xor edx, edx
002B7F7C  41 F7 B4 8B C0 DC E2 00         div dword ptr [r11 + rcx*4 + 0xe2dcc0]
002B7F84  0F B6 D2                        movzx edx, dl
002B7F87  41 0B D2                        or edx, r10d
002B7F8A  45 33 C0                        xor r8d, r8d
002B7F8D  48 8B CE                        mov rcx, rsi
002B7F90  E8 2B 05 FD FF                  call 0x1402884c0
002B7F95  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
002B7F9A  48 83 F8 FF                     cmp rax, -1
002B7F9E  0F 84 84 04 00 00               je 0x1402b8428
002B7FA4  48 8D 34 40                     lea rsi, [rax + rax*2]
002B7FA8  48 C1 E6 04                     shl rsi, 4
002B7FAC  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
002B7FB6  48 03 F0                        add rsi, rax
002B7FB9  48 89 B4 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rsi
002B7FC1  45 33 ED                        xor r13d, r13d
002B7FC4  33 C0                           xor eax, eax
002B7FC6  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
002B7FCA  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
002B7FCE  48 81 7C 24 60 00 10 00 00      cmp qword ptr [rsp + 0x60], 0x1000
002B7FD7  0F 85 6F 03 00 00               jne 0x1402b834c
002B7FDD  48 8D 46 20                     lea rax, [rsi + 0x20]
002B7FE1  48 89 84 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rax
002B7FE9  8B 00                           mov eax, dword ptr [rax]
002B7FEB  C1 E8 10                        shr eax, 0x10
002B7FEE  0F B6 C8                        movzx ecx, al
002B7FF1  C1 E9 06                        shr ecx, 6
002B7FF4  41 3B CC                        cmp ecx, r12d
002B7FF7  74 11                           je 0x1402b800a
002B7FF9  41 B8 08 00 00 00               mov r8d, 8
002B7FFF  41 8B D4                        mov edx, r12d
002B8002  48 8B CE                        mov rcx, rsi
002B8005  E8 C2 AE 07 00                  call 0x140332ecc
002B800A  4C 8D 66 18                     lea r12, [rsi + 0x18]
002B800E  4C 89 A4 24 90 00 00 00         mov qword ptr [rsp + 0x90], r12
002B8016  49 8B 14 24                     mov rdx, qword ptr [r12]
002B801A  48 8B CA                        mov rcx, rdx
002B801D  49 B9 FF FF FF FF FF FF FF C7   movabs r9, 0xc7ffffffffffffff
002B8027  49 23 C9                        and rcx, r9
002B802A  48 8B C2                        mov rax, rdx
002B802D  F0 49 0F B1 0C 24               lock cmpxchg qword ptr [r12], rcx
002B8033  48 3B D0                        cmp rdx, rax
002B8036  4C 8B C0                        mov r8, rax
002B8039  0F 85 0A 04 00 00               jne 0x1402b8449
002B803F  41 8B D7                        mov edx, r15d
002B8042  48 8D 0D 1F F6 B7 00            lea rcx, [rip + 0xb7f61f]
002B8049  E8 D2 0C 06 00                  call 0x140318d20
002B804E  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
002B8053  48 85 C0                        test rax, rax
002B8056  0F 84 99 02 00 00               je 0x1402b82f5
002B805C  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
002B8061  48 8B C8                        mov rcx, rax
002B8064  E8 27 F1 00 00                  call 0x1402c7190
002B8069  48 8B C8                        mov rcx, rax
002B806C  44 8B 44 24 58                  mov r8d, dword ptr [rsp + 0x58]
002B8071  4C 89 44 24 40                  mov qword ptr [rsp + 0x40], r8
002B8076  49 8D 14 00                     lea rdx, [r8 + rax]
002B807A  48 89 54 24 58                  mov qword ptr [rsp + 0x58], rdx
002B807F  45 85 ED                        test r13d, r13d
002B8082  0F 85 DA 02 00 00               jne 0x1402b8362
002B8088  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
002B808D  45 33 ED                        xor r13d, r13d
002B8090  44 89 6C 24 48                  mov dword ptr [rsp + 0x48], r13d
002B8095  4C 8B C1                        mov r8, rcx
002B8098  48 8B 94 24 A8 00 00 00         mov rdx, qword ptr [rsp + 0xa8]
002B80A0  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
002B80A5  E8 96 E7 40 00                  call 0x1406c6840
002B80AA  EB 4F                           jmp 0x1402b80fb
002B80AC  41 BF 01 00 00 00               mov r15d, 1
002B80B2  44 8B 6C 24 48                  mov r13d, dword ptr [rsp + 0x48]
002B80B7  48 8B B4 24 B0 00 00 00         mov rsi, qword ptr [rsp + 0xb0]
002B80BF  48 8B 84 24 B8 00 00 00         mov rax, qword ptr [rsp + 0xb8]
002B80C7  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
002B80CF  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
002B80D3  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
002B80D7  8B 5C 24 38                     mov ebx, dword ptr [rsp + 0x38]
002B80DB  4C 8B B4 24 C0 00 00 00         mov r14, qword ptr [rsp + 0xc0]
002B80E3  48 8B 8C 24 C8 00 00 00         mov rcx, qword ptr [rsp + 0xc8]
002B80EB  48 89 8C 24 80 00 00 00         mov qword ptr [rsp + 0x80], rcx
002B80F3  4C 8B A4 24 90 00 00 00         mov r12, qword ptr [rsp + 0x90]
002B80FB  45 8B C7                        mov r8d, r15d
002B80FE  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
002B8103  48 8D 0D 5E F5 B7 00            lea rcx, [rip + 0xb7f55e]
002B810A  E8 31 F1 F8 FF                  call 0x140247240
002B810F  45 85 ED                        test r13d, r13d
002B8112  0F 88 72 03 00 00               js 0x1402b848a
002B8118  8B 05 E6 E9 D0 00               mov eax, dword ptr [rip + 0xd0e9e6]
002B811E  41 23 C7                        and eax, r15d
002B8121  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
002B8125  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
002B812A  4C 8B AC 24 80 00 00 00         mov r13, qword ptr [rsp + 0x80]
002B8132  49 8B CD                        mov rcx, r13
002B8135  E8 46 0A 00 00                  call 0x1402b8b80
002B813A  48 8B C8                        mov rcx, rax
002B813D  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
002B8145  48 85 C0                        test rax, rax
002B8148  0F 84 54 01 00 00               je 0x1402b82a2
002B814E  49 8B 45 00                     mov rax, qword ptr [r13]
002B8152  41 84 C7                        test r15b, al
002B8155  0F 85 54 03 00 00               jne 0x1402b84af
002B815B  48 0F BA E0 0B                  bt rax, 0xb
002B8160  0F 82 3E 03 00 00               jb 0x1402b84a4
002B8166  48 C1 E8 05                     shr rax, 5
002B816A  83 E0 1F                        and eax, 0x1f
002B816D  3B D8                           cmp ebx, eax
002B816F  0F 85 3A 03 00 00               jne 0x1402b84af
002B8175  83 64 24 50 00                  and dword ptr [rsp + 0x50], 0
002B817A  F0 49 0F BA 2C 24 3F            lock bts qword ptr [r12], 0x3f
002B8181  0F 82 43 01 00 00               jb 0x1402b82ca
002B8187  41 B9 03 00 00 00               mov r9d, 3
002B818D  44 8B C3                        mov r8d, ebx
002B8190  4C 8B AC 24 80 00 00 00         mov r13, qword ptr [rsp + 0x80]
002B8198  49 8B D5                        mov rdx, r13
002B819B  48 8B CE                        mov rcx, rsi
002B819E  E8 BD 9C 07 00                  call 0x140331e60
002B81A3  F6 84 24 A0 01 00 00 02         test byte ptr [rsp + 0x1a0], 2
002B81AB  0F 85 65 01 00 00               jne 0x1402b8316
002B81B1  45 8B C7                        mov r8d, r15d
002B81B4  49 8B D6                        mov rdx, r14
002B81B7  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
002B81BF  E8 C0 BE 0A 00                  call 0x140364084
002B81C4  0F BA EB 1F                     bts ebx, 0x1f
002B81C8  44 8B C3                        mov r8d, ebx
002B81CB  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
002B81D0  33 C9                           xor ecx, ecx
002B81D2  E8 B9 D3 00 00                  call 0x1402c5590
002B81D7  48 8B D8                        mov rbx, rax
002B81DA  48 0F BA F3 08                  btr rbx, 8
002B81DF  48 89 9C 24 10 01 00 00         mov qword ptr [rsp + 0x110], rbx
002B81E7  49 BE 00 00 00 00 80 F6 FF FF   movabs r14, 0xfffff68000000000
002B81F1  48 0F BA 25 8E E8 D0 00 24      bt qword ptr [rip + 0xd0e88e], 0x24
002B81FA  0F 82 95 01 00 00               jb 0x1402b8395
002B8200  48 B9 00 00 00 00 40 00 00 00   movabs rcx, 0x4000000000
002B820A  49 89 5D 00                     mov qword ptr [r13], rbx
002B820E  48 89 9C 24 18 01 00 00         mov qword ptr [rsp + 0x118], rbx
002B8216  48 0F BA 25 69 E8 D0 00 24      bt qword ptr [rip + 0xd0e869], 0x24
002B821F  0F 82 A8 01 00 00               jb 0x1402b83cd
002B8225  4C 8B 74 24 68                  mov r14, qword ptr [rsp + 0x68]
002B822A  49 89 1E                        mov qword ptr [r14], rbx
002B822D  8B 5C 24 38                     mov ebx, dword ptr [rsp + 0x38]
002B8231  85 DB                           test ebx, ebx
002B8233  0F 85 84 02 00 00               jne 0x1402b84bd
002B8239  33 D2                           xor edx, edx
002B823B  48 8B CE                        mov rcx, rsi
002B823E  E8 2D BD 07 00                  call 0x140333f70
002B8243  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
002B824D  F0 49 21 04 24                  lock and qword ptr [r12], rax
002B8252  8A 54 24 30                     mov dl, byte ptr [rsp + 0x30]
002B8256  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
002B825E  E8 2D DE F8 FF                  call 0x140246090
002B8263  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
002B826B  83 20 00                        and dword ptr [rax], 0
002B826E  85 DB                           test ebx, ebx
002B8270  0F 85 5E 02 00 00               jne 0x1402b84d4
002B8276  F7 5C 24 34                     neg dword ptr [rsp + 0x34]
002B827A  1B C0                           sbb eax, eax
002B827C  83 E0 02                        and eax, 2
002B827F  48 8B 8C 24 30 01 00 00         mov rcx, qword ptr [rsp + 0x130]
002B8287  48 33 CC                        xor rcx, rsp
002B828A  E8 B1 43 3F 00                  call 0x1406ac640
002B828F  48 81 C4 48 01 00 00            add rsp, 0x148
002B8296  41 5F                           pop r15
002B8298  41 5E                           pop r14
002B829A  41 5D                           pop r13
002B829C  41 5C                           pop r12
002B829E  5E                              pop rsi
002B829F  5B                              pop rbx
002B82A0  C3                              ret
002B82A1  CC                              int3
002B82A2  48 8B CE                        mov rcx, rsi
002B82A5  E8 FE 8C 1B 00                  call 0x140470fa8
002B82AA  41 8B C7                        mov eax, r15d
002B82AD  EB D0                           jmp 0x1402b827f
002B82AF  65 4C 8B 14 25 20 00 00 00      mov r10, qword ptr gs:[0x20]
002B82B8  44 8D 48 FF                     lea r9d, [rax - 1]
002B82BC  E9 39 FC FF FF                  jmp 0x1402b7efa
002B82C1  49 83 E6 EF                     and r14, 0xffffffffffffffef
002B82C5  E9 C3 FB FF FF                  jmp 0x1402b7e8d
002B82CA  44 8B 6C 24 50                  mov r13d, dword ptr [rsp + 0x50]
002B82CF  45 03 EF                        add r13d, r15d
002B82D2  44 89 6C 24 50                  mov dword ptr [rsp + 0x50], r13d
002B82D7  44 85 2D CE CF D0 00            test dword ptr [rip + 0xd0cfce], r13d
002B82DE  0F 84 1C 01 00 00               je 0x1402b8400
002B82E4  F3 90                           pause
002B82E6  49 8B 04 24                     mov rax, qword ptr [r12]
002B82EA  48 85 C0                        test rax, rax
002B82ED  0F 89 87 FE FF FF               jns 0x1402b817a
002B82F3  EB D5                           jmp 0x1402b82ca
002B82F5  44 84 BC 24 A0 01 00 00         test byte ptr [rsp + 0x1a0], r15b
002B82FD  0F 84 34 01 00 00               je 0x1402b8437
002B8303  45 85 ED                        test r13d, r13d
002B8306  0F 85 54 01 00 00               jne 0x1402b8460
002B830C  44 89 7C 24 34                  mov dword ptr [rsp + 0x34], r15d
002B8311  E9 02 FE FF FF                  jmp 0x1402b8118
002B8316  48 8B CE                        mov rcx, rsi
002B8319  E8 D2 A3 06 00                  call 0x1403226f0
002B831E  83 F8 02                        cmp eax, 2
002B8321  0F 86 8A FE FF FF               jbe 0x1402b81b1
002B8327  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
002B832F  8B 00                           mov eax, dword ptr [rax]
002B8331  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
002B8335  C1 E8 18                        shr eax, 0x18
002B8338  24 FA                           and al, 0xfa
002B833A  0C 02                           or al, 2
002B833C  88 44 24 43                     mov byte ptr [rsp + 0x43], al
002B8340  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
002B8344  89 46 20                        mov dword ptr [rsi + 0x20], eax
002B8347  E9 65 FE FF FF                  jmp 0x1402b81b1
002B834C  41 8B D4                        mov edx, r12d
002B834F  48 8B CE                        mov rcx, rsi
002B8352  E8 29 77 FE FF                  call 0x14029fa80
002B8357  85 C0                           test eax, eax
002B8359  45 0F 45 EF                     cmovne r13d, r15d
002B835D  E9 7B FC FF FF                  jmp 0x1402b7fdd
002B8362  45 85 C0                        test r8d, r8d
002B8365  0F 85 0E 01 00 00               jne 0x1402b8479
002B836B  B8 00 10 00 00                  mov eax, 0x1000
002B8370  48 2B 44 24 40                  sub rax, qword ptr [rsp + 0x40]
002B8375  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
002B837A  48 2B C1                        sub rax, rcx
002B837D  0F 84 0A FD FF FF               je 0x1402b808d
002B8383  48 03 CA                        add rcx, rdx
002B8386  4C 8B C0                        mov r8, rax
002B8389  33 D2                           xor edx, edx
002B838B  E8 B0 E8 40 00                  call 0x1406c6c40
002B8390  E9 F3 FC FF FF                  jmp 0x1402b8088
002B8395  F6 C3 20                        test bl, 0x20
002B8398  0F 85 62 FE FF FF               jne 0x1402b8200
002B839E  49 8B C6                        mov rax, r14
002B83A1  48 B9 00 00 00 00 40 00 00 00   movabs rcx, 0x4000000000
002B83AB  48 03 C1                        add rax, rcx
002B83AE  4C 3B E8                        cmp r13, rax
002B83B1  0F 82 53 FE FF FF               jb 0x1402b820a
002B83B7  41 B8 80 00 00 00               mov r8d, 0x80
002B83BD  48 8B D3                        mov rdx, rbx
002B83C0  49 8B CD                        mov rcx, r13
002B83C3  E8 B8 A9 FD FF                  call 0x140292d80
002B83C8  E9 33 FE FF FF                  jmp 0x1402b8200
002B83CD  F6 C3 20                        test bl, 0x20
002B83D0  0F 85 4F FE FF FF               jne 0x1402b8225
002B83D6  49 8B C6                        mov rax, r14
002B83D9  48 03 C1                        add rax, rcx
002B83DC  4C 8B 74 24 68                  mov r14, qword ptr [rsp + 0x68]
002B83E1  4C 3B F0                        cmp r14, rax
002B83E4  0F 82 40 FE FF FF               jb 0x1402b822a
002B83EA  41 B8 80 00 00 00               mov r8d, 0x80
002B83F0  48 8B D3                        mov rdx, rbx
002B83F3  49 8B CE                        mov rcx, r14
002B83F6  E8 85 A9 FD FF                  call 0x140292d80
002B83FB  E9 2A FE FF FF                  jmp 0x1402b822a
002B8400  8B 05 B2 E6 D0 00               mov eax, dword ptr [rip + 0xd0e6b2]
002B8406  A8 40                           test al, 0x40
002B8408  0F 84 D6 FE FF FF               je 0x1402b82e4
002B840E  E8 7D 70 05 00                  call 0x14030f490
002B8413  84 C0                           test al, al
002B8415  0F 84 C9 FE FF FF               je 0x1402b82e4
002B841B  41 8B CD                        mov ecx, r13d
002B841E  E8 3D 70 05 00                  call 0x14030f460
002B8423  E9 BE FE FF FF                  jmp 0x1402b82e6
002B8428  33 D2                           xor edx, edx
002B842A  48 8B CE                        mov rcx, rsi
002B842D  E8 F2 AE FE FF                  call 0x1402a3324
002B8432  E9 73 FE FF FF                  jmp 0x1402b82aa
002B8437  48 8B CE                        mov rcx, rsi
002B843A  E8 A1 C6 07 00                  call 0x140334ae0
002B843F  B8 02 00 00 00                  mov eax, 2
002B8444  E9 36 FE FF FF                  jmp 0x1402b827f
002B8449  49 8B C8                        mov rcx, r8
002B844C  4D 23 C1                        and r8, r9
002B844F  48 8B C1                        mov rax, rcx
002B8452  F0 4D 0F B1 04 24               lock cmpxchg qword ptr [r12], r8
002B8458  48 3B C8                        cmp rcx, rax
002B845B  E9 D6 FB FF FF                  jmp 0x1402b8036
002B8460  44 8B 4C 24 40                  mov r9d, dword ptr [rsp + 0x40]
002B8465  45 33 C0                        xor r8d, r8d
002B8468  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
002B846D  33 C9                           xor ecx, ecx
002B846F  E8 1C A1 07 00                  call 0x140332590
002B8474  E9 93 FE FF FF                  jmp 0x1402b830c
002B8479  33 D2                           xor edx, edx
002B847B  E8 C0 E7 40 00                  call 0x1406c6c40
002B8480  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
002B8485  E9 E1 FE FF FF                  jmp 0x1402b836b
002B848A  48 8B CE                        mov rcx, rsi
002B848D  E8 16 8B 1B 00                  call 0x140470fa8
002B8492  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
002B849A  44 89 28                        mov dword ptr [rax], r13d
002B849D  33 C0                           xor eax, eax
002B849F  E9 DB FD FF FF                  jmp 0x1402b827f
002B84A4  48 0F BA E0 0A                  bt rax, 0xa
002B84A9  0F 82 B7 FC FF FF               jb 0x1402b8166
002B84AF  8A 54 24 30                     mov dl, byte ptr [rsp + 0x30]
002B84B3  E8 D8 DB F8 FF                  call 0x140246090
002B84B8  E9 E5 FD FF FF                  jmp 0x1402b82a2
002B84BD  48 8D 94 24 E8 00 00 00         lea rdx, [rsp + 0xe8]
002B84C5  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
002B84CA  E8 F1 45 06 00                  call 0x14031cac0
002B84CF  E9 65 FD FF FF                  jmp 0x1402b8239
002B84D4  48 83 8C 24 00 01 00 00 04      or qword ptr [rsp + 0x100], 4
002B84DD  48 8D 84 24 E8 00 00 00         lea rax, [rsp + 0xe8]
002B84E5  48 89 84 24 20 01 00 00         mov qword ptr [rsp + 0x120], rax
002B84ED  C7 84 24 28 01 00 00 20 00 00 00  mov dword ptr [rsp + 0x128], 0x20
002B84F8  83 A4 24 2C 01 00 00 00         and dword ptr [rsp + 0x12c], 0
002B8500  41 B9 82 02 00 00               mov r9d, 0x282
002B8506  C7 44 24 20 04 1B 50 11         mov dword ptr [rsp + 0x20], 0x11501b04
002B850E  41 B8 01 00 00 20               mov r8d, 0x20000001
002B8514  41 8B D7                        mov edx, r15d
002B8517  48 8D 8C 24 20 01 00 00         lea rcx, [rsp + 0x120]
002B851F  E8 2C CE F7 FF                  call 0x140235350
002B8524  E9 4D FD FF FF                  jmp 0x1402b8276
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiMakePageAvoidRead(__int64 a1, __int64 a2, int a3, __int64 a4, unsigned __int8 a5, __int64 a6, __int64 a7)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned int v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned int v_stack_m130;
    unsigned int v_stack_m138;
    unsigned int v_stack_m140;
    unsigned int v_stack_m144;
    unsigned __int8 v_stack_m148;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m98;
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
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p100;
    unsigned __int64 v_stack_p120;
    unsigned int v_stack_p128;
    unsigned int v_stack_p12C;
    unsigned __int8 v_stack_p1A0;
    unsigned int v_stack_p20;
    unsigned __int8 v_stack_p30;
    unsigned int v_stack_p34;
    unsigned int v_stack_p40;
    unsigned __int8 v_stack_p43;
    unsigned int v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p88;
    unsigned __int64 v_stack_pD0;
    unsigned __int64 v_stack_pE8;

    v_rsp = (v_rsp) - (328);
    result = (*(unsigned __int64 *)(v_rip + 11872583)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m118 = a4;
    v_stack_m120 = a3;
    v_stack_mD0 = a2;
    v_stack_mF8 = a1;
    v_stack_mB0 = a1;
    v_stack_m110 = a6;
    v_stack_mF0 = a7;
    v_stack_m148 = 0;
    v_stack_mA0 = v_xmm0;
    v_stack_m90 = v_xmm1;
    v_stack_m80 = v_xmm1;
    if (*(unsigned __int64 *)(v_rip + 12017162) == 0) goto loc_002B7E8D;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a6))) & (16)) != 0) goto loc_002B82C1;
    v_r14 = ~(*(unsigned __int64 *)(v_rip + 12017162));
    v_r14 = (v_r14) & (*(unsigned __int64 *)(a6));
loc_002B7E8D:
    v_r14 = (v_r14) >> (16);
    v_stack_mB8 = v_r14;
    v_stack_mE0 = *(unsigned __int64 *)(v_r14);
    v_stack_mC0 = *(unsigned __int64 *)(v_r14);
    result = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_r14) + 60)) & ((unsigned __int16)((unsigned int)(0x3FFULL))));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r14) + 56))) >> (20));
    result = (unsigned int)((result) & (127));
    if (condition_is_not_equal) goto loc_002B82AF;
loc_002B7EFA:
    v_stack_mD8 = *(unsigned __int64 *)(v_rip - 2850518 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 588)) * 8 + 16550976);
    result = MiAssignDefaultChannel((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip - 2850518 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 588)) * 8 + 16550976) + 34644)))), *(unsigned __int64 *)(v_r14), a3, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip - 2850518 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 588)) * 8 + 16550976) + 34644)));
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip - 2850518 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 588)) * 8 + 16550976) + 34644))) & (63));
    a4 = (unsigned int)((a4) | (384));
    a4 = (unsigned int)((a4) + ((unsigned int)(a4)));
    result = (unsigned int)(((unsigned __int8)(result)) & (1));
    a4 = (unsigned int)((a4) | ((unsigned int)(result)));
    a4 = (unsigned int)((a4) << (8));
    v_stack_mA0 = *(unsigned __int64 *)(v_rip - 2850518 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 588)) * 8 + 16550976) + 34640;
    v_rbx = (*(unsigned __int64 *)(a6)) >> (5);
    v_rbx = (unsigned int)((v_rbx) & (31));
    v_stack_m140 = (unsigned int)(v_rbx);
    result = MiProtectionToCacheAttribute((unsigned int)((unsigned int)(v_rbx)), *(unsigned __int64 *)(v_r14), *(unsigned __int64 *)(v_rip - 2850518 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 588)) * 8 + 16550976) + 34640, a4);
    v_stack_m138 = (unsigned int)(result);
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)(result))) & (3));
    v_r10 = (unsigned int)((v_r10) << (18));
    v_r10 = (unsigned int)((v_r10) | ((unsigned int)(a4)));
    v_stack_m98 = (unsigned int)(v_r10);
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r10))) >> (16));
    a1 = (unsigned int)((a1) & (3));
    a2 = 0;
    a2 = (unsigned int)((0) | ((unsigned int)(v_r10)));
    a3 = 0;
    result = MiGetPage(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12026310) + (unsigned __int16)(result) * 8), a2, a3, a4);
    v_stack_m108 = result;
    if (result == -1) goto loc_002B8428;
    v_rsi = (result + result * 2) << (4);
    v_rsi = (v_rsi) + (result);
    v_stack_mC8 = v_rsi;
    v_r13 = 0;
    result = 0;
    v_stack_m144 = 0;
    v_stack_m100 = 0;
    if (v_stack_m118 != 0x1000ULL) goto loc_002B834C;
loc_002B7FDD:
    v_stack_mA8 = v_rsi + 32;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 32))) >> (16));
    a1 = (unsigned int)(((unsigned __int8)(result)) >> (6));
    if (((unsigned int)(a1)) != ((unsigned int)((unsigned int)((unsigned int)(result))))) {
        a3 = 8;
        a2 = (unsigned int)((unsigned int)((unsigned int)(result)));
        a1 = v_rsi;
        result = MiChangePageAttribute(a1, a2, a3, a4);
    }
    v_stack_mE8 = v_rsi + 24;
    a1 = (*(unsigned __int64 *)(v_rsi + 24)) & (a4);
loc_002B8036:
    if ((*(unsigned __int64 *)(v_rsi + 24)) != (*(unsigned __int64 *)(v_rsi + 24))) goto loc_002B8449;
    result = MiReservePtes(v_rip + 12056095, 1, *(unsigned __int64 *)(v_rsi + 24), a4);
    v_stack_m128 = result;
    if (result == 0) goto loc_002B82F5;
    result = MiMapFrame(result, v_stack_m108, *(unsigned __int64 *)(v_rsi + 24), a4);
    v_stack_m138 = (unsigned int)(v_stack_m120);
    v_stack_m120 = (unsigned int)(v_stack_m120) + result * 1;
    if (0 != 0) goto loc_002B8362;
loc_002B8088:
loc_002B808D:
    v_r13 = 0;
    v_stack_m130 = 0;
    result = memcpy(v_stack_m120, v_stack_mD0, v_stack_m118, a4);
    goto loc_002B80FB;
loc_002B80FB:
    result = MiReleasePtes(v_rip + 12055902, v_stack_m128, 1, a4);
    if (sign_flag) goto loc_002B848A;
loc_002B8118:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 13691366))) & (1));
    v_stack_m140 = (unsigned int)(result);
    result = MiLockProtoPoolPage(v_stack_mF8, v_stack_m148, 1, a4);
    v_stack_mE8 = result;
    if (result == 0) goto loc_002B82A2;
    if (((1) & ((unsigned __int8)(*(unsigned __int64 *)(v_stack_mF8)))) != 0) goto loc_002B84AF;
    if (condition_is_below) goto loc_002B84A4;
loc_002B8166:
    result = (*(unsigned __int64 *)(v_stack_mF8)) >> (5);
    result = (unsigned int)((result) & (31));
    if (((unsigned int)(v_rbx)) != ((unsigned int)(result))) goto loc_002B84AF;
loc_002B817A:
    if (((unsigned int)(v_rbx)) < ((unsigned int)(result))) goto loc_002B82CA;
    result = MiInitializePfn(v_rsi, v_stack_mF8, (unsigned int)((unsigned int)(v_rbx)), 3);
    if (((a5) & (2)) != 0) goto loc_002B8316;
loc_002B81B1:
    result = MiReferenceControlAreaPfn(v_stack_mE0, v_r14, 1, 3);
    a1 = 0;
    result = MiMakeValidPte(a1, v_stack_m108, (unsigned int)((unsigned int)(v_rbx)), 3);
    v_stack_m68 = result;
    if (condition_is_below) goto loc_002B8395;
loc_002B8200:
loc_002B820A:
    *(unsigned __int64 *)(v_stack_mF8) = result;
    v_stack_m60 = result;
    if (condition_is_below) goto loc_002B83CD;
loc_002B8225:
loc_002B822A:
    *(unsigned __int64 *)(v_stack_m110) = result;
    if ((unsigned int)((unsigned int)(v_stack_m140)) != 0) goto loc_002B84BD;
loc_002B8239:
    a2 = 0;
    result = MiDecrementShareCountEx(v_rsi, a2, (unsigned int)((unsigned int)(v_rbx)), 3);
    result = MiUnlockProtoPoolPage(v_stack_mE8, v_stack_m148, (unsigned int)((unsigned int)(v_rbx)), 3);
    if ((unsigned int)((unsigned int)(v_stack_m140)) != 0) goto loc_002B84D4;
loc_002B8276:
    result = (unsigned int)((v_stack_mF0) & (2));
loc_002B827F:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m148, (unsigned int)((unsigned int)(v_rbx)), 3);
    v_rsp = (v_rsp) + (328);
    return result;
loc_002B82A2:
    result = MiLockAndInsertPageInFreeList(v_rsi, v_stack_m148, (unsigned int)((unsigned int)(v_rbx)), 3);
loc_002B82AA:
    goto loc_002B827F;
loc_002B82AF:
    goto loc_002B7EFA;
loc_002B82C1:
    v_r14 = (v_stack_m110) & (-17);
    goto loc_002B7E8D;
loc_002B82CA:
    v_r13 = (unsigned int)(((unsigned int)(v_stack_p50)) + (1));
    v_stack_p50 = (unsigned int)(v_r13);
    if (((*(unsigned int *)(v_rip + 13684686)) & ((unsigned int)(v_r13))) == 0) goto loc_002B8400;
loc_002B82E4:
loc_002B82E6:
    if (!sign_flag) goto loc_002B817A;
    goto loc_002B82CA;
loc_002B82F5:
    if (((v_stack_p1A0) & (1)) == 0) goto loc_002B8437;
    if ((unsigned int)(v_r13) != 0) goto loc_002B8460;
loc_002B830C:
    v_stack_p34 = 1;
    goto loc_002B8118;
loc_002B8316:
    result = MiGetPfnPriority(v_rsi, v_stack_m148, (unsigned int)((unsigned int)(v_rbx)), 1 - 1);
    if (((unsigned int)(result)) <= 2) goto loc_002B81B1;
    v_stack_p40 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_pD0)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_pD0))) >> (24));
    result = (unsigned __int8)((result) & (250));
    result = (unsigned __int8)((result) | (2));
    v_stack_p43 = (unsigned __int8)(result);
    *(unsigned int *)(v_rsi + 32) = (unsigned int)((unsigned int)(v_stack_p40));
    goto loc_002B81B1;
loc_002B834C:
    result = MiPfnZeroingNeeded(v_rsi, (unsigned int)((unsigned int)(v_rsi + 24)), (unsigned int)((unsigned int)(v_rbx)), 1 - 1);
    if ((unsigned int)(result) != 0) { v_r13 = 1; }
    goto loc_002B7FDD;
loc_002B8362:
    if ((unsigned int)((unsigned int)((unsigned int)(v_rbx))) != 0) goto loc_002B8479;
loc_002B836B:
    result = ((unsigned int)(0x1000ULL)) - (v_stack_p40);
    result = (result) - (v_stack_p60);
    if (condition_is_equal) goto loc_002B808D;
    a1 = (v_stack_p60) + ((unsigned int)((unsigned int)(v_rsi + 24)));
    a2 = 0;
    result = memset(a1, a2, result, 1 - 1);
    goto loc_002B8088;
loc_002B8395:
    if ((((unsigned __int8)((unsigned int)(v_stack_m140))) & (32)) != 0) goto loc_002B8200;
    result = (v_r14) + (a1);
    if (v_r13 < result) goto loc_002B820A;
    result = MiCheckLinearProtectedPteAccessedBit(v_r13, (unsigned int)(v_stack_m140), 128, 1 - 1);
    goto loc_002B8200;
loc_002B83CD:
    if ((((unsigned __int8)((unsigned int)(v_stack_m140))) & (32)) != 0) goto loc_002B8225;
    result = (v_r14) + (v_r13);
    if (v_stack_p68 < result) goto loc_002B822A;
    result = MiCheckLinearProtectedPteAccessedBit(v_stack_p68, (unsigned int)(v_stack_m140), 128, 1 - 1);
    goto loc_002B822A;
loc_002B8400:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13690546)))) & (64)) == 0) goto loc_002B82E4;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_p68, (unsigned int)(v_stack_m140), 128, 1 - 1);
    if ((unsigned __int8)(result) == 0) goto loc_002B82E4;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r13)), (unsigned int)(v_stack_m140), 128, 1 - 1);
    goto loc_002B82E6;
loc_002B8428:
    a2 = 0;
    result = MiWaitForFreePage(v_rsi, a2, 128, 1 - 1);
    goto loc_002B82AA;
loc_002B8437:
    result = MiReleaseFreshPage(v_rsi, a2, 128, 1 - 1);
    goto loc_002B827F;
loc_002B8449:
    a3 = (128) & (1 - 1);
    goto loc_002B8036;
loc_002B8460:
    a3 = 0;
    a1 = 0;
    result = MiZeroPhysicalPage(a1, v_stack_p70, a3, (unsigned int)(v_stack_p40));
    goto loc_002B830C;
loc_002B8479:
    a2 = 0;
    result = memset(a1, a2, a3, (unsigned int)(v_stack_p40));
    goto loc_002B836B;
loc_002B848A:
    result = MiLockAndInsertPageInFreeList(v_rsi, v_stack_p58, a3, (unsigned int)(v_stack_p40));
    *(unsigned int *)(v_stack_p88) = (unsigned int)(v_r13);
    result = 0;
    goto loc_002B827F;
loc_002B84A4:
    if (condition_is_below) goto loc_002B8166;
loc_002B84AF:
    result = MiUnlockProtoPoolPage(v_rsi, v_stack_p30, a3, (unsigned int)(v_stack_p40));
    goto loc_002B82A2;
loc_002B84BD:
    result = MiIdentifyPfn(v_stack_p70, v_stack_pE8, a3, (unsigned int)(v_stack_p40));
    goto loc_002B8239;
loc_002B84D4:
    v_stack_p120 = v_stack_pE8;
    v_stack_p128 = 32;
    v_stack_p20 = 0x11501B04ULL;
    result = EtwTraceKernelEvent(v_stack_p120, 1, (unsigned int)(0x20000001ULL), 642);
    goto loc_002B8276;
}
```

## 5. (Beta) C Style

```c
int64_t MiMakePageAvoidRead(int64_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, uint8_t Arg5, void *Arg6, void *Arg7)
{
    uint8_t *arg6 = (uint8_t *)Arg6;
    uint8_t *arg7 = (uint8_t *)Arg7;

    int64_t result;
    int64_t local_r10;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint32_t v_stack_m120;
    uint64_t v_stack_m128;
    uint32_t v_stack_m130;
    uint32_t v_stack_m138;
    uint32_t v_stack_m140;
    uint32_t v_stack_m144;
    uint8_t v_stack_m148;
    uint64_t v_stack_m48;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m80;
    uint64_t v_stack_m90;
    uint32_t v_stack_m98;
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
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p100;
    uint64_t v_stack_p120;
    uint32_t v_stack_p128;
    uint32_t v_stack_p12C;
    uint8_t v_stack_p1A0;
    uint32_t v_stack_p20;
    uint8_t v_stack_p30;
    uint32_t v_stack_p34;
    uint32_t v_stack_p40;
    uint8_t v_stack_p43;
    uint32_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p88;
    uint64_t v_stack_pD0;
    uint64_t v_stack_pE8;

    local_rsp = (local_rsp) - (328);
    result = (*(uint64_t *)(v_rip + 0xB52947)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m118 = Arg4;
    v_stack_m120 = Arg3;
    v_stack_mD0 = Arg2;
    v_stack_mF8 = Arg1;
    v_stack_mB0 = Arg1;
    v_stack_m110 = Arg6;
    v_stack_mF0 = Arg7;
    v_stack_m148 = 0;
    v_stack_mA0 = v_xmm0;
    v_stack_m90 = v_xmm1;
    v_stack_m80 = v_xmm1;
    if (*(uint64_t *)(v_rip + 0xB75E0A) == 0) goto loc_002B7E8D;
    if ((((uint8_t)(*(uint64_t *)(arg6))) & (16)) != 0) goto loc_002B82C1;
    local_r14 = ~(*(uint64_t *)(v_rip + 0xB75E0A));
    local_r14 = (local_r14) & (*(uint64_t *)(arg6));
loc_002B7E8D:
    local_r14 = (local_r14) >> (16);
    v_stack_mB8 = local_r14;
    v_stack_mE0 = *(uint64_t *)(local_r14);
    v_stack_mC0 = *(uint64_t *)(local_r14);
    result = (uint16_t)((*(uint16_t *)(*(uint64_t *)(local_r14) + 0x3C)) & ((uint16_t)((uint32_t)(0x3FFULL))));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r14) + 0x38))) >> (20));
    result = (uint32_t)((result) & (127));
    if (condition_is_not_equal) goto loc_002B82AF;
loc_002B7EFA:
    v_stack_mD8 = *(uint64_t *)(v_rip - 0x2B7ED6 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x24C)) * 8 + 0xFC8C40);
    result = MiAssignDefaultChannel((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip - 0x2B7ED6 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x24C)) * 8 + 0xFC8C40) + 0x8754)))), *(uint64_t *)(local_r14), Arg3, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip - 0x2B7ED6 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x24C)) * 8 + 0xFC8C40) + 0x8754)));
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip - 0x2B7ED6 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x24C)) * 8 + 0xFC8C40) + 0x8754))) & (63));
    Arg4 = (uint32_t)((Arg4) | (384));
    Arg4 = (uint32_t)((Arg4) + ((uint32_t)(Arg4)));
    result = (uint32_t)(((uint8_t)(result)) & (1));
    Arg4 = (uint32_t)((Arg4) | ((uint32_t)(result)));
    Arg4 = (uint32_t)((Arg4) << (8));
    v_stack_mA0 = *(uint64_t *)(v_rip - 0x2B7ED6 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x24C)) * 8 + 0xFC8C40) + 34640;
    local_rbx = (*(uint64_t *)(arg6)) >> (5);
    local_rbx = (uint32_t)((local_rbx) & (31));
    v_stack_m140 = (uint32_t)(local_rbx);
    result = MiProtectionToCacheAttribute((uint32_t)((uint32_t)(local_rbx)), *(uint64_t *)(local_r14), *(uint64_t *)(v_rip - 0x2B7ED6 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x24C)) * 8 + 0xFC8C40) + 34640, Arg4);
    v_stack_m138 = (uint32_t)(result);
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)(result))) & (3));
    local_r10 = (uint32_t)((local_r10) << (18));
    local_r10 = (uint32_t)((local_r10) | ((uint32_t)(Arg4)));
    v_stack_m98 = (uint32_t)(local_r10);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r10))) >> (16));
    Arg1 = (uint32_t)((Arg1) & (3));
    Arg2 = 0;
    Arg2 = (uint32_t)((0) | ((uint32_t)(local_r10)));
    Arg3 = 0;
    result = MiGetPage(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB781C6) + (uint16_t)(result) * 8), Arg2, Arg3, Arg4);
    v_stack_m108 = result;
    if (result == -1) goto loc_002B8428;
    local_rsi = (result + result * 2) << (4);
    local_rsi = (local_rsi) + (result);
    v_stack_mC8 = local_rsi;
    local_r13 = 0;
    result = 0;
    v_stack_m144 = 0;
    v_stack_m100 = 0;
    if (v_stack_m118 != 0x1000ULL) goto loc_002B834C;
loc_002B7FDD:
    v_stack_mA8 = local_rsi + 32;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x20))) >> (16));
    Arg1 = (uint32_t)(((uint8_t)(result)) >> (6));
    if (((uint32_t)(Arg1)) != ((uint32_t)((uint32_t)((uint32_t)(result))))) {
        Arg3 = 8;
        Arg2 = (uint32_t)((uint32_t)((uint32_t)(result)));
        Arg1 = local_rsi;
        result = MiChangePageAttribute(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_mE8 = local_rsi + 24;
    Arg1 = (*(uint64_t *)(local_rsi + 0x18)) & (Arg4);
loc_002B8036:
    if ((*(uint64_t *)(local_rsi + 0x18)) != (*(uint64_t *)(local_rsi + 0x18))) goto loc_002B8449;
    result = MiReservePtes(v_rip + 12056095, 1, *(uint64_t *)(local_rsi + 0x18), Arg4);
    v_stack_m128 = result;
    if (result == 0) goto loc_002B82F5;
    result = MiMapFrame(result, v_stack_m108, *(uint64_t *)(local_rsi + 0x18), Arg4);
    v_stack_m138 = (uint32_t)(v_stack_m120);
    v_stack_m120 = (uint32_t)(v_stack_m120) + result * 1;
    if (0 != 0) goto loc_002B8362;
loc_002B8088:
loc_002B808D:
    local_r13 = 0;
    v_stack_m130 = 0;
    result = memcpy(v_stack_m120, v_stack_mD0, v_stack_m118, Arg4);
    goto loc_002B80FB;
loc_002B80FB:
    result = MiReleasePtes(v_rip + 12055902, v_stack_m128, 1, Arg4);
    if (sign_flag) goto loc_002B848A;
loc_002B8118:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xD0E9E6))) & (1));
    v_stack_m140 = (uint32_t)(result);
    result = MiLockProtoPoolPage(v_stack_mF8, v_stack_m148, 1, Arg4);
    v_stack_mE8 = result;
    if (result == 0) goto loc_002B82A2;
    if (((1) & ((uint8_t)(*(uint64_t *)(v_stack_mF8)))) != 0) goto loc_002B84AF;
    if (condition_is_below) goto loc_002B84A4;
loc_002B8166:
    result = (*(uint64_t *)(v_stack_mF8)) >> (5);
    result = (uint32_t)((result) & (31));
    if (((uint32_t)(local_rbx)) != ((uint32_t)(result))) goto loc_002B84AF;
loc_002B817A:
    if (((uint32_t)(local_rbx)) < ((uint32_t)(result))) goto loc_002B82CA;
    result = MiInitializePfn(local_rsi, v_stack_mF8, (uint32_t)((uint32_t)(local_rbx)), 3);
    if (((Arg5) & (2)) != 0) goto loc_002B8316;
loc_002B81B1:
    result = MiReferenceControlAreaPfn(v_stack_mE0, local_r14, 1, 3);
    Arg1 = 0;
    result = MiMakeValidPte(Arg1, v_stack_m108, (uint32_t)((uint32_t)(local_rbx)), 3);
    v_stack_m68 = result;
    if (condition_is_below) goto loc_002B8395;
loc_002B8200:
loc_002B820A:
    *(uint64_t *)(v_stack_mF8) = result;
    v_stack_m60 = result;
    if (condition_is_below) goto loc_002B83CD;
loc_002B8225:
loc_002B822A:
    *(uint64_t *)(v_stack_m110) = result;
    if ((uint32_t)((uint32_t)(v_stack_m140)) != 0) goto loc_002B84BD;
loc_002B8239:
    Arg2 = 0;
    result = MiDecrementShareCountEx(local_rsi, Arg2, (uint32_t)((uint32_t)(local_rbx)), 3);
    result = MiUnlockProtoPoolPage(v_stack_mE8, v_stack_m148, (uint32_t)((uint32_t)(local_rbx)), 3);
    if ((uint32_t)((uint32_t)(v_stack_m140)) != 0) goto loc_002B84D4;
loc_002B8276:
    result = (uint32_t)((v_stack_mF0) & (2));
loc_002B827F:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m148, (uint32_t)((uint32_t)(local_rbx)), 3);
    local_rsp = (local_rsp) + (328);
    return result;
loc_002B82A2:
    result = MiLockAndInsertPageInFreeList(local_rsi, v_stack_m148, (uint32_t)((uint32_t)(local_rbx)), 3);
loc_002B82AA:
    goto loc_002B827F;
loc_002B82AF:
    goto loc_002B7EFA;
loc_002B82C1:
    local_r14 = (v_stack_m110) & (-17);
    goto loc_002B7E8D;
loc_002B82CA:
    local_r13 = (uint32_t)(((uint32_t)(v_stack_p50)) + (1));
    v_stack_p50 = (uint32_t)(local_r13);
    if (((*(uint32_t *)(v_rip + 0xD0CFCE)) & ((uint32_t)(local_r13))) == 0) goto loc_002B8400;
loc_002B82E4:
loc_002B82E6:
    if (!sign_flag) goto loc_002B817A;
    goto loc_002B82CA;
loc_002B82F5:
    if (((v_stack_p1A0) & (1)) == 0) goto loc_002B8437;
    if ((uint32_t)(local_r13) != 0) goto loc_002B8460;
loc_002B830C:
    v_stack_p34 = 1;
    goto loc_002B8118;
loc_002B8316:
    result = MiGetPfnPriority(local_rsi, v_stack_m148, (uint32_t)((uint32_t)(local_rbx)), 1 - 1);
    if (((uint32_t)(result)) <= 2) goto loc_002B81B1;
    v_stack_p40 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_pD0)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_pD0))) >> (24));
    result = (uint8_t)((result) & (250));
    result = (uint8_t)((result) | (2));
    v_stack_p43 = (uint8_t)(result);
    *(uint32_t *)(local_rsi + 0x20) = (uint32_t)((uint32_t)(v_stack_p40));
    goto loc_002B81B1;
loc_002B834C:
    result = MiPfnZeroingNeeded(local_rsi, (uint32_t)((uint32_t)(local_rsi + 24)), (uint32_t)((uint32_t)(local_rbx)), 1 - 1);
    if ((uint32_t)(result) != 0) { local_r13 = 1; }
    goto loc_002B7FDD;
loc_002B8362:
    if ((uint32_t)((uint32_t)((uint32_t)(local_rbx))) != 0) goto loc_002B8479;
loc_002B836B:
    result = ((uint32_t)(0x1000ULL)) - (v_stack_p40);
    result = (result) - (v_stack_p60);
    if (condition_is_equal) goto loc_002B808D;
    Arg1 = (v_stack_p60) + ((uint32_t)((uint32_t)(local_rsi + 24)));
    Arg2 = 0;
    result = memset(Arg1, Arg2, result, 1 - 1);
    goto loc_002B8088;
loc_002B8395:
    if ((((uint8_t)((uint32_t)(v_stack_m140))) & (32)) != 0) goto loc_002B8200;
    result = (local_r14) + (Arg1);
    if (local_r13 < result) goto loc_002B820A;
    result = MiCheckLinearProtectedPteAccessedBit(local_r13, (uint32_t)(v_stack_m140), 128, 1 - 1);
    goto loc_002B8200;
loc_002B83CD:
    if ((((uint8_t)((uint32_t)(v_stack_m140))) & (32)) != 0) goto loc_002B8225;
    result = (local_r14) + (local_r13);
    if (v_stack_p68 < result) goto loc_002B822A;
    result = MiCheckLinearProtectedPteAccessedBit(v_stack_p68, (uint32_t)(v_stack_m140), 128, 1 - 1);
    goto loc_002B822A;
loc_002B8400:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD0E6B2)))) & (64)) == 0) goto loc_002B82E4;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_p68, (uint32_t)(v_stack_m140), 128, 1 - 1);
    if ((uint8_t)(result) == 0) goto loc_002B82E4;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r13)), (uint32_t)(v_stack_m140), 128, 1 - 1);
    goto loc_002B82E6;
loc_002B8428:
    Arg2 = 0;
    result = MiWaitForFreePage(local_rsi, Arg2, 128, 1 - 1);
    goto loc_002B82AA;
loc_002B8437:
    result = MiReleaseFreshPage(local_rsi, Arg2, 128, 1 - 1);
    goto loc_002B827F;
loc_002B8449:
    Arg3 = (128) & (1 - 1);
    goto loc_002B8036;
loc_002B8460:
    Arg3 = 0;
    Arg1 = 0;
    result = MiZeroPhysicalPage(Arg1, v_stack_p70, Arg3, (uint32_t)(v_stack_p40));
    goto loc_002B830C;
loc_002B8479:
    Arg2 = 0;
    result = memset(Arg1, Arg2, Arg3, (uint32_t)(v_stack_p40));
    goto loc_002B836B;
loc_002B848A:
    result = MiLockAndInsertPageInFreeList(local_rsi, v_stack_p58, Arg3, (uint32_t)(v_stack_p40));
    *(uint32_t *)(v_stack_p88) = (uint32_t)(local_r13);
    result = 0;
    goto loc_002B827F;
loc_002B84A4:
    if (condition_is_below) goto loc_002B8166;
loc_002B84AF:
    result = MiUnlockProtoPoolPage(local_rsi, v_stack_p30, Arg3, (uint32_t)(v_stack_p40));
    goto loc_002B82A2;
loc_002B84BD:
    result = MiIdentifyPfn(v_stack_p70, v_stack_pE8, Arg3, (uint32_t)(v_stack_p40));
    goto loc_002B8239;
loc_002B84D4:
    v_stack_p120 = v_stack_pE8;
    v_stack_p128 = 32;
    v_stack_p20 = 0x11501B04ULL;
    result = EtwTraceKernelEvent(v_stack_p120, 1, (uint32_t)(0x20000001ULL), 642);
    goto loc_002B8276;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg6` | `+ 0x0` | `64` | `R` |
| `Arg7` | `+ 0x0` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002B7DE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
