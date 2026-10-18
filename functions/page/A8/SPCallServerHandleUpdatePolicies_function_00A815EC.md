# SPCallServerHandleUpdatePolicies

- RVA: `0x00A815EC`–`0x00A8190D` (길이 `801` bytes)
- VA: `0x0000000140A815EC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000B7168`
- 디코드: `216`개 명령, `801/801` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00A81715` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00A8174B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A8178F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)

### Direct callers
- [sub_00968AF6](../96/Unknown_function_00968AF6.md) at `0x0096A1C4`

### Static image references
- `0x00A8169F` → RVA `0x00FD8218` (`PAGEDATA`; read)
- `0x00A81702` → RVA `0x00FD8440` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00A81715` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00A8174B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A8178F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **8**
  - `0x00A8182B` → [sub_00B4355C + 0x2C9](../B4/Unknown_function_00B4355C.md) (`tail-transfer`)
  - `0x00A8185E` → [sub_00B4355C](../B4/Unknown_function_00B4355C.md) (`tail-transfer`)
  - `0x00A81875` → [sub_00B4355C + 0x56](../B4/Unknown_function_00B4355C.md) (`tail-transfer`)
  - `0x00A8187D` → [sub_00B4355C + 0x121](../B4/Unknown_function_00B4355C.md) (`tail-transfer`)
  - `0x00A818BD` → [sub_00B4355C + 0x129](../B4/Unknown_function_00B4355C.md) (`tail-transfer`)
  - `0x00A818D4` → [sub_00B4355C + 0x17F](../B4/Unknown_function_00B4355C.md) (`tail-transfer`)
  - `0x00A818F1` → [sub_00B4355C + 0x205](../B4/Unknown_function_00B4355C.md) (`tail-transfer`)
  - `0x00A81908` → [sub_00B4355C + 0x25A](../B4/Unknown_function_00B4355C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00A815EC  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00A815F1  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
00A815F6  41 56                           push r14
00A815F8  48 83 EC 20                     sub rsp, 0x20
00A815FC  49 8B D9                        mov rbx, r9
00A815FF  4C 8B C9                        mov r9, rcx
00A81602  8B 4A 10                        mov ecx, dword ptr [rdx + 0x10]
00A81605  44 8B 52 20                     mov r10d, dword ptr [rdx + 0x20]
00A81609  83 C1 20                        add ecx, 0x20
00A8160C  83 F9 20                        cmp ecx, 0x20
00A8160F  73 1B                           jae 0x140a8162c
00A81611  41 B8 95 00 00 C0               mov r8d, 0xc0000095
00A81617  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00A8161C  41 8B C0                        mov eax, r8d
00A8161F  48 8B 6C 24 38                  mov rbp, qword ptr [rsp + 0x38]
00A81624  48 83 C4 20                     add rsp, 0x20
00A81628  41 5E                           pop r14
00A8162A  C3                              ret
00A8162B  CC                              int3
00A8162C  8D 41 04                        lea eax, [rcx + 4]
00A8162F  3B C1                           cmp eax, ecx
00A81631  72 DE                           jb 0x140a81611
00A81633  42 8D 0C 10                     lea ecx, [rax + r10]
00A81637  3B C8                           cmp ecx, eax
00A81639  72 D6                           jb 0x140a81611
00A8163B  44 3B C1                        cmp r8d, ecx
00A8163E  0F 82 95 02 00 00               jb 0x140a818d9
00A81644  49 8B 41 08                     mov rax, qword ptr [r9 + 8]
00A81648  48 85 C0                        test rax, rax
00A8164B  0F 84 17 01 00 00               je 0x140a81768
00A81651  41 83 39 03                     cmp dword ptr [r9], 3
00A81655  0F 86 0D 01 00 00               jbe 0x140a81768
00A8165B  33 D2                           xor edx, edx
00A8165D  44 8B 00                        mov r8d, dword ptr [rax]
00A81660  48 8D 48 04                     lea rcx, [rax + 4]
00A81664  83 FA 03                        cmp edx, 3
00A81667  73 12                           jae 0x140a8167b
00A81669  48 3B C8                        cmp rcx, rax
00A8166C  72 A3                           jb 0x140a81611
00A8166E  4A 8D 04 01                     lea rax, [rcx + r8]
00A81672  48 3B C1                        cmp rax, rcx
00A81675  72 9A                           jb 0x140a81611
00A81677  FF C2                           inc edx
00A81679  EB E2                           jmp 0x140a8165d
00A8167B  48 3B C8                        cmp rcx, rax
00A8167E  72 91                           jb 0x140a81611
00A81680  33 C0                           xor eax, eax
00A81682  45 85 C0                        test r8d, r8d
00A81685  48 0F 45 C1                     cmovne rax, rcx
00A81689  41 83 F8 08                     cmp r8d, 8
00A8168D  0F 85 9D 01 00 00               jne 0x140a81830
00A81693  48 8B 08                        mov rcx, qword ptr [rax]
00A81696  48 85 C9                        test rcx, rcx
00A81699  0F 84 09 02 00 00               je 0x140a818a8
00A8169F  48 8B 05 72 6B 55 00            mov rax, qword ptr [rip + 0x556b72]
00A816A6  48 85 C0                        test rax, rax
00A816A9  0F 84 F9 01 00 00               je 0x140a818a8
00A816AF  48 3B C8                        cmp rcx, rax
00A816B2  0F 85 91 01 00 00               jne 0x140a81849
00A816B8  49 8B 41 08                     mov rax, qword ptr [r9 + 8]
00A816BC  48 85 C0                        test rax, rax
00A816BF  0F 84 A3 00 00 00               je 0x140a81768
00A816C5  41 8D 68 FC                     lea ebp, [r8 - 4]
00A816C9  41 39 29                        cmp dword ptr [r9], ebp
00A816CC  0F 86 96 00 00 00               jbe 0x140a81768
00A816D2  33 D2                           xor edx, edx
00A816D4  44 8B 00                        mov r8d, dword ptr [rax]
00A816D7  48 8D 48 04                     lea rcx, [rax + 4]
00A816DB  3B D5                           cmp edx, ebp
00A816DD  73 1A                           jae 0x140a816f9
00A816DF  48 3B C8                        cmp rcx, rax
00A816E2  0F 82 29 FF FF FF               jb 0x140a81611
00A816E8  4A 8D 04 01                     lea rax, [rcx + r8]
00A816EC  48 3B C1                        cmp rax, rcx
00A816EF  0F 82 1C FF FF FF               jb 0x140a81611
00A816F5  FF C2                           inc edx
00A816F7  EB DB                           jmp 0x140a816d4
00A816F9  48 3B C8                        cmp rcx, rax
00A816FC  0F 82 0F FF FF FF               jb 0x140a81611
00A81702  48 8B 05 37 6D 55 00            mov rax, qword ptr [rip + 0x556d37]
00A81709  33 D2                           xor edx, edx
00A8170B  45 85 C0                        test r8d, r8d
00A8170E  48 0F 45 D1                     cmovne rdx, rcx
00A81712  41 8B C8                        mov ecx, r8d
00A81715  E8 B6 93 C3 FF                  call 0x1406baad0
00A8171A  44 8B F0                        mov r14d, eax
00A8171D  3D 07 01 00 00                  cmp eax, 0x107
00A81722  0F 84 65 01 00 00               je 0x140a8188d
00A81728  3D 00 00 00 40                  cmp eax, 0x40000000
00A8172D  0F 85 47 01 00 00               jne 0x140a8187a
00A81733  41 BE 01 D6 04 40               mov r14d, 0x4004d601
00A81739  83 63 04 00                     and dword ptr [rbx + 4], 0
00A8173D  83 23 00                        and dword ptr [rbx], 0
00A81740  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
00A81744  48 85 C9                        test rcx, rcx
00A81747  74 0C                           je 0x140a81755
00A81749  33 D2                           xor edx, edx
00A8174B  E8 20 11 10 00                  call 0x140b82870
00A81750  48 83 63 08 00                  and qword ptr [rbx + 8], 0
00A81755  8B 43 04                        mov eax, dword ptr [rbx + 4]
00A81758  8D 48 08                        lea ecx, [rax + 8]
00A8175B  3B C8                           cmp ecx, eax
00A8175D  73 14                           jae 0x140a81773
00A8175F  83 4B 04 FF                     or dword ptr [rbx + 4], 0xffffffff
00A81763  E9 A9 FE FF FF                  jmp 0x140a81611
00A81768  41 B8 0D 00 00 C0               mov r8d, 0xc000000d
00A8176E  E9 A4 FE FF FF                  jmp 0x140a81617
00A81773  FF 03                           inc dword ptr [rbx]
00A81775  8B C1                           mov eax, ecx
00A81777  89 4B 04                        mov dword ptr [rbx + 4], ecx
00A8177A  85 C0                           test eax, eax
00A8177C  0F 84 16 01 00 00               je 0x140a81898
00A81782  8B D0                           mov edx, eax
00A81784  B9 00 01 00 00                  mov ecx, 0x100
00A81789  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00A8178F  E8 5C 09 10 00                  call 0x140b820f0
00A81794  48 85 C0                        test rax, rax
00A81797  0F 84 03 01 00 00               je 0x140a818a0
00A8179D  48 89 43 08                     mov qword ptr [rbx + 8], rax
00A817A1  83 23 00                        and dword ptr [rbx], 0
00A817A4  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
00A817A8  48 85 D2                        test rdx, rdx
00A817AB  74 58                           je 0x140a81805
00A817AD  44 8B 0B                        mov r9d, dword ptr [rbx]
00A817B0  33 C9                           xor ecx, ecx
00A817B2  41 3B C9                        cmp ecx, r9d
00A817B5  73 22                           jae 0x140a817d9
00A817B7  8B 02                           mov eax, dword ptr [rdx]
00A817B9  03 C5                           add eax, ebp
00A817BB  3B C5                           cmp eax, ebp
00A817BD  0F 82 4E FE FF FF               jb 0x140a81611
00A817C3  44 8B C0                        mov r8d, eax
00A817C6  4C 03 C2                        add r8, rdx
00A817C9  4C 3B C2                        cmp r8, rdx
00A817CC  0F 82 3F FE FF FF               jb 0x140a81611
00A817D2  49 8B D0                        mov rdx, r8
00A817D5  FF C1                           inc ecx
00A817D7  EB D9                           jmp 0x140a817b2
00A817D9  4C 8D 4A 04                     lea r9, [rdx + 4]
00A817DD  4C 3B CA                        cmp r9, rdx
00A817E0  0F 82 2B FE FF FF               jb 0x140a81611
00A817E6  8B 4B 04                        mov ecx, dword ptr [rbx + 4]
00A817E9  48 8D 42 08                     lea rax, [rdx + 8]
00A817ED  48 03 4B 08                     add rcx, qword ptr [rbx + 8]
00A817F1  45 33 C0                        xor r8d, r8d
00A817F4  48 3B C1                        cmp rax, rcx
00A817F7  77 37                           ja 0x140a81830
00A817F9  89 2A                           mov dword ptr [rdx], ebp
00A817FB  45 89 31                        mov dword ptr [r9], r14d
00A817FE  FF 03                           inc dword ptr [rbx]
00A81800  E9 12 FE FF FF                  jmp 0x140a81617
00A81805  8B 53 04                        mov edx, dword ptr [rbx + 4]
00A81808  83 C8 FF                        or eax, 0xffffffff
00A8180B  41 B8 95 00 00 C0               mov r8d, 0xc0000095
00A81811  8D 4A 08                        lea ecx, [rdx + 8]
00A81814  3B CA                           cmp ecx, edx
00A81816  0F 43 C1                        cmovae eax, ecx
00A81819  89 43 04                        mov dword ptr [rbx + 4], eax
00A8181C  1B C0                           sbb eax, eax
00A8181E  44 23 C0                        and r8d, eax
00A81821  3B CA                           cmp ecx, edx
00A81823  0F 82 EE FD FF FF               jb 0x140a81617
00A81829  FF 03                           inc dword ptr [rbx]
00A8182B  E9 F5 1F 0C 00                  jmp 0x140b43825
00A81830  41 B8 23 00 00 C0               mov r8d, 0xc0000023
00A81836  E9 DC FD FF FF                  jmp 0x140a81617
00A8183B  45 85 C0                        test r8d, r8d
00A8183E  0F 89 60 FF FF FF               jns 0x140a817a4
00A81844  E9 CE FD FF FF                  jmp 0x140a81617
00A81849  48 85 DB                        test rbx, rbx
00A8184C  0F 84 16 FF FF FF               je 0x140a81768
00A81852  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
00A81856  BD 04 00 00 00                  mov ebp, 4
00A8185B  48 85 D2                        test rdx, rdx
00A8185E  0F 85 F8 1C 0C 00               jne 0x140b4355c
00A81864  8B 43 04                        mov eax, dword ptr [rbx + 4]
00A81867  8D 48 08                        lea ecx, [rax + 8]
00A8186A  3B C8                           cmp ecx, eax
00A8186C  0F 82 ED FE FF FF               jb 0x140a8175f
00A81872  89 4B 04                        mov dword ptr [rbx + 4], ecx
00A81875  E9 38 1D 0C 00                  jmp 0x140b435b2
00A8187A  45 85 F6                        test r14d, r14d
00A8187D  0F 89 FA 1D 0C 00               jns 0x140b4367d
00A81883  41 0F BA EE 1C                  bts r14d, 0x1c
00A81888  E9 AC FE FF FF                  jmp 0x140a81739
00A8188D  41 BE 02 D6 04 40               mov r14d, 0x4004d602
00A81893  E9 A1 FE FF FF                  jmp 0x140a81739
00A81898  41 B8 3E 00 00 C0               mov r8d, 0xc000003e
00A8189E  EB 9B                           jmp 0x140a8183b
00A818A0  41 B8 17 00 00 C0               mov r8d, 0xc0000017
00A818A6  EB 93                           jmp 0x140a8183b
00A818A8  48 85 DB                        test rbx, rbx
00A818AB  0F 84 B7 FE FF FF               je 0x140a81768
00A818B1  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
00A818B5  BD 04 00 00 00                  mov ebp, 4
00A818BA  48 85 D2                        test rdx, rdx
00A818BD  0F 85 C2 1D 0C 00               jne 0x140b43685
00A818C3  8B 43 04                        mov eax, dword ptr [rbx + 4]
00A818C6  8D 48 08                        lea ecx, [rax + 8]
00A818C9  3B C8                           cmp ecx, eax
00A818CB  0F 82 8E FE FF FF               jb 0x140a8175f
00A818D1  89 4B 04                        mov dword ptr [rbx + 4], ecx
00A818D4  E9 02 1E 0C 00                  jmp 0x140b436db
00A818D9  48 85 DB                        test rbx, rbx
00A818DC  0F 84 86 FE FF FF               je 0x140a81768
00A818E2  4C 8D 73 08                     lea r14, [rbx + 8]
00A818E6  BD 04 00 00 00                  mov ebp, 4
00A818EB  4D 8B 06                        mov r8, qword ptr [r14]
00A818EE  4D 85 C0                        test r8, r8
00A818F1  0F 85 6A 1E 0C 00               jne 0x140b43761
00A818F7  8B 43 04                        mov eax, dword ptr [rbx + 4]
00A818FA  8D 48 08                        lea ecx, [rax + 8]
00A818FD  3B C8                           cmp ecx, eax
00A818FF  0F 82 5A FE FF FF               jb 0x140a8175f
00A81905  89 4B 04                        mov dword ptr [rbx + 4], ecx
00A81908  E9 A9 1E 0C 00                  jmp 0x140b437b6
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SPCallServerHandleUpdatePolicies(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_rsp = (v_rsp) - (32);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 16))) + (32));
    if (((unsigned int)(a1)) >= 32) goto loc_00A8162C;
