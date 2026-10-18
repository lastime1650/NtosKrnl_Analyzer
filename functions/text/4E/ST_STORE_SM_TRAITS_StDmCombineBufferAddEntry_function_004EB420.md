# ST_STORE&lt;SM_TRAITS&gt;::StDmCombineBufferAddEntry

- RVA: `0x004EB420`–`0x004EB9A5` (길이 `1,413` bytes)
- VA: `0x00000001404EB420`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D1810`
- 디코드: `378`개 명령, `1,413/1,413` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **10**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x004EB594` → [B_TREE<unsigned long,ST_STORE<SM_TRAITS>::_ST_HASH_ENTRY,4096,NP_CONTEXT,ST_STORE<SM_TRAITS>::ST_HASH_ENTRY_COMPARATOR>::BTreeSearchResultDeref](../3A/B_TREE_unsigned_long_ST_STORE_SM_TRAITS__ST_HASH_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS_ST_HASH_EN_function_003AE310.md) (function, `0x003AE310`)
- `0x004EB5BB` → [B_TREE<unsigned long,ST_STORE<SM_TRAITS>::_ST_HASH_ENTRY,4096,NP_CONTEXT,ST_STORE<SM_TRAITS>::ST_HASH_ENTRY_COMPARATOR>::BTreeSearchKey](../3A/B_TREE_unsigned_long_ST_STORE_SM_TRAITS__ST_HASH_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS_ST_HASH_EN_function_003ADDB0.md) (function, `0x003ADDB0`)
- `0x004EB5CA` → [B_TREE<unsigned long,ST_STORE<SM_TRAITS>::_ST_HASH_ENTRY,4096,NP_CONTEXT,ST_STORE<SM_TRAITS>::ST_HASH_ENTRY_COMPARATOR>::BTreeIteratorFromSearchResult](../43/B_TREE_unsigned_long_ST_STORE_SM_TRAITS__ST_HASH_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS_ST_HASH_EN_function_0043B840.md) (function, `0x0043B840`)
- `0x004EB641` → [B_TREE<unsigned long,ST_STORE<SM_TRAITS>::_ST_HASH_ENTRY,4096,NP_CONTEXT,ST_STORE<SM_TRAITS>::ST_HASH_ENTRY_COMPARATOR>::BTreeFindLeafSibling](../43/B_TREE_unsigned_long_ST_STORE_SM_TRAITS__ST_HASH_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS_ST_HASH_EN_function_0043F728.md) (function, `0x0043F728`)
- `0x004EB810` → [qsort_s](../50/qsort_s_function_00500DD0.md) (function, `0x00500DD0`)
- `0x004EB8F8` → [_chkstk](../6B/_chkstk_function_006BA960.md) (function, `0x006BA960`)
- `0x004EB92C` → [B_TREE<unsigned long,ST_STORE<SM_TRAITS>::_ST_HASH_ENTRY,4096,NP_CONTEXT,ST_STORE<SM_TRAITS>::ST_HASH_ENTRY_COMPARATOR>::BTreeSearchKey](../3A/B_TREE_unsigned_long_ST_STORE_SM_TRAITS__ST_HASH_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS_ST_HASH_EN_function_003ADDB0.md) (function, `0x003ADDB0`)
- `0x004EB948` → [B_TREE<unsigned long,ST_STORE<SM_TRAITS>::_ST_HASH_ENTRY,4096,NP_CONTEXT,ST_STORE<SM_TRAITS>::ST_HASH_ENTRY_COMPARATOR>::BTreeSearchResultDeref](../3A/B_TREE_unsigned_long_ST_STORE_SM_TRAITS__ST_HASH_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS_ST_HASH_EN_function_003AE310.md) (function, `0x003AE310`)
- `0x004EB96E` → [NP_CONTEXT::NpLeafDerefInternal](../3A/NP_CONTEXT_NpLeafDerefInternal_function_003A9A70.md) (function, `0x003A9A70`)
- `0x004EB97C` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [ST_STORE&lt;SM_TRAITS&gt;::StDmCombineRegion](../3B/ST_STORE_SM_TRAITS_StDmCombineRegion_function_003B0E34.md) at `0x003B0F9E`

