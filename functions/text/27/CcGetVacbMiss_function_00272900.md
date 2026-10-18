# CcGetVacbMiss

- RVA: `0x00272900`–`0x0027308C` (길이 `1,932` bytes)
- VA: `0x0000000140272900`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00065C90`
- 디코드: `467`개 명령, `1,932/1,932` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **37**; 고유 호출 대상: **24**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **13**

### Outgoing calls
- `0x002729F8` → [KiAcquireQueuedSpinLockInstrumented](KiAcquireQueuedSpinLockInstrumented_function_00275850.md) (function, `0x00275850`)
- `0x00272A7D` → [KeReleaseInStackQueuedSpinLockFromDpcLevel](../21/KeReleaseInStackQueuedSpinLockFromDpcLevel_function_002171B0.md) (function, `0x002171B0`)
- `0x00272A92` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00272AEA` → [MmMapViewInSystemCache](MmMapViewInSystemCache_function_00273094.md) (function, `0x00273094`)
- `0x00272AFD` → [ExAcquireFastMutex](../20/ExAcquireFastMutex_function_0020E5A0.md) (function, `0x0020E5A0`)
- `0x00272B0B` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00272B27` → [ExfAcquirePushLockExclusiveEx](../20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00272BA6` → [CcSetVacbLargeOffset](CcSetVacbLargeOffset_function_002733D0.md) (function, `0x002733D0`)
- `0x00272C55` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00272C6B` → [ExReleaseFastMutex](../25/ExReleaseFastMutex_function_002519C0.md) (function, `0x002519C0`)
- `0x00272C80` → [CcReleaseBcbLockAndVacbLock](../2D/CcReleaseBcbLockAndVacbLock_function_002DFDF0.md) (function, `0x002DFDF0`)
- `0x00272CA1` → [KeAcquireQueuedSpinLock](KeAcquireQueuedSpinLock_function_00273D80.md) (function, `0x00273D80`)
- `0x00272CB5` → [CcSetVacbInFreeList](../26/CcSetVacbInFreeList_function_0026FBB0.md) (function, `0x0026FBB0`)
- `0x00272CC2` → [KeReleaseQueuedSpinLock](KeReleaseQueuedSpinLock_function_00272540.md) (function, `0x00272540`)
- `0x00272CC9` → [FsRtlIsNtstatusExpected](../26/FsRtlIsNtstatusExpected_function_0026D390.md) (function, `0x0026D390`)
- `0x00272D96` → [CcUnmapInactiveViewsInternal](CcUnmapInactiveViewsInternal_function_0027174C.md) (function, `0x0027174C`)
- `0x00272DA4` → [KeAcquireQueuedSpinLock](KeAcquireQueuedSpinLock_function_00273D80.md) (function, `0x00273D80`)
- `0x00272DB3` → [CcGetVacbFromFreeList](CcGetVacbFromFreeList_function_00271630.md) (function, `0x00271630`)
- `0x00272DC3` → [KeReleaseQueuedSpinLock](KeReleaseQueuedSpinLock_function_00272540.md) (function, `0x00272540`)
- `0x00272E22` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00272E30` → [ExfReleasePushLock](../26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x00272E3D` → [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x00272E60` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00272EC7` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00272EDC` → [ExReleaseFastMutex](../25/ExReleaseFastMutex_function_002519C0.md) (function, `0x002519C0`)
- `0x00272EEA` → [CcUnmapVacb](../../page/9E/CcUnmapVacb_function_009E9600.md) (function, `0x009E9600`)
- `0x00272EF4` → [KeAcquireQueuedSpinLock](KeAcquireQueuedSpinLock_function_00273D80.md) (function, `0x00273D80`)
- `0x00272F69` → [KeReleaseInStackQueuedSpinLockFromDpcLevel](../21/KeReleaseInStackQueuedSpinLockFromDpcLevel_function_002171B0.md) (function, `0x002171B0`)
- `0x00272F7D` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00272F92` → [ExfReleasePushLock](../26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x00272FD3` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00272FE8` → [CcSetVacbIntoList](../26/CcSetVacbIntoList_function_0026E524.md) (function, `0x0026E524`)
- `0x00273016` → [CcUnmapVacb](../../page/9E/CcUnmapVacb_function_009E9600.md) (function, `0x009E9600`)
- `0x00273042` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00273060` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00273068` → [RtlRaiseStatus](../2F/RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)
- `0x00273086` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [CcGetVirtualAddress](../34/CcGetVirtualAddress_function_00340C9C.md) at `0x00340F0C`

### Static image references
- `0x00272968` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x00272986` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x002729D2` → RVA `0x00E65B8C` (`.data`; read/write)
- `0x002729EE` → RVA `0x00F0DE58` (`.data`; read)
- `0x00272A4C` → RVA `0x00F8F4A0` (`.data`; read)
- `0x00272D6D` → RVA `0x00E65B50` (`.data`; read)
- `0x00272D76` → RVA `0x00E65B8C` (`.data`; read)
- `0x00272F10` → RVA `0x00F8F4C0` (`.data`; read)
- `0x00272F37` → RVA `0x00F8F4C0` (`.data`; write)
- `0x00272F56` → RVA `0x00F8F4A8` (`.data`; read/write)
- `0x00272FA3` → RVA `0x00F8F4A8` (`.data`; read)
- `0x00272FAF` → RVA `0x00F8F4AC` (`.data`; read/write)
- `0x00272FFD` → RVA `0x00F8F4B0` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00272EEA` → [CcUnmapVacb](../../page/9E/CcUnmapVacb_function_009E9600.md) (`.text` → `PAGE`)
  - `0x00273016` → [CcUnmapVacb](../../page/9E/CcUnmapVacb_function_009E9600.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00272900  4C 8B DC                        mov r11, rsp
00272903  45 89 4B 20                     mov dword ptr [r11 + 0x20], r9d
00272907  45 89 43 18                     mov dword ptr [r11 + 0x18], r8d
0027290B  53                              push rbx
0027290C  55                              push rbp
0027290D  56                              push rsi
0027290E  57                              push rdi
0027290F  41 54                           push r12
00272911  41 55                           push r13
00272913  41 56                           push r14
00272915  41 57                           push r15
00272917  48 83 EC 48                     sub rsp, 0x48
0027291B  48 8B A9 18 02 00 00            mov rbp, qword ptr [rcx + 0x218]
00272922  33 C0                           xor eax, eax
00272924  44 8B E8                        mov r13d, eax
00272927  49 89 53 10                     mov qword ptr [r11 + 0x10], rdx
0027292B  8B C2                           mov eax, edx
0027292D  48 89 6C 24 30                  mov qword ptr [rsp + 0x30], rbp
00272932  25 FF FF 03 00                  and eax, 0x3ffff
00272937  40 32 FF                        xor dil, dil
0027293A  2B D0                           sub edx, eax
0027293C  45 8B F9                        mov r15d, r9d
0027293F  41 89 53 10                     mov dword ptr [r11 + 0x10], edx
00272943  45 8B F0                        mov r14d, r8d
00272946  48 8B F1                        mov rsi, rcx
00272949  41 BC 01 00 00 00               mov r12d, 1
0027294F  B8 02 00 00 00                  mov eax, 2
00272954  40 88 BC 24 90 00 00 00         mov byte ptr [rsp + 0x90], dil
0027295C  0F 1F 40 00                     nop dword ptr [rax]
00272960  44 0F 20 C3                     mov rbx, cr8
00272964  44 0F 22 C0                     mov cr8, rax
00272968  83 3D B1 43 D5 00 00            cmp dword ptr [rip + 0xd543b1], 0
0027296F  0F 85 A8 04 00 00               jne 0x140272e1d
00272975  65 48 8B 0C 25 28 00 00 00      mov rcx, qword ptr gs:[0x28]
0027297E  48 8B 51 48                     mov rdx, qword ptr [rcx + 0x48]
00272982  48 83 C1 40                     add rcx, 0x40
00272986  F6 05 79 41 D5 00 21            test byte ptr [rip + 0xd54179], 0x21
0027298D  75 5F                           jne 0x1402729ee
0027298F  48 8B C1                        mov rax, rcx
00272992  48 87 02                        xchg qword ptr [rdx], rax
00272995  48 85 C0                        test rax, rax
00272998  0F 85 9C 04 00 00               jne 0x140272e3a
0027299E  40 84 FF                        test dil, dil
002729A1  0F 84 F5 05 00 00               je 0x140272f9c
002729A7  41 83 CD 02                     or r13d, 2
002729AB  48 8D 8D D0 04 00 00            lea rcx, [rbp + 0x4d0]
002729B2  4C 8D 85 E0 04 00 00            lea r8, [rbp + 0x4e0]
002729B9  48 8B 01                        mov rax, qword ptr [rcx]
002729BC  45 33 C9                        xor r9d, r9d
002729BF  41 8B F9                        mov edi, r9d
002729C2  48 3B C1                        cmp rax, rcx
002729C5  0F 84 A5 00 00 00               je 0x140272a70
002729CB  48 8B 10                        mov rdx, qword ptr [rax]
002729CE  48 8D 78 F0                     lea rdi, [rax - 0x10]
002729D2  FF 05 B4 31 BF 00               inc dword ptr [rip + 0xbf31b4]
002729D8  48 39 42 08                     cmp qword ptr [rdx + 8], rax
002729DC  75 09                           jne 0x1402729e7
002729DE  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
002729E2  48 39 01                        cmp qword ptr [rcx], rax
002729E5  74 18                           je 0x1402729ff
002729E7  B9 03 00 00 00                  mov ecx, 3
002729EC  CD 29                           int 0x29
002729EE  8B 05 64 B4 C9 00               mov eax, dword ptr [rip + 0xc9b464]
002729F4  85 C0                           test eax, eax
002729F6  75 97                           jne 0x14027298f
002729F8  E8 53 2E 00 00                  call 0x140275850
002729FD  EB 9F                           jmp 0x14027299e
002729FF  48 89 11                        mov qword ptr [rcx], rdx
00272A02  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
00272A06  41 8B 00                        mov eax, dword ptr [r8]
00272A09  41 3B C4                        cmp eax, r12d
00272A0C  0F 82 36 06 00 00               jb 0x140273048
00272A12  FF C8                           dec eax
00272A14  48 BA CD CC CC CC CC CC CC CC   movabs rdx, 0xcccccccccccccccd
00272A1E  41 89 00                        mov dword ptr [r8], eax
00272A21  48 8B C7                        mov rax, rdi
00272A24  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
00272A28  48 2B C1                        sub rax, rcx
00272A2B  48 83 E8 10                     sub rax, 0x10
00272A2F  48 C1 F8 03                     sar rax, 3
00272A33  48 0F AF C2                     imul rax, rdx
00272A37  3B 41 08                        cmp eax, dword ptr [rcx + 8]
00272A3A  76 03                           jbe 0x140272a3f
00272A3C  89 41 08                        mov dword ptr [rcx + 8], eax
00272A3F  48 83 3F 00                     cmp qword ptr [rdi], 0
00272A43  75 23                           jne 0x140272a68
00272A45  48 8B 47 20                     mov rax, qword ptr [rdi + 0x20]
00272A49  44 8B 00                        mov r8d, dword ptr [rax]
00272A4C  48 8B 05 4D CA D1 00            mov rax, qword ptr [rip + 0xd1ca4d]
00272A53  4A 8B 14 C0                     mov rdx, qword ptr [rax + r8*8]
00272A57  48 85 D2                        test rdx, rdx
00272A5A  74 0C                           je 0x140272a68
00272A5C  FF 42 04                        inc dword ptr [rdx + 4]
00272A5F  44 39 02                        cmp dword ptr [rdx], r8d
00272A62  0F 85 C2 05 00 00               jne 0x14027302a
00272A68  48 C7 47 08 FF FF FF FF         mov qword ptr [rdi + 8], 0xffffffffffffffff
00272A70  65 48 8B 0C 25 28 00 00 00      mov rcx, qword ptr gs:[0x28]
00272A79  48 83 C1 40                     add rcx, 0x40
00272A7D  E8 2E 47 FA FF                  call 0x1402171b0
00272A82  83 3D 97 42 D5 00 00            cmp dword ptr [rip + 0xd54297], 0
00272A89  74 0C                           je 0x140272a97
00272A8B  44 0F 20 C1                     mov rcx, cr8
00272A8F  0F B6 D3                        movzx edx, bl
00272A92  E8 01 2C 28 00                  call 0x1404f5698
00272A97  0F B6 C3                        movzx eax, bl
00272A9A  44 0F 22 C0                     mov cr8, rax
00272A9E  48 85 FF                        test rdi, rdi
00272AA1  0F 84 BD 02 00 00               je 0x140272d64
00272AA7  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
00272AAB  48 2B 8C 24 98 00 00 00         sub rcx, qword ptr [rsp + 0x98]
00272AB3  48 8B C1                        mov rax, rcx
00272AB6  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00272ABB  48 C1 E8 20                     shr rax, 0x20
00272ABF  85 C0                           test eax, eax
00272AC1  75 08                           jne 0x140272acb
00272AC3  81 F9 00 00 04 00               cmp ecx, 0x40000
00272AC9  76 08                           jbe 0x140272ad3
00272ACB  C7 44 24 38 00 00 04 00         mov dword ptr [rsp + 0x38], 0x40000
00272AD3  48 8B 8E B0 00 00 00            mov rcx, qword ptr [rsi + 0xb0]
00272ADA  4C 8D 4C 24 38                  lea r9, [rsp + 0x38]
00272ADF  4C 8D 84 24 98 00 00 00         lea r8, [rsp + 0x98]
00272AE7  48 8B D7                        mov rdx, rdi
00272AEA  E8 A5 05 00 00                  call 0x140273094
00272AEF  8B E8                           mov ebp, eax
00272AF1  45 85 F6                        test r14d, r14d
00272AF4  74 0C                           je 0x140272b02
00272AF6  48 8D 8E 20 01 00 00            lea rcx, [rsi + 0x120]
00272AFD  E8 9E BA F9 FF                  call 0x14020e5a0
00272B02  45 33 C0                        xor r8d, r8d
00272B05  48 8D 4E 68                     lea rcx, [rsi + 0x68]
00272B09  33 D2                           xor edx, edx
00272B0B  E8 20 D7 F9 FF                  call 0x140210230
00272B10  F0 48 0F BA 6E 68 00            lock bts qword ptr [rsi + 0x68], 0
00272B17  48 8B D8                        mov rbx, rax
00272B1A  73 10                           jae 0x140272b2c
00272B1C  4C 8D 46 68                     lea r8, [rsi + 0x68]
00272B20  48 8B D0                        mov rdx, rax
00272B23  48 8D 4E 68                     lea rcx, [rsi + 0x68]
00272B27  E8 64 D1 F9 FF                  call 0x14020fc90
00272B2C  48 85 DB                        test rbx, rbx
00272B2F  74 04                           je 0x140272b35
00272B31  44 88 63 0A                     mov byte ptr [rbx + 0xa], r12b
00272B35  4C 8B 4E 20                     mov r9, qword ptr [rsi + 0x20]
00272B39  4C 8B 7E 58                     mov r15, qword ptr [rsi + 0x58]
00272B3D  48 8B 9C 24 98 00 00 00         mov rbx, qword ptr [rsp + 0x98]
00272B45  49 81 F9 00 00 00 02            cmp r9, 0x2000000
00272B4C  0F 8F A5 01 00 00               jg 0x140272cf7
00272B52  8B 84 24 98 00 00 00            mov eax, dword ptr [rsp + 0x98]
00272B59  48 C1 E8 12                     shr rax, 0x12
00272B5D  4D 8B 3C C7                     mov r15, qword ptr [r15 + rax*8]
00272B61  4D 85 FF                        test r15, r15
00272B64  0F 85 FC 02 00 00               jne 0x140272e66
00272B6A  85 ED                           test ebp, ebp
00272B6C  0F 88 00 01 00 00               js 0x140272c72
00272B72  41 0F B6 D4                     movzx edx, r12b
00272B76  49 81 F9 00 00 00 02            cmp r9, 0x2000000
00272B7D  7F 1B                           jg 0x140272b9a
00272B7F  48 83 FF FE                     cmp rdi, -2
00272B83  73 29                           jae 0x140272bae
00272B85  8B 8C 24 98 00 00 00            mov ecx, dword ptr [rsp + 0x98]
00272B8C  48 8B 46 58                     mov rax, qword ptr [rsi + 0x58]
00272B90  48 C1 E9 12                     shr rcx, 0x12
00272B94  48 89 3C C8                     mov qword ptr [rax + rcx*8], rdi
00272B98  EB 1A                           jmp 0x140272bb4
00272B9A  45 33 C9                        xor r9d, r9d
00272B9D  4C 8B C7                        mov r8, rdi
00272BA0  48 8B D3                        mov rdx, rbx
00272BA3  48 8B CE                        mov rcx, rsi
00272BA6  E8 25 08 00 00                  call 0x1402733d0
00272BAB  0F B6 D0                        movzx edx, al
00272BAE  48 83 FF FD                     cmp rdi, -3
00272BB2  77 0F                           ja 0x140272bc3
00272BB4  F0 FF 86 24 02 00 00            lock inc dword ptr [rsi + 0x224]
00272BBB  48 8B 9C 24 98 00 00 00         mov rbx, qword ptr [rsp + 0x98]
00272BC3  84 D2                           test dl, dl
00272BC5  0F 84 3D 04 00 00               je 0x140273008
00272BCB  48 83 7F 08 FF                  cmp qword ptr [rdi + 8], -1
00272BD0  0F 85 E4 03 00 00               jne 0x140272fba
00272BD6  48 89 77 08                     mov qword ptr [rdi + 8], rsi
00272BDA  48 89 5F 10                     mov qword ptr [rdi + 0x10], rbx
00272BDE  F0 44 0F C1 67 10               lock xadd dword ptr [rdi + 0x10], r12d
00272BE4  41 FF C4                        inc r12d
00272BE7  66 45 85 E4                     test r12w, r12w
00272BEB  0F 84 56 02 00 00               je 0x140272e47
00272BF1  66 41 83 FC 01                  cmp r12w, 1
00272BF6  75 07                           jne 0x140272bff
00272BF8  F0 FF 86 28 02 00 00            lock inc dword ptr [rsi + 0x228]
00272BFF  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
00272C07  48 3B 86 78 01 00 00            cmp rax, qword ptr [rsi + 0x178]
00272C0E  7C 0D                           jl 0x140272c1d
00272C10  48 05 00 00 04 00               add rax, 0x40000
00272C16  48 89 86 78 01 00 00            mov qword ptr [rsi + 0x178], rax
00272C1D  0F 0D 4E 68                     prefetchw byte ptr [rsi + 0x68]
00272C21  48 8B 46 68                     mov rax, qword ptr [rsi + 0x68]
00272C25  48 8B C8                        mov rcx, rax
00272C28  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
00272C2C  48 83 F9 10                     cmp rcx, 0x10
00272C30  B9 00 00 00 00                  mov ecx, 0
00272C35  48 8D 50 F0                     lea rdx, [rax - 0x10]
00272C39  48 0F 46 D1                     cmovbe rdx, rcx
00272C3D  A8 02                           test al, 2
00272C3F  0F 85 E7 01 00 00               jne 0x140272e2c
00272C45  F0 48 0F B1 56 68               lock cmpxchg qword ptr [rsi + 0x68], rdx
00272C4B  0F 85 DB 01 00 00               jne 0x140272e2c
00272C51  48 8D 4E 68                     lea rcx, [rsi + 0x68]
00272C55  E8 A6 E9 06 00                  call 0x1402e1600
00272C5A  83 BC 24 A0 00 00 00 00         cmp dword ptr [rsp + 0xa0], 0
00272C62  74 7E                           je 0x140272ce2
00272C64  48 8D 8E 20 01 00 00            lea rcx, [rsi + 0x120]
00272C6B  E8 50 ED FD FF                  call 0x1402519c0
00272C70  EB 70                           jmp 0x140272ce2
00272C72  44 8B B4 24 A0 00 00 00         mov r14d, dword ptr [rsp + 0xa0]
00272C7A  48 8B D6                        mov rdx, rsi
00272C7D  41 8B CE                        mov ecx, r14d
00272C80  E8 6B D1 06 00                  call 0x1402dfdf0
00272C85  44 0F B6 BC 24 90 00 00 00      movzx r15d, byte ptr [rsp + 0x90]
00272C8E  45 84 FF                        test r15b, r15b
00272C91  0F 85 18 03 00 00               jne 0x140272faf
00272C97  33 C0                           xor eax, eax
00272C99  48 89 07                        mov qword ptr [rdi], rax
00272C9C  B9 04 00 00 00                  mov ecx, 4
00272CA1  E8 DA 10 00 00                  call 0x140273d80
00272CA6  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00272CAB  45 0F B6 C7                     movzx r8d, r15b
00272CAF  48 8B D7                        mov rdx, rdi
00272CB2  0F B6 D8                        movzx ebx, al
00272CB5  E8 F6 CE FF FF                  call 0x14026fbb0
00272CBA  0F B6 D3                        movzx edx, bl
00272CBD  B9 04 00 00 00                  mov ecx, 4
00272CC2  E8 79 F8 FF FF                  call 0x140272540
00272CC7  8B CD                           mov ecx, ebp
00272CC9  E8 C2 A6 FF FF                  call 0x14026d390
00272CCE  84 C0                           test al, al
00272CD0  0F 84 4A 03 00 00               je 0x140273020
00272CD6  33 C0                           xor eax, eax
00272CD8  8B F8                           mov edi, eax
00272CDA  85 ED                           test ebp, ebp
00272CDC  0F 88 13 01 00 00               js 0x140272df5
00272CE2  48 8B C7                        mov rax, rdi
00272CE5  48 83 C4 48                     add rsp, 0x48
00272CE9  41 5F                           pop r15
00272CEB  41 5E                           pop r14
00272CED  41 5D                           pop r13
00272CEF  41 5C                           pop r12
00272CF1  5F                              pop rdi
00272CF2  5E                              pop rsi
00272CF3  5D                              pop rbp
00272CF4  5B                              pop rbx
00272CF5  C3                              ret
00272CF6  CC                              int3
00272CF7  33 C0                           xor eax, eax
00272CF9  4C 8B D3                        mov r10, rbx
00272CFC  8B D0                           mov edx, eax
00272CFE  B9 19 00 00 00                  mov ecx, 0x19
00272D03  44 8B C1                        mov r8d, ecx
00272D06  49 8B C4                        mov rax, r12
00272D09  83 C1 07                        add ecx, 7
00272D0C  FF C2                           inc edx
00272D0E  48 D3 E0                        shl rax, cl
00272D11  4C 3B C8                        cmp r9, rax
00272D14  7F ED                           jg 0x140272d03
00272D16  48 8B C3                        mov rax, rbx
00272D19  41 8B C8                        mov ecx, r8d
00272D1C  48 D3 F8                        sar rax, cl
00272D1F  4D 8B 3C C7                     mov r15, qword ptr [r15 + rax*8]
00272D23  4D 85 FF                        test r15, r15
00272D26  0F 84 3E FE FF FF               je 0x140272b6a
00272D2C  0F 1F 40 00                     nop dword ptr [rax]
00272D30  85 D2                           test edx, edx
00272D32  0F 84 29 FE FF FF               je 0x140272b61
00272D38  41 8B C8                        mov ecx, r8d
00272D3B  49 8B C4                        mov rax, r12
00272D3E  48 D3 E0                        shl rax, cl
00272D41  41 83 C0 F9                     add r8d, -7
00272D45  48 FF C8                        dec rax
00272D48  41 8B C8                        mov ecx, r8d
00272D4B  4C 23 D0                        and r10, rax
00272D4E  FF CA                           dec edx
00272D50  49 8B C2                        mov rax, r10
00272D53  48 D3 F8                        sar rax, cl
00272D56  4D 8B 3C C7                     mov r15, qword ptr [r15 + rax*8]
00272D5A  4D 85 FF                        test r15, r15
00272D5D  75 D1                           jne 0x140272d30
00272D5F  E9 FD FD FF FF                  jmp 0x140272b61
00272D64  44 0F B6 BC 24 90 00 00 00      movzx r15d, byte ptr [rsp + 0x90]
00272D6D  83 3D DC 2D BF 00 00            cmp dword ptr [rip + 0xbf2ddc], 0
00272D74  74 57                           je 0x140272dcd
00272D76  83 3D 0F 2E BF 00 00            cmp dword ptr [rip + 0xbf2e0f], 0
00272D7D  74 4E                           je 0x140272dcd
00272D7F  48 8B 45 08                     mov rax, qword ptr [rbp + 8]
00272D83  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00272D87  48 85 C9                        test rcx, rcx
00272D8A  74 41                           je 0x140272dcd
00272D8C  45 33 C9                        xor r9d, r9d
00272D8F  45 33 C0                        xor r8d, r8d
00272D92  41 8D 51 40                     lea edx, [r9 + 0x40]
00272D96  E8 B1 E9 FF FF                  call 0x14027174c
00272D9B  85 C0                           test eax, eax
00272D9D  74 2E                           je 0x140272dcd
00272D9F  B9 04 00 00 00                  mov ecx, 4
00272DA4  E8 D7 0F 00 00                  call 0x140273d80
00272DA9  41 0F B6 D7                     movzx edx, r15b
00272DAD  48 8B CD                        mov rcx, rbp
00272DB0  0F B6 D8                        movzx ebx, al
00272DB3  E8 78 E8 FF FF                  call 0x140271630
00272DB8  0F B6 D3                        movzx edx, bl
00272DBB  B9 04 00 00 00                  mov ecx, 4
00272DC0  48 8B F8                        mov rdi, rax
00272DC3  E8 78 F7 FF FF                  call 0x140272540
00272DC8  48 85 FF                        test rdi, rdi
00272DCB  74 A0                           je 0x140272d6d
00272DCD  44 8B BC 24 A8 00 00 00         mov r15d, dword ptr [rsp + 0xa8]
00272DD5  48 85 FF                        test rdi, rdi
00272DD8  0F 85 C9 FC FF FF               jne 0x140272aa7
00272DDE  45 3B FC                        cmp r15d, r12d
00272DE1  0F 84 16 02 00 00               je 0x140272ffd
00272DE7  44 0F B6 BC 24 90 00 00 00      movzx r15d, byte ptr [rsp + 0x90]
00272DF0  BD 9A 00 00 C0                  mov ebp, 0xc000009a
00272DF5  45 84 FF                        test r15b, r15b
00272DF8  0F 85 68 02 00 00               jne 0x140273066
00272DFE  44 8B BC 24 A8 00 00 00         mov r15d, dword ptr [rsp + 0xa8]
00272E06  45 3B FC                        cmp r15d, r12d
00272E09  0F 85 57 02 00 00               jne 0x140273066
00272E0F  48 8B 6C 24 30                  mov rbp, qword ptr [rsp + 0x30]
00272E14  41 0F B6 FC                     movzx edi, r12b
00272E18  E9 32 FB FF FF                  jmp 0x14027294f
00272E1D  B2 02                           mov dl, 2
00272E1F  0F B6 CB                        movzx ecx, bl
00272E22  E8 D5 28 28 00                  call 0x1404f56fc
00272E27  E9 49 FB FF FF                  jmp 0x140272975
00272E2C  48 8D 4E 68                     lea rcx, [rsi + 0x68]
00272E30  E8 9B 0A FF FF                  call 0x1402638d0
00272E35  E9 17 FE FF FF                  jmp 0x140272c51
00272E3A  48 8B D0                        mov rdx, rax
00272E3D  E8 6E 50 FE FF                  call 0x140257eb0
00272E42  E9 57 FB FF FF                  jmp 0x14027299e
00272E47  33 C0                           xor eax, eax
00272E49  45 33 C9                        xor r9d, r9d
00272E4C  BA AC 0B 00 00                  mov edx, 0xbac
00272E51  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00272E56  49 C7 C0 20 04 00 C0            mov r8, 0xffffffffc0000420
00272E5D  8D 48 34                        lea ecx, [rax + 0x34]
00272E60  E8 FB A7 28 00                  call 0x1404fd660
00272E65  CC                              int3
00272E66  85 ED                           test ebp, ebp
00272E68  0F 88 04 FE FF FF               js 0x140272c72
00272E6E  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
00272E72  F0 45 0F C1 67 10               lock xadd dword ptr [r15 + 0x10], r12d
00272E78  41 FF C4                        inc r12d
00272E7B  66 45 85 E4                     test r12w, r12w
00272E7F  74 C6                           je 0x140272e47
00272E81  66 41 83 FC 01                  cmp r12w, 1
00272E86  75 07                           jne 0x140272e8f
00272E88  F0 FF 80 28 02 00 00            lock inc dword ptr [rax + 0x228]
00272E8F  0F 0D 4E 68                     prefetchw byte ptr [rsi + 0x68]
00272E93  48 8B 46 68                     mov rax, qword ptr [rsi + 0x68]
00272E97  BD 00 00 00 00                  mov ebp, 0
00272E9C  48 8B C8                        mov rcx, rax
00272E9F  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
00272EA3  48 83 F9 10                     cmp rcx, 0x10
00272EA7  48 8D 50 F0                     lea rdx, [rax - 0x10]
00272EAB  48 0F 46 D5                     cmovbe rdx, rbp
00272EAF  A8 02                           test al, 2
00272EB1  0F 85 D7 00 00 00               jne 0x140272f8e
00272EB7  F0 48 0F B1 56 68               lock cmpxchg qword ptr [rsi + 0x68], rdx
00272EBD  0F 85 CB 00 00 00               jne 0x140272f8e
00272EC3  48 8D 4E 68                     lea rcx, [rsi + 0x68]
00272EC7  E8 34 E7 06 00                  call 0x1402e1600
00272ECC  39 AC 24 A0 00 00 00            cmp dword ptr [rsp + 0xa0], ebp
00272ED3  74 0C                           je 0x140272ee1
00272ED5  48 8D 8E 20 01 00 00            lea rcx, [rsi + 0x120]
00272EDC  E8 DF EA FD FF                  call 0x1402519c0
00272EE1  45 8B C5                        mov r8d, r13d
00272EE4  48 8B D6                        mov rdx, rsi
00272EE7  48 8B CF                        mov rcx, rdi
00272EEA  E8 11 67 77 00                  call 0x1409e9600
00272EEF  B9 04 00 00 00                  mov ecx, 4
00272EF4  E8 87 0E 00 00                  call 0x140273d80
00272EF9  FF 0D 8D 2C BF 00               dec dword ptr [rip + 0xbf2c8d]
00272EFF  0F B6 D8                        movzx ebx, al
00272F02  40 38 AC 24 90 00 00 00         cmp byte ptr [rsp + 0x90], bpl
00272F0A  0F 85 C9 00 00 00               jne 0x140272fd9
00272F10  48 8B 0D A9 C5 D1 00            mov rcx, qword ptr [rip + 0xd1c5a9]
00272F17  48 8D 15 A2 C5 D1 00            lea rdx, [rip + 0xd1c5a2]
00272F1E  48 8D 47 10                     lea rax, [rdi + 0x10]
00272F22  48 39 51 08                     cmp qword ptr [rcx + 8], rdx
00272F26  0F 85 BB FA FF FF               jne 0x1402729e7
00272F2C  48 89 08                        mov qword ptr [rax], rcx
00272F2F  48 89 50 08                     mov qword ptr [rax + 8], rdx
00272F33  48 89 41 08                     mov qword ptr [rcx + 8], rax
00272F37  48 89 05 82 C5 D1 00            mov qword ptr [rip + 0xd1c582], rax
00272F3E  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
00272F42  48 89 6F 08                     mov qword ptr [rdi + 8], rbp
00272F46  8B 41 04                        mov eax, dword ptr [rcx + 4]
00272F49  85 C0                           test eax, eax
00272F4B  0F 84 1D 01 00 00               je 0x14027306e
00272F51  FF C8                           dec eax
00272F53  89 41 04                        mov dword ptr [rcx + 4], eax
00272F56  FF 05 4C C5 D1 00               inc dword ptr [rip + 0xd1c54c]
00272F5C  65 48 8B 0C 25 28 00 00 00      mov rcx, qword ptr gs:[0x28]
00272F65  48 83 C1 40                     add rcx, 0x40
00272F69  E8 42 42 FA FF                  call 0x1402171b0
00272F6E  39 2D AC 3D D5 00               cmp dword ptr [rip + 0xd53dac], ebp
00272F74  74 0C                           je 0x140272f82
00272F76  44 0F 20 C1                     mov rcx, cr8
00272F7A  0F B6 D3                        movzx edx, bl
00272F7D  E8 16 27 28 00                  call 0x1404f5698
00272F82  44 0F 22 C3                     mov cr8, rbx
00272F86  49 8B FF                        mov rdi, r15
00272F89  E9 54 FD FF FF                  jmp 0x140272ce2
00272F8E  48 8D 4E 68                     lea rcx, [rsi + 0x68]
00272F92  E8 39 09 FF FF                  call 0x1402638d0
00272F97  E9 27 FF FF FF                  jmp 0x140272ec3
00272F9C  48 8D 0D 1D C5 D1 00            lea rcx, [rip + 0xd1c51d]
00272FA3  4C 8D 05 FE C4 D1 00            lea r8, [rip + 0xd1c4fe]
00272FAA  E9 0A FA FF FF                  jmp 0x1402729b9
00272FAF  FF 05 F7 C4 D1 00               inc dword ptr [rip + 0xd1c4f7]
00272FB5  E9 E2 FC FF FF                  jmp 0x140272c9c
00272FBA  33 C0                           xor eax, eax
00272FBC  45 33 C9                        xor r9d, r9d
00272FBF  BA A4 07 00 00                  mov edx, 0x7a4
00272FC4  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00272FC9  49 C7 C0 20 04 00 C0            mov r8, 0xffffffffc0000420
00272FD0  8D 48 34                        lea ecx, [rax + 0x34]
00272FD3  E8 88 A6 28 00                  call 0x1404fd660
00272FD8  CC                              int3
00272FD9  4C 8B 4C 24 30                  mov r9, qword ptr [rsp + 0x30]
00272FDE  48 8B CF                        mov rcx, rdi
00272FE1  49 8D 91 D0 04 00 00            lea rdx, [r9 + 0x4d0]
00272FE8  E8 37 B5 FF FF                  call 0x14026e524
00272FED  48 89 6F 08                     mov qword ptr [rdi + 8], rbp
00272FF1  41 FF 81 E0 04 00 00            inc dword ptr [r9 + 0x4e0]
00272FF8  E9 5F FF FF FF                  jmp 0x140272f5c
00272FFD  FF 05 AD C4 D1 00               inc dword ptr [rip + 0xd1c4ad]
00273003  E9 DF FD FF FF                  jmp 0x140272de7
00273008  45 8B C5                        mov r8d, r13d
0027300B  48 8B D6                        mov rdx, rsi
0027300E  48 8B CF                        mov rcx, rdi
00273011  BD 9A 00 00 C0                  mov ebp, 0xc000009a
00273016  E8 E5 65 77 00                  call 0x1409e9600
0027301B  E9 52 FC FF FF                  jmp 0x140272c72
00273020  BD EB 00 00 C0                  mov ebp, 0xc00000eb
00273025  E9 CB FD FF FF                  jmp 0x140272df5
0027302A  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
0027302F  BA 76 01 00 00                  mov edx, 0x176
00273034  45 33 C9                        xor r9d, r9d
00273037  49 C7 C0 20 04 00 C0            mov r8, 0xffffffffc0000420
0027303E  41 8D 49 34                     lea ecx, [r9 + 0x34]
00273042  E8 19 A6 28 00                  call 0x1404fd660
00273047  CC                              int3
00273048  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
0027304D  BA 94 03 00 00                  mov edx, 0x394
00273052  45 33 C9                        xor r9d, r9d
00273055  49 C7 C0 20 04 00 C0            mov r8, 0xffffffffc0000420
0027305C  41 8D 49 34                     lea ecx, [r9 + 0x34]
00273060  E8 FB A5 28 00                  call 0x1404fd660
00273065  CC                              int3
00273066  8B CD                           mov ecx, ebp
00273068  E8 E3 39 08 00                  call 0x1402f6a50
0027306D  CC                              int3
0027306E  45 33 C9                        xor r9d, r9d
00273071  48 89 6C 24 20                  mov qword ptr [rsp + 0x20], rbp
00273076  BA A5 01 00 00                  mov edx, 0x1a5
0027307B  49 C7 C0 20 04 00 C0            mov r8, 0xffffffffc0000420
00273082  41 8D 49 34                     lea ecx, [r9 + 0x34]
00273086  E8 D5 A5 28 00                  call 0x1404fd660
0027308B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CcGetVacbMiss(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p30;
    unsigned __int8 v_stack_p8;
    unsigned __int8 v_stack_p90;
    unsigned int v_stack_pA0;
    unsigned int v_stack_pA8;

    *(unsigned int *)(v_rsp + 32) = a4;
    *(unsigned int *)(v_rsp + 24) = a3;
    v_rsp = (v_rsp) - (72);
    result = 0;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    v_stack_m58 = *(unsigned __int64 *)(a1 + 536);
    result = (unsigned int)(((unsigned int)((unsigned int)(a2))) & (0x3FFFFULL));
    v_rdi = 0;
    a2 = (unsigned int)((a2) - ((unsigned int)(result)));
    *(unsigned int *)(v_rsp + 16) = (unsigned int)(a2);
loc_0027294F:
    v_stack_p8 = 0;
    if ((*(unsigned int *)(v_rip + 13976497)) != 0) goto loc_00272E1D;
loc_00272975:
    a1 = (*(unsigned __int64 *)(gs_base + (0 + 40))) + (64);
    if (((*(unsigned __int8 *)(v_rip + 13975929)) & (33)) != 0) goto loc_002729EE;
loc_0027298F:
    if (a1 != 0) goto loc_00272E3A;
loc_0027299E:
    if (0 == 0) goto loc_00272F9C;
    v_r13 = (unsigned int)((0) | (2));
loc_002729B9:
    a4 = 0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 536) + 1232)) == (*(unsigned __int64 *)(a1 + 536) + 1232)) goto loc_00272A70;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 536) + 1232)) + 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 536) + 1232))) goto loc_002729E7;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 536) + 1232) + 8))) == (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 536) + 1232))) goto loc_002729FF;
