# MiCreateSlabEntry

- RVA: `0x00374DEC`–`0x003755A2` (길이 `1,974` bytes)
- VA: `0x0000000140374DEC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007AB48`
- 디코드: `465`개 명령, `1,974/1,974` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **27**; 고유 호출 대상: **25**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x00374E30` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00374E40` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00374EC6` → [MiAcquireNonPagedResources](../28/MiAcquireNonPagedResources_function_00286C60.md) (function, `0x00286C60`)
- `0x00374FA8` → [MiInitializeDemandCoalesceContext](../3D/MiInitializeDemandCoalesceContext_function_003D3350.md) (function, `0x003D3350`)
- `0x00374FBC` → [MiAllocateLargeZeroPages](../3B/MiAllocateLargeZeroPages_function_003B743C.md) (function, `0x003B743C`)
- `0x00374FF8` → [MiPopLargePfnList](../49/MiPopLargePfnList_function_0049C460.md) (function, `0x0049C460`)
- `0x0037501D` → [MiConvertActiveLargePageToSmall](../42/MiConvertActiveLargePageToSmall_function_00420AF8.md) (function, `0x00420AF8`)
- `0x00375025` → [MiAllocateSlabEntry](../4A/MiAllocateSlabEntry_function_004AE468.md) (function, `0x004AE468`)
- `0x00375053` → [MiGetCurrentSlabIdentity](../3B/MiGetCurrentSlabIdentity_function_003BD020.md) (function, `0x003BD020`)
- `0x003750B5` → [MiSetSlabTypeIdentifiers](../49/MiSetSlabTypeIdentifiers_function_00498AC8.md) (function, `0x00498AC8`)
- `0x003751AB` → [MiReInitializeFreeSlabPfn](MiReInitializeFreeSlabPfn_function_003758D8.md) (function, `0x003758D8`)
- `0x003751FE` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0037521A` → [MiUpdateSlabPagePlaceholderState](../2A/MiUpdateSlabPagePlaceholderState_function_002A0FB0.md) (function, `0x002A0FB0`)
- `0x00375230` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0037526F` → [MiGetSlabCurrentTime](../3B/MiGetSlabCurrentTime_function_003BCBCC.md) (function, `0x003BCBCC`)
- `0x003752A6` → [MiSetPfnIdentity](../2A/MiSetPfnIdentity_function_002A2350.md) (function, `0x002A2350`)
- `0x003752AE` → [MiAbortCombineScan](../2A/MiAbortCombineScan_function_002A1160.md) (function, `0x002A1160`)
- `0x003752DA` → [RtlpGetStackLimits](../2F/RtlpGetStackLimits_function_002F5F50.md) (function, `0x002F5F50`)
- `0x00375348` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00375367` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0037537A` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x003753ED` → [PsReferencePartitionSafe](../3B/PsReferencePartitionSafe_function_003BA6C0.md) (function, `0x003BA6C0`)
- `0x00375458` → [MiReleaseNonPagedResources](../32/MiReleaseNonPagedResources_function_0032299C.md) (function, `0x0032299C`)
- `0x003754AA` → [MiLogSlabEntryAllocateFailure](../3B/MiLogSlabEntryAllocateFailure_function_003BAA60.md) (function, `0x003BAA60`)
- `0x00375523` → [PsDereferencePartition](../34/PsDereferencePartition_function_00342E70.md) (function, `0x00342E70`)
- `0x0037555E` → [MiFreeLargePageMemory](MiFreeLargePageMemory_function_00377938.md) (function, `0x00377938`)
- `0x0037557E` → [PsDereferencePartition](../34/PsDereferencePartition_function_00342E70.md) (function, `0x00342E70`)

### Direct callers
- [MiReplenishSlabAllocator](MiReplenishSlabAllocator_function_003788E4.md) at `0x00378976`

