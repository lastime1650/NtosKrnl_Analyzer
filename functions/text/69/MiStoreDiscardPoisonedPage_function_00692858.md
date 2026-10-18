# MiStoreDiscardPoisonedPage

- RVA: `0x00692858`–`0x00692D89` (길이 `1,329` bytes)
- VA: `0x0000000140692858`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CC31C`
- 디코드: `336`개 명령, `1,329/1,329` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **30**; 고유 호출 대상: **27**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x006928CB` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00692944` → [MiGetTopLevelPfn](../2B/MiGetTopLevelPfn_function_002B44E0.md) (function, `0x002B44E0`)
- `0x00692954` → [MiGetPageTablePfnBuddyRaw](../2B/MiGetPageTablePfnBuddyRaw_function_002B4470.md) (function, `0x002B4470`)
- `0x0069296E` → [MiIsStoreProcess](../2B/MiIsStoreProcess_function_002B62E0.md) (function, `0x002B62E0`)
- `0x0069298B` → [MiAreChargesNeededToLockPage](../31/MiAreChargesNeededToLockPage_function_00318720.md) (function, `0x00318720`)
- `0x006929AE` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)
- `0x006929BB` → [MiMakeDemandZeroPte](../33/MiMakeDemandZeroPte_function_00337A00.md) (function, `0x00337A00`)
- `0x006929DF` → [KiStackAttachProcess](../21/KiStackAttachProcess_function_00216820.md) (function, `0x00216820`)
- `0x006929EF` → [MiLockVadTree](../27/MiLockVadTree_function_0027C0F0.md) (function, `0x0027C0F0`)
- `0x006929FA` → [MiLocateAddress](../31/MiLocateAddress_function_003168D0.md) (function, `0x003168D0`)
- `0x00692A17` → [MiTryLockVad](../42/MiTryLockVad_function_0042ABFC.md) (function, `0x0042ABFC`)
- `0x00692A45` → [MiUnlockVadTree](../29/MiUnlockVadTree_function_00297020.md) (function, `0x00297020`)
- `0x00692A5C` → [MiUnlockVadTree](../29/MiUnlockVadTree_function_00297020.md) (function, `0x00297020`)
- `0x00692AD4` → [MiDecommitInitializePacket](../24/MiDecommitInitializePacket_function_00242F30.md) (function, `0x00242F30`)
- `0x00692AE8` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x00692B05` → [MiMakeSystemAddressValid](../27/MiMakeSystemAddressValid_function_0027FF70.md) (function, `0x0027FF70`)
- `0x00692B7D` → [MiAreChargesNeededToLockPage](../31/MiAreChargesNeededToLockPage_function_00318720.md) (function, `0x00318720`)
- `0x00692B9F` → [MiGetWsleContents](../31/MiGetWsleContents_function_00316540.md) (function, `0x00316540`)
- `0x00692BD5` → [MiDecommitHandleValidPte](../24/MiDecommitHandleValidPte_function_00241A50.md) (function, `0x00241A50`)
- `0x00692BE2` → [MiDecommitPagesTail](../27/MiDecommitPagesTail_function_002790FC.md) (function, `0x002790FC`)
- `0x00692C11` → [MiLockTransitionLeafPageEx](../40/MiLockTransitionLeafPageEx_function_00405884.md) (function, `0x00405884`)
- `0x00692C4C` → [MiAreChargesNeededToLockPage](../31/MiAreChargesNeededToLockPage_function_00318720.md) (function, `0x00318720`)
- `0x00692C9F` → [MiDeleteTransitionPte](../37/MiDeleteTransitionPte_function_00371B70.md) (function, `0x00371B70`)
- `0x00692CD7` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x00692CF0` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x00692D00` → [MiUnlockVad](../2A/MiUnlockVad_function_002A59C8.md) (function, `0x002A59C8`)
- `0x00692D27` → [KiCheckForKernelApcDelivery](../2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x00692D35` → [KiUnstackDetachProcess](../21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x00692D57` → [MiStoreLogDiscardPoisonedPage](MiStoreLogDiscardPoisonedPage_function_00692D90.md) (function, `0x00692D90`)
- `0x00692D68` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [MmMarkPhysicalMemoryAsBad](../67/MmMarkPhysicalMemoryAsBad_function_0067AA50.md) at `0x0067ADC1`

### Static image references
- `0x00692877` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00692858  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0069285D  55                              push rbp
0069285E  56                              push rsi
0069285F  57                              push rdi
00692860  41 54                           push r12
00692862  41 55                           push r13
00692864  41 56                           push r14
00692866  41 57                           push r15
00692868  48 8D AC 24 20 FF FF FF         lea rbp, [rsp - 0xe0]
00692870  48 81 EC E0 01 00 00            sub rsp, 0x1e0
00692877  48 8B 05 C2 7E 77 00            mov rax, qword ptr [rip + 0x777ec2]
0069287E  48 33 C4                        xor rax, rsp
00692881  48 89 85 D0 00 00 00            mov qword ptr [rbp + 0xd0], rax
00692888  0F 57 C0                        xorps xmm0, xmm0
0069288B  48 89 4D 80                     mov qword ptr [rbp - 0x80], rcx
0069288F  0F 57 C9                        xorps xmm1, xmm1
00692892  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00692896  49 8B D8                        mov rbx, r8
00692899  48 8B FA                        mov rdi, rdx
0069289C  33 C0                           xor eax, eax
0069289E  33 D2                           xor edx, edx
006928A0  41 B8 E0 00 00 00               mov r8d, 0xe0
006928A6  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
006928AA  0F 11 85 A0 00 00 00            movups xmmword ptr [rbp + 0xa0], xmm0
006928B1  0F 11 85 B0 00 00 00            movups xmmword ptr [rbp + 0xb0], xmm0
006928B8  0F 11 85 C0 00 00 00            movups xmmword ptr [rbp + 0xc0], xmm0
006928BF  0F 11 4D 88                     movups xmmword ptr [rbp - 0x78], xmm1
006928C3  0F 11 4D 98                     movups xmmword ptr [rbp - 0x68], xmm1
006928C7  0F 11 4D A8                     movups xmmword ptr [rbp - 0x58], xmm1
006928CB  E8 70 43 03 00                  call 0x1406c6c40
006928D0  48 8B 77 08                     mov rsi, qword ptr [rdi + 8]
006928D4  48 B8 00 00 00 00 00 00 00 80   movabs rax, 0x8000000000000000
006928DE  48 0B F0                        or rsi, rax
006928E1  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
006928EB  4C 8B E6                        mov r12, rsi
006928EE  49 C1 E4 19                     shl r12, 0x19
006928F2  48 8B C0                        mov rax, rax
006928F5  48 C1 E0 19                     shl rax, 0x19
006928F9  45 33 F6                        xor r14d, r14d
006928FC  4C 2B E0                        sub r12, rax
006928FF  C6 44 24 50 11                  mov byte ptr [rsp + 0x50], 0x11
00692904  49 C1 FC 10                     sar r12, 0x10
00692908  4C 89 64 24 60                  mov qword ptr [rsp + 0x60], r12
0069290D  4C 89 74 24 70                  mov qword ptr [rsp + 0x70], r14
00692912  4C 89 74 24 58                  mov qword ptr [rsp + 0x58], r14
00692917  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00692921  48 8B C0                        mov rax, rax
00692924  48 8B CF                        mov rcx, rdi
00692927  48 2B C8                        sub rcx, rax
0069292A  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
00692934  48 C1 F9 04                     sar rcx, 4
00692938  48 0F AF C8                     imul rcx, rax
0069293C  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
00692941  48 8B CF                        mov rcx, rdi
00692944  E8 97 1B C2 FF                  call 0x1402b44e0
00692949  4C 8B C0                        mov r8, rax
0069294C  48 3B C7                        cmp rax, rdi
0069294F  74 26                           je 0x140692977
00692951  48 8B C8                        mov rcx, rax
00692954  E8 17 1B C2 FF                  call 0x1402b4470
00692959  4C 8B E8                        mov r13, rax
0069295C  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00692966  F0 49 21 40 18                  lock and qword ptr [r8 + 0x18], rax
0069296B  49 8B CD                        mov rcx, r13
0069296E  E8 6D 39 C2 FF                  call 0x1402b62e0
00692973  85 C0                           test eax, eax
00692975  75 0A                           jne 0x140692981
00692977  BF 72 02 00 C0                  mov edi, 0xc0000272
0069297C  E9 DB 03 00 00                  jmp 0x140692d5c
00692981  66 44 39 77 20                  cmp word ptr [rdi + 0x20], r14w
00692986  74 21                           je 0x1406929a9
00692988  48 8B CF                        mov rcx, rdi
0069298B  E8 90 5D C8 FF                  call 0x140318720
00692990  85 C0                           test eax, eax
00692992  74 06                           je 0x14069299a
00692994  F6 47 22 08                     test byte ptr [rdi + 0x22], 8
00692998  74 0F                           je 0x1406929a9
0069299A  BE 0A 00 00 00                  mov esi, 0xa
0069299F  BF 08 07 00 C0                  mov edi, 0xc0000708
006929A4  E9 9B 03 00 00                  jmp 0x140692d44
006929A9  8A 13                           mov dl, byte ptr [rbx]
006929AB  48 8B CF                        mov rcx, rdi
006929AE  E8 2D 7A C8 FF                  call 0x14031a3e0
006929B3  B9 18 00 00 00                  mov ecx, 0x18
006929B8  C6 03 11                        mov byte ptr [rbx], 0x11
006929BB  E8 40 50 CA FF                  call 0x140337a00
006929C0  65 4C 8B 34 25 88 01 00 00      mov r14, qword ptr gs:[0x188]
006929C9  4C 8D 85 A0 00 00 00            lea r8, [rbp + 0xa0]
006929D0  49 8B CD                        mov rcx, r13
006929D3  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
006929D8  33 D2                           xor edx, edx
006929DA  BB 03 00 00 00                  mov ebx, 3
006929DF  E8 3C 3E B8 FF                  call 0x140216820
006929E4  66 41 FF 8E E6 01 00 00         dec word ptr [r14 + 0x1e6]
006929EC  33 C9                           xor ecx, ecx
006929EE  90                              nop
006929EF  E8 FC 96 BE FF                  call 0x14027c0f0
006929F4  49 8B CC                        mov rcx, r12
006929F7  44 8A F8                        mov r15b, al
006929FA  E8 D1 3E C8 FF                  call 0x1403168d0
006929FF  4C 8B E0                        mov r12, rax
00692A02  48 85 C0                        test rax, rax
00692A05  75 0A                           jne 0x140692a11
00692A07  8D 73 11                        lea esi, [rbx + 0x11]
00692A0A  BF 89 01 00 C0                  mov edi, 0xc0000189
00692A0F  EB 25                           jmp 0x140692a36
00692A11  49 8B D4                        mov rdx, r12
00692A14  49 8B CE                        mov rcx, r14
00692A17  E8 E0 81 D9 FF                  call 0x14042abfc
00692A1C  8B C8                           mov ecx, eax
00692A1E  83 E1 01                        and ecx, 1
00692A21  8D 04 8D 00 00 00 00            lea eax, [rcx*4]
00692A28  0B D8                           or ebx, eax
00692A2A  85 C9                           test ecx, ecx
00692A2C  75 26                           jne 0x140692a54
00692A2E  8D 71 1E                        lea esi, [rcx + 0x1e]
00692A31  BF 2A 04 00 C0                  mov edi, 0xc000042a
00692A36  41 80 FF 11                     cmp r15b, 0x11
00692A3A  0F 84 B5 02 00 00               je 0x140692cf5
00692A40  41 8A D7                        mov dl, r15b
00692A43  33 C9                           xor ecx, ecx
00692A45  E8 D6 45 C0 FF                  call 0x140297020
00692A4A  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
00692A4F  E9 73 02 00 00                  jmp 0x140692cc7
00692A54  41 8A D7                        mov dl, r15b
00692A57  33 C9                           xor ecx, ecx
00692A59  83 E3 FD                        and ebx, 0xfffffffd
00692A5C  E8 BF 45 C0 FF                  call 0x140297020
00692A61  41 8B 44 24 30                  mov eax, dword ptr [r12 + 0x30]
00692A66  A8 04                           test al, 4
00692A68  74 0F                           je 0x140692a79
00692A6A  BE 28 00 00 00                  mov esi, 0x28
00692A6F  BF 89 01 00 C0                  mov edi, 0xc0000189
00692A74  E9 7C 02 00 00                  jmp 0x140692cf5
00692A79  41 8B 4C 24 34                  mov ecx, dword ptr [r12 + 0x34]
00692A7E  48 B8 FE FF FF FF 07 00 00 00   movabs rax, 0x7fffffffe
00692A88  41 0F B6 54 24 22               movzx edx, byte ptr [r12 + 0x22]
00692A8E  48 C1 E2 20                     shl rdx, 0x20
00692A92  48 0B D1                        or rdx, rcx
00692A95  48 3B D0                        cmp rdx, rax
00692A98  74 07                           je 0x140692aa1
00692A9A  BE 32 00 00 00                  mov esi, 0x32
00692A9F  EB CE                           jmp 0x140692a6f
00692AA1  48 8D 45 88                     lea rax, [rbp - 0x78]
00692AA5  45 33 C9                        xor r9d, r9d
00692AA8  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00692AAD  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00692AB1  48 8D 44 24 68                  lea rax, [rsp + 0x68]
00692AB6  48 8B D6                        mov rdx, rsi
00692AB9  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00692ABE  B8 01 00 00 00                  mov eax, 1
00692AC3  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00692AC7  44 8B C0                        mov r8d, eax
00692ACA  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
00692ACF  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00692AD4  E8 57 04 BB FF                  call 0x140242f30
00692AD9  49 8D 85 00 04 00 00            lea rax, [r13 + 0x400]
00692AE0  48 8B C8                        mov rcx, rax
00692AE3  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00692AE8  E8 03 A1 BE FF                  call 0x14027cbf0
00692AED  41 8B 54 24 30                  mov edx, dword ptr [r12 + 0x30]
00692AF2  45 33 C9                        xor r9d, r9d
00692AF5  C1 EA 0C                        shr edx, 0xc
00692AF8  44 8A C0                        mov r8b, al
00692AFB  83 E2 7F                        and edx, 0x7f
00692AFE  88 44 24 50                     mov byte ptr [rsp + 0x50], al
00692B02  48 8B CE                        mov rcx, rsi
00692B05  E8 66 D4 BE FF                  call 0x14027ff70
00692B0A  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
00692B14  4C 8B FE                        mov r15, rsi
00692B17  49 C1 EF 09                     shr r15, 9
00692B1B  4C 23 F8                        and r15, rax
00692B1E  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00692B28  48 8B C0                        mov rax, rax
00692B2B  4C 8B 16                        mov r10, qword ptr [rsi]
00692B2E  4C 03 F8                        add r15, rax
00692B31  B8 01 00 00 00                  mov eax, 1
00692B36  44 84 D0                        test al, r10b
00692B39  0F 84 BF 00 00 00               je 0x140692bfe
00692B3F  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
00692B49  49 8B C2                        mov rax, r10
00692B4C  48 C1 E8 0C                     shr rax, 0xc
00692B50  48 23 C1                        and rax, rcx
00692B53  48 8D 0C 40                     lea rcx, [rax + rax*2]
00692B57  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00692B61  48 C1 E1 04                     shl rcx, 4
00692B65  48 8B C0                        mov rax, rax
00692B68  48 03 C8                        add rcx, rax
00692B6B  48 3B CF                        cmp rcx, rdi
00692B6E  74 0A                           je 0x140692b7a
00692B70  BE 3C 00 00 00                  mov esi, 0x3c
00692B75  E9 48 01 00 00                  jmp 0x140692cc2
00692B7A  48 8B CF                        mov rcx, rdi
00692B7D  E8 9E 5B C8 FF                  call 0x140318720
00692B82  85 C0                           test eax, eax
00692B84  74 69                           je 0x140692bef
00692B86  8A 47 22                        mov al, byte ptr [rdi + 0x22]
00692B89  A8 08                           test al, 8
00692B8B  75 62                           jne 0x140692bef
00692B8D  4C 8B 5C 24 60                  mov r11, qword ptr [rsp + 0x60]
00692B92  41 F6 C2 42                     test r10b, 0x42
00692B96  75 21                           jne 0x140692bb9
00692B98  A8 10                           test al, 0x10
00692B9A  75 1D                           jne 0x140692bb9
00692B9C  49 8B D3                        mov rdx, r11
00692B9F  E8 9C 39 C8 FF                  call 0x140316540
00692BA4  24 0F                           and al, 0xf
00692BA6  3C 08                           cmp al, 8
00692BA8  74 0F                           je 0x140692bb9
00692BAA  BE 50 00 00 00                  mov esi, 0x50
00692BAF  BF 34 00 19 40                  mov edi, 0x40190034
00692BB4  E9 0E 01 00 00                  jmp 0x140692cc7
00692BB9  48 8D 46 08                     lea rax, [rsi + 8]
00692BBD  48 89 75 08                     mov qword ptr [rbp + 8], rsi
00692BC1  33 FF                           xor edi, edi
00692BC3  48 89 45 18                     mov qword ptr [rbp + 0x18], rax
00692BC7  49 8B D2                        mov rdx, r10
00692BCA  89 7D 20                        mov dword ptr [rbp + 0x20], edi
00692BCD  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00692BD1  4C 89 5D F8                     mov qword ptr [rbp - 8], r11
00692BD5  E8 76 EE BA FF                  call 0x140241a50
00692BDA  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00692BDE  C6 45 EC 11                     mov byte ptr [rbp - 0x14], 0x11
00692BE2  E8 15 65 BE FF                  call 0x1402790fc
00692BE7  8D 77 5A                        lea esi, [rdi + 0x5a]
00692BEA  E9 D8 00 00 00                  jmp 0x140692cc7
00692BEF  BE 46 00 00 00                  mov esi, 0x46
00692BF4  BF 08 07 00 C0                  mov edi, 0xc0000708
00692BF9  E9 C9 00 00 00                  jmp 0x140692cc7
00692BFE  49 0F BA E2 0B                  bt r10, 0xb
00692C03  0F 83 B4 00 00 00               jae 0x140692cbd
00692C09  45 33 C0                        xor r8d, r8d
00692C0C  33 D2                           xor edx, edx
00692C0E  48 8B CE                        mov rcx, rsi
00692C11  E8 6E 2C D7 FF                  call 0x140405884
00692C16  48 85 C0                        test rax, rax
00692C19  75 08                           jne 0x140692c23
00692C1B  8D 70 64                        lea esi, [rax + 0x64]
00692C1E  E9 9F 00 00 00                  jmp 0x140692cc2
00692C23  48 3B C7                        cmp rax, rdi
00692C26  74 19                           je 0x140692c41
00692C28  48 B9 FF FF FF FF FF FF FF 7F   movabs rcx, 0x7fffffffffffffff
00692C32  F0 48 21 48 18                  lock and qword ptr [rax + 0x18], rcx
00692C37  BE 6E 00 00 00                  mov esi, 0x6e
00692C3C  E9 81 00 00 00                  jmp 0x140692cc2
00692C41  33 C0                           xor eax, eax
00692C43  66 39 47 20                     cmp word ptr [rdi + 0x20], ax
00692C47  74 28                           je 0x140692c71
00692C49  48 8B CF                        mov rcx, rdi
00692C4C  E8 CF 5A C8 FF                  call 0x140318720
00692C51  85 C0                           test eax, eax
00692C53  74 06                           je 0x140692c5b
00692C55  F6 47 22 08                     test byte ptr [rdi + 0x22], 8
00692C59  74 16                           je 0x140692c71
00692C5B  48 B9 FF FF FF FF FF FF FF 7F   movabs rcx, 0x7fffffffffffffff
00692C65  F0 48 21 4F 18                  lock and qword ptr [rdi + 0x18], rcx
00692C6A  BE 78 00 00 00                  mov esi, 0x78
00692C6F  EB 83                           jmp 0x140692bf4
00692C71  8A 47 22                        mov al, byte ptr [rdi + 0x22]
00692C74  24 07                           and al, 7
00692C76  3C 02                           cmp al, 2
00692C78  75 19                           jne 0x140692c93
00692C7A  48 B9 FF FF FF FF FF FF FF 7F   movabs rcx, 0x7fffffffffffffff
00692C84  F0 48 21 4F 18                  lock and qword ptr [rdi + 0x18], rcx
00692C89  BE 82 00 00 00                  mov esi, 0x82
00692C8E  E9 1C FF FF FF                  jmp 0x140692baf
00692C93  45 33 C9                        xor r9d, r9d
00692C96  41 B0 11                        mov r8b, 0x11
00692C99  48 8B D7                        mov rdx, rdi
00692C9C  48 8B CE                        mov rcx, rsi
00692C9F  E8 CC EE CD FF                  call 0x140371b70
00692CA4  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00692CA9  48 89 06                        mov qword ptr [rsi], rax
00692CAC  BE 8C 00 00 00                  mov esi, 0x8c
00692CB1  F0 49 FF 8D 88 02 00 00         lock dec qword ptr [r13 + 0x288]
00692CB9  33 FF                           xor edi, edi
00692CBB  EB 0A                           jmp 0x140692cc7
00692CBD  BE 96 00 00 00                  mov esi, 0x96
00692CC2  BF 89 01 00 C0                  mov edi, 0xc0000189
00692CC7  4D 85 FF                        test r15, r15
00692CCA  74 12                           je 0x140692cde
00692CCC  49 8B D7                        mov rdx, r15
00692CCF  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
00692CD4  49 8B CF                        mov rcx, r15
00692CD7  E8 E4 41 B8 FF                  call 0x140216ec0
00692CDC  EB 05                           jmp 0x140692ce3
00692CDE  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
00692CE3  8A 44 24 50                     mov al, byte ptr [rsp + 0x50]
00692CE7  3C 11                           cmp al, 0x11
00692CE9  74 0A                           je 0x140692cf5
00692CEB  8A D0                           mov dl, al
00692CED  49 8B CF                        mov rcx, r15
00692CF0  E8 9B A9 BE FF                  call 0x14027d690
00692CF5  F6 C3 04                        test bl, 4
00692CF8  74 0B                           je 0x140692d05
00692CFA  49 8B D4                        mov rdx, r12
00692CFD  49 8B CE                        mov rcx, r14
00692D00  E8 C3 2C C1 FF                  call 0x1402a59c8
00692D05  F6 C3 02                        test bl, 2
00692D08  74 22                           je 0x140692d2c
00692D0A  B9 01 00 00 00                  mov ecx, 1
00692D0F  90                              nop
00692D10  66 41 01 8E E6 01 00 00         add word ptr [r14 + 0x1e6], cx
00692D18  75 12                           jne 0x140692d2c
00692D1A  49 8D 86 98 00 00 00            lea rax, [r14 + 0x98]
00692D21  90                              nop
00692D22  48 39 00                        cmp qword ptr [rax], rax
00692D25  74 05                           je 0x140692d2c
00692D27  E8 54 FF C4 FF                  call 0x1402e2c80
00692D2C  33 D2                           xor edx, edx
00692D2E  48 8D 8D A0 00 00 00            lea rcx, [rbp + 0xa0]
00692D35  E8 F6 4F B8 FF                  call 0x140217d30
00692D3A  83 FE FF                        cmp esi, -1
00692D3D  74 1D                           je 0x140692d5c
00692D3F  4C 8B 64 24 60                  mov r12, qword ptr [rsp + 0x60]
00692D44  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
00692D49  44 8B CE                        mov r9d, esi
00692D4C  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
00692D50  4D 8B C4                        mov r8, r12
00692D53  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
00692D57  E8 34 00 00 00                  call 0x140692d90
00692D5C  8B C7                           mov eax, edi
00692D5E  48 8B 8D D0 00 00 00            mov rcx, qword ptr [rbp + 0xd0]
00692D65  48 33 CC                        xor rcx, rsp
00692D68  E8 D3 98 01 00                  call 0x1406ac640
00692D6D  48 8B 9C 24 38 02 00 00         mov rbx, qword ptr [rsp + 0x238]
00692D75  48 81 C4 E0 01 00 00            add rsp, 0x1e0
00692D7C  41 5F                           pop r15
00692D7E  41 5E                           pop r14
00692D80  41 5D                           pop r13
00692D82  41 5C                           pop r12
00692D84  5F                              pop rdi
00692D85  5E                              pop rsi
00692D86  5D                              pop rbp
00692D87  C3                              ret
00692D88  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiStoreDiscardPoisonedPage(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int8 v_stack_m12C;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int8 v_stack_m1C8;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned int v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_mF8;
    unsigned __int64 v_stack_p20;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (480);
    result = (*(unsigned __int64 *)(v_rip + 7831234)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m198 = a1;
    result = 0;
    a2 = 0;
    v_stack_m160 = 0;
    v_stack_m78 = v_xmm0;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    v_stack_m190 = v_xmm1;
    v_stack_m180 = v_xmm1;
    v_stack_m170 = v_xmm1;
    result = memset(v_stack_m158, a2, 224, a4);
    v_rsi = (*(unsigned __int64 *)(a2 + 8)) | (result);
    v_r12 = (v_rsi) << (25);
    result = (result) << (25);
    v_r14 = 0;
    v_r12 = (v_r12) - (result);
    v_stack_m1C8 = 17;
    v_r12 = (v_r12) >> (16);
    v_stack_m1B8 = v_r12;
    v_stack_m1A8 = 0;
    v_stack_m1C0 = 0;
    a1 = (0) - (result);
    a1 = (a1) >> (4);
    a1 = (a1) * (result);
    v_stack_m1A0 = a1;
    result = MiGetTopLevelPfn(0, a2, 224, a4);
    if (result == 0) goto loc_00692977;
    result = MiGetPageTablePfnBuddyRaw(result, a2, result, a4);
    result = MiIsStoreProcess(result, a2, result, a4);
    if ((unsigned int)(result) != 0) goto loc_00692981;
loc_00692977:
    goto loc_00692D5C;
loc_00692981:
    if ((*(unsigned __int16 *)((unsigned int)(0xC0000272ULL) + 32)) == 0) goto loc_006929A9;
    result = MiAreChargesNeededToLockPage((unsigned int)(0xC0000272ULL), a2, result, a4);
    if ((unsigned int)(result) == 0) goto loc_0069299A;
    if (((*(unsigned __int8 *)((unsigned int)(0xC0000272ULL) + 34)) & (8)) == 0) goto loc_006929A9;
loc_0069299A:
    goto loc_00692D44;
loc_006929A9:
    result = MiUnlockPage((unsigned int)(0xC0000708ULL), *(unsigned __int8 *)(a3), result, a4);
    *(unsigned __int8 *)(a3) = 17;
    result = MiMakeDemandZeroPte(24, *(unsigned __int8 *)(a3), result, a4);
    v_stack_m1B0 = result;
    a2 = 0;
    result = KiStackAttachProcess(result, a2, v_stack_m78, a4);
    a1 = 0;
    result = MiLockVadTree(a1, a2, v_stack_m78, a4);
    result = MiLocateAddress(v_r12, a2, v_stack_m78, a4);
    if (result != 0) goto loc_00692A11;
    goto loc_00692A36;
loc_00692A11:
    result = MiTryLockVad(*(unsigned __int64 *)(gs_base + (0 + 392)), result, v_stack_m78, a4);
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result))) & (1));
    v_rbx = (unsigned int)((3) | ((unsigned int)(a1 * 4)));
    if ((unsigned int)(a1) != 0) goto loc_00692A54;