loc_002729E7:
loc_002729EE:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13218916))) != 0) goto loc_0027298F;
    result = KiAcquireQueuedSpinLockInstrumented(3, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 536) + 1232)), *(unsigned __int64 *)(a1 + 536) + 1248, a4);
    goto loc_0027299E;
loc_002729FF:
    *(unsigned __int64 *)(3) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 536) + 1232));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 536) + 1232)) + 8) = 3;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 536) + 1248)))) < 1) goto loc_00273048;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 536) + 1248))) - 1);
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 536) + 1248) = (unsigned int)(result);
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 536) + 1232) - 16) - (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 536) + 1232) - 16 + 32));
    result = (result) - (16);
    result = (result) >> (3);
    result = (result) * (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 536) + 1232)));
    if (((unsigned int)(result)) >= = (*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 536) + 1232) - 16 + 32) + 8))) {
        *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 536) + 1232) - 16 + 32) + 8) = (unsigned int)(result);
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 536) + 1232) - 16)) != 0) goto loc_00272A68;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13748813) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 536) + 1232) - 16 + 32))) * 8) == 0) goto loc_00272A68;
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13748813) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 536) + 1232) - 16 + 32))) * 8))) != ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 536) + 1232) - 16 + 32)))))) goto loc_0027302A;
loc_00272A68:
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 536) + 1232) - 16 + 8) = -1;
loc_00272A70:
    a1 = (*(unsigned __int64 *)(gs_base + (0 + 40))) + (64);
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13748813) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 536) + 1232) - 16 + 32))) * 8), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 536) + 1232) - 16 + 32))), a4);
    if ((*(unsigned int *)(v_rip + 13976215)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 536) + 1232) - 16 + 32))), a4);
    }
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 536) + 1232) - 16 == 0) goto loc_00272D64;
loc_00272AA7:
    a1 = (*(unsigned __int64 *)(a1 + 32)) - (v_stack_p10);
    v_stack_m50 = a1;
    result = (a1) >> (32);
    if ((unsigned int)(result) != 0) goto loc_00272ACB;
    if (((unsigned int)(a1)) >= = 0x40000ULL) {
        v_stack_m50 = 0x40000ULL;
    }
    result = MmMapViewInSystemCache(*(unsigned __int64 *)(a1 + 176), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 536) + 1232) - 16, v_stack_p10, v_stack_m50);
    if ((unsigned int)((unsigned int)(a3)) != 0) {
        a1 = a1 + 288;
        result = ExAcquireFastMutex(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 536) + 1232) - 16, v_stack_p10, v_stack_m50);
    }
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1 + 104, a2, a3, v_stack_m50);
    if (!(condition_is_above_or_equal)) {
        a3 = a1 + 104;
        a2 = result;
        a1 = a1 + 104;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, v_stack_m50);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if ((*(unsigned __int64 *)(a1 + 32)) > 0x2000000ULL) goto loc_00272CF7;
    result = ((unsigned int)(v_stack_p10)) >> (18);