### Static image references
- `0x00374E05` → RVA `0x00E0A740` (`.data`; read)
- `0x00374E47` → RVA `0x00011C60` (`.rdata`; read)
- `0x00374F6A` → RVA `0x00FC6ED0` (`ALMOSTRO`; read)
- `0x0037511F` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x00375161` → RVA `0x00FCF080` (`CACHEALI`; read)
- `0x0037524D` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x003752FF` → RVA `0x00FC5020` (`ALMOSTRO`; read)
- `0x00375359` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x003753AB` → RVA `0x00E38D00` (`.data`; read)
- `0x003753CB` → RVA `0x00E30088` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00374DEC  40 55                           push rbp
00374DEE  53                              push rbx
00374DEF  56                              push rsi
00374DF0  57                              push rdi
00374DF1  41 54                           push r12
00374DF3  41 55                           push r13
00374DF5  41 56                           push r14
00374DF7  41 57                           push r15
00374DF9  48 8D 6C 24 88                  lea rbp, [rsp - 0x78]
00374DFE  48 81 EC 78 01 00 00            sub rsp, 0x178
00374E05  48 8B 05 34 59 A9 00            mov rax, qword ptr [rip + 0xa95934]
00374E0C  48 33 C4                        xor rax, rsp
00374E0F  48 89 45 60                     mov qword ptr [rbp + 0x60], rax
00374E13  4C 8B EA                        mov r13, rdx
00374E16  44 89 44 24 3C                  mov dword ptr [rsp + 0x3c], r8d
00374E1B  33 D2                           xor edx, edx
00374E1D  44 88 4C 24 30                  mov byte ptr [rsp + 0x30], r9b
00374E22  48 8B F9                        mov rdi, rcx
00374E25  45 8A F1                        mov r14b, r9b
00374E28  48 8D 4D 00                     lea rcx, [rbp]
00374E2C  44 8D 42 60                     lea r8d, [rdx + 0x60]
00374E30  E8 0B 1E 35 00                  call 0x1406c6c40
00374E35  33 D2                           xor edx, edx
00374E37  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
00374E3C  44 8D 42 58                     lea r8d, [rdx + 0x58]
00374E40  E8 FB 1D 35 00                  call 0x1406c6c40
00374E45  33 C0                           xor eax, eax
00374E47  48 8D 15 12 CE C9 FF            lea rdx, [rip - 0x3631ee]
00374E4E  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00374E52  45 33 D2                        xor r10d, r10d
00374E55  89 45 F8                        mov dword ptr [rbp - 8], eax
00374E58  0F 57 C0                        xorps xmm0, xmm0
00374E5B  8B 87 88 00 00 00               mov eax, dword ptr [rdi + 0x88]
00374E61  B1 01                           mov cl, 1
00374E63  48 C1 E8 04                     shr rax, 4
00374E67  45 8B FA                        mov r15d, r10d
00374E6A  83 E0 03                        and eax, 3
00374E6D  88 4C 24 31                     mov byte ptr [rsp + 0x31], cl
00374E71  0F 11 45 C0                     movups xmmword ptr [rbp - 0x40], xmm0
00374E75  44 89 54 24 38                  mov dword ptr [rsp + 0x38], r10d
00374E7A  45 8B E2                        mov r12d, r10d
00374E7D  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
00374E81  8B 14 C2                        mov edx, dword ptr [rdx + rax*8]
00374E84  48 8B 87 B0 00 00 00            mov rax, qword ptr [rdi + 0xb0]
00374E8B  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
00374E8F  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00374E93  48 85 C0                        test rax, rax
00374E96  0F 85 1A 06 00 00               jne 0x1403754b6
00374E9C  49 81 BD 00 49 00 00 20 04 00 00  cmp qword ptr [r13 + 0x4900], 0x420
00374EA7  C7 44 24 34 01 00 00 00         mov dword ptr [rsp + 0x34], 1
00374EAF  0F 82 08 06 00 00               jb 0x1403754bd
00374EB5  45 8D 4A 02                     lea r9d, [r10 + 2]
00374EB9  48 89 54 24 58                  mov qword ptr [rsp + 0x58], rdx
00374EBE  45 33 C0                        xor r8d, r8d
00374EC1  49 8B CD                        mov rcx, r13
00374EC4  8B F2                           mov esi, edx
00374EC6  E8 95 1D F1 FF                  call 0x140286c60
00374ECB  45 33 D2                        xor r10d, r10d
00374ECE  85 C0                           test eax, eax
00374ED0  0F 88 94 03 00 00               js 0x14037526a
00374ED6  8B 5C 24 60                     mov ebx, dword ptr [rsp + 0x60]
00374EDA  48 83 4D 88 FF                  or qword ptr [rbp - 0x78], 0xffffffffffffffff
00374EDF  83 CB 08                        or ebx, 8
00374EE2  8B 87 84 00 00 00               mov eax, dword ptr [rdi + 0x84]
00374EE8  44 8B 44 24 3C                  mov r8d, dword ptr [rsp + 0x3c]
00374EED  4C 89 6C 24 68                  mov qword ptr [rsp + 0x68], r13
00374EF2  48 89 74 24 70                  mov qword ptr [rsp + 0x70], rsi
00374EF7  48 89 74 24 78                  mov qword ptr [rsp + 0x78], rsi
00374EFC  89 45 80                        mov dword ptr [rbp - 0x80], eax
00374EFF  C7 45 84 04 00 00 00            mov dword ptr [rbp - 0x7c], 4
00374F06  89 5C 24 60                     mov dword ptr [rsp + 0x60], ebx
00374F0A  44 89 45 94                     mov dword ptr [rbp - 0x6c], r8d
00374F0E  41 80 FE 02                     cmp r14b, 2
00374F12  0F 84 AF 05 00 00               je 0x1403754c7
00374F18  8B 87 88 00 00 00               mov eax, dword ptr [rdi + 0x88]
00374F1E  A8 04                           test al, 4
00374F20  0F 84 AD 05 00 00               je 0x1403754d3
00374F26  F6 C3 04                        test bl, 4
00374F29  0F 84 90 03 00 00               je 0x1403752bf
00374F2F  45 8B F2                        mov r14d, r10d
00374F32  F6 C3 04                        test bl, 4
00374F35  0F 84 70 04 00 00               je 0x1403753ab
00374F3B  48 8D 45 00                     lea rax, [rbp]
00374F3F  B9 04 00 00 00                  mov ecx, 4
00374F44  4C 89 50 10                     mov qword ptr [rax + 0x10], r10
00374F48  48 89 40 08                     mov qword ptr [rax + 8], rax
00374F4C  48 89 00                        mov qword ptr [rax], rax
00374F4F  48 83 C0 18                     add rax, 0x18
00374F53  48 83 E9 01                     sub rcx, 1
00374F57  75 EB                           jne 0x140374f44
00374F59  48 8D 45 00                     lea rax, [rbp]
00374F5D  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
00374F61  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00374F6A  48 3B 05 5F 1F C5 00            cmp rax, qword ptr [rip + 0xc51f5f]
00374F71  0F 84 79 05 00 00               je 0x1403754f0
00374F77  8B 4D 94                        mov ecx, dword ptr [rbp - 0x6c]
00374F7A  8B 87 88 00 00 00               mov eax, dword ptr [rdi + 0x88]
00374F80  A8 30                           test al, 0x30
00374F82  0F 85 90 04 00 00               jne 0x140375418
00374F88  BB 01 00 00 00                  mov ebx, 1
00374F8D  89 5C 24 34                     mov dword ptr [rsp + 0x34], ebx
00374F91  45 8B CA                        mov r9d, r10d
00374F94  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00374F98  83 FB 01                        cmp ebx, 1
00374F9B  41 B8 01 00 00 00               mov r8d, 1
00374FA1  48 8B D6                        mov rdx, rsi
00374FA4  41 0F 94 C1                     sete r9b
00374FA8  E8 A3 E3 05 00                  call 0x1403d3350
00374FAD  4C 8D 45 C0                     lea r8, [rbp - 0x40]
00374FB1  33 F6                           xor esi, esi
00374FB3  4C 89 45 A0                     mov qword ptr [rbp - 0x60], r8
00374FB7  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
00374FBC  E8 7B 24 04 00                  call 0x1403b743c
00374FC1  48 83 7D A8 00                  cmp qword ptr [rbp - 0x58], 0
00374FC6  0F 84 32 05 00 00               je 0x1403754fe
00374FCC  45 85 F6                        test r14d, r14d
00374FCF  74 0E                           je 0x140374fdf
00374FD1  41 80 A4 24 AA 05 00 00 FE      and byte ptr [r12 + 0x5aa], 0xfe
00374FDA  83 64 24 38 00                  and dword ptr [rsp + 0x38], 0
00374FDF  4D 85 FF                        test r15, r15
00374FE2  0F 85 33 05 00 00               jne 0x14037551b
00374FE8  8B 97 88 00 00 00               mov edx, dword ptr [rdi + 0x88]
00374FEE  48 8D 4D 00                     lea rcx, [rbp]
00374FF2  C1 EA 04                        shr edx, 4
00374FF5  83 E2 03                        and edx, 3
00374FF8  E8 63 74 12 00                  call 0x14049c460
00374FFD  4C 8B F0                        mov r14, rax
00375000  4C 8D 04 40                     lea r8, [rax + rax*2]
00375004  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0037500E  49 C1 E0 04                     shl r8, 4
00375012  48 8B C8                        mov rcx, rax
00375015  49 03 C8                        add rcx, r8
00375018  BA 01 00 00 00                  mov edx, 1
0037501D  E8 D6 BA 0A 00                  call 0x140420af8
00375022  48 8B CF                        mov rcx, rdi
00375025  E8 3E 94 13 00                  call 0x1404ae468
0037502A  48 8B F0                        mov rsi, rax
0037502D  48 85 C0                        test rax, rax
00375030  0F 84 0B 04 00 00               je 0x140375441
00375036  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
0037503A  89 46 54                        mov dword ptr [rsi + 0x54], eax
0037503D  83 BF 80 00 00 00 08            cmp dword ptr [rdi + 0x80], 8
00375044  0F 85 36 02 00 00               jne 0x140375280
0037504A  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00375053  E8 C8 7F 04 00                  call 0x1403bd020
00375058  8B 4E 5C                        mov ecx, dword ptr [rsi + 0x5c]
0037505B  44 0F B6 C8                     movzx r9d, al
0037505F  41 8B D1                        mov edx, r9d
00375062  C1 E2 03                        shl edx, 3
00375065  33 D1                           xor edx, ecx
00375067  81 E2 F8 01 00 00               and edx, 0x1f8
0037506D  33 D1                           xor edx, ecx
0037506F  83 CA 04                        or edx, 4
00375072  89 56 5C                        mov dword ptr [rsi + 0x5c], edx
00375075  8B 8F 80 00 00 00               mov ecx, dword ptr [rdi + 0x80]
0037507B  41 8B 85 54 45 00 00            mov eax, dword ptr [r13 + 0x4554]
00375082  0F A3 C8                        bt eax, ecx
00375085  0F 82 00 05 00 00               jb 0x14037558b
0037508B  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
00375090  49 8B CE                        mov rcx, r14
00375093  D1 EA                           shr edx, 1
00375095  83 E2 01                        and edx, 1
00375098  4C 89 76 28                     mov qword ptr [rsi + 0x28], r14
0037509C  89 54 24 20                     mov dword ptr [rsp + 0x20], edx
003750A0  49 8B D7                        mov rdx, r15
003750A3  49 8D 47 FF                     lea rax, [r15 - 1]
003750A7  49 03 C6                        add rax, r14
003750AA  48 89 46 30                     mov qword ptr [rsi + 0x30], rax
003750AE  44 8B 87 80 00 00 00            mov r8d, dword ptr [rdi + 0x80]
003750B5  E8 0E 3A 12 00                  call 0x140498ac8
003750BA  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
003750BE  BA 02 00 00 00                  mov edx, 2
003750C3  8B 8F 80 00 00 00               mov ecx, dword ptr [rdi + 0x80]
003750C9  C1 E8 02                        shr eax, 2
003750CC  83 E0 01                        and eax, 1
003750CF  83 F9 04                        cmp ecx, 4
003750D2  0F 86 2F 03 00 00               jbe 0x140375407
003750D8  44 8B E0                        mov r12d, eax
003750DB  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
003750DF  48 B9 00 00 00 00 00 DE FF FF   movabs rcx, 0xffffde0000000000
003750E9  48 8D 1C 40                     lea rbx, [rax + rax*2]
003750ED  48 C1 E3 04                     shl rbx, 4
003750F1  48 8B C1                        mov rax, rcx
003750F4  48 03 D8                        add rbx, rax
003750F7  48 8B 46 30                     mov rax, qword ptr [rsi + 0x30]
003750FB  4C 8D 34 40                     lea r14, [rax + rax*2]
003750FF  49 C1 E6 04                     shl r14, 4
00375103  48 8B C1                        mov rax, rcx
00375106  44 0F B6 6C 24 30               movzx r13d, byte ptr [rsp + 0x30]
0037510C  4C 03 F0                        add r14, rax
0037510F  45 33 D2                        xor r10d, r10d
00375112  44 3A EA                        cmp r13b, dl
00375115  74 15                           je 0x14037512c
00375117  44 0F 20 C1                     mov rcx, cr8
0037511B  44 0F 22 C2                     mov cr8, rdx
0037511F  44 39 15 FA 1B C5 00            cmp dword ptr [rip + 0xc51bfa], r10d
00375126  0F 85 1C 02 00 00               jne 0x140375348
0037512C  49 3B DE                        cmp rbx, r14
0037512F  0F 87 B4 00 00 00               ja 0x1403751e9
00375135  48 83 C3 18                     add rbx, 0x18
00375139  45 8B FA                        mov r15d, r10d
0037513C  F0 48 0F BA 2B 3F               lock bts qword ptr [rbx], 0x3f
00375142  0F 82 02 01 00 00               jb 0x14037524a
00375148  8B 43 08                        mov eax, dword ptr [rbx + 8]
0037514B  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
0037514F  66 44 89 54 24 34               mov word ptr [rsp + 0x34], r10w
00375155  8B 44 24 34                     mov eax, dword ptr [rsp + 0x34]
00375159  89 43 08                        mov dword ptr [rbx + 8], eax
0037515C  F0 44 09 14 24                  lock or dword ptr [rsp], r10d
00375161  8B 15 19 9F C5 00               mov edx, dword ptr [rip + 0xc59f19]
00375167  4C 8D 7B E8                     lea r15, [rbx - 0x18]
0037516B  48 8B 03                        mov rax, qword ptr [rbx]
0037516E  48 C1 E2 3B                     shl rdx, 0x3b
00375172  48 8B CA                        mov rcx, rdx
00375175  48 33 C8                        xor rcx, rax
00375178  48 B8 FF FF FF FF FF FF FF C7   movabs rax, 0xc7ffffffffffffff
00375182  48 23 C8                        and rcx, rax
00375185  48 33 CA                        xor rcx, rdx
00375188  48 8B D7                        mov rdx, rdi
0037518B  48 89 0B                        mov qword ptr [rbx], rcx
0037518E  49 8B CF                        mov rcx, r15
00375191  8B 43 08                        mov eax, dword ptr [rbx + 8]
00375194  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
00375198  C1 E8 10                        shr eax, 0x10
0037519B  24 F8                           and al, 0xf8
0037519D  41 0A C4                        or al, r12b
003751A0  88 44 24 36                     mov byte ptr [rsp + 0x36], al
003751A4  8B 44 24 34                     mov eax, dword ptr [rsp + 0x34]
003751A8  89 43 08                        mov dword ptr [rbx + 8], eax
003751AB  E8 28 07 00 00                  call 0x1403758d8
003751B0  44 8B 8F 80 00 00 00            mov r9d, dword ptr [rdi + 0x80]
003751B7  BA 02 00 00 00                  mov edx, 2
003751BC  45 85 C9                        test r9d, r9d
003751BF  0F 89 C6 00 00 00               jns 0x14037528b
003751C5  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
003751CF  F0 48 21 03                     lock and qword ptr [rbx], rax
003751D3  48 83 C3 30                     add rbx, 0x30
003751D7  48 8D 43 E8                     lea rax, [rbx - 0x18]
003751DB  49 3B C6                        cmp rax, r14
003751DE  0F 86 55 FF FF FF               jbe 0x140375139
003751E4  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
003751E9  44 3A EA                        cmp r13b, dl
003751EC  74 19                           je 0x140375207
003751EE  44 39 15 2B 1B C5 00            cmp dword ptr [rip + 0xc51b2b], r10d
003751F5  74 0C                           je 0x140375203
003751F7  44 0F 20 C1                     mov rcx, cr8
003751FB  41 8A D5                        mov dl, r13b
003751FE  E8 95 04 18 00                  call 0x1404f5698
00375203  45 0F 22 C5                     mov cr8, r13
00375207  48 8B 56 28                     mov rdx, qword ptr [rsi + 0x28]
0037520B  41 B9 01 00 00 00               mov r9d, 1
00375211  8B 8F 80 00 00 00               mov ecx, dword ptr [rdi + 0x80]
00375217  4D 8B C7                        mov r8, r15
0037521A  E8 91 BD F2 FF                  call 0x1402a0fb0
0037521F  F0 FF 87 90 00 00 00            lock inc dword ptr [rdi + 0x90]
00375226  48 8B C6                        mov rax, rsi
00375229  48 8B 4D 60                     mov rcx, qword ptr [rbp + 0x60]
0037522D  48 33 CC                        xor rcx, rsp
00375230  E8 0B 74 33 00                  call 0x1406ac640
00375235  48 81 C4 78 01 00 00            add rsp, 0x178
0037523C  41 5F                           pop r15
0037523E  41 5E                           pop r14
00375240  41 5D                           pop r13
00375242  41 5C                           pop r12
00375244  5F                              pop rdi
00375245  5E                              pop rsi
00375246  5B                              pop rbx
00375247  5D                              pop rbp
00375248  C3                              ret
00375249  CC                              int3
0037524A  41 FF C7                        inc r15d
0037524D  44 85 3D 58 00 C5 00            test dword ptr [rip + 0xc50058], r15d
00375254  0F 84 FF 00 00 00               je 0x140375359
0037525A  F3 90                           pause
0037525C  48 8B 03                        mov rax, qword ptr [rbx]
0037525F  48 85 C0                        test rax, rax
00375262  0F 89 D4 FE FF FF               jns 0x14037513c
00375268  EB E0                           jmp 0x14037524a
0037526A  BB 1E 00 00 00                  mov ebx, 0x1e
0037526F  E8 58 79 04 00                  call 0x1403bcbcc
00375274  48 89 87 B0 00 00 00            mov qword ptr [rdi + 0xb0], rax
0037527B  E9 FF 01 00 00                  jmp 0x14037547f
00375280  8B 56 5C                        mov edx, dword ptr [rsi + 0x5c]
00375283  45 32 C9                        xor r9b, r9b
00375286  E9 EA FD FF FF                  jmp 0x140375075
0037528B  44 3B CA                        cmp r9d, edx
0037528E  0F 84 31 FF FF FF               je 0x1403751c5
00375294  41 83 F9 04                     cmp r9d, 4
00375298  0F 8F 27 FF FF FF               jg 0x1403751c5
0037529E  BA 03 00 00 00                  mov edx, 3
003752A3  49 8B CF                        mov rcx, r15
003752A6  E8 A5 D0 F2 FF                  call 0x1402a2350
003752AB  49 8B CF                        mov rcx, r15
003752AE  E8 AD BE F2 FF                  call 0x1402a1160
003752B3  45 33 D2                        xor r10d, r10d
003752B6  41 8D 52 02                     lea edx, [r10 + 2]
003752BA  E9 06 FF FF FF                  jmp 0x1403751c5
003752BF  41 0F BA E0 11                  bt r8d, 0x11
003752C4  72 76                           jb 0x14037533c
003752C6  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
003752CB  4C 89 54 24 50                  mov qword ptr [rsp + 0x50], r10
003752D0  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
003752D5  4C 89 54 24 48                  mov qword ptr [rsp + 0x48], r10
003752DA  E8 71 0C F8 FF                  call 0x1402f5f50
003752DF  45 33 D2                        xor r10d, r10d
003752E2  84 C0                           test al, al
003752E4  0F 85 9D 00 00 00               jne 0x140375387
003752EA  41 8B C2                        mov eax, r10d
003752ED  4C 89 54 24 50                  mov qword ptr [rsp + 0x50], r10
003752F2  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
003752F7  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
003752FC  48 2B C8                        sub rcx, rax
003752FF  8B 05 1B FD C4 00               mov eax, dword ptr [rip + 0xc4fd1b]
00375305  48 C1 E8 02                     shr rax, 2
00375309  48 3B C8                        cmp rcx, rax
0037530C  0F 82 CD 01 00 00               jb 0x1403754df
00375312  44 0F 20 C0                     mov rax, cr8
00375316  3C 02                           cmp al, 2
00375318  0F 83 C8 01 00 00               jae 0x1403754e6
0037531E  65 4C 8B 24 25 88 01 00 00      mov r12, qword ptr gs:[0x188]
00375327  8B 5C 24 60                     mov ebx, dword ptr [rsp + 0x60]
0037532B  44 8B 44 24 3C                  mov r8d, dword ptr [rsp + 0x3c]
00375330  41 8A 84 24 AA 05 00 00         mov al, byte ptr [r12 + 0x5aa]
00375338  A8 01                           test al, 1
0037533A  74 55                           je 0x140375391
0037533C  83 CB 04                        or ebx, 4
0037533F  89 5C 24 60                     mov dword ptr [rsp + 0x60], ebx
00375343  E9 E7 FB FF FF                  jmp 0x140374f2f
00375348  E8 AF 03 18 00                  call 0x1404f56fc
0037534D  45 33 D2                        xor r10d, r10d
00375350  41 8D 52 02                     lea edx, [r10 + 2]
00375354  E9 D3 FD FF FF                  jmp 0x14037512c
00375359  8B 05 59 17 C5 00               mov eax, dword ptr [rip + 0xc51759]
0037535F  A8 40                           test al, 0x40
00375361  0F 84 F3 FE FF FF               je 0x14037525a
00375367  E8 24 A1 F9 FF                  call 0x14030f490
0037536C  45 33 D2                        xor r10d, r10d
0037536F  84 C0                           test al, al
00375371  0F 84 E3 FE FF FF               je 0x14037525a
00375377  41 8B CF                        mov ecx, r15d
0037537A  E8 E1 A0 F9 FF                  call 0x14030f460
0037537F  45 33 D2                        xor r10d, r10d
00375382  E9 D5 FE FF FF                  jmp 0x14037525c
00375387  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
0037538C  E9 66 FF FF FF                  jmp 0x1403752f7
00375391  0C 01                           or al, 1
00375393  41 BE 01 00 00 00               mov r14d, 1
00375399  41 88 84 24 AA 05 00 00         mov byte ptr [r12 + 0x5aa], al
003753A1  44 89 74 24 38                  mov dword ptr [rsp + 0x38], r14d
003753A6  E9 87 FB FF FF                  jmp 0x140374f32
003753AB  48 8D 05 4E 39 AC 00            lea rax, [rip + 0xac394e]
003753B2  4C 3B E8                        cmp r13, rax
003753B5  0F 84 80 FB FF FF               je 0x140374f3b
003753BB  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
003753C4  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
003753CB  48 8B 05 B6 AC AB 00            mov rax, qword ptr [rip + 0xabacb6]
003753D2  0F B7 91 AE 04 00 00            movzx edx, word ptr [rcx + 0x4ae]
003753D9  4C 39 2C D0                     cmp qword ptr [rax + rdx*8], r13
003753DD  0F 84 58 FB FF FF               je 0x140374f3b
003753E3  4D 8B BD B8 00 00 00            mov r15, qword ptr [r13 + 0xb8]
003753EA  49 8B CF                        mov rcx, r15
003753ED  E8 CE 52 04 00                  call 0x1403ba6c0
003753F2  84 C0                           test al, al
003753F4  0F 85 41 FB FF FF               jne 0x140374f3b
003753FA  83 4C 24 60 04                  or dword ptr [rsp + 0x60], 4
003753FF  4D 8B FA                        mov r15, r10
00375402  E9 34 FB FF FF                  jmp 0x140374f3b
00375407  3B CA                           cmp ecx, edx
00375409  41 BC 01 00 00 00               mov r12d, 1
0037540F  44 0F 44 E0                     cmove r12d, eax
00375413  E9 C3 FC FF FF                  jmp 0x1403750db
00375418  F6 C1 40                        test cl, 0x40
0037541B  74 0F                           je 0x14037542c
0037541D  BB 01 00 00 00                  mov ebx, 1
00375422  44 89 54 24 34                  mov dword ptr [rsp + 0x34], r10d
00375427  E9 65 FB FF FF                  jmp 0x140374f91
0037542C  83 C9 40                        or ecx, 0x40
0037542F  44 88 54 24 31                  mov byte ptr [rsp + 0x31], r10b
00375434  89 4D 94                        mov dword ptr [rbp - 0x6c], ecx
00375437  BB 02 00 00 00                  mov ebx, 2
0037543C  E9 50 FB FF FF                  jmp 0x140374f91
00375441  BB 28 00 00 00                  mov ebx, 0x28
00375446  49 83 FE FF                     cmp r14, -1
0037544A  0F 85 E0 00 00 00               jne 0x140375530
00375450  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
00375455  49 8B CD                        mov rcx, r13
00375458  E8 3F D5 FA FF                  call 0x14032299c
0037545D  45 33 D2                        xor r10d, r10d
00375460  44 39 54 24 38                  cmp dword ptr [rsp + 0x38], r10d
00375465  0F 85 FD 00 00 00               jne 0x140375568
0037546B  4D 85 FF                        test r15, r15
0037546E  0F 85 02 01 00 00               jne 0x140375576
00375474  44 39 54 24 34                  cmp dword ptr [rsp + 0x34], r10d
00375479  0F 85 F0 FD FF FF               jne 0x14037526f
0037547F  8A 4C 24 31                     mov cl, byte ptr [rsp + 0x31]
00375483  84 C9                           test cl, cl
00375485  0F 84 0B 01 00 00               je 0x140375596
0037548B  48 8D 87 98 00 00 00            lea rax, [rdi + 0x98]
00375492  F0 FF 00                        lock inc dword ptr [rax]
00375495  44 8B 4D 94                     mov r9d, dword ptr [rbp - 0x6c]
00375499  8B D3                           mov edx, ebx
0037549B  44 8B 44 24 3C                  mov r8d, dword ptr [rsp + 0x3c]
003754A0  0F B6 C1                        movzx eax, cl
003754A3  48 8B CF                        mov rcx, rdi
003754A6  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
003754AA  E8 B1 55 04 00                  call 0x1403baa60
003754AF  33 C0                           xor eax, eax
003754B1  E9 73 FD FF FF                  jmp 0x140375229
003754B6  BB 0A 00 00 00                  mov ebx, 0xa
003754BB  EB CE                           jmp 0x14037548b
003754BD  BB 14 00 00 00                  mov ebx, 0x14
003754C2  E9 A8 FD FF FF                  jmp 0x14037526f
003754C7  83 CB 10                        or ebx, 0x10
003754CA  89 5C 24 60                     mov dword ptr [rsp + 0x60], ebx
003754CE  E9 45 FA FF FF                  jmp 0x140374f18
003754D3  83 CB 04                        or ebx, 4
003754D6  89 5C 24 60                     mov dword ptr [rsp + 0x60], ebx
003754DA  E9 47 FA FF FF                  jmp 0x140374f26
003754DF  83 CB 04                        or ebx, 4
003754E2  89 5C 24 60                     mov dword ptr [rsp + 0x60], ebx
003754E6  44 8B 44 24 3C                  mov r8d, dword ptr [rsp + 0x3c]
003754EB  E9 3F FA FF FF                  jmp 0x140374f2f
003754F0  41 8B C8                        mov ecx, r8d
003754F3  83 C9 08                        or ecx, 8
003754F6  89 4D 94                        mov dword ptr [rbp - 0x6c], ecx
003754F9  E9 7C FA FF FF                  jmp 0x140374f7a
003754FE  83 65 94 BF                     and dword ptr [rbp - 0x6c], 0xffffffbf
00375502  FF C6                           inc esi
00375504  83 64 24 60 F7                  and dword ptr [rsp + 0x60], 0xfffffff7
00375509  3B F3                           cmp esi, ebx
0037550B  0F 82 A6 FA FF FF               jb 0x140374fb7
00375511  BB 32 00 00 00                  mov ebx, 0x32
00375516  E9 35 FF FF FF                  jmp 0x140375450
0037551B  BA 4D 6D 53 61                  mov edx, 0x61536d4d
00375520  49 8B CF                        mov rcx, r15
00375523  E8 48 D9 FC FF                  call 0x140342e70
00375528  45 33 FF                        xor r15d, r15d
0037552B  E9 B8 FA FF FF                  jmp 0x140374fe8
00375530  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
00375534  49 8B CE                        mov rcx, r14
00375537  8B 97 88 00 00 00               mov edx, dword ptr [rdi + 0x88]
0037553D  C1 E8 02                        shr eax, 2
00375540  F7 D0                           not eax
00375542  83 E0 01                        and eax, 1
00375545  83 C0 0E                        add eax, 0xe
00375548  44 8B C0                        mov r8d, eax
0037554B  41 83 C8 10                     or r8d, 0x10
0037554F  80 7C 24 30 02                  cmp byte ptr [rsp + 0x30], 2
00375554  44 0F 45 C0                     cmovne r8d, eax
00375558  C1 EA 04                        shr edx, 4
0037555B  83 E2 03                        and edx, 3
0037555E  E8 D5 23 00 00                  call 0x140377938
00375563  E9 E8 FE FF FF                  jmp 0x140375450
00375568  41 80 A4 24 AA 05 00 00 FE      and byte ptr [r12 + 0x5aa], 0xfe
00375571  E9 F5 FE FF FF                  jmp 0x14037546b
00375576  BA 4D 6D 53 61                  mov edx, 0x61536d4d
0037557B  49 8B CF                        mov rcx, r15
0037557E  E8 ED D8 FC FF                  call 0x140342e70
00375583  45 33 D2                        xor r10d, r10d
00375586  E9 E9 FE FF FF                  jmp 0x140375474
0037558B  83 CA 02                        or edx, 2
0037558E  89 56 5C                        mov dword ptr [rsi + 0x5c], edx
00375591  E9 F5 FA FF FF                  jmp 0x14037508b
00375596  48 8D 87 9C 00 00 00            lea rax, [rdi + 0x9c]
0037559D  E9 F0 FE FF FF                  jmp 0x140375492
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiCreateSlabEntry(__int64 a1, __int64 a2, int a3, unsigned __int8 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned int v_stack_m124;
    unsigned __int64 v_stack_m130;
    unsigned int v_stack_m134;
    unsigned int v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned int v_stack_m178;
    unsigned int v_stack_m17C;
    unsigned int v_stack_m180;
    unsigned __int8 v_stack_m182;
    unsigned int v_stack_m184;
    unsigned __int8 v_stack_m187;
    unsigned __int8 v_stack_m188;
    unsigned int v_stack_m198;
    unsigned int v_stack_m1B8;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF8;
    unsigned int v_stack_p20;
    unsigned __int8 v_stack_p30;
    unsigned __int8 v_stack_p31;
    unsigned int v_stack_p34;
    unsigned int v_stack_p38;
    unsigned int v_stack_p3C;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned int v_stack_p60;

    v_rsp = (v_rsp) - (376);
    result = (*(unsigned __int64 *)(v_rip + 11098420)) ^ (v_rsp);
    v_stack_m58 = result;
    v_stack_m17C = a3;
    a2 = 0;
    v_stack_m188 = a4;
    result = memset(v_stack_mB8, a2, a2 + 96, a4);
    a2 = 0;
    result = memset(v_stack_m158, a2, a2 + 88, a4);
    result = 0;
    v_stack_mC8 = 0;
    v_r10 = 0;
    v_stack_mC0 = 0;
    result = ((unsigned int)(*(unsigned int *)(a1 + 136))) >> (4);
    result = (unsigned int)((result) & (3));
    v_stack_m187 = 1;
    v_stack_mF8 = v_xmm0;
    v_stack_m180 = 0;
    v_stack_mE8 = v_xmm0;
    v_stack_m178 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 3551726 + result * 8)));
    v_stack_mD8 = v_xmm0;
    if (*(unsigned __int64 *)(a1 + 176) != 0) goto loc_003754B6;
    v_stack_m184 = 1;
    if ((*(unsigned __int64 *)(a2 + 18688)) < 0x420ULL) goto loc_003754BD;
    v_stack_m160 = (unsigned int)(*(unsigned int *)(v_rip - 3551726 + result * 8));
    a3 = 0;
    result = MiAcquireNonPagedResources(0, (unsigned int)(*(unsigned int *)(v_rip - 3551726 + result * 8)), a3, v_r10 + 2);
    v_r10 = 0;
    if (sign_flag) goto loc_0037526A;
    v_rbx = (unsigned int)(((unsigned int)(v_stack_m158)) | (8));
    v_stack_m150 = 0;
    v_stack_m148 = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 3551726 + result * 8))));
    v_stack_m140 = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 3551726 + result * 8))));
    v_stack_m138 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 132)));
    v_stack_m134 = 4;
    v_stack_m158 = (unsigned int)(v_rbx);
    v_stack_m124 = (unsigned int)((unsigned int)(v_stack_m17C));
    if (a4 == 2) goto loc_003754C7;
loc_00374F18:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 136)))) & (4)) == 0) goto loc_003754D3;
loc_00374F26:
    if ((((unsigned __int8)(v_rbx)) & (4)) == 0) goto loc_003752BF;
loc_00374F2F:
loc_00374F32:
    if ((((unsigned __int8)(v_rbx)) & (4)) == 0) goto loc_003753AB;
loc_00374F3B:
loc_00374F44:
    *(unsigned __int64 *)(v_stack_mB8 + 16) = 0;
    *(unsigned __int64 *)(v_stack_mB8 + 8) = v_stack_mB8;
    *(unsigned __int64 *)(v_stack_mB8) = v_stack_mB8;
    result = (v_stack_mB8) + (24);
    a1 = (4) - (1);
    if (condition_is_not_equal) goto loc_00374F44;
    v_stack_m108 = v_stack_mB8;
    if ((*(unsigned __int64 *)(gs_base + (0 + 392))) == (*(unsigned __int64 *)(v_rip + 12918623))) goto loc_003754F0;
loc_00374F7A:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 136)))) & (48)) != 0) goto loc_00375418;
    v_stack_m184 = 1;
loc_00374F91:
    a4 = (1 == 1) ? 1 : 0;
    result = MiInitializeDemandCoalesceContext(v_stack_mF8, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 3551726 + result * 8)))), 1, a4);
    v_rsi = 0;
    v_stack_m118 = v_stack_mF8;
loc_00374FB7:
    result = MiAllocateLargeZeroPages(v_stack_m158, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 3551726 + result * 8)))), v_stack_mF8, a4);
    if (v_stack_m110 == 0) goto loc_003754FE;
    if (0 != 0) {
    }
    if (0 != 0) goto loc_0037551B;
loc_00374FE8:
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 136))) >> (4));
    a2 = (unsigned int)((a2) & (3));
    result = MiPopLargePfnList(v_stack_mB8, a2, v_stack_mF8, a4);
    a3 = (result + result * 2) << (4);
    a1 = (result) + (a3);
    result = MiConvertActiveLargePageToSmall(a1, 1, a3, a4);
    result = MiAllocateSlabEntry(a1, 1, a3, a4);
    if (result == 0) goto loc_00375441;
    *(unsigned int *)(result + 84) = (unsigned int)((unsigned int)(v_stack_m178));
    if ((*(unsigned int *)(a1 + 128)) != 8) goto loc_00375280;
    result = MiGetCurrentSlabIdentity(*(unsigned __int64 *)(gs_base + (0 + 392)), 1, a3, a4);
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned __int8)(result)))) << (3));
    a2 = (unsigned int)((a2) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(result + 92)))));
    a2 = (unsigned int)((a2) & (504));
    a2 = (unsigned int)((a2) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(result + 92)))));
    a2 = (unsigned int)((a2) | (4));
    *(unsigned int *)(result + 92) = (unsigned int)(a2);
loc_00375075:
    if (condition_is_below) goto loc_0037558B;
loc_0037508B:
    a2 = (unsigned int)((a2) >> (1));
    a2 = (unsigned int)((a2) & (1));
    *(unsigned __int64 *)(result + 40) = result;
    v_stack_m198 = (unsigned int)(a2);
    result = (v_stack_m160 - 1) + (result);
    *(unsigned __int64 *)(result + 48) = result;
    result = MiSetSlabTypeIdentifiers(result, v_stack_m160, (unsigned int)(*(unsigned int *)(a1 + 128)), (unsigned __int8)(result));
    result = (unsigned int)(((unsigned int)(v_stack_m158)) >> (2));
    result = (unsigned int)((result) & (1));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 128)))) <= 4) goto loc_00375407;
loc_003750DB:
    v_rbx = (*(unsigned __int64 *)(result + 40) + *(unsigned __int64 *)(result + 40) * 2) << (4);
    v_rbx = (v_rbx) + ((unsigned int)(*(unsigned int *)(a1 + 128)));
    v_r14 = (*(unsigned __int64 *)(result + 48) + *(unsigned __int64 *)(result + 48) * 2) << (4);
    v_r14 = (v_r14) + ((unsigned int)(*(unsigned int *)(a1 + 128)));
    v_r10 = 0;
    if (((unsigned __int8)(v_stack_m188)) == 2) goto loc_0037512C;
    if ((*(unsigned int *)(v_rip + 12917754)) != 0) goto loc_00375348;
loc_0037512C:
    if (v_rbx > v_r14) goto loc_003751E9;
    v_rbx = (v_rbx) + (24);
loc_00375139:
loc_0037513C:
    if (condition_is_below) goto loc_0037524A;
    v_stack_m184 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 8)));
    v_stack_m184 = 0;
    *(unsigned int *)(v_rbx + 8) = (unsigned int)((unsigned int)(v_stack_m184));
    a2 = ((unsigned int)(*(unsigned int *)(v_rip + 12951321))) << (59);
    a1 = (a2) ^ (*(unsigned __int64 *)(v_rbx));
    a1 = (a1) & (*(unsigned __int64 *)(v_rbx));
    a1 = (a1) ^ (a2);
    *(unsigned __int64 *)(v_rbx) = a1;
    v_stack_m184 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 8)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 8))) >> (16));
    result = (unsigned __int8)((result) & (248));
    result = (unsigned __int8)((result) | ((unsigned __int8)((unsigned int)((unsigned int)(result)))));
    v_stack_m182 = (unsigned __int8)(result);
    *(unsigned int *)(v_rbx + 8) = (unsigned int)((unsigned int)(v_stack_m184));
    result = MiReInitializeFreeSlabPfn(v_rbx - 24, a1, (unsigned int)(*(unsigned int *)(a1 + 128)), (unsigned __int8)(result));
    if (!sign_flag) goto loc_0037528B;
loc_003751C5:
    v_rbx = (v_rbx) + (48);
    if ((v_rbx - 24) <= v_r14) goto loc_00375139;
loc_003751E9:
    if (((unsigned __int8)(v_stack_m188)) == 2) goto loc_00375207;
    result = v_rbx - 24;
    if ((*(unsigned int *)(v_rip + 12917547)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)(v_stack_m188);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, (unsigned int)(*(unsigned int *)(a1 + 128)), (unsigned int)(*(unsigned int *)(a1 + 128)));
    }
loc_00375207:
    result = MiUpdateSlabPagePlaceholderState((unsigned int)(*(unsigned int *)(a1 + 128)), *(unsigned __int64 *)(result + 40), v_stack_m160, 1);
loc_00375229:
    a1 = (v_stack_m58) ^ (v_rsp);
    result = _security_check_cookie(a1, *(unsigned __int64 *)(result + 40), v_stack_m160, 1);
    v_rsp = (v_rsp) + (376);
    return result;
loc_0037524A:
    v_r15 = (unsigned int)((v_stack_m160) + 1);
    if (((*(unsigned int *)(v_rip + 12910680)) & ((unsigned int)(v_r15))) == 0) goto loc_00375359;
loc_0037525A:
loc_0037525C:
    if (!sign_flag) goto loc_0037513C;
    goto loc_0037524A;
loc_0037526A:
loc_0037526F:
    result = MiGetSlabCurrentTime(a1, *(unsigned __int64 *)(result + 40), v_stack_m160, 1);
    *(unsigned __int64 *)(a1 + 176) = result;
    goto loc_0037547F;
loc_00375280:
    a4 = 0;
    goto loc_00375075;
loc_0037528B:
    if (0 == ((unsigned int)((unsigned int)(*(unsigned int *)(result + 92))))) goto loc_003751C5;
    if (0 > 4) goto loc_003751C5;
    result = MiSetPfnIdentity(v_r15, 3, v_stack_m160, a4);
    result = MiAbortCombineScan(v_r15, 3, v_stack_m160, a4);
    v_r10 = 0;
    goto loc_003751C5;
loc_003752BF:
    if (condition_is_below) goto loc_0037533C;
    v_stack_p50 = 0;
    v_stack_p48 = 0;
    result = RtlpGetStackLimits(v_stack_p48, v_stack_p50, v_stack_m160, a4);
    v_r10 = 0;
    if ((unsigned __int8)(result) != 0) goto loc_00375387;
    v_stack_p50 = 0;
    v_stack_p48 = 0;
loc_003752F7:
    a1 = (v_stack_p50) - (0);
    result = ((unsigned int)(*(unsigned int *)(v_rip + 12909851))) >> (2);
    if (a1 < result) goto loc_003754DF;
    if (((unsigned __int8)(v_stack_m188)) >= 2) goto loc_003754E6;
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1450))) & (1)) == 0) goto loc_00375391;
loc_0037533C:
    v_rbx = (unsigned int)(((unsigned int)(v_stack_p60)) | (4));
    v_stack_p60 = (unsigned int)(v_rbx);
    goto loc_00374F2F;
loc_00375348:
    result = KiRaiseIrqlProcessIrqlFlags(a1, v_stack_p50, (unsigned int)(v_stack_p3C), a4);
    v_r10 = 0;
    goto loc_0037512C;
loc_00375359:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12916569)))) & (64)) == 0) goto loc_0037525A;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, v_r10 + 2, (unsigned int)(v_stack_p3C), a4);
    v_r10 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_0037525A;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r15)), v_r10 + 2, (unsigned int)(v_stack_p3C), a4);
    v_r10 = 0;
    goto loc_0037525C;
loc_00375387:
    goto loc_003752F7;
loc_00375391:
    result = (unsigned __int8)((v_stack_p48) | (1));
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1450) = (unsigned __int8)(result);
    v_stack_p38 = 1;
    goto loc_00374F32;
loc_003753AB:
    if (v_stack_m188 == (v_rip + 11286862)) goto loc_00374F3B;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11250870) + *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1198) * 8)) == v_stack_m188) goto loc_00374F3B;
    result = PsReferencePartitionSafe(*(unsigned __int64 *)(v_stack_m188 + 184), *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1198), (unsigned int)(v_stack_p3C), a4);
    if ((unsigned __int8)(result) != 0) goto loc_00374F3B;
    goto loc_00374F3B;
loc_00375407:
    v_r12 = 1;
    if (((unsigned int)(*(unsigned __int64 *)(v_stack_m188 + 184))) == ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1198)))) { v_r12 = (unsigned int)(result); }
    goto loc_003750DB;
loc_00375418:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m188 + 184))) & (64)) == 0) goto loc_0037542C;
    v_stack_p34 = 0;
    goto loc_00374F91;
loc_0037542C:
    a1 = (unsigned int)((*(unsigned __int64 *)(v_stack_m188 + 184)) | (64));
    v_stack_p31 = 0;
    v_stack_m124 = (unsigned int)(a1);
    goto loc_00374F91;
loc_00375441:
    if (1 != -1) goto loc_00375530;
loc_00375450:
    result = MiReleaseNonPagedResources(v_stack_m188, v_stack_p58, (unsigned int)(v_stack_p3C), a4);
    v_r10 = 0;
    if (v_stack_p38 != 0) goto loc_00375568;
loc_0037546B:
    if (0 != 0) goto loc_00375576;
loc_00375474:
    if (v_stack_p34 != 0) goto loc_0037526F;
loc_0037547F:
    if ((unsigned __int8)(v_stack_p31) == 0) goto loc_00375596;
loc_0037548B:
loc_00375492:
    v_stack_p20 = (unsigned int)((unsigned __int8)(v_stack_p31));
    result = MiLogSlabEntryAllocateFailure(a1, 40, (unsigned int)(v_stack_p3C), (unsigned int)(v_stack_m124));
    result = 0;
    goto loc_00375229;
loc_003754B6:
    goto loc_0037548B;
loc_003754BD:
    goto loc_0037526F;
loc_003754C7:
    v_rbx = (unsigned int)((20) | (16));
    v_stack_p60 = (unsigned int)(v_rbx);
    goto loc_00374F18;
loc_003754D3:
    v_rbx = (unsigned int)((v_rbx) | (4));
    v_stack_p60 = (unsigned int)(v_rbx);
    goto loc_00374F26;
loc_003754DF:
    v_rbx = (unsigned int)((v_rbx) | (4));
    v_stack_p60 = (unsigned int)(v_rbx);
loc_003754E6:
    goto loc_00374F2F;
loc_003754F0:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_p3C)))) | (8));
    v_stack_m124 = (unsigned int)(a1);
    goto loc_00374F7A;
loc_003754FE:
    v_rsi = (unsigned int)((result) + 1);
    if (((unsigned int)(v_rsi)) < ((unsigned int)(v_rbx))) goto loc_00374FB7;
    goto loc_00375450;
loc_0037551B:
    result = PsDereferencePartition(0, (unsigned int)(0x61536D4DULL), (unsigned int)(v_stack_p3C), (unsigned int)(v_stack_m124));
    v_r15 = 0;
    goto loc_00374FE8;
loc_00375530:
    result = (unsigned int)(((unsigned int)(v_stack_p60)) >> (2));
    result = (unsigned int)(~(result));
    result = (unsigned int)((result) & (1));
    result = (unsigned int)((result) + (14));
    a3 = (unsigned int)(((unsigned int)((unsigned int)(result))) | (16));
    if (v_stack_p30 != 2) { a3 = (unsigned int)(result); }
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 136))) >> (4));
    a2 = (unsigned int)((a2) & (3));
    result = MiFreeLargePageMemory(1, a2, a3, (unsigned int)(v_stack_m124));
    goto loc_00375450;
loc_00375568:
    goto loc_0037546B;
loc_00375576:
    result = PsDereferencePartition(0, (unsigned int)(0x61536D4DULL), a3, (unsigned int)(v_stack_m124));
    v_r10 = 0;
    goto loc_00375474;
loc_0037558B:
    a2 = (unsigned int)(((unsigned int)(0x61536D4DULL)) | (2));
    *(unsigned int *)(v_rsi + 92) = (unsigned int)(a2);
    goto loc_0037508B;
loc_00375596:
    goto loc_00375492;
}
```

