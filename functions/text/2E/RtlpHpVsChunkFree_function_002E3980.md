# RtlpHpVsChunkFree

- RVA: `0x002E3980`–`0x002E436F` (길이 `2,543` bytes)
- VA: `0x00000001402E3980`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00070EE0`
- 디코드: `655`개 명령, `2,543/2,543` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **10**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x002E3A2B` → [RtlRbRemoveNode](RtlRbRemoveNode_function_002E4C10.md) (function, `0x002E4C10`)
- `0x002E3B24` → [RtlRbRemoveNode](RtlRbRemoveNode_function_002E4C10.md) (function, `0x002E4C10`)
- `0x002E3C23` → [RtlRbRemoveNode](RtlRbRemoveNode_function_002E4C10.md) (function, `0x002E4C10`)
- `0x002E3E65` → [RtlRbInsertNodeEx](RtlRbInsertNodeEx_function_002E4570.md) (function, `0x002E4570`)
- `0x002E3F81` → [RtlRbInsertNodeEx](RtlRbInsertNodeEx_function_002E4570.md) (function, `0x002E4570`)
- `0x002E4068` → [RtlpHpVsCommitLimitCheck](RtlpHpVsCommitLimitCheck_function_002E5BBC.md) (function, `0x002E5BBC`)
- `0x002E40DC` → [RtlpHpReleaseQueuedLockExclusive](RtlpHpReleaseQueuedLockExclusive_function_002E2A70.md) (function, `0x002E2A70`)
- `0x002E40F3` → [RtlpHpVsSubsegmentCommitPages](RtlpHpVsSubsegmentCommitPages_function_002E6C74.md) (function, `0x002E6C74`)
- `0x002E4115` → [RtlpHpAcquireQueuedLockExclusive](../32/RtlpHpAcquireQueuedLockExclusive_function_00324820.md) (function, `0x00324820`)
- `0x002E42FD` → [RtlpHpVsSubsegmentCleanup](RtlpHpVsSubsegmentCleanup_function_002E6DA8.md) (function, `0x002E6DA8`)

### Direct callers
- [sub_002E6E90](Unknown_function_002E6E90.md) at `0x002E70F0`
- [RtlpHpVsSlotFreeList](../36/RtlpHpVsSlotFreeList_function_00361ACC.md) at `0x00361C3F`