loc_00A81611:
loc_00A81617:
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL)));
loc_00A8162C:
    if (((unsigned int)(a1 + 4)) < ((unsigned int)(a1))) goto loc_00A81611;
    if (((unsigned int)(a1 + 4 + (unsigned int)(*(unsigned int *)(a2 + 32)) * 1)) < ((unsigned int)(a1 + 4))) goto loc_00A81611;
    if (((unsigned int)((unsigned int)(0xC0000095ULL))) < ((unsigned int)(a1 + 4 + (unsigned int)(*(unsigned int *)(a2 + 32)) * 1))) goto loc_00A818D9;
    if (*(unsigned __int64 *)(a1 + 8) == 0) goto loc_00A81768;
    if ((*(unsigned int *)(a1)) <= 3) goto loc_00A81768;
    a2 = 0;
loc_00A8165D:
    if (0 >= 3) goto loc_00A8167B;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_00A81611;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00A81611;
    a2 = (unsigned int)((a2) + 1);
    goto loc_00A8165D;
loc_00A8167B:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00A81611;
    result = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { result = *(unsigned __int64 *)(a1 + 8) + 4; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) != 8) goto loc_00A81830;
    if (*(unsigned __int64 *)(result) == 0) goto loc_00A818A8;
    if (*(unsigned __int64 *)(v_rip + 5598066) == 0) goto loc_00A818A8;
    if ((*(unsigned __int64 *)(result)) != (*(unsigned __int64 *)(v_rip + 5598066))) goto loc_00A81849;
    if (*(unsigned __int64 *)(a1 + 8) == 0) goto loc_00A81768;
    if ((*(unsigned int *)(a1)) <= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) - 4))) goto loc_00A81768;
    a2 = 0;