## 5. (Beta) C Style

```c
int64_t MiCreateSlabEntry(void *Arg1, void *Arg2, int32_t Arg3, uint8_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint32_t v_stack_m124;
    uint64_t v_stack_m130;
    uint32_t v_stack_m134;
    uint32_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint32_t v_stack_m178;
    uint32_t v_stack_m17C;
    uint32_t v_stack_m180;
    uint8_t v_stack_m182;
    uint32_t v_stack_m184;
    uint8_t v_stack_m187;
    uint8_t v_stack_m188;
    uint32_t v_stack_m198;
    uint32_t v_stack_m1B8;
    uint64_t v_stack_m58;
    uint64_t v_stack_mB8;
    uint32_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF8;
    uint32_t v_stack_p20;
    uint8_t v_stack_p30;
    uint8_t v_stack_p31;
    uint32_t v_stack_p34;
    uint32_t v_stack_p38;
    uint32_t v_stack_p3C;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint32_t v_stack_p60;

    local_rsp = (local_rsp) - (376);
    result = (*(uint64_t *)(v_rip + 0xA95934)) ^ (local_rsp);
    v_stack_m58 = result;
    v_stack_m17C = Arg3;
    Arg2 = 0;
    v_stack_m188 = Arg4;
    result = memset(v_stack_mB8, Arg2, Arg2 + 96, Arg4);
    Arg2 = 0;
    result = memset(v_stack_m158, Arg2, Arg2 + 88, Arg4);
    result = 0;
    v_stack_mC8 = 0;
    local_r10 = 0;
    v_stack_mC0 = 0;
    result = ((uint32_t)(*(uint32_t *)(arg1 + 0x88))) >> (4);
    result = (uint32_t)((result) & (3));
    v_stack_m187 = 1;
    v_stack_mF8 = v_xmm0;
    v_stack_m180 = 0;
    v_stack_mE8 = v_xmm0;
    v_stack_m178 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x3631EE + result * 8)));
    v_stack_mD8 = v_xmm0;
    if (*(uint64_t *)(arg1 + 0xB0) != 0) goto loc_003754B6;
    v_stack_m184 = 1;
    if ((*(uint64_t *)(arg2 + 0x4900)) < 0x420ULL) goto loc_003754BD;
    v_stack_m160 = (uint32_t)(*(uint32_t *)(v_rip - 0x3631EE + result * 8));
    Arg3 = 0;
    result = MiAcquireNonPagedResources(0, (uint32_t)(*(uint32_t *)(v_rip - 0x3631EE + result * 8)), Arg3, local_r10 + 2);
    local_r10 = 0;
    if (sign_flag) goto loc_0037526A;
    local_rbx = (uint32_t)(((uint32_t)(v_stack_m158)) | (8));
    v_stack_m150 = 0;
    v_stack_m148 = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x3631EE + result * 8))));
    v_stack_m140 = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x3631EE + result * 8))));
    v_stack_m138 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x84)));
    v_stack_m134 = 4;
    v_stack_m158 = (uint32_t)(local_rbx);
    v_stack_m124 = (uint32_t)((uint32_t)(v_stack_m17C));
    if (Arg4 == 2) goto loc_003754C7;
loc_00374F18:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x88)))) & (4)) == 0) goto loc_003754D3;
loc_00374F26:
    if ((((uint8_t)(local_rbx)) & (4)) == 0) goto loc_003752BF;
loc_00374F2F:
loc_00374F32:
    if ((((uint8_t)(local_rbx)) & (4)) == 0) goto loc_003753AB;
loc_00374F3B:
loc_00374F44:
    *(uint64_t *)(v_stack_mB8 + 0x10) = 0;
    *(uint64_t *)(v_stack_mB8 + 0x8) = v_stack_mB8;
    *(uint64_t *)(v_stack_mB8) = v_stack_mB8;
    result = (v_stack_mB8) + (24);
    Arg1 = (4) - (1);
    if (condition_is_not_equal) goto loc_00374F44;
    v_stack_m108 = v_stack_mB8;
    if ((*(uint64_t *)(gs_base + (0 + 0x188))) == (*(uint64_t *)(v_rip + 0xC51F5F))) goto loc_003754F0;
loc_00374F7A:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x88)))) & (48)) != 0) goto loc_00375418;
    v_stack_m184 = 1;
loc_00374F91:
    Arg4 = (1 == 1) ? 1 : 0;
    result = MiInitializeDemandCoalesceContext(v_stack_mF8, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x3631EE + result * 8)))), 1, Arg4);
    local_rsi = 0;
    v_stack_m118 = v_stack_mF8;
loc_00374FB7:
    result = MiAllocateLargeZeroPages(v_stack_m158, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x3631EE + result * 8)))), v_stack_mF8, Arg4);
    if (v_stack_m110 == 0) goto loc_003754FE;
    if (0 != 0) {
    }
    if (0 != 0) goto loc_0037551B;
loc_00374FE8:
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x88))) >> (4));
    Arg2 = (uint32_t)((Arg2) & (3));
    result = MiPopLargePfnList(v_stack_mB8, Arg2, v_stack_mF8, Arg4);
    Arg3 = (result + result * 2) << (4);
    Arg1 = (result) + (Arg3);
    result = MiConvertActiveLargePageToSmall(Arg1, 1, Arg3, Arg4);
    result = MiAllocateSlabEntry(Arg1, 1, Arg3, Arg4);
    if (result == 0) goto loc_00375441;
    *(uint32_t *)(result + 0x54) = (uint32_t)((uint32_t)(v_stack_m178));
    if ((*(uint32_t *)(arg1 + 0x80)) != 8) goto loc_00375280;
    result = MiGetCurrentSlabIdentity(*(uint64_t *)(gs_base + (0 + 0x188)), 1, Arg3, Arg4);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint8_t)(result)))) << (3));
    Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x5C)))));
    Arg2 = (uint32_t)((Arg2) & (504));
    Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x5C)))));
    Arg2 = (uint32_t)((Arg2) | (4));
    *(uint32_t *)(result + 0x5C) = (uint32_t)(Arg2);
loc_00375075:
    if (condition_is_below) goto loc_0037558B;
loc_0037508B:
    Arg2 = (uint32_t)((Arg2) >> (1));
    Arg2 = (uint32_t)((Arg2) & (1));
    *(uint64_t *)(result + 0x28) = result;
    v_stack_m198 = (uint32_t)(Arg2);
    result = (v_stack_m160 - 1) + (result);
    *(uint64_t *)(result + 0x30) = result;
    result = MiSetSlabTypeIdentifiers(result, v_stack_m160, (uint32_t)(*(uint32_t *)(arg1 + 0x80)), (uint8_t)(result));
    result = (uint32_t)(((uint32_t)(v_stack_m158)) >> (2));
    result = (uint32_t)((result) & (1));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x80)))) <= 4) goto loc_00375407;
loc_003750DB:
    local_rbx = (*(uint64_t *)(result + 0x28) + *(uint64_t *)(result + 0x28) * 2) << (4);
    local_rbx = (local_rbx) + ((uint32_t)(*(uint32_t *)(arg1 + 0x80)));
    local_r14 = (*(uint64_t *)(result + 0x30) + *(uint64_t *)(result + 0x30) * 2) << (4);
    local_r14 = (local_r14) + ((uint32_t)(*(uint32_t *)(arg1 + 0x80)));
    local_r10 = 0;
    if (((uint8_t)(v_stack_m188)) == 2) goto loc_0037512C;
    if ((*(uint32_t *)(v_rip + 0xC51BFA)) != 0) goto loc_00375348;
loc_0037512C:
    if (local_rbx > local_r14) goto loc_003751E9;
    local_rbx = (local_rbx) + (24);
loc_00375139:
loc_0037513C:
    if (condition_is_below) goto loc_0037524A;
    v_stack_m184 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x8)));
    v_stack_m184 = 0;
    *(uint32_t *)(local_rbx + 0x8) = (uint32_t)((uint32_t)(v_stack_m184));
    Arg2 = ((uint32_t)(*(uint32_t *)(v_rip + 0xC59F19))) << (59);
    Arg1 = (Arg2) ^ (*(uint64_t *)(local_rbx));
    Arg1 = (Arg1) & (*(uint64_t *)(local_rbx));
    Arg1 = (Arg1) ^ (Arg2);
    *(void **)(local_rbx) = Arg1;
    v_stack_m184 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x8)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0x8))) >> (16));
    result = (uint8_t)((result) & (248));
    result = (uint8_t)((result) | ((uint8_t)((uint32_t)((uint32_t)(result)))));
    v_stack_m182 = (uint8_t)(result);
    *(uint32_t *)(local_rbx + 0x8) = (uint32_t)((uint32_t)(v_stack_m184));
    result = MiReInitializeFreeSlabPfn(local_rbx - 24, Arg1, (uint32_t)(*(uint32_t *)(arg1 + 0x80)), (uint8_t)(result));
    if (!sign_flag) goto loc_0037528B;
loc_003751C5:
    local_rbx = (local_rbx) + (48);
    if ((local_rbx - 24) <= local_r14) goto loc_00375139;
loc_003751E9:
    if (((uint8_t)(v_stack_m188)) == 2) goto loc_00375207;
    result = local_rbx - 24;
    if ((*(uint32_t *)(v_rip + 0xC51B2B)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)(v_stack_m188);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, (uint32_t)(*(uint32_t *)(arg1 + 0x80)), (uint32_t)(*(uint32_t *)(arg1 + 0x80)));
    }
loc_00375207:
    result = MiUpdateSlabPagePlaceholderState((uint32_t)(*(uint32_t *)(arg1 + 0x80)), *(uint64_t *)(result + 0x28), v_stack_m160, 1);
loc_00375229:
    Arg1 = (v_stack_m58) ^ (local_rsp);
    result = _security_check_cookie(Arg1, *(uint64_t *)(result + 0x28), v_stack_m160, 1);
    local_rsp = (local_rsp) + (376);
    return result;
loc_0037524A:
    local_r15 = (uint32_t)((v_stack_m160) + 1);
    if (((*(uint32_t *)(v_rip + 0xC50058)) & ((uint32_t)(local_r15))) == 0) goto loc_00375359;
loc_0037525A:
loc_0037525C:
    if (!sign_flag) goto loc_0037513C;
    goto loc_0037524A;
loc_0037526A:
loc_0037526F:
    result = MiGetSlabCurrentTime(Arg1, *(uint64_t *)(result + 0x28), v_stack_m160, 1);
    *(uint64_t *)(arg1 + 0xB0) = result;
    goto loc_0037547F;
loc_00375280:
    Arg4 = 0;
    goto loc_00375075;
loc_0037528B:
    if (0 == ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x5C))))) goto loc_003751C5;
    if (0 > 4) goto loc_003751C5;
    result = MiSetPfnIdentity(local_r15, 3, v_stack_m160, Arg4);
    result = MiAbortCombineScan(local_r15, 3, v_stack_m160, Arg4);
    local_r10 = 0;
    goto loc_003751C5;
loc_003752BF:
    if (condition_is_below) goto loc_0037533C;
    v_stack_p50 = 0;
    v_stack_p48 = 0;
    result = RtlpGetStackLimits(v_stack_p48, v_stack_p50, v_stack_m160, Arg4);
    local_r10 = 0;
    if ((uint8_t)(result) != 0) goto loc_00375387;
    v_stack_p50 = 0;
    v_stack_p48 = 0;
loc_003752F7:
    Arg1 = (v_stack_p50) - (0);
    result = ((uint32_t)(*(uint32_t *)(v_rip + 0xC4FD1B))) >> (2);
    if (Arg1 < result) goto loc_003754DF;
    if (((uint8_t)(v_stack_m188)) >= 2) goto loc_003754E6;
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5AA))) & (1)) == 0) goto loc_00375391;
loc_0037533C:
    local_rbx = (uint32_t)(((uint32_t)(v_stack_p60)) | (4));
    v_stack_p60 = (uint32_t)(local_rbx);
    goto loc_00374F2F;
loc_00375348:
    result = KiRaiseIrqlProcessIrqlFlags(Arg1, v_stack_p50, (uint32_t)(v_stack_p3C), Arg4);
    local_r10 = 0;
    goto loc_0037512C;
loc_00375359:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC51759)))) & (64)) == 0) goto loc_0037525A;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, local_r10 + 2, (uint32_t)(v_stack_p3C), Arg4);
    local_r10 = 0;
    if ((uint8_t)(result) == 0) goto loc_0037525A;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r15)), local_r10 + 2, (uint32_t)(v_stack_p3C), Arg4);
    local_r10 = 0;
    goto loc_0037525C;
loc_00375387:
    goto loc_003752F7;
loc_00375391:
    result = (uint8_t)((v_stack_p48) | (1));
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5AA) = (uint8_t)(result);
    v_stack_p38 = 1;
    goto loc_00374F32;
loc_003753AB:
    if (v_stack_m188 == (v_rip + 11286862)) goto loc_00374F3B;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xABACB6) + *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x4AE) * 8)) == v_stack_m188) goto loc_00374F3B;
    result = PsReferencePartitionSafe(*(uint64_t *)(v_stack_m188 + 0xB8), *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x4AE), (uint32_t)(v_stack_p3C), Arg4);
    if ((uint8_t)(result) != 0) goto loc_00374F3B;
    goto loc_00374F3B;
loc_00375407:
    local_r12 = 1;
    if (((uint32_t)(*(uint64_t *)(v_stack_m188 + 0xB8))) == ((uint32_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x4AE)))) { local_r12 = (uint32_t)(result); }
    goto loc_003750DB;
loc_00375418:
    if ((((uint8_t)(*(uint64_t *)(v_stack_m188 + 0xB8))) & (64)) == 0) goto loc_0037542C;
    v_stack_p34 = 0;
    goto loc_00374F91;
loc_0037542C:
    Arg1 = (uint32_t)((*(uint64_t *)(v_stack_m188 + 0xB8)) | (64));
    v_stack_p31 = 0;
    v_stack_m124 = (uint32_t)(Arg1);
    goto loc_00374F91;
loc_00375441:
    if (1 != -1) goto loc_00375530;
loc_00375450:
    result = MiReleaseNonPagedResources(v_stack_m188, v_stack_p58, (uint32_t)(v_stack_p3C), Arg4);
    local_r10 = 0;
    if (v_stack_p38 != 0) goto loc_00375568;
loc_0037546B:
    if (0 != 0) goto loc_00375576;
loc_00375474:
    if (v_stack_p34 != 0) goto loc_0037526F;
loc_0037547F:
    if ((uint8_t)(v_stack_p31) == 0) goto loc_00375596;
loc_0037548B:
loc_00375492:
    v_stack_p20 = (uint32_t)((uint8_t)(v_stack_p31));
    result = MiLogSlabEntryAllocateFailure(Arg1, 40, (uint32_t)(v_stack_p3C), (uint32_t)(v_stack_m124));
    result = 0;
    goto loc_00375229;
loc_003754B6:
    goto loc_0037548B;
loc_003754BD:
    goto loc_0037526F;
loc_003754C7:
    local_rbx = (uint32_t)((20) | (16));
    v_stack_p60 = (uint32_t)(local_rbx);
    goto loc_00374F18;
loc_003754D3:
    local_rbx = (uint32_t)((local_rbx) | (4));
    v_stack_p60 = (uint32_t)(local_rbx);
    goto loc_00374F26;
loc_003754DF:
    local_rbx = (uint32_t)((local_rbx) | (4));
    v_stack_p60 = (uint32_t)(local_rbx);
loc_003754E6:
    goto loc_00374F2F;
loc_003754F0:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_p3C)))) | (8));
    v_stack_m124 = (uint32_t)(Arg1);
    goto loc_00374F7A;
loc_003754FE:
    local_rsi = (uint32_t)((result) + 1);
    if (((uint32_t)(local_rsi)) < ((uint32_t)(local_rbx))) goto loc_00374FB7;
    goto loc_00375450;
loc_0037551B:
    result = PsDereferencePartition(0, (uint32_t)(0x61536D4DULL), (uint32_t)(v_stack_p3C), (uint32_t)(v_stack_m124));
    local_r15 = 0;
    goto loc_00374FE8;
loc_00375530:
    result = (uint32_t)(((uint32_t)(v_stack_p60)) >> (2));
    result = (uint32_t)(~(result));
    result = (uint32_t)((result) & (1));
    result = (uint32_t)((result) + (14));
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(result))) | (16));
    if (v_stack_p30 != 2) { Arg3 = (uint32_t)(result); }
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x88))) >> (4));
    Arg2 = (uint32_t)((Arg2) & (3));
    result = MiFreeLargePageMemory(1, Arg2, Arg3, (uint32_t)(v_stack_m124));
    goto loc_00375450;
loc_00375568:
    goto loc_0037546B;
loc_00375576:
    result = PsDereferencePartition(0, (uint32_t)(0x61536D4DULL), Arg3, (uint32_t)(v_stack_m124));
    local_r10 = 0;
    goto loc_00375474;
loc_0037558B:
    Arg2 = (uint32_t)(((uint32_t)(0x61536D4DULL)) | (2));
    *(uint32_t *)(local_rsi + 0x5C) = (uint32_t)(Arg2);
    goto loc_0037508B;
loc_00375596:
    goto loc_00375492;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R/W` |
| `Arg1` | `+ 0x80` | `32` | `R` |
| `Arg1` | `+ 0x84` | `32` | `R` |
| `Arg1` | `+ 0x88` | `32` | `R` |
| `Arg1` | `+ 0x90` | `32` | `R/W` |
| `Arg1` | `+ 0x98` | `64` | `R` |
| `Arg1` | `+ 0x9C` | `64` | `R` |
| `Arg1` | `+ 0xB0` | `64` | `R` |
| `Arg1` | `+ 0xB0` | `64` | `W` |
| `Arg2` | `+ 0x4900` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00374DEC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
