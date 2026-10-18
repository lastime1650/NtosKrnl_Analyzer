# ST_STORE&lt;SM_TRAITS&gt;::StDmPageRemove

- RVA: `0x002049A0`–`0x00204FC0` (길이 `1,568` bytes)
- VA: `0x00000001402049A0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CC70`
- 디코드: `409`개 명령, `1,568/1,568` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **32**; 고유 호출 대상: **22**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00204A14` → [B_TREE<_SM_PAGE_KEY,ST_STORE<SM_TRAITS>::_ST_PAGE_ENTRY,4096,NP_CONTEXT,B_TREE_KEY_COMPARATOR<_SM_PAGE_KEY> >::BTreeSearchResultDeref](../3A/B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS__ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PAGE_function_003AC5D0.md) (function, `0x003AC5D0`)
- `0x00204A2D` → [B_TREE<unsigned long,ST_STORE<SM_TRAITS>::_ST_REGION_ENTRY,4096,NP_CONTEXT,ST_STORE<SM_TRAITS>::ST_REGION_ENTRY_COMPARATOR>::BTreeSearchResultDeref](../3A/B_TREE_unsigned_long_ST_STORE_SM_TRAITS__ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS_ST_REGIO_function_003AD260.md) (function, `0x003AD260`)
- `0x00204A48` → [B_TREE<_SM_PAGE_KEY,ST_STORE<SM_TRAITS>::_ST_PAGE_ENTRY,4096,NP_CONTEXT,B_TREE_KEY_COMPARATOR<_SM_PAGE_KEY> >::BTreeSearchKey](../3A/B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS__ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PAGE_function_003AC3C0.md) (function, `0x003AC3C0`)
- `0x00204A6A` → [B_TREE<_SM_PAGE_KEY,ST_STORE<SM_TRAITS>::_ST_PAGE_ENTRY,4096,NP_CONTEXT,B_TREE_KEY_COMPARATOR<_SM_PAGE_KEY> >::BTreeIteratorFromSearchResult](../43/B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS__ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PAGE_function_00434250.md) (function, `0x00434250`)
- `0x00204AB9` → [B_TREE<_SM_PAGE_KEY,ST_STORE<SM_TRAITS>::_ST_PAGE_ENTRY,4096,NP_CONTEXT,B_TREE_KEY_COMPARATOR<_SM_PAGE_KEY> >::BTreeFindLeafSibling](../41/B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS__ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PAGE_function_00410EF0.md) (function, `0x00410EF0`)
- `0x00204B1C` → [ST_STORE<SM_TRAITS>::StDmCombinePageEntry](../41/ST_STORE_SM_TRAITS_StDmCombinePageEntry_function_00410D40.md) (function, `0x00410D40`)
- `0x00204B35` → [ST_STORE<SM_TRAITS>::StDmPageRecordUnprotect](../26/ST_STORE_SM_TRAITS_StDmPageRecordUnprotect_function_00268B30.md) (function, `0x00268B30`)
- `0x00204B67` → [SmEtwLogStoreOp](../60/SmEtwLogStoreOp_function_0060F584.md) (function, `0x0060F584`)
- `0x00204BB7` → [B_TREE<_SM_PAGE_KEY,ST_STORE<SM_TRAITS>::_ST_PAGE_ENTRY,4096,NP_CONTEXT,B_TREE_KEY_COMPARATOR<_SM_PAGE_KEY> >::BTreeSearchResultDeref](../3A/B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS__ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PAGE_function_003AC5D0.md) (function, `0x003AC5D0`)
- `0x00204BDF` → [B_TREE<_SM_PAGE_KEY,ST_STORE<SM_TRAITS>::_ST_PAGE_ENTRY,4096,NP_CONTEXT,B_TREE_KEY_COMPARATOR<_SM_PAGE_KEY> >::BTreeSearchKey](../3A/B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS__ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PAGE_function_003AC3C0.md) (function, `0x003AC3C0`)
- `0x00204C08` → [B_TREE<_SM_PAGE_KEY,ST_STORE<SM_TRAITS>::_ST_PAGE_ENTRY,4096,NP_CONTEXT,B_TREE_KEY_COMPARATOR<_SM_PAGE_KEY> >::BTreeIteratorCleanup](../41/B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS__ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PAGE_function_00411010.md) (function, `0x00411010`)
- `0x00204C2C` → [StLockAcquireExclusive](../26/StLockAcquireExclusive_function_00266FF0.md) (function, `0x00266FF0`)
- `0x00204C45` → [B_TREE<_SM_PAGE_KEY,ST_STORE<SM_TRAITS>::_ST_PAGE_ENTRY,4096,NP_CONTEXT,B_TREE_KEY_COMPARATOR<_SM_PAGE_KEY> >::BTreeDeleteEx](../3A/B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS__ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PAGE_function_003AB210.md) (function, `0x003AB210`)
- `0x00204C99` → [StLockReleaseExclusive](../26/StLockReleaseExclusive_function_00267050.md) (function, `0x00267050`)
- `0x00204CC5` → [StLockReleaseExclusive](../26/StLockReleaseExclusive_function_00267050.md) (function, `0x00267050`)
- `0x00204CD9` → [B_TREE<unsigned long,ST_STORE<SM_TRAITS>::_ST_REGION_ENTRY,4096,NP_CONTEXT,ST_STORE<SM_TRAITS>::ST_REGION_ENTRY_COMPARATOR>::BTreeSearchKey](../3A/B_TREE_unsigned_long_ST_STORE_SM_TRAITS__ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS_ST_REGIO_function_003ACD20.md) (function, `0x003ACD20`)
- `0x00204D61` → [ST_STORE<SM_TRAITS>::StDmPageRecordRemove](../3A/ST_STORE_SM_TRAITS_StDmPageRecordRemove_function_003AD400.md) (function, `0x003AD400`)
- `0x00204D77` → [SmHpChunkFree](../26/SmHpChunkFree_function_00268D50.md) (function, `0x00268D50`)
- `0x00204DA4` → [SMKM_STORE<SM_TRAITS>::SmStReleaseStoreLockExclusive](../2D/SMKM_STORE_SM_TRAITS_SmStReleaseStoreLockExclusive_function_002DFE68.md) (function, `0x002DFE68`)
- `0x00204DBE` → [SMKM_STORE_MGR<SM_TRAITS>::SmEvictKeys](../61/SMKM_STORE_MGR_SM_TRAITS_SmEvictKeys_function_006103AC.md) (function, `0x006103AC`)
- `0x00204DDA` → [StLockAcquireExclusive](../26/StLockAcquireExclusive_function_00266FF0.md) (function, `0x00266FF0`)
- `0x00204E30` → [B_TREE<_SM_PAGE_KEY,ST_STORE<SM_TRAITS>::_ST_PAGE_ENTRY,4096,NP_CONTEXT,B_TREE_KEY_COMPARATOR<_SM_PAGE_KEY> >::BTreeSearchKey](../3A/B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS__ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PAGE_function_003AC3C0.md) (function, `0x003AC3C0`)
- `0x00204E5C` → [SMKM_STORE<SM_TRAITS>::SmStReleaseStoreLockExclusive](../2D/SMKM_STORE_SM_TRAITS_SmStReleaseStoreLockExclusive_function_002DFE68.md) (function, `0x002DFE68`)
- `0x00204E76` → [SMKM_STORE_MGR<SM_TRAITS>::SmEvictKeys](../61/SMKM_STORE_MGR_SM_TRAITS_SmEvictKeys_function_006103AC.md) (function, `0x006103AC`)
- `0x00204E92` → [StLockAcquireExclusive](../26/StLockAcquireExclusive_function_00266FF0.md) (function, `0x00266FF0`)
- `0x00204EC2` → [ST_STORE<SM_TRAITS>::StDmCheckForCompaction](../41/ST_STORE_SM_TRAITS_StDmCheckForCompaction_function_0041147C.md) (function, `0x0041147C`)
- `0x00204ED0` → [ST_STORE<SM_TRAITS>::StQueueCompaction](../41/ST_STORE_SM_TRAITS_StQueueCompaction_function_00411790.md) (function, `0x00411790`)
- `0x00204F20` → [_chkstk](../6B/_chkstk_function_006BA960.md) (function, `0x006BA960`)
- `0x00204F54` → [B_TREE<_SM_PAGE_KEY,ST_STORE<SM_TRAITS>::_ST_PAGE_ENTRY,4096,NP_CONTEXT,B_TREE_KEY_COMPARATOR<_SM_PAGE_KEY> >::BTreeSearchKey](../3A/B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS__ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PAGE_function_003AC3C0.md) (function, `0x003AC3C0`)
- `0x00204F6F` → [B_TREE<_SM_PAGE_KEY,ST_STORE<SM_TRAITS>::_ST_PAGE_ENTRY,4096,NP_CONTEXT,B_TREE_KEY_COMPARATOR<_SM_PAGE_KEY> >::BTreeSearchResultDeref](../3A/B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS__ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PAGE_function_003AC5D0.md) (function, `0x003AC5D0`)
- `0x00204F94` → [NP_CONTEXT::NpLeafDerefInternal](../3A/NP_CONTEXT_NpLeafDerefInternal_function_003A9A70.md) (function, `0x003A9A70`)
- `0x00204FA3` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [sub_00205FE2](Unknown_function_00205FE2.md) at `0x00206014`
- [ST_STORE&lt;SM_TRAITS&gt;::StDmRegionEvict](../60/ST_STORE_SM_TRAITS_StDmRegionEvict_function_0060DF9C.md) at `0x0060E0D8`
- [ST_STORE&lt;SM_TRAITS&gt;::StNpLeafDelete](../60/ST_STORE_SM_TRAITS_StNpLeafDelete_function_0060E5C0.md) at `0x0060E5F5`

### Static image references
- `0x002049BF` → RVA `0x00E0A740` (`.data`; read)
- `0x002049CD` → RVA `0x00E288DC` (`.data`; read)
- `0x002049DD` → RVA `0x00E288D0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002049A0  40 55                           push rbp
002049A2  56                              push rsi
002049A3  57                              push rdi
002049A4  41 54                           push r12
002049A6  41 55                           push r13
002049A8  41 56                           push r14
002049AA  41 57                           push r15
002049AC  48 81 EC B0 00 00 00            sub rsp, 0xb0
002049B3  48 8D 6C 24 40                  lea rbp, [rsp + 0x40]
002049B8  48 89 9D C0 00 00 00            mov qword ptr [rbp + 0xc0], rbx
002049BF  48 8B 05 7A 5D C0 00            mov rax, qword ptr [rip + 0xc05d7a]
002049C6  48 33 C5                        xor rax, rbp
002049C9  48 89 45 60                     mov qword ptr [rbp + 0x60], rax
002049CD  8B 05 09 3F C2 00               mov eax, dword ptr [rip + 0xc23f09]
002049D3  4C 8D 69 18                     lea r13, [rcx + 0x18]
002049D7  A8 10                           test al, 0x10
002049D9  48 89 55 28                     mov qword ptr [rbp + 0x28], rdx
002049DD  48 8D 05 EC 3E C2 00            lea rax, [rip + 0xc23eec]
002049E4  BB 00 00 00 00                  mov ebx, 0
002049E9  48 0F 44 C3                     cmove rax, rbx
002049ED  0F 57 C0                        xorps xmm0, xmm0
002049F0  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
002049F4  4C 8B F2                        mov r14, rdx
002049F7  8B 42 08                        mov eax, dword ptr [rdx + 8]
002049FA  48 8B F1                        mov rsi, rcx
002049FD  FF C8                           dec eax
002049FF  03 42 0C                        add eax, dword ptr [rdx + 0xc]
00204A02  89 45 18                        mov dword ptr [rbp + 0x18], eax
00204A05  41 8B 45 20                     mov eax, dword ptr [r13 + 0x20]
00204A09  0F 11 45 08                     movups xmmword ptr [rbp + 8], xmm0
00204A0D  A8 01                           test al, 1
00204A0F  74 08                           je 0x140204a19
00204A11  49 8B D5                        mov rdx, r13
00204A14  E8 B7 7B 1A 00                  call 0x1403ac5d0
00204A19  41 83 65 20 FE                  and dword ptr [r13 + 0x20], 0xfffffffe
00204A1E  8B 46 78                        mov eax, dword ptr [rsi + 0x78]
00204A21  A8 01                           test al, 1
00204A23  74 0D                           je 0x140204a32
00204A25  48 8D 4E 40                     lea rcx, [rsi + 0x40]
00204A29  48 8D 56 58                     lea rdx, [rsi + 0x58]
00204A2D  E8 2E 88 1A 00                  call 0x1403ad260
00204A32  83 66 78 FE                     and dword ptr [rsi + 0x78], 0xfffffffe
00204A36  4D 8B C5                        mov r8, r13
00204A39  41 8B 56 08                     mov edx, dword ptr [r14 + 8]
00204A3D  48 8B CE                        mov rcx, rsi
00204A40  89 5D 00                        mov dword ptr [rbp], ebx
00204A43  8B FB                           mov edi, ebx
00204A45  89 5D 04                        mov dword ptr [rbp + 4], ebx
00204A48  E8 73 79 1A 00                  call 0x1403ac3c0
00204A4D  44 8B F0                        mov r14d, eax
00204A50  3D 06 00 00 C0                  cmp eax, 0xc0000006
00204A55  0F 84 B7 02 00 00               je 0x140204d12
00204A5B  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00204A60  4D 8B C5                        mov r8, r13
00204A63  48 8D 55 08                     lea rdx, [rbp + 8]
00204A67  48 8B CE                        mov rcx, rsi
00204A6A  E8 E1 F7 22 00                  call 0x140434250
00204A6F  4C 8B 7D 08                     mov r15, qword ptr [rbp + 8]
00204A73  4D 85 FF                        test r15, r15
00204A76  0F 84 D2 03 00 00               je 0x140204e4e
00204A7C  4C 8B 65 10                     mov r12, qword ptr [rbp + 0x10]
00204A80  41 8B 07                        mov eax, dword ptr [r15]
00204A83  49 83 C4 08                     add r12, 8
00204A87  0F B7 C0                        movzx eax, ax
00204A8A  48 83 C0 02                     add rax, 2
00204A8E  4C 89 65 10                     mov qword ptr [rbp + 0x10], r12
00204A92  49 8D 04 C7                     lea rax, [r15 + rax*8]
00204A96  4C 3B E0                        cmp r12, rax
00204A99  72 59                           jb 0x140204af4
00204A9B  48 8D 46 10                     lea rax, [rsi + 0x10]
00204A9F  48 85 F6                        test rsi, rsi
00204AA2  75 03                           jne 0x140204aa7
00204AA4  48 8B C3                        mov rax, rbx
00204AA7  48 8B 00                        mov rax, qword ptr [rax]
00204AAA  48 8D 4E 10                     lea rcx, [rsi + 0x10]
00204AAE  83 38 FF                        cmp dword ptr [rax], -1
00204AB1  74 1A                           je 0x140204acd
00204AB3  49 8B D7                        mov rdx, r15
00204AB6  48 8B CE                        mov rcx, rsi
00204AB9  E8 32 C4 20 00                  call 0x140410ef0
00204ABE  48 83 F8 FF                     cmp rax, -1
00204AC2  0F 85 D7 00 00 00               jne 0x140204b9f
00204AC8  4C 8B F0                        mov r14, rax
00204ACB  EB 2A                           jmp 0x140204af7
00204ACD  48 85 F6                        test rsi, rsi
00204AD0  48 0F 44 CB                     cmove rcx, rbx
00204AD4  48 8B 01                        mov rax, qword ptr [rcx]
00204AD7  83 38 FF                        cmp dword ptr [rax], -1
00204ADA  0F 84 BB 00 00 00               je 0x140204b9b
00204AE0  B8 1E 0D 00 00                  mov eax, 0xd1e
00204AE5  4C 8D 60 10                     lea r12, [rax + 0x10]
00204AE9  48 89 45 08                     mov qword ptr [rbp + 8], rax
00204AED  4C 89 65 10                     mov qword ptr [rbp + 0x10], r12
00204AF1  4C 8B F8                        mov r15, rax
00204AF4  4D 8B F4                        mov r14, r12
00204AF7  49 83 FE FF                     cmp r14, -1
00204AFB  0F 84 F0 03 00 00               je 0x140204ef1
00204B01  4D 85 F6                        test r14, r14
00204B04  0F 84 44 03 00 00               je 0x140204e4e
00204B0A  41 8B 1E                        mov ebx, dword ptr [r14]
00204B0D  39 5D 18                        cmp dword ptr [rbp + 0x18], ebx
00204B10  0F 82 38 03 00 00               jb 0x140204e4e
00204B16  49 8B D6                        mov rdx, r14
00204B19  48 8B CE                        mov rcx, rsi
00204B1C  E8 1F C2 20 00                  call 0x140410d40
00204B21  4C 8B E8                        mov r13, rax
00204B24  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
00204B28  41 8B 46 04                     mov eax, dword ptr [r14 + 4]
00204B2C  49 8B D5                        mov rdx, r13
00204B2F  48 8B CE                        mov rcx, rsi
00204B32  89 45 1C                        mov dword ptr [rbp + 0x1c], eax
00204B35  E8 F6 3F 06 00                  call 0x140268b30
00204B3A  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00204B3E  48 85 C0                        test rax, rax
00204B41  74 29                           je 0x140204b6c
00204B43  33 C9                           xor ecx, ecx
00204B45  4D 8B C6                        mov r8, r14
00204B48  66 89 4C 24 38                  mov word ptr [rsp + 0x38], cx
00204B4D  BA 01 00 00 00                  mov edx, 1
00204B52  66 89 4C 24 30                  mov word ptr [rsp + 0x30], cx
00204B57  41 8B 4D 00                     mov ecx, dword ptr [r13]
00204B5B  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
00204B60  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
00204B64  48 8B C8                        mov rcx, rax
00204B67  E8 18 AA 40 00                  call 0x14060f584
00204B6C  8B 46 30                        mov eax, dword ptr [rsi + 0x30]
00204B6F  4C 8D 76 20                     lea r14, [rsi + 0x20]
00204B73  4D 8B EE                        mov r13, r14
00204B76  83 F8 FF                        cmp eax, -1
00204B79  74 10                           je 0x140204b8b
00204B7B  85 C0                           test eax, eax
00204B7D  74 0C                           je 0x140204b8b
00204B7F  44 8D 68 FF                     lea r13d, [rax - 1]
00204B83  49 C1 E5 04                     shl r13, 4
00204B87  4C 03 6E 18                     add r13, qword ptr [rsi + 0x18]
00204B8B  4D 39 7D 00                     cmp qword ptr [r13], r15
00204B8F  75 1F                           jne 0x140204bb0
00204B91  4D 89 65 08                     mov qword ptr [r13 + 8], r12
00204B95  4C 8D 6E 18                     lea r13, [rsi + 0x18]
00204B99  EB 66                           jmp 0x140204c01
00204B9B  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
00204B9F  48 85 C0                        test rax, rax
00204BA2  0F 85 3D FF FF FF               jne 0x140204ae5
00204BA8  4C 8B F3                        mov r14, rbx
00204BAB  E9 47 FF FF FF                  jmp 0x140204af7
00204BB0  48 8D 56 18                     lea rdx, [rsi + 0x18]
00204BB4  48 8B CE                        mov rcx, rsi
00204BB7  E8 14 7A 1A 00                  call 0x1403ac5d0
00204BBC  83 7E 30 FF                     cmp dword ptr [rsi + 0x30], -1
00204BC0  75 0F                           jne 0x140204bd1
00204BC2  0F 10 45 08                     movups xmm0, xmmword ptr [rbp + 8]
00204BC6  41 0F 11 45 00                  movups xmmword ptr [r13], xmm0
00204BCB  4C 8D 6E 18                     lea r13, [rsi + 0x18]
00204BCF  EB 30                           jmp 0x140204c01
00204BD1  41 8B 57 10                     mov edx, dword ptr [r15 + 0x10]
00204BD5  4C 8D 6E 18                     lea r13, [rsi + 0x18]
00204BD9  4D 8B C5                        mov r8, r13
00204BDC  48 8B CE                        mov rcx, rsi
00204BDF  E8 DC 77 1A 00                  call 0x1403ac3c0
00204BE4  41 8B 45 18                     mov eax, dword ptr [r13 + 0x18]
00204BE8  83 F8 FF                        cmp eax, -1
00204BEB  74 10                           je 0x140204bfd
00204BED  85 C0                           test eax, eax
00204BEF  74 0C                           je 0x140204bfd
00204BF1  44 8D 70 FF                     lea r14d, [rax - 1]
00204BF5  49 C1 E6 04                     shl r14, 4
00204BF9  4D 03 75 00                     add r14, qword ptr [r13]
00204BFD  4D 89 66 08                     mov qword ptr [r14 + 8], r12
00204C01  48 8B D6                        mov rdx, rsi
00204C04  48 8D 4D 08                     lea rcx, [rbp + 8]
00204C08  E8 03 C4 20 00                  call 0x140411010
00204C0D  4C 8B B6 20 03 00 00            mov r14, qword ptr [rsi + 0x320]
00204C14  0F 57 C0                        xorps xmm0, xmm0
00204C17  0F 11 45 08                     movups xmmword ptr [rbp + 8], xmm0
00204C1B  41 F6 86 95 1A 00 00 04         test byte ptr [r14 + 0x1a95], 4
00204C23  74 1A                           je 0x140204c3f
00204C25  49 8D 8E B0 1A 00 00            lea rcx, [r14 + 0x1ab0]
00204C2C  E8 BF 23 06 00                  call 0x140266ff0
00204C31  49 FF 86 C0 1A 00 00            inc qword ptr [r14 + 0x1ac0]
00204C38  41 89 86 B8 1A 00 00            mov dword ptr [r14 + 0x1ab8], eax
00204C3F  49 8B D5                        mov rdx, r13
00204C42  48 8B CE                        mov rcx, rsi
00204C45  E8 C6 65 1A 00                  call 0x1403ab210
00204C4A  44 8B F0                        mov r14d, eax
00204C4D  85 C0                           test eax, eax
00204C4F  0F 88 8A 02 00 00               js 0x140204edf
00204C55  80 BE 08 03 00 00 00            cmp byte ptr [rsi + 0x308], 0
00204C5C  75 50                           jne 0x140204cae
00204C5E  4C 8B 7D 20                     mov r15, qword ptr [rbp + 0x20]
00204C62  41 8B 4F 04                     mov ecx, dword ptr [r15 + 4]
00204C66  8B C1                           mov eax, ecx
00204C68  C1 E8 0C                        shr eax, 0xc
00204C6B  85 C0                           test eax, eax
00204C6D  75 02                           jne 0x140204c71
00204C6F  CD 2C                           int 0x2c
00204C71  FF C8                           dec eax
00204C73  81 E1 FF 0F 00 00               and ecx, 0xfff
00204C79  C1 E0 0C                        shl eax, 0xc
00204C7C  0B C1                           or eax, ecx
00204C7E  41 89 47 04                     mov dword ptr [r15 + 4], eax
00204C82  48 8B 8E 20 03 00 00            mov rcx, qword ptr [rsi + 0x320]
00204C89  F6 81 95 1A 00 00 04            test byte ptr [rcx + 0x1a95], 4
00204C90  74 0C                           je 0x140204c9e
00204C92  48 81 C1 B0 1A 00 00            add rcx, 0x1ab0
00204C99  E8 B2 23 06 00                  call 0x140267050
00204C9E  41 F7 47 04 00 F0 FF FF         test dword ptr [r15 + 4], 0xfffff000
00204CA6  0F 87 77 01 00 00               ja 0x140204e23
00204CAC  EB 20                           jmp 0x140204cce
00204CAE  48 8B 8E 20 03 00 00            mov rcx, qword ptr [rsi + 0x320]
00204CB5  F6 81 95 1A 00 00 04            test byte ptr [rcx + 0x1a95], 4
00204CBC  74 0C                           je 0x140204cca
00204CBE  48 81 C1 B0 1A 00 00            add rcx, 0x1ab0
00204CC5  E8 86 23 06 00                  call 0x140267050
00204CCA  4C 8B 7D 20                     mov r15, qword ptr [rbp + 0x20]
00204CCE  8B 55 1C                        mov edx, dword ptr [rbp + 0x1c]
00204CD1  48 8D 4E 40                     lea rcx, [rsi + 0x40]
00204CD5  4C 8D 46 58                     lea r8, [rsi + 0x58]
00204CD9  E8 42 80 1A 00                  call 0x1403acd20
00204CDE  44 8B F0                        mov r14d, eax
00204CE1  85 C0                           test eax, eax
00204CE3  79 72                           jns 0x140204d57
00204CE5  3D 06 00 00 C0                  cmp eax, 0xc0000006
00204CEA  74 26                           je 0x140204d12
00204CEC  3D 25 02 00 C0                  cmp eax, 0xc0000225
00204CF1  75 10                           jne 0x140204d03
00204CF3  48 8B 86 F8 08 00 00            mov rax, qword ptr [rsi + 0x8f8]
00204CFA  83 38 02                        cmp dword ptr [rax], 2
00204CFD  0F 8D 20 01 00 00               jge 0x140204e23
00204D03  CD 2C                           int 0x2c
00204D05  41 81 FE 25 02 00 C0            cmp r14d, 0xc0000225
00204D0C  0F 84 11 01 00 00               je 0x140204e23
00204D12  4C 8B 7D 08                     mov r15, qword ptr [rbp + 8]
00204D16  48 85 F6                        test rsi, rsi
00204D19  48 8D 46 10                     lea rax, [rsi + 0x10]
00204D1D  B9 00 00 00 00                  mov ecx, 0
00204D22  48 0F 44 C1                     cmove rax, rcx
00204D26  48 8B 00                        mov rax, qword ptr [rax]
00204D29  83 38 FF                        cmp dword ptr [rax], -1
00204D2C  0F 84 67 02 00 00               je 0x140204f99
00204D32  4D 85 FF                        test r15, r15
00204D35  0F 84 5E 02 00 00               je 0x140204f99
00204D3B  48 8B 06                        mov rax, qword ptr [rsi]
00204D3E  4C 3B F8                        cmp r15, rax
00204D41  0F 84 52 02 00 00               je 0x140204f99
00204D47  48 85 C0                        test rax, rax
00204D4A  0F 85 AC 01 00 00               jne 0x140204efc
00204D50  8B F8                           mov edi, eax
00204D52  E9 A9 01 00 00                  jmp 0x140204f00
00204D57  4C 8D 46 58                     lea r8, [rsi + 0x58]
00204D5B  49 8B D7                        mov rdx, r15
00204D5E  48 8B CE                        mov rcx, rsi
00204D61  E8 9A 86 1A 00                  call 0x1403ad400
00204D66  44 8B F0                        mov r14d, eax
00204D69  85 C0                           test eax, eax
00204D6B  78 A5                           js 0x140204d12
00204D6D  48 8D 8E C0 00 00 00            lea rcx, [rsi + 0xc0]
00204D74  49 8B D7                        mov rdx, r15
00204D77  E8 D4 3F 06 00                  call 0x140268d50
00204D7C  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00204D80  8B 41 10                        mov eax, dword ptr [rcx + 0x10]
00204D83  A8 01                           test al, 1
00204D85  0F 84 93 00 00 00               je 0x140204e1e
00204D8B  44 8B 75 00                     mov r14d, dword ptr [rbp]
00204D8F  45 85 F6                        test r14d, r14d
00204D92  74 63                           je 0x140204df7
00204D94  8B C3                           mov eax, ebx
00204D96  2B C7                           sub eax, edi
00204D98  41 3B C6                        cmp eax, r14d
00204D9B  74 5A                           je 0x140204df7
00204D9D  48 8B 8E 20 03 00 00            mov rcx, qword ptr [rsi + 0x320]
00204DA4  E8 BF B0 0D 00                  call 0x1402dfe68
00204DA9  48 8B 8E 20 03 00 00            mov rcx, qword ptr [rsi + 0x320]
00204DB0  48 8D 55 04                     lea rdx, [rbp + 4]
00204DB4  45 8B C6                        mov r8d, r14d
00204DB7  48 8B 89 90 1D 00 00            mov rcx, qword ptr [rcx + 0x1d90]
00204DBE  E8 E9 B5 40 00                  call 0x1406103ac
00204DC3  48 8B BE 20 03 00 00            mov rdi, qword ptr [rsi + 0x320]
00204DCA  F6 87 95 1A 00 00 04            test byte ptr [rdi + 0x1a95], 4
00204DD1  74 19                           je 0x140204dec
00204DD3  48 8D 8F 98 1A 00 00            lea rcx, [rdi + 0x1a98]
00204DDA  E8 11 22 06 00                  call 0x140266ff0
00204DDF  48 FF 87 A8 1A 00 00            inc qword ptr [rdi + 0x1aa8]
00204DE6  89 87 A0 1A 00 00               mov dword ptr [rdi + 0x1aa0], eax
00204DEC  8B 7D 04                        mov edi, dword ptr [rbp + 4]
00204DEF  33 C0                           xor eax, eax
00204DF1  44 8B F0                        mov r14d, eax
00204DF4  89 45 00                        mov dword ptr [rbp], eax
00204DF7  48 8B 8E F8 08 00 00            mov rcx, qword ptr [rsi + 0x8f8]
00204DFE  8B 01                           mov eax, dword ptr [rcx]
00204E00  85 C0                           test eax, eax
00204E02  74 0A                           je 0x140204e0e
00204E04  83 F8 03                        cmp eax, 3
00204E07  75 15                           jne 0x140204e1e
00204E09  3B 59 04                        cmp ebx, dword ptr [rcx + 4]
00204E0C  73 10                           jae 0x140204e1e
00204E0E  45 85 F6                        test r14d, r14d
00204E11  0F 44 FB                        cmove edi, ebx
00204E14  41 FF C6                        inc r14d
00204E17  44 89 75 00                     mov dword ptr [rbp], r14d
00204E1B  89 7D 04                        mov dword ptr [rbp + 4], edi
00204E1E  39 5D 18                        cmp dword ptr [rbp + 0x18], ebx
00204E21  74 27                           je 0x140204e4a
00204E23  48 8B 45 28                     mov rax, qword ptr [rbp + 0x28]
00204E27  4D 8B C5                        mov r8, r13
00204E2A  48 8B CE                        mov rcx, rsi
00204E2D  8B 50 08                        mov edx, dword ptr [rax + 8]
00204E30  E8 8B 75 1A 00                  call 0x1403ac3c0
00204E35  44 8B F0                        mov r14d, eax
00204E38  3D 06 00 00 C0                  cmp eax, 0xc0000006
00204E3D  0F 84 CF FE FF FF               je 0x140204d12
00204E43  33 DB                           xor ebx, ebx
00204E45  E9 16 FC FF FF                  jmp 0x140204a60
00204E4A  4C 8B 7D 08                     mov r15, qword ptr [rbp + 8]
00204E4E  8B 5D 00                        mov ebx, dword ptr [rbp]
00204E51  85 DB                           test ebx, ebx
00204E53  74 4F                           je 0x140204ea4
00204E55  48 8B 8E 20 03 00 00            mov rcx, qword ptr [rsi + 0x320]
00204E5C  E8 07 B0 0D 00                  call 0x1402dfe68
00204E61  48 8B 8E 20 03 00 00            mov rcx, qword ptr [rsi + 0x320]
00204E68  48 8D 55 04                     lea rdx, [rbp + 4]
00204E6C  44 8B C3                        mov r8d, ebx
00204E6F  48 8B 89 90 1D 00 00            mov rcx, qword ptr [rcx + 0x1d90]
00204E76  E8 31 B5 40 00                  call 0x1406103ac
00204E7B  48 8B 9E 20 03 00 00            mov rbx, qword ptr [rsi + 0x320]
00204E82  F6 83 95 1A 00 00 04            test byte ptr [rbx + 0x1a95], 4
00204E89  74 19                           je 0x140204ea4
00204E8B  48 8D 8B 98 1A 00 00            lea rcx, [rbx + 0x1a98]
00204E92  E8 59 21 06 00                  call 0x140266ff0
00204E97  48 FF 83 A8 1A 00 00            inc qword ptr [rbx + 0x1aa8]
00204E9E  89 83 A0 1A 00 00               mov dword ptr [rbx + 0x1aa0], eax
00204EA4  80 BE 08 03 00 00 00            cmp byte ptr [rsi + 0x308], 0
00204EAB  75 28                           jne 0x140204ed5
00204EAD  0F B6 86 E8 08 00 00            movzx eax, byte ptr [rsi + 0x8e8]
00204EB4  24 03                           and al, 3
00204EB6  3C 03                           cmp al, 3
00204EB8  74 1B                           je 0x140204ed5
00204EBA  45 33 C0                        xor r8d, r8d
00204EBD  33 D2                           xor edx, edx
00204EBF  48 8B CE                        mov rcx, rsi
00204EC2  E8 B5 C5 20 00                  call 0x14041147c
00204EC7  85 C0                           test eax, eax
00204EC9  74 0A                           je 0x140204ed5
00204ECB  8B D0                           mov edx, eax
00204ECD  48 8B CE                        mov rcx, rsi
00204ED0  E8 BB C8 20 00                  call 0x140411790
00204ED5  33 C0                           xor eax, eax
00204ED7  44 8B F0                        mov r14d, eax
00204EDA  E9 37 FE FF FF                  jmp 0x140204d16
00204EDF  3D 06 00 00 C0                  cmp eax, 0xc0000006
00204EE4  0F 84 28 FE FF FF               je 0x140204d12
00204EEA  CD 2C                           int 0x2c
00204EEC  E9 21 FE FF FF                  jmp 0x140204d12
00204EF1  41 BE 06 00 00 C0               mov r14d, 0xc0000006
00204EF7  E9 1A FE FF FF                  jmp 0x140204d16
00204EFC  0F B6 78 02                     movzx edi, byte ptr [rax + 2]
00204F00  8B C7                           mov eax, edi
00204F02  48 C1 E0 04                     shl rax, 4
00204F06  48 8D 48 0F                     lea rcx, [rax + 0xf]
00204F0A  48 3B C8                        cmp rcx, rax
00204F0D  77 0A                           ja 0x140204f19
00204F0F  48 B9 F0 FF FF FF FF FF FF 0F   movabs rcx, 0xffffffffffffff0
00204F19  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
00204F1D  48 8B C1                        mov rax, rcx
00204F20  E8 3B 5A 4B 00                  call 0x1406ba960
00204F25  41 8B 57 10                     mov edx, dword ptr [r15 + 0x10]
00204F29  4C 8D 45 38                     lea r8, [rbp + 0x38]
00204F2D  48 2B E1                        sub rsp, rcx
00204F30  48 C7 45 58 01 00 00 00         mov qword ptr [rbp + 0x58], 1
00204F38  0F 57 C0                        xorps xmm0, xmm0
00204F3B  89 7D 54                        mov dword ptr [rbp + 0x54], edi
00204F3E  33 C0                           xor eax, eax
00204F40  48 8B CE                        mov rcx, rsi
00204F43  F3 0F 7F 45 40                  movdqu xmmword ptr [rbp + 0x40], xmm0
00204F48  48 8D 5C 24 40                  lea rbx, [rsp + 0x40]
00204F4D  89 45 50                        mov dword ptr [rbp + 0x50], eax
00204F50  48 89 5D 38                     mov qword ptr [rbp + 0x38], rbx
00204F54  E8 67 74 1A 00                  call 0x1403ac3c0
00204F59  8D 57 FE                        lea edx, [rdi - 2]
00204F5C  48 8B CE                        mov rcx, rsi
00204F5F  48 03 D2                        add rdx, rdx
00204F62  48 8B 7C D3 08                  mov rdi, qword ptr [rbx + rdx*8 + 8]
00204F67  48 8B 1C D3                     mov rbx, qword ptr [rbx + rdx*8]
00204F6B  48 8D 55 38                     lea rdx, [rbp + 0x38]
00204F6F  E8 5C 76 1A 00                  call 0x1403ac5d0
00204F74  48 8D 43 08                     lea rax, [rbx + 8]
00204F78  4C 8D 43 10                     lea r8, [rbx + 0x10]
00204F7C  49 3B F8                        cmp rdi, r8
00204F7F  48 8D 57 F8                     lea rdx, [rdi - 8]
00204F83  48 0F 46 D0                     cmovbe rdx, rax
00204F87  48 8B 46 10                     mov rax, qword ptr [rsi + 0x10]
00204F8B  83 38 FF                        cmp dword ptr [rax], -1
00204F8E  74 09                           je 0x140204f99
00204F90  48 8D 4E 10                     lea rcx, [rsi + 0x10]
00204F94  E8 D7 4A 1A 00                  call 0x1403a9a70
00204F99  41 8B C6                        mov eax, r14d
00204F9C  48 8B 4D 60                     mov rcx, qword ptr [rbp + 0x60]
00204FA0  48 33 CD                        xor rcx, rbp
00204FA3  E8 98 76 4A 00                  call 0x1406ac640
00204FA8  48 8B 9D C0 00 00 00            mov rbx, qword ptr [rbp + 0xc0]
00204FAF  48 8D 65 70                     lea rsp, [rbp + 0x70]
00204FB3  41 5F                           pop r15
00204FB5  41 5E                           pop r14
00204FB7  41 5D                           pop r13
00204FB9  41 5C                           pop r12
00204FBB  5F                              pop rdi
00204FBC  5E                              pop rsi
00204FBD  5D                              pop rbp
00204FBE  C3                              ret
00204FBF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ST_STORE_SM_TRAITS___StDmPageRemove(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m54;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m8C;
    unsigned int v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned int v_stack_mA4;
    unsigned __int64 v_stack_mA8;
    unsigned __int16 v_stack_mB0;
    unsigned __int16 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC8;
    unsigned __int64 v_stack_p18;

    v_rsp = (v_rsp) - (176);
    v_stack_p18 = v_rbx;
    result = (*(unsigned __int64 *)(v_rip + 12606842)) ^ (v_stack_mA8);
    v_stack_m48 = result;
    v_stack_m80 = a2;
    result = v_rip + 12730092;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12730121)))) & (16)) == 0) { result = 0; }
    v_stack_m78 = result;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 8))) - 1);
    result = (unsigned int)((result) + (*(unsigned int *)(a2 + 12)));
    v_stack_m90 = (unsigned int)(result);
    v_stack_mA0 = v_xmm0;
    result = (unsigned int)(*(unsigned int *)(a1 + 24 + 32));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 24 + 32)))) & (1)) != 0) {
        a2 = a1 + 24;
        result = B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS____ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PA(a1, a2, a3, a4);
    }
    result = (unsigned int)(*(unsigned int *)(a1 + 120));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 120)))) & (1)) != 0) {
        a1 = a1 + 64;
        a2 = a1 + 88;
        result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_R(a1, a2, a3, a4);
    }
    v_stack_mA8 = 0;
    v_stack_mA4 = 0;
    result = B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS____ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PA(a1, (unsigned int)(*(unsigned int *)(a2 + 8)), a1 + 24, a4);
    if (((unsigned int)(result)) == 0xC0000006ULL) goto loc_00204D12;