### Static image references
- `0x004EB44B` → RVA `0x00E0A740` (`.data`; read)
- `0x004EB7EA` → RVA `0x00451140` (`ST_STORE<SM_TRAITS>::StDmCombineTargetCompare`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004EB420  40 55                           push rbp
004EB422  41 54                           push r12
004EB424  41 55                           push r13
004EB426  41 56                           push r14
004EB428  41 57                           push r15
004EB42A  48 81 EC A0 00 00 00            sub rsp, 0xa0
004EB431  48 8D 6C 24 30                  lea rbp, [rsp + 0x30]
004EB436  48 89 9D A0 00 00 00            mov qword ptr [rbp + 0xa0], rbx
004EB43D  48 89 B5 A8 00 00 00            mov qword ptr [rbp + 0xa8], rsi
004EB444  48 89 BD B0 00 00 00            mov qword ptr [rbp + 0xb0], rdi
004EB44B  48 8B 05 EE F2 91 00            mov rax, qword ptr [rip + 0x91f2ee]
004EB452  48 33 C5                        xor rax, rbp
004EB455  48 89 45 68                     mov qword ptr [rbp + 0x68], rax
004EB459  0F B7 72 06                     movzx esi, word ptr [rdx + 6]
004EB45D  4D 8B E9                        mov r13, r9
004EB460  48 03 F2                        add rsi, rdx
004EB463  4C 89 45 20                     mov qword ptr [rbp + 0x20], r8
004EB467  4D 8B C8                        mov r9, r8
004EB46A  48 89 55 18                     mov qword ptr [rbp + 0x18], rdx
004EB46E  44 0F B7 42 04                  movzx r8d, word ptr [rdx + 4]
004EB473  33 FF                           xor edi, edi
004EB475  4C 03 C2                        add r8, rdx
004EB478  0F 57 C0                        xorps xmm0, xmm0
004EB47B  48 8D 46 08                     lea rax, [rsi + 8]
004EB47F  4C 89 45 38                     mov qword ptr [rbp + 0x38], r8
004EB483  48 8D 5E 08                     lea rbx, [rsi + 8]
004EB487  0F 57 C9                        xorps xmm1, xmm1
004EB48A  4C 8B E2                        mov r12, rdx
004EB48D  4C 8B F1                        mov r14, rcx
004EB490  0F 11 45 28                     movups xmmword ptr [rbp + 0x28], xmm0
004EB494  0F 11 4D 08                     movups xmmword ptr [rbp + 8], xmm1
004EB498  49 3B C0                        cmp rax, r8
004EB49B  76 11                           jbe 0x1404eb4ae
004EB49D  48 8B 7D 08                     mov rdi, qword ptr [rbp + 8]
004EB4A1  BE 05 00 00 80                  mov esi, 0x80000005
004EB4A6  45 33 FF                        xor r15d, r15d
004EB4A9  E9 EF 03 00 00                  jmp 0x1404eb89d
004EB4AE  33 C0                           xor eax, eax
004EB4B0  8B CF                           mov ecx, edi
004EB4B2  48 89 06                        mov qword ptr [rsi], rax
004EB4B5  48 85 F6                        test rsi, rsi
004EB4B8  74 0D                           je 0x1404eb4c7
004EB4BA  41 8B 8E 28 03 00 00            mov ecx, dword ptr [r14 + 0x328]
004EB4C1  41 23 4D 00                     and ecx, dword ptr [r13]
004EB4C5  89 0E                           mov dword ptr [rsi], ecx
004EB4C7  C1 E1 04                        shl ecx, 4
004EB4CA  B8 00 10 00 00                  mov eax, 0x1000
004EB4CF  89 0E                           mov dword ptr [rsi], ecx
004EB4D1  41 8B 4D 04                     mov ecx, dword ptr [r13 + 4]
004EB4D5  81 E1 FF 0F 00 00               and ecx, 0xfff
004EB4DB  0F 47 C1                        cmova eax, ecx
004EB4DE  66 89 46 04                     mov word ptr [rsi + 4], ax
004EB4E2  41 8B 45 08                     mov eax, dword ptr [r13 + 8]
004EB4E6  41 39 41 04                     cmp dword ptr [r9 + 4], eax
004EB4EA  0F 85 89 00 00 00               jne 0x1404eb579
004EB4F0  41 8B 45 04                     mov eax, dword ptr [r13 + 4]
004EB4F4  25 FF 0F 00 00                  and eax, 0xfff
004EB4F9  41 39 41 08                     cmp dword ptr [r9 + 8], eax
004EB4FD  75 7A                           jne 0x1404eb579
004EB4FF  41 8B 01                        mov eax, dword ptr [r9]
004EB502  85 C0                           test eax, eax
004EB504  74 73                           je 0x1404eb579
004EB506  48 03 D0                        add rdx, rax
004EB509  8B CE                           mov ecx, esi
004EB50B  2B CA                           sub ecx, edx
004EB50D  48 03 CE                        add rcx, rsi
004EB510  49 3B C8                        cmp rcx, r8
004EB513  76 11                           jbe 0x1404eb526
004EB515  48 8B 7D 08                     mov rdi, qword ptr [rbp + 8]
004EB519  BE 05 00 00 80                  mov esi, 0x80000005
004EB51E  45 33 FF                        xor r15d, r15d
004EB521  E9 77 03 00 00                  jmp 0x1404eb89d
004EB526  0F B6 42 06                     movzx eax, byte ptr [rdx + 6]
004EB52A  48 8D 4A 08                     lea rcx, [rdx + 8]
004EB52E  48 8D 14 C1                     lea rdx, [rcx + rax*8]
004EB532  48 3B CA                        cmp rcx, rdx
004EB535  73 25                           jae 0x1404eb55c
004EB537  8B 06                           mov eax, dword ptr [rsi]
004EB539  39 41 04                        cmp dword ptr [rcx + 4], eax
004EB53C  75 08                           jne 0x1404eb546
004EB53E  41 8B 04 24                     mov eax, dword ptr [r12]
004EB542  39 01                           cmp dword ptr [rcx], eax
004EB544  74 0D                           je 0x1404eb553
004EB546  48 8B 01                        mov rax, qword ptr [rcx]
004EB549  48 89 03                        mov qword ptr [rbx], rax
004EB54C  48 83 C3 08                     add rbx, 8
004EB550  FE 46 06                        inc byte ptr [rsi + 6]
004EB553  48 83 C1 08                     add rcx, 8
004EB557  48 3B CA                        cmp rcx, rdx
004EB55A  72 DB                           jb 0x1404eb537
004EB55C  45 33 FF                        xor r15d, r15d
004EB55F  40 38 7E 06                     cmp byte ptr [rsi + 6], dil
004EB563  75 0B                           jne 0x1404eb570
004EB565  8B F7                           mov esi, edi
004EB567  48 8B 7D 08                     mov rdi, qword ptr [rbp + 8]
004EB56B  E9 2D 03 00 00                  jmp 0x1404eb89d
004EB570  48 8B 7D 08                     mov rdi, qword ptr [rbp + 8]
004EB574  E9 EB 02 00 00                  jmp 0x1404eb864
004EB579  49 8D BE 98 00 00 00            lea rdi, [r14 + 0x98]
004EB580  8B 47 20                        mov eax, dword ptr [rdi + 0x20]
004EB583  4D 8D BE 80 00 00 00            lea r15, [r14 + 0x80]
004EB58A  A8 01                           test al, 1
004EB58C  75 0B                           jne 0x1404eb599
004EB58E  48 8B D7                        mov rdx, rdi
004EB591  49 8B CF                        mov rcx, r15
004EB594  E8 77 2D EC FF                  call 0x1403ae310
004EB599  83 4F 20 01                     or dword ptr [rdi + 0x20], 1
004EB59D  4C 8B C7                        mov r8, rdi
004EB5A0  49 8B 96 F8 02 00 00            mov rdx, qword ptr [r14 + 0x2f8]
004EB5A7  49 8B CF                        mov rcx, r15
004EB5AA  41 8B 45 08                     mov eax, dword ptr [r13 + 8]
004EB5AE  4D 8B E7                        mov r12, r15
004EB5B1  89 42 08                        mov dword ptr [rdx + 8], eax
004EB5B4  41 8B 96 00 03 00 00            mov edx, dword ptr [r14 + 0x300]
004EB5BB  E8 F0 27 EC FF                  call 0x1403addb0
004EB5C0  4C 8B C7                        mov r8, rdi
004EB5C3  48 8D 55 08                     lea rdx, [rbp + 8]
004EB5C7  49 8B CF                        mov rcx, r15
004EB5CA  E8 71 02 F5 FF                  call 0x14043b840
004EB5CF  4C 8B 65 18                     mov r12, qword ptr [rbp + 0x18]
004EB5D3  49 8B 86 78 05 00 00            mov rax, qword ptr [r14 + 0x578]
004EB5DA  48 8B 7D 08                     mov rdi, qword ptr [rbp + 8]
004EB5DE  41 8B 0C 24                     mov ecx, dword ptr [r12]
004EB5E2  44 0F B7 1C 48                  movzx r11d, word ptr [rax + rcx*2]
004EB5E7  41 C1 EB 0D                     shr r11d, 0xd
004EB5EB  45 33 C0                        xor r8d, r8d
004EB5EE  44 89 5D 18                     mov dword ptr [rbp + 0x18], r11d
004EB5F2  45 8B D0                        mov r10d, r8d
004EB5F5  44 89 45 00                     mov dword ptr [rbp], r8d
004EB5F9  0F 1F 80 00 00 00 00            nop dword ptr [rax]
004EB600  48 85 FF                        test rdi, rdi
004EB603  0F 84 C0 01 00 00               je 0x1404eb7c9
004EB609  4C 8B 4D 10                     mov r9, qword ptr [rbp + 0x10]
004EB60D  8B 07                           mov eax, dword ptr [rdi]
004EB60F  49 83 C1 04                     add r9, 4
004EB613  0F B7 C0                        movzx eax, ax
004EB616  48 83 C0 04                     add rax, 4
004EB61A  4C 89 4D 10                     mov qword ptr [rbp + 0x10], r9
004EB61E  48 8D 04 87                     lea rax, [rdi + rax*4]
004EB622  4C 3B C8                        cmp r9, rax
004EB625  72 65                           jb 0x1404eb68c
004EB627  49 8D 47 10                     lea rax, [r15 + 0x10]
004EB62B  4D 85 FF                        test r15, r15
004EB62E  75 03                           jne 0x1404eb633
004EB630  49 8B C0                        mov rax, r8
004EB633  48 8B 00                        mov rax, qword ptr [rax]
004EB636  83 38 FF                        cmp dword ptr [rax], -1
004EB639  74 1A                           je 0x1404eb655
004EB63B  48 8B D7                        mov rdx, rdi
004EB63E  49 8B CF                        mov rcx, r15
004EB641  E8 E2 40 F5 FF                  call 0x14043f728
004EB646  48 83 F8 FF                     cmp rax, -1
004EB64A  0F 85 3F 01 00 00               jne 0x1404eb78f
004EB650  4C 8B C8                        mov r9, rax
004EB653  EB 2C                           jmp 0x1404eb681
004EB655  49 8D 47 10                     lea rax, [r15 + 0x10]
004EB659  4D 85 FF                        test r15, r15
004EB65C  75 03                           jne 0x1404eb661
004EB65E  49 8B C0                        mov rax, r8
004EB661  48 8B 00                        mov rax, qword ptr [rax]
004EB664  83 38 FF                        cmp dword ptr [rax], -1
004EB667  0F 84 1C 01 00 00               je 0x1404eb789
004EB66D  B8 1E 0D 00 00                  mov eax, 0xd1e
004EB672  4C 8D 48 10                     lea r9, [rax + 0x10]
004EB676  48 89 45 08                     mov qword ptr [rbp + 8], rax
004EB67A  4C 89 4D 10                     mov qword ptr [rbp + 0x10], r9
004EB67E  48 8B F8                        mov rdi, rax
004EB681  44 8B 55 00                     mov r10d, dword ptr [rbp]
004EB685  45 33 C0                        xor r8d, r8d
004EB688  44 8B 5D 18                     mov r11d, dword ptr [rbp + 0x18]
004EB68C  4D 85 C9                        test r9, r9
004EB68F  0F 84 34 01 00 00               je 0x1404eb7c9
004EB695  41 8B 8E C8 01 00 00            mov ecx, dword ptr [r14 + 0x1c8]
004EB69C  41 8B 86 CC 01 00 00            mov eax, dword ptr [r14 + 0x1cc]
004EB6A3  45 8B 09                        mov r9d, dword ptr [r9]
004EB6A6  41 8B D1                        mov edx, r9d
004EB6A9  D3 EA                           shr edx, cl
004EB6AB  41 23 C1                        and eax, r9d
004EB6AE  41 0F AF 86 D0 01 00 00         imul eax, dword ptr [r14 + 0x1d0]
004EB6B6  0F BD CA                        bsr ecx, edx
004EB6B9  44 89 45 00                     mov dword ptr [rbp], r8d
004EB6BD  41 B8 01 00 00 00               mov r8d, 1
004EB6C3  41 D3 E0                        shl r8d, cl
004EB6C6  4C 33 C2                        xor r8, rdx
004EB6C9  4D 03 C0                        add r8, r8
004EB6CC  49 8B 8C CE C0 00 00 00         mov rcx, qword ptr [r14 + rcx*8 + 0xc0]
004EB6D4  4A 8B 14 C1                     mov rdx, qword ptr [rcx + r8*8]
004EB6D8  48 03 D0                        add rdx, rax
004EB6DB  41 8B 86 D8 01 00 00            mov eax, dword ptr [r14 + 0x1d8]
004EB6E2  48 03 D0                        add rdx, rax
004EB6E5  49 3B D5                        cmp rdx, r13
004EB6E8  0F 84 B9 00 00 00               je 0x1404eb7a7
004EB6EE  41 8B 45 08                     mov eax, dword ptr [r13 + 8]
004EB6F2  39 42 08                        cmp dword ptr [rdx + 8], eax
004EB6F5  0F 85 CE 00 00 00               jne 0x1404eb7c9
004EB6FB  8B 4A 04                        mov ecx, dword ptr [rdx + 4]
004EB6FE  41 33 4D 04                     xor ecx, dword ptr [r13 + 4]
004EB702  F7 C1 FF 0F 00 00               test ecx, 0xfff
004EB708  0F 85 99 00 00 00               jne 0x1404eb7a7
004EB70E  44 8B 02                        mov r8d, dword ptr [rdx]
004EB711  41 8B 8E 2C 03 00 00            mov ecx, dword ptr [r14 + 0x32c]
004EB718  49 8B 86 78 05 00 00            mov rax, qword ptr [r14 + 0x578]
004EB71F  41 D3 E8                        shr r8d, cl
004EB722  42 0F B7 0C 40                  movzx ecx, word ptr [rax + r8*2]
004EB727  C1 E9 0D                        shr ecx, 0xd
004EB72A  41 3B CB                        cmp ecx, r11d
004EB72D  72 78                           jb 0x1404eb7a7
004EB72F  49 8B 86 20 03 00 00            mov rax, qword ptr [r14 + 0x320]
004EB736  48 8B 80 F0 1C 00 00            mov rax, qword ptr [rax + 0x1cf0]
004EB73D  48 85 C0                        test rax, rax
004EB740  74 10                           je 0x1404eb752
004EB742  48 83 F8 FF                     cmp rax, -1
004EB746  74 5B                           je 0x1404eb7a3
004EB748  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
004EB74C  4C 0F A3 00                     bt qword ptr [rax], r8
004EB750  72 51                           jb 0x1404eb7a3
004EB752  8B 42 04                        mov eax, dword ptr [rdx + 4]
004EB755  25 00 F0 FF FF                  and eax, 0xfffff000
004EB75A  3D 00 F0 EF FF                  cmp eax, 0xffeff000
004EB75F  73 42                           jae 0x1404eb7a3
004EB761  48 8B 7D 08                     mov rdi, qword ptr [rbp + 8]
004EB765  48 8D 4B 08                     lea rcx, [rbx + 8]
004EB769  48 3B 4D 38                     cmp rcx, qword ptr [rbp + 0x38]
004EB76D  77 4D                           ja 0x1404eb7bc
004EB76F  33 C0                           xor eax, eax
004EB771  48 89 03                        mov qword ptr [rbx], rax
004EB774  8B 02                           mov eax, dword ptr [rdx]
004EB776  89 03                           mov dword ptr [rbx], eax
004EB778  8B 42 04                        mov eax, dword ptr [rdx + 4]
004EB77B  C1 E8 0C                        shr eax, 0xc
004EB77E  89 43 04                        mov dword ptr [rbx + 4], eax
004EB781  48 8B D9                        mov rbx, rcx
004EB784  FE 46 06                        inc byte ptr [rsi + 6]
004EB787  EB 1E                           jmp 0x1404eb7a7
004EB789  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
004EB78D  EB 03                           jmp 0x1404eb792
004EB78F  45 33 C0                        xor r8d, r8d
004EB792  48 85 C0                        test rax, rax
004EB795  0F 85 D7 FE FF FF               jne 0x1404eb672
004EB79B  4D 8B C8                        mov r9, r8
004EB79E  E9 DE FE FF FF                  jmp 0x1404eb681
004EB7A3  48 8B 7D 08                     mov rdi, qword ptr [rbp + 8]
004EB7A7  41 FF C2                        inc r10d
004EB7AA  44 89 55 00                     mov dword ptr [rbp], r10d
004EB7AE  41 83 FA 10                     cmp r10d, 0x10
004EB7B2  73 15                           jae 0x1404eb7c9
004EB7B4  45 33 C0                        xor r8d, r8d
004EB7B7  E9 44 FE FF FF                  jmp 0x1404eb600
004EB7BC  BE 05 00 00 80                  mov esi, 0x80000005
004EB7C1  45 33 FF                        xor r15d, r15d
004EB7C4  E9 D4 00 00 00                  jmp 0x1404eb89d
004EB7C9  0F B6 4E 06                     movzx ecx, byte ptr [rsi + 6]
004EB7CD  45 33 FF                        xor r15d, r15d
004EB7D0  84 C9                           test cl, cl
004EB7D2  0F 84 C2 00 00 00               je 0x1404eb89a
004EB7D8  8B C1                           mov eax, ecx
004EB7DA  48 F7 D8                        neg rax
004EB7DD  48 8D 1C C3                     lea rbx, [rbx + rax*8]
004EB7E1  80 F9 01                        cmp cl, 1
004EB7E4  76 2F                           jbe 0x1404eb815
004EB7E6  41 8B 04 24                     mov eax, dword ptr [r12]
004EB7EA  4C 8D 0D 4F 59 F6 FF            lea r9, [rip - 0x9a6b1]
004EB7F1  89 45 28                        mov dword ptr [rbp + 0x28], eax
004EB7F4  45 8D 47 08                     lea r8d, [r15 + 8]
004EB7F8  48 8D 45 28                     lea rax, [rbp + 0x28]
004EB7FC  44 89 7D 2C                     mov dword ptr [rbp + 0x2c], r15d
004EB800  4C 89 75 30                     mov qword ptr [rbp + 0x30], r14
004EB804  48 8B CB                        mov rcx, rbx
004EB807  0F B6 56 06                     movzx edx, byte ptr [rsi + 6]
004EB80B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
004EB810  E8 BB 55 01 00                  call 0x140500dd0
004EB815  0F B6 46 06                     movzx eax, byte ptr [rsi + 6]
004EB819  4C 8D 0C C3                     lea r9, [rbx + rax*8]
004EB81D  49 3B D9                        cmp rbx, r9
004EB820  73 3E                           jae 0x1404eb860
004EB822  8B 13                           mov edx, dword ptr [rbx]
004EB824  4C 8D 43 04                     lea r8, [rbx + 4]
004EB828  33 C0                           xor eax, eax
004EB82A  48 89 03                        mov qword ptr [rbx], rax
004EB82D  4D 85 C0                        test r8, r8
004EB830  74 0C                           je 0x1404eb83e
004EB832  41 8B 86 28 03 00 00            mov eax, dword ptr [r14 + 0x328]
004EB839  23 C2                           and eax, edx
004EB83B  41 89 00                        mov dword ptr [r8], eax
004EB83E  48 85 DB                        test rbx, rbx
004EB841  74 0B                           je 0x1404eb84e
004EB843  41 8B 8E 2C 03 00 00            mov ecx, dword ptr [r14 + 0x32c]
004EB84A  D3 EA                           shr edx, cl
004EB84C  89 13                           mov dword ptr [rbx], edx
004EB84E  41 8B 00                        mov eax, dword ptr [r8]
004EB851  48 83 C3 08                     add rbx, 8
004EB855  C1 E0 04                        shl eax, 4
004EB858  41 89 00                        mov dword ptr [r8], eax
004EB85B  49 3B D9                        cmp rbx, r9
004EB85E  72 C2                           jb 0x1404eb822
004EB860  4C 8B 4D 20                     mov r9, qword ptr [rbp + 0x20]
004EB864  41 0F B7 44 24 06               movzx eax, word ptr [r12 + 6]
004EB86A  41 89 01                        mov dword ptr [r9], eax
004EB86D  41 8B 45 08                     mov eax, dword ptr [r13 + 8]
004EB871  41 89 41 04                     mov dword ptr [r9 + 4], eax
004EB875  41 8B 45 04                     mov eax, dword ptr [r13 + 4]
004EB879  25 FF 0F 00 00                  and eax, 0xfff
004EB87E  41 89 41 08                     mov dword ptr [r9 + 8], eax
004EB882  0F B6 46 06                     movzx eax, byte ptr [rsi + 6]
004EB886  66 FF C0                        inc ax
004EB889  66 C1 E0 03                     shl ax, 3
004EB88D  66 41 2B C4                     sub ax, r12w
004EB891  66 03 C6                        add ax, si
004EB894  66 41 89 44 24 06               mov word ptr [r12 + 6], ax
004EB89A  41 8B F7                        mov esi, r15d
004EB89D  49 81 C6 80 00 00 00            add r14, 0x80
004EB8A4  49 8D 46 10                     lea rax, [r14 + 0x10]
004EB8A8  49 0F 44 C7                     cmove rax, r15
004EB8AC  48 8B 00                        mov rax, qword ptr [rax]
004EB8AF  83 38 FF                        cmp dword ptr [rax], -1
004EB8B2  0F 84 BB 00 00 00               je 0x1404eb973
004EB8B8  48 85 FF                        test rdi, rdi
004EB8BB  0F 84 B2 00 00 00               je 0x1404eb973
004EB8C1  49 8B 06                        mov rax, qword ptr [r14]
004EB8C4  48 3B F8                        cmp rdi, rax
004EB8C7  0F 84 A6 00 00 00               je 0x1404eb973
004EB8CD  48 85 C0                        test rax, rax
004EB8D0  74 05                           je 0x1404eb8d7
004EB8D2  44 0F B6 78 02                  movzx r15d, byte ptr [rax + 2]
004EB8D7  41 8B C7                        mov eax, r15d
004EB8DA  48 C1 E0 04                     shl rax, 4
004EB8DE  48 8D 48 0F                     lea rcx, [rax + 0xf]
004EB8E2  48 3B C8                        cmp rcx, rax
004EB8E5  77 0A                           ja 0x1404eb8f1
004EB8E7  48 B9 F0 FF FF FF FF FF FF 0F   movabs rcx, 0xffffffffffffff0
004EB8F1  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
004EB8F5  48 8B C1                        mov rax, rcx
004EB8F8  E8 63 F0 1C 00                  call 0x1406ba960
004EB8FD  8B 57 10                        mov edx, dword ptr [rdi + 0x10]
004EB900  4C 8D 45 40                     lea r8, [rbp + 0x40]
004EB904  48 2B E1                        sub rsp, rcx
004EB907  48 C7 45 60 01 00 00 00         mov qword ptr [rbp + 0x60], 1
004EB90F  0F 57 C0                        xorps xmm0, xmm0
004EB912  44 89 7D 5C                     mov dword ptr [rbp + 0x5c], r15d
004EB916  33 C0                           xor eax, eax
004EB918  49 8B CE                        mov rcx, r14
004EB91B  F3 0F 7F 45 48                  movdqu xmmword ptr [rbp + 0x48], xmm0
004EB920  48 8D 5C 24 30                  lea rbx, [rsp + 0x30]
004EB925  89 45 58                        mov dword ptr [rbp + 0x58], eax
004EB928  48 89 5D 40                     mov qword ptr [rbp + 0x40], rbx
004EB92C  E8 7F 24 EC FF                  call 0x1403addb0
004EB931  41 8D 57 FE                     lea edx, [r15 - 2]
004EB935  49 8B CE                        mov rcx, r14
004EB938  48 03 D2                        add rdx, rdx
004EB93B  48 8B 7C D3 08                  mov rdi, qword ptr [rbx + rdx*8 + 8]
004EB940  48 8B 1C D3                     mov rbx, qword ptr [rbx + rdx*8]
004EB944  48 8D 55 40                     lea rdx, [rbp + 0x40]
004EB948  E8 C3 29 EC FF                  call 0x1403ae310
004EB94D  4C 8D 43 08                     lea r8, [rbx + 8]
004EB951  4C 8D 4B 10                     lea r9, [rbx + 0x10]
004EB955  49 3B F9                        cmp rdi, r9
004EB958  48 8D 57 F8                     lea rdx, [rdi - 8]
004EB95C  49 0F 46 D0                     cmovbe rdx, r8
004EB960  4D 8B 46 10                     mov r8, qword ptr [r14 + 0x10]
004EB964  41 83 38 FF                     cmp dword ptr [r8], -1
004EB968  74 09                           je 0x1404eb973
004EB96A  49 8D 4E 10                     lea rcx, [r14 + 0x10]
004EB96E  E8 FD E0 EB FF                  call 0x1403a9a70
004EB973  8B C6                           mov eax, esi
004EB975  48 8B 4D 68                     mov rcx, qword ptr [rbp + 0x68]
004EB979  48 33 CD                        xor rcx, rbp
004EB97C  E8 BF 0C 1C 00                  call 0x1406ac640
004EB981  48 8B 9D A0 00 00 00            mov rbx, qword ptr [rbp + 0xa0]
004EB988  48 8B B5 A8 00 00 00            mov rsi, qword ptr [rbp + 0xa8]
004EB98F  48 8B BD B0 00 00 00            mov rdi, qword ptr [rbp + 0xb0]
004EB996  48 8D 65 70                     lea rsp, [rbp + 0x70]
004EB99A  41 5F                           pop r15
004EB99C  41 5E                           pop r14
004EB99E  41 5D                           pop r13
004EB9A0  41 5C                           pop r12
004EB9A2  5D                              pop rbp
004EB9A3  C3                              ret
004EB9A4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ST_STORE_SM_TRAITS___StDmCombineBufferAddEntry(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m3C;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m6C;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (160);
    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p18 = v_rdi;
    result = (*(unsigned __int64 *)(v_rip + 9564910)) ^ (v_stack_m98);
    v_stack_m30 = result;
    v_rsi = (*(unsigned __int16 *)(a2 + 6)) + (a2);
    v_stack_m78 = a3;
    v_stack_m80 = a2;
    v_rdi = 0;
    a3 = (*(unsigned __int16 *)(a2 + 4)) + (a2);
    v_stack_m60 = a3;
    v_stack_m70 = v_xmm0;
    v_stack_m90 = v_xmm1;
    if ((v_rsi + 8) <= a3) goto loc_004EB4AE;
    v_r15 = 0;
    goto loc_004EB89D;
loc_004EB4AE:
    result = 0;
    *(unsigned __int64 *)((unsigned int)(0x80000005ULL)) = 0;
    if ((unsigned int)(0x80000005ULL) != 0) {
        a1 = *(unsigned int *)(a1 + 808);
        a1 = (unsigned int)((a1) & (*(unsigned int *)(a4)));
        *(unsigned int *)((unsigned int)(0x80000005ULL)) = (unsigned int)(a1);
    }
    a1 = (unsigned int)((a1) << (4));
    *(unsigned int *)((unsigned int)(0x80000005ULL)) = (unsigned int)(a1);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a4 + 4))) & (0xFFFULL));
    result = (unsigned int)(0x1000ULL);
    if (condition_is_above) { result = (unsigned int)(a1); }
    *(unsigned __int16 *)((unsigned int)(0x80000005ULL) + 4) = (unsigned __int16)(result);
    if ((*(unsigned int *)(a3 + 4)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 8))))) goto loc_004EB579;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a4 + 4))) & (0xFFFULL));
    if ((*(unsigned int *)(a3 + 8)) != ((unsigned int)(result))) goto loc_004EB579;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a3))) == 0) goto loc_004EB579;
    a2 = (a2) + ((unsigned int)(*(unsigned int *)(a3)));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x80000005ULL)))) - ((unsigned int)(a2)));
    a1 = (a1) + ((unsigned int)(0x80000005ULL));
    if (a1 <= a3) goto loc_004EB526;
    v_r15 = 0;
    goto loc_004EB89D;
