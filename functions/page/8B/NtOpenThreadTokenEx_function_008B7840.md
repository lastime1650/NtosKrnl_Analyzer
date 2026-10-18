# NtOpenThreadTokenEx

- RVA: `0x008B7840`–`0x008B8135` (길이 `2,293` bytes)
- VA: `0x00000001408B7840`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00082BB4`
- 디코드: `482`개 명령, `2,293/2,293` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **37**; 고유 호출 대상: **19**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x008B7955` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x008B797F` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008B79DC` → [PspLockThreadSecurityExclusive](../../text/4E/PspLockThreadSecurityExclusive_function_004E96E0.md) (function, `0x004E96E0`)
- `0x008B7A3F` → [PspUnlockThreadSecurityExclusive](../../text/4E/PspUnlockThreadSecurityExclusive_function_004E97C0.md) (function, `0x004E97C0`)
- `0x008B7AA2` → [PsReferencePrimaryTokenWithTag](../../text/20/PsReferencePrimaryTokenWithTag_function_0020FF80.md) (function, `0x0020FF80`)
- `0x008B7AB8` → [SepCreateImpersonationTokenDacl](SepCreateImpersonationTokenDacl_function_008B8140.md) (function, `0x008B8140`)
- `0x008B7B0C` → [ObpPushStackInfo](../../text/21/ObpPushStackInfo_function_002109E4.md) (function, `0x002109E4`)
- `0x008B7BCF` → [SepDuplicateToken](SepDuplicateToken_function_008B87EC.md) (function, `0x008B87EC`)
- `0x008B7C0E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008B7C1F` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x008B7C4C` → [ObInsertObjectEx](ObInsertObjectEx_function_008B97A0.md) (function, `0x008B97A0`)
- `0x008B7C5E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008B7CAB` → [SeQueryTokenTrustLink](../../text/47/SeQueryTokenTrustLink_function_0047168C.md) (function, `0x0047168C`)
- `0x008B7CE8` → [PspLockThreadSecurityExclusive](../../text/4E/PspLockThreadSecurityExclusive_function_004E96E0.md) (function, `0x004E96E0`)
- `0x008B7D43` → [PspUnlockThreadSecurityExclusive](../../text/4E/PspUnlockThreadSecurityExclusive_function_004E97C0.md) (function, `0x004E97C0`)
- `0x008B7DA3` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x008B7DB3` → [PspLockThreadSecurityExclusive](../../text/4E/PspLockThreadSecurityExclusive_function_004E96E0.md) (function, `0x004E96E0`)
- `0x008B7E2A` → [PspUnlockThreadSecurityExclusive](../../text/4E/PspUnlockThreadSecurityExclusive_function_004E97C0.md) (function, `0x004E97C0`)
- `0x008B7E3A` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008B7E47` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008B7E54` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x008B7E63` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008B7E6D` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008B7EA6` → [PspLockThreadSecurityShared](../../text/3C/PspLockThreadSecurityShared_function_003C4720.md) (function, `0x003C4720`)
- `0x008B7EDB` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x008B7F12` → [PspUnlockThreadSecurityShared](../../text/3C/PspUnlockThreadSecurityShared_function_003C2E40.md) (function, `0x003C2E40`)
- `0x008B7F57` → [ObOpenObjectByPointer](ObOpenObjectByPointer_function_008B7420.md) (function, `0x008B7420`)
- `0x008B7FBD` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008B7FE9` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008B802A` → [SeQueryTokenTrustLink](../../text/47/SeQueryTokenTrustLink_function_0047168C.md) (function, `0x0047168C`)
- `0x008B8035` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x008B805D` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008B8093` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x008B80B2` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x008B80BC` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008B80FA` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008B8113` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)

### Direct callers
- [NtOpenThreadToken](NtOpenThreadToken_function_008B7820.md) at `0x008B782C`