loc_00A816D4:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) - 4))) goto loc_00A816F9;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_00A81611;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00A81611;
    a2 = (unsigned int)((a2) + 1);
    goto loc_00A816D4;
loc_00A816F9:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00A81611;
    a2 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { a2 = *(unsigned __int64 *)(a1 + 8) + 4; }
    result = guard_dispatch_icall((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))), a2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))), a1);
    if (((unsigned int)(result)) == 263) goto loc_00A8188D;
    if (((unsigned int)(result)) != 0x40000000ULL) goto loc_00A8187A;
loc_00A81739:
    if (*(unsigned __int64 *)(v_stack_p8 + 8) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(v_stack_p8 + 8), a2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))), a1);
    }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 4)) + 8)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 4))))) goto loc_00A81773;
loc_00A8175F:
    goto loc_00A81611;
loc_00A81768:
    goto loc_00A81617;
loc_00A81773:
    *(unsigned int *)(v_stack_p8 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 4)) + 8);
    if ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 4)) + 8))) == 0) goto loc_00A81898;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 4)) + 8)))), (unsigned int)(0x20534C53ULL), a1);
    if (result == 0) goto loc_00A818A0;
    *(unsigned __int64 *)(v_stack_p8 + 8) = result;
loc_00A817A4:
    if (*(unsigned __int64 *)(v_stack_p8 + 8) == 0) goto loc_00A81805;
    a1 = 0;
