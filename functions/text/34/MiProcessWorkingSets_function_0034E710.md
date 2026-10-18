# MiProcessWorkingSets

- RVA: `0x0034E710`–`0x0034EDBF` (길이 `1,711` bytes)
- VA: `0x000000014034E710`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00078B94`
- 디코드: `391`개 명령, `1,711/1,711` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **23**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x0034E754` → [MiLogPartitionState](MiLogPartitionState_function_0034F330.md) (function, `0x0034F330`)
- `0x0034E767` → [MiComputeAgingPercent](MiComputeAgingPercent_function_0034F508.md) (function, `0x0034F508`)
- `0x0034E772` → [MiComputeSystemTrimCriteria](MiComputeSystemTrimCriteria_function_0034E184.md) (function, `0x0034E184`)
- `0x0034E783` → [MiLogProcessWorkingSetsStart](MiLogProcessWorkingSetsStart_function_0034F468.md) (function, `0x0034F468`)
- `0x0034E7AE` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x0034E8BE` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x0034E8CC` → [MiTrimOrAgeWorkingSet](MiTrimOrAgeWorkingSet_function_0034EFC0.md) (function, `0x0034EFC0`)
- `0x0034E8E4` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x0034E926` → [MiReturnWsToExpansionList](../35/MiReturnWsToExpansionList_function_003504E0.md) (function, `0x003504E0`)
- `0x0034E998` → [MiCheckSystemTrimEndCriteria](MiCheckSystemTrimEndCriteria_function_0034EDC8.md) (function, `0x0034EDC8`)
- `0x0034E9E0` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x0034E9E8` → [MiLogProcessWorkingSetsStop](MiLogProcessWorkingSetsStop_function_0034F60C.md) (function, `0x0034F60C`)
- `0x0034EAD2` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x0034EAE0` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x0034EB55` → [MiReturnWsToExpansionList](../35/MiReturnWsToExpansionList_function_003504E0.md) (function, `0x003504E0`)
- `0x0034EC3D` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x0034EC49` → [KeRetryOutswapProcess](../4A/KeRetryOutswapProcess_function_004A2E20.md) (function, `0x004A2E20`)
- `0x0034EC55` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x0034EC8D` → [MiReturnWsToExpansionList](../35/MiReturnWsToExpansionList_function_003504E0.md) (function, `0x003504E0`)
- `0x0034ECC9` → [MiDrainZeroLookasides](../44/MiDrainZeroLookasides_function_0044D818.md) (function, `0x0044D818`)
- `0x0034ED12` → [MiOrderTrimList](../40/MiOrderTrimList_function_00409F24.md) (function, `0x00409F24`)
- `0x0034ED35` → [MiInitializeWorkingSetManagerParameters](../67/MiInitializeWorkingSetManagerParameters_function_0067E7F8.md) (function, `0x0067E7F8`)
- `0x0034EDAC` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)

### Direct callers
- [MiWorkingSetManager](../2D/MiWorkingSetManager_function_002DA7E0.md) at `0x002DA940`
- [MiWorkingSetManager](../2D/MiWorkingSetManager_function_002DA7E0.md) at `0x002DAAE8`

