# ST_STORE&lt;SM_TRAITS&gt;::StCompactRegions

- RVA: `0x004A48E0`–`0x004A4F86` (길이 `1,702` bytes)
- VA: `0x00000001404A48E0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B6770`
- 디코드: `447`개 명령, `1,702/1,702` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **30**; 고유 호출 대상: **16**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004A4934` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004A4981` → [ST_STORE<SM_TRAITS>::StDmPageRecordUnprotect](../26/ST_STORE_SM_TRAITS_StDmPageRecordUnprotect_function_00268B30.md) (function, `0x00268B30`)
- `0x004A4995` → [B_TREE<unsigned long,ST_STORE<SM_TRAITS>::_ST_REGION_ENTRY,4096,NP_CONTEXT,ST_STORE<SM_TRAITS>::ST_REGION_ENTRY_COMPARATOR>::BTreeSearchResultDeref](../3A/B_TREE_unsigned_long_ST_STORE_SM_TRAITS__ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS_ST_REGIO_function_003AD260.md) (function, `0x003AD260`)
- `0x004A49C3` → [B_TREE<unsigned long,ST_STORE<SM_TRAITS>::_ST_REGION_ENTRY,4096,NP_CONTEXT,ST_STORE<SM_TRAITS>::ST_REGION_ENTRY_COMPARATOR>::BTreeSearchKey](../3A/B_TREE_unsigned_long_ST_STORE_SM_TRAITS__ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS_ST_REGIO_function_003ACD20.md) (function, `0x003ACD20`)
- `0x004A49E0` → [B_TREE<unsigned long,ST_STORE<SM_TRAITS>::_ST_REGION_ENTRY,4096,NP_CONTEXT,ST_STORE<SM_TRAITS>::ST_REGION_ENTRY_COMPARATOR>::BTreeIteratorFromSearchResult](../44/B_TREE_unsigned_long_ST_STORE_SM_TRAITS__ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS_ST_REGIO_function_004483D0.md) (function, `0x004483D0`)
- `0x004A4A16` → [B_TREE<unsigned long,ST_STORE<SM_TRAITS>::_ST_REGION_ENTRY,4096,NP_CONTEXT,ST_STORE<SM_TRAITS>::ST_REGION_ENTRY_COMPARATOR>::BTreeSearchKey](../3A/B_TREE_unsigned_long_ST_STORE_SM_TRAITS__ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS_ST_REGIO_function_003ACD20.md) (function, `0x003ACD20`)
- `0x004A4A2F` → [B_TREE<unsigned long,ST_STORE<SM_TRAITS>::_ST_REGION_ENTRY,4096,NP_CONTEXT,ST_STORE<SM_TRAITS>::ST_REGION_ENTRY_COMPARATOR>::BTreeIteratorCleanup](../44/B_TREE_unsigned_long_ST_STORE_SM_TRAITS__ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS_ST_REGIO_function_00445970.md) (function, `0x00445970`)
- `0x004A4A3F` → [B_TREE<unsigned long,ST_STORE<SM_TRAITS>::_ST_REGION_ENTRY,4096,NP_CONTEXT,ST_STORE<SM_TRAITS>::ST_REGION_ENTRY_COMPARATOR>::BTreeIteratorFromSearchResult](../44/B_TREE_unsigned_long_ST_STORE_SM_TRAITS__ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS_ST_REGIO_function_004483D0.md) (function, `0x004483D0`)
- `0x004A4A8B` → [B_TREE<unsigned long,ST_STORE<SM_TRAITS>::_ST_REGION_ENTRY,4096,NP_CONTEXT,ST_STORE<SM_TRAITS>::ST_REGION_ENTRY_COMPARATOR>::BTreeFindLeafSibling](../45/B_TREE_unsigned_long_ST_STORE_SM_TRAITS__ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS_ST_REGIO_function_00450FB8.md) (function, `0x00450FB8`)
- `0x004A4C20` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x004A4C27` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x004A4C32` → [ST_STORE<SM_TRAITS>::StDmPageRecordUnprotect](../26/ST_STORE_SM_TRAITS_StDmPageRecordUnprotect_function_00268B30.md) (function, `0x00268B30`)
- `0x004A4C7B` → [B_TREE<unsigned long,ST_STORE<SM_TRAITS>::_ST_REGION_ENTRY,4096,NP_CONTEXT,ST_STORE<SM_TRAITS>::ST_REGION_ENTRY_COMPARATOR>::BTreeSearchResultDeref](../3A/B_TREE_unsigned_long_ST_STORE_SM_TRAITS__ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS_ST_REGIO_function_003AD260.md) (function, `0x003AD260`)
- `0x004A4C9A` → [B_TREE<unsigned long,ST_STORE<SM_TRAITS>::_ST_REGION_ENTRY,4096,NP_CONTEXT,ST_STORE<SM_TRAITS>::ST_REGION_ENTRY_COMPARATOR>::BTreeSearchKey](../3A/B_TREE_unsigned_long_ST_STORE_SM_TRAITS__ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS_ST_REGIO_function_003ACD20.md) (function, `0x003ACD20`)
- `0x004A4CE2` → [B_TREE<unsigned long,ST_STORE<SM_TRAITS>::_ST_REGION_ENTRY,4096,NP_CONTEXT,ST_STORE<SM_TRAITS>::ST_REGION_ENTRY_COMPARATOR>::BTreeChangeKey](../3A/B_TREE_unsigned_long_ST_STORE_SM_TRAITS__ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS_ST_REGIO_function_003A9D80.md) (function, `0x003A9D80`)
- `0x004A4D06` → [B_TREE<unsigned long,ST_STORE<SM_TRAITS>::_ST_REGION_ENTRY,4096,NP_CONTEXT,ST_STORE<SM_TRAITS>::ST_REGION_ENTRY_COMPARATOR>::BTreeChangeKey](../3A/B_TREE_unsigned_long_ST_STORE_SM_TRAITS__ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS_ST_REGIO_function_003A9D80.md) (function, `0x003A9D80`)
- `0x004A4D35` → [B_TREE<unsigned long,ST_STORE<SM_TRAITS>::_ST_REGION_ENTRY,4096,NP_CONTEXT,ST_STORE<SM_TRAITS>::ST_REGION_ENTRY_COMPARATOR>::BTreeChangeKey](../3A/B_TREE_unsigned_long_ST_STORE_SM_TRAITS__ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS_ST_REGIO_function_003A9D80.md) (function, `0x003A9D80`)
- `0x004A4D41` → [B_TREE<unsigned long,ST_STORE<SM_TRAITS>::_ST_REGION_ENTRY,4096,NP_CONTEXT,ST_STORE<SM_TRAITS>::ST_REGION_ENTRY_COMPARATOR>::BTreeIteratorCleanup](../44/B_TREE_unsigned_long_ST_STORE_SM_TRAITS__ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS_ST_REGIO_function_00445970.md) (function, `0x00445970`)
- `0x004A4D9B` → [B_TREE<unsigned long,ST_STORE<SM_TRAITS>::_ST_REGION_ENTRY,4096,NP_CONTEXT,ST_STORE<SM_TRAITS>::ST_REGION_ENTRY_COMPARATOR>::BTreeInsert](../3A/B_TREE_unsigned_long_ST_STORE_SM_TRAITS__ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS_ST_REGIO_function_003AC820.md) (function, `0x003AC820`)
- `0x004A4DAC` → [B_TREE<unsigned long,ST_STORE<SM_TRAITS>::_ST_REGION_ENTRY,4096,NP_CONTEXT,ST_STORE<SM_TRAITS>::ST_REGION_ENTRY_COMPARATOR>::BTreeSearchResultDeref](../3A/B_TREE_unsigned_long_ST_STORE_SM_TRAITS__ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS_ST_REGIO_function_003AD260.md) (function, `0x003AD260`)
- `0x004A4DCA` → [B_TREE<unsigned long,ST_STORE<SM_TRAITS>::_ST_REGION_ENTRY,4096,NP_CONTEXT,ST_STORE<SM_TRAITS>::ST_REGION_ENTRY_COMPARATOR>::BTreeDelete](../3A/B_TREE_unsigned_long_ST_STORE_SM_TRAITS__ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS_ST_REGIO_function_003AC7A8.md) (function, `0x003AC7A8`)
- `0x004A4E04` → [ST_STORE<SM_TRAITS>::StDmpUpdateRegionState](../3A/ST_STORE_SM_TRAITS_StDmpUpdateRegionState_function_003AEFE0.md) (function, `0x003AEFE0`)
- `0x004A4E14` → [ST_STORE<SM_TRAITS>::StDmpUpdateRegionState](../3A/ST_STORE_SM_TRAITS_StDmpUpdateRegionState_function_003AEFE0.md) (function, `0x003AEFE0`)
- `0x004A4E3B` → [ST_STORE<SM_TRAITS>::StDmCheckForCompaction](../41/ST_STORE_SM_TRAITS_StDmCheckForCompaction_function_0041147C.md) (function, `0x0041147C`)
- `0x004A4E63` → [B_TREE<unsigned long,ST_STORE<SM_TRAITS>::_ST_REGION_ENTRY,4096,NP_CONTEXT,ST_STORE<SM_TRAITS>::ST_REGION_ENTRY_COMPARATOR>::BTreeChangeKey](../3A/B_TREE_unsigned_long_ST_STORE_SM_TRAITS__ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS_ST_REGIO_function_003A9D80.md) (function, `0x003A9D80`)
- `0x004A4ECC` → [_chkstk](../6B/_chkstk_function_006BA960.md) (function, `0x006BA960`)
- `0x004A4F00` → [B_TREE<unsigned long,ST_STORE<SM_TRAITS>::_ST_REGION_ENTRY,4096,NP_CONTEXT,ST_STORE<SM_TRAITS>::ST_REGION_ENTRY_COMPARATOR>::BTreeSearchKey](../3A/B_TREE_unsigned_long_ST_STORE_SM_TRAITS__ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS_ST_REGIO_function_003ACD20.md) (function, `0x003ACD20`)
- `0x004A4F1B` → [B_TREE<unsigned long,ST_STORE<SM_TRAITS>::_ST_REGION_ENTRY,4096,NP_CONTEXT,ST_STORE<SM_TRAITS>::ST_REGION_ENTRY_COMPARATOR>::BTreeSearchResultDeref](../3A/B_TREE_unsigned_long_ST_STORE_SM_TRAITS__ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS_ST_REGIO_function_003AD260.md) (function, `0x003AD260`)
- `0x004A4F40` → [NP_CONTEXT::NpLeafDerefInternal](../3A/NP_CONTEXT_NpLeafDerefInternal_function_003A9A70.md) (function, `0x003A9A70`)
- `0x004A4F51` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [ST_STORE&lt;SM_TRAITS&gt;::StDmReuseCurrentRegion](../3B/ST_STORE_SM_TRAITS_StDmReuseCurrentRegion_function_003B107C.md) at `0x003B10FC`
- [ST_STORE&lt;SM_TRAITS&gt;::StDmCurrentRegionSet](../3B/ST_STORE_SM_TRAITS_StDmCurrentRegionSet_function_003B1130.md) at `0x003B11E0`
- [ST_STORE&lt;SM_TRAITS&gt;::StCompactionPerformInMem](../41/ST_STORE_SM_TRAITS_StCompactionPerformInMem_function_004111D8.md) at `0x004112FD`
- [ST_STORE&lt;SM_TRAITS&gt;::StCompactionPerformInMem](../41/ST_STORE_SM_TRAITS_StCompactionPerformInMem_function_004111D8.md) at `0x004113B9`
- [ST_STORE&lt;SM_TRAITS&gt;::StCompactionPerformEmergency](../4E/ST_STORE_SM_TRAITS_StCompactionPerformEmergency_function_004EB170.md) at `0x004EB2CA`
- [ST_STORE&lt;SM_TRAITS&gt;::StCompactionPerformEmergency](../4E/ST_STORE_SM_TRAITS_StCompactionPerformEmergency_function_004EB170.md) at `0x004EB320`

