# CmpFindControlSet

- RVA: `0x007F1A34`–`0x007F1F78` (길이 `1,348` bytes)
- VA: `0x00000001407F1A34`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D72CC`
- 디코드: `344`개 명령, `1,348/1,348` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **54**; 고유 호출 대상: **11**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x007F1AC2` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x007F1AC9` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x007F1AE6` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x007F1AFF` → [CmpFindSubKeyByNameWithStatus](../85/CmpFindSubKeyByNameWithStatus_function_00852770.md) (function, `0x00852770`)
- `0x007F1B15` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007F1B1C` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007F1B41` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x007F1B48` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x007F1B65` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x007F1B75` → [CmpFindValueByName](../84/CmpFindValueByName_function_00844E1C.md) (function, `0x00844E1C`)
- `0x007F1B8D` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007F1B94` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007F1BB9` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x007F1BC0` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x007F1BE5` → [CmpValueToData](CmpValueToData_function_007F3934.md) (function, `0x007F3934`)
- `0x007F1BFE` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007F1C05` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007F1C29` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007F1C30` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007F1C48` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x007F1C4F` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x007F1C69` → [CmpFindValueByName](../84/CmpFindValueByName_function_00844E1C.md) (function, `0x00844E1C`)
- `0x007F1C81` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007F1C88` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007F1CA9` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x007F1CB0` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x007F1CE5` → [CmpValueToData](CmpValueToData_function_007F3934.md) (function, `0x007F3934`)
- `0x007F1CFE` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007F1D05` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007F1D26` → [sprintf_s](../../text/50/sprintf_s_function_00505E40.md) (function, `0x00505E40`)
- `0x007F1D6D` → [RtlAnsiStringToUnicodeString](../90/RtlAnsiStringToUnicodeString_function_0090BEA0.md) (function, `0x0090BEA0`)
- `0x007F1D9A` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x007F1DA1` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x007F1DD1` → [CmpFindSubKeyByNameWithStatus](../85/CmpFindSubKeyByNameWithStatus_function_00852770.md) (function, `0x00852770`)
- `0x007F1DE7` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007F1DEE` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007F1E1D` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x007F1E24` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x007F1E41` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x007F1E51` → [CmpFindValueByName](../84/CmpFindValueByName_function_00844E1C.md) (function, `0x00844E1C`)
- `0x007F1E69` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007F1E70` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007F1E91` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x007F1E98` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x007F1EC3` → [CmpValueToData](CmpValueToData_function_007F3934.md) (function, `0x007F3934`)
- `0x007F1EE1` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007F1EF3` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x007F1F0D` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007F1F29` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007F1F30` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007F1F46` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007F1F4D` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007F1F63` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007F1F6A` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)

### Direct callers
- [CmpAcquireSystemDriverHiveContext](../../init/C5/CmpAcquireSystemDriverHiveContext_function_00C56514.md) at `0x00C5655A`
- [CmpGetSystemControlValues](../../init/C5/CmpGetSystemControlValues_function_00C5959C.md) at `0x00C59774`

### Static image references
- `0x007F1A50` → RVA `0x00E0A740` (`.data`; read)
- `0x007F1ADA` → RVA `0x00B09B70` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007F1B59` → RVA `0x00B09B40` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007F1D16` → RVA `0x00B09B60` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007F1E35` → RVA `0x00AFD370` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **5**
  - `0x007F1AE6` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x007F1B65` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x007F1D26` → [sprintf_s](../../text/50/sprintf_s_function_00505E40.md) (`PAGE` → `.text`)
  - `0x007F1E41` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x007F1EF3` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007F1A34  40 55                           push rbp
007F1A36  53                              push rbx
007F1A37  56                              push rsi
007F1A38  57                              push rdi
007F1A39  41 54                           push r12
007F1A3B  41 55                           push r13
007F1A3D  41 56                           push r14
007F1A3F  41 57                           push r15
007F1A41  48 8D AC 24 E8 FE FF FF         lea rbp, [rsp - 0x118]
007F1A49  48 81 EC 18 02 00 00            sub rsp, 0x218
007F1A50  48 8B 05 E9 8C 61 00            mov rax, qword ptr [rip + 0x618ce9]
007F1A57  48 33 C4                        xor rax, rsp
007F1A5A  48 89 85 00 01 00 00            mov qword ptr [rbp + 0x100], rax
007F1A61  33 F6                           xor esi, esi
007F1A63  48 8B D9                        mov rbx, rcx
007F1A66  83 C9 FF                        or ecx, 0xffffffff
007F1A69  89 74 24 44                     mov dword ptr [rsp + 0x44], esi
007F1A6D  41 B5 01                        mov r13b, 1
007F1A70  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
007F1A74  0F 57 C0                        xorps xmm0, xmm0
007F1A77  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
007F1A7B  0F 57 C9                        xorps xmm1, xmm1
007F1A7E  4D 8B E0                        mov r12, r8
007F1A81  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
007F1A86  89 4C 24 58                     mov dword ptr [rsp + 0x58], ecx
007F1A8A  4D 8B F1                        mov r14, r9
007F1A8D  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
007F1A91  44 8B FA                        mov r15d, edx
007F1A94  89 4C 24 50                     mov dword ptr [rsp + 0x50], ecx
007F1A98  48 8B CB                        mov rcx, rbx
007F1A9B  89 74 24 3C                     mov dword ptr [rsp + 0x3c], esi
007F1A9F  0F 11 44 24 60                  movups xmmword ptr [rsp + 0x60], xmm0
007F1AA4  89 74 24 5C                     mov dword ptr [rsp + 0x5c], esi
007F1AA8  0F 11 4C 24 70                  movups xmmword ptr [rsp + 0x70], xmm1
007F1AAD  89 74 24 4C                     mov dword ptr [rsp + 0x4c], esi
007F1AB1  89 74 24 34                     mov dword ptr [rsp + 0x34], esi
007F1AB5  89 74 24 54                     mov dword ptr [rsp + 0x54], esi
007F1AB9  44 84 AB 8C 00 00 00            test byte ptr [rbx + 0x8c], r13b
007F1AC0  74 07                           je 0x1407f1ac9
007F1AC2  E8 99 31 06 00                  call 0x140854c60
007F1AC7  EB 05                           jmp 0x1407f1ace
007F1AC9  E8 E2 31 06 00                  call 0x140854cb0
007F1ACE  48 8B F8                        mov rdi, rax
007F1AD1  48 85 C0                        test rax, rax
007F1AD4  0F 84 0C 04 00 00               je 0x1407f1ee6
007F1ADA  48 8D 15 8F 80 31 00            lea rdx, [rip + 0x31808f]
007F1AE1  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
007F1AE6  E8 95 8C C3 FF                  call 0x14042a780
007F1AEB  4C 8D 4C 24 48                  lea r9, [rsp + 0x48]
007F1AF0  89 74 24 48                     mov dword ptr [rsp + 0x48], esi
007F1AF4  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
007F1AF9  48 8B D7                        mov rdx, rdi
007F1AFC  48 8B CB                        mov rcx, rbx
007F1AFF  E8 6C 0C 06 00                  call 0x140852770
007F1B04  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
007F1B09  48 8B CB                        mov rcx, rbx
007F1B0C  44 84 AB 8C 00 00 00            test byte ptr [rbx + 0x8c], r13b
007F1B13  74 07                           je 0x1407f1b1c
007F1B15  E8 06 B1 06 00                  call 0x14085cc20
007F1B1A  EB 05                           jmp 0x1407f1b21
007F1B1C  E8 1F 44 06 00                  call 0x140855f40
007F1B21  8B 7C 24 48                     mov edi, dword ptr [rsp + 0x48]
007F1B25  83 FF FF                        cmp edi, -1
007F1B28  0F 84 B8 03 00 00               je 0x1407f1ee6
007F1B2E  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
007F1B33  8B D7                           mov edx, edi
007F1B35  48 8B CB                        mov rcx, rbx
007F1B38  44 84 AB 8C 00 00 00            test byte ptr [rbx + 0x8c], r13b
007F1B3F  74 07                           je 0x1407f1b48
007F1B41  E8 1A 31 06 00                  call 0x140854c60
007F1B46  EB 05                           jmp 0x1407f1b4d
007F1B48  E8 63 31 06 00                  call 0x140854cb0
007F1B4D  48 8B F0                        mov rsi, rax
007F1B50  48 85 C0                        test rax, rax
007F1B53  0F 84 8D 03 00 00               je 0x1407f1ee6
007F1B59  48 8D 15 E0 7F 31 00            lea rdx, [rip + 0x317fe0]
007F1B60  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
007F1B65  E8 16 8C C3 FF                  call 0x14042a780
007F1B6A  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
007F1B6F  48 8B D6                        mov rdx, rsi
007F1B72  48 8B CB                        mov rcx, rbx
007F1B75  E8 A2 32 05 00                  call 0x140844e1c
007F1B7A  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
007F1B7F  8B F0                           mov esi, eax
007F1B81  48 8B CB                        mov rcx, rbx
007F1B84  44 84 AB 8C 00 00 00            test byte ptr [rbx + 0x8c], r13b
007F1B8B  74 07                           je 0x1407f1b94
007F1B8D  E8 8E B0 06 00                  call 0x14085cc20
007F1B92  EB 05                           jmp 0x1407f1b99
007F1B94  E8 A7 43 06 00                  call 0x140855f40
007F1B99  83 FE FF                        cmp esi, -1
007F1B9C  75 08                           jne 0x1407f1ba6
007F1B9E  45 88 2E                        mov byte ptr [r14], r13b
007F1BA1  E9 8F 00 00 00                  jmp 0x1407f1c35
007F1BA6  4C 8D 44 24 40                  lea r8, [rsp + 0x40]
007F1BAB  8B D6                           mov edx, esi
007F1BAD  48 8B CB                        mov rcx, rbx
007F1BB0  44 84 AB 8C 00 00 00            test byte ptr [rbx + 0x8c], r13b
007F1BB7  74 07                           je 0x1407f1bc0
007F1BB9  E8 A2 30 06 00                  call 0x140854c60
007F1BBE  EB 05                           jmp 0x1407f1bc5
007F1BC0  E8 EB 30 06 00                  call 0x140854cb0
007F1BC5  48 85 C0                        test rax, rax
007F1BC8  0F 84 18 03 00 00               je 0x1407f1ee6
007F1BCE  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
007F1BD3  4C 8B C0                        mov r8, rax
007F1BD6  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
007F1BDB  4C 8D 4C 24 4C                  lea r9, [rsp + 0x4c]
007F1BE0  48 8B CB                        mov rcx, rbx
007F1BE3  8B D6                           mov edx, esi
007F1BE5  E8 4A 1D 00 00                  call 0x1407f3934
007F1BEA  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
007F1BEF  48 8B F0                        mov rsi, rax
007F1BF2  48 8B CB                        mov rcx, rbx
007F1BF5  44 84 AB 8C 00 00 00            test byte ptr [rbx + 0x8c], r13b
007F1BFC  74 07                           je 0x1407f1c05
007F1BFE  E8 1D B0 06 00                  call 0x14085cc20
007F1C03  EB 05                           jmp 0x1407f1c0a
007F1C05  E8 36 43 06 00                  call 0x140855f40
007F1C0A  48 85 F6                        test rsi, rsi
007F1C0D  0F 84 D3 02 00 00               je 0x1407f1ee6
007F1C13  8A 06                           mov al, byte ptr [rsi]
007F1C15  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
007F1C1A  41 88 06                        mov byte ptr [r14], al
007F1C1D  48 8B CB                        mov rcx, rbx
007F1C20  44 84 AB 8C 00 00 00            test byte ptr [rbx + 0x8c], r13b
007F1C27  74 07                           je 0x1407f1c30
007F1C29  E8 F2 AF 06 00                  call 0x14085cc20
007F1C2E  EB 05                           jmp 0x1407f1c35
007F1C30  E8 0B 43 06 00                  call 0x140855f40
007F1C35  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
007F1C3A  8B D7                           mov edx, edi
007F1C3C  48 8B CB                        mov rcx, rbx
007F1C3F  44 84 AB 8C 00 00 00            test byte ptr [rbx + 0x8c], r13b
007F1C46  74 07                           je 0x1407f1c4f
007F1C48  E8 13 30 06 00                  call 0x140854c60
007F1C4D  EB 05                           jmp 0x1407f1c54
007F1C4F  E8 5C 30 06 00                  call 0x140854cb0
007F1C54  45 33 F6                        xor r14d, r14d
007F1C57  48 85 C0                        test rax, rax
007F1C5A  0F 84 86 02 00 00               je 0x1407f1ee6
007F1C60  4D 8B C4                        mov r8, r12
007F1C63  48 8B D0                        mov rdx, rax
007F1C66  48 8B CB                        mov rcx, rbx
007F1C69  E8 AE 31 05 00                  call 0x140844e1c
007F1C6E  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
007F1C73  8B F0                           mov esi, eax
007F1C75  48 8B CB                        mov rcx, rbx
007F1C78  44 84 AB 8C 00 00 00            test byte ptr [rbx + 0x8c], r13b
007F1C7F  74 07                           je 0x1407f1c88
007F1C81  E8 9A AF 06 00                  call 0x14085cc20
007F1C86  EB 05                           jmp 0x1407f1c8d
007F1C88  E8 B3 42 06 00                  call 0x140855f40
007F1C8D  83 FE FF                        cmp esi, -1
007F1C90  0F 84 50 02 00 00               je 0x1407f1ee6
007F1C96  4C 8D 44 24 40                  lea r8, [rsp + 0x40]
007F1C9B  8B D6                           mov edx, esi
007F1C9D  48 8B CB                        mov rcx, rbx
007F1CA0  44 84 AB 8C 00 00 00            test byte ptr [rbx + 0x8c], r13b
007F1CA7  74 07                           je 0x1407f1cb0
007F1CA9  E8 B2 2F 06 00                  call 0x140854c60
007F1CAE  EB 05                           jmp 0x1407f1cb5
007F1CB0  E8 FB 2F 06 00                  call 0x140854cb0
007F1CB5  48 85 C0                        test rax, rax
007F1CB8  0F 84 28 02 00 00               je 0x1407f1ee6
007F1CBE  83 78 0C 04                     cmp dword ptr [rax + 0xc], 4
007F1CC2  74 0A                           je 0x1407f1cce
007F1CC4  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
007F1CC9  E9 07 02 00 00                  jmp 0x1407f1ed5
007F1CCE  48 8D 4C 24 38                  lea rcx, [rsp + 0x38]
007F1CD3  4C 8B C0                        mov r8, rax
007F1CD6  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
007F1CDB  4C 8D 4C 24 4C                  lea r9, [rsp + 0x4c]
007F1CE0  48 8B CB                        mov rcx, rbx
007F1CE3  8B D6                           mov edx, esi
007F1CE5  E8 4A 1C 00 00                  call 0x1407f3934
007F1CEA  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
007F1CEF  48 8B F0                        mov rsi, rax
007F1CF2  48 8B CB                        mov rcx, rbx
007F1CF5  44 84 AB 8C 00 00 00            test byte ptr [rbx + 0x8c], r13b
007F1CFC  74 07                           je 0x1407f1d05
007F1CFE  E8 1D AF 06 00                  call 0x14085cc20
007F1D03  EB 05                           jmp 0x1407f1d0a
007F1D05  E8 36 42 06 00                  call 0x140855f40
007F1D0A  48 85 F6                        test rsi, rsi
007F1D0D  0F 84 D3 01 00 00               je 0x1407f1ee6
007F1D13  44 8B 0E                        mov r9d, dword ptr [rsi]
007F1D16  4C 8D 05 43 7E 31 00            lea r8, [rip + 0x317e43]
007F1D1D  BA 80 00 00 00                  mov edx, 0x80
007F1D22  48 8D 4D 80                     lea rcx, [rbp - 0x80]
007F1D26  E8 15 41 D1 FF                  call 0x140505e40
007F1D2B  48 8D 4D 80                     lea rcx, [rbp - 0x80]
007F1D2F  48 83 C8 FF                     or rax, 0xffffffffffffffff
007F1D33  48 FF C0                        inc rax
007F1D36  44 38 34 01                     cmp byte ptr [rcx + rax], r14b
007F1D3A  75 F7                           jne 0x1407f1d33
007F1D3C  66 89 44 24 72                  mov word ptr [rsp + 0x72], ax
007F1D41  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
007F1D46  66 89 44 24 70                  mov word ptr [rsp + 0x70], ax
007F1D4B  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
007F1D50  48 8D 45 80                     lea rax, [rbp - 0x80]
007F1D54  C7 44 24 60 00 00 00 01         mov dword ptr [rsp + 0x60], 0x1000000
007F1D5C  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
007F1D61  45 33 C0                        xor r8d, r8d
007F1D64  48 8D 45 00                     lea rax, [rbp]
007F1D68  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
007F1D6D  E8 2E A1 11 00                  call 0x14090bea0
007F1D72  8A 8B 8C 00 00 00               mov cl, byte ptr [rbx + 0x8c]
007F1D78  41 22 CD                        and cl, r13b
007F1D7B  85 C0                           test eax, eax
007F1D7D  79 0C                           jns 0x1407f1d8b
007F1D7F  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
007F1D84  84 C9                           test cl, cl
007F1D86  E9 51 01 00 00                  jmp 0x1407f1edc
007F1D8B  84 C9                           test cl, cl
007F1D8D  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
007F1D92  48 8B CB                        mov rcx, rbx
007F1D95  41 8B D7                        mov edx, r15d
007F1D98  74 07                           je 0x1407f1da1
007F1D9A  E8 C1 2E 06 00                  call 0x140854c60
007F1D9F  EB 05                           jmp 0x1407f1da6
007F1DA1  E8 0A 2F 06 00                  call 0x140854cb0
007F1DA6  48 8B CB                        mov rcx, rbx
007F1DA9  48 85 C0                        test rax, rax
007F1DAC  75 11                           jne 0x1407f1dbf
007F1DAE  44 84 AB 8C 00 00 00            test byte ptr [rbx + 0x8c], r13b
007F1DB5  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
007F1DBA  E9 20 01 00 00                  jmp 0x1407f1edf
007F1DBF  4C 8D 4C 24 48                  lea r9, [rsp + 0x48]
007F1DC4  44 89 74 24 48                  mov dword ptr [rsp + 0x48], r14d
007F1DC9  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
007F1DCE  48 8B D0                        mov rdx, rax
007F1DD1  E8 9A 09 06 00                  call 0x140852770
007F1DD6  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
007F1DDB  48 8B CB                        mov rcx, rbx
007F1DDE  44 84 AB 8C 00 00 00            test byte ptr [rbx + 0x8c], r13b
007F1DE5  74 07                           je 0x1407f1dee
007F1DE7  E8 34 AE 06 00                  call 0x14085cc20
007F1DEC  EB 05                           jmp 0x1407f1df3
007F1DEE  E8 4D 41 06 00                  call 0x140855f40
007F1DF3  8A 83 8C 00 00 00               mov al, byte ptr [rbx + 0x8c]
007F1DF9  48 8B CB                        mov rcx, rbx
007F1DFC  41 22 C5                        and al, r13b
007F1DFF  83 7C 24 48 FF                  cmp dword ptr [rsp + 0x48], -1
007F1E04  75 0C                           jne 0x1407f1e12
007F1E06  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
007F1E0B  84 C0                           test al, al
007F1E0D  E9 CD 00 00 00                  jmp 0x1407f1edf
007F1E12  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
007F1E17  8B D7                           mov edx, edi
007F1E19  84 C0                           test al, al
007F1E1B  74 07                           je 0x1407f1e24
007F1E1D  E8 3E 2E 06 00                  call 0x140854c60
007F1E22  EB 05                           jmp 0x1407f1e29
007F1E24  E8 87 2E 06 00                  call 0x140854cb0
007F1E29  48 8B F8                        mov rdi, rax
007F1E2C  48 85 C0                        test rax, rax
007F1E2F  0F 84 9B 00 00 00               je 0x1407f1ed0
007F1E35  48 8D 15 34 B5 30 00            lea rdx, [rip + 0x30b534]
007F1E3C  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
007F1E41  E8 3A 89 C3 FF                  call 0x14042a780
007F1E46  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
007F1E4B  48 8B D7                        mov rdx, rdi
007F1E4E  48 8B CB                        mov rcx, rbx
007F1E51  E8 C6 2F 05 00                  call 0x140844e1c
007F1E56  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
007F1E5B  8B F8                           mov edi, eax
007F1E5D  48 8B CB                        mov rcx, rbx
007F1E60  44 84 AB 8C 00 00 00            test byte ptr [rbx + 0x8c], r13b
007F1E67  74 07                           je 0x1407f1e70
007F1E69  E8 B2 AD 06 00                  call 0x14085cc20
007F1E6E  EB 05                           jmp 0x1407f1e75
007F1E70  E8 CB 40 06 00                  call 0x140855f40
007F1E75  83 FF FF                        cmp edi, -1
007F1E78  0F 84 D4 00 00 00               je 0x1407f1f52
007F1E7E  4C 8D 44 24 40                  lea r8, [rsp + 0x40]
007F1E83  8B D7                           mov edx, edi
007F1E85  48 8B CB                        mov rcx, rbx
007F1E88  44 84 AB 8C 00 00 00            test byte ptr [rbx + 0x8c], r13b
007F1E8F  74 07                           je 0x1407f1e98
007F1E91  E8 CA 2D 06 00                  call 0x140854c60
007F1E96  EB 05                           jmp 0x1407f1e9d
007F1E98  E8 13 2E 06 00                  call 0x140854cb0
007F1E9D  48 85 C0                        test rax, rax
007F1EA0  74 2E                           je 0x1407f1ed0
007F1EA2  83 78 0C 04                     cmp dword ptr [rax + 0xc], 4
007F1EA6  0F 85 89 00 00 00               jne 0x1407f1f35
007F1EAC  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
007F1EB1  4C 8B C0                        mov r8, rax
007F1EB4  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
007F1EB9  4C 8D 4C 24 4C                  lea r9, [rsp + 0x4c]
007F1EBE  48 8B CB                        mov rcx, rbx
007F1EC1  8B D7                           mov edx, edi
007F1EC3  E8 6C 1A 00 00                  call 0x1407f3934
007F1EC8  48 8B C8                        mov rcx, rax
007F1ECB  48 85 C0                        test rax, rax
007F1ECE  75 44                           jne 0x1407f1f14
007F1ED0  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
007F1ED5  44 84 AB 8C 00 00 00            test byte ptr [rbx + 0x8c], r13b
007F1EDC  48 8B CB                        mov rcx, rbx
007F1EDF  74 2C                           je 0x1407f1f0d
007F1EE1  E8 3A AD 06 00                  call 0x14085cc20
007F1EE6  83 C8 FF                        or eax, 0xffffffff
007F1EE9  48 8B 8D 00 01 00 00            mov rcx, qword ptr [rbp + 0x100]
007F1EF0  48 33 CC                        xor rcx, rsp
007F1EF3  E8 48 A7 EB FF                  call 0x1406ac640
007F1EF8  48 81 C4 18 02 00 00            add rsp, 0x218
007F1EFF  41 5F                           pop r15
007F1F01  41 5E                           pop r14
007F1F03  41 5D                           pop r13
007F1F05  41 5C                           pop r12
007F1F07  5F                              pop rdi
007F1F08  5E                              pop rsi
007F1F09  5B                              pop rbx
007F1F0A  5D                              pop rbp
007F1F0B  C3                              ret
007F1F0C  CC                              int3
007F1F0D  E8 2E 40 06 00                  call 0x140855f40
007F1F12  EB D2                           jmp 0x1407f1ee6
007F1F14  8B 06                           mov eax, dword ptr [rsi]
007F1F16  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
007F1F1B  89 01                           mov dword ptr [rcx], eax
007F1F1D  48 8B CB                        mov rcx, rbx
007F1F20  44 84 AB 8C 00 00 00            test byte ptr [rbx + 0x8c], r13b
007F1F27  74 07                           je 0x1407f1f30
007F1F29  E8 F2 AC 06 00                  call 0x14085cc20
007F1F2E  EB 05                           jmp 0x1407f1f35
007F1F30  E8 0B 40 06 00                  call 0x140855f40
007F1F35  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
007F1F3A  48 8B CB                        mov rcx, rbx
007F1F3D  44 84 AB 8C 00 00 00            test byte ptr [rbx + 0x8c], r13b
007F1F44  74 07                           je 0x1407f1f4d
007F1F46  E8 D5 AC 06 00                  call 0x14085cc20
007F1F4B  EB 05                           jmp 0x1407f1f52
007F1F4D  E8 EE 3F 06 00                  call 0x140855f40
007F1F52  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
007F1F57  48 8B CB                        mov rcx, rbx
007F1F5A  44 84 AB 8C 00 00 00            test byte ptr [rbx + 0x8c], r13b
007F1F61  74 07                           je 0x1407f1f6a
007F1F63  E8 B8 AC 06 00                  call 0x14085cc20
007F1F68  EB 05                           jmp 0x1407f1f6f
007F1F6A  E8 D1 3F 06 00                  call 0x140855f40
007F1F6F  8B 44 24 48                     mov eax, dword ptr [rsp + 0x48]
007F1F73  E9 71 FF FF FF                  jmp 0x1407f1ee9
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpFindControlSet(__int64 a1, int a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned __int16 v_stack_m1E6;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned __int64 v_stack_m1F8;
    unsigned int v_stack_m1FC;
    unsigned int v_stack_m200;
    unsigned int v_stack_m204;
    unsigned int v_stack_m208;
    unsigned int v_stack_m20C;
    unsigned __int64 v_stack_m210;
    unsigned int v_stack_m214;
    unsigned int v_stack_m218;
    unsigned int v_stack_m21C;
    unsigned int v_stack_m220;
    unsigned int v_stack_m224;
    unsigned __int64 v_stack_m228;
    unsigned __int64 v_stack_m238;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned int v_stack_p48;
    unsigned __int64 v_stack_p58;

    v_rsp = (v_rsp) - (536);
    result = (*(unsigned __int64 *)(v_rip + 6393065)) ^ (v_rsp);
    v_stack_m58 = result;
    v_rsi = 0;
    a1 = (unsigned int)((a1) | (0xFFFFFFFFULL));
    v_stack_m214 = 0;
    v_stack_m218 = (unsigned int)(a1);
    v_stack_m220 = (unsigned int)(a1);
    v_stack_m200 = (unsigned int)(a1);
    v_stack_m228 = (unsigned int)(a1);
    v_stack_m208 = (unsigned int)(a1);
    v_stack_m21C = 0;
    v_stack_m1F8 = v_xmm0;
    v_stack_m1FC = 0;
    v_stack_m1E8 = v_xmm1;
    v_stack_m20C = 0;
    v_stack_m224 = 0;
    v_stack_m204 = 0;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_007F1AC9;
    result = HvpGetCellFlat(a1, a2, v_stack_m228, a4);
    goto loc_007F1ACE;
loc_007F1AC9:
    result = HvpGetCellPaged(a1, a2, v_stack_m228, a4);
loc_007F1ACE:
    if (result == 0) goto loc_007F1EE6;
    result = RtlInitUnicodeString(v_stack_m1F8, v_rip + 3244175, v_stack_m228, a4);
    v_stack_m210 = 0;
    result = CmpFindSubKeyByNameWithStatus(a1, result, v_stack_m1F8, v_stack_m210);
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_007F1B1C;
    result = HvpReleaseCellFlat(a1, v_stack_m228, v_stack_m1F8, v_stack_m210);
    goto loc_007F1B21;
loc_007F1B1C:
    result = HvpReleaseCellPaged(a1, v_stack_m228, v_stack_m1F8, v_stack_m210);
loc_007F1B21:
    if (((unsigned int)((unsigned int)(v_stack_m210))) == -1) goto loc_007F1EE6;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_007F1B48;
    result = HvpGetCellFlat(a1, (unsigned int)((unsigned int)((unsigned int)(v_stack_m210))), v_stack_m228, v_stack_m210);
    goto loc_007F1B4D;
loc_007F1B48:
    result = HvpGetCellPaged(a1, (unsigned int)((unsigned int)((unsigned int)(v_stack_m210))), v_stack_m228, v_stack_m210);
loc_007F1B4D:
    if (result == 0) goto loc_007F1EE6;
    result = RtlInitUnicodeString(v_stack_m1F8, v_rip + 3244000, v_stack_m228, v_stack_m210);
    result = CmpFindValueByName(a1, result, v_stack_m1F8, v_stack_m210);
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_007F1B94;
    result = HvpReleaseCellFlat(a1, v_stack_m228, v_stack_m1F8, v_stack_m210);
    goto loc_007F1B99;
loc_007F1B94:
    result = HvpReleaseCellPaged(a1, v_stack_m228, v_stack_m1F8, v_stack_m210);
loc_007F1B99:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != -1) goto loc_007F1BA6;
    *(unsigned __int8 *)(a4) = 1;
    goto loc_007F1C35;
loc_007F1BA6:
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_007F1BC0;
    result = HvpGetCellFlat(a1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_stack_m218, v_stack_m210);
    goto loc_007F1BC5;
loc_007F1BC0:
    result = HvpGetCellPaged(a1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_stack_m218, v_stack_m210);
loc_007F1BC5:
    if (result == 0) goto loc_007F1EE6;
    v_stack_m238 = v_stack_m208;
    result = CmpValueToData(a1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), result, v_stack_m20C);
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_007F1C05;
    result = HvpReleaseCellFlat(a1, v_stack_m218, result, v_stack_m20C);
    goto loc_007F1C0A;
loc_007F1C05:
    result = HvpReleaseCellPaged(a1, v_stack_m218, result, v_stack_m20C);
loc_007F1C0A:
    if (result == 0) goto loc_007F1EE6;
    *(unsigned __int8 *)(a4) = (unsigned __int8)(*(unsigned __int8 *)(result));
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_007F1C30;
    result = HvpReleaseCellFlat(a1, v_stack_m208, result, v_stack_m20C);
    goto loc_007F1C35;
loc_007F1C30:
    result = HvpReleaseCellPaged(a1, v_stack_m208, result, v_stack_m20C);
loc_007F1C35:
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_007F1C4F;
    result = HvpGetCellFlat(a1, (unsigned int)((unsigned int)((unsigned int)(v_stack_m210))), v_stack_m228, v_stack_m20C);
    goto loc_007F1C54;
loc_007F1C4F:
    result = HvpGetCellPaged(a1, (unsigned int)((unsigned int)((unsigned int)(v_stack_m210))), v_stack_m228, v_stack_m20C);
loc_007F1C54:
    v_r14 = 0;
    if (result == 0) goto loc_007F1EE6;
    result = CmpFindValueByName(a1, result, a3, v_stack_m20C);
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_007F1C88;
    result = HvpReleaseCellFlat(a1, v_stack_m228, a3, v_stack_m20C);
    goto loc_007F1C8D;
loc_007F1C88:
    result = HvpReleaseCellPaged(a1, v_stack_m228, a3, v_stack_m20C);
loc_007F1C8D:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == -1) goto loc_007F1EE6;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_007F1CB0;
    result = HvpGetCellFlat(a1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_stack_m218, v_stack_m20C);
    goto loc_007F1CB5;
loc_007F1CB0:
    result = HvpGetCellPaged(a1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_stack_m218, v_stack_m20C);
loc_007F1CB5:
    if (result == 0) goto loc_007F1EE6;
    if ((*(unsigned int *)(result + 12)) == 4) goto loc_007F1CCE;
    goto loc_007F1ED5;
loc_007F1CCE:
    v_stack_m238 = v_stack_m220;
    result = CmpValueToData(a1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), result, v_stack_m20C);
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_007F1D05;
    result = HvpReleaseCellFlat(a1, v_stack_m218, result, v_stack_m20C);
    goto loc_007F1D0A;
loc_007F1D05:
    result = HvpReleaseCellPaged(a1, v_stack_m218, result, v_stack_m20C);
loc_007F1D0A:
    if (result == 0) goto loc_007F1EE6;
    result = sprintf_s(v_stack_m1D8, 128, v_rip + 3243587, (unsigned int)(*(unsigned int *)(result)));
    result = (result) | (-1);
loc_007F1D33:
    result = (result) + 1;
    if ((*(unsigned __int8 *)(v_stack_m1D8 + result * 1)) != 0) goto loc_007F1D33;
    v_stack_m1E6 = (unsigned __int16)(result);
    v_stack_m1E8 = (unsigned __int16)(result);
    v_stack_m1F8 = 0x1000000ULL;
    v_stack_m1E0 = v_stack_m1D8;
    a3 = 0;
    v_stack_m1F0 = v_stack_m158;
    result = RtlAnsiStringToUnicodeString(v_stack_m1F8, v_stack_m1E8, a3, (unsigned int)(*(unsigned int *)(result)));
    a1 = (unsigned __int8)((*(unsigned __int8 *)(a1 + 140)) & (1));
    if (!sign_flag) goto loc_007F1D8B;
    goto loc_007F1EDC;
loc_007F1D8B:
    if ((unsigned __int8)(a1) == 0) goto loc_007F1DA1;
    result = HvpGetCellFlat(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), v_stack_m228, (unsigned int)(*(unsigned int *)(result)));
    goto loc_007F1DA6;
loc_007F1DA1:
    result = HvpGetCellPaged(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), v_stack_m228, (unsigned int)(*(unsigned int *)(result)));
loc_007F1DA6:
    if (result != 0) goto loc_007F1DBF;
    goto loc_007F1EDF;
loc_007F1DBF:
    v_stack_m210 = 0;
    result = CmpFindSubKeyByNameWithStatus(a1, result, v_stack_m1F8, v_stack_m210);
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_007F1DEE;
    result = HvpReleaseCellFlat(a1, v_stack_m228, v_stack_m1F8, v_stack_m210);
    goto loc_007F1DF3;
loc_007F1DEE:
    result = HvpReleaseCellPaged(a1, v_stack_m228, v_stack_m1F8, v_stack_m210);
loc_007F1DF3:
    result = (unsigned __int8)((*(unsigned __int8 *)(a1 + 140)) & (1));
    if (v_stack_m210 != -1) goto loc_007F1E12;
    goto loc_007F1EDF;
loc_007F1E12:
    if ((unsigned __int8)(result) == 0) goto loc_007F1E24;
    result = HvpGetCellFlat(a1, (unsigned int)((unsigned int)((unsigned int)(v_stack_m210))), v_stack_m228, v_stack_m210);
    goto loc_007F1E29;
loc_007F1E24:
    result = HvpGetCellPaged(a1, (unsigned int)((unsigned int)((unsigned int)(v_stack_m210))), v_stack_m228, v_stack_m210);
loc_007F1E29:
    if (result == 0) goto loc_007F1ED0;
    result = RtlInitUnicodeString(v_stack_m1F8, v_rip + 3192116, v_stack_m228, v_stack_m210);
    result = CmpFindValueByName(a1, result, v_stack_m1F8, v_stack_m210);
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_007F1E70;
    result = HvpReleaseCellFlat(a1, v_stack_m228, v_stack_m1F8, v_stack_m210);
    goto loc_007F1E75;
loc_007F1E70:
    result = HvpReleaseCellPaged(a1, v_stack_m228, v_stack_m1F8, v_stack_m210);
loc_007F1E75:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == -1) goto loc_007F1F52;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_007F1E98;
    result = HvpGetCellFlat(a1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_stack_m218, v_stack_m210);
    goto loc_007F1E9D;
loc_007F1E98:
    result = HvpGetCellPaged(a1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_stack_m218, v_stack_m210);
loc_007F1E9D:
    if (result == 0) goto loc_007F1ED0;
    if ((*(unsigned int *)(result + 12)) != 4) goto loc_007F1F35;
    v_stack_m238 = v_stack_m200;
    result = CmpValueToData(a1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), result, v_stack_m20C);
    if (result != 0) goto loc_007F1F14;
loc_007F1ED0:
loc_007F1ED5:
loc_007F1EDC:
loc_007F1EDF:
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_007F1F0D;
    result = HvpReleaseCellFlat(a1, v_stack_m220, result, v_stack_m20C);
loc_007F1EE6:
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
loc_007F1EE9:
    a1 = (v_stack_m58) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m220, result, v_stack_m20C);
    v_rsp = (v_rsp) + (536);
    return result;
loc_007F1F0D:
    result = HvpReleaseCellPaged(a1, v_stack_m220, result, v_stack_m20C);
    goto loc_007F1EE6;
loc_007F1F14:
    *(unsigned int *)(a1) = (unsigned int)((unsigned int)(*(unsigned int *)(result)));
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_007F1F30;
    result = HvpReleaseCellFlat(a1, v_stack_p58, result, v_stack_m20C);
    goto loc_007F1F35;
loc_007F1F30:
    result = HvpReleaseCellPaged(a1, v_stack_p58, result, v_stack_m20C);
loc_007F1F35:
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_007F1F4D;
    result = HvpReleaseCellFlat(a1, v_stack_p40, result, v_stack_m20C);
    goto loc_007F1F52;
loc_007F1F4D:
    result = HvpReleaseCellPaged(a1, v_stack_p40, result, v_stack_m20C);
loc_007F1F52:
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_007F1F6A;
    result = HvpReleaseCellFlat(a1, v_stack_p38, result, v_stack_m20C);
    goto loc_007F1F6F;
loc_007F1F6A:
    result = HvpReleaseCellPaged(a1, v_stack_p38, result, v_stack_m20C);
loc_007F1F6F:
    goto loc_007F1EE9;
}
```

