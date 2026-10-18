# MiUpControlAreaRefs

- RVA: `0x003B2BF0`–`0x003B2F54` (길이 `868` bytes)
- VA: `0x00000001403B2BF0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008C448`
- 디코드: `237`개 명령, `868/868` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **20**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x003B2C20` → [MiControlAreaRequiresCharge](MiControlAreaRequiresCharge_function_003B36CC.md) (function, `0x003B36CC`)
- `0x003B2CBD` → [MiLockNestedVad](../../page/A2/MiLockNestedVad_function_00A25FBC.md) (function, `0x00A25FBC`)
- `0x003B2CDD` → [MiGetProtoPteAddress](../32/MiGetProtoPteAddress_function_0032E970.md) (function, `0x0032E970`)
- `0x003B2D0A` → [MiUnlockNestedVad](../../page/A2/MiUnlockNestedVad_function_00A26BC4.md) (function, `0x00A26BC4`)
- `0x003B2D3F` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x003B2D58` → [ExfAcquirePushLockExclusiveEx](../20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x003B2D7D` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x003B2DD8` → [MiGetProtoPteAddress](../32/MiGetProtoPteAddress_function_0032E970.md) (function, `0x0032E970`)
- `0x003B2DFD` → [MiReferenceActiveSubsection](../32/MiReferenceActiveSubsection_function_00325060.md) (function, `0x00325060`)
- `0x003B2E1E` → [MiDecrementSubsections](../29/MiDecrementSubsections_function_00298B50.md) (function, `0x00298B50`)
- `0x003B2E31` → [MiDecrementSubsections](../29/MiDecrementSubsections_function_00298B50.md) (function, `0x00298B50`)
- `0x003B2E5D` → [MiReferenceActiveSubsection](../32/MiReferenceActiveSubsection_function_00325060.md) (function, `0x00325060`)
- `0x003B2E78` → [MiDecrementSubsectionViewCount](../29/MiDecrementSubsectionViewCount_function_00298E90.md) (function, `0x00298E90`)
- `0x003B2E8B` → [MiDecrementSubsections](../29/MiDecrementSubsections_function_00298B50.md) (function, `0x00298B50`)
- `0x003B2E9E` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x003B2EC6` → [MiReturnCrossPartitionSectionCharges](../4B/MiReturnCrossPartitionSectionCharges_function_004BA61C.md) (function, `0x004BA61C`)
- `0x003B2EEA` → [ExfTryToWakePushLock](../26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x003B2EF3` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x003B2F15` → [KiCheckForKernelApcDelivery](../2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x003B2F27` → [MiUnlockNestedVad](../../page/A2/MiUnlockNestedVad_function_00A26BC4.md) (function, `0x00A26BC4`)

### Direct callers
- [MiDeleteNewlyCreatedPartialVads](../../page/81/MiDeleteNewlyCreatedPartialVads_function_00810374.md) at `0x00810411`
- [MiInsertChildVads](../../page/97/MiInsertChildVads_function_0097DBB0.md) at `0x0097DCDC`
- [MiInsertChildVads](../../page/97/MiInsertChildVads_function_0097DBB0.md) at `0x0097DD32`
- [sub_00B19076](../../page/B1/Unknown_function_00B19076.md) at `0x00B1907E`

### Static image references
- `0x003B2D82` → RVA `0x00013600` (`.rdata`; read)
- `0x003B2EB2` → RVA `0x00E30088` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x003B2CBD` → [MiLockNestedVad](../../page/A2/MiLockNestedVad_function_00A25FBC.md) (`.text` → `PAGE`)
  - `0x003B2D0A` → [MiUnlockNestedVad](../../page/A2/MiUnlockNestedVad_function_00A26BC4.md) (`.text` → `PAGE`)
  - `0x003B2F27` → [MiUnlockNestedVad](../../page/A2/MiUnlockNestedVad_function_00A26BC4.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003B2BF0  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
003B2BF4  53                              push rbx
003B2BF5  55                              push rbp
003B2BF6  56                              push rsi
003B2BF7  57                              push rdi
003B2BF8  41 54                           push r12
003B2BFA  41 55                           push r13
003B2BFC  41 56                           push r14
003B2BFE  41 57                           push r15
003B2C00  48 83 EC 48                     sub rsp, 0x48
003B2C04  48 8B 41 48                     mov rax, qword ptr [rcx + 0x48]
003B2C08  8B F2                           mov esi, edx
003B2C0A  48 8B E9                        mov rbp, rcx
003B2C0D  45 33 ED                        xor r13d, r13d
003B2C10  33 D2                           xor edx, edx
003B2C12  44 89 AC 24 A8 00 00 00         mov dword ptr [rsp + 0xa8], r13d
003B2C1A  48 8B 18                        mov rbx, qword ptr [rax]
003B2C1D  48 8B CB                        mov rcx, rbx
003B2C20  E8 A7 0A 00 00                  call 0x1403b36cc
003B2C25  44 8B F8                        mov r15d, eax
003B2C28  85 C0                           test eax, eax
003B2C2A  75 0A                           jne 0x1403b2c36
003B2C2C  B8 0B 06 00 C0                  mov eax, 0xc000060b
003B2C31  E9 0C 03 00 00                  jmp 0x1403b2f42
003B2C36  48 8B 4B 40                     mov rcx, qword ptr [rbx + 0x40]
003B2C3A  41 8B C5                        mov eax, r13d
003B2C3D  48 85 C9                        test rcx, rcx
003B2C40  BA 01 00 00 00                  mov edx, 1
003B2C45  0F 95 C0                        setne al
003B2C48  49 83 C8 FF                     or r8, 0xffffffffffffffff
003B2C4C  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
003B2C50  8B 45 30                        mov eax, dword ptr [rbp + 0x30]
003B2C53  25 80 0F 00 00                  and eax, 0xf80
003B2C58  3D 00 02 00 00                  cmp eax, 0x200
003B2C5D  74 07                           je 0x1403b2c66
003B2C5F  3D 00 03 00 00                  cmp eax, 0x300
003B2C64  75 22                           jne 0x1403b2c88
003B2C66  48 85 C9                        test rcx, rcx
003B2C69  74 1D                           je 0x1403b2c88
003B2C6B  8B 43 38                        mov eax, dword ptr [rbx + 0x38]
003B2C6E  A8 20                           test al, 0x20
003B2C70  75 16                           jne 0x1403b2c88
003B2C72  85 F6                           test esi, esi
003B2C74  74 06                           je 0x1403b2c7c
003B2C76  F0 01 53 5C                     lock add dword ptr [rbx + 0x5c], edx
003B2C7A  EB 05                           jmp 0x1403b2c81
003B2C7C  F0 44 01 43 5C                  lock add dword ptr [rbx + 0x5c], r8d
003B2C81  89 94 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], edx
003B2C88  F7 43 38 00 04 00 00            test dword ptr [rbx + 0x38], 0x400
003B2C8F  45 8B E5                        mov r12d, r13d
003B2C92  44 89 AC 24 A0 00 00 00         mov dword ptr [rsp + 0xa0], r13d
003B2C9A  4D 8B F5                        mov r14, r13
003B2C9D  49 8B FD                        mov rdi, r13
003B2CA0  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
003B2CA5  4C 89 6C 24 30                  mov qword ptr [rsp + 0x30], r13
003B2CAA  75 67                           jne 0x1403b2d13
003B2CAC  0F B6 7D 20                     movzx edi, byte ptr [rbp + 0x20]
003B2CB0  48 8B CD                        mov rcx, rbp
003B2CB3  8B 45 18                        mov eax, dword ptr [rbp + 0x18]
003B2CB6  48 C1 E7 20                     shl rdi, 0x20
003B2CBA  48 0B F8                        or rdi, rax
003B2CBD  E8 FA 32 67 00                  call 0x140a25fbc
003B2CC2  4C 39 6B 40                     cmp qword ptr [rbx + 0x40], r13
003B2CC6  74 21                           je 0x1403b2ce9
003B2CC8  8B 43 38                        mov eax, dword ptr [rbx + 0x38]
003B2CCB  A8 20                           test al, 0x20
003B2CCD  75 1A                           jne 0x1403b2ce9
003B2CCF  4C 8D 4C 24 28                  lea r9, [rsp + 0x28]
003B2CD4  45 33 C0                        xor r8d, r8d
003B2CD7  48 8B D7                        mov rdx, rdi
003B2CDA  48 8B CD                        mov rcx, rbp
003B2CDD  E8 8E BC F7 FF                  call 0x14032e970
003B2CE2  48 8B 7C 24 28                  mov rdi, qword ptr [rsp + 0x28]
003B2CE7  EB 0C                           jmp 0x1403b2cf5
003B2CE9  48 8D BB 80 00 00 00            lea rdi, [rbx + 0x80]
003B2CF0  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
003B2CF5  48 85 FF                        test rdi, rdi
003B2CF8  74 0D                           je 0x1403b2d07
003B2CFA  C7 84 24 A0 00 00 00 01 00 00 00  mov dword ptr [rsp + 0xa0], 1
003B2D05  EB 08                           jmp 0x1403b2d0f
003B2D07  48 8B CD                        mov rcx, rbp
003B2D0A  E8 B5 3E 67 00                  call 0x140a26bc4
003B2D0F  49 83 C8 FF                     or r8, 0xffffffffffffffff
003B2D13  4C 39 6B 40                     cmp qword ptr [rbx + 0x40], r13
003B2D17  75 5B                           jne 0x1403b2d74
003B2D19  65 4C 8B 2C 25 88 01 00 00      mov r13, qword ptr gs:[0x188]
003B2D22  33 D2                           xor edx, edx
003B2D24  48 8B 03                        mov rax, qword ptr [rbx]
003B2D27  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
003B2D2C  66 45 01 85 E6 01 00 00         add word ptr [r13 + 0x1e6], r8w
003B2D34  90                              nop
003B2D35  48 8D 78 28                     lea rdi, [rax + 0x28]
003B2D39  45 33 C0                        xor r8d, r8d
003B2D3C  48 8B CF                        mov rcx, rdi
003B2D3F  E8 EC D4 E5 FF                  call 0x140210230
003B2D44  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
003B2D4A  48 8B F0                        mov rsi, rax
003B2D4D  73 0E                           jae 0x1403b2d5d
003B2D4F  4C 8B C7                        mov r8, rdi
003B2D52  48 8B D0                        mov rdx, rax
003B2D55  48 8B CF                        mov rcx, rdi
003B2D58  E8 33 CF E5 FF                  call 0x14020fc90
003B2D5D  48 8B 7C 24 28                  mov rdi, qword ptr [rsp + 0x28]
003B2D62  48 85 F6                        test rsi, rsi
003B2D65  74 04                           je 0x1403b2d6b
003B2D67  C6 46 0A 01                     mov byte ptr [rsi + 0xa], 1
003B2D6B  8B B4 24 98 00 00 00            mov esi, dword ptr [rsp + 0x98]
003B2D72  EB 05                           jmp 0x1403b2d79
003B2D74  4C 21 64 24 38                  and qword ptr [rsp + 0x38], r12
003B2D79  48 8D 4B 48                     lea rcx, [rbx + 0x48]
003B2D7D  E8 0E 59 E9 FF                  call 0x140248690
003B2D82  66 0F 6F 0D 76 08 C6 FF         movdqa xmm1, xmmword ptr [rip - 0x39f78a]
003B2D8A  88 84 24 90 00 00 00            mov byte ptr [rsp + 0x90], al
003B2D91  F3 0F 6F 43 28                  movdqu xmm0, xmmword ptr [rbx + 0x28]
003B2D96  66 0F D4 C8                     paddq xmm1, xmm0
003B2D9A  F3 0F 7F 4B 28                  movdqu xmmword ptr [rbx + 0x28], xmm1
003B2D9F  48 85 FF                        test rdi, rdi
003B2DA2  0F 84 EB 00 00 00               je 0x1403b2e93
003B2DA8  8B 4B 38                        mov ecx, dword ptr [rbx + 0x38]
003B2DAB  83 E1 20                        and ecx, 0x20
003B2DAE  0F 85 9A 00 00 00               jne 0x1403b2e4e
003B2DB4  4C 39 63 40                     cmp qword ptr [rbx + 0x40], r12
003B2DB8  0F 84 90 00 00 00               je 0x1403b2e4e
003B2DBE  0F B6 55 21                     movzx edx, byte ptr [rbp + 0x21]
003B2DC2  44 8D 41 01                     lea r8d, [rcx + 1]
003B2DC6  8B 45 1C                        mov eax, dword ptr [rbp + 0x1c]
003B2DC9  4C 8D 4C 24 30                  lea r9, [rsp + 0x30]
003B2DCE  48 C1 E2 20                     shl rdx, 0x20
003B2DD2  48 8B CD                        mov rcx, rbp
003B2DD5  48 0B D0                        or rdx, rax
003B2DD8  E8 93 BB F7 FF                  call 0x14032e970
003B2DDD  45 33 FF                        xor r15d, r15d
003B2DE0  48 8B F7                        mov rsi, rdi
003B2DE3  83 BC 24 98 00 00 00 00         cmp dword ptr [rsp + 0x98], 0
003B2DEB  48 8B CE                        mov rcx, rsi
003B2DEE  74 38                           je 0x1403b2e28
003B2DF0  44 8A 84 24 90 00 00 00         mov r8b, byte ptr [rsp + 0x90]
003B2DF8  BA 08 00 00 00                  mov edx, 8
003B2DFD  E8 5E 22 F7 FF                  call 0x140325060
003B2E02  44 8B E0                        mov r12d, eax
003B2E05  85 C0                           test eax, eax
003B2E07  79 30                           jns 0x1403b2e39
003B2E09  4D 85 FF                        test r15, r15
003B2E0C  0F 84 81 00 00 00               je 0x1403b2e93
003B2E12  41 B8 08 00 00 00               mov r8d, 8
003B2E18  49 8B D7                        mov rdx, r15
003B2E1B  48 8B CF                        mov rcx, rdi
003B2E1E  E8 2D 5D EE FF                  call 0x140298b50
003B2E23  4C 03 F0                        add r14, rax
003B2E26  EB 6B                           jmp 0x1403b2e93
003B2E28  41 B8 08 00 00 00               mov r8d, 8
003B2E2E  48 8B D6                        mov rdx, rsi
003B2E31  E8 1A 5D EE FF                  call 0x140298b50
003B2E36  4C 03 F0                        add r14, rax
003B2E39  4C 8B FE                        mov r15, rsi
003B2E3C  48 3B 74 24 30                  cmp rsi, qword ptr [rsp + 0x30]
003B2E41  74 50                           je 0x1403b2e93
003B2E43  48 8B 76 10                     mov rsi, qword ptr [rsi + 0x10]
003B2E47  48 85 F6                        test rsi, rsi
003B2E4A  75 97                           jne 0x1403b2de3
003B2E4C  EB 45                           jmp 0x1403b2e93
003B2E4E  85 F6                           test esi, esi
003B2E50  74 15                           je 0x1403b2e67
003B2E52  44 8A C0                        mov r8b, al
003B2E55  BA 08 00 00 00                  mov edx, 8
003B2E5A  48 8B CF                        mov rcx, rdi
003B2E5D  E8 FE 21 F7 FF                  call 0x140325060
003B2E62  44 8B E0                        mov r12d, eax
003B2E65  EB 2C                           jmp 0x1403b2e93
003B2E67  85 C9                           test ecx, ecx
003B2E69  74 14                           je 0x1403b2e7f
003B2E6B  41 83 FF 02                     cmp r15d, 2
003B2E6F  75 22                           jne 0x1403b2e93
003B2E71  41 8D 57 16                     lea edx, [r15 + 0x16]
003B2E75  48 8B CF                        mov rcx, rdi
003B2E78  E8 13 60 EE FF                  call 0x140298e90
003B2E7D  EB 11                           jmp 0x1403b2e90
003B2E7F  41 B8 08 00 00 00               mov r8d, 8
003B2E85  48 8B D7                        mov rdx, rdi
003B2E88  48 8B CF                        mov rcx, rdi
003B2E8B  E8 C0 5C EE FF                  call 0x140298b50
003B2E90  4C 8B F0                        mov r14, rax
003B2E93  8A 94 24 90 00 00 00            mov dl, byte ptr [rsp + 0x90]
003B2E9A  48 8D 4B 48                     lea rcx, [rbx + 0x48]
003B2E9E  E8 1D 54 E9 FF                  call 0x1402482c0
003B2EA3  45 33 FF                        xor r15d, r15d
003B2EA6  4D 85 F6                        test r14, r14
003B2EA9  74 20                           je 0x1403b2ecb
003B2EAB  0F B7 43 3C                     movzx eax, word ptr [rbx + 0x3c]
003B2EAF  4D 8B C6                        mov r8, r14
003B2EB2  48 8B 0D CF D1 A7 00            mov rcx, qword ptr [rip + 0xa7d1cf]
003B2EB9  25 FF 03 00 00                  and eax, 0x3ff
003B2EBE  8B 54 24 20                     mov edx, dword ptr [rsp + 0x20]
003B2EC2  48 8B 0C C1                     mov rcx, qword ptr [rcx + rax*8]
003B2EC6  E8 51 77 10 00                  call 0x1404ba61c
003B2ECB  4C 39 7B 40                     cmp qword ptr [rbx + 0x40], r15
003B2ECF  75 49                           jne 0x1403b2f1a
003B2ED1  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
003B2ED6  48 83 C8 FF                     or rax, 0xffffffffffffffff
003B2EDA  F0 48 0F C1 47 28               lock xadd qword ptr [rdi + 0x28], rax
003B2EE0  24 06                           and al, 6
003B2EE2  3C 02                           cmp al, 2
003B2EE4  75 09                           jne 0x1403b2eef
003B2EE6  48 8D 4F 28                     lea rcx, [rdi + 0x28]
003B2EEA  E8 E1 2E EB FF                  call 0x140265dd0
003B2EEF  48 8D 4F 28                     lea rcx, [rdi + 0x28]
003B2EF3  E8 08 E7 F2 FF                  call 0x1402e1600
003B2EF8  B9 01 00 00 00                  mov ecx, 1
003B2EFD  90                              nop
003B2EFE  66 41 01 8D E6 01 00 00         add word ptr [r13 + 0x1e6], cx
003B2F06  75 12                           jne 0x1403b2f1a
003B2F08  49 8D 85 98 00 00 00            lea rax, [r13 + 0x98]
003B2F0F  90                              nop
003B2F10  48 39 00                        cmp qword ptr [rax], rax
003B2F13  74 05                           je 0x1403b2f1a
003B2F15  E8 66 FD F2 FF                  call 0x1402e2c80
003B2F1A  44 39 BC 24 A0 00 00 00         cmp dword ptr [rsp + 0xa0], r15d
003B2F22  74 08                           je 0x1403b2f2c
003B2F24  48 8B CD                        mov rcx, rbp
003B2F27  E8 98 3C 67 00                  call 0x140a26bc4
003B2F2C  45 85 E4                        test r12d, r12d
003B2F2F  79 0E                           jns 0x1403b2f3f
003B2F31  44 39 BC 24 A8 00 00 00         cmp dword ptr [rsp + 0xa8], r15d
003B2F39  74 04                           je 0x1403b2f3f
003B2F3B  F0 FF 4B 5C                     lock dec dword ptr [rbx + 0x5c]
003B2F3F  41 8B C4                        mov eax, r12d
003B2F42  48 83 C4 48                     add rsp, 0x48
003B2F46  41 5F                           pop r15
003B2F48  41 5E                           pop r14
003B2F4A  41 5D                           pop r13
003B2F4C  41 5C                           pop r12
003B2F4E  5F                              pop rdi
003B2F4F  5E                              pop rsi
003B2F50  5D                              pop rbp
003B2F51  5B                              pop rbx
003B2F52  C3                              ret
003B2F53  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiUpControlAreaRefs(__int64 a1, int a2, __int64 a3)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m68;
    unsigned int v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int8 v_stack_p8;

    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (72);
    v_r13 = 0;
    a2 = 0;
    v_stack_p20 = 0;
    result = MiControlAreaRequiresCharge(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72)), a2, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_003B2C36;
    goto loc_003B2F42;
loc_003B2C36:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72)) + 64) != 0) ? 1 : 0;
    a3 = (a3) | (-1);
    v_stack_m68 = (unsigned int)(result);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 48))) & (0xF80ULL));
    if (((unsigned int)(result)) == 512) goto loc_003B2C66;
    if (((unsigned int)(result)) != 768) goto loc_003B2C88;
loc_003B2C66:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72)) + 64) == 0) goto loc_003B2C88;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72)) + 56)))) & (32)) != 0) goto loc_003B2C88;
    if ((unsigned int)((unsigned int)(a2)) == 0) goto loc_003B2C7C;
    goto loc_003B2C81;
loc_003B2C7C:
loc_003B2C81:
    v_stack_p20 = 1;
loc_003B2C88:
    v_stack_p18 = 0;
    v_stack_m60 = 0;
    v_stack_m58 = 0;
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72)) + 56)) & (0x400ULL)) != 0) goto loc_003B2D13;
    v_rdi = (*(unsigned __int8 *)(a1 + 32)) << (32);
    v_rdi = (v_rdi) | ((unsigned int)(*(unsigned int *)(a1 + 24)));
    result = MiLockNestedVad(a1, 1, a3, a4);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72)) + 64)) == 0) goto loc_003B2CE9;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72)) + 56)))) & (32)) != 0) goto loc_003B2CE9;
    a3 = 0;
    result = MiGetProtoPteAddress(a1, v_rdi, a3, v_stack_m60);
    goto loc_003B2CF5;
loc_003B2CE9:
    v_stack_m60 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72)) + 128;
loc_003B2CF5:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72)) + 128 == 0) goto loc_003B2D07;
    v_stack_p18 = 1;
    goto loc_003B2D0F;
loc_003B2D07:
    result = MiUnlockNestedVad(a1, v_rdi, a3, v_stack_m60);
loc_003B2D0F:
    a3 = (a3) | (-1);
loc_003B2D13:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72)) + 64)) != 0) goto loc_003B2D74;
    a2 = 0;
    v_stack_m50 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72)));
    a3 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72))) + 40, a2, a3, v_stack_m60);
    if (!(condition_is_above_or_equal)) {
        a3 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72))) + 40;
        a2 = result;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72))) + 40;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, v_stack_m60);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    goto loc_003B2D79;
loc_003B2D74:
loc_003B2D79:
    result = ExAcquireSpinLockExclusive(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72)) + 72, a2, a3, v_stack_m60);
    v_stack_p8 = (unsigned __int8)(result);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72)) + 40) = v_xmm1;
    if (v_stack_m60 == 0) goto loc_003B2E93;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72)) + 56))) & (32));
    if (condition_is_not_equal) goto loc_003B2E4E;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72)) + 64)) == 0) goto loc_003B2E4E;
    a2 = (*(unsigned __int8 *)(a1 + 33)) << (32);
    a2 = (a2) | ((unsigned int)(*(unsigned int *)(a1 + 28)));
    result = MiGetProtoPteAddress(a1, a2, a1 + 1, v_stack_m58);
    v_r15 = 0;
loc_003B2DE3:
    if (v_stack_p10 == 0) goto loc_003B2E28;
    result = MiReferenceActiveSubsection(v_stack_m60, 8, v_stack_p8, v_stack_m58);
    if (!sign_flag) goto loc_003B2E39;
    if (0 == 0) goto loc_003B2E93;
    result = MiDecrementSubsections(v_stack_m60, 0, 8, v_stack_m58);
    v_r14 = (0) + (result);
    goto loc_003B2E93;
loc_003B2E28:
    result = MiDecrementSubsections(v_stack_m60, v_stack_m60, 8, v_stack_m58);
    v_r14 = (v_r14) + (result);
loc_003B2E39:
    if (v_stack_m60 == v_stack_m58) goto loc_003B2E93;
    if (*(unsigned __int64 *)(v_stack_m60 + 16) != 0) goto loc_003B2DE3;
    goto loc_003B2E93;
loc_003B2E4E:
    if ((unsigned int)(*(unsigned __int64 *)(v_stack_m60 + 16)) == 0) goto loc_003B2E67;
    result = MiReferenceActiveSubsection(v_stack_m60, 8, (unsigned __int8)(result), v_stack_m58);
    goto loc_003B2E93;
loc_003B2E67:
    if ((unsigned int)(v_stack_m60) == 0) goto loc_003B2E7F;
    if (((unsigned int)(v_stack_m60)) != 2) goto loc_003B2E93;
    result = MiDecrementSubsectionViewCount(v_stack_m60, v_stack_m60 + 22, (unsigned __int8)(result), v_stack_m58);
    goto loc_003B2E90;
loc_003B2E7F:
    result = MiDecrementSubsections(v_stack_m60, v_stack_m60, 8, v_stack_m58);
loc_003B2E90:
loc_003B2E93:
    result = MiReleaseSpinLockExclusive(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72)) + 72, v_stack_p8, 8, v_stack_m58);
    v_r15 = 0;
    if (result != 0) {
        result = *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72)) + 60);
        a3 = result;
        a1 = *(unsigned __int64 *)(v_rip + 10998223);
        result = (unsigned int)((result) & (0x3FFULL));
        a2 = v_stack_m68;
        a1 = *(unsigned __int64 *)(a1 + result * 8);
        result = MiReturnCrossPartitionSectionCharges(a1, a2, a3, v_stack_m58);
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72)) + 64)) != 0) goto loc_003B2F1A;
    result = (result) | (-1);
    result = (unsigned __int8)((result) & (6));
    if (((unsigned __int8)(result)) == 2) {
        a1 = v_stack_m50 + 40;
        result = ExfTryToWakePushLock(a1, a2, a3, v_stack_m58);
    }
    result = KeAbPostRelease(v_stack_m50 + 40, a2, a3, v_stack_m58);
    if (((unsigned __int8)(result)) != 2) goto loc_003B2F1A;
    result = *(unsigned __int64 *)(gs_base + (0 + 392)) + 152;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) != (*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) {
        result = KiCheckForKernelApcDelivery(1, a2, a3, v_stack_m58);
    }
    if (v_stack_p18 != 0) {
        a1 = a1;
        result = MiUnlockNestedVad(a1, a2, a3, v_stack_m58);
    }
    if (!sign_flag) goto loc_003B2F3F;
    if (v_stack_p20 != 0) {
    }
loc_003B2F42:
    v_rsp = (v_rsp) + (72);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
}
```

## 5. (Beta) C Style

```c
int64_t MiUpControlAreaRefs(void *Arg1, int32_t Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint32_t v_stack_m68;
    uint32_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint8_t v_stack_p8;

    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (72);
    local_r13 = 0;
    Arg2 = 0;
    v_stack_p20 = 0;
    result = MiControlAreaRequiresCharge(*(uint64_t *)(*(uint64_t *)(arg1 + 0x48)), Arg2, Arg3, a4);
    if ((uint32_t)(result) != 0) goto loc_003B2C36;
    goto loc_003B2F42;
loc_003B2C36:
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x48)) + 0x40) != 0) ? 1 : 0;
    Arg3 = (Arg3) | (-1);
    v_stack_m68 = (uint32_t)(result);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x30))) & (0xF80ULL));
    if (((uint32_t)(result)) == 512) goto loc_003B2C66;
    if (((uint32_t)(result)) != 768) goto loc_003B2C88;
loc_003B2C66:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x48)) + 0x40) == 0) goto loc_003B2C88;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x48)) + 0x38)))) & (32)) != 0) goto loc_003B2C88;
    if ((uint32_t)((uint32_t)(Arg2)) == 0) goto loc_003B2C7C;
    goto loc_003B2C81;
loc_003B2C7C:
loc_003B2C81:
    v_stack_p20 = 1;
loc_003B2C88:
    v_stack_p18 = 0;
    v_stack_m60 = 0;
    v_stack_m58 = 0;
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x48)) + 0x38)) & (0x400ULL)) != 0) goto loc_003B2D13;
    local_rdi = (*(uint8_t *)(arg1 + 0x20)) << (32);
    local_rdi = (local_rdi) | ((uint32_t)(*(uint32_t *)(arg1 + 0x18)));
    result = MiLockNestedVad(Arg1, 1, Arg3, a4);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x48)) + 0x40)) == 0) goto loc_003B2CE9;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x48)) + 0x38)))) & (32)) != 0) goto loc_003B2CE9;
    Arg3 = 0;
    result = MiGetProtoPteAddress(Arg1, local_rdi, Arg3, v_stack_m60);
    goto loc_003B2CF5;
loc_003B2CE9:
    v_stack_m60 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x48)) + 128;
loc_003B2CF5:
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x48)) + 128 == 0) goto loc_003B2D07;
    v_stack_p18 = 1;
    goto loc_003B2D0F;
loc_003B2D07:
    result = MiUnlockNestedVad(Arg1, local_rdi, Arg3, v_stack_m60);
loc_003B2D0F:
    Arg3 = (Arg3) | (-1);
loc_003B2D13:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x48)) + 0x40)) != 0) goto loc_003B2D74;
    Arg2 = 0;
    v_stack_m50 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x48)));
    Arg3 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x48))) + 40, Arg2, Arg3, v_stack_m60);
    if (!(condition_is_above_or_equal)) {
        Arg3 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x48))) + 40;
        Arg2 = result;
        Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x48))) + 40;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, v_stack_m60);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    goto loc_003B2D79;
loc_003B2D74:
loc_003B2D79:
    result = ExAcquireSpinLockExclusive(*(uint64_t *)(*(uint64_t *)(arg1 + 0x48)) + 72, Arg2, Arg3, v_stack_m60);
    v_stack_p8 = (uint8_t)(result);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x48)) + 0x28) = v_xmm1;
    if (v_stack_m60 == 0) goto loc_003B2E93;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x48)) + 0x38))) & (32));
    if (condition_is_not_equal) goto loc_003B2E4E;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x48)) + 0x40)) == 0) goto loc_003B2E4E;
    Arg2 = (*(uint8_t *)(arg1 + 0x21)) << (32);
    Arg2 = (Arg2) | ((uint32_t)(*(uint32_t *)(arg1 + 0x1C)));
    result = MiGetProtoPteAddress(Arg1, Arg2, Arg1 + 1, v_stack_m58);
    local_r15 = 0;
loc_003B2DE3:
    if (v_stack_p10 == 0) goto loc_003B2E28;
    result = MiReferenceActiveSubsection(v_stack_m60, 8, v_stack_p8, v_stack_m58);
    if (!sign_flag) goto loc_003B2E39;
    if (0 == 0) goto loc_003B2E93;
    result = MiDecrementSubsections(v_stack_m60, 0, 8, v_stack_m58);
    local_r14 = (0) + (result);
    goto loc_003B2E93;
loc_003B2E28:
    result = MiDecrementSubsections(v_stack_m60, v_stack_m60, 8, v_stack_m58);
    local_r14 = (local_r14) + (result);
loc_003B2E39:
    if (v_stack_m60 == v_stack_m58) goto loc_003B2E93;
    if (*(uint64_t *)(v_stack_m60 + 0x10) != 0) goto loc_003B2DE3;
    goto loc_003B2E93;
loc_003B2E4E:
    if ((uint32_t)(*(uint64_t *)(v_stack_m60 + 0x10)) == 0) goto loc_003B2E67;
    result = MiReferenceActiveSubsection(v_stack_m60, 8, (uint8_t)(result), v_stack_m58);
    goto loc_003B2E93;
loc_003B2E67:
    if ((uint32_t)(v_stack_m60) == 0) goto loc_003B2E7F;
    if (((uint32_t)(v_stack_m60)) != 2) goto loc_003B2E93;
    result = MiDecrementSubsectionViewCount(v_stack_m60, v_stack_m60 + 22, (uint8_t)(result), v_stack_m58);
    goto loc_003B2E90;
loc_003B2E7F:
    result = MiDecrementSubsections(v_stack_m60, v_stack_m60, 8, v_stack_m58);
loc_003B2E90:
loc_003B2E93:
    result = MiReleaseSpinLockExclusive(*(uint64_t *)(*(uint64_t *)(arg1 + 0x48)) + 72, v_stack_p8, 8, v_stack_m58);
    local_r15 = 0;
    if (result != 0) {
        result = *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x48)) + 0x3C);
        Arg3 = result;
        Arg1 = *(uint64_t *)(v_rip + 0xA7D1CF);
        result = (uint32_t)((result) & (0x3FFULL));
        Arg2 = v_stack_m68;
        Arg1 = *(uint64_t *)(arg1 + result * 8);
        result = MiReturnCrossPartitionSectionCharges(Arg1, Arg2, Arg3, v_stack_m58);
    }
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x48)) + 0x40)) != 0) goto loc_003B2F1A;
    result = (result) | (-1);
    result = (uint8_t)((result) & (6));
    if (((uint8_t)(result)) == 2) {
        Arg1 = v_stack_m50 + 40;
        result = ExfTryToWakePushLock(Arg1, Arg2, Arg3, v_stack_m58);
    }
    result = KeAbPostRelease(v_stack_m50 + 40, Arg2, Arg3, v_stack_m58);
    if (((uint8_t)(result)) != 2) goto loc_003B2F1A;
    result = *(uint64_t *)(gs_base + (0 + 0x188)) + 152;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x98)) != (*(uint64_t *)(gs_base + (0 + 0x188)) + 152)) {
        result = KiCheckForKernelApcDelivery(1, Arg2, Arg3, v_stack_m58);
    }
    if (v_stack_p18 != 0) {
        Arg1 = Arg1;
        result = MiUnlockNestedVad(Arg1, Arg2, Arg3, v_stack_m58);
    }
    if (!sign_flag) goto loc_003B2F3F;
    if (v_stack_p20 != 0) {
    }
loc_003B2F42:
    local_rsp = (local_rsp) + (72);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x18` | `32` | `R` |
| `Arg1` | `+ 0x1C` | `32` | `R` |
| `Arg1` | `+ 0x20` | `8` | `R` |
| `Arg1` | `+ 0x21` | `8` | `R` |
| `Arg1` | `+ 0x30` | `32` | `R` |
| `Arg1` | `+ 0x48` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003B2BF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