loc_00272B61:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88) + result * 8) != 0) goto loc_00272E66;
loc_00272B6A:
    if (sign_flag) goto loc_00272C72;
    if ((*(unsigned __int64 *)(a1 + 32)) > 0x2000000ULL) goto loc_00272B9A;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 536) + 1232) - 16) >= -2) goto loc_00272BAE;
    a1 = ((unsigned int)(v_stack_p10)) >> (18);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88) + a1 * 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 536) + 1232) - 16;
    goto loc_00272BB4;
loc_00272B9A:
    a4 = 0;
    result = CcSetVacbLargeOffset(a1, v_stack_p10, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 536) + 1232) - 16, a4);
loc_00272BAE:
    v_rbx = v_stack_p10;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 536) + 1232) - 16) <= -3) {
        v_rbx = v_stack_p10;
    }
    if ((unsigned __int8)((unsigned __int8)(result)) == 0) goto loc_00273008;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 536) + 1232) - 16 + 8)) != -1) goto loc_00272FBA;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 536) + 1232) - 16 + 8) = a1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 536) + 1232) - 16 + 16) = v_rbx;
    v_r12 = (unsigned int)((1) + 1);
    if ((unsigned __int16)(v_r12) == 0) goto loc_00272E47;
    if (((unsigned __int16)(v_r12)) == 1) {
    }
    result = v_stack_p10;
    if (v_stack_p10 >= (*(unsigned __int64 *)(a1 + 376))) {
        result = (v_stack_p10) + (0x40000ULL);
        *(unsigned __int64 *)(a1 + 376) = result;
    }
    a1 = (*(unsigned __int64 *)(a1 + 104)) & (-16);
    a2 = *(unsigned __int64 *)(a1 + 104) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 + 104))) & (2)) != 0) goto loc_00272E2C;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 + 104))) & (2)) != 0) goto loc_00272E2C;