### Static image references
- `0x008B7932` → RVA `0x00FC6AC8` (`ALMOSTRO`; read)
- `0x008B7AEF` → RVA `0x00FC5010` (`ALMOSTRO`; read)
- `0x008B7F3A` → RVA `0x00FD8020` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **32**
  - `0x008B797F` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008B79DC` → [PspLockThreadSecurityExclusive](../../text/4E/PspLockThreadSecurityExclusive_function_004E96E0.md) (`PAGE` → `.text`)
  - `0x008B7A3F` → [PspUnlockThreadSecurityExclusive](../../text/4E/PspUnlockThreadSecurityExclusive_function_004E97C0.md) (`PAGE` → `.text`)
  - `0x008B7AA2` → [PsReferencePrimaryTokenWithTag](../../text/20/PsReferencePrimaryTokenWithTag_function_0020FF80.md) (`PAGE` → `.text`)
  - `0x008B7B0C` → [ObpPushStackInfo](../../text/21/ObpPushStackInfo_function_002109E4.md) (`PAGE` → `.text`)
  - `0x008B7C0E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008B7C1F` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x008B7C5E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008B7CAB` → [SeQueryTokenTrustLink](../../text/47/SeQueryTokenTrustLink_function_0047168C.md) (`PAGE` → `.text`)
  - `0x008B7CE8` → [PspLockThreadSecurityExclusive](../../text/4E/PspLockThreadSecurityExclusive_function_004E96E0.md) (`PAGE` → `.text`)
  - `0x008B7D43` → [PspUnlockThreadSecurityExclusive](../../text/4E/PspUnlockThreadSecurityExclusive_function_004E97C0.md) (`PAGE` → `.text`)
  - `0x008B7DA3` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x008B7DB3` → [PspLockThreadSecurityExclusive](../../text/4E/PspLockThreadSecurityExclusive_function_004E96E0.md) (`PAGE` → `.text`)
  - `0x008B7E2A` → [PspUnlockThreadSecurityExclusive](../../text/4E/PspUnlockThreadSecurityExclusive_function_004E97C0.md) (`PAGE` → `.text`)
  - `0x008B7E3A` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008B7E47` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008B7E54` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x008B7E63` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008B7E6D` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008B7EA6` → [PspLockThreadSecurityShared](../../text/3C/PspLockThreadSecurityShared_function_003C4720.md) (`PAGE` → `.text`)
  - `0x008B7EDB` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (`PAGE` → `.text`)
  - `0x008B7F12` → [PspUnlockThreadSecurityShared](../../text/3C/PspUnlockThreadSecurityShared_function_003C2E40.md) (`PAGE` → `.text`)
  - `0x008B7FBD` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008B7FE9` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008B802A` → [SeQueryTokenTrustLink](../../text/47/SeQueryTokenTrustLink_function_0047168C.md) (`PAGE` → `.text`)
  - `0x008B8035` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x008B805D` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008B8093` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x008B80B2` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x008B80BC` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008B80FA` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008B8113` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x008B810A` → [sub_00B1A8E2](../B1/Unknown_function_00B1A8E2.md) (`tail-transfer`)
  - `0x008B8119` → [sub_00B1A8E2](../B1/Unknown_function_00B1A8E2.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008B7840  4C 8B DC                        mov r11, rsp
008B7843  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
008B7847  49 89 73 20                     mov qword ptr [r11 + 0x20], rsi
008B784B  45 88 43 18                     mov byte ptr [r11 + 0x18], r8b
008B784F  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
008B7853  57                              push rdi
008B7854  41 54                           push r12
008B7856  41 55                           push r13
008B7858  41 56                           push r14
008B785A  41 57                           push r15
008B785C  48 81 EC 00 01 00 00            sub rsp, 0x100
008B7863  41 0F B6 D8                     movzx ebx, r8b
008B7867  4C 8B D1                        mov r10, rcx
008B786A  33 F6                           xor esi, esi
008B786C  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
008B7871  40 88 74 24 50                  mov byte ptr [rsp + 0x50], sil
008B7876  40 88 74 24 43                  mov byte ptr [rsp + 0x43], sil
008B787B  8B FE                           mov edi, esi
008B787D  89 74 24 78                     mov dword ptr [rsp + 0x78], esi
008B7881  0F 57 C0                        xorps xmm0, xmm0
008B7884  0F 11 44 24 68                  movups xmmword ptr [rsp + 0x68], xmm0
008B7889  40 88 74 24 41                  mov byte ptr [rsp + 0x41], sil
008B788E  49 89 B3 68 FF FF FF            mov qword ptr [r11 - 0x98], rsi
008B7895  33 C0                           xor eax, eax
008B7897  41 0F 11 43 B0                  movups xmmword ptr [r11 - 0x50], xmm0
008B789C  41 0F 11 43 C0                  movups xmmword ptr [r11 - 0x40], xmm0
008B78A1  49 89 43 D0                     mov qword ptr [r11 - 0x30], rax
008B78A5  0F 11 84 24 A0 00 00 00         movups xmmword ptr [rsp + 0xa0], xmm0
008B78AD  41 0F 11 43 88                  movups xmmword ptr [r11 - 0x78], xmm0
008B78B2  49 89 43 98                     mov qword ptr [r11 - 0x68], rax
008B78B6  41 89 43 A0                     mov dword ptr [r11 - 0x60], eax
008B78BA  49 89 B3 60 FF FF FF            mov qword ptr [r11 - 0xa0], rsi
008B78C1  48 89 74 24 60                  mov qword ptr [rsp + 0x60], rsi
008B78C6  88 44 24 40                     mov byte ptr [rsp + 0x40], al
008B78CA  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008B78D3  44 0F B6 A0 32 02 00 00         movzx r12d, byte ptr [rax + 0x232]
008B78DB  44 88 64 24 42                  mov byte ptr [rsp + 0x42], r12b
008B78E0  B8 F2 1D 00 00                  mov eax, 0x1df2
008B78E5  41 BE F2 1F 01 00               mov r14d, 0x11ff2
008B78EB  45 84 E4                        test r12b, r12b
008B78EE  44 0F 45 F0                     cmovne r14d, eax
008B78F2  45 23 F1                        and r14d, r9d
008B78F5  45 84 E4                        test r12b, r12b
008B78F8  0F 84 46 07 00 00               je 0x1408b8044
008B78FE  48 B9 00 00 FF FF FF 7F 00 00   movabs rcx, 0x7fffffff0000
008B7908  4C 8B AC 24 50 01 00 00         mov r13, qword ptr [rsp + 0x150]
008B7910  4C 3B E9                        cmp r13, rcx
008B7913  49 0F 42 CD                     cmovb rcx, r13
008B7917  48 8B 01                        mov rax, qword ptr [rcx]
008B791A  48 89 01                        mov qword ptr [rcx], rax
008B791D  EB 02                           jmp 0x1408b7921
008B791F  EB 68                           jmp 0x1408b7989
008B7921  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008B792A  44 0F B6 88 32 02 00 00         movzx r9d, byte ptr [rax + 0x232]
008B7932  4C 8B 05 8F F1 70 00            mov r8, qword ptr [rip + 0x70f18f]
008B7939  48 89 74 24 48                  mov qword ptr [rsp + 0x48], rsi
008B793E  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
008B7943  48 8D 44 24 48                  lea rax, [rsp + 0x48]
008B7948  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008B794D  BA 00 08 00 00                  mov edx, 0x800
008B7952  49 8B CA                        mov rcx, r10
008B7955  E8 56 14 FB FF                  call 0x140868db0
008B795A  85 C0                           test eax, eax
008B795C  78 2B                           js 0x1408b7989
008B795E  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
008B7963  8B 88 A0 05 00 00               mov ecx, dword ptr [rax + 0x5a0]
008B7969  F6 C1 08                        test cl, 8
008B796C  0F 85 20 05 00 00               jne 0x1408b7e92
008B7972  4C 8B FE                        mov r15, rsi
008B7975  4D 85 FF                        test r15, r15
008B7978  75 2D                           jne 0x1408b79a7
008B797A  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
008B797F  E8 CC 19 A4 FF                  call 0x1402f9350
008B7984  B8 7C 00 00 C0                  mov eax, 0xc000007c
008B7989  4C 8D 9C 24 00 01 00 00         lea r11, [rsp + 0x100]
008B7991  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
008B7995  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
008B7999  49 8B E3                        mov rsp, r11
008B799C  41 5F                           pop r15
008B799E  41 5E                           pop r14
008B79A0  41 5D                           pop r13
008B79A2  41 5C                           pop r12
008B79A4  5F                              pop rdi
008B79A5  C3                              ret
008B79A6  CC                              int3
008B79A7  85 FF                           test edi, edi
008B79A9  0F 84 FB 06 00 00               je 0x1408b80aa
008B79AF  84 DB                           test bl, bl
008B79B1  0F 84 A9 00 00 00               je 0x1408b7a60
008B79B7  65 48 8B 1C 25 88 01 00 00      mov rbx, qword ptr gs:[0x188]
008B79C0  45 32 E4                        xor r12b, r12b
008B79C3  8B 83 A0 05 00 00               mov eax, dword ptr [rbx + 0x5a0]
008B79C9  A8 08                           test al, 8
008B79CB  74 77                           je 0x1408b7a44
008B79CD  65 48 8B 3C 25 88 01 00 00      mov rdi, qword ptr gs:[0x188]
008B79D6  48 8B D7                        mov rdx, rdi
008B79D9  48 8B CB                        mov rcx, rbx
008B79DC  E8 FF 1C C3 FF                  call 0x1404e96e0
008B79E1  F0 0F BA B3 A0 05 00 00 03      lock btr dword ptr [rbx + 0x5a0], 3
008B79EA  73 4D                           jae 0x1408b7a39
008B79EC  41 B4 01                        mov r12b, 1
008B79EF  8B 83 38 05 00 00               mov eax, dword ptr [rbx + 0x538]
008B79F5  83 E0 03                        and eax, 3
008B79F8  89 44 24 74                     mov dword ptr [rsp + 0x74], eax
008B79FC  48 8B 8B 38 05 00 00            mov rcx, qword ptr [rbx + 0x538]
008B7A03  0F B6 C1                        movzx eax, cl
008B7A06  C0 E8 02                        shr al, 2
008B7A09  41 22 C4                        and al, r12b
008B7A0C  88 44 24 71                     mov byte ptr [rsp + 0x71], al
008B7A10  8B 83 A0 05 00 00               mov eax, dword ptr [rbx + 0x5a0]
008B7A16  C1 E8 08                        shr eax, 8
008B7A19  41 22 C4                        and al, r12b
008B7A1C  88 44 24 70                     mov byte ptr [rsp + 0x70], al
008B7A20  48 8B 83 48 06 00 00            mov rax, qword ptr [rbx + 0x648]
008B7A27  48 83 E1 F8                     and rcx, 0xfffffffffffffff8
008B7A2B  48 85 C0                        test rax, rax
008B7A2E  0F 85 1D 06 00 00               jne 0x1408b8051
008B7A34  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
008B7A39  48 8B D7                        mov rdx, rdi
008B7A3C  48 8B CB                        mov rcx, rbx
008B7A3F  E8 7C 1D C3 FF                  call 0x1404e97c0
008B7A44  0F B6 9C 24 40 01 00 00         movzx ebx, byte ptr [rsp + 0x140]
008B7A4C  45 84 E4                        test r12b, r12b
008B7A4F  44 0F B6 64 24 42               movzx r12d, byte ptr [rsp + 0x42]
008B7A55  0F 84 16 06 00 00               je 0x1408b8071
008B7A5B  C6 44 24 41 01                  mov byte ptr [rsp + 0x41], 1
008B7A60  80 7C 24 50 00                  cmp byte ptr [rsp + 0x50], 0
008B7A65  0F 84 BD 04 00 00               je 0x1408b7f28
008B7A6B  84 DB                           test bl, bl
008B7A6D  0F 84 88 05 00 00               je 0x1408b7ffb
008B7A73  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
008B7A78  48 85 C0                        test rax, rax
008B7A7B  74 11                           je 0x1408b7a8e
008B7A7D  48 8B 80 50 04 00 00            mov rax, qword ptr [rax + 0x450]
008B7A84  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
008B7A89  C6 44 24 40 01                  mov byte ptr [rsp + 0x40], 1
008B7A8E  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
008B7A93  48 8B 98 20 02 00 00            mov rbx, qword ptr [rax + 0x220]
008B7A9A  BA 44 66 6C 74                  mov edx, 0x746c6644
008B7A9F  48 8B CB                        mov rcx, rbx
008B7AA2  E8 D9 84 95 FF                  call 0x14020ff80
008B7AA7  48 8B F8                        mov rdi, rax
008B7AAA  4C 8D 84 24 88 00 00 00         lea r8, [rsp + 0x88]
008B7AB2  48 8B D0                        mov rdx, rax
008B7AB5  49 8B CF                        mov rcx, r15
008B7AB8  E8 83 06 00 00                  call 0x1408b8140
008B7ABD  44 8B E0                        mov r12d, eax
008B7AC0  0F 0D 8B 48 02 00 00            prefetchw byte ptr [rbx + 0x248]
008B7AC7  48 8B 83 48 02 00 00            mov rax, qword ptr [rbx + 0x248]
008B7ACE  48 8B C8                        mov rcx, rax
008B7AD1  48 33 CF                        xor rcx, rdi
008B7AD4  48 83 F9 0F                     cmp rcx, 0xf
008B7AD8  0F 83 AD 05 00 00               jae 0x1408b808b
008B7ADE  48 8D 48 01                     lea rcx, [rax + 1]
008B7AE2  F0 48 0F B1 8B 48 02 00 00      lock cmpxchg qword ptr [rbx + 0x248], rcx
008B7AEB  75 E1                           jne 0x1408b7ace
008B7AED  8B C6                           mov eax, esi
008B7AEF  39 35 1B D5 70 00               cmp dword ptr [rip + 0x70d51b], esi
008B7AF5  0F 95 C0                        setne al
008B7AF8  85 C0                           test eax, eax
008B7AFA  74 15                           je 0x1408b7b11
008B7AFC  48 8D 4F D0                     lea rcx, [rdi - 0x30]
008B7B00  33 D2                           xor edx, edx
008B7B02  41 B9 44 66 6C 74               mov r9d, 0x746c6644
008B7B08  44 8D 42 01                     lea r8d, [rdx + 1]
008B7B0C  E8 D3 8E 95 FF                  call 0x1402109e4
008B7B11  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
008B7B19  45 85 E4                        test r12d, r12d
008B7B1C  0F 88 32 01 00 00               js 0x1408b7c54
008B7B22  48 85 DB                        test rbx, rbx
008B7B25  74 31                           je 0x1408b7b58
008B7B27  C6 84 24 D8 00 00 00 01         mov byte ptr [rsp + 0xd8], 1
008B7B2F  0F B7 84 24 DA 00 00 00         movzx eax, word ptr [rsp + 0xda]
008B7B37  66 85 C0                        test ax, ax
008B7B3A  78 1C                           js 0x1408b7b58
008B7B3C  48 89 9C 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], rbx
008B7B44  B9 F7 FF 00 00                  mov ecx, 0xfff7
008B7B49  66 23 C1                        and ax, cx
008B7B4C  66 83 C8 04                     or ax, 4
008B7B50  66 89 84 24 DA 00 00 00         mov word ptr [rsp + 0xda], ax
008B7B58  C7 84 24 A0 00 00 00 30 00 00 00  mov dword ptr [rsp + 0xa0], 0x30
008B7B63  48 89 B4 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rsi
008B7B6B  44 89 B4 24 B8 00 00 00         mov dword ptr [rsp + 0xb8], r14d
008B7B73  48 89 B4 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rsi
008B7B7B  48 85 DB                        test rbx, rbx
008B7B7E  0F 84 19 05 00 00               je 0x1408b809d
008B7B84  48 8D 84 24 D8 00 00 00         lea rax, [rsp + 0xd8]
008B7B8C  48 89 84 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rax
008B7B94  48 89 B4 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rsi
008B7B9C  48 8D 44 24 58                  lea rax, [rsp + 0x58]
008B7BA1  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008B7BA6  C6 44 24 30 00                  mov byte ptr [rsp + 0x30], 0
008B7BAB  C6 44 24 28 00                  mov byte ptr [rsp + 0x28], 0
008B7BB0  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
008B7BB4  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008B7BB8  41 B9 02 00 00 00               mov r9d, 2
008B7BBE  44 0F B6 44 24 43               movzx r8d, byte ptr [rsp + 0x43]
008B7BC4  48 8D 94 24 A0 00 00 00         lea rdx, [rsp + 0xa0]
008B7BCC  49 8B CF                        mov rcx, r15
008B7BCF  E8 18 0C 00 00                  call 0x1408b87ec
008B7BD4  44 8B E0                        mov r12d, eax
008B7BD7  85 C0                           test eax, eax
008B7BD9  78 79                           js 0x1408b7c54
008B7BDB  80 7C 24 40 00                  cmp byte ptr [rsp + 0x40], 0
008B7BE0  74 38                           je 0x1408b7c1a
008B7BE2  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
008B7BE7  48 8B FE                        mov rdi, rsi
008B7BEA  48 89 B4 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rsi
008B7BF2  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
008B7BF7  48 85 C0                        test rax, rax
008B7BFA  0F 85 99 03 00 00               jne 0x1408b7f99
008B7C00  49 8B 8E 50 04 00 00            mov rcx, qword ptr [r14 + 0x450]
008B7C07  48 85 C9                        test rcx, rcx
008B7C0A  74 07                           je 0x1408b7c13
008B7C0C  33 D2                           xor edx, edx
008B7C0E  E8 5D AC 2C 00                  call 0x140b82870
008B7C13  49 89 BE 50 04 00 00            mov qword ptr [r14 + 0x450], rdi
008B7C1A  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
008B7C1F  E8 FC 7D 95 FF                  call 0x14020fa20
008B7C24  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
008B7C2C  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008B7C31  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
008B7C36  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
008B7C3A  45 33 C9                        xor r9d, r9d
008B7C3D  44 8B 84 24 38 01 00 00         mov r8d, dword ptr [rsp + 0x138]
008B7C45  33 D2                           xor edx, edx
008B7C47  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
008B7C4C  E8 4F 1B 00 00                  call 0x1408b97a0
008B7C51  44 8B E0                        mov r12d, eax
008B7C54  48 85 DB                        test rbx, rbx
008B7C57  74 0A                           je 0x1408b7c63
008B7C59  33 D2                           xor edx, edx
008B7C5B  48 8B CB                        mov rcx, rbx
008B7C5E  E8 0D AC 2C 00                  call 0x140b82870
008B7C63  80 7C 24 41 00                  cmp byte ptr [rsp + 0x41], 0
008B7C68  0F 84 E8 00 00 00               je 0x1408b7d56
008B7C6E  65 4C 8B 34 25 88 01 00 00      mov r14, qword ptr gs:[0x188]
008B7C77  48 89 74 24 78                  mov qword ptr [rsp + 0x78], rsi
008B7C7C  48 89 B4 24 80 00 00 00         mov qword ptr [rsp + 0x80], rsi
008B7C84  48 89 74 24 60                  mov qword ptr [rsp + 0x60], rsi
008B7C89  65 48 8B 3C 25 88 01 00 00      mov rdi, qword ptr gs:[0x188]
008B7C92  48 89 BC 24 98 00 00 00         mov qword ptr [rsp + 0x98], rdi
008B7C9A  48 8B 5C 24 68                  mov rbx, qword ptr [rsp + 0x68]
008B7C9F  48 85 DB                        test rbx, rbx
008B7CA2  0F 84 E9 02 00 00               je 0x1408b7f91
008B7CA8  48 8B CB                        mov rcx, rbx
008B7CAB  E8 DC 99 BB FF                  call 0x14047168c
008B7CB0  48 85 C0                        test rax, rax
008B7CB3  0F 85 71 03 00 00               jne 0x1408b802a
008B7CB9  48 8B FB                        mov rdi, rbx
008B7CBC  0F B6 44 24 71                  movzx eax, byte ptr [rsp + 0x71]
008B7CC1  F6 D8                           neg al
008B7CC3  48 1B C9                        sbb rcx, rcx
008B7CC6  83 E1 04                        and ecx, 4
008B7CC9  8B 5C 24 74                     mov ebx, dword ptr [rsp + 0x74]
008B7CCD  83 E3 03                        and ebx, 3
008B7CD0  48 83 E7 F8                     and rdi, 0xfffffffffffffff8
008B7CD4  48 0B DF                        or rbx, rdi
008B7CD7  48 0B D9                        or rbx, rcx
008B7CDA  48 8B BC 24 98 00 00 00         mov rdi, qword ptr [rsp + 0x98]
008B7CE2  48 8B D7                        mov rdx, rdi
008B7CE5  49 8B CE                        mov rcx, r14
008B7CE8  E8 F3 19 C3 FF                  call 0x1404e96e0
008B7CED  41 8B 86 A0 05 00 00            mov eax, dword ptr [r14 + 0x5a0]
008B7CF4  A8 08                           test al, 8
008B7CF6  0F 85 DA 03 00 00               jne 0x1408b80d6
008B7CFC  48 83 7C 24 68 00               cmp qword ptr [rsp + 0x68], 0
008B7D02  0F 84 72 02 00 00               je 0x1408b7f7a
008B7D08  49 89 9E 38 05 00 00            mov qword ptr [r14 + 0x538], rbx
008B7D0F  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
008B7D14  49 89 86 48 06 00 00            mov qword ptr [r14 + 0x648], rax
008B7D1B  80 7C 24 70 00                  cmp byte ptr [rsp + 0x70], 0
008B7D20  0F 84 43 02 00 00               je 0x1408b7f69
008B7D26  F0 41 81 8E A0 05 00 00 00 01 00 00  lock or dword ptr [r14 + 0x5a0], 0x100
008B7D32  F0 41 83 8E A0 05 00 00 08      lock or dword ptr [r14 + 0x5a0], 8
008B7D3B  32 DB                           xor bl, bl
008B7D3D  48 8B D7                        mov rdx, rdi
008B7D40  49 8B CE                        mov rcx, r14
008B7D43  E8 78 1A C3 FF                  call 0x1404e97c0
008B7D48  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
008B7D4D  48 85 C9                        test rcx, rcx
008B7D50  0F 85 A4 03 00 00               jne 0x1408b80fa
008B7D56  45 85 E4                        test r12d, r12d
008B7D59  0F 88 ED 00 00 00               js 0x1408b7e4c
008B7D5F  80 7C 24 50 00                  cmp byte ptr [rsp + 0x50], 0
008B7D64  0F 84 E2 00 00 00               je 0x1408b7e4c
008B7D6A  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
008B7D6F  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
008B7D77  4C 8B F6                        mov r14, rsi
008B7D7A  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
008B7D7F  8B 87 A0 05 00 00               mov eax, dword ptr [rdi + 0x5a0]
008B7D85  A8 08                           test al, 8
008B7D87  0F 84 BF 00 00 00               je 0x1408b7e4c
008B7D8D  65 48 8B 1C 25 88 01 00 00      mov rbx, qword ptr gs:[0x188]
008B7D96  48 89 9C 24 98 00 00 00         mov qword ptr [rsp + 0x98], rbx
008B7D9E  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
008B7DA3  E8 78 7C 95 FF                  call 0x14020fa20
008B7DA8  48 8B D3                        mov rdx, rbx
008B7DAB  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
008B7DB0  48 8B CB                        mov rcx, rbx
008B7DB3  E8 28 19 C3 FF                  call 0x1404e96e0
008B7DB8  8B 83 A0 05 00 00               mov eax, dword ptr [rbx + 0x5a0]
008B7DBE  A8 08                           test al, 8
008B7DC0  0F 84 A1 02 00 00               je 0x1408b8067
008B7DC6  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
008B7DCB  48 8B 8B 38 05 00 00            mov rcx, qword ptr [rbx + 0x538]
008B7DD2  48 8B C1                        mov rax, rcx
008B7DD5  48 83 E0 F8                     and rax, 0xfffffffffffffff8
008B7DD9  49 3B C7                        cmp rax, r15
008B7DDC  0F 85 3C 03 00 00               jne 0x1408b811e
008B7DE2  F7 83 A0 05 00 00 00 01 00 00   test dword ptr [rbx + 0x5a0], 0x100
008B7DEC  0F 84 2C 03 00 00               je 0x1408b811e
008B7DF2  83 E1 07                        and ecx, 7
008B7DF5  48 0B 8C 24 80 00 00 00         or rcx, qword ptr [rsp + 0x80]
008B7DFD  48 89 8B 38 05 00 00            mov qword ptr [rbx + 0x538], rcx
008B7E04  4C 8B B3 48 06 00 00            mov r14, qword ptr [rbx + 0x648]
008B7E0B  48 89 B3 48 06 00 00            mov qword ptr [rbx + 0x648], rsi
008B7E12  F0 81 A7 A0 05 00 00 FF FE FF FF  lock and dword ptr [rdi + 0x5a0], 0xfffffeff
008B7E1D  48 8B 94 24 98 00 00 00         mov rdx, qword ptr [rsp + 0x98]
008B7E25  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
008B7E2A  E8 91 19 C3 FF                  call 0x1404e97c0
008B7E2F  85 F6                           test esi, esi
008B7E31  0F 88 F1 02 00 00               js 0x1408b8128
008B7E37  49 8B CF                        mov rcx, r15
008B7E3A  E8 11 15 A4 FF                  call 0x1402f9350
008B7E3F  4D 85 F6                        test r14, r14
008B7E42  74 08                           je 0x1408b7e4c
008B7E44  49 8B CE                        mov rcx, r14
008B7E47  E8 04 15 A4 FF                  call 0x1402f9350
008B7E4C  BA 53 68 72 74                  mov edx, 0x74726853
008B7E51  49 8B CF                        mov rcx, r15
008B7E54  E8 87 FA A3 FF                  call 0x1402f78e0
008B7E59  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
008B7E5E  48 85 C9                        test rcx, rcx
008B7E61  74 05                           je 0x1408b7e68
008B7E63  E8 E8 14 A4 FF                  call 0x1402f9350
008B7E68  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
008B7E6D  E8 DE 14 A4 FF                  call 0x1402f9350
008B7E72  45 85 E4                        test r12d, r12d
008B7E75  78 13                           js 0x1408b7e8a
008B7E77  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
008B7E7F  49 89 45 00                     mov qword ptr [r13], rax
008B7E83  EB 05                           jmp 0x1408b7e8a
008B7E85  E9 FF FA FF FF                  jmp 0x1408b7989
008B7E8A  41 8B C4                        mov eax, r12d
008B7E8D  E9 F7 FA FF FF                  jmp 0x1408b7989
008B7E92  65 48 8B 3C 25 88 01 00 00      mov rdi, qword ptr gs:[0x188]
008B7E9B  48 8B D7                        mov rdx, rdi
008B7E9E  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
008B7EA3  48 8B CB                        mov rcx, rbx
008B7EA6  E8 75 C8 B0 FF                  call 0x1403c4720
008B7EAB  8B 83 A0 05 00 00               mov eax, dword ptr [rbx + 0x5a0]
008B7EB1  A8 08                           test al, 8
008B7EB3  0F 84 69 01 00 00               je 0x1408b8022
008B7EB9  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
008B7EBE  4C 8B BB 38 05 00 00            mov r15, qword ptr [rbx + 0x538]
008B7EC5  49 83 E7 F8                     and r15, 0xfffffffffffffff8
008B7EC9  8B 83 A0 05 00 00               mov eax, dword ptr [rbx + 0x5a0]
008B7ECF  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
008B7ED3  BA 53 68 72 74                  mov edx, 0x74726853
008B7ED8  49 8B CF                        mov rcx, r15
008B7EDB  E8 30 88 95 FF                  call 0x140210710
008B7EE0  8B 83 38 05 00 00               mov eax, dword ptr [rbx + 0x538]
008B7EE6  83 E0 03                        and eax, 3
008B7EE9  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
008B7EED  0F B6 83 38 05 00 00            movzx eax, byte ptr [rbx + 0x538]
008B7EF4  C0 E8 02                        shr al, 2
008B7EF7  24 01                           and al, 1
008B7EF9  88 44 24 43                     mov byte ptr [rsp + 0x43], al
008B7EFD  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
008B7F01  C1 E8 08                        shr eax, 8
008B7F04  24 01                           and al, 1
008B7F06  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
008B7F0A  48 8B D7                        mov rdx, rdi
008B7F0D  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
008B7F12  E8 29 AF B0 FF                  call 0x1403c2e40
008B7F17  0F B6 9C 24 40 01 00 00         movzx ebx, byte ptr [rsp + 0x140]
008B7F1F  8B 7C 24 78                     mov edi, dword ptr [rsp + 0x78]
008B7F23  E9 4D FA FF FF                  jmp 0x1408b7975
008B7F28  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
008B7F30  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008B7F35  44 88 64 24 28                  mov byte ptr [rsp + 0x28], r12b
008B7F3A  48 8B 05 DF 00 72 00            mov rax, qword ptr [rip + 0x7200df]
008B7F41  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008B7F46  44 8B 8C 24 38 01 00 00         mov r9d, dword ptr [rsp + 0x138]
008B7F4E  45 33 C0                        xor r8d, r8d
008B7F51  41 8B D6                        mov edx, r14d
008B7F54  49 8B CF                        mov rcx, r15
008B7F57  E8 C4 F4 FF FF                  call 0x1408b7420
008B7F5C  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
008B7F64  E9 E8 FC FF FF                  jmp 0x1408b7c51
008B7F69  F0 41 81 A6 A0 05 00 00 FF FE FF FF  lock and dword ptr [r14 + 0x5a0], 0xfffffeff
008B7F75  E9 B8 FD FF FF                  jmp 0x1408b7d32
008B7F7A  F0 41 0F BA B6 A0 05 00 00 03   lock btr dword ptr [r14 + 0x5a0], 3
008B7F84  0F 83 B1 FD FF FF               jae 0x1408b7d3b
008B7F8A  B3 01                           mov bl, 1
008B7F8C  E9 AC FD FF FF                  jmp 0x1408b7d3d
008B7F91  48 8B DE                        mov rbx, rsi
008B7F94  E9 49 FD FF FF                  jmp 0x1408b7ce2
008B7F99  0F B6 40 01                     movzx eax, byte ptr [rax + 1]
008B7F9D  44 8D 24 85 08 00 00 00         lea r12d, [rax*4 + 8]
008B7FA5  41 8D 54 24 03                  lea edx, [r12 + 3]
008B7FAA  B8 FC FF FF FF                  mov eax, 0xfffffffc
008B7FAF  48 23 D0                        and rdx, rax
008B7FB2  B9 00 01 00 00                  mov ecx, 0x100
008B7FB7  41 B8 53 65 53 69               mov r8d, 0x69536553
008B7FBD  E8 2E A1 2C 00                  call 0x140b820f0
008B7FC2  48 8B F8                        mov rdi, rax
008B7FC5  48 85 C0                        test rax, rax
008B7FC8  0F 84 FD 00 00 00               je 0x1408b80cb
008B7FCE  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
008B7FD3  0F B6 42 01                     movzx eax, byte ptr [rdx + 1]
008B7FD7  8D 04 85 08 00 00 00            lea eax, [rax*4 + 8]
008B7FDE  41 3B C4                        cmp eax, r12d
008B7FE1  77 0B                           ja 0x1408b7fee
008B7FE3  44 8B C0                        mov r8d, eax
008B7FE6  48 8B CF                        mov rcx, rdi
008B7FE9  E8 52 E8 E0 FF                  call 0x1406c6840
008B7FEE  48 89 BC 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rdi
008B7FF6  E9 05 FC FF FF                  jmp 0x1408b7c00
008B7FFB  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
008B8000  48 8B 88 48 06 00 00            mov rcx, qword ptr [rax + 0x648]
008B8007  48 85 C9                        test rcx, rcx
008B800A  74 0C                           je 0x1408b8018
008B800C  48 8B 91 50 04 00 00            mov rdx, qword ptr [rcx + 0x450]
008B8013  48 89 54 24 60                  mov qword ptr [rsp + 0x60], rdx
008B8018  0F 95 44 24 40                  setne byte ptr [rsp + 0x40]
008B801D  E9 6C FA FF FF                  jmp 0x1408b7a8e
008B8022  4C 8B FE                        mov r15, rsi
008B8025  E9 E0 FE FF FF                  jmp 0x1408b7f0a
008B802A  E8 5D 96 BB FF                  call 0x14047168c
008B802F  48 8B F8                        mov rdi, rax
008B8032  48 8B C8                        mov rcx, rax
008B8035  E8 E6 79 95 FF                  call 0x14020fa20
008B803A  48 89 5C 24 60                  mov qword ptr [rsp + 0x60], rbx
008B803F  E9 78 FC FF FF                  jmp 0x1408b7cbc
008B8044  4C 8B AC 24 50 01 00 00         mov r13, qword ptr [rsp + 0x150]
008B804C  E9 D0 F8 FF FF                  jmp 0x1408b7921
008B8051  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
008B8056  48 89 B3 48 06 00 00            mov qword ptr [rbx + 0x648], rsi
008B805D  E8 EE 12 A4 FF                  call 0x1402f9350
008B8062  E9 D2 F9 FF FF                  jmp 0x1408b7a39
008B8067  BE 7C 00 00 C0                  mov esi, 0xc000007c
008B806C  E9 AC FD FF FF                  jmp 0x1408b7e1d
008B8071  89 74 24 74                     mov dword ptr [rsp + 0x74], esi
008B8075  66 C7 44 24 70 00 00            mov word ptr [rsp + 0x70], 0
008B807C  48 89 74 24 68                  mov qword ptr [rsp + 0x68], rsi
008B8081  C6 44 24 41 00                  mov byte ptr [rsp + 0x41], 0
008B8086  E9 D5 F9 FF FF                  jmp 0x1408b7a60
008B808B  BA 44 66 6C 74                  mov edx, 0x746c6644
008B8090  48 8B CF                        mov rcx, rdi
008B8093  E8 48 F8 A3 FF                  call 0x1402f78e0
008B8098  E9 74 FA FF FF                  jmp 0x1408b7b11
008B809D  48 89 B4 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rsi
008B80A5  E9 EA FA FF FF                  jmp 0x1408b7b94
008B80AA  BA 53 68 72 74                  mov edx, 0x74726853
008B80AF  49 8B CF                        mov rcx, r15
008B80B2  E8 29 F8 A3 FF                  call 0x1402f78e0
008B80B7  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
008B80BC  E8 8F 12 A4 FF                  call 0x1402f9350
008B80C1  B8 A6 00 00 C0                  mov eax, 0xc00000a6
008B80C6  E9 BE F8 FF FF                  jmp 0x1408b7989
008B80CB  41 BC 9A 00 00 C0               mov r12d, 0xc000009a
008B80D1  E9 7E FB FF FF                  jmp 0x1408b7c54
008B80D6  49 8B 86 38 05 00 00            mov rax, qword ptr [r14 + 0x538]
008B80DD  48 83 E0 F8                     and rax, 0xfffffffffffffff8
008B80E1  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
008B80E6  49 8B 86 48 06 00 00            mov rax, qword ptr [r14 + 0x648]
008B80ED  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
008B80F5  E9 02 FC FF FF                  jmp 0x1408b7cfc
008B80FA  E8 51 12 A4 FF                  call 0x1402f9350
008B80FF  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
008B8107  48 85 C0                        test rax, rax
008B810A  0F 84 D2 27 26 00               je 0x140b1a8e2
008B8110  48 8B C8                        mov rcx, rax
008B8113  E8 38 12 A4 FF                  call 0x1402f9350
008B8118  90                              nop
008B8119  E9 C4 27 26 00                  jmp 0x140b1a8e2
008B811E  BE 01 00 00 C0                  mov esi, 0xc0000001
008B8123  E9 F5 FC FF FF                  jmp 0x1408b7e1d
008B8128  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
008B8130  E9 12 FD FF FF                  jmp 0x1408b7e47
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtOpenThreadTokenEx(__int64 a1, int a2, unsigned __int8 a3, int a4, __int64 a5)
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
    unsigned __int64 v_stack_m108;
    unsigned __int16 v_stack_m26;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m8;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m8C;
    unsigned __int8 v_stack_m8F;
    unsigned __int8 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int8 v_stack_mBD;
    unsigned __int8 v_stack_mBE;
    unsigned __int8 v_stack_mBF;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int8 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int8 v_stack_mE5;
    unsigned __int8 v_stack_mE6;
    unsigned __int8 v_stack_mE7;
    unsigned __int8 v_stack_mE8;
    unsigned int v_stack_p10;
    unsigned int v_stack_p38;
    unsigned __int8 v_stack_p40;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 32) = v_rsi;
    *(unsigned __int8 *)(v_rsp + 24) = a3;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (256);
    v_rsi = 0;
    v_stack_mD0 = 0;
    v_stack_mD8 = 0;
    v_stack_mE5 = 0;
    v_stack_mB0 = 0;
    v_stack_mC0 = v_xmm0;
    v_stack_mE7 = 0;
    *(unsigned __int64 *)(v_rsp - 152) = 0;
    result = 0;
    *(unsigned __int64 *)(v_rsp - 80) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 64) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 48) = 0;
    v_stack_m88 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 120) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 104) = 0;
    *(unsigned int *)(v_rsp - 96) = 0;
    *(unsigned __int64 *)(v_rsp - 160) = 0;
    v_stack_mC8 = 0;
    v_stack_mE8 = 0;
    v_stack_mE6 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_r14 = (unsigned int)(0x11FF2ULL);
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) != 0) { v_r14 = (unsigned int)((unsigned int)(0x1DF2ULL)); }
    v_r14 = (unsigned int)((v_r14) & (a4));
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_008B8044;
    if (a5 < a1) { a1 = a5; }
    *(unsigned __int64 *)(a1) = *(unsigned __int64 *)(a1);
    goto loc_008B7921;
loc_008B7921:
    v_stack_mE0 = 0;
    v_stack_m100 = 0;
    v_stack_m108 = v_stack_mE0;
    result = ObReferenceObjectByHandle(a1, (unsigned int)(0x800ULL), *(unsigned __int64 *)(v_rip + 7401871), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if (sign_flag) goto loc_008B7989;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_mE0 + 1440)))) & (8)) != 0) goto loc_008B7E92;
loc_008B7975:
    if (0 != 0) goto loc_008B79A7;
    result = ObfDereferenceObject(v_stack_mE0, (unsigned int)(0x800ULL), *(unsigned __int64 *)(v_rip + 7401871), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
loc_008B7989:
    return (unsigned int)(0xC000007CULL);
loc_008B79A7:
    if (0 == 0) goto loc_008B80AA;
    if ((unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 48)) == 0) goto loc_008B7A60;
    v_r12 = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1440)))) & (8)) == 0) goto loc_008B7A44;
    result = PspLockThreadSecurityExclusive(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(v_rip + 7401871), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if (condition_is_above_or_equal) goto loc_008B7A39;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1336))) & (3));
    v_stack_m8C = (unsigned int)(result);
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1336))) >> (2));
    result = (unsigned __int8)((result) & (1));
    v_stack_m8F = (unsigned __int8)(result);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1440))) >> (8));
    result = (unsigned __int8)((result) & (1));
    v_stack_m90 = (unsigned __int8)(result);
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1336)) & (-8);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1608) != 0) goto loc_008B8051;
    v_stack_m98 = a1;
loc_008B7A39:
    result = PspUnlockThreadSecurityExclusive(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(v_rip + 7401871), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
loc_008B7A44:
    if (1 == 0) goto loc_008B8071;
    v_stack_mBF = 1;
loc_008B7A60:
    if (v_stack_mB0 == 0) goto loc_008B7F28;
    if ((unsigned __int8)(v_stack_p40) == 0) goto loc_008B7FFB;
    result = v_stack_m98;
    if (v_stack_m98 != 0) {
        result = *(unsigned __int64 *)(v_stack_m98 + 1104);
        v_stack_mA0 = result;
        v_stack_mC0 = 1;
    }
    result = PsReferencePrimaryTokenWithTag(*(unsigned __int64 *)(v_stack_mB8 + 544), (unsigned int)(0x746C6644ULL), *(unsigned __int64 *)(v_rip + 7401871), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    result = SepCreateImpersonationTokenDacl(0, result, v_stack_m78, *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
loc_008B7ACE:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB8 + 544) + 584)) ^ (result);
    if (a1 >= 15) goto loc_008B808B;
    if (a1 != 15) goto loc_008B7ACE;
    result = ((*(unsigned int *)(v_rip + 7394587)) != ((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 72)))) ? 1 : 0;
    if ((unsigned int)(result) != 0) {
        a1 = result - 48;
        a2 = 0;
        a4 = 0x746C6644ULL;
        a3 = a2 + 1;
        result = ObpPushStackInfo(a1, a2, a3, a4);
    }
    if (sign_flag) goto loc_008B7C54;
    if (v_stack_m78 == 0) goto loc_008B7B58;
    v_stack_m28 = 1;
    result = v_stack_m26;
    if (!(sign_flag)) {
        v_stack_m8 = v_stack_m78;
        a1 = 0xFFF7ULL;
        result = (unsigned __int16)((v_stack_m26) & ((unsigned __int16)(a1)));
        result = (unsigned __int16)((result) | (4));
        v_stack_m26 = (unsigned __int16)(result);
    }
    v_stack_m60 = 48;
    v_stack_m58 = *(unsigned __int64 *)(v_stack_m28 + 72);
    v_stack_m48 = (unsigned int)(v_r14);
    v_stack_m50 = *(unsigned __int64 *)(v_stack_m28 + 72);
    if (v_stack_m78 == 0) goto loc_008B809D;
    v_stack_m40 = v_stack_m28;
loc_008B7B94:
    v_stack_m38 = *(unsigned __int64 *)(v_stack_m28 + 72);
    v_stack_mC8 = v_stack_mA8;
    v_stack_mD0 = 0;
    v_stack_mD8 = 0;
    v_stack_mE0 = (unsigned int)((unsigned int)(v_stack_m88));
    result = SepDuplicateToken(0, v_stack_m60, v_stack_mBD, 2);
    if (sign_flag) goto loc_008B7C54;
    if (v_stack_mC0 == 0) goto loc_008B7C1A;
    v_stack_m30 = *(unsigned __int64 *)(v_stack_m28 + 72);
    if (v_stack_mA0 != 0) goto loc_008B7F99;
loc_008B7C00:
    result = v_stack_mA0;
    if (*(unsigned __int64 *)(v_stack_mA8 + 1104) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(v_stack_mA8 + 1104), a2, v_stack_mBD, 2);
    }
    *(unsigned __int64 *)(v_stack_mA8 + 1104) = *(unsigned __int64 *)(v_stack_m28 + 72);
loc_008B7C1A:
    result = ObfReferenceObject(v_stack_mA8, a2, v_stack_mBD, 2);
    v_stack_mD0 = v_stack_m70;
    v_stack_mD8 = *(unsigned __int64 *)(v_stack_m28 + 72);
    v_stack_mE0 = (unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 72));
    a4 = 0;
    a2 = 0;
    result = ObInsertObjectEx(v_stack_mA8, a2, (unsigned int)(v_stack_p38), a4);
loc_008B7C51:
loc_008B7C54:
    if (v_stack_m78 != 0) {
        a2 = 0;
        a1 = v_stack_m78;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(v_stack_p38), a4);
    }
    if (v_stack_mBF == 0) goto loc_008B7D56;
    v_stack_m88 = *(unsigned __int64 *)(v_stack_m28 + 72);
    v_stack_m80 = *(unsigned __int64 *)(v_stack_m28 + 72);
    v_stack_mA0 = *(unsigned __int64 *)(v_stack_m28 + 72);
    v_stack_m68 = *(unsigned __int64 *)(gs_base + (0 + 392));
    if (v_stack_m98 == 0) goto loc_008B7F91;
    result = SeQueryTokenTrustLink(v_stack_m98, a2, (unsigned int)(v_stack_p38), a4);
    if (result != 0) goto loc_008B802A;
loc_008B7CBC:
    result = (unsigned __int8)(-(v_stack_m8F));
    a1 = (unsigned int)((v_stack_m98) & (4));
    v_rbx = (unsigned int)(((unsigned int)(v_stack_m8C)) & (3));
    v_rdi = (v_stack_m98) & (-8);
    v_rbx = (v_rbx) | (v_rdi);
    v_rbx = (v_rbx) | (a1);
loc_008B7CE2:
    result = PspLockThreadSecurityExclusive(*(unsigned __int64 *)(gs_base + (0 + 392)), v_stack_m68, (unsigned int)(v_stack_p38), a4);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1440)))) & (8)) != 0) goto loc_008B80D6;
loc_008B7CFC:
    if (v_stack_m98 == 0) goto loc_008B7F7A;
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1336) = v_rbx;
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1608) = v_stack_mA0;
    if (v_stack_m90 == 0) goto loc_008B7F69;
loc_008B7D32:
loc_008B7D3B:
    v_rbx = 0;
loc_008B7D3D:
    result = PspUnlockThreadSecurityExclusive(*(unsigned __int64 *)(gs_base + (0 + 392)), v_stack_m68, (unsigned int)(v_stack_p38), a4);
    if (v_stack_m88 != 0) goto loc_008B80FA;
loc_008B7D56:
    if (sign_flag) goto loc_008B7E4C;
    if (v_stack_mB0 == 0) goto loc_008B7E4C;
    v_stack_m80 = v_stack_mA8;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_mB8 + 1440)))) & (8)) == 0) goto loc_008B7E4C;
    v_stack_m68 = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = ObfReferenceObject(v_stack_mA8, v_stack_m68, (unsigned int)(v_stack_p38), a4);
    result = PspLockThreadSecurityExclusive(v_stack_mB8, *(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)(v_stack_p38), a4);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_mB8 + 1440)))) & (8)) == 0) goto loc_008B8067;
    result = (*(unsigned __int64 *)(v_stack_mB8 + 1336)) & (-8);
    if (result != 0) goto loc_008B811E;
    if (((*(unsigned int *)(v_stack_mB8 + 1440)) & (256)) == 0) goto loc_008B811E;
    a1 = (unsigned int)((*(unsigned __int64 *)(v_stack_mB8 + 1336)) & (7));
    a1 = (a1) | (v_stack_m80);
    *(unsigned __int64 *)(v_stack_mB8 + 1336) = a1;
    *(unsigned __int64 *)(v_stack_mB8 + 1608) = *(unsigned __int64 *)(v_stack_m28 + 72);
loc_008B7E1D:
    result = PspUnlockThreadSecurityExclusive(v_stack_mB8, v_stack_m68, (unsigned int)(v_stack_p38), a4);
    if (sign_flag) goto loc_008B8128;
    result = ObfDereferenceObject(0, v_stack_m68, (unsigned int)(v_stack_p38), a4);
    if (*(unsigned __int64 *)(v_stack_mB8 + 1608) == 0) goto loc_008B7E4C;
loc_008B7E47:
    result = ObfDereferenceObject(*(unsigned __int64 *)(v_stack_mB8 + 1608), v_stack_m68, (unsigned int)(v_stack_p38), a4);
loc_008B7E4C:
    result = ObfDereferenceObjectWithTag(0, (unsigned int)(0x74726853ULL), (unsigned int)(v_stack_p38), a4);
    if (v_stack_mA8 != 0) {
        result = ObfDereferenceObject(v_stack_mA8, (unsigned int)(0x74726853ULL), (unsigned int)(v_stack_p38), a4);
    }
    result = ObfDereferenceObject(v_stack_mB8, (unsigned int)(0x74726853ULL), (unsigned int)(v_stack_p38), a4);
    if (sign_flag) goto loc_008B7E8A;
    *(unsigned __int64 *)(a5) = v_stack_m70;
    goto loc_008B7E8A;
loc_008B7E8A:
    goto loc_008B7989;
loc_008B7E92:
    result = PspLockThreadSecurityShared(v_stack_mB8, *(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)(v_stack_p38), a4);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_mB8 + 1440)))) & (8)) == 0) goto loc_008B8022;
    v_r15 = (*(unsigned __int64 *)(v_stack_mB8 + 1336)) & (-8);
    v_stack_mB0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mB8 + 1440)));
    result = ObfReferenceObjectWithTag(v_r15, (unsigned int)(0x74726853ULL), (unsigned int)(v_stack_p38), a4);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_mB8 + 1336))) & (3));
    v_stack_m88 = (unsigned int)(result);
    result = (unsigned __int8)((*(unsigned __int8 *)(v_stack_mB8 + 1336)) >> (2));
    result = (unsigned __int8)((result) & (1));
    v_stack_mBD = (unsigned __int8)(result);
    result = (unsigned int)(((unsigned int)(v_stack_mB0)) >> (8));
    result = (unsigned __int8)((result) & (1));
    v_stack_mB0 = (unsigned int)(result);
loc_008B7F0A:
    result = PspUnlockThreadSecurityShared(v_stack_mB8, *(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)(v_stack_p38), a4);
    goto loc_008B7975;
loc_008B7F28:
    v_stack_mD0 = v_stack_m70;
    v_stack_mD8 = (unsigned __int8)((unsigned int)((unsigned int)(result)));
    v_stack_mE0 = *(unsigned __int64 *)(v_rip + 7471327);
    a3 = 0;
    result = ObOpenObjectByPointer(v_r15, (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_mB8 + 1608))), a3, (unsigned int)(v_stack_p38));
    goto loc_008B7C51;
loc_008B7F69:
    goto loc_008B7D32;
loc_008B7F7A:
    if (condition_is_above_or_equal) goto loc_008B7D3B;
    goto loc_008B7D3D;
loc_008B7F91:
    goto loc_008B7CE2;
loc_008B7F99:
    a2 = (*(unsigned __int8 *)(result + 1) * 4 + 8 + 3) & ((unsigned int)(0xFFFFFFFCULL));
    result = ExAllocatePool2(256, a2, (unsigned int)(0x69536553ULL), (unsigned int)(v_stack_p38));
    if (result == 0) goto loc_008B80CB;
    result = *(unsigned __int8 *)(v_stack_mA0 + 1) * 4 + 8;
    if (((unsigned int)(*(unsigned __int8 *)(v_stack_mA0 + 1) * 4 + 8)) <= ((unsigned int)(*(unsigned __int8 *)(result + 1) * 4 + 8))) {
        a3 = (unsigned int)(*(unsigned __int8 *)(v_stack_mA0 + 1) * 4 + 8);
        a1 = result;
        result = memcpy(a1, v_stack_mA0, a3, (unsigned int)(v_stack_p38));
    }
    v_stack_m30 = result;
    goto loc_008B7C00;
loc_008B7FFB:
    if (*(unsigned __int64 *)(v_stack_mB8 + 1608) != 0) {
        a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB8 + 1608) + 1104);
        v_stack_mA0 = a2;
    }
    goto loc_008B7A8E;
loc_008B8022:
    goto loc_008B7F0A;
loc_008B802A:
    result = SeQueryTokenTrustLink(*(unsigned __int64 *)(v_stack_mB8 + 1608), a2, a3, (unsigned int)(v_stack_p38));
    result = ObfReferenceObject(result, a2, a3, (unsigned int)(v_stack_p38));
    v_stack_mA0 = *(unsigned __int64 *)(v_stack_m28 + 72);
    goto loc_008B7CBC;
loc_008B8044:
    goto loc_008B7921;
loc_008B8051:
    v_stack_m98 = result;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 1608) = *(unsigned __int64 *)(v_stack_m28 + 72);
    result = ObfDereferenceObject(result, a2, a3, (unsigned int)(v_stack_p38));
    goto loc_008B7A39;
loc_008B8067:
    goto loc_008B7E1D;
loc_008B8071:
    v_stack_m8C = (unsigned int)((unsigned int)(0xC000007CULL));
    v_stack_m90 = 0;
    v_stack_m98 = (unsigned int)(0xC000007CULL);
    v_stack_mBF = 0;
    goto loc_008B7A60;
loc_008B808B:
    result = ObfDereferenceObjectWithTag(result, (unsigned int)(0x746C6644ULL), a3, (unsigned int)(v_stack_p38));
    goto loc_008B7B11;
loc_008B809D:
    v_stack_m40 = (unsigned int)(0xC000007CULL);
    goto loc_008B7B94;
loc_008B80AA:
    result = ObfDereferenceObjectWithTag(*(unsigned __int64 *)(v_stack_m28 + 72), (unsigned int)(0x74726853ULL), a3, (unsigned int)(v_stack_p38));
    result = ObfDereferenceObject(v_stack_mB8, (unsigned int)(0x74726853ULL), a3, (unsigned int)(v_stack_p38));
    goto loc_008B7989;
loc_008B80CB:
    goto loc_008B7C54;
loc_008B80D6:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB8 + 1608) + 1336)) & (-8);
    v_stack_m88 = result;
    v_stack_m80 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB8 + 1608) + 1608);
    goto loc_008B7CFC;
loc_008B80FA:
    result = ObfDereferenceObject(v_stack_mB8, (unsigned int)(0x74726853ULL), a3, (unsigned int)(v_stack_p38));
    result = ObfDereferenceObject(v_stack_m80, (unsigned int)(0x74726853ULL), a3, (unsigned int)(v_stack_p38));
loc_008B811E:
    goto loc_008B7E1D;
loc_008B8128:
    goto loc_008B7E47;
}
```