loc_00204A60:
    result = B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS____ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PA(a1, v_stack_mA0, a1 + 24, a4);
    if (v_stack_mA0 == 0) goto loc_00204E4E;
    v_r12 = (v_stack_m98) + (8);
    result = ((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_mA0)))) + (2);
    v_stack_m98 = v_r12;
    if (v_r12 < (v_stack_mA0 + result * 8)) goto loc_00204AF4;
    result = a1 + 16;
    if (a1 == 0) {
        result = 0;
    }
    if ((*(unsigned int *)(*(unsigned __int64 *)(result))) == -1) goto loc_00204ACD;
    result = B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS____ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PA(a1, v_stack_mA0, a1 + 24, a4);
    if (result != -1) goto loc_00204B9F;
    goto loc_00204AF7;
loc_00204ACD:
    if (a1 == 0) { a1 = 0; }
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1))) == -1) goto loc_00204B9B;
loc_00204AE5:
    v_stack_mA0 = (unsigned int)(0xD1EULL);
    v_stack_m98 = (unsigned int)(0xD1EULL) + 16;
loc_00204AF4:
loc_00204AF7:
    if (((unsigned int)(0xD1EULL) + 16) == -1) goto loc_00204EF1;
    if ((unsigned int)(0xD1EULL) + 16 == 0) goto loc_00204E4E;
    if (v_stack_m90 < ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(0xD1EULL) + 16))))) goto loc_00204E4E;
    result = ST_STORE_SM_TRAITS___StDmCombinePageEntry(a1, (unsigned int)(0xD1EULL) + 16, a1 + 24, a4);
    v_stack_m88 = result;
    v_stack_m8C = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(0xD1EULL) + 16 + 4)));
    result = ST_STORE_SM_TRAITS___StDmPageRecordUnprotect(a1, result, a1 + 24, a4);
    result = v_stack_m78;
    if (v_stack_m78 != 0) {
        a1 = 0;
        a3 = (unsigned int)(0xD1EULL) + 16;
        v_stack_mB0 = 0;
        a2 = 1;
        v_stack_mB8 = 0;
        a1 = *(unsigned int *)(result);
        v_stack_mC0 = a1;
        v_stack_mC8 = (unsigned int)(a1);
        a1 = v_stack_m78;
        result = SmEtwLogStoreOp(a1, a2, a3, a4);
    }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)))) == -1) goto loc_00204B8B;
    v_r13 = a1 + 32;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48))) != 0) {
        v_r13 = (unsigned int)(*(unsigned int *)(a1 + 48)) - 1;
        v_r13 = (v_r13) << (4);
        v_r13 = (v_r13) + (*(unsigned __int64 *)(a1 + 24));
    }
    if ((*(unsigned __int64 *)(v_r13)) != ((unsigned int)(0xD1EULL))) goto loc_00204BB0;
    *(unsigned __int64 *)(v_r13 + 8) = (unsigned int)(0xD1EULL) + 16;
    goto loc_00204C01;