loc_004EB526:
    if ((a2 + 8) >= (a2 + 8 + *(unsigned __int8 *)(a2 + 6) * 8)) goto loc_004EB55C;
loc_004EB537:
    if ((*(unsigned int *)(a2 + 8 + 4)) != ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(0x80000005ULL)))))) goto loc_004EB546;
    result = (unsigned int)(*(unsigned int *)(a2));
    v_rbx = v_rsi + 8;
    if ((*(unsigned int *)(a2 + 8)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a2))))) {
        result = *(unsigned __int64 *)(a2 + 8);
        *(unsigned __int64 *)(v_rsi + 8) = result;
        v_rbx = (v_rsi + 8) + (8);
    }
    a1 = (a2 + 8) + (8);
    if (a1 < (a2 + 8 + *(unsigned __int8 *)(a2 + 6) * 8)) goto loc_004EB537;
loc_004EB55C:
    v_r15 = 0;
    if ((*(unsigned __int8 *)((unsigned int)(0x80000005ULL) + 6)) != ((unsigned __int8)(v_stack_m90))) goto loc_004EB570;
    goto loc_004EB89D;
loc_004EB570:
    goto loc_004EB864;
loc_004EB579:
    result = (unsigned int)(*(unsigned int *)(a1 + 152 + 32));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 152 + 32)))) & (1)) == 0) {
        a2 = a1 + 152;
        a1 = a1 + 128;
        result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_HASH_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_HAS(a1, a2, a3, a3);
    }
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 760) + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 8)));
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_HASH_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_HAS(a1 + 128, (unsigned int)(*(unsigned int *)(a1 + 768)), a1 + 152, a3);
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_HASH_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_HAS(a1 + 128, v_stack_m90, a1 + 152, a3);
    v_r11 = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 1400) + (unsigned int)(*(unsigned int *)(v_stack_m80)) * 2)) >> (13));
    a3 = 0;
    v_stack_m80 = (unsigned int)(v_r11);
    v_stack_m98 = 0;
