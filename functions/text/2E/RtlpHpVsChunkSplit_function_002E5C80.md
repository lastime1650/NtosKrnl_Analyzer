# RtlpHpVsChunkSplit

- RVA: `0x002E5C80`–`0x002E6B9A` (길이 `3,866` bytes)
- VA: `0x00000001402E5C80`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00071238`
- 디코드: `953`개 명령, `3,866/3,866` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **17**; 고유 호출 대상: **9**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x002E5CC0` → [RtlRbRemoveNode](RtlRbRemoveNode_function_002E4C10.md) (function, `0x002E4C10`)
- `0x002E5FF3` → [RtlRbRemoveNode](RtlRbRemoveNode_function_002E4C10.md) (function, `0x002E4C10`)
- `0x002E60F7` → [RtlRbRemoveNode](RtlRbRemoveNode_function_002E4C10.md) (function, `0x002E4C10`)
- `0x002E6201` → [RtlRbRemoveNode](RtlRbRemoveNode_function_002E4C10.md) (function, `0x002E4C10`)
- `0x002E6466` → [RtlRbInsertNodeEx](RtlRbInsertNodeEx_function_002E4570.md) (function, `0x002E4570`)
- `0x002E6580` → [RtlRbInsertNodeEx](RtlRbInsertNodeEx_function_002E4570.md) (function, `0x002E4570`)
- `0x002E6677` → [RtlpHpVsCommitLimitCheck](RtlpHpVsCommitLimitCheck_function_002E5BBC.md) (function, `0x002E5BBC`)
- `0x002E66F2` → [RtlpHpReleaseQueuedLockExclusive](RtlpHpReleaseQueuedLockExclusive_function_002E2A70.md) (function, `0x002E2A70`)
- `0x002E670C` → [RtlpHpVsSubsegmentCommitPages](RtlpHpVsSubsegmentCommitPages_function_002E6C74.md) (function, `0x002E6C74`)
- `0x002E6731` → [RtlpHpAcquireQueuedLockExclusive](../32/RtlpHpAcquireQueuedLockExclusive_function_00324820.md) (function, `0x00324820`)
- `0x002E6853` → [RtlpHpReleaseQueuedLockExclusive](RtlpHpReleaseQueuedLockExclusive_function_002E2A70.md) (function, `0x002E2A70`)
- `0x002E68D9` → [RtlpHpAcquireQueuedLockExclusive](../32/RtlpHpAcquireQueuedLockExclusive_function_00324820.md) (function, `0x00324820`)
- `0x002E6916` → [RtlpHpSegLfhVsCommit](../32/RtlpHpSegLfhVsCommit_function_00325750.md) (function, `0x00325750`)
- `0x002E695D` → [RtlpHpReleaseQueuedLockExclusive](RtlpHpReleaseQueuedLockExclusive_function_002E2A70.md) (function, `0x002E2A70`)
- `0x002E69BB` → [RtlpHpAcquireQueuedLockExclusive](../32/RtlpHpAcquireQueuedLockExclusive_function_00324820.md) (function, `0x00324820`)
- `0x002E6AE0` → [RtlpHpVsSubsegmentCleanup](RtlpHpVsSubsegmentCleanup_function_002E6DA8.md) (function, `0x002E6DA8`)
- `0x002E6B44` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [RtlpHpVsSlotAllocate](RtlpHpVsSlotAllocate_function_002EAB38.md) at `0x002EACAC`