### Static image references
- `0x004A48F9` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004A48E0  40 55                           push rbp
004A48E2  53                              push rbx
004A48E3  56                              push rsi
004A48E4  57                              push rdi
004A48E5  41 54                           push r12
004A48E7  41 55                           push r13
004A48E9  41 56                           push r14
004A48EB  41 57                           push r15
004A48ED  48 81 EC 68 01 00 00            sub rsp, 0x168
004A48F4  48 8D 6C 24 20                  lea rbp, [rsp + 0x20]
004A48F9  48 8B 05 40 5E 96 00            mov rax, qword ptr [rip + 0x965e40]
004A4900  48 33 C5                        xor rax, rbp
004A4903  48 89 85 30 01 00 00            mov qword ptr [rbp + 0x130], rax
004A490A  8B B5 B0 01 00 00               mov esi, dword ptr [rbp + 0x1b0]
004A4910  48 8B D9                        mov rbx, rcx
004A4913  45 8B E0                        mov r12d, r8d
004A4916  48 8D 8D 80 00 00 00            lea rcx, [rbp + 0x80]
004A491D  48 89 55 38                     mov qword ptr [rbp + 0x38], rdx
004A4921  41 B8 A8 00 00 00               mov r8d, 0xa8
004A4927  33 D2                           xor edx, edx
004A4929  44 89 65 20                     mov dword ptr [rbp + 0x20], r12d
004A492D  89 75 08                        mov dword ptr [rbp + 8], esi
004A4930  4C 89 4D 30                     mov qword ptr [rbp + 0x30], r9
004A4934  E8 07 23 22 00                  call 0x1406c6c40
004A4939  48 8B 8B 78 05 00 00            mov rcx, qword ptr [rbx + 0x578]
004A4940  45 33 C0                        xor r8d, r8d
004A4943  0F 57 C0                        xorps xmm0, xmm0
004A4946  44 89 45 04                     mov dword ptr [rbp + 4], r8d
004A494A  45 8B E8                        mov r13d, r8d
004A494D  0F 11 45 10                     movups xmmword ptr [rbp + 0x10], xmm0
004A4951  4A 8D 14 61                     lea rdx, [rcx + r12*2]
004A4955  48 8D 04 71                     lea rax, [rcx + rsi*2]
004A4959  48 89 55 48                     mov qword ptr [rbp + 0x48], rdx
004A495D  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
004A4961  48 3B D0                        cmp rdx, rax
004A4964  74 0D                           je 0x1404a4973
004A4966  0F B7 00                        movzx eax, word ptr [rax]
004A4969  25 FF 1F 00 00                  and eax, 0x1fff
004A496E  89 45 00                        mov dword ptr [rbp], eax
004A4971  EB 04                           jmp 0x1404a4977
004A4973  44 89 45 00                     mov dword ptr [rbp], r8d
004A4977  48 8B 93 F8 02 00 00            mov rdx, qword ptr [rbx + 0x2f8]
004A497E  48 8B CB                        mov rcx, rbx
004A4981  E8 AA 41 DC FF                  call 0x140268b30
004A4986  8B 43 78                        mov eax, dword ptr [rbx + 0x78]
004A4989  A8 01                           test al, 1
004A498B  74 0D                           je 0x1404a499a
004A498D  48 8D 4B 40                     lea rcx, [rbx + 0x40]
004A4991  48 8D 53 58                     lea rdx, [rbx + 0x58]
004A4995  E8 C6 88 F0 FF                  call 0x1403ad260
004A499A  83 63 78 FE                     and dword ptr [rbx + 0x78], 0xfffffffe
004A499E  4C 8D 7B 40                     lea r15, [rbx + 0x40]
004A49A2  8B 8B 2C 03 00 00               mov ecx, dword ptr [rbx + 0x32c]
004A49A8  4C 8D 43 58                     lea r8, [rbx + 0x58]
004A49AC  48 8B 83 F8 02 00 00            mov rax, qword ptr [rbx + 0x2f8]
004A49B3  41 8B D4                        mov edx, r12d
004A49B6  D3 E2                           shl edx, cl
004A49B8  49 8B CF                        mov rcx, r15
004A49BB  89 10                           mov dword ptr [rax], edx
004A49BD  8B 93 00 03 00 00               mov edx, dword ptr [rbx + 0x300]
004A49C3  E8 58 83 F0 FF                  call 0x1403acd20
004A49C8  8B F0                           mov esi, eax
004A49CA  3D 06 00 00 C0                  cmp eax, 0xc0000006
004A49CF  0F 84 93 04 00 00               je 0x1404a4e68
004A49D5  4C 8D 43 58                     lea r8, [rbx + 0x58]
004A49D9  49 8B CF                        mov rcx, r15
004A49DC  48 8D 55 10                     lea rdx, [rbp + 0x10]
004A49E0  E8 EB 39 FA FF                  call 0x1404483d0
004A49E5  4C 8B 75 10                     mov r14, qword ptr [rbp + 0x10]
004A49E9  0F 1F 80 00 00 00 00            nop dword ptr [rax]
004A49F0  45 85 ED                        test r13d, r13d
004A49F3  74 53                           je 0x1404a4a48
004A49F5  8B 8B 2C 03 00 00               mov ecx, dword ptr [rbx + 0x32c]
004A49FB  4C 8D 43 58                     lea r8, [rbx + 0x58]
004A49FF  48 8B 83 F8 02 00 00            mov rax, qword ptr [rbx + 0x2f8]
004A4A06  41 8B D4                        mov edx, r12d
004A4A09  D3 E2                           shl edx, cl
004A4A0B  49 8B CF                        mov rcx, r15
004A4A0E  89 10                           mov dword ptr [rax], edx
004A4A10  8B 93 00 03 00 00               mov edx, dword ptr [rbx + 0x300]
004A4A16  E8 05 83 F0 FF                  call 0x1403acd20
004A4A1B  8B F0                           mov esi, eax
004A4A1D  3D 06 00 00 C0                  cmp eax, 0xc0000006
004A4A22  0F 84 44 04 00 00               je 0x1404a4e6c
004A4A28  49 8B D7                        mov rdx, r15
004A4A2B  48 8D 4D 10                     lea rcx, [rbp + 0x10]
004A4A2F  E8 3C 0F FA FF                  call 0x140445970
004A4A34  4C 8D 43 58                     lea r8, [rbx + 0x58]
004A4A38  49 8B CF                        mov rcx, r15
004A4A3B  48 8D 55 10                     lea rdx, [rbp + 0x10]
004A4A3F  E8 8C 39 FA FF                  call 0x1404483d0
004A4A44  4C 8B 75 10                     mov r14, qword ptr [rbp + 0x10]
004A4A48  4D 85 F6                        test r14, r14
004A4A4B  0F 84 2E 05 00 00               je 0x1404a4f7f
004A4A51  48 8B 55 18                     mov rdx, qword ptr [rbp + 0x18]
004A4A55  41 8B 06                        mov eax, dword ptr [r14]
004A4A58  48 83 C2 04                     add rdx, 4
004A4A5C  0F B7 C0                        movzx eax, ax
004A4A5F  48 83 C0 04                     add rax, 4
004A4A63  48 89 55 18                     mov qword ptr [rbp + 0x18], rdx
004A4A67  49 8D 04 86                     lea rax, [r14 + rax*4]
004A4A6B  48 3B D0                        cmp rdx, rax
004A4A6E  72 5B                           jb 0x1404a4acb
004A4A70  33 F6                           xor esi, esi
004A4A72  49 8D 47 10                     lea rax, [r15 + 0x10]
004A4A76  4D 85 FF                        test r15, r15
004A4A79  75 02                           jne 0x1404a4a7d
004A4A7B  8B C6                           mov eax, esi
004A4A7D  48 8B 00                        mov rax, qword ptr [rax]
004A4A80  83 38 FF                        cmp dword ptr [rax], -1
004A4A83  74 1A                           je 0x1404a4a9f
004A4A85  49 8B D6                        mov rdx, r14
004A4A88  49 8B CF                        mov rcx, r15
004A4A8B  E8 28 C5 FA FF                  call 0x140450fb8
004A4A90  48 83 F8 FF                     cmp rax, -1
004A4A94  0F 85 3D 01 00 00               jne 0x1404a4bd7
004A4A9A  48 8B D0                        mov rdx, rax
004A4A9D  EB 2C                           jmp 0x1404a4acb
004A4A9F  49 8D 47 10                     lea rax, [r15 + 0x10]
004A4AA3  4D 85 FF                        test r15, r15
004A4AA6  75 03                           jne 0x1404a4aab
004A4AA8  48 8B C6                        mov rax, rsi
004A4AAB  48 8B 00                        mov rax, qword ptr [rax]
004A4AAE  83 38 FF                        cmp dword ptr [rax], -1
004A4AB1  0F 84 1C 01 00 00               je 0x1404a4bd3
004A4AB7  B8 1E 0D 00 00                  mov eax, 0xd1e
004A4ABC  48 8D 50 10                     lea rdx, [rax + 0x10]
004A4AC0  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
004A4AC4  48 89 55 18                     mov qword ptr [rbp + 0x18], rdx
004A4AC8  4C 8B F0                        mov r14, rax
004A4ACB  48 83 FA FF                     cmp rdx, -1
004A4ACF  0F 84 A0 04 00 00               je 0x1404a4f75
004A4AD5  48 85 D2                        test rdx, rdx
004A4AD8  0F 84 A1 04 00 00               je 0x1404a4f7f
004A4ADE  44 8B 0A                        mov r9d, dword ptr [rdx]
004A4AE1  41 B8 01 00 00 00               mov r8d, 1
004A4AE7  8B 8B C8 01 00 00               mov ecx, dword ptr [rbx + 0x1c8]
004A4AED  41 8B D1                        mov edx, r9d
004A4AF0  8B 83 CC 01 00 00               mov eax, dword ptr [rbx + 0x1cc]
004A4AF6  41 23 C1                        and eax, r9d
004A4AF9  D3 EA                           shr edx, cl
004A4AFB  0F AF 83 D0 01 00 00            imul eax, dword ptr [rbx + 0x1d0]
004A4B02  0F BD CA                        bsr ecx, edx
004A4B05  44 89 4D 0C                     mov dword ptr [rbp + 0xc], r9d
004A4B09  44 8B 8B 28 03 00 00            mov r9d, dword ptr [rbx + 0x328]
004A4B10  41 D3 E0                        shl r8d, cl
004A4B13  4C 33 C2                        xor r8, rdx
004A4B16  C7 45 28 00 00 00 00            mov dword ptr [rbp + 0x28], 0
004A4B1D  48 8B 8C CB C0 00 00 00         mov rcx, qword ptr [rbx + rcx*8 + 0xc0]
004A4B25  4D 03 C0                        add r8, r8
004A4B28  4A 8B 34 C1                     mov rsi, qword ptr [rcx + r8*8]
004A4B2C  8B 8B 2C 03 00 00               mov ecx, dword ptr [rbx + 0x32c]
004A4B32  48 03 F0                        add rsi, rax
004A4B35  8B 83 D8 01 00 00               mov eax, dword ptr [rbx + 0x1d8]
004A4B3B  48 03 F0                        add rsi, rax
004A4B3E  48 89 75 28                     mov qword ptr [rbp + 0x28], rsi
004A4B42  8B 06                           mov eax, dword ptr [rsi]
004A4B44  44 23 C8                        and r9d, eax
004A4B47  D3 E8                           shr eax, cl
004A4B49  41 3B C4                        cmp eax, r12d
004A4B4C  0F 85 2D 04 00 00               jne 0x1404a4f7f
004A4B52  44 8B 83 38 03 00 00            mov r8d, dword ptr [rbx + 0x338]
004A4B59  BA 00 10 00 00                  mov edx, 0x1000
004A4B5E  8B 46 04                        mov eax, dword ptr [rsi + 4]
004A4B61  44 8B 5D 08                     mov r11d, dword ptr [rbp + 8]
004A4B65  25 FF 0F 00 00                  and eax, 0xfff
004A4B6A  0F 47 D0                        cmova edx, eax
004A4B6D  45 8D 68 0F                     lea r13d, [r8 + 0xf]
004A4B71  48 8B 83 68 05 00 00            mov rax, qword ptr [rbx + 0x568]
004A4B78  44 03 EA                        add r13d, edx
004A4B7B  41 C1 ED 04                     shr r13d, 4
004A4B7F  8B 48 08                        mov ecx, dword ptr [rax + 8]
004A4B82  44 8D 51 FF                     lea r10d, [rcx - 1]
004A4B86  F7 D9                           neg ecx
004A4B88  44 03 D2                        add r10d, edx
004A4B8B  44 23 D1                        and r10d, ecx
004A4B8E  45 03 D0                        add r10d, r8d
004A4B91  4C 8B 45 38                     mov r8, qword ptr [rbp + 0x38]
004A4B95  45 3B DC                        cmp r11d, r12d
004A4B98  74 4E                           je 0x1404a4be8
004A4B9A  48 8B 45 40                     mov rax, qword ptr [rbp + 0x40]
004A4B9E  0F B7 00                        movzx eax, word ptr [rax]
004A4BA1  25 FF 1F 00 00                  and eax, 0x1fff
004A4BA6  41 03 C5                        add eax, r13d
004A4BA9  3B 83 30 03 00 00               cmp eax, dword ptr [rbx + 0x330]
004A4BAF  76 37                           jbe 0x1404a4be8
004A4BB1  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
004A4BB5  33 C9                           xor ecx, ecx
004A4BB7  49 8B D0                        mov rdx, r8
004A4BBA  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
004A4BBE  8B C1                           mov eax, ecx
004A4BC0  44 89 65 08                     mov dword ptr [rbp + 8], r12d
004A4BC4  45 8B DC                        mov r11d, r12d
004A4BC7  48 89 55 30                     mov qword ptr [rbp + 0x30], rdx
004A4BCB  89 4D 00                        mov dword ptr [rbp], ecx
004A4BCE  89 4D 04                        mov dword ptr [rbp + 4], ecx
004A4BD1  EB 1C                           jmp 0x1404a4bef
004A4BD3  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
004A4BD7  48 85 C0                        test rax, rax
004A4BDA  0F 85 DC FE FF FF               jne 0x1404a4abc
004A4BE0  48 8B D6                        mov rdx, rsi
004A4BE3  E9 E3 FE FF FF                  jmp 0x1404a4acb
004A4BE8  48 8B 55 30                     mov rdx, qword ptr [rbp + 0x30]
004A4BEC  8B 45 00                        mov eax, dword ptr [rbp]
004A4BEF  44 3B C8                        cmp r9d, eax
004A4BF2  75 09                           jne 0x1404a4bfd
004A4BF4  45 3B E3                        cmp r12d, r11d
004A4BF7  0F 84 1F 02 00 00               je 0x1404a4e1c
004A4BFD  48 85 D2                        test rdx, rdx
004A4C00  0F 84 65 03 00 00               je 0x1404a4f6b
004A4C06  C1 E0 04                        shl eax, 4
004A4C09  41 C1 E1 04                     shl r9d, 4
004A4C0D  8B C8                           mov ecx, eax
004A4C0F  48 03 CA                        add rcx, rdx
004A4C12  41 8B D1                        mov edx, r9d
004A4C15  49 03 D0                        add rdx, r8
004A4C18  45 8B C2                        mov r8d, r10d
004A4C1B  45 3B E3                        cmp r12d, r11d
004A4C1E  75 07                           jne 0x1404a4c27
004A4C20  E8 1B 1C 22 00                  call 0x1406c6840
004A4C25  EB 05                           jmp 0x1404a4c2c
004A4C27  E8 14 1C 22 00                  call 0x1406c6840
004A4C2C  48 8B D6                        mov rdx, rsi
004A4C2F  48 8B CB                        mov rcx, rbx
004A4C32  E8 F9 3E DC FF                  call 0x140268b30
004A4C37  44 8B 65 08                     mov r12d, dword ptr [rbp + 8]
004A4C3B  8B 8B 2C 03 00 00               mov ecx, dword ptr [rbx + 0x32c]
004A4C41  8B 43 70                        mov eax, dword ptr [rbx + 0x70]
004A4C44  41 D3 E4                        shl r12d, cl
004A4C47  44 0B 65 00                     or r12d, dword ptr [rbp]
004A4C4B  83 F8 FF                        cmp eax, -1
004A4C4E  74 11                           je 0x1404a4c61
004A4C50  85 C0                           test eax, eax
004A4C52  74 0D                           je 0x1404a4c61
004A4C54  8D 70 FF                        lea esi, [rax - 1]
004A4C57  48 C1 E6 04                     shl rsi, 4
004A4C5B  48 03 73 58                     add rsi, qword ptr [rbx + 0x58]
004A4C5F  EB 04                           jmp 0x1404a4c65
004A4C61  48 8D 73 60                     lea rsi, [rbx + 0x60]
004A4C65  4C 39 36                        cmp qword ptr [rsi], r14
004A4C68  75 0A                           jne 0x1404a4c74
004A4C6A  48 8B 45 18                     mov rax, qword ptr [rbp + 0x18]
004A4C6E  48 89 46 08                     mov qword ptr [rsi + 8], rax
004A4C72  EB 50                           jmp 0x1404a4cc4
004A4C74  48 8D 53 58                     lea rdx, [rbx + 0x58]
004A4C78  49 8B CF                        mov rcx, r15
004A4C7B  E8 E0 85 F0 FF                  call 0x1403ad260
004A4C80  83 7B 70 FF                     cmp dword ptr [rbx + 0x70], -1
004A4C84  75 09                           jne 0x1404a4c8f
004A4C86  0F 10 45 10                     movups xmm0, xmmword ptr [rbp + 0x10]
004A4C8A  0F 11 06                        movups xmmword ptr [rsi], xmm0
004A4C8D  EB 35                           jmp 0x1404a4cc4
004A4C8F  41 8B 56 10                     mov edx, dword ptr [r14 + 0x10]
004A4C93  4C 8D 43 58                     lea r8, [rbx + 0x58]
004A4C97  49 8B CF                        mov rcx, r15
004A4C9A  E8 81 80 F0 FF                  call 0x1403acd20
004A4C9F  8B 43 70                        mov eax, dword ptr [rbx + 0x70]
004A4CA2  83 F8 FF                        cmp eax, -1
004A4CA5  74 11                           je 0x1404a4cb8
004A4CA7  85 C0                           test eax, eax
004A4CA9  74 0D                           je 0x1404a4cb8
004A4CAB  8D 48 FF                        lea ecx, [rax - 1]
004A4CAE  48 C1 E1 04                     shl rcx, 4
004A4CB2  48 03 4B 58                     add rcx, qword ptr [rbx + 0x58]
004A4CB6  EB 04                           jmp 0x1404a4cbc
004A4CB8  48 8D 4B 60                     lea rcx, [rbx + 0x60]
004A4CBC  48 8B 45 18                     mov rax, qword ptr [rbp + 0x18]
004A4CC0  48 89 41 08                     mov qword ptr [rcx + 8], rax
004A4CC4  83 7D 04 00                     cmp dword ptr [rbp + 4], 0
004A4CC8  75 4D                           jne 0x1404a4d17
004A4CCA  48 8B 83 F8 02 00 00            mov rax, qword ptr [rbx + 0x2f8]
004A4CD1  48 8D 53 58                     lea rdx, [rbx + 0x58]
004A4CD5  49 8B CF                        mov rcx, r15
004A4CD8  44 89 20                        mov dword ptr [rax], r12d
004A4CDB  44 8B 83 00 03 00 00            mov r8d, dword ptr [rbx + 0x300]
004A4CE2  E8 99 50 F0 FF                  call 0x1403a9d80
004A4CE7  85 C0                           test eax, eax
004A4CE9  74 25                           je 0x1404a4d10
004A4CEB  83 F8 FF                        cmp eax, -1
004A4CEE  0F 84 81 02 00 00               je 0x1404a4f75
004A4CF4  48 8B 45 28                     mov rax, qword ptr [rbp + 0x28]
004A4CF8  48 8D 53 58                     lea rdx, [rbx + 0x58]
004A4CFC  44 8B 45 0C                     mov r8d, dword ptr [rbp + 0xc]
004A4D00  49 8B CF                        mov rcx, r15
004A4D03  44 89 20                        mov dword ptr [rax], r12d
004A4D06  E8 75 50 F0 FF                  call 0x1403a9d80
004A4D0B  E9 D6 00 00 00                  jmp 0x1404a4de6
004A4D10  C7 45 04 01 00 00 00            mov dword ptr [rbp + 4], 1
004A4D17  48 8B 8B F8 02 00 00            mov rcx, qword ptr [rbx + 0x2f8]
004A4D1E  48 8D 53 58                     lea rdx, [rbx + 0x58]
004A4D22  4C 8B 75 28                     mov r14, qword ptr [rbp + 0x28]
004A4D26  41 8B 06                        mov eax, dword ptr [r14]
004A4D29  89 01                           mov dword ptr [rcx], eax
004A4D2B  49 8B CF                        mov rcx, r15
004A4D2E  44 8B 83 00 03 00 00            mov r8d, dword ptr [rbx + 0x300]
004A4D35  E8 46 50 F0 FF                  call 0x1403a9d80
004A4D3A  49 8B D7                        mov rdx, r15
004A4D3D  48 8D 4D 10                     lea rcx, [rbp + 0x10]
004A4D41  E8 2A 0C FA FF                  call 0x140445970
004A4D46  45 89 26                        mov dword ptr [r14], r12d
004A4D49  48 8D 85 A8 00 00 00            lea rax, [rbp + 0xa8]
004A4D50  44 8B 65 0C                     mov r12d, dword ptr [rbp + 0xc]
004A4D54  4C 8D 85 80 00 00 00            lea r8, [rbp + 0x80]
004A4D5B  33 C9                           xor ecx, ecx
004A4D5D  44 89 65 0C                     mov dword ptr [rbp + 0xc], r12d
004A4D61  48 89 8D 88 00 00 00            mov qword ptr [rbp + 0x88], rcx
004A4D68  48 8D 55 0C                     lea rdx, [rbp + 0xc]
004A4D6C  48 89 8D 90 00 00 00            mov qword ptr [rbp + 0x90], rcx
004A4D73  0F 57 C0                        xorps xmm0, xmm0
004A4D76  48 89 8D A0 00 00 00            mov qword ptr [rbp + 0xa0], rcx
004A4D7D  89 8D 98 00 00 00               mov dword ptr [rbp + 0x98], ecx
004A4D83  49 8B CF                        mov rcx, r15
004A4D86  0F 11 45 10                     movups xmmword ptr [rbp + 0x10], xmm0
004A4D8A  48 89 85 80 00 00 00            mov qword ptr [rbp + 0x80], rax
004A4D91  C7 85 9C 00 00 00 08 00 00 00   mov dword ptr [rbp + 0x9c], 8
004A4D9B  E8 80 7A F0 FF                  call 0x1403ac820
004A4DA0  48 8D 95 80 00 00 00            lea rdx, [rbp + 0x80]
004A4DA7  49 8B CF                        mov rcx, r15
004A4DAA  8B F0                           mov esi, eax
004A4DAC  E8 AF 84 F0 FF                  call 0x1403ad260
004A4DB1  48 8D 53 58                     lea rdx, [rbx + 0x58]
004A4DB5  85 F6                           test esi, esi
004A4DB7  0F 88 93 00 00 00               js 0x1404a4e50
004A4DBD  4C 8B C2                        mov r8, rdx
004A4DC0  48 8D 4B 40                     lea rcx, [rbx + 0x40]
004A4DC4  8B 93 00 03 00 00               mov edx, dword ptr [rbx + 0x300]
004A4DCA  E8 D9 79 F0 FF                  call 0x1403ac7a8
004A4DCF  8B F0                           mov esi, eax
004A4DD1  85 C0                           test eax, eax
004A4DD3  79 0D                           jns 0x1404a4de2
004A4DD5  3D 06 00 00 C0                  cmp eax, 0xc0000006
004A4DDA  0F 84 88 00 00 00               je 0x1404a4e68
004A4DE0  CD 2C                           int 0x2c
004A4DE2  4C 8B 75 10                     mov r14, qword ptr [rbp + 0x10]
004A4DE6  44 8B 65 20                     mov r12d, dword ptr [rbp + 0x20]
004A4DEA  8B 75 08                        mov esi, dword ptr [rbp + 8]
004A4DED  44 3B E6                        cmp r12d, esi
004A4DF0  74 27                           je 0x1404a4e19
004A4DF2  45 8B C5                        mov r8d, r13d
004A4DF5  41 B9 01 00 00 00               mov r9d, 1
004A4DFB  41 F7 D8                        neg r8d
004A4DFE  41 8B D4                        mov edx, r12d
004A4E01  48 8B CB                        mov rcx, rbx
004A4E04  E8 D7 A1 F0 FF                  call 0x1403aefe0
004A4E09  45 33 C9                        xor r9d, r9d
004A4E0C  45 8B C5                        mov r8d, r13d
004A4E0F  8B D6                           mov edx, esi
004A4E11  48 8B CB                        mov rcx, rbx
004A4E14  E8 C7 A1 F0 FF                  call 0x1403aefe0
004A4E19  8B 45 00                        mov eax, dword ptr [rbp]
004A4E1C  41 03 C5                        add eax, r13d
004A4E1F  44 8B 6D 04                     mov r13d, dword ptr [rbp + 4]
004A4E23  83 BD B8 01 00 00 00            cmp dword ptr [rbp + 0x1b8], 0
004A4E2A  89 45 00                        mov dword ptr [rbp], eax
004A4E2D  0F 84 BD FB FF FF               je 0x1404a49f0
004A4E33  45 33 C0                        xor r8d, r8d
004A4E36  33 D2                           xor edx, edx
004A4E38  48 8B CB                        mov rcx, rbx
004A4E3B  E8 3C C6 F6 FF                  call 0x14041147c
004A4E40  83 F8 02                        cmp eax, 2
004A4E43  0F 84 A7 FB FF FF               je 0x1404a49f0
004A4E49  BE 0E 00 00 80                  mov esi, 0x8000000e
004A4E4E  EB 1C                           jmp 0x1404a4e6c
004A4E50  48 8B 83 F8 02 00 00            mov rax, qword ptr [rbx + 0x2f8]
004A4E57  45 8B C4                        mov r8d, r12d
004A4E5A  8B 08                           mov ecx, dword ptr [rax]
004A4E5C  41 89 0E                        mov dword ptr [r14], ecx
004A4E5F  48 8D 4B 40                     lea rcx, [rbx + 0x40]
004A4E63  E8 18 4F F0 FF                  call 0x1403a9d80
004A4E68  4C 8B 75 10                     mov r14, qword ptr [rbp + 0x10]
004A4E6C  4C 8D 7B 40                     lea r15, [rbx + 0x40]
004A4E70  BB 00 00 00 00                  mov ebx, 0
004A4E75  4D 85 FF                        test r15, r15
004A4E78  49 8D 47 10                     lea rax, [r15 + 0x10]
004A4E7C  48 0F 44 C3                     cmove rax, rbx
004A4E80  48 8B 00                        mov rax, qword ptr [rax]
004A4E83  83 38 FF                        cmp dword ptr [rax], -1
004A4E86  0F 84 B9 00 00 00               je 0x1404a4f45
004A4E8C  4D 85 F6                        test r14, r14
004A4E8F  0F 84 B0 00 00 00               je 0x1404a4f45
004A4E95  49 8B 07                        mov rax, qword ptr [r15]
004A4E98  4C 3B F0                        cmp r14, rax
004A4E9B  0F 84 A4 00 00 00               je 0x1404a4f45
004A4EA1  8B FB                           mov edi, ebx
004A4EA3  48 85 C0                        test rax, rax
004A4EA6  74 04                           je 0x1404a4eac
004A4EA8  0F B6 78 02                     movzx edi, byte ptr [rax + 2]
004A4EAC  8B C7                           mov eax, edi
004A4EAE  48 C1 E0 04                     shl rax, 4
004A4EB2  48 8D 48 0F                     lea rcx, [rax + 0xf]
004A4EB6  48 3B C8                        cmp rcx, rax
004A4EB9  77 0A                           ja 0x1404a4ec5
004A4EBB  48 B9 F0 FF FF FF FF FF FF 0F   movabs rcx, 0xffffffffffffff0
004A4EC5  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
004A4EC9  48 8B C1                        mov rax, rcx
004A4ECC  E8 8F 5A 21 00                  call 0x1406ba960
004A4ED1  41 8B 56 10                     mov edx, dword ptr [r14 + 0x10]
004A4ED5  4C 8D 45 50                     lea r8, [rbp + 0x50]
004A4ED9  48 2B E1                        sub rsp, rcx
004A4EDC  48 C7 45 70 01 00 00 00         mov qword ptr [rbp + 0x70], 1
004A4EE4  0F 57 C0                        xorps xmm0, xmm0
004A4EE7  89 7D 6C                        mov dword ptr [rbp + 0x6c], edi
004A4EEA  33 C0                           xor eax, eax
004A4EEC  49 8B CF                        mov rcx, r15
004A4EEF  F3 0F 7F 45 58                  movdqu xmmword ptr [rbp + 0x58], xmm0
004A4EF4  48 8D 5C 24 20                  lea rbx, [rsp + 0x20]
004A4EF9  89 45 68                        mov dword ptr [rbp + 0x68], eax
004A4EFC  48 89 5D 50                     mov qword ptr [rbp + 0x50], rbx
004A4F00  E8 1B 7E F0 FF                  call 0x1403acd20
004A4F05  8D 57 FE                        lea edx, [rdi - 2]
004A4F08  49 8B CF                        mov rcx, r15
004A4F0B  48 03 D2                        add rdx, rdx
004A4F0E  48 8B 7C D3 08                  mov rdi, qword ptr [rbx + rdx*8 + 8]
004A4F13  48 8B 1C D3                     mov rbx, qword ptr [rbx + rdx*8]
004A4F17  48 8D 55 50                     lea rdx, [rbp + 0x50]
004A4F1B  E8 40 83 F0 FF                  call 0x1403ad260
004A4F20  48 8D 43 08                     lea rax, [rbx + 8]
004A4F24  4C 8D 43 10                     lea r8, [rbx + 0x10]
004A4F28  49 3B F8                        cmp rdi, r8
004A4F2B  48 8D 57 F8                     lea rdx, [rdi - 8]
004A4F2F  48 0F 46 D0                     cmovbe rdx, rax
004A4F33  49 8B 47 10                     mov rax, qword ptr [r15 + 0x10]
004A4F37  83 38 FF                        cmp dword ptr [rax], -1
004A4F3A  74 09                           je 0x1404a4f45
004A4F3C  49 8D 4F 10                     lea rcx, [r15 + 0x10]
004A4F40  E8 2B 4B F0 FF                  call 0x1403a9a70
004A4F45  8B C6                           mov eax, esi
004A4F47  48 8B 8D 30 01 00 00            mov rcx, qword ptr [rbp + 0x130]
004A4F4E  48 33 CD                        xor rcx, rbp
004A4F51  E8 EA 76 20 00                  call 0x1406ac640
004A4F56  48 8D A5 48 01 00 00            lea rsp, [rbp + 0x148]
004A4F5D  41 5F                           pop r15
004A4F5F  41 5E                           pop r14
004A4F61  41 5D                           pop r13
004A4F63  41 5C                           pop r12
004A4F65  5F                              pop rdi
004A4F66  5E                              pop rsi
004A4F67  5B                              pop rbx
004A4F68  5D                              pop rbp
004A4F69  C3                              ret
004A4F6A  CC                              int3
004A4F6B  BE 16 00 00 C0                  mov esi, 0xc0000016
004A4F70  E9 F7 FE FF FF                  jmp 0x1404a4e6c
004A4F75  BE 06 00 00 C0                  mov esi, 0xc0000006
004A4F7A  E9 ED FE FF FF                  jmp 0x1404a4e6c
004A4F7F  33 F6                           xor esi, esi
004A4F81  E9 E6 FE FF FF                  jmp 0x1404a4e6c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ST_STORE_SM_TRAITS___StCompactRegions(__int64 a1, __int64 a2, int a3, __int64 a4, unsigned int a5, unsigned int a6)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m118;
    unsigned int v_stack_m11C;
    unsigned int v_stack_m120;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned int v_stack_m160;
    unsigned int v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned int v_stack_m17C;
    unsigned int v_stack_m180;
    unsigned int v_stack_m184;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned int v_stack_mEC;
    unsigned int v_stack_mF0;
    unsigned __int64 v_stack_mF8;

    v_rsp = (v_rsp) - (360);
    result = (*(unsigned __int64 *)(v_rip + 9854528)) ^ (v_stack_m188);
    v_stack_m58 = result;
    v_stack_m150 = a2;
    a2 = 0;
    v_stack_m168 = (unsigned int)((unsigned int)(a3));
    v_stack_m180 = (unsigned int)((unsigned int)(a5));
    v_stack_m158 = a4;
    result = memset(v_stack_m108, a2, 168, a4);
    a3 = 0;
    v_stack_m184 = 0;
    v_stack_m178 = v_xmm0;
    v_stack_m140 = *(unsigned __int64 *)(a1 + 1400) + (unsigned int)(a3) * 2;
    v_stack_m148 = *(unsigned __int64 *)(a1 + 1400) + (unsigned int)(a5) * 2;
    if ((*(unsigned __int64 *)(a1 + 1400) + (unsigned int)(a3) * 2) == (*(unsigned __int64 *)(a1 + 1400) + (unsigned int)(a5) * 2)) goto loc_004A4973;
    result = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 1400) + (unsigned int)(a5) * 2)) & (0x1FFFULL));
    v_stack_m188 = (unsigned int)(result);
    goto loc_004A4977;
