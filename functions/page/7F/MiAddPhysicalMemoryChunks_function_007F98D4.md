# MiAddPhysicalMemoryChunks

- RVA: `0x007F98D4`–`0x007F9E2B` (길이 `1,367` bytes)
- VA: `0x00000001407F98D4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AE098`
- 디코드: `399`개 명령, `1,367/1,367` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **11**; 고유 호출 대상: **9**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x007F997B` → [MiAddPhysicalMemory](MiAddPhysicalMemory_function_007F95FC.md) (function, `0x007F95FC`)
- `0x007F99E6` → [MiRestrictRangeToNode](../../text/40/MiRestrictRangeToNode_function_0040199C.md) (function, `0x0040199C`)
- `0x007F9A17` → [MiPageToNode](../../text/33/MiPageToNode_function_00338CD0.md) (function, `0x00338CD0`)
- `0x007F9A26` → [MiGetClosestImplicitNode](../../text/3F/MiGetClosestImplicitNode_function_003F00AC.md) (function, `0x003F00AC`)
- `0x007F9BAF` → [MiNodeLargeFreeZeroPages2](../../text/68/MiNodeLargeFreeZeroPages2_function_0068AD04.md) (function, `0x0068AD04`)
- `0x007F9C0F` → [MiNodeLargeFreeZeroPages2](../../text/68/MiNodeLargeFreeZeroPages2_function_0068AD04.md) (function, `0x0068AD04`)
- `0x007F9C33` → [MiNodeAvailablePages](../../text/3B/MiNodeAvailablePages_function_003BB920.md) (function, `0x003BB920`)
- `0x007F9C52` → [MiGetAvailablePagesExcludeSlists](../../text/48/MiGetAvailablePagesExcludeSlists_function_00483924.md) (function, `0x00483924`)
- `0x007F9D19` → [MiGetLargestPageIndex](../../text/49/MiGetLargestPageIndex_function_0049F730.md) (function, `0x0049F730`)
- `0x007F9D86` → [MiAddPhysicalMemory](MiAddPhysicalMemory_function_007F95FC.md) (function, `0x007F95FC`)
- `0x007F9E0F` → [IoUpdateDumpPhysicalRanges](../../text/59/IoUpdateDumpPhysicalRanges_function_0059343C.md) (function, `0x0059343C`)

### Direct callers
- [MiActOnPartitionNodePages](../../text/68/MiActOnPartitionNodePages_function_0068F7F4.md) at `0x0068FFD1`
- [MmAddPhysicalMemory](MmAddPhysicalMemory_function_007FB460.md) at `0x007FB4F8`
- [MiHotAddBootDeferredDescriptorsDiscardable](../../init/C6/MiHotAddBootDeferredDescriptorsDiscardable_function_00C624E4.md) at `0x00C62588`

### Static image references
- `0x007F99AE` → RVA `0x00E38D00` (`.data`; read)
- `0x007F9A35` → RVA `0x00E38D10` (`.data`; read)
- `0x007F9A61` → RVA `0x00011C60` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **9**
  - `0x007F99E6` → [MiRestrictRangeToNode](../../text/40/MiRestrictRangeToNode_function_0040199C.md) (`PAGE` → `.text`)
  - `0x007F9A17` → [MiPageToNode](../../text/33/MiPageToNode_function_00338CD0.md) (`PAGE` → `.text`)
  - `0x007F9A26` → [MiGetClosestImplicitNode](../../text/3F/MiGetClosestImplicitNode_function_003F00AC.md) (`PAGE` → `.text`)
  - `0x007F9BAF` → [MiNodeLargeFreeZeroPages2](../../text/68/MiNodeLargeFreeZeroPages2_function_0068AD04.md) (`PAGE` → `.text`)
  - `0x007F9C0F` → [MiNodeLargeFreeZeroPages2](../../text/68/MiNodeLargeFreeZeroPages2_function_0068AD04.md) (`PAGE` → `.text`)
  - `0x007F9C33` → [MiNodeAvailablePages](../../text/3B/MiNodeAvailablePages_function_003BB920.md) (`PAGE` → `.text`)
  - `0x007F9C52` → [MiGetAvailablePagesExcludeSlists](../../text/48/MiGetAvailablePagesExcludeSlists_function_00483924.md) (`PAGE` → `.text`)
  - `0x007F9D19` → [MiGetLargestPageIndex](../../text/49/MiGetLargestPageIndex_function_0049F730.md) (`PAGE` → `.text`)
  - `0x007F9E0F` → [IoUpdateDumpPhysicalRanges](../../text/59/IoUpdateDumpPhysicalRanges_function_0059343C.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007F98D4  48 8B C4                        mov rax, rsp
007F98D7  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
007F98DB  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
007F98DF  48 89 48 08                     mov qword ptr [rax + 8], rcx
007F98E3  55                              push rbp
007F98E4  53                              push rbx
007F98E5  56                              push rsi
007F98E6  57                              push rdi
007F98E7  41 54                           push r12
007F98E9  41 55                           push r13
007F98EB  41 56                           push r14
007F98ED  41 57                           push r15
007F98EF  48 8D 68 B1                     lea rbp, [rax - 0x4f]
007F98F3  48 81 EC 98 00 00 00            sub rsp, 0x98
007F98FA  44 8B 75 77                     mov r14d, dword ptr [rbp + 0x77]
007F98FE  4C 8B D1                        mov r10, rcx
007F9901  C7 45 5F 00 30 00 00            mov dword ptr [rbp + 0x5f], 0x3000
007F9908  B9 00 02 00 00                  mov ecx, 0x200
007F990D  48 89 4D BF                     mov qword ptr [rbp - 0x41], rcx
007F9911  4D 8B F8                        mov r15, r8
007F9914  C7 45 B7 01 00 00 00            mov dword ptr [rbp - 0x49], 1
007F991B  4D 85 C9                        test r9, r9
007F991E  74 1F                           je 0x1407f993f
007F9920  45 33 C0                        xor r8d, r8d
007F9923  B8 00 00 04 00                  mov eax, 0x40000
007F9928  41 0F BA EE 15                  bts r14d, 0x15
007F992D  4C 3B C8                        cmp r9, rax
007F9930  41 0F 95 C0                     setne r8b
007F9934  0F 45 C1                        cmovne eax, ecx
007F9937  44 89 45 B7                     mov dword ptr [rbp - 0x49], r8d
007F993B  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
007F993F  48 8B 02                        mov rax, qword ptr [rdx]
007F9942  33 FF                           xor edi, edi
007F9944  49 8B 1F                        mov rbx, qword ptr [r15]
007F9947  48 89 45 C7                     mov qword ptr [rbp - 0x39], rax
007F994B  48 89 5D AF                     mov qword ptr [rbp - 0x51], rbx
007F994F  41 0F BA E6 10                  bt r14d, 0x10
007F9954  73 56                           jae 0x1407f99ac
007F9956  41 81 CE 00 60 20 00            or r14d, 0x206000
007F995D  48 81 E3 00 F0 FF FF            and rbx, 0xfffffffffffff000
007F9964  48 21 7C 24 20                  and qword ptr [rsp + 0x20], rdi
007F9969  4C 8D 45 AF                     lea r8, [rbp - 0x51]
007F996D  45 8B CE                        mov r9d, r14d
007F9970  48 89 5D AF                     mov qword ptr [rbp - 0x51], rbx
007F9974  48 8D 55 C7                     lea rdx, [rbp - 0x39]
007F9978  49 8B CA                        mov rcx, r10
007F997B  E8 7C FC FF FF                  call 0x1407f95fc
007F9980  8B F0                           mov esi, eax
007F9982  85 C0                           test eax, eax
007F9984  79 1A                           jns 0x1407f99a0
007F9986  41 0F BA E6 0E                  bt r14d, 0xe
007F998B  73 0B                           jae 0x1407f9998
007F998D  4C 8B 55 57                     mov r10, qword ptr [rbp + 0x57]
007F9991  41 0F BA F6 0E                  btr r14d, 0xe
007F9996  EB CC                           jmp 0x1407f9964
007F9998  49 21 3F                        and qword ptr [r15], rdi
007F999B  E9 76 04 00 00                  jmp 0x1407f9e16
007F99A0  48 8B 45 AF                     mov rax, qword ptr [rbp - 0x51]
007F99A4  49 89 07                        mov qword ptr [r15], rax
007F99A7  E9 53 04 00 00                  jmp 0x1407f9dff
007F99AC  33 C0                           xor eax, eax
007F99AE  48 8D 0D 4B F3 63 00            lea rcx, [rip + 0x63f34b]
007F99B5  48 89 45 D7                     mov qword ptr [rbp - 0x29], rax
007F99B9  49 8B C2                        mov rax, r10
007F99BC  48 2B C1                        sub rax, rcx
007F99BF  48 F7 D8                        neg rax
007F99C2  45 1B E4                        sbb r12d, r12d
007F99C5  41 83 E4 02                     and r12d, 2
007F99C9  45 33 ED                        xor r13d, r13d
007F99CC  45 8B FC                        mov r15d, r12d
007F99CF  48 8B 45 C7                     mov rax, qword ptr [rbp - 0x39]
007F99D3  48 8B 55 AF                     mov rdx, qword ptr [rbp - 0x51]
007F99D7  48 C1 E8 0C                     shr rax, 0xc
007F99DB  48 8B C8                        mov rcx, rax
007F99DE  48 C1 EA 0C                     shr rdx, 0xc
007F99E2  48 89 45 A7                     mov qword ptr [rbp - 0x59], rax
007F99E6  E8 B1 7F C0 FF                  call 0x14040199c
007F99EB  48 8B F0                        mov rsi, rax
007F99EE  48 3B 45 6F                     cmp rax, qword ptr [rbp + 0x6f]
007F99F2  0F 82 F1 03 00 00               jb 0x1407f9de9
007F99F8  48 8B 45 A7                     mov rax, qword ptr [rbp - 0x59]
007F99FC  BA 00 00 10 00                  mov edx, 0x100000
007F9A01  48 3B C2                        cmp rax, rdx
007F9A04  73 0E                           jae 0x1407f9a14
007F9A06  48 8D 0C 06                     lea rcx, [rsi + rax]
007F9A0A  48 3B CA                        cmp rcx, rdx
007F9A0D  76 05                           jbe 0x1407f9a14
007F9A0F  8B F2                           mov esi, edx
007F9A11  48 2B F0                        sub rsi, rax
007F9A14  48 8B C8                        mov rcx, rax
007F9A17  E8 B4 F2 B3 FF                  call 0x140338cd0
007F9A1C  41 BB 01 00 00 00               mov r11d, 1
007F9A22  41 8D 0C 03                     lea ecx, [r11 + rax]
007F9A26  E8 81 66 BF FF                  call 0x1403f00ac
007F9A2B  41 2B C3                        sub eax, r11d
007F9A2E  4C 69 D0 80 DF 00 00            imul r10, rax, 0xdf80
007F9A35  4C 03 15 D4 F2 63 00            add r10, qword ptr [rip + 0x63f2d4]
007F9A3C  4C 89 55 EF                     mov qword ptr [rbp - 0x11], r10
007F9A40  45 85 ED                        test r13d, r13d
007F9A43  78 60                           js 0x1407f9aa5
007F9A45  4C 8B 4D A7                     mov r9, qword ptr [rbp - 0x59]
007F9A49  48 8D 05 B0 F2 63 00            lea rax, [rip + 0x63f2b0]
007F9A50  45 33 FF                        xor r15d, r15d
007F9A53  45 8B C3                        mov r8d, r11d
007F9A56  48 39 45 57                     cmp qword ptr [rbp + 0x57], rax
007F9A5A  45 0F 45 FC                     cmovne r15d, r12d
007F9A5E  41 8B C0                        mov eax, r8d
007F9A61  48 8D 0D F8 81 81 FF            lea rcx, [rip - 0x7e7e08]
007F9A68  33 D2                           xor edx, edx
007F9A6A  48 8B 0C C1                     mov rcx, qword ptr [rcx + rax*8]
007F9A6E  49 8B C1                        mov rax, r9
007F9A71  48 F7 F1                        div rcx
007F9A74  48 85 D2                        test rdx, rdx
007F9A77  75 19                           jne 0x1407f9a92
007F9A79  48 3B F1                        cmp rsi, rcx
007F9A7C  72 1E                           jb 0x1407f9a9c
007F9A7E  48 8D 41 FF                     lea rax, [rcx - 1]
007F9A82  48 F7 D0                        not rax
007F9A85  48 23 F0                        and rsi, rax
007F9A88  45 85 C0                        test r8d, r8d
007F9A8B  74 0F                           je 0x1407f9a9c
007F9A8D  41 FF C8                        dec r8d
007F9A90  EB CC                           jmp 0x1407f9a5e
007F9A92  48 2B CA                        sub rcx, rdx
007F9A95  48 3B F1                        cmp rsi, rcx
007F9A98  48 0F 47 F1                     cmova rsi, rcx
007F9A9C  4C 8B 4D BF                     mov r9, qword ptr [rbp - 0x41]
007F9AA0  E9 B4 00 00 00                  jmp 0x1407f9b59
007F9AA5  48 8B 45 D7                     mov rax, qword ptr [rbp - 0x29]
007F9AA9  48 8D 15 50 F2 63 00            lea rdx, [rip + 0x63f250]
007F9AB0  4C 8B 4D BF                     mov r9, qword ptr [rbp - 0x41]
007F9AB4  48 8B F0                        mov rsi, rax
007F9AB7  48 8B 4D 57                     mov rcx, qword ptr [rbp + 0x57]
007F9ABB  49 3B C1                        cmp rax, r9
007F9ABE  76 22                           jbe 0x1407f9ae2
007F9AC0  48 3B CA                        cmp rcx, rdx
007F9AC3  75 05                           jne 0x1407f9aca
007F9AC5  49 8B F1                        mov rsi, r9
007F9AC8  EB 18                           jmp 0x1407f9ae2
007F9ACA  48 D1 E8                        shr rax, 1
007F9ACD  49 8D 71 FF                     lea rsi, [r9 - 1]
007F9AD1  48 F7 D6                        not rsi
007F9AD4  48 23 F0                        and rsi, rax
007F9AD7  48 8B 45 D7                     mov rax, qword ptr [rbp - 0x29]
007F9ADB  49 3B F1                        cmp rsi, r9
007F9ADE  49 0F 42 F1                     cmovb rsi, r9
007F9AE2  45 85 E4                        test r12d, r12d
007F9AE5  75 20                           jne 0x1407f9b07
007F9AE7  4C 8B 45 A7                     mov r8, qword ptr [rbp - 0x59]
007F9AEB  49 3B C1                        cmp rax, r9
007F9AEE  76 05                           jbe 0x1407f9af5
007F9AF0  45 33 FF                        xor r15d, r15d
007F9AF3  EB 68                           jmp 0x1407f9b5d
007F9AF5  49 81 F8 00 00 10 00            cmp r8, 0x100000
007F9AFC  45 1B FF                        sbb r15d, r15d
007F9AFF  41 F7 DF                        neg r15d
007F9B02  45 03 FB                        add r15d, r11d
007F9B05  EB 56                           jmp 0x1407f9b5d
007F9B07  45 3B E3                        cmp r12d, r11d
007F9B0A  75 0C                           jne 0x1407f9b18
007F9B0C  4C 3B C8                        cmp r9, rax
007F9B0F  45 1B FF                        sbb r15d, r15d
007F9B12  41 83 C7 02                     add r15d, 2
007F9B16  EB 41                           jmp 0x1407f9b59
007F9B18  41 83 FC 02                     cmp r12d, 2
007F9B1C  75 20                           jne 0x1407f9b3e
007F9B1E  4C 8B 45 A7                     mov r8, qword ptr [rbp - 0x59]
007F9B22  48 3B CA                        cmp rcx, rdx
007F9B25  75 07                           jne 0x1407f9b2e
007F9B27  45 8D 7C 24 01                  lea r15d, [r12 + 1]
007F9B2C  EB 2F                           jmp 0x1407f9b5d
007F9B2E  4C 3B C8                        cmp r9, rax
007F9B31  45 1B FF                        sbb r15d, r15d
007F9B34  41 83 E7 FE                     and r15d, 0xfffffffe
007F9B38  41 83 C7 04                     add r15d, 4
007F9B3C  EB 1F                           jmp 0x1407f9b5d
007F9B3E  41 83 FC 03                     cmp r12d, 3
007F9B42  74 0F                           je 0x1407f9b53
007F9B44  41 83 FC 04                     cmp r12d, 4
007F9B48  75 0F                           jne 0x1407f9b59
007F9B4A  49 3B C1                        cmp rax, r9
007F9B4D  0F 86 9C 02 00 00               jbe 0x1407f9def
007F9B53  41 BF 04 00 00 00               mov r15d, 4
007F9B59  4C 8B 45 A7                     mov r8, qword ptr [rbp - 0x59]
007F9B5D  4D 8B E3                        mov r12, r11
007F9B60  45 33 ED                        xor r13d, r13d
007F9B63  45 3B EB                        cmp r13d, r11d
007F9B66  77 2B                           ja 0x1407f9b93
007F9B68  33 D2                           xor edx, edx
007F9B6A  48 8D 0D EF 80 81 FF            lea rcx, [rip - 0x7e7f11]
007F9B71  4A 8B 0C E9                     mov rcx, qword ptr [rcx + r13*8]
007F9B75  49 8B C0                        mov rax, r8
007F9B78  48 F7 F1                        div rcx
007F9B7B  48 85 D2                        test rdx, rdx
007F9B7E  75 0B                           jne 0x1407f9b8b
007F9B80  48 8B C6                        mov rax, rsi
007F9B83  48 F7 F1                        div rcx
007F9B86  48 85 D2                        test rdx, rdx
007F9B89  74 05                           je 0x1407f9b90
007F9B8B  45 03 EB                        add r13d, r11d
007F9B8E  EB D3                           jmp 0x1407f9b63
007F9B90  4C 8B E1                        mov r12, rcx
007F9B93  41 81 E6 FF 4F FF FF            and r14d, 0xffff4fff
007F9B9A  49 3B F1                        cmp rsi, r9
007F9B9D  0F 82 5E 01 00 00               jb 0x1407f9d01
007F9BA3  33 C9                           xor ecx, ecx
007F9BA5  45 85 FF                        test r15d, r15d
007F9BA8  75 40                           jne 0x1407f9bea
007F9BAA  33 D2                           xor edx, edx
007F9BAC  49 8B CA                        mov rcx, r10
007F9BAF  E8 50 11 E9 FF                  call 0x14068ad04
007F9BB4  48 8B C8                        mov rcx, rax
007F9BB7  48 85 C0                        test rax, rax
007F9BBA  75 2E                           jne 0x1407f9bea
007F9BBC  48 8B 45 A7                     mov rax, qword ptr [rbp - 0x59]
007F9BC0  48 03 C6                        add rax, rsi
007F9BC3  48 3D 00 00 10 00               cmp rax, 0x100000
007F9BC9  76 13                           jbe 0x1407f9bde
007F9BCB  48 8B 45 BF                     mov rax, qword ptr [rbp - 0x41]
007F9BCF  48 3B F0                        cmp rsi, rax
007F9BD2  76 0A                           jbe 0x1407f9bde
007F9BD4  44 8B 6D B7                     mov r13d, dword ptr [rbp - 0x49]
007F9BD8  48 8B F0                        mov rsi, rax
007F9BDB  4C 8B E0                        mov r12, rax
007F9BDE  41 BF 01 00 00 00               mov r15d, 1
007F9BE4  48 89 75 E7                     mov qword ptr [rbp - 0x19], rsi
007F9BE8  EB 1C                           jmp 0x1407f9c06
007F9BEA  41 8B D7                        mov edx, r15d
007F9BED  4C 8B C6                        mov r8, rsi
007F9BF0  45 85 FF                        test r15d, r15d
007F9BF3  74 68                           je 0x1407f9c5d
007F9BF5  48 8B C6                        mov rax, rsi
007F9BF8  83 FA 03                        cmp edx, 3
007F9BFB  74 60                           je 0x1407f9c5d
007F9BFD  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
007F9C01  83 FA 01                        cmp edx, 1
007F9C04  75 14                           jne 0x1407f9c1a
007F9C06  48 8B 4D EF                     mov rcx, qword ptr [rbp - 0x11]
007F9C0A  BA 01 00 00 00                  mov edx, 1
007F9C0F  E8 F0 10 E9 FF                  call 0x14068ad04
007F9C14  4C 8B 45 E7                     mov r8, qword ptr [rbp - 0x19]
007F9C18  EB 40                           jmp 0x1407f9c5a
007F9C1A  4C 8B C0                        mov r8, rax
007F9C1D  48 8D 05 DC F0 63 00            lea rax, [rip + 0x63f0dc]
007F9C24  48 39 45 57                     cmp qword ptr [rbp + 0x57], rax
007F9C28  74 33                           je 0x1407f9c5d
007F9C2A  83 FA 02                        cmp edx, 2
007F9C2D  75 20                           jne 0x1407f9c4f
007F9C2F  48 8B 4D EF                     mov rcx, qword ptr [rbp - 0x11]
007F9C33  E8 E8 1C BC FF                  call 0x1403bb920
007F9C38  48 8B C8                        mov rcx, rax
007F9C3B  48 83 F8 06                     cmp rax, 6
007F9C3F  73 34                           jae 0x1407f9c75
007F9C41  33 C0                           xor eax, eax
007F9C43  45 33 ED                        xor r13d, r13d
007F9C46  44 8D 60 04                     lea r12d, [rax + 4]
007F9C4A  E9 4A 01 00 00                  jmp 0x1407f9d99
007F9C4F  48 8B C8                        mov rcx, rax
007F9C52  E8 CD 9C C8 FF                  call 0x140483924
007F9C57  4C 8B C6                        mov r8, rsi
007F9C5A  48 8B C8                        mov rcx, rax
007F9C5D  48 85 C9                        test rcx, rcx
007F9C60  75 13                           jne 0x1407f9c75
007F9C62  48 8B 45 BF                     mov rax, qword ptr [rbp - 0x41]
007F9C66  48 3B F0                        cmp rsi, rax
007F9C69  49 0F 44 C0                     cmove rax, r8
007F9C6D  48 8B F0                        mov rsi, rax
007F9C70  E9 8C 00 00 00                  jmp 0x1407f9d01
007F9C75  41 BB 01 00 00 00               mov r11d, 1
007F9C7B  48 8D 15 DE 7F 81 FF            lea rdx, [rip - 0x7e8022]
007F9C82  4B 8D 04 64                     lea rax, [r12 + r12*2]
007F9C86  48 C1 E0 04                     shl rax, 4
007F9C8A  48 C1 E8 0C                     shr rax, 0xc
007F9C8E  48 3B C8                        cmp rcx, rax
007F9C91  73 14                           jae 0x1407f9ca7
007F9C93  44 3B 6D B7                     cmp r13d, dword ptr [rbp - 0x49]
007F9C97  73 09                           jae 0x1407f9ca2
007F9C99  45 03 EB                        add r13d, r11d
007F9C9C  4E 8B 24 EA                     mov r12, qword ptr [rdx + r13*8]
007F9CA0  EB E0                           jmp 0x1407f9c82
007F9CA2  4D 8B C3                        mov r8, r11
007F9CA5  EB 1A                           jmp 0x1407f9cc1
007F9CA7  4D 8B C4                        mov r8, r12
007F9CAA  4D 3B E3                        cmp r12, r11
007F9CAD  74 12                           je 0x1407f9cc1
007F9CAF  48 8D 05 4A F0 63 00            lea rax, [rip + 0x63f04a]
007F9CB6  48 39 45 57                     cmp qword ptr [rbp + 0x57], rax
007F9CBA  75 05                           jne 0x1407f9cc1
007F9CBC  41 0F BA EE 0F                  bts r14d, 0xf
007F9CC1  48 C1 E1 0C                     shl rcx, 0xc
007F9CC5  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
007F9CCF  48 F7 E1                        mul rcx
007F9CD2  48 8B 4D 6F                     mov rcx, qword ptr [rbp + 0x6f]
007F9CD6  49 8D 40 FF                     lea rax, [r8 - 1]
007F9CDA  48 C1 EA 05                     shr rdx, 5
007F9CDE  48 F7 D0                        not rax
007F9CE1  48 23 D0                        and rdx, rax
007F9CE4  48 85 C9                        test rcx, rcx
007F9CE7  74 11                           je 0x1407f9cfa
007F9CE9  48 8D 41 FF                     lea rax, [rcx - 1]
007F9CED  48 F7 D0                        not rax
007F9CF0  48 23 D0                        and rdx, rax
007F9CF3  48 3B D1                        cmp rdx, rcx
007F9CF6  48 0F 42 D1                     cmovb rdx, rcx
007F9CFA  48 3B F2                        cmp rsi, rdx
007F9CFD  48 0F 47 F2                     cmova rsi, rdx
007F9D01  45 84 F6                        test r14b, r14b
007F9D04  78 48                           js 0x1407f9d4e
007F9D06  48 8B 4D A7                     mov rcx, qword ptr [rbp - 0x59]
007F9D0A  B8 FF 01 00 00                  mov eax, 0x1ff
007F9D0F  48 85 C8                        test rax, rcx
007F9D12  75 3A                           jne 0x1407f9d4e
007F9D14  48 85 F0                        test rax, rsi
007F9D17  75 35                           jne 0x1407f9d4e
007F9D19  E8 12 5A CA FF                  call 0x14049f730
007F9D1E  85 C0                           test eax, eax
007F9D20  75 1D                           jne 0x1407f9d3f
007F9D22  B8 FF FF 03 00                  mov eax, 0x3ffff
007F9D27  48 85 C8                        test rax, rcx
007F9D2A  75 13                           jne 0x1407f9d3f
007F9D2C  48 85 F0                        test rax, rsi
007F9D2F  8B 45 5F                        mov eax, dword ptr [rbp + 0x5f]
007F9D32  75 0E                           jne 0x1407f9d42
007F9D34  B9 00 20 00 00                  mov ecx, 0x2000
007F9D39  85 C1                           test ecx, eax
007F9D3B  74 05                           je 0x1407f9d42
007F9D3D  EB 0C                           jmp 0x1407f9d4b
007F9D3F  8B 45 5F                        mov eax, dword ptr [rbp + 0x5f]
007F9D42  B9 00 10 00 00                  mov ecx, 0x1000
007F9D47  85 C1                           test ecx, eax
007F9D49  74 03                           je 0x1407f9d4e
007F9D4B  44 0B F1                        or r14d, ecx
007F9D4E  48 8B 4D 57                     mov rcx, qword ptr [rbp + 0x57]
007F9D52  4C 8D 45 AF                     lea r8, [rbp - 0x51]
007F9D56  41 8B C6                        mov eax, r14d
007F9D59  48 89 75 D7                     mov qword ptr [rbp - 0x29], rsi
007F9D5D  0F BA F0 0E                     btr eax, 0xe
007F9D61  48 8D 55 C7                     lea rdx, [rbp - 0x39]
007F9D65  41 0F BA EE 0E                  bts r14d, 0xe
007F9D6A  41 83 FF 02                     cmp r15d, 2
007F9D6E  44 0F 4F F0                     cmovg r14d, eax
007F9D72  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
007F9D78  48 C1 E6 0C                     shl rsi, 0xc
007F9D7C  45 8B CE                        mov r9d, r14d
007F9D7F  48 89 75 AF                     mov qword ptr [rbp - 0x51], rsi
007F9D83  45 8B E6                        mov r12d, r14d
007F9D86  E8 71 F8 FF FF                  call 0x1407f95fc
007F9D8B  44 8B E8                        mov r13d, eax
007F9D8E  85 C0                           test eax, eax
007F9D90  78 20                           js 0x1407f9db2
007F9D92  48 8B 45 AF                     mov rax, qword ptr [rbp - 0x51]
007F9D96  45 8B E7                        mov r12d, r15d
007F9D99  48 01 45 C7                     add qword ptr [rbp - 0x39], rax
007F9D9D  48 03 F8                        add rdi, rax
007F9DA0  48 8B CB                        mov rcx, rbx
007F9DA3  48 2B CF                        sub rcx, rdi
007F9DA6  48 89 4D AF                     mov qword ptr [rbp - 0x51], rcx
007F9DAA  0F 85 1F FC FF FF               jne 0x1407f99cf
007F9DB0  EB 3D                           jmp 0x1407f9def
007F9DB2  3D 9A 00 00 C0                  cmp eax, 0xc000009a
007F9DB7  74 28                           je 0x1407f9de1
007F9DB9  3D 2D 01 00 C0                  cmp eax, 0xc000012d
007F9DBE  74 21                           je 0x1407f9de1
007F9DC0  3D BB 00 00 C0                  cmp eax, 0xc00000bb
007F9DC5  75 28                           jne 0x1407f9def
007F9DC7  41 0F BA E4 0D                  bt r12d, 0xd
007F9DCC  73 07                           jae 0x1407f9dd5
007F9DCE  0F BA 75 5F 0D                  btr dword ptr [rbp + 0x5f], 0xd
007F9DD3  EB 0C                           jmp 0x1407f9de1
007F9DD5  41 0F BA E4 0C                  bt r12d, 0xc
007F9DDA  73 13                           jae 0x1407f9def
007F9DDC  0F BA 75 5F 0C                  btr dword ptr [rbp + 0x5f], 0xc
007F9DE1  45 8B E7                        mov r12d, r15d
007F9DE4  E9 E6 FB FF FF                  jmp 0x1407f99cf
007F9DE9  41 BD 18 00 00 C0               mov r13d, 0xc0000018
007F9DEF  48 8B 45 67                     mov rax, qword ptr [rbp + 0x67]
007F9DF3  33 F6                           xor esi, esi
007F9DF5  48 85 FF                        test rdi, rdi
007F9DF8  41 0F 44 F5                     cmove esi, r13d
007F9DFC  48 89 38                        mov qword ptr [rax], rdi
007F9DFF  83 7D 7F 00                     cmp dword ptr [rbp + 0x7f], 0
007F9E03  75 0F                           jne 0x1407f9e14
007F9E05  85 F6                           test esi, esi
007F9E07  78 0B                           js 0x1407f9e14
007F9E09  41 F6 C6 02                     test r14b, 2
007F9E0D  75 05                           jne 0x1407f9e14
007F9E0F  E8 28 96 D9 FF                  call 0x14059343c
007F9E14  8B C6                           mov eax, esi
007F9E16  48 81 C4 98 00 00 00            add rsp, 0x98
007F9E1D  41 5F                           pop r15
007F9E1F  41 5E                           pop r14
007F9E21  41 5D                           pop r13
007F9E23  41 5C                           pop r12
007F9E25  5F                              pop rdi
007F9E26  5E                              pop rsi
007F9E27  5B                              pop rbx
007F9E28  5D                              pop rbp
007F9E29  C3                              ret
007F9E2A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiAddPhysicalMemoryChunks(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_mB8;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (152);
    *(unsigned int *)(v_rsp - 79 + 95) = 0x3000ULL;
    *(unsigned __int64 *)(v_rsp - 79 - 65) = 512;
    *(unsigned int *)(v_rsp - 79 - 73) = 1;
    result = v_rsp;
    if (a4 != 0) {
        a3 = 0;
        result = 0x40000ULL;
        a3 = (a4 != result) ? 1 : 0;
        if (a4 != result) { result = 512; }
        *(unsigned int *)(v_rsp - 79 - 73) = (unsigned int)(a3);
        *(unsigned __int64 *)(v_rsp - 79 - 65) = result;
    }
    v_rdi = 0;
    *(unsigned __int64 *)(v_rsp - 79 - 57) = *(unsigned __int64 *)(a2);
    *(unsigned __int64 *)(v_rsp - 79 - 81) = *(unsigned __int64 *)(a3);
    if (condition_is_above_or_equal) goto loc_007F99AC;
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 79 + 119))) | (0x206000ULL));
    v_rbx = (*(unsigned __int64 *)(a3)) & (0xFFFFFFFFFFFFF000ULL);
loc_007F9964:
    *(unsigned __int64 *)(v_rsp - 79 - 81) = v_rbx;
    result = MiAddPhysicalMemory(a1, v_rsp - 79 - 57, v_rsp - 79 - 81, (unsigned int)((unsigned int)(v_r14)));
    if (!sign_flag) goto loc_007F99A0;
    if (condition_is_above_or_equal) goto loc_007F9998;
    goto loc_007F9964;
loc_007F9998:
    goto loc_007F9E16;
loc_007F99A0:
    *(unsigned __int64 *)(a3) = *(unsigned __int64 *)(v_rsp - 79 - 81);
    goto loc_007F9DFF;
loc_007F99AC:
    result = 0;
    *(unsigned __int64 *)(v_rsp - 79 - 41) = 0;
    result = (*(unsigned __int64 *)(v_rsp - 79 + 87)) - (v_rip + 6550347);
    result = -(result);
    v_r12 = (unsigned int)((v_r12) & (2));
    v_r13 = 0;
loc_007F99CF:
    result = (*(unsigned __int64 *)(v_rsp - 79 - 57)) >> (12);
    a2 = (*(unsigned __int64 *)(v_rsp - 79 - 81)) >> (12);
    *(unsigned __int64 *)(v_rsp - 79 - 89) = result;
    result = MiRestrictRangeToNode(result, a2, v_rsp - 79 - 81, (unsigned int)((unsigned int)(v_r14)));
    if (result < (*(unsigned __int64 *)(v_rsp - 79 + 111))) goto loc_007F9DE9;
    if ((*(unsigned __int64 *)(v_rsp - 79 - 89)) >= ((unsigned int)(0x100000ULL))) goto loc_007F9A14;
    v_rsi = result;
    if ((result + *(unsigned __int64 *)(v_rsp - 79 - 89) * 1) >= = ((unsigned int)(0x100000ULL))) {
        v_rsi = (unsigned int)((unsigned int)(0x100000ULL));
        v_rsi = (v_rsi) - (*(unsigned __int64 *)(v_rsp - 79 - 89));
    }
    result = MiPageToNode(*(unsigned __int64 *)(v_rsp - 79 - 89), (unsigned int)(0x100000ULL), v_rsp - 79 - 81, (unsigned int)((unsigned int)(v_r14)));
    result = MiGetClosestImplicitNode(1 + result * 1, (unsigned int)(0x100000ULL), v_rsp - 79 - 81, (unsigned int)((unsigned int)(v_r14)));
    result = (unsigned int)((result) - (1));
    v_r10 = (*(unsigned __int64 *)(v_rsp - 79 + 87)) * (result);
    v_r10 = (v_r10) + (*(unsigned __int64 *)(v_rip + 6550228));
    *(unsigned __int64 *)(v_rsp - 79 - 17) = v_r10;
    if (sign_flag) goto loc_007F9AA5;
    v_r15 = 0;
    if ((*(unsigned __int64 *)(v_rsp - 79 + 87)) != (v_rip + 6550192)) { v_r15 = (unsigned int)(v_r12); }
loc_007F9A5E:
    a2 = 0;
    if (0 != 0) goto loc_007F9A92;
    if (v_rsi < (*(unsigned __int64 *)(v_rip - 8289800 + 1 * 8))) goto loc_007F9A9C;
    result = ~(*(unsigned __int64 *)(v_rip - 8289800 + 1 * 8) - 1);
    v_rsi = (v_rsi) & (result);
    if (1 == 0) goto loc_007F9A9C;
    a3 = (unsigned int)((1) - 1);
    goto loc_007F9A5E;
loc_007F9A92:
    a1 = (*(unsigned __int64 *)(v_rip - 8289800 + 1 * 8)) - (0);
    if (v_rsi > a1) { v_rsi = a1; }
loc_007F9A9C:
    goto loc_007F9B59;
loc_007F9AA5:
    if ((*(unsigned __int64 *)(v_rsp - 79 - 41)) <= (*(unsigned __int64 *)(v_rsp - 79 - 65))) goto loc_007F9AE2;
    if ((*(unsigned __int64 *)(v_rsp - 79 + 87)) != (v_rip + 6550096)) goto loc_007F9ACA;
    goto loc_007F9AE2;
loc_007F9ACA:
    result = (*(unsigned __int64 *)(v_rsp - 79 - 41)) >> (1);
    v_rsi = ~(*(unsigned __int64 *)(v_rsp - 79 - 65) - 1);
    v_rsi = (v_rsi) & (result);
    if (v_rsi < (*(unsigned __int64 *)(v_rsp - 79 - 65))) { v_rsi = *(unsigned __int64 *)(v_rsp - 79 - 65); }
loc_007F9AE2:
    if ((unsigned int)(v_r12) != 0) goto loc_007F9B07;
    if ((*(unsigned __int64 *)(v_rsp - 79 - 41)) <= (*(unsigned __int64 *)(v_rsp - 79 - 65))) goto loc_007F9AF5;
    v_r15 = 0;
    goto loc_007F9B5D;
loc_007F9AF5:
    v_r15 = (unsigned int)(-(v_r15));
    v_r15 = (unsigned int)((v_r15) + (1));
    goto loc_007F9B5D;
loc_007F9B07:
    if (((unsigned int)(v_r12)) != 1) goto loc_007F9B18;
    v_r15 = (unsigned int)((v_r15) + (2));
    goto loc_007F9B59;
loc_007F9B18:
    if (((unsigned int)(v_r12)) != 2) goto loc_007F9B3E;
    if ((*(unsigned __int64 *)(v_rsp - 79 + 87)) != (v_rip + 6550096)) goto loc_007F9B2E;
    goto loc_007F9B5D;
loc_007F9B2E:
    v_r15 = (unsigned int)((v_r12 + 1) & (0xFFFFFFFEULL));
    v_r15 = (unsigned int)((v_r15) + (4));
    goto loc_007F9B5D;
loc_007F9B3E:
    if (((unsigned int)(v_r12)) == 3) goto loc_007F9B53;
    if (((unsigned int)(v_r12)) != 4) goto loc_007F9B59;
    if ((*(unsigned __int64 *)(v_rsp - 79 - 41)) <= (*(unsigned __int64 *)(v_rsp - 79 - 65))) goto loc_007F9DEF;
loc_007F9B53:
loc_007F9B59:
loc_007F9B5D:
    v_r13 = 0;
loc_007F9B63:
    if (0 > 1) goto loc_007F9B93;
    a2 = 0;
    if (0 != 0) goto loc_007F9B8B;
    if (0 == 0) goto loc_007F9B90;
loc_007F9B8B:
    v_r13 = (unsigned int)((v_r13) + (1));
    goto loc_007F9B63;
loc_007F9B90:
loc_007F9B93:
    v_r14 = (unsigned int)((v_r14) & (0xFFFF4FFFULL));
    if (v_rsi < (*(unsigned __int64 *)(v_rsp - 79 - 65))) goto loc_007F9D01;
    a1 = 0;
    if (4 != 0) goto loc_007F9BEA;
    a2 = 0;
    result = MiNodeLargeFreeZeroPages2(v_r10, a2, *(unsigned __int64 *)(v_rsp - 79 - 89), *(unsigned __int64 *)(v_rsp - 79 - 65));
    if (result != 0) goto loc_007F9BEA;
    result = (*(unsigned __int64 *)(v_rsp - 79 - 89)) + (v_rsi);
    if (result <= 0x100000ULL) goto loc_007F9BDE;
    v_r12 = *(unsigned __int64 *)(v_rip - 8290065 + v_r13 * 8);
    if (v_rsi >= = (*(unsigned __int64 *)(v_rsp - 79 - 65))) {
        v_r13 = *(unsigned int *)(v_rsp - 79 - 73);
        v_rsi = *(unsigned __int64 *)(v_rsp - 79 - 65);
        v_r12 = *(unsigned __int64 *)(v_rsp - 79 - 65);
    }
    *(unsigned __int64 *)(v_rsp - 79 - 25) = v_rsi;
    goto loc_007F9C06;
loc_007F9BEA:
    if (1 == 0) goto loc_007F9C5D;
    if (1 == 3) goto loc_007F9C5D;
    *(unsigned __int64 *)(v_rsp - 79 - 25) = v_rsi;
    if (1 != 1) goto loc_007F9C1A;
loc_007F9C06:
    result = MiNodeLargeFreeZeroPages2(*(unsigned __int64 *)(v_rsp - 79 - 17), 1, v_rsi, *(unsigned __int64 *)(v_rsp - 79 - 65));
    goto loc_007F9C5A;
loc_007F9C1A:
    if ((*(unsigned __int64 *)(v_rsp - 79 + 87)) == (v_rip + 6549724)) goto loc_007F9C5D;
    if (1 != 2) goto loc_007F9C4F;
    result = MiNodeAvailablePages(*(unsigned __int64 *)(v_rsp - 79 - 17), 1, result, *(unsigned __int64 *)(v_rsp - 79 - 65));
    if (result >= 6) goto loc_007F9C75;
    result = 0;
    v_r13 = 0;
    goto loc_007F9D99;
loc_007F9C4F:
    result = MiGetAvailablePagesExcludeSlists(0, 1, result, *(unsigned __int64 *)(v_rsp - 79 - 65));
loc_007F9C5A:
loc_007F9C5D:
    if (result != 0) goto loc_007F9C75;
    result = *(unsigned __int64 *)(v_rsp - 79 - 65);
    if (v_rsi == (*(unsigned __int64 *)(v_rsp - 79 - 65))) { result = v_rsi; }
    goto loc_007F9D01;
loc_007F9C75:
loc_007F9C82:
    result = (result + 4 + result + 4 * 2) << (4);
    result = (result) >> (12);
    if (result >= result) goto loc_007F9CA7;
    if (0 >= (*(unsigned int *)(v_rsp - 79 - 73))) goto loc_007F9CA2;
    v_r13 = (unsigned int)((v_r13) + (1));
    goto loc_007F9C82;
loc_007F9CA2:
    goto loc_007F9CC1;
loc_007F9CA7:
    if ((*(unsigned __int64 *)(v_rip - 8290338 + v_r13 * 8)) == 1) goto loc_007F9CC1;
    if ((*(unsigned __int64 *)(v_rsp - 79 + 87)) == (v_rip + 6549578)) {
    }
    a1 = (result) << (12);
    a2 = (v_rip - 8290338) >> (5);
    result = ~(*(unsigned __int64 *)(v_rip - 8290338 + v_r13 * 8) - 1);
    a2 = (a2) & (result);
    if (*(unsigned __int64 *)(v_rsp - 79 + 111) != 0) {
        result = *(unsigned __int64 *)(v_rsp - 79 + 111) - 1;
        result = ~(result);
        a2 = (a2) & (result);
        if (a2 < (*(unsigned __int64 *)(v_rsp - 79 + 111))) { a2 = *(unsigned __int64 *)(v_rsp - 79 + 111); }
    }
    v_rsi = result;
    if (result > a2) { v_rsi = a2; }
loc_007F9D01:
    if (sign_flag) goto loc_007F9D4E;
    if (((511) & (*(unsigned __int64 *)(v_rsp - 79 - 89))) != 0) goto loc_007F9D4E;
    if (((511) & (v_rsi)) != 0) goto loc_007F9D4E;
    result = MiGetLargestPageIndex(*(unsigned __int64 *)(v_rsp - 79 - 89), a2, *(unsigned __int64 *)(v_rip - 8290338 + v_r13 * 8), *(unsigned __int64 *)(v_rsp - 79 - 65));
    if ((unsigned int)(result) != 0) goto loc_007F9D3F;
    if ((((unsigned int)(0x3FFFFULL)) & (*(unsigned __int64 *)(v_rsp - 79 - 89))) != 0) goto loc_007F9D3F;
    if ((((unsigned int)(0x3FFFFULL)) & (v_rsi)) != 0) goto loc_007F9D42;
    if ((((unsigned int)((unsigned int)(0x2000ULL))) & ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 + 95))))) == 0) goto loc_007F9D42;
    goto loc_007F9D4B;
loc_007F9D3F:
loc_007F9D42:
    if ((((unsigned int)((unsigned int)(0x1000ULL))) & ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 + 95))))) != 0) {
        v_r14 = (unsigned int)((v_r14) | ((unsigned int)((unsigned int)(0x1000ULL))));
    }
    *(unsigned __int64 *)(v_rsp - 79 - 41) = v_rsi;
    if (1 > 2) { v_r14 = (unsigned int)((unsigned int)((unsigned int)(v_r14))); }
    v_rsi = (v_rsi) << (12);
    *(unsigned __int64 *)(v_rsp - 79 - 81) = v_rsi;
    result = MiAddPhysicalMemory(*(unsigned __int64 *)(v_rsp - 79 + 87), v_rsp - 79 - 57, v_rsp - 79 - 81, (unsigned int)((unsigned int)(v_r14)));
    if (sign_flag) goto loc_007F9DB2;
loc_007F9D99:
    v_rdi = (v_rdi) + (*(unsigned __int64 *)(v_rsp - 79 - 81));
    a1 = (v_rbx) - (v_rdi);
    *(unsigned __int64 *)(v_rsp - 79 - 81) = a1;
    if (condition_is_not_equal) goto loc_007F99CF;
    goto loc_007F9DEF;
loc_007F9DB2:
    if (((unsigned int)(*(unsigned __int64 *)(v_rsp - 79 - 81))) == 0xC000009AULL) goto loc_007F9DE1;
    if (((unsigned int)(*(unsigned __int64 *)(v_rsp - 79 - 81))) == 0xC000012DULL) goto loc_007F9DE1;
    if (((unsigned int)(*(unsigned __int64 *)(v_rsp - 79 - 81))) != 0xC00000BBULL) goto loc_007F9DEF;
    if (((unsigned int)(*(unsigned __int64 *)(v_rsp - 79 - 81))) >= 0xC00000BBULL) goto loc_007F9DD5;
    goto loc_007F9DE1;
loc_007F9DD5:
    if (((unsigned int)(*(unsigned __int64 *)(v_rsp - 79 - 81))) >= 0xC00000BBULL) goto loc_007F9DEF;
loc_007F9DE1:
    goto loc_007F99CF;
loc_007F9DE9:
loc_007F9DEF:
    v_rsi = 0;
    if (v_rdi == 0) { v_rsi = (unsigned int)((unsigned int)(0xC0000018ULL)); }
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 79 + 103)) = v_rdi;
loc_007F9DFF:
    if ((*(unsigned int *)(v_rsp - 79 + 127)) != 0) goto loc_007F9E14;
    if (sign_flag) goto loc_007F9E14;
    result = *(unsigned __int64 *)(v_rsp - 79 + 103);
    if ((((unsigned __int8)(v_r14)) & (2)) == 0) {
        result = IoUpdateDumpPhysicalRanges(a1, v_rsp - 79 - 57, v_rsp - 79 - 81, (unsigned int)((unsigned int)(v_r14)));
    }
loc_007F9E16:
    v_rsp = (v_rsp) + (152);
    return (unsigned int)((unsigned int)(v_rsi));
}
```

