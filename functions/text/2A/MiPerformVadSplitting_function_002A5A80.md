# MiPerformVadSplitting

- RVA: `0x002A5A80`–`0x002A6084` (길이 `1,540` bytes)
- VA: `0x00000001402A5A80`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00068A18`
- 디코드: `360`개 명령, `1,540/1,540` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **20**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002A5B7B` → [LOCK_PAGE_TABLE_COMMITMENT](LOCK_PAGE_TABLE_COMMITMENT_function_002A6090.md) (function, `0x002A6090`)
- `0x002A5BA1` → [MiLockWorkingSetExclusive](../32/MiLockWorkingSetExclusive_function_003238A0.md) (function, `0x003238A0`)
- `0x002A5BC0` → [MiLockVadTree](../27/MiLockVadTree_function_0027C0F0.md) (function, `0x0027C0F0`)
- `0x002A5C20` → [MiAdvanceVadView](MiAdvanceVadView_function_002A60EC.md) (function, `0x002A60EC`)
- `0x002A5C2C` → [MiUnlockVadTree](../29/MiUnlockVadTree_function_00297020.md) (function, `0x00297020`)
- `0x002A5C3B` → [MiUnlockWorkingSetExclusive](../27/MiUnlockWorkingSetExclusive_function_0027EC70.md) (function, `0x0027EC70`)
- `0x002A5C57` → [MiPostInsertVad](../26/MiPostInsertVad_function_002643C0.md) (function, `0x002643C0`)
- `0x002A5C64` → [UNLOCK_PAGE_TABLE_COMMITMENT](../2E/UNLOCK_PAGE_TABLE_COMMITMENT_function_002E27D0.md) (function, `0x002E27D0`)
- `0x002A5D05` → [MiInsertVad](../26/MiInsertVad_function_00265540.md) (function, `0x00265540`)
- `0x002A5D3D` → [MiLockWorkingSetExclusive](../32/MiLockWorkingSetExclusive_function_003238A0.md) (function, `0x003238A0`)
- `0x002A5D4D` → [MiUnlockNestedVad](../../page/A2/MiUnlockNestedVad_function_00A26BC4.md) (function, `0x00A26BC4`)
- `0x002A5D5D` → [PsReturnProcessPagedPoolQuota](PsReturnProcessPagedPoolQuota_function_002A6860.md) (function, `0x002A6860`)
- `0x002A5D70` → [MiPostInsertVad](../26/MiPostInsertVad_function_002643C0.md) (function, `0x002643C0`)
- `0x002A5DA2` → [MiLockWorkingSetExclusive](../32/MiLockWorkingSetExclusive_function_003238A0.md) (function, `0x003238A0`)
- `0x002A5DD0` → [MiComputePageCommitment](../2C/MiComputePageCommitment_function_002C5C34.md) (function, `0x002C5C34`)
- `0x002A5E5F` → [MiCountSharedPages](../2C/MiCountSharedPages_function_002C30A4.md) (function, `0x002C30A4`)
- `0x002A5E9C` → [MiCountSharedPages](../2C/MiCountSharedPages_function_002C30A4.md) (function, `0x002C30A4`)
- `0x002A5F54` → [MiInsertVad](../26/MiInsertVad_function_00265540.md) (function, `0x00265540`)
- `0x002A5FDC` → [MiLockNestedVad](../../page/A2/MiLockNestedVad_function_00A25FBC.md) (function, `0x00A25FBC`)
- `0x002A603F` → [MiComputePageCommitment](../2C/MiComputePageCommitment_function_002C5C34.md) (function, `0x002C5C34`)