### Static image references
- `0x002E5CA9` → RVA `0x00E28302` (`.data`; read)
- `0x002E5D13` → RVA `0x00E28300` (`.data`; read)
- `0x002E68EF` → RVA `0x00325750` (`RtlpHpSegLfhVsCommit`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002E5C80  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
002E5C85  53                              push rbx
002E5C86  56                              push rsi
002E5C87  57                              push rdi
002E5C88  41 54                           push r12
002E5C8A  41 55                           push r13
002E5C8C  41 56                           push r14
002E5C8E  41 57                           push r15
002E5C90  48 83 EC 60                     sub rsp, 0x60
002E5C94  45 0F B7 79 02                  movzx r15d, word ptr [r9 + 2]
002E5C99  41 8B C1                        mov eax, r9d
002E5C9C  C1 E8 10                        shr eax, 0x10
002E5C9F  4C 8B F1                        mov r14, rcx
002E5CA2  44 33 F8                        xor r15d, eax
002E5CA5  48 8D 4A 10                     lea rcx, [rdx + 0x10]
002E5CA9  0F B7 05 52 26 B4 00            movzx eax, word ptr [rip + 0xb42652]
002E5CB0  49 8D 51 08                     lea rdx, [r9 + 8]
002E5CB4  44 33 F8                        xor r15d, eax
002E5CB7  49 8B F9                        mov rdi, r9
002E5CBA  4D 8B E8                        mov r13, r8
002E5CBD  41 8B F1                        mov esi, r9d
002E5CC0  E8 4B EF FF FF                  call 0x1402e4c10
002E5CC5  0F B7 05 36 26 B4 00            movzx eax, word ptr [rip + 0xb42636]
002E5CCC  33 DB                           xor ebx, ebx
002E5CCE  44 8B 07                        mov r8d, dword ptr [rdi]
002E5CD1  8B CF                           mov ecx, edi
002E5CD3  4D 0F BF 56 06                  movsx r10, word ptr [r14 + 6]
002E5CD8  41 33 C8                        xor ecx, r8d
002E5CDB  C1 E9 10                        shr ecx, 0x10
002E5CDE  44 8B DF                        mov r11d, edi
002E5CE1  33 C8                           xor ecx, eax
002E5CE3  45 2B DD                        sub r11d, r13d
002E5CE6  C1 E1 04                        shl ecx, 4
002E5CE9  8B C1                           mov eax, ecx
002E5CEB  44 8B C9                        mov r9d, ecx
002E5CEE  41 2B C5                        sub eax, r13d
002E5CF1  03 C7                           add eax, edi
002E5CF3  41 8D 93 1F 10 00 00            lea edx, [r11 + 0x101f]
002E5CFA  25 00 F0 FF FF                  and eax, 0xfffff000
002E5CFF  81 E2 00 F0 FF FF               and edx, 0xfffff000
002E5D05  8B C8                           mov ecx, eax
002E5D07  2B CA                           sub ecx, edx
002E5D09  3B D0                           cmp edx, eax
002E5D0B  8B C7                           mov eax, edi
002E5D0D  0F 43 CB                        cmovae ecx, ebx
002E5D10  41 33 C0                        xor eax, r8d
002E5D13  33 05 E7 25 B4 00               xor eax, dword ptr [rip + 0xb425e7]
002E5D19  C1 E9 0C                        shr ecx, 0xc
002E5D1C  0F B7 D0                        movzx edx, ax
002E5D1F  49 8D 81 FF 0F 00 00            lea rax, [r9 + 0xfff]
002E5D26  2B D1                           sub edx, ecx
002E5D28  48 C1 E8 0C                     shr rax, 0xc
002E5D2C  8B CE                           mov ecx, esi
002E5D2E  81 E1 FF 0F 00 00               and ecx, 0xfff
002E5D34  48 81 C1 FF 0F 00 00            add rcx, 0xfff
002E5D3B  49 03 C9                        add rcx, r9
002E5D3E  48 C1 E9 0C                     shr rcx, 0xc
002E5D42  2B D1                           sub edx, ecx
002E5D44  03 D0                           add edx, eax
002E5D46  48 63 CA                        movsxd rcx, edx
002E5D49  66 45 85 D2                     test r10w, r10w
002E5D4D  0F 84 11 0E 00 00               je 0x1402e6b64
002E5D53  F0 4B 01 4C 32 20               lock add qword ptr [r10 + r14 + 0x20], rcx
002E5D59  8B 94 24 C0 00 00 00            mov edx, dword ptr [rsp + 0xc0]
002E5D60  44 2B FA                        sub r15d, edx
002E5D63  74 3E                           je 0x1402e5da3
002E5D65  41 F6 46 04 01                  test byte ptr [r14 + 4], 1
002E5D6A  74 37                           je 0x1402e5da3
002E5D6C  8B C2                           mov eax, edx
002E5D6E  48 C1 E0 04                     shl rax, 4
002E5D72  48 03 C7                        add rax, rdi
002E5D75  48 8D 88 FF 0F 00 00            lea rcx, [rax + 0xfff]
002E5D7C  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
002E5D83  48 2B C8                        sub rcx, rax
002E5D86  48 C1 E9 04                     shr rcx, 4
002E5D8A  8B C1                           mov eax, ecx
002E5D8C  C1 E0 04                        shl eax, 4
002E5D8F  83 F8 20                        cmp eax, 0x20
002E5D92  0F 82 38 0D 00 00               jb 0x1402e6ad0
002E5D98  A9 C0 FF FF FF                  test eax, 0xffffffc0
002E5D9D  0F 84 1C 08 00 00               je 0x1402e65bf
002E5DA3  45 8D 0C 17                     lea r9d, [r15 + rdx]
002E5DA7  48 89 9C 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rbx
002E5DAF  41 8B C7                        mov eax, r15d
002E5DB2  C7 84 24 A4 00 00 00 00 00 01 00  mov dword ptr [rsp + 0xa4], 0x10000
002E5DBD  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
002E5DC5  44 8B D3                        mov r10d, ebx
002E5DC8  C1 E0 04                        shl eax, 4
002E5DCB  45 8B C3                        mov r8d, r11d
002E5DCE  83 F8 20                        cmp eax, 0x20
002E5DD1  48 8B 05 28 25 B4 00            mov rax, qword ptr [rip + 0xb42528]
002E5DD8  44 0F 43 CA                     cmovae r9d, edx
002E5DDC  45 0F 43 D7                     cmovae r10d, r15d
002E5DE0  48 C1 E8 20                     shr rax, 0x20
002E5DE4  41 8B D1                        mov edx, r9d
002E5DE7  C1 E8 10                        shr eax, 0x10
002E5DEA  45 8B E1                        mov r12d, r9d
002E5DED  48 C1 E9 20                     shr rcx, 0x20
002E5DF1  C1 E9 10                        shr ecx, 0x10
002E5DF4  32 C8                           xor cl, al
002E5DF6  C1 E2 04                        shl edx, 4
002E5DF9  41 C1 E8 0C                     shr r8d, 0xc
002E5DFD  48 8B C7                        mov rax, rdi
002E5E00  48 C1 E8 20                     shr rax, 0x20
002E5E04  C1 E8 10                        shr eax, 0x10
002E5E07  32 C8                           xor cl, al
002E5E09  44 89 4C 24 34                  mov dword ptr [rsp + 0x34], r9d
002E5E0E  88 4F 06                        mov byte ptr [rdi + 6], cl
002E5E11  8B C6                           mov eax, esi
002E5E13  41 33 C0                        xor eax, r8d
002E5E16  44 89 94 24 B0 00 00 00         mov dword ptr [rsp + 0xb0], r10d
002E5E1E  33 05 DC 24 B4 00               xor eax, dword ptr [rip + 0xb424dc]
002E5E24  B9 3F 00 00 00                  mov ecx, 0x3f
002E5E29  0F B6 C0                        movzx eax, al
002E5E2C  45 85 D2                        test r10d, r10d
002E5E2F  89 84 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], eax
002E5E36  89 47 08                        mov dword ptr [rdi + 8], eax
002E5E39  8D 42 20                        lea eax, [rdx + 0x20]
002E5E3C  0F 44 C2                        cmove eax, edx
002E5E3F  44 89 8C 24 C0 00 00 00         mov dword ptr [rsp + 0xc0], r9d
002E5E47  41 8D 53 FF                     lea edx, [r11 - 1]
002E5E4B  03 D0                           add edx, eax
002E5E4D  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
002E5E54  4C 8B F8                        mov r15, rax
002E5E57  48 C1 EA 0C                     shr rdx, 0xc
002E5E5B  2A CA                           sub cl, dl
002E5E5D  49 D3 EF                        shr r15, cl
002E5E60  41 8B C8                        mov ecx, r8d
002E5E63  48 D3 E0                        shl rax, cl
002E5E66  45 8B C2                        mov r8d, r10d
002E5E69  4C 23 F8                        and r15, rax
002E5E6C  49 8B C7                        mov rax, r15
002E5E6F  49 33 45 10                     xor rax, qword ptr [r13 + 0x10]
002E5E73  4C 23 F8                        and r15, rax
002E5E76  0F 85 AD 09 00 00               jne 0x1402e6829
002E5E7C  C1 EE 10                        shr esi, 0x10
002E5E7F  66 41 33 F4                     xor si, r12w
002E5E83  66 33 35 78 24 B4 00            xor si, word ptr [rip + 0xb42478]
002E5E8A  66 89 77 02                     mov word ptr [rdi + 2], si
002E5E8E  45 85 C0                        test r8d, r8d
002E5E91  75 14                           jne 0x1402e5ea7
002E5E93  41 8B C4                        mov eax, r12d
002E5E96  48 83 C4 60                     add rsp, 0x60
002E5E9A  41 5F                           pop r15
002E5E9C  41 5E                           pop r14
002E5E9E  41 5D                           pop r13
002E5EA0  41 5C                           pop r12
002E5EA2  5F                              pop rdi
002E5EA3  5E                              pop rsi
002E5EA4  5B                              pop rbx
002E5EA5  C3                              ret
002E5EA6  CC                              int3
002E5EA7  41 8B C4                        mov eax, r12d
002E5EAA  48 C1 E0 04                     shl rax, 4
002E5EAE  48 03 F8                        add rdi, rax
002E5EB1  45 85 E4                        test r12d, r12d
002E5EB4  0F 84 94 0C 00 00               je 0x1402e6b4e
002E5EBA  0F B7 C3                        movzx eax, bx
002E5EBD  41 8B C8                        mov ecx, r8d
002E5EC0  C1 E1 10                        shl ecx, 0x10
002E5EC3  41 0F B7 D4                     movzx edx, r12w
002E5EC7  48 0F BA EA 10                  bts rdx, 0x10
002E5ECC  48 C1 E2 20                     shl rdx, 0x20
002E5ED0  48 0B D0                        or rdx, rax
002E5ED3  48 0B D1                        or rdx, rcx
002E5ED6  8B CF                           mov ecx, edi
002E5ED8  48 33 15 21 24 B4 00            xor rdx, qword ptr [rip + 0xb42421]
002E5EDF  41 2B CD                        sub ecx, r13d
002E5EE2  48 33 D7                        xor rdx, rdi
002E5EE5  C1 E9 0C                        shr ecx, 0xc
002E5EE8  48 89 17                        mov qword ptr [rdi], rdx
002E5EEB  33 CF                           xor ecx, edi
002E5EED  33 0D 0D 24 B4 00               xor ecx, dword ptr [rip + 0xb4240d]
002E5EF3  0F B6 C1                        movzx eax, cl
002E5EF6  89 47 08                        mov dword ptr [rdi + 8], eax
002E5EF9  41 0F B7 45 20                  movzx eax, word ptr [r13 + 0x20]
002E5EFE  48 83 C0 03                     add rax, 3
002E5F02  41 8B D0                        mov edx, r8d
002E5F05  48 C1 E0 04                     shl rax, 4
002E5F09  48 C1 E2 04                     shl rdx, 4
002E5F0D  49 03 C5                        add rax, r13
002E5F10  48 03 D7                        add rdx, rdi
002E5F13  48 3B D0                        cmp rdx, rax
002E5F16  73 3B                           jae 0x1402e5f53
002E5F18  41 0F B7 C0                     movzx eax, r8w
002E5F1C  48 89 9C 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rbx
002E5F24  89 84 24 A4 00 00 00            mov dword ptr [rsp + 0xa4], eax
002E5F2B  48 8B 05 CE 23 B4 00            mov rax, qword ptr [rip + 0xb423ce]
002E5F32  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
002E5F3A  48 C1 E8 20                     shr rax, 0x20
002E5F3E  48 C1 E9 20                     shr rcx, 0x20
002E5F42  66 33 C8                        xor cx, ax
002E5F45  48 8B C2                        mov rax, rdx
002E5F48  48 C1 E8 20                     shr rax, 0x20
002E5F4C  66 33 C8                        xor cx, ax
002E5F4F  66 89 4A 04                     mov word ptr [rdx + 4], cx
002E5F53  89 9C 24 B0 00 00 00            mov dword ptr [rsp + 0xb0], ebx
002E5F5A  4D 8D 4D 30                     lea r9, [r13 + 0x30]
002E5F5E  66 90                           nop
002E5F60  48 8B 15 99 23 B4 00            mov rdx, qword ptr [rip + 0xb42399]
002E5F67  48 8B C7                        mov rax, rdi
002E5F6A  48 33 07                        xor rax, qword ptr [rdi]
002E5F6D  48 8B CB                        mov rcx, rbx
002E5F70  48 33 C2                        xor rax, rdx
002E5F73  48 C1 E9 20                     shr rcx, 0x20
002E5F77  44 8B E0                        mov r12d, eax
002E5F7A  C1 E9 10                        shr ecx, 0x10
002E5F7D  48 C1 E8 20                     shr rax, 0x20
002E5F81  44 0F B7 C0                     movzx r8d, ax
002E5F85  48 8B C7                        mov rax, rdi
002E5F88  41 C1 EC 10                     shr r12d, 0x10
002E5F8C  48 C1 E8 20                     shr rax, 0x20
002E5F90  45 8B FC                        mov r15d, r12d
002E5F93  C1 E8 10                        shr eax, 0x10
002E5F96  48 C1 EA 20                     shr rdx, 0x20
002E5F9A  32 C8                           xor cl, al
002E5F9C  C1 EA 10                        shr edx, 0x10
002E5F9F  32 CA                           xor cl, dl
002E5FA1  44 89 A4 24 A0 00 00 00         mov dword ptr [rsp + 0xa0], r12d
002E5FA9  88 4F 06                        mov byte ptr [rdi + 6], cl
002E5FAC  45 85 C0                        test r8d, r8d
002E5FAF  0F 84 ED 00 00 00               je 0x1402e60a2
002E5FB5  41 8B C0                        mov eax, r8d
002E5FB8  4C 8B E7                        mov r12, rdi
002E5FBB  48 C1 E0 04                     shl rax, 4
002E5FBF  4C 2B E0                        sub r12, rax
002E5FC2  49 8B F4                        mov rsi, r12
002E5FC5  49 33 34 24                     xor rsi, qword ptr [r12]
002E5FC9  48 33 35 30 23 B4 00            xor rsi, qword ptr [rip + 0xb42330]
002E5FD0  48 8B C6                        mov rax, rsi
002E5FD3  48 C1 E8 20                     shr rax, 0x20
002E5FD7  A9 00 00 FF 00                  test eax, 0xff0000
002E5FDC  0F 85 40 0B 00 00               jne 0x1402e6b22
002E5FE2  48 8B 8C 24 A8 00 00 00         mov rcx, qword ptr [rsp + 0xa8]
002E5FEA  49 8D 54 24 08                  lea rdx, [r12 + 8]
002E5FEF  48 83 C1 10                     add rcx, 0x10
002E5FF3  E8 18 EC FF FF                  call 0x1402e4c10
002E5FF8  0F B7 05 03 23 B4 00            movzx eax, word ptr [rip + 0xb42303]
002E5FFF  41 8B D4                        mov edx, r12d
002E6002  45 8B 0C 24                     mov r9d, dword ptr [r12]
002E6006  41 2B D5                        sub edx, r13d
002E6009  4D 0F BF 5E 06                  movsx r11, word ptr [r14 + 6]
002E600E  81 C2 1F 10 00 00               add edx, 0x101f
002E6014  81 E2 00 F0 FF FF               and edx, 0xfffff000
002E601A  41 8B C9                        mov ecx, r9d
002E601D  41 33 CC                        xor ecx, r12d
002E6020  45 8B D4                        mov r10d, r12d
002E6023  C1 E9 10                        shr ecx, 0x10
002E6026  33 C8                           xor ecx, eax
002E6028  C1 E1 04                        shl ecx, 4
002E602B  44 8B C1                        mov r8d, ecx
002E602E  41 2B CD                        sub ecx, r13d
002E6031  41 03 CC                        add ecx, r12d
002E6034  81 E1 00 F0 FF FF               and ecx, 0xfffff000
002E603A  8B C1                           mov eax, ecx
002E603C  2B C2                           sub eax, edx
002E603E  3B D1                           cmp edx, ecx
002E6040  0F 43 C3                        cmovae eax, ebx
002E6043  45 33 CC                        xor r9d, r12d
002E6046  44 33 0D B3 22 B4 00            xor r9d, dword ptr [rip + 0xb422b3]
002E604D  41 81 E2 FF 0F 00 00            and r10d, 0xfff
002E6054  C1 E8 0C                        shr eax, 0xc
002E6057  41 0F B7 C9                     movzx ecx, r9w
002E605B  2B C8                           sub ecx, eax
002E605D  49 8D 80 FF 0F 00 00            lea rax, [r8 + 0xfff]
002E6064  49 03 C2                        add rax, r10
002E6067  48 C1 E8 0C                     shr rax, 0xc
002E606B  2B C8                           sub ecx, eax
002E606D  49 8D 80 FF 0F 00 00            lea rax, [r8 + 0xfff]
002E6074  48 C1 E8 0C                     shr rax, 0xc
002E6078  03 C8                           add ecx, eax
002E607A  48 63 D1                        movsxd rdx, ecx
002E607D  66 45 85 DB                     test r11w, r11w
002E6081  0F 84 EF 0A 00 00               je 0x1402e6b76
002E6087  F0 4B 01 54 33 20               lock add qword ptr [r11 + r14 + 0x20], rdx
002E608D  C1 EE 10                        shr esi, 0x10
002E6090  4D 8D 4D 30                     lea r9, [r13 + 0x30]
002E6094  49 8B FC                        mov rdi, r12
002E6097  44 03 FE                        add r15d, esi
002E609A  44 8B A4 24 A0 00 00 00         mov r12d, dword ptr [rsp + 0xa0]
002E60A2  41 0F B7 4D 20                  movzx ecx, word ptr [r13 + 0x20]
002E60A7  8B C1                           mov eax, ecx
002E60A9  41 8B F7                        mov esi, r15d
002E60AC  48 C1 E0 04                     shl rax, 4
002E60B0  48 C1 E6 04                     shl rsi, 4
002E60B4  49 03 C1                        add rax, r9
002E60B7  48 03 F7                        add rsi, rdi
002E60BA  48 3B F0                        cmp rsi, rax
002E60BD  0F 83 DF 00 00 00               jae 0x1402e61a2
002E60C3  48 8B C6                        mov rax, rsi
002E60C6  48 33 06                        xor rax, qword ptr [rsi]
002E60C9  48 33 05 30 22 B4 00            xor rax, qword ptr [rip + 0xb42230]
002E60D0  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
002E60D8  48 C1 E8 20                     shr rax, 0x20
002E60DC  A9 00 00 FF 00                  test eax, 0xff0000
002E60E1  0F 85 BB 00 00 00               jne 0x1402e61a2
002E60E7  48 8B 8C 24 A8 00 00 00         mov rcx, qword ptr [rsp + 0xa8]
002E60EF  48 8D 56 08                     lea rdx, [rsi + 8]
002E60F3  48 83 C1 10                     add rcx, 0x10
002E60F7  E8 14 EB FF FF                  call 0x1402e4c10
002E60FC  44 8B 0E                        mov r9d, dword ptr [rsi]
002E60FF  8B D6                           mov edx, esi
002E6101  0F B7 05 FA 21 B4 00            movzx eax, word ptr [rip + 0xb421fa]
002E6108  41 2B D5                        sub edx, r13d
002E610B  4D 0F BF 5E 06                  movsx r11, word ptr [r14 + 6]
002E6110  81 C2 1F 10 00 00               add edx, 0x101f
002E6116  81 E2 00 F0 FF FF               and edx, 0xfffff000
002E611C  44 8B D6                        mov r10d, esi
002E611F  41 8B C9                        mov ecx, r9d
002E6122  33 CE                           xor ecx, esi
002E6124  C1 E9 10                        shr ecx, 0x10
002E6127  33 C8                           xor ecx, eax
002E6129  C1 E1 04                        shl ecx, 4
002E612C  44 8B C1                        mov r8d, ecx
002E612F  41 2B CD                        sub ecx, r13d
002E6132  03 CE                           add ecx, esi
002E6134  81 E1 00 F0 FF FF               and ecx, 0xfffff000
002E613A  8B C1                           mov eax, ecx
002E613C  2B C2                           sub eax, edx
002E613E  3B D1                           cmp edx, ecx
002E6140  0F 43 C3                        cmovae eax, ebx
002E6143  33 35 B7 21 B4 00               xor esi, dword ptr [rip + 0xb421b7]
002E6149  C1 E8 0C                        shr eax, 0xc
002E614C  41 33 F1                        xor esi, r9d
002E614F  41 81 E2 FF 0F 00 00            and r10d, 0xfff
002E6156  0F B7 CE                        movzx ecx, si
002E6159  2B C8                           sub ecx, eax
002E615B  49 8D 80 FF 0F 00 00            lea rax, [r8 + 0xfff]
002E6162  49 03 C2                        add rax, r10
002E6165  48 C1 E8 0C                     shr rax, 0xc
002E6169  2B C8                           sub ecx, eax
002E616B  49 8D 80 FF 0F 00 00            lea rax, [r8 + 0xfff]
002E6172  48 C1 E8 0C                     shr rax, 0xc
002E6176  03 C8                           add ecx, eax
002E6178  48 63 D1                        movsxd rdx, ecx
002E617B  66 45 85 DB                     test r11w, r11w
002E617F  0F 84 FA 09 00 00               je 0x1402e6b7f
002E6185  F0 4B 01 54 33 20               lock add qword ptr [r11 + r14 + 0x20], rdx
002E618B  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
002E6193  4D 8D 4D 30                     lea r9, [r13 + 0x30]
002E6197  41 0F B7 4D 20                  movzx ecx, word ptr [r13 + 0x20]
002E619C  C1 E8 10                        shr eax, 0x10
002E619F  44 03 F8                        add r15d, eax
002E61A2  41 F6 46 04 01                  test byte ptr [r14 + 4], 1
002E61A7  0F 84 0F 01 00 00               je 0x1402e62bc
002E61AD  41 8B D7                        mov edx, r15d
002E61B0  48 C1 E2 04                     shl rdx, 4
002E61B4  48 03 D7                        add rdx, rdi
002E61B7  0F B7 C1                        movzx eax, cx
002E61BA  48 C1 E0 04                     shl rax, 4
002E61BE  49 03 C1                        add rax, r9
002E61C1  48 89 94 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rdx
002E61C9  48 3B D0                        cmp rdx, rax
002E61CC  0F 83 EA 00 00 00               jae 0x1402e62bc
002E61D2  48 8B F2                        mov rsi, rdx
002E61D5  48 33 32                        xor rsi, qword ptr [rdx]
002E61D8  48 33 35 21 21 B4 00            xor rsi, qword ptr [rip + 0xb42121]
002E61DF  48 8B C6                        mov rax, rsi
002E61E2  48 C1 E8 20                     shr rax, 0x20
002E61E6  A9 00 00 FF 00                  test eax, 0xff0000
002E61EB  0F 85 CB 00 00 00               jne 0x1402e62bc
002E61F1  48 8B 8C 24 A8 00 00 00         mov rcx, qword ptr [rsp + 0xa8]
002E61F9  48 83 C2 08                     add rdx, 8
002E61FD  48 83 C1 10                     add rcx, 0x10
002E6201  E8 0A EA FF FF                  call 0x1402e4c10
002E6206  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
002E620E  0F B7 15 ED 20 B4 00            movzx edx, word ptr [rip + 0xb420ed]
002E6215  44 8B C0                        mov r8d, eax
002E6218  44 8B D8                        mov r11d, eax
002E621B  45 2B C5                        sub r8d, r13d
002E621E  41 81 C0 1F 10 00 00            add r8d, 0x101f
002E6225  44 8B 10                        mov r10d, dword ptr [rax]
002E6228  41 81 E0 00 F0 FF FF            and r8d, 0xfffff000
002E622F  45 8B CA                        mov r9d, r10d
002E6232  41 8B CA                        mov ecx, r10d
002E6235  33 C8                           xor ecx, eax
002E6237  44 33 C8                        xor r9d, eax
002E623A  C1 E9 10                        shr ecx, 0x10
002E623D  33 CA                           xor ecx, edx
002E623F  41 C1 E9 10                     shr r9d, 0x10
002E6243  C1 E1 04                        shl ecx, 4
002E6246  44 33 CA                        xor r9d, edx
002E6249  49 0F BF 56 06                  movsx rdx, word ptr [r14 + 6]
002E624E  41 2B CD                        sub ecx, r13d
002E6251  03 C8                           add ecx, eax
002E6253  41 C1 E1 04                     shl r9d, 4
002E6257  81 E1 00 F0 FF FF               and ecx, 0xfffff000
002E625D  8B C1                           mov eax, ecx
002E625F  41 2B C0                        sub eax, r8d
002E6262  44 3B C1                        cmp r8d, ecx
002E6265  0F 43 C3                        cmovae eax, ebx
002E6268  44 33 94 24 A0 00 00 00         xor r10d, dword ptr [rsp + 0xa0]
002E6270  44 33 15 89 20 B4 00            xor r10d, dword ptr [rip + 0xb42089]
002E6277  41 81 E3 FF 0F 00 00            and r11d, 0xfff
002E627E  C1 E8 0C                        shr eax, 0xc
002E6281  41 0F B7 CA                     movzx ecx, r10w
002E6285  2B C8                           sub ecx, eax
002E6287  49 8D 83 FF 0F 00 00            lea rax, [r11 + 0xfff]
002E628E  49 03 C1                        add rax, r9
002E6291  48 C1 E8 0C                     shr rax, 0xc
002E6295  2B C8                           sub ecx, eax
002E6297  49 8D 81 FF 0F 00 00            lea rax, [r9 + 0xfff]
002E629E  48 C1 E8 0C                     shr rax, 0xc
002E62A2  03 C8                           add ecx, eax
002E62A4  4C 63 C1                        movsxd r8, ecx
002E62A7  66 85 D2                        test dx, dx
002E62AA  0F 84 D8 08 00 00               je 0x1402e6b88
002E62B0  F0 4E 01 44 32 20               lock add qword ptr [rdx + r14 + 0x20], r8
002E62B6  C1 EE 10                        shr esi, 0x10
002E62B9  44 03 FE                        add r15d, esi
002E62BC  45 3B E7                        cmp r12d, r15d
002E62BF  0F 85 96 04 00 00               jne 0x1402e675b
002E62C5  41 0F B7 45 20                  movzx eax, word ptr [r13 + 0x20]
002E62CA  44 3B F8                        cmp r15d, eax
002E62CD  0F 84 07 08 00 00               je 0x1402e6ada
002E62D3  44 3B BC 24 B0 00 00 00         cmp r15d, dword ptr [rsp + 0xb0]
002E62DB  0F 87 F1 02 00 00               ja 0x1402e65d2
002E62E1  41 F6 46 04 01                  test byte ptr [r14 + 4], 1
002E62E6  0F 84 81 01 00 00               je 0x1402e646d
002E62EC  48 8D 47 20                     lea rax, [rdi + 0x20]
002E62F0  48 A9 FF 0F 00 00               test rax, 0xfff
002E62F6  0F 84 71 01 00 00               je 0x1402e646d
002E62FC  0F B7 57 02                     movzx edx, word ptr [rdi + 2]
002E6300  4C 8D 8F 0F 10 00 00            lea r9, [rdi + 0x100f]
002E6307  44 0F B7 05 F3 1F B4 00         movzx r8d, word ptr [rip + 0xb41ff3]
002E630F  8B C7                           mov eax, edi
002E6311  C1 E8 10                        shr eax, 0x10
002E6314  49 81 E1 00 F0 FF FF            and r9, 0xfffffffffffff000
002E631B  33 D0                           xor edx, eax
002E631D  49 8B C1                        mov rax, r9
002E6320  41 33 D0                        xor edx, r8d
002E6323  48 2B C7                        sub rax, rdi
002E6326  8B CA                           mov ecx, edx
002E6328  48 C1 E1 04                     shl rcx, 4
002E632C  48 3B C1                        cmp rax, rcx
002E632F  0F 82 B0 06 00 00               jb 0x1402e69e5
002E6335  4C 8B CB                        mov r9, rbx
002E6338  4D 85 C9                        test r9, r9
002E633B  0F 84 2C 01 00 00               je 0x1402e646d
002E6341  41 0F B7 49 02                  movzx ecx, word ptr [r9 + 2]
002E6346  41 8B C1                        mov eax, r9d
002E6349  C1 E8 10                        shr eax, 0x10
002E634C  45 8B D9                        mov r11d, r9d
002E634F  33 C8                           xor ecx, eax
002E6351  41 81 E3 FF 0F 00 00            and r11d, 0xfff
002E6358  0F B7 05 A3 1F B4 00            movzx eax, word ptr [rip + 0xb41fa3]
002E635F  49 81 C3 FF 0F 00 00            add r11, 0xfff
002E6366  33 C8                           xor ecx, eax
002E6368  45 8B D1                        mov r10d, r9d
002E636B  C1 E1 04                        shl ecx, 4
002E636E  45 2B D5                        sub r10d, r13d
002E6371  44 8B C1                        mov r8d, ecx
002E6374  41 81 C2 1F 10 00 00            add r10d, 0x101f
002E637B  4D 03 D8                        add r11, r8
002E637E  41 81 E2 00 F0 FF FF            and r10d, 0xfffff000
002E6385  45 2B C5                        sub r8d, r13d
002E6388  49 C1 EB 0C                     shr r11, 0xc
002E638C  45 03 C1                        add r8d, r9d
002E638F  48 8D 81 FF 0F 00 00            lea rax, [rcx + 0xfff]
002E6396  48 C1 E8 0C                     shr rax, 0xc
002E639A  41 81 E0 00 F0 FF FF            and r8d, 0xfffff000
002E63A1  44 2B D8                        sub r11d, eax
002E63A4  49 C7 C7 FF FF FF FF            mov r15, 0xffffffffffffffff
002E63AB  45 3B D0                        cmp r10d, r8d
002E63AE  0F 82 DA 06 00 00               jb 0x1402e6a8e
002E63B4  8B D3                           mov edx, ebx
002E63B6  4C 8B C3                        mov r8, rbx
002E63B9  49 0F BF 46 06                  movsx rax, word ptr [r14 + 6]
002E63BE  F3 49 0F B8 C8                  popcnt rcx, r8
002E63C3  C1 EA 0C                        shr edx, 0xc
002E63C6  4C 63 C1                        movsxd r8, ecx
002E63C9  66 85 C0                        test ax, ax
002E63CC  0F 84 BF 07 00 00               je 0x1402e6b91
002E63D2  F0 4E 01 44 30 20               lock add qword ptr [rax + r14 + 0x20], r8
002E63D8  4C 8B A4 24 A8 00 00 00         mov r12, qword ptr [rsp + 0xa8]
002E63E0  66 2B D1                        sub dx, cx
002E63E3  66 41 03 D3                     add dx, r11w
002E63E7  41 8B C9                        mov ecx, r9d
002E63EA  66 41 33 D1                     xor dx, r9w
002E63EE  66 33 15 0B 1F B4 00            xor dx, word ptr [rip + 0xb41f0b]
002E63F5  66 41 89 11                     mov word ptr [r9], dx
002E63F9  41 33 09                        xor ecx, dword ptr [r9]
002E63FC  4C 8B 15 FD 1E B4 00            mov r10, qword ptr [rip + 0xb41efd]
002E6403  49 8B 44 24 18                  mov rax, qword ptr [r12 + 0x18]
002E6408  41 33 CA                        xor ecx, r10d
002E640B  A8 01                           test al, 1
002E640D  0F 85 FE 06 00 00               jne 0x1402e6b11
002E6413  4D 8B 5C 24 10                  mov r11, qword ptr [r12 + 0x10]
002E6418  44 0F B6 C0                     movzx r8d, al
002E641C  49 8B D3                        mov rdx, r11
002E641F  41 83 E0 01                     and r8d, 1
002E6423  32 C0                           xor al, al
002E6425  4D 85 DB                        test r11, r11
002E6428  74 2F                           je 0x1402e6459
002E642A  66 0F 1F 44 00 00               nop word ptr [rax + rax]
002E6430  48 8D 42 F8                     lea rax, [rdx - 8]
002E6434  33 00                           xor eax, dword ptr [rax]
002E6436  41 33 C2                        xor eax, r10d
002E6439  3B C8                           cmp ecx, eax
002E643B  0F 82 91 03 00 00               jb 0x1402e67d2
002E6441  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
002E6445  45 85 C0                        test r8d, r8d
002E6448  0F 84 89 05 00 00               je 0x1402e69d7
002E644E  48 85 C0                        test rax, rax
002E6451  0F 85 7D 05 00 00               jne 0x1402e69d4
002E6457  B0 01                           mov al, 1
002E6459  49 83 C1 08                     add r9, 8
002E645D  49 8D 4C 24 10                  lea rcx, [r12 + 0x10]
002E6462  44 0F B6 C0                     movzx r8d, al
002E6466  E8 05 E1 FF FF                  call 0x1402e4570
002E646B  EB 0F                           jmp 0x1402e647c
002E646D  4C 8B A4 24 A8 00 00 00         mov r12, qword ptr [rsp + 0xa8]
002E6475  49 C7 C7 FF FF FF FF            mov r15, 0xffffffffffffffff
002E647C  0F B7 4F 02                     movzx ecx, word ptr [rdi + 2]
002E6480  8B C7                           mov eax, edi
002E6482  C1 E8 10                        shr eax, 0x10
002E6485  44 8B D7                        mov r10d, edi
002E6488  33 C8                           xor ecx, eax
002E648A  41 81 E2 FF 0F 00 00            and r10d, 0xfff
002E6491  0F B7 05 6A 1E B4 00            movzx eax, word ptr [rip + 0xb41e6a]
002E6498  49 81 C2 FF 0F 00 00            add r10, 0xfff
002E649F  33 C8                           xor ecx, eax
002E64A1  44 8B CF                        mov r9d, edi
002E64A4  C1 E1 04                        shl ecx, 4
002E64A7  45 2B CD                        sub r9d, r13d
002E64AA  44 8B C1                        mov r8d, ecx
002E64AD  41 81 C1 1F 10 00 00            add r9d, 0x101f
002E64B4  4D 03 D0                        add r10, r8
002E64B7  41 81 E1 00 F0 FF FF            and r9d, 0xfffff000
002E64BE  45 2B C5                        sub r8d, r13d
002E64C1  49 C1 EA 0C                     shr r10, 0xc
002E64C5  44 03 C7                        add r8d, edi
002E64C8  48 8D 81 FF 0F 00 00            lea rax, [rcx + 0xfff]
002E64CF  48 C1 E8 0C                     shr rax, 0xc
002E64D3  41 81 E0 00 F0 FF FF            and r8d, 0xfffff000
002E64DA  44 2B D0                        sub r10d, eax
002E64DD  45 3B C8                        cmp r9d, r8d
002E64E0  0F 82 11 03 00 00               jb 0x1402e67f7
002E64E6  48 8B C3                        mov rax, rbx
002E64E9  F3 48 0F B8 C8                  popcnt rcx, rax
002E64EE  49 0F BF 46 06                  movsx rax, word ptr [r14 + 6]
002E64F3  C1 EB 0C                        shr ebx, 0xc
002E64F6  48 63 D1                        movsxd rdx, ecx
002E64F9  66 85 C0                        test ax, ax
002E64FC  0F 84 6B 06 00 00               je 0x1402e6b6d
002E6502  F0 4A 01 54 30 20               lock add qword ptr [rax + r14 + 0x20], rdx
002E6508  66 2B D9                        sub bx, cx
002E650B  8B CF                           mov ecx, edi
002E650D  66 41 03 DA                     add bx, r10w
002E6511  4D 8D 54 24 10                  lea r10, [r12 + 0x10]
002E6516  66 33 DF                        xor bx, di
002E6519  66 33 1D E0 1D B4 00            xor bx, word ptr [rip + 0xb41de0]
002E6520  66 89 1F                        mov word ptr [rdi], bx
002E6523  33 0F                           xor ecx, dword ptr [rdi]
002E6525  4C 8B 05 D4 1D B4 00            mov r8, qword ptr [rip + 0xb41dd4]
002E652C  49 8B 42 08                     mov rax, qword ptr [r10 + 8]
002E6530  41 33 C8                        xor ecx, r8d
002E6533  49 8B 12                        mov rdx, qword ptr [r10]
002E6536  A8 01                           test al, 1
002E6538  0F 85 BF 05 00 00               jne 0x1402e6afd
002E653E  44 0F B6 C8                     movzx r9d, al
002E6542  32 C0                           xor al, al
002E6544  41 83 E1 01                     and r9d, 1
002E6548  48 85 D2                        test rdx, rdx
002E654B  74 28                           je 0x1402e6575
002E654D  0F 1F 00                        nop dword ptr [rax]
002E6550  48 8D 42 F8                     lea rax, [rdx - 8]
002E6554  33 00                           xor eax, dword ptr [rax]
002E6556  41 33 C0                        xor eax, r8d
002E6559  3B C8                           cmp ecx, eax
002E655B  72 40                           jb 0x1402e659d
002E655D  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
002E6561  45 85 C9                        test r9d, r9d
002E6564  0F 84 E3 01 00 00               je 0x1402e674d
002E656A  48 85 C0                        test rax, rax
002E656D  0F 85 D7 01 00 00               jne 0x1402e674a
002E6573  B0 01                           mov al, 1
002E6575  4C 8D 4F 08                     lea r9, [rdi + 8]
002E6579  44 0F B6 C0                     movzx r8d, al
002E657D  49 8B CA                        mov rcx, r10
002E6580  E8 EB DF FF FF                  call 0x1402e4570
002E6585  8B 84 24 C0 00 00 00            mov eax, dword ptr [rsp + 0xc0]
002E658C  48 83 C4 60                     add rsp, 0x60
002E6590  41 5F                           pop r15
002E6592  41 5E                           pop r14
002E6594  41 5D                           pop r13
002E6596  41 5C                           pop r12
002E6598  5F                              pop rdi
002E6599  5E                              pop rsi
002E659A  5B                              pop rbx
002E659B  C3                              ret
002E659C  CC                              int3
002E659D  48 8B 02                        mov rax, qword ptr [rdx]
002E65A0  45 85 C9                        test r9d, r9d
002E65A3  74 0C                           je 0x1402e65b1
002E65A5  48 85 C0                        test rax, rax
002E65A8  0F 84 54 05 00 00               je 0x1402e6b02
002E65AE  48 33 C2                        xor rax, rdx
002E65B1  48 85 C0                        test rax, rax
002E65B4  0F 84 48 05 00 00               je 0x1402e6b02
002E65BA  48 8B D0                        mov rdx, rax
002E65BD  EB 91                           jmp 0x1402e6550
002E65BF  83 F8 20                        cmp eax, 0x20
002E65C2  0F 84 DB F7 FF FF               je 0x1402e5da3
002E65C8  FF C2                           inc edx
002E65CA  41 FF CF                        dec r15d
002E65CD  E9 D1 F7 FF FF                  jmp 0x1402e5da3
002E65D2  44 0F B7 47 02                  movzx r8d, word ptr [rdi + 2]
002E65D7  8B C7                           mov eax, edi
002E65D9  C1 E8 10                        shr eax, 0x10
002E65DC  44 8B E7                        mov r12d, edi
002E65DF  44 33 C0                        xor r8d, eax
002E65E2  45 2B E5                        sub r12d, r13d
002E65E5  0F B7 05 16 1D B4 00            movzx eax, word ptr [rip + 0xb41d16]
002E65EC  44 33 C0                        xor r8d, eax
002E65EF  41 C1 E0 04                     shl r8d, 4
002E65F3  45 2B C5                        sub r8d, r13d
002E65F6  45 8D 8C 24 1F 10 00 00         lea r9d, [r12 + 0x101f]
002E65FE  44 03 C7                        add r8d, edi
002E6601  41 81 E1 00 F0 FF FF            and r9d, 0xfffff000
002E6608  41 81 E0 00 F0 FF FF            and r8d, 0xfffff000
002E660F  45 3B C8                        cmp r9d, r8d
002E6612  0F 83 C9 FC FF FF               jae 0x1402e62e1
002E6618  41 8D 40 FF                     lea eax, [r8 - 1]
002E661C  B9 3F 00 00 00                  mov ecx, 0x3f
002E6621  48 C1 E8 0C                     shr rax, 0xc
002E6625  41 8B D0                        mov edx, r8d
002E6628  2A C8                           sub cl, al
002E662A  41 2B D1                        sub edx, r9d
002E662D  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
002E6634  41 C1 E9 0C                     shr r9d, 0xc
002E6638  48 8B F0                        mov rsi, rax
002E663B  48 D3 EE                        shr rsi, cl
002E663E  41 0F B6 C9                     movzx ecx, r9b
002E6642  48 D3 E0                        shl rax, cl
002E6645  48 23 F0                        and rsi, rax
002E6648  49 23 75 10                     and rsi, qword ptr [r13 + 0x10]
002E664C  81 FA 00 10 00 00               cmp edx, 0x1000
002E6652  0F 82 89 FC FF FF               jb 0x1402e62e1
002E6658  48 85 F6                        test rsi, rsi
002E665B  0F 84 80 FC FF FF               je 0x1402e62e1
002E6661  F3 48 0F B8 C6                  popcnt rax, rsi
002E6666  44 8B C0                        mov r8d, eax
002E6669  48 89 84 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rax
002E6671  49 8B D5                        mov rdx, r13
002E6674  49 8B CE                        mov rcx, r14
002E6677  E8 40 F5 FF FF                  call 0x1402e5bbc
002E667C  85 C0                           test eax, eax
002E667E  0F 84 5D FC FF FF               je 0x1402e62e1
002E6684  41 C1 EC 0C                     shr r12d, 0xc
002E6688  48 8B C7                        mov rax, rdi
002E668B  48 C1 E8 20                     shr rax, 0x20
002E668F  44 33 E7                        xor r12d, edi
002E6692  C1 E8 10                        shr eax, 0x10
002E6695  48 89 9C 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rbx
002E669D  C7 84 24 A4 00 00 00 00 00 01 00  mov dword ptr [rsp + 0xa4], 0x10000
002E66A8  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
002E66B0  48 C1 E9 20                     shr rcx, 0x20
002E66B4  C1 E9 10                        shr ecx, 0x10
002E66B7  32 C8                           xor cl, al
002E66B9  48 8B 05 40 1C B4 00            mov rax, qword ptr [rip + 0xb41c40]
002E66C0  48 C1 E8 20                     shr rax, 0x20
002E66C4  C1 E8 10                        shr eax, 0x10
002E66C7  32 C8                           xor cl, al
002E66C9  88 4F 06                        mov byte ptr [rdi + 6], cl
002E66CC  44 33 25 2D 1C B4 00            xor r12d, dword ptr [rip + 0xb41c2d]
002E66D3  41 0F B6 C4                     movzx eax, r12b
002E66D7  0F BA E8 09                     bts eax, 9
002E66DB  89 47 08                        mov dword ptr [rdi + 8], eax
002E66DE  41 F6 46 05 01                  test byte ptr [r14 + 5], 1
002E66E3  75 12                           jne 0x1402e66f7
002E66E5  41 0F B6 4E 03                  movzx ecx, byte ptr [r14 + 3]
002E66EA  48 8B 94 24 C8 00 00 00         mov rdx, qword ptr [rsp + 0xc8]
002E66F2  E8 79 C3 FF FF                  call 0x1402e2a70
002E66F7  44 8B 8C 24 B0 00 00 00         mov r9d, dword ptr [rsp + 0xb0]
002E66FF  4C 8B C6                        mov r8, rsi
002E6702  49 8B D5                        mov rdx, r13
002E6705  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
002E6709  49 8B CE                        mov rcx, r14
002E670C  E8 63 05 00 00                  call 0x1402e6c74
002E6711  41 F6 46 05 01                  test byte ptr [r14 + 5], 1
002E6716  75 1E                           jne 0x1402e6736
002E6718  48 8B 8C 24 A8 00 00 00         mov rcx, qword ptr [rsp + 0xa8]
002E6720  41 0F B6 56 03                  movzx edx, byte ptr [r14 + 3]
002E6725  48 83 C1 08                     add rcx, 8
002E6729  4C 8B 84 24 C8 00 00 00         mov r8, qword ptr [rsp + 0xc8]
002E6731  E8 EA E0 03 00                  call 0x140324820
002E6736  81 67 08 FF FD FF FF            and dword ptr [rdi + 8], 0xfffffdff
002E673D  44 89 BC 24 B0 00 00 00         mov dword ptr [rsp + 0xb0], r15d
002E6745  E9 10 F8 FF FF                  jmp 0x1402e5f5a
002E674A  48 33 C2                        xor rax, rdx
002E674D  48 85 C0                        test rax, rax
002E6750  0F 85 64 FE FF FF               jne 0x1402e65ba
002E6756  E9 18 FE FF FF                  jmp 0x1402e6573
002E675B  8B C7                           mov eax, edi
002E675D  41 8B D7                        mov edx, r15d
002E6760  C1 E8 10                        shr eax, 0x10
002E6763  49 8D 4D 30                     lea rcx, [r13 + 0x30]
002E6767  66 41 33 C7                     xor ax, r15w
002E676B  48 C1 E2 04                     shl rdx, 4
002E676F  66 33 05 8C 1B B4 00            xor ax, word ptr [rip + 0xb41b8c]
002E6776  48 03 D7                        add rdx, rdi
002E6779  66 89 47 02                     mov word ptr [rdi + 2], ax
002E677D  41 0F B7 45 20                  movzx eax, word ptr [r13 + 0x20]
002E6782  48 C1 E0 04                     shl rax, 4
002E6786  48 03 C1                        add rax, rcx
002E6789  48 3B D0                        cmp rdx, rax
002E678C  0F 83 33 FB FF FF               jae 0x1402e62c5
002E6792  41 0F B7 C7                     movzx eax, r15w
002E6796  48 89 9C 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rbx
002E679E  89 84 24 A4 00 00 00            mov dword ptr [rsp + 0xa4], eax
002E67A5  48 8B C2                        mov rax, rdx
002E67A8  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
002E67B0  48 C1 E8 20                     shr rax, 0x20
002E67B4  48 C1 E9 20                     shr rcx, 0x20
002E67B8  66 33 C8                        xor cx, ax
002E67BB  48 8B 05 3E 1B B4 00            mov rax, qword ptr [rip + 0xb41b3e]
002E67C2  48 C1 E8 20                     shr rax, 0x20
002E67C6  66 33 C8                        xor cx, ax
002E67C9  66 89 4A 04                     mov word ptr [rdx + 4], cx
002E67CD  E9 F3 FA FF FF                  jmp 0x1402e62c5
002E67D2  48 8B 02                        mov rax, qword ptr [rdx]
002E67D5  45 85 C0                        test r8d, r8d
002E67D8  74 0C                           je 0x1402e67e6
002E67DA  48 85 C0                        test rax, rax
002E67DD  0F 84 38 03 00 00               je 0x1402e6b1b
002E67E3  48 33 C2                        xor rax, rdx
002E67E6  48 85 C0                        test rax, rax
002E67E9  0F 84 2C 03 00 00               je 0x1402e6b1b
002E67EF  48 8B D0                        mov rdx, rax
002E67F2  E9 39 FC FF FF                  jmp 0x1402e6430
002E67F7  41 8D 40 FF                     lea eax, [r8 - 1]
002E67FB  B9 3F 00 00 00                  mov ecx, 0x3f
002E6800  48 C1 E8 0C                     shr rax, 0xc
002E6804  41 8B D8                        mov ebx, r8d
002E6807  2A C8                           sub cl, al
002E6809  41 2B D9                        sub ebx, r9d
002E680C  49 8B C7                        mov rax, r15
002E680F  41 C1 E9 0C                     shr r9d, 0xc
002E6813  48 D3 E8                        shr rax, cl
002E6816  41 0F B6 C9                     movzx ecx, r9b
002E681A  49 D3 E7                        shl r15, cl
002E681D  49 23 C7                        and rax, r15
002E6820  49 23 45 10                     and rax, qword ptr [r13 + 0x10]
002E6824  E9 C0 FC FF FF                  jmp 0x1402e64e9
002E6829  8B 84 24 A0 00 00 00            mov eax, dword ptr [rsp + 0xa0]
002E6830  4D 8D 66 05                     lea r12, [r14 + 5]
002E6834  0F BA E8 09                     bts eax, 9
002E6838  89 47 08                        mov dword ptr [rdi + 8], eax
002E683B  41 F6 04 24 01                  test byte ptr [r12], 1
002E6840  0F 85 F1 02 00 00               jne 0x1402e6b37
002E6846  41 0F B6 4E 03                  movzx ecx, byte ptr [r14 + 3]
002E684B  48 8B 94 24 C8 00 00 00         mov rdx, qword ptr [rsp + 0xc8]
002E6853  E8 18 C2 FF FF                  call 0x1402e2a70
002E6858  4D 8D 46 05                     lea r8, [r14 + 5]
002E685C  4C 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], r8
002E6864  49 0F BC D7                     bsf rdx, r15
002E6868  F3 49 0F B8 C7                  popcnt rax, r15
002E686D  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
002E6872  44 8B D2                        mov r10d, edx
002E6875  33 C0                           xor eax, eax
002E6877  41 C1 E2 0C                     shl r10d, 0xc
002E687B  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
002E6880  4D 03 D5                        add r10, r13
002E6883  49 0F BD C7                     bsr rax, r15
002E6887  41 BF 01 00 00 00               mov r15d, 1
002E688D  89 94 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], edx
002E6894  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
002E6898  0F 57 C0                        xorps xmm0, xmm0
002E689B  2B C2                           sub eax, edx
002E689D  4C 89 54 24 38                  mov qword ptr [rsp + 0x38], r10
002E68A2  0F 11 44 24 48                  movups xmmword ptr [rsp + 0x48], xmm0
002E68A7  8D 48 01                        lea ecx, [rax + 1]
002E68AA  49 D3 E7                        shl r15, cl
002E68AD  44 8B C1                        mov r8d, ecx
002E68B0  49 FF CF                        dec r15
002E68B3  41 C1 E0 0C                     shl r8d, 0xc
002E68B7  8B CA                           mov ecx, edx
002E68B9  44 89 84 24 C0 00 00 00         mov dword ptr [rsp + 0xc0], r8d
002E68C1  49 D3 E7                        shl r15, cl
002E68C4  41 F6 04 24 01                  test byte ptr [r12], 1
002E68C9  75 20                           jne 0x1402e68eb
002E68CB  41 0F B6 56 03                  movzx edx, byte ptr [r14 + 3]
002E68D0  49 8D 4D 18                     lea rcx, [r13 + 0x18]
002E68D4  4C 8D 44 24 48                  lea r8, [rsp + 0x48]
002E68D9  E8 42 DF 03 00                  call 0x140324820
002E68DE  4C 8B 54 24 38                  mov r10, qword ptr [rsp + 0x38]
002E68E3  44 8B 84 24 C0 00 00 00         mov r8d, dword ptr [rsp + 0xc0]
002E68EB  49 8B 46 20                     mov rax, qword ptr [r14 + 0x20]
002E68EF  48 8D 15 5A EE 03 00            lea rdx, [rip + 0x3ee5a]
002E68F6  48 33 05 03 1A B4 00            xor rax, qword ptr [rip + 0xb41a03]
002E68FD  49 8B CE                        mov rcx, r14
002E6900  49 33 4E 08                     xor rcx, qword ptr [r14 + 8]
002E6904  49 33 C6                        xor rax, r14
002E6907  45 33 C9                        xor r9d, r9d
002E690A  48 3B C2                        cmp rax, rdx
002E690D  49 8B D2                        mov rdx, r10
002E6910  0F 85 2E 02 00 00               jne 0x1402e6b44
002E6916  E8 35 EE 03 00                  call 0x140325750
002E691B  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
002E6923  89 84 24 C0 00 00 00            mov dword ptr [rsp + 0xc0], eax
002E692A  4C 8B E1                        mov r12, rcx
002E692D  85 C0                           test eax, eax
002E692F  0F 88 8E 01 00 00               js 0x1402e6ac3
002E6935  4D 09 7D 10                     or qword ptr [r13 + 0x10], r15
002E6939  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
002E693D  F0 49 01 46 50                  lock add qword ptr [r14 + 0x50], rax
002E6942  44 8B FB                        mov r15d, ebx
002E6945  4D 8D 66 05                     lea r12, [r14 + 5]
002E6949  44 0F B6 01                     movzx r8d, byte ptr [rcx]
002E694D  41 F6 C0 01                     test r8b, 1
002E6951  75 14                           jne 0x1402e6967
002E6953  41 0F B6 4E 03                  movzx ecx, byte ptr [r14 + 3]
002E6958  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
002E695D  E8 0E C1 FF FF                  call 0x1402e2a70
002E6962  45 0F B6 04 24                  movzx r8d, byte ptr [r12]
002E6967  8B 4C 24 34                     mov ecx, dword ptr [rsp + 0x34]
002E696B  44 8B E1                        mov r12d, ecx
002E696E  8B 94 24 B0 00 00 00            mov edx, dword ptr [rsp + 0xb0]
002E6975  89 94 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], edx
002E697C  89 8C 24 C0 00 00 00            mov dword ptr [rsp + 0xc0], ecx
002E6983  45 85 FF                        test r15d, r15d
002E6986  79 14                           jns 0x1402e699c
002E6988  8D 04 11                        lea eax, [rcx + rdx]
002E698B  89 9C 24 C0 00 00 00            mov dword ptr [rsp + 0xc0], ebx
002E6992  89 84 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], eax
002E6999  44 8B E3                        mov r12d, ebx
002E699C  41 F6 C0 01                     test r8b, 1
002E69A0  75 1E                           jne 0x1402e69c0
002E69A2  48 8B 8C 24 A8 00 00 00         mov rcx, qword ptr [rsp + 0xa8]
002E69AA  41 0F B6 56 03                  movzx edx, byte ptr [r14 + 3]
002E69AF  48 83 C1 08                     add rcx, 8
002E69B3  4C 8B 84 24 C8 00 00 00         mov r8, qword ptr [rsp + 0xc8]
002E69BB  E8 60 DE 03 00                  call 0x140324820
002E69C0  81 67 08 FF FD FF FF            and dword ptr [rdi + 8], 0xfffffdff
002E69C7  44 8B 84 24 A0 00 00 00         mov r8d, dword ptr [rsp + 0xa0]
002E69CF  E9 A8 F4 FF FF                  jmp 0x1402e5e7c
002E69D4  48 33 C2                        xor rax, rdx
002E69D7  48 85 C0                        test rax, rax
002E69DA  0F 85 0F FE FF FF               jne 0x1402e67ef
002E69E0  E9 72 FA FF FF                  jmp 0x1402e6457
002E69E5  49 83 C1 E0                     add r9, -0x20
002E69E9  8B C7                           mov eax, edi
002E69EB  C1 E8 10                        shr eax, 0x10
002E69EE  0F 57 C0                        xorps xmm0, xmm0
002E69F1  49 8B C9                        mov rcx, r9
002E69F4  48 2B CF                        sub rcx, rdi
002E69F7  48 C1 F9 04                     sar rcx, 4
002E69FB  66 33 C1                        xor ax, cx
002E69FE  2B D1                           sub edx, ecx
002E6A00  66 41 33 C0                     xor ax, r8w
002E6A04  44 8B C2                        mov r8d, edx
002E6A07  66 89 47 02                     mov word ptr [rdi + 2], ax
002E6A0B  49 8B C1                        mov rax, r9
002E6A0E  41 0F 11 01                     movups xmmword ptr [r9], xmm0
002E6A12  49 C1 E0 04                     shl r8, 4
002E6A16  41 0F 11 41 10                  movups xmmword ptr [r9 + 0x10], xmm0
002E6A1B  66 41 89 51 02                  mov word ptr [r9 + 2], dx
002E6A20  4D 03 C1                        add r8, r9
002E6A23  66 41 89 49 04                  mov word ptr [r9 + 4], cx
002E6A28  49 33 01                        xor rax, qword ptr [r9]
002E6A2B  48 33 05 CE 18 B4 00            xor rax, qword ptr [rip + 0xb418ce]
002E6A32  49 89 01                        mov qword ptr [r9], rax
002E6A35  41 0F B7 45 20                  movzx eax, word ptr [r13 + 0x20]
002E6A3A  48 83 C0 03                     add rax, 3
002E6A3E  48 C1 E0 04                     shl rax, 4
002E6A42  49 03 C5                        add rax, r13
002E6A45  4C 3B C0                        cmp r8, rax
002E6A48  0F 83 EA F8 FF FF               jae 0x1402e6338
002E6A4E  0F B7 C2                        movzx eax, dx
002E6A51  48 89 9C 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rbx
002E6A59  89 84 24 A4 00 00 00            mov dword ptr [rsp + 0xa4], eax
002E6A60  49 8B C0                        mov rax, r8
002E6A63  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
002E6A6B  48 C1 E8 20                     shr rax, 0x20
002E6A6F  48 C1 E9 20                     shr rcx, 0x20
002E6A73  66 33 C8                        xor cx, ax
002E6A76  48 8B 05 83 18 B4 00            mov rax, qword ptr [rip + 0xb41883]
002E6A7D  48 C1 E8 20                     shr rax, 0x20
002E6A81  66 33 C8                        xor cx, ax
002E6A84  66 41 89 48 04                  mov word ptr [r8 + 4], cx
002E6A89  E9 AA F8 FF FF                  jmp 0x1402e6338
002E6A8E  41 8D 40 FF                     lea eax, [r8 - 1]
002E6A92  41 8B D0                        mov edx, r8d
002E6A95  48 C1 E8 0C                     shr rax, 0xc
002E6A99  41 2B D2                        sub edx, r10d
002E6A9C  41 C1 EA 0C                     shr r10d, 0xc
002E6AA0  B9 3F 00 00 00                  mov ecx, 0x3f
002E6AA5  2A C8                           sub cl, al
002E6AA7  4D 8B C7                        mov r8, r15
002E6AAA  49 D3 E8                        shr r8, cl
002E6AAD  49 8B C7                        mov rax, r15
002E6AB0  41 0F B6 CA                     movzx ecx, r10b
002E6AB4  48 D3 E0                        shl rax, cl
002E6AB7  4C 23 C0                        and r8, rax
002E6ABA  4D 23 45 10                     and r8, qword ptr [r13 + 0x10]
002E6ABE  E9 F6 F8 FF FF                  jmp 0x1402e63b9
002E6AC3  44 8B BC 24 C0 00 00 00         mov r15d, dword ptr [rsp + 0xc0]
002E6ACB  E9 79 FE FF FF                  jmp 0x1402e6949
002E6AD0  03 D1                           add edx, ecx
002E6AD2  44 2B F9                        sub r15d, ecx
002E6AD5  E9 C9 F2 FF FF                  jmp 0x1402e5da3
002E6ADA  49 8B D5                        mov rdx, r13
002E6ADD  49 8B CE                        mov rcx, r14
002E6AE0  E8 C3 02 00 00                  call 0x1402e6da8
002E6AE5  8B 84 24 C0 00 00 00            mov eax, dword ptr [rsp + 0xc0]
002E6AEC  48 83 C4 60                     add rsp, 0x60
002E6AF0  41 5F                           pop r15
002E6AF2  41 5E                           pop r14
002E6AF4  41 5D                           pop r13
002E6AF6  41 5C                           pop r12
002E6AF8  5F                              pop rdi
002E6AF9  5E                              pop rsi
002E6AFA  5B                              pop rbx
002E6AFB  C3                              ret
002E6AFC  CC                              int3
002E6AFD  48 85 D2                        test rdx, rdx
002E6B00  75 07                           jne 0x1402e6b09
002E6B02  32 C0                           xor al, al
002E6B04  E9 6C FA FF FF                  jmp 0x1402e6575
002E6B09  49 33 D2                        xor rdx, r10
002E6B0C  E9 2D FA FF FF                  jmp 0x1402e653e
002E6B11  49 8B 54 24 10                  mov rdx, qword ptr [r12 + 0x10]
002E6B16  48 85 D2                        test rdx, rdx
002E6B19  75 0F                           jne 0x1402e6b2a
002E6B1B  32 C0                           xor al, al
002E6B1D  E9 37 F9 FF FF                  jmp 0x1402e6459
002E6B22  45 8B E7                        mov r12d, r15d
002E6B25  E9 78 F5 FF FF                  jmp 0x1402e60a2
002E6B2A  4D 8D 5C 24 10                  lea r11, [r12 + 0x10]
002E6B2F  4C 33 DA                        xor r11, rdx
002E6B32  E9 E1 F8 FF FF                  jmp 0x1402e6418
002E6B37  4C 89 A4 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], r12
002E6B3F  E9 20 FD FF FF                  jmp 0x1402e6864
002E6B44  E8 87 3F 3D 00                  call 0x1406baad0
002E6B49  E9 CD FD FF FF                  jmp 0x1402e691b
002E6B4E  4C 8B 27                        mov r12, qword ptr [rdi]
002E6B51  4C 33 25 A8 17 B4 00            xor r12, qword ptr [rip + 0xb417a8]
002E6B58  4C 33 E7                        xor r12, rdi
002E6B5B  49 C1 EC 20                     shr r12, 0x20
002E6B5F  E9 56 F3 FF FF                  jmp 0x1402e5eba
002E6B64  49 01 4E 58                     add qword ptr [r14 + 0x58], rcx
002E6B68  E9 EC F1 FF FF                  jmp 0x1402e5d59
002E6B6D  49 01 56 58                     add qword ptr [r14 + 0x58], rdx
002E6B71  E9 92 F9 FF FF                  jmp 0x1402e6508
002E6B76  49 01 56 58                     add qword ptr [r14 + 0x58], rdx
002E6B7A  E9 0E F5 FF FF                  jmp 0x1402e608d
002E6B7F  49 01 56 58                     add qword ptr [r14 + 0x58], rdx
002E6B83  E9 03 F6 FF FF                  jmp 0x1402e618b
002E6B88  4D 01 46 58                     add qword ptr [r14 + 0x58], r8
002E6B8C  E9 25 F7 FF FF                  jmp 0x1402e62b6
002E6B91  4D 01 46 58                     add qword ptr [r14 + 0x58], r8
002E6B95  E9 3E F8 FF FF                  jmp 0x1402e63d8
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpHpVsChunkSplit(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, __int64 a6)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m64;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p138;
    unsigned int v_stack_p13C;
    unsigned __int64 v_stack_p140;
    unsigned __int64 v_stack_p148;
    unsigned int v_stack_p150;
    unsigned int v_stack_p158;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p1D0;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_pA0;
    unsigned int v_stack_pA4;
    unsigned __int64 v_stack_pA8;
    unsigned int v_stack_pB0;
    unsigned int v_stack_pB8;
    unsigned int v_stack_pC;
    unsigned int v_stack_pC8;
    unsigned int v_stack_pCC;
    unsigned __int64 v_stack_pD0;
    unsigned __int64 v_stack_pD8;
    unsigned __int64 v_stack_pE0;
    unsigned __int64 v_stack_pF0;

    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (96);
    result = (unsigned int)(((unsigned int)((unsigned int)(a4))) >> (16));
    v_r15 = (unsigned int)((*(unsigned __int16 *)(a4 + 2)) ^ ((unsigned int)(result)));
    v_r15 = (unsigned int)((v_r15) ^ ((unsigned int)(*(unsigned __int16 *)(v_rip + 11806290))));
    result = RtlRbRemoveNode(a2 + 16, a4 + 8, a3, a4);
    v_rbx = 0;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(a4))) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(a4)))));
    a1 = (unsigned int)((a1) >> (16));
    a1 = (unsigned int)((a1) ^ ((unsigned int)(*(unsigned __int16 *)(v_rip + 11806262))));
    v_r11 = (unsigned int)(((unsigned int)((unsigned int)(a4))) - ((unsigned int)(a3)));
    a1 = (unsigned int)((a1) << (4));
    result = (unsigned int)(((unsigned int)((unsigned int)(a1))) - ((unsigned int)(a3)));
    result = (unsigned int)((result) + ((unsigned int)(a4)));
    result = (unsigned int)((result) & (0xFFFFF000ULL));
    a2 = (unsigned int)((v_r11 + 4127) & (0xFFFFF000ULL));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result))) - ((unsigned int)(a2)));
    if (((unsigned int)(a2)) >= ((unsigned int)(result))) { a1 = 0; }
    result = (unsigned int)(((unsigned int)((unsigned int)(a4))) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(a4)))));
    result = (unsigned int)((result) ^ (*(unsigned int *)(v_rip + 11806183)));
    a1 = (unsigned int)((a1) >> (12));
    a2 = (unsigned int)(((unsigned __int16)(result)) - ((unsigned int)(a1)));
    result = ((unsigned int)((unsigned int)(a1)) + 4095) >> (12);
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a4))))) & (0xFFFULL));
    a1 = (a1) + (0xFFFULL);
    a1 = (a1) + ((unsigned int)((unsigned int)(a1)));
    a1 = (a1) >> (12);
    a2 = (unsigned int)((a2) - ((unsigned int)(a1)));
    a2 = (unsigned int)((a2) + ((unsigned int)(result)));
    if ((unsigned __int16)((__int16)(*(unsigned __int16 *)(a1 + 6))) == 0) goto loc_002E6B64;