loc_00204B9B:
loc_00204B9F:
    if (*(unsigned __int64 *)((unsigned int)(0xD1EULL) + 8) != 0) goto loc_00204AE5;
    goto loc_00204AF7;
loc_00204BB0:
    result = B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS____ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PA(a1, a1 + 24, a3, a4);
    if ((*(unsigned int *)(a1 + 48)) != -1) goto loc_00204BD1;
    *(unsigned __int64 *)(a1 + 24) = v_xmm0;
    goto loc_00204C01;
loc_00204BD1:
    result = B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS____ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PA(a1, (unsigned int)(*(unsigned int *)((unsigned int)(0xD1EULL) + 16)), a1 + 24, a4);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24 + 24)))) == -1) goto loc_00204BFD;
    v_r14 = (unsigned int)(*(unsigned int *)((unsigned int)(0xD1EULL) + 16));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24 + 24))) != 0) {
        v_r14 = (unsigned int)(*(unsigned int *)(a1 + 24 + 24)) - 1;
        v_r14 = (v_r14) << (4);
        v_r14 = (v_r14) + (*(unsigned __int64 *)(a1 + 24));
    }
    *(unsigned __int64 *)(v_r14 + 8) = (unsigned int)(0xD1EULL) + 16;
loc_00204C01:
    result = B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS____ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PA(v_stack_mA0, a1, a1 + 24, a4);
    v_stack_mA0 = v_xmm0;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 800) + 6805)) & (4)) != 0) {
        a1 = *(unsigned __int64 *)(a1 + 800) + 6832;
        result = StLockAcquireExclusive(a1, a1, a1 + 24, a4);
        *(unsigned int *)(*(unsigned __int64 *)(a1 + 800) + 6840) = (unsigned int)(result);
    }
    result = B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS____ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PA(a1, a1 + 24, a1 + 24, a4);
    if (sign_flag) goto loc_00204EDF;
    if ((*(unsigned __int8 *)(a1 + 776)) != 0) goto loc_00204CAE;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m88 + 4))))) >> (12));
    if ((unsigned int)(result) == 0) {
    }
    result = (unsigned int)((result) - 1);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m88 + 4))) & (0xFFFULL));
    result = (unsigned int)((result) << (12));
    result = (unsigned int)((result) | ((unsigned int)(a1)));
    *(unsigned int *)(v_stack_m88 + 4) = (unsigned int)(result);
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 800) + 6805)) & (4)) != 0) {
        a1 = (*(unsigned __int64 *)(a1 + 800)) + (0x1AB0ULL);
        result = StLockReleaseExclusive(a1, a1 + 24, a1 + 24, a4);
    }
    if (condition_is_above) goto loc_00204E23;
    goto loc_00204CCE;
