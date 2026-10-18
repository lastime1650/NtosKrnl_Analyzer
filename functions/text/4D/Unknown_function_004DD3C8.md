# sub_004DD3C8

- RVA: `0x004DD3C8`–`0x004DD895` (길이 `1,229` bytes)
- VA: `0x00000001404DD3C8`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BEBA0`
- 디코드: `375`개 명령, `1,229/1,229` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **6**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004DD506` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x004DD525` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004DD558` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x004DD61D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x004DD7CC` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x004DD869` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [sub_00968AF6](../../page/96/Unknown_function_00968AF6.md) at `0x0096A477`

### Static image references
- `0x004DD531` → RVA `0x00FD83A8` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x004DD506` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x004DD61D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x004DD869` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004DD3C8  48 8B C4                        mov rax, rsp
004DD3CB  48 89 58 08                     mov qword ptr [rax + 8], rbx
004DD3CF  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
004DD3D3  48 89 70 20                     mov qword ptr [rax + 0x20], rsi
004DD3D7  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
004DD3DB  57                              push rdi
004DD3DC  41 54                           push r12
004DD3DE  41 55                           push r13
004DD3E0  41 56                           push r14
004DD3E2  41 57                           push r15
004DD3E4  48 83 EC 30                     sub rsp, 0x30
004DD3E8  4C 8B 41 08                     mov r8, qword ptr [rcx + 8]
004DD3EC  45 33 E4                        xor r12d, r12d
004DD3EF  44 21 60 18                     and dword ptr [rax + 0x18], r12d
004DD3F3  49 8B F1                        mov rsi, r9
004DD3F6  4C 8B EA                        mov r13, rdx
004DD3F9  4C 8B C9                        mov r9, rcx
004DD3FC  4D 85 C0                        test r8, r8
004DD3FF  74 5C                           je 0x1404dd45d
004DD401  83 39 03                        cmp dword ptr [rcx], 3
004DD404  76 57                           jbe 0x1404dd45d
004DD406  49 8B C0                        mov rax, r8
004DD409  45 8D 5C 24 01                  lea r11d, [r12 + 1]
004DD40E  33 D2                           xor edx, edx
004DD410  44 8B 10                        mov r10d, dword ptr [rax]
004DD413  48 8D 48 04                     lea rcx, [rax + 4]
004DD417  83 FA 03                        cmp edx, 3
004DD41A  73 1B                           jae 0x1404dd437
004DD41C  48 3B C8                        cmp rcx, rax
004DD41F  0F 82 4B 04 00 00               jb 0x1404dd870
004DD425  4A 8D 04 11                     lea rax, [rcx + r10]
004DD429  48 3B C1                        cmp rax, rcx
004DD42C  0F 82 3E 04 00 00               jb 0x1404dd870
004DD432  41 03 D3                        add edx, r11d
004DD435  EB D9                           jmp 0x1404dd410
004DD437  48 3B C8                        cmp rcx, rax
004DD43A  0F 82 30 04 00 00               jb 0x1404dd870
004DD440  45 33 F6                        xor r14d, r14d
004DD443  45 85 D2                        test r10d, r10d
004DD446  4C 0F 45 F1                     cmovne r14, rcx
004DD44A  41 83 FA 08                     cmp r10d, 8
004DD44E  0F 85 94 00 00 00               jne 0x1404dd4e8
004DD454  41 83 39 04                     cmp dword ptr [r9], 4
004DD458  4D 8B 36                        mov r14, qword ptr [r14]
004DD45B  77 0A                           ja 0x1404dd467
004DD45D  BB 0D 00 00 C0                  mov ebx, 0xc000000d
004DD462  E9 0E 04 00 00                  jmp 0x1404dd875
004DD467  49 8B C0                        mov rax, r8
004DD46A  33 D2                           xor edx, edx
004DD46C  8B 18                           mov ebx, dword ptr [rax]
004DD46E  48 8D 48 04                     lea rcx, [rax + 4]
004DD472  83 FA 04                        cmp edx, 4
004DD475  73 1B                           jae 0x1404dd492
004DD477  48 3B C8                        cmp rcx, rax
004DD47A  0F 82 F0 03 00 00               jb 0x1404dd870
004DD480  48 8D 04 19                     lea rax, [rcx + rbx]
004DD484  48 3B C1                        cmp rax, rcx
004DD487  0F 82 E3 03 00 00               jb 0x1404dd870
004DD48D  41 03 D3                        add edx, r11d
004DD490  EB DA                           jmp 0x1404dd46c
004DD492  48 3B C8                        cmp rcx, rax
004DD495  0F 82 D5 03 00 00               jb 0x1404dd870
004DD49B  33 FF                           xor edi, edi
004DD49D  85 DB                           test ebx, ebx
004DD49F  48 0F 45 F9                     cmovne rdi, rcx
004DD4A3  41 83 39 05                     cmp dword ptr [r9], 5
004DD4A7  76 B4                           jbe 0x1404dd45d
004DD4A9  33 D2                           xor edx, edx
004DD4AB  41 8B 00                        mov eax, dword ptr [r8]
004DD4AE  49 8D 48 04                     lea rcx, [r8 + 4]
004DD4B2  83 FA 05                        cmp edx, 5
004DD4B5  73 1B                           jae 0x1404dd4d2
004DD4B7  49 3B C8                        cmp rcx, r8
004DD4BA  0F 82 B0 03 00 00               jb 0x1404dd870
004DD4C0  4C 8D 04 01                     lea r8, [rcx + rax]
004DD4C4  4C 3B C1                        cmp r8, rcx
004DD4C7  0F 82 A3 03 00 00               jb 0x1404dd870
004DD4CD  41 03 D3                        add edx, r11d
004DD4D0  EB D9                           jmp 0x1404dd4ab
004DD4D2  49 3B C8                        cmp rcx, r8
004DD4D5  0F 82 95 03 00 00               jb 0x1404dd870
004DD4DB  33 ED                           xor ebp, ebp
004DD4DD  85 C0                           test eax, eax
004DD4DF  48 0F 45 E9                     cmovne rbp, rcx
004DD4E3  83 F8 04                        cmp eax, 4
004DD4E6  74 0A                           je 0x1404dd4f2
004DD4E8  BB 23 00 00 C0                  mov ebx, 0xc0000023
004DD4ED  E9 83 03 00 00                  jmp 0x1404dd875
004DD4F2  8B 6D 00                        mov ebp, dword ptr [rbp]
004DD4F5  85 ED                           test ebp, ebp
004DD4F7  74 35                           je 0x1404dd52e
004DD4F9  41 B8 53 4C 53 20               mov r8d, 0x20534c53
004DD4FF  8B D5                           mov edx, ebp
004DD501  B9 00 01 00 00                  mov ecx, 0x100
004DD506  E8 E5 4B 6A 00                  call 0x140b820f0
004DD50B  4C 8B E0                        mov r12, rax
004DD50E  48 85 C0                        test rax, rax
004DD511  75 0A                           jne 0x1404dd51d
004DD513  BB 17 00 00 C0                  mov ebx, 0xc0000017
004DD518  E9 58 03 00 00                  jmp 0x1404dd875
004DD51D  4C 8B C5                        mov r8, rbp
004DD520  33 D2                           xor edx, edx
004DD522  48 8B C8                        mov rcx, rax
004DD525  E8 16 97 1E 00                  call 0x1406c6c40
004DD52A  33 C9                           xor ecx, ecx
004DD52C  EB 03                           jmp 0x1404dd531
004DD52E  41 8B CB                        mov ecx, r11d
004DD531  48 8B 05 70 AE AF 00            mov rax, qword ptr [rip + 0xafae70]
004DD538  48 85 C0                        test rax, rax
004DD53B  74 25                           je 0x1404dd562
004DD53D  45 33 C0                        xor r8d, r8d
004DD540  44 8B CD                        mov r9d, ebp
004DD543  85 C9                           test ecx, ecx
004DD545  8B D3                           mov edx, ebx
004DD547  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
004DD54C  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
004DD551  4D 0F 44 C4                     cmove r8, r12
004DD555  48 8B CF                        mov rcx, rdi
004DD558  E8 73 D5 1D 00                  call 0x1406baad0
004DD55D  44 8B F8                        mov r15d, eax
004DD560  EB 06                           jmp 0x1404dd568
004DD562  41 BF BB 00 00 C0               mov r15d, 0xc00000bb
004DD568  8D 45 04                        lea eax, [rbp + 4]
004DD56B  83 F8 04                        cmp eax, 4
004DD56E  0F 82 E6 02 00 00               jb 0x1404dd85a
004DD574  83 C0 14                        add eax, 0x14
004DD577  83 F8 14                        cmp eax, 0x14
004DD57A  0F 82 DA 02 00 00               jb 0x1404dd85a
004DD580  8D 48 08                        lea ecx, [rax + 8]
004DD583  3B C8                           cmp ecx, eax
004DD585  0F 82 CF 02 00 00               jb 0x1404dd85a
004DD58B  8D 41 08                        lea eax, [rcx + 8]
004DD58E  83 F8 08                        cmp eax, 8
004DD591  0F 82 C3 02 00 00               jb 0x1404dd85a
004DD597  48 8D 50 07                     lea rdx, [rax + 7]
004DD59B  83 E2 F8                        and edx, 0xfffffff8
004DD59E  3B D0                           cmp edx, eax
004DD5A0  0F 82 B4 02 00 00               jb 0x1404dd85a
004DD5A6  8D 42 08                        lea eax, [rdx + 8]
004DD5A9  3B C2                           cmp eax, edx
004DD5AB  0F 82 A9 02 00 00               jb 0x1404dd85a
004DD5B1  45 8B 4D 20                     mov r9d, dword ptr [r13 + 0x20]
004DD5B5  83 C0 04                        add eax, 4
004DD5B8  45 8B 45 10                     mov r8d, dword ptr [r13 + 0x10]
004DD5BC  83 F8 04                        cmp eax, 4
004DD5BF  72 27                           jb 0x1404dd5e8
004DD5C1  8D 50 04                        lea edx, [rax + 4]
004DD5C4  3B D0                           cmp edx, eax
004DD5C6  72 20                           jb 0x1404dd5e8
004DD5C8  41 8D 04 10                     lea eax, [r8 + rdx]
004DD5CC  3B C2                           cmp eax, edx
004DD5CE  72 18                           jb 0x1404dd5e8
004DD5D0  8D 50 04                        lea edx, [rax + 4]
004DD5D3  BF 95 00 00 C0                  mov edi, 0xc0000095
004DD5D8  3B D0                           cmp edx, eax
004DD5DA  72 11                           jb 0x1404dd5ed
004DD5DC  41 8D 04 11                     lea eax, [r9 + rdx]
004DD5E0  3B C2                           cmp eax, edx
004DD5E2  1B DB                           sbb ebx, ebx
004DD5E4  23 DF                           and ebx, edi
004DD5E6  EB 07                           jmp 0x1404dd5ef
004DD5E8  BF 95 00 00 C0                  mov edi, 0xc0000095
004DD5ED  8B DF                           mov ebx, edi
004DD5EF  85 DB                           test ebx, ebx
004DD5F1  0F 88 68 02 00 00               js 0x1404dd85f
004DD5F7  48 85 F6                        test rsi, rsi
004DD5FA  0F 84 36 01 00 00               je 0x1404dd736
004DD600  33 DB                           xor ebx, ebx
004DD602  89 4E 04                        mov dword ptr [rsi + 4], ecx
004DD605  85 C9                           test ecx, ecx
004DD607  75 07                           jne 0x1404dd610
004DD609  BB 3E 00 00 C0                  mov ebx, 0xc000003e
004DD60E  EB 24                           jmp 0x1404dd634
004DD610  8B D1                           mov edx, ecx
004DD612  41 B8 53 4C 53 20               mov r8d, 0x20534c53
004DD618  B9 00 01 00 00                  mov ecx, 0x100
004DD61D  E8 CE 4A 6A 00                  call 0x140b820f0
004DD622  48 85 C0                        test rax, rax
004DD625  75 07                           jne 0x1404dd62e
004DD627  BB 17 00 00 C0                  mov ebx, 0xc0000017
004DD62C  EB 06                           jmp 0x1404dd634
004DD62E  48 89 46 08                     mov qword ptr [rsi + 8], rax
004DD632  21 1E                           and dword ptr [rsi], ebx
004DD634  85 DB                           test ebx, ebx
004DD636  0F 88 23 02 00 00               js 0x1404dd85f
004DD63C  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
004DD640  41 0F BA EF 1C                  bts r15d, 0x1c
004DD645  48 85 D2                        test rdx, rdx
004DD648  75 17                           jne 0x1404dd661
004DD64A  8B 46 04                        mov eax, dword ptr [rsi + 4]
004DD64D  8D 48 08                        lea ecx, [rax + 8]
004DD650  3B C8                           cmp ecx, eax
004DD652  0F 82 0C 01 00 00               jb 0x1404dd764
004DD658  89 4E 04                        mov dword ptr [rsi + 4], ecx
004DD65B  44 8D 6A 01                     lea r13d, [rdx + 1]
004DD65F  EB 5D                           jmp 0x1404dd6be
004DD661  44 8B 16                        mov r10d, dword ptr [rsi]
004DD664  33 C9                           xor ecx, ecx
004DD666  44 8D 69 01                     lea r13d, [rcx + 1]
004DD66A  41 3B CA                        cmp ecx, r10d
004DD66D  73 25                           jae 0x1404dd694
004DD66F  8B 02                           mov eax, dword ptr [rdx]
004DD671  83 C0 04                        add eax, 4
004DD674  83 F8 04                        cmp eax, 4
004DD677  0F 82 EB 00 00 00               jb 0x1404dd768
004DD67D  44 8B C0                        mov r8d, eax
004DD680  4C 03 C2                        add r8, rdx
004DD683  4C 3B C2                        cmp r8, rdx
004DD686  0F 82 DC 00 00 00               jb 0x1404dd768
004DD68C  49 8B D0                        mov rdx, r8
004DD68F  41 03 CD                        add ecx, r13d
004DD692  EB D6                           jmp 0x1404dd66a
004DD694  4C 8D 42 04                     lea r8, [rdx + 4]
004DD698  4C 3B C2                        cmp r8, rdx
004DD69B  0F 82 C7 00 00 00               jb 0x1404dd768
004DD6A1  8B 4E 04                        mov ecx, dword ptr [rsi + 4]
004DD6A4  48 8D 42 08                     lea rax, [rdx + 8]
004DD6A8  48 03 4E 08                     add rcx, qword ptr [rsi + 8]
004DD6AC  48 3B C1                        cmp rax, rcx
004DD6AF  0F 87 00 01 00 00               ja 0x1404dd7b5
004DD6B5  C7 02 04 00 00 00               mov dword ptr [rdx], 4
004DD6BB  45 89 38                        mov dword ptr [r8], r15d
004DD6BE  44 01 2E                        add dword ptr [rsi], r13d
004DD6C1  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
004DD6C5  48 85 D2                        test rdx, rdx
004DD6C8  75 13                           jne 0x1404dd6dd
004DD6CA  8B 46 04                        mov eax, dword ptr [rsi + 4]
004DD6CD  8D 48 0C                        lea ecx, [rax + 0xc]
004DD6D0  3B C8                           cmp ecx, eax
004DD6D2  0F 82 8C 00 00 00               jb 0x1404dd764
004DD6D8  89 4E 04                        mov dword ptr [rsi + 4], ecx
004DD6DB  EB 4D                           jmp 0x1404dd72a
004DD6DD  44 8B 0E                        mov r9d, dword ptr [rsi]
004DD6E0  33 C9                           xor ecx, ecx
004DD6E2  41 3B C9                        cmp ecx, r9d
004DD6E5  73 1D                           jae 0x1404dd704
004DD6E7  8B 02                           mov eax, dword ptr [rdx]
004DD6E9  83 C0 04                        add eax, 4
004DD6EC  83 F8 04                        cmp eax, 4
004DD6EF  72 77                           jb 0x1404dd768
004DD6F1  44 8B C0                        mov r8d, eax
004DD6F4  4C 03 C2                        add r8, rdx
004DD6F7  4C 3B C2                        cmp r8, rdx
004DD6FA  72 6C                           jb 0x1404dd768
004DD6FC  49 8B D0                        mov rdx, r8
004DD6FF  41 03 CD                        add ecx, r13d
004DD702  EB DE                           jmp 0x1404dd6e2
004DD704  4C 8D 42 04                     lea r8, [rdx + 4]
004DD708  4C 3B C2                        cmp r8, rdx
004DD70B  72 5B                           jb 0x1404dd768
004DD70D  8B 4E 04                        mov ecx, dword ptr [rsi + 4]
004DD710  48 8D 42 0C                     lea rax, [rdx + 0xc]
004DD714  48 03 4E 08                     add rcx, qword ptr [rsi + 8]
004DD718  48 3B C1                        cmp rax, rcx
004DD71B  0F 87 94 00 00 00               ja 0x1404dd7b5
004DD721  C7 02 08 00 00 00               mov dword ptr [rdx], 8
004DD727  4D 89 30                        mov qword ptr [r8], r14
004DD72A  44 01 2E                        add dword ptr [rsi], r13d
004DD72D  4D 85 E4                        test r12, r12
004DD730  75 0E                           jne 0x1404dd740
004DD732  85 ED                           test ebp, ebp
004DD734  74 0E                           je 0x1404dd744
004DD736  BB 0D 00 00 C0                  mov ebx, 0xc000000d
004DD73B  E9 1F 01 00 00                  jmp 0x1404dd85f
004DD740  85 ED                           test ebp, ebp
004DD742  74 F2                           je 0x1404dd736
004DD744  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
004DD748  48 85 D2                        test rdx, rdx
004DD74B  75 22                           jne 0x1404dd76f
004DD74D  83 C5 04                        add ebp, 4
004DD750  83 FD 04                        cmp ebp, 4
004DD753  72 13                           jb 0x1404dd768
004DD755  8B 46 04                        mov eax, dword ptr [rsi + 4]
004DD758  8D 0C 28                        lea ecx, [rax + rbp]
004DD75B  3B C8                           cmp ecx, eax
004DD75D  72 05                           jb 0x1404dd764
004DD75F  89 4E 04                        mov dword ptr [rsi + 4], ecx
004DD762  EB 6D                           jmp 0x1404dd7d1
004DD764  83 4E 04 FF                     or dword ptr [rsi + 4], 0xffffffff
004DD768  8B DF                           mov ebx, edi
004DD76A  E9 F0 00 00 00                  jmp 0x1404dd85f
004DD76F  44 8B 0E                        mov r9d, dword ptr [rsi]
004DD772  33 C9                           xor ecx, ecx
004DD774  41 3B C9                        cmp ecx, r9d
004DD777  73 1D                           jae 0x1404dd796
004DD779  8B 02                           mov eax, dword ptr [rdx]
004DD77B  83 C0 04                        add eax, 4
004DD77E  83 F8 04                        cmp eax, 4
004DD781  72 E5                           jb 0x1404dd768
004DD783  44 8B C0                        mov r8d, eax
004DD786  4C 03 C2                        add r8, rdx
004DD789  4C 3B C2                        cmp r8, rdx
004DD78C  72 DA                           jb 0x1404dd768
004DD78E  49 8B D0                        mov rdx, r8
004DD791  41 03 CD                        add ecx, r13d
004DD794  EB DE                           jmp 0x1404dd774
004DD796  4C 8D 4A 04                     lea r9, [rdx + 4]
004DD79A  4C 3B CA                        cmp r9, rdx
004DD79D  72 C9                           jb 0x1404dd768
004DD79F  8B 4E 04                        mov ecx, dword ptr [rsi + 4]
004DD7A2  48 8D 45 04                     lea rax, [rbp + 4]
004DD7A6  48 03 4E 08                     add rcx, qword ptr [rsi + 8]
004DD7AA  48 03 C2                        add rax, rdx
004DD7AD  44 8B C5                        mov r8d, ebp
004DD7B0  48 3B C1                        cmp rax, rcx
004DD7B3  76 0A                           jbe 0x1404dd7bf
004DD7B5  BB 23 00 00 C0                  mov ebx, 0xc0000023
004DD7BA  E9 A0 00 00 00                  jmp 0x1404dd85f
004DD7BF  89 2A                           mov dword ptr [rdx], ebp
004DD7C1  4D 85 E4                        test r12, r12
004DD7C4  74 0B                           je 0x1404dd7d1
004DD7C6  49 8B D4                        mov rdx, r12
004DD7C9  49 8B C9                        mov rcx, r9
004DD7CC  E8 6F 90 1E 00                  call 0x1406c6840
004DD7D1  44 01 2E                        add dword ptr [rsi], r13d
004DD7D4  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
004DD7D8  44 8B 44 24 70                  mov r8d, dword ptr [rsp + 0x70]
004DD7DD  48 85 D2                        test rdx, rdx
004DD7E0  75 18                           jne 0x1404dd7fa
004DD7E2  8B 46 04                        mov eax, dword ptr [rsi + 4]
004DD7E5  8D 48 08                        lea ecx, [rax + 8]
004DD7E8  3B C8                           cmp ecx, eax
004DD7EA  0F 82 74 FF FF FF               jb 0x1404dd764
004DD7F0  44 01 2E                        add dword ptr [rsi], r13d
004DD7F3  33 DB                           xor ebx, ebx
004DD7F5  89 4E 04                        mov dword ptr [rsi + 4], ecx
004DD7F8  EB 65                           jmp 0x1404dd85f
004DD7FA  44 8B 16                        mov r10d, dword ptr [rsi]
004DD7FD  33 C9                           xor ecx, ecx
004DD7FF  41 3B CA                        cmp ecx, r10d
004DD802  73 25                           jae 0x1404dd829
004DD804  8B 02                           mov eax, dword ptr [rdx]
004DD806  83 C0 04                        add eax, 4
004DD809  83 F8 04                        cmp eax, 4
004DD80C  0F 82 56 FF FF FF               jb 0x1404dd768
004DD812  44 8B C8                        mov r9d, eax
004DD815  4C 03 CA                        add r9, rdx
004DD818  4C 3B CA                        cmp r9, rdx
004DD81B  0F 82 47 FF FF FF               jb 0x1404dd768
004DD821  49 8B D1                        mov rdx, r9
004DD824  41 03 CD                        add ecx, r13d
004DD827  EB D6                           jmp 0x1404dd7ff
004DD829  4C 8D 4A 04                     lea r9, [rdx + 4]
004DD82D  4C 3B CA                        cmp r9, rdx
004DD830  0F 82 32 FF FF FF               jb 0x1404dd768
004DD836  8B 4E 04                        mov ecx, dword ptr [rsi + 4]
004DD839  48 8D 42 08                     lea rax, [rdx + 8]
004DD83D  48 03 4E 08                     add rcx, qword ptr [rsi + 8]
004DD841  33 DB                           xor ebx, ebx
004DD843  48 3B C1                        cmp rax, rcx
004DD846  0F 87 69 FF FF FF               ja 0x1404dd7b5
004DD84C  C7 02 04 00 00 00               mov dword ptr [rdx], 4
004DD852  45 89 01                        mov dword ptr [r9], r8d
004DD855  44 01 2E                        add dword ptr [rsi], r13d
004DD858  EB 05                           jmp 0x1404dd85f
004DD85A  BB 95 00 00 C0                  mov ebx, 0xc0000095
004DD85F  4D 85 E4                        test r12, r12
004DD862  74 11                           je 0x1404dd875
004DD864  33 D2                           xor edx, edx
004DD866  49 8B CC                        mov rcx, r12
004DD869  E8 02 50 6A 00                  call 0x140b82870
004DD86E  EB 05                           jmp 0x1404dd875
004DD870  BB 95 00 00 C0                  mov ebx, 0xc0000095
004DD875  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
004DD87A  8B C3                           mov eax, ebx
004DD87C  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
004DD881  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
004DD886  48 83 C4 30                     add rsp, 0x30
004DD88A  41 5F                           pop r15
004DD88C  41 5E                           pop r14
004DD88E  41 5D                           pop r13
004DD890  41 5C                           pop r12
004DD892  5F                              pop rdi
004DD893  C3                              ret
004DD894  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_004DD3C8(__int64 a1, __int64 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 32) = v_rsi;
    *(unsigned int *)(v_rsp + 24) = a3;
    v_rsp = (v_rsp) - (48);
    v_r12 = 0;
    if (*(unsigned __int64 *)(a1 + 8) == 0) goto loc_004DD45D;
    if ((*(unsigned int *)(a1)) <= 3) goto loc_004DD45D;
    a2 = 0;