loc_00692A36:
    if (((unsigned __int8)((unsigned __int8)(result))) == 17) goto loc_00692CF5;
    a1 = 0;
    result = MiUnlockVadTree(a1, (unsigned __int8)((unsigned __int8)(result)), v_stack_m78, a4);
    goto loc_00692CC7;
loc_00692A54:
    a1 = 0;
    v_rbx = (unsigned int)((v_rbx) & (0xFFFFFFFDULL));
    result = MiUnlockVadTree(a1, (unsigned __int8)(v_stack_m1A8), v_stack_m78, a4);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 48)))) & (4)) == 0) goto loc_00692A79;
loc_00692A6F:
    goto loc_00692CF5;
loc_00692A79:
    a2 = (*(unsigned __int8 *)(result + 34)) << (32);
    a2 = (a2) | ((unsigned int)(*(unsigned int *)(result + 52)));
    if (a2 == ((unsigned int)(*(unsigned int *)(result + 48)))) goto loc_00692AA1;
    goto loc_00692A6F;
loc_00692AA1:
    a4 = 0;
    v_stack_m1D8 = v_stack_m190;
    v_stack_m1E0 = v_stack_m1B0;
    v_stack_m1E8 = 1;
    v_stack_m1F0 = result;
    v_stack_m1F8 = result;
    result = MiDecommitInitializePacket(v_stack_m158, 50, 1, a4);
    v_stack_m1C0 = result + 1024;
    result = MiLockWorkingSetShared(result + 1024, 50, 1, a4);
    a4 = 0;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 48))) >> (12));
    a2 = (unsigned int)((a2) & (127));
    v_stack_m1C8 = (unsigned __int8)(result);
    result = MiMakeSystemAddressValid(50, a2, (unsigned __int8)(result), a4);
    v_r15 = (50) >> (9);
    v_r15 = (v_r15) & (result);
    v_r15 = (v_r15) + (result);
    if (((1) & ((unsigned __int8)(*(unsigned __int64 *)(50)))) == 0) goto loc_00692BFE;
    result = (*(unsigned __int64 *)(50)) >> (12);
    result = (result) & (50);
    a1 = (result + result * 2) << (4);
    a1 = (a1) + (result);
    if (a1 == ((unsigned int)(0xC0000189ULL))) goto loc_00692B7A;
    goto loc_00692CC2;