loc_002E5D59:
    v_r15 = (unsigned int)((v_r15) - ((unsigned int)((unsigned int)(a5))));
    if (condition_is_equal) goto loc_002E5DA3;
    if (((*(unsigned __int8 *)(a1 + 4)) & (1)) == 0) goto loc_002E5DA3;
    result = ((unsigned int)((unsigned int)((unsigned int)(a5)))) << (4);
    result = (result) + (a4);
    a1 = (result + 4095) & (0xFFFFFFFFFFFFF000ULL);
    a1 = (a1) - (result);
    a1 = (a1) >> (4);
    result = (unsigned int)(((unsigned int)((unsigned int)(a1))) << (4));
    if (((unsigned int)(result)) < 32) goto loc_002E6AD0;
    if ((((unsigned int)(result)) & (0xFFFFFFC0ULL)) == 0) goto loc_002E65BF;
loc_002E5DA3:
    v_stack_p8 = 0;
    v_stack_pC = 0x10000ULL;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) << (4));
    a4 = v_r15 + (unsigned int)(a5) * 1;
    if (((unsigned int)(result)) >= 32) { a4 = (unsigned int)((unsigned int)(a5)); }
    v_r10 = 0;
    if (((unsigned int)(result)) >= 32) { v_r10 = (unsigned int)(v_r15); }
    result = (*(unsigned __int64 *)(v_rip + 11805992)) >> (32);
    result = (unsigned int)((result) >> (16));
    a1 = (v_stack_p8) >> (32);
    a1 = (unsigned int)((a1) >> (16));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(result)));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(a4))) << (4));
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_r11))) >> (12));
    result = (a4) >> (32);
    result = (unsigned int)((result) >> (16));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(result)));
    v_stack_m64 = (unsigned int)(a4);
    *(unsigned __int8 *)(a4 + 6) = (unsigned __int8)(a1);
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a4))))) ^ ((unsigned int)(a3)));
    v_stack_p18 = (unsigned int)(v_r10);
    result = (unsigned int)((result) ^ (*(unsigned int *)(v_rip + 11805916)));
    v_stack_p8 = (unsigned int)((unsigned __int8)(result));
    *(unsigned int *)(a4 + 8) = (unsigned int)((unsigned __int8)(result));
    result = a2 + 32;
    if ((unsigned int)(v_r10) == 0) { result = (unsigned int)(a2); }
    v_stack_p28 = (unsigned int)(a4);
    a2 = (unsigned int)((v_r11 - 1) + ((unsigned int)(result)));
    a2 = (a2) >> (12);
    a1 = (unsigned __int8)((63) - ((unsigned __int8)(a2)));
    v_r15 = (-1) >> ((unsigned __int8)(a1));
    result = (-1) << ((unsigned __int8)((unsigned int)((unsigned int)(a3))));
    v_r15 = (v_r15) & (result);
    result = (v_r15) ^ (*(unsigned __int64 *)(a3 + 16));
    v_r15 = (v_r15) & (result);
    if (condition_is_not_equal) goto loc_002E6829;