loc_004A4973:
    v_stack_m188 = 0;
loc_004A4977:
    result = ST_STORE_SM_TRAITS___StDmPageRecordUnprotect(a1, *(unsigned __int64 *)(a1 + 760), a3, a4);
    result = (unsigned int)(*(unsigned int *)(a1 + 120));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 120)))) & (1)) != 0) {
        a1 = a1 + 64;
        a2 = a1 + 88;
        result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_R(a1, a2, a3, a4);
    }
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) << ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 812)))));
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 760)) = (unsigned int)(a2);
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_R(a1 + 64, (unsigned int)(*(unsigned int *)(a1 + 768)), a1 + 88, a4);
    if (((unsigned int)(result)) == 0xC0000006ULL) goto loc_004A4E68;
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_R(a1 + 64, v_stack_m178, a1 + 88, a4);
loc_004A49F0:
    if (0 == 0) goto loc_004A4A48;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) << ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 812)))));
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 760)) = (unsigned int)(a2);
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_R(a1 + 64, (unsigned int)(*(unsigned int *)(a1 + 768)), a1 + 88, a4);
    if (((unsigned int)(result)) == 0xC0000006ULL) goto loc_004A4E6C;
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_R(v_stack_m178, a1 + 64, a1 + 88, a4);
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_R(a1 + 64, v_stack_m178, a1 + 88, a4);
loc_004A4A48:
    if (v_stack_m178 == 0) goto loc_004A4F7F;
    a2 = (v_stack_m170) + (4);
    result = ((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_m178)))) + (4);
    v_stack_m170 = a2;
    if (a2 < (v_stack_m178 + result * 4)) goto loc_004A4ACB;
    v_rsi = 0;
    result = a1 + 64 + 16;
    if (a1 + 64 == 0) {
        result = 0;
    }
    if ((*(unsigned int *)(*(unsigned __int64 *)(result))) == -1) goto loc_004A4A9F;
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_R(a1 + 64, v_stack_m178, a1 + 88, a4);
    if (result != -1) goto loc_004A4BD7;
    goto loc_004A4ACB;