loc_00692B7A:
    result = MiAreChargesNeededToLockPage((unsigned int)(0xC0000189ULL), a2, (unsigned __int8)(result), a4);
    if ((unsigned int)(result) == 0) goto loc_00692BEF;
    if ((((unsigned __int8)(*(unsigned __int8 *)((unsigned int)(0xC0000189ULL) + 34))) & (8)) != 0) goto loc_00692BEF;
    if ((((unsigned __int8)(*(unsigned __int64 *)(50))) & (66)) != 0) goto loc_00692BB9;
    if ((((unsigned __int8)(*(unsigned __int8 *)((unsigned int)(0xC0000189ULL) + 34))) & (16)) != 0) goto loc_00692BB9;
    result = MiGetWsleContents((unsigned int)(0xC0000189ULL), v_stack_m1B8, (unsigned __int8)(result), a4);
    result = (unsigned __int8)((result) & (15));
    if (((unsigned __int8)(result)) == 8) goto loc_00692BB9;
loc_00692BAF:
    goto loc_00692CC7;
loc_00692BB9:
    v_stack_m110 = 80;
    v_rdi = 0;
    v_stack_m100 = 80 + 8;
    v_stack_mF8 = 0;
    v_stack_m120 = v_stack_m1B8;
    result = MiDecommitHandleValidPte(v_stack_m158, *(unsigned __int64 *)(50), (unsigned __int8)(result), a4);
    v_stack_m12C = 17;
    result = MiDecommitPagesTail(v_stack_m158, *(unsigned __int64 *)(50), (unsigned __int8)(result), a4);
    goto loc_00692CC7;