loc_004EB600:
    if (v_stack_m90 == 0) goto loc_004EB7C9;
    a4 = (v_stack_m88) + (4);
    result = ((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_m90)))) + (4);
    v_stack_m88 = a4;
    if (a4 < (v_stack_m90 + result * 4)) goto loc_004EB68C;
    result = a1 + 128 + 16;
    if (a1 + 128 == 0) {
        result = 0;
    }
    if ((*(unsigned int *)(*(unsigned __int64 *)(result))) == -1) goto loc_004EB655;
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_HASH_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_HAS(a1 + 128, v_stack_m90, a3, a4);
    if (result != -1) goto loc_004EB78F;
    goto loc_004EB681;
loc_004EB655:
    result = a1 + 128 + 16;
    if (a1 + 128 == 0) {
        result = 0;
    }
    if ((*(unsigned int *)(*(unsigned __int64 *)(result))) == -1) goto loc_004EB789;
loc_004EB672:
    v_stack_m90 = (unsigned int)(0xD1EULL);
    v_stack_m88 = (unsigned int)(0xD1EULL) + 16;
loc_004EB681:
    a3 = 0;
loc_004EB68C:
    if ((unsigned int)(0xD1EULL) + 16 == 0) goto loc_004EB7C9;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(0xD1EULL) + 16))))) >> ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 456)))));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 460))) & ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(0xD1EULL) + 16)))));
    result = (unsigned int)((result) * (*(unsigned int *)(a1 + 464)));
    v_stack_m98 = 0;
    a3 = (unsigned int)((1) << ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 456)))));
    a3 = (a3) ^ (a2);
    a3 = (a3) + (a3);
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + (unsigned int)(*(unsigned int *)(a1 + 456)) * 8 + 192) + a3 * 8)) + (result);
    a2 = (a2) + ((unsigned int)(*(unsigned int *)(a1 + 472)));
    if (a2 == a4) goto loc_004EB7A7;
    if ((*(unsigned int *)(a2 + 8)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 8))))) goto loc_004EB7C9;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 4))) ^ (*(unsigned int *)(a4 + 4)));
    if ((((unsigned int)(a1)) & (0xFFFULL)) != 0) goto loc_004EB7A7;
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2))) >> ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 812)))));
    a1 = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 1400) + a3 * 2)) >> (13));
    if (((unsigned int)(a1)) < ((unsigned int)((unsigned int)(v_stack_m80)))) goto loc_004EB7A7;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 800) + 7408) == 0) goto loc_004EB752;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 800) + 7408)) == -1) goto loc_004EB7A3;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 800) + 7408)) < -1) goto loc_004EB7A3;