loc_00204CAE:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 800) + 6805)) & (4)) != 0) {
        a1 = (*(unsigned __int64 *)(a1 + 800)) + (0x1AB0ULL);
        result = StLockReleaseExclusive(a1, a1 + 24, a1 + 24, a4);
    }
loc_00204CCE:
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_R(a1 + 64, (unsigned int)(v_stack_m8C), a1 + 88, a4);
    if (!sign_flag) goto loc_00204D57;
    if (((unsigned int)(result)) == 0xC0000006ULL) goto loc_00204D12;
    if (((unsigned int)(result)) != 0xC0000225ULL) goto loc_00204D03;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 2296))) >= 2) goto loc_00204E23;
loc_00204D03:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 0xC0000225ULL) goto loc_00204E23;
loc_00204D12:
loc_00204D16:
    result = a1 + 16;
    if (a1 == 0) { result = 0; }
    if ((*(unsigned int *)(*(unsigned __int64 *)(result))) == -1) goto loc_00204F99;
    if (v_stack_mA0 == 0) goto loc_00204F99;
    if (v_stack_mA0 == (*(unsigned __int64 *)(a1))) goto loc_00204F99;
    if (*(unsigned __int64 *)(a1) != 0) goto loc_00204EFC;
    goto loc_00204F00;