loc_00272C51:
    result = KeAbPostRelease(a1 + 104, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 536) + 1232) - 16, a4);
    if (v_stack_p18 == 0) goto loc_00272CE2;
    result = ExReleaseFastMutex(a1 + 288, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 536) + 1232) - 16, a4);
    goto loc_00272CE2;
loc_00272C72:
    result = CcReleaseBcbLockAndVacbLock((unsigned int)((unsigned int)((unsigned int)(v_stack_p18))), a1, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 536) + 1232) - 16, a4);
    if ((unsigned __int8)(v_stack_p8) != 0) goto loc_00272FAF;
    result = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 536) + 1232) - 16) = 0;
loc_00272C9C:
    result = KeAcquireQueuedSpinLock(4, a1, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 536) + 1232) - 16, a4);
    result = CcSetVacbInFreeList(v_stack_m58, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 536) + 1232) - 16, (unsigned __int8)(v_stack_p8), a4);
    result = KeReleaseQueuedSpinLock(4, (unsigned __int8)((unsigned __int8)(result)), (unsigned __int8)(v_stack_p8), a4);
    result = FsRtlIsNtstatusExpected((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned __int8)((unsigned __int8)(result)), (unsigned __int8)(v_stack_p8), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00273020;
    result = 0;
    if (sign_flag) goto loc_00272DF5;
loc_00272CE2:
    v_rsp = (v_rsp) + (72);
    return 0;
loc_00272CF7:
    result = 0;
loc_00272D03:
    a1 = (unsigned int)((25) + (7));
    a2 = (unsigned int)((0) + 1);
    result = (v_r12) << ((unsigned __int8)(a1));
    if (0 > result) goto loc_00272D03;
    result = ((unsigned __int8)(result)) >> (25);
    if (*(unsigned __int64 *)(v_stack_p8 + result * 8) == 0) goto loc_00272B6A;
loc_00272D30:
    if ((unsigned int)(a2) == 0) goto loc_00272B61;
    result = (v_r12) << (25);
    a3 = (unsigned int)((25) + (-7));
    result = (result) - 1;
    v_r10 = ((unsigned __int8)(result)) & (result);
    a2 = (unsigned int)((a2) - 1);
    result = (v_r10) >> ((unsigned __int8)((unsigned int)(a3)));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + result * 8) + result * 8) != 0) goto loc_00272D30;
    goto loc_00272B61;