loc_004DD410:
    if (0 >= 3) goto loc_004DD437;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_004DD870;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_004DD870;
    a2 = (unsigned int)((a2) + ((unsigned int)(v_r12 + 1)));
    goto loc_004DD410;
loc_004DD437:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_004DD870;
    v_r14 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { v_r14 = *(unsigned __int64 *)(a1 + 8) + 4; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) != 8) goto loc_004DD4E8;
    if ((*(unsigned int *)(a1)) > 4) goto loc_004DD467;
loc_004DD45D:
    goto loc_004DD875;
loc_004DD467:
    a2 = 0;
loc_004DD46C:
    if (0 >= 4) goto loc_004DD492;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_004DD870;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_004DD870;
    a2 = (unsigned int)((a2) + ((unsigned int)(v_r12 + 1)));
    goto loc_004DD46C;
loc_004DD492:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_004DD870;
    v_rdi = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { v_rdi = *(unsigned __int64 *)(a1 + 8) + 4; }
    if ((*(unsigned int *)(a1)) <= 5) goto loc_004DD45D;
    a2 = 0;
loc_004DD4AB:
    if (0 >= 5) goto loc_004DD4D2;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_004DD870;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_004DD870;
    a2 = (unsigned int)((a2) + ((unsigned int)(v_r12 + 1)));
    goto loc_004DD4AB;