### Direct callers
- [MiDeletePartialVad](MiDeletePartialVad_function_002A7A30.md) at `0x002A7AB3`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x002A5D4D` → [MiUnlockNestedVad](../../page/A2/MiUnlockNestedVad_function_00A26BC4.md) (`.text` → `PAGE`)
  - `0x002A5FDC` → [MiLockNestedVad](../../page/A2/MiLockNestedVad_function_00A25FBC.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002A5A80  40 53                           push rbx
002A5A82  55                              push rbp
002A5A83  56                              push rsi
002A5A84  57                              push rdi
002A5A85  41 54                           push r12
002A5A87  41 55                           push r13
002A5A89  41 56                           push r14
002A5A8B  41 57                           push r15
002A5A8D  48 83 EC 78                     sub rsp, 0x78
002A5A91  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002A5A9A  49 B9 F8 FF FF FF 7F 00 00 00   movabs r9, 0x7ffffffff8
002A5AA4  48 8B 51 20                     mov rdx, qword ptr [rcx + 0x20]
002A5AA8  44 8B 41 10                     mov r8d, dword ptr [rcx + 0x10]
002A5AAC  48 8B 79 08                     mov rdi, qword ptr [rcx + 8]
002A5AB0  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
002A5AB5  48 8B 80 B8 00 00 00            mov rax, qword ptr [rax + 0xb8]
002A5ABC  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
002A5AC1  48 05 00 04 00 00               add rax, 0x400
002A5AC7  48 89 84 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rax
002A5ACF  33 C0                           xor eax, eax
002A5AD1  48 21 44 24 50                  and qword ptr [rsp + 0x50], rax
002A5AD6  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
002A5ADB  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
002A5ADF  4C 8B E8                        mov r13, rax
002A5AE2  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
002A5AE7  49 C1 ED 09                     shr r13, 9
002A5AEB  4D 23 E9                        and r13, r9
002A5AEE  48 89 54 24 60                  mov qword ptr [rsp + 0x60], rdx
002A5AF3  44 89 84 24 C8 00 00 00         mov dword ptr [rsp + 0xc8], r8d
002A5AFB  49 BA 00 00 00 00 80 F6 FF FF   movabs r10, 0xfffff68000000000
002A5B05  49 8B C2                        mov rax, r10
002A5B08  48 C1 EA 09                     shr rdx, 9
002A5B0C  4C 03 E8                        add r13, rax
002A5B0F  49 23 D1                        and rdx, r9
002A5B12  49 8B C2                        mov rax, r10
002A5B15  48 8B 31                        mov rsi, qword ptr [rcx]
002A5B18  48 03 D0                        add rdx, rax
002A5B1B  48 89 94 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rdx
002A5B23  41 83 F8 01                     cmp r8d, 1
002A5B27  0F 85 91 03 00 00               jne 0x1402a5ebe
002A5B2D  45 33 F6                        xor r14d, r14d
002A5B30  8B 4F 34                        mov ecx, dword ptr [rdi + 0x34]
002A5B33  45 33 E4                        xor r12d, r12d
002A5B36  0F B6 57 22                     movzx edx, byte ptr [rdi + 0x22]
002A5B3A  48 B8 FD FF FF FF 07 00 00 00   movabs rax, 0x7fffffffd
002A5B44  48 C1 E2 20                     shl rdx, 0x20
002A5B48  48 0B D1                        or rdx, rcx
002A5B4B  48 3B D0                        cmp rdx, rax
002A5B4E  0F 85 BB 01 00 00               jne 0x1402a5d0f
002A5B54  45 33 FF                        xor r15d, r15d
002A5B57  48 8B E8                        mov rbp, rax
002A5B5A  48 8B DD                        mov rbx, rbp
002A5B5D  41 83 F8 03                     cmp r8d, 3
002A5B61  0F 84 1A 04 00 00               je 0x1402a5f81
002A5B67  33 C9                           xor ecx, ecx
002A5B69  48 89 8C 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rcx
002A5B71  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
002A5B76  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
002A5B7B  E8 10 05 00 00                  call 0x1402a6090
002A5B80  8B 47 30                        mov eax, dword ptr [rdi + 0x30]
002A5B83  25 00 00 20 00                  and eax, 0x200000
002A5B88  4D 85 FF                        test r15, r15
002A5B8B  0F 85 01 02 00 00               jne 0x1402a5d92
002A5B91  85 C0                           test eax, eax
002A5B93  0F 84 F1 01 00 00               je 0x1402a5d8a
002A5B99  48 8B 8C 24 D8 00 00 00         mov rcx, qword ptr [rsp + 0xd8]
002A5BA1  E8 FA DC 07 00                  call 0x1403238a0
002A5BA6  44 8A F8                        mov r15b, al
002A5BA9  4C 8B AC 24 D0 00 00 00         mov r13, qword ptr [rsp + 0xd0]
002A5BB1  41 80 FF 11                     cmp r15b, 0x11
002A5BB5  0F 84 7A 01 00 00               je 0x1402a5d35
002A5BBB  B9 03 00 00 00                  mov ecx, 3
002A5BC0  E8 2B 65 FD FF                  call 0x14027c0f0
002A5BC5  4D 85 F6                        test r14, r14
002A5BC8  0F 85 04 03 00 00               jne 0x1402a5ed2
002A5BCE  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
002A5BD3  48 85 F6                        test rsi, rsi
002A5BD6  0F 85 B6 00 00 00               jne 0x1402a5c92
002A5BDC  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
002A5BE1  8B 4F 34                        mov ecx, dword ptr [rdi + 0x34]
002A5BE4  49 B8 FD FF FF FF 07 00 00 00   movabs r8, 0x7fffffffd
002A5BEE  0F B6 57 22                     movzx edx, byte ptr [rdi + 0x22]
002A5BF2  48 C1 E2 20                     shl rdx, 0x20
002A5BF6  48 0B D1                        or rdx, rcx
002A5BF9  49 3B D0                        cmp rdx, r8
002A5BFC  0F 84 23 01 00 00               je 0x1402a5d25
002A5C02  F7 47 30 00 00 20 00            test dword ptr [rdi + 0x30], 0x200000
002A5C09  0F 84 48 04 00 00               je 0x1402a6057
002A5C0F  44 89 67 34                     mov dword ptr [rdi + 0x34], r12d
002A5C13  49 C1 EC 20                     shr r12, 0x20
002A5C17  44 88 67 22                     mov byte ptr [rdi + 0x22], r12b
002A5C1B  33 D2                           xor edx, edx
002A5C1D  48 8B CF                        mov rcx, rdi
002A5C20  E8 C7 04 00 00                  call 0x1402a60ec
002A5C25  B2 11                           mov dl, 0x11
002A5C27  B9 03 00 00 00                  mov ecx, 3
002A5C2C  E8 EF 13 FF FF                  call 0x140297020
002A5C31  41 8A D7                        mov dl, r15b
002A5C34  48 8D 8B 00 04 00 00            lea rcx, [rbx + 0x400]
002A5C3B  E8 30 90 FD FF                  call 0x14027ec70
002A5C40  4D 85 F6                        test r14, r14
002A5C43  0F 85 1E 01 00 00               jne 0x1402a5d67
002A5C49  48 85 F6                        test rsi, rsi
002A5C4C  74 0E                           je 0x1402a5c5c
002A5C4E  45 33 C0                        xor r8d, r8d
002A5C51  48 8B D3                        mov rdx, rbx
002A5C54  48 8B CE                        mov rcx, rsi
002A5C57  E8 64 E7 FB FF                  call 0x1402643c0
002A5C5C  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
002A5C61  48 8B D3                        mov rdx, rbx
002A5C64  E8 67 CB 03 00                  call 0x1402e27d0
002A5C69  4D 85 ED                        test r13, r13
002A5C6C  0F 85 D8 00 00 00               jne 0x1402a5d4a
002A5C72  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
002A5C77  48 85 C0                        test rax, rax
002A5C7A  0F 85 D7 00 00 00               jne 0x1402a5d57
002A5C80  48 83 C4 78                     add rsp, 0x78
002A5C84  41 5F                           pop r15
002A5C86  41 5E                           pop r14
002A5C88  41 5D                           pop r13
002A5C8A  41 5C                           pop r12
002A5C8C  5F                              pop rdi
002A5C8D  5E                              pop rsi
002A5C8E  5D                              pop rbp
002A5C8F  5B                              pop rbx
002A5C90  C3                              ret
002A5C91  CC                              int3
002A5C92  8B 4E 34                        mov ecx, dword ptr [rsi + 0x34]
002A5C95  48 B8 FD FF FF FF 07 00 00 00   movabs rax, 0x7fffffffd
002A5C9F  0F B6 56 22                     movzx edx, byte ptr [rsi + 0x22]
002A5CA3  48 C1 E2 20                     shl rdx, 0x20
002A5CA7  48 0B D1                        or rdx, rcx
002A5CAA  48 3B D0                        cmp rdx, rax
002A5CAD  0F 85 C7 00 00 00               jne 0x1402a5d7a
002A5CB3  C7 46 34 FD FF FF FF            mov dword ptr [rsi + 0x34], 0xfffffffd
002A5CBA  C6 46 22 07                     mov byte ptr [rsi + 0x22], 7
002A5CBE  8B 46 18                        mov eax, dword ptr [rsi + 0x18]
002A5CC1  41 B8 03 00 00 00               mov r8d, 3
002A5CC7  0F B6 56 20                     movzx edx, byte ptr [rsi + 0x20]
002A5CCB  0F B6 4E 21                     movzx ecx, byte ptr [rsi + 0x21]
002A5CCF  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
002A5CD4  48 C1 E1 20                     shl rcx, 0x20
002A5CD8  48 C1 E2 20                     shl rdx, 0x20
002A5CDC  48 0B D0                        or rdx, rax
002A5CDF  8B 46 1C                        mov eax, dword ptr [rsi + 0x1c]
002A5CE2  48 0B C8                        or rcx, rax
002A5CE5  48 2B CA                        sub rcx, rdx
002A5CE8  48 8D 42 FF                     lea rax, [rdx - 1]
002A5CEC  48 8B D3                        mov rdx, rbx
002A5CEF  89 47 1C                        mov dword ptr [rdi + 0x1c], eax
002A5CF2  48 8D 6C CD 00                  lea rbp, [rbp + rcx*8]
002A5CF7  48 C1 E8 20                     shr rax, 0x20
002A5CFB  48 83 C5 08                     add rbp, 8
002A5CFF  88 47 21                        mov byte ptr [rdi + 0x21], al
002A5D02  48 8B CE                        mov rcx, rsi
002A5D05  E8 36 F8 FB FF                  call 0x140265540
002A5D0A  E9 D2 FE FF FF                  jmp 0x1402a5be1
002A5D0F  8B 4F 34                        mov ecx, dword ptr [rdi + 0x34]
002A5D12  44 0F B6 7F 22                  movzx r15d, byte ptr [rdi + 0x22]
002A5D17  49 C1 E7 20                     shl r15, 0x20
002A5D1B  4C 0B F9                        or r15, rcx
002A5D1E  33 ED                           xor ebp, ebp
002A5D20  E9 35 FE FF FF                  jmp 0x1402a5b5a
002A5D25  C7 47 34 FD FF FF FF            mov dword ptr [rdi + 0x34], 0xfffffffd
002A5D2C  C6 47 22 07                     mov byte ptr [rdi + 0x22], 7
002A5D30  E9 E6 FE FF FF                  jmp 0x1402a5c1b
002A5D35  48 8B 8C 24 D8 00 00 00         mov rcx, qword ptr [rsp + 0xd8]
002A5D3D  E8 5E DB 07 00                  call 0x1403238a0
002A5D42  44 8A F8                        mov r15b, al
002A5D45  E9 71 FE FF FF                  jmp 0x1402a5bbb
002A5D4A  49 8B CD                        mov rcx, r13
002A5D4D  E8 72 0E 78 00                  call 0x140a26bc4
002A5D52  E9 1B FF FF FF                  jmp 0x1402a5c72
002A5D57  48 8B D0                        mov rdx, rax
002A5D5A  48 8B CB                        mov rcx, rbx
002A5D5D  E8 FE 0A 00 00                  call 0x1402a6860
002A5D62  E9 19 FF FF FF                  jmp 0x1402a5c80
002A5D67  45 33 C0                        xor r8d, r8d
002A5D6A  48 8B D3                        mov rdx, rbx
002A5D6D  49 8B CE                        mov rcx, r14
002A5D70  E8 4B E6 FB FF                  call 0x1402643c0
002A5D75  E9 CF FE FF FF                  jmp 0x1402a5c49
002A5D7A  89 6E 34                        mov dword ptr [rsi + 0x34], ebp
002A5D7D  48 C1 ED 20                     shr rbp, 0x20
002A5D81  40 88 6E 22                     mov byte ptr [rsi + 0x22], bpl
002A5D85  E9 34 FF FF FF                  jmp 0x1402a5cbe
002A5D8A  41 B7 11                        mov r15b, 0x11
002A5D8D  E9 17 FE FF FF                  jmp 0x1402a5ba9
002A5D92  85 C0                           test eax, eax
002A5D94  0F 84 F1 00 00 00               je 0x1402a5e8b
002A5D9A  48 8B 8C 24 D8 00 00 00         mov rcx, qword ptr [rsp + 0xd8]
002A5DA2  E8 F9 DA 07 00                  call 0x1403238a0
002A5DA7  4C 21 64 24 30                  and qword ptr [rsp + 0x30], r12
002A5DAC  44 8A C8                        mov r9b, al
002A5DAF  4C 21 64 24 28                  and qword ptr [rsp + 0x28], r12
002A5DB4  4C 8B C7                        mov r8, rdi
002A5DB7  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
002A5DBC  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
002A5DC1  C7 44 24 20 04 00 00 00         mov dword ptr [rsp + 0x20], 4
002A5DC9  88 84 24 C0 00 00 00            mov byte ptr [rsp + 0xc0], al
002A5DD0  E8 5F FE 01 00                  call 0x1402c5c34
002A5DD5  44 8A 84 24 C0 00 00 00         mov r8b, byte ptr [rsp + 0xc0]
002A5DDD  4C 8B E0                        mov r12, rax
002A5DE0  8B 84 24 C8 00 00 00            mov eax, dword ptr [rsp + 0xc8]
002A5DE7  83 F8 01                        cmp eax, 1
002A5DEA  0F 84 5C 02 00 00               je 0x1402a604c
002A5DF0  83 F8 02                        cmp eax, 2
002A5DF3  0F 84 65 01 00 00               je 0x1402a5f5e
002A5DF9  4C 8B AC 24 D0 00 00 00         mov r13, qword ptr [rsp + 0xd0]
002A5E01  41 0F B6 4D 20                  movzx ecx, byte ptr [r13 + 0x20]
002A5E06  48 C1 E1 20                     shl rcx, 0x20
002A5E0A  F7 47 30 00 00 20 00            test dword ptr [rdi + 0x30], 0x200000
002A5E11  0F 85 E8 01 00 00               jne 0x1402a5fff
002A5E17  41 8B 45 18                     mov eax, dword ptr [r13 + 0x18]
002A5E1B  48 BA FF FF FF FF 0F 00 00 00   movabs rdx, 0xfffffffff
002A5E25  48 0B C8                        or rcx, rax
002A5E28  49 B8 00 00 00 00 80 F6 FF FF   movabs r8, 0xfffff68000000000
002A5E32  48 23 CA                        and rcx, rdx
002A5E35  49 8B C0                        mov rax, r8
002A5E38  48 8D 1C C8                     lea rbx, [rax + rcx*8]
002A5E3C  41 0F B6 4D 21                  movzx ecx, byte ptr [r13 + 0x21]
002A5E41  41 8B 45 1C                     mov eax, dword ptr [r13 + 0x1c]
002A5E45  48 C1 E1 20                     shl rcx, 0x20
002A5E49  48 0B C8                        or rcx, rax
002A5E4C  48 23 CA                        and rcx, rdx
002A5E4F  49 8B C0                        mov rax, r8
002A5E52  48 8D 2C C8                     lea rbp, [rax + rcx*8]
002A5E56  48 8B D3                        mov rdx, rbx
002A5E59  4C 8B C5                        mov r8, rbp
002A5E5C  49 8B CD                        mov rcx, r13
002A5E5F  E8 40 D2 01 00                  call 0x1402c30a4
002A5E64  48 2B EB                        sub rbp, rbx
002A5E67  48 C1 FD 03                     sar rbp, 3
002A5E6B  48 2B E8                        sub rbp, rax
002A5E6E  48 FF C5                        inc rbp
002A5E71  4D 2B FC                        sub r15, r12
002A5E74  4C 2B FD                        sub r15, rbp
002A5E77  4D 3B EE                        cmp r13, r14
002A5E7A  0F 85 77 01 00 00               jne 0x1402a5ff7
002A5E80  48 8B DD                        mov rbx, rbp
002A5E83  49 8B EF                        mov rbp, r15
002A5E86  E9 E1 00 00 00                  jmp 0x1402a5f6c
002A5E8B  4C 8B A4 24 C0 00 00 00         mov r12, qword ptr [rsp + 0xc0]
002A5E93  49 8B D5                        mov rdx, r13
002A5E96  4D 8B C4                        mov r8, r12
002A5E99  48 8B CF                        mov rcx, rdi
002A5E9C  E8 03 D2 01 00                  call 0x1402c30a4
002A5EA1  4D 2B E5                        sub r12, r13
002A5EA4  41 B0 11                        mov r8b, 0x11
002A5EA7  49 C1 FC 03                     sar r12, 3
002A5EAB  4C 2B E0                        sub r12, rax
002A5EAE  44 88 84 24 C0 00 00 00         mov byte ptr [rsp + 0xc0], r8b
002A5EB6  49 FF C4                        inc r12
002A5EB9  E9 22 FF FF FF                  jmp 0x1402a5de0
002A5EBE  4C 8B F6                        mov r14, rsi
002A5EC1  41 83 F8 02                     cmp r8d, 2
002A5EC5  0F 85 AE 00 00 00               jne 0x1402a5f79
002A5ECB  33 F6                           xor esi, esi
002A5ECD  E9 5E FC FF FF                  jmp 0x1402a5b30
002A5ED2  41 8B 4E 34                     mov ecx, dword ptr [r14 + 0x34]
002A5ED6  48 B8 FD FF FF FF 07 00 00 00   movabs rax, 0x7fffffffd
002A5EE0  41 0F B6 56 22                  movzx edx, byte ptr [r14 + 0x22]
002A5EE5  48 C1 E2 20                     shl rdx, 0x20
002A5EE9  48 0B D1                        or rdx, rcx
002A5EEC  48 3B D0                        cmp rdx, rax
002A5EEF  0F 85 F1 00 00 00               jne 0x1402a5fe6
002A5EF5  41 C7 46 34 FD FF FF FF         mov dword ptr [r14 + 0x34], 0xfffffffd
002A5EFD  41 C6 46 22 07                  mov byte ptr [r14 + 0x22], 7
002A5F02  41 8B 46 1C                     mov eax, dword ptr [r14 + 0x1c]
002A5F06  41 B8 03 00 00 00               mov r8d, 3
002A5F0C  41 0F B6 56 21                  movzx edx, byte ptr [r14 + 0x21]
002A5F11  41 0F B6 4E 20                  movzx ecx, byte ptr [r14 + 0x20]
002A5F16  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
002A5F1B  48 C1 E2 20                     shl rdx, 0x20
002A5F1F  48 0B D0                        or rdx, rax
002A5F22  48 C1 E1 20                     shl rcx, 0x20
002A5F26  41 8B 46 18                     mov eax, dword ptr [r14 + 0x18]
002A5F2A  48 0B C8                        or rcx, rax
002A5F2D  48 8B C2                        mov rax, rdx
002A5F30  48 2B C1                        sub rax, rcx
002A5F33  49 8B CE                        mov rcx, r14
002A5F36  48 8D 04 C5 08 00 00 00         lea rax, [rax*8 + 8]
002A5F3E  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
002A5F43  48 8D 42 01                     lea rax, [rdx + 1]
002A5F47  89 47 18                        mov dword ptr [rdi + 0x18], eax
002A5F4A  48 8B D3                        mov rdx, rbx
002A5F4D  48 C1 E8 20                     shr rax, 0x20
002A5F51  88 47 20                        mov byte ptr [rdi + 0x20], al
002A5F54  E8 E7 F5 FB FF                  call 0x140265540
002A5F59  E9 75 FC FF FF                  jmp 0x1402a5bd3
002A5F5E  49 8B DF                        mov rbx, r15
002A5F61  49 2B DC                        sub rbx, r12
002A5F64  4C 8B AC 24 D0 00 00 00         mov r13, qword ptr [rsp + 0xd0]
002A5F6C  44 8A BC 24 C0 00 00 00         mov r15b, byte ptr [rsp + 0xc0]
002A5F74  E9 38 FC FF FF                  jmp 0x1402a5bb1
002A5F79  48 8B 36                        mov rsi, qword ptr [rsi]
002A5F7C  E9 AF FB FF FF                  jmp 0x1402a5b30
002A5F81  8B 46 1C                        mov eax, dword ptr [rsi + 0x1c]
002A5F84  44 0F B6 46 21                  movzx r8d, byte ptr [rsi + 0x21]
002A5F89  0F B6 4E 20                     movzx ecx, byte ptr [rsi + 0x20]
002A5F8D  41 0F B6 56 21                  movzx edx, byte ptr [r14 + 0x21]
002A5F92  48 C1 E1 20                     shl rcx, 0x20
002A5F96  49 C1 E0 20                     shl r8, 0x20
002A5F9A  4C 0B C0                        or r8, rax
002A5F9D  48 C1 E2 20                     shl rdx, 0x20
002A5FA1  8B 46 18                        mov eax, dword ptr [rsi + 0x18]
002A5FA4  48 0B C8                        or rcx, rax
002A5FA7  41 8B 46 1C                     mov eax, dword ptr [r14 + 0x1c]
002A5FAB  4C 2B C1                        sub r8, rcx
002A5FAE  48 0B D0                        or rdx, rax
002A5FB1  41 0F B6 4E 20                  movzx ecx, byte ptr [r14 + 0x20]
002A5FB6  49 FF C0                        inc r8
002A5FB9  41 8B 46 18                     mov eax, dword ptr [r14 + 0x18]
002A5FBD  48 C1 E1 20                     shl rcx, 0x20
002A5FC1  48 0B C8                        or rcx, rax
002A5FC4  48 2B D1                        sub rdx, rcx
002A5FC7  49 8B CE                        mov rcx, r14
002A5FCA  48 FF C2                        inc rdx
002A5FCD  49 3B D0                        cmp rdx, r8
002A5FD0  48 0F 47 CE                     cmova rcx, rsi
002A5FD4  48 89 8C 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rcx
002A5FDC  E8 DB FF 77 00                  call 0x140a25fbc
002A5FE1  E9 8B FB FF FF                  jmp 0x1402a5b71
002A5FE6  41 89 5E 34                     mov dword ptr [r14 + 0x34], ebx
002A5FEA  48 C1 EB 20                     shr rbx, 0x20
002A5FEE  41 88 5E 22                     mov byte ptr [r14 + 0x22], bl
002A5FF2  E9 0B FF FF FF                  jmp 0x1402a5f02
002A5FF7  49 8B DF                        mov rbx, r15
002A5FFA  E9 6D FF FF FF                  jmp 0x1402a5f6c
002A5FFF  41 8B 45 1C                     mov eax, dword ptr [r13 + 0x1c]
002A6003  45 8A C8                        mov r9b, r8b
002A6006  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
002A600C  4D 8B C5                        mov r8, r13
002A600F  41 0F B6 55 21                  movzx edx, byte ptr [r13 + 0x21]
002A6014  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
002A601A  48 C1 E2 20                     shl rdx, 0x20
002A601E  48 0B D0                        or rdx, rax
002A6021  C7 44 24 20 04 00 00 00         mov dword ptr [rsp + 0x20], 4
002A6029  41 8B 45 18                     mov eax, dword ptr [r13 + 0x18]
002A602D  48 0B C8                        or rcx, rax
002A6030  48 C1 E2 0C                     shl rdx, 0xc
002A6034  48 C1 E1 0C                     shl rcx, 0xc
002A6038  48 81 CA FF 0F 00 00            or rdx, 0xfff
002A603F  E8 F0 FB 01 00                  call 0x1402c5c34
002A6044  48 8B E8                        mov rbp, rax
002A6047  E9 25 FE FF FF                  jmp 0x1402a5e71
002A604C  49 8B EF                        mov rbp, r15
002A604F  49 2B EC                        sub rbp, r12
002A6052  E9 0D FF FF FF                  jmp 0x1402a5f64
002A6057  8B 4F 34                        mov ecx, dword ptr [rdi + 0x34]
002A605A  0F B6 57 22                     movzx edx, byte ptr [rdi + 0x22]
002A605E  48 C1 E2 20                     shl rdx, 0x20
002A6062  48 0B D1                        or rdx, rcx
002A6065  49 3B D0                        cmp rdx, r8
002A6068  0F 83 A1 FB FF FF               jae 0x1402a5c0f
002A606E  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
002A6073  48 85 ED                        test rbp, rbp
002A6076  48 0F 45 C5                     cmovne rax, rbp
002A607A  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
002A607F  E9 8B FB FF FF                  jmp 0x1402a5c0f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiPerformVadSplitting(__int64 a1)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p8;
    unsigned __int8 v_stack_pC0;
    unsigned int v_stack_pC8;
    unsigned __int64 v_stack_pD0;
    unsigned __int64 v_stack_pD8;

    v_rsp = (v_rsp) - (120);
    v_stack_m60 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m78 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) + (0x400ULL);
    v_stack_p20 = result;
    result = 0;
    v_stack_m70 = 0;
    v_stack_m50 = *(unsigned __int64 *)(a1 + 24);
    v_r13 = (*(unsigned __int64 *)(a1 + 24)) >> (9);
    v_r13 = (v_r13) & (a4);
    v_stack_m58 = *(unsigned __int64 *)(a1 + 32);
    v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16)));
    a2 = (*(unsigned __int64 *)(a1 + 32)) >> (9);
    v_r13 = (v_r13) + (v_r10);
    a2 = (a2) & (a4);
    a2 = (a2) + (v_r10);
    v_stack_p8 = a2;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16)))) != 1) goto loc_002A5EBE;
    v_r14 = 0;
loc_002A5B30:
    v_r12 = 0;
    a2 = (*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 34)) << (32);
    a2 = (a2) | ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 52)));
    if (a2 != v_r10) goto loc_002A5D0F;
    v_r15 = 0;
loc_002A5B5A:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16)))) == 3) goto loc_002A5F81;
    a1 = 0;
    v_stack_p18 = 0;
loc_002A5B71:
    result = LOCK_PAGE_TABLE_COMMITMENT(v_stack_m60, v_stack_m78, (unsigned int)(*(unsigned int *)(a1 + 16)), a4);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 48))) & (0x200000ULL));
    if (0 != 0) goto loc_002A5D92;
    if ((unsigned int)(result) == 0) goto loc_002A5D8A;
    result = MiLockWorkingSetExclusive(v_stack_p20, v_stack_m78, (unsigned int)(*(unsigned int *)(a1 + 16)), a4);
loc_002A5BA9:
loc_002A5BB1:
    if (((unsigned __int8)((unsigned __int8)(result))) == 17) goto loc_002A5D35;
loc_002A5BBB:
    result = MiLockVadTree(3, v_stack_m78, (unsigned int)(*(unsigned int *)(a1 + 16)), a4);
    if (0 != 0) goto loc_002A5ED2;
loc_002A5BD3:
    if (*(unsigned __int64 *)(a1) != 0) goto loc_002A5C92;
loc_002A5BE1:
    a2 = (*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 34)) << (32);
    a2 = (a2) | ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 52)));
    if (a2 == ((unsigned int)(*(unsigned int *)(a1 + 16)))) goto loc_002A5D25;
    if (((*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 48)) & (0x200000ULL)) == 0) goto loc_002A6057;
loc_002A5C0F:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 52) = 0;
    v_r12 = (v_r12) >> (32);
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 34) = (unsigned __int8)(v_r12);
loc_002A5C1B:
    a2 = 0;
    result = MiAdvanceVadView(*(unsigned __int64 *)(a1 + 8), a2, (unsigned int)(*(unsigned int *)(a1 + 16)), a4);
    result = MiUnlockVadTree(3, 17, (unsigned int)(*(unsigned int *)(a1 + 16)), a4);
    result = MiUnlockWorkingSetExclusive(v_stack_m78 + 1024, (unsigned __int8)((unsigned __int8)(result)), (unsigned int)(*(unsigned int *)(a1 + 16)), a4);
    if (0 != 0) goto loc_002A5D67;
loc_002A5C49:
    if (*(unsigned __int64 *)(a1) != 0) {
        a3 = 0;
        a2 = v_stack_m78;
        a1 = *(unsigned __int64 *)(a1);
        result = MiPostInsertVad(a1, a2, a3, a4);
    }
    result = UNLOCK_PAGE_TABLE_COMMITMENT(v_stack_m60, v_stack_m78, a3, a4);
    if (v_stack_p18 != 0) goto loc_002A5D4A;
loc_002A5C72:
    if (v_stack_m68 != 0) goto loc_002A5D57;
loc_002A5C80:
    v_rsp = (v_rsp) + (120);
    return v_stack_m68;
loc_002A5C92:
    a2 = (*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 34)) << (32);
    a2 = (a2) | ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 52)));
    if (a2 != v_stack_m68) goto loc_002A5D7A;
    *(unsigned int *)(*(unsigned __int64 *)(a1) + 52) = 0xFFFFFFFDULL;
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 34) = 7;
loc_002A5CBE:
    a1 = (*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 33)) << (32);
    a2 = (*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 32)) << (32);
    a2 = (a2) | ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 24)));
    a1 = (a1) | ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 28)));
    a1 = (a1) - (a2);
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 28) = (unsigned int)(a2 - 1);
    result = (a2 - 1) >> (32);
    v_rbp = (v_stack_p48 + a1 * 8) + (8);
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 33) = (unsigned __int8)(result);
    result = MiInsertVad(*(unsigned __int64 *)(a1), v_stack_m78, 3, a4);
    goto loc_002A5BE1;
loc_002A5D0F:
    v_r15 = (*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 34)) << (32);
    v_r15 = (v_r15) | ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 52)));
    v_rbp = 0;
    goto loc_002A5B5A;
loc_002A5D25:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 52) = 0xFFFFFFFDULL;
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 34) = 7;
    goto loc_002A5C1B;
loc_002A5D35:
    result = MiLockWorkingSetExclusive(v_stack_pD8, v_stack_m78, 3, a4);
    goto loc_002A5BBB;
loc_002A5D4A:
    result = MiUnlockNestedVad(v_stack_p18, v_stack_m78, 3, a4);
    goto loc_002A5C72;
loc_002A5D57:
    result = PsReturnProcessPagedPoolQuota(v_stack_m78, result, 3, a4);
    goto loc_002A5C80;
loc_002A5D67:
    a3 = 0;
    result = MiPostInsertVad(0, v_stack_m78, a3, a4);
    goto loc_002A5C49;
loc_002A5D7A:
    *(unsigned int *)(*(unsigned __int64 *)(a1) + 52) = 0;
    v_rbp = (v_rbp) >> (32);
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 34) = (unsigned __int8)(v_rbp);
    goto loc_002A5CBE;
loc_002A5D8A:
    goto loc_002A5BA9;
loc_002A5D92:
    if ((unsigned int)(result) == 0) goto loc_002A5E8B;
    result = MiLockWorkingSetExclusive(v_stack_pD8, v_stack_m78, a3, a4);
    v_stack_p20 = 4;
    v_stack_pC0 = (unsigned __int8)(result);
    result = MiComputePageCommitment(v_stack_p68, v_stack_p60, *(unsigned __int64 *)(a1 + 8), (unsigned __int8)(result));
loc_002A5DE0:
    if (((unsigned int)((unsigned int)(v_stack_pC8))) == 1) goto loc_002A604C;
    if (((unsigned int)((unsigned int)(v_stack_pC8))) == 2) goto loc_002A5F5E;
    a1 = (*(unsigned __int8 *)(v_stack_pD0 + 32)) << (32);
    if (((*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 48)) & (0x200000ULL)) != 0) goto loc_002A5FFF;
    a1 = (a1) | ((unsigned int)(*(unsigned int *)(v_stack_pD0 + 24)));
    a1 = (a1) & (v_stack_p60);
    a1 = (*(unsigned __int8 *)(v_stack_pD0 + 33)) << (32);
    a1 = (a1) | ((unsigned int)(*(unsigned int *)(v_stack_pD0 + 28)));
    a1 = (a1) & (v_stack_p60);
    result = MiCountSharedPages(v_stack_pD0, v_stack_pC0 + a1 * 8, v_stack_pC0 + a1 * 8, (unsigned __int8)(result));
    v_rbp = (v_stack_pC0 + a1 * 8) - (v_stack_pC0 + a1 * 8);
    v_rbp = (v_rbp) >> (3);
    v_rbp = (v_rbp) - (result);
    v_rbp = (v_rbp) + 1;
loc_002A5E71:
    v_r15 = (17) - (result);
    v_r15 = (v_r15) - (v_rbp);
    if (v_stack_pD0 != 0) goto loc_002A5FF7;
    goto loc_002A5F6C;
loc_002A5E8B:
    result = MiCountSharedPages(*(unsigned __int64 *)(a1 + 8), v_stack_pD0, v_stack_pC0, (unsigned __int8)(result));
    v_r12 = (v_stack_pC0) - (v_stack_pD0);
    v_r12 = (v_r12) >> (3);
    v_r12 = (v_r12) - (result);
    v_stack_pC0 = 17;
    v_r12 = (v_r12) + 1;
    goto loc_002A5DE0;
loc_002A5EBE:
    if (17 != 2) goto loc_002A5F79;
    v_rsi = 0;
    goto loc_002A5B30;
loc_002A5ED2:
    a2 = (*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 34)) << (32);
    a2 = (a2) | ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 52)));
    if (a2 != result) goto loc_002A5FE6;
    *(unsigned int *)(*(unsigned __int64 *)(a1) + 52) = 0xFFFFFFFDULL;
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 34) = 7;
loc_002A5F02:
    a2 = (*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 33)) << (32);
    a2 = (a2) | ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 28)));
    a1 = (*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 32)) << (32);
    a1 = (a1) | ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 24)));
    result = (a2) - (a1);
    v_stack_p48 = result * 8 + 8;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 24) = (unsigned int)(a2 + 1);
    result = (a2 + 1) >> (32);
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 32) = (unsigned __int8)(result);
    result = MiInsertVad(*(unsigned __int64 *)(a1), v_stack_p40, 3, (unsigned __int8)(result));
    goto loc_002A5BD3;
loc_002A5F5E:
    v_rbx = (v_r15) - (v_r12);
loc_002A5F64:
loc_002A5F6C:
    goto loc_002A5BB1;
loc_002A5F79:
    goto loc_002A5B30;
loc_002A5F81:
    a1 = (*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsi) + 32)) << (32);
    a3 = (*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsi) + 33)) << (32);
    a3 = (a3) | ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsi) + 28)));
    a2 = (*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 33)) << (32);
    a1 = (a1) | ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsi) + 24)));
    a3 = (a3) - (a1);
    a2 = (a2) | ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 28)));
    a3 = (a3) + 1;
    a1 = (*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 32)) << (32);
    a1 = (a1) | ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 24)));
    a2 = (a2) - (a1);
    a2 = (a2) + 1;
    a1 = *(unsigned __int64 *)(a1);
    if (a2 > a3) { a1 = *(unsigned __int64 *)(v_rsi); }
    v_stack_pD0 = a1;
    result = MiLockNestedVad(a1, a2, a3, (unsigned __int8)(result));
    goto loc_002A5B71;
loc_002A5FE6:
    *(unsigned int *)(*(unsigned __int64 *)(a1) + 52) = (unsigned int)(v_rbx);
    v_rbx = (v_rbx) >> (32);
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 34) = (unsigned __int8)(v_rbx);
    goto loc_002A5F02;
loc_002A5FF7:
    goto loc_002A5F6C;
loc_002A5FFF:
    a2 = (*(unsigned __int8 *)(v_stack_pD0 + 33)) << (32);
    a2 = (a2) | ((unsigned int)(*(unsigned int *)(v_stack_pD0 + 28)));
    v_stack_p20 = 4;
    a1 = (a1) | ((unsigned int)(*(unsigned int *)(v_stack_pD0 + 24)));
    a2 = (a2) << (12);
    a1 = (a1) << (12);
    a2 = (a2) | (0xFFFULL);
    result = MiComputePageCommitment(a1, a2, v_stack_pD0, (unsigned __int8)(a3));
    goto loc_002A5E71;
loc_002A604C:
    v_rbp = (v_stack_pC0) - (v_r12);
    goto loc_002A5F64;
loc_002A6057:
    a2 = (*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 34)) << (32);
    a2 = (a2) | ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 52)));
    if (a2 >= v_stack_pD0) goto loc_002A5C0F;
    result = v_stack_p50;
    if (v_rbp != 0) { result = v_rbp; }
    v_stack_p50 = result;
    goto loc_002A5C0F;
}
```