loc_00204D57:
    result = ST_STORE_SM_TRAITS___StDmPageRecordRemove(a1, v_stack_mA0, a1 + 88, a4);
    if (sign_flag) goto loc_00204D12;
    result = SmHpChunkFree(a1 + 192, v_stack_mA0, a1 + 88, a4);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m80 + 16)))) & (1)) == 0) goto loc_00204E1E;
    if ((unsigned int)((unsigned int)(v_stack_mA8)) == 0) goto loc_00204DF7;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(0xD1EULL) + 16))))) - ((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(a1))))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(v_stack_mA8)))) goto loc_00204DF7;
    result = SMKM_STORE_SM_TRAITS___SmStReleaseStoreLockExclusive(*(unsigned __int64 *)(a1 + 800), v_stack_mA0, a1 + 88, a4);
    result = SMKM_STORE_MGR_SM_TRAITS___SmEvictKeys(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 800) + 7568), v_stack_mA4, (unsigned int)((unsigned int)((unsigned int)(v_stack_mA8))), a4);
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 800) + 6805)) & (4)) != 0) {
        a1 = *(unsigned __int64 *)(a1 + 800) + 6808;
        result = StLockAcquireExclusive(a1, v_stack_mA4, (unsigned int)((unsigned int)((unsigned int)(v_stack_mA8))), a4);
        *(unsigned int *)(*(unsigned __int64 *)(a1 + 800) + 6816) = (unsigned int)(result);
    }
    result = 0;
    v_stack_mA8 = 0;