loc_004DD4D2:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_004DD870;
    v_rbp = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { v_rbp = *(unsigned __int64 *)(a1 + 8) + 4; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) == 4) goto loc_004DD4F2;
loc_004DD4E8:
    goto loc_004DD875;
loc_004DD4F2:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbp))) == 0) goto loc_004DD52E;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rbp)))), (unsigned int)(0x20534C53ULL), a1);
    if (result != 0) goto loc_004DD51D;
    goto loc_004DD875;
loc_004DD51D:
    a2 = 0;
    result = memset(result, a2, (unsigned int)(*(unsigned int *)(v_rbp)), a1);
    a1 = 0;
    goto loc_004DD531;
loc_004DD52E:
loc_004DD531:
    if (*(unsigned __int64 *)(v_rip + 11513456) == 0) goto loc_004DD562;
    a3 = 0;
    v_stack_m38 = v_stack_p18;
    if ((unsigned int)((unsigned int)((unsigned int)(v_r12 + 1))) == 0) { a3 = result; }
    result = guard_dispatch_icall(v_rdi, (unsigned int)((unsigned int)((unsigned int)(0xC0000017ULL))), a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rbp)))));
    goto loc_004DD568;
loc_004DD562:
loc_004DD568:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rbp)) + 4)) < 4) goto loc_004DD85A;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbp)) + 4) + (20));
    if (((unsigned int)(result)) < 20) goto loc_004DD85A;
    if (((unsigned int)(result + 8)) < ((unsigned int)(result))) goto loc_004DD85A;
    if (((unsigned int)(result + 8 + 8)) < 8) goto loc_004DD85A;
    a2 = (unsigned int)((result + 8 + 8 + 7) & (0xFFFFFFF8ULL));
    if (((unsigned int)(a2)) < ((unsigned int)(result + 8 + 8))) goto loc_004DD85A;
    if (((unsigned int)(a2 + 8)) < ((unsigned int)(a2))) goto loc_004DD85A;
    result = (unsigned int)((a2 + 8) + (4));
    if (((unsigned int)(result)) < 4) goto loc_004DD5E8;
    if (((unsigned int)(result + 4)) < ((unsigned int)(result))) goto loc_004DD5E8;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 16)) + result + 4 * 1)) < ((unsigned int)(result + 4))) goto loc_004DD5E8;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 16)) + result + 4 * 1 + 4)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 16)) + result + 4 * 1))) goto loc_004DD5ED;
    v_rbx = (unsigned int)(((unsigned int)(0xC0000017ULL)) & ((unsigned int)((unsigned int)(0xC0000095ULL))));
    goto loc_004DD5EF;