### Static image references
- `0x002E39AD` → RVA `0x00E28300` (`.data`; read)
- `0x002E3A30` → RVA `0x00E28302` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002E3980  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
002E3985  53                              push rbx
002E3986  56                              push rsi
002E3987  57                              push rdi
002E3988  41 54                           push r12
002E398A  41 55                           push r13
002E398C  41 57                           push r15
002E398E  48 83 EC 38                     sub rsp, 0x38
002E3992  4C 8B E9                        mov r13, rcx
002E3995  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
002E399A  33 C9                           xor ecx, ecx
002E399C  49 8B D9                        mov rbx, r9
002E399F  89 4C 24 70                     mov dword ptr [rsp + 0x70], ecx
002E39A3  4D 8D 48 30                     lea r9, [r8 + 0x30]
002E39A7  4D 8B F8                        mov r15, r8
002E39AA  4C 8B D2                        mov r10, rdx
002E39AD  48 8B 15 4C 49 B4 00            mov rdx, qword ptr [rip + 0xb4494c]
002E39B4  48 8B 03                        mov rax, qword ptr [rbx]
002E39B7  48 33 C2                        xor rax, rdx
002E39BA  48 C1 E9 20                     shr rcx, 0x20
002E39BE  48 33 C3                        xor rax, rbx
002E39C1  C1 E9 10                        shr ecx, 0x10
002E39C4  44 8B E0                        mov r12d, eax
002E39C7  48 C1 EA 20                     shr rdx, 0x20
002E39CB  48 C1 E8 20                     shr rax, 0x20
002E39CF  44 0F B7 C0                     movzx r8d, ax
002E39D3  48 8B C3                        mov rax, rbx
002E39D6  48 C1 E8 20                     shr rax, 0x20
002E39DA  C1 EA 10                        shr edx, 0x10
002E39DD  C1 E8 10                        shr eax, 0x10
002E39E0  32 CA                           xor cl, dl
002E39E2  32 C8                           xor cl, al
002E39E4  41 C1 EC 10                     shr r12d, 0x10
002E39E8  88 4B 06                        mov byte ptr [rbx + 6], cl
002E39EB  41 8B F4                        mov esi, r12d
002E39EE  45 85 C0                        test r8d, r8d
002E39F1  0F 84 E6 00 00 00               je 0x1402e3add
002E39F7  41 8B C0                        mov eax, r8d
002E39FA  4C 8B F3                        mov r14, rbx
002E39FD  48 C1 E0 04                     shl rax, 4
002E3A01  4C 2B F0                        sub r14, rax
002E3A04  49 8B 3E                        mov rdi, qword ptr [r14]
002E3A07  48 33 3D F2 48 B4 00            xor rdi, qword ptr [rip + 0xb448f2]
002E3A0E  49 33 FE                        xor rdi, r14
002E3A11  48 8B C7                        mov rax, rdi
002E3A14  48 C1 E8 20                     shr rax, 0x20
002E3A18  A9 00 00 FF 00                  test eax, 0xff0000
002E3A1D  0F 85 BA 00 00 00               jne 0x1402e3add
002E3A23  49 8D 56 08                     lea rdx, [r14 + 8]
002E3A27  49 8D 4A 10                     lea rcx, [r10 + 0x10]
002E3A2B  E8 E0 11 00 00                  call 0x1402e4c10
002E3A30  0F B7 05 CB 48 B4 00            movzx eax, word ptr [rip + 0xb448cb]
002E3A37  45 8B D6                        mov r10d, r14d
002E3A3A  45 8B 06                        mov r8d, dword ptr [r14]
002E3A3D  41 8B CE                        mov ecx, r14d
002E3A40  4D 0F BF 5D 06                  movsx r11, word ptr [r13 + 6]
002E3A45  41 2B CF                        sub ecx, r15d
002E3A48  81 C1 1F 10 00 00               add ecx, 0x101f
002E3A4E  45 8B C8                        mov r9d, r8d
002E3A51  45 33 CE                        xor r9d, r14d
002E3A54  81 E1 00 F0 FF FF               and ecx, 0xfffff000
002E3A5A  41 C1 E9 10                     shr r9d, 0x10
002E3A5E  44 33 C8                        xor r9d, eax
002E3A61  41 C1 E1 04                     shl r9d, 4
002E3A65  41 8B C1                        mov eax, r9d
002E3A68  41 2B C7                        sub eax, r15d
002E3A6B  41 03 C6                        add eax, r14d
002E3A6E  25 00 F0 FF FF                  and eax, 0xfffff000
002E3A73  8B D0                           mov edx, eax
002E3A75  2B D1                           sub edx, ecx
002E3A77  3B C8                           cmp ecx, eax
002E3A79  B8 00 00 00 00                  mov eax, 0
002E3A7E  0F 43 D0                        cmovae edx, eax
002E3A81  41 8B C6                        mov eax, r14d
002E3A84  41 33 C0                        xor eax, r8d
002E3A87  C1 EA 0C                        shr edx, 0xc
002E3A8A  33 05 70 48 B4 00               xor eax, dword ptr [rip + 0xb44870]
002E3A90  41 81 E2 FF 0F 00 00            and r10d, 0xfff
002E3A97  0F B7 C8                        movzx ecx, ax
002E3A9A  49 8D 81 FF 0F 00 00            lea rax, [r9 + 0xfff]
002E3AA1  49 03 C2                        add rax, r10
002E3AA4  2B CA                           sub ecx, edx
002E3AA6  48 C1 E8 0C                     shr rax, 0xc
002E3AAA  2B C8                           sub ecx, eax
002E3AAC  49 8D 81 FF 0F 00 00            lea rax, [r9 + 0xfff]
002E3AB3  48 C1 E8 0C                     shr rax, 0xc
002E3AB7  03 C8                           add ecx, eax
002E3AB9  48 63 D1                        movsxd rdx, ecx
002E3ABC  66 45 85 DB                     test r11w, r11w
002E3AC0  0F 84 85 08 00 00               je 0x1402e434b
002E3AC6  F0 4B 01 54 2B 20               lock add qword ptr [r11 + r13 + 0x20], rdx
002E3ACC  4C 8B 54 24 78                  mov r10, qword ptr [rsp + 0x78]
002E3AD1  4D 8D 4F 30                     lea r9, [r15 + 0x30]
002E3AD5  C1 EF 10                        shr edi, 0x10
002E3AD8  49 8B DE                        mov rbx, r14
002E3ADB  03 F7                           add esi, edi
002E3ADD  41 0F B7 4F 20                  movzx ecx, word ptr [r15 + 0x20]
002E3AE2  8B C1                           mov eax, ecx
002E3AE4  8B FE                           mov edi, esi
002E3AE6  48 C1 E0 04                     shl rax, 4
002E3AEA  48 C1 E7 04                     shl rdi, 4
002E3AEE  49 03 C1                        add rax, r9
002E3AF1  48 03 FB                        add rdi, rbx
002E3AF4  48 3B F8                        cmp rdi, rax
002E3AF7  0F 83 D2 00 00 00               jae 0x1402e3bcf
002E3AFD  4C 8B 37                        mov r14, qword ptr [rdi]
002E3B00  4C 33 35 F9 47 B4 00            xor r14, qword ptr [rip + 0xb447f9]
002E3B07  4C 33 F7                        xor r14, rdi
002E3B0A  49 8B C6                        mov rax, r14
002E3B0D  48 C1 E8 20                     shr rax, 0x20
002E3B11  A9 00 00 FF 00                  test eax, 0xff0000
002E3B16  0F 85 B3 00 00 00               jne 0x1402e3bcf
002E3B1C  48 8D 57 08                     lea rdx, [rdi + 8]
002E3B20  49 8D 4A 10                     lea rcx, [r10 + 0x10]
002E3B24  E8 E7 10 00 00                  call 0x1402e4c10
002E3B29  0F B7 05 D2 47 B4 00            movzx eax, word ptr [rip + 0xb447d2]
002E3B30  8B D7                           mov edx, edi
002E3B32  44 8B 0F                        mov r9d, dword ptr [rdi]
002E3B35  41 2B D7                        sub edx, r15d
002E3B38  4D 0F BF 5D 06                  movsx r11, word ptr [r13 + 6]
002E3B3D  41 8B C9                        mov ecx, r9d
002E3B40  33 CF                           xor ecx, edi
002E3B42  81 C2 1F 10 00 00               add edx, 0x101f
002E3B48  C1 E9 10                        shr ecx, 0x10
002E3B4B  81 E2 00 F0 FF FF               and edx, 0xfffff000
002E3B51  33 C8                           xor ecx, eax
002E3B53  44 8B D7                        mov r10d, edi
002E3B56  C1 E1 04                        shl ecx, 4
002E3B59  44 8B C1                        mov r8d, ecx
002E3B5C  41 2B CF                        sub ecx, r15d
002E3B5F  03 CF                           add ecx, edi
002E3B61  81 E1 00 F0 FF FF               and ecx, 0xfffff000
002E3B67  8B C1                           mov eax, ecx
002E3B69  2B C2                           sub eax, edx
002E3B6B  3B D1                           cmp edx, ecx
002E3B6D  B9 00 00 00 00                  mov ecx, 0
002E3B72  0F 43 C1                        cmovae eax, ecx
002E3B75  44 33 0D 84 47 B4 00            xor r9d, dword ptr [rip + 0xb44784]
002E3B7C  C1 E8 0C                        shr eax, 0xc
002E3B7F  44 33 CF                        xor r9d, edi
002E3B82  41 81 E2 FF 0F 00 00            and r10d, 0xfff
002E3B89  41 0F B7 C9                     movzx ecx, r9w
002E3B8D  2B C8                           sub ecx, eax
002E3B8F  49 8D 80 FF 0F 00 00            lea rax, [r8 + 0xfff]
002E3B96  49 03 C2                        add rax, r10
002E3B99  48 C1 E8 0C                     shr rax, 0xc
002E3B9D  2B C8                           sub ecx, eax
002E3B9F  49 8D 80 FF 0F 00 00            lea rax, [r8 + 0xfff]
002E3BA6  48 C1 E8 0C                     shr rax, 0xc
002E3BAA  03 C8                           add ecx, eax
002E3BAC  48 63 D1                        movsxd rdx, ecx
002E3BAF  66 45 85 DB                     test r11w, r11w
002E3BB3  0F 84 9B 07 00 00               je 0x1402e4354
002E3BB9  F0 4B 01 54 2B 20               lock add qword ptr [r11 + r13 + 0x20], rdx
002E3BBF  41 0F B7 4F 20                  movzx ecx, word ptr [r15 + 0x20]
002E3BC4  4D 8D 4F 30                     lea r9, [r15 + 0x30]
002E3BC8  41 C1 EE 10                     shr r14d, 0x10
002E3BCC  41 03 F6                        add esi, r14d
002E3BCF  41 F6 45 04 01                  test byte ptr [r13 + 4], 1
002E3BD4  0F 84 EC 00 00 00               je 0x1402e3cc6
002E3BDA  44 8B F6                        mov r14d, esi
002E3BDD  49 C1 E6 04                     shl r14, 4
002E3BE1  0F B7 C1                        movzx eax, cx
002E3BE4  4C 03 F3                        add r14, rbx
002E3BE7  48 C1 E0 04                     shl rax, 4
002E3BEB  49 03 C1                        add rax, r9
002E3BEE  4C 3B F0                        cmp r14, rax
002E3BF1  0F 83 CF 00 00 00               jae 0x1402e3cc6
002E3BF7  49 8B 3E                        mov rdi, qword ptr [r14]
002E3BFA  48 33 3D FF 46 B4 00            xor rdi, qword ptr [rip + 0xb446ff]
002E3C01  49 33 FE                        xor rdi, r14
002E3C04  48 8B C7                        mov rax, rdi
002E3C07  48 C1 E8 20                     shr rax, 0x20
002E3C0B  A9 00 00 FF 00                  test eax, 0xff0000
002E3C10  0F 85 B0 00 00 00               jne 0x1402e3cc6
002E3C16  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
002E3C1B  49 8D 56 08                     lea rdx, [r14 + 8]
002E3C1F  48 83 C1 10                     add rcx, 0x10
002E3C23  E8 E8 0F 00 00                  call 0x1402e4c10
002E3C28  0F B7 05 D3 46 B4 00            movzx eax, word ptr [rip + 0xb446d3]
002E3C2F  41 8B D6                        mov edx, r14d
002E3C32  45 8B 0E                        mov r9d, dword ptr [r14]
002E3C35  41 2B D7                        sub edx, r15d
002E3C38  4D 0F BF 5D 06                  movsx r11, word ptr [r13 + 6]
002E3C3D  41 8B C9                        mov ecx, r9d
002E3C40  41 33 CE                        xor ecx, r14d
002E3C43  81 C2 1F 10 00 00               add edx, 0x101f
002E3C49  C1 E9 10                        shr ecx, 0x10
002E3C4C  81 E2 00 F0 FF FF               and edx, 0xfffff000
002E3C52  33 C8                           xor ecx, eax
002E3C54  45 8B D6                        mov r10d, r14d
002E3C57  C1 E1 04                        shl ecx, 4
002E3C5A  44 8B C1                        mov r8d, ecx
002E3C5D  41 2B CF                        sub ecx, r15d
002E3C60  41 03 CE                        add ecx, r14d
002E3C63  81 E1 00 F0 FF FF               and ecx, 0xfffff000
002E3C69  8B C1                           mov eax, ecx
002E3C6B  2B C2                           sub eax, edx
002E3C6D  3B D1                           cmp edx, ecx
002E3C6F  B9 00 00 00 00                  mov ecx, 0
002E3C74  0F 43 C1                        cmovae eax, ecx
002E3C77  44 33 0D 82 46 B4 00            xor r9d, dword ptr [rip + 0xb44682]
002E3C7E  C1 E8 0C                        shr eax, 0xc
002E3C81  45 33 CE                        xor r9d, r14d
002E3C84  41 81 E2 FF 0F 00 00            and r10d, 0xfff
002E3C8B  41 0F B7 C9                     movzx ecx, r9w
002E3C8F  2B C8                           sub ecx, eax
002E3C91  49 8D 80 FF 0F 00 00            lea rax, [r8 + 0xfff]
002E3C98  49 03 C2                        add rax, r10
002E3C9B  48 C1 E8 0C                     shr rax, 0xc
002E3C9F  2B C8                           sub ecx, eax
002E3CA1  49 8D 80 FF 0F 00 00            lea rax, [r8 + 0xfff]
002E3CA8  48 C1 E8 0C                     shr rax, 0xc
002E3CAC  03 C8                           add ecx, eax
002E3CAE  48 63 D1                        movsxd rdx, ecx
002E3CB1  66 45 85 DB                     test r11w, r11w
002E3CB5  0F 84 A2 06 00 00               je 0x1402e435d
002E3CBB  F0 4B 01 54 2B 20               lock add qword ptr [r11 + r13 + 0x20], rdx
002E3CC1  C1 EF 10                        shr edi, 0x10
002E3CC4  03 F7                           add esi, edi
002E3CC6  44 3B E6                        cmp r12d, esi
002E3CC9  0F 85 77 04 00 00               jne 0x1402e4146
002E3CCF  41 0F B7 47 20                  movzx eax, word ptr [r15 + 0x20]
002E3CD4  3B F0                           cmp esi, eax
002E3CD6  0F 84 1B 06 00 00               je 0x1402e42f7
002E3CDC  3B 74 24 70                     cmp esi, dword ptr [rsp + 0x70]
002E3CE0  0F 87 D9 02 00 00               ja 0x1402e3fbf
002E3CE6  49 C7 C4 FF FF FF FF            mov r12, 0xffffffffffffffff
002E3CED  41 F6 45 04 01                  test byte ptr [r13 + 4], 1
002E3CF2  0F 84 74 01 00 00               je 0x1402e3e6c
002E3CF8  48 8D 43 20                     lea rax, [rbx + 0x20]
002E3CFC  48 A9 FF 0F 00 00               test rax, 0xfff
002E3D02  0F 84 64 01 00 00               je 0x1402e3e6c
002E3D08  0F B7 53 02                     movzx edx, word ptr [rbx + 2]
002E3D0C  4C 8D 8B 0F 10 00 00            lea r9, [rbx + 0x100f]
002E3D13  44 0F B7 05 E7 45 B4 00         movzx r8d, word ptr [rip + 0xb445e7]
002E3D1B  8B C3                           mov eax, ebx
002E3D1D  C1 E8 10                        shr eax, 0x10
002E3D20  49 81 E1 00 F0 FF FF            and r9, 0xfffffffffffff000
002E3D27  33 D0                           xor edx, eax
002E3D29  49 8B C9                        mov rcx, r9
002E3D2C  41 33 D0                        xor edx, r8d
002E3D2F  48 2B CB                        sub rcx, rbx
002E3D32  8B C2                           mov eax, edx
002E3D34  33 FF                           xor edi, edi
002E3D36  48 C1 E0 04                     shl rax, 4
002E3D3A  48 3B C8                        cmp rcx, rax
002E3D3D  0F 82 DF 04 00 00               jb 0x1402e4222
002E3D43  44 8B CF                        mov r9d, edi
002E3D46  4D 85 C9                        test r9, r9
002E3D49  0F 84 1D 01 00 00               je 0x1402e3e6c
002E3D4F  41 0F B7 49 02                  movzx ecx, word ptr [r9 + 2]
002E3D54  41 8B C1                        mov eax, r9d
002E3D57  C1 E8 10                        shr eax, 0x10
002E3D5A  45 8B D9                        mov r11d, r9d
002E3D5D  33 C8                           xor ecx, eax
002E3D5F  41 81 E3 FF 0F 00 00            and r11d, 0xfff
002E3D66  0F B7 05 95 45 B4 00            movzx eax, word ptr [rip + 0xb44595]
002E3D6D  49 81 C3 FF 0F 00 00            add r11, 0xfff
002E3D74  33 C8                           xor ecx, eax
002E3D76  45 8B D1                        mov r10d, r9d
002E3D79  C1 E1 04                        shl ecx, 4
002E3D7C  45 2B D7                        sub r10d, r15d
002E3D7F  44 8B C1                        mov r8d, ecx
002E3D82  41 81 C2 1F 10 00 00            add r10d, 0x101f
002E3D89  4D 03 D8                        add r11, r8
002E3D8C  41 81 E2 00 F0 FF FF            and r10d, 0xfffff000
002E3D93  45 2B C7                        sub r8d, r15d
002E3D96  49 C1 EB 0C                     shr r11, 0xc
002E3D9A  45 03 C1                        add r8d, r9d
002E3D9D  48 8D 81 FF 0F 00 00            lea rax, [rcx + 0xfff]
002E3DA4  48 C1 E8 0C                     shr rax, 0xc
002E3DA8  41 81 E0 00 F0 FF FF            and r8d, 0xfffff000
002E3DAF  44 2B D8                        sub r11d, eax
002E3DB2  45 3B D0                        cmp r10d, r8d
002E3DB5  0F 82 07 05 00 00               jb 0x1402e42c2
002E3DBB  8B D7                           mov edx, edi
002E3DBD  4C 8B C7                        mov r8, rdi
002E3DC0  49 0F BF 45 06                  movsx rax, word ptr [r13 + 6]
002E3DC5  F3 49 0F B8 C8                  popcnt rcx, r8
002E3DCA  C1 EA 0C                        shr edx, 0xc
002E3DCD  4C 63 C1                        movsxd r8, ecx
002E3DD0  66 85 C0                        test ax, ax
002E3DD3  0F 84 8D 05 00 00               je 0x1402e4366
002E3DD9  F0 4E 01 44 28 20               lock add qword ptr [rax + r13 + 0x20], r8
002E3DDF  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
002E3DE4  66 2B D1                        sub dx, cx
002E3DE7  66 41 03 D3                     add dx, r11w
002E3DEB  41 8B C9                        mov ecx, r9d
002E3DEE  66 41 33 D1                     xor dx, r9w
002E3DF2  66 33 15 07 45 B4 00            xor dx, word ptr [rip + 0xb44507]
002E3DF9  66 41 89 11                     mov word ptr [r9], dx
002E3DFD  41 33 09                        xor ecx, dword ptr [r9]
002E3E00  4C 8B 15 F9 44 B4 00            mov r10, qword ptr [rip + 0xb444f9]
002E3E07  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
002E3E0B  41 33 CA                        xor ecx, r10d
002E3E0E  A8 01                           test al, 1
002E3E10  0F 85 10 05 00 00               jne 0x1402e4326
002E3E16  4C 8B 5E 10                     mov r11, qword ptr [rsi + 0x10]
002E3E1A  44 0F B6 C0                     movzx r8d, al
002E3E1E  49 8B D3                        mov rdx, r11
002E3E21  41 83 E0 01                     and r8d, 1
002E3E25  32 C0                           xor al, al
002E3E27  4D 85 DB                        test r11, r11
002E3E2A  74 2D                           je 0x1402e3e59
002E3E2C  0F 1F 40 00                     nop dword ptr [rax]
002E3E30  48 8D 42 F8                     lea rax, [rdx - 8]
002E3E34  33 00                           xor eax, dword ptr [rax]
002E3E36  41 33 C2                        xor eax, r10d
002E3E39  3B C8                           cmp ecx, eax
002E3E3B  0F 82 7B 03 00 00               jb 0x1402e41bc
002E3E41  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
002E3E45  45 85 C0                        test r8d, r8d
002E3E48  0F 84 CA 03 00 00               je 0x1402e4218
002E3E4E  48 85 C0                        test rax, rax
002E3E51  0F 85 BE 03 00 00               jne 0x1402e4215
002E3E57  B0 01                           mov al, 1
002E3E59  49 83 C1 08                     add r9, 8
002E3E5D  48 8D 4E 10                     lea rcx, [rsi + 0x10]
002E3E61  44 0F B6 C0                     movzx r8d, al
002E3E65  E8 06 07 00 00                  call 0x1402e4570
002E3E6A  EB 05                           jmp 0x1402e3e71
002E3E6C  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
002E3E71  44 8B 0B                        mov r9d, dword ptr [rbx]
002E3E74  44 8B DB                        mov r11d, ebx
002E3E77  0F B7 15 84 44 B4 00            movzx edx, word ptr [rip + 0xb44484]
002E3E7E  41 8B C9                        mov ecx, r9d
002E3E81  44 33 CB                        xor r9d, ebx
002E3E84  33 CB                           xor ecx, ebx
002E3E86  41 C1 E9 10                     shr r9d, 0x10
002E3E8A  41 81 E3 FF 0F 00 00            and r11d, 0xfff
002E3E91  C1 E9 10                        shr ecx, 0x10
002E3E94  44 33 CA                        xor r9d, edx
002E3E97  33 CA                           xor ecx, edx
002E3E99  41 C1 E1 04                     shl r9d, 4
002E3E9D  49 81 C3 FF 0F 00 00            add r11, 0xfff
002E3EA4  C1 E1 04                        shl ecx, 4
002E3EA7  4C 03 D9                        add r11, rcx
002E3EAA  45 2B CF                        sub r9d, r15d
002E3EAD  49 C1 EB 0C                     shr r11, 0xc
002E3EB1  44 03 CB                        add r9d, ebx
002E3EB4  44 8B D3                        mov r10d, ebx
002E3EB7  41 81 E1 00 F0 FF FF            and r9d, 0xfffff000
002E3EBE  45 2B D7                        sub r10d, r15d
002E3EC1  48 8D 81 FF 0F 00 00            lea rax, [rcx + 0xfff]
002E3EC8  48 C1 E8 0C                     shr rax, 0xc
002E3ECC  41 81 C2 1F 10 00 00            add r10d, 0x101f
002E3ED3  44 2B D8                        sub r11d, eax
002E3ED6  41 81 E2 00 F0 FF FF            and r10d, 0xfffff000
002E3EDD  45 3B D1                        cmp r10d, r9d
002E3EE0  0F 82 FB 02 00 00               jb 0x1402e41e1
002E3EE6  33 FF                           xor edi, edi
002E3EE8  8B D7                           mov edx, edi
002E3EEA  8B C7                           mov eax, edi
002E3EEC  F3 48 0F B8 C8                  popcnt rcx, rax
002E3EF1  49 0F BF 45 06                  movsx rax, word ptr [r13 + 6]
002E3EF6  C1 EA 0C                        shr edx, 0xc
002E3EF9  4C 63 C1                        movsxd r8, ecx
002E3EFC  66 85 C0                        test ax, ax
002E3EFF  0F 84 3D 04 00 00               je 0x1402e4342
002E3F05  F0 4E 01 44 28 20               lock add qword ptr [rax + r13 + 0x20], r8
002E3F0B  66 2B D1                        sub dx, cx
002E3F0E  8B CB                           mov ecx, ebx
002E3F10  66 41 03 D3                     add dx, r11w
002E3F14  66 33 D3                        xor dx, bx
002E3F17  66 33 15 E2 43 B4 00            xor dx, word ptr [rip + 0xb443e2]
002E3F1E  66 89 13                        mov word ptr [rbx], dx
002E3F21  33 0B                           xor ecx, dword ptr [rbx]
002E3F23  4C 8B 05 D6 43 B4 00            mov r8, qword ptr [rip + 0xb443d6]
002E3F2A  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
002E3F2E  41 33 C8                        xor ecx, r8d
002E3F31  A8 01                           test al, 1
002E3F33  0F 85 D1 03 00 00               jne 0x1402e430a
002E3F39  4C 8B 56 10                     mov r10, qword ptr [rsi + 0x10]
002E3F3D  44 0F B6 C8                     movzx r9d, al
002E3F41  49 8B D2                        mov rdx, r10
002E3F44  41 83 E1 01                     and r9d, 1
002E3F48  32 C0                           xor al, al
002E3F4A  4D 85 D2                        test r10, r10
002E3F4D  74 26                           je 0x1402e3f75
002E3F4F  90                              nop
002E3F50  48 8D 42 F8                     lea rax, [rdx - 8]
002E3F54  33 00                           xor eax, dword ptr [rax]
002E3F56  41 33 C0                        xor eax, r8d
002E3F59  3B C8                           cmp ecx, eax
002E3F5B  72 40                           jb 0x1402e3f9d
002E3F5D  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
002E3F61  45 85 C9                        test r9d, r9d
002E3F64  0F 84 CE 01 00 00               je 0x1402e4138
002E3F6A  48 85 C0                        test rax, rax
002E3F6D  0F 85 C2 01 00 00               jne 0x1402e4135
002E3F73  B0 01                           mov al, 1
002E3F75  4C 8D 4B 08                     lea r9, [rbx + 8]
002E3F79  44 0F B6 C0                     movzx r8d, al
002E3F7D  48 8D 4E 10                     lea rcx, [rsi + 0x10]
002E3F81  E8 EA 05 00 00                  call 0x1402e4570
002E3F86  48 8B C7                        mov rax, rdi
002E3F89  4C 8B 74 24 30                  mov r14, qword ptr [rsp + 0x30]
002E3F8E  48 83 C4 38                     add rsp, 0x38
002E3F92  41 5F                           pop r15
002E3F94  41 5D                           pop r13
002E3F96  41 5C                           pop r12
002E3F98  5F                              pop rdi
002E3F99  5E                              pop rsi
002E3F9A  5B                              pop rbx
002E3F9B  C3                              ret
002E3F9C  CC                              int3
002E3F9D  48 8B 02                        mov rax, qword ptr [rdx]
002E3FA0  45 85 C9                        test r9d, r9d
002E3FA3  74 0C                           je 0x1402e3fb1
002E3FA5  48 85 C0                        test rax, rax
002E3FA8  0F 84 65 03 00 00               je 0x1402e4313
002E3FAE  48 33 C2                        xor rax, rdx
002E3FB1  48 85 C0                        test rax, rax
002E3FB4  0F 84 59 03 00 00               je 0x1402e4313
002E3FBA  48 8B D0                        mov rdx, rax
002E3FBD  EB 91                           jmp 0x1402e3f50
002E3FBF  44 0F B7 43 02                  movzx r8d, word ptr [rbx + 2]
002E3FC4  8B C3                           mov eax, ebx
002E3FC6  C1 E8 10                        shr eax, 0x10
002E3FC9  44 8B F3                        mov r14d, ebx
002E3FCC  44 33 C0                        xor r8d, eax
002E3FCF  45 2B F7                        sub r14d, r15d
002E3FD2  0F B7 05 29 43 B4 00            movzx eax, word ptr [rip + 0xb44329]
002E3FD9  49 C7 C4 FF FF FF FF            mov r12, 0xffffffffffffffff
002E3FE0  44 33 C0                        xor r8d, eax
002E3FE3  41 C1 E0 04                     shl r8d, 4
002E3FE7  45 2B C7                        sub r8d, r15d
002E3FEA  45 8D 8E 1F 10 00 00            lea r9d, [r14 + 0x101f]
002E3FF1  44 03 C3                        add r8d, ebx
002E3FF4  41 81 E1 00 F0 FF FF            and r9d, 0xfffff000
002E3FFB  41 81 E0 00 F0 FF FF            and r8d, 0xfffff000
002E4002  45 3B C8                        cmp r9d, r8d
002E4005  0F 83 E2 FC FF FF               jae 0x1402e3ced
002E400B  41 8D 40 FF                     lea eax, [r8 - 1]
002E400F  41 8B D0                        mov edx, r8d
002E4012  48 C1 E8 0C                     shr rax, 0xc
002E4016  41 2B D1                        sub edx, r9d
002E4019  41 C1 E9 0C                     shr r9d, 0xc
002E401D  B9 3F 00 00 00                  mov ecx, 0x3f
002E4022  2A C8                           sub cl, al
002E4024  49 8B FC                        mov rdi, r12
002E4027  48 D3 EF                        shr rdi, cl
002E402A  49 8B C4                        mov rax, r12
002E402D  41 0F B6 C9                     movzx ecx, r9b
002E4031  48 D3 E0                        shl rax, cl
002E4034  48 23 F8                        and rdi, rax
002E4037  49 23 7F 10                     and rdi, qword ptr [r15 + 0x10]
002E403B  81 FA 00 10 00 00               cmp edx, 0x1000
002E4041  0F 82 A6 FC FF FF               jb 0x1402e3ced
002E4047  48 85 FF                        test rdi, rdi
002E404A  0F 84 9D FC FF FF               je 0x1402e3ced
002E4050  F3 4C 0F B8 E7                  popcnt r12, rdi
002E4055  F6 84 24 90 00 00 00 01         test byte ptr [rsp + 0x90], 1
002E405D  75 16                           jne 0x1402e4075
002E405F  45 8B C4                        mov r8d, r12d
002E4062  49 8B D7                        mov rdx, r15
002E4065  49 8B CD                        mov rcx, r13
002E4068  E8 4F 1B 00 00                  call 0x1402e5bbc
002E406D  85 C0                           test eax, eax
002E406F  0F 84 71 FC FF FF               je 0x1402e3ce6
002E4075  33 C0                           xor eax, eax
002E4077  41 C1 EE 0C                     shr r14d, 0xc
002E407B  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
002E4080  44 33 F3                        xor r14d, ebx
002E4083  48 8B 05 76 42 B4 00            mov rax, qword ptr [rip + 0xb44276]
002E408A  48 C1 E8 20                     shr rax, 0x20
002E408E  C1 E8 10                        shr eax, 0x10
002E4091  C7 44 24 74 00 00 01 00         mov dword ptr [rsp + 0x74], 0x10000
002E4099  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
002E409E  48 C1 E9 20                     shr rcx, 0x20
002E40A2  C1 E9 10                        shr ecx, 0x10
002E40A5  32 C8                           xor cl, al
002E40A7  48 8B C3                        mov rax, rbx
002E40AA  48 C1 E8 20                     shr rax, 0x20
002E40AE  C1 E8 10                        shr eax, 0x10
002E40B1  32 C8                           xor cl, al
002E40B3  88 4B 06                        mov byte ptr [rbx + 6], cl
002E40B6  44 33 35 43 42 B4 00            xor r14d, dword ptr [rip + 0xb44243]
002E40BD  41 0F B6 C6                     movzx eax, r14b
002E40C1  0F BA E8 09                     bts eax, 9
002E40C5  89 43 08                        mov dword ptr [rbx + 8], eax
002E40C8  41 F6 45 05 01                  test byte ptr [r13 + 5], 1
002E40CD  75 12                           jne 0x1402e40e1
002E40CF  41 0F B6 4D 03                  movzx ecx, byte ptr [r13 + 3]
002E40D4  48 8B 94 24 98 00 00 00         mov rdx, qword ptr [rsp + 0x98]
002E40DC  E8 8F E9 FF FF                  call 0x1402e2a70
002E40E1  33 C0                           xor eax, eax
002E40E3  45 8B CC                        mov r9d, r12d
002E40E6  4C 8B C7                        mov r8, rdi
002E40E9  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
002E40ED  49 8B D7                        mov rdx, r15
002E40F0  49 8B CD                        mov rcx, r13
002E40F3  E8 7C 2B 00 00                  call 0x1402e6c74
002E40F8  41 F6 45 05 01                  test byte ptr [r13 + 5], 1
002E40FD  75 1B                           jne 0x1402e411a
002E40FF  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
002E4104  41 0F B6 55 03                  movzx edx, byte ptr [r13 + 3]
002E4109  48 83 C1 08                     add rcx, 8
002E410D  4C 8B 84 24 98 00 00 00         mov r8, qword ptr [rsp + 0x98]
002E4115  E8 06 07 04 00                  call 0x140324820
002E411A  81 63 08 FF FD FF FF            and dword ptr [rbx + 8], 0xfffffdff
002E4121  4D 8D 4F 30                     lea r9, [r15 + 0x30]
002E4125  4C 8B 54 24 78                  mov r10, qword ptr [rsp + 0x78]
002E412A  33 C9                           xor ecx, ecx
002E412C  89 74 24 70                     mov dword ptr [rsp + 0x70], esi
002E4130  E9 78 F8 FF FF                  jmp 0x1402e39ad
002E4135  48 33 C2                        xor rax, rdx
002E4138  48 85 C0                        test rax, rax
002E413B  0F 85 79 FE FF FF               jne 0x1402e3fba
002E4141  E9 2D FE FF FF                  jmp 0x1402e3f73
002E4146  8B C3                           mov eax, ebx
002E4148  8B D6                           mov edx, esi
002E414A  C1 E8 10                        shr eax, 0x10
002E414D  49 8D 4F 30                     lea rcx, [r15 + 0x30]
002E4151  66 33 C6                        xor ax, si
002E4154  48 C1 E2 04                     shl rdx, 4
002E4158  66 33 05 A3 41 B4 00            xor ax, word ptr [rip + 0xb441a3]
002E415F  48 03 D3                        add rdx, rbx
002E4162  66 89 43 02                     mov word ptr [rbx + 2], ax
002E4166  41 0F B7 47 20                  movzx eax, word ptr [r15 + 0x20]
002E416B  48 C1 E0 04                     shl rax, 4
002E416F  48 03 C1                        add rax, rcx
002E4172  48 3B D0                        cmp rdx, rax
002E4175  0F 83 54 FB FF FF               jae 0x1402e3ccf
002E417B  33 C0                           xor eax, eax
002E417D  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
002E4185  0F B7 C6                        movzx eax, si
002E4188  89 84 24 84 00 00 00            mov dword ptr [rsp + 0x84], eax
002E418F  48 8B 05 6A 41 B4 00            mov rax, qword ptr [rip + 0xb4416a]
002E4196  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
002E419E  48 C1 E8 20                     shr rax, 0x20
002E41A2  48 C1 E9 20                     shr rcx, 0x20
002E41A6  66 33 C8                        xor cx, ax
002E41A9  48 8B C2                        mov rax, rdx
002E41AC  48 C1 E8 20                     shr rax, 0x20
002E41B0  66 33 C8                        xor cx, ax
002E41B3  66 89 4A 04                     mov word ptr [rdx + 4], cx
002E41B7  E9 13 FB FF FF                  jmp 0x1402e3ccf
002E41BC  48 8B 02                        mov rax, qword ptr [rdx]
002E41BF  45 85 C0                        test r8d, r8d
002E41C2  74 0C                           je 0x1402e41d0
002E41C4  48 85 C0                        test rax, rax
002E41C7  0F 84 62 01 00 00               je 0x1402e432f
002E41CD  48 33 C2                        xor rax, rdx
002E41D0  48 85 C0                        test rax, rax
002E41D3  0F 84 56 01 00 00               je 0x1402e432f
002E41D9  48 8B D0                        mov rdx, rax
002E41DC  E9 4F FC FF FF                  jmp 0x1402e3e30
002E41E1  41 8D 41 FF                     lea eax, [r9 - 1]
002E41E5  B9 3F 00 00 00                  mov ecx, 0x3f
002E41EA  48 C1 E8 0C                     shr rax, 0xc
002E41EE  41 8B D1                        mov edx, r9d
002E41F1  2A C8                           sub cl, al
002E41F3  41 2B D2                        sub edx, r10d
002E41F6  49 8B C4                        mov rax, r12
002E41F9  41 C1 EA 0C                     shr r10d, 0xc
002E41FD  48 D3 E8                        shr rax, cl
002E4200  41 0F B6 CA                     movzx ecx, r10b
002E4204  49 D3 E4                        shl r12, cl
002E4207  49 23 C4                        and rax, r12
002E420A  49 23 47 10                     and rax, qword ptr [r15 + 0x10]
002E420E  33 FF                           xor edi, edi
002E4210  E9 D7 FC FF FF                  jmp 0x1402e3eec
002E4215  48 33 C2                        xor rax, rdx
002E4218  48 85 C0                        test rax, rax
002E421B  75 BC                           jne 0x1402e41d9
002E421D  E9 35 FC FF FF                  jmp 0x1402e3e57
002E4222  49 83 C1 E0                     add r9, -0x20
002E4226  8B C3                           mov eax, ebx
002E4228  C1 E8 10                        shr eax, 0x10
002E422B  0F 57 C0                        xorps xmm0, xmm0
002E422E  66 41 33 C0                     xor ax, r8w
002E4232  49 8B C9                        mov rcx, r9
002E4235  48 2B CB                        sub rcx, rbx
002E4238  48 C1 F9 04                     sar rcx, 4
002E423C  66 33 C1                        xor ax, cx
002E423F  2B D1                           sub edx, ecx
002E4241  66 89 43 02                     mov word ptr [rbx + 2], ax
002E4245  49 8B C1                        mov rax, r9
002E4248  41 0F 11 01                     movups xmmword ptr [r9], xmm0
002E424C  44 8B C2                        mov r8d, edx
002E424F  41 0F 11 41 10                  movups xmmword ptr [r9 + 0x10], xmm0
002E4254  66 41 89 51 02                  mov word ptr [r9 + 2], dx
002E4259  66 41 89 49 04                  mov word ptr [r9 + 4], cx
002E425E  49 33 01                        xor rax, qword ptr [r9]
002E4261  48 33 05 98 40 B4 00            xor rax, qword ptr [rip + 0xb44098]
002E4268  49 89 01                        mov qword ptr [r9], rax
002E426B  41 0F B7 47 20                  movzx eax, word ptr [r15 + 0x20]
002E4270  48 83 C0 03                     add rax, 3
002E4274  49 C1 E0 04                     shl r8, 4
002E4278  48 C1 E0 04                     shl rax, 4
002E427C  4D 03 C1                        add r8, r9
002E427F  49 03 C7                        add rax, r15
002E4282  4C 3B C0                        cmp r8, rax
002E4285  0F 83 BB FA FF FF               jae 0x1402e3d46
002E428B  0F B7 C2                        movzx eax, dx
002E428E  48 89 7C 24 70                  mov qword ptr [rsp + 0x70], rdi
002E4293  89 44 24 74                     mov dword ptr [rsp + 0x74], eax
002E4297  49 8B C0                        mov rax, r8
002E429A  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
002E429F  48 C1 E8 20                     shr rax, 0x20
002E42A3  48 C1 E9 20                     shr rcx, 0x20
002E42A7  66 33 C8                        xor cx, ax
002E42AA  48 8B 05 4F 40 B4 00            mov rax, qword ptr [rip + 0xb4404f]
002E42B1  48 C1 E8 20                     shr rax, 0x20
002E42B5  66 33 C8                        xor cx, ax
002E42B8  66 41 89 48 04                  mov word ptr [r8 + 4], cx
002E42BD  E9 84 FA FF FF                  jmp 0x1402e3d46
002E42C2  41 8D 40 FF                     lea eax, [r8 - 1]
002E42C6  41 8B D0                        mov edx, r8d
002E42C9  48 C1 E8 0C                     shr rax, 0xc
002E42CD  41 2B D2                        sub edx, r10d
002E42D0  41 C1 EA 0C                     shr r10d, 0xc
002E42D4  B9 3F 00 00 00                  mov ecx, 0x3f
002E42D9  2A C8                           sub cl, al
002E42DB  4D 8B C4                        mov r8, r12
002E42DE  49 D3 E8                        shr r8, cl
002E42E1  49 8B C4                        mov rax, r12
002E42E4  41 0F B6 CA                     movzx ecx, r10b
002E42E8  48 D3 E0                        shl rax, cl
002E42EB  4C 23 C0                        and r8, rax
002E42EE  4D 23 47 10                     and r8, qword ptr [r15 + 0x10]
002E42F2  E9 C9 FA FF FF                  jmp 0x1402e3dc0
002E42F7  49 8B D7                        mov rdx, r15
002E42FA  49 8B CD                        mov rcx, r13
002E42FD  E8 A6 2A 00 00                  call 0x1402e6da8
002E4302  49 8B C7                        mov rax, r15
002E4305  E9 7F FC FF FF                  jmp 0x1402e3f89
002E430A  48 8B 56 10                     mov rdx, qword ptr [rsi + 0x10]
002E430E  48 85 D2                        test rdx, rdx
002E4311  75 07                           jne 0x1402e431a
002E4313  32 C0                           xor al, al
002E4315  E9 5B FC FF FF                  jmp 0x1402e3f75
002E431A  4C 8D 56 10                     lea r10, [rsi + 0x10]
002E431E  4C 33 D2                        xor r10, rdx
002E4321  E9 17 FC FF FF                  jmp 0x1402e3f3d
002E4326  48 8B 56 10                     mov rdx, qword ptr [rsi + 0x10]
002E432A  48 85 D2                        test rdx, rdx
002E432D  75 07                           jne 0x1402e4336
002E432F  32 C0                           xor al, al
002E4331  E9 23 FB FF FF                  jmp 0x1402e3e59
002E4336  4C 8D 5E 10                     lea r11, [rsi + 0x10]
002E433A  4C 33 DA                        xor r11, rdx
002E433D  E9 D8 FA FF FF                  jmp 0x1402e3e1a
002E4342  4D 01 45 58                     add qword ptr [r13 + 0x58], r8
002E4346  E9 C0 FB FF FF                  jmp 0x1402e3f0b
002E434B  49 01 55 58                     add qword ptr [r13 + 0x58], rdx
002E434F  E9 78 F7 FF FF                  jmp 0x1402e3acc
002E4354  49 01 55 58                     add qword ptr [r13 + 0x58], rdx
002E4358  E9 62 F8 FF FF                  jmp 0x1402e3bbf
002E435D  49 01 55 58                     add qword ptr [r13 + 0x58], rdx
002E4361  E9 5B F9 FF FF                  jmp 0x1402e3cc1
002E4366  4D 01 45 58                     add qword ptr [r13 + 0x58], r8
002E436A  E9 70 FA FF FF                  jmp 0x1402e3ddf
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpHpVsChunkFree(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned __int8 a5, __int64 a6)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p70;
    unsigned int v_stack_p74;
    unsigned __int64 v_stack_p78;
    unsigned int v_stack_p8;
    unsigned __int64 v_stack_p80;
    unsigned int v_stack_p84;

    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (56);
    v_stack_m38 = v_r14;
    a1 = 0;
    v_stack_p8 = 0;