loc_00204DF7:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 2296)))) == 0) goto loc_00204E0E;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 2296))))) != 3) goto loc_00204E1E;
    v_rdi = (unsigned int)(v_stack_mA4);
    v_r14 = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(0xD1EULL) + 16)))) < (*(unsigned int *)(*(unsigned __int64 *)(a1 + 2296) + 4))) {
        v_rdi = (unsigned int)(v_stack_mA4);
        if (0 == 0) { v_rdi = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(0xD1EULL) + 16))); }
        v_r14 = (unsigned int)((0) + 1);
        v_stack_mA8 = (unsigned int)(v_r14);
        v_stack_mA4 = (unsigned int)(v_rdi);
    }
    if (v_stack_m90 == ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(0xD1EULL) + 16))))) goto loc_00204E4A;
loc_00204E23:
    result = B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS____ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PA(a1, (unsigned int)(*(unsigned int *)(v_stack_m80 + 8)), a1 + 24, a4);
    if (((unsigned int)(result)) == 0xC0000006ULL) goto loc_00204D12;
    v_rbx = 0;
    goto loc_00204A60;
loc_00204E4A:
loc_00204E4E:
    if ((unsigned int)((unsigned int)(v_stack_mA8)) == 0) goto loc_00204EA4;
    result = SMKM_STORE_SM_TRAITS___SmStReleaseStoreLockExclusive(*(unsigned __int64 *)(a1 + 800), (unsigned int)(*(unsigned int *)(v_stack_m80 + 8)), a1 + 24, a4);
    result = SMKM_STORE_MGR_SM_TRAITS___SmEvictKeys(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 800) + 7568), v_stack_mA4, (unsigned int)((unsigned int)((unsigned int)(v_stack_mA8))), a4);
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 800) + 6805)) & (4)) != 0) {
        a1 = *(unsigned __int64 *)(a1 + 800) + 6808;
        result = StLockAcquireExclusive(a1, v_stack_mA4, (unsigned int)((unsigned int)((unsigned int)(v_stack_mA8))), a4);
        *(unsigned int *)(*(unsigned __int64 *)(a1 + 800) + 6816) = (unsigned int)(result);
    }
    if ((*(unsigned __int8 *)(a1 + 776)) != 0) goto loc_00204ED5;
    result = (unsigned __int8)((*(unsigned __int8 *)(a1 + 2280)) & (3));
    if (((unsigned __int8)(result)) == 3) goto loc_00204ED5;
    a3 = 0;
    a2 = 0;
    result = ST_STORE_SM_TRAITS___StDmCheckForCompaction(a1, a2, a3, a4);
    if ((unsigned int)(result) != 0) {
        a2 = (unsigned int)(result);
        a1 = a1;
        result = ST_STORE_SM_TRAITS___StQueueCompaction(a1, a2, a3, a4);
    }
    result = 0;
    goto loc_00204D16;
loc_00204EDF:
    if (0 == 0xC0000006ULL) goto loc_00204D12;
    goto loc_00204D12;
loc_00204EF1:
    goto loc_00204D16;