loc_00692BEF:
loc_00692BF4:
    goto loc_00692CC7;
loc_00692BFE:
    if (condition_is_above_or_equal) goto loc_00692CBD;
    a3 = 0;
    a2 = 0;
    result = MiLockTransitionLeafPageEx(70, a2, a3, a4);
    if (result != 0) goto loc_00692C23;
    goto loc_00692CC2;
loc_00692C23:
    if (result == ((unsigned int)(0xC0000708ULL))) goto loc_00692C41;
    goto loc_00692CC2;
loc_00692C41:
    result = 0;
    if ((*(unsigned __int16 *)((unsigned int)(0xC0000708ULL) + 32)) == 0) goto loc_00692C71;
    result = MiAreChargesNeededToLockPage((unsigned int)(0xC0000708ULL), a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_00692C5B;
    if (((*(unsigned __int8 *)((unsigned int)(0xC0000708ULL) + 34)) & (8)) == 0) goto loc_00692C71;
loc_00692C5B:
    goto loc_00692BF4;
loc_00692C71:
    result = (unsigned __int8)((*(unsigned __int8 *)((unsigned int)(0xC0000708ULL) + 34)) & (7));
    if (((unsigned __int8)(result)) != 2) goto loc_00692C93;
    goto loc_00692BAF;
loc_00692C93:
    a4 = 0;
    result = MiDeleteTransitionPte(130, (unsigned int)(0xC0000708ULL), 17, a4);
    *(unsigned __int64 *)(130) = v_stack_m1B0;
    v_rdi = 0;
    goto loc_00692CC7;
loc_00692CBD:
loc_00692CC2:
loc_00692CC7:
    if (v_r15 == 0) goto loc_00692CDE;
    result = MiUnlockPageTable(v_stack_m1C0, v_r15, 17, a4);
    goto loc_00692CE3;
loc_00692CDE:
loc_00692CE3:
    result = v_stack_m1C8;
    if (((unsigned __int8)(v_stack_m1C8)) != 17) {
        a2 = (unsigned __int8)(v_stack_m1C8);
        a1 = v_stack_m1C0;
        result = MiUnlockWorkingSetShared(a1, a2, 17, a4);
    }
    if ((((unsigned __int8)(v_rbx)) & (4)) != 0) {
        a2 = result;
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        result = MiUnlockVad(a1, a2, 17, a4);
    }
    if ((((unsigned __int8)(v_rbx)) & (2)) == 0) goto loc_00692D2C;
    if ((((unsigned __int8)(v_rbx)) & (2)) != 0) goto loc_00692D2C;
    result = *(unsigned __int64 *)(gs_base + (0 + 392)) + 152;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) != (*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) {
        result = KiCheckForKernelApcDelivery(1, a2, 17, a4);
    }
    a2 = 0;
    result = KiUnstackDetachProcess(v_stack_m78, a2, 17, a4);
    if (150 == -1) goto loc_00692D5C;