loc_002E5E7C:
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(a4))) >> (16));
    v_rsi = (unsigned __int16)((v_rsi) ^ ((unsigned __int16)((unsigned int)((unsigned int)(a4)))));
    v_rsi = (unsigned __int16)((v_rsi) ^ (*(unsigned __int16 *)(v_rip + 11805816)));
    *(unsigned __int16 *)(a4 + 2) = (unsigned __int16)(v_rsi);
    if ((unsigned int)((unsigned int)((unsigned int)(v_r10))) != 0) goto loc_002E5EA7;
    v_rsp = (v_rsp) + (96);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a4))));
loc_002E5EA7:
    result = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a4))))) << (4);
    v_rdi = (a4) + (result);
    if ((unsigned int)((unsigned int)((unsigned int)(a4))) == 0) goto loc_002E6B4E;
loc_002E5EBA:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r10))))) << (16));
    a2 = ((unsigned __int16)((unsigned int)((unsigned int)(a4)))) << (32);
    a2 = (a2) | (0);
    a2 = (a2) | (a1);
    a2 = (a2) ^ (*(unsigned __int64 *)(v_rip + 11805729));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) - ((unsigned int)(a3)));
    a2 = (a2) ^ (v_rdi);
    a1 = (unsigned int)((a1) >> (12));
    *(unsigned __int64 *)(v_rdi) = a2;
    a1 = (unsigned int)((a1) ^ ((unsigned int)(v_rdi)));
    a1 = (unsigned int)((a1) ^ (*(unsigned int *)(v_rip + 11805709)));
    *(unsigned int *)(v_rdi + 8) = (unsigned int)((unsigned __int8)(a1));
    result = (*(unsigned __int16 *)(a3 + 32)) + (3);
    result = (result) << (4);
    a2 = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r10))))) << (4);
    result = (result) + (a3);
    a2 = (a2) + (v_rdi);
    if (a2 < result) {
        result = (unsigned __int16)((unsigned int)((unsigned int)(v_r10)));
        v_stack_pA0 = 0;
        v_stack_pA4 = (unsigned int)(result);
        result = *(unsigned __int64 *)(v_rip + 11805646);
        a1 = v_stack_pA0;
        result = (result) >> (32);
        a1 = (a1) >> (32);
        a1 = (unsigned __int16)((a1) ^ ((unsigned __int16)(result)));
        result = a2;
        result = (result) >> (32);
        a1 = (unsigned __int16)((a1) ^ ((unsigned __int16)(result)));
        *(unsigned __int16 *)(a2 + 4) = (unsigned __int16)(a1);
    }
    v_stack_pB0 = 0;