loc_004EB752:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 4))) & (0xFFFFF000ULL));
    if (((unsigned int)(result)) >= 0xFFEFF000ULL) goto loc_004EB7A3;
    if ((v_rbx + 8) > v_stack_m60) goto loc_004EB7BC;
    result = 0;
    *(unsigned __int64 *)(v_rbx) = 0;
    *(unsigned int *)(v_rbx) = (unsigned int)((unsigned int)(*(unsigned int *)(a2)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 4))) >> (12));
    *(unsigned int *)(v_rbx + 4) = (unsigned int)(result);
    goto loc_004EB7A7;
loc_004EB789:
    goto loc_004EB792;
loc_004EB78F:
    a3 = 0;
loc_004EB792:
    if (*(unsigned __int64 *)(v_stack_m90 + 8) != 0) goto loc_004EB672;
    goto loc_004EB681;
loc_004EB7A3:
loc_004EB7A7:
    v_r10 = (unsigned int)(((unsigned int)(v_stack_m98)) + 1);
    v_stack_m98 = (unsigned int)(v_r10);
    if (((unsigned int)(v_r10)) >= 16) goto loc_004EB7C9;
    a3 = 0;
    goto loc_004EB600;
loc_004EB7BC:
    v_r15 = 0;
    goto loc_004EB89D;