## 5. (Beta) C Style

```c
int64_t NtOpenThreadTokenEx(int64_t Arg1, int32_t Arg2, uint8_t Arg3, int32_t Arg4, int64_t Arg5)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint16_t v_stack_m26;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint32_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m8;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint32_t v_stack_m8C;
    uint8_t v_stack_m8F;
    uint8_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint32_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint8_t v_stack_mBD;
    uint8_t v_stack_mBE;
    uint8_t v_stack_mBF;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint8_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint8_t v_stack_mE5;
    uint8_t v_stack_mE6;
    uint8_t v_stack_mE7;
    uint8_t v_stack_mE8;
    uint32_t v_stack_p10;
    uint32_t v_stack_p38;
    uint8_t v_stack_p40;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x20) = local_rsi;
    *(uint8_t *)(local_rsp + 0x18) = Arg3;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (256);
    local_rsi = 0;
    v_stack_mD0 = 0;
    v_stack_mD8 = 0;
    v_stack_mE5 = 0;
    v_stack_mB0 = 0;
    v_stack_mC0 = v_xmm0;
    v_stack_mE7 = 0;
    *(uint64_t *)(local_rsp - 0x98) = 0;
    result = 0;
    *(uint64_t *)(local_rsp - 0x50) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x40) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x30) = 0;
    v_stack_m88 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x78) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x68) = 0;
    *(uint32_t *)(local_rsp - 0x60) = 0;
    *(uint64_t *)(local_rsp - 0xA0) = 0;
    v_stack_mC8 = 0;
    v_stack_mE8 = 0;
    v_stack_mE6 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    local_r14 = (uint32_t)(0x11FF2ULL);
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) != 0) { local_r14 = (uint32_t)((uint32_t)(0x1DF2ULL)); }
    local_r14 = (uint32_t)((local_r14) & (Arg4));
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_008B8044;
    if (Arg5 < Arg1) { Arg1 = Arg5; }
    *(uint64_t *)(Arg1) = *(uint64_t *)(Arg1);
    goto loc_008B7921;
loc_008B7921:
    v_stack_mE0 = 0;
    v_stack_m100 = 0;
    v_stack_m108 = v_stack_mE0;
    result = ObReferenceObjectByHandle(Arg1, (uint32_t)(0x800ULL), *(uint64_t *)(v_rip + 0x70F18F), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if (sign_flag) goto loc_008B7989;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_mE0 + 0x5A0)))) & (8)) != 0) goto loc_008B7E92;
loc_008B7975:
    if (0 != 0) goto loc_008B79A7;
    result = ObfDereferenceObject(v_stack_mE0, (uint32_t)(0x800ULL), *(uint64_t *)(v_rip + 0x70F18F), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
loc_008B7989:
    return (uint32_t)(0xC000007CULL);
loc_008B79A7:
    if (0 == 0) goto loc_008B80AA;
    if ((uint8_t)(*(uint64_t *)(v_stack_m28 + 0x30)) == 0) goto loc_008B7A60;
    local_r12 = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A0)))) & (8)) == 0) goto loc_008B7A44;
    result = PspLockThreadSecurityExclusive(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(v_rip + 0x70F18F), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if (condition_is_above_or_equal) goto loc_008B7A39;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x538))) & (3));
    v_stack_m8C = (uint32_t)(result);
    result = (uint8_t)(((uint8_t)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x538))) >> (2));
    result = (uint8_t)((result) & (1));
    v_stack_m8F = (uint8_t)(result);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A0))) >> (8));
    result = (uint8_t)((result) & (1));
    v_stack_m90 = (uint8_t)(result);
    Arg1 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x538)) & (-8);
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x648) != 0) goto loc_008B8051;
    v_stack_m98 = Arg1;
loc_008B7A39:
    result = PspUnlockThreadSecurityExclusive(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(v_rip + 0x70F18F), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
loc_008B7A44:
    if (1 == 0) goto loc_008B8071;
    v_stack_mBF = 1;
loc_008B7A60:
    if (v_stack_mB0 == 0) goto loc_008B7F28;
    if ((uint8_t)(v_stack_p40) == 0) goto loc_008B7FFB;
    result = v_stack_m98;
    if (v_stack_m98 != 0) {
        result = *(uint64_t *)(v_stack_m98 + 0x450);
        v_stack_mA0 = result;
        v_stack_mC0 = 1;
    }
    result = PsReferencePrimaryTokenWithTag(*(uint64_t *)(v_stack_mB8 + 0x220), (uint32_t)(0x746C6644ULL), *(uint64_t *)(v_rip + 0x70F18F), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    result = SepCreateImpersonationTokenDacl(0, result, v_stack_m78, *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
loc_008B7ACE:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_stack_mB8 + 0x220) + 0x248)) ^ (result);
    if (Arg1 >= 15) goto loc_008B808B;
    if (Arg1 != 15) goto loc_008B7ACE;
    result = ((*(uint32_t *)(v_rip + 0x70D51B)) != ((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x48)))) ? 1 : 0;
    if ((uint32_t)(result) != 0) {
        Arg1 = result - 48;
        Arg2 = 0;
        Arg4 = 0x746C6644ULL;
        Arg3 = Arg2 + 1;
        result = ObpPushStackInfo(Arg1, Arg2, Arg3, Arg4);
    }
    if (sign_flag) goto loc_008B7C54;
    if (v_stack_m78 == 0) goto loc_008B7B58;
    v_stack_m28 = 1;
    result = v_stack_m26;
    if (!(sign_flag)) {
        v_stack_m8 = v_stack_m78;
        Arg1 = 0xFFF7ULL;
        result = (uint16_t)((v_stack_m26) & ((uint16_t)(Arg1)));
        result = (uint16_t)((result) | (4));
        v_stack_m26 = (uint16_t)(result);
    }
    v_stack_m60 = 48;
    v_stack_m58 = *(uint64_t *)(v_stack_m28 + 0x48);
    v_stack_m48 = (uint32_t)(local_r14);
    v_stack_m50 = *(uint64_t *)(v_stack_m28 + 0x48);
    if (v_stack_m78 == 0) goto loc_008B809D;
    v_stack_m40 = v_stack_m28;
loc_008B7B94:
    v_stack_m38 = *(uint64_t *)(v_stack_m28 + 0x48);
    v_stack_mC8 = v_stack_mA8;
    v_stack_mD0 = 0;
    v_stack_mD8 = 0;
    v_stack_mE0 = (uint32_t)((uint32_t)(v_stack_m88));
    result = SepDuplicateToken(0, v_stack_m60, v_stack_mBD, 2);
    if (sign_flag) goto loc_008B7C54;
    if (v_stack_mC0 == 0) goto loc_008B7C1A;
    v_stack_m30 = *(uint64_t *)(v_stack_m28 + 0x48);
    if (v_stack_mA0 != 0) goto loc_008B7F99;
loc_008B7C00:
    result = v_stack_mA0;
    if (*(uint64_t *)(v_stack_mA8 + 0x450) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(v_stack_mA8 + 0x450), Arg2, v_stack_mBD, 2);
    }
    *(uint64_t *)(v_stack_mA8 + 0x450) = *(uint64_t *)(v_stack_m28 + 0x48);
loc_008B7C1A:
    result = ObfReferenceObject(v_stack_mA8, Arg2, v_stack_mBD, 2);
    v_stack_mD0 = v_stack_m70;
    v_stack_mD8 = *(uint64_t *)(v_stack_m28 + 0x48);
    v_stack_mE0 = (uint32_t)(*(uint64_t *)(v_stack_m28 + 0x48));
    Arg4 = 0;
    Arg2 = 0;
    result = ObInsertObjectEx(v_stack_mA8, Arg2, (uint32_t)(v_stack_p38), Arg4);
loc_008B7C51:
loc_008B7C54:
    if (v_stack_m78 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m78;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)(v_stack_p38), Arg4);
    }
    if (v_stack_mBF == 0) goto loc_008B7D56;
    v_stack_m88 = *(uint64_t *)(v_stack_m28 + 0x48);
    v_stack_m80 = *(uint64_t *)(v_stack_m28 + 0x48);
    v_stack_mA0 = *(uint64_t *)(v_stack_m28 + 0x48);
    v_stack_m68 = *(uint64_t *)(gs_base + (0 + 0x188));
    if (v_stack_m98 == 0) goto loc_008B7F91;
    result = SeQueryTokenTrustLink(v_stack_m98, Arg2, (uint32_t)(v_stack_p38), Arg4);
    if (result != 0) goto loc_008B802A;
loc_008B7CBC:
    result = (uint8_t)(-(v_stack_m8F));
    Arg1 = (uint32_t)((v_stack_m98) & (4));
    local_rbx = (uint32_t)(((uint32_t)(v_stack_m8C)) & (3));
    local_rdi = (v_stack_m98) & (-8);
    local_rbx = (local_rbx) | (local_rdi);
    local_rbx = (local_rbx) | (Arg1);
loc_008B7CE2:
    result = PspLockThreadSecurityExclusive(*(uint64_t *)(gs_base + (0 + 0x188)), v_stack_m68, (uint32_t)(v_stack_p38), Arg4);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A0)))) & (8)) != 0) goto loc_008B80D6;
loc_008B7CFC:
    if (v_stack_m98 == 0) goto loc_008B7F7A;
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x538) = local_rbx;
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x648) = v_stack_mA0;
    if (v_stack_m90 == 0) goto loc_008B7F69;
loc_008B7D32:
loc_008B7D3B:
    local_rbx = 0;
loc_008B7D3D:
    result = PspUnlockThreadSecurityExclusive(*(uint64_t *)(gs_base + (0 + 0x188)), v_stack_m68, (uint32_t)(v_stack_p38), Arg4);
    if (v_stack_m88 != 0) goto loc_008B80FA;
loc_008B7D56:
    if (sign_flag) goto loc_008B7E4C;
    if (v_stack_mB0 == 0) goto loc_008B7E4C;
    v_stack_m80 = v_stack_mA8;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_mB8 + 0x5A0)))) & (8)) == 0) goto loc_008B7E4C;
    v_stack_m68 = *(uint64_t *)(gs_base + (0 + 0x188));
    result = ObfReferenceObject(v_stack_mA8, v_stack_m68, (uint32_t)(v_stack_p38), Arg4);
    result = PspLockThreadSecurityExclusive(v_stack_mB8, *(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)(v_stack_p38), Arg4);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_mB8 + 0x5A0)))) & (8)) == 0) goto loc_008B8067;
    result = (*(uint64_t *)(v_stack_mB8 + 0x538)) & (-8);
    if (result != 0) goto loc_008B811E;
    if (((*(uint32_t *)(v_stack_mB8 + 0x5A0)) & (256)) == 0) goto loc_008B811E;
    Arg1 = (uint32_t)((*(uint64_t *)(v_stack_mB8 + 0x538)) & (7));
    Arg1 = (Arg1) | (v_stack_m80);
    *(uint64_t *)(v_stack_mB8 + 0x538) = Arg1;
    *(uint64_t *)(v_stack_mB8 + 0x648) = *(uint64_t *)(v_stack_m28 + 0x48);
loc_008B7E1D:
    result = PspUnlockThreadSecurityExclusive(v_stack_mB8, v_stack_m68, (uint32_t)(v_stack_p38), Arg4);
    if (sign_flag) goto loc_008B8128;
    result = ObfDereferenceObject(0, v_stack_m68, (uint32_t)(v_stack_p38), Arg4);
    if (*(uint64_t *)(v_stack_mB8 + 0x648) == 0) goto loc_008B7E4C;
loc_008B7E47:
    result = ObfDereferenceObject(*(uint64_t *)(v_stack_mB8 + 0x648), v_stack_m68, (uint32_t)(v_stack_p38), Arg4);
loc_008B7E4C:
    result = ObfDereferenceObjectWithTag(0, (uint32_t)(0x74726853ULL), (uint32_t)(v_stack_p38), Arg4);
    if (v_stack_mA8 != 0) {
        result = ObfDereferenceObject(v_stack_mA8, (uint32_t)(0x74726853ULL), (uint32_t)(v_stack_p38), Arg4);
    }
    result = ObfDereferenceObject(v_stack_mB8, (uint32_t)(0x74726853ULL), (uint32_t)(v_stack_p38), Arg4);
    if (sign_flag) goto loc_008B7E8A;
    *(uint64_t *)(Arg5) = v_stack_m70;
    goto loc_008B7E8A;
loc_008B7E8A:
    goto loc_008B7989;
loc_008B7E92:
    result = PspLockThreadSecurityShared(v_stack_mB8, *(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)(v_stack_p38), Arg4);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_mB8 + 0x5A0)))) & (8)) == 0) goto loc_008B8022;
    local_r15 = (*(uint64_t *)(v_stack_mB8 + 0x538)) & (-8);
    v_stack_mB0 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mB8 + 0x5A0)));
    result = ObfReferenceObjectWithTag(local_r15, (uint32_t)(0x74726853ULL), (uint32_t)(v_stack_p38), Arg4);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_mB8 + 0x538))) & (3));
    v_stack_m88 = (uint32_t)(result);
    result = (uint8_t)((*(uint8_t *)(v_stack_mB8 + 0x538)) >> (2));
    result = (uint8_t)((result) & (1));
    v_stack_mBD = (uint8_t)(result);
    result = (uint32_t)(((uint32_t)(v_stack_mB0)) >> (8));
    result = (uint8_t)((result) & (1));
    v_stack_mB0 = (uint32_t)(result);
loc_008B7F0A:
    result = PspUnlockThreadSecurityShared(v_stack_mB8, *(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)(v_stack_p38), Arg4);
    goto loc_008B7975;
loc_008B7F28:
    v_stack_mD0 = v_stack_m70;
    v_stack_mD8 = (uint8_t)((uint32_t)((uint32_t)(result)));
    v_stack_mE0 = *(uint64_t *)(v_rip + 0x7200DF);
    Arg3 = 0;
    result = ObOpenObjectByPointer(local_r15, (uint32_t)((uint32_t)(*(uint64_t *)(v_stack_mB8 + 0x648))), Arg3, (uint32_t)(v_stack_p38));
    goto loc_008B7C51;
loc_008B7F69:
    goto loc_008B7D32;
loc_008B7F7A:
    if (condition_is_above_or_equal) goto loc_008B7D3B;
    goto loc_008B7D3D;
loc_008B7F91:
    goto loc_008B7CE2;
loc_008B7F99:
    Arg2 = (*(uint8_t *)(result + 0x1) * 4 + 8 + 3) & ((uint32_t)(0xFFFFFFFCULL));
    result = ExAllocatePool2(256, Arg2, (uint32_t)(0x69536553ULL), (uint32_t)(v_stack_p38));
    if (result == 0) goto loc_008B80CB;
    result = *(uint8_t *)(v_stack_mA0 + 0x1) * 4 + 8;
    if (((uint32_t)(*(uint8_t *)(v_stack_mA0 + 0x1) * 4 + 8)) <= ((uint32_t)(*(uint8_t *)(result + 0x1) * 4 + 8))) {
        Arg3 = (uint32_t)(*(uint8_t *)(v_stack_mA0 + 0x1) * 4 + 8);
        Arg1 = result;
        result = memcpy(Arg1, v_stack_mA0, Arg3, (uint32_t)(v_stack_p38));
    }
    v_stack_m30 = result;
    goto loc_008B7C00;
loc_008B7FFB:
    if (*(uint64_t *)(v_stack_mB8 + 0x648) != 0) {
        Arg2 = *(uint64_t *)(*(uint64_t *)(v_stack_mB8 + 0x648) + 0x450);
        v_stack_mA0 = Arg2;
    }
    goto loc_008B7A8E;
loc_008B8022:
    goto loc_008B7F0A;
loc_008B802A:
    result = SeQueryTokenTrustLink(*(uint64_t *)(v_stack_mB8 + 0x648), Arg2, Arg3, (uint32_t)(v_stack_p38));
    result = ObfReferenceObject(result, Arg2, Arg3, (uint32_t)(v_stack_p38));
    v_stack_mA0 = *(uint64_t *)(v_stack_m28 + 0x48);
    goto loc_008B7CBC;
loc_008B8044:
    goto loc_008B7921;
loc_008B8051:
    v_stack_m98 = result;
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x648) = *(uint64_t *)(v_stack_m28 + 0x48);
    result = ObfDereferenceObject(result, Arg2, Arg3, (uint32_t)(v_stack_p38));
    goto loc_008B7A39;
loc_008B8067:
    goto loc_008B7E1D;
loc_008B8071:
    v_stack_m8C = (uint32_t)((uint32_t)(0xC000007CULL));
    v_stack_m90 = 0;
    v_stack_m98 = (uint32_t)(0xC000007CULL);
    v_stack_mBF = 0;
    goto loc_008B7A60;
loc_008B808B:
    result = ObfDereferenceObjectWithTag(result, (uint32_t)(0x746C6644ULL), Arg3, (uint32_t)(v_stack_p38));
    goto loc_008B7B11;
loc_008B809D:
    v_stack_m40 = (uint32_t)(0xC000007CULL);
    goto loc_008B7B94;
loc_008B80AA:
    result = ObfDereferenceObjectWithTag(*(uint64_t *)(v_stack_m28 + 0x48), (uint32_t)(0x74726853ULL), Arg3, (uint32_t)(v_stack_p38));
    result = ObfDereferenceObject(v_stack_mB8, (uint32_t)(0x74726853ULL), Arg3, (uint32_t)(v_stack_p38));
    goto loc_008B7989;
loc_008B80CB:
    goto loc_008B7C54;
loc_008B80D6:
    result = (*(uint64_t *)(*(uint64_t *)(v_stack_mB8 + 0x648) + 0x538)) & (-8);
    v_stack_m88 = result;
    v_stack_m80 = *(uint64_t *)(*(uint64_t *)(v_stack_mB8 + 0x648) + 0x648);
    goto loc_008B7CFC;
loc_008B80FA:
    result = ObfDereferenceObject(v_stack_mB8, (uint32_t)(0x74726853ULL), Arg3, (uint32_t)(v_stack_p38));
    result = ObfDereferenceObject(v_stack_m80, (uint32_t)(0x74726853ULL), Arg3, (uint32_t)(v_stack_p38));
loc_008B811E:
    goto loc_008B7E1D;
loc_008B8128:
    goto loc_008B7E47;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008B7840&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