loc_002E39AD:
    result = (*(unsigned __int64 *)(a4)) ^ (*(unsigned __int64 *)(v_rip + 11815244));
    a1 = (a1) >> (32);
    result = (result) ^ (a4);
    a1 = (unsigned int)((a1) >> (16));
    a2 = (*(unsigned __int64 *)(v_rip + 11815244)) >> (32);
    result = (result) >> (32);
    result = (a4) >> (32);
    a2 = (unsigned int)((a2) >> (16));
    result = (unsigned int)((result) >> (16));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(a2)));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(result)));
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)(result))) >> (16));
    *(unsigned __int8 *)(a4 + 6) = (unsigned __int8)(a1);
    if ((unsigned int)((unsigned __int16)(result)) == 0) goto loc_002E3ADD;
    result = ((unsigned int)((unsigned int)((unsigned __int16)(result)))) << (4);
    v_r14 = (a4) - (result);
    v_rdi = (*(unsigned __int64 *)(v_r14)) ^ (*(unsigned __int64 *)(v_rip + 11815154));
    v_rdi = (v_rdi) ^ (v_r14);
    result = (v_rdi) >> (32);
    if ((((unsigned int)(result)) & (0xFF0000ULL)) != 0) goto loc_002E3ADD;
    result = RtlRbRemoveNode(a2 + 16, v_r14 + 8, (unsigned __int16)(result), a3 + 48);
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) - ((unsigned int)(a3)));
    a1 = (unsigned int)((a1) + (0x101FULL));
    a4 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r14))))) ^ ((unsigned int)(v_r14)));
    a1 = (unsigned int)((a1) & (0xFFFFF000ULL));
    a4 = (unsigned int)((a4) >> (16));
    a4 = (unsigned int)((a4) ^ ((unsigned int)(*(unsigned __int16 *)(v_rip + 11815115))));
    a4 = (unsigned int)((a4) << (4));
    result = (unsigned int)(((unsigned int)((unsigned int)(a4))) - ((unsigned int)(a3)));
    result = (unsigned int)((result) + ((unsigned int)(v_r14)));
    result = (unsigned int)((result) & (0xFFFFF000ULL));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(result))) - ((unsigned int)(a1)));
    if (((unsigned int)(a1)) >= ((unsigned int)(result))) { a2 = 0; }
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(v_r14)))));
    a2 = (unsigned int)((a2) >> (12));
    result = (unsigned int)((result) ^ (*(unsigned int *)(v_rip + 11815024)));
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) & (0xFFFULL));
    result = (a4 + 4095) + (v_r10);
    a1 = (unsigned int)(((unsigned __int16)(result)) - ((unsigned int)(a2)));
    result = (result) >> (12);
    a1 = (unsigned int)((a1) - ((unsigned int)(result)));
    result = (a4 + 4095) >> (12);
    a1 = (unsigned int)((a1) + ((unsigned int)(result)));
    if ((unsigned __int16)((__int16)(*(unsigned __int16 *)(a1 + 6))) == 0) goto loc_002E434B;