loc_00A817B2:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8))))) goto loc_00A817D9;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p8 + 8)))) + ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) - 4)));
    if (((unsigned int)(result)) < ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) - 4))) goto loc_00A81611;
    a3 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(v_stack_p8 + 8));
    if (a3 < (*(unsigned __int64 *)(v_stack_p8 + 8))) goto loc_00A81611;
    a1 = (unsigned int)((a1) + 1);
    goto loc_00A817B2;
loc_00A817D9:
    if ((a3 + 4) < a3) goto loc_00A81611;
    a1 = ((unsigned int)(*(unsigned int *)(v_stack_p8 + 4))) + (*(unsigned __int64 *)(v_stack_p8 + 8));
    a3 = 0;
    if ((a3 + 8) > a1) goto loc_00A81830;
    *(unsigned int *)(a3) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) - 4);
    *(unsigned int *)(a3 + 4) = (unsigned int)((unsigned int)(0x4004D601ULL));
    goto loc_00A81617;
loc_00A81805:
    result = (unsigned int)((a3 + 8) | (0xFFFFFFFFULL));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 4)) + 8)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 4))))) { result = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 4)) + 8); }
    *(unsigned int *)(v_stack_p8 + 4) = (unsigned int)(result);
    a3 = (unsigned int)(((unsigned int)(0xC0000095ULL)) & ((unsigned int)(result)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 4)) + 8)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 4))))) goto loc_00A81617;