loc_004A4A9F:
    result = a1 + 64 + 16;
    if (a1 + 64 == 0) {
        result = 0;
    }
    if ((*(unsigned int *)(*(unsigned __int64 *)(result))) == -1) goto loc_004A4BD3;
loc_004A4ABC:
    v_stack_m178 = (unsigned int)(0xD1EULL);
    v_stack_m170 = (unsigned int)(0xD1EULL) + 16;
loc_004A4ACB:
    if (((unsigned int)(0xD1EULL) + 16) == -1) goto loc_004A4F75;
    if ((unsigned int)(0xD1EULL) + 16 == 0) goto loc_004A4F7F;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 460))) & ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(0xD1EULL) + 16)))));
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(0xD1EULL) + 16))))) >> ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 456)))));
    result = (unsigned int)((result) * (*(unsigned int *)(a1 + 464)));
    v_stack_m17C = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(0xD1EULL) + 16)));
    a3 = (unsigned int)((1) << ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 456)))));
    a3 = (a3) ^ (a2);
    v_stack_m160 = 0;
    a3 = (a3) + (a3);
    v_rsi = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + (unsigned int)(*(unsigned int *)(a1 + 456)) * 8 + 192) + a3 * 8)) + (result);
    v_rsi = (v_rsi) + ((unsigned int)(*(unsigned int *)(a1 + 472)));
    v_stack_m160 = v_rsi;
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 808))) & ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi))) >> ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 812)))));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(a3)))) goto loc_004A4F7F;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 4))) & (0xFFFULL));
    a2 = (unsigned int)(0x1000ULL);
    if (condition_is_above) { a2 = (unsigned int)(result); }
    v_r13 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 824)) + 15) + ((unsigned int)(a2)));
    v_r13 = (unsigned int)((v_r13) >> (4));
    a1 = (unsigned int)(-((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 1384) + 8))));
    v_r10 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 1384) + 8)) - 1) + ((unsigned int)(a2)));
    v_r10 = (unsigned int)((v_r10) & ((unsigned int)(a1)));
    v_r10 = (unsigned int)((v_r10) + ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 824)))));
    if (((unsigned int)((unsigned int)(v_stack_m180))) == ((unsigned int)((unsigned int)(a3)))) goto loc_004A4BE8;
    result = (unsigned int)((*(unsigned __int16 *)(v_stack_m148)) & (0x1FFFULL));
    result = (unsigned int)((result) + ((unsigned int)(v_r13)));
    if (((unsigned int)(result)) <= (*(unsigned int *)(a1 + 816))) goto loc_004A4BE8;
    a1 = 0;
    v_stack_m148 = v_stack_m140;
    v_stack_m180 = (unsigned int)((unsigned int)(a3));
    v_stack_m158 = v_stack_m150;
    v_stack_m188 = 0;
    v_stack_m184 = 0;
    goto loc_004A4BEF;