loc_002E3ACC:
    v_rdi = (unsigned int)((v_rdi) >> (16));
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) + ((unsigned int)(v_rdi)));
loc_002E3ADD:
    result = ((unsigned int)((unsigned int)(*(unsigned __int16 *)(a3 + 32)))) << (4);
    v_rdi = ((unsigned int)((unsigned int)(v_rsi))) << (4);
    result = (result) + (a3 + 48);
    v_rdi = (v_rdi) + (v_r14);
    if (v_rdi >= result) goto loc_002E3BCF;
    v_r14 = (*(unsigned __int64 *)(v_rdi)) ^ (*(unsigned __int64 *)(v_rip + 11814905));
    v_r14 = (v_r14) ^ (v_rdi);
    result = (v_r14) >> (32);
    if ((((unsigned int)(result)) & (0xFF0000ULL)) != 0) goto loc_002E3BCF;
    result = RtlRbRemoveNode(v_stack_p10 + 16, v_rdi + 8, (unsigned int)(*(unsigned int *)(v_r14)), a3 + 48);
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) - ((unsigned int)(a3)));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi))))) ^ ((unsigned int)(v_rdi)));
    a2 = (unsigned int)((a2) + (0x101FULL));
    a1 = (unsigned int)((a1) >> (16));
    a2 = (unsigned int)((a2) & (0xFFFFF000ULL));
    a1 = (unsigned int)((a1) ^ ((unsigned int)(*(unsigned __int16 *)(v_rip + 11814866))));
    a1 = (unsigned int)((a1) << (4));
    a1 = (unsigned int)((a1) - ((unsigned int)(a3)));
    a1 = (unsigned int)((a1) + ((unsigned int)(v_rdi)));
    a1 = (unsigned int)((a1) & (0xFFFFF000ULL));
    result = (unsigned int)(((unsigned int)((unsigned int)(a1))) - ((unsigned int)(a2)));
    if (((unsigned int)(a2)) >= ((unsigned int)(a1))) { result = 0; }
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi))) ^ (*(unsigned int *)(v_rip + 11814788)));
    result = (unsigned int)((result) >> (12));
    a4 = (unsigned int)((a4) ^ ((unsigned int)(v_rdi)));
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) & (0xFFFULL));
    a1 = (unsigned int)(((unsigned __int16)(a4)) - ((unsigned int)(result)));
    result = ((unsigned int)((unsigned int)(a1)) + 4095) + (v_r10);
    result = (result) >> (12);
    a1 = (unsigned int)((a1) - ((unsigned int)(result)));
    result = ((unsigned int)((unsigned int)(a1)) + 4095) >> (12);
    a1 = (unsigned int)((a1) + ((unsigned int)(result)));
    if ((unsigned __int16)((__int16)(*(unsigned __int16 *)(a1 + 6))) == 0) goto loc_002E4354;