## 5. (Beta) C Style

```c
int64_t MiAddPhysicalMemoryChunks(int64_t Arg1, void *Arg2, void *Arg3, int64_t Arg4)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_mB8;

    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(void **)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (152);
    *(uint32_t *)(local_rsp - 0x4F + 0x5F) = 0x3000ULL;
    *(uint64_t *)(local_rsp - 0x4F - 0x41) = 512;
    *(uint32_t *)(local_rsp - 0x4F - 0x49) = 1;
    result = local_rsp;
    if (Arg4 != 0) {
        Arg3 = 0;
        result = 0x40000ULL;
        Arg3 = (Arg4 != result) ? 1 : 0;
        if (Arg4 != result) { result = 512; }
        *(uint32_t *)(local_rsp - 0x4F - 0x49) = (uint32_t)(Arg3);
        *(uint64_t *)(local_rsp - 0x4F - 0x41) = result;
    }
    local_rdi = 0;
    *(uint64_t *)(local_rsp - 0x4F - 0x39) = *(uint64_t *)(arg2);
    *(uint64_t *)(local_rsp - 0x4F - 0x51) = *(uint64_t *)(arg3);
    if (condition_is_above_or_equal) goto loc_007F99AC;
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x77))) | (0x206000ULL));
    local_rbx = (*(uint64_t *)(arg3)) & (0xFFFFFFFFFFFFF000ULL);
loc_007F9964:
    *(uint64_t *)(local_rsp - 0x4F - 0x51) = local_rbx;
    result = MiAddPhysicalMemory(Arg1, local_rsp - 79 - 57, local_rsp - 79 - 81, (uint32_t)((uint32_t)(local_r14)));
    if (!sign_flag) goto loc_007F99A0;
    if (condition_is_above_or_equal) goto loc_007F9998;
    goto loc_007F9964;
loc_007F9998:
    goto loc_007F9E16;
loc_007F99A0:
    *(uint64_t *)(arg3) = *(uint64_t *)(local_rsp - 0x4F - 0x51);
    goto loc_007F9DFF;
loc_007F99AC:
    result = 0;
    *(uint64_t *)(local_rsp - 0x4F - 0x29) = 0;
    result = (*(uint64_t *)(local_rsp - 0x4F + 0x57)) - (v_rip + 6550347);
    result = -(result);
    local_r12 = (uint32_t)((local_r12) & (2));
    local_r13 = 0;
loc_007F99CF:
    result = (*(uint64_t *)(local_rsp - 0x4F - 0x39)) >> (12);
    Arg2 = (*(uint64_t *)(local_rsp - 0x4F - 0x51)) >> (12);
    *(uint64_t *)(local_rsp - 0x4F - 0x59) = result;
    result = MiRestrictRangeToNode(result, Arg2, local_rsp - 79 - 81, (uint32_t)((uint32_t)(local_r14)));
    if (result < (*(uint64_t *)(local_rsp - 0x4F + 0x6F))) goto loc_007F9DE9;
    if ((*(uint64_t *)(local_rsp - 0x4F - 0x59)) >= ((uint32_t)(0x100000ULL))) goto loc_007F9A14;
    local_rsi = result;
    if ((result + *(uint64_t *)(local_rsp - 0x4F - 0x59) * 1) >= = ((uint32_t)(0x100000ULL))) {
        local_rsi = (uint32_t)((uint32_t)(0x100000ULL));
        local_rsi = (local_rsi) - (*(uint64_t *)(local_rsp - 0x4F - 0x59));
    }
    result = MiPageToNode(*(uint64_t *)(local_rsp - 0x4F - 0x59), (uint32_t)(0x100000ULL), local_rsp - 79 - 81, (uint32_t)((uint32_t)(local_r14)));
    result = MiGetClosestImplicitNode(1 + result * 1, (uint32_t)(0x100000ULL), local_rsp - 79 - 81, (uint32_t)((uint32_t)(local_r14)));
    result = (uint32_t)((result) - (1));
    local_r10 = (*(uint64_t *)(local_rsp - 0x4F + 0x57)) * (result);
    local_r10 = (local_r10) + (*(uint64_t *)(v_rip + 0x63F2D4));
    *(uint64_t *)(local_rsp - 0x4F - 0x11) = local_r10;
    if (sign_flag) goto loc_007F9AA5;
    local_r15 = 0;
    if ((*(uint64_t *)(local_rsp - 0x4F + 0x57)) != (v_rip + 6550192)) { local_r15 = (uint32_t)(local_r12); }
loc_007F9A5E:
    Arg2 = 0;
    if (0 != 0) goto loc_007F9A92;
    if (local_rsi < (*(uint64_t *)(v_rip - 0x7E7E08 + 0x1 * 8))) goto loc_007F9A9C;
    result = ~(*(uint64_t *)(v_rip - 0x7E7E08 + 0x1 * 8) - 1);
    local_rsi = (local_rsi) & (result);
    if (1 == 0) goto loc_007F9A9C;
    Arg3 = (uint32_t)((1) - 1);
    goto loc_007F9A5E;
loc_007F9A92:
    Arg1 = (*(uint64_t *)(v_rip - 0x7E7E08 + 0x1 * 8)) - (0);
    if (local_rsi > Arg1) { local_rsi = Arg1; }
loc_007F9A9C:
    goto loc_007F9B59;
loc_007F9AA5:
    if ((*(uint64_t *)(local_rsp - 0x4F - 0x29)) <= (*(uint64_t *)(local_rsp - 0x4F - 0x41))) goto loc_007F9AE2;
    if ((*(uint64_t *)(local_rsp - 0x4F + 0x57)) != (v_rip + 6550096)) goto loc_007F9ACA;
    goto loc_007F9AE2;
loc_007F9ACA:
    result = (*(uint64_t *)(local_rsp - 0x4F - 0x29)) >> (1);
    local_rsi = ~(*(uint64_t *)(local_rsp - 0x4F - 0x41) - 1);
    local_rsi = (local_rsi) & (result);
    if (local_rsi < (*(uint64_t *)(local_rsp - 0x4F - 0x41))) { local_rsi = *(uint64_t *)(local_rsp - 0x4F - 0x41); }
loc_007F9AE2:
    if ((uint32_t)(local_r12) != 0) goto loc_007F9B07;
    if ((*(uint64_t *)(local_rsp - 0x4F - 0x29)) <= (*(uint64_t *)(local_rsp - 0x4F - 0x41))) goto loc_007F9AF5;
    local_r15 = 0;
    goto loc_007F9B5D;
loc_007F9AF5:
    local_r15 = (uint32_t)(-(local_r15));
    local_r15 = (uint32_t)((local_r15) + (1));
    goto loc_007F9B5D;
loc_007F9B07:
    if (((uint32_t)(local_r12)) != 1) goto loc_007F9B18;
    local_r15 = (uint32_t)((local_r15) + (2));
    goto loc_007F9B59;
loc_007F9B18:
    if (((uint32_t)(local_r12)) != 2) goto loc_007F9B3E;
    if ((*(uint64_t *)(local_rsp - 0x4F + 0x57)) != (v_rip + 6550096)) goto loc_007F9B2E;
    goto loc_007F9B5D;
loc_007F9B2E:
    local_r15 = (uint32_t)((local_r12 + 1) & (0xFFFFFFFEULL));
    local_r15 = (uint32_t)((local_r15) + (4));
    goto loc_007F9B5D;
loc_007F9B3E:
    if (((uint32_t)(local_r12)) == 3) goto loc_007F9B53;
    if (((uint32_t)(local_r12)) != 4) goto loc_007F9B59;
    if ((*(uint64_t *)(local_rsp - 0x4F - 0x29)) <= (*(uint64_t *)(local_rsp - 0x4F - 0x41))) goto loc_007F9DEF;
loc_007F9B53:
loc_007F9B59:
loc_007F9B5D:
    local_r13 = 0;
loc_007F9B63:
    if (0 > 1) goto loc_007F9B93;
    Arg2 = 0;
    if (0 != 0) goto loc_007F9B8B;
    if (0 == 0) goto loc_007F9B90;
loc_007F9B8B:
    local_r13 = (uint32_t)((local_r13) + (1));
    goto loc_007F9B63;
loc_007F9B90:
loc_007F9B93:
    local_r14 = (uint32_t)((local_r14) & (0xFFFF4FFFULL));
    if (local_rsi < (*(uint64_t *)(local_rsp - 0x4F - 0x41))) goto loc_007F9D01;
    Arg1 = 0;
    if (4 != 0) goto loc_007F9BEA;
    Arg2 = 0;
    result = MiNodeLargeFreeZeroPages2(local_r10, Arg2, *(uint64_t *)(local_rsp - 0x4F - 0x59), *(uint64_t *)(local_rsp - 0x4F - 0x41));
    if (result != 0) goto loc_007F9BEA;
    result = (*(uint64_t *)(local_rsp - 0x4F - 0x59)) + (local_rsi);
    if (result <= 0x100000ULL) goto loc_007F9BDE;
    local_r12 = *(uint64_t *)(v_rip - 0x7E7F11 + local_r13 * 8);
    if (local_rsi >= = (*(uint64_t *)(local_rsp - 0x4F - 0x41))) {
        local_r13 = *(uint32_t *)(local_rsp - 0x4F - 0x49);
        local_rsi = *(uint64_t *)(local_rsp - 0x4F - 0x41);
        local_r12 = *(uint64_t *)(local_rsp - 0x4F - 0x41);
    }
    *(uint64_t *)(local_rsp - 0x4F - 0x19) = local_rsi;
    goto loc_007F9C06;
loc_007F9BEA:
    if (1 == 0) goto loc_007F9C5D;
    if (1 == 3) goto loc_007F9C5D;
    *(uint64_t *)(local_rsp - 0x4F - 0x19) = local_rsi;
    if (1 != 1) goto loc_007F9C1A;
loc_007F9C06:
    result = MiNodeLargeFreeZeroPages2(*(uint64_t *)(local_rsp - 0x4F - 0x11), 1, local_rsi, *(uint64_t *)(local_rsp - 0x4F - 0x41));
    goto loc_007F9C5A;
loc_007F9C1A:
    if ((*(uint64_t *)(local_rsp - 0x4F + 0x57)) == (v_rip + 6549724)) goto loc_007F9C5D;
    if (1 != 2) goto loc_007F9C4F;
    result = MiNodeAvailablePages(*(uint64_t *)(local_rsp - 0x4F - 0x11), 1, result, *(uint64_t *)(local_rsp - 0x4F - 0x41));
    if (result >= 6) goto loc_007F9C75;
    result = 0;
    local_r13 = 0;
    goto loc_007F9D99;
loc_007F9C4F:
    result = MiGetAvailablePagesExcludeSlists(0, 1, result, *(uint64_t *)(local_rsp - 0x4F - 0x41));
loc_007F9C5A:
loc_007F9C5D:
    if (result != 0) goto loc_007F9C75;
    result = *(uint64_t *)(local_rsp - 0x4F - 0x41);
    if (local_rsi == (*(uint64_t *)(local_rsp - 0x4F - 0x41))) { result = local_rsi; }
    goto loc_007F9D01;
loc_007F9C75:
loc_007F9C82:
    result = (result + 4 + result + 4 * 2) << (4);
    result = (result) >> (12);
    if (result >= result) goto loc_007F9CA7;
    if (0 >= (*(uint32_t *)(local_rsp - 0x4F - 0x49))) goto loc_007F9CA2;
    local_r13 = (uint32_t)((local_r13) + (1));
    goto loc_007F9C82;
loc_007F9CA2:
    goto loc_007F9CC1;
loc_007F9CA7:
    if ((*(uint64_t *)(v_rip - 0x7E8022 + local_r13 * 8)) == 1) goto loc_007F9CC1;
    if ((*(uint64_t *)(local_rsp - 0x4F + 0x57)) == (v_rip + 6549578)) {
    }
    Arg1 = (result) << (12);
    Arg2 = (v_rip - 8290338) >> (5);
    result = ~(*(uint64_t *)(v_rip - 0x7E8022 + local_r13 * 8) - 1);
    Arg2 = (Arg2) & (result);
    if (*(uint64_t *)(local_rsp - 0x4F + 0x6F) != 0) {
        result = *(uint64_t *)(local_rsp - 0x4F + 0x6F) - 1;
        result = ~(result);
        Arg2 = (Arg2) & (result);
        if (Arg2 < (*(uint64_t *)(local_rsp - 0x4F + 0x6F))) { Arg2 = *(uint64_t *)(local_rsp - 0x4F + 0x6F); }
    }
    local_rsi = result;
    if (result > Arg2) { local_rsi = Arg2; }
loc_007F9D01:
    if (sign_flag) goto loc_007F9D4E;
    if (((511) & (*(uint64_t *)(local_rsp - 0x4F - 0x59))) != 0) goto loc_007F9D4E;
    if (((511) & (local_rsi)) != 0) goto loc_007F9D4E;
    result = MiGetLargestPageIndex(*(uint64_t *)(local_rsp - 0x4F - 0x59), Arg2, *(uint64_t *)(v_rip - 0x7E8022 + local_r13 * 8), *(uint64_t *)(local_rsp - 0x4F - 0x41));
    if ((uint32_t)(result) != 0) goto loc_007F9D3F;
    if ((((uint32_t)(0x3FFFFULL)) & (*(uint64_t *)(local_rsp - 0x4F - 0x59))) != 0) goto loc_007F9D3F;
    if ((((uint32_t)(0x3FFFFULL)) & (local_rsi)) != 0) goto loc_007F9D42;
    if ((((uint32_t)((uint32_t)(0x2000ULL))) & ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x5F))))) == 0) goto loc_007F9D42;
    goto loc_007F9D4B;
loc_007F9D3F:
loc_007F9D42:
    if ((((uint32_t)((uint32_t)(0x1000ULL))) & ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x5F))))) != 0) {
        local_r14 = (uint32_t)((local_r14) | ((uint32_t)((uint32_t)(0x1000ULL))));
    }
    *(uint64_t *)(local_rsp - 0x4F - 0x29) = local_rsi;
    if (1 > 2) { local_r14 = (uint32_t)((uint32_t)((uint32_t)(local_r14))); }
    local_rsi = (local_rsi) << (12);
    *(uint64_t *)(local_rsp - 0x4F - 0x51) = local_rsi;
    result = MiAddPhysicalMemory(*(uint64_t *)(local_rsp - 0x4F + 0x57), local_rsp - 79 - 57, local_rsp - 79 - 81, (uint32_t)((uint32_t)(local_r14)));
    if (sign_flag) goto loc_007F9DB2;
loc_007F9D99:
    local_rdi = (local_rdi) + (*(uint64_t *)(local_rsp - 0x4F - 0x51));
    Arg1 = (local_rbx) - (local_rdi);
    *(uint64_t *)(local_rsp - 0x4F - 0x51) = Arg1;
    if (condition_is_not_equal) goto loc_007F99CF;
    goto loc_007F9DEF;
loc_007F9DB2:
    if (((uint32_t)(*(uint64_t *)(local_rsp - 0x4F - 0x51))) == 0xC000009AULL) goto loc_007F9DE1;
    if (((uint32_t)(*(uint64_t *)(local_rsp - 0x4F - 0x51))) == 0xC000012DULL) goto loc_007F9DE1;
    if (((uint32_t)(*(uint64_t *)(local_rsp - 0x4F - 0x51))) != 0xC00000BBULL) goto loc_007F9DEF;
    if (((uint32_t)(*(uint64_t *)(local_rsp - 0x4F - 0x51))) >= 0xC00000BBULL) goto loc_007F9DD5;
    goto loc_007F9DE1;
loc_007F9DD5:
    if (((uint32_t)(*(uint64_t *)(local_rsp - 0x4F - 0x51))) >= 0xC00000BBULL) goto loc_007F9DEF;
loc_007F9DE1:
    goto loc_007F99CF;
loc_007F9DE9:
loc_007F9DEF:
    local_rsi = 0;
    if (local_rdi == 0) { local_rsi = (uint32_t)((uint32_t)(0xC0000018ULL)); }
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x4F + 0x67)) = local_rdi;
loc_007F9DFF:
    if ((*(uint32_t *)(local_rsp - 0x4F + 0x7F)) != 0) goto loc_007F9E14;
    if (sign_flag) goto loc_007F9E14;
    result = *(uint64_t *)(local_rsp - 0x4F + 0x67);
    if ((((uint8_t)(local_r14)) & (2)) == 0) {
        result = IoUpdateDumpPhysicalRanges(Arg1, local_rsp - 79 - 57, local_rsp - 79 - 81, (uint32_t)((uint32_t)(local_r14)));
    }
loc_007F9E16:
    local_rsp = (local_rsp) + (152);
    return (uint32_t)((uint32_t)(local_rsi));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg3` | `+ 0x0` | `64` | `R` |
| `Arg3` | `+ 0x0` | `64` | `R/W` |
| `Arg3` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007F98D4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