loc_004EB7C9:
    v_r15 = 0;
    if ((unsigned __int8)(*(unsigned __int8 *)((unsigned int)(0x80000005ULL) + 6)) == 0) goto loc_004EB89A;
    result = -((unsigned int)((unsigned int)(*(unsigned __int8 *)((unsigned int)(0x80000005ULL) + 6))));
    if (((unsigned __int8)(*(unsigned __int8 *)((unsigned int)(0x80000005ULL) + 6))) >= = 1) {
        result = *(unsigned int *)(v_stack_m80);
        a4 = v_rip - 632497;
        v_stack_m70 = (unsigned int)(result);
        a3 = v_r15 + 8;
        result = v_stack_m70;
        v_stack_m6C = 0;
        v_stack_m68 = a1;
        a1 = v_rbx + 8 + result * 8;
        a2 = *(unsigned __int8 *)((unsigned int)(0x80000005ULL) + 6);
        v_stack_mA8 = result;
        result = qsort_s(a1, a2, a3, a4);
    }
    if ((v_rbx + 8 + result * 8) >= (v_rbx + 8 + result * 8 + *(unsigned __int8 *)((unsigned int)(0x80000005ULL) + 6) * 8)) goto loc_004EB860;
loc_004EB822:
    result = 0;
    *(unsigned __int64 *)(v_rbx + 8 + result * 8) = 0;
    if (v_rbx + 8 + result * 8 + 4 != 0) {
        result = *(unsigned int *)(a1 + 808);
        result = (unsigned int)((result) & ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 8 + result * 8)))));
        *(unsigned int *)(v_rbx + 8 + result * 8 + 4) = (unsigned int)(result);
    }
    if (v_rbx + 8 + result * 8 != 0) {
        a1 = *(unsigned int *)(a1 + 812);
        a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 8 + result * 8))) >> ((unsigned __int8)(a1)));
        *(unsigned int *)(v_rbx + 8 + result * 8) = (unsigned int)(a2);
    }
    v_rbx = (v_rbx + 8 + result * 8) + (8);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 8 + result * 8 + 4))) << (4));
    *(unsigned int *)(v_rbx + 8 + result * 8 + 4) = (unsigned int)(result);
    if (v_rbx < (v_rbx + 8 + result * 8 + *(unsigned __int8 *)((unsigned int)(0x80000005ULL) + 6) * 8)) goto loc_004EB822;
loc_004EB860:
loc_004EB864:
    *(unsigned int *)(v_stack_m78) = (unsigned int)(*(unsigned __int16 *)(v_stack_m80 + 6));
    *(unsigned int *)(v_stack_m78 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 8)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a4 + 4))) & (0xFFFULL));
    *(unsigned int *)(v_stack_m78 + 8) = (unsigned int)(result);
    result = (unsigned __int16)((*(unsigned __int8 *)((unsigned int)(0x80000005ULL) + 6)) + 1);
    result = (unsigned __int16)((result) << (3));
    result = (unsigned __int16)((result) - ((unsigned __int16)(v_stack_m80)));
    result = (unsigned __int16)((result) + ((unsigned __int16)((unsigned int)(0x80000005ULL))));
    *(unsigned __int16 *)(v_stack_m80 + 6) = (unsigned __int16)(result);
loc_004EB89A:
loc_004EB89D:
    v_r14 = (a1) + (128);
    result = v_r14 + 16;
    if (condition_is_equal) { result = 0; }
    if ((*(unsigned int *)(*(unsigned __int64 *)(result))) == -1) goto loc_004EB973;
    if (v_stack_m90 == 0) goto loc_004EB973;
    if (v_stack_m90 == (*(unsigned __int64 *)(v_r14))) goto loc_004EB973;
    if (*(unsigned __int64 *)(v_r14) != 0) {
        v_r15 = *(unsigned __int8 *)(*(unsigned __int64 *)(v_r14) + 2);
    }
    result = ((unsigned int)((unsigned int)(v_r15))) << (4);
    if ((result + 15) <= result) {
    }
    a1 = (result + 15) & (-16);
    result = _chkstk(a1, a2, v_rbx + 8 + result * 8 + 4, v_stack_m78);
    v_rsp = (v_rsp) - (a1);
    v_stack_m38 = 1;
    v_stack_m3C = (unsigned int)(v_r15);
    result = 0;
    v_stack_m50 = v_xmm0;
    v_stack_m40 = 0;
    v_stack_m58 = v_stack_m98;
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_HASH_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_HAS(v_r14, (unsigned int)(*(unsigned int *)(v_stack_m90 + 16)), v_stack_m58, v_stack_m78);
    a2 = (v_r15 - 2) + (v_r15 - 2);
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_HASH_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_HAS(v_r14, v_stack_m58, v_stack_m58, v_stack_m78);
    a2 = *(unsigned __int64 *)(v_stack_m98 + a2 * 8 + 8) - 8;
    if ((*(unsigned __int64 *)(v_stack_m98 + a2 * 8 + 8)) <= (*(unsigned __int64 *)(v_stack_m98 + a2 * 8) + 16)) { a2 = *(unsigned __int64 *)(v_stack_m98 + a2 * 8) + 8; }
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_r14 + 16))) != -1) {
        a1 = v_r14 + 16;
        result = NP_CONTEXT__NpLeafDerefInternal(a1, a2, *(unsigned __int64 *)(v_r14 + 16), *(unsigned __int64 *)(v_stack_m98 + a2 * 8) + 16);
    }
    a1 = (v_stack_m30) ^ (v_stack_m98);
    result = _security_check_cookie(a1, a2, *(unsigned __int64 *)(v_r14 + 16), *(unsigned __int64 *)(v_stack_m98 + a2 * 8) + 16);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ST_STORE_SM_TRAITS___StDmCombineBufferAddEntry(void *Arg1, void *Arg2, void *Arg3, void *Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m3C;
    uint32_t v_stack_m40;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m6C;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (160);
    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p18 = local_rdi;
    result = (*(uint64_t *)(v_rip + 0x91F2EE)) ^ (v_stack_m98);
    v_stack_m30 = result;
    local_rsi = (*(uint16_t *)(arg2 + 0x6)) + (Arg2);
    v_stack_m78 = Arg3;
    v_stack_m80 = Arg2;
    local_rdi = 0;
    Arg3 = (*(uint16_t *)(arg2 + 0x4)) + (Arg2);
    v_stack_m60 = Arg3;
    v_stack_m70 = v_xmm0;
    v_stack_m90 = v_xmm1;
    if ((local_rsi + 8) <= Arg3) goto loc_004EB4AE;
    local_r15 = 0;
    goto loc_004EB89D;
loc_004EB4AE:
    result = 0;
    *(uint64_t *)((uint32_t)(0x80000005ULL)) = 0;
    if ((uint32_t)(0x80000005ULL) != 0) {
        Arg1 = *(uint32_t *)(arg1 + 0x328);
        Arg1 = (uint32_t)((Arg1) & (*(uint32_t *)(arg4)));
        *(uint32_t *)((uint32_t)(0x80000005ULL)) = (uint32_t)(Arg1);
    }
    Arg1 = (uint32_t)((Arg1) << (4));
    *(uint32_t *)((uint32_t)(0x80000005ULL)) = (uint32_t)(Arg1);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg4 + 0x4))) & (0xFFFULL));
    result = (uint32_t)(0x1000ULL);
    if (condition_is_above) { result = (uint32_t)(Arg1); }
    *(uint16_t *)((uint32_t)(0x80000005ULL) + 0x4) = (uint16_t)(result);
    if ((*(uint32_t *)(arg3 + 0x4)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x8))))) goto loc_004EB579;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg4 + 0x4))) & (0xFFFULL));
    if ((*(uint32_t *)(arg3 + 0x8)) != ((uint32_t)(result))) goto loc_004EB579;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg3))) == 0) goto loc_004EB579;
    Arg2 = (Arg2) + ((uint32_t)(*(uint32_t *)(arg3)));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x80000005ULL)))) - ((uint32_t)(Arg2)));
    Arg1 = (Arg1) + ((uint32_t)(0x80000005ULL));
    if (Arg1 <= Arg3) goto loc_004EB526;
    local_r15 = 0;
    goto loc_004EB89D;