loc_00272D64:
loc_00272D6D:
    if ((*(unsigned int *)(v_rip + 12529116)) == 0) goto loc_00272DCD;
    if ((*(unsigned int *)(v_rip + 12529167)) == 0) goto loc_00272DCD;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 8) + 8) == 0) goto loc_00272DCD;
    a4 = 0;
    a3 = 0;
    result = CcUnmapInactiveViewsInternal(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 8) + 8), a4 + 64, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_00272DCD;
    result = KeAcquireQueuedSpinLock(4, a4 + 64, a3, a4);
    result = CcGetVacbFromFreeList((unsigned int)((unsigned int)(result)), (unsigned __int8)(v_stack_p90), a3, a4);
    result = KeReleaseQueuedSpinLock(4, (unsigned __int8)((unsigned __int8)(result)), a3, a4);
    if (result == 0) goto loc_00272D6D;
loc_00272DCD:
    if (result != 0) goto loc_00272AA7;
    if (((unsigned int)((unsigned int)(v_stack_pA8))) == ((unsigned int)(v_r12))) goto loc_00272FFD;
loc_00272DE7:
loc_00272DF5:
    if ((unsigned __int8)(v_stack_p90) != 0) goto loc_00273066;
    if (((unsigned int)((unsigned int)(v_stack_pA8))) != ((unsigned int)(v_r12))) goto loc_00273066;
    goto loc_0027294F;