loc_002E3BBF:
    v_r14 = (unsigned int)((v_r14) >> (16));
    v_rsi = (unsigned int)((v_rsi) + ((unsigned int)(v_r14)));
loc_002E3BCF:
    if (((*(unsigned __int8 *)(a1 + 4)) & (1)) == 0) goto loc_002E3CC6;
    v_r14 = ((unsigned int)((unsigned int)(v_rsi))) << (4);
    v_r14 = (v_r14) + (v_r14);
    result = ((unsigned __int16)(*(unsigned __int16 *)(a3 + 32))) << (4);
    result = (result) + (a3 + 48);
    if (v_r14 >= result) goto loc_002E3CC6;
    v_rdi = (*(unsigned __int64 *)(v_r14)) ^ (*(unsigned __int64 *)(v_rip + 11814655));
    v_rdi = (v_rdi) ^ (v_r14);
    result = (v_rdi) >> (32);
    if ((((unsigned int)(result)) & (0xFF0000ULL)) != 0) goto loc_002E3CC6;
    a1 = (v_stack_p10) + (16);
    result = RtlRbRemoveNode(a1, v_r14 + 8, (unsigned int)((unsigned int)(a1)), a3 + 48);
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) - ((unsigned int)(a3)));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r14))))) ^ ((unsigned int)(v_r14)));
    a2 = (unsigned int)((a2) + (0x101FULL));
    a1 = (unsigned int)((a1) >> (16));
    a2 = (unsigned int)((a2) & (0xFFFFF000ULL));
    a1 = (unsigned int)((a1) ^ ((unsigned int)(*(unsigned __int16 *)(v_rip + 11814611))));
    a1 = (unsigned int)((a1) << (4));
    a1 = (unsigned int)((a1) - ((unsigned int)(a3)));
    a1 = (unsigned int)((a1) + ((unsigned int)(v_r14)));
    a1 = (unsigned int)((a1) & (0xFFFFF000ULL));
    result = (unsigned int)(((unsigned int)((unsigned int)(a1))) - ((unsigned int)(a2)));
    if (((unsigned int)(a2)) >= ((unsigned int)(a1))) { result = 0; }
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r14))) ^ (*(unsigned int *)(v_rip + 11814530)));
    result = (unsigned int)((result) >> (12));
    a4 = (unsigned int)((a4) ^ ((unsigned int)(v_r14)));
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) & (0xFFFULL));
    a1 = (unsigned int)(((unsigned __int16)(a4)) - ((unsigned int)(result)));
    result = ((unsigned int)((unsigned int)(a1)) + 4095) + (v_r10);
    result = (result) >> (12);
    a1 = (unsigned int)((a1) - ((unsigned int)(result)));
    result = ((unsigned int)((unsigned int)(a1)) + 4095) >> (12);
    a1 = (unsigned int)((a1) + ((unsigned int)(result)));
    if ((unsigned __int16)((__int16)(*(unsigned __int16 *)(a1 + 6))) == 0) goto loc_002E435D;
loc_002E3CC1:
    v_rdi = (unsigned int)((v_rdi) >> (16));
    v_rsi = (unsigned int)((v_rsi) + ((unsigned int)(v_rdi)));
loc_002E3CC6:
    if (((unsigned int)(v_r12)) != ((unsigned int)(v_rsi))) goto loc_002E4146;
loc_002E3CCF:
    if (((unsigned int)(v_rsi)) == ((unsigned int)(*(unsigned __int16 *)(a3 + 32)))) goto loc_002E42F7;
    if (((unsigned int)(v_rsi)) > v_stack_p8) goto loc_002E3FBF;
loc_002E3CE6:
loc_002E3CED:
    if (((*(unsigned __int8 *)(a1 + 4)) & (1)) == 0) goto loc_002E3E6C;
    if (((v_r14 + 32) & (0xFFFULL)) == 0) goto loc_002E3E6C;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) >> (16));
    a4 = (v_r14 + 4111) & (0xFFFFFFFFFFFFF000ULL);
    a2 = (unsigned int)((*(unsigned __int16 *)(v_r14 + 2)) ^ ((unsigned int)(result)));
    a2 = (unsigned int)((a2) ^ ((unsigned int)(*(unsigned __int16 *)(v_rip + 11814375))));
    a1 = (a4) - (v_r14);
    v_rdi = 0;
    result = ((unsigned int)((unsigned int)(a2))) << (4);
    if (a1 < result) goto loc_002E4222;
loc_002E3D46:
    if (0 == 0) goto loc_002E3E6C;
    result = (unsigned int)((0) >> (16));
    a1 = (unsigned int)((*(unsigned __int16 *)(0 + 2)) ^ ((unsigned int)(result)));
    v_r11 = (unsigned int)((0) & (0xFFFULL));
    v_r11 = (v_r11) + (0xFFFULL);
    a1 = (unsigned int)((a1) ^ ((unsigned int)(*(unsigned __int16 *)(v_rip + 11814293))));
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
    if (((unsigned int)(v_r10)) < ((unsigned int)(a3))) goto loc_002E42C2;
loc_002E3DC0:
    a2 = (unsigned int)((0) >> (12));
    if ((unsigned __int16)((__int16)(*(unsigned __int16 *)(a1 + 6))) == 0) goto loc_002E4366;
loc_002E3DDF:
    a2 = (unsigned __int16)((a2) - ((unsigned __int16)(a1)));
    a2 = (unsigned __int16)((a2) + ((unsigned __int16)(v_r11)));
    a2 = (unsigned __int16)((a2) ^ (0));
    a2 = (unsigned __int16)((a2) ^ (*(unsigned __int16 *)(v_rip + 11814151)));
    *(unsigned __int16 *)(0) = (unsigned __int16)(a2);
    a1 = (unsigned int)((0) ^ (*(unsigned int *)(0)));
    a1 = (unsigned int)((a1) ^ ((unsigned int)(*(unsigned __int64 *)(v_rip + 11814137))));
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_p10 + 24))) & (1)) != 0) goto loc_002E4326;
loc_002E3E1A:
    a3 = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)(v_stack_p10 + 24))) & (1));
    result = 0;
    if (*(unsigned __int64 *)(v_stack_p10 + 16) == 0) goto loc_002E3E59;
loc_002E3E30:
    result = (unsigned int)((*(unsigned __int64 *)(v_stack_p10 + 16) - 8) ^ (*(unsigned int *)(*(unsigned __int64 *)(v_stack_p10 + 16) - 8)));
    result = (unsigned int)((result) ^ ((unsigned int)(*(unsigned __int64 *)(v_rip + 11814137))));
    if (((unsigned int)(a1)) < ((unsigned int)(result))) goto loc_002E41BC;
    if ((unsigned int)(a3) == 0) goto loc_002E4218;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 16) + 8) != 0) goto loc_002E4215;
loc_002E3E57:
loc_002E3E59:
    a4 = (0) + (8);
    result = RtlRbInsertNodeEx(v_stack_p10 + 16, *(unsigned __int64 *)(v_stack_p10 + 16), 1, a4);
    goto loc_002E3E71;
loc_002E3E6C:
loc_002E3E71:
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r14))) ^ ((unsigned int)(v_r14)));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r14))))) ^ ((unsigned int)(v_r14)));
    a4 = (unsigned int)((a4) >> (16));
    v_r11 = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) & (0xFFFULL));
    a1 = (unsigned int)((a1) >> (16));
    a4 = (unsigned int)((a4) ^ ((unsigned int)(*(unsigned __int16 *)(v_rip + 11814020))));
    a1 = (unsigned int)((a1) ^ ((unsigned int)(*(unsigned __int16 *)(v_rip + 11814020))));
    a4 = (unsigned int)((a4) << (4));
    v_r11 = (v_r11) + (0xFFFULL);
    a1 = (unsigned int)((a1) << (4));
    v_r11 = (v_r11) + (a1);
    a4 = (unsigned int)((a4) - ((unsigned int)(a3)));
    v_r11 = (v_r11) >> (12);
    a4 = (unsigned int)((a4) + ((unsigned int)(v_r14)));
    a4 = (unsigned int)((a4) & (0xFFFFF000ULL));
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) - ((unsigned int)(a3)));
    result = (a1 + 4095) >> (12);
    v_r10 = (unsigned int)((v_r10) + (0x101FULL));
    v_r11 = (unsigned int)((v_r11) - ((unsigned int)(result)));
    v_r10 = (unsigned int)((v_r10) & (0xFFFFF000ULL));
    if (((unsigned int)(v_r10)) < ((unsigned int)(a4))) goto loc_002E41E1;
    v_rdi = 0;
loc_002E3EEC:
    a2 = (unsigned int)((0) >> (12));
    if ((unsigned __int16)((__int16)(*(unsigned __int16 *)(a1 + 6))) == 0) goto loc_002E4342;
loc_002E3F0B:
    a2 = (unsigned __int16)((a2) - ((unsigned __int16)(a1)));
    a2 = (unsigned __int16)((a2) + ((unsigned __int16)(v_r11)));
    a2 = (unsigned __int16)((a2) ^ ((unsigned __int16)(v_r14)));
    a2 = (unsigned __int16)((a2) ^ (*(unsigned __int16 *)(v_rip + 11813858)));
    *(unsigned __int16 *)(v_r14) = (unsigned __int16)(a2);
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) ^ (*(unsigned int *)(v_r14)));
    a1 = (unsigned int)((a1) ^ ((unsigned int)(*(unsigned __int64 *)(v_rip + 11813846))));
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_p10 + 24))) & (1)) != 0) goto loc_002E430A;
loc_002E3F3D:
    a4 = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)(v_stack_p10 + 24))) & (1));
    result = 0;
    if (*(unsigned __int64 *)(v_stack_p10 + 16) == 0) goto loc_002E3F75;
loc_002E3F50:
    result = (unsigned int)((*(unsigned __int64 *)(v_stack_p10 + 16) - 8) ^ (*(unsigned int *)(*(unsigned __int64 *)(v_stack_p10 + 16) - 8)));
    result = (unsigned int)((result) ^ ((unsigned int)(*(unsigned __int64 *)(v_rip + 11813846))));
    if (((unsigned int)(a1)) < ((unsigned int)(result))) goto loc_002E3F9D;
    if ((unsigned int)(a4) == 0) goto loc_002E4138;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 16) + 8) != 0) goto loc_002E4135;
loc_002E3F73:
loc_002E3F75:
    result = RtlRbInsertNodeEx(v_stack_p10 + 16, *(unsigned __int64 *)(v_stack_p10 + 16), 1, v_r14 + 8);
loc_002E3F89:
    v_rsp = (v_rsp) + (56);
    return 0;