loc_00692D44:
    v_stack_m1F8 = (unsigned int)((unsigned int)(0xC0000189ULL));
    result = MiStoreLogDiscardPoisonedPage(v_stack_m198, v_stack_m1A0, v_stack_m1B8, 150);
loc_00692D5C:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m1A0, v_stack_m1B8, 150);
    v_rsp = (v_rsp) + (480);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiStoreDiscardPoisonedPage(int64_t Arg1, void *Arg2, void *Arg3, int32_t Arg4)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint8_t v_stack_m12C;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m170;
    uint64_t v_stack_m180;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint8_t v_stack_m1C8;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint32_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint32_t v_stack_mF8;
    uint64_t v_stack_p20;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (480);
    result = (*(uint64_t *)(v_rip + 0x777EC2)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m198 = Arg1;
    result = 0;
    Arg2 = 0;
    v_stack_m160 = 0;
    v_stack_m78 = v_xmm0;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    v_stack_m190 = v_xmm1;
    v_stack_m180 = v_xmm1;
    v_stack_m170 = v_xmm1;
    result = memset(v_stack_m158, Arg2, 224, Arg4);
    local_rsi = (*(uint64_t *)(arg2 + 0x8)) | (result);
    local_r12 = (local_rsi) << (25);
    result = (result) << (25);
    local_r14 = 0;
    local_r12 = (local_r12) - (result);
    v_stack_m1C8 = 17;
    local_r12 = (local_r12) >> (16);
    v_stack_m1B8 = local_r12;
    v_stack_m1A8 = 0;
    v_stack_m1C0 = 0;
    Arg1 = (0) - (result);
    Arg1 = (Arg1) >> (4);
    Arg1 = (Arg1) * (result);
    v_stack_m1A0 = Arg1;
    result = MiGetTopLevelPfn(0, Arg2, 224, Arg4);
    if (result == 0) goto loc_00692977;
    result = MiGetPageTablePfnBuddyRaw(result, Arg2, result, Arg4);
    result = MiIsStoreProcess(result, Arg2, result, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00692981;
loc_00692977:
    goto loc_00692D5C;
loc_00692981:
    if ((*(uint16_t *)((uint32_t)(0xC0000272ULL) + 0x20)) == 0) goto loc_006929A9;
    result = MiAreChargesNeededToLockPage((uint32_t)(0xC0000272ULL), Arg2, result, Arg4);
    if ((uint32_t)(result) == 0) goto loc_0069299A;
    if (((*(uint8_t *)((uint32_t)(0xC0000272ULL) + 0x22)) & (8)) == 0) goto loc_006929A9;
loc_0069299A:
    goto loc_00692D44;
loc_006929A9:
    result = MiUnlockPage((uint32_t)(0xC0000708ULL), *(uint8_t *)(arg3), result, Arg4);
    *(uint8_t *)(arg3) = 17;
    result = MiMakeDemandZeroPte(24, *(uint8_t *)(arg3), result, Arg4);
    v_stack_m1B0 = result;
    Arg2 = 0;
    result = KiStackAttachProcess(result, Arg2, v_stack_m78, Arg4);
    Arg1 = 0;
    result = MiLockVadTree(Arg1, Arg2, v_stack_m78, Arg4);
    result = MiLocateAddress(local_r12, Arg2, v_stack_m78, Arg4);
    if (result != 0) goto loc_00692A11;
    goto loc_00692A36;
loc_00692A11:
    result = MiTryLockVad(*(uint64_t *)(gs_base + (0 + 0x188)), result, v_stack_m78, Arg4);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result))) & (1));
    local_rbx = (uint32_t)((3) | ((uint32_t)(Arg1 * 4)));
    if ((uint32_t)(Arg1) != 0) goto loc_00692A54;