loc_00272E1D:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)((unsigned __int8)(result)), 2, a3, a4);
    goto loc_00272975;
loc_00272E2C:
    result = ExfReleasePushLock(a1 + 104, 2, a3, a4);
    goto loc_00272C51;
loc_00272E3A:
    result = KxWaitForLockOwnerShip(a1 + 104, result, a3, a4);
    goto loc_0027299E;
loc_00272E47:
    result = 0;
    a4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(result + 52, (unsigned int)(0xBACULL), 0xFFFFFFFFC0000420ULL, a4);
loc_00272E66:
    if (sign_flag) goto loc_00272C72;
    v_r12 = (unsigned int)((v_r12) + 1);
    if ((unsigned __int16)(v_r12) == 0) goto loc_00272E47;
    if (((unsigned __int16)(v_r12)) == 1) {
    }
    a1 = (*(unsigned __int64 *)(a1 + 104)) & (-16);
    a2 = *(unsigned __int64 *)(a1 + 104) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 + 104))) & (2)) != 0) goto loc_00272F8E;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 + 104))) & (2)) != 0) goto loc_00272F8E;
loc_00272EC3:
    result = KeAbPostRelease(a1 + 104, a2, 0xFFFFFFFFC0000420ULL, a4);
    if (v_stack_pA0 != 0) {
        a1 = a1 + 288;
        result = ExReleaseFastMutex(a1, a2, 0xFFFFFFFFC0000420ULL, a4);
    }
    result = CcUnmapVacb((unsigned __int8)(v_r12), a1, (unsigned int)((unsigned int)(v_r13)), a4);
    result = KeAcquireQueuedSpinLock(4, a1, (unsigned int)((unsigned int)(v_r13)), a4);
    if (v_stack_p90 != 0) goto loc_00272FD9;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13747625) + 8)) != (v_rip + 13747618)) goto loc_002729E7;
    *(unsigned __int64 *)((unsigned __int8)(v_r12) + 16) = *(unsigned __int64 *)(v_rip + 13747625);
    *(unsigned __int64 *)((unsigned __int8)(v_r12) + 16 + 8) = v_rip + 13747618;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13747625) + 8) = (unsigned __int8)(v_r12) + 16;
    *(unsigned __int64 *)(v_rip + 13747586) = (unsigned __int8)(v_r12) + 16;
    *(unsigned __int64 *)((unsigned __int8)(v_r12) + 8) = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned __int8)(v_r12) + 32) + 4))) == 0) goto loc_0027306E;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned __int8)(v_r12) + 32) + 4))) - 1);
    *(unsigned int *)(*(unsigned __int64 *)((unsigned __int8)(v_r12) + 32) + 4) = (unsigned int)(result);
loc_00272F5C:
    a1 = (*(unsigned __int64 *)(gs_base + (0 + 40))) + (64);
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(a1, v_rip + 13747618, (unsigned int)((unsigned int)(v_r13)), a4);
    if ((*(unsigned int *)(v_rip + 13974956)) != 0) {
        a1 = (unsigned __int8)(v_cr8);
        a2 = (unsigned __int8)((unsigned __int8)(result));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, (unsigned int)((unsigned int)(v_r13)), a4);
    }
    goto loc_00272CE2;
loc_00272F8E:
    result = ExfReleasePushLock(a1 + 104, a2, (unsigned int)((unsigned int)(v_r13)), a4);
    goto loc_00272EC3;
loc_00272F9C:
    goto loc_002729B9;
loc_00272FAF:
    goto loc_00272C9C;
loc_00272FBA:
    result = 0;
    a4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(result + 52, (unsigned int)(0x7A4ULL), 0xFFFFFFFFC0000420ULL, a4);
loc_00272FD9:
    result = CcSetVacbIntoList((unsigned int)(v_stack_pA8), v_stack_p30 + 1232, 0xFFFFFFFFC0000420ULL, v_stack_p30);
    *(unsigned __int64 *)((unsigned int)(v_stack_pA8) + 8) = 0;
    goto loc_00272F5C;
loc_00272FFD:
    goto loc_00272DE7;
loc_00273008:
    result = CcUnmapVacb((unsigned int)(v_stack_pA8), a1, (unsigned int)((unsigned int)(v_r13)), v_stack_p30);
    goto loc_00272C72;
loc_00273020:
    goto loc_00272DF5;
loc_0027302A:
    v_stack_p20 = v_stack_p30;
    a4 = 0;
    result = KeBugCheckEx(a4 + 52, 374, 0xFFFFFFFFC0000420ULL, a4);
loc_00273048:
    v_stack_p20 = 0;
    a4 = 0;
    result = KeBugCheckEx(a4 + 52, 916, 0xFFFFFFFFC0000420ULL, a4);
loc_00273066:
    result = RtlRaiseStatus((unsigned int)((unsigned int)((unsigned int)(0xC00000EBULL))), 916, 0xFFFFFFFFC0000420ULL, a4);
loc_0027306E:
    a4 = 0;
    v_stack_p20 = (unsigned int)(0xC00000EBULL);
    result = KeBugCheckEx(a4 + 52, 421, 0xFFFFFFFFC0000420ULL, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CcGetVacbMiss(void *Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p30;
    uint8_t v_stack_p8;
    uint8_t v_stack_p90;
    uint32_t v_stack_pA0;
    uint32_t v_stack_pA8;

    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    local_rsp = (local_rsp) - (72);
    result = 0;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    v_stack_m58 = *(uint64_t *)(arg1 + 0x218);
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) & (0x3FFFFULL));
    local_rdi = 0;
    Arg2 = (uint32_t)((Arg2) - ((uint32_t)(result)));
    *(uint32_t *)(local_rsp + 0x10) = (uint32_t)(Arg2);