loc_00A81830:
    goto loc_00A81617;
loc_00A8183B:
    if (!sign_flag) goto loc_00A817A4;
    goto loc_00A81617;
loc_00A81849:
    if (v_stack_p8 == 0) goto loc_00A81768;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 4)) + 8)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 4))))) goto loc_00A8175F;
    *(unsigned int *)(v_stack_p8 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 4)) + 8);
loc_00A8187A:
    goto loc_00A81739;
loc_00A8188D:
    goto loc_00A81739;
loc_00A81898:
    goto loc_00A8183B;
loc_00A818A0:
    goto loc_00A8183B;
loc_00A818A8:
    if (v_stack_p8 == 0) goto loc_00A81768;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 4)) + 8)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 4))))) goto loc_00A8175F;
    *(unsigned int *)(v_stack_p8 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 4)) + 8);
loc_00A818D9:
    if (v_stack_p8 == 0) goto loc_00A81768;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 4)) + 8)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 4))))) goto loc_00A8175F;
    *(unsigned int *)(v_stack_p8 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 4)) + 8);
}
```

## 5. (Beta) C Style

```c
int64_t SPCallServerHandleUpdatePolicies(void *Arg1, void *Arg2, int64_t Arg3, void *Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    local_rsp = (local_rsp) - (32);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x10))) + (32));
    if (((uint32_t)(Arg1)) >= 32) goto loc_00A8162C;