### Static image references
- `0x0034E72B` → RVA `0x00E38D00` (`.data`; read)
- `0x0034E7A4` → RVA `0x00E374C0` (`.data`; read)
- `0x0034EA83` → RVA `0x00FC5000` (`ALMOSTRO`; read)
- `0x0034EA91` → RVA `0x00E37700` (`.data`; read)
- `0x0034ED01` → RVA `0x000110F0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0034E710  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
0034E715  55                              push rbp
0034E716  56                              push rsi
0034E717  57                              push rdi
0034E718  41 54                           push r12
0034E71A  41 55                           push r13
0034E71C  41 56                           push r14
0034E71E  41 57                           push r15
0034E720  48 83 EC 30                     sub rsp, 0x30
0034E724  48 8B B9 C0 44 00 00            mov rdi, qword ptr [rcx + 0x44c0]
0034E72B  48 8D 05 CE A5 AE 00            lea rax, [rip + 0xaea5ce]
0034E732  33 F6                           xor esi, esi
0034E734  4C 8B EA                        mov r13, rdx
0034E737  48 8B E9                        mov rbp, rcx
0034E73A  44 8D 76 01                     lea r14d, [rsi + 1]
0034E73E  48 3B C8                        cmp rcx, rax
0034E741  0F 84 3C 03 00 00               je 0x14034ea83
0034E747  40 38 75 0C                     cmp byte ptr [rbp + 0xc], sil
0034E74B  0F 85 E1 05 00 00               jne 0x14034ed32
0034E751  48 8B CD                        mov rcx, rbp
0034E754  E8 D7 0B 00 00                  call 0x14034f330
0034E759  8B 45 04                        mov eax, dword ptr [rbp + 4]
0034E75C  A8 10                           test al, 0x10
0034E75E  0F 85 89 02 00 00               jne 0x14034e9ed
0034E764  48 8B CD                        mov rcx, rbp
0034E767  E8 9C 0D 00 00                  call 0x14034f508
0034E76C  49 8B D5                        mov rdx, r13
0034E76F  48 8B CD                        mov rcx, rbp
0034E772  E8 0D FA FF FF                  call 0x14034e184
0034E777  44 8B C0                        mov r8d, eax
0034E77A  49 8B D5                        mov rdx, r13
0034E77D  48 8B CD                        mov rcx, rbp
0034E780  44 8B F8                        mov r15d, eax
0034E783  E8 E0 0C 00 00                  call 0x14034f468
0034E788  41 F6 C7 05                     test r15b, 5
0034E78C  0F 85 2C 05 00 00               jne 0x14034ecbe
0034E792  89 74 24 28                     mov dword ptr [rsp + 0x28], esi
0034E796  89 74 24 24                     mov dword ptr [rsp + 0x24], esi
0034E79A  41 F6 C7 02                     test r15b, 2
0034E79E  74 04                           je 0x14034e7a4
0034E7A0  44 01 77 54                     add dword ptr [rdi + 0x54], r14d
0034E7A4  48 8D 0D 15 8D AE 00            lea rcx, [rip + 0xae8d15]
0034E7AB  48 8B DE                        mov rbx, rsi
0034E7AE  E8 DD 9E EF FF                  call 0x140248690
0034E7B3  88 44 24 70                     mov byte ptr [rsp + 0x70], al
0034E7B7  44 8A D0                        mov r10b, al
0034E7BA  41 F6 C7 20                     test r15b, 0x20
0034E7BE  0F 85 A8 03 00 00               jne 0x14034eb6c
0034E7C4  44 88 77 35                     mov byte ptr [rdi + 0x35], r14b
0034E7C8  4C 8D A5 C8 44 00 00            lea r12, [rbp + 0x44c8]
0034E7CF  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
0034E7D3  45 84 FE                        test r14b, r15b
0034E7D6  0F 85 20 05 00 00               jne 0x14034ecfc
0034E7DC  66 44 01 B7 10 01 00 00         add word ptr [rdi + 0x110], r14w
0034E7E4  0F B7 97 10 01 00 00            movzx edx, word ptr [rdi + 0x110]
0034E7EB  49 8B 4D 50                     mov rcx, qword ptr [r13 + 0x50]
0034E7EF  49 2B 4D 60                     sub rcx, qword ptr [r13 + 0x60]
0034E7F3  49 89 4D 58                     mov qword ptr [r13 + 0x58], rcx
0034E7F7  66 89 94 24 80 00 00 00         mov word ptr [rsp + 0x80], dx
0034E7FF  49 8B 0C 24                     mov rcx, qword ptr [r12]
0034E803  49 3B CC                        cmp rcx, r12
0034E806  0F 84 9E 01 00 00               je 0x14034e9aa
0034E80C  4C 39 61 08                     cmp qword ptr [rcx + 8], r12
0034E810  75 34                           jne 0x14034e846
0034E812  48 8B 01                        mov rax, qword ptr [rcx]
0034E815  48 39 48 08                     cmp qword ptr [rax + 8], rcx
0034E819  75 2B                           jne 0x14034e846
0034E81B  49 89 04 24                     mov qword ptr [r12], rax
0034E81F  4C 8D 71 E8                     lea r14, [rcx - 0x18]
0034E823  4C 89 60 08                     mov qword ptr [rax + 8], r12
0034E827  41 8B 86 B8 00 00 00            mov eax, dword ptr [r14 + 0xb8]
0034E82E  66 41 39 96 AC 00 00 00         cmp word ptr [r14 + 0xac], dx
0034E836  75 15                           jne 0x14034e84d
0034E838  49 8B 04 24                     mov rax, qword ptr [r12]
0034E83C  4C 39 60 08                     cmp qword ptr [rax + 8], r12
0034E840  0F 84 2F 01 00 00               je 0x14034e975
0034E846  B9 03 00 00 00                  mov ecx, 3
0034E84B  CD 29                           int 0x29
0034E84D  41 8B C7                        mov eax, r15d
0034E850  48 89 31                        mov qword ptr [rcx], rsi
0034E853  83 E0 20                        and eax, 0x20
0034E856  66 41 89 96 AC 00 00 00         mov word ptr [r14 + 0xac], dx
0034E85E  89 44 24 2C                     mov dword ptr [rsp + 0x2c], eax
0034E862  0F 85 82 02 00 00               jne 0x14034eaea
0034E868  49 8B 86 90 00 00 00            mov rax, qword ptr [r14 + 0x90]
0034E86F  48 83 F8 01                     cmp rax, 1
0034E873  0F 86 77 03 00 00               jbe 0x14034ebf0
0034E879  41 8B 86 B8 00 00 00            mov eax, dword ptr [r14 + 0xb8]
0034E880  B9 02 00 00 00                  mov ecx, 2
0034E885  89 84 24 88 00 00 00            mov dword ptr [rsp + 0x88], eax
0034E88C  C1 E8 08                        shr eax, 8
0034E88F  24 FB                           and al, 0xfb
0034E891  0A C1                           or al, cl
0034E893  88 84 24 89 00 00 00            mov byte ptr [rsp + 0x89], al
0034E89A  0F B7 84 24 88 00 00 00         movzx eax, word ptr [rsp + 0x88]
0034E8A2  66 41 89 86 B8 00 00 00         mov word ptr [r14 + 0xb8], ax
0034E8AA  41 38 4D 02                     cmp byte ptr [r13 + 2], cl
0034E8AE  0F 84 98 04 00 00               je 0x14034ed4c
0034E8B4  41 8A D2                        mov dl, r10b
0034E8B7  48 8D 0D 02 8C AE 00            lea rcx, [rip + 0xae8c02]
0034E8BE  E8 FD 99 EF FF                  call 0x1402482c0
0034E8C3  45 8B C7                        mov r8d, r15d
0034E8C6  49 8B D5                        mov rdx, r13
0034E8C9  49 8B CE                        mov rcx, r14
0034E8CC  E8 EF 06 00 00                  call 0x14034efc0
0034E8D1  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0034E8D5  85 C0                           test eax, eax
0034E8D7  0F 85 9C 04 00 00               jne 0x14034ed79
0034E8DD  48 8D 0D DC 8B AE 00            lea rcx, [rip + 0xae8bdc]
0034E8E4  E8 A7 9D EF FF                  call 0x140248690
0034E8E9  44 8A D0                        mov r10b, al
0034E8EC  88 44 24 70                     mov byte ptr [rsp + 0x70], al
0034E8F0  41 8B 8E B8 00 00 00            mov ecx, dword ptr [r14 + 0xb8]
0034E8F7  89 8C 24 88 00 00 00            mov dword ptr [rsp + 0x88], ecx
0034E8FE  39 74 24 2C                     cmp dword ptr [rsp + 0x2c], esi
0034E902  75 3F                           jne 0x14034e943
0034E904  C1 E9 08                        shr ecx, 8
0034E907  33 D2                           xor edx, edx
0034E909  80 E1 F9                        and cl, 0xf9
0034E90C  88 8C 24 89 00 00 00            mov byte ptr [rsp + 0x89], cl
0034E913  49 8B CE                        mov rcx, r14
0034E916  0F B7 84 24 88 00 00 00         movzx eax, word ptr [rsp + 0x88]
0034E91E  66 41 89 86 B8 00 00 00         mov word ptr [r14 + 0xb8], ax
0034E926  E8 B5 1B 00 00                  call 0x1403504e0
0034E92B  44 8A 54 24 70                  mov r10b, byte ptr [rsp + 0x70]
0034E930  39 74 24 20                     cmp dword ptr [rsp + 0x20], esi
0034E934  75 74                           jne 0x14034e9aa
0034E936  0F B7 94 24 80 00 00 00         movzx edx, word ptr [rsp + 0x80]
0034E93E  E9 BC FE FF FF                  jmp 0x14034e7ff
0034E943  49 8B 46 60                     mov rax, qword ptr [r14 + 0x60]
0034E947  48 3B 47 38                     cmp rax, qword ptr [rdi + 0x38]
0034E94B  72 B7                           jb 0x14034e904
0034E94D  49 39 76 68                     cmp qword ptr [r14 + 0x68], rsi
0034E951  75 B1                           jne 0x14034e904
0034E953  80 8C 24 89 00 00 00 06         or byte ptr [rsp + 0x89], 6
0034E95B  0F B7 84 24 88 00 00 00         movzx eax, word ptr [rsp + 0x88]
0034E963  66 41 89 86 B8 00 00 00         mov word ptr [r14 + 0xb8], ax
0034E96B  49 89 5E 20                     mov qword ptr [r14 + 0x20], rbx
0034E96F  49 8D 5E 20                     lea rbx, [r14 + 0x20]
0034E973  EB BB                           jmp 0x14034e930
0034E975  48 89 01                        mov qword ptr [rcx], rax
0034E978  41 BE 01 00 00 00               mov r14d, 1
0034E97E  4C 89 61 08                     mov qword ptr [rcx + 8], r12
0034E982  48 89 48 08                     mov qword ptr [rax + 8], rcx
0034E986  49 89 0C 24                     mov qword ptr [r12], rcx
0034E98A  45 84 FE                        test r14b, r15b
0034E98D  74 1B                           je 0x14034e9aa
0034E98F  45 8A C2                        mov r8b, r10b
0034E992  49 8B D5                        mov rdx, r13
0034E995  48 8B CD                        mov rcx, rbp
0034E998  E8 2B 04 00 00                  call 0x14034edc8
0034E99D  44 8A 54 24 70                  mov r10b, byte ptr [rsp + 0x70]
0034E9A2  85 C0                           test eax, eax
0034E9A4  0F 84 25 FE FF FF               je 0x14034e7cf
0034E9AA  41 F6 C7 20                     test r15b, 0x20
0034E9AE  0F 85 61 01 00 00               jne 0x14034eb15
0034E9B4  44 8B 74 24 24                  mov r14d, dword ptr [rsp + 0x24]
0034E9B9  45 0B F7                        or r14d, r15d
0034E9BC  44 89 74 24 24                  mov dword ptr [rsp + 0x24], r14d
0034E9C1  39 74 24 20                     cmp dword ptr [rsp + 0x20], esi
0034E9C5  74 3C                           je 0x14034ea03
0034E9C7  40 88 77 35                     mov byte ptr [rdi + 0x35], sil
0034E9CB  41 F6 C6 05                     test r14b, 5
0034E9CF  0F 85 E1 03 00 00               jne 0x14034edb6
0034E9D5  8A 54 24 70                     mov dl, byte ptr [rsp + 0x70]
0034E9D9  48 8D 0D E0 8A AE 00            lea rcx, [rip + 0xae8ae0]
0034E9E0  E8 DB 98 EF FF                  call 0x1402482c0
0034E9E5  48 8B CD                        mov rcx, rbp
0034E9E8  E8 1F 0C 00 00                  call 0x14034f60c
0034E9ED  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
0034E9F2  48 83 C4 30                     add rsp, 0x30
0034E9F6  41 5F                           pop r15
0034E9F8  41 5E                           pop r14
0034E9FA  41 5D                           pop r13
0034E9FC  41 5C                           pop r12
0034E9FE  5F                              pop rdi
0034E9FF  5E                              pop rsi
0034EA00  5D                              pop rbp
0034EA01  C3                              ret
0034EA02  CC                              int3
0034EA03  8B 4C 24 28                     mov ecx, dword ptr [rsp + 0x28]
0034EA07  41 83 E7 9C                     and r15d, 0xffffff9c
0034EA0B  8B 47 28                        mov eax, dword ptr [rdi + 0x28]
0034EA0E  41 0B CF                        or ecx, r15d
0034EA11  89 4C 24 28                     mov dword ptr [rsp + 0x28], ecx
0034EA15  3B C8                           cmp ecx, eax
0034EA17  0F 85 BA 02 00 00               jne 0x14034ecd7
0034EA1D  40 88 77 35                     mov byte ptr [rdi + 0x35], sil
0034EA21  41 F6 C6 05                     test r14b, 5
0034EA25  0F 85 6C 03 00 00               jne 0x14034ed97
0034EA2B  8B 47 28                        mov eax, dword ptr [rdi + 0x28]
0034EA2E  85 C0                           test eax, eax
0034EA30  0F 85 6A 03 00 00               jne 0x14034eda0
0034EA36  41 F6 C6 43                     test r14b, 0x43
0034EA3A  74 99                           je 0x14034e9d5
0034EA3C  48 8D 8F 58 01 00 00            lea rcx, [rdi + 0x158]
0034EA43  4C 2B EF                        sub r13, rdi
0034EA46  BA 08 00 00 00                  mov edx, 8
0034EA4B  4A 8B 84 29 B0 FE FF FF         mov rax, qword ptr [rcx + r13 - 0x150]
0034EA53  48 89 01                        mov qword ptr [rcx], rax
0034EA56  48 8D 49 08                     lea rcx, [rcx + 8]
0034EA5A  48 83 EA 01                     sub rdx, 1
0034EA5E  75 EB                           jne 0x14034ea4b
0034EA60  48 8D 87 88 01 00 00            lea rax, [rdi + 0x188]
0034EA67  8D 4A 02                        lea ecx, [rdx + 2]
0034EA6A  48 03 30                        add rsi, qword ptr [rax]
0034EA6D  48 8D 40 08                     lea rax, [rax + 8]
0034EA71  48 83 E9 01                     sub rcx, 1
0034EA75  75 F3                           jne 0x14034ea6a
0034EA77  48 89 B7 50 01 00 00            mov qword ptr [rdi + 0x150], rsi
0034EA7E  E9 52 FF FF FF                  jmp 0x14034e9d5
0034EA83  0F B7 15 76 65 C7 00            movzx edx, word ptr [rip + 0xc76576]
0034EA8A  48 8B C6                        mov rax, rsi
0034EA8D  85 D2                           test edx, edx
0034EA8F  74 16                           je 0x14034eaa7
0034EA91  48 8D 0D 68 8C AE 00            lea rcx, [rip + 0xae8c68]
0034EA98  44 8B C2                        mov r8d, edx
0034EA9B  48 03 01                        add rax, qword ptr [rcx]
0034EA9E  48 8D 49 08                     lea rcx, [rcx + 8]
0034EAA2  4D 2B C6                        sub r8, r14
0034EAA5  75 F4                           jne 0x14034ea9b
0034EAA7  48 39 85 50 48 00 00            cmp qword ptr [rbp + 0x4850], rax
0034EAAE  0F 86 71 02 00 00               jbe 0x14034ed25
0034EAB4  48 39 87 00 02 00 00            cmp qword ptr [rdi + 0x200], rax
0034EABB  0F 84 86 FC FF FF               je 0x14034e747
0034EAC1  48 8D 9D C8 00 00 00            lea rbx, [rbp + 0xc8]
0034EAC8  48 89 87 00 02 00 00            mov qword ptr [rdi + 0x200], rax
0034EACF  48 8B CB                        mov rcx, rbx
0034EAD2  E8 B9 9B EF FF                  call 0x140248690
0034EAD7  8A D0                           mov dl, al
0034EAD9  44 88 75 0C                     mov byte ptr [rbp + 0xc], r14b
0034EADD  48 8B CB                        mov rcx, rbx
0034EAE0  E8 DB 97 EF FF                  call 0x1402482c0
0034EAE5  E9 5D FC FF FF                  jmp 0x14034e747
0034EAEA  49 8B 46 60                     mov rax, qword ptr [r14 + 0x60]
0034EAEE  48 3B 47 38                     cmp rax, qword ptr [rdi + 0x38]
0034EAF2  0F 83 70 FD FF FF               jae 0x14034e868
0034EAF8  49 8B 44 24 08                  mov rax, qword ptr [r12 + 8]
0034EAFD  4C 39 20                        cmp qword ptr [rax], r12
0034EB00  0F 85 40 FD FF FF               jne 0x14034e846
0034EB06  4C 89 21                        mov qword ptr [rcx], r12
0034EB09  48 89 41 08                     mov qword ptr [rcx + 8], rax
0034EB0D  48 89 08                        mov qword ptr [rax], rcx
0034EB10  49 89 4C 24 08                  mov qword ptr [r12 + 8], rcx
0034EB15  48 8B CB                        mov rcx, rbx
0034EB18  48 85 DB                        test rbx, rbx
0034EB1B  0F 84 93 FE FF FF               je 0x14034e9b4
0034EB21  8B 81 98 00 00 00               mov eax, dword ptr [rcx + 0x98]
0034EB27  48 83 C1 E0                     add rcx, -0x20
0034EB2B  48 8B 1B                        mov rbx, qword ptr [rbx]
0034EB2E  BA 01 00 00 00                  mov edx, 1
0034EB33  89 84 24 88 00 00 00            mov dword ptr [rsp + 0x88], eax
0034EB3A  C1 E8 08                        shr eax, 8
0034EB3D  24 F9                           and al, 0xf9
0034EB3F  88 84 24 89 00 00 00            mov byte ptr [rsp + 0x89], al
0034EB46  0F B7 84 24 88 00 00 00         movzx eax, word ptr [rsp + 0x88]
0034EB4E  66 89 81 B8 00 00 00            mov word ptr [rcx + 0xb8], ax
0034EB55  E8 86 19 00 00                  call 0x1403504e0
0034EB5A  8A 44 24 70                     mov al, byte ptr [rsp + 0x70]
0034EB5E  88 44 24 70                     mov byte ptr [rsp + 0x70], al
0034EB62  8B 44 24 20                     mov eax, dword ptr [rsp + 0x20]
0034EB66  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0034EB6A  EB A9                           jmp 0x14034eb15
0034EB6C  B8 0A 00 00 00                  mov eax, 0xa
0034EB71  66 39 87 12 01 00 00            cmp word ptr [rdi + 0x112], ax
0034EB78  0F 87 C1 01 00 00               ja 0x14034ed3f
0034EB7E  40 38 77 36                     cmp byte ptr [rdi + 0x36], sil
0034EB82  0F 84 3C FC FF FF               je 0x14034e7c4
0034EB88  48 8D 95 C8 44 00 00            lea rdx, [rbp + 0x44c8]
0034EB8F  40 88 77 36                     mov byte ptr [rdi + 0x36], sil
0034EB93  4C 8B 02                        mov r8, qword ptr [rdx]
0034EB96  4C 3B C2                        cmp r8, rdx
0034EB99  0F 84 25 FC FF FF               je 0x14034e7c4
0034EB9F  49 8B C0                        mov rax, r8
0034EBA2  49 8B C8                        mov rcx, r8
0034EBA5  4D 8B 00                        mov r8, qword ptr [r8]
0034EBA8  48 8B 40 48                     mov rax, qword ptr [rax + 0x48]
0034EBAC  48 3B 47 38                     cmp rax, qword ptr [rdi + 0x38]
0034EBB0  72 E4                           jb 0x14034eb96
0034EBB2  48 8B 01                        mov rax, qword ptr [rcx]
0034EBB5  48 39 48 08                     cmp qword ptr [rax + 8], rcx
0034EBB9  0F 85 87 FC FF FF               jne 0x14034e846
0034EBBF  4C 8B 49 08                     mov r9, qword ptr [rcx + 8]
0034EBC3  49 39 09                        cmp qword ptr [r9], rcx
0034EBC6  0F 85 7A FC FF FF               jne 0x14034e846
0034EBCC  49 89 01                        mov qword ptr [r9], rax
0034EBCF  4C 89 48 08                     mov qword ptr [rax + 8], r9
0034EBD3  48 8B 02                        mov rax, qword ptr [rdx]
0034EBD6  48 39 50 08                     cmp qword ptr [rax + 8], rdx
0034EBDA  0F 85 66 FC FF FF               jne 0x14034e846
0034EBE0  48 89 01                        mov qword ptr [rcx], rax
0034EBE3  48 89 51 08                     mov qword ptr [rcx + 8], rdx
0034EBE7  48 89 48 08                     mov qword ptr [rax + 8], rcx
0034EBEB  48 89 0A                        mov qword ptr [rdx], rcx
0034EBEE  EB A6                           jmp 0x14034eb96
0034EBF0  41 8B 86 B8 00 00 00            mov eax, dword ptr [r14 + 0xb8]
0034EBF7  A8 0F                           test al, 0xf
0034EBF9  0F 85 7A FC FF FF               jne 0x14034e879
0034EBFF  49 39 76 68                     cmp qword ptr [r14 + 0x68], rsi
0034EC03  0F 85 93 00 00 00               jne 0x14034ec9c
0034EC09  41 8B 86 B8 00 00 00            mov eax, dword ptr [r14 + 0xb8]
0034EC10  48 8D 0D A9 88 AE 00            lea rcx, [rip + 0xae88a9]
0034EC17  89 84 24 88 00 00 00            mov dword ptr [rsp + 0x88], eax
0034EC1E  41 8A D2                        mov dl, r10b
0034EC21  C1 E8 08                        shr eax, 8
0034EC24  0C 06                           or al, 6
0034EC26  88 84 24 89 00 00 00            mov byte ptr [rsp + 0x89], al
0034EC2D  0F B7 84 24 88 00 00 00         movzx eax, word ptr [rsp + 0x88]
0034EC35  66 41 89 86 B8 00 00 00         mov word ptr [r14 + 0xb8], ax
0034EC3D  E8 7E 96 EF FF                  call 0x1402482c0
0034EC42  49 8D 8E 00 FC FF FF            lea rcx, [r14 - 0x400]
0034EC49  E8 D2 41 15 00                  call 0x1404a2e20
0034EC4E  48 8D 0D 6B 88 AE 00            lea rcx, [rip + 0xae886b]
0034EC55  E8 36 9A EF FF                  call 0x140248690
0034EC5A  88 44 24 70                     mov byte ptr [rsp + 0x70], al
0034EC5E  33 D2                           xor edx, edx
0034EC60  41 8B 86 B8 00 00 00            mov eax, dword ptr [r14 + 0xb8]
0034EC67  49 8B CE                        mov rcx, r14
0034EC6A  89 84 24 88 00 00 00            mov dword ptr [rsp + 0x88], eax
0034EC71  C1 E8 08                        shr eax, 8
0034EC74  24 F9                           and al, 0xf9
0034EC76  88 84 24 89 00 00 00            mov byte ptr [rsp + 0x89], al
0034EC7D  0F B7 84 24 88 00 00 00         movzx eax, word ptr [rsp + 0x88]
0034EC85  66 41 89 86 B8 00 00 00         mov word ptr [r14 + 0xb8], ax
0034EC8D  E8 4E 18 00 00                  call 0x1403504e0
0034EC92  44 8A 54 24 70                  mov r10b, byte ptr [rsp + 0x70]
0034EC97  E9 9A FC FF FF                  jmp 0x14034e936
0034EC9C  49 8B 44 24 08                  mov rax, qword ptr [r12 + 8]
0034ECA1  4C 39 20                        cmp qword ptr [rax], r12
0034ECA4  0F 85 9C FB FF FF               jne 0x14034e846
0034ECAA  4C 89 21                        mov qword ptr [rcx], r12
0034ECAD  48 89 41 08                     mov qword ptr [rcx + 8], rax
0034ECB1  48 89 08                        mov qword ptr [rax], rcx
0034ECB4  49 89 4C 24 08                  mov qword ptr [r12 + 8], rcx
0034ECB9  E9 41 FB FF FF                  jmp 0x14034e7ff
0034ECBE  44 8B CE                        mov r9d, esi
0034ECC1  45 33 C0                        xor r8d, r8d
0034ECC4  33 D2                           xor edx, edx
0034ECC6  48 8B CD                        mov rcx, rbp
0034ECC9  E8 4A EB 0F 00                  call 0x14044d818
0034ECCE  44 88 77 34                     mov byte ptr [rdi + 0x34], r14b
0034ECD2  E9 BB FA FF FF                  jmp 0x14034e792
0034ECD7  44 8B F9                        mov r15d, ecx
0034ECDA  41 BE 01 00 00 00               mov r14d, 1
0034ECE0  44 33 F8                        xor r15d, eax
0034ECE3  41 F6 C7 05                     test r15b, 5
0034ECE7  0F 85 A1 00 00 00               jne 0x14034ed8e
0034ECED  44 8A 54 24 70                  mov r10b, byte ptr [rsp + 0x70]
0034ECF2  41 C6 45 02 06                  mov byte ptr [r13 + 2], 6
0034ECF7  E9 D3 FA FF FF                  jmp 0x14034e7cf
0034ECFC  41 0F B6 45 00                  movzx eax, byte ptr [r13]
0034ED01  48 8D 0D E8 23 CC FF            lea rcx, [rip - 0x33dc18]
0034ED08  83 E0 7F                        and eax, 0x7f
0034ED0B  0F B6 14 08                     movzx edx, byte ptr [rax + rcx]
0034ED0F  48 8B CD                        mov rcx, rbp
0034ED12  E8 0D B2 0B 00                  call 0x140409f24
0034ED17  44 8A 54 24 70                  mov r10b, byte ptr [rsp + 0x70]
0034ED1C  49 89 45 68                     mov qword ptr [r13 + 0x68], rax
0034ED20  E9 B7 FA FF FF                  jmp 0x14034e7dc
0034ED25  48 83 8F 00 02 00 00 FF         or qword ptr [rdi + 0x200], 0xffffffffffffffff
0034ED2D  E9 15 FA FF FF                  jmp 0x14034e747
0034ED32  48 8B CD                        mov rcx, rbp
0034ED35  E8 BE FA 32 00                  call 0x14067e7f8
0034ED3A  E9 12 FA FF FF                  jmp 0x14034e751
0034ED3F  90                              nop
0034ED40  66 89 87 12 01 00 00            mov word ptr [rdi + 0x112], ax
0034ED47  E9 32 FE FF FF                  jmp 0x14034eb7e
0034ED4C  49 8B 86 90 00 00 00            mov rax, qword ptr [r14 + 0x90]
0034ED53  49 3B 46 70                     cmp rax, qword ptr [r14 + 0x70]
0034ED57  0F 86 93 FB FF FF               jbe 0x14034e8f0
0034ED5D  49 8B 86 90 00 00 00            mov rax, qword ptr [r14 + 0x90]
0034ED64  49 2B 46 70                     sub rax, qword ptr [r14 + 0x70]
0034ED68  48 3D 00 00 04 00               cmp rax, 0x40000
0034ED6E  0F 82 7C FB FF FF               jb 0x14034e8f0
0034ED74  E9 3B FB FF FF                  jmp 0x14034e8b4
0034ED79  41 80 7D 04 01                  cmp byte ptr [r13 + 4], 1
0034ED7E  0F 85 59 FB FF FF               jne 0x14034e8dd
0034ED84  41 C6 45 04 02                  mov byte ptr [r13 + 4], 2
0034ED89  E9 4F FB FF FF                  jmp 0x14034e8dd
0034ED8E  44 88 77 34                     mov byte ptr [rdi + 0x34], r14b
0034ED92  E9 56 FF FF FF                  jmp 0x14034eced
0034ED97  40 88 77 34                     mov byte ptr [rdi + 0x34], sil
0034ED9B  E9 8B FC FF FF                  jmp 0x14034ea2b
0034EDA0  F0 21 77 28                     lock and dword ptr [rdi + 0x28], esi
0034EDA4  45 33 C0                        xor r8d, r8d
0034EDA7  33 D2                           xor edx, edx
0034EDA9  48 8B CF                        mov rcx, rdi
0034EDAC  E8 5F 05 FF FF                  call 0x14033f310
0034EDB1  E9 80 FC FF FF                  jmp 0x14034ea36
0034EDB6  40 88 77 34                     mov byte ptr [rdi + 0x34], sil
0034EDBA  E9 16 FC FF FF                  jmp 0x14034e9d5
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiProcessWorkingSets(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m3C;
    unsigned int v_stack_m40;
    unsigned int v_stack_m44;
    unsigned int v_stack_m48;
    unsigned __int64 v_stack_p10;
    unsigned __int16 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int8 v_stack_p21;
    unsigned int v_stack_p28;
    unsigned __int8 v_stack_p70;
    unsigned __int8 v_stack_p8;
    unsigned int v_stack_p88;
    unsigned __int8 v_stack_p89;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (48);
    v_rsi = 0;
    if (a1 == (v_rip + 11445710)) goto loc_0034EA83;
loc_0034E747:
    if ((*(unsigned __int8 *)(a1 + 12)) != 0) goto loc_0034ED32;
loc_0034E751:
    result = MiLogPartitionState(a1, a2, a3, a4);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 4)))) & (16)) != 0) goto loc_0034E9ED;
    result = MiComputeAgingPercent(a1, a2, a3, a4);
    result = MiComputeSystemTrimCriteria(a1, a2, a3, a4);
    result = MiLogProcessWorkingSetsStart(a1, a2, (unsigned int)((unsigned int)(result)), a4);
    if ((((unsigned __int8)((unsigned int)((unsigned int)(result)))) & (5)) != 0) goto loc_0034ECBE;
loc_0034E792:
    v_stack_m40 = 0;
    v_stack_m44 = 0;
    if ((((unsigned __int8)((unsigned int)((unsigned int)(result)))) & (2)) != 0) {
    }
    result = ExAcquireSpinLockExclusive(v_rip + 11439381, a2, (unsigned int)((unsigned int)(result)), a4);
    v_stack_p8 = (unsigned __int8)(result);
    if ((((unsigned __int8)((unsigned int)((unsigned int)(result)))) & (32)) != 0) goto loc_0034EB6C;
loc_0034E7C4:
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 17600) + 53) = (unsigned __int8)(v_rsi + 1);
loc_0034E7CF:
    v_stack_m48 = 0;
    if ((((unsigned __int8)(v_rsi + 1)) & ((unsigned __int8)((unsigned int)((unsigned int)(result))))) != 0) goto loc_0034ECFC;
loc_0034E7DC:
    a1 = (*(unsigned __int64 *)(a2 + 80)) - (*(unsigned __int64 *)(a2 + 96));
    *(unsigned __int64 *)(a2 + 88) = a1;
    v_stack_p18 = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 17600) + 272));
loc_0034E7FF:
    if ((*(unsigned __int64 *)(a1 + 17608)) == (a1 + 17608)) goto loc_0034E9AA;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17608) + 8)) != (a1 + 17608)) goto loc_0034E846;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17608)) + 8)) != (*(unsigned __int64 *)(a1 + 17608))) goto loc_0034E846;
    *(unsigned __int64 *)(a1 + 17608) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17608));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17608)) + 8) = a1 + 17608;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 17608) - 24 + 172)) != ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 17600) + 272)))) goto loc_0034E84D;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17608) + 8)) == (a1 + 17608)) goto loc_0034E975;
loc_0034E846:
loc_0034E84D:
    *(unsigned __int64 *)(3) = 0;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))) & (32));
    *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 17608) - 24 + 172) = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 17600) + 272));
    v_stack_m3C = (unsigned int)(result);
    if (condition_is_not_equal) goto loc_0034EAEA;
loc_0034E868:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17608) - 24 + 144)) <= 1) goto loc_0034EBF0;
loc_0034E879:
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 17608) - 24 + 184)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 17608) - 24 + 184))) >> (8));
    result = (unsigned __int8)((result) & (251));
    result = (unsigned __int8)((result) | (2));
    v_stack_p21 = (unsigned __int8)(result);
    *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 17608) - 24 + 184) = (unsigned __int16)(v_stack_p20);
    if ((*(unsigned __int8 *)(a2 + 2)) == 2) goto loc_0034ED4C;
loc_0034E8B4:
    result = MiReleaseSpinLockExclusive(v_rip + 11439106, (unsigned __int8)((unsigned __int8)(result)), (unsigned int)((unsigned int)(result)), a4);
    result = MiTrimOrAgeWorkingSet(*(unsigned __int64 *)(a1 + 17608) - 24, a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a4);
    v_stack_m48 = (unsigned int)(result);
    if ((unsigned int)(result) != 0) goto loc_0034ED79;
loc_0034E8DD:
    result = ExAcquireSpinLockExclusive(v_rip + 11439068, a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a4);
    v_stack_p8 = (unsigned __int8)(result);
loc_0034E8F0:
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 17608) - 24 + 184)));
    if (v_stack_m3C != 0) goto loc_0034E943;
loc_0034E904:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 17608) - 24 + 184))) >> (8));
    a2 = 0;
    a1 = (unsigned __int8)((a1) & (249));
    v_stack_p21 = (unsigned __int8)(a1);
    *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 17608) - 24 + 184) = (unsigned __int16)(v_stack_p20);
    result = MiReturnWsToExpansionList(*(unsigned __int64 *)(a1 + 17608) - 24, a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a4);
loc_0034E930:
    if (v_stack_m48 != 0) goto loc_0034E9AA;
loc_0034E936:
    goto loc_0034E7FF;
loc_0034E943:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17608) - 24 + 96)) < (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17600) + 56))) goto loc_0034E904;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17608) - 24 + 104)) != 0) goto loc_0034E904;
    *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 17608) - 24 + 184) = (unsigned __int16)(v_stack_p20);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17608) - 24 + 32) = 0;
    goto loc_0034E930;
loc_0034E975:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17608) - 24) = v_stack_p20;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17608) - 24 + 8) = a1 + 17608;
    *(unsigned __int64 *)(v_stack_p20 + 8) = *(unsigned __int64 *)(a1 + 17608) - 24;
    *(unsigned __int64 *)(a1 + 17608) = *(unsigned __int64 *)(a1 + 17608) - 24;
    if (((1) & ((unsigned __int8)((unsigned int)((unsigned int)(result))))) == 0) goto loc_0034E9AA;
    result = MiCheckSystemTrimEndCriteria(a1, 0, (unsigned __int8)(v_stack_p8), a4);
    if ((unsigned int)(result) == 0) goto loc_0034E7CF;
loc_0034E9AA:
    if ((((unsigned __int8)((unsigned int)((unsigned int)(result)))) & (32)) != 0) goto loc_0034EB15;
loc_0034E9B4:
    v_r14 = (unsigned int)(((unsigned int)(v_stack_m44)) | ((unsigned int)((unsigned int)((unsigned int)(result)))));
    v_stack_m44 = (unsigned int)(v_r14);
    if (v_stack_m48 == 0) goto loc_0034EA03;
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 17600) + 53) = 0;
    if ((((unsigned __int8)(v_r14)) & (5)) != 0) goto loc_0034EDB6;
loc_0034E9D5:
    result = MiReleaseSpinLockExclusive(v_rip + 11438816, v_stack_p8, (unsigned __int8)(v_stack_p8), a4);
    result = MiLogProcessWorkingSetsStop(a1, v_stack_p8, (unsigned __int8)(v_stack_p8), a4);
loc_0034E9ED:
    v_rsp = (v_rsp) + (48);
    return result;
loc_0034EA03:
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)(result))) & (0xFFFFFF9CULL));
    a1 = (unsigned int)(((unsigned int)(v_stack_p28)) | ((unsigned int)(v_r15)));
    v_stack_p28 = (unsigned int)(a1);
    if (((unsigned int)(a1)) != ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 17600) + 40))))) goto loc_0034ECD7;
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 17600) + 53) = 0;
    if ((((unsigned __int8)(v_r14)) & (5)) != 0) goto loc_0034ED97;
loc_0034EA2B:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 17600) + 40))) != 0) goto loc_0034EDA0;
loc_0034EA36:
    if ((((unsigned __int8)(v_r14)) & (67)) == 0) goto loc_0034E9D5;
    v_r13 = (a2) - (*(unsigned __int64 *)(a1 + 17600));
loc_0034EA4B:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17600) + 344) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17600) + 344 + v_r13 * 1 - 336);
    a2 = (8) - (1);
    if (condition_is_not_equal) goto loc_0034EA4B;
loc_0034EA6A:
    v_rsi = (v_rsi) + (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17600) + 392));
    a1 = (a2 + 2) - (1);
    if (condition_is_not_equal) goto loc_0034EA6A;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17600) + 336) = v_rsi;
    goto loc_0034E9D5;
loc_0034EA83:
    if ((unsigned int)(*(unsigned __int16 *)(v_rip + 13067638)) == 0) goto loc_0034EAA7;
loc_0034EA9B:
    result = (v_rsi) + (*(unsigned __int64 *)(v_rip + 11439208));
    a3 = ((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rip + 13067638)))) - (v_r14);
    if (condition_is_not_equal) goto loc_0034EA9B;
loc_0034EAA7:
    if ((*(unsigned __int64 *)(a1 + 18512)) <= result) goto loc_0034ED25;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17600) + 512)) == result) goto loc_0034E747;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17600) + 512) = result;
    result = ExAcquireSpinLockExclusive(a1 + 200, *(unsigned __int16 *)(v_rip + 13067638), a3, a4);
    *(unsigned __int8 *)(a1 + 12) = (unsigned __int8)(v_r14);
    result = MiReleaseSpinLockExclusive(a1 + 200, (unsigned __int8)(result), a3, a4);
    goto loc_0034E747;
loc_0034EAEA:
    if ((*(unsigned __int64 *)(v_r14 + 96)) >= (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17600) + 56))) goto loc_0034E868;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17608 + 8))) != (a1 + 17608)) goto loc_0034E846;
    *(unsigned __int64 *)(a1 + 200) = a1 + 17608;
    *(unsigned __int64 *)(a1 + 200 + 8) = *(unsigned __int64 *)(a1 + 17608 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17608 + 8)) = a1 + 200;
    *(unsigned __int64 *)(a1 + 17608 + 8) = a1 + 200;
loc_0034EB15:
    if (a1 + 200 == 0) goto loc_0034E9B4;
    a1 = (a1 + 200) + (-32);
    v_stack_p88 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 200 + 152)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 200 + 152))) >> (8));
    result = (unsigned __int8)((result) & (249));
    v_stack_p89 = (unsigned __int8)(result);
    *(unsigned __int16 *)(a1 + 184) = (unsigned __int16)(v_stack_p88);
    result = MiReturnWsToExpansionList(a1, 1, a3, a4);
    v_stack_p70 = (unsigned __int8)(v_stack_p70);
    v_stack_p20 = (unsigned int)((unsigned int)(v_stack_p20));
    goto loc_0034EB15;
loc_0034EB6C:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 17600) + 274)) > 10) goto loc_0034ED3F;
loc_0034EB7E:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 17600) + 54)) == ((unsigned __int8)(v_rsi))) goto loc_0034E7C4;
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 17600) + 54) = (unsigned __int8)(v_rsi);
loc_0034EB96:
    if ((*(unsigned __int64 *)(a1 + 17608)) == (a1 + 17608)) goto loc_0034E7C4;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17608) + 72)) < (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17600) + 56))) goto loc_0034EB96;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17608)) + 8)) != (*(unsigned __int64 *)(a1 + 17608))) goto loc_0034E846;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17608) + 8))) != (*(unsigned __int64 *)(a1 + 17608))) goto loc_0034E846;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17608) + 8)) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17608));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17608)) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17608) + 8);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17608) + 8)) != (a1 + 17608)) goto loc_0034E846;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17608)) = *(unsigned __int64 *)(a1 + 17608);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17608) + 8) = a1 + 17608;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17608) + 8) = *(unsigned __int64 *)(a1 + 17608);
    *(unsigned __int64 *)(a1 + 17608) = *(unsigned __int64 *)(a1 + 17608);
    goto loc_0034EB96;
loc_0034EBF0:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_r14 + 184)))) & (15)) != 0) goto loc_0034E879;
    if ((*(unsigned __int64 *)(v_r14 + 104)) != v_rsi) goto loc_0034EC9C;
    v_stack_p88 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 184)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r14 + 184))) >> (8));
    result = (unsigned __int8)((result) | (6));
    v_stack_p89 = (unsigned __int8)(result);
    *(unsigned __int16 *)(v_r14 + 184) = (unsigned __int16)(v_stack_p88);
    result = MiReleaseSpinLockExclusive(v_rip + 11438249, (unsigned __int8)(v_stack_p8), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17608)), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17608) + 8));
    result = KeRetryOutswapProcess(v_r14 - 1024, (unsigned __int8)(v_stack_p8), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17608)), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17608) + 8));
    result = ExAcquireSpinLockExclusive(v_rip + 11438187, (unsigned __int8)(v_stack_p8), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17608)), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17608) + 8));
    v_stack_p70 = (unsigned __int8)(result);
    a2 = 0;
    v_stack_p88 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 184)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r14 + 184))) >> (8));
    result = (unsigned __int8)((result) & (249));
    v_stack_p89 = (unsigned __int8)(result);
    *(unsigned __int16 *)(v_r14 + 184) = (unsigned __int16)(v_stack_p88);
    result = MiReturnWsToExpansionList(v_r14, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17608)), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17608) + 8));
    goto loc_0034E936;
loc_0034EC9C:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17608 + 8))) != (a1 + 17608)) goto loc_0034E846;
    *(unsigned __int64 *)(v_r14) = a1 + 17608;
    *(unsigned __int64 *)(v_r14 + 8) = *(unsigned __int64 *)(a1 + 17608 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17608 + 8)) = v_r14;
    *(unsigned __int64 *)(a1 + 17608 + 8) = v_r14;
    goto loc_0034E7FF;
loc_0034ECBE:
    a3 = 0;
    a2 = 0;
    result = MiDrainZeroLookasides(a1, a2, a3, (unsigned int)((unsigned int)(v_rsi)));
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 17600) + 52) = (unsigned __int8)(v_r14);
    goto loc_0034E792;
loc_0034ECD7:
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)(a1))) ^ ((unsigned int)(result)));
    if ((((unsigned __int8)(v_r15)) & (5)) != 0) goto loc_0034ED8E;
loc_0034ECED:
    *(unsigned __int8 *)(v_r13 + 2) = 6;
    goto loc_0034E7CF;
loc_0034ECFC:
    result = (unsigned int)((*(unsigned __int8 *)(v_r13)) & (127));
    result = MiOrderTrimList(a1, *(unsigned __int8 *)(result + v_rip - 3398680 * 1), a3, (unsigned int)((unsigned int)(v_rsi)));
    *(unsigned __int64 *)(v_r13 + 104) = result;
    goto loc_0034E7DC;
loc_0034ED25:
    goto loc_0034E747;
loc_0034ED32:
    result = MiInitializeWorkingSetManagerParameters(a1, *(unsigned __int8 *)(result + v_rip - 3398680 * 1), a3, (unsigned int)((unsigned int)(v_rsi)));
    goto loc_0034E751;
loc_0034ED3F:
    *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 17600) + 274) = (unsigned __int16)(result);
    goto loc_0034EB7E;
loc_0034ED4C:
    if ((*(unsigned __int64 *)(1 + 144)) <= (*(unsigned __int64 *)(1 + 112))) goto loc_0034E8F0;
    result = (*(unsigned __int64 *)(1 + 144)) - (*(unsigned __int64 *)(1 + 112));
    if (result < 0x40000ULL) goto loc_0034E8F0;
    goto loc_0034E8B4;
loc_0034ED79:
    if ((*(unsigned __int8 *)(v_r13 + 4)) != 1) goto loc_0034E8DD;
    *(unsigned __int8 *)(v_r13 + 4) = 2;
    goto loc_0034E8DD;
loc_0034ED8E:
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 17600) + 52) = 1;
    goto loc_0034ECED;
loc_0034ED97:
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 17600) + 52) = (unsigned __int8)(v_rsi);
    goto loc_0034EA2B;
loc_0034EDA0:
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(*(unsigned __int64 *)(a1 + 17600), a2, a3, (unsigned int)((unsigned int)(v_rsi)));
    goto loc_0034EA36;
loc_0034EDB6:
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 17600) + 52) = (unsigned __int8)(v_rsi);
    goto loc_0034E9D5;
}
```