## 5. (Beta) C Style

```c
int64_t CmpFindControlSet(void *Arg1, int32_t Arg2, int64_t Arg3, void *Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r14;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m158;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint16_t v_stack_m1E6;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint64_t v_stack_m1F8;
    uint32_t v_stack_m1FC;
    uint32_t v_stack_m200;
    uint32_t v_stack_m204;
    uint32_t v_stack_m208;
    uint32_t v_stack_m20C;
    uint64_t v_stack_m210;
    uint32_t v_stack_m214;
    uint32_t v_stack_m218;
    uint32_t v_stack_m21C;
    uint32_t v_stack_m220;
    uint32_t v_stack_m224;
    uint64_t v_stack_m228;
    uint64_t v_stack_m238;
    uint64_t v_stack_m58;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint32_t v_stack_p48;
    uint64_t v_stack_p58;

    local_rsp = (local_rsp) - (536);
    result = (*(uint64_t *)(v_rip + 0x618CE9)) ^ (local_rsp);
    v_stack_m58 = result;
    local_rsi = 0;
    Arg1 = (uint32_t)((Arg1) | (0xFFFFFFFFULL));
    v_stack_m214 = 0;
    v_stack_m218 = (uint32_t)(Arg1);
    v_stack_m220 = (uint32_t)(Arg1);
    v_stack_m200 = (uint32_t)(Arg1);
    v_stack_m228 = (uint32_t)(Arg1);
    v_stack_m208 = (uint32_t)(Arg1);
    v_stack_m21C = 0;
    v_stack_m1F8 = v_xmm0;
    v_stack_m1FC = 0;
    v_stack_m1E8 = v_xmm1;
    v_stack_m20C = 0;
    v_stack_m224 = 0;
    v_stack_m204 = 0;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_007F1AC9;
    result = HvpGetCellFlat(Arg1, Arg2, v_stack_m228, Arg4);
    goto loc_007F1ACE;
loc_007F1AC9:
    result = HvpGetCellPaged(Arg1, Arg2, v_stack_m228, Arg4);
loc_007F1ACE:
    if (result == 0) goto loc_007F1EE6;
    result = RtlInitUnicodeString(v_stack_m1F8, v_rip + 3244175, v_stack_m228, Arg4);
    v_stack_m210 = 0;
    result = CmpFindSubKeyByNameWithStatus(Arg1, result, v_stack_m1F8, v_stack_m210);
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_007F1B1C;
    result = HvpReleaseCellFlat(Arg1, v_stack_m228, v_stack_m1F8, v_stack_m210);
    goto loc_007F1B21;
loc_007F1B1C:
    result = HvpReleaseCellPaged(Arg1, v_stack_m228, v_stack_m1F8, v_stack_m210);
loc_007F1B21:
    if (((uint32_t)((uint32_t)(v_stack_m210))) == -1) goto loc_007F1EE6;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_007F1B48;
    result = HvpGetCellFlat(Arg1, (uint32_t)((uint32_t)((uint32_t)(v_stack_m210))), v_stack_m228, v_stack_m210);
    goto loc_007F1B4D;
loc_007F1B48:
    result = HvpGetCellPaged(Arg1, (uint32_t)((uint32_t)((uint32_t)(v_stack_m210))), v_stack_m228, v_stack_m210);
loc_007F1B4D:
    if (result == 0) goto loc_007F1EE6;
    result = RtlInitUnicodeString(v_stack_m1F8, v_rip + 3244000, v_stack_m228, v_stack_m210);
    result = CmpFindValueByName(Arg1, result, v_stack_m1F8, v_stack_m210);
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_007F1B94;
    result = HvpReleaseCellFlat(Arg1, v_stack_m228, v_stack_m1F8, v_stack_m210);
    goto loc_007F1B99;
loc_007F1B94:
    result = HvpReleaseCellPaged(Arg1, v_stack_m228, v_stack_m1F8, v_stack_m210);
loc_007F1B99:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != -1) goto loc_007F1BA6;
    *(uint8_t *)(arg4) = 1;
    goto loc_007F1C35;
loc_007F1BA6:
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_007F1BC0;
    result = HvpGetCellFlat(Arg1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), v_stack_m218, v_stack_m210);
    goto loc_007F1BC5;
loc_007F1BC0:
    result = HvpGetCellPaged(Arg1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), v_stack_m218, v_stack_m210);
loc_007F1BC5:
    if (result == 0) goto loc_007F1EE6;
    v_stack_m238 = v_stack_m208;
    result = CmpValueToData(Arg1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), result, v_stack_m20C);
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_007F1C05;
    result = HvpReleaseCellFlat(Arg1, v_stack_m218, result, v_stack_m20C);
    goto loc_007F1C0A;
loc_007F1C05:
    result = HvpReleaseCellPaged(Arg1, v_stack_m218, result, v_stack_m20C);
loc_007F1C0A:
    if (result == 0) goto loc_007F1EE6;
    *(uint8_t *)(arg4) = (uint8_t)(*(uint8_t *)(result));
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_007F1C30;
    result = HvpReleaseCellFlat(Arg1, v_stack_m208, result, v_stack_m20C);
    goto loc_007F1C35;
loc_007F1C30:
    result = HvpReleaseCellPaged(Arg1, v_stack_m208, result, v_stack_m20C);
loc_007F1C35:
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_007F1C4F;
    result = HvpGetCellFlat(Arg1, (uint32_t)((uint32_t)((uint32_t)(v_stack_m210))), v_stack_m228, v_stack_m20C);
    goto loc_007F1C54;
loc_007F1C4F:
    result = HvpGetCellPaged(Arg1, (uint32_t)((uint32_t)((uint32_t)(v_stack_m210))), v_stack_m228, v_stack_m20C);
loc_007F1C54:
    local_r14 = 0;
    if (result == 0) goto loc_007F1EE6;
    result = CmpFindValueByName(Arg1, result, Arg3, v_stack_m20C);
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_007F1C88;
    result = HvpReleaseCellFlat(Arg1, v_stack_m228, Arg3, v_stack_m20C);
    goto loc_007F1C8D;
loc_007F1C88:
    result = HvpReleaseCellPaged(Arg1, v_stack_m228, Arg3, v_stack_m20C);
loc_007F1C8D:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == -1) goto loc_007F1EE6;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_007F1CB0;
    result = HvpGetCellFlat(Arg1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), v_stack_m218, v_stack_m20C);
    goto loc_007F1CB5;
loc_007F1CB0:
    result = HvpGetCellPaged(Arg1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), v_stack_m218, v_stack_m20C);
loc_007F1CB5:
    if (result == 0) goto loc_007F1EE6;
    if ((*(uint32_t *)(result + 0xC)) == 4) goto loc_007F1CCE;
    goto loc_007F1ED5;
loc_007F1CCE:
    v_stack_m238 = v_stack_m220;
    result = CmpValueToData(Arg1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), result, v_stack_m20C);
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_007F1D05;
    result = HvpReleaseCellFlat(Arg1, v_stack_m218, result, v_stack_m20C);
    goto loc_007F1D0A;
loc_007F1D05:
    result = HvpReleaseCellPaged(Arg1, v_stack_m218, result, v_stack_m20C);
loc_007F1D0A:
    if (result == 0) goto loc_007F1EE6;
    result = sprintf_s(v_stack_m1D8, 128, v_rip + 3243587, (uint32_t)(*(uint32_t *)(result)));
    result = (result) | (-1);
loc_007F1D33:
    result = (result) + 1;
    if ((*(uint8_t *)(v_stack_m1D8 + result * 1)) != 0) goto loc_007F1D33;
    v_stack_m1E6 = (uint16_t)(result);
    v_stack_m1E8 = (uint16_t)(result);
    v_stack_m1F8 = 0x1000000ULL;
    v_stack_m1E0 = v_stack_m1D8;
    Arg3 = 0;
    v_stack_m1F0 = v_stack_m158;
    result = RtlAnsiStringToUnicodeString(v_stack_m1F8, v_stack_m1E8, Arg3, (uint32_t)(*(uint32_t *)(result)));
    Arg1 = (uint8_t)((*(uint8_t *)(arg1 + 0x8C)) & (1));
    if (!sign_flag) goto loc_007F1D8B;
    goto loc_007F1EDC;
loc_007F1D8B:
    if ((uint8_t)(Arg1) == 0) goto loc_007F1DA1;
    result = HvpGetCellFlat(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), v_stack_m228, (uint32_t)(*(uint32_t *)(result)));
    goto loc_007F1DA6;
loc_007F1DA1:
    result = HvpGetCellPaged(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), v_stack_m228, (uint32_t)(*(uint32_t *)(result)));
loc_007F1DA6:
    if (result != 0) goto loc_007F1DBF;
    goto loc_007F1EDF;
loc_007F1DBF:
    v_stack_m210 = 0;
    result = CmpFindSubKeyByNameWithStatus(Arg1, result, v_stack_m1F8, v_stack_m210);
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_007F1DEE;
    result = HvpReleaseCellFlat(Arg1, v_stack_m228, v_stack_m1F8, v_stack_m210);
    goto loc_007F1DF3;
loc_007F1DEE:
    result = HvpReleaseCellPaged(Arg1, v_stack_m228, v_stack_m1F8, v_stack_m210);
loc_007F1DF3:
    result = (uint8_t)((*(uint8_t *)(arg1 + 0x8C)) & (1));
    if (v_stack_m210 != -1) goto loc_007F1E12;
    goto loc_007F1EDF;
loc_007F1E12:
    if ((uint8_t)(result) == 0) goto loc_007F1E24;
    result = HvpGetCellFlat(Arg1, (uint32_t)((uint32_t)((uint32_t)(v_stack_m210))), v_stack_m228, v_stack_m210);
    goto loc_007F1E29;
loc_007F1E24:
    result = HvpGetCellPaged(Arg1, (uint32_t)((uint32_t)((uint32_t)(v_stack_m210))), v_stack_m228, v_stack_m210);
loc_007F1E29:
    if (result == 0) goto loc_007F1ED0;
    result = RtlInitUnicodeString(v_stack_m1F8, v_rip + 3192116, v_stack_m228, v_stack_m210);
    result = CmpFindValueByName(Arg1, result, v_stack_m1F8, v_stack_m210);
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_007F1E70;
    result = HvpReleaseCellFlat(Arg1, v_stack_m228, v_stack_m1F8, v_stack_m210);
    goto loc_007F1E75;
loc_007F1E70:
    result = HvpReleaseCellPaged(Arg1, v_stack_m228, v_stack_m1F8, v_stack_m210);
loc_007F1E75:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == -1) goto loc_007F1F52;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_007F1E98;
    result = HvpGetCellFlat(Arg1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), v_stack_m218, v_stack_m210);
    goto loc_007F1E9D;
loc_007F1E98:
    result = HvpGetCellPaged(Arg1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), v_stack_m218, v_stack_m210);
loc_007F1E9D:
    if (result == 0) goto loc_007F1ED0;
    if ((*(uint32_t *)(result + 0xC)) != 4) goto loc_007F1F35;
    v_stack_m238 = v_stack_m200;
    result = CmpValueToData(Arg1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), result, v_stack_m20C);
    if (result != 0) goto loc_007F1F14;
loc_007F1ED0:
loc_007F1ED5:
loc_007F1EDC:
loc_007F1EDF:
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_007F1F0D;
    result = HvpReleaseCellFlat(Arg1, v_stack_m220, result, v_stack_m20C);
loc_007F1EE6:
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
loc_007F1EE9:
    Arg1 = (v_stack_m58) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m220, result, v_stack_m20C);
    local_rsp = (local_rsp) + (536);
    return result;
loc_007F1F0D:
    result = HvpReleaseCellPaged(Arg1, v_stack_m220, result, v_stack_m20C);
    goto loc_007F1EE6;
loc_007F1F14:
    *(uint32_t *)(arg1) = (uint32_t)((uint32_t)(*(uint32_t *)(result)));
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_007F1F30;
    result = HvpReleaseCellFlat(Arg1, v_stack_p58, result, v_stack_m20C);
    goto loc_007F1F35;
loc_007F1F30:
    result = HvpReleaseCellPaged(Arg1, v_stack_p58, result, v_stack_m20C);
loc_007F1F35:
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_007F1F4D;
    result = HvpReleaseCellFlat(Arg1, v_stack_p40, result, v_stack_m20C);
    goto loc_007F1F52;
loc_007F1F4D:
    result = HvpReleaseCellPaged(Arg1, v_stack_p40, result, v_stack_m20C);
loc_007F1F52:
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_007F1F6A;
    result = HvpReleaseCellFlat(Arg1, v_stack_p38, result, v_stack_m20C);
    goto loc_007F1F6F;
loc_007F1F6A:
    result = HvpReleaseCellPaged(Arg1, v_stack_p38, result, v_stack_m20C);
loc_007F1F6F:
    goto loc_007F1EE9;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8C` | `8` | `R` |
| `Arg4` | `+ 0x0` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007F1A34&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