loc_004A4BD3:
loc_004A4BD7:
    if (*(unsigned __int64 *)((unsigned int)(0xD1EULL) + 8) != 0) goto loc_004A4ABC;
    goto loc_004A4ACB;
loc_004A4BE8:
loc_004A4BEF:
    if (((unsigned int)(a4)) != ((unsigned int)((unsigned int)(v_stack_m188)))) goto loc_004A4BFD;
    if (((unsigned int)((unsigned int)(a3))) == ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a3)))))) goto loc_004A4E1C;
loc_004A4BFD:
    if (v_stack_m158 == 0) goto loc_004A4F6B;
    result = (unsigned int)(((unsigned int)(v_stack_m188)) << (4));
    a4 = (unsigned int)((a4) << (4));
    a1 = ((unsigned int)((unsigned int)(result))) + (v_stack_m158);
    a2 = ((unsigned int)((unsigned int)(a4))) + (v_stack_m150);
    if (((unsigned int)((unsigned int)(a3))) != ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a3)))))) goto loc_004A4C27;
    result = memcpy(a1, a2, (unsigned int)((unsigned int)(v_r10)), a4);
    goto loc_004A4C2C;
loc_004A4C27:
    result = memcpy(a1, a2, (unsigned int)((unsigned int)(v_r10)), a4);