loc_002E5F5A:
    result = (v_rdi) ^ (*(unsigned __int64 *)(v_rdi));
    result = (result) ^ (*(unsigned __int64 *)(v_rip + 11805593));
    a1 = (0) >> (32);
    a1 = (unsigned int)((a1) >> (16));
    result = (result) >> (32);
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)(result))) >> (16));
    result = (v_rdi) >> (32);
    result = (unsigned int)((result) >> (16));
    a2 = (*(unsigned __int64 *)(v_rip + 11805593)) >> (32);
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(result)));
    a2 = (unsigned int)((a2) >> (16));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(a2)));
    v_stack_pA0 = (unsigned int)(v_r12);
    *(unsigned __int8 *)(v_rdi + 6) = (unsigned __int8)(a1);
    if ((unsigned int)((unsigned __int16)(result)) == 0) goto loc_002E60A2;
    result = ((unsigned int)((unsigned int)((unsigned __int16)(result)))) << (4);
    v_r12 = (v_rdi) - (result);
    v_rsi = (v_r12) ^ (*(unsigned __int64 *)(v_r12));
    v_rsi = (v_rsi) ^ (*(unsigned __int64 *)(v_rip + 11805488));
    result = (v_rsi) >> (32);
    if ((((unsigned int)(result)) & (0xFF0000ULL)) != 0) goto loc_002E6B22;
    a1 = (v_stack_pA8) + (16);
    result = RtlRbRemoveNode(a1, v_r12 + 8, (unsigned __int16)(result), a3 + 48);
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) - ((unsigned int)(a3)));
    a2 = (unsigned int)((a2) + (0x101FULL));
    a2 = (unsigned int)((a2) & (0xFFFFF000ULL));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r12))))) ^ ((unsigned int)(v_r12)));
    a1 = (unsigned int)((a1) >> (16));
    a1 = (unsigned int)((a1) ^ ((unsigned int)(*(unsigned __int16 *)(v_rip + 11805443))));
    a1 = (unsigned int)((a1) << (4));
    a1 = (unsigned int)((a1) - ((unsigned int)(a3)));
    a1 = (unsigned int)((a1) + ((unsigned int)(v_r12)));
    a1 = (unsigned int)((a1) & (0xFFFFF000ULL));
    result = (unsigned int)(((unsigned int)((unsigned int)(a1))) - ((unsigned int)(a2)));
    if (((unsigned int)(a2)) >= ((unsigned int)(a1))) { result = 0; }
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r12))) ^ ((unsigned int)(v_r12)));
    a4 = (unsigned int)((a4) ^ (*(unsigned int *)(v_rip + 11805363)));
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) & (0xFFFULL));
    result = (unsigned int)((result) >> (12));
    a1 = (unsigned int)(((unsigned __int16)(a4)) - ((unsigned int)(result)));
    result = ((unsigned int)((unsigned int)(a1)) + 4095) + (v_r10);
    result = (result) >> (12);
    a1 = (unsigned int)((a1) - ((unsigned int)(result)));
    result = ((unsigned int)((unsigned int)(a1)) + 4095) >> (12);
    a1 = (unsigned int)((a1) + ((unsigned int)(result)));
    if ((unsigned __int16)((__int16)(*(unsigned __int16 *)(a1 + 6))) == 0) goto loc_002E6B76;
loc_002E608D:
    v_rsi = (unsigned int)((v_rsi) >> (16));
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) + ((unsigned int)(v_rsi)));
loc_002E60A2:
    result = ((unsigned int)((unsigned int)(*(unsigned __int16 *)(a3 + 32)))) << (4);
    v_rsi = ((unsigned int)((unsigned int)(v_r15))) << (4);
    result = (result) + (a3 + 48);
    v_rsi = (v_rsi) + (v_r12);
    if (v_rsi >= result) goto loc_002E61A2;
    result = (v_rsi) ^ (*(unsigned __int64 *)(v_rsi));
    result = (result) ^ (*(unsigned __int64 *)(v_rip + 11805232));
    v_stack_pA0 = result;
    result = (result) >> (32);
    if ((((unsigned int)(result)) & (0xFF0000ULL)) != 0) goto loc_002E61A2;
    a1 = (v_stack_pA8) + (16);
    result = RtlRbRemoveNode(a1, v_rsi + 8, (unsigned int)((unsigned int)(a1)), a3 + 48);
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) - ((unsigned int)(a3)));
    a2 = (unsigned int)((a2) + (0x101FULL));
    a2 = (unsigned int)((a2) & (0xFFFFF000ULL));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi))))) ^ ((unsigned int)(v_rsi)));
    a1 = (unsigned int)((a1) >> (16));
    a1 = (unsigned int)((a1) ^ ((unsigned int)(*(unsigned __int16 *)(v_rip + 11805178))));
    a1 = (unsigned int)((a1) << (4));
    a1 = (unsigned int)((a1) - ((unsigned int)(a3)));
    a1 = (unsigned int)((a1) + ((unsigned int)(v_rsi)));
    a1 = (unsigned int)((a1) & (0xFFFFF000ULL));
    result = (unsigned int)(((unsigned int)((unsigned int)(a1))) - ((unsigned int)(a2)));
    if (((unsigned int)(a2)) >= ((unsigned int)(a1))) { result = 0; }
    v_rsi = (unsigned int)((v_rsi) ^ (*(unsigned int *)(v_rip + 11805111)));
    result = (unsigned int)((result) >> (12));
    v_rsi = (unsigned int)((v_rsi) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))));
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) & (0xFFFULL));
    a1 = (unsigned int)(((unsigned __int16)(v_rsi)) - ((unsigned int)(result)));
    result = ((unsigned int)((unsigned int)(a1)) + 4095) + (v_r10);
    result = (result) >> (12);
    a1 = (unsigned int)((a1) - ((unsigned int)(result)));
    result = ((unsigned int)((unsigned int)(a1)) + 4095) >> (12);
    a1 = (unsigned int)((a1) + ((unsigned int)(result)));
    if ((unsigned __int16)((__int16)(*(unsigned __int16 *)(a1 + 6))) == 0) goto loc_002E6B7F;
loc_002E618B:
    result = (unsigned int)((v_stack_pA0) >> (16));
    v_r15 = (unsigned int)((v_r15) + ((unsigned int)(result)));
loc_002E61A2:
    if (((*(unsigned __int8 *)(a1 + 4)) & (1)) == 0) goto loc_002E62BC;
    a2 = ((unsigned int)((unsigned int)(v_r15))) << (4);
    a2 = (a2) + (v_r12);
    result = ((unsigned __int16)(*(unsigned __int16 *)(a3 + 32))) << (4);
    result = (result) + (a3 + 48);
    v_stack_pA0 = a2;
    if (a2 >= result) goto loc_002E62BC;
    v_rsi = (a2) ^ (*(unsigned __int64 *)(a2));
    v_rsi = (v_rsi) ^ (*(unsigned __int64 *)(v_rip + 11804961));
    result = (v_rsi) >> (32);
    if ((((unsigned int)(result)) & (0xFF0000ULL)) != 0) goto loc_002E62BC;
    a2 = (a2) + (8);
    a1 = (v_stack_pA8) + (16);
    result = RtlRbRemoveNode(a1, a2, (unsigned int)((unsigned int)(a1)), a3 + 48);
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_pA0))) - ((unsigned int)(a3)));
    a3 = (unsigned int)((a3) + (0x101FULL));
    a3 = (unsigned int)((a3) & (0xFFFFF000ULL));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_pA0))))) ^ ((unsigned int)(v_stack_pA0)));
    a4 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_pA0))))) ^ ((unsigned int)(v_stack_pA0)));
    a1 = (unsigned int)((a1) >> (16));
    a1 = (unsigned int)((a1) ^ ((unsigned int)(*(unsigned __int16 *)(v_rip + 11804909))));
    a4 = (unsigned int)((a4) >> (16));
    a1 = (unsigned int)((a1) << (4));
    a4 = (unsigned int)((a4) ^ ((unsigned int)(*(unsigned __int16 *)(v_rip + 11804909))));
    a1 = (unsigned int)((a1) - ((unsigned int)(a3)));
    a1 = (unsigned int)((a1) + ((unsigned int)(v_stack_pA0)));
    a4 = (unsigned int)((a4) << (4));
    a1 = (unsigned int)((a1) & (0xFFFFF000ULL));
    result = (unsigned int)(((unsigned int)((unsigned int)(a1))) - ((unsigned int)(a3)));
    if (((unsigned int)(a3)) >= ((unsigned int)(a1))) { result = 0; }
    v_r10 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_pA0))) ^ (v_stack_pA0));
    v_r10 = (unsigned int)((v_r10) ^ (*(unsigned int *)(v_rip + 11804809)));
    v_r11 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_pA0))) & (0xFFFULL));
    result = (unsigned int)((result) >> (12));
    a1 = (unsigned int)(((unsigned __int16)(v_r10)) - ((unsigned int)(result)));
    result = (v_r11 + 4095) + (a4);
    result = (result) >> (12);
    a1 = (unsigned int)((a1) - ((unsigned int)(result)));
    result = (a4 + 4095) >> (12);
    a1 = (unsigned int)((a1) + ((unsigned int)(result)));
    if ((unsigned __int16)((__int16)(*(unsigned __int16 *)(a1 + 6))) == 0) goto loc_002E6B88;
loc_002E62B6:
    v_rsi = (unsigned int)((v_rsi) >> (16));
    v_r15 = (unsigned int)((v_r15) + ((unsigned int)(v_rsi)));
loc_002E62BC:
    if (((unsigned int)((unsigned int)(v_stack_pA0))) != ((unsigned int)(v_r15))) goto loc_002E675B;
loc_002E62C5:
    if (((unsigned int)(v_r15)) == ((unsigned int)(*(unsigned __int16 *)(a3 + 32)))) goto loc_002E6ADA;
    if (((unsigned int)(v_r15)) > v_stack_pB0) goto loc_002E65D2;
loc_002E62E1:
    if (((*(unsigned __int8 *)(a1 + 4)) & (1)) == 0) goto loc_002E646D;
    if (((v_r12 + 32) & (0xFFFULL)) == 0) goto loc_002E646D;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) >> (16));
    a4 = (v_r12 + 4111) & (0xFFFFFFFFFFFFF000ULL);
    a2 = (unsigned int)((*(unsigned __int16 *)(v_r12 + 2)) ^ ((unsigned int)(result)));
    a2 = (unsigned int)((a2) ^ ((unsigned int)(*(unsigned __int16 *)(v_rip + 11804659))));
    result = (a4) - (v_r12);
    a1 = ((unsigned int)((unsigned int)(a2))) << (4);
    if (result < a1) goto loc_002E69E5;
loc_002E6338:
    if (0 == 0) goto loc_002E646D;
    result = (unsigned int)((0) >> (16));
    a1 = (unsigned int)((*(unsigned __int16 *)(0 + 2)) ^ ((unsigned int)(result)));
    v_r11 = (unsigned int)((0) & (0xFFFULL));
    v_r11 = (v_r11) + (0xFFFULL);
    a1 = (unsigned int)((a1) ^ ((unsigned int)(*(unsigned __int16 *)(v_rip + 11804579))));
    a1 = (unsigned int)((a1) << (4));
    v_r10 = (unsigned int)((0) - ((unsigned int)(a3)));
    v_r10 = (unsigned int)((v_r10) + (0x101FULL));
    v_r11 = (v_r11) + ((unsigned int)((unsigned int)(a1)));
    v_r10 = (unsigned int)((v_r10) & (0xFFFFF000ULL));
    a3 = (unsigned int)(((unsigned int)((unsigned int)(a1))) - ((unsigned int)(a3)));
    v_r11 = (v_r11) >> (12);
    a3 = (unsigned int)((a3) + (0));
    result = (a1 + 4095) >> (12);
    a3 = (unsigned int)((a3) & (0xFFFFF000ULL));
    v_r11 = (unsigned int)((v_r11) - ((unsigned int)(result)));
    if (((unsigned int)(v_r10)) < ((unsigned int)(a3))) goto loc_002E6A8E;
loc_002E63B9:
    a2 = (unsigned int)((0) >> (12));
    if ((unsigned __int16)((__int16)(*(unsigned __int16 *)(a1 + 6))) == 0) goto loc_002E6B91;
loc_002E63D8:
    a2 = (unsigned __int16)((a2) - ((unsigned __int16)(a1)));
    a2 = (unsigned __int16)((a2) + ((unsigned __int16)(v_r11)));
    a2 = (unsigned __int16)((a2) ^ (0));
    a2 = (unsigned __int16)((a2) ^ (*(unsigned __int16 *)(v_rip + 11804427)));
    *(unsigned __int16 *)(0) = (unsigned __int16)(a2);
    a1 = (unsigned int)((0) ^ (*(unsigned int *)(0)));
    a1 = (unsigned int)((a1) ^ ((unsigned int)(*(unsigned __int64 *)(v_rip + 11804413))));
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_pA8 + 24))) & (1)) != 0) goto loc_002E6B11;
loc_002E6418:
    a3 = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)(v_stack_pA8 + 24))) & (1));
    result = 0;
    if (*(unsigned __int64 *)(v_stack_pA8 + 16) == 0) goto loc_002E6459;
loc_002E6430:
    result = (unsigned int)((*(unsigned __int64 *)(v_stack_pA8 + 16) - 8) ^ (*(unsigned int *)(*(unsigned __int64 *)(v_stack_pA8 + 16) - 8)));
    result = (unsigned int)((result) ^ ((unsigned int)(*(unsigned __int64 *)(v_rip + 11804413))));
    if (((unsigned int)(a1)) < ((unsigned int)(result))) goto loc_002E67D2;
    if ((unsigned int)(a3) == 0) goto loc_002E69D7;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_pA8 + 16) + 8) != 0) goto loc_002E69D4;
loc_002E6457:
loc_002E6459:
    a4 = (0) + (8);
    result = RtlRbInsertNodeEx(v_stack_pA8 + 16, *(unsigned __int64 *)(v_stack_pA8 + 16), 1, a4);
    goto loc_002E647C;
loc_002E646D:
loc_002E647C:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) >> (16));
    a1 = (unsigned int)((*(unsigned __int16 *)(v_r12 + 2)) ^ ((unsigned int)(result)));
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) & (0xFFFULL));
    v_r10 = (v_r10) + (0xFFFULL);
    a1 = (unsigned int)((a1) ^ ((unsigned int)(*(unsigned __int16 *)(v_rip + 11804266))));
    a1 = (unsigned int)((a1) << (4));
    a4 = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) - ((unsigned int)(a3)));
    a4 = (unsigned int)((a4) + (0x101FULL));
    v_r10 = (v_r10) + ((unsigned int)((unsigned int)(a1)));
    a4 = (unsigned int)((a4) & (0xFFFFF000ULL));
    a3 = (unsigned int)(((unsigned int)((unsigned int)(a1))) - ((unsigned int)(a3)));
    v_r10 = (v_r10) >> (12);
    a3 = (unsigned int)((a3) + ((unsigned int)(v_r12)));
    result = (a1 + 4095) >> (12);
    a3 = (unsigned int)((a3) & (0xFFFFF000ULL));
    v_r10 = (unsigned int)((v_r10) - ((unsigned int)(result)));
    if (((unsigned int)(a4)) < ((unsigned int)(a3))) goto loc_002E67F7;
loc_002E64E9:
    v_rbx = (unsigned int)((v_rbx) >> (12));
    if ((unsigned __int16)((__int16)(*(unsigned __int16 *)(a1 + 6))) == 0) goto loc_002E6B6D;
loc_002E6508:
    v_rbx = (unsigned __int16)((v_rbx) - ((unsigned __int16)(a1)));
    v_rbx = (unsigned __int16)((v_rbx) + ((unsigned __int16)(v_r10)));
    v_rbx = (unsigned __int16)((v_rbx) ^ ((unsigned __int16)(v_r12)));
    v_rbx = (unsigned __int16)((v_rbx) ^ (*(unsigned __int16 *)(v_rip + 11804128)));
    *(unsigned __int16 *)(v_r12) = (unsigned __int16)(v_rbx);
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) ^ (*(unsigned int *)(v_r12)));
    a1 = (unsigned int)((a1) ^ ((unsigned int)(*(unsigned __int64 *)(v_rip + 11804116))));
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_pA8 + 16 + 8))) & (1)) != 0) goto loc_002E6AFD;
loc_002E653E:
    result = 0;
    a4 = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)(v_stack_pA8 + 16 + 8))) & (1));
    if (*(unsigned __int64 *)(v_stack_pA8 + 16) == 0) goto loc_002E6575;
loc_002E6550:
    result = (unsigned int)((*(unsigned __int64 *)(v_stack_pA8 + 16) - 8) ^ (*(unsigned int *)(*(unsigned __int64 *)(v_stack_pA8 + 16) - 8)));
    result = (unsigned int)((result) ^ ((unsigned int)(*(unsigned __int64 *)(v_rip + 11804116))));
    if (((unsigned int)(a1)) < ((unsigned int)(result))) goto loc_002E659D;
    if ((unsigned int)(a4) == 0) goto loc_002E674D;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_pA8 + 16) + 8) != 0) goto loc_002E674A;
loc_002E6573:
loc_002E6575:
    result = RtlRbInsertNodeEx(v_stack_pA8 + 16, *(unsigned __int64 *)(v_stack_pA8 + 16), 1, v_r12 + 8);
    v_rsp = (v_rsp) + (96);
    return (unsigned int)(a5);
loc_002E659D:
    if ((unsigned int)(v_r12 + 8) == 0) goto loc_002E65B1;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_pA8 + 16)) == 0) goto loc_002E6B02;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_pA8 + 16))) ^ (*(unsigned __int64 *)(v_stack_pA8 + 16));
loc_002E65B1:
    if (result == 0) goto loc_002E6B02;
loc_002E65BA:
    goto loc_002E6550;
loc_002E65BF:
    if (((unsigned int)(result)) == 32) goto loc_002E5DA3;
    a2 = (unsigned int)((result) + 1);
    v_r15 = (unsigned int)((-1) - 1);
    goto loc_002E5DA3;