loc_004EB526:
    if ((Arg2 + 8) >= (Arg2 + 8 + *(uint8_t *)(arg2 + 0x6) * 8)) goto loc_004EB55C;
loc_004EB537:
    if ((*(uint32_t *)(arg2 + 0x8 + 0x4)) != ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(0x80000005ULL)))))) goto loc_004EB546;
    result = (uint32_t)(*(uint32_t *)(arg2));
    local_rbx = local_rsi + 8;
    if ((*(uint32_t *)(arg2 + 0x8)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg2))))) {
        result = *(uint64_t *)(arg2 + 0x8);
        *(uint64_t *)(local_rsi + 0x8) = result;
        local_rbx = (local_rsi + 8) + (8);
    }
    Arg1 = (Arg2 + 8) + (8);
    if (Arg1 < (Arg2 + 8 + *(uint8_t *)(arg2 + 0x6) * 8)) goto loc_004EB537;
loc_004EB55C:
    local_r15 = 0;
    if ((*(uint8_t *)((uint32_t)(0x80000005ULL) + 0x6)) != ((uint8_t)(v_stack_m90))) goto loc_004EB570;
    goto loc_004EB89D;
loc_004EB570:
    goto loc_004EB864;
loc_004EB579:
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x98 + 0x20));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x98 + 0x20)))) & (1)) == 0) {
        Arg2 = Arg1 + 152;
        Arg1 = Arg1 + 128;
        result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_HASH_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_HAS(Arg1, Arg2, Arg3, Arg3);
    }
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x2F8) + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x8)));
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_HASH_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_HAS(Arg1 + 128, (uint32_t)(*(uint32_t *)(arg1 + 0x300)), Arg1 + 152, Arg3);
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_HASH_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_HAS(Arg1 + 128, v_stack_m90, Arg1 + 152, Arg3);
    local_r11 = (uint32_t)((*(uint16_t *)(*(uint64_t *)(arg1 + 0x578) + (uint32_t)(*(uint32_t *)(v_stack_m80)) * 2)) >> (13));
    Arg3 = 0;
    v_stack_m80 = (uint32_t)(local_r11);
    v_stack_m98 = 0;
loc_004EB600:
    if (v_stack_m90 == 0) goto loc_004EB7C9;
    Arg4 = (v_stack_m88) + (4);
    result = ((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_m90)))) + (4);
    v_stack_m88 = Arg4;
    if (Arg4 < (v_stack_m90 + result * 4)) goto loc_004EB68C;
    result = Arg1 + 128 + 16;
    if (Arg1 + 128 == 0) {
        result = 0;
    }
    if ((*(uint32_t *)(*(uint64_t *)(result))) == -1) goto loc_004EB655;
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_HASH_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_HAS(Arg1 + 128, v_stack_m90, Arg3, Arg4);
    if (result != -1) goto loc_004EB78F;
    goto loc_004EB681;
loc_004EB655:
    result = Arg1 + 128 + 16;
    if (Arg1 + 128 == 0) {
        result = 0;
    }
    if ((*(uint32_t *)(*(uint64_t *)(result))) == -1) goto loc_004EB789;
loc_004EB672:
    v_stack_m90 = (uint32_t)(0xD1EULL);
    v_stack_m88 = (uint32_t)(0xD1EULL) + 16;
loc_004EB681:
    Arg3 = 0;
loc_004EB68C:
    if ((uint32_t)(0xD1EULL) + 16 == 0) goto loc_004EB7C9;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(0xD1EULL) + 0x10))))) >> ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1C8)))));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x1CC))) & ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(0xD1EULL) + 0x10)))));
    result = (uint32_t)((result) * (*(uint32_t *)(arg1 + 0x1D0)));
    v_stack_m98 = 0;
    Arg3 = (uint32_t)((1) << ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1C8)))));
    Arg3 = (Arg3) ^ (Arg2);
    Arg3 = (Arg3) + (Arg3);
    Arg2 = (*(uint64_t *)(*(uint64_t *)(arg1 + (uint32_t)(*(uint32_t *)(arg1 + 0x1C8)) * 8 + 0xC0) + arg3 * 8)) + (result);
    Arg2 = (Arg2) + ((uint32_t)(*(uint32_t *)(arg1 + 0x1D8)));
    if (Arg2 == Arg4) goto loc_004EB7A7;
    if ((*(uint32_t *)(arg2 + 0x8)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x8))))) goto loc_004EB7C9;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x4))) ^ (*(uint32_t *)(arg4 + 0x4)));
    if ((((uint32_t)(Arg1)) & (0xFFFULL)) != 0) goto loc_004EB7A7;
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2))) >> ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x32C)))));
    Arg1 = (uint32_t)((*(uint16_t *)(*(uint64_t *)(arg1 + 0x578) + arg3 * 2)) >> (13));
    if (((uint32_t)(Arg1)) < ((uint32_t)((uint32_t)(v_stack_m80)))) goto loc_004EB7A7;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x320) + 0x1CF0) == 0) goto loc_004EB752;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x320) + 0x1CF0)) == -1) goto loc_004EB7A3;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x320) + 0x1CF0)) < -1) goto loc_004EB7A3;
loc_004EB752:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x4))) & (0xFFFFF000ULL));
    if (((uint32_t)(result)) >= 0xFFEFF000ULL) goto loc_004EB7A3;
    if ((local_rbx + 8) > v_stack_m60) goto loc_004EB7BC;
    result = 0;
    *(uint64_t *)(local_rbx) = 0;
    *(uint32_t *)(local_rbx) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x4))) >> (12));
    *(uint32_t *)(local_rbx + 0x4) = (uint32_t)(result);
    goto loc_004EB7A7;
loc_004EB789:
    goto loc_004EB792;
loc_004EB78F:
    Arg3 = 0;
loc_004EB792:
    if (*(uint64_t *)(v_stack_m90 + 0x8) != 0) goto loc_004EB672;
    goto loc_004EB681;
loc_004EB7A3:
loc_004EB7A7:
    local_r10 = (uint32_t)(((uint32_t)(v_stack_m98)) + 1);
    v_stack_m98 = (uint32_t)(local_r10);
    if (((uint32_t)(local_r10)) >= 16) goto loc_004EB7C9;
    Arg3 = 0;
    goto loc_004EB600;