loc_0027294F:
    v_stack_p8 = 0;
    if ((*(uint32_t *)(v_rip + 0xD543B1)) != 0) goto loc_00272E1D;
loc_00272975:
    Arg1 = (*(uint64_t *)(gs_base + (0 + 0x28))) + (64);
    if (((*(uint8_t *)(v_rip + 0xD54179)) & (33)) != 0) goto loc_002729EE;
loc_0027298F:
    if (Arg1 != NULL) goto loc_00272E3A;
loc_0027299E:
    if (0 == 0) goto loc_00272F9C;
    local_r13 = (uint32_t)((0) | (2));
loc_002729B9:
    Arg4 = 0;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x218) + 0x4D0)) == (*(uint64_t *)(arg1 + 0x218) + 1232)) goto loc_00272A70;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x218) + 0x4D0)) + 0x8)) != (*(uint64_t *)(*(uint64_t *)(arg1 + 0x218) + 0x4D0))) goto loc_002729E7;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x218) + 0x4D0) + 0x8))) == (*(uint64_t *)(*(uint64_t *)(arg1 + 0x218) + 0x4D0))) goto loc_002729FF;
loc_002729E7:
loc_002729EE:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC9B464))) != 0) goto loc_0027298F;
    result = KiAcquireQueuedSpinLockInstrumented(3, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x218) + 0x4D0)), *(uint64_t *)(arg1 + 0x218) + 1248, Arg4);
    goto loc_0027299E;
loc_002729FF:
    *(uint64_t *)(3) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x218) + 0x4D0));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x218) + 0x4D0)) + 0x8) = 3;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x218) + 0x4E0)))) < 1) goto loc_00273048;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x218) + 0x4E0))) - 1);
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x218) + 0x4E0) = (uint32_t)(result);
    result = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x218) + 0x4D0) - 16) - (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x218) + 0x4D0) - 0x10 + 0x20));
    result = (result) - (16);
    result = (result) >> (3);
    result = (result) * (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x218) + 0x4D0)));
    if (((uint32_t)(result)) >= = (*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x218) + 0x4D0) - 0x10 + 0x20) + 0x8))) {
        *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x218) + 0x4D0) - 0x10 + 0x20) + 0x8) = (uint32_t)(result);
    }
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x218) + 0x4D0) - 0x10)) != 0) goto loc_00272A68;
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0xD1CA4D) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x218) + 0x4D0) - 0x10 + 0x20))) * 8) == 0) goto loc_00272A68;
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xD1CA4D) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x218) + 0x4D0) - 0x10 + 0x20))) * 8))) != ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x218) + 0x4D0) - 0x10 + 0x20)))))) goto loc_0027302A;
loc_00272A68:
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x218) + 0x4D0) - 0x10 + 0x8) = -1;
loc_00272A70:
    Arg1 = (*(uint64_t *)(gs_base + (0 + 0x28))) + (64);
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(Arg1, *(uint64_t *)(*(uint64_t *)(v_rip + 0xD1CA4D) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x218) + 0x4D0) - 0x10 + 0x20))) * 8), (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x218) + 0x4D0) - 0x10 + 0x20))), Arg4);
    if ((*(uint32_t *)(v_rip + 0xD54297)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x218) + 0x4D0) - 0x10 + 0x20))), Arg4);
    }
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x218) + 0x4D0) - 16 == 0) goto loc_00272D64;
loc_00272AA7:
    Arg1 = (*(uint64_t *)(arg1 + 0x20)) - (v_stack_p10);
    v_stack_m50 = Arg1;
    result = (Arg1) >> (32);
    if ((uint32_t)(result) != 0) goto loc_00272ACB;
    if (((uint32_t)(Arg1)) >= = 0x40000ULL) {
        v_stack_m50 = 0x40000ULL;
    }
    result = MmMapViewInSystemCache(*(uint64_t *)(arg1 + 0xB0), *(uint64_t *)(*(uint64_t *)(arg1 + 0x218) + 0x4D0) - 16, v_stack_p10, v_stack_m50);
    if ((uint32_t)((uint32_t)(Arg3)) != 0) {
        Arg1 = Arg1 + 288;
        result = ExAcquireFastMutex(Arg1, *(uint64_t *)(*(uint64_t *)(arg1 + 0x218) + 0x4D0) - 16, v_stack_p10, v_stack_m50);
    }
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1 + 104, Arg2, Arg3, v_stack_m50);
    if (!(condition_is_above_or_equal)) {
        Arg3 = Arg1 + 104;
        Arg2 = result;
        Arg1 = Arg1 + 104;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, v_stack_m50);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if ((*(uint64_t *)(arg1 + 0x20)) > 0x2000000ULL) goto loc_00272CF7;
    result = ((uint32_t)(v_stack_p10)) >> (18);
loc_00272B61:
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x58) + result * 8) != 0) goto loc_00272E66;
loc_00272B6A:
    if (sign_flag) goto loc_00272C72;
    if ((*(uint64_t *)(arg1 + 0x20)) > 0x2000000ULL) goto loc_00272B9A;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x218) + 0x4D0) - 16) >= -2) goto loc_00272BAE;
    Arg1 = ((uint32_t)(v_stack_p10)) >> (18);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x58) + arg1 * 8) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x218) + 0x4D0) - 16;
    goto loc_00272BB4;
loc_00272B9A:
    Arg4 = 0;
    result = CcSetVacbLargeOffset(Arg1, v_stack_p10, *(uint64_t *)(*(uint64_t *)(arg1 + 0x218) + 0x4D0) - 16, Arg4);
loc_00272BAE:
    local_rbx = v_stack_p10;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x218) + 0x4D0) - 16) <= -3) {
        local_rbx = v_stack_p10;
    }
    if ((uint8_t)((uint8_t)(result)) == 0) goto loc_00273008;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x218) + 0x4D0) - 0x10 + 0x8)) != -1) goto loc_00272FBA;
    *(void **)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x218) + 0x4D0) - 0x10 + 0x8) = Arg1;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x218) + 0x4D0) - 0x10 + 0x10) = local_rbx;
    local_r12 = (uint32_t)((1) + 1);
    if ((uint16_t)(local_r12) == 0) goto loc_00272E47;
    if (((uint16_t)(local_r12)) == 1) {
    }
    result = v_stack_p10;
    if (v_stack_p10 >= (*(uint64_t *)(arg1 + 0x178))) {
        result = (v_stack_p10) + (0x40000ULL);
        *(uint64_t *)(arg1 + 0x178) = result;
    }
    Arg1 = (*(uint64_t *)(arg1 + 0x68)) & (-16);
    Arg2 = *(uint64_t *)(arg1 + 0x68) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(arg1 + 0x68))) & (2)) != 0) goto loc_00272E2C;
    if ((((uint8_t)(*(uint64_t *)(arg1 + 0x68))) & (2)) != 0) goto loc_00272E2C;
loc_00272C51:
    result = KeAbPostRelease(Arg1 + 104, Arg2, *(uint64_t *)(*(uint64_t *)(arg1 + 0x218) + 0x4D0) - 16, Arg4);
    if (v_stack_p18 == 0) goto loc_00272CE2;
    result = ExReleaseFastMutex(Arg1 + 288, Arg2, *(uint64_t *)(*(uint64_t *)(arg1 + 0x218) + 0x4D0) - 16, Arg4);
    goto loc_00272CE2;
loc_00272C72:
    result = CcReleaseBcbLockAndVacbLock((uint32_t)((uint32_t)((uint32_t)(v_stack_p18))), Arg1, *(uint64_t *)(*(uint64_t *)(arg1 + 0x218) + 0x4D0) - 16, Arg4);
    if ((uint8_t)(v_stack_p8) != 0) goto loc_00272FAF;
    result = 0;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x218) + 0x4D0) - 0x10) = 0;
loc_00272C9C:
    result = KeAcquireQueuedSpinLock(4, Arg1, *(uint64_t *)(*(uint64_t *)(arg1 + 0x218) + 0x4D0) - 16, Arg4);
    result = CcSetVacbInFreeList(v_stack_m58, *(uint64_t *)(*(uint64_t *)(arg1 + 0x218) + 0x4D0) - 16, (uint8_t)(v_stack_p8), Arg4);
    result = KeReleaseQueuedSpinLock(4, (uint8_t)((uint8_t)(result)), (uint8_t)(v_stack_p8), Arg4);
    result = FsRtlIsNtstatusExpected((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint8_t)((uint8_t)(result)), (uint8_t)(v_stack_p8), Arg4);
    if ((uint8_t)(result) == 0) goto loc_00273020;
    result = 0;
    if (sign_flag) goto loc_00272DF5;