loc_002E65D2:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) >> (16));
    a3 = (unsigned int)((*(unsigned __int16 *)(v_r12 + 2)) ^ ((unsigned int)(result)));
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) - ((unsigned int)(a3)));
    a3 = (unsigned int)((a3) ^ ((unsigned int)(*(unsigned __int16 *)(v_rip + 11803926))));
    a3 = (unsigned int)((a3) << (4));
    a3 = (unsigned int)((a3) - ((unsigned int)(a3)));
    a3 = (unsigned int)((a3) + ((unsigned int)(v_r12)));
    a4 = (unsigned int)((v_r12 + 4127) & (0xFFFFF000ULL));
    a3 = (unsigned int)((a3) & (0xFFFFF000ULL));
    if (((unsigned int)(a4)) >= ((unsigned int)(a3))) goto loc_002E62E1;
    result = (a3 - 1) >> (12);
    a1 = (unsigned __int8)((63) - ((unsigned __int8)(result)));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(a3))) - ((unsigned int)(a4)));
    a4 = (unsigned int)((a4) >> (12));
    v_rsi = (-1) >> ((unsigned __int8)(a1));
    result = (-1) << ((unsigned __int8)((unsigned __int8)(a4)));
    v_rsi = (v_rsi) & (result);
    v_rsi = (v_rsi) & (*(unsigned __int64 *)(a3 + 16));
    if (((unsigned int)(a2)) < 0x1000ULL) goto loc_002E62E1;
    if (v_rsi == 0) goto loc_002E62E1;
    v_stack_p148 = result;
    result = RtlpHpVsCommitLimitCheck(a1, a3, (unsigned int)((unsigned int)(result)), a4);
    if ((unsigned int)(result) == 0) goto loc_002E62E1;
    v_r12 = (unsigned int)((v_r12) >> (12));
    result = (v_r12) >> (32);
    v_r12 = (unsigned int)((v_r12) ^ ((unsigned int)(v_r12)));
    result = (unsigned int)((result) >> (16));
    v_stack_p138 = v_rbx;
    v_stack_p13C = 0x10000ULL;
    a1 = (v_stack_p138) >> (32);
    a1 = (unsigned int)((a1) >> (16));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(result)));
    result = (*(unsigned __int64 *)(v_rip + 11803712)) >> (32);
    result = (unsigned int)((result) >> (16));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(result)));
    *(unsigned __int8 *)(v_r12 + 6) = (unsigned __int8)(a1);
    v_r12 = (unsigned int)((v_r12) ^ (*(unsigned int *)(v_rip + 11803693)));
    *(unsigned int *)(v_r12 + 8) = (unsigned int)((unsigned __int8)(v_r12));
    result = (unsigned __int8)(v_r12);
    if (((*(unsigned __int8 *)(a1 + 5)) & (1)) == 0) {
        a1 = *(unsigned __int8 *)(a1 + 3);
        a2 = a6;
        result = RtlpHpReleaseQueuedLockExclusive(a1, a2, (unsigned int)((unsigned int)(result)), a4);
    }
    v_stack_pB8 = (unsigned int)(v_rbx);
    result = RtlpHpVsSubsegmentCommitPages(a1, a3, v_rsi, (unsigned int)(v_stack_p148));
    if (((*(unsigned __int8 *)(a1 + 5)) & (1)) == 0) {
        a1 = v_stack_p140;
        a2 = *(unsigned __int8 *)(a1 + 3);
        a1 = (a1) + (8);
        a3 = a6;
        result = RtlpHpAcquireQueuedLockExclusive(a1, a2, a3, (unsigned int)(v_stack_p148));
    }
    v_stack_p148 = (unsigned int)(v_r15);
    goto loc_002E5F5A;
loc_002E674A:
    result = (result) ^ (a2);
loc_002E674D:
    if (result != 0) goto loc_002E65BA;
    goto loc_002E6573;
loc_002E675B:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) >> (16));
    result = (unsigned __int16)((result) ^ ((unsigned __int16)(v_r15)));
    a2 = ((unsigned int)((unsigned int)(v_r15))) << (4);
    result = (unsigned __int16)((result) ^ (*(unsigned __int16 *)(v_rip + 11803532)));
    a2 = (a2) + (v_r12);
    *(unsigned __int16 *)(v_r12 + 2) = (unsigned __int16)(result);
    result = (*(unsigned __int16 *)(a3 + 32)) << (4);
    result = (result) + (a3 + 48);
    if (a2 >= result) goto loc_002E62C5;
    v_stack_p138 = v_rbx;
    v_stack_p13C = (unsigned int)((unsigned __int16)(v_r15));
    result = (a2) >> (32);
    a1 = (v_stack_p138) >> (32);
    a1 = (unsigned __int16)((a1) ^ ((unsigned __int16)(result)));
    result = (*(unsigned __int64 *)(v_rip + 11803454)) >> (32);
    a1 = (unsigned __int16)((a1) ^ ((unsigned __int16)(result)));
    *(unsigned __int16 *)(a2 + 4) = (unsigned __int16)(a1);
    goto loc_002E62C5;
loc_002E67D2:
    if ((unsigned int)(a3) == 0) goto loc_002E67E6;
    if (*(unsigned __int64 *)(a2) == 0) goto loc_002E6B1B;
    result = (*(unsigned __int64 *)(a2)) ^ (a2);
loc_002E67E6:
    if (result == 0) goto loc_002E6B1B;
loc_002E67EF:
    goto loc_002E6430;
loc_002E67F7:
    result = (a3 - 1) >> (12);
    a1 = (unsigned __int8)((63) - ((unsigned __int8)(result)));
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(a3))) - ((unsigned int)((unsigned int)(v_stack_p148))));
    a4 = (unsigned int)(((unsigned int)(v_stack_p148)) >> (12));
    result = (v_r15) >> ((unsigned __int8)(a1));
    v_r15 = (v_r15) << ((unsigned __int8)((unsigned __int8)(a4)));
    result = (result) & (v_r15);
    result = (result) & (*(unsigned __int64 *)(a3 + 16));
    goto loc_002E64E9;
loc_002E6829:
    *(unsigned int *)(v_r12 + 8) = (unsigned int)((unsigned int)(v_stack_p138));
    if (((*(unsigned __int8 *)(a1 + 5)) & (1)) != 0) goto loc_002E6B37;
    result = RtlpHpReleaseQueuedLockExclusive(*(unsigned __int8 *)(a1 + 3), a6, a3, a4);
    v_stack_p138 = a1 + 5;
loc_002E6864:
    v_stack_pD8 = result;
    result = 0;
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)(a6))) << (12));
    v_stack_pF0 = 0;
    v_r10 = (v_r10) + (a3);
    v_stack_p150 = (unsigned int)(a6);
    v_stack_pC8 = 0;
    result = (unsigned int)((result) - ((unsigned int)(a6)));
    v_stack_pD0 = v_r10;
    v_stack_pE0 = v_xmm0;
    v_r15 = (1) << ((unsigned __int8)(result + 1));
    v_r15 = (v_r15) - 1;
    a3 = (unsigned int)(((unsigned int)((unsigned int)(result + 1))) << (12));
    v_stack_p158 = (unsigned int)(a3);
    v_r15 = (v_r15) << ((unsigned __int8)((unsigned int)((unsigned int)(a6))));
    if (((*(unsigned __int8 *)(a1 + 5)) & (1)) == 0) {
        a2 = *(unsigned __int8 *)(a1 + 3);
        a1 = a3 + 24;
        a3 = v_stack_pE0;
        result = RtlpHpAcquireQueuedLockExclusive(a1, a2, a3, a4);
        v_r10 = v_stack_pD0;
        a3 = a5;
    }
    result = (*(unsigned __int64 *)(a1 + 32)) ^ (*(unsigned __int64 *)(v_rip + 11803139));
    a1 = (a1) ^ (*(unsigned __int64 *)(a1 + 8));
    result = (result) ^ (a1);
    a4 = 0;
    if (result != (v_rip + 257626)) goto loc_002E6B44;
    result = RtlpHpSegLfhVsCommit(a1, v_r10, a3, a4);
loc_002E691B:
    v_stack_p158 = (unsigned int)(result);
    if (sign_flag) goto loc_002E6AC3;
loc_002E6949:
    result = (unsigned int)(v_stack_pD8);
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_stack_p138))) & (1)) == 0) {
        a1 = *(unsigned __int8 *)(a1 + 3);
        a2 = v_stack_pE0;
        result = RtlpHpReleaseQueuedLockExclusive(a1, a2, *(unsigned __int8 *)(v_stack_p138), a4);
        a3 = *(unsigned __int8 *)(a1 + 5);
    }
    v_stack_p138 = (unsigned int)((unsigned int)(v_stack_p148));
    v_stack_p158 = (unsigned int)((unsigned int)(v_stack_pCC));
    v_r12 = (unsigned int)((unsigned int)((unsigned int)(v_stack_pCC)));
    if (sign_flag) {
        result = (unsigned int)(v_stack_pCC) + (unsigned int)(v_stack_p148) * 1;
        v_stack_p158 = (unsigned int)(v_rbx);
        v_stack_p138 = (unsigned int)(result);
        v_r12 = (unsigned int)(v_rbx);
    }
    if ((((unsigned __int8)(a3)) & (1)) == 0) {
        a1 = v_stack_p140;
        a2 = *(unsigned __int8 *)(a1 + 3);
        a1 = (a1) + (8);
        a3 = a6;
        result = RtlpHpAcquireQueuedLockExclusive(a1, a2, a3, a4);
    }
    goto loc_002E5E7C;
loc_002E69D4:
    result = (result) ^ (a2);
loc_002E69D7:
    if (result != 0) goto loc_002E67EF;
    goto loc_002E6457;
loc_002E69E5:
    a4 = (a4) + (-32);
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) >> (16));
    a1 = (a4) - (v_r12);
    a1 = (a1) >> (4);
    result = (unsigned __int16)((result) ^ ((unsigned __int16)(a1)));
    a2 = (unsigned int)((a2) - ((unsigned int)(a1)));
    result = (unsigned __int16)((result) ^ ((unsigned __int16)((unsigned int)(v_stack_p138))));
    *(unsigned __int16 *)(v_r12 + 2) = (unsigned __int16)(result);
    *(unsigned __int64 *)(a4) = v_xmm0;
    a3 = ((unsigned int)((unsigned int)(a2))) << (4);
    *(unsigned __int64 *)(a4 + 16) = v_xmm0;
    *(unsigned __int16 *)(a4 + 2) = (unsigned __int16)(a2);
    a3 = (a3) + (a4);
    *(unsigned __int16 *)(a4 + 4) = (unsigned __int16)(a1);
    result = (a4) ^ (*(unsigned __int64 *)(a4));
    result = (result) ^ (*(unsigned __int64 *)(v_rip + 11802830));
    *(unsigned __int64 *)(a4) = result;
    result = (*(unsigned __int16 *)(a3 + 32)) + (3);
    result = (result) << (4);
    result = (result) + (a3);
    if (a3 >= result) goto loc_002E6338;
    v_stack_p138 = v_rbx;
    v_stack_p13C = (unsigned int)((unsigned __int16)(a2));
    result = (a3) >> (32);
    a1 = (v_stack_p138) >> (32);
    a1 = (unsigned __int16)((a1) ^ ((unsigned __int16)(result)));
    result = (*(unsigned __int64 *)(v_rip + 11802755)) >> (32);
    a1 = (unsigned __int16)((a1) ^ ((unsigned __int16)(result)));
    *(unsigned __int16 *)(a3 + 4) = (unsigned __int16)(a1);
    goto loc_002E6338;
loc_002E6A8E:
    result = (a3 - 1) >> (12);
    a2 = (unsigned int)(((unsigned int)((unsigned int)(a3))) - ((unsigned int)(v_r10)));
    v_r10 = (unsigned int)((v_r10) >> (12));
    a1 = (unsigned __int8)((63) - ((unsigned __int8)(result)));
    a3 = ((unsigned int)((unsigned int)(v_rbx))) >> ((unsigned __int8)(a1));
    result = ((unsigned int)((unsigned int)(v_rbx))) << ((unsigned __int8)((unsigned __int8)(v_r10)));
    a3 = (a3) & (result);
    a3 = (a3) & (*(unsigned __int64 *)(a3 + 16));
    goto loc_002E63B9;
loc_002E6AC3:
    goto loc_002E6949;
loc_002E6AD0:
    a2 = (unsigned int)((a2) + ((unsigned int)((unsigned __int8)(v_r10))));
    v_r15 = (unsigned int)(((unsigned int)(a5)) - ((unsigned int)((unsigned __int8)(v_r10))));
    goto loc_002E5DA3;
loc_002E6ADA:
    result = RtlpHpVsSubsegmentCleanup(a1, a3, a3, a4);
    v_rsp = (v_rsp) + (96);
    return (unsigned int)(a5);
loc_002E6AFD:
    if (a3 != 0) goto loc_002E6B09;
loc_002E6B02:
    result = 0;
    goto loc_002E6575;
loc_002E6B09:
    a2 = (a3) ^ (v_r10);
    goto loc_002E653E;
loc_002E6B11:
    if (*(unsigned __int64 *)(v_r12 + 16) != 0) goto loc_002E6B2A;
loc_002E6B1B:
    result = 0;
    goto loc_002E6459;
loc_002E6B22:
    goto loc_002E60A2;
loc_002E6B2A:
    v_r11 = ((unsigned int)((unsigned int)(v_r15)) + 16) ^ (*(unsigned __int64 *)(v_r12 + 16));
    goto loc_002E6418;
loc_002E6B37:
    v_stack_p1D0 = (unsigned int)((unsigned int)(v_r15));
    goto loc_002E6864;
loc_002E6B44:
    result = guard_dispatch_icall(a1, *(unsigned __int64 *)(v_r12 + 16), a3, a4);
    goto loc_002E691B;
loc_002E6B4E:
    v_r12 = (*(unsigned __int64 *)(v_r12)) ^ (*(unsigned __int64 *)(v_rip + 11802536));
    v_r12 = (v_r12) ^ (v_r12);
    v_r12 = (v_r12) >> (32);
    goto loc_002E5EBA;
loc_002E6B64:
    goto loc_002E5D59;
loc_002E6B6D:
    goto loc_002E6508;
loc_002E6B76:
    goto loc_002E608D;
loc_002E6B7F:
    goto loc_002E618B;
loc_002E6B88:
    goto loc_002E62B6;
loc_002E6B91:
    goto loc_002E63D8;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpHpVsChunkSplit(void *Arg1, void *Arg2, void *Arg3, void *Arg4, uint32_t Arg5, int64_t Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m64;
    uint64_t v_stack_p10;
    uint64_t v_stack_p138;
    uint32_t v_stack_p13C;
    uint64_t v_stack_p140;
    uint64_t v_stack_p148;
    uint32_t v_stack_p150;
    uint32_t v_stack_p158;
    uint32_t v_stack_p18;
    uint64_t v_stack_p1D0;
    uint32_t v_stack_p28;
    uint64_t v_stack_p8;
    uint64_t v_stack_pA0;
    uint32_t v_stack_pA4;
    uint64_t v_stack_pA8;
    uint32_t v_stack_pB0;
    uint32_t v_stack_pB8;
    uint32_t v_stack_pC;
    uint32_t v_stack_pC8;
    uint32_t v_stack_pCC;
    uint64_t v_stack_pD0;
    uint64_t v_stack_pD8;
    uint64_t v_stack_pE0;
    uint64_t v_stack_pF0;

    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (96);
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg4))) >> (16));
    local_r15 = (uint32_t)((*(uint16_t *)(arg4 + 0x2)) ^ ((uint32_t)(result)));
    local_r15 = (uint32_t)((local_r15) ^ ((uint32_t)(*(uint16_t *)(v_rip + 0xB42652))));
    result = RtlRbRemoveNode(Arg2 + 16, Arg4 + 8, Arg3, Arg4);
    local_rbx = 0;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(Arg4))) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(arg4)))));
    Arg1 = (uint32_t)((Arg1) >> (16));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)(*(uint16_t *)(v_rip + 0xB42636))));
    local_r11 = (uint32_t)(((uint32_t)((uint32_t)(Arg4))) - ((uint32_t)(Arg3)));
    Arg1 = (uint32_t)((Arg1) << (4));
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) - ((uint32_t)(Arg3)));
    result = (uint32_t)((result) + ((uint32_t)(Arg4)));
    result = (uint32_t)((result) & (0xFFFFF000ULL));
    Arg2 = (uint32_t)((local_r11 + 4127) & (0xFFFFF000ULL));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result))) - ((uint32_t)(Arg2)));
    if (((uint32_t)(Arg2)) >= ((uint32_t)(result))) { Arg1 = 0; }
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg4))) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(arg4)))));
    result = (uint32_t)((result) ^ (*(uint32_t *)(v_rip + 0xB425E7)));
    Arg1 = (uint32_t)((Arg1) >> (12));
    Arg2 = (uint32_t)(((uint16_t)(result)) - ((uint32_t)(Arg1)));
    result = ((uint32_t)((uint32_t)(Arg1)) + 4095) >> (12);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg4))))) & (0xFFFULL));
    Arg1 = (Arg1) + (0xFFFULL);
    Arg1 = (Arg1) + ((uint32_t)((uint32_t)(Arg1)));
    Arg1 = (Arg1) >> (12);
    Arg2 = (uint32_t)((Arg2) - ((uint32_t)(Arg1)));
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(result)));
    if ((uint16_t)((int16_t)(*(uint16_t *)(arg1 + 0x6))) == 0) goto loc_002E6B64;
loc_002E5D59:
    local_r15 = (uint32_t)((local_r15) - ((uint32_t)((uint32_t)(Arg5))));
    if (condition_is_equal) goto loc_002E5DA3;
    if (((*(uint8_t *)(arg1 + 0x4)) & (1)) == 0) goto loc_002E5DA3;
    result = ((uint32_t)((uint32_t)((uint32_t)(Arg5)))) << (4);
    result = (result) + (Arg4);
    Arg1 = (result + 4095) & (0xFFFFFFFFFFFFF000ULL);
    Arg1 = (Arg1) - (result);
    Arg1 = (Arg1) >> (4);
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) << (4));
    if (((uint32_t)(result)) < 32) goto loc_002E6AD0;
    if ((((uint32_t)(result)) & (0xFFFFFFC0ULL)) == 0) goto loc_002E65BF;
loc_002E5DA3:
    v_stack_p8 = 0;
    v_stack_pC = 0x10000ULL;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) << (4));
    Arg4 = local_r15 + (uint32_t)(Arg5) * 1;
    if (((uint32_t)(result)) >= 32) { Arg4 = (uint32_t)((uint32_t)(Arg5)); }
    local_r10 = 0;
    if (((uint32_t)(result)) >= 32) { local_r10 = (uint32_t)(local_r15); }
    result = (*(uint64_t *)(v_rip + 0xB42528)) >> (32);
    result = (uint32_t)((result) >> (16));
    Arg1 = (v_stack_p8) >> (32);
    Arg1 = (uint32_t)((Arg1) >> (16));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(result)));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(Arg4))) << (4));
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(local_r11))) >> (12));
    result = (Arg4) >> (32);
    result = (uint32_t)((result) >> (16));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(result)));
    v_stack_m64 = (uint32_t)(Arg4);
    *(uint8_t *)(arg4 + 0x6) = (uint8_t)(Arg1);
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg4))))) ^ ((uint32_t)(Arg3)));
    v_stack_p18 = (uint32_t)(local_r10);
    result = (uint32_t)((result) ^ (*(uint32_t *)(v_rip + 0xB424DC)));
    v_stack_p8 = (uint32_t)((uint8_t)(result));
    *(uint32_t *)(arg4 + 0x8) = (uint32_t)((uint8_t)(result));
    result = Arg2 + 32;
    if ((uint32_t)(local_r10) == 0) { result = (uint32_t)(Arg2); }
    v_stack_p28 = (uint32_t)(Arg4);
    Arg2 = (uint32_t)((local_r11 - 1) + ((uint32_t)(result)));
    Arg2 = (Arg2) >> (12);
    Arg1 = (uint8_t)((63) - ((uint8_t)(Arg2)));
    local_r15 = (-1) >> ((uint8_t)(Arg1));
    result = (-1) << ((uint8_t)((uint32_t)((uint32_t)(Arg3))));
    local_r15 = (local_r15) & (result);
    result = (local_r15) ^ (*(uint64_t *)(arg3 + 0x10));
    local_r15 = (local_r15) & (result);
    if (condition_is_not_equal) goto loc_002E6829;