loc_00A81611:
loc_00A81617:
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL)));
loc_00A8162C:
    if (((uint32_t)(Arg1 + 4)) < ((uint32_t)(Arg1))) goto loc_00A81611;
    if (((uint32_t)(Arg1 + 4 + (uint32_t)(*(uint32_t *)(arg2 + 0x20)) * 1)) < ((uint32_t)(Arg1 + 4))) goto loc_00A81611;
    if (((uint32_t)((uint32_t)(0xC0000095ULL))) < ((uint32_t)(Arg1 + 4 + (uint32_t)(*(uint32_t *)(arg2 + 0x20)) * 1))) goto loc_00A818D9;
    if (*(uint64_t *)(arg1 + 0x8) == 0) goto loc_00A81768;
    if ((*(uint32_t *)(arg1)) <= 3) goto loc_00A81768;
    Arg2 = 0;
loc_00A8165D:
    if (0 >= 3) goto loc_00A8167B;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_00A81611;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00A81611;
    Arg2 = (uint32_t)((Arg2) + 1);
    goto loc_00A8165D;
loc_00A8167B:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00A81611;
    result = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { result = *(uint64_t *)(arg1 + 0x8) + 4; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) != 8) goto loc_00A81830;
    if (*(uint64_t *)(result) == 0) goto loc_00A818A8;
    if (*(uint64_t *)(v_rip + 0x556B72) == 0) goto loc_00A818A8;
    if ((*(uint64_t *)(result)) != (*(uint64_t *)(v_rip + 0x556B72))) goto loc_00A81849;
    if (*(uint64_t *)(arg1 + 0x8) == 0) goto loc_00A81768;
    if ((*(uint32_t *)(arg1)) <= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) - 4))) goto loc_00A81768;
    Arg2 = 0;
loc_00A816D4:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) - 4))) goto loc_00A816F9;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_00A81611;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00A81611;
    Arg2 = (uint32_t)((Arg2) + 1);
    goto loc_00A816D4;
loc_00A816F9:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00A81611;
    Arg2 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { Arg2 = *(uint64_t *)(arg1 + 0x8) + 4; }
    result = guard_dispatch_icall((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))), Arg2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))), Arg1);
    if (((uint32_t)(result)) == 263) goto loc_00A8188D;
    if (((uint32_t)(result)) != 0x40000000ULL) goto loc_00A8187A;