loc_004DD5E8:
loc_004DD5ED:
loc_004DD5EF:
    if (sign_flag) goto loc_004DD85F;
    if (a4 == 0) goto loc_004DD736;
    v_rbx = 0;
    *(unsigned int *)(a4 + 4) = (unsigned int)(result + 8);
    if ((unsigned int)(result + 8) != 0) goto loc_004DD610;
    goto loc_004DD634;
loc_004DD610:
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(result + 8)), (unsigned int)(0x20534C53ULL), (unsigned int)(*(unsigned int *)(a2 + 32)));
    if (result != 0) goto loc_004DD62E;
    goto loc_004DD634;
loc_004DD62E:
    *(unsigned __int64 *)(a4 + 8) = result;
loc_004DD634:
    if (sign_flag) goto loc_004DD85F;
    if (*(unsigned __int64 *)(a4 + 8) != 0) goto loc_004DD661;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_004DD764;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8);
    goto loc_004DD6BE;
loc_004DD661:
    a1 = 0;
loc_004DD66A:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_004DD694;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_004DD768;
    a3 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a3 < (*(unsigned __int64 *)(a4 + 8))) goto loc_004DD768;
    a1 = (unsigned int)((a1) + ((unsigned int)(a1 + 1)));
    goto loc_004DD66A;