loc_002E5E7C:
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(Arg4))) >> (16));
    local_rsi = (uint16_t)((local_rsi) ^ ((uint16_t)((uint32_t)((uint32_t)(Arg4)))));
    local_rsi = (uint16_t)((local_rsi) ^ (*(uint16_t *)(v_rip + 0xB42478)));
    *(uint16_t *)(arg4 + 0x2) = (uint16_t)(local_rsi);
    if ((uint32_t)((uint32_t)((uint32_t)(local_r10))) != 0) goto loc_002E5EA7;
    local_rsp = (local_rsp) + (96);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg4))));
loc_002E5EA7:
    result = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg4))))) << (4);
    local_rdi = (Arg4) + (result);
    if ((uint32_t)((uint32_t)((uint32_t)(Arg4))) == 0) goto loc_002E6B4E;
loc_002E5EBA:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r10))))) << (16));
    Arg2 = ((uint16_t)((uint32_t)((uint32_t)(Arg4)))) << (32);
    Arg2 = (Arg2) | (0);
    Arg2 = (Arg2) | (Arg1);
    Arg2 = (Arg2) ^ (*(uint64_t *)(v_rip + 0xB42421));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) - ((uint32_t)(Arg3)));
    Arg2 = (Arg2) ^ (local_rdi);
    Arg1 = (uint32_t)((Arg1) >> (12));
    *(void **)(local_rdi) = Arg2;
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)(local_rdi)));
    Arg1 = (uint32_t)((Arg1) ^ (*(uint32_t *)(v_rip + 0xB4240D)));
    *(uint32_t *)(local_rdi + 0x8) = (uint32_t)((uint8_t)(Arg1));
    result = (*(uint16_t *)(arg3 + 0x20)) + (3);
    result = (result) << (4);
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r10))))) << (4);
    result = (result) + (Arg3);
    Arg2 = (Arg2) + (local_rdi);
    if (Arg2 < result) {
        result = (uint16_t)((uint32_t)((uint32_t)(local_r10)));
        v_stack_pA0 = 0;
        v_stack_pA4 = (uint32_t)(result);
        result = *(uint64_t *)(v_rip + 0xB423CE);
        Arg1 = v_stack_pA0;
        result = (result) >> (32);
        Arg1 = (Arg1) >> (32);
        Arg1 = (uint16_t)((Arg1) ^ ((uint16_t)(result)));
        result = Arg2;
        result = (result) >> (32);
        Arg1 = (uint16_t)((Arg1) ^ ((uint16_t)(result)));
        *(uint16_t *)(arg2 + 0x4) = (uint16_t)(Arg1);
    }
    v_stack_pB0 = 0;
loc_002E5F5A:
    result = (local_rdi) ^ (*(uint64_t *)(local_rdi));
    result = (result) ^ (*(uint64_t *)(v_rip + 0xB42399));
    Arg1 = (0) >> (32);
    Arg1 = (uint32_t)((Arg1) >> (16));
    result = (result) >> (32);
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)(result))) >> (16));
    result = (local_rdi) >> (32);
    result = (uint32_t)((result) >> (16));
    Arg2 = (*(uint64_t *)(v_rip + 0xB42399)) >> (32);
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(result)));
    Arg2 = (uint32_t)((Arg2) >> (16));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(Arg2)));
    v_stack_pA0 = (uint32_t)(local_r12);
    *(uint8_t *)(local_rdi + 0x6) = (uint8_t)(Arg1);
    if ((uint32_t)((uint16_t)(result)) == 0) goto loc_002E60A2;
    result = ((uint32_t)((uint32_t)((uint16_t)(result)))) << (4);
    local_r12 = (local_rdi) - (result);
    local_rsi = (local_r12) ^ (*(uint64_t *)(local_r12));
    local_rsi = (local_rsi) ^ (*(uint64_t *)(v_rip + 0xB42330));
    result = (local_rsi) >> (32);
    if ((((uint32_t)(result)) & (0xFF0000ULL)) != 0) goto loc_002E6B22;
    Arg1 = (v_stack_pA8) + (16);
    result = RtlRbRemoveNode(Arg1, local_r12 + 8, (uint16_t)(result), Arg3 + 48);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) - ((uint32_t)(Arg3)));
    Arg2 = (uint32_t)((Arg2) + (0x101FULL));
    Arg2 = (uint32_t)((Arg2) & (0xFFFFF000ULL));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r12))))) ^ ((uint32_t)(local_r12)));
    Arg1 = (uint32_t)((Arg1) >> (16));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)(*(uint16_t *)(v_rip + 0xB42303))));
    Arg1 = (uint32_t)((Arg1) << (4));
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(Arg3)));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(local_r12)));
    Arg1 = (uint32_t)((Arg1) & (0xFFFFF000ULL));
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) - ((uint32_t)(Arg2)));
    if (((uint32_t)(Arg2)) >= ((uint32_t)(Arg1))) { result = 0; }
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r12))) ^ ((uint32_t)(local_r12)));
    Arg4 = (uint32_t)((Arg4) ^ (*(uint32_t *)(v_rip + 0xB422B3)));
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) & (0xFFFULL));
    result = (uint32_t)((result) >> (12));
    Arg1 = (uint32_t)(((uint16_t)(Arg4)) - ((uint32_t)(result)));
    result = ((uint32_t)((uint32_t)(Arg1)) + 4095) + (local_r10);
    result = (result) >> (12);
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(result)));
    result = ((uint32_t)((uint32_t)(Arg1)) + 4095) >> (12);
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(result)));
    if ((uint16_t)((int16_t)(*(uint16_t *)(arg1 + 0x6))) == 0) goto loc_002E6B76;
loc_002E608D:
    local_rsi = (uint32_t)((local_rsi) >> (16));
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) + ((uint32_t)(local_rsi)));
loc_002E60A2:
    result = ((uint32_t)((uint32_t)(*(uint16_t *)(arg3 + 0x20)))) << (4);
    local_rsi = ((uint32_t)((uint32_t)(local_r15))) << (4);
    result = (result) + (Arg3 + 48);
    local_rsi = (local_rsi) + (local_r12);
    if (local_rsi >= result) goto loc_002E61A2;
    result = (local_rsi) ^ (*(uint64_t *)(local_rsi));
    result = (result) ^ (*(uint64_t *)(v_rip + 0xB42230));
    v_stack_pA0 = result;
    result = (result) >> (32);
    if ((((uint32_t)(result)) & (0xFF0000ULL)) != 0) goto loc_002E61A2;
    Arg1 = (v_stack_pA8) + (16);
    result = RtlRbRemoveNode(Arg1, local_rsi + 8, (uint32_t)((uint32_t)(Arg1)), Arg3 + 48);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) - ((uint32_t)(Arg3)));
    Arg2 = (uint32_t)((Arg2) + (0x101FULL));
    Arg2 = (uint32_t)((Arg2) & (0xFFFFF000ULL));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi))))) ^ ((uint32_t)(local_rsi)));
    Arg1 = (uint32_t)((Arg1) >> (16));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)(*(uint16_t *)(v_rip + 0xB421FA))));
    Arg1 = (uint32_t)((Arg1) << (4));
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(Arg3)));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(local_rsi)));
    Arg1 = (uint32_t)((Arg1) & (0xFFFFF000ULL));
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) - ((uint32_t)(Arg2)));
    if (((uint32_t)(Arg2)) >= ((uint32_t)(Arg1))) { result = 0; }
    local_rsi = (uint32_t)((local_rsi) ^ (*(uint32_t *)(v_rip + 0xB421B7)));
    result = (uint32_t)((result) >> (12));
    local_rsi = (uint32_t)((local_rsi) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))));
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) & (0xFFFULL));
    Arg1 = (uint32_t)(((uint16_t)(local_rsi)) - ((uint32_t)(result)));
    result = ((uint32_t)((uint32_t)(Arg1)) + 4095) + (local_r10);
    result = (result) >> (12);
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(result)));
    result = ((uint32_t)((uint32_t)(Arg1)) + 4095) >> (12);
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(result)));
    if ((uint16_t)((int16_t)(*(uint16_t *)(arg1 + 0x6))) == 0) goto loc_002E6B7F;
loc_002E618B:
    result = (uint32_t)((v_stack_pA0) >> (16));
    local_r15 = (uint32_t)((local_r15) + ((uint32_t)(result)));
loc_002E61A2:
    if (((*(uint8_t *)(arg1 + 0x4)) & (1)) == 0) goto loc_002E62BC;
    Arg2 = ((uint32_t)((uint32_t)(local_r15))) << (4);
    Arg2 = (Arg2) + (local_r12);
    result = ((uint16_t)(*(uint16_t *)(arg3 + 0x20))) << (4);
    result = (result) + (Arg3 + 48);
    v_stack_pA0 = Arg2;
    if (Arg2 >= result) goto loc_002E62BC;
    local_rsi = (Arg2) ^ (*(uint64_t *)(arg2));
    local_rsi = (local_rsi) ^ (*(uint64_t *)(v_rip + 0xB42121));
    result = (local_rsi) >> (32);
    if ((((uint32_t)(result)) & (0xFF0000ULL)) != 0) goto loc_002E62BC;
    Arg2 = (Arg2) + (8);
    Arg1 = (v_stack_pA8) + (16);
    result = RtlRbRemoveNode(Arg1, Arg2, (uint32_t)((uint32_t)(Arg1)), Arg3 + 48);
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_pA0))) - ((uint32_t)(Arg3)));
    Arg3 = (uint32_t)((Arg3) + (0x101FULL));
    Arg3 = (uint32_t)((Arg3) & (0xFFFFF000ULL));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_pA0))))) ^ ((uint32_t)(v_stack_pA0)));
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_pA0))))) ^ ((uint32_t)(v_stack_pA0)));
    Arg1 = (uint32_t)((Arg1) >> (16));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)(*(uint16_t *)(v_rip + 0xB420ED))));
    Arg4 = (uint32_t)((Arg4) >> (16));
    Arg1 = (uint32_t)((Arg1) << (4));
    Arg4 = (uint32_t)((Arg4) ^ ((uint32_t)(*(uint16_t *)(v_rip + 0xB420ED))));
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(Arg3)));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(v_stack_pA0)));
    Arg4 = (uint32_t)((Arg4) << (4));
    Arg1 = (uint32_t)((Arg1) & (0xFFFFF000ULL));
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) - ((uint32_t)(Arg3)));
    if (((uint32_t)(Arg3)) >= ((uint32_t)(Arg1))) { result = 0; }
    local_r10 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_pA0))) ^ (v_stack_pA0));
    local_r10 = (uint32_t)((local_r10) ^ (*(uint32_t *)(v_rip + 0xB42089)));
    local_r11 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_pA0))) & (0xFFFULL));
    result = (uint32_t)((result) >> (12));
    Arg1 = (uint32_t)(((uint16_t)(local_r10)) - ((uint32_t)(result)));
    result = (local_r11 + 4095) + (Arg4);
    result = (result) >> (12);
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(result)));
    result = (Arg4 + 4095) >> (12);
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(result)));
    if ((uint16_t)((int16_t)(*(uint16_t *)(arg1 + 0x6))) == 0) goto loc_002E6B88;
loc_002E62B6:
    local_rsi = (uint32_t)((local_rsi) >> (16));
    local_r15 = (uint32_t)((local_r15) + ((uint32_t)(local_rsi)));
loc_002E62BC:
    if (((uint32_t)((uint32_t)(v_stack_pA0))) != ((uint32_t)(local_r15))) goto loc_002E675B;
loc_002E62C5:
    if (((uint32_t)(local_r15)) == ((uint32_t)(*(uint16_t *)(arg3 + 0x20)))) goto loc_002E6ADA;
    if (((uint32_t)(local_r15)) > v_stack_pB0) goto loc_002E65D2;
loc_002E62E1:
    if (((*(uint8_t *)(arg1 + 0x4)) & (1)) == 0) goto loc_002E646D;
    if (((local_r12 + 32) & (0xFFFULL)) == 0) goto loc_002E646D;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) >> (16));
    Arg4 = (local_r12 + 4111) & (0xFFFFFFFFFFFFF000ULL);
    Arg2 = (uint32_t)((*(uint16_t *)(local_r12 + 0x2)) ^ ((uint32_t)(result)));
    Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)(*(uint16_t *)(v_rip + 0xB41FF3))));
    result = (Arg4) - (local_r12);
    Arg1 = ((uint32_t)((uint32_t)(Arg2))) << (4);
    if (result < Arg1) goto loc_002E69E5;
loc_002E6338:
    if (0 == 0) goto loc_002E646D;
    result = (uint32_t)((0) >> (16));
    Arg1 = (uint32_t)((*(uint16_t *)(0 + 0x2)) ^ ((uint32_t)(result)));
    local_r11 = (uint32_t)((0) & (0xFFFULL));
    local_r11 = (local_r11) + (0xFFFULL);
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)(*(uint16_t *)(v_rip + 0xB41FA3))));
    Arg1 = (uint32_t)((Arg1) << (4));
    local_r10 = (uint32_t)((0) - ((uint32_t)(Arg3)));
    local_r10 = (uint32_t)((local_r10) + (0x101FULL));
    local_r11 = (local_r11) + ((uint32_t)((uint32_t)(Arg1)));
    local_r10 = (uint32_t)((local_r10) & (0xFFFFF000ULL));
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) - ((uint32_t)(Arg3)));
    local_r11 = (local_r11) >> (12);
    Arg3 = (uint32_t)((Arg3) + (0));
    result = (Arg1 + 4095) >> (12);
    Arg3 = (uint32_t)((Arg3) & (0xFFFFF000ULL));
    local_r11 = (uint32_t)((local_r11) - ((uint32_t)(result)));
    if (((uint32_t)(local_r10)) < ((uint32_t)(Arg3))) goto loc_002E6A8E;
loc_002E63B9:
    Arg2 = (uint32_t)((0) >> (12));
    if ((uint16_t)((int16_t)(*(uint16_t *)(arg1 + 0x6))) == 0) goto loc_002E6B91;
loc_002E63D8:
    Arg2 = (uint16_t)((Arg2) - ((uint16_t)(Arg1)));
    Arg2 = (uint16_t)((Arg2) + ((uint16_t)(local_r11)));
    Arg2 = (uint16_t)((Arg2) ^ (0));
    Arg2 = (uint16_t)((Arg2) ^ (*(uint16_t *)(v_rip + 0xB41F0B)));
    *(uint16_t *)(0) = (uint16_t)(Arg2);
    Arg1 = (uint32_t)((0) ^ (*(uint32_t *)(0)));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)(*(uint64_t *)(v_rip + 0xB41EFD))));
    if ((((uint8_t)(*(uint64_t *)(v_stack_pA8 + 0x18))) & (1)) != 0) goto loc_002E6B11;
loc_002E6418:
    Arg3 = (uint32_t)(((uint8_t)(*(uint64_t *)(v_stack_pA8 + 0x18))) & (1));
    result = 0;
    if (*(uint64_t *)(v_stack_pA8 + 0x10) == 0) goto loc_002E6459;
loc_002E6430:
    result = (uint32_t)((*(uint64_t *)(v_stack_pA8 + 0x10) - 8) ^ (*(uint32_t *)(*(uint64_t *)(v_stack_pA8 + 0x10) - 0x8)));
    result = (uint32_t)((result) ^ ((uint32_t)(*(uint64_t *)(v_rip + 0xB41EFD))));
    if (((uint32_t)(Arg1)) < ((uint32_t)(result))) goto loc_002E67D2;
    if ((uint32_t)(Arg3) == 0) goto loc_002E69D7;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_pA8 + 0x10) + 0x8) != 0) goto loc_002E69D4;
loc_002E6457:
loc_002E6459:
    Arg4 = (0) + (8);
    result = RtlRbInsertNodeEx(v_stack_pA8 + 16, *(uint64_t *)(v_stack_pA8 + 0x10), 1, Arg4);
    goto loc_002E647C;
loc_002E646D:
loc_002E647C:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) >> (16));
    Arg1 = (uint32_t)((*(uint16_t *)(local_r12 + 0x2)) ^ ((uint32_t)(result)));
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) & (0xFFFULL));
    local_r10 = (local_r10) + (0xFFFULL);
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)(*(uint16_t *)(v_rip + 0xB41E6A))));
    Arg1 = (uint32_t)((Arg1) << (4));
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) - ((uint32_t)(Arg3)));
    Arg4 = (uint32_t)((Arg4) + (0x101FULL));
    local_r10 = (local_r10) + ((uint32_t)((uint32_t)(Arg1)));
    Arg4 = (uint32_t)((Arg4) & (0xFFFFF000ULL));
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) - ((uint32_t)(Arg3)));
    local_r10 = (local_r10) >> (12);
    Arg3 = (uint32_t)((Arg3) + ((uint32_t)(local_r12)));
    result = (Arg1 + 4095) >> (12);
    Arg3 = (uint32_t)((Arg3) & (0xFFFFF000ULL));
    local_r10 = (uint32_t)((local_r10) - ((uint32_t)(result)));
    if (((uint32_t)(Arg4)) < ((uint32_t)(Arg3))) goto loc_002E67F7;
loc_002E64E9:
    local_rbx = (uint32_t)((local_rbx) >> (12));
    if ((uint16_t)((int16_t)(*(uint16_t *)(arg1 + 0x6))) == 0) goto loc_002E6B6D;
loc_002E6508:
    local_rbx = (uint16_t)((local_rbx) - ((uint16_t)(Arg1)));
    local_rbx = (uint16_t)((local_rbx) + ((uint16_t)(local_r10)));
    local_rbx = (uint16_t)((local_rbx) ^ ((uint16_t)(local_r12)));
    local_rbx = (uint16_t)((local_rbx) ^ (*(uint16_t *)(v_rip + 0xB41DE0)));
    *(uint16_t *)(local_r12) = (uint16_t)(local_rbx);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) ^ (*(uint32_t *)(local_r12)));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)(*(uint64_t *)(v_rip + 0xB41DD4))));
    if ((((uint8_t)(*(uint64_t *)(v_stack_pA8 + 0x10 + 0x8))) & (1)) != 0) goto loc_002E6AFD;