loc_004A4C2C:
    result = ST_STORE_SM_TRAITS___StDmPageRecordUnprotect(a1, v_rsi, (unsigned int)((unsigned int)(v_r10)), a4);
    v_r12 = (unsigned int)(((unsigned int)(v_stack_m180)) << ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 812)))));
    v_r12 = (unsigned int)((v_r12) | (v_stack_m188));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 112)))) == -1) goto loc_004A4C61;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 112))) == 0) goto loc_004A4C61;
    v_rsi = ((unsigned int)(*(unsigned int *)(a1 + 112)) - 1) << (4);
    v_rsi = (v_rsi) + (*(unsigned __int64 *)(a1 + 88));
    goto loc_004A4C65;
loc_004A4C61:
loc_004A4C65:
    if ((*(unsigned __int64 *)(a1 + 96)) != ((unsigned int)(0xD1EULL))) goto loc_004A4C74;
    *(unsigned __int64 *)(a1 + 96 + 8) = v_stack_m170;
    goto loc_004A4CC4;
loc_004A4C74:
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_R(a1 + 64, a1 + 88, (unsigned int)((unsigned int)(v_r10)), a4);
    if ((*(unsigned int *)(a1 + 112)) != -1) goto loc_004A4C8F;
    *(unsigned __int64 *)(a1 + 96) = v_xmm0;
    goto loc_004A4CC4;
loc_004A4C8F:
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_R(a1 + 64, (unsigned int)(*(unsigned int *)((unsigned int)(0xD1EULL) + 16)), a1 + 88, a4);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 112)))) == -1) goto loc_004A4CB8;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 112))) == 0) goto loc_004A4CB8;
    a1 = ((unsigned int)(*(unsigned int *)(a1 + 112)) - 1) << (4);
    a1 = (a1) + (*(unsigned __int64 *)(a1 + 88));
    goto loc_004A4CBC;
loc_004A4CB8:
loc_004A4CBC:
    *(unsigned __int64 *)(a1 + 96 + 8) = v_stack_m170;
loc_004A4CC4:
    if (v_stack_m184 != 0) goto loc_004A4D17;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 760)) = (unsigned int)(v_r12);
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_R(a1 + 64, a1 + 88, (unsigned int)(*(unsigned int *)(a1 + 768)), a4);
    if ((unsigned int)(result) == 0) goto loc_004A4D10;
    if (((unsigned int)(result)) == -1) goto loc_004A4F75;
    *(unsigned int *)(v_stack_m160) = (unsigned int)(v_r12);
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_R(a1 + 64, a1 + 88, (unsigned int)(v_stack_m17C), a4);
    goto loc_004A4DE6;
loc_004A4D10:
    v_stack_m184 = 1;
loc_004A4D17:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 760)) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m160)));
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_R(a1 + 64, a1 + 88, (unsigned int)(*(unsigned int *)(a1 + 768)), a4);
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_R(v_stack_m178, a1 + 64, (unsigned int)(*(unsigned int *)(a1 + 768)), a4);
    *(unsigned int *)(v_stack_m160) = (unsigned int)(v_r12);
    a1 = 0;
    v_stack_m17C = (unsigned int)((unsigned int)(v_stack_m17C));
    v_stack_m100 = 0;
    v_stack_mF8 = 0;
    v_stack_mE8 = 0;
    v_stack_mF0 = 0;
    v_stack_m178 = v_xmm0;
    v_stack_m108 = v_stack_mE0;
    v_stack_mEC = 8;
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_R(a1 + 64, v_stack_m17C, v_stack_m108, a4);
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_R(a1 + 64, v_stack_m108, v_stack_m108, a4);
    if (sign_flag) goto loc_004A4E50;
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_R(a1 + 64, (unsigned int)(*(unsigned int *)(a1 + 768)), a1 + 88, a4);
    if (!sign_flag) goto loc_004A4DE2;
    if (((unsigned int)(result)) == 0xC0000006ULL) goto loc_004A4E68;
loc_004A4DE2:
loc_004A4DE6:
    if (((unsigned int)((unsigned int)(v_stack_m168))) != ((unsigned int)((unsigned int)(v_stack_m180)))) {
        a3 = (unsigned int)(v_r13);
        a4 = 1;
        a3 = (unsigned int)(-(a3));
        a2 = (unsigned int)((unsigned int)(v_stack_m168));
        a1 = 0;
        result = ST_STORE_SM_TRAITS___StDmpUpdateRegionState(a1, a2, a3, a4);
        a4 = 0;
        a3 = (unsigned int)(v_r13);
        a2 = (unsigned int)((unsigned int)(v_stack_m180));
        a1 = a1;
        result = ST_STORE_SM_TRAITS___StDmpUpdateRegionState(a1, a2, a3, a4);
    }
loc_004A4E1C:
    result = (unsigned int)(((unsigned int)(v_stack_m188)) + ((unsigned int)(v_r13)));
    v_stack_m188 = (unsigned int)(result);
    if (a6 == 0) goto loc_004A49F0;
    a3 = 0;
    a2 = 0;
    result = ST_STORE_SM_TRAITS___StDmCheckForCompaction(a1, a2, a3, a4);
    if (((unsigned int)(result)) == 2) goto loc_004A49F0;
    goto loc_004A4E6C;
loc_004A4E50:
    *(unsigned int *)(v_stack_m178) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 760))));
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_R(a1 + 64, a2, (unsigned int)((unsigned int)((unsigned int)(v_stack_m168))), a4);
loc_004A4E68:
loc_004A4E6C:
    result = a1 + 64 + 16;
    if (a1 + 64 == 0) { result = 0; }
    if ((*(unsigned int *)(*(unsigned __int64 *)(result))) == -1) goto loc_004A4F45;
    if (v_stack_m178 == 0) goto loc_004A4F45;
    if (v_stack_m178 == (*(unsigned __int64 *)(a1 + 64))) goto loc_004A4F45;
    v_rdi = 0;
    if (*(unsigned __int64 *)(a1 + 64) != 0) {
        v_rdi = *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 64) + 2);
    }
    result = ((unsigned int)((unsigned int)(v_rdi))) << (4);
    if ((result + 15) <= result) {
    }
    a1 = (result + 15) & (-16);
    result = _chkstk(a1, a2, (unsigned int)((unsigned int)((unsigned int)(v_stack_m168))), a4);
    v_rsp = (v_rsp) - (a1);
    v_stack_m118 = 1;
    v_stack_m11C = (unsigned int)(v_rdi);
    result = 0;
    v_stack_m130 = v_xmm0;
    v_stack_m120 = 0;
    v_stack_m138 = v_stack_m188;
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_R(a1 + 64, (unsigned int)(*(unsigned int *)(v_stack_m178 + 16)), v_stack_m138, a4);
    a2 = (v_rdi - 2) + (v_rdi - 2);
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_R(a1 + 64, v_stack_m138, v_stack_m138, a4);
    a2 = *(unsigned __int64 *)(v_stack_m188 + a2 * 8 + 8) - 8;
    if ((*(unsigned __int64 *)(v_stack_m188 + a2 * 8 + 8)) <= (*(unsigned __int64 *)(v_stack_m188 + a2 * 8) + 16)) { a2 = *(unsigned __int64 *)(v_stack_m188 + a2 * 8) + 8; }
    result = *(unsigned __int64 *)(a1 + 64 + 16);
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 64 + 16))) != -1) {
        a1 = a1 + 64 + 16;
        result = NP_CONTEXT__NpLeafDerefInternal(a1, a2, *(unsigned __int64 *)(v_stack_m188 + a2 * 8) + 16, a4);
    }
    a1 = (v_stack_m58) ^ (v_stack_m188);
    result = _security_check_cookie(a1, a2, *(unsigned __int64 *)(v_stack_m188 + a2 * 8) + 16, a4);
    return result;