loc_004DD694:
    if ((a3 + 4) < a3) goto loc_004DD768;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a3 + 8) > a1) goto loc_004DD7B5;
    *(unsigned int *)(a3) = 4;
    *(unsigned int *)(a3 + 4) = (unsigned int)((unsigned int)(0xC00000BBULL));
loc_004DD6BE:
    if (*(unsigned __int64 *)(a4 + 8) != 0) goto loc_004DD6DD;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_004DD764;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12);
    goto loc_004DD72A;
loc_004DD6DD:
    a1 = 0;
loc_004DD6E2:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_004DD704;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_004DD768;
    a3 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a3 < (*(unsigned __int64 *)(a4 + 8))) goto loc_004DD768;
    a1 = (unsigned int)((a1) + ((unsigned int)(a1 + 1)));
    goto loc_004DD6E2;
loc_004DD704:
    if ((a3 + 4) < a3) goto loc_004DD768;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a3 + 12) > a1) goto loc_004DD7B5;
    *(unsigned int *)(a3) = 8;
    *(unsigned __int64 *)(a3 + 4) = *(unsigned __int64 *)(v_r14);
loc_004DD72A:
    if (result != 0) goto loc_004DD740;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbp))) == 0) goto loc_004DD744;
loc_004DD736:
    goto loc_004DD85F;