loc_002E653E:
    result = 0;
    Arg4 = (uint32_t)(((uint8_t)(*(uint64_t *)(v_stack_pA8 + 0x10 + 0x8))) & (1));
    if (*(uint64_t *)(v_stack_pA8 + 0x10) == 0) goto loc_002E6575;
loc_002E6550:
    result = (uint32_t)((*(uint64_t *)(v_stack_pA8 + 0x10) - 8) ^ (*(uint32_t *)(*(uint64_t *)(v_stack_pA8 + 0x10) - 0x8)));
    result = (uint32_t)((result) ^ ((uint32_t)(*(uint64_t *)(v_rip + 0xB41DD4))));
    if (((uint32_t)(Arg1)) < ((uint32_t)(result))) goto loc_002E659D;
    if ((uint32_t)(Arg4) == 0) goto loc_002E674D;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_pA8 + 0x10) + 0x8) != 0) goto loc_002E674A;
loc_002E6573:
loc_002E6575:
    result = RtlRbInsertNodeEx(v_stack_pA8 + 16, *(uint64_t *)(v_stack_pA8 + 0x10), 1, local_r12 + 8);
    local_rsp = (local_rsp) + (96);
    return (uint32_t)(Arg5);
loc_002E659D:
    if ((uint32_t)(local_r12 + 8) == 0) goto loc_002E65B1;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_pA8 + 0x10)) == 0) goto loc_002E6B02;
    result = (*(uint64_t *)(*(uint64_t *)(v_stack_pA8 + 0x10))) ^ (*(uint64_t *)(v_stack_pA8 + 0x10));
loc_002E65B1:
    if (result == 0) goto loc_002E6B02;
loc_002E65BA:
    goto loc_002E6550;
loc_002E65BF:
    if (((uint32_t)(result)) == 32) goto loc_002E5DA3;
    Arg2 = (uint32_t)((result) + 1);
    local_r15 = (uint32_t)((-1) - 1);
    goto loc_002E5DA3;
loc_002E65D2:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) >> (16));
    Arg3 = (uint32_t)((*(uint16_t *)(local_r12 + 0x2)) ^ ((uint32_t)(result)));
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) - ((uint32_t)(Arg3)));
    Arg3 = (uint32_t)((Arg3) ^ ((uint32_t)(*(uint16_t *)(v_rip + 0xB41D16))));
    Arg3 = (uint32_t)((Arg3) << (4));
    Arg3 = (uint32_t)((Arg3) - ((uint32_t)(Arg3)));
    Arg3 = (uint32_t)((Arg3) + ((uint32_t)(local_r12)));
    Arg4 = (uint32_t)((local_r12 + 4127) & (0xFFFFF000ULL));
    Arg3 = (uint32_t)((Arg3) & (0xFFFFF000ULL));
    if (((uint32_t)(Arg4)) >= ((uint32_t)(Arg3))) goto loc_002E62E1;
    result = (Arg3 - 1) >> (12);
    Arg1 = (uint8_t)((63) - ((uint8_t)(result)));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(Arg3))) - ((uint32_t)(Arg4)));
    Arg4 = (uint32_t)((Arg4) >> (12));
    local_rsi = (-1) >> ((uint8_t)(Arg1));
    result = (-1) << ((uint8_t)((uint8_t)(Arg4)));
    local_rsi = (local_rsi) & (result);
    local_rsi = (local_rsi) & (*(uint64_t *)(arg3 + 0x10));
    if (((uint32_t)(Arg2)) < 0x1000ULL) goto loc_002E62E1;
    if (local_rsi == 0) goto loc_002E62E1;
    v_stack_p148 = result;
    result = RtlpHpVsCommitLimitCheck(Arg1, Arg3, (uint32_t)((uint32_t)(result)), Arg4);
    if ((uint32_t)(result) == 0) goto loc_002E62E1;
    local_r12 = (uint32_t)((local_r12) >> (12));
    result = (local_r12) >> (32);
    local_r12 = (uint32_t)((local_r12) ^ ((uint32_t)(local_r12)));
    result = (uint32_t)((result) >> (16));
    v_stack_p138 = local_rbx;
    v_stack_p13C = 0x10000ULL;
    Arg1 = (v_stack_p138) >> (32);
    Arg1 = (uint32_t)((Arg1) >> (16));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(result)));
    result = (*(uint64_t *)(v_rip + 0xB41C40)) >> (32);
    result = (uint32_t)((result) >> (16));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(result)));
    *(uint8_t *)(local_r12 + 0x6) = (uint8_t)(Arg1);
    local_r12 = (uint32_t)((local_r12) ^ (*(uint32_t *)(v_rip + 0xB41C2D)));
    *(uint32_t *)(local_r12 + 0x8) = (uint32_t)((uint8_t)(local_r12));
    result = (uint8_t)(local_r12);
    if (((*(uint8_t *)(arg1 + 0x5)) & (1)) == 0) {
        Arg1 = *(uint8_t *)(arg1 + 0x3);
        Arg2 = Arg6;
        result = RtlpHpReleaseQueuedLockExclusive(Arg1, Arg2, (uint32_t)((uint32_t)(result)), Arg4);
    }
    v_stack_pB8 = (uint32_t)(local_rbx);
    result = RtlpHpVsSubsegmentCommitPages(Arg1, Arg3, local_rsi, (uint32_t)(v_stack_p148));
    if (((*(uint8_t *)(arg1 + 0x5)) & (1)) == 0) {
        Arg1 = v_stack_p140;
        Arg2 = *(uint8_t *)(arg1 + 0x3);
        Arg1 = (Arg1) + (8);
        Arg3 = Arg6;
        result = RtlpHpAcquireQueuedLockExclusive(Arg1, Arg2, Arg3, (uint32_t)(v_stack_p148));
    }
    v_stack_p148 = (uint32_t)(local_r15);
    goto loc_002E5F5A;
loc_002E674A:
    result = (result) ^ (Arg2);
loc_002E674D:
    if (result != 0) goto loc_002E65BA;
    goto loc_002E6573;
loc_002E675B:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) >> (16));
    result = (uint16_t)((result) ^ ((uint16_t)(local_r15)));
    Arg2 = ((uint32_t)((uint32_t)(local_r15))) << (4);
    result = (uint16_t)((result) ^ (*(uint16_t *)(v_rip + 0xB41B8C)));
    Arg2 = (Arg2) + (local_r12);
    *(uint16_t *)(local_r12 + 0x2) = (uint16_t)(result);
    result = (*(uint16_t *)(arg3 + 0x20)) << (4);
    result = (result) + (Arg3 + 48);
    if (Arg2 >= result) goto loc_002E62C5;
    v_stack_p138 = local_rbx;
    v_stack_p13C = (uint32_t)((uint16_t)(local_r15));
    result = (Arg2) >> (32);
    Arg1 = (v_stack_p138) >> (32);
    Arg1 = (uint16_t)((Arg1) ^ ((uint16_t)(result)));
    result = (*(uint64_t *)(v_rip + 0xB41B3E)) >> (32);
    Arg1 = (uint16_t)((Arg1) ^ ((uint16_t)(result)));
    *(uint16_t *)(arg2 + 0x4) = (uint16_t)(Arg1);
    goto loc_002E62C5;
loc_002E67D2:
    if ((uint32_t)(Arg3) == 0) goto loc_002E67E6;
    if (*(uint64_t *)(arg2) == 0) goto loc_002E6B1B;
    result = (*(uint64_t *)(arg2)) ^ (Arg2);
loc_002E67E6:
    if (result == 0) goto loc_002E6B1B;
loc_002E67EF:
    goto loc_002E6430;
loc_002E67F7:
    result = (Arg3 - 1) >> (12);
    Arg1 = (uint8_t)((63) - ((uint8_t)(result)));
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(Arg3))) - ((uint32_t)((uint32_t)(v_stack_p148))));
    Arg4 = (uint32_t)(((uint32_t)(v_stack_p148)) >> (12));
    result = (local_r15) >> ((uint8_t)(Arg1));
    local_r15 = (local_r15) << ((uint8_t)((uint8_t)(Arg4)));
    result = (result) & (local_r15);
    result = (result) & (*(uint64_t *)(arg3 + 0x10));
    goto loc_002E64E9;
loc_002E6829:
    *(uint32_t *)(local_r12 + 0x8) = (uint32_t)((uint32_t)(v_stack_p138));
    if (((*(uint8_t *)(arg1 + 0x5)) & (1)) != 0) goto loc_002E6B37;
    result = RtlpHpReleaseQueuedLockExclusive(*(uint8_t *)(arg1 + 0x3), Arg6, Arg3, Arg4);
    v_stack_p138 = Arg1 + 5;
loc_002E6864:
    v_stack_pD8 = result;
    result = 0;
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)(Arg6))) << (12));
    v_stack_pF0 = 0;
    local_r10 = (local_r10) + (Arg3);
    v_stack_p150 = (uint32_t)(Arg6);
    v_stack_pC8 = 0;
    result = (uint32_t)((result) - ((uint32_t)(Arg6)));
    v_stack_pD0 = local_r10;
    v_stack_pE0 = v_xmm0;
    local_r15 = (1) << ((uint8_t)(result + 1));
    local_r15 = (local_r15) - 1;
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(result + 1))) << (12));
    v_stack_p158 = (uint32_t)(Arg3);
    local_r15 = (local_r15) << ((uint8_t)((uint32_t)((uint32_t)(Arg6))));
    if (((*(uint8_t *)(arg1 + 0x5)) & (1)) == 0) {
        Arg2 = *(uint8_t *)(arg1 + 0x3);
        Arg1 = Arg3 + 24;
        Arg3 = v_stack_pE0;
        result = RtlpHpAcquireQueuedLockExclusive(Arg1, Arg2, Arg3, Arg4);
        local_r10 = v_stack_pD0;
        Arg3 = Arg5;
    }
    result = (*(uint64_t *)(arg1 + 0x20)) ^ (*(uint64_t *)(v_rip + 0xB41A03));
    Arg1 = (Arg1) ^ (*(uint64_t *)(arg1 + 0x8));
    result = (result) ^ (Arg1);
    Arg4 = 0;
    if (result != (v_rip + 257626)) goto loc_002E6B44;
    result = RtlpHpSegLfhVsCommit(Arg1, local_r10, Arg3, Arg4);
loc_002E691B:
    v_stack_p158 = (uint32_t)(result);
    if (sign_flag) goto loc_002E6AC3;
loc_002E6949:
    result = (uint32_t)(v_stack_pD8);
    if ((((uint8_t)(*(uint8_t *)(v_stack_p138))) & (1)) == 0) {
        Arg1 = *(uint8_t *)(arg1 + 0x3);
        Arg2 = v_stack_pE0;
        result = RtlpHpReleaseQueuedLockExclusive(Arg1, Arg2, *(uint8_t *)(v_stack_p138), Arg4);
        Arg3 = *(uint8_t *)(arg1 + 0x5);
    }
    v_stack_p138 = (uint32_t)((uint32_t)(v_stack_p148));
    v_stack_p158 = (uint32_t)((uint32_t)(v_stack_pCC));
    local_r12 = (uint32_t)((uint32_t)((uint32_t)(v_stack_pCC)));
    if (sign_flag) {
        result = (uint32_t)(v_stack_pCC) + (uint32_t)(v_stack_p148) * 1;
        v_stack_p158 = (uint32_t)(local_rbx);
        v_stack_p138 = (uint32_t)(result);
        local_r12 = (uint32_t)(local_rbx);
    }
    if ((((uint8_t)(Arg3)) & (1)) == 0) {
        Arg1 = v_stack_p140;
        Arg2 = *(uint8_t *)(arg1 + 0x3);
        Arg1 = (Arg1) + (8);
        Arg3 = Arg6;
        result = RtlpHpAcquireQueuedLockExclusive(Arg1, Arg2, Arg3, Arg4);
    }
    goto loc_002E5E7C;
loc_002E69D4:
    result = (result) ^ (Arg2);
loc_002E69D7:
    if (result != 0) goto loc_002E67EF;
    goto loc_002E6457;
loc_002E69E5:
    Arg4 = (Arg4) + (-32);
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) >> (16));
    Arg1 = (Arg4) - (local_r12);
    Arg1 = (Arg1) >> (4);
    result = (uint16_t)((result) ^ ((uint16_t)(Arg1)));
    Arg2 = (uint32_t)((Arg2) - ((uint32_t)(Arg1)));
    result = (uint16_t)((result) ^ ((uint16_t)((uint32_t)(v_stack_p138))));
    *(uint16_t *)(local_r12 + 0x2) = (uint16_t)(result);
    *(uint64_t *)(arg4) = v_xmm0;
    Arg3 = ((uint32_t)((uint32_t)(Arg2))) << (4);
    *(uint64_t *)(arg4 + 0x10) = v_xmm0;
    *(uint16_t *)(arg4 + 0x2) = (uint16_t)(Arg2);
    Arg3 = (Arg3) + (Arg4);
    *(uint16_t *)(arg4 + 0x4) = (uint16_t)(Arg1);
    result = (Arg4) ^ (*(uint64_t *)(arg4));
    result = (result) ^ (*(uint64_t *)(v_rip + 0xB418CE));
    *(uint64_t *)(arg4) = result;
    result = (*(uint16_t *)(arg3 + 0x20)) + (3);
    result = (result) << (4);
    result = (result) + (Arg3);
    if (Arg3 >= result) goto loc_002E6338;
    v_stack_p138 = local_rbx;
    v_stack_p13C = (uint32_t)((uint16_t)(Arg2));
    result = (Arg3) >> (32);
    Arg1 = (v_stack_p138) >> (32);
    Arg1 = (uint16_t)((Arg1) ^ ((uint16_t)(result)));
    result = (*(uint64_t *)(v_rip + 0xB41883)) >> (32);
    Arg1 = (uint16_t)((Arg1) ^ ((uint16_t)(result)));
    *(uint16_t *)(arg3 + 0x4) = (uint16_t)(Arg1);
    goto loc_002E6338;
loc_002E6A8E:
    result = (Arg3 - 1) >> (12);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(Arg3))) - ((uint32_t)(local_r10)));
    local_r10 = (uint32_t)((local_r10) >> (12));
    Arg1 = (uint8_t)((63) - ((uint8_t)(result)));
    Arg3 = ((uint32_t)((uint32_t)(local_rbx))) >> ((uint8_t)(Arg1));
    result = ((uint32_t)((uint32_t)(local_rbx))) << ((uint8_t)((uint8_t)(local_r10)));
    Arg3 = (Arg3) & (result);
    Arg3 = (Arg3) & (*(uint64_t *)(arg3 + 0x10));
    goto loc_002E63B9;
loc_002E6AC3:
    goto loc_002E6949;
loc_002E6AD0:
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)((uint8_t)(local_r10))));
    local_r15 = (uint32_t)(((uint32_t)(Arg5)) - ((uint32_t)((uint8_t)(local_r10))));
    goto loc_002E5DA3;
loc_002E6ADA:
    result = RtlpHpVsSubsegmentCleanup(Arg1, Arg3, Arg3, Arg4);
    local_rsp = (local_rsp) + (96);
    return (uint32_t)(Arg5);
loc_002E6AFD:
    if (Arg3 != NULL) goto loc_002E6B09;
loc_002E6B02:
    result = 0;
    goto loc_002E6575;
loc_002E6B09:
    Arg2 = (Arg3) ^ (local_r10);
    goto loc_002E653E;
loc_002E6B11:
    if (*(uint64_t *)(local_r12 + 0x10) != 0) goto loc_002E6B2A;
loc_002E6B1B:
    result = 0;
    goto loc_002E6459;
loc_002E6B22:
    goto loc_002E60A2;
loc_002E6B2A:
    local_r11 = ((uint32_t)((uint32_t)(local_r15)) + 16) ^ (*(uint64_t *)(local_r12 + 0x10));
    goto loc_002E6418;
loc_002E6B37:
    v_stack_p1D0 = (uint32_t)((uint32_t)(local_r15));
    goto loc_002E6864;
loc_002E6B44:
    result = guard_dispatch_icall(Arg1, *(uint64_t *)(local_r12 + 0x10), Arg3, Arg4);
    goto loc_002E691B;
loc_002E6B4E:
    local_r12 = (*(uint64_t *)(local_r12)) ^ (*(uint64_t *)(v_rip + 0xB417A8));
    local_r12 = (local_r12) ^ (local_r12);
    local_r12 = (local_r12) >> (32);
    goto loc_002E5EBA;
loc_002E6B64:
    goto loc_002E5D59;
loc_002E6B6D:
    goto loc_002E6508;
loc_002E6B76:
    goto loc_002E608D;
loc_002E6B7F:
    goto loc_002E618B;
loc_002E6B88:
    goto loc_002E62B6;
loc_002E6B91:
    goto loc_002E63D8;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `8` | `R` |
| `Arg1` | `+ 0x3` | `8` | `R` |
| `Arg1` | `+ 0x4` | `8` | `R` |
| `Arg1` | `+ 0x5` | `8` | `R` |
| `Arg1` | `+ 0x5` | `64` | `R` |
| `Arg1` | `+ 0x6` | `16` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x50` | `64` | `R/W` |
| `Arg1` | `+ 0x58` | `64` | `R/W` |
| `Arg2` | `+ 0x10` | `64` | `R` |
| `Arg3` | `+ 0x10` | `64` | `R` |
| `Arg3` | `+ 0x10` | `64` | `R/W` |
| `Arg3` | `+ 0x18` | `64` | `R` |
| `Arg3` | `+ 0x20` | `16` | `R` |
| `Arg3` | `+ 0x30` | `64` | `R` |
| `Arg4` | `- 0x1` | `32` | `R` |
| `Arg4` | `+ 0x0` | `16` | `W` |
| `Arg4` | `+ 0x0` | `32` | `R` |
| `Arg4` | `+ 0x0` | `64` | `R` |
| `Arg4` | `+ 0x0` | `64` | `W` |
| `Arg4` | `+ 0x0` | `128` | `R` |
| `Arg4` | `+ 0x2` | `16` | `R` |
| `Arg4` | `+ 0x2` | `16` | `W` |
| `Arg4` | `+ 0x4` | `16` | `W` |
| `Arg4` | `+ 0x6` | `8` | `W` |
| `Arg4` | `+ 0x8` | `32` | `R/W` |
| `Arg4` | `+ 0x8` | `32` | `W` |
| `Arg4` | `+ 0x8` | `64` | `R` |
| `Arg4` | `+ 0x10` | `128` | `R` |
| `Arg4` | `+ 0x20` | `64` | `R` |
| `Arg4` | `+ 0x100F` | `64` | `R` |

추가 오프셋 1개는 표에서 생략했습니다.

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002E5C80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