loc_004A4F6B:
    goto loc_004A4E6C;
loc_004A4F75:
    goto loc_004A4E6C;
loc_004A4F7F:
    v_rsi = 0;
    goto loc_004A4E6C;
}
```

## 5. (Beta) C Style

```c
int64_t ST_STORE_SM_TRAITS___StCompactRegions(void *Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, uint32_t Arg5, uint32_t Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m118;
    uint32_t v_stack_m11C;
    uint32_t v_stack_m120;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint32_t v_stack_m160;
    uint32_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint32_t v_stack_m17C;
    uint32_t v_stack_m180;
    uint32_t v_stack_m184;
    uint64_t v_stack_m188;
    uint64_t v_stack_m40;
    uint64_t v_stack_m58;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint32_t v_stack_mEC;
    uint32_t v_stack_mF0;
    uint64_t v_stack_mF8;

    local_rsp = (local_rsp) - (360);
    result = (*(uint64_t *)(v_rip + 0x965E40)) ^ (v_stack_m188);
    v_stack_m58 = result;
    v_stack_m150 = Arg2;
    Arg2 = 0;
    v_stack_m168 = (uint32_t)((uint32_t)(Arg3));
    v_stack_m180 = (uint32_t)((uint32_t)(Arg5));
    v_stack_m158 = Arg4;
    result = memset(v_stack_m108, Arg2, 168, Arg4);
    Arg3 = 0;
    v_stack_m184 = 0;
    v_stack_m178 = v_xmm0;
    v_stack_m140 = *(uint64_t *)(arg1 + 0x578) + (uint32_t)(Arg3) * 2;
    v_stack_m148 = *(uint64_t *)(arg1 + 0x578) + (uint32_t)(Arg5) * 2;
    if ((*(uint64_t *)(arg1 + 0x578) + (uint32_t)(Arg3) * 2) == (*(uint64_t *)(arg1 + 0x578) + (uint32_t)(Arg5) * 2)) goto loc_004A4973;
    result = (uint32_t)((*(uint16_t *)(*(uint64_t *)(arg1 + 0x578) + (uint32_t)(Arg5) * 2)) & (0x1FFFULL));
    v_stack_m188 = (uint32_t)(result);
    goto loc_004A4977;
loc_004A4973:
    v_stack_m188 = 0;
loc_004A4977:
    result = ST_STORE_SM_TRAITS___StDmPageRecordUnprotect(Arg1, *(uint64_t *)(arg1 + 0x2F8), Arg3, Arg4);
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x78));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x78)))) & (1)) != 0) {
        Arg1 = Arg1 + 64;
        Arg2 = Arg1 + 88;
        result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_R(Arg1, Arg2, Arg3, Arg4);
    }
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) << ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x32C)))));
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x2F8)) = (uint32_t)(Arg2);
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_R(Arg1 + 64, (uint32_t)(*(uint32_t *)(arg1 + 0x300)), Arg1 + 88, Arg4);
    if (((uint32_t)(result)) == 0xC0000006ULL) goto loc_004A4E68;
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_R(Arg1 + 64, v_stack_m178, Arg1 + 88, Arg4);
loc_004A49F0:
    if (0 == 0) goto loc_004A4A48;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) << ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x32C)))));
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x2F8)) = (uint32_t)(Arg2);
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_R(Arg1 + 64, (uint32_t)(*(uint32_t *)(arg1 + 0x300)), Arg1 + 88, Arg4);
    if (((uint32_t)(result)) == 0xC0000006ULL) goto loc_004A4E6C;
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_R(v_stack_m178, Arg1 + 64, Arg1 + 88, Arg4);
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_R(Arg1 + 64, v_stack_m178, Arg1 + 88, Arg4);
loc_004A4A48:
    if (v_stack_m178 == 0) goto loc_004A4F7F;
    Arg2 = (v_stack_m170) + (4);
    result = ((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_m178)))) + (4);
    v_stack_m170 = Arg2;
    if (Arg2 < (v_stack_m178 + result * 4)) goto loc_004A4ACB;
    local_rsi = 0;
    result = Arg1 + 64 + 16;
    if (Arg1 + 64 == 0) {
        result = 0;
    }
    if ((*(uint32_t *)(*(uint64_t *)(result))) == -1) goto loc_004A4A9F;
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_R(Arg1 + 64, v_stack_m178, Arg1 + 88, Arg4);
    if (result != -1) goto loc_004A4BD7;
    goto loc_004A4ACB;
loc_004A4A9F:
    result = Arg1 + 64 + 16;
    if (Arg1 + 64 == 0) {
        result = 0;
    }
    if ((*(uint32_t *)(*(uint64_t *)(result))) == -1) goto loc_004A4BD3;
loc_004A4ABC:
    v_stack_m178 = (uint32_t)(0xD1EULL);
    v_stack_m170 = (uint32_t)(0xD1EULL) + 16;
loc_004A4ACB:
    if (((uint32_t)(0xD1EULL) + 16) == -1) goto loc_004A4F75;
    if ((uint32_t)(0xD1EULL) + 16 == 0) goto loc_004A4F7F;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x1CC))) & ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(0xD1EULL) + 0x10)))));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(0xD1EULL) + 0x10))))) >> ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1C8)))));
    result = (uint32_t)((result) * (*(uint32_t *)(arg1 + 0x1D0)));
    v_stack_m17C = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(0xD1EULL) + 0x10)));
    Arg3 = (uint32_t)((1) << ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1C8)))));
    Arg3 = (Arg3) ^ (Arg2);
    v_stack_m160 = 0;
    Arg3 = (Arg3) + (Arg3);
    local_rsi = (*(uint64_t *)(*(uint64_t *)(arg1 + (uint32_t)(*(uint32_t *)(arg1 + 0x1C8)) * 8 + 0xC0) + Arg3 * 8)) + (result);
    local_rsi = (local_rsi) + ((uint32_t)(*(uint32_t *)(arg1 + 0x1D8)));
    v_stack_m160 = local_rsi;
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x328))) & ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi))) >> ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x32C)))));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(Arg3)))) goto loc_004A4F7F;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x4))) & (0xFFFULL));
    Arg2 = (uint32_t)(0x1000ULL);
    if (condition_is_above) { Arg2 = (uint32_t)(result); }
    local_r13 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x338)) + 15) + ((uint32_t)(Arg2)));
    local_r13 = (uint32_t)((local_r13) >> (4));
    Arg1 = (uint32_t)(-((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x568) + 0x8))));
    local_r10 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x568) + 0x8)) - 1) + ((uint32_t)(Arg2)));
    local_r10 = (uint32_t)((local_r10) & ((uint32_t)(Arg1)));
    local_r10 = (uint32_t)((local_r10) + ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x338)))));
    if (((uint32_t)((uint32_t)(v_stack_m180))) == ((uint32_t)((uint32_t)(Arg3)))) goto loc_004A4BE8;
    result = (uint32_t)((*(uint16_t *)(v_stack_m148)) & (0x1FFFULL));
    result = (uint32_t)((result) + ((uint32_t)(local_r13)));
    if (((uint32_t)(result)) <= (*(uint32_t *)(arg1 + 0x330))) goto loc_004A4BE8;
    Arg1 = 0;
    v_stack_m148 = v_stack_m140;
    v_stack_m180 = (uint32_t)((uint32_t)(Arg3));
    v_stack_m158 = v_stack_m150;
    v_stack_m188 = 0;
    v_stack_m184 = 0;
    goto loc_004A4BEF;
loc_004A4BD3:
loc_004A4BD7:
    if (*(uint64_t *)((uint32_t)(0xD1EULL) + 0x8) != 0) goto loc_004A4ABC;
    goto loc_004A4ACB;
loc_004A4BE8:
loc_004A4BEF:
    if (((uint32_t)(Arg4)) != ((uint32_t)((uint32_t)(v_stack_m188)))) goto loc_004A4BFD;
    if (((uint32_t)((uint32_t)(Arg3))) == ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg3)))))) goto loc_004A4E1C;
loc_004A4BFD:
    if (v_stack_m158 == 0) goto loc_004A4F6B;
    result = (uint32_t)(((uint32_t)(v_stack_m188)) << (4));
    Arg4 = (uint32_t)((Arg4) << (4));
    Arg1 = ((uint32_t)((uint32_t)(result))) + (v_stack_m158);
    Arg2 = ((uint32_t)((uint32_t)(Arg4))) + (v_stack_m150);
    if (((uint32_t)((uint32_t)(Arg3))) != ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg3)))))) goto loc_004A4C27;
    result = memcpy(Arg1, Arg2, (uint32_t)((uint32_t)(local_r10)), Arg4);
    goto loc_004A4C2C;