## 5. (Beta) C Style

```c
int64_t MiProcessWorkingSets(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m3C;
    uint32_t v_stack_m40;
    uint32_t v_stack_m44;
    uint32_t v_stack_m48;
    uint64_t v_stack_p10;
    uint16_t v_stack_p18;
    uint32_t v_stack_p20;
    uint8_t v_stack_p21;
    uint32_t v_stack_p28;
    uint8_t v_stack_p70;
    uint8_t v_stack_p8;
    uint32_t v_stack_p88;
    uint8_t v_stack_p89;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (48);
    local_rsi = 0;
    if (Arg1 == (v_rip + 11445710)) goto loc_0034EA83;
loc_0034E747:
    if ((*(uint8_t *)(arg1 + 0xC)) != 0) goto loc_0034ED32;
loc_0034E751:
    result = MiLogPartitionState(Arg1, Arg2, a3, a4);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)))) & (16)) != 0) goto loc_0034E9ED;
    result = MiComputeAgingPercent(Arg1, Arg2, a3, a4);
    result = MiComputeSystemTrimCriteria(Arg1, Arg2, a3, a4);
    result = MiLogProcessWorkingSetsStart(Arg1, Arg2, (uint32_t)((uint32_t)(result)), a4);
    if ((((uint8_t)((uint32_t)((uint32_t)(result)))) & (5)) != 0) goto loc_0034ECBE;
loc_0034E792:
    v_stack_m40 = 0;
    v_stack_m44 = 0;
    if ((((uint8_t)((uint32_t)((uint32_t)(result)))) & (2)) != 0) {
    }
    result = ExAcquireSpinLockExclusive(v_rip + 11439381, Arg2, (uint32_t)((uint32_t)(result)), a4);
    v_stack_p8 = (uint8_t)(result);
    if ((((uint8_t)((uint32_t)((uint32_t)(result)))) & (32)) != 0) goto loc_0034EB6C;
loc_0034E7C4:
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x35) = (uint8_t)(local_rsi + 1);
loc_0034E7CF:
    v_stack_m48 = 0;
    if ((((uint8_t)(local_rsi + 1)) & ((uint8_t)((uint32_t)((uint32_t)(result))))) != 0) goto loc_0034ECFC;
loc_0034E7DC:
    Arg1 = (*(uint64_t *)(arg2 + 0x50)) - (*(uint64_t *)(arg2 + 0x60));
    *(void **)(arg2 + 0x58) = Arg1;
    v_stack_p18 = (uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x110));
loc_0034E7FF:
    if ((*(uint64_t *)(arg1 + 0x44C8)) == (Arg1 + 17608)) goto loc_0034E9AA;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x44C8) + 0x8)) != (Arg1 + 17608)) goto loc_0034E846;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x44C8)) + 0x8)) != (*(uint64_t *)(arg1 + 0x44C8))) goto loc_0034E846;
    *(uint64_t *)(arg1 + 0x44C8) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x44C8));
    *(void **)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x44C8)) + 0x8) = Arg1 + 17608;
    if ((*(uint16_t *)(*(uint64_t *)(arg1 + 0x44C8) - 0x18 + 0xAC)) != ((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x110)))) goto loc_0034E84D;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x44C8) + 0x8)) == (Arg1 + 17608)) goto loc_0034E975;
loc_0034E846:
loc_0034E84D:
    *(uint64_t *)(3) = 0;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))) & (32));
    *(uint16_t *)(*(uint64_t *)(arg1 + 0x44C8) - 0x18 + 0xAC) = (uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x110));
    v_stack_m3C = (uint32_t)(result);
    if (condition_is_not_equal) goto loc_0034EAEA;
loc_0034E868:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x44C8) - 0x18 + 0x90)) <= 1) goto loc_0034EBF0;
loc_0034E879:
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x44C8) - 0x18 + 0xB8)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x44C8) - 0x18 + 0xB8))) >> (8));
    result = (uint8_t)((result) & (251));
    result = (uint8_t)((result) | (2));
    v_stack_p21 = (uint8_t)(result);
    *(uint16_t *)(*(uint64_t *)(arg1 + 0x44C8) - 0x18 + 0xB8) = (uint16_t)(v_stack_p20);
    if ((*(uint8_t *)(arg2 + 0x2)) == 2) goto loc_0034ED4C;
loc_0034E8B4:
    result = MiReleaseSpinLockExclusive(v_rip + 11439106, (uint8_t)((uint8_t)(result)), (uint32_t)((uint32_t)(result)), a4);
    result = MiTrimOrAgeWorkingSet(*(uint64_t *)(arg1 + 0x44C8) - 24, Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), a4);
    v_stack_m48 = (uint32_t)(result);
    if ((uint32_t)(result) != 0) goto loc_0034ED79;
loc_0034E8DD:
    result = ExAcquireSpinLockExclusive(v_rip + 11439068, Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), a4);
    v_stack_p8 = (uint8_t)(result);
loc_0034E8F0:
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x44C8) - 0x18 + 0xB8)));
    if (v_stack_m3C != 0) goto loc_0034E943;
loc_0034E904:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x44C8) - 0x18 + 0xB8))) >> (8));
    Arg2 = 0;
    Arg1 = (uint8_t)((Arg1) & (249));
    v_stack_p21 = (uint8_t)(Arg1);
    *(uint16_t *)(*(uint64_t *)(arg1 + 0x44C8) - 0x18 + 0xB8) = (uint16_t)(v_stack_p20);
    result = MiReturnWsToExpansionList(*(uint64_t *)(arg1 + 0x44C8) - 24, Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), a4);
loc_0034E930:
    if (v_stack_m48 != 0) goto loc_0034E9AA;
loc_0034E936:
    goto loc_0034E7FF;
loc_0034E943:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x44C8) - 0x18 + 0x60)) < (*(uint64_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x38))) goto loc_0034E904;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x44C8) - 0x18 + 0x68)) != 0) goto loc_0034E904;
    *(uint16_t *)(*(uint64_t *)(arg1 + 0x44C8) - 0x18 + 0xB8) = (uint16_t)(v_stack_p20);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x44C8) - 0x18 + 0x20) = 0;
    goto loc_0034E930;
loc_0034E975:
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x44C8) - 0x18) = v_stack_p20;
    *(void **)(*(uint64_t *)(arg1 + 0x44C8) - 0x18 + 0x8) = Arg1 + 17608;
    *(uint64_t *)(v_stack_p20 + 0x8) = *(uint64_t *)(arg1 + 0x44C8) - 24;
    *(uint64_t *)(arg1 + 0x44C8) = *(uint64_t *)(arg1 + 0x44C8) - 24;
    if (((1) & ((uint8_t)((uint32_t)((uint32_t)(result))))) == 0) goto loc_0034E9AA;
    result = MiCheckSystemTrimEndCriteria(Arg1, 0, (uint8_t)(v_stack_p8), a4);
    if ((uint32_t)(result) == 0) goto loc_0034E7CF;
loc_0034E9AA:
    if ((((uint8_t)((uint32_t)((uint32_t)(result)))) & (32)) != 0) goto loc_0034EB15;
loc_0034E9B4:
    local_r14 = (uint32_t)(((uint32_t)(v_stack_m44)) | ((uint32_t)((uint32_t)((uint32_t)(result)))));
    v_stack_m44 = (uint32_t)(local_r14);
    if (v_stack_m48 == 0) goto loc_0034EA03;
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x35) = 0;
    if ((((uint8_t)(local_r14)) & (5)) != 0) goto loc_0034EDB6;
loc_0034E9D5:
    result = MiReleaseSpinLockExclusive(v_rip + 11438816, v_stack_p8, (uint8_t)(v_stack_p8), a4);
    result = MiLogProcessWorkingSetsStop(Arg1, v_stack_p8, (uint8_t)(v_stack_p8), a4);
loc_0034E9ED:
    local_rsp = (local_rsp) + (48);
    return result;
loc_0034EA03:
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)(result))) & (0xFFFFFF9CULL));
    Arg1 = (uint32_t)(((uint32_t)(v_stack_p28)) | ((uint32_t)(local_r15)));
    v_stack_p28 = (uint32_t)(Arg1);
    if (((uint32_t)(Arg1)) != ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x28))))) goto loc_0034ECD7;
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x35) = 0;
    if ((((uint8_t)(local_r14)) & (5)) != 0) goto loc_0034ED97;
loc_0034EA2B:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x28))) != 0) goto loc_0034EDA0;
loc_0034EA36:
    if ((((uint8_t)(local_r14)) & (67)) == 0) goto loc_0034E9D5;
    local_r13 = (Arg2) - (*(uint64_t *)(arg1 + 0x44C0));
loc_0034EA4B:
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x158) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x158 + local_r13 * 1 - 0x150);
    Arg2 = (8) - (1);
    if (condition_is_not_equal) goto loc_0034EA4B;
loc_0034EA6A:
    local_rsi = (local_rsi) + (*(uint64_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x188));
    Arg1 = (Arg2 + 2) - (1);
    if (condition_is_not_equal) goto loc_0034EA6A;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x150) = local_rsi;
    goto loc_0034E9D5;
loc_0034EA83:
    if ((uint32_t)(*(uint16_t *)(v_rip + 0xC76576)) == 0) goto loc_0034EAA7;
loc_0034EA9B:
    result = (local_rsi) + (*(uint64_t *)(v_rip + 0xAE8C68));
    a3 = ((uint32_t)((uint32_t)(*(uint16_t *)(v_rip + 0xC76576)))) - (local_r14);
    if (condition_is_not_equal) goto loc_0034EA9B;
loc_0034EAA7:
    if ((*(uint64_t *)(arg1 + 0x4850)) <= result) goto loc_0034ED25;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x200)) == result) goto loc_0034E747;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x200) = result;
    result = ExAcquireSpinLockExclusive(Arg1 + 200, *(uint16_t *)(v_rip + 0xC76576), a3, a4);
    *(uint8_t *)(arg1 + 0xC) = (uint8_t)(local_r14);
    result = MiReleaseSpinLockExclusive(Arg1 + 200, (uint8_t)(result), a3, a4);
    goto loc_0034E747;
loc_0034EAEA:
    if ((*(uint64_t *)(local_r14 + 0x60)) >= (*(uint64_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x38))) goto loc_0034E868;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x44C8 + 0x8))) != (Arg1 + 17608)) goto loc_0034E846;
    *(void **)(arg1 + 0xC8) = Arg1 + 17608;
    *(uint64_t *)(arg1 + 0xC8 + 0x8) = *(uint64_t *)(arg1 + 0x44C8 + 0x8);
    *(void **)(*(uint64_t *)(arg1 + 0x44C8 + 0x8)) = Arg1 + 200;
    *(void **)(arg1 + 0x44C8 + 0x8) = Arg1 + 200;
loc_0034EB15:
    if (Arg1 + 200 == 0) goto loc_0034E9B4;
    Arg1 = (Arg1 + 200) + (-32);
    v_stack_p88 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xC8 + 0x98)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xC8 + 0x98))) >> (8));
    result = (uint8_t)((result) & (249));
    v_stack_p89 = (uint8_t)(result);
    *(uint16_t *)(arg1 + 0xB8) = (uint16_t)(v_stack_p88);
    result = MiReturnWsToExpansionList(Arg1, 1, a3, a4);
    v_stack_p70 = (uint8_t)(v_stack_p70);
    v_stack_p20 = (uint32_t)((uint32_t)(v_stack_p20));
    goto loc_0034EB15;
loc_0034EB6C:
    if ((*(uint16_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x112)) > 10) goto loc_0034ED3F;
loc_0034EB7E:
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x36)) == ((uint8_t)(local_rsi))) goto loc_0034E7C4;
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x36) = (uint8_t)(local_rsi);
loc_0034EB96:
    if ((*(uint64_t *)(arg1 + 0x44C8)) == (Arg1 + 17608)) goto loc_0034E7C4;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x44C8) + 0x48)) < (*(uint64_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x38))) goto loc_0034EB96;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x44C8)) + 0x8)) != (*(uint64_t *)(arg1 + 0x44C8))) goto loc_0034E846;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x44C8) + 0x8))) != (*(uint64_t *)(arg1 + 0x44C8))) goto loc_0034E846;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x44C8) + 0x8)) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x44C8));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x44C8)) + 0x8) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x44C8) + 0x8);
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x44C8) + 0x8)) != (Arg1 + 17608)) goto loc_0034E846;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x44C8)) = *(uint64_t *)(arg1 + 0x44C8);
    *(void **)(*(uint64_t *)(arg1 + 0x44C8) + 0x8) = Arg1 + 17608;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x44C8) + 0x8) = *(uint64_t *)(arg1 + 0x44C8);
    *(uint64_t *)(arg1 + 0x44C8) = *(uint64_t *)(arg1 + 0x44C8);
    goto loc_0034EB96;
loc_0034EBF0:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_r14 + 0xB8)))) & (15)) != 0) goto loc_0034E879;
    if ((*(uint64_t *)(local_r14 + 0x68)) != local_rsi) goto loc_0034EC9C;
    v_stack_p88 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0xB8)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r14 + 0xB8))) >> (8));
    result = (uint8_t)((result) | (6));
    v_stack_p89 = (uint8_t)(result);
    *(uint16_t *)(local_r14 + 0xB8) = (uint16_t)(v_stack_p88);
    result = MiReleaseSpinLockExclusive(v_rip + 11438249, (uint8_t)(v_stack_p8), *(uint64_t *)(*(uint64_t *)(arg1 + 0x44C8)), *(uint64_t *)(*(uint64_t *)(arg1 + 0x44C8) + 0x8));
    result = KeRetryOutswapProcess(local_r14 - 1024, (uint8_t)(v_stack_p8), *(uint64_t *)(*(uint64_t *)(arg1 + 0x44C8)), *(uint64_t *)(*(uint64_t *)(arg1 + 0x44C8) + 0x8));
    result = ExAcquireSpinLockExclusive(v_rip + 11438187, (uint8_t)(v_stack_p8), *(uint64_t *)(*(uint64_t *)(arg1 + 0x44C8)), *(uint64_t *)(*(uint64_t *)(arg1 + 0x44C8) + 0x8));
    v_stack_p70 = (uint8_t)(result);
    Arg2 = 0;
    v_stack_p88 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0xB8)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r14 + 0xB8))) >> (8));
    result = (uint8_t)((result) & (249));
    v_stack_p89 = (uint8_t)(result);
    *(uint16_t *)(local_r14 + 0xB8) = (uint16_t)(v_stack_p88);
    result = MiReturnWsToExpansionList(local_r14, Arg2, *(uint64_t *)(*(uint64_t *)(arg1 + 0x44C8)), *(uint64_t *)(*(uint64_t *)(arg1 + 0x44C8) + 0x8));
    goto loc_0034E936;
loc_0034EC9C:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x44C8 + 0x8))) != (Arg1 + 17608)) goto loc_0034E846;
    *(void **)(local_r14) = Arg1 + 17608;
    *(uint64_t *)(local_r14 + 0x8) = *(uint64_t *)(arg1 + 0x44C8 + 0x8);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x44C8 + 0x8)) = local_r14;
    *(uint64_t *)(arg1 + 0x44C8 + 0x8) = local_r14;
    goto loc_0034E7FF;
loc_0034ECBE:
    a3 = 0;
    Arg2 = 0;
    result = MiDrainZeroLookasides(Arg1, Arg2, a3, (uint32_t)((uint32_t)(local_rsi)));
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x34) = (uint8_t)(local_r14);
    goto loc_0034E792;
loc_0034ECD7:
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) ^ ((uint32_t)(result)));
    if ((((uint8_t)(local_r15)) & (5)) != 0) goto loc_0034ED8E;
loc_0034ECED:
    *(uint8_t *)(local_r13 + 0x2) = 6;
    goto loc_0034E7CF;
loc_0034ECFC:
    result = (uint32_t)((*(uint8_t *)(local_r13)) & (127));
    result = MiOrderTrimList(Arg1, *(uint8_t *)(result + v_rip - 0x33DC18 * 1), a3, (uint32_t)((uint32_t)(local_rsi)));
    *(uint64_t *)(local_r13 + 0x68) = result;
    goto loc_0034E7DC;
loc_0034ED25:
    goto loc_0034E747;
loc_0034ED32:
    result = MiInitializeWorkingSetManagerParameters(Arg1, *(uint8_t *)(result + v_rip - 0x33DC18 * 1), a3, (uint32_t)((uint32_t)(local_rsi)));
    goto loc_0034E751;
loc_0034ED3F:
    *(uint16_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x112) = (uint16_t)(result);
    goto loc_0034EB7E;
loc_0034ED4C:
    if ((*(uint64_t *)(1 + 0x90)) <= (*(uint64_t *)(1 + 0x70))) goto loc_0034E8F0;
    result = (*(uint64_t *)(1 + 0x90)) - (*(uint64_t *)(1 + 0x70));
    if (result < 0x40000ULL) goto loc_0034E8F0;
    goto loc_0034E8B4;
loc_0034ED79:
    if ((*(uint8_t *)(local_r13 + 0x4)) != 1) goto loc_0034E8DD;
    *(uint8_t *)(local_r13 + 0x4) = 2;
    goto loc_0034E8DD;
loc_0034ED8E:
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x34) = 1;
    goto loc_0034ECED;
loc_0034ED97:
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x34) = (uint8_t)(local_rsi);
    goto loc_0034EA2B;
loc_0034EDA0:
    a3 = 0;
    Arg2 = 0;
    result = KeSetEvent(*(uint64_t *)(arg1 + 0x44C0), Arg2, a3, (uint32_t)((uint32_t)(local_rsi)));
    goto loc_0034EA36;
loc_0034EDB6:
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x34) = (uint8_t)(local_rsi);
    goto loc_0034E9D5;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0xC` | `8` | `R` |
| `Arg1` | `+ 0xC` | `8` | `W` |
| `Arg1` | `+ 0xC8` | `64` | `R` |
| `Arg1` | `+ 0x44C0` | `64` | `R` |
| `Arg1` | `+ 0x44C8` | `64` | `R` |
| `Arg1` | `+ 0x4850` | `64` | `R` |
| `Arg2` | `+ 0x0` | `8` | `R` |
| `Arg2` | `+ 0x2` | `8` | `R` |
| `Arg2` | `+ 0x2` | `8` | `W` |
| `Arg2` | `+ 0x4` | `8` | `R` |
| `Arg2` | `+ 0x4` | `8` | `W` |
| `Arg2` | `+ 0x50` | `64` | `R` |
| `Arg2` | `+ 0x58` | `64` | `W` |
| `Arg2` | `+ 0x60` | `64` | `R` |
| `Arg2` | `+ 0x68` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0034E710&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