loc_004EB7BC:
    local_r15 = 0;
    goto loc_004EB89D;
loc_004EB7C9:
    local_r15 = 0;
    if ((uint8_t)(*(uint8_t *)((uint32_t)(0x80000005ULL) + 0x6)) == 0) goto loc_004EB89A;
    result = -((uint32_t)((uint32_t)(*(uint8_t *)((uint32_t)(0x80000005ULL) + 0x6))));
    if (((uint8_t)(*(uint8_t *)((uint32_t)(0x80000005ULL) + 0x6))) >= = 1) {
        result = *(uint32_t *)(v_stack_m80);
        Arg4 = v_rip - 632497;
        v_stack_m70 = (uint32_t)(result);
        Arg3 = local_r15 + 8;
        result = v_stack_m70;
        v_stack_m6C = 0;
        v_stack_m68 = Arg1;
        Arg1 = local_rbx + 8 + result * 8;
        Arg2 = *(uint8_t *)((uint32_t)(0x80000005ULL) + 0x6);
        v_stack_mA8 = result;
        result = qsort_s(Arg1, Arg2, Arg3, Arg4);
    }
    if ((local_rbx + 8 + result * 8) >= (local_rbx + 8 + result * 8 + *(uint8_t *)((uint32_t)(0x80000005ULL) + 0x6) * 8)) goto loc_004EB860;
loc_004EB822:
    result = 0;
    *(uint64_t *)(local_rbx + 0x8 + result * 8) = 0;
    if (local_rbx + 8 + result * 8 + 4 != 0) {
        result = *(uint32_t *)(arg1 + 0x328);
        result = (uint32_t)((result) & ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x8 + result * 8)))));
        *(uint32_t *)(local_rbx + 0x8 + result * 8 + 0x4) = (uint32_t)(result);
    }
    if (local_rbx + 8 + result * 8 != 0) {
        Arg1 = *(uint32_t *)(arg1 + 0x32C);
        Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0x8 + result * 8))) >> ((uint8_t)(Arg1)));
        *(uint32_t *)(local_rbx + 0x8 + result * 8) = (uint32_t)(Arg2);
    }
    local_rbx = (local_rbx + 8 + result * 8) + (8);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0x8 + result * 8 + 0x4))) << (4));
    *(uint32_t *)(local_rbx + 0x8 + result * 8 + 0x4) = (uint32_t)(result);
    if (local_rbx < (local_rbx + 8 + result * 8 + *(uint8_t *)((uint32_t)(0x80000005ULL) + 0x6) * 8)) goto loc_004EB822;
loc_004EB860:
loc_004EB864:
    *(uint32_t *)(v_stack_m78) = (uint32_t)(*(uint16_t *)(v_stack_m80 + 0x6));
    *(uint32_t *)(v_stack_m78 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x8)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg4 + 0x4))) & (0xFFFULL));
    *(uint32_t *)(v_stack_m78 + 0x8) = (uint32_t)(result);
    result = (uint16_t)((*(uint8_t *)((uint32_t)(0x80000005ULL) + 0x6)) + 1);
    result = (uint16_t)((result) << (3));
    result = (uint16_t)((result) - ((uint16_t)(v_stack_m80)));
    result = (uint16_t)((result) + ((uint16_t)((uint32_t)(0x80000005ULL))));
    *(uint16_t *)(v_stack_m80 + 0x6) = (uint16_t)(result);
loc_004EB89A:
loc_004EB89D:
    local_r14 = (Arg1) + (128);
    result = local_r14 + 16;
    if (condition_is_equal) { result = 0; }
    if ((*(uint32_t *)(*(uint64_t *)(result))) == -1) goto loc_004EB973;
    if (v_stack_m90 == 0) goto loc_004EB973;
    if (v_stack_m90 == (*(uint64_t *)(local_r14))) goto loc_004EB973;
    if (*(uint64_t *)(local_r14) != 0) {
        local_r15 = *(uint8_t *)(*(uint64_t *)(local_r14) + 0x2);
    }
    result = ((uint32_t)((uint32_t)(local_r15))) << (4);
    if ((result + 15) <= result) {
    }
    Arg1 = (result + 15) & (-16);
    result = _chkstk(Arg1, Arg2, local_rbx + 8 + result * 8 + 4, v_stack_m78);
    local_rsp = (local_rsp) - (Arg1);
    v_stack_m38 = 1;
    v_stack_m3C = (uint32_t)(local_r15);
    result = 0;
    v_stack_m50 = v_xmm0;
    v_stack_m40 = 0;
    v_stack_m58 = v_stack_m98;
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_HASH_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_HAS(local_r14, (uint32_t)(*(uint32_t *)(v_stack_m90 + 0x10)), v_stack_m58, v_stack_m78);
    Arg2 = (local_r15 - 2) + (local_r15 - 2);
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_HASH_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_HAS(local_r14, v_stack_m58, v_stack_m58, v_stack_m78);
    Arg2 = *(uint64_t *)(v_stack_m98 + arg2 * 8 + 0x8) - 8;
    if ((*(uint64_t *)(v_stack_m98 + arg2 * 8 + 0x8)) <= (*(uint64_t *)(v_stack_m98 + arg2 * 8) + 16)) { Arg2 = *(uint64_t *)(v_stack_m98 + arg2 * 8) + 8; }
    if ((*(uint32_t *)(*(uint64_t *)(local_r14 + 0x10))) != -1) {
        Arg1 = local_r14 + 16;
        result = NP_CONTEXT__NpLeafDerefInternal(Arg1, Arg2, *(uint64_t *)(local_r14 + 0x10), *(uint64_t *)(v_stack_m98 + arg2 * 8) + 16);
    }
    Arg1 = (v_stack_m30) ^ (v_stack_m98);
    result = _security_check_cookie(Arg1, Arg2, *(uint64_t *)(local_r14 + 0x10), *(uint64_t *)(v_stack_m98 + arg2 * 8) + 16);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x20` | `32` | `R` |
| `Arg1` | `+ 0x20` | `32` | `R/W` |
| `Arg1` | `+ 0x80` | `64` | `R` |
| `Arg1` | `+ 0x98` | `64` | `R` |
| `Arg1` | `+ 0xC0 + rcx*8` | `64` | `R` |
| `Arg1` | `+ 0x1C8` | `32` | `R` |
| `Arg1` | `+ 0x1CC` | `32` | `R` |
| `Arg1` | `+ 0x1D0` | `32` | `R` |
| `Arg1` | `+ 0x1D8` | `32` | `R` |
| `Arg1` | `+ 0x2F8` | `64` | `R` |
| `Arg1` | `+ 0x300` | `32` | `R` |
| `Arg1` | `+ 0x320` | `64` | `R` |
| `Arg1` | `+ 0x328` | `32` | `R` |
| `Arg1` | `+ 0x32C` | `32` | `R` |
| `Arg1` | `+ 0x578` | `64` | `R` |
| `Arg2` | `+ 0x0` | `32` | `R` |
| `Arg2` | `+ 0x0 + rax*8` | `64` | `R` |
| `Arg2` | `+ 0x4` | `16` | `R` |
| `Arg2` | `+ 0x6` | `8` | `R` |
| `Arg2` | `+ 0x6` | `16` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg3` | `+ 0x0` | `32` | `R` |
| `Arg3` | `+ 0x4` | `32` | `R` |
| `Arg3` | `+ 0x8` | `32` | `R` |
| `Arg4` | `+ 0x0` | `32` | `R` |
| `Arg4` | `+ 0x4` | `32` | `R` |
| `Arg4` | `+ 0x8` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004EB420&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