loc_004A4C27:
    result = memcpy(Arg1, Arg2, (uint32_t)((uint32_t)(local_r10)), Arg4);
loc_004A4C2C:
    result = ST_STORE_SM_TRAITS___StDmPageRecordUnprotect(Arg1, local_rsi, (uint32_t)((uint32_t)(local_r10)), Arg4);
    local_r12 = (uint32_t)(((uint32_t)(v_stack_m180)) << ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x32C)))));
    local_r12 = (uint32_t)((local_r12) | (v_stack_m188));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x70)))) == -1) goto loc_004A4C61;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x70))) == 0) goto loc_004A4C61;
    local_rsi = ((uint32_t)(*(uint32_t *)(arg1 + 0x70)) - 1) << (4);
    local_rsi = (local_rsi) + (*(uint64_t *)(arg1 + 0x58));
    goto loc_004A4C65;
loc_004A4C61:
loc_004A4C65:
    if ((*(uint64_t *)(arg1 + 0x60)) != ((uint32_t)(0xD1EULL))) goto loc_004A4C74;
    *(uint64_t *)(arg1 + 0x60 + 0x8) = v_stack_m170;
    goto loc_004A4CC4;
loc_004A4C74:
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_R(Arg1 + 64, Arg1 + 88, (uint32_t)((uint32_t)(local_r10)), Arg4);
    if ((*(uint32_t *)(arg1 + 0x70)) != -1) goto loc_004A4C8F;
    *(uint64_t *)(arg1 + 0x60) = v_xmm0;
    goto loc_004A4CC4;
loc_004A4C8F:
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_R(Arg1 + 64, (uint32_t)(*(uint32_t *)((uint32_t)(0xD1EULL) + 0x10)), Arg1 + 88, Arg4);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x70)))) == -1) goto loc_004A4CB8;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x70))) == 0) goto loc_004A4CB8;
    Arg1 = ((uint32_t)(*(uint32_t *)(arg1 + 0x70)) - 1) << (4);
    Arg1 = (Arg1) + (*(uint64_t *)(arg1 + 0x58));
    goto loc_004A4CBC;
loc_004A4CB8:
loc_004A4CBC:
    *(uint64_t *)(arg1 + 0x60 + 0x8) = v_stack_m170;
loc_004A4CC4:
    if (v_stack_m184 != 0) goto loc_004A4D17;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x2F8)) = (uint32_t)(local_r12);
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_R(Arg1 + 64, Arg1 + 88, (uint32_t)(*(uint32_t *)(arg1 + 0x300)), Arg4);
    if ((uint32_t)(result) == 0) goto loc_004A4D10;
    if (((uint32_t)(result)) == -1) goto loc_004A4F75;
    *(uint32_t *)(v_stack_m160) = (uint32_t)(local_r12);
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_R(Arg1 + 64, Arg1 + 88, (uint32_t)(v_stack_m17C), Arg4);
    goto loc_004A4DE6;
loc_004A4D10:
    v_stack_m184 = 1;
loc_004A4D17:
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x2F8)) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m160)));
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_R(Arg1 + 64, Arg1 + 88, (uint32_t)(*(uint32_t *)(arg1 + 0x300)), Arg4);
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_R(v_stack_m178, Arg1 + 64, (uint32_t)(*(uint32_t *)(arg1 + 0x300)), Arg4);
    *(uint32_t *)(v_stack_m160) = (uint32_t)(local_r12);
    Arg1 = 0;
    v_stack_m17C = (uint32_t)((uint32_t)(v_stack_m17C));
    v_stack_m100 = 0;
    v_stack_mF8 = 0;
    v_stack_mE8 = 0;
    v_stack_mF0 = 0;
    v_stack_m178 = v_xmm0;
    v_stack_m108 = v_stack_mE0;
    v_stack_mEC = 8;
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_R(Arg1 + 64, v_stack_m17C, v_stack_m108, Arg4);
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_R(Arg1 + 64, v_stack_m108, v_stack_m108, Arg4);
    if (sign_flag) goto loc_004A4E50;
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_R(Arg1 + 64, (uint32_t)(*(uint32_t *)(arg1 + 0x300)), Arg1 + 88, Arg4);
    if (!sign_flag) goto loc_004A4DE2;
    if (((uint32_t)(result)) == 0xC0000006ULL) goto loc_004A4E68;
loc_004A4DE2:
loc_004A4DE6:
    if (((uint32_t)((uint32_t)(v_stack_m168))) != ((uint32_t)((uint32_t)(v_stack_m180)))) {
        Arg3 = (uint32_t)(local_r13);
        Arg4 = 1;
        Arg3 = (uint32_t)(-(Arg3));
        Arg2 = (uint32_t)((uint32_t)(v_stack_m168));
        Arg1 = 0;
        result = ST_STORE_SM_TRAITS___StDmpUpdateRegionState(Arg1, Arg2, Arg3, Arg4);
        Arg4 = 0;
        Arg3 = (uint32_t)(local_r13);
        Arg2 = (uint32_t)((uint32_t)(v_stack_m180));
        Arg1 = Arg1;
        result = ST_STORE_SM_TRAITS___StDmpUpdateRegionState(Arg1, Arg2, Arg3, Arg4);
    }
loc_004A4E1C:
    result = (uint32_t)(((uint32_t)(v_stack_m188)) + ((uint32_t)(local_r13)));
    v_stack_m188 = (uint32_t)(result);
    if (Arg6 == 0) goto loc_004A49F0;
    Arg3 = 0;
    Arg2 = 0;
    result = ST_STORE_SM_TRAITS___StDmCheckForCompaction(Arg1, Arg2, Arg3, Arg4);
    if (((uint32_t)(result)) == 2) goto loc_004A49F0;
    goto loc_004A4E6C;
loc_004A4E50:
    *(uint32_t *)(v_stack_m178) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x2F8))));
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_R(Arg1 + 64, Arg2, (uint32_t)((uint32_t)((uint32_t)(v_stack_m168))), Arg4);
loc_004A4E68:
loc_004A4E6C:
    result = Arg1 + 64 + 16;
    if (Arg1 + 64 == 0) { result = 0; }
    if ((*(uint32_t *)(*(uint64_t *)(result))) == -1) goto loc_004A4F45;
    if (v_stack_m178 == 0) goto loc_004A4F45;
    if (v_stack_m178 == (*(uint64_t *)(arg1 + 0x40))) goto loc_004A4F45;
    local_rdi = 0;
    if (*(uint64_t *)(arg1 + 0x40) != 0) {
        local_rdi = *(uint8_t *)(*(uint64_t *)(arg1 + 0x40) + 0x2);
    }
    result = ((uint32_t)((uint32_t)(local_rdi))) << (4);
    if ((result + 15) <= result) {
    }
    Arg1 = (result + 15) & (-16);
    result = _chkstk(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(v_stack_m168))), Arg4);
    local_rsp = (local_rsp) - (Arg1);
    v_stack_m118 = 1;
    v_stack_m11C = (uint32_t)(local_rdi);
    result = 0;
    v_stack_m130 = v_xmm0;
    v_stack_m120 = 0;
    v_stack_m138 = v_stack_m188;
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_R(Arg1 + 64, (uint32_t)(*(uint32_t *)(v_stack_m178 + 0x10)), v_stack_m138, Arg4);
    Arg2 = (local_rdi - 2) + (local_rdi - 2);
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_R(Arg1 + 64, v_stack_m138, v_stack_m138, Arg4);
    Arg2 = *(uint64_t *)(v_stack_m188 + Arg2 * 8 + 0x8) - 8;
    if ((*(uint64_t *)(v_stack_m188 + Arg2 * 8 + 0x8)) <= (*(uint64_t *)(v_stack_m188 + Arg2 * 8) + 16)) { Arg2 = *(uint64_t *)(v_stack_m188 + Arg2 * 8) + 8; }
    result = *(uint64_t *)(arg1 + 0x40 + 0x10);
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x40 + 0x10))) != -1) {
        Arg1 = Arg1 + 64 + 16;
        result = NP_CONTEXT__NpLeafDerefInternal(Arg1, Arg2, *(uint64_t *)(v_stack_m188 + Arg2 * 8) + 16, Arg4);
    }
    Arg1 = (v_stack_m58) ^ (v_stack_m188);
    result = _security_check_cookie(Arg1, Arg2, *(uint64_t *)(v_stack_m188 + Arg2 * 8) + 16, Arg4);
    return result;
loc_004A4F6B:
    goto loc_004A4E6C;
loc_004A4F75:
    goto loc_004A4E6C;
loc_004A4F7F:
    local_rsi = 0;
    goto loc_004A4E6C;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x58` | `64` | `R` |
| `Arg1` | `+ 0x60` | `64` | `R` |
| `Arg1` | `+ 0x70` | `32` | `R` |
| `Arg1` | `+ 0x78` | `32` | `R` |
| `Arg1` | `+ 0x78` | `32` | `R/W` |
| `Arg1` | `+ 0xC0 + rcx*8` | `64` | `R` |
| `Arg1` | `+ 0x1C8` | `32` | `R` |
| `Arg1` | `+ 0x1CC` | `32` | `R` |
| `Arg1` | `+ 0x1D0` | `32` | `R` |
| `Arg1` | `+ 0x1D8` | `32` | `R` |
| `Arg1` | `+ 0x2F8` | `64` | `R` |
| `Arg1` | `+ 0x300` | `32` | `R` |
| `Arg1` | `+ 0x328` | `32` | `R` |
| `Arg1` | `+ 0x32C` | `32` | `R` |
| `Arg1` | `+ 0x330` | `32` | `R` |
| `Arg1` | `+ 0x338` | `32` | `R` |
| `Arg1` | `+ 0x568` | `64` | `R` |
| `Arg1` | `+ 0x578` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004A48E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