loc_00272CE2:
    local_rsp = (local_rsp) + (72);
    return 0;
loc_00272CF7:
    result = 0;
loc_00272D03:
    Arg1 = (uint32_t)((25) + (7));
    Arg2 = (uint32_t)((0) + 1);
    result = (local_r12) << ((uint8_t)(Arg1));
    if (0 > result) goto loc_00272D03;
    result = ((uint8_t)(result)) >> (25);
    if (*(uint64_t *)(v_stack_p8 + result * 8) == 0) goto loc_00272B6A;
loc_00272D30:
    if ((uint32_t)(Arg2) == 0) goto loc_00272B61;
    result = (local_r12) << (25);
    Arg3 = (uint32_t)((25) + (-7));
    result = (result) - 1;
    local_r10 = ((uint8_t)(result)) & (result);
    Arg2 = (uint32_t)((Arg2) - 1);
    result = (local_r10) >> ((uint8_t)((uint32_t)(Arg3)));
    if (*(uint64_t *)(*(uint64_t *)(v_stack_p8 + result * 8) + result * 8) != 0) goto loc_00272D30;
    goto loc_00272B61;
loc_00272D64:
loc_00272D6D:
    if ((*(uint32_t *)(v_rip + 0xBF2DDC)) == 0) goto loc_00272DCD;
    if ((*(uint32_t *)(v_rip + 0xBF2E0F)) == 0) goto loc_00272DCD;
    if (*(uint64_t *)(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x8) + 0x8) == 0) goto loc_00272DCD;
    Arg4 = 0;
    Arg3 = 0;
    result = CcUnmapInactiveViewsInternal(*(uint64_t *)(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x8) + 0x8), Arg4 + 64, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00272DCD;
    result = KeAcquireQueuedSpinLock(4, Arg4 + 64, Arg3, Arg4);
    result = CcGetVacbFromFreeList((uint32_t)((uint32_t)(result)), (uint8_t)(v_stack_p90), Arg3, Arg4);
    result = KeReleaseQueuedSpinLock(4, (uint8_t)((uint8_t)(result)), Arg3, Arg4);
    if (result == 0) goto loc_00272D6D;
loc_00272DCD:
    if (result != 0) goto loc_00272AA7;
    if (((uint32_t)((uint32_t)(v_stack_pA8))) == ((uint32_t)(local_r12))) goto loc_00272FFD;
loc_00272DE7:
loc_00272DF5:
    if ((uint8_t)(v_stack_p90) != 0) goto loc_00273066;
    if (((uint32_t)((uint32_t)(v_stack_pA8))) != ((uint32_t)(local_r12))) goto loc_00273066;
    goto loc_0027294F;
loc_00272E1D:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)((uint8_t)(result)), 2, Arg3, Arg4);
    goto loc_00272975;
loc_00272E2C:
    result = ExfReleasePushLock(Arg1 + 104, 2, Arg3, Arg4);
    goto loc_00272C51;
loc_00272E3A:
    result = KxWaitForLockOwnerShip(Arg1 + 104, result, Arg3, Arg4);
    goto loc_0027299E;
loc_00272E47:
    result = 0;
    Arg4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(result + 52, (uint32_t)(0xBACULL), 0xFFFFFFFFC0000420ULL, Arg4);
loc_00272E66:
    if (sign_flag) goto loc_00272C72;
    local_r12 = (uint32_t)((local_r12) + 1);
    if ((uint16_t)(local_r12) == 0) goto loc_00272E47;
    if (((uint16_t)(local_r12)) == 1) {
    }
    Arg1 = (*(uint64_t *)(arg1 + 0x68)) & (-16);
    Arg2 = *(uint64_t *)(arg1 + 0x68) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(arg1 + 0x68))) & (2)) != 0) goto loc_00272F8E;
    if ((((uint8_t)(*(uint64_t *)(arg1 + 0x68))) & (2)) != 0) goto loc_00272F8E;
loc_00272EC3:
    result = KeAbPostRelease(Arg1 + 104, Arg2, 0xFFFFFFFFC0000420ULL, Arg4);
    if (v_stack_pA0 != 0) {
        Arg1 = Arg1 + 288;
        result = ExReleaseFastMutex(Arg1, Arg2, 0xFFFFFFFFC0000420ULL, Arg4);
    }
    result = CcUnmapVacb((uint8_t)(local_r12), Arg1, (uint32_t)((uint32_t)(local_r13)), Arg4);
    result = KeAcquireQueuedSpinLock(4, Arg1, (uint32_t)((uint32_t)(local_r13)), Arg4);
    if (v_stack_p90 != 0) goto loc_00272FD9;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xD1C5A9) + 0x8)) != (v_rip + 13747618)) goto loc_002729E7;
    *(uint64_t *)((uint8_t)(local_r12) + 0x10) = *(uint64_t *)(v_rip + 0xD1C5A9);
    *(uint64_t *)((uint8_t)(local_r12) + 0x10 + 0x8) = v_rip + 13747618;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0xD1C5A9) + 0x8) = (uint8_t)(local_r12) + 16;
    *(uint64_t *)(v_rip + 0xD1C582) = (uint8_t)(local_r12) + 16;
    *(uint64_t *)((uint8_t)(local_r12) + 0x8) = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint8_t)(local_r12) + 0x20) + 0x4))) == 0) goto loc_0027306E;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint8_t)(local_r12) + 0x20) + 0x4))) - 1);
    *(uint32_t *)(*(uint64_t *)((uint8_t)(local_r12) + 0x20) + 0x4) = (uint32_t)(result);
loc_00272F5C:
    Arg1 = (*(uint64_t *)(gs_base + (0 + 0x28))) + (64);
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(Arg1, v_rip + 13747618, (uint32_t)((uint32_t)(local_r13)), Arg4);
    if ((*(uint32_t *)(v_rip + 0xD53DAC)) != 0) {
        Arg1 = (uint8_t)(v_cr8);
        Arg2 = (uint8_t)((uint8_t)(result));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, (uint32_t)((uint32_t)(local_r13)), Arg4);
    }
    goto loc_00272CE2;
loc_00272F8E:
    result = ExfReleasePushLock(Arg1 + 104, Arg2, (uint32_t)((uint32_t)(local_r13)), Arg4);
    goto loc_00272EC3;
loc_00272F9C:
    goto loc_002729B9;
loc_00272FAF:
    goto loc_00272C9C;
loc_00272FBA:
    result = 0;
    Arg4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(result + 52, (uint32_t)(0x7A4ULL), 0xFFFFFFFFC0000420ULL, Arg4);
loc_00272FD9:
    result = CcSetVacbIntoList((uint32_t)(v_stack_pA8), v_stack_p30 + 1232, 0xFFFFFFFFC0000420ULL, v_stack_p30);
    *(uint64_t *)((uint32_t)(v_stack_pA8) + 0x8) = 0;
    goto loc_00272F5C;
loc_00272FFD:
    goto loc_00272DE7;
loc_00273008:
    result = CcUnmapVacb((uint32_t)(v_stack_pA8), Arg1, (uint32_t)((uint32_t)(local_r13)), v_stack_p30);
    goto loc_00272C72;
loc_00273020:
    goto loc_00272DF5;
loc_0027302A:
    v_stack_p20 = v_stack_p30;
    Arg4 = 0;
    result = KeBugCheckEx(Arg4 + 52, 374, 0xFFFFFFFFC0000420ULL, Arg4);
loc_00273048:
    v_stack_p20 = 0;
    Arg4 = 0;
    result = KeBugCheckEx(Arg4 + 52, 916, 0xFFFFFFFFC0000420ULL, Arg4);
loc_00273066:
    result = RtlRaiseStatus((uint32_t)((uint32_t)((uint32_t)(0xC00000EBULL))), 916, 0xFFFFFFFFC0000420ULL, Arg4);
loc_0027306E:
    Arg4 = 0;
    v_stack_p20 = (uint32_t)(0xC00000EBULL);
    result = KeBugCheckEx(Arg4 + 52, 421, 0xFFFFFFFFC0000420ULL, Arg4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x58` | `64` | `R` |
| `Arg1` | `+ 0x68` | `8` | `R` |
| `Arg1` | `+ 0x68` | `64` | `R` |
| `Arg1` | `+ 0x68` | `64` | `R/W` |
| `Arg1` | `+ 0xB0` | `64` | `R` |
| `Arg1` | `+ 0x120` | `64` | `R` |
| `Arg1` | `+ 0x178` | `64` | `R` |
| `Arg1` | `+ 0x178` | `64` | `W` |
| `Arg1` | `+ 0x218` | `64` | `R` |
| `Arg1` | `+ 0x224` | `32` | `R/W` |
| `Arg1` | `+ 0x228` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00272900&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