loc_002E3F9D:
    if ((unsigned int)(v_r14 + 8) == 0) goto loc_002E3FB1;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 16)) == 0) goto loc_002E4313;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 16))) ^ (*(unsigned __int64 *)(v_stack_p10 + 16));
loc_002E3FB1:
    if (result == 0) goto loc_002E4313;
loc_002E3FBA:
    goto loc_002E3F50;
loc_002E3FBF:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) >> (16));
    a3 = (unsigned int)((*(unsigned __int16 *)(v_r14 + 2)) ^ ((unsigned int)(result)));
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) - ((unsigned int)(a3)));
    a3 = (unsigned int)((a3) ^ ((unsigned int)(*(unsigned __int16 *)(v_rip + 11813673))));
    a3 = (unsigned int)((a3) << (4));
    a3 = (unsigned int)((a3) - ((unsigned int)(a3)));
    a3 = (unsigned int)((a3) + ((unsigned int)(v_r14)));
    a4 = (unsigned int)((v_r14 + 4127) & (0xFFFFF000ULL));
    a3 = (unsigned int)((a3) & (0xFFFFF000ULL));
    if (((unsigned int)(a4)) >= ((unsigned int)(a3))) goto loc_002E3CED;
    result = (a3 - 1) >> (12);
    a2 = (unsigned int)(((unsigned int)((unsigned int)(a3))) - ((unsigned int)(a4)));
    a4 = (unsigned int)((a4) >> (12));
    a1 = (unsigned __int8)((63) - ((unsigned __int8)(result)));
    v_rdi = (-1) >> ((unsigned __int8)(a1));
    result = (-1) << ((unsigned __int8)((unsigned __int8)(a4)));
    v_rdi = (v_rdi) & (result);
    v_rdi = (v_rdi) & (*(unsigned __int64 *)(a3 + 16));
    if (((unsigned int)(a2)) < 0x1000ULL) goto loc_002E3CED;
    if (v_rdi == 0) goto loc_002E3CED;
    if (((a5) & (1)) != 0) goto loc_002E4075;
    result = RtlpHpVsCommitLimitCheck(a1, a3, -1, a4);
    if ((unsigned int)(result) == 0) goto loc_002E3CE6;
loc_002E4075:
    result = 0;
    v_r14 = (unsigned int)((v_r14) >> (12));
    v_stack_p70 = 0;
    v_r14 = (unsigned int)((v_r14) ^ ((unsigned int)(v_r14)));
    result = (*(unsigned __int64 *)(v_rip + 11813494)) >> (32);
    result = (unsigned int)((result) >> (16));
    v_stack_p74 = 0x10000ULL;
    a1 = (v_stack_p70) >> (32);
    a1 = (unsigned int)((a1) >> (16));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(result)));
    result = (v_r14) >> (32);
    result = (unsigned int)((result) >> (16));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(result)));
    *(unsigned __int8 *)(v_r14 + 6) = (unsigned __int8)(a1);
    v_r14 = (unsigned int)((v_r14) ^ (*(unsigned int *)(v_rip + 11813443)));
    *(unsigned int *)(v_r14 + 8) = (unsigned int)((unsigned __int8)(v_r14));
    result = (unsigned __int8)(v_r14);
    if (((*(unsigned __int8 *)(a1 + 5)) & (1)) == 0) {
        a1 = *(unsigned __int8 *)(a1 + 3);
        a2 = a6;
        result = RtlpHpReleaseQueuedLockExclusive(a1, a2, -1, a4);
    }
    result = 0;
    v_stack_p20 = 0;
    result = RtlpHpVsSubsegmentCommitPages(a1, a3, v_rdi, -1);
    if (((*(unsigned __int8 *)(a1 + 5)) & (1)) == 0) {
        a1 = v_stack_p78;
        a2 = *(unsigned __int8 *)(a1 + 3);
        a1 = (a1) + (8);
        a3 = a6;
        result = RtlpHpAcquireQueuedLockExclusive(a1, a2, a3, -1);
    }
    a1 = 0;
    v_stack_p70 = (unsigned int)(v_stack_p10);
    goto loc_002E39AD;
loc_002E4135:
    result = (result) ^ (a2);
loc_002E4138:
    if (result != 0) goto loc_002E3FBA;
    goto loc_002E3F73;
loc_002E4146:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) >> (16));
    result = (unsigned __int16)((result) ^ ((unsigned __int16)(v_stack_p10)));
    a2 = ((unsigned int)((unsigned int)(v_stack_p10))) << (4);
    result = (unsigned __int16)((result) ^ (*(unsigned __int16 *)(v_rip + 11813283)));
    a2 = (a2) + (v_r14);
    *(unsigned __int16 *)(v_r14 + 2) = (unsigned __int16)(result);
    result = (*(unsigned __int16 *)(a3 + 32)) << (4);
    result = (result) + (a3 + 48);
    if (a2 >= result) goto loc_002E3CCF;
    result = 0;
    v_stack_p80 = 0;
    v_stack_p84 = (unsigned int)((unsigned __int16)(v_stack_p10));
    result = (*(unsigned __int64 *)(v_rip + 11813226)) >> (32);
    a1 = (v_stack_p80) >> (32);
    a1 = (unsigned __int16)((a1) ^ ((unsigned __int16)(result)));
    result = (a2) >> (32);
    a1 = (unsigned __int16)((a1) ^ ((unsigned __int16)(result)));
    *(unsigned __int16 *)(a2 + 4) = (unsigned __int16)(a1);
    goto loc_002E3CCF;
loc_002E41BC:
    if ((unsigned int)(a3) == 0) goto loc_002E41D0;
    if (*(unsigned __int64 *)(a2) == 0) goto loc_002E432F;
    result = (*(unsigned __int64 *)(a2)) ^ (a2);
loc_002E41D0:
    if (result == 0) goto loc_002E432F;
loc_002E41D9:
    goto loc_002E3E30;
loc_002E41E1:
    result = (a3 + 48 - 1) >> (12);
    a1 = (unsigned __int8)((63) - ((unsigned __int8)(result)));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(a3 + 48))) - ((unsigned int)(v_stack_p78)));
    v_r10 = (unsigned int)((v_stack_p78) >> (12));
    result = (-1) >> ((unsigned __int8)(a1));
    v_r12 = (-1) << ((unsigned __int8)((unsigned __int8)(v_r10)));
    result = (result) & (v_r12);
    result = (result) & (*(unsigned __int64 *)(a3 + 16));
    v_rdi = 0;
    goto loc_002E3EEC;
loc_002E4215:
    result = (result) ^ (a2);
loc_002E4218:
    if (result != 0) goto loc_002E41D9;
    goto loc_002E3E57;
loc_002E4222:
    a4 = (a3 + 48) + (-32);
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) >> (16));
    result = (unsigned __int16)((result) ^ ((unsigned __int16)(a3)));
    a1 = (a4) - (v_r14);
    a1 = (a1) >> (4);
    result = (unsigned __int16)((result) ^ ((unsigned __int16)(a1)));
    a2 = (unsigned int)((a2) - ((unsigned int)(a1)));
    *(unsigned __int16 *)(v_r14 + 2) = (unsigned __int16)(result);
    *(unsigned __int64 *)(a4) = v_xmm0;
    *(unsigned __int64 *)(a4 + 16) = v_xmm0;
    *(unsigned __int16 *)(a4 + 2) = (unsigned __int16)(a2);
    *(unsigned __int16 *)(a4 + 4) = (unsigned __int16)(a1);
    result = (a4) ^ (*(unsigned __int64 *)(a4));
    result = (result) ^ (*(unsigned __int64 *)(v_rip + 11813016));
    *(unsigned __int64 *)(a4) = result;
    result = (*(unsigned __int16 *)(a3 + 32)) + (3);
    a3 = ((unsigned int)((unsigned int)(a2))) << (4);
    result = (result) << (4);
    a3 = (a3) + (a4);
    result = (result) + (a3);
    if (a3 >= result) goto loc_002E3D46;
    v_stack_p70 = 0;
    v_stack_p74 = (unsigned int)((unsigned __int16)(a2));
    result = (a3) >> (32);
    a1 = (v_stack_p70) >> (32);
    a1 = (unsigned __int16)((a1) ^ ((unsigned __int16)(result)));
    result = (*(unsigned __int64 *)(v_rip + 11812943)) >> (32);
    a1 = (unsigned __int16)((a1) ^ ((unsigned __int16)(result)));
    *(unsigned __int16 *)(a3 + 4) = (unsigned __int16)(a1);
    goto loc_002E3D46;
loc_002E42C2:
    result = (a3 - 1) >> (12);
    a2 = (unsigned int)(((unsigned int)((unsigned int)(a3))) - ((unsigned int)(v_r10)));
    v_r10 = (unsigned int)((v_r10) >> (12));
    a1 = (unsigned __int8)((63) - ((unsigned __int8)(result)));
    a3 = (v_r12) >> ((unsigned __int8)(a1));
    result = (v_r12) << ((unsigned __int8)((unsigned __int8)(v_r10)));
    a3 = (a3) & (result);
    a3 = (a3) & (*(unsigned __int64 *)(a3 + 16));
    goto loc_002E3DC0;
loc_002E42F7:
    result = RtlpHpVsSubsegmentCleanup(a1, a3, a3, a4);
    goto loc_002E3F89;
loc_002E430A:
    if (*(unsigned __int64 *)(v_stack_p10 + 16) != 0) goto loc_002E431A;
loc_002E4313:
    result = 0;
    goto loc_002E3F75;
loc_002E431A:
    v_r10 = (v_stack_p10 + 16) ^ (*(unsigned __int64 *)(v_stack_p10 + 16));
    goto loc_002E3F3D;
loc_002E4326:
    if (*(unsigned __int64 *)(v_stack_p10 + 16) != 0) goto loc_002E4336;
loc_002E432F:
    result = 0;
    goto loc_002E3E59;
loc_002E4336:
    v_r11 = (v_stack_p10 + 16) ^ (*(unsigned __int64 *)(v_stack_p10 + 16));
    goto loc_002E3E1A;
loc_002E4342:
    goto loc_002E3F0B;
loc_002E434B:
    goto loc_002E3ACC;
loc_002E4354:
    goto loc_002E3BBF;
loc_002E435D:
    goto loc_002E3CC1;
loc_002E4366:
    goto loc_002E3DDF;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpHpVsChunkFree(void *Arg1, int64_t Arg2, void *Arg3, void *Arg4, uint8_t Arg5, int64_t Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m38;
    uint64_t v_stack_p10;
    uint32_t v_stack_p20;
    uint64_t v_stack_p70;
    uint32_t v_stack_p74;
    uint64_t v_stack_p78;
    uint32_t v_stack_p8;
    uint64_t v_stack_p80;
    uint32_t v_stack_p84;

    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (56);
    v_stack_m38 = local_r14;
    Arg1 = 0;
    v_stack_p8 = 0;
loc_002E39AD:
    result = (*(uint64_t *)(arg4)) ^ (*(uint64_t *)(v_rip + 0xB4494C));
    Arg1 = (Arg1) >> (32);
    result = (result) ^ (Arg4);
    Arg1 = (uint32_t)((Arg1) >> (16));
    Arg2 = (*(uint64_t *)(v_rip + 0xB4494C)) >> (32);
    result = (result) >> (32);
    result = (Arg4) >> (32);
    Arg2 = (uint32_t)((Arg2) >> (16));
    result = (uint32_t)((result) >> (16));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(Arg2)));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(result)));
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)(result))) >> (16));
    *(uint8_t *)(arg4 + 0x6) = (uint8_t)(Arg1);
    if ((uint32_t)((uint16_t)(result)) == 0) goto loc_002E3ADD;
    result = ((uint32_t)((uint32_t)((uint16_t)(result)))) << (4);
    local_r14 = (Arg4) - (result);
    local_rdi = (*(uint64_t *)(local_r14)) ^ (*(uint64_t *)(v_rip + 0xB448F2));
    local_rdi = (local_rdi) ^ (local_r14);
    result = (local_rdi) >> (32);
    if ((((uint32_t)(result)) & (0xFF0000ULL)) != 0) goto loc_002E3ADD;
    result = RtlRbRemoveNode(Arg2 + 16, local_r14 + 8, (uint16_t)(result), Arg3 + 48);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) - ((uint32_t)(Arg3)));
    Arg1 = (uint32_t)((Arg1) + (0x101FULL));
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r14))))) ^ ((uint32_t)(local_r14)));
    Arg1 = (uint32_t)((Arg1) & (0xFFFFF000ULL));
    Arg4 = (uint32_t)((Arg4) >> (16));
    Arg4 = (uint32_t)((Arg4) ^ ((uint32_t)(*(uint16_t *)(v_rip + 0xB448CB))));
    Arg4 = (uint32_t)((Arg4) << (4));
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg4))) - ((uint32_t)(Arg3)));
    result = (uint32_t)((result) + ((uint32_t)(local_r14)));
    result = (uint32_t)((result) & (0xFFFFF000ULL));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(result))) - ((uint32_t)(Arg1)));
    if (((uint32_t)(Arg1)) >= ((uint32_t)(result))) { Arg2 = 0; }
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(local_r14)))));
    Arg2 = (uint32_t)((Arg2) >> (12));
    result = (uint32_t)((result) ^ (*(uint32_t *)(v_rip + 0xB44870)));
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) & (0xFFFULL));
    result = (Arg4 + 4095) + (local_r10);
    Arg1 = (uint32_t)(((uint16_t)(result)) - ((uint32_t)(Arg2)));
    result = (result) >> (12);
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(result)));
    result = (Arg4 + 4095) >> (12);
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(result)));
    if ((uint16_t)((int16_t)(*(uint16_t *)(arg1 + 0x6))) == 0) goto loc_002E434B;