loc_00692A36:
    if (((uint8_t)((uint8_t)(result))) == 17) goto loc_00692CF5;
    Arg1 = 0;
    result = MiUnlockVadTree(Arg1, (uint8_t)((uint8_t)(result)), v_stack_m78, Arg4);
    goto loc_00692CC7;
loc_00692A54:
    Arg1 = 0;
    local_rbx = (uint32_t)((local_rbx) & (0xFFFFFFFDULL));
    result = MiUnlockVadTree(Arg1, (uint8_t)(v_stack_m1A8), v_stack_m78, Arg4);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x30)))) & (4)) == 0) goto loc_00692A79;
loc_00692A6F:
    goto loc_00692CF5;
loc_00692A79:
    Arg2 = (*(uint8_t *)(result + 0x22)) << (32);
    Arg2 = (Arg2) | ((uint32_t)(*(uint32_t *)(result + 0x34)));
    if (Arg2 == ((uint32_t)(*(uint32_t *)(result + 0x30)))) goto loc_00692AA1;
    goto loc_00692A6F;
loc_00692AA1:
    Arg4 = 0;
    v_stack_m1D8 = v_stack_m190;
    v_stack_m1E0 = v_stack_m1B0;
    v_stack_m1E8 = 1;
    v_stack_m1F0 = result;
    v_stack_m1F8 = result;
    result = MiDecommitInitializePacket(v_stack_m158, 50, 1, Arg4);
    v_stack_m1C0 = result + 1024;
    result = MiLockWorkingSetShared(result + 1024, 50, 1, Arg4);
    Arg4 = 0;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x30))) >> (12));
    Arg2 = (uint32_t)((Arg2) & (127));
    v_stack_m1C8 = (uint8_t)(result);
    result = MiMakeSystemAddressValid(50, Arg2, (uint8_t)(result), Arg4);
    local_r15 = (50) >> (9);
    local_r15 = (local_r15) & (result);
    local_r15 = (local_r15) + (result);
    if (((1) & ((uint8_t)(*(uint64_t *)(50)))) == 0) goto loc_00692BFE;
    result = (*(uint64_t *)(50)) >> (12);
    result = (result) & (50);
    Arg1 = (result + result * 2) << (4);
    Arg1 = (Arg1) + (result);
    if (Arg1 == ((uint32_t)(0xC0000189ULL))) goto loc_00692B7A;
    goto loc_00692CC2;
