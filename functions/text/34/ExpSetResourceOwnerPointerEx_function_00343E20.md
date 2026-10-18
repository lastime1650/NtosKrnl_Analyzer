# ExpSetResourceOwnerPointerEx

- RVA: `0x00343E20`–`0x00344349` (길이 `1,321` bytes)
- VA: `0x0000000140343E20`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00077C88`
- 디코드: `345`개 명령, `1,321/1,321` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **22**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00343F52` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00343F6E` → [KiAcquireQueuedSpinLockInstrumented](../27/KiAcquireQueuedSpinLockInstrumented_function_00275850.md) (function, `0x00275850`)
- `0x00344022` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0034406B` → [ObfReferenceObjectWithTag](../21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x0034408D` → [KeReleaseInStackQueuedSpinLock](KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x00344102` → [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x00344173` → [ExpResourceEnforcesOwnershipTransfer](../41/ExpResourceEnforcesOwnershipTransfer_function_00411EB0.md) (function, `0x00411EB0`)
- `0x0034419B` → [ObfReferenceObjectWithTag](../21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x003441DF` → [PsBoostThreadIoQoS](../21/PsBoostThreadIoQoS_function_0021EFC0.md) (function, `0x0021EFC0`)
- `0x00344201` → [PsBoostThreadIoQoS](../21/PsBoostThreadIoQoS_function_0021EFC0.md) (function, `0x0021EFC0`)
- `0x0034422E` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00344248` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0034425A` → [PsBoostThreadIoEx](../39/PsBoostThreadIoEx_function_00392C00.md) (function, `0x00392C00`)
- `0x0034427C` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00344298` → [PsBoostThreadIoEx](../39/PsBoostThreadIoEx_function_00392C00.md) (function, `0x00392C00`)
- `0x003442B6` → [PsBoostThreadIoQoS](../21/PsBoostThreadIoQoS_function_0021EFC0.md) (function, `0x0021EFC0`)
- `0x003442C9` → [ObfReferenceObjectWithTag](../21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x003442E2` → [PsBoostThreadIoEx](../39/PsBoostThreadIoEx_function_00392C00.md) (function, `0x00392C00`)
- `0x00344307` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00344318` → [PsBoostThreadIoEx](../39/PsBoostThreadIoEx_function_00392C00.md) (function, `0x00392C00`)
- `0x00344334` → [KeReleaseInStackQueuedSpinLock](KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x0034433F` → [PerfLogExecutiveResourceSetOwnerPointer](../65/PerfLogExecutiveResourceSetOwnerPointer_function_00652690.md) (function, `0x00652690`)

### Direct callers
- [ExSetResourceOwnerPointerEx](../45/ExSetResourceOwnerPointerEx_function_00459140.md) at `0x00459165`
- [ExSetResourceOwnerPointer](../46/ExSetResourceOwnerPointer_function_004663D0.md) at `0x004663F8`

### Static image references
- `0x00343E3C` → RVA `0x00FC6B04` (`ALMOSTRO`; read)
- `0x00343E8D` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x00343E9A` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x00343F58` → RVA `0x00F0DE58` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x00344287` → [sub_006E2096](../6E/Unknown_function_006E2096.md) (`tail-transfer`)
  - `0x0034429E` → [sub_006E2096 + 0x6](../6E/Unknown_function_006E2096.md) (`tail-transfer`)
  - `0x003442A8` → [sub_006E2096 + 0x12](../6E/Unknown_function_006E2096.md) (`tail-transfer`)
  - `0x003442BC` → [sub_006E2096 + 0x18](../6E/Unknown_function_006E2096.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00343E20  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00343E25  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
00343E2A  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00343E2F  57                              push rdi
00343E30  41 54                           push r12
00343E32  41 55                           push r13
00343E34  41 56                           push r14
00343E36  41 57                           push r15
00343E38  48 83 EC 50                     sub rsp, 0x50
00343E3C  44 8B 35 C1 2C C8 00            mov r14d, dword ptr [rip + 0xc82cc1]
00343E43  48 8D 71 60                     lea rsi, [rcx + 0x60]
00343E47  33 C0                           xor eax, eax
00343E49  0F 57 C0                        xorps xmm0, xmm0
00343E4C  0F 11 44 24 30                  movups xmmword ptr [rsp + 0x30], xmm0
00343E51  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00343E56  45 8B F8                        mov r15d, r8d
00343E59  65 48 8B 2C 25 88 01 00 00      mov rbp, qword ptr gs:[0x188]
00343E62  4C 8B E2                        mov r12, rdx
00343E65  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
00343E6A  48 8B D9                        mov rbx, rcx
00343E6D  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00343E72  41 81 E6 00 00 02 00            and r14d, 0x20000
00343E79  90                              nop
00343E7A  41 BD 00 01 01 00               mov r13d, 0x10100
00343E80  44 0F 20 C7                     mov rdi, cr8
00343E84  B8 02 00 00 00                  mov eax, 2
00343E89  44 0F 22 C0                     mov cr8, rax
00343E8D  83 3D 8C 2E C8 00 00            cmp dword ptr [rip + 0xc82e8c], 0
00343E94  0F 85 81 01 00 00               jne 0x14034401b
00343E9A  F6 05 65 2C C8 00 21            test byte ptr [rip + 0xc82c65], 0x21
00343EA1  40 88 7C 24 40                  mov byte ptr [rsp + 0x40], dil
00343EA6  0F 85 AC 00 00 00               jne 0x140343f58
00343EAC  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
00343EB1  48 87 16                        xchg qword ptr [rsi], rdx
00343EB4  48 85 D2                        test rdx, rdx
00343EB7  0F 85 40 02 00 00               jne 0x1403440fd
00343EBD  0F B6 43 1A                     movzx eax, byte ptr [rbx + 0x1a]
00343EC1  84 C0                           test al, al
00343EC3  0F 88 A7 02 00 00               js 0x140344170
00343EC9  48 8B 43 30                     mov rax, qword ptr [rbx + 0x30]
00343ECD  48 8D 73 30                     lea rsi, [rbx + 0x30]
00343ED1  49 3B C4                        cmp rax, r12
00343ED4  74 20                           je 0x140343ef6
00343ED6  8B 4B 48                        mov ecx, dword ptr [rbx + 0x48]
00343ED9  33 D2                           xor edx, edx
00343EDB  48 8B 73 10                     mov rsi, qword ptr [rbx + 0x10]
00343EDF  48 85 C0                        test rax, rax
00343EE2  8B 43 40                        mov eax, dword ptr [rbx + 0x40]
00343EE5  0F 95 C2                        setne dl
00343EE8  48 03 C8                        add rcx, rax
00343EEB  48 85 F6                        test rsi, rsi
00343EEE  0F 85 A5 00 00 00               jne 0x140343f99
00343EF4  33 F6                           xor esi, esi
00343EF6  40 F6 C5 03                     test bpl, 3
00343EFA  0F 85 F6 01 00 00               jne 0x1403440f6
00343F00  0F B6 8D 60 04 00 00            movzx ecx, byte ptr [rbp + 0x460]
00343F07  48 8B 43 30                     mov rax, qword ptr [rbx + 0x30]
00343F0B  48 8D 7B 30                     lea rdi, [rbx + 0x30]
00343F0F  48 3B C5                        cmp rax, rbp
00343F12  0F 84 2C 01 00 00               je 0x140344044
00343F18  33 D2                           xor edx, edx
00343F1A  48 85 C0                        test rax, rax
00343F1D  0F 95 C2                        setne dl
00343F20  85 C9                           test ecx, ecx
00343F22  75 54                           jne 0x140343f78
00343F24  8B 4B 48                        mov ecx, dword ptr [rbx + 0x48]
00343F27  8B 43 40                        mov eax, dword ptr [rbx + 0x40]
00343F2A  48 8B 7B 10                     mov rdi, qword ptr [rbx + 0x10]
00343F2E  48 03 C8                        add rcx, rax
00343F31  48 85 FF                        test rdi, rdi
00343F34  0F 85 A2 00 00 00               jne 0x140343fdc
00343F3A  4C 8B 4B 10                     mov r9, qword ptr [rbx + 0x10]
00343F3E  4C 8B C5                        mov r8, rbp
00343F41  48 8B D3                        mov rdx, rbx
00343F44  48 C7 44 24 20 04 00 00 00      mov qword ptr [rsp + 0x20], 4
00343F4D  B9 E3 00 00 00                  mov ecx, 0xe3
00343F52  E8 09 97 1B 00                  call 0x1404fd660
00343F57  CC                              int3
00343F58  8B 05 FA 9E BC 00               mov eax, dword ptr [rip + 0xbc9efa]
00343F5E  85 C0                           test eax, eax
00343F60  0F 85 46 FF FF FF               jne 0x140343eac
00343F66  48 8B D6                        mov rdx, rsi
00343F69  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
00343F6E  E8 DD 18 F3 FF                  call 0x140275850
00343F73  E9 45 FF FF FF                  jmp 0x140343ebd
00343F78  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
00343F7C  48 85 C0                        test rax, rax
00343F7F  74 A3                           je 0x140343f24
00343F81  3B 48 08                        cmp ecx, dword ptr [rax + 8]
00343F84  73 9E                           jae 0x140343f24
00343F86  8B F9                           mov edi, ecx
00343F88  48 C1 E7 04                     shl rdi, 4
00343F8C  48 03 F8                        add rdi, rax
00343F8F  48 39 2F                        cmp qword ptr [rdi], rbp
00343F92  75 90                           jne 0x140343f24
00343F94  E9 AB 00 00 00                  jmp 0x140344044
00343F99  44 8B 46 08                     mov r8d, dword ptr [rsi + 8]
00343F9D  49 C1 E0 04                     shl r8, 4
00343FA1  4C 03 C6                        add r8, rsi
00343FA4  48 83 C6 10                     add rsi, 0x10
00343FA8  48 3B D1                        cmp rdx, rcx
00343FAB  0F 83 43 FF FF FF               jae 0x140343ef4
00343FB1  48 8B 06                        mov rax, qword ptr [rsi]
00343FB4  49 3B C4                        cmp rax, r12
00343FB7  0F 84 1C 01 00 00               je 0x1403440d9
00343FBD  48 85 C0                        test rax, rax
00343FC0  74 0C                           je 0x140343fce
00343FC2  48 FF C2                        inc rdx
00343FC5  48 3B D1                        cmp rdx, rcx
00343FC8  0F 84 26 FF FF FF               je 0x140343ef4
00343FCE  48 83 C6 10                     add rsi, 0x10
00343FD2  49 3B F0                        cmp rsi, r8
00343FD5  75 DA                           jne 0x140343fb1
00343FD7  E9 18 FF FF FF                  jmp 0x140343ef4
00343FDC  44 8B 47 08                     mov r8d, dword ptr [rdi + 8]
00343FE0  49 C1 E0 04                     shl r8, 4
00343FE4  4C 03 C7                        add r8, rdi
00343FE7  48 83 C7 10                     add rdi, 0x10
00343FEB  48 3B D1                        cmp rdx, rcx
00343FEE  0F 83 46 FF FF FF               jae 0x140343f3a
00343FF4  48 8B 07                        mov rax, qword ptr [rdi]
00343FF7  48 3B C5                        cmp rax, rbp
00343FFA  74 30                           je 0x14034402c
00343FFC  48 85 C0                        test rax, rax
00343FFF  74 0C                           je 0x14034400d
00344001  48 FF C2                        inc rdx
00344004  48 3B D1                        cmp rdx, rcx
00344007  0F 84 2D FF FF FF               je 0x140343f3a
0034400D  48 83 C7 10                     add rdi, 0x10
00344011  49 3B F8                        cmp rdi, r8
00344014  75 DE                           jne 0x140343ff4
00344016  E9 1F FF FF FF                  jmp 0x140343f3a
0034401B  0F B6 D0                        movzx edx, al
0034401E  40 0F B6 CF                     movzx ecx, dil
00344022  E8 D5 16 1B 00                  call 0x1404f56fc
00344027  E9 6E FE FF FF                  jmp 0x140343e9a
0034402C  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00344035  8B C7                           mov eax, edi
00344037  2B 43 10                        sub eax, dword ptr [rbx + 0x10]
0034403A  48 C1 F8 04                     sar rax, 4
0034403E  88 81 60 04 00 00               mov byte ptr [rcx + 0x460], al
00344044  41 83 E7 01                     and r15d, 1
00344048  48 85 F6                        test rsi, rsi
0034404B  0F 85 BB 00 00 00               jne 0x14034410c
00344051  45 85 FF                        test r15d, r15d
00344054  74 64                           je 0x1403440ba
00344056  49 8B CC                        mov rcx, r12
00344059  48 83 E1 FC                     and rcx, 0xfffffffffffffffc
0034405D  48 3B CD                        cmp rcx, rbp
00344060  0F 85 8D 02 00 00               jne 0x1403442f3
00344066  BA 44 66 6C 74                  mov edx, 0x746c6644
0034406B  E8 A0 C6 EC FF                  call 0x140210710
00344070  83 4F 08 02                     or dword ptr [rdi + 8], 2
00344074  4C 89 27                        mov qword ptr [rdi], r12
00344077  B8 D8 90 00 00                  mov eax, 0x90d8
0034407C  65 FF 00                        inc dword ptr gs:[rax]
0034407F  45 85 F6                        test r14d, r14d
00344082  0F 85 A1 02 00 00               jne 0x140344329
00344088  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
0034408D  E8 4E EC FF FF                  call 0x140342ce0
00344092  45 85 F6                        test r14d, r14d
00344095  0F 85 9E 02 00 00               jne 0x140344339
0034409B  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
003440A0  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
003440A4  49 8B 6B 38                     mov rbp, qword ptr [r11 + 0x38]
003440A8  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
003440AC  49 8B E3                        mov rsp, r11
003440AF  41 5F                           pop r15
003440B1  41 5E                           pop r14
003440B3  41 5D                           pop r13
003440B5  41 5C                           pop r12
003440B7  5F                              pop rdi
003440B8  C3                              ret
003440B9  CC                              int3
003440BA  8B 47 08                        mov eax, dword ptr [rdi + 8]
003440BD  A8 01                           test al, 1
003440BF  0F 85 48 02 00 00               jne 0x14034430d
003440C5  A8 04                           test al, 4
003440C7  74 AB                           je 0x140344074
003440C9  48 8B 07                        mov rax, qword ptr [rdi]
003440CC  F0 FF 88 E4 05 00 00            lock dec dword ptr [rax + 0x5e4]
003440D3  83 67 08 FB                     and dword ptr [rdi + 8], 0xfffffffb
003440D7  EB 9B                           jmp 0x140344074
003440D9  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
003440E2  8B C6                           mov eax, esi
003440E4  2B 43 10                        sub eax, dword ptr [rbx + 0x10]
003440E7  48 C1 F8 04                     sar rax, 4
003440EB  88 81 60 04 00 00               mov byte ptr [rcx + 0x460], al
003440F1  E9 00 FE FF FF                  jmp 0x140343ef6
003440F6  33 C9                           xor ecx, ecx
003440F8  E9 0A FE FF FF                  jmp 0x140343f07
003440FD  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
00344102  E8 A9 3D F1 FF                  call 0x140257eb0
00344107  E9 B1 FD FF FF                  jmp 0x140343ebd
0034410C  45 85 FF                        test r15d, r15d
0034410F  0F 84 AF 00 00 00               je 0x1403441c4
00344115  49 8B C4                        mov rax, r12
00344118  48 83 E0 FC                     and rax, 0xfffffffffffffffc
0034411C  48 3B C5                        cmp rax, rbp
0034411F  0F 85 43 01 00 00               jne 0x140344268
00344125  8B 47 08                        mov eax, dword ptr [rdi + 8]
00344128  A8 01                           test al, 1
0034412A  0F 85 52 01 00 00               jne 0x140344282
00344130  A8 04                           test al, 4
00344132  0F 85 6B 01 00 00               jne 0x1403442a3
00344138  8B 46 08                        mov eax, dword ptr [rsi + 8]
0034413B  A8 02                           test al, 2
0034413D  0F 84 7E 01 00 00               je 0x1403442c1
00344143  8B 4E 08                        mov ecx, dword ptr [rsi + 8]
00344146  8B C1                           mov eax, ecx
00344148  83 E0 F8                        and eax, 0xfffffff8
0034414B  03 47 08                        add eax, dword ptr [rdi + 8]
0034414E  33 C8                           xor ecx, eax
00344150  83 E1 07                        and ecx, 7
00344153  33 C8                           xor ecx, eax
00344155  B8 DC 90 00 00                  mov eax, 0x90dc
0034415A  89 4E 08                        mov dword ptr [rsi + 8], ecx
0034415D  83 67 08 07                     and dword ptr [rdi + 8], 7
00344161  48 C7 07 00 00 00 00            mov qword ptr [rdi], 0
00344168  FF 4B 40                        dec dword ptr [rbx + 0x40]
0034416B  E9 0C FF FF FF                  jmp 0x14034407c
00344170  48 8B CB                        mov rcx, rbx
00344173  E8 38 DD 0C 00                  call 0x140411eb0
00344178  84 C0                           test al, al
0034417A  0F 85 8C 00 00 00               jne 0x14034420c
00344180  41 F6 C7 01                     test r15b, 1
00344184  74 67                           je 0x1403441ed
00344186  49 8B CC                        mov rcx, r12
00344189  48 83 E1 FC                     and rcx, 0xfffffffffffffffc
0034418D  48 3B CD                        cmp rcx, rbp
00344190  0F 85 9E 00 00 00               jne 0x140344234
00344196  BA 44 66 6C 74                  mov edx, 0x746c6644
0034419B  E8 70 C5 EC FF                  call 0x140210710
003441A0  83 4B 38 02                     or dword ptr [rbx + 0x38], 2
003441A4  4C 89 63 30                     mov qword ptr [rbx + 0x30], r12
003441A8  B8 20 01 01 00                  mov eax, 0x10120
003441AD  65 FF 04 25 D4 90 00 00         inc dword ptr gs:[0x90d4]
003441B5  45 85 F6                        test r14d, r14d
003441B8  41 0F 44 C5                     cmove eax, r13d
003441BC  44 8B E8                        mov r13d, eax
003441BF  E9 C4 FE FF FF                  jmp 0x140344088
003441C4  8B 47 08                        mov eax, dword ptr [rdi + 8]
003441C7  A8 01                           test al, 1
003441C9  0F 85 08 01 00 00               jne 0x1403442d7
003441CF  A8 04                           test al, 4
003441D1  0F 84 6C FF FF FF               je 0x140344143
003441D7  48 8B 0F                        mov rcx, qword ptr [rdi]
003441DA  BA 01 00 00 00                  mov edx, 1
003441DF  E8 DC AD ED FF                  call 0x14021efc0
003441E4  83 67 08 FB                     and dword ptr [rdi + 8], 0xfffffffb
003441E8  E9 56 FF FF FF                  jmp 0x140344143
003441ED  8B 43 38                        mov eax, dword ptr [rbx + 0x38]
003441F0  A8 01                           test al, 1
003441F2  75 5A                           jne 0x14034424e
003441F4  A8 04                           test al, 4
003441F6  74 AC                           je 0x1403441a4
003441F8  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
003441FC  BA 01 00 00 00                  mov edx, 1
00344201  E8 BA AD ED FF                  call 0x14021efc0
00344206  83 63 38 FB                     and dword ptr [rbx + 0x38], 0xfffffffb
0034420A  EB 98                           jmp 0x1403441a4
0034420C  48 39 6B 30                     cmp qword ptr [rbx + 0x30], rbp
00344210  0F 84 6A FF FF FF               je 0x140344180
00344216  4C 8B 4B 10                     mov r9, qword ptr [rbx + 0x10]
0034421A  4C 8B C5                        mov r8, rbp
0034421D  48 8B D3                        mov rdx, rbx
00344220  48 C7 44 24 20 05 00 00 00      mov qword ptr [rsp + 0x20], 5
00344229  B9 E3 00 00 00                  mov ecx, 0xe3
0034422E  E8 2D 94 1B 00                  call 0x1404fd660
00344233  CC                              int3
00344234  4C 8B 43 10                     mov r8, qword ptr [rbx + 0x10]
00344238  4C 8B CD                        mov r9, rbp
0034423B  48 8B D3                        mov rdx, rbx
0034423E  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00344243  B9 32 01 00 00                  mov ecx, 0x132
00344248  E8 13 94 1B 00                  call 0x1404fd660
0034424D  CC                              int3
0034424E  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00344252  45 33 C9                        xor r9d, r9d
00344255  45 33 C0                        xor r8d, r8d
00344258  B2 01                           mov dl, 1
0034425A  E8 A1 E9 04 00                  call 0x140392c00
0034425F  83 63 38 FE                     and dword ptr [rbx + 0x38], 0xfffffffe
00344263  8B 43 38                        mov eax, dword ptr [rbx + 0x38]
00344266  EB 8C                           jmp 0x1403441f4
00344268  4C 8B 43 10                     mov r8, qword ptr [rbx + 0x10]
0034426C  4C 8B CD                        mov r9, rbp
0034426F  48 8B D3                        mov rdx, rbx
00344272  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00344277  B9 32 01 00 00                  mov ecx, 0x132
0034427C  E8 DF 93 1B 00                  call 0x1404fd660
00344281  CC                              int3
00344282  8B 46 08                        mov eax, dword ptr [rsi + 8]
00344285  A8 01                           test al, 1
00344287  0F 84 09 DE 39 00               je 0x1406e2096
0034428D  48 8B 0F                        mov rcx, qword ptr [rdi]
00344290  45 33 C9                        xor r9d, r9d
00344293  45 33 C0                        xor r8d, r8d
00344296  B2 01                           mov dl, 1
00344298  E8 63 E9 04 00                  call 0x140392c00
0034429D  90                              nop
0034429E  E9 F9 DD 39 00                  jmp 0x1406e209c
003442A3  8B 46 08                        mov eax, dword ptr [rsi + 8]
003442A6  A8 04                           test al, 4
003442A8  0F 84 FA DD 39 00               je 0x1406e20a8
003442AE  48 8B 0F                        mov rcx, qword ptr [rdi]
003442B1  BA 01 00 00 00                  mov edx, 1
003442B6  E8 05 AD ED FF                  call 0x14021efc0
003442BB  90                              nop
003442BC  E9 ED DD 39 00                  jmp 0x1406e20ae
003442C1  48 8B 0F                        mov rcx, qword ptr [rdi]
003442C4  BA 44 66 6C 74                  mov edx, 0x746c6644
003442C9  E8 42 C4 EC FF                  call 0x140210710
003442CE  83 4E 08 02                     or dword ptr [rsi + 8], 2
003442D2  E9 6C FE FF FF                  jmp 0x140344143
003442D7  48 8B 0F                        mov rcx, qword ptr [rdi]
003442DA  45 33 C9                        xor r9d, r9d
003442DD  45 33 C0                        xor r8d, r8d
003442E0  B2 01                           mov dl, 1
003442E2  E8 19 E9 04 00                  call 0x140392c00
003442E7  83 67 08 FE                     and dword ptr [rdi + 8], 0xfffffffe
003442EB  8B 47 08                        mov eax, dword ptr [rdi + 8]
003442EE  E9 DC FE FF FF                  jmp 0x1403441cf
003442F3  4C 8B 43 10                     mov r8, qword ptr [rbx + 0x10]
003442F7  4C 8B CD                        mov r9, rbp
003442FA  48 8B D3                        mov rdx, rbx
003442FD  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00344302  B9 32 01 00 00                  mov ecx, 0x132
00344307  E8 54 93 1B 00                  call 0x1404fd660
0034430C  CC                              int3
0034430D  48 8B 0F                        mov rcx, qword ptr [rdi]
00344310  45 33 C9                        xor r9d, r9d
00344313  45 33 C0                        xor r8d, r8d
00344316  B2 01                           mov dl, 1
00344318  E8 E3 E8 04 00                  call 0x140392c00
0034431D  83 67 08 FE                     and dword ptr [rdi + 8], 0xfffffffe
00344321  8B 47 08                        mov eax, dword ptr [rdi + 8]
00344324  E9 9C FD FF FF                  jmp 0x1403440c5
00344329  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
0034432E  41 BD 40 01 01 00               mov r13d, 0x10140
00344334  E8 A7 E9 FF FF                  call 0x140342ce0
00344339  48 8B D3                        mov rdx, rbx
0034433C  41 8B CD                        mov ecx, r13d
0034433F  E8 4C E3 30 00                  call 0x140652690
00344344  E9 52 FD FF FF                  jmp 0x14034409b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpSetResourceOwnerPointerEx(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (80);
    result = 0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = 0;
    v_stack_m40 = a1 + 96;
    v_stack_m48 = 0;
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 13118657))) & (0x20000ULL));
    if ((*(unsigned int *)(v_rip + 13119116)) != 0) goto loc_0034401B;
loc_00343E9A:
    v_stack_m38 = (unsigned __int8)(v_cr8);
    if (((*(unsigned __int8 *)(v_rip + 13118565)) & (33)) != 0) goto loc_00343F58;
loc_00343EAC:
    if (v_stack_m48 != 0) goto loc_003440FD;
loc_00343EBD:
    if (sign_flag) goto loc_00344170;
    if ((*(unsigned __int64 *)(a1 + 48)) == a2) goto loc_00343EF6;
    a2 = 0;
    a2 = (*(unsigned __int64 *)(a1 + 48) != 0) ? 1 : 0;
    a1 = ((unsigned int)(*(unsigned int *)(a1 + 72))) + ((unsigned int)(*(unsigned int *)(a1 + 64)));
    if (*(unsigned __int64 *)(a1 + 16) != 0) goto loc_00343F99;
loc_00343EF4:
    v_rsi = 0;
loc_00343EF6:
    if ((((unsigned __int8)(*(unsigned __int64 *)(gs_base + (0 + 392)))) & (3)) != 0) goto loc_003440F6;
loc_00343F07:
    if ((*(unsigned __int64 *)(a1 + 48)) == (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_00344044;
    a2 = 0;
    a2 = (*(unsigned __int64 *)(a1 + 48) != 0) ? 1 : 0;
    if ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1120)) != 0) goto loc_00343F78;
loc_00343F24:
    a1 = ((unsigned int)(*(unsigned int *)(a1 + 72))) + ((unsigned int)(*(unsigned int *)(a1 + 64)));
    if (*(unsigned __int64 *)(a1 + 16) != 0) goto loc_00343FDC;
loc_00343F3A:
    v_stack_m58 = 4;
    result = KeBugCheckEx(227, a1, *(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(a1 + 16));
loc_00343F58:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12361466))) != 0) goto loc_00343EAC;
    result = KiAcquireQueuedSpinLockInstrumented(v_stack_m48, 0, *(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(a1 + 16));
    goto loc_00343EBD;
loc_00343F78:
    if (*(unsigned __int64 *)(a1 + 16) == 0) goto loc_00343F24;
    if (((unsigned int)(v_stack_m48)) >= (*(unsigned int *)(*(unsigned __int64 *)(a1 + 16) + 8))) goto loc_00343F24;
    v_rdi = ((unsigned int)((unsigned int)(v_stack_m48))) << (4);
    v_rdi = (v_rdi) + (*(unsigned __int64 *)(a1 + 16));
    if ((*(unsigned __int64 *)(v_rdi)) != (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_00343F24;
    goto loc_00344044;
loc_00343F99:
    a3 = ((unsigned int)(*(unsigned int *)(v_rsi + 8))) << (4);
    a3 = (a3) + (0);
    v_rsi = (v_rsi) + (16);
    if (0 >= v_stack_m48) goto loc_00343EF4;
loc_00343FB1:
    if ((*(unsigned __int64 *)(v_rsi)) == a2) goto loc_003440D9;
    if (*(unsigned __int64 *)(v_rsi) == 0) goto loc_00343FCE;
    a2 = (0) + 1;
    if (a2 == v_stack_m48) goto loc_00343EF4;
loc_00343FCE:
    v_rsi = (v_rsi) + (16);
    if (v_rsi != a3) goto loc_00343FB1;
    goto loc_00343EF4;
loc_00343FDC:
    a3 = ((unsigned int)(*(unsigned int *)(v_rdi + 8))) << (4);
    a3 = (a3) + (v_rdi);
    v_rdi = (v_rdi) + (16);
    if (a2 >= v_stack_m48) goto loc_00343F3A;
loc_00343FF4:
    if ((*(unsigned __int64 *)(v_rdi)) == (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_0034402C;
    if (*(unsigned __int64 *)(v_rdi) == 0) goto loc_0034400D;
    a2 = (a2) + 1;
    if (a2 == v_stack_m48) goto loc_00343F3A;
loc_0034400D:
    v_rdi = (v_rdi) + (16);
    if (v_rdi != a3) goto loc_00343FF4;
    goto loc_00343F3A;
loc_0034401B:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_rdi), (unsigned __int8)(*(unsigned __int64 *)(v_rdi)), a3, *(unsigned __int64 *)(a1 + 16));
    goto loc_00343E9A;
loc_0034402C:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) - (*(unsigned int *)(a1 + 16)));
    result = (result) >> (4);
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1120) = (unsigned __int8)(result);
loc_00344044:
    v_r15 = (unsigned int)(((unsigned int)(a3)) & (1));
    if (v_rsi != 0) goto loc_0034410C;
    if ((unsigned int)(v_r15) == 0) goto loc_003440BA;
    a1 = (a2) & (-4);
    if (a1 != (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_003442F3;
    result = ObfReferenceObjectWithTag(a1, (unsigned int)(0x746C6644ULL), a3, *(unsigned __int64 *)(a1 + 16));
loc_00344074:
    *(unsigned __int64 *)(v_rdi) = a2;
loc_0034407C:
    if ((unsigned int)(v_r14) != 0) goto loc_00344329;
loc_00344088:
    result = KeReleaseInStackQueuedSpinLock(v_stack_m48, (unsigned int)(0x746C6644ULL), a3, *(unsigned __int64 *)(a1 + 16));
    if ((unsigned int)(v_r14) != 0) goto loc_00344339;
loc_0034409B:
    return result;
loc_003440BA:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rdi + 8)))) & (1)) != 0) goto loc_0034430D;
loc_003440C5:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rdi + 8)))) & (4)) == 0) goto loc_00344074;
    goto loc_00344074;
loc_003440D9:
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64)))) - (*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 48) + 16)));
    result = (result) >> (4);
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1120) = (unsigned __int8)(result);
    goto loc_00343EF6;
loc_003440F6:
    a1 = 0;
    goto loc_00343F07;
loc_003440FD:
    result = KxWaitForLockOwnerShip(v_stack_m20, (unsigned int)(0x746C6644ULL), a3, *(unsigned __int64 *)(a1 + 16));
    goto loc_00343EBD;
loc_0034410C:
    if ((unsigned int)(v_r15) == 0) goto loc_003441C4;
    result = (a2) & (-4);
    if (result != (*(unsigned __int64 *)(v_stack_m28 + 56))) goto loc_00344268;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rdi + 8)))) & (1)) != 0) goto loc_00344282;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rdi + 8)))) & (4)) != 0) goto loc_003442A3;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 8)))) & (2)) == 0) goto loc_003442C1;
loc_00344143:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 8))))) & (0xFFFFFFF8ULL));
    result = (unsigned int)((result) + (*(unsigned int *)(v_rdi + 8)));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 8))) ^ ((unsigned int)(result)));
    a1 = (unsigned int)((a1) & (7));
    a1 = (unsigned int)((a1) ^ ((unsigned int)(result)));
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 8) = (unsigned int)(a1);
    *(unsigned __int64 *)(v_rdi) = 0;
    goto loc_0034407C;
loc_00344170:
    result = ExpResourceEnforcesOwnershipTransfer(*(unsigned __int64 *)(v_stack_m28 + 48), (unsigned int)(0x746C6644ULL), a3, *(unsigned __int64 *)(a1 + 16));
    if ((unsigned __int8)(result) != 0) goto loc_0034420C;
loc_00344180:
    if ((((unsigned __int8)(v_r15)) & (1)) == 0) goto loc_003441ED;
    a1 = (a2) & (-4);
    if (a1 != (*(unsigned __int64 *)(v_stack_m28 + 56))) goto loc_00344234;
    result = ObfReferenceObjectWithTag(a1, (unsigned int)(0x746C6644ULL), a3, *(unsigned __int64 *)(a1 + 16));
loc_003441A4:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 48) + 48) = a2;
    result = (unsigned int)(0x10120ULL);
    if ((unsigned int)(v_r14) == 0) { result = (unsigned int)((unsigned int)(0x10100ULL)); }
    goto loc_00344088;
loc_003441C4:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rdi + 8)))) & (1)) != 0) goto loc_003442D7;
loc_003441CF:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rdi + 8)))) & (4)) == 0) goto loc_00344143;
    result = PsBoostThreadIoQoS(*(unsigned __int64 *)(v_rdi), 1, a3, *(unsigned __int64 *)(a1 + 16));
    goto loc_00344143;
loc_003441ED:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 48) + 56)))) & (1)) != 0) goto loc_0034424E;
loc_003441F4:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 48) + 56)))) & (4)) == 0) goto loc_003441A4;
    result = PsBoostThreadIoQoS(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 48) + 48), 1, a3, *(unsigned __int64 *)(a1 + 16));
    goto loc_003441A4;
loc_0034420C:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 48) + 48)) == (*(unsigned __int64 *)(v_stack_m28 + 56))) goto loc_00344180;
    v_stack_m30 = 5;
    result = KeBugCheckEx(227, *(unsigned __int64 *)(v_stack_m28 + 48), *(unsigned __int64 *)(v_stack_m28 + 56), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 48) + 16));
loc_00344234:
    v_stack_m30 = a2;
    result = KeBugCheckEx(306, *(unsigned __int64 *)(v_stack_m28 + 48), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 48) + 16), *(unsigned __int64 *)(v_stack_m28 + 56));
loc_0034424E:
    a4 = 0;
    a3 = 0;
    result = PsBoostThreadIoEx(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 48) + 48), 1, a3, a4);
    goto loc_003441F4;
loc_00344268:
    v_stack_m30 = a2;
    result = KeBugCheckEx(306, *(unsigned __int64 *)(v_stack_m28 + 48), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 48) + 16), *(unsigned __int64 *)(v_stack_m28 + 56));
loc_00344282:
    a4 = 0;
    a3 = 0;
    result = PsBoostThreadIoEx(*(unsigned __int64 *)(v_rdi), 1, a3, a4);
loc_003442A3:
    result = PsBoostThreadIoQoS(*(unsigned __int64 *)(v_rdi), 1, a3, a4);
loc_003442C1:
    result = ObfReferenceObjectWithTag(*(unsigned __int64 *)(v_rdi), (unsigned int)(0x746C6644ULL), a3, a4);
    goto loc_00344143;
loc_003442D7:
    a4 = 0;
    a3 = 0;
    result = PsBoostThreadIoEx(*(unsigned __int64 *)(v_rdi), 1, a3, a4);
    goto loc_003441CF;
loc_003442F3:
    v_stack_m30 = a2;
    result = KeBugCheckEx(306, *(unsigned __int64 *)(v_stack_m28 + 48), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 48) + 16), *(unsigned __int64 *)(v_stack_m28 + 56));
loc_0034430D:
    a4 = 0;
    a3 = 0;
    result = PsBoostThreadIoEx(*(unsigned __int64 *)(v_rdi), 1, a3, a4);
    goto loc_003440C5;
loc_00344329:
    result = KeReleaseInStackQueuedSpinLock(v_stack_m20, 1, a3, a4);
loc_00344339:
    result = PerfLogExecutiveResourceSetOwnerPointer((unsigned int)((unsigned int)((unsigned int)(0x10140ULL))), *(unsigned __int64 *)(v_stack_m28 + 48), a3, a4);
    goto loc_0034409B;
}
```

## 5. (Beta) C Style

```c
int64_t ExpSetResourceOwnerPointerEx(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (80);
    result = 0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = 0;
    v_stack_m40 = Arg1 + 96;
    v_stack_m48 = 0;
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xC82CC1))) & (0x20000ULL));
    if ((*(uint32_t *)(v_rip + 0xC82E8C)) != 0) goto loc_0034401B;
loc_00343E9A:
    v_stack_m38 = (uint8_t)(v_cr8);
    if (((*(uint8_t *)(v_rip + 0xC82C65)) & (33)) != 0) goto loc_00343F58;
loc_00343EAC:
    if (v_stack_m48 != 0) goto loc_003440FD;
loc_00343EBD:
    if (sign_flag) goto loc_00344170;
    if ((*(uint64_t *)(arg1 + 0x30)) == Arg2) goto loc_00343EF6;
    Arg2 = 0;
    Arg2 = (*(uint64_t *)(arg1 + 0x30) != 0) ? 1 : 0;
    Arg1 = ((uint32_t)(*(uint32_t *)(arg1 + 0x48))) + ((uint32_t)(*(uint32_t *)(arg1 + 0x40)));
    if (*(uint64_t *)(arg1 + 0x10) != 0) goto loc_00343F99;
loc_00343EF4:
    local_rsi = 0;
loc_00343EF6:
    if ((((uint8_t)(*(uint64_t *)(gs_base + (0 + 0x188)))) & (3)) != 0) goto loc_003440F6;
loc_00343F07:
    if ((*(uint64_t *)(arg1 + 0x30)) == (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_00344044;
    Arg2 = 0;
    Arg2 = (*(uint64_t *)(arg1 + 0x30) != 0) ? 1 : 0;
    if ((uint32_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x460)) != 0) goto loc_00343F78;
loc_00343F24:
    Arg1 = ((uint32_t)(*(uint32_t *)(arg1 + 0x48))) + ((uint32_t)(*(uint32_t *)(arg1 + 0x40)));
    if (*(uint64_t *)(arg1 + 0x10) != 0) goto loc_00343FDC;
loc_00343F3A:
    v_stack_m58 = 4;
    result = KeBugCheckEx(227, Arg1, *(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(arg1 + 0x10));
loc_00343F58:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBC9EFA))) != 0) goto loc_00343EAC;
    result = KiAcquireQueuedSpinLockInstrumented(v_stack_m48, 0, *(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(arg1 + 0x10));
    goto loc_00343EBD;
loc_00343F78:
    if (*(uint64_t *)(arg1 + 0x10) == 0) goto loc_00343F24;
    if (((uint32_t)(v_stack_m48)) >= (*(uint32_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8))) goto loc_00343F24;
    local_rdi = ((uint32_t)((uint32_t)(v_stack_m48))) << (4);
    local_rdi = (local_rdi) + (*(uint64_t *)(arg1 + 0x10));
    if ((*(uint64_t *)(local_rdi)) != (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_00343F24;
    goto loc_00344044;
loc_00343F99:
    Arg3 = ((uint32_t)(*(uint32_t *)(local_rsi + 0x8))) << (4);
    Arg3 = (Arg3) + (0);
    local_rsi = (local_rsi) + (16);
    if (0 >= v_stack_m48) goto loc_00343EF4;
loc_00343FB1:
    if ((*(uint64_t *)(local_rsi)) == Arg2) goto loc_003440D9;
    if (*(uint64_t *)(local_rsi) == 0) goto loc_00343FCE;
    Arg2 = (0) + 1;
    if (Arg2 == v_stack_m48) goto loc_00343EF4;
loc_00343FCE:
    local_rsi = (local_rsi) + (16);
    if (local_rsi != Arg3) goto loc_00343FB1;
    goto loc_00343EF4;
loc_00343FDC:
    Arg3 = ((uint32_t)(*(uint32_t *)(local_rdi + 0x8))) << (4);
    Arg3 = (Arg3) + (local_rdi);
    local_rdi = (local_rdi) + (16);
    if (Arg2 >= v_stack_m48) goto loc_00343F3A;
loc_00343FF4:
    if ((*(uint64_t *)(local_rdi)) == (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_0034402C;
    if (*(uint64_t *)(local_rdi) == 0) goto loc_0034400D;
    Arg2 = (Arg2) + 1;
    if (Arg2 == v_stack_m48) goto loc_00343F3A;
loc_0034400D:
    local_rdi = (local_rdi) + (16);
    if (local_rdi != Arg3) goto loc_00343FF4;
    goto loc_00343F3A;
loc_0034401B:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(local_rdi), (uint8_t)(*(uint64_t *)(local_rdi)), Arg3, *(uint64_t *)(arg1 + 0x10));
    goto loc_00343E9A;
loc_0034402C:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) - (*(uint32_t *)(arg1 + 0x10)));
    result = (result) >> (4);
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x460) = (uint8_t)(result);
loc_00344044:
    local_r15 = (uint32_t)(((uint32_t)(Arg3)) & (1));
    if (local_rsi != 0) goto loc_0034410C;
    if ((uint32_t)(local_r15) == 0) goto loc_003440BA;
    Arg1 = (Arg2) & (-4);
    if (Arg1 != (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_003442F3;
    result = ObfReferenceObjectWithTag(Arg1, (uint32_t)(0x746C6644ULL), Arg3, *(uint64_t *)(arg1 + 0x10));
loc_00344074:
    *(uint64_t *)(local_rdi) = Arg2;
loc_0034407C:
    if ((uint32_t)(local_r14) != 0) goto loc_00344329;
loc_00344088:
    result = KeReleaseInStackQueuedSpinLock(v_stack_m48, (uint32_t)(0x746C6644ULL), Arg3, *(uint64_t *)(arg1 + 0x10));
    if ((uint32_t)(local_r14) != 0) goto loc_00344339;
loc_0034409B:
    return result;
loc_003440BA:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x8)))) & (1)) != 0) goto loc_0034430D;
loc_003440C5:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x8)))) & (4)) == 0) goto loc_00344074;
    goto loc_00344074;
loc_003440D9:
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40)))) - (*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x30) + 0x10)));
    result = (result) >> (4);
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x460) = (uint8_t)(result);
    goto loc_00343EF6;
loc_003440F6:
    Arg1 = 0;
    goto loc_00343F07;
loc_003440FD:
    result = KxWaitForLockOwnerShip(v_stack_m20, (uint32_t)(0x746C6644ULL), Arg3, *(uint64_t *)(arg1 + 0x10));
    goto loc_00343EBD;
loc_0034410C:
    if ((uint32_t)(local_r15) == 0) goto loc_003441C4;
    result = (Arg2) & (-4);
    if (result != (*(uint64_t *)(v_stack_m28 + 0x38))) goto loc_00344268;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x8)))) & (1)) != 0) goto loc_00344282;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x8)))) & (4)) != 0) goto loc_003442A3;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x8)))) & (2)) == 0) goto loc_003442C1;
loc_00344143:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x8))))) & (0xFFFFFFF8ULL));
    result = (uint32_t)((result) + (*(uint32_t *)(local_rdi + 0x8)));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x8))) ^ ((uint32_t)(result)));
    Arg1 = (uint32_t)((Arg1) & (7));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)(result)));
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x8) = (uint32_t)(Arg1);
    *(uint64_t *)(local_rdi) = 0;
    goto loc_0034407C;
loc_00344170:
    result = ExpResourceEnforcesOwnershipTransfer(*(uint64_t *)(v_stack_m28 + 0x30), (uint32_t)(0x746C6644ULL), Arg3, *(uint64_t *)(arg1 + 0x10));
    if ((uint8_t)(result) != 0) goto loc_0034420C;
loc_00344180:
    if ((((uint8_t)(local_r15)) & (1)) == 0) goto loc_003441ED;
    Arg1 = (Arg2) & (-4);
    if (Arg1 != (*(uint64_t *)(v_stack_m28 + 0x38))) goto loc_00344234;
    result = ObfReferenceObjectWithTag(Arg1, (uint32_t)(0x746C6644ULL), Arg3, *(uint64_t *)(arg1 + 0x10));
loc_003441A4:
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x30) + 0x30) = Arg2;
    result = (uint32_t)(0x10120ULL);
    if ((uint32_t)(local_r14) == 0) { result = (uint32_t)((uint32_t)(0x10100ULL)); }
    goto loc_00344088;
loc_003441C4:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x8)))) & (1)) != 0) goto loc_003442D7;
loc_003441CF:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x8)))) & (4)) == 0) goto loc_00344143;
    result = PsBoostThreadIoQoS(*(uint64_t *)(local_rdi), 1, Arg3, *(uint64_t *)(arg1 + 0x10));
    goto loc_00344143;
loc_003441ED:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x30) + 0x38)))) & (1)) != 0) goto loc_0034424E;
loc_003441F4:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x30) + 0x38)))) & (4)) == 0) goto loc_003441A4;
    result = PsBoostThreadIoQoS(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x30) + 0x30), 1, Arg3, *(uint64_t *)(arg1 + 0x10));
    goto loc_003441A4;
loc_0034420C:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x30) + 0x30)) == (*(uint64_t *)(v_stack_m28 + 0x38))) goto loc_00344180;
    v_stack_m30 = 5;
    result = KeBugCheckEx(227, *(uint64_t *)(v_stack_m28 + 0x30), *(uint64_t *)(v_stack_m28 + 0x38), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x30) + 0x10));
loc_00344234:
    v_stack_m30 = Arg2;
    result = KeBugCheckEx(306, *(uint64_t *)(v_stack_m28 + 0x30), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x30) + 0x10), *(uint64_t *)(v_stack_m28 + 0x38));
loc_0034424E:
    a4 = 0;
    Arg3 = 0;
    result = PsBoostThreadIoEx(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x30) + 0x30), 1, Arg3, a4);
    goto loc_003441F4;
loc_00344268:
    v_stack_m30 = Arg2;
    result = KeBugCheckEx(306, *(uint64_t *)(v_stack_m28 + 0x30), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x30) + 0x10), *(uint64_t *)(v_stack_m28 + 0x38));
loc_00344282:
    a4 = 0;
    Arg3 = 0;
    result = PsBoostThreadIoEx(*(uint64_t *)(local_rdi), 1, Arg3, a4);
loc_003442A3:
    result = PsBoostThreadIoQoS(*(uint64_t *)(local_rdi), 1, Arg3, a4);
loc_003442C1:
    result = ObfReferenceObjectWithTag(*(uint64_t *)(local_rdi), (uint32_t)(0x746C6644ULL), Arg3, a4);
    goto loc_00344143;
loc_003442D7:
    a4 = 0;
    Arg3 = 0;
    result = PsBoostThreadIoEx(*(uint64_t *)(local_rdi), 1, Arg3, a4);
    goto loc_003441CF;
loc_003442F3:
    v_stack_m30 = Arg2;
    result = KeBugCheckEx(306, *(uint64_t *)(v_stack_m28 + 0x30), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x30) + 0x10), *(uint64_t *)(v_stack_m28 + 0x38));
loc_0034430D:
    a4 = 0;
    Arg3 = 0;
    result = PsBoostThreadIoEx(*(uint64_t *)(local_rdi), 1, Arg3, a4);
    goto loc_003440C5;
loc_00344329:
    result = KeReleaseInStackQueuedSpinLock(v_stack_m20, 1, Arg3, a4);
loc_00344339:
    result = PerfLogExecutiveResourceSetOwnerPointer((uint32_t)((uint32_t)((uint32_t)(0x10140ULL))), *(uint64_t *)(v_stack_m28 + 0x30), Arg3, a4);
    goto loc_0034409B;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x1A` | `8` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `W` |
| `Arg1` | `+ 0x38` | `32` | `R` |
| `Arg1` | `+ 0x38` | `32` | `R/W` |
| `Arg1` | `+ 0x40` | `32` | `R` |
| `Arg1` | `+ 0x40` | `32` | `R/W` |
| `Arg1` | `+ 0x48` | `32` | `R` |
| `Arg1` | `+ 0x60` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00343E20&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
