# B_TREE&lt;unsigned long,ST_STORE&lt;SM_TRAITS&gt;::_ST_HASH_ENTRY,4096,NP_CONTEXT,ST_STORE&lt;SM_TRAITS&gt;::ST_HASH_ENTRY_COMPARATOR&gt;::BTreeSearchKey

- RVA: `0x003ADDB0`–`0x003AE306` (길이 `1,366` bytes)
- VA: `0x00000001403ADDB0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008BEB0`
- 디코드: `349`개 명령, `1,366/1,366` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **6**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003ADDD9` → [B_TREE<unsigned long,ST_STORE<SM_TRAITS>::_ST_HASH_ENTRY,4096,NP_CONTEXT,ST_STORE<SM_TRAITS>::ST_HASH_ENTRY_COMPARATOR>::BTreeSearchResultDeref](B_TREE_unsigned_long_ST_STORE_SM_TRAITS__ST_HASH_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS_ST_HASH_EN_function_003AE310.md) (function, `0x003AE310`)
- `0x003AE12E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x003AE151` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x003AE164` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x003AE16F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x003AE2C9` → [NP_CONTEXT::NpLeafRefInternal](NP_CONTEXT_NpLeafRefInternal_function_003AA340.md) (function, `0x003AA340`)

### Direct callers
- [B_TREE&lt;unsigned long,ST_STORE&lt;SM_TRAITS&gt;::_ST_HASH_ENTRY,4096,NP_CONTEXT,ST_STORE&lt;SM_TRAITS&gt;::ST_HASH_ENTRY_COMPARATOR&gt;::BTreeFindLeafSibling](../43/B_TREE_unsigned_long_ST_STORE_SM_TRAITS__ST_HASH_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS_ST_HASH_EN_function_0043F728.md) at `0x0043F7C0`
- [ST_STORE&lt;SM_TRAITS&gt;::StDmCombineBufferAddEntry](../4E/ST_STORE_SM_TRAITS_StDmCombineBufferAddEntry_function_004EB420.md) at `0x004EB5BB`
- [ST_STORE&lt;SM_TRAITS&gt;::StDmCombineBufferAddEntry](../4E/ST_STORE_SM_TRAITS_StDmCombineBufferAddEntry_function_004EB420.md) at `0x004EB92C`
- [sub_004EBED8](../4E/Unknown_function_004EBED8.md) at `0x004EBEF8`
- [sub_006E6E64](../6E/Unknown_function_006E6E64.md) at `0x006E6EB6`
- [sub_006EF588](../6E/Unknown_function_006EF588.md) at `0x006EF5E9`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x003AE12E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x003AE16F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003ADDB0  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
003ADDB5  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
003ADDBA  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
003ADDBF  55                              push rbp
003ADDC0  56                              push rsi
003ADDC1  57                              push rdi
003ADDC2  41 54                           push r12
003ADDC4  41 55                           push r13
003ADDC6  41 56                           push r14
003ADDC8  41 57                           push r15
003ADDCA  48 83 EC 50                     sub rsp, 0x50
003ADDCE  8B F2                           mov esi, edx
003ADDD0  4D 8B E0                        mov r12, r8
003ADDD3  49 8B D0                        mov rdx, r8
003ADDD6  4C 8B E9                        mov r13, rcx
003ADDD9  E8 32 05 00 00                  call 0x1403ae310
003ADDDE  41 BB FF FF FF FF               mov r11d, 0xffffffff
003ADDE4  41 B8 01 00 00 00               mov r8d, 1
003ADDEA  45 39 5C 24 18                  cmp dword ptr [r12 + 0x18], r11d
003ADDEF  0F 84 F0 02 00 00               je 0x1403ae0e5
003ADDF5  49 8B 45 00                     mov rax, qword ptr [r13]
003ADDF9  41 8B D0                        mov edx, r8d
003ADDFC  89 94 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], edx
003ADE03  48 85 C0                        test rax, rax
003ADE06  0F 84 D4 02 00 00               je 0x1403ae0e0
003ADE0C  0F B6 40 02                     movzx eax, byte ptr [rax + 2]
003ADE10  41 8B 4C 24 1C                  mov ecx, dword ptr [r12 + 0x1c]
003ADE15  3B C8                           cmp ecx, eax
003ADE17  0F 82 E4 02 00 00               jb 0x1403ae101
003ADE1D  4D 8B 34 24                     mov r14, qword ptr [r12]
003ADE21  49 8B 5D 00                     mov rbx, qword ptr [r13]
003ADE25  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
003ADE2A  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
003ADE2F  48 85 DB                        test rbx, rbx
003ADE32  0F 84 63 03 00 00               je 0x1403ae19b
003ADE38  8B 0B                           mov ecx, dword ptr [rbx]
003ADE3A  4C 8D 4B 10                     lea r9, [rbx + 0x10]
003ADE3E  0F B7 C1                        movzx eax, cx
003ADE41  45 8B D3                        mov r10d, r11d
003ADE44  C1 E9 18                        shr ecx, 0x18
003ADE47  4C 89 4C 24 40                  mov qword ptr [rsp + 0x40], r9
003ADE4C  84 C9                           test cl, cl
003ADE4E  0F 84 64 03 00 00               je 0x1403ae1b8
003ADE54  85 C0                           test eax, eax
003ADE56  0F 84 14 01 00 00               je 0x1403adf70
003ADE5C  45 8B BD 48 01 00 00            mov r15d, dword ptr [r13 + 0x148]
003ADE63  8B FE                           mov edi, esi
003ADE65  45 8B A5 4C 01 00 00            mov r12d, dword ptr [r13 + 0x14c]
003ADE6C  41 8B CF                        mov ecx, r15d
003ADE6F  D3 EF                           shr edi, cl
003ADE71  41 8B D4                        mov edx, r12d
003ADE74  41 8B 8D 58 01 00 00            mov ecx, dword ptr [r13 + 0x158]
003ADE7B  23 D6                           and edx, esi
003ADE7D  45 8B AD 50 01 00 00            mov r13d, dword ptr [r13 + 0x150]
003ADE84  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
003ADE89  41 8B CD                        mov ecx, r13d
003ADE8C  48 8B 5C 24 28                  mov rbx, qword ptr [rsp + 0x28]
003ADE91  0F AF CA                        imul ecx, edx
003ADE94  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
003ADE99  44 8B F1                        mov r14d, ecx
003ADE9C  EB 08                           jmp 0x1403adea6
003ADE9E  66 90                           nop
003ADEA0  41 B8 01 00 00 00               mov r8d, 1
003ADEA6  42 8D 0C 10                     lea ecx, [rax + r10]
003ADEAA  C7 44 24 28 00 00 00 00         mov dword ptr [rsp + 0x28], 0
003ADEB2  D1 E9                           shr ecx, 1
003ADEB4  8B E9                           mov ebp, ecx
003ADEB6  C7 44 24 28 00 00 00 00         mov dword ptr [rsp + 0x28], 0
003ADEBE  45 8B 1C 89                     mov r11d, dword ptr [r9 + rcx*4]
003ADEC2  41 8B CF                        mov ecx, r15d
003ADEC5  41 8B D3                        mov edx, r11d
003ADEC8  45 8B CC                        mov r9d, r12d
003ADECB  D3 EA                           shr edx, cl
003ADECD  45 23 CB                        and r9d, r11d
003ADED0  0F BD CA                        bsr ecx, edx
003ADED3  45 0F AF CD                     imul r9d, r13d
003ADED7  41 D3 E0                        shl r8d, cl
003ADEDA  44 33 C2                        xor r8d, edx
003ADEDD  48 8B 94 24 90 00 00 00         mov rdx, qword ptr [rsp + 0x90]
003ADEE5  48 8B 54 CA 40                  mov rdx, qword ptr [rdx + rcx*8 + 0x40]
003ADEEA  41 8B C8                        mov ecx, r8d
003ADEED  41 B8 01 00 00 00               mov r8d, 1
003ADEF3  48 03 C9                        add rcx, rcx
003ADEF6  48 8B 14 CA                     mov rdx, qword ptr [rdx + rcx*8]
003ADEFA  48 03 D3                        add rdx, rbx
003ADEFD  4C 03 CA                        add r9, rdx
003ADF00  48 8B 94 24 90 00 00 00         mov rdx, qword ptr [rsp + 0x90]
003ADF08  0F BD CF                        bsr ecx, edi
003ADF0B  41 D3 E0                        shl r8d, cl
003ADF0E  44 33 C7                        xor r8d, edi
003ADF11  48 8B 54 CA 40                  mov rdx, qword ptr [rdx + rcx*8 + 0x40]
003ADF16  41 8B C8                        mov ecx, r8d
003ADF19  48 03 C9                        add rcx, rcx
003ADF1C  48 8B 14 CA                     mov rdx, qword ptr [rdx + rcx*8]
003ADF20  41 8B 49 08                     mov ecx, dword ptr [r9 + 8]
003ADF24  48 03 D3                        add rdx, rbx
003ADF27  41 3B 4C 16 08                  cmp ecx, dword ptr [r14 + rdx + 8]
003ADF2C  0F 82 A0 00 00 00               jb 0x1403adfd2
003ADF32  77 09                           ja 0x1403adf3d
003ADF34  44 3B DE                        cmp r11d, esi
003ADF37  0F 82 95 00 00 00               jb 0x1403adfd2
003ADF3D  8B C5                           mov eax, ebp
003ADF3F  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
003ADF44  41 8D 4A 01                     lea ecx, [r10 + 1]
003ADF48  3B C8                           cmp ecx, eax
003ADF4A  0F 85 50 FF FF FF               jne 0x1403adea0
003ADF50  48 8B 5C 24 20                  mov rbx, qword ptr [rsp + 0x20]
003ADF55  4C 8B AC 24 90 00 00 00         mov r13, qword ptr [rsp + 0x90]
003ADF5D  4C 8B A4 24 A0 00 00 00         mov r12, qword ptr [rsp + 0xa0]
003ADF65  41 BB FF FF FF FF               mov r11d, 0xffffffff
003ADF6B  4C 8B 74 24 30                  mov r14, qword ptr [rsp + 0x30]
003ADF70  80 7B 03 00                     cmp byte ptr [rbx + 3], 0
003ADF74  75 64                           jne 0x1403adfda
003ADF76  83 BC 24 A8 00 00 00 00         cmp dword ptr [rsp + 0xa8], 0
003ADF7E  74 1C                           je 0x1403adf9c
003ADF80  8B C8                           mov ecx, eax
003ADF82  48 FF C1                        inc rcx
003ADF85  49 89 1E                        mov qword ptr [r14], rbx
003ADF88  48 C1 E1 04                     shl rcx, 4
003ADF8C  48 03 CB                        add rcx, rbx
003ADF8F  49 89 4E 08                     mov qword ptr [r14 + 8], rcx
003ADF93  49 83 C6 10                     add r14, 0x10
003ADF97  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
003ADF9C  85 C0                           test eax, eax
003ADF9E  0F 84 54 01 00 00               je 0x1403ae0f8
003ADFA4  8D 48 FF                        lea ecx, [rax - 1]
003ADFA7  48 C1 E1 04                     shl rcx, 4
003ADFAB  48 83 C1 18                     add rcx, 0x18
003ADFAF  48 03 CB                        add rcx, rbx
003ADFB2  49 8B 45 10                     mov rax, qword ptr [r13 + 0x10]
003ADFB6  44 39 18                        cmp dword ptr [rax], r11d
003ADFB9  0F 85 EC 02 00 00               jne 0x1403ae2ab
003ADFBF  48 8B 19                        mov rbx, qword ptr [rcx]
003ADFC2  41 B8 01 00 00 00               mov r8d, 1
003ADFC8  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
003ADFCD  E9 66 FE FF FF                  jmp 0x1403ade38
003ADFD2  44 8B D5                        mov r10d, ebp
003ADFD5  E9 65 FF FF FF                  jmp 0x1403adf3f
003ADFDA  44 8B C0                        mov r8d, eax
003ADFDD  49 83 C0 04                     add r8, 4
003ADFE1  49 89 1E                        mov qword ptr [r14], rbx
003ADFE4  83 BC 24 A8 00 00 00 00         cmp dword ptr [rsp + 0xa8], 0
003ADFEC  4E 8D 04 83                     lea r8, [rbx + r8*4]
003ADFF0  4D 89 46 08                     mov qword ptr [r14 + 8], r8
003ADFF4  74 10                           je 0x1403ae006
003ADFF6  4D 2B 34 24                     sub r14, qword ptr [r12]
003ADFFA  49 C1 FE 04                     sar r14, 4
003ADFFE  41 FF C6                        inc r14d
003AE001  45 89 74 24 18                  mov dword ptr [r12 + 0x18], r14d
003AE006  8B 0B                           mov ecx, dword ptr [rbx]
003AE008  0F B7 D1                        movzx edx, cx
003AE00B  3B C2                           cmp eax, edx
003AE00D  0F 83 9B 01 00 00               jae 0x1403ae1ae
003AE013  41 8B 28                        mov ebp, dword ptr [r8]
003AE016  41 BE 01 00 00 00               mov r14d, 1
003AE01C  45 8B 8D 48 01 00 00            mov r9d, dword ptr [r13 + 0x148]
003AE023  8B D5                           mov edx, ebp
003AE025  41 8B 9D 4C 01 00 00            mov ebx, dword ptr [r13 + 0x14c]
003AE02C  41 8B C9                        mov ecx, r9d
003AE02F  45 8B 9D 50 01 00 00            mov r11d, dword ptr [r13 + 0x150]
003AE036  8B C3                           mov eax, ebx
003AE038  41 8B BD 58 01 00 00            mov edi, dword ptr [r13 + 0x158]
003AE03F  45 8B C6                        mov r8d, r14d
003AE042  D3 EA                           shr edx, cl
003AE044  23 C5                           and eax, ebp
003AE046  0F BD CA                        bsr ecx, edx
003AE049  41 0F AF C3                     imul eax, r11d
003AE04D  23 DE                           and ebx, esi
003AE04F  41 D3 E0                        shl r8d, cl
003AE052  4C 33 C2                        xor r8, rdx
003AE055  41 0F AF DB                     imul ebx, r11d
003AE059  4D 03 C0                        add r8, r8
003AE05C  C7 84 24 A0 00 00 00 00 00 00 00  mov dword ptr [rsp + 0xa0], 0
003AE067  49 8B 54 CD 40                  mov rdx, qword ptr [r13 + rcx*8 + 0x40]
003AE06C  41 8B C9                        mov ecx, r9d
003AE06F  C7 84 24 A0 00 00 00 00 00 00 00  mov dword ptr [rsp + 0xa0], 0
003AE07A  4E 8B 14 C2                     mov r10, qword ptr [rdx + r8*8]
003AE07E  8B D6                           mov edx, esi
003AE080  D3 EA                           shr edx, cl
003AE082  4C 03 D0                        add r10, rax
003AE085  0F BD CA                        bsr ecx, edx
003AE088  8B C3                           mov eax, ebx
003AE08A  41 D3 E6                        shl r14d, cl
003AE08D  45 8B C6                        mov r8d, r14d
003AE090  4C 33 C2                        xor r8, rdx
003AE093  49 8B 4C CD 40                  mov rcx, qword ptr [r13 + rcx*8 + 0x40]
003AE098  4D 03 C0                        add r8, r8
003AE09B  4A 8B 14 C1                     mov rdx, qword ptr [rcx + r8*8]
003AE09F  41 8B 4C 3A 08                  mov ecx, dword ptr [r10 + rdi + 8]
003AE0A4  48 03 D0                        add rdx, rax
003AE0A7  3B 4C 3A 08                     cmp ecx, dword ptr [rdx + rdi + 8]
003AE0AB  0F 82 FD 00 00 00               jb 0x1403ae1ae
003AE0B1  0F 87 F7 00 00 00               ja 0x1403ae1ae
003AE0B7  3B EE                           cmp ebp, esi
003AE0B9  0F 82 EF 00 00 00               jb 0x1403ae1ae
003AE0BF  0F 87 E9 00 00 00               ja 0x1403ae1ae
003AE0C5  33 C0                           xor eax, eax
003AE0C7  48 8B 9C 24 98 00 00 00         mov rbx, qword ptr [rsp + 0x98]
003AE0CF  48 83 C4 50                     add rsp, 0x50
003AE0D3  41 5F                           pop r15
003AE0D5  41 5E                           pop r14
003AE0D7  41 5D                           pop r13
003AE0D9  41 5C                           pop r12
003AE0DB  5F                              pop rdi
003AE0DC  5E                              pop rsi
003AE0DD  5D                              pop rbp
003AE0DE  C3                              ret
003AE0DF  CC                              int3
003AE0E0  E9 2B FD FF FF                  jmp 0x1403ade10
003AE0E5  33 D2                           xor edx, edx
003AE0E7  4D 8D 74 24 08                  lea r14, [r12 + 8]
003AE0EC  89 94 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], edx
003AE0F3  E9 29 FD FF FF                  jmp 0x1403ade21
003AE0F8  48 8D 4B 08                     lea rcx, [rbx + 8]
003AE0FC  E9 B1 FE FF FF                  jmp 0x1403adfb2
003AE101  8D 2C 09                        lea ebp, [rcx + rcx]
003AE104  B9 08 00 00 00                  mov ecx, 8
003AE109  3B E9                           cmp ebp, ecx
003AE10B  0F 42 E9                        cmovb ebp, ecx
003AE10E  3B C5                           cmp eax, ebp
003AE110  0F 83 E0 01 00 00               jae 0x1403ae2f6
003AE116  8B FD                           mov edi, ebp
003AE118  48 C1 E7 04                     shl rdi, 4
003AE11C  49 3B FB                        cmp rdi, r11
003AE11F  77 70                           ja 0x1403ae191
003AE121  8B D7                           mov edx, edi
003AE123  B9 40 00 00 00                  mov ecx, 0x40
003AE128  41 B8 73 6D 41 72               mov r8d, 0x72416d73
003AE12E  E8 BD 3F 7D 00                  call 0x140b820f0
003AE133  4C 8B F0                        mov r14, rax
003AE136  48 85 C0                        test rax, rax
003AE139  74 56                           je 0x1403ae191
003AE13B  41 8B 5C 24 1C                  mov ebx, dword ptr [r12 + 0x1c]
003AE140  33 D2                           xor edx, edx
003AE142  C1 E3 04                        shl ebx, 4
003AE145  2B FB                           sub edi, ebx
003AE147  44 8B FB                        mov r15d, ebx
003AE14A  44 8B C7                        mov r8d, edi
003AE14D  48 8D 0C 03                     lea rcx, [rbx + rax]
003AE151  E8 EA 8A 31 00                  call 0x1406c6c40
003AE156  85 DB                           test ebx, ebx
003AE158  74 1A                           je 0x1403ae174
003AE15A  49 8B 14 24                     mov rdx, qword ptr [r12]
003AE15E  45 8B C7                        mov r8d, r15d
003AE161  49 8B CE                        mov rcx, r14
003AE164  E8 D7 86 31 00                  call 0x1406c6840
003AE169  49 8B 0C 24                     mov rcx, qword ptr [r12]
003AE16D  33 D2                           xor edx, edx
003AE16F  E8 FC 46 7D 00                  call 0x140b82870
003AE174  41 B8 01 00 00 00               mov r8d, 1
003AE17A  4D 89 34 24                     mov qword ptr [r12], r14
003AE17E  41 8B D0                        mov edx, r8d
003AE181  41 89 6C 24 1C                  mov dword ptr [r12 + 0x1c], ebp
003AE186  41 BB FF FF FF FF               mov r11d, 0xffffffff
003AE18C  E9 8C FC FF FF                  jmp 0x1403ade1d
003AE191  B8 9A 00 00 C0                  mov eax, 0xc000009a
003AE196  E9 2C FF FF FF                  jmp 0x1403ae0c7
003AE19B  85 D2                           test edx, edx
003AE19D  75 0F                           jne 0x1403ae1ae
003AE19F  49 C7 06 00 00 00 00            mov qword ptr [r14], 0
003AE1A6  49 C7 46 08 00 00 00 00         mov qword ptr [r14 + 8], 0
003AE1AE  B8 25 02 00 C0                  mov eax, 0xc0000225
003AE1B3  E9 0F FF FF FF                  jmp 0x1403ae0c7
003AE1B8  85 C0                           test eax, eax
003AE1BA  0F 84 B0 FD FF FF               je 0x1403adf70
003AE1C0  45 8B BD 48 01 00 00            mov r15d, dword ptr [r13 + 0x148]
003AE1C7  8B EE                           mov ebp, esi
003AE1C9  45 8B B5 58 01 00 00            mov r14d, dword ptr [r13 + 0x158]
003AE1D0  41 8B CF                        mov ecx, r15d
003AE1D3  D3 ED                           shr ebp, cl
003AE1D5  41 8B 8D 4C 01 00 00            mov ecx, dword ptr [r13 + 0x14c]
003AE1DC  8B D1                           mov edx, ecx
003AE1DE  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
003AE1E2  23 D6                           and edx, esi
003AE1E4  41 8B 8D 50 01 00 00            mov ecx, dword ptr [r13 + 0x150]
003AE1EB  44 8B 64 24 20                  mov r12d, dword ptr [rsp + 0x20]
003AE1F0  89 4C 24 28                     mov dword ptr [rsp + 0x28], ecx
003AE1F4  0F AF CA                        imul ecx, edx
003AE1F7  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
003AE1FC  EB 08                           jmp 0x1403ae206
003AE1FE  66 90                           nop
003AE200  41 B8 01 00 00 00               mov r8d, 1
003AE206  42 8D 0C 10                     lea ecx, [rax + r10]
003AE20A  C7 44 24 20 00 00 00 00         mov dword ptr [rsp + 0x20], 0
003AE212  D1 E9                           shr ecx, 1
003AE214  8B F9                           mov edi, ecx
003AE216  48 03 C9                        add rcx, rcx
003AE219  C7 44 24 20 00 00 00 00         mov dword ptr [rsp + 0x20], 0
003AE221  45 8B 1C C9                     mov r11d, dword ptr [r9 + rcx*8]
003AE225  41 8B CF                        mov ecx, r15d
003AE228  41 8B D3                        mov edx, r11d
003AE22B  45 8B CC                        mov r9d, r12d
003AE22E  D3 EA                           shr edx, cl
003AE230  45 23 CB                        and r9d, r11d
003AE233  44 0F AF 4C 24 28               imul r9d, dword ptr [rsp + 0x28]
003AE239  0F BD CA                        bsr ecx, edx
003AE23C  41 D3 E0                        shl r8d, cl
003AE23F  44 33 C2                        xor r8d, edx
003AE242  49 8B 54 CD 40                  mov rdx, qword ptr [r13 + rcx*8 + 0x40]
003AE247  41 8B C8                        mov ecx, r8d
003AE24A  41 B8 01 00 00 00               mov r8d, 1
003AE250  48 03 C9                        add rcx, rcx
003AE253  48 8B 14 CA                     mov rdx, qword ptr [rdx + rcx*8]
003AE257  49 03 D6                        add rdx, r14
003AE25A  4C 03 CA                        add r9, rdx
003AE25D  0F BD CD                        bsr ecx, ebp
003AE260  41 D3 E0                        shl r8d, cl
003AE263  44 33 C5                        xor r8d, ebp
003AE266  49 8B 54 CD 40                  mov rdx, qword ptr [r13 + rcx*8 + 0x40]
003AE26B  41 8B C8                        mov ecx, r8d
003AE26E  4C 8B 44 24 40                  mov r8, qword ptr [rsp + 0x40]
003AE273  48 03 C9                        add rcx, rcx
003AE276  48 8B 14 CA                     mov rdx, qword ptr [rdx + rcx*8]
003AE27A  41 8B 49 08                     mov ecx, dword ptr [r9 + 8]
003AE27E  49 03 D6                        add rdx, r14
003AE281  41 3B 4C 10 08                  cmp ecx, dword ptr [r8 + rdx + 8]
003AE286  72 07                           jb 0x1403ae28f
003AE288  77 1D                           ja 0x1403ae2a7
003AE28A  44 3B DE                        cmp r11d, esi
003AE28D  77 18                           ja 0x1403ae2a7
003AE28F  44 8B D7                        mov r10d, edi
003AE292  41 8D 4A 01                     lea ecx, [r10 + 1]
003AE296  4C 8D 4B 10                     lea r9, [rbx + 0x10]
003AE29A  3B C8                           cmp ecx, eax
003AE29C  0F 85 5E FF FF FF               jne 0x1403ae200
003AE2A2  E9 B6 FC FF FF                  jmp 0x1403adf5d
003AE2A7  8B C7                           mov eax, edi
003AE2A9  EB E7                           jmp 0x1403ae292
003AE2AB  80 7B 02 02                     cmp byte ptr [rbx + 2], 2
003AE2AF  0F 85 0A FD FF FF               jne 0x1403adfbf
003AE2B5  45 0F B6 44 24 20               movzx r8d, byte ptr [r12 + 0x20]
003AE2BB  48 8B D1                        mov rdx, rcx
003AE2BE  41 83 E0 01                     and r8d, 1
003AE2C2  49 8D 4D 10                     lea rcx, [r13 + 0x10]
003AE2C6  45 03 C0                        add r8d, r8d
003AE2C9  E8 72 C0 FF FF                  call 0x1403aa340
003AE2CE  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
003AE2D3  48 8B D8                        mov rbx, rax
003AE2D6  48 85 C0                        test rax, rax
003AE2D9  74 11                           je 0x1403ae2ec
003AE2DB  41 B8 01 00 00 00               mov r8d, 1
003AE2E1  41 BB FF FF FF FF               mov r11d, 0xffffffff
003AE2E7  E9 4C FB FF FF                  jmp 0x1403ade38
003AE2EC  B8 06 00 00 C0                  mov eax, 0xc0000006
003AE2F1  E9 D1 FD FF FF                  jmp 0x1403ae0c7
003AE2F6  8D 68 08                        lea ebp, [rax + 8]
003AE2F9  3B E8                           cmp ebp, eax
003AE2FB  0F 82 90 FE FF FF               jb 0x1403ae191
003AE301  E9 10 FE FF FF                  jmp 0x1403ae116
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_HASH_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_HAS(__int64 a1, int a2, __int64 a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p8;
    unsigned int v_stack_pA8;

    v_stack_p10 = v_rbx;
    v_stack_p18 = a3;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (80);
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_HASH_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_HAS(a1, a3, a3, a4);
    if ((*(unsigned int *)(a3 + 24)) == ((unsigned int)((unsigned int)(0xFFFFFFFFULL)))) goto loc_003AE0E5;
    v_stack_p20 = 1;
    if (*(unsigned __int64 *)(a1) == 0) goto loc_003AE0E0;
loc_003ADE10:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 28)))) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 2)))) goto loc_003AE101;
loc_003ADE1D:
loc_003ADE21:
    v_stack_m58 = *(unsigned __int64 *)(a3);
    v_stack_m68 = *(unsigned __int64 *)(a1);
    if (*(unsigned __int64 *)(a1) == 0) goto loc_003AE19B;
loc_003ADE38:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1)))) >> (24));
    v_stack_m48 = *(unsigned __int64 *)(a1) + 16;
    if ((unsigned __int8)(a1) == 0) goto loc_003AE1B8;
    if ((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1))))) == 0) goto loc_003ADF70;
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) >> ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 328)))))));
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 332))))) & ((unsigned int)((unsigned int)(a2))));
    v_stack_m60 = (unsigned int)(*(unsigned int *)(a1 + 344));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 336))))) * (a2));
    v_stack_m50 = a1;
    goto loc_003ADEA6;
loc_003ADEA0:
loc_003ADEA6:
    v_stack_m60 = 0;
    a1 = (unsigned int)(((unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1)))) + (unsigned int)((unsigned int)((unsigned int)(0xFFFFFFFFULL))) * 1) >> (1));
    v_stack_m60 = 0;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 16 + a1 * 4))))) >> ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 328)))))));
    a4 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 332))))) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 16 + a1 * 4)))));
    a4 = (unsigned int)((a4) * ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 336)))));
    a3 = (unsigned int)((1) << ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 328)))))));
    a3 = (unsigned int)((a3) ^ (a2));
    a1 = ((unsigned int)((unsigned int)(a3))) + ((unsigned int)((unsigned int)(a3)));
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 328)))) * 8 + 64) + a1 * 8)) + (v_stack_m60);
    a4 = (a4) + (a2);
    a3 = (unsigned int)((1) << ((unsigned __int8)(a1)));
    a3 = (unsigned int)((a3) ^ ((unsigned int)(v_rdi)));
    a1 = ((unsigned int)((unsigned int)(a3))) + ((unsigned int)((unsigned int)(a3)));
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + a1 * 8 + 64) + a1 * 8)) + (v_stack_m60);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 8)))) < (*(unsigned int *)((unsigned int)((unsigned int)(a1)) + a2 * 1 + 8))) goto loc_003ADFD2;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 8)))) > (*(unsigned int *)((unsigned int)((unsigned int)(a1)) + a2 * 1 + 8))) goto loc_003ADF3D;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 16 + a1 * 4)))) < ((unsigned int)((unsigned int)(a2)))) goto loc_003ADFD2;
loc_003ADF3D:
loc_003ADF3F:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xFFFFFFFFULL))) + 1)) != ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1))))))) goto loc_003ADEA0;
loc_003ADF5D:
loc_003ADF70:
    if ((*(unsigned __int8 *)(v_stack_m68 + 3)) != 0) goto loc_003ADFDA;
    v_r14 = v_stack_m58;
    if (v_stack_p20 != 0) {
        a1 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1)))));
        a1 = (a1) + 1;
        *(unsigned __int64 *)(v_stack_m58) = v_stack_m68;
        a1 = (a1) << (4);
        a1 = (a1) + (v_stack_m68);
        *(unsigned __int64 *)(v_stack_m58 + 8) = a1;
        v_r14 = (v_stack_m58) + (16);
        v_stack_m58 = v_r14;
    }
    if ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1))))) == 0) goto loc_003AE0F8;
    a1 = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1)))) - 1) << (4);
    a1 = (a1) + (24);
    a1 = (a1) + (v_stack_m68);
loc_003ADFB2:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_p8 + 16))) != ((unsigned int)((unsigned int)(0xFFFFFFFFULL)))) goto loc_003AE2AB;
loc_003ADFBF:
    v_stack_m68 = *(unsigned __int64 *)(a1);
    goto loc_003ADE38;
loc_003ADFD2:
    goto loc_003ADF3F;
loc_003ADFDA:
    a3 = ((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_p8 + 16)))) + (4);
    *(unsigned __int64 *)(v_r14) = *(unsigned __int64 *)(a1);
    *(unsigned __int64 *)(v_r14 + 8) = *(unsigned __int64 *)(a1) + a3 * 4;
    if (v_stack_p20 != 0) {
        v_r14 = (v_r14) - (*(unsigned __int64 *)(v_stack_p18));
        v_r14 = (v_r14) >> (4);
        v_r14 = (unsigned int)((v_r14) + 1);
        *(unsigned int *)(v_stack_p18 + 24) = (unsigned int)(v_r14);
    }
    if (((unsigned int)(*(unsigned __int64 *)(v_stack_p8 + 16))) >= ((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1))))))) goto loc_003AE1AE;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + a3 * 4))))) >> ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 328)))))));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 332))))) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + a3 * 4)))));
    result = (unsigned int)((result) * ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 336)))));
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p8 + 332))) & ((unsigned int)((unsigned int)(a2))));
    a3 = (unsigned int)((1) << ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 328)))))));
    a3 = (a3) ^ (a2);
    v_rbx = (unsigned int)((v_rbx) * ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 336)))));
    a3 = (a3) + (a3);
    v_stack_p18 = 0;
    v_stack_p18 = 0;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) >> ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 328)))))));
    v_r10 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 328)))) * 8 + 64) + a3 * 8)) + (result);
    v_r14 = (unsigned int)((1) << ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 328)))))));
    a3 = ((unsigned int)((unsigned int)(v_r14))) ^ (a2);
    a3 = (a3) + (a3);
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 328)))) * 8 + 64) + a3 * 8)) + ((unsigned int)((unsigned int)(v_rbx)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r10 + (unsigned int)(*(unsigned int *)(v_stack_p8 + 344)) * 1 + 8)))) < (*(unsigned int *)(a2 + (unsigned int)(*(unsigned int *)(v_stack_p8 + 344)) * 1 + 8))) goto loc_003AE1AE;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r10 + (unsigned int)(*(unsigned int *)(v_stack_p8 + 344)) * 1 + 8)))) > (*(unsigned int *)(a2 + (unsigned int)(*(unsigned int *)(v_stack_p8 + 344)) * 1 + 8))) goto loc_003AE1AE;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + a3 * 4)))) < ((unsigned int)((unsigned int)(a2)))) goto loc_003AE1AE;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + a3 * 4)))) > ((unsigned int)((unsigned int)(a2)))) goto loc_003AE1AE;
    result = 0;
loc_003AE0C7:
    v_rsp = (v_rsp) + (80);
    return result;
loc_003AE0E0:
    goto loc_003ADE10;
loc_003AE0E5:
    a2 = 0;
    v_stack_pA8 = 0;
    goto loc_003ADE21;
loc_003AE0F8:
    goto loc_003ADFB2;
loc_003AE101:
    v_rbp = v_stack_p10 + 8 + v_stack_p10 + 8 * 1;
    if (((unsigned int)(v_stack_p10 + 8 + v_stack_p10 + 8 * 1)) < 8) { v_rbp = 8; }
    if (0 >= ((unsigned int)(v_rbp))) goto loc_003AE2F6;
loc_003AE116:
    v_rdi = ((unsigned int)((unsigned int)(v_rbp))) << (4);
    if (v_rdi > ((unsigned int)(*(unsigned int *)(v_stack_p8 + 336)))) goto loc_003AE191;
    result = ExAllocatePool2(64, (unsigned int)((unsigned int)(v_rdi)), (unsigned int)(0x72416D73ULL), (unsigned int)(*(unsigned int *)(v_stack_p8 + 328)));
    if (result == 0) goto loc_003AE191;
    a2 = 0;
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p18 + 28))) << (4));
    v_rdi = (unsigned int)((v_rdi) - ((unsigned int)(v_rbx)));
    result = memset(v_rbx + result * 1, a2, (unsigned int)((unsigned int)(v_rdi)), (unsigned int)(*(unsigned int *)(v_stack_p8 + 328)));
    if ((unsigned int)(v_rbx) != 0) {
        a2 = *(unsigned __int64 *)(v_stack_p18);
        a3 = (unsigned int)((unsigned int)((unsigned int)(v_rbx)));
        a1 = result;
        result = memcpy(a1, a2, a3, (unsigned int)(*(unsigned int *)(v_stack_p8 + 328)));
        a1 = *(unsigned __int64 *)(v_stack_p18);
        a2 = 0;
        result = ExFreePoolWithTag(a1, a2, a3, (unsigned int)(*(unsigned int *)(v_stack_p8 + 328)));
    }
    *(unsigned __int64 *)(v_stack_p18) = result;
    *(unsigned int *)(v_stack_p18 + 28) = (unsigned int)(v_rbp);
    goto loc_003ADE1D;
loc_003AE191:
    goto loc_003AE0C7;
loc_003AE19B:
    if (1 == 0) {
        *(unsigned __int64 *)(result) = 0;
        *(unsigned __int64 *)(result + 8) = 0;
    }
    goto loc_003AE0C7;
loc_003AE1B8:
    if ((unsigned int)((unsigned int)(0xC0000225ULL)) == 0) goto loc_003ADF70;
    v_rbp = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) >> ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 328)))))));
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 332)));
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 332))))) & ((unsigned int)((unsigned int)(a2))));
    v_stack_p28 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 336)));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p8 + 336))) * (a2));
    v_stack_p40 = a1;
    goto loc_003AE206;
loc_003AE200:
loc_003AE206:
    v_stack_p20 = 0;
    a1 = (unsigned int)(((unsigned int)(0xC0000225ULL) + v_r10 * 1) >> (1));
    a1 = (a1) + (a1);
    v_stack_p20 = 0;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_stack_p8 + 328)) + a1 * 8))))) >> ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 328)))))));
    a4 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_p20)))) & ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_stack_p8 + 328)) + a1 * 8)))));
    a4 = (unsigned int)((a4) * (v_stack_p28));
    a3 = (unsigned int)((1) << ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 328)))))));
    a3 = (unsigned int)((a3) ^ (a2));
    a1 = ((unsigned int)((unsigned int)(a3))) + ((unsigned int)((unsigned int)(a3)));
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 328)))) * 8 + 64) + a1 * 8)) + ((unsigned int)(*(unsigned int *)(v_stack_p8 + 344)));
    a4 = (a4) + (a2);
    a3 = (unsigned int)((1) << ((unsigned __int8)(a1)));
    a3 = (unsigned int)((a3) ^ ((unsigned int)(v_rbp)));
    a1 = ((unsigned int)((unsigned int)(a3))) + ((unsigned int)((unsigned int)(a3)));
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + a1 * 8 + 64) + a1 * 8)) + ((unsigned int)(*(unsigned int *)(v_stack_p8 + 344)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 8)))) < (*(unsigned int *)(v_stack_p40 + a2 * 1 + 8))) goto loc_003AE28F;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 8)))) > (*(unsigned int *)(v_stack_p40 + a2 * 1 + 8))) goto loc_003AE2A7;
    if (((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_stack_p8 + 328)) + a1 * 8)))) > ((unsigned int)((unsigned int)(a2)))) goto loc_003AE2A7;
loc_003AE28F:
loc_003AE292:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1)))) + 1)) != ((unsigned int)((unsigned int)(0xC0000225ULL)))) goto loc_003AE200;
    goto loc_003ADF5D;
loc_003AE2A7:
    goto loc_003AE292;
loc_003AE2AB:
    if ((*(unsigned __int8 *)(v_rbx + 2)) != 2) goto loc_003ADFBF;
    a3 = (unsigned int)((*(unsigned __int8 *)((unsigned int)(v_stack_p20) + 32)) & (1));
    a3 = (unsigned int)((a3) + ((unsigned int)(a3)));
    result = NP_CONTEXT__NpLeafRefInternal(v_stack_p8 + 16, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1)))) + 1, a3, v_rbx + 16);
    v_stack_p20 = result;
    if (result == 0) goto loc_003AE2EC;
    goto loc_003ADE38;
loc_003AE2EC:
    goto loc_003AE0C7;
loc_003AE2F6:
    if (((unsigned int)((unsigned int)(0xC0000006ULL) + 8)) < ((unsigned int)((unsigned int)(0xC0000006ULL)))) goto loc_003AE191;
    goto loc_003AE116;
}
```