loc_002E3ACC:
    local_rdi = (uint32_t)((local_rdi) >> (16));
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) + ((uint32_t)(local_rdi)));
loc_002E3ADD:
    result = ((uint32_t)((uint32_t)(*(uint16_t *)(arg3 + 0x20)))) << (4);
    local_rdi = ((uint32_t)((uint32_t)(local_rsi))) << (4);
    result = (result) + (Arg3 + 48);
    local_rdi = (local_rdi) + (local_r14);
    if (local_rdi >= result) goto loc_002E3BCF;
    local_r14 = (*(uint64_t *)(local_rdi)) ^ (*(uint64_t *)(v_rip + 0xB447F9));
    local_r14 = (local_r14) ^ (local_rdi);
    result = (local_r14) >> (32);
    if ((((uint32_t)(result)) & (0xFF0000ULL)) != 0) goto loc_002E3BCF;
    result = RtlRbRemoveNode(v_stack_p10 + 16, local_rdi + 8, (uint32_t)(*(uint32_t *)(local_r14)), Arg3 + 48);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) - ((uint32_t)(Arg3)));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi))))) ^ ((uint32_t)(local_rdi)));
    Arg2 = (uint32_t)((Arg2) + (0x101FULL));
    Arg1 = (uint32_t)((Arg1) >> (16));
    Arg2 = (uint32_t)((Arg2) & (0xFFFFF000ULL));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)(*(uint16_t *)(v_rip + 0xB447D2))));
    Arg1 = (uint32_t)((Arg1) << (4));
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(Arg3)));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(local_rdi)));
    Arg1 = (uint32_t)((Arg1) & (0xFFFFF000ULL));
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) - ((uint32_t)(Arg2)));
    if (((uint32_t)(Arg2)) >= ((uint32_t)(Arg1))) { result = 0; }
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi))) ^ (*(uint32_t *)(v_rip + 0xB44784)));
    result = (uint32_t)((result) >> (12));
    Arg4 = (uint32_t)((Arg4) ^ ((uint32_t)(local_rdi)));
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) & (0xFFFULL));
    Arg1 = (uint32_t)(((uint16_t)(Arg4)) - ((uint32_t)(result)));
    result = ((uint32_t)((uint32_t)(Arg1)) + 4095) + (local_r10);
    result = (result) >> (12);
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(result)));
    result = ((uint32_t)((uint32_t)(Arg1)) + 4095) >> (12);
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(result)));
    if ((uint16_t)((int16_t)(*(uint16_t *)(arg1 + 0x6))) == 0) goto loc_002E4354;
loc_002E3BBF:
    local_r14 = (uint32_t)((local_r14) >> (16));
    local_rsi = (uint32_t)((local_rsi) + ((uint32_t)(local_r14)));
loc_002E3BCF:
    if (((*(uint8_t *)(arg1 + 0x4)) & (1)) == 0) goto loc_002E3CC6;
    local_r14 = ((uint32_t)((uint32_t)(local_rsi))) << (4);
    local_r14 = (local_r14) + (local_r14);
    result = ((uint16_t)(*(uint16_t *)(arg3 + 0x20))) << (4);
    result = (result) + (Arg3 + 48);
    if (local_r14 >= result) goto loc_002E3CC6;
    local_rdi = (*(uint64_t *)(local_r14)) ^ (*(uint64_t *)(v_rip + 0xB446FF));
    local_rdi = (local_rdi) ^ (local_r14);
    result = (local_rdi) >> (32);
    if ((((uint32_t)(result)) & (0xFF0000ULL)) != 0) goto loc_002E3CC6;
    Arg1 = (v_stack_p10) + (16);
    result = RtlRbRemoveNode(Arg1, local_r14 + 8, (uint32_t)((uint32_t)(Arg1)), Arg3 + 48);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) - ((uint32_t)(Arg3)));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r14))))) ^ ((uint32_t)(local_r14)));
    Arg2 = (uint32_t)((Arg2) + (0x101FULL));
    Arg1 = (uint32_t)((Arg1) >> (16));
    Arg2 = (uint32_t)((Arg2) & (0xFFFFF000ULL));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)(*(uint16_t *)(v_rip + 0xB446D3))));
    Arg1 = (uint32_t)((Arg1) << (4));
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(Arg3)));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(local_r14)));
    Arg1 = (uint32_t)((Arg1) & (0xFFFFF000ULL));
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) - ((uint32_t)(Arg2)));
    if (((uint32_t)(Arg2)) >= ((uint32_t)(Arg1))) { result = 0; }
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r14))) ^ (*(uint32_t *)(v_rip + 0xB44682)));
    result = (uint32_t)((result) >> (12));
    Arg4 = (uint32_t)((Arg4) ^ ((uint32_t)(local_r14)));
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) & (0xFFFULL));
    Arg1 = (uint32_t)(((uint16_t)(Arg4)) - ((uint32_t)(result)));
    result = ((uint32_t)((uint32_t)(Arg1)) + 4095) + (local_r10);
    result = (result) >> (12);
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(result)));
    result = ((uint32_t)((uint32_t)(Arg1)) + 4095) >> (12);
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(result)));
    if ((uint16_t)((int16_t)(*(uint16_t *)(arg1 + 0x6))) == 0) goto loc_002E435D;
loc_002E3CC1:
    local_rdi = (uint32_t)((local_rdi) >> (16));
    local_rsi = (uint32_t)((local_rsi) + ((uint32_t)(local_rdi)));
loc_002E3CC6:
    if (((uint32_t)(local_r12)) != ((uint32_t)(local_rsi))) goto loc_002E4146;
loc_002E3CCF:
    if (((uint32_t)(local_rsi)) == ((uint32_t)(*(uint16_t *)(arg3 + 0x20)))) goto loc_002E42F7;
    if (((uint32_t)(local_rsi)) > v_stack_p8) goto loc_002E3FBF;
loc_002E3CE6:
loc_002E3CED:
    if (((*(uint8_t *)(arg1 + 0x4)) & (1)) == 0) goto loc_002E3E6C;
    if (((local_r14 + 32) & (0xFFFULL)) == 0) goto loc_002E3E6C;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) >> (16));
    Arg4 = (local_r14 + 4111) & (0xFFFFFFFFFFFFF000ULL);
    Arg2 = (uint32_t)((*(uint16_t *)(local_r14 + 0x2)) ^ ((uint32_t)(result)));
    Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)(*(uint16_t *)(v_rip + 0xB445E7))));
    Arg1 = (Arg4) - (local_r14);
    local_rdi = 0;
    result = ((uint32_t)((uint32_t)(Arg2))) << (4);
    if (Arg1 < result) goto loc_002E4222;
loc_002E3D46:
    if (0 == 0) goto loc_002E3E6C;
    result = (uint32_t)((0) >> (16));
    Arg1 = (uint32_t)((*(uint16_t *)(0 + 0x2)) ^ ((uint32_t)(result)));
    local_r11 = (uint32_t)((0) & (0xFFFULL));
    local_r11 = (local_r11) + (0xFFFULL);
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)(*(uint16_t *)(v_rip + 0xB44595))));
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
    if (((uint32_t)(local_r10)) < ((uint32_t)(Arg3))) goto loc_002E42C2;
loc_002E3DC0:
    Arg2 = (uint32_t)((0) >> (12));
    if ((uint16_t)((int16_t)(*(uint16_t *)(arg1 + 0x6))) == 0) goto loc_002E4366;
loc_002E3DDF:
    Arg2 = (uint16_t)((Arg2) - ((uint16_t)(Arg1)));
    Arg2 = (uint16_t)((Arg2) + ((uint16_t)(local_r11)));
    Arg2 = (uint16_t)((Arg2) ^ (0));
    Arg2 = (uint16_t)((Arg2) ^ (*(uint16_t *)(v_rip + 0xB44507)));
    *(uint16_t *)(0) = (uint16_t)(Arg2);
    Arg1 = (uint32_t)((0) ^ (*(uint32_t *)(0)));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)(*(uint64_t *)(v_rip + 0xB444F9))));
    if ((((uint8_t)(*(uint64_t *)(v_stack_p10 + 0x18))) & (1)) != 0) goto loc_002E4326;
loc_002E3E1A:
    Arg3 = (uint32_t)(((uint8_t)(*(uint64_t *)(v_stack_p10 + 0x18))) & (1));
    result = 0;
    if (*(uint64_t *)(v_stack_p10 + 0x10) == 0) goto loc_002E3E59;
loc_002E3E30:
    result = (uint32_t)((*(uint64_t *)(v_stack_p10 + 0x10) - 8) ^ (*(uint32_t *)(*(uint64_t *)(v_stack_p10 + 0x10) - 0x8)));
    result = (uint32_t)((result) ^ ((uint32_t)(*(uint64_t *)(v_rip + 0xB444F9))));
    if (((uint32_t)(Arg1)) < ((uint32_t)(result))) goto loc_002E41BC;
    if ((uint32_t)(Arg3) == 0) goto loc_002E4218;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x10) + 0x8) != 0) goto loc_002E4215;
loc_002E3E57:
loc_002E3E59:
    Arg4 = (0) + (8);
    result = RtlRbInsertNodeEx(v_stack_p10 + 16, *(uint64_t *)(v_stack_p10 + 0x10), 1, Arg4);
    goto loc_002E3E71;
loc_002E3E6C:
loc_002E3E71:
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r14))) ^ ((uint32_t)(local_r14)));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r14))))) ^ ((uint32_t)(local_r14)));
    Arg4 = (uint32_t)((Arg4) >> (16));
    local_r11 = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) & (0xFFFULL));
    Arg1 = (uint32_t)((Arg1) >> (16));
    Arg4 = (uint32_t)((Arg4) ^ ((uint32_t)(*(uint16_t *)(v_rip + 0xB44484))));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)(*(uint16_t *)(v_rip + 0xB44484))));
    Arg4 = (uint32_t)((Arg4) << (4));
    local_r11 = (local_r11) + (0xFFFULL);
    Arg1 = (uint32_t)((Arg1) << (4));
    local_r11 = (local_r11) + (Arg1);
    Arg4 = (uint32_t)((Arg4) - ((uint32_t)(Arg3)));
    local_r11 = (local_r11) >> (12);
    Arg4 = (uint32_t)((Arg4) + ((uint32_t)(local_r14)));
    Arg4 = (uint32_t)((Arg4) & (0xFFFFF000ULL));
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) - ((uint32_t)(Arg3)));
    result = (Arg1 + 4095) >> (12);
    local_r10 = (uint32_t)((local_r10) + (0x101FULL));
    local_r11 = (uint32_t)((local_r11) - ((uint32_t)(result)));
    local_r10 = (uint32_t)((local_r10) & (0xFFFFF000ULL));
    if (((uint32_t)(local_r10)) < ((uint32_t)(Arg4))) goto loc_002E41E1;
    local_rdi = 0;
loc_002E3EEC:
    Arg2 = (uint32_t)((0) >> (12));
    if ((uint16_t)((int16_t)(*(uint16_t *)(arg1 + 0x6))) == 0) goto loc_002E4342;
loc_002E3F0B:
    Arg2 = (uint16_t)((Arg2) - ((uint16_t)(Arg1)));
    Arg2 = (uint16_t)((Arg2) + ((uint16_t)(local_r11)));
    Arg2 = (uint16_t)((Arg2) ^ ((uint16_t)(local_r14)));
    Arg2 = (uint16_t)((Arg2) ^ (*(uint16_t *)(v_rip + 0xB443E2)));
    *(uint16_t *)(local_r14) = (uint16_t)(Arg2);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) ^ (*(uint32_t *)(local_r14)));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)(*(uint64_t *)(v_rip + 0xB443D6))));
    if ((((uint8_t)(*(uint64_t *)(v_stack_p10 + 0x18))) & (1)) != 0) goto loc_002E430A;
