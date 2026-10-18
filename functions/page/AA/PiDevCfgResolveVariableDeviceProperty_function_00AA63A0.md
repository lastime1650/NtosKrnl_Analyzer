# PiDevCfgResolveVariableDeviceProperty

- RVA: `0x00AA63A0`–`0x00AA67D6` (길이 `1,078` bytes)
- VA: `0x0000000140AA63A0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A6A6C`
- 디코드: `304`개 명령, `1,078/1,078` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **19**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00AA6412` → [IopGetRegistryValue](../99/IopGetRegistryValue_function_009990EC.md) (function, `0x009990EC`)
- `0x00AA6428` → [PnpValidateRegistryString](../../text/4B/PnpValidateRegistryString_function_004B763C.md) (function, `0x004B763C`)
- `0x00AA6480` → [RtlGUIDFromString](../8F/RtlGUIDFromString_function_008F1EF0.md) (function, `0x008F1EF0`)
- `0x00AA6494` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AA64AE` → [IopGetRegistryValue](../99/IopGetRegistryValue_function_009990EC.md) (function, `0x009990EC`)
- `0x00AA64C6` → [PnpValidateRegistryDword](../../text/4D/PnpValidateRegistryDword_function_004D109C.md) (function, `0x004D109C`)
- `0x00AA6525` → [PnpGetObjectProperty](../8E/PnpGetObjectProperty_function_008E1110.md) (function, `0x008E1110`)
- `0x00AA6592` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AA65D0` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AA6637` → [RtlStringFromGUIDEx](../91/RtlStringFromGUIDEx_function_00915450.md) (function, `0x00915450`)
- `0x00AA6659` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AA6681` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AA66C9` → [PnpValidateMultiSzData](../../text/4B/PnpValidateMultiSzData_function_004BD294.md) (function, `0x004BD294`)
- `0x00AA6707` → [PnpValidateStringData](../../text/4B/PnpValidateStringData_function_004B7678.md) (function, `0x004B7678`)
- `0x00AA673F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AA6782` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x00AA6792` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AA67A7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AA67B5` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00AA63BC` → RVA `0x00E0A740` (`.data`; read)
- `0x00AA6400` → RVA `0x00AFF620` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AA64A4` → RVA `0x00AFF580` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **14**
  - `0x00AA6428` → [PnpValidateRegistryString](../../text/4B/PnpValidateRegistryString_function_004B763C.md) (`PAGE` → `.text`)
  - `0x00AA6494` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AA64C6` → [PnpValidateRegistryDword](../../text/4D/PnpValidateRegistryDword_function_004D109C.md) (`PAGE` → `.text`)
  - `0x00AA6592` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AA65D0` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AA6659` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AA6681` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AA66C9` → [PnpValidateMultiSzData](../../text/4B/PnpValidateMultiSzData_function_004BD294.md) (`PAGE` → `.text`)
  - `0x00AA6707` → [PnpValidateStringData](../../text/4B/PnpValidateStringData_function_004B7678.md) (`PAGE` → `.text`)
  - `0x00AA673F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AA6782` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x00AA6792` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AA67A7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AA67B5` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AA63A0  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00AA63A5  55                              push rbp
00AA63A6  56                              push rsi
00AA63A7  57                              push rdi
00AA63A8  41 54                           push r12
00AA63AA  41 55                           push r13
00AA63AC  41 56                           push r14
00AA63AE  41 57                           push r15
00AA63B0  48 8D 6C 24 D9                  lea rbp, [rsp - 0x27]
00AA63B5  48 81 EC C0 00 00 00            sub rsp, 0xc0
00AA63BC  48 8B 05 7D 43 36 00            mov rax, qword ptr [rip + 0x36437d]
00AA63C3  48 33 C4                        xor rax, rsp
00AA63C6  48 89 45 1F                     mov qword ptr [rbp + 0x1f], rax
00AA63CA  45 33 FF                        xor r15d, r15d
00AA63CD  4C 8D 4D D7                     lea r9, [rbp - 0x29]
00AA63D1  48 8B FA                        mov rdi, rdx
00AA63D4  4C 89 7D D7                     mov qword ptr [rbp - 0x29], r15
00AA63D8  4D 8B E8                        mov r13, r8
00AA63DB  44 89 7D FB                     mov dword ptr [rbp - 5], r15d
00AA63DF  48 8B F1                        mov rsi, rcx
00AA63E2  44 89 7D DF                     mov dword ptr [rbp - 0x21], r15d
00AA63E6  0F 57 C0                        xorps xmm0, xmm0
00AA63E9  44 89 7D C7                     mov dword ptr [rbp - 0x39], r15d
00AA63ED  33 C0                           xor eax, eax
00AA63EF  4C 89 7D CF                     mov qword ptr [rbp - 0x31], r15
00AA63F3  48 8B CF                        mov rcx, rdi
00AA63F6  89 45 17                        mov dword ptr [rbp + 0x17], eax
00AA63F9  45 33 C0                        xor r8d, r8d
00AA63FC  4C 89 7D E7                     mov qword ptr [rbp - 0x19], r15
00AA6400  48 8D 15 19 92 05 00            lea rdx, [rip + 0x59219]
00AA6407  4C 89 7D EF                     mov qword ptr [rbp - 0x11], r15
00AA640B  0F 11 45 07                     movups xmmword ptr [rbp + 7], xmm0
00AA640F  45 8B E7                        mov r12d, r15d
00AA6412  E8 D5 2C EF FF                  call 0x1409990ec
00AA6417  8B D8                           mov ebx, eax
00AA6419  85 C0                           test eax, eax
00AA641B  0F 88 78 03 00 00               js 0x140aa6799
00AA6421  4C 8B 7D D7                     mov r15, qword ptr [rbp - 0x29]
00AA6425  49 8B CF                        mov rcx, r15
00AA6428  E8 0F 12 A1 FF                  call 0x1404b763c
00AA642D  33 DB                           xor ebx, ebx
00AA642F  84 C0                           test al, al
00AA6431  75 0A                           jne 0x140aa643d
00AA6433  BB 01 00 00 C0                  mov ebx, 0xc0000001
00AA6438  E9 60 03 00 00                  jmp 0x140aa679d
00AA643D  41 8B 57 08                     mov edx, dword ptr [r15 + 8]
00AA6441  41 8B 47 0C                     mov eax, dword ptr [r15 + 0xc]
00AA6445  49 03 D7                        add rdx, r15
00AA6448  48 D1 E8                        shr rax, 1
00AA644B  48 8B CA                        mov rcx, rdx
00AA644E  4C 8D 04 42                     lea r8, [rdx + rax*2]
00AA6452  49 3B D0                        cmp rdx, r8
00AA6455  73 0E                           jae 0x140aa6465
00AA6457  66 39 19                        cmp word ptr [rcx], bx
00AA645A  74 09                           je 0x140aa6465
00AA645C  48 83 C1 02                     add rcx, 2
00AA6460  49 3B C8                        cmp rcx, r8
00AA6463  72 F2                           jb 0x140aa6457
00AA6465  41 0F B7 47 0C                  movzx eax, word ptr [r15 + 0xc]
00AA646A  2B CA                           sub ecx, edx
00AA646C  66 89 4D F7                     mov word ptr [rbp - 9], cx
00AA6470  48 8D 4D F7                     lea rcx, [rbp - 9]
00AA6474  48 89 55 FF                     mov qword ptr [rbp - 1], rdx
00AA6478  48 8D 55 07                     lea rdx, [rbp + 7]
00AA647C  66 89 45 F9                     mov word ptr [rbp - 7], ax
00AA6480  E8 6B BA E4 FF                  call 0x1408f1ef0
00AA6485  8B D8                           mov ebx, eax
00AA6487  85 C0                           test eax, eax
00AA6489  0F 88 0E 03 00 00               js 0x140aa679d
00AA648F  33 D2                           xor edx, edx
00AA6491  49 8B CF                        mov rcx, r15
00AA6494  E8 D7 C3 0D 00                  call 0x140b82870
00AA6499  4C 21 65 D7                     and qword ptr [rbp - 0x29], r12
00AA649D  4C 8D 4D D7                     lea r9, [rbp - 0x29]
00AA64A1  45 33 C0                        xor r8d, r8d
00AA64A4  48 8D 15 D5 90 05 00            lea rdx, [rip + 0x590d5]
00AA64AB  48 8B CF                        mov rcx, rdi
00AA64AE  E8 39 2C EF FF                  call 0x1409990ec
00AA64B3  33 FF                           xor edi, edi
00AA64B5  8B D8                           mov ebx, eax
00AA64B7  85 C0                           test eax, eax
00AA64B9  0F 88 DA 02 00 00               js 0x140aa6799
00AA64BF  4C 8B 7D D7                     mov r15, qword ptr [rbp - 0x29]
00AA64C3  49 8B CF                        mov rcx, r15
00AA64C6  E8 D1 AB A2 FF                  call 0x1404d109c
00AA64CB  84 C0                           test al, al
00AA64CD  0F 84 60 FF FF FF               je 0x140aa6433
00AA64D3  41 8B 47 08                     mov eax, dword ptr [r15 + 8]
00AA64D7  44 8D 77 01                     lea r14d, [rdi + 1]
00AA64DB  4C 8B 06                        mov r8, qword ptr [rsi]
00AA64DE  45 8B CE                        mov r9d, r14d
00AA64E1  89 7C 24 50                     mov dword ptr [rsp + 0x50], edi
00AA64E5  33 D2                           xor edx, edx
00AA64E7  42 8B 0C 38                     mov ecx, dword ptr [rax + r15]
00AA64EB  48 8D 45 C7                     lea rax, [rbp - 0x39]
00AA64EF  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00AA64F4  48 8D 45 CF                     lea rax, [rbp - 0x31]
00AA64F8  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00AA64FD  48 8D 45 DF                     lea rax, [rbp - 0x21]
00AA6501  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00AA6506  48 8D 45 07                     lea rax, [rbp + 7]
00AA650A  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AA650F  89 4D 17                        mov dword ptr [rbp + 0x17], ecx
00AA6512  B9 50 6E 70 47                  mov ecx, 0x47706e50
00AA6517  4D 8B 40 30                     mov r8, qword ptr [r8 + 0x30]
00AA651B  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
00AA6520  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00AA6525  E8 E6 AB E3 FF                  call 0x1408e1110
00AA652A  33 C9                           xor ecx, ecx
00AA652C  8B D8                           mov ebx, eax
00AA652E  85 C0                           test eax, eax
00AA6530  0F 88 2A 02 00 00               js 0x140aa6760
00AA6536  8B 45 DF                        mov eax, dword ptr [rbp - 0x21]
00AA6539  83 F8 0D                        cmp eax, 0xd
00AA653C  0F 87 49 01 00 00               ja 0x140aa668b
00AA6542  0F 84 DE 00 00 00               je 0x140aa6626
00AA6548  83 F8 05                        cmp eax, 5
00AA654B  0F 87 A2 00 00 00               ja 0x140aa65f3
00AA6551  74 24                           je 0x140aa6577
00AA6553  85 C0                           test eax, eax
00AA6555  0F 84 0E 02 00 00               je 0x140aa6769
00AA655B  41 2B C6                        sub eax, r14d
00AA655E  0F 84 05 02 00 00               je 0x140aa6769
00AA6564  41 2B C6                        sub eax, r14d
00AA6567  74 42                           je 0x140aa65ab
00AA6569  41 2B C6                        sub eax, r14d
00AA656C  74 3D                           je 0x140aa65ab
00AA656E  41 3B C6                        cmp eax, r14d
00AA6571  0F 85 67 01 00 00               jne 0x140aa66de
00AA6577  83 7D C7 02                     cmp dword ptr [rbp - 0x39], 2
00AA657B  75 34                           jne 0x140aa65b1
00AA657D  BA 04 00 00 00                  mov edx, 4
00AA6582  B9 00 01 00 00                  mov ecx, 0x100
00AA6587  41 B8 50 70 64 63               mov r8d, 0x63647050
00AA658D  44 8B F2                        mov r14d, edx
00AA6590  8B F2                           mov esi, edx
00AA6592  E8 59 BB 0D 00                  call 0x140b820f0
00AA6597  48 8B F8                        mov rdi, rax
00AA659A  48 85 C0                        test rax, rax
00AA659D  74 3E                           je 0x140aa65dd
00AA659F  48 8B 45 CF                     mov rax, qword ptr [rbp - 0x31]
00AA65A3  0F B7 08                        movzx ecx, word ptr [rax]
00AA65A6  E9 B1 01 00 00                  jmp 0x140aa675c
00AA65AB  44 39 75 C7                     cmp dword ptr [rbp - 0x39], r14d
00AA65AF  74 0A                           je 0x140aa65bb
00AA65B1  BB 01 00 00 C0                  mov ebx, 0xc0000001
00AA65B6  E9 CC 01 00 00                  jmp 0x140aa6787
00AA65BB  BA 04 00 00 00                  mov edx, 4
00AA65C0  B9 00 01 00 00                  mov ecx, 0x100
00AA65C5  41 B8 50 70 64 63               mov r8d, 0x63647050
00AA65CB  44 8B F2                        mov r14d, edx
00AA65CE  8B F2                           mov esi, edx
00AA65D0  E8 1B BB 0D 00                  call 0x140b820f0
00AA65D5  48 8B F8                        mov rdi, rax
00AA65D8  48 85 C0                        test rax, rax
00AA65DB  75 0A                           jne 0x140aa65e7
00AA65DD  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00AA65E2  E9 A0 01 00 00                  jmp 0x140aa6787
00AA65E7  48 8B 45 CF                     mov rax, qword ptr [rbp - 0x31]
00AA65EB  0F B6 08                        movzx ecx, byte ptr [rax]
00AA65EE  E9 69 01 00 00                  jmp 0x140aa675c
00AA65F3  83 E8 06                        sub eax, 6
00AA65F6  0F 84 ED 00 00 00               je 0x140aa66e9
00AA65FC  41 2B C6                        sub eax, r14d
00AA65FF  0F 84 E4 00 00 00               je 0x140aa66e9
00AA6605  41 2B C6                        sub eax, r14d
00AA6608  74 09                           je 0x140aa6613
00AA660A  41 3B C6                        cmp eax, r14d
00AA660D  0F 85 CB 00 00 00               jne 0x140aa66de
00AA6613  BE 08 00 00 00                  mov esi, 8
00AA6618  39 75 C7                        cmp dword ptr [rbp - 0x39], esi
00AA661B  75 94                           jne 0x140aa65b1
00AA661D  44 8D 76 03                     lea r14d, [rsi + 3]
00AA6621  E9 F0 00 00 00                  jmp 0x140aa6716
00AA6626  83 7D C7 10                     cmp dword ptr [rbp - 0x39], 0x10
00AA662A  75 85                           jne 0x140aa65b1
00AA662C  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
00AA6630  48 8D 55 E7                     lea rdx, [rbp - 0x19]
00AA6634  45 8A C6                        mov r8b, r14b
00AA6637  E8 14 EE E6 FF                  call 0x140915450
00AA663C  8B D8                           mov ebx, eax
00AA663E  85 C0                           test eax, eax
00AA6640  78 29                           js 0x140aa666b
00AA6642  0F B7 75 E7                     movzx esi, word ptr [rbp - 0x19]
00AA6646  41 B8 50 70 64 63               mov r8d, 0x63647050
00AA664C  83 C6 02                        add esi, 2
00AA664F  B9 00 01 00 00                  mov ecx, 0x100
00AA6654  8B D6                           mov edx, esi
00AA6656  44 8B E6                        mov r12d, esi
00AA6659  E8 92 BA 0D 00                  call 0x140b820f0
00AA665E  48 8B F8                        mov rdi, rax
00AA6661  48 85 C0                        test rax, rax
00AA6664  75 0E                           jne 0x140aa6674
00AA6666  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00AA666B  4C 8B 65 EF                     mov r12, qword ptr [rbp - 0x11]
00AA666F  E9 06 01 00 00                  jmp 0x140aa677a
00AA6674  4D 8B C4                        mov r8, r12
00AA6677  48 8B C8                        mov rcx, rax
00AA667A  4C 8B 65 EF                     mov r12, qword ptr [rbp - 0x11]
00AA667E  49 8B D4                        mov rdx, r12
00AA6681  E8 BA 01 C2 FF                  call 0x1406c6840
00AA6686  E9 E3 00 00 00                  jmp 0x140aa676e
00AA668B  83 E8 11                        sub eax, 0x11
00AA668E  0F 84 8C 00 00 00               je 0x140aa6720
00AA6694  41 2B C6                        sub eax, r14d
00AA6697  74 65                           je 0x140aa66fe
00AA6699  83 E8 02                        sub eax, 2
00AA669C  74 60                           je 0x140aa66fe
00AA669E  83 E8 02                        sub eax, 2
00AA66A1  74 46                           je 0x140aa66e9
00AA66A3  41 2B C6                        sub eax, r14d
00AA66A6  74 41                           je 0x140aa66e9
00AA66A8  41 2B C6                        sub eax, r14d
00AA66AB  74 3C                           je 0x140aa66e9
00AA66AD  41 2B C6                        sub eax, r14d
00AA66B0  74 4C                           je 0x140aa66fe
00AA66B2  2D EA 0F 00 00                  sub eax, 0xfea
00AA66B7  74 25                           je 0x140aa66de
00AA66B9  3D 0F 10 00 00                  cmp eax, 0x100f
00AA66BE  75 1E                           jne 0x140aa66de
00AA66C0  8B 75 C7                        mov esi, dword ptr [rbp - 0x39]
00AA66C3  8B D6                           mov edx, esi
00AA66C5  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
00AA66C9  E8 C6 6B A1 FF                  call 0x1404bd294
00AA66CE  33 C9                           xor ecx, ecx
00AA66D0  84 C0                           test al, al
00AA66D2  0F 84 D9 FE FF FF               je 0x140aa65b1
00AA66D8  44 8D 71 07                     lea r14d, [rcx + 7]
00AA66DC  EB 38                           jmp 0x140aa6716
00AA66DE  8B 75 C7                        mov esi, dword ptr [rbp - 0x39]
00AA66E1  41 BE 03 00 00 00               mov r14d, 3
00AA66E7  EB 2D                           jmp 0x140aa6716
00AA66E9  BA 04 00 00 00                  mov edx, 4
00AA66EE  39 55 C7                        cmp dword ptr [rbp - 0x39], edx
00AA66F1  0F 85 BA FE FF FF               jne 0x140aa65b1
00AA66F7  44 8B F2                        mov r14d, edx
00AA66FA  8B F2                           mov esi, edx
00AA66FC  EB 18                           jmp 0x140aa6716
00AA66FE  8B 75 C7                        mov esi, dword ptr [rbp - 0x39]
00AA6701  8B D6                           mov edx, esi
00AA6703  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
00AA6707  E8 6C 0F A1 FF                  call 0x1404b7678
00AA670C  33 C9                           xor ecx, ecx
00AA670E  84 C0                           test al, al
00AA6710  0F 84 9B FE FF FF               je 0x140aa65b1
00AA6716  48 8B 7D CF                     mov rdi, qword ptr [rbp - 0x31]
00AA671A  48 89 4D CF                     mov qword ptr [rbp - 0x31], rcx
00AA671E  EB 4E                           jmp 0x140aa676e
00AA6720  44 39 75 C7                     cmp dword ptr [rbp - 0x39], r14d
00AA6724  0F 85 87 FE FF FF               jne 0x140aa65b1
00AA672A  BA 04 00 00 00                  mov edx, 4
00AA672F  B9 00 01 00 00                  mov ecx, 0x100
00AA6734  41 B8 50 70 64 63               mov r8d, 0x63647050
00AA673A  44 8B F2                        mov r14d, edx
00AA673D  8B F2                           mov esi, edx
00AA673F  E8 AC B9 0D 00                  call 0x140b820f0
00AA6744  33 C9                           xor ecx, ecx
00AA6746  48 8B F8                        mov rdi, rax
00AA6749  48 85 C0                        test rax, rax
00AA674C  0F 84 8B FE FF FF               je 0x140aa65dd
00AA6752  48 8B 45 CF                     mov rax, qword ptr [rbp - 0x31]
00AA6756  80 38 FF                        cmp byte ptr [rax], 0xff
00AA6759  0F 94 C1                        sete cl
00AA675C  89 0F                           mov dword ptr [rdi], ecx
00AA675E  EB 0E                           jmp 0x140aa676e
00AA6760  3D 25 02 00 C0                  cmp eax, 0xc0000225
00AA6765  75 20                           jne 0x140aa6787
00AA6767  8B D9                           mov ebx, ecx
00AA6769  8B F1                           mov esi, ecx
00AA676B  44 8B F1                        mov r14d, ecx
00AA676E  45 89 75 20                     mov dword ptr [r13 + 0x20], r14d
00AA6772  41 89 75 24                     mov dword ptr [r13 + 0x24], esi
00AA6776  49 89 7D 28                     mov qword ptr [r13 + 0x28], rdi
00AA677A  4D 85 E4                        test r12, r12
00AA677D  74 08                           je 0x140aa6787
00AA677F  49 8B CC                        mov rcx, r12
00AA6782  E8 C9 C0 0D 00                  call 0x140b82850
00AA6787  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
00AA678B  48 85 C9                        test rcx, rcx
00AA678E  74 0D                           je 0x140aa679d
00AA6790  33 D2                           xor edx, edx
00AA6792  E8 D9 C0 0D 00                  call 0x140b82870
00AA6797  EB 04                           jmp 0x140aa679d
00AA6799  4C 8B 7D D7                     mov r15, qword ptr [rbp - 0x29]
00AA679D  4D 85 FF                        test r15, r15
00AA67A0  74 0A                           je 0x140aa67ac
00AA67A2  33 D2                           xor edx, edx
00AA67A4  49 8B CF                        mov rcx, r15
00AA67A7  E8 C4 C0 0D 00                  call 0x140b82870
00AA67AC  8B C3                           mov eax, ebx
00AA67AE  48 8B 4D 1F                     mov rcx, qword ptr [rbp + 0x1f]
00AA67B2  48 33 CC                        xor rcx, rsp
00AA67B5  E8 86 5E C0 FF                  call 0x1406ac640
00AA67BA  48 8B 9C 24 18 01 00 00         mov rbx, qword ptr [rsp + 0x118]
00AA67C2  48 81 C4 C0 00 00 00            add rsp, 0xc0
00AA67C9  41 5F                           pop r15
00AA67CB  41 5E                           pop r14
00AA67CD  41 5D                           pop r13
00AA67CF  41 5C                           pop r12
00AA67D1  5F                              pop rdi
00AA67D2  5E                              pop rsi
00AA67D3  5D                              pop rbp
00AA67D4  C3                              ret
00AA67D5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiDevCfgResolveVariableDeviceProperty(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m64;
    unsigned __int16 v_stack_m66;
    unsigned __int16 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m98;
    unsigned int v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_p20;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (192);
    result = (*(unsigned __int64 *)(v_rip + 3556221)) ^ (v_rsp);
    v_stack_m40 = result;
    v_r15 = 0;
    v_stack_m88 = 0;
    v_stack_m64 = 0;
    v_stack_m80 = 0;
    v_stack_m98 = 0;
    result = 0;
    v_stack_m90 = 0;
    v_stack_m48 = 0;
    a3 = 0;
    v_stack_m78 = 0;
    v_stack_m70 = 0;
    v_stack_m58 = v_xmm0;
    result = IopGetRegistryValue(a2, v_rip + 365081, a3, v_stack_m88);
    if (sign_flag) goto loc_00AA6799;
    result = PnpValidateRegistryString(v_stack_m88, v_rip + 365081, a3, v_stack_m88);
    v_rbx = 0;
    if ((unsigned __int8)(result) != 0) goto loc_00AA643D;
loc_00AA6433:
    goto loc_00AA679D;
loc_00AA643D:
    a2 = ((unsigned int)(*(unsigned int *)(v_stack_m88 + 8))) + (v_stack_m88);
    result = ((unsigned int)(*(unsigned int *)(v_stack_m88 + 12))) >> (1);
    if (a2 >= (a2 + result * 2)) goto loc_00AA6465;
loc_00AA6457:
    if ((*(unsigned __int16 *)(a2)) == ((unsigned __int16)((unsigned int)(0xC0000001ULL)))) goto loc_00AA6465;
    a1 = (a2) + (2);
    if (a1 < (a2 + result * 2)) goto loc_00AA6457;
loc_00AA6465:
    a1 = (unsigned int)((a1) - ((unsigned int)(a2)));
    v_stack_m68 = (unsigned __int16)(a1);
    v_stack_m60 = a2;
    v_stack_m66 = (unsigned __int16)(*(unsigned __int16 *)(v_stack_m88 + 12));
    result = RtlGUIDFromString(v_stack_m68, v_stack_m58, a2 + result * 2, v_stack_m88);
    if (sign_flag) goto loc_00AA679D;
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m88, a2, a2 + result * 2, v_stack_m88);
    a3 = 0;
    result = IopGetRegistryValue(0, v_rip + 364757, a3, v_stack_m88);
    v_rdi = 0;
    if (sign_flag) goto loc_00AA6799;
    result = PnpValidateRegistryDword(v_stack_m88, v_rip + 364757, a3, v_stack_m88);
    if ((unsigned __int8)(result) == 0) goto loc_00AA6433;
    v_stack_mA8 = 0;
    a2 = 0;
    v_stack_mB0 = v_stack_m98;
    v_stack_mB8 = v_stack_m90;
    v_stack_mC0 = v_stack_m80;
    v_stack_mC8 = v_stack_m58;
    v_stack_m48 = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_stack_m88 + 8)) + v_stack_m88 * 1)));
    v_stack_mD0 = 0;
    v_stack_mD8 = 0;
    result = PnpGetObjectProperty((unsigned int)(0x47706E50ULL), a2, *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 48), (unsigned int)((unsigned int)(v_rdi + 1)));
    a1 = 0;
    if (sign_flag) goto loc_00AA6760;
    if (((unsigned int)((unsigned int)(v_stack_m80))) > 13) goto loc_00AA668B;
    if (((unsigned int)((unsigned int)(v_stack_m80))) == 13) goto loc_00AA6626;
    if (((unsigned int)((unsigned int)(v_stack_m80))) > 5) goto loc_00AA65F3;
    if (((unsigned int)((unsigned int)(v_stack_m80))) == 5) goto loc_00AA6577;
    if ((unsigned int)((unsigned int)(v_stack_m80)) == 0) goto loc_00AA6769;
    result = (unsigned int)(((unsigned int)(v_stack_m80)) - ((unsigned int)(v_rdi + 1)));
    if (condition_is_equal) goto loc_00AA6769;
    result = (unsigned int)((result) - ((unsigned int)(v_rdi + 1)));
    if (condition_is_equal) goto loc_00AA65AB;
    result = (unsigned int)((result) - ((unsigned int)(v_rdi + 1)));
    if (condition_is_equal) goto loc_00AA65AB;
    if (((unsigned int)(result)) != ((unsigned int)(v_rdi + 1))) goto loc_00AA66DE;
loc_00AA6577:
    if (v_stack_m98 != 2) goto loc_00AA65B1;
    result = ExAllocatePool2(256, 4, (unsigned int)(0x63647050ULL), (unsigned int)((unsigned int)(v_rdi + 1)));
    if (result == 0) goto loc_00AA65DD;
    goto loc_00AA675C;
loc_00AA65AB:
    if (v_stack_m98 == 4) goto loc_00AA65BB;
loc_00AA65B1:
    goto loc_00AA6787;
loc_00AA65BB:
    result = ExAllocatePool2(256, 4, (unsigned int)(0x63647050ULL), (unsigned int)((unsigned int)(v_rdi + 1)));
    if (result != 0) goto loc_00AA65E7;
loc_00AA65DD:
    goto loc_00AA6787;
loc_00AA65E7:
    goto loc_00AA675C;
loc_00AA65F3:
    result = (unsigned int)((v_stack_m90) - (6));
    if (condition_is_equal) goto loc_00AA66E9;
    result = (unsigned int)((result) - (4));
    if (condition_is_equal) goto loc_00AA66E9;
    result = (unsigned int)((result) - (4));
    if (condition_is_equal) goto loc_00AA6613;
    if (((unsigned int)(result)) != 4) goto loc_00AA66DE;
loc_00AA6613:
    if (v_stack_m98 != 8) goto loc_00AA65B1;
    goto loc_00AA6716;
loc_00AA6626:
    if (v_stack_m98 != 16) goto loc_00AA65B1;
    result = RtlStringFromGUIDEx(v_stack_m90, v_stack_m78, (unsigned __int8)(8 + 3), (unsigned int)((unsigned int)(v_rdi + 1)));
    if (sign_flag) goto loc_00AA666B;
    v_rsi = (unsigned int)((v_stack_m78) + (2));
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(v_rsi)), (unsigned int)(0x63647050ULL), (unsigned int)((unsigned int)(v_rdi + 1)));
    if (result != 0) goto loc_00AA6674;
loc_00AA666B:
    goto loc_00AA677A;
loc_00AA6674:
    result = memcpy(result, v_stack_m70, v_stack_m70, (unsigned int)((unsigned int)(v_rdi + 1)));
    goto loc_00AA676E;
loc_00AA668B:
    result = (unsigned int)((result) - (17));
    if (condition_is_equal) goto loc_00AA6720;
    result = (unsigned int)((result) - ((unsigned int)(8 + 3)));
    if (condition_is_equal) goto loc_00AA66FE;
    result = (unsigned int)((result) - (2));
    if (condition_is_equal) goto loc_00AA66FE;
    result = (unsigned int)((result) - (2));
    if (condition_is_equal) goto loc_00AA66E9;
    result = (unsigned int)((result) - ((unsigned int)(8 + 3)));
    if (condition_is_equal) goto loc_00AA66E9;
    result = (unsigned int)((result) - ((unsigned int)(8 + 3)));
    if (condition_is_equal) goto loc_00AA66E9;
    result = (unsigned int)((result) - ((unsigned int)(8 + 3)));
    if (condition_is_equal) goto loc_00AA66FE;
    result = (unsigned int)((result) - (0xFEAULL));
    if (condition_is_equal) goto loc_00AA66DE;
    if (((unsigned int)(result)) != 0x100FULL) goto loc_00AA66DE;
    result = PnpValidateMultiSzData(v_stack_m90, (unsigned int)((unsigned int)((unsigned int)(v_stack_m98))), v_stack_m70, (unsigned int)((unsigned int)(v_rdi + 1)));
    a1 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_00AA65B1;
    goto loc_00AA6716;
loc_00AA66DE:
    goto loc_00AA6716;
loc_00AA66E9:
    if (v_stack_m98 != 4) goto loc_00AA65B1;
    goto loc_00AA6716;
loc_00AA66FE:
    result = PnpValidateStringData(v_stack_m90, (unsigned int)((unsigned int)((unsigned int)(v_stack_m98))), v_stack_m70, (unsigned int)((unsigned int)(v_rdi + 1)));
    a1 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_00AA65B1;
loc_00AA6716:
    v_stack_m90 = 0;
    goto loc_00AA676E;
loc_00AA6720:
    if (v_stack_m98 != 4) goto loc_00AA65B1;
    result = ExAllocatePool2(256, 4, (unsigned int)(0x63647050ULL), (unsigned int)((unsigned int)(v_rdi + 1)));
    a1 = 0;
    if (result == 0) goto loc_00AA65DD;
    a1 = ((*(unsigned __int8 *)(v_stack_m90)) == 255) ? 1 : 0;
loc_00AA675C:
    *(unsigned int *)(result) = (unsigned int)(a1);
    goto loc_00AA676E;
loc_00AA6760:
    if (((unsigned int)(v_stack_m90)) != 0xC0000225ULL) goto loc_00AA6787;
loc_00AA6769:
loc_00AA676E:
    *(unsigned int *)(a3 + 32) = (unsigned int)((unsigned int)((unsigned int)(a1)));
    *(unsigned int *)(a3 + 36) = (unsigned int)((unsigned int)((unsigned int)(a1)));
    *(unsigned __int64 *)(a3 + 40) = result;
loc_00AA677A:
    result = v_stack_m90;
    if (v_stack_m70 != 0) {
        a1 = v_stack_m70;
        result = ExFreePool(a1, 4, (unsigned int)(0x63647050ULL), (unsigned int)((unsigned int)(v_rdi + 1)));
    }
    if (v_stack_m90 == 0) goto loc_00AA679D;
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m90, a2, (unsigned int)(0x63647050ULL), (unsigned int)((unsigned int)(v_rdi + 1)));
    goto loc_00AA679D;
loc_00AA6799:
loc_00AA679D:
    if (v_stack_m88 != 0) {
        a2 = 0;
        a1 = v_stack_m88;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(0x63647050ULL), (unsigned int)((unsigned int)(v_rdi + 1)));
    }
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, (unsigned int)(0x63647050ULL), (unsigned int)((unsigned int)(v_rdi + 1)));
    v_rsp = (v_rsp) + (192);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PiDevCfgResolveVariableDeviceProperty(void *Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint32_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m60;
    uint32_t v_stack_m64;
    uint16_t v_stack_m66;
    uint16_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint32_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint32_t v_stack_m98;
    uint32_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_p20;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (192);
    result = (*(uint64_t *)(v_rip + 0x36437D)) ^ (local_rsp);
    v_stack_m40 = result;
    local_r15 = 0;
    v_stack_m88 = 0;
    v_stack_m64 = 0;
    v_stack_m80 = 0;
    v_stack_m98 = 0;
    result = 0;
    v_stack_m90 = 0;
    v_stack_m48 = 0;
    Arg3 = 0;
    v_stack_m78 = 0;
    v_stack_m70 = 0;
    v_stack_m58 = v_xmm0;
    result = IopGetRegistryValue(Arg2, v_rip + 365081, Arg3, v_stack_m88);
    if (sign_flag) goto loc_00AA6799;
    result = PnpValidateRegistryString(v_stack_m88, v_rip + 365081, Arg3, v_stack_m88);
    local_rbx = 0;
    if ((uint8_t)(result) != 0) goto loc_00AA643D;
loc_00AA6433:
    goto loc_00AA679D;
loc_00AA643D:
    Arg2 = ((uint32_t)(*(uint32_t *)(v_stack_m88 + 0x8))) + (v_stack_m88);
    result = ((uint32_t)(*(uint32_t *)(v_stack_m88 + 0xC))) >> (1);
    if (Arg2 >= (Arg2 + result * 2)) goto loc_00AA6465;
loc_00AA6457:
    if ((*(uint16_t *)(Arg2)) == ((uint16_t)((uint32_t)(0xC0000001ULL)))) goto loc_00AA6465;
    Arg1 = (Arg2) + (2);
    if (Arg1 < (Arg2 + result * 2)) goto loc_00AA6457;
loc_00AA6465:
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(Arg2)));
    v_stack_m68 = (uint16_t)(Arg1);
    v_stack_m60 = Arg2;
    v_stack_m66 = (uint16_t)(*(uint16_t *)(v_stack_m88 + 0xC));
    result = RtlGUIDFromString(v_stack_m68, v_stack_m58, Arg2 + result * 2, v_stack_m88);
    if (sign_flag) goto loc_00AA679D;
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m88, Arg2, Arg2 + result * 2, v_stack_m88);
    Arg3 = 0;
    result = IopGetRegistryValue(0, v_rip + 364757, Arg3, v_stack_m88);
    local_rdi = 0;
    if (sign_flag) goto loc_00AA6799;
    result = PnpValidateRegistryDword(v_stack_m88, v_rip + 364757, Arg3, v_stack_m88);
    if ((uint8_t)(result) == 0) goto loc_00AA6433;
    v_stack_mA8 = 0;
    Arg2 = 0;
    v_stack_mB0 = v_stack_m98;
    v_stack_mB8 = v_stack_m90;
    v_stack_mC0 = v_stack_m80;
    v_stack_mC8 = v_stack_m58;
    v_stack_m48 = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(v_stack_m88 + 0x8)) + v_stack_m88 * 1)));
    v_stack_mD0 = 0;
    v_stack_mD8 = 0;
    result = PnpGetObjectProperty((uint32_t)(0x47706E50ULL), Arg2, *(uint64_t *)(*(uint64_t *)(arg1) + 0x30), (uint32_t)((uint32_t)(local_rdi + 1)));
    Arg1 = 0;
    if (sign_flag) goto loc_00AA6760;
    if (((uint32_t)((uint32_t)(v_stack_m80))) > 13) goto loc_00AA668B;
    if (((uint32_t)((uint32_t)(v_stack_m80))) == 13) goto loc_00AA6626;
    if (((uint32_t)((uint32_t)(v_stack_m80))) > 5) goto loc_00AA65F3;
    if (((uint32_t)((uint32_t)(v_stack_m80))) == 5) goto loc_00AA6577;
    if ((uint32_t)((uint32_t)(v_stack_m80)) == 0) goto loc_00AA6769;
    result = (uint32_t)(((uint32_t)(v_stack_m80)) - ((uint32_t)(local_rdi + 1)));
    if (condition_is_equal) goto loc_00AA6769;
    result = (uint32_t)((result) - ((uint32_t)(local_rdi + 1)));
    if (condition_is_equal) goto loc_00AA65AB;
    result = (uint32_t)((result) - ((uint32_t)(local_rdi + 1)));
    if (condition_is_equal) goto loc_00AA65AB;
    if (((uint32_t)(result)) != ((uint32_t)(local_rdi + 1))) goto loc_00AA66DE;
loc_00AA6577:
    if (v_stack_m98 != 2) goto loc_00AA65B1;
    result = ExAllocatePool2(256, 4, (uint32_t)(0x63647050ULL), (uint32_t)((uint32_t)(local_rdi + 1)));
    if (result == 0) goto loc_00AA65DD;
    goto loc_00AA675C;
loc_00AA65AB:
    if (v_stack_m98 == 4) goto loc_00AA65BB;
loc_00AA65B1:
    goto loc_00AA6787;
loc_00AA65BB:
    result = ExAllocatePool2(256, 4, (uint32_t)(0x63647050ULL), (uint32_t)((uint32_t)(local_rdi + 1)));
    if (result != 0) goto loc_00AA65E7;
loc_00AA65DD:
    goto loc_00AA6787;
loc_00AA65E7:
    goto loc_00AA675C;
loc_00AA65F3:
    result = (uint32_t)((v_stack_m90) - (6));
    if (condition_is_equal) goto loc_00AA66E9;
    result = (uint32_t)((result) - (4));
    if (condition_is_equal) goto loc_00AA66E9;
    result = (uint32_t)((result) - (4));
    if (condition_is_equal) goto loc_00AA6613;
    if (((uint32_t)(result)) != 4) goto loc_00AA66DE;
loc_00AA6613:
    if (v_stack_m98 != 8) goto loc_00AA65B1;
    goto loc_00AA6716;
loc_00AA6626:
    if (v_stack_m98 != 16) goto loc_00AA65B1;
    result = RtlStringFromGUIDEx(v_stack_m90, v_stack_m78, (uint8_t)(8 + 3), (uint32_t)((uint32_t)(local_rdi + 1)));
    if (sign_flag) goto loc_00AA666B;
    local_rsi = (uint32_t)((v_stack_m78) + (2));
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(local_rsi)), (uint32_t)(0x63647050ULL), (uint32_t)((uint32_t)(local_rdi + 1)));
    if (result != 0) goto loc_00AA6674;
loc_00AA666B:
    goto loc_00AA677A;
loc_00AA6674:
    result = memcpy(result, v_stack_m70, v_stack_m70, (uint32_t)((uint32_t)(local_rdi + 1)));
    goto loc_00AA676E;
loc_00AA668B:
    result = (uint32_t)((result) - (17));
    if (condition_is_equal) goto loc_00AA6720;
    result = (uint32_t)((result) - ((uint32_t)(8 + 3)));
    if (condition_is_equal) goto loc_00AA66FE;
    result = (uint32_t)((result) - (2));
    if (condition_is_equal) goto loc_00AA66FE;
    result = (uint32_t)((result) - (2));
    if (condition_is_equal) goto loc_00AA66E9;
    result = (uint32_t)((result) - ((uint32_t)(8 + 3)));
    if (condition_is_equal) goto loc_00AA66E9;
    result = (uint32_t)((result) - ((uint32_t)(8 + 3)));
    if (condition_is_equal) goto loc_00AA66E9;
    result = (uint32_t)((result) - ((uint32_t)(8 + 3)));
    if (condition_is_equal) goto loc_00AA66FE;
    result = (uint32_t)((result) - (0xFEAULL));
    if (condition_is_equal) goto loc_00AA66DE;
    if (((uint32_t)(result)) != 0x100FULL) goto loc_00AA66DE;
    result = PnpValidateMultiSzData(v_stack_m90, (uint32_t)((uint32_t)((uint32_t)(v_stack_m98))), v_stack_m70, (uint32_t)((uint32_t)(local_rdi + 1)));
    Arg1 = 0;
    if ((uint8_t)(result) == 0) goto loc_00AA65B1;
    goto loc_00AA6716;
loc_00AA66DE:
    goto loc_00AA6716;
loc_00AA66E9:
    if (v_stack_m98 != 4) goto loc_00AA65B1;
    goto loc_00AA6716;
loc_00AA66FE:
    result = PnpValidateStringData(v_stack_m90, (uint32_t)((uint32_t)((uint32_t)(v_stack_m98))), v_stack_m70, (uint32_t)((uint32_t)(local_rdi + 1)));
    Arg1 = 0;
    if ((uint8_t)(result) == 0) goto loc_00AA65B1;
loc_00AA6716:
    v_stack_m90 = 0;
    goto loc_00AA676E;
loc_00AA6720:
    if (v_stack_m98 != 4) goto loc_00AA65B1;
    result = ExAllocatePool2(256, 4, (uint32_t)(0x63647050ULL), (uint32_t)((uint32_t)(local_rdi + 1)));
    Arg1 = 0;
    if (result == 0) goto loc_00AA65DD;
    Arg1 = ((*(uint8_t *)(v_stack_m90)) == 255) ? 1 : 0;
loc_00AA675C:
    *(uint32_t *)(result) = (uint32_t)(Arg1);
    goto loc_00AA676E;
loc_00AA6760:
    if (((uint32_t)(v_stack_m90)) != 0xC0000225ULL) goto loc_00AA6787;
loc_00AA6769:
loc_00AA676E:
    *(uint32_t *)(arg3 + 0x20) = (uint32_t)((uint32_t)((uint32_t)(Arg1)));
    *(uint32_t *)(arg3 + 0x24) = (uint32_t)((uint32_t)((uint32_t)(Arg1)));
    *(uint64_t *)(arg3 + 0x28) = result;
loc_00AA677A:
    result = v_stack_m90;
    if (v_stack_m70 != 0) {
        Arg1 = v_stack_m70;
        result = ExFreePool(Arg1, 4, (uint32_t)(0x63647050ULL), (uint32_t)((uint32_t)(local_rdi + 1)));
    }
    if (v_stack_m90 == 0) goto loc_00AA679D;
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m90, Arg2, (uint32_t)(0x63647050ULL), (uint32_t)((uint32_t)(local_rdi + 1)));
    goto loc_00AA679D;
loc_00AA6799:
loc_00AA679D:
    if (v_stack_m88 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m88;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)(0x63647050ULL), (uint32_t)((uint32_t)(local_rdi + 1)));
    }
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, (uint32_t)(0x63647050ULL), (uint32_t)((uint32_t)(local_rdi + 1)));
    local_rsp = (local_rsp) + (192);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg3` | `+ 0x20` | `32` | `W` |
| `Arg3` | `+ 0x24` | `32` | `W` |
| `Arg3` | `+ 0x28` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AA63A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