loc_00692B7A:
    result = MiAreChargesNeededToLockPage((uint32_t)(0xC0000189ULL), Arg2, (uint8_t)(result), Arg4);
    if ((uint32_t)(result) == 0) goto loc_00692BEF;
    if ((((uint8_t)(*(uint8_t *)((uint32_t)(0xC0000189ULL) + 0x22))) & (8)) != 0) goto loc_00692BEF;
    if ((((uint8_t)(*(uint64_t *)(50))) & (66)) != 0) goto loc_00692BB9;
    if ((((uint8_t)(*(uint8_t *)((uint32_t)(0xC0000189ULL) + 0x22))) & (16)) != 0) goto loc_00692BB9;
    result = MiGetWsleContents((uint32_t)(0xC0000189ULL), v_stack_m1B8, (uint8_t)(result), Arg4);
    result = (uint8_t)((result) & (15));
    if (((uint8_t)(result)) == 8) goto loc_00692BB9;
loc_00692BAF:
    goto loc_00692CC7;
loc_00692BB9:
    v_stack_m110 = 80;
    local_rdi = 0;
    v_stack_m100 = 80 + 8;
    v_stack_mF8 = 0;
    v_stack_m120 = v_stack_m1B8;
    result = MiDecommitHandleValidPte(v_stack_m158, *(uint64_t *)(50), (uint8_t)(result), Arg4);
    v_stack_m12C = 17;
    result = MiDecommitPagesTail(v_stack_m158, *(uint64_t *)(50), (uint8_t)(result), Arg4);
    goto loc_00692CC7;