## 5. (Beta) C Style

```c
int64_t B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_HASH_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_HAS(void *Arg1, int32_t Arg2, void *Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r10;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint32_t v_stack_p28;
    uint64_t v_stack_p40;
    uint64_t v_stack_p8;
    uint32_t v_stack_pA8;

    v_stack_p10 = local_rbx;
    v_stack_p18 = Arg3;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (80);
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_HASH_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_HAS(Arg1, Arg3, Arg3, a4);
    if ((*(uint32_t *)(arg3 + 0x18)) == ((uint32_t)((uint32_t)(0xFFFFFFFFULL)))) goto loc_003AE0E5;
    v_stack_p20 = 1;
    if (*(uint64_t *)(arg1) == 0) goto loc_003AE0E0;
loc_003ADE10:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x1C)))) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg1) + 0x2)))) goto loc_003AE101;
loc_003ADE1D:
loc_003ADE21:
    v_stack_m58 = *(uint64_t *)(arg3);
    v_stack_m68 = *(uint64_t *)(arg1);
    if (*(uint64_t *)(arg1) == 0) goto loc_003AE19B;
loc_003ADE38:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1)))) >> (24));
    v_stack_m48 = *(uint64_t *)(arg1) + 16;
    if ((uint8_t)(Arg1) == 0) goto loc_003AE1B8;
    if ((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1))))) == 0) goto loc_003ADF70;
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) >> ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x148)))))));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x14C))))) & ((uint32_t)((uint32_t)(Arg2))));
    v_stack_m60 = (uint32_t)(*(uint32_t *)(arg1 + 0x158));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x150))))) * (Arg2));
    v_stack_m50 = Arg1;
    goto loc_003ADEA6;
loc_003ADEA0:
loc_003ADEA6:
    v_stack_m60 = 0;
    Arg1 = (uint32_t)(((uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1)))) + (uint32_t)((uint32_t)((uint32_t)(0xFFFFFFFFULL))) * 1) >> (1));
    v_stack_m60 = 0;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x10 + arg1 * 4))))) >> ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x148)))))));
    a4 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x14C))))) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x10 + arg1 * 4)))));
    a4 = (uint32_t)((a4) * ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x150)))));
    Arg3 = (uint32_t)((1) << ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x148)))))));
    Arg3 = (uint32_t)((Arg3) ^ (Arg2));
    Arg1 = ((uint32_t)((uint32_t)(Arg3))) + ((uint32_t)((uint32_t)(Arg3)));
    Arg2 = (*(uint64_t *)(*(uint64_t *)(v_stack_p8 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x148)))) * 8 + 0x40) + arg1 * 8)) + (v_stack_m60);
    a4 = (a4) + (Arg2);
    Arg3 = (uint32_t)((1) << ((uint8_t)(Arg1)));
    Arg3 = (uint32_t)((Arg3) ^ ((uint32_t)(local_rdi)));
    Arg1 = ((uint32_t)((uint32_t)(Arg3))) + ((uint32_t)((uint32_t)(Arg3)));
    Arg2 = (*(uint64_t *)(*(uint64_t *)(v_stack_p8 + arg1 * 8 + 0x40) + arg1 * 8)) + (v_stack_m60);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(a4 + 0x8)))) < (*(uint32_t *)((uint32_t)((uint32_t)(arg1)) + Arg2 * 1 + 0x8))) goto loc_003ADFD2;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(a4 + 0x8)))) > (*(uint32_t *)((uint32_t)((uint32_t)(arg1)) + Arg2 * 1 + 0x8))) goto loc_003ADF3D;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x10 + arg1 * 4)))) < ((uint32_t)((uint32_t)(Arg2)))) goto loc_003ADFD2;
loc_003ADF3D:
loc_003ADF3F:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xFFFFFFFFULL))) + 1)) != ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1))))))) goto loc_003ADEA0;
loc_003ADF5D:
loc_003ADF70:
    if ((*(uint8_t *)(v_stack_m68 + 0x3)) != 0) goto loc_003ADFDA;
    local_r14 = v_stack_m58;
    if (v_stack_p20 != 0) {
        Arg1 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1)))));
        Arg1 = (Arg1) + 1;
        *(uint64_t *)(v_stack_m58) = v_stack_m68;
        Arg1 = (Arg1) << (4);
        Arg1 = (Arg1) + (v_stack_m68);
        *(void **)(v_stack_m58 + 0x8) = Arg1;
        local_r14 = (v_stack_m58) + (16);
        v_stack_m58 = local_r14;
    }
    if ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1))))) == 0) goto loc_003AE0F8;
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1)))) - 1) << (4);
    Arg1 = (Arg1) + (24);
    Arg1 = (Arg1) + (v_stack_m68);
loc_003ADFB2:
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_p8 + 0x10))) != ((uint32_t)((uint32_t)(0xFFFFFFFFULL)))) goto loc_003AE2AB;
loc_003ADFBF:
    v_stack_m68 = *(uint64_t *)(arg1);
    goto loc_003ADE38;
loc_003ADFD2:
    goto loc_003ADF3F;
loc_003ADFDA:
    Arg3 = ((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_p8 + 0x10)))) + (4);
    *(uint64_t *)(local_r14) = *(uint64_t *)(arg1);
    *(uint64_t *)(local_r14 + 0x8) = *(uint64_t *)(arg1) + Arg3 * 4;
    if (v_stack_p20 != 0) {
        local_r14 = (local_r14) - (*(uint64_t *)(v_stack_p18));
        local_r14 = (local_r14) >> (4);
        local_r14 = (uint32_t)((local_r14) + 1);
        *(uint32_t *)(v_stack_p18 + 0x18) = (uint32_t)(local_r14);
    }
    if (((uint32_t)(*(uint64_t *)(v_stack_p8 + 0x10))) >= ((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1))))))) goto loc_003AE1AE;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + arg3 * 4))))) >> ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x148)))))));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x14C))))) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + arg3 * 4)))));
    result = (uint32_t)((result) * ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x150)))));
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x14C))) & ((uint32_t)((uint32_t)(Arg2))));
    Arg3 = (uint32_t)((1) << ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x148)))))));
    Arg3 = (Arg3) ^ (Arg2);
    local_rbx = (uint32_t)((local_rbx) * ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x150)))));
    Arg3 = (Arg3) + (Arg3);
    v_stack_p18 = 0;
    v_stack_p18 = 0;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) >> ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x148)))))));
    local_r10 = (*(uint64_t *)(*(uint64_t *)(v_stack_p8 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x148)))) * 8 + 0x40) + arg3 * 8)) + (result);
    local_r14 = (uint32_t)((1) << ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x148)))))));
    Arg3 = ((uint32_t)((uint32_t)(local_r14))) ^ (Arg2);
    Arg3 = (Arg3) + (Arg3);
    Arg2 = (*(uint64_t *)(*(uint64_t *)(v_stack_p8 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x148)))) * 8 + 0x40) + arg3 * 8)) + ((uint32_t)((uint32_t)(local_rbx)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r10 + (uint32_t)(*(uint32_t *)(v_stack_p8 + 0x158)) * 1 + 0x8)))) < (*(uint32_t *)(Arg2 + (uint32_t)(*(uint32_t *)(v_stack_p8 + 0x158)) * 1 + 0x8))) goto loc_003AE1AE;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r10 + (uint32_t)(*(uint32_t *)(v_stack_p8 + 0x158)) * 1 + 0x8)))) > (*(uint32_t *)(Arg2 + (uint32_t)(*(uint32_t *)(v_stack_p8 + 0x158)) * 1 + 0x8))) goto loc_003AE1AE;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + arg3 * 4)))) < ((uint32_t)((uint32_t)(Arg2)))) goto loc_003AE1AE;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + arg3 * 4)))) > ((uint32_t)((uint32_t)(Arg2)))) goto loc_003AE1AE;
    result = 0;
loc_003AE0C7:
    local_rsp = (local_rsp) + (80);
    return result;
loc_003AE0E0:
    goto loc_003ADE10;
loc_003AE0E5:
    Arg2 = 0;
    v_stack_pA8 = 0;
    goto loc_003ADE21;
loc_003AE0F8:
    goto loc_003ADFB2;
loc_003AE101:
    local_rbp = v_stack_p10 + 8 + v_stack_p10 + 8 * 1;
    if (((uint32_t)(v_stack_p10 + 8 + v_stack_p10 + 8 * 1)) < 8) { local_rbp = 8; }
    if (0 >= ((uint32_t)(local_rbp))) goto loc_003AE2F6;
loc_003AE116:
    local_rdi = ((uint32_t)((uint32_t)(local_rbp))) << (4);
    if (local_rdi > ((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x150)))) goto loc_003AE191;
    result = ExAllocatePool2(64, (uint32_t)((uint32_t)(local_rdi)), (uint32_t)(0x72416D73ULL), (uint32_t)(*(uint32_t *)(v_stack_p8 + 0x148)));
    if (result == 0) goto loc_003AE191;
    Arg2 = 0;
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p18 + 0x1C))) << (4));
    local_rdi = (uint32_t)((local_rdi) - ((uint32_t)(local_rbx)));
    result = memset(local_rbx + result * 1, Arg2, (uint32_t)((uint32_t)(local_rdi)), (uint32_t)(*(uint32_t *)(v_stack_p8 + 0x148)));
    if ((uint32_t)(local_rbx) != 0) {
        Arg2 = *(uint64_t *)(v_stack_p18);
        Arg3 = (uint32_t)((uint32_t)((uint32_t)(local_rbx)));
        Arg1 = result;
        result = memcpy(Arg1, Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_stack_p8 + 0x148)));
        Arg1 = *(uint64_t *)(v_stack_p18);
        Arg2 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_stack_p8 + 0x148)));
    }
    *(uint64_t *)(v_stack_p18) = result;
    *(uint32_t *)(v_stack_p18 + 0x1C) = (uint32_t)(local_rbp);
    goto loc_003ADE1D;
loc_003AE191:
    goto loc_003AE0C7;
loc_003AE19B:
    if (1 == 0) {
        *(uint64_t *)(result) = 0;
        *(uint64_t *)(result + 0x8) = 0;
    }
    goto loc_003AE0C7;
loc_003AE1B8:
    if ((uint32_t)((uint32_t)(0xC0000225ULL)) == 0) goto loc_003ADF70;
    local_rbp = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) >> ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x148)))))));
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x14C)));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x14C))))) & ((uint32_t)((uint32_t)(Arg2))));
    v_stack_p28 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x150)));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x150))) * (Arg2));
    v_stack_p40 = Arg1;
    goto loc_003AE206;
loc_003AE200:
loc_003AE206:
    v_stack_p20 = 0;
    Arg1 = (uint32_t)(((uint32_t)(0xC0000225ULL) + local_r10 * 1) >> (1));
    Arg1 = (Arg1) + (Arg1);
    v_stack_p20 = 0;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x148)) + arg1 * 8))))) >> ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x148)))))));
    a4 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_p20)))) & ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x148)) + arg1 * 8)))));
    a4 = (uint32_t)((a4) * (v_stack_p28));
    Arg3 = (uint32_t)((1) << ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x148)))))));
    Arg3 = (uint32_t)((Arg3) ^ (Arg2));
    Arg1 = ((uint32_t)((uint32_t)(Arg3))) + ((uint32_t)((uint32_t)(Arg3)));
    Arg2 = (*(uint64_t *)(*(uint64_t *)(v_stack_p8 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x148)))) * 8 + 0x40) + arg1 * 8)) + ((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x158)));
    a4 = (a4) + (Arg2);
    Arg3 = (uint32_t)((1) << ((uint8_t)(Arg1)));
    Arg3 = (uint32_t)((Arg3) ^ ((uint32_t)(local_rbp)));
    Arg1 = ((uint32_t)((uint32_t)(Arg3))) + ((uint32_t)((uint32_t)(Arg3)));
    Arg2 = (*(uint64_t *)(*(uint64_t *)(v_stack_p8 + arg1 * 8 + 0x40) + arg1 * 8)) + ((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x158)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(a4 + 0x8)))) < (*(uint32_t *)(v_stack_p40 + Arg2 * 1 + 0x8))) goto loc_003AE28F;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(a4 + 0x8)))) > (*(uint32_t *)(v_stack_p40 + Arg2 * 1 + 0x8))) goto loc_003AE2A7;
    if (((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x148)) + arg1 * 8)))) > ((uint32_t)((uint32_t)(Arg2)))) goto loc_003AE2A7;
loc_003AE28F:
loc_003AE292:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1)))) + 1)) != ((uint32_t)((uint32_t)(0xC0000225ULL)))) goto loc_003AE200;
    goto loc_003ADF5D;
loc_003AE2A7:
    goto loc_003AE292;
loc_003AE2AB:
    if ((*(uint8_t *)(local_rbx + 0x2)) != 2) goto loc_003ADFBF;
    Arg3 = (uint32_t)((*(uint8_t *)((uint32_t)(v_stack_p20) + 0x20)) & (1));
    Arg3 = (uint32_t)((Arg3) + ((uint32_t)(Arg3)));
    result = NP_CONTEXT__NpLeafRefInternal(v_stack_p8 + 16, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1)))) + 1, Arg3, local_rbx + 16);
    v_stack_p20 = result;
    if (result == 0) goto loc_003AE2EC;
    goto loc_003ADE38;
loc_003AE2EC:
    goto loc_003AE0C7;
loc_003AE2F6:
    if (((uint32_t)((uint32_t)(0xC0000006ULL) + 8)) < ((uint32_t)((uint32_t)(0xC0000006ULL)))) goto loc_003AE191;
    goto loc_003AE116;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg3` | `+ 0x0` | `64` | `R` |
| `Arg3` | `+ 0x0` | `64` | `W` |
| `Arg3` | `+ 0x8` | `64` | `R` |
| `Arg3` | `+ 0x18` | `32` | `R` |
| `Arg3` | `+ 0x1C` | `32` | `R` |
| `Arg3` | `+ 0x1C` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003ADDB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