loc_004DD740:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbp))) == 0) goto loc_004DD736;
loc_004DD744:
    if (*(unsigned __int64 *)(a4 + 8) != 0) goto loc_004DD76F;
    v_rbp = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbp))) + (4));
    if (((unsigned int)(v_rbp)) < 4) goto loc_004DD768;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + v_rbp * 1)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_004DD764;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + v_rbp * 1);
    goto loc_004DD7D1;
loc_004DD764:
loc_004DD768:
    goto loc_004DD85F;
loc_004DD76F:
    a1 = 0;
loc_004DD774:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_004DD796;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_004DD768;
    a3 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a3 < (*(unsigned __int64 *)(a4 + 8))) goto loc_004DD768;
    a1 = (unsigned int)((a1) + ((unsigned int)(a1 + 1)));
    goto loc_004DD774;
loc_004DD796:
    if ((a3 + 4) < a3) goto loc_004DD768;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    result = (v_rbp + 4) + (a3);
    if (result <= a1) goto loc_004DD7BF;
loc_004DD7B5:
    goto loc_004DD85F;
loc_004DD7BF:
    *(unsigned int *)(a3) = (unsigned int)(v_rbp);
    if (result != 0) {
        a2 = result;
        a1 = a3 + 4;
        result = memcpy(a1, a2, (unsigned int)((unsigned int)(v_rbp)), a3 + 4);
    }
    if (*(unsigned __int64 *)(a4 + 8) != 0) goto loc_004DD7FA;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_004DD764;
    v_rbx = 0;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8);
    goto loc_004DD85F;