loc_00204EFC:
loc_00204F00:
    result = ((unsigned int)((unsigned int)(*(unsigned __int8 *)(result + 2)))) << (4);
    if ((result + 15) <= result) {
    }
    a1 = (result + 15) & (-16);
    result = _chkstk(a1, a2, a3, a4);
    v_rsp = (v_rsp) - (a1);
    v_stack_m50 = 1;
    v_stack_m54 = (unsigned int)(*(unsigned __int8 *)(result + 2));
    result = 0;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = 0;
    v_stack_m70 = v_stack_mA8;
    result = B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS____ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PA(a1, (unsigned int)(*(unsigned int *)(v_stack_mA0 + 16)), v_stack_m70, a4);
    a2 = (*(unsigned __int8 *)(result + 2) - 2) + (*(unsigned __int8 *)(result + 2) - 2);
    result = B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS____ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PA(a1, v_stack_m70, v_stack_m70, a4);
    a2 = *(unsigned __int64 *)(v_stack_mA8 + a2 * 8 + 8) - 8;
    if ((*(unsigned __int64 *)(v_stack_mA8 + a2 * 8 + 8)) <= (*(unsigned __int64 *)(v_stack_mA8 + a2 * 8) + 16)) { a2 = *(unsigned __int64 *)(v_stack_mA8 + a2 * 8) + 8; }
    result = *(unsigned __int64 *)(a1 + 16);
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 16))) != -1) {
        a1 = a1 + 16;
        result = NP_CONTEXT__NpLeafDerefInternal(a1, a2, *(unsigned __int64 *)(v_stack_mA8 + a2 * 8) + 16, a4);
    }
    a1 = (v_stack_m48) ^ (v_stack_mA8);
    result = _security_check_cookie(a1, a2, *(unsigned __int64 *)(v_stack_mA8 + a2 * 8) + 16, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ST_STORE_SM_TRAITS___StDmPageRemove(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m38;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint32_t v_stack_m54;
    uint32_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint32_t v_stack_m8C;
    uint32_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint32_t v_stack_mA4;
    uint64_t v_stack_mA8;
    uint16_t v_stack_mB0;
    uint16_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC8;
    uint64_t v_stack_p18;

    local_rsp = (local_rsp) - (176);
    v_stack_p18 = local_rbx;
    result = (*(uint64_t *)(v_rip + 0xC05D7A)) ^ (v_stack_mA8);
    v_stack_m48 = result;
    v_stack_m80 = Arg2;
    result = v_rip + 12730092;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC23F09)))) & (16)) == 0) { result = 0; }
    v_stack_m78 = result;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x8))) - 1);
    result = (uint32_t)((result) + (*(uint32_t *)(arg2 + 0xC)));
    v_stack_m90 = (uint32_t)(result);
    v_stack_mA0 = v_xmm0;
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x18 + 0x20));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18 + 0x20)))) & (1)) != 0) {
        Arg2 = Arg1 + 24;
        result = B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS____ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PA(Arg1, Arg2, a3, a4);
    }
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x78));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x78)))) & (1)) != 0) {
        Arg1 = Arg1 + 64;
        Arg2 = Arg1 + 88;
        result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_R(Arg1, Arg2, a3, a4);
    }
    v_stack_mA8 = 0;
    v_stack_mA4 = 0;
    result = B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS____ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PA(Arg1, (uint32_t)(*(uint32_t *)(arg2 + 0x8)), Arg1 + 24, a4);
    if (((uint32_t)(result)) == 0xC0000006ULL) goto loc_00204D12;
loc_00204A60:
    result = B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS____ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PA(Arg1, v_stack_mA0, Arg1 + 24, a4);
    if (v_stack_mA0 == 0) goto loc_00204E4E;
    local_r12 = (v_stack_m98) + (8);
    result = ((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_mA0)))) + (2);
    v_stack_m98 = local_r12;
    if (local_r12 < (v_stack_mA0 + result * 8)) goto loc_00204AF4;
    result = Arg1 + 16;
    if (Arg1 == NULL) {
        result = 0;
    }
    if ((*(uint32_t *)(*(uint64_t *)(result))) == -1) goto loc_00204ACD;
    result = B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS____ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PA(Arg1, v_stack_mA0, Arg1 + 24, a4);
    if (result != -1) goto loc_00204B9F;
    goto loc_00204AF7;
loc_00204ACD:
    if (Arg1 == NULL) { Arg1 = 0; }
    if ((*(uint32_t *)(*(uint64_t *)(arg1))) == -1) goto loc_00204B9B;
loc_00204AE5:
    v_stack_mA0 = (uint32_t)(0xD1EULL);
    v_stack_m98 = (uint32_t)(0xD1EULL) + 16;
loc_00204AF4:
loc_00204AF7:
    if (((uint32_t)(0xD1EULL) + 16) == -1) goto loc_00204EF1;
    if ((uint32_t)(0xD1EULL) + 16 == 0) goto loc_00204E4E;
    if (v_stack_m90 < ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(0xD1EULL) + 0x10))))) goto loc_00204E4E;
    result = ST_STORE_SM_TRAITS___StDmCombinePageEntry(Arg1, (uint32_t)(0xD1EULL) + 16, Arg1 + 24, a4);
    v_stack_m88 = result;
    v_stack_m8C = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(0xD1EULL) + 0x10 + 0x4)));
    result = ST_STORE_SM_TRAITS___StDmPageRecordUnprotect(Arg1, result, Arg1 + 24, a4);
    result = v_stack_m78;
    if (v_stack_m78 != 0) {
        Arg1 = 0;
        a3 = (uint32_t)(0xD1EULL) + 16;
        v_stack_mB0 = 0;
        Arg2 = 1;
        v_stack_mB8 = 0;
        Arg1 = *(uint32_t *)(result);
        v_stack_mC0 = Arg1;
        v_stack_mC8 = (uint32_t)(Arg1);
        Arg1 = v_stack_m78;
        result = SmEtwLogStoreOp(Arg1, Arg2, a3, a4);
    }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)))) == -1) goto loc_00204B8B;
    local_r13 = Arg1 + 32;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30))) != 0) {
        local_r13 = (uint32_t)(*(uint32_t *)(arg1 + 0x30)) - 1;
        local_r13 = (local_r13) << (4);
        local_r13 = (local_r13) + (*(uint64_t *)(arg1 + 0x18));
    }
    if ((*(uint64_t *)(local_r13)) != ((uint32_t)(0xD1EULL))) goto loc_00204BB0;
    *(uint64_t *)(local_r13 + 0x8) = (uint32_t)(0xD1EULL) + 16;
    goto loc_00204C01;
loc_00204B9B:
loc_00204B9F:
    if (*(uint64_t *)((uint32_t)(0xD1EULL) + 0x8) != 0) goto loc_00204AE5;
    goto loc_00204AF7;
loc_00204BB0:
    result = B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS____ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PA(Arg1, Arg1 + 24, a3, a4);
    if ((*(uint32_t *)(arg1 + 0x30)) != -1) goto loc_00204BD1;
    *(uint64_t *)(arg1 + 0x18) = v_xmm0;
    goto loc_00204C01;
loc_00204BD1:
    result = B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS____ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PA(Arg1, (uint32_t)(*(uint32_t *)((uint32_t)(0xD1EULL) + 0x10)), Arg1 + 24, a4);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18 + 0x18)))) == -1) goto loc_00204BFD;
    local_r14 = (uint32_t)(*(uint32_t *)((uint32_t)(0xD1EULL) + 0x10));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18 + 0x18))) != 0) {
        local_r14 = (uint32_t)(*(uint32_t *)(arg1 + 0x18 + 0x18)) - 1;
        local_r14 = (local_r14) << (4);
        local_r14 = (local_r14) + (*(uint64_t *)(arg1 + 0x18));
    }
    *(uint64_t *)(local_r14 + 0x8) = (uint32_t)(0xD1EULL) + 16;
loc_00204C01:
    result = B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS____ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PA(v_stack_mA0, Arg1, Arg1 + 24, a4);
    v_stack_mA0 = v_xmm0;
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x320) + 0x1A95)) & (4)) != 0) {
        Arg1 = *(uint64_t *)(arg1 + 0x320) + 6832;
        result = StLockAcquireExclusive(Arg1, Arg1, Arg1 + 24, a4);
        *(uint32_t *)(*(uint64_t *)(arg1 + 0x320) + 0x1AB8) = (uint32_t)(result);
    }
    result = B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS____ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PA(Arg1, Arg1 + 24, Arg1 + 24, a4);
    if (sign_flag) goto loc_00204EDF;
    if ((*(uint8_t *)(arg1 + 0x308)) != 0) goto loc_00204CAE;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m88 + 0x4))))) >> (12));
    if ((uint32_t)(result) == 0) {
    }
    result = (uint32_t)((result) - 1);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m88 + 0x4))) & (0xFFFULL));
    result = (uint32_t)((result) << (12));
    result = (uint32_t)((result) | ((uint32_t)(Arg1)));
    *(uint32_t *)(v_stack_m88 + 0x4) = (uint32_t)(result);
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x320) + 0x1A95)) & (4)) != 0) {
        Arg1 = (*(uint64_t *)(arg1 + 0x320)) + (0x1AB0ULL);
        result = StLockReleaseExclusive(Arg1, Arg1 + 24, Arg1 + 24, a4);
    }
    if (condition_is_above) goto loc_00204E23;
    goto loc_00204CCE;