loc_002E3F3D:
    Arg4 = (uint32_t)(((uint8_t)(*(uint64_t *)(v_stack_p10 + 0x18))) & (1));
    result = 0;
    if (*(uint64_t *)(v_stack_p10 + 0x10) == 0) goto loc_002E3F75;
loc_002E3F50:
    result = (uint32_t)((*(uint64_t *)(v_stack_p10 + 0x10) - 8) ^ (*(uint32_t *)(*(uint64_t *)(v_stack_p10 + 0x10) - 0x8)));
    result = (uint32_t)((result) ^ ((uint32_t)(*(uint64_t *)(v_rip + 0xB443D6))));
    if (((uint32_t)(Arg1)) < ((uint32_t)(result))) goto loc_002E3F9D;
    if ((uint32_t)(Arg4) == 0) goto loc_002E4138;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x10) + 0x8) != 0) goto loc_002E4135;
loc_002E3F73:
loc_002E3F75:
    result = RtlRbInsertNodeEx(v_stack_p10 + 16, *(uint64_t *)(v_stack_p10 + 0x10), 1, local_r14 + 8);
loc_002E3F89:
    local_rsp = (local_rsp) + (56);
    return 0;
loc_002E3F9D:
    if ((uint32_t)(local_r14 + 8) == 0) goto loc_002E3FB1;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x10)) == 0) goto loc_002E4313;
    result = (*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x10))) ^ (*(uint64_t *)(v_stack_p10 + 0x10));
loc_002E3FB1:
    if (result == 0) goto loc_002E4313;
loc_002E3FBA:
    goto loc_002E3F50;
loc_002E3FBF:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) >> (16));
    Arg3 = (uint32_t)((*(uint16_t *)(local_r14 + 0x2)) ^ ((uint32_t)(result)));
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) - ((uint32_t)(Arg3)));
    Arg3 = (uint32_t)((Arg3) ^ ((uint32_t)(*(uint16_t *)(v_rip + 0xB44329))));
    Arg3 = (uint32_t)((Arg3) << (4));
    Arg3 = (uint32_t)((Arg3) - ((uint32_t)(Arg3)));
    Arg3 = (uint32_t)((Arg3) + ((uint32_t)(local_r14)));
    Arg4 = (uint32_t)((local_r14 + 4127) & (0xFFFFF000ULL));
    Arg3 = (uint32_t)((Arg3) & (0xFFFFF000ULL));
    if (((uint32_t)(Arg4)) >= ((uint32_t)(Arg3))) goto loc_002E3CED;
    result = (Arg3 - 1) >> (12);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(Arg3))) - ((uint32_t)(Arg4)));
    Arg4 = (uint32_t)((Arg4) >> (12));
    Arg1 = (uint8_t)((63) - ((uint8_t)(result)));
    local_rdi = (-1) >> ((uint8_t)(Arg1));
    result = (-1) << ((uint8_t)((uint8_t)(Arg4)));
    local_rdi = (local_rdi) & (result);
    local_rdi = (local_rdi) & (*(uint64_t *)(arg3 + 0x10));
    if (((uint32_t)(Arg2)) < 0x1000ULL) goto loc_002E3CED;
    if (local_rdi == 0) goto loc_002E3CED;
    if (((Arg5) & (1)) != 0) goto loc_002E4075;
    result = RtlpHpVsCommitLimitCheck(Arg1, Arg3, -1, Arg4);
    if ((uint32_t)(result) == 0) goto loc_002E3CE6;
loc_002E4075:
    result = 0;
    local_r14 = (uint32_t)((local_r14) >> (12));
    v_stack_p70 = 0;
    local_r14 = (uint32_t)((local_r14) ^ ((uint32_t)(local_r14)));
    result = (*(uint64_t *)(v_rip + 0xB44276)) >> (32);
    result = (uint32_t)((result) >> (16));
    v_stack_p74 = 0x10000ULL;
    Arg1 = (v_stack_p70) >> (32);
    Arg1 = (uint32_t)((Arg1) >> (16));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(result)));
    result = (local_r14) >> (32);
    result = (uint32_t)((result) >> (16));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(result)));
    *(uint8_t *)(local_r14 + 0x6) = (uint8_t)(Arg1);
    local_r14 = (uint32_t)((local_r14) ^ (*(uint32_t *)(v_rip + 0xB44243)));
    *(uint32_t *)(local_r14 + 0x8) = (uint32_t)((uint8_t)(local_r14));
    result = (uint8_t)(local_r14);
    if (((*(uint8_t *)(arg1 + 0x5)) & (1)) == 0) {
        Arg1 = *(uint8_t *)(arg1 + 0x3);
        Arg2 = Arg6;
        result = RtlpHpReleaseQueuedLockExclusive(Arg1, Arg2, -1, Arg4);
    }
    result = 0;
    v_stack_p20 = 0;
    result = RtlpHpVsSubsegmentCommitPages(Arg1, Arg3, local_rdi, -1);
    if (((*(uint8_t *)(arg1 + 0x5)) & (1)) == 0) {
        Arg1 = v_stack_p78;
        Arg2 = *(uint8_t *)(arg1 + 0x3);
        Arg1 = (Arg1) + (8);
        Arg3 = Arg6;
        result = RtlpHpAcquireQueuedLockExclusive(Arg1, Arg2, Arg3, -1);
    }
    Arg1 = 0;
    v_stack_p70 = (uint32_t)(v_stack_p10);
    goto loc_002E39AD;
loc_002E4135:
    result = (result) ^ (Arg2);
loc_002E4138:
    if (result != 0) goto loc_002E3FBA;
    goto loc_002E3F73;
loc_002E4146:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) >> (16));
    result = (uint16_t)((result) ^ ((uint16_t)(v_stack_p10)));
    Arg2 = ((uint32_t)((uint32_t)(v_stack_p10))) << (4);
    result = (uint16_t)((result) ^ (*(uint16_t *)(v_rip + 0xB441A3)));
    Arg2 = (Arg2) + (local_r14);
    *(uint16_t *)(local_r14 + 0x2) = (uint16_t)(result);
    result = (*(uint16_t *)(arg3 + 0x20)) << (4);
    result = (result) + (Arg3 + 48);
    if (Arg2 >= result) goto loc_002E3CCF;
    result = 0;
    v_stack_p80 = 0;
    v_stack_p84 = (uint32_t)((uint16_t)(v_stack_p10));
    result = (*(uint64_t *)(v_rip + 0xB4416A)) >> (32);
    Arg1 = (v_stack_p80) >> (32);
    Arg1 = (uint16_t)((Arg1) ^ ((uint16_t)(result)));
    result = (Arg2) >> (32);
    Arg1 = (uint16_t)((Arg1) ^ ((uint16_t)(result)));
    *(uint16_t *)(Arg2 + 0x4) = (uint16_t)(Arg1);
    goto loc_002E3CCF;
loc_002E41BC:
    if ((uint32_t)(Arg3) == 0) goto loc_002E41D0;
    if (*(uint64_t *)(Arg2) == 0) goto loc_002E432F;
    result = (*(uint64_t *)(Arg2)) ^ (Arg2);
loc_002E41D0:
    if (result == 0) goto loc_002E432F;
loc_002E41D9:
    goto loc_002E3E30;
loc_002E41E1:
    result = (Arg3 + 48 - 1) >> (12);
    Arg1 = (uint8_t)((63) - ((uint8_t)(result)));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(Arg3 + 48))) - ((uint32_t)(v_stack_p78)));
    local_r10 = (uint32_t)((v_stack_p78) >> (12));
    result = (-1) >> ((uint8_t)(Arg1));
    local_r12 = (-1) << ((uint8_t)((uint8_t)(local_r10)));
    result = (result) & (local_r12);
    result = (result) & (*(uint64_t *)(arg3 + 0x10));
    local_rdi = 0;
    goto loc_002E3EEC;
loc_002E4215:
    result = (result) ^ (Arg2);
loc_002E4218:
    if (result != 0) goto loc_002E41D9;
    goto loc_002E3E57;
loc_002E4222:
    Arg4 = (Arg3 + 48) + (-32);
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) >> (16));
    result = (uint16_t)((result) ^ ((uint16_t)(Arg3)));
    Arg1 = (Arg4) - (local_r14);
    Arg1 = (Arg1) >> (4);
    result = (uint16_t)((result) ^ ((uint16_t)(Arg1)));
    Arg2 = (uint32_t)((Arg2) - ((uint32_t)(Arg1)));
    *(uint16_t *)(local_r14 + 0x2) = (uint16_t)(result);
    *(uint64_t *)(arg4) = v_xmm0;
    *(uint64_t *)(arg4 + 0x10) = v_xmm0;
    *(uint16_t *)(arg4 + 0x2) = (uint16_t)(Arg2);
    *(uint16_t *)(arg4 + 0x4) = (uint16_t)(Arg1);
    result = (Arg4) ^ (*(uint64_t *)(arg4));
    result = (result) ^ (*(uint64_t *)(v_rip + 0xB44098));
    *(uint64_t *)(arg4) = result;
    result = (*(uint16_t *)(arg3 + 0x20)) + (3);
    Arg3 = ((uint32_t)((uint32_t)(Arg2))) << (4);
    result = (result) << (4);
    Arg3 = (Arg3) + (Arg4);
    result = (result) + (Arg3);
    if (Arg3 >= result) goto loc_002E3D46;
    v_stack_p70 = 0;
    v_stack_p74 = (uint32_t)((uint16_t)(Arg2));
    result = (Arg3) >> (32);
    Arg1 = (v_stack_p70) >> (32);
    Arg1 = (uint16_t)((Arg1) ^ ((uint16_t)(result)));
    result = (*(uint64_t *)(v_rip + 0xB4404F)) >> (32);
    Arg1 = (uint16_t)((Arg1) ^ ((uint16_t)(result)));
    *(uint16_t *)(arg3 + 0x4) = (uint16_t)(Arg1);
    goto loc_002E3D46;
loc_002E42C2:
    result = (Arg3 - 1) >> (12);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(Arg3))) - ((uint32_t)(local_r10)));
    local_r10 = (uint32_t)((local_r10) >> (12));
    Arg1 = (uint8_t)((63) - ((uint8_t)(result)));
    Arg3 = (local_r12) >> ((uint8_t)(Arg1));
    result = (local_r12) << ((uint8_t)((uint8_t)(local_r10)));
    Arg3 = (Arg3) & (result);
    Arg3 = (Arg3) & (*(uint64_t *)(arg3 + 0x10));
    goto loc_002E3DC0;
loc_002E42F7:
    result = RtlpHpVsSubsegmentCleanup(Arg1, Arg3, Arg3, Arg4);
    goto loc_002E3F89;
loc_002E430A:
    if (*(uint64_t *)(v_stack_p10 + 0x10) != 0) goto loc_002E431A;
loc_002E4313:
    result = 0;
    goto loc_002E3F75;
loc_002E431A:
    local_r10 = (v_stack_p10 + 16) ^ (*(uint64_t *)(v_stack_p10 + 0x10));
    goto loc_002E3F3D;
loc_002E4326:
    if (*(uint64_t *)(v_stack_p10 + 0x10) != 0) goto loc_002E4336;
loc_002E432F:
    result = 0;
    goto loc_002E3E59;
loc_002E4336:
    local_r11 = (v_stack_p10 + 16) ^ (*(uint64_t *)(v_stack_p10 + 0x10));
    goto loc_002E3E1A;
loc_002E4342:
    goto loc_002E3F0B;
loc_002E434B:
    goto loc_002E3ACC;
loc_002E4354:
    goto loc_002E3BBF;
loc_002E435D:
    goto loc_002E3CC1;
loc_002E4366:
    goto loc_002E3DDF;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x3` | `8` | `R` |
| `Arg1` | `+ 0x4` | `8` | `R` |
| `Arg1` | `+ 0x5` | `8` | `R` |
| `Arg1` | `+ 0x6` | `16` | `R` |
| `Arg1` | `+ 0x58` | `64` | `R/W` |
| `Arg3` | `+ 0x10` | `64` | `R` |
| `Arg3` | `+ 0x20` | `16` | `R` |
| `Arg3` | `+ 0x30` | `64` | `R` |
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
| `Arg4` | `+ 0x101F` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002E3980&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