loc_004DD7FA:
    a1 = 0;
loc_004DD7FF:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_004DD829;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_004DD768;
    a4 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a4 < (*(unsigned __int64 *)(a4 + 8))) goto loc_004DD768;
    a1 = (unsigned int)((a1) + ((unsigned int)(a1 + 1)));
    goto loc_004DD7FF;
loc_004DD829:
    if ((a4 + 4) < a4) goto loc_004DD768;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    v_rbx = 0;
    if ((a4 + 8) > a1) goto loc_004DD7B5;
    *(unsigned int *)(a4) = 4;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(v_stack_p18));
    goto loc_004DD85F;
loc_004DD85A:
loc_004DD85F:
    if (result == 0) goto loc_004DD875;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (unsigned int)(v_stack_p18), a4 + 4);
    goto loc_004DD875;
loc_004DD870:
loc_004DD875:
    v_rsp = (v_rsp) + (48);
    return (unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL)));
}
```

## 5. (Beta) C Style

```c
int64_t sub_004DD3C8(void *Arg1, void *Arg2, int32_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m38;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x20) = local_rsi;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    local_rsp = (local_rsp) - (48);
    local_r12 = 0;
    if (*(uint64_t *)(arg1 + 0x8) == 0) goto loc_004DD45D;
    if ((*(uint32_t *)(arg1)) <= 3) goto loc_004DD45D;
    Arg2 = 0;
loc_004DD410:
    if (0 >= 3) goto loc_004DD437;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_004DD870;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_004DD870;
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(local_r12 + 1)));
    goto loc_004DD410;
loc_004DD437:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_004DD870;
    local_r14 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { local_r14 = *(uint64_t *)(arg1 + 0x8) + 4; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) != 8) goto loc_004DD4E8;
    if ((*(uint32_t *)(arg1)) > 4) goto loc_004DD467;
loc_004DD45D:
    goto loc_004DD875;
loc_004DD467:
    Arg2 = 0;
loc_004DD46C:
    if (0 >= 4) goto loc_004DD492;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_004DD870;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_004DD870;
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(local_r12 + 1)));
    goto loc_004DD46C;
loc_004DD492:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_004DD870;
    local_rdi = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { local_rdi = *(uint64_t *)(arg1 + 0x8) + 4; }
    if ((*(uint32_t *)(arg1)) <= 5) goto loc_004DD45D;
    Arg2 = 0;
loc_004DD4AB:
    if (0 >= 5) goto loc_004DD4D2;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_004DD870;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_004DD870;
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(local_r12 + 1)));
    goto loc_004DD4AB;
loc_004DD4D2:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_004DD870;
    local_rbp = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { local_rbp = *(uint64_t *)(arg1 + 0x8) + 4; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) == 4) goto loc_004DD4F2;
loc_004DD4E8:
    goto loc_004DD875;
loc_004DD4F2:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbp))) == 0) goto loc_004DD52E;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rbp)))), (uint32_t)(0x20534C53ULL), Arg1);
    if (result != 0) goto loc_004DD51D;
    goto loc_004DD875;
loc_004DD51D:
    Arg2 = 0;
    result = memset(result, Arg2, (uint32_t)(*(uint32_t *)(local_rbp)), Arg1);
    Arg1 = 0;
    goto loc_004DD531;
loc_004DD52E:
loc_004DD531:
    if (*(uint64_t *)(v_rip + 0xAFAE70) == 0) goto loc_004DD562;
    Arg3 = 0;
    v_stack_m38 = v_stack_p18;
    if ((uint32_t)((uint32_t)((uint32_t)(local_r12 + 1))) == 0) { Arg3 = result; }
    result = guard_dispatch_icall(local_rdi, (uint32_t)((uint32_t)((uint32_t)(0xC0000017ULL))), Arg3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rbp)))));
    goto loc_004DD568;
loc_004DD562:
loc_004DD568:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rbp)) + 4)) < 4) goto loc_004DD85A;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbp)) + 4) + (20));
    if (((uint32_t)(result)) < 20) goto loc_004DD85A;
    if (((uint32_t)(result + 8)) < ((uint32_t)(result))) goto loc_004DD85A;
    if (((uint32_t)(result + 8 + 8)) < 8) goto loc_004DD85A;
    Arg2 = (uint32_t)((result + 8 + 8 + 7) & (0xFFFFFFF8ULL));
    if (((uint32_t)(Arg2)) < ((uint32_t)(result + 8 + 8))) goto loc_004DD85A;
    if (((uint32_t)(Arg2 + 8)) < ((uint32_t)(Arg2))) goto loc_004DD85A;
    result = (uint32_t)((Arg2 + 8) + (4));
    if (((uint32_t)(result)) < 4) goto loc_004DD5E8;
    if (((uint32_t)(result + 4)) < ((uint32_t)(result))) goto loc_004DD5E8;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10)) + result + 4 * 1)) < ((uint32_t)(result + 4))) goto loc_004DD5E8;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10)) + result + 4 * 1 + 4)) < ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10)) + result + 4 * 1))) goto loc_004DD5ED;
    local_rbx = (uint32_t)(((uint32_t)(0xC0000017ULL)) & ((uint32_t)((uint32_t)(0xC0000095ULL))));
    goto loc_004DD5EF;