## 5. (Beta) C Style

```c
int64_t MiPerformVadSplitting(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p8;
    uint8_t v_stack_pC0;
    uint32_t v_stack_pC8;
    uint64_t v_stack_pD0;
    uint64_t v_stack_pD8;

    local_rsp = (local_rsp) - (120);
    v_stack_m60 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m78 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    result = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) + (0x400ULL);
    v_stack_p20 = result;
    result = 0;
    v_stack_m70 = 0;
    v_stack_m50 = *(uint64_t *)(arg1 + 0x18);
    local_r13 = (*(uint64_t *)(arg1 + 0x18)) >> (9);
    local_r13 = (local_r13) & (a4);
    v_stack_m58 = *(uint64_t *)(arg1 + 0x20);
    v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10)));
    a2 = (*(uint64_t *)(arg1 + 0x20)) >> (9);
    local_r13 = (local_r13) + (local_r10);
    a2 = (a2) & (a4);
    a2 = (a2) + (local_r10);
    v_stack_p8 = a2;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10)))) != 1) goto loc_002A5EBE;
    local_r14 = 0;
loc_002A5B30:
    local_r12 = 0;
    a2 = (*(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x22)) << (32);
    a2 = (a2) | ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x34)));
    if (a2 != local_r10) goto loc_002A5D0F;
    local_r15 = 0;
loc_002A5B5A:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10)))) == 3) goto loc_002A5F81;
    Arg1 = 0;
    v_stack_p18 = 0;
loc_002A5B71:
    result = LOCK_PAGE_TABLE_COMMITMENT(v_stack_m60, v_stack_m78, (uint32_t)(*(uint32_t *)(arg1 + 0x10)), a4);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x30))) & (0x200000ULL));
    if (0 != 0) goto loc_002A5D92;
    if ((uint32_t)(result) == 0) goto loc_002A5D8A;
    result = MiLockWorkingSetExclusive(v_stack_p20, v_stack_m78, (uint32_t)(*(uint32_t *)(arg1 + 0x10)), a4);
loc_002A5BA9:
loc_002A5BB1:
    if (((uint8_t)((uint8_t)(result))) == 17) goto loc_002A5D35;
loc_002A5BBB:
    result = MiLockVadTree(3, v_stack_m78, (uint32_t)(*(uint32_t *)(arg1 + 0x10)), a4);
    if (0 != 0) goto loc_002A5ED2;
loc_002A5BD3:
    if (*(uint64_t *)(arg1) != 0) goto loc_002A5C92;
loc_002A5BE1:
    a2 = (*(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x22)) << (32);
    a2 = (a2) | ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x34)));
    if (a2 == ((uint32_t)(*(uint32_t *)(arg1 + 0x10)))) goto loc_002A5D25;
    if (((*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x30)) & (0x200000ULL)) == 0) goto loc_002A6057;
loc_002A5C0F:
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x34) = 0;
    local_r12 = (local_r12) >> (32);
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x22) = (uint8_t)(local_r12);
loc_002A5C1B:
    a2 = 0;
    result = MiAdvanceVadView(*(uint64_t *)(arg1 + 0x8), a2, (uint32_t)(*(uint32_t *)(arg1 + 0x10)), a4);
    result = MiUnlockVadTree(3, 17, (uint32_t)(*(uint32_t *)(arg1 + 0x10)), a4);
    result = MiUnlockWorkingSetExclusive(v_stack_m78 + 1024, (uint8_t)((uint8_t)(result)), (uint32_t)(*(uint32_t *)(arg1 + 0x10)), a4);
    if (0 != 0) goto loc_002A5D67;
loc_002A5C49:
    if (*(uint64_t *)(arg1) != 0) {
        a3 = 0;
        a2 = v_stack_m78;
        Arg1 = *(uint64_t *)(arg1);
        result = MiPostInsertVad(Arg1, a2, a3, a4);
    }
    result = UNLOCK_PAGE_TABLE_COMMITMENT(v_stack_m60, v_stack_m78, a3, a4);
    if (v_stack_p18 != 0) goto loc_002A5D4A;
loc_002A5C72:
    if (v_stack_m68 != 0) goto loc_002A5D57;
loc_002A5C80:
    local_rsp = (local_rsp) + (120);
    return v_stack_m68;
loc_002A5C92:
    a2 = (*(uint8_t *)(*(uint64_t *)(arg1) + 0x22)) << (32);
    a2 = (a2) | ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x34)));
    if (a2 != v_stack_m68) goto loc_002A5D7A;
    *(uint32_t *)(*(uint64_t *)(arg1) + 0x34) = 0xFFFFFFFDULL;
    *(uint8_t *)(*(uint64_t *)(arg1) + 0x22) = 7;
loc_002A5CBE:
    Arg1 = (*(uint8_t *)(*(uint64_t *)(arg1) + 0x21)) << (32);
    a2 = (*(uint8_t *)(*(uint64_t *)(arg1) + 0x20)) << (32);
    a2 = (a2) | ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x18)));
    Arg1 = (Arg1) | ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x1C)));
    Arg1 = (Arg1) - (a2);
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x1C) = (uint32_t)(a2 - 1);
    result = (a2 - 1) >> (32);
    local_rbp = (v_stack_p48 + Arg1 * 8) + (8);
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x21) = (uint8_t)(result);
    result = MiInsertVad(*(uint64_t *)(arg1), v_stack_m78, 3, a4);
    goto loc_002A5BE1;
loc_002A5D0F:
    local_r15 = (*(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x22)) << (32);
    local_r15 = (local_r15) | ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x34)));
    local_rbp = 0;
    goto loc_002A5B5A;
loc_002A5D25:
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x34) = 0xFFFFFFFDULL;
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x22) = 7;
    goto loc_002A5C1B;
loc_002A5D35:
    result = MiLockWorkingSetExclusive(v_stack_pD8, v_stack_m78, 3, a4);
    goto loc_002A5BBB;
loc_002A5D4A:
    result = MiUnlockNestedVad(v_stack_p18, v_stack_m78, 3, a4);
    goto loc_002A5C72;
loc_002A5D57:
    result = PsReturnProcessPagedPoolQuota(v_stack_m78, result, 3, a4);
    goto loc_002A5C80;
loc_002A5D67:
    a3 = 0;
    result = MiPostInsertVad(0, v_stack_m78, a3, a4);
    goto loc_002A5C49;
loc_002A5D7A:
    *(uint32_t *)(*(uint64_t *)(arg1) + 0x34) = 0;
    local_rbp = (local_rbp) >> (32);
    *(uint8_t *)(*(uint64_t *)(arg1) + 0x22) = (uint8_t)(local_rbp);
    goto loc_002A5CBE;
loc_002A5D8A:
    goto loc_002A5BA9;
loc_002A5D92:
    if ((uint32_t)(result) == 0) goto loc_002A5E8B;
    result = MiLockWorkingSetExclusive(v_stack_pD8, v_stack_m78, a3, a4);
    v_stack_p20 = 4;
    v_stack_pC0 = (uint8_t)(result);
    result = MiComputePageCommitment(v_stack_p68, v_stack_p60, *(uint64_t *)(arg1 + 0x8), (uint8_t)(result));
loc_002A5DE0:
    if (((uint32_t)((uint32_t)(v_stack_pC8))) == 1) goto loc_002A604C;
    if (((uint32_t)((uint32_t)(v_stack_pC8))) == 2) goto loc_002A5F5E;
    Arg1 = (*(uint8_t *)(v_stack_pD0 + 0x20)) << (32);
    if (((*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x30)) & (0x200000ULL)) != 0) goto loc_002A5FFF;
    Arg1 = (Arg1) | ((uint32_t)(*(uint32_t *)(v_stack_pD0 + 0x18)));
    Arg1 = (Arg1) & (v_stack_p60);
    Arg1 = (*(uint8_t *)(v_stack_pD0 + 0x21)) << (32);
    Arg1 = (Arg1) | ((uint32_t)(*(uint32_t *)(v_stack_pD0 + 0x1C)));
    Arg1 = (Arg1) & (v_stack_p60);
    result = MiCountSharedPages(v_stack_pD0, v_stack_pC0 + Arg1 * 8, v_stack_pC0 + Arg1 * 8, (uint8_t)(result));
    local_rbp = (v_stack_pC0 + Arg1 * 8) - (v_stack_pC0 + Arg1 * 8);
    local_rbp = (local_rbp) >> (3);
    local_rbp = (local_rbp) - (result);
    local_rbp = (local_rbp) + 1;
loc_002A5E71:
    local_r15 = (17) - (result);
    local_r15 = (local_r15) - (local_rbp);
    if (v_stack_pD0 != 0) goto loc_002A5FF7;
    goto loc_002A5F6C;
loc_002A5E8B:
    result = MiCountSharedPages(*(uint64_t *)(arg1 + 0x8), v_stack_pD0, v_stack_pC0, (uint8_t)(result));
    local_r12 = (v_stack_pC0) - (v_stack_pD0);
    local_r12 = (local_r12) >> (3);
    local_r12 = (local_r12) - (result);
    v_stack_pC0 = 17;
    local_r12 = (local_r12) + 1;
    goto loc_002A5DE0;
loc_002A5EBE:
    if (17 != 2) goto loc_002A5F79;
    local_rsi = 0;
    goto loc_002A5B30;
loc_002A5ED2:
    a2 = (*(uint8_t *)(*(uint64_t *)(arg1) + 0x22)) << (32);
    a2 = (a2) | ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x34)));
    if (a2 != result) goto loc_002A5FE6;
    *(uint32_t *)(*(uint64_t *)(arg1) + 0x34) = 0xFFFFFFFDULL;
    *(uint8_t *)(*(uint64_t *)(arg1) + 0x22) = 7;
loc_002A5F02:
    a2 = (*(uint8_t *)(*(uint64_t *)(arg1) + 0x21)) << (32);
    a2 = (a2) | ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x1C)));
    Arg1 = (*(uint8_t *)(*(uint64_t *)(arg1) + 0x20)) << (32);
    Arg1 = (Arg1) | ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x18)));
    result = (a2) - (Arg1);
    v_stack_p48 = result * 8 + 8;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18) = (uint32_t)(a2 + 1);
    result = (a2 + 1) >> (32);
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) = (uint8_t)(result);
    result = MiInsertVad(*(uint64_t *)(arg1), v_stack_p40, 3, (uint8_t)(result));
    goto loc_002A5BD3;
loc_002A5F5E:
    local_rbx = (local_r15) - (local_r12);
loc_002A5F64:
loc_002A5F6C:
    goto loc_002A5BB1;
loc_002A5F79:
    goto loc_002A5B30;
loc_002A5F81:
    Arg1 = (*(uint8_t *)(*(uint64_t *)(local_rsi) + 0x20)) << (32);
    a3 = (*(uint8_t *)(*(uint64_t *)(local_rsi) + 0x21)) << (32);
    a3 = (a3) | ((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsi) + 0x1C)));
    a2 = (*(uint8_t *)(*(uint64_t *)(arg1) + 0x21)) << (32);
    Arg1 = (Arg1) | ((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsi) + 0x18)));
    a3 = (a3) - (Arg1);
    a2 = (a2) | ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x1C)));
    a3 = (a3) + 1;
    Arg1 = (*(uint8_t *)(*(uint64_t *)(arg1) + 0x20)) << (32);
    Arg1 = (Arg1) | ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x18)));
    a2 = (a2) - (Arg1);
    a2 = (a2) + 1;
    Arg1 = *(uint64_t *)(arg1);
    if (a2 > a3) { Arg1 = *(uint64_t *)(local_rsi); }
    v_stack_pD0 = Arg1;
    result = MiLockNestedVad(Arg1, a2, a3, (uint8_t)(result));
    goto loc_002A5B71;
loc_002A5FE6:
    *(uint32_t *)(*(uint64_t *)(arg1) + 0x34) = (uint32_t)(local_rbx);
    local_rbx = (local_rbx) >> (32);
    *(uint8_t *)(*(uint64_t *)(arg1) + 0x22) = (uint8_t)(local_rbx);
    goto loc_002A5F02;
loc_002A5FF7:
    goto loc_002A5F6C;
loc_002A5FFF:
    a2 = (*(uint8_t *)(v_stack_pD0 + 0x21)) << (32);
    a2 = (a2) | ((uint32_t)(*(uint32_t *)(v_stack_pD0 + 0x1C)));
    v_stack_p20 = 4;
    Arg1 = (Arg1) | ((uint32_t)(*(uint32_t *)(v_stack_pD0 + 0x18)));
    a2 = (a2) << (12);
    Arg1 = (Arg1) << (12);
    a2 = (a2) | (0xFFFULL);
    result = MiComputePageCommitment(Arg1, a2, v_stack_pD0, (uint8_t)(a3));
    goto loc_002A5E71;
loc_002A604C:
    local_rbp = (v_stack_pC0) - (local_r12);
    goto loc_002A5F64;
loc_002A6057:
    a2 = (*(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x22)) << (32);
    a2 = (a2) | ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x34)));
    if (a2 >= v_stack_pD0) goto loc_002A5C0F;
    result = v_stack_p50;
    if (local_rbp != 0) { result = local_rbp; }
    v_stack_p50 = result;
    goto loc_002A5C0F;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002A5A80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