loc_00204CAE:
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x320) + 0x1A95)) & (4)) != 0) {
        Arg1 = (*(uint64_t *)(arg1 + 0x320)) + (0x1AB0ULL);
        result = StLockReleaseExclusive(Arg1, Arg1 + 24, Arg1 + 24, a4);
    }
loc_00204CCE:
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_R(Arg1 + 64, (uint32_t)(v_stack_m8C), Arg1 + 88, a4);
    if (!sign_flag) goto loc_00204D57;
    if (((uint32_t)(result)) == 0xC0000006ULL) goto loc_00204D12;
    if (((uint32_t)(result)) != 0xC0000225ULL) goto loc_00204D03;
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x8F8))) >= 2) goto loc_00204E23;
loc_00204D03:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 0xC0000225ULL) goto loc_00204E23;
loc_00204D12:
loc_00204D16:
    result = Arg1 + 16;
    if (Arg1 == NULL) { result = 0; }
    if ((*(uint32_t *)(*(uint64_t *)(result))) == -1) goto loc_00204F99;
    if (v_stack_mA0 == 0) goto loc_00204F99;
    if (v_stack_mA0 == (*(uint64_t *)(arg1))) goto loc_00204F99;
    if (*(uint64_t *)(arg1) != 0) goto loc_00204EFC;
    goto loc_00204F00;
loc_00204D57:
    result = ST_STORE_SM_TRAITS___StDmPageRecordRemove(Arg1, v_stack_mA0, Arg1 + 88, a4);
    if (sign_flag) goto loc_00204D12;
    result = SmHpChunkFree(Arg1 + 192, v_stack_mA0, Arg1 + 88, a4);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m80 + 0x10)))) & (1)) == 0) goto loc_00204E1E;
    if ((uint32_t)((uint32_t)(v_stack_mA8)) == 0) goto loc_00204DF7;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(0xD1EULL) + 0x10))))) - ((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(arg1))))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(v_stack_mA8)))) goto loc_00204DF7;
    result = SMKM_STORE_SM_TRAITS___SmStReleaseStoreLockExclusive(*(uint64_t *)(arg1 + 0x320), v_stack_mA0, Arg1 + 88, a4);
    result = SMKM_STORE_MGR_SM_TRAITS___SmEvictKeys(*(uint64_t *)(*(uint64_t *)(arg1 + 0x320) + 0x1D90), v_stack_mA4, (uint32_t)((uint32_t)((uint32_t)(v_stack_mA8))), a4);
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x320) + 0x1A95)) & (4)) != 0) {
        Arg1 = *(uint64_t *)(arg1 + 0x320) + 6808;
        result = StLockAcquireExclusive(Arg1, v_stack_mA4, (uint32_t)((uint32_t)((uint32_t)(v_stack_mA8))), a4);
        *(uint32_t *)(*(uint64_t *)(arg1 + 0x320) + 0x1AA0) = (uint32_t)(result);
    }
    result = 0;
    v_stack_mA8 = 0;
loc_00204DF7:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8F8)))) == 0) goto loc_00204E0E;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8F8))))) != 3) goto loc_00204E1E;
    local_rdi = (uint32_t)(v_stack_mA4);
    local_r14 = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(0xD1EULL) + 0x10)))) < (*(uint32_t *)(*(uint64_t *)(arg1 + 0x8F8) + 0x4))) {
        local_rdi = (uint32_t)(v_stack_mA4);
        if (0 == 0) { local_rdi = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(0xD1EULL) + 0x10))); }
        local_r14 = (uint32_t)((0) + 1);
        v_stack_mA8 = (uint32_t)(local_r14);
        v_stack_mA4 = (uint32_t)(local_rdi);
    }
    if (v_stack_m90 == ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(0xD1EULL) + 0x10))))) goto loc_00204E4A;
loc_00204E23:
    result = B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS____ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PA(Arg1, (uint32_t)(*(uint32_t *)(v_stack_m80 + 0x8)), Arg1 + 24, a4);
    if (((uint32_t)(result)) == 0xC0000006ULL) goto loc_00204D12;
    local_rbx = 0;
    goto loc_00204A60;
loc_00204E4A:
loc_00204E4E:
    if ((uint32_t)((uint32_t)(v_stack_mA8)) == 0) goto loc_00204EA4;
    result = SMKM_STORE_SM_TRAITS___SmStReleaseStoreLockExclusive(*(uint64_t *)(arg1 + 0x320), (uint32_t)(*(uint32_t *)(v_stack_m80 + 0x8)), Arg1 + 24, a4);
    result = SMKM_STORE_MGR_SM_TRAITS___SmEvictKeys(*(uint64_t *)(*(uint64_t *)(arg1 + 0x320) + 0x1D90), v_stack_mA4, (uint32_t)((uint32_t)((uint32_t)(v_stack_mA8))), a4);
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x320) + 0x1A95)) & (4)) != 0) {
        Arg1 = *(uint64_t *)(arg1 + 0x320) + 6808;
        result = StLockAcquireExclusive(Arg1, v_stack_mA4, (uint32_t)((uint32_t)((uint32_t)(v_stack_mA8))), a4);
        *(uint32_t *)(*(uint64_t *)(arg1 + 0x320) + 0x1AA0) = (uint32_t)(result);
    }
    if ((*(uint8_t *)(arg1 + 0x308)) != 0) goto loc_00204ED5;
    result = (uint8_t)((*(uint8_t *)(arg1 + 0x8E8)) & (3));
    if (((uint8_t)(result)) == 3) goto loc_00204ED5;
    a3 = 0;
    Arg2 = 0;
    result = ST_STORE_SM_TRAITS___StDmCheckForCompaction(Arg1, Arg2, a3, a4);
    if ((uint32_t)(result) != 0) {
        Arg2 = (uint32_t)(result);
        Arg1 = Arg1;
        result = ST_STORE_SM_TRAITS___StQueueCompaction(Arg1, Arg2, a3, a4);
    }
    result = 0;
    goto loc_00204D16;
loc_00204EDF:
    if (0 == 0xC0000006ULL) goto loc_00204D12;
    goto loc_00204D12;
loc_00204EF1:
    goto loc_00204D16;
loc_00204EFC:
loc_00204F00:
    result = ((uint32_t)((uint32_t)(*(uint8_t *)(result + 0x2)))) << (4);
    if ((result + 15) <= result) {
    }
    Arg1 = (result + 15) & (-16);
    result = _chkstk(Arg1, Arg2, a3, a4);
    local_rsp = (local_rsp) - (Arg1);
    v_stack_m50 = 1;
    v_stack_m54 = (uint32_t)(*(uint8_t *)(result + 0x2));
    result = 0;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = 0;
    v_stack_m70 = v_stack_mA8;
    result = B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS____ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PA(Arg1, (uint32_t)(*(uint32_t *)(v_stack_mA0 + 0x10)), v_stack_m70, a4);
    Arg2 = (*(uint8_t *)(result + 0x2) - 2) + (*(uint8_t *)(result + 0x2) - 2);
    result = B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS____ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PA(Arg1, v_stack_m70, v_stack_m70, a4);
    Arg2 = *(uint64_t *)(v_stack_mA8 + arg2 * 8 + 0x8) - 8;
    if ((*(uint64_t *)(v_stack_mA8 + arg2 * 8 + 0x8)) <= (*(uint64_t *)(v_stack_mA8 + arg2 * 8) + 16)) { Arg2 = *(uint64_t *)(v_stack_mA8 + arg2 * 8) + 8; }
    result = *(uint64_t *)(arg1 + 0x10);
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x10))) != -1) {
        Arg1 = Arg1 + 16;
        result = NP_CONTEXT__NpLeafDerefInternal(Arg1, Arg2, *(uint64_t *)(v_stack_mA8 + arg2 * 8) + 16, a4);
    }
    Arg1 = (v_stack_m48) ^ (v_stack_mA8);
    result = _security_check_cookie(Arg1, Arg2, *(uint64_t *)(v_stack_mA8 + arg2 * 8) + 16, a4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x20` | `32` | `R` |
| `Arg1` | `+ 0x20` | `32` | `R/W` |
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x58` | `64` | `R` |
| `Arg1` | `+ 0x78` | `32` | `R` |
| `Arg1` | `+ 0x78` | `32` | `R/W` |
| `Arg2` | `+ 0x8` | `32` | `R` |
| `Arg2` | `+ 0xC` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002049A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