loc_004DD5E8:
loc_004DD5ED:
loc_004DD5EF:
    if (sign_flag) goto loc_004DD85F;
    if (Arg4 == 0) goto loc_004DD736;
    local_rbx = 0;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)(result + 8);
    if ((uint32_t)(result + 8) != 0) goto loc_004DD610;
    goto loc_004DD634;
loc_004DD610:
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(result + 8)), (uint32_t)(0x20534C53ULL), (uint32_t)(*(uint32_t *)(arg2 + 0x20)));
    if (result != 0) goto loc_004DD62E;
    goto loc_004DD634;
loc_004DD62E:
    *(uint64_t *)(Arg4 + 0x8) = result;
loc_004DD634:
    if (sign_flag) goto loc_004DD85F;
    if (*(uint64_t *)(Arg4 + 0x8) != 0) goto loc_004DD661;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_004DD764;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8);
    goto loc_004DD6BE;
loc_004DD661:
    Arg1 = 0;
loc_004DD66A:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_004DD694;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_004DD768;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(Arg4 + 0x8));
    if (Arg3 < (*(uint64_t *)(Arg4 + 0x8))) goto loc_004DD768;
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(Arg1 + 1)));
    goto loc_004DD66A;
loc_004DD694:
    if ((Arg3 + 4) < Arg3) goto loc_004DD768;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    if ((Arg3 + 8) > Arg1) goto loc_004DD7B5;
    *(uint32_t *)(Arg3) = 4;
    *(uint32_t *)(Arg3 + 0x4) = (uint32_t)((uint32_t)(0xC00000BBULL));
loc_004DD6BE:
    if (*(uint64_t *)(Arg4 + 0x8) != 0) goto loc_004DD6DD;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 12)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_004DD764;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 12);
    goto loc_004DD72A;
loc_004DD6DD:
    Arg1 = 0;
loc_004DD6E2:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_004DD704;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_004DD768;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(Arg4 + 0x8));
    if (Arg3 < (*(uint64_t *)(Arg4 + 0x8))) goto loc_004DD768;
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(Arg1 + 1)));
    goto loc_004DD6E2;
loc_004DD704:
    if ((Arg3 + 4) < Arg3) goto loc_004DD768;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    if ((Arg3 + 12) > Arg1) goto loc_004DD7B5;
    *(uint32_t *)(Arg3) = 8;
    *(uint64_t *)(Arg3 + 0x4) = *(uint64_t *)(local_r14);
loc_004DD72A:
    if (result != 0) goto loc_004DD740;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbp))) == 0) goto loc_004DD744;
loc_004DD736:
    goto loc_004DD85F;
loc_004DD740:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbp))) == 0) goto loc_004DD736;
loc_004DD744:
    if (*(uint64_t *)(Arg4 + 0x8) != 0) goto loc_004DD76F;
    local_rbp = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbp))) + (4));
    if (((uint32_t)(local_rbp)) < 4) goto loc_004DD768;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + local_rbp * 1)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_004DD764;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + local_rbp * 1);
    goto loc_004DD7D1;
loc_004DD764:
loc_004DD768:
    goto loc_004DD85F;
loc_004DD76F:
    Arg1 = 0;
loc_004DD774:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_004DD796;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_004DD768;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(Arg4 + 0x8));
    if (Arg3 < (*(uint64_t *)(Arg4 + 0x8))) goto loc_004DD768;
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(Arg1 + 1)));
    goto loc_004DD774;
loc_004DD796:
    if ((Arg3 + 4) < Arg3) goto loc_004DD768;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    result = (local_rbp + 4) + (Arg3);
    if (result <= Arg1) goto loc_004DD7BF;
loc_004DD7B5:
    goto loc_004DD85F;
loc_004DD7BF:
    *(uint32_t *)(Arg3) = (uint32_t)(local_rbp);
    if (result != 0) {
        Arg2 = result;
        Arg1 = Arg3 + 4;
        result = memcpy(Arg1, Arg2, (uint32_t)((uint32_t)(local_rbp)), Arg3 + 4);
    }
    if (*(uint64_t *)(Arg4 + 0x8) != 0) goto loc_004DD7FA;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_004DD764;
    local_rbx = 0;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8);
    goto loc_004DD85F;
loc_004DD7FA:
    Arg1 = 0;
loc_004DD7FF:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_004DD829;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_004DD768;
    Arg4 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(Arg4 + 0x8));
    if (Arg4 < (*(uint64_t *)(Arg4 + 0x8))) goto loc_004DD768;
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(Arg1 + 1)));
    goto loc_004DD7FF;
loc_004DD829:
    if ((Arg4 + 4) < Arg4) goto loc_004DD768;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    local_rbx = 0;
    if ((Arg4 + 8) > Arg1) goto loc_004DD7B5;
    *(uint32_t *)(Arg4) = 4;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(v_stack_p18));
    goto loc_004DD85F;
loc_004DD85A:
loc_004DD85F:
    if (result == 0) goto loc_004DD875;
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, (uint32_t)(v_stack_p18), Arg4 + 4);
    goto loc_004DD875;
loc_004DD870:
loc_004DD875:
    local_rsp = (local_rsp) + (48);
    return (uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL)));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x10` | `32` | `R` |
| `Arg2` | `+ 0x20` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004DD3C8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