loc_00A81739:
    if (*(uint64_t *)(v_stack_p8 + 0x8) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(v_stack_p8 + 0x8), Arg2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))), Arg1);
    }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4)) + 8)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4))))) goto loc_00A81773;
loc_00A8175F:
    goto loc_00A81611;
loc_00A81768:
    goto loc_00A81617;
loc_00A81773:
    *(uint32_t *)(v_stack_p8 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4)) + 8);
    if ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4)) + 8))) == 0) goto loc_00A81898;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4)) + 8)))), (uint32_t)(0x20534C53ULL), Arg1);
    if (result == 0) goto loc_00A818A0;
    *(uint64_t *)(v_stack_p8 + 0x8) = result;
loc_00A817A4:
    if (*(uint64_t *)(v_stack_p8 + 0x8) == 0) goto loc_00A81805;
    Arg1 = 0;
loc_00A817B2:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8))))) goto loc_00A817D9;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p8 + 0x8)))) + ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) - 4)));
    if (((uint32_t)(result)) < ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) - 4))) goto loc_00A81611;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(v_stack_p8 + 0x8));
    if (Arg3 < (*(uint64_t *)(v_stack_p8 + 0x8))) goto loc_00A81611;
    Arg1 = (uint32_t)((Arg1) + 1);
    goto loc_00A817B2;
loc_00A817D9:
    if ((Arg3 + 4) < Arg3) goto loc_00A81611;
    Arg1 = ((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4))) + (*(uint64_t *)(v_stack_p8 + 0x8));
    Arg3 = 0;
    if ((Arg3 + 8) > Arg1) goto loc_00A81830;
    *(uint32_t *)(Arg3) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) - 4);
    *(uint32_t *)(Arg3 + 0x4) = (uint32_t)((uint32_t)(0x4004D601ULL));
    goto loc_00A81617;
loc_00A81805:
    result = (uint32_t)((Arg3 + 8) | (0xFFFFFFFFULL));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4)) + 8)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4))))) { result = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4)) + 8); }
    *(uint32_t *)(v_stack_p8 + 0x4) = (uint32_t)(result);
    Arg3 = (uint32_t)(((uint32_t)(0xC0000095ULL)) & ((uint32_t)(result)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4)) + 8)) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4))))) goto loc_00A81617;
loc_00A81830:
    goto loc_00A81617;
loc_00A8183B:
    if (!sign_flag) goto loc_00A817A4;
    goto loc_00A81617;
loc_00A81849:
    if (v_stack_p8 == 0) goto loc_00A81768;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4)) + 8)) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4))))) goto loc_00A8175F;
    *(uint32_t *)(v_stack_p8 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4)) + 8);
loc_00A8187A:
    goto loc_00A81739;
loc_00A8188D:
    goto loc_00A81739;
loc_00A81898:
    goto loc_00A8183B;
loc_00A818A0:
    goto loc_00A8183B;
loc_00A818A8:
    if (v_stack_p8 == 0) goto loc_00A81768;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4)) + 8)) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4))))) goto loc_00A8175F;
    *(uint32_t *)(v_stack_p8 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4)) + 8);
loc_00A818D9:
    if (v_stack_p8 == 0) goto loc_00A81768;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4)) + 8)) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4))))) goto loc_00A8175F;
    *(uint32_t *)(v_stack_p8 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4)) + 8);
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
| `Arg4` | `+ 0x0` | `32` | `R` |
| `Arg4` | `+ 0x0` | `32` | `R/W` |
| `Arg4` | `+ 0x4` | `32` | `R` |
| `Arg4` | `+ 0x4` | `32` | `R/W` |
| `Arg4` | `+ 0x4` | `32` | `W` |
| `Arg4` | `+ 0x8` | `64` | `R` |
| `Arg4` | `+ 0x8` | `64` | `R/W` |
| `Arg4` | `+ 0x8` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A815EC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