loc_00692BEF:
loc_00692BF4:
    goto loc_00692CC7;
loc_00692BFE:
    if (condition_is_above_or_equal) goto loc_00692CBD;
    Arg3 = 0;
    Arg2 = 0;
    result = MiLockTransitionLeafPageEx(70, Arg2, Arg3, Arg4);
    if (result != 0) goto loc_00692C23;
    goto loc_00692CC2;
loc_00692C23:
    if (result == ((uint32_t)(0xC0000708ULL))) goto loc_00692C41;
    goto loc_00692CC2;
loc_00692C41:
    result = 0;
    if ((*(uint16_t *)((uint32_t)(0xC0000708ULL) + 0x20)) == 0) goto loc_00692C71;
    result = MiAreChargesNeededToLockPage((uint32_t)(0xC0000708ULL), Arg2, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00692C5B;
    if (((*(uint8_t *)((uint32_t)(0xC0000708ULL) + 0x22)) & (8)) == 0) goto loc_00692C71;
loc_00692C5B:
    goto loc_00692BF4;
loc_00692C71:
    result = (uint8_t)((*(uint8_t *)((uint32_t)(0xC0000708ULL) + 0x22)) & (7));
    if (((uint8_t)(result)) != 2) goto loc_00692C93;
    goto loc_00692BAF;
loc_00692C93:
    Arg4 = 0;
    result = MiDeleteTransitionPte(130, (uint32_t)(0xC0000708ULL), 17, Arg4);
    *(uint64_t *)(130) = v_stack_m1B0;
    local_rdi = 0;
    goto loc_00692CC7;
loc_00692CBD:
loc_00692CC2:
loc_00692CC7:
    if (local_r15 == 0) goto loc_00692CDE;
    result = MiUnlockPageTable(v_stack_m1C0, local_r15, 17, Arg4);
    goto loc_00692CE3;
loc_00692CDE:
loc_00692CE3:
    result = v_stack_m1C8;
    if (((uint8_t)(v_stack_m1C8)) != 17) {
        Arg2 = (uint8_t)(v_stack_m1C8);
        Arg1 = v_stack_m1C0;
        result = MiUnlockWorkingSetShared(Arg1, Arg2, 17, Arg4);
    }
    if ((((uint8_t)(local_rbx)) & (4)) != 0) {
        Arg2 = result;
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        result = MiUnlockVad(Arg1, Arg2, 17, Arg4);
    }
    if ((((uint8_t)(local_rbx)) & (2)) == 0) goto loc_00692D2C;
    if ((((uint8_t)(local_rbx)) & (2)) != 0) goto loc_00692D2C;
    result = *(uint64_t *)(gs_base + (0 + 0x188)) + 152;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x98)) != (*(uint64_t *)(gs_base + (0 + 0x188)) + 152)) {
        result = KiCheckForKernelApcDelivery(1, Arg2, 17, Arg4);
    }
    Arg2 = 0;
    result = KiUnstackDetachProcess(v_stack_m78, Arg2, 17, Arg4);
    if (150 == -1) goto loc_00692D5C;
loc_00692D44:
    v_stack_m1F8 = (uint32_t)((uint32_t)(0xC0000189ULL));
    result = MiStoreLogDiscardPoisonedPage(v_stack_m198, v_stack_m1A0, v_stack_m1B8, 150);
loc_00692D5C:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m1A0, v_stack_m1B8, 150);
    local_rsp = (local_rsp) + (480);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x18` | `64` | `R/W` |
| `Arg2` | `+ 0x20` | `16` | `R` |
| `Arg2` | `+ 0x22` | `8` | `R` |
| `Arg3` | `+ 0x0` | `8` | `R` |
| `Arg3` | `+ 0x0` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00692858&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
