# MiHotAddPartitionMemory

- RVA: `0x0080D5B4`–`0x0080D8AF` (길이 `763` bytes)
- VA: `0x000000014080D5B4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D9048`
- 디코드: `238`개 명령, `763/763` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **11**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0080D5F7` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0080D62D` → [MiFreePartitionTree](../../text/69/MiFreePartitionTree_function_00690E50.md) (function, `0x00690E50`)
- `0x0080D6CF` → [MiAddRangeToPartitionTree](../../text/69/MiAddRangeToPartitionTree_function_0069020C.md) (function, `0x0069020C`)
- `0x0080D70F` → [MiUpdatePartitionLargePfnBitMap](MiUpdatePartitionLargePfnBitMap_function_0080DB50.md) (function, `0x0080DB50`)
- `0x0080D7F1` → [MiActOnPartitionNodePages](../../text/68/MiActOnPartitionNodePages_function_0068F7F4.md) (function, `0x0068F7F4`)
- `0x0080D80D` → [RtlAreBitsClearEx](../../text/41/RtlAreBitsClearEx_function_0041DBF0.md) (function, `0x0041DBF0`)
- `0x0080D82A` → [RtlAvlRemoveNode](../../text/29/RtlAvlRemoveNode_function_00296650.md) (function, `0x00296650`)
- `0x0080D832` → [MiDeletePartitionPageNode](../../text/69/MiDeletePartitionPageNode_function_006908C4.md) (function, `0x006908C4`)
- `0x0080D858` → [IoUpdateDumpPhysicalRanges](../../text/59/IoUpdateDumpPhysicalRanges_function_0059343C.md) (function, `0x0059343C`)
- `0x0080D883` → [MiFreePartitionTree](../../text/69/MiFreePartitionTree_function_00690E50.md) (function, `0x00690E50`)
- `0x0080D8A1` → [MiInsertPartitionPages](../../text/69/MiInsertPartitionPages_function_006911A0.md) (function, `0x006911A0`)

### Direct callers
- [MmManagePartitionInitialAddMemory](MmManagePartitionInitialAddMemory_function_0080E144.md) at `0x0080E1B9`

### Static image references
- `0x0080D601` → RVA `0x00E38D00` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **10**
  - `0x0080D5F7` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0080D62D` → [MiFreePartitionTree](../../text/69/MiFreePartitionTree_function_00690E50.md) (`PAGE` → `.text`)
  - `0x0080D6CF` → [MiAddRangeToPartitionTree](../../text/69/MiAddRangeToPartitionTree_function_0069020C.md) (`PAGE` → `.text`)
  - `0x0080D7F1` → [MiActOnPartitionNodePages](../../text/68/MiActOnPartitionNodePages_function_0068F7F4.md) (`PAGE` → `.text`)
  - `0x0080D80D` → [RtlAreBitsClearEx](../../text/41/RtlAreBitsClearEx_function_0041DBF0.md) (`PAGE` → `.text`)
  - `0x0080D82A` → [RtlAvlRemoveNode](../../text/29/RtlAvlRemoveNode_function_00296650.md) (`PAGE` → `.text`)
  - `0x0080D832` → [MiDeletePartitionPageNode](../../text/69/MiDeletePartitionPageNode_function_006908C4.md) (`PAGE` → `.text`)
  - `0x0080D858` → [IoUpdateDumpPhysicalRanges](../../text/59/IoUpdateDumpPhysicalRanges_function_0059343C.md) (`PAGE` → `.text`)
  - `0x0080D883` → [MiFreePartitionTree](../../text/69/MiFreePartitionTree_function_00690E50.md) (`PAGE` → `.text`)
  - `0x0080D8A1` → [MiInsertPartitionPages](../../text/69/MiInsertPartitionPages_function_006911A0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0080D5B4  48 8B C4                        mov rax, rsp
0080D5B7  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
0080D5BB  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
0080D5BF  48 89 48 08                     mov qword ptr [rax + 8], rcx
0080D5C3  55                              push rbp
0080D5C4  56                              push rsi
0080D5C5  57                              push rdi
0080D5C6  41 54                           push r12
0080D5C8  41 55                           push r13
0080D5CA  41 56                           push r14
0080D5CC  41 57                           push r15
0080D5CE  48 8D 68 A1                     lea rbp, [rax - 0x5f]
0080D5D2  48 81 EC B0 00 00 00            sub rsp, 0xb0
0080D5D9  0F 57 C0                        xorps xmm0, xmm0
0080D5DC  48 8B F2                        mov rsi, rdx
0080D5DF  33 D2                           xor edx, edx
0080D5E1  4D 8B F8                        mov r15, r8
0080D5E4  4C 8B E9                        mov r13, rcx
0080D5E7  48 8D 4D D7                     lea rcx, [rbp - 0x29]
0080D5EB  0F 11 45 AF                     movups xmmword ptr [rbp - 0x51], xmm0
0080D5EF  44 8D 42 48                     lea r8d, [rdx + 0x48]
0080D5F3  0F 11 45 BF                     movups xmmword ptr [rbp - 0x41], xmm0
0080D5F7  E8 44 96 EB FF                  call 0x1406c6c40
0080D5FC  48 83 65 9F 00                  and qword ptr [rbp - 0x61], 0
0080D601  48 8D 05 F8 B6 62 00            lea rax, [rip + 0x62b6f8]
0080D608  C7 45 7F 0E 00 00 00            mov dword ptr [rbp + 0x7f], 0xe
0080D60F  4C 3B E8                        cmp r13, rax
0080D612  75 40                           jne 0x14080d654
0080D614  41 8B 07                        mov eax, dword ptr [r15]
0080D617  A8 04                           test al, 4
0080D619  75 35                           jne 0x14080d650
0080D61B  BB BB 00 00 C0                  mov ebx, 0xc00000bb
0080D620  45 33 C9                        xor r9d, r9d
0080D623  48 8D 55 9F                     lea rdx, [rbp - 0x61]
0080D627  45 33 C0                        xor r8d, r8d
0080D62A  49 8B CD                        mov rcx, r13
0080D62D  E8 1E 38 E8 FF                  call 0x140690e50
0080D632  8B C3                           mov eax, ebx
0080D634  48 8B 9C 24 F8 00 00 00         mov rbx, qword ptr [rsp + 0xf8]
0080D63C  48 81 C4 B0 00 00 00            add rsp, 0xb0
0080D643  41 5F                           pop r15
0080D645  41 5E                           pop r14
0080D647  41 5D                           pop r13
0080D649  41 5C                           pop r12
0080D64B  5F                              pop rdi
0080D64C  5E                              pop rsi
0080D64D  5D                              pop rbp
0080D64E  C3                              ret
0080D64F  CC                              int3
0080D650  A8 08                           test al, 8
0080D652  75 C7                           jne 0x14080d61b
0080D654  41 8B 0F                        mov ecx, dword ptr [r15]
0080D657  F6 C1 20                        test cl, 0x20
0080D65A  74 08                           je 0x14080d664
0080D65C  41 BE 00 02 00 00               mov r14d, 0x200
0080D662  EB 1A                           jmp 0x14080d67e
0080D664  41 BE 00 00 04 00               mov r14d, 0x40000
0080D66A  F6 C1 40                        test cl, 0x40
0080D66D  75 0F                           jne 0x14080d67e
0080D66F  F6 C1 04                        test cl, 4
0080D672  B8 00 00 00 00                  mov eax, 0
0080D677  41 0F 45 C6                     cmovne eax, r14d
0080D67B  44 8B F0                        mov r14d, eax
0080D67E  49 83 67 08 00                  and qword ptr [r15 + 8], 0
0080D683  41 8B 47 04                     mov eax, dword ptr [r15 + 4]
0080D687  89 45 97                        mov dword ptr [rbp - 0x69], eax
0080D68A  F6 C1 01                        test cl, 1
0080D68D  74 08                           je 0x14080d697
0080D68F  41 BC 01 00 00 00               mov r12d, 1
0080D695  EB 1F                           jmp 0x14080d6b6
0080D697  41 8B 45 04                     mov eax, dword ptr [r13 + 4]
0080D69B  A8 20                           test al, 0x20
0080D69D  74 0A                           je 0x14080d6a9
0080D69F  BB F0 00 00 C0                  mov ebx, 0xc00000f0
0080D6A4  E9 77 FF FF FF                  jmp 0x14080d620
0080D6A9  41 8B 07                        mov eax, dword ptr [r15]
0080D6AC  A8 04                           test al, 4
0080D6AE  75 EF                           jne 0x14080d69f
0080D6B0  8B 45 97                        mov eax, dword ptr [rbp - 0x69]
0080D6B3  45 33 E4                        xor r12d, r12d
0080D6B6  33 FF                           xor edi, edi
0080D6B8  33 DB                           xor ebx, ebx
0080D6BA  3B D8                           cmp ebx, eax
0080D6BC  73 2F                           jae 0x14080d6ed
0080D6BE  4C 8B 46 08                     mov r8, qword ptr [rsi + 8]
0080D6C2  48 8D 4D 9F                     lea rcx, [rbp - 0x61]
0080D6C6  48 8B 16                        mov rdx, qword ptr [rsi]
0080D6C9  45 33 C9                        xor r9d, r9d
0080D6CC  49 03 F8                        add rdi, r8
0080D6CF  E8 38 2B E8 FF                  call 0x14069020c
0080D6D4  85 C0                           test eax, eax
0080D6D6  74 0B                           je 0x14080d6e3
0080D6D8  8B 45 97                        mov eax, dword ptr [rbp - 0x69]
0080D6DB  FF C3                           inc ebx
0080D6DD  48 83 C6 10                     add rsi, 0x10
0080D6E1  EB D7                           jmp 0x14080d6ba
0080D6E3  BB 9A 00 00 C0                  mov ebx, 0xc000009a
0080D6E8  E9 33 FF FF FF                  jmp 0x14080d620
0080D6ED  41 8B 07                        mov eax, dword ptr [r15]
0080D6F0  A8 04                           test al, 4
0080D6F2  74 14                           je 0x14080d708
0080D6F4  0F B6 C0                        movzx eax, al
0080D6F7  83 E0 02                        and eax, 2
0080D6FA  C6 45 E8 01                     mov byte ptr [rbp - 0x18], 1
0080D6FE  83 C8 04                        or eax, 4
0080D701  D1 E8                           shr eax, 1
0080D703  89 45 EB                        mov dword ptr [rbp - 0x15], eax
0080D706  EB 16                           jmp 0x14080d71e
0080D708  48 8D 55 9F                     lea rdx, [rbp - 0x61]
0080D70C  49 8B CD                        mov rcx, r13
0080D70F  E8 3C 04 00 00                  call 0x14080db50
0080D714  8B D8                           mov ebx, eax
0080D716  85 C0                           test eax, eax
0080D718  0F 88 02 FF FF FF               js 0x14080d620
0080D71E  41 8B 45 04                     mov eax, dword ptr [r13 + 4]
0080D722  33 DB                           xor ebx, ebx
0080D724  8B 75 C7                        mov esi, dword ptr [rbp - 0x39]
0080D727  A8 20                           test al, 0x20
0080D729  74 07                           je 0x14080d732
0080D72B  C6 45 E7 01                     mov byte ptr [rbp - 0x19], 1
0080D72F  83 CE 08                        or esi, 8
0080D732  45 85 E4                        test r12d, r12d
0080D735  75 0B                           jne 0x14080d742
0080D737  83 CE 02                        or esi, 2
0080D73A  89 75 C7                        mov dword ptr [rbp - 0x39], esi
0080D73D  E9 1B 01 00 00                  jmp 0x14080d85d
0080D742  45 8B 27                        mov r12d, dword ptr [r15]
0080D745  41 8B C4                        mov eax, r12d
0080D748  21 5D A7                        and dword ptr [rbp - 0x59], ebx
0080D74B  83 E0 08                        and eax, 8
0080D74E  C1 E0 03                        shl eax, 3
0080D751  89 45 97                        mov dword ptr [rbp - 0x69], eax
0080D754  41 83 E4 02                     and r12d, 2
0080D758  75 04                           jne 0x14080d75e
0080D75A  0F BA EE 07                     bts esi, 7
0080D75E  41 8B C4                        mov eax, r12d
0080D761  4C 89 6D D7                     mov qword ptr [rbp - 0x29], r13
0080D765  F7 D8                           neg eax
0080D767  4C 89 75 0F                     mov qword ptr [rbp + 0xf], r14
0080D76B  1B C0                           sbb eax, eax
0080D76D  0F BA EE 08                     bts esi, 8
0080D771  83 C0 0C                        add eax, 0xc
0080D774  89 75 AB                        mov dword ptr [rbp - 0x55], esi
0080D777  89 45 7F                        mov dword ptr [rbp + 0x7f], eax
0080D77A  33 FF                           xor edi, edi
0080D77C  48 8B 45 9F                     mov rax, qword ptr [rbp - 0x61]
0080D780  89 75 C7                        mov dword ptr [rbp - 0x39], esi
0080D783  EB 06                           jmp 0x14080d78b
0080D785  48 8B F8                        mov rdi, rax
0080D788  48 8B 00                        mov rax, qword ptr [rax]
0080D78B  48 85 C0                        test rax, rax
0080D78E  75 F5                           jne 0x14080d785
0080D790  48 85 FF                        test rdi, rdi
0080D793  0F 84 B2 00 00 00               je 0x14080d84b
0080D799  44 8B 7D 97                     mov r15d, dword ptr [rbp - 0x69]
0080D79D  44 8B 6D A7                     mov r13d, dword ptr [rbp - 0x59]
0080D7A1  8B 75 7F                        mov esi, dword ptr [rbp + 0x7f]
0080D7A4  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
0080D7A8  4C 8B F7                        mov r14, rdi
0080D7AB  48 8B CF                        mov rcx, rdi
0080D7AE  48 85 C0                        test rax, rax
0080D7B1  74 23                           je 0x14080d7d6
0080D7B3  48 8B 08                        mov rcx, qword ptr [rax]
0080D7B6  48 8B F8                        mov rdi, rax
0080D7B9  48 85 C9                        test rcx, rcx
0080D7BC  74 22                           je 0x14080d7e0
0080D7BE  48 8B 01                        mov rax, qword ptr [rcx]
0080D7C1  48 8B F9                        mov rdi, rcx
0080D7C4  48 8B C8                        mov rcx, rax
0080D7C7  48 85 C0                        test rax, rax
0080D7CA  75 F2                           jne 0x14080d7be
0080D7CC  EB 12                           jmp 0x14080d7e0
0080D7CE  48 39 0F                        cmp qword ptr [rdi], rcx
0080D7D1  74 0D                           je 0x14080d7e0
0080D7D3  48 8B CF                        mov rcx, rdi
0080D7D6  48 8B 7F 10                     mov rdi, qword ptr [rdi + 0x10]
0080D7DA  48 83 E7 FC                     and rdi, 0xfffffffffffffffc
0080D7DE  75 EE                           jne 0x14080d7ce
0080D7E0  45 85 ED                        test r13d, r13d
0080D7E3  75 3E                           jne 0x14080d823
0080D7E5  4C 8D 4D D7                     lea r9, [rbp - 0x29]
0080D7E9  45 8B C7                        mov r8d, r15d
0080D7EC  8B D6                           mov edx, esi
0080D7EE  49 8B CE                        mov rcx, r14
0080D7F1  E8 FE 1F E8 FF                  call 0x14068f7f4
0080D7F6  8B 45 EF                        mov eax, dword ptr [rbp - 0x11]
0080D7F9  85 C0                           test eax, eax
0080D7FB  79 21                           jns 0x14080d81e
0080D7FD  8B D8                           mov ebx, eax
0080D7FF  45 85 E4                        test r12d, r12d
0080D802  74 14                           je 0x14080d818
0080D804  49 8D 4E 20                     lea rcx, [r14 + 0x20]
0080D808  33 D2                           xor edx, edx
0080D80A  4C 8B 01                        mov r8, qword ptr [rcx]
0080D80D  E8 DE 03 C1 FF                  call 0x14041dbf0
0080D812  84 C0                           test al, al
0080D814  49 0F 45 FE                     cmovne rdi, r14
0080D818  41 BD 01 00 00 00               mov r13d, 1
0080D81E  45 85 E4                        test r12d, r12d
0080D821  75 14                           jne 0x14080d837
0080D823  49 8B D6                        mov rdx, r14
0080D826  48 8D 4D 9F                     lea rcx, [rbp - 0x61]
0080D82A  E8 21 8E A8 FF                  call 0x140296650
0080D82F  49 8B CE                        mov rcx, r14
0080D832  E8 8D 30 E8 FF                  call 0x1406908c4
0080D837  48 85 FF                        test rdi, rdi
0080D83A  0F 85 64 FF FF FF               jne 0x14080d7a4
0080D840  8B 75 AB                        mov esi, dword ptr [rbp - 0x55]
0080D843  4C 8B 7D 77                     mov r15, qword ptr [rbp + 0x77]
0080D847  4C 8B 6D 67                     mov r13, qword ptr [rbp + 0x67]
0080D84B  48 8B 7D 07                     mov rdi, qword ptr [rbp + 7]
0080D84F  48 85 FF                        test rdi, rdi
0080D852  0F 84 C8 FD FF FF               je 0x14080d620
0080D858  E8 DF 5B D8 FF                  call 0x14059343c
0080D85D  41 8B 07                        mov eax, dword ptr [r15]
0080D860  A8 02                           test al, 2
0080D862  75 06                           jne 0x14080d86a
0080D864  83 CE 01                        or esi, 1
0080D867  89 75 C7                        mov dword ptr [rbp - 0x39], esi
0080D86A  48 8D 4D 9F                     lea rcx, [rbp - 0x61]
0080D86E  48 89 4D AF                     mov qword ptr [rbp - 0x51], rcx
0080D872  A8 04                           test al, 4
0080D874  74 14                           je 0x14080d88a
0080D876  45 33 C9                        xor r9d, r9d
0080D879  48 8D 55 9F                     lea rdx, [rbp - 0x61]
0080D87D  45 33 C0                        xor r8d, r8d
0080D880  49 8B CD                        mov rcx, r13
0080D883  E8 C8 35 E8 FF                  call 0x140690e50
0080D888  EB 1C                           jmp 0x14080d8a6
0080D88A  83 7D 7F 0C                     cmp dword ptr [rbp + 0x7f], 0xc
0080D88E  74 16                           je 0x14080d8a6
0080D890  4C 8B CF                        mov r9, rdi
0080D893  4C 8D 45 AF                     lea r8, [rbp - 0x51]
0080D897  49 8B D5                        mov rdx, r13
0080D89A  48 8D 0D 5F B4 62 00            lea rcx, [rip + 0x62b45f]
0080D8A1  E8 FA 38 E8 FF                  call 0x1406911a0
0080D8A6  49 89 7F 08                     mov qword ptr [r15 + 8], rdi
0080D8AA  E9 83 FD FF FF                  jmp 0x14080d632
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiHotAddPartitionMemory(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (176);
    a2 = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 81) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 95 - 65) = v_xmm0;
    result = memset(v_rsp - 95 - 41, a2, a2 + 72, a4);
    *(unsigned int *)(v_rsp - 95 + 127) = 14;
    if (a1 != (v_rip + 6469368)) goto loc_0080D654;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a3)))) & (4)) != 0) goto loc_0080D650;
loc_0080D61B:
loc_0080D620:
    a4 = 0;
    a3 = 0;
    result = MiFreePartitionTree(a1, v_rsp - 95 - 97, a3, a4);
loc_0080D632:
    v_rsp = (v_rsp) + (176);
    return (unsigned int)((unsigned int)((unsigned int)(0xC00000BBULL)));
loc_0080D650:
    if ((((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(0xC00000BBULL))))) & (8)) != 0) goto loc_0080D61B;
loc_0080D654:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a3)))) & (32)) == 0) goto loc_0080D664;
    goto loc_0080D67E;
loc_0080D664:
    result = (unsigned int)((unsigned int)((unsigned int)(0xC00000BBULL)));
    v_r14 = (unsigned int)(0x40000ULL);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a3)))) & (64)) == 0) {
        result = 0;
        if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a3)))) & (4)) != 0) { result = (unsigned int)((unsigned int)(0x40000ULL)); }
        v_r14 = (unsigned int)(result);
    }
    *(unsigned int *)(v_rsp - 95 - 105) = (unsigned int)((unsigned int)(*(unsigned int *)(a3 + 4)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a3)))) & (1)) == 0) goto loc_0080D697;
    goto loc_0080D6B6;
loc_0080D697:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 4)))) & (32)) == 0) goto loc_0080D6A9;
loc_0080D69F:
    goto loc_0080D620;
loc_0080D6A9:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a3)))) & (4)) != 0) goto loc_0080D69F;
    v_r12 = 0;
loc_0080D6B6:
    v_rdi = 0;
    v_rbx = 0;
loc_0080D6BA:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 105))))) goto loc_0080D6ED;
    a4 = 0;
    v_rdi = (v_rdi) + (*(unsigned __int64 *)(a2 + 8));
    result = MiAddRangeToPartitionTree(v_rsp - 95 - 97, *(unsigned __int64 *)(a2), *(unsigned __int64 *)(a2 + 8), a4);
    if ((unsigned int)(result) == 0) goto loc_0080D6E3;
    v_rbx = (unsigned int)((v_rbx) + 1);
    v_rsi = (a2) + (16);
    goto loc_0080D6BA;
loc_0080D6E3:
    goto loc_0080D620;
loc_0080D6ED:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a3)))) & (4)) == 0) goto loc_0080D708;
    result = (unsigned int)(((unsigned __int8)((unsigned int)(*(unsigned int *)(a3)))) & (2));
    *(unsigned __int8 *)(v_rsp - 95 - 24) = 1;
    result = (unsigned int)((result) | (4));
    result = (unsigned int)((result) >> (1));
    *(unsigned int *)(v_rsp - 95 - 21) = (unsigned int)(result);
    goto loc_0080D71E;
loc_0080D708:
    result = MiUpdatePartitionLargePfnBitMap(a1, v_rsp - 95 - 97, *(unsigned __int64 *)(a2 + 8), a4);
    if (sign_flag) goto loc_0080D620;
loc_0080D71E:
    v_rbx = 0;
    v_rsi = (unsigned int)(*(unsigned int *)(v_rsp - 95 - 57));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 4)))) & (32)) != 0) {
        *(unsigned __int8 *)(v_rsp - 95 - 25) = 1;
        v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 95 - 57))) | (8));
    }
    if (0 != 0) goto loc_0080D742;
    v_rsi = (unsigned int)((v_rsi) | (2));
    *(unsigned int *)(v_rsp - 95 - 57) = (unsigned int)(v_rsi);
    goto loc_0080D85D;
loc_0080D742:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3))))) & (8));
    result = (unsigned int)((result) << (3));
    *(unsigned int *)(v_rsp - 95 - 105) = (unsigned int)(result);
    v_r12 = (unsigned int)(((unsigned int)(*(unsigned int *)(a3))) & (2));
    if (!(condition_is_not_equal)) {
    }
    *(unsigned __int64 *)(v_rsp - 95 - 41) = a1;
    result = (unsigned int)(-((unsigned int)((unsigned int)(v_r12))));
    *(unsigned __int64 *)(v_rsp - 95 + 15) = v_r14;
    result = (unsigned int)((result) + (12));
    *(unsigned int *)(v_rsp - 95 - 85) = (unsigned int)(v_rsi);
    *(unsigned int *)(v_rsp - 95 + 127) = (unsigned int)(result);
    v_rdi = 0;
    *(unsigned int *)(v_rsp - 95 - 57) = (unsigned int)(v_rsi);
    goto loc_0080D78B;
loc_0080D785:
loc_0080D78B:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 97)) != 0) goto loc_0080D785;
    if (*(unsigned __int64 *)(v_rsp - 95 - 97) == 0) goto loc_0080D84B;
loc_0080D7A4:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 97) + 8) == 0) goto loc_0080D7D6;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 97) + 8)) == 0) goto loc_0080D7E0;
loc_0080D7BE:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 97) + 8))) != 0) goto loc_0080D7BE;
    goto loc_0080D7E0;
loc_0080D7CE:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 97) + 8)))) == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 97) + 8))))) goto loc_0080D7E0;
loc_0080D7D6:
    v_rdi = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 97) + 8)) + 16)) & (-4);
    if (condition_is_not_equal) goto loc_0080D7CE;
loc_0080D7E0:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 89))) != 0) goto loc_0080D823;
    result = MiActOnPartitionNodePages(*(unsigned __int64 *)(v_rsp - 95 - 97), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 + 127)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 105)))), v_rsp - 95 - 41);
    if (!sign_flag) goto loc_0080D81E;
    result = (unsigned int)(*(unsigned int *)(v_rsp - 95 - 17));
    if ((unsigned int)(v_r12) != 0) {
        a1 = *(unsigned __int64 *)(v_rsp - 95 - 97) + 32;
        a2 = 0;
        a3 = *(unsigned __int64 *)(a1);
        result = RtlAreBitsClearEx(a1, a2, a3, v_rsp - 95 - 41);
        if ((unsigned __int8)(result) != 0) { v_rdi = *(unsigned __int64 *)(v_rsp - 95 - 97); }
    }
loc_0080D81E:
    if ((unsigned int)(v_r12) == 0) {
        a2 = *(unsigned __int64 *)(v_rsp - 95 - 97);
        a1 = v_rsp - 95 - 97;
        result = RtlAvlRemoveNode(a1, a2, a3, v_rsp - 95 - 41);
        a1 = *(unsigned __int64 *)(v_rsp - 95 - 97);
        result = MiDeletePartitionPageNode(a1, a2, a3, v_rsp - 95 - 41);
    }
    if (v_rdi != 0) goto loc_0080D7A4;
loc_0080D84B:
    if (*(unsigned __int64 *)(v_rsp - 95 + 7) == 0) goto loc_0080D620;
    result = IoUpdateDumpPhysicalRanges(a1, a2, a3, v_rsp - 95 - 41);
loc_0080D85D:
    v_rsi = (unsigned int)(*(unsigned int *)(v_rsp - 95 - 85));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 119))))) & (2)) == 0) {
        v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 95 - 85))) | (1));
        *(unsigned int *)(v_rsp - 95 - 57) = (unsigned int)(v_rsi);
    }
    *(unsigned __int64 *)(v_rsp - 95 - 81) = v_rsp - 95 - 97;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 119))))) & (4)) == 0) goto loc_0080D88A;
    a4 = 0;
    a3 = 0;
    result = MiFreePartitionTree(*(unsigned __int64 *)(v_rsp - 95 + 103), v_rsp - 95 - 97, a3, a4);
    goto loc_0080D8A6;
loc_0080D88A:
    if ((*(unsigned int *)(v_rsp - 95 + 127)) != 12) {
        a4 = *(unsigned __int64 *)(v_rsp - 95 + 7);
        a3 = v_rsp - 95 - 81;
        a2 = *(unsigned __int64 *)(v_rsp - 95 + 103);
        a1 = v_rip + 6468703;
        result = MiInsertPartitionPages(a1, a2, a3, a4);
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 + 119) + 8) = *(unsigned __int64 *)(v_rsp - 95 + 7);
    goto loc_0080D632;
}
```

## 5. (Beta) C Style

```c
int64_t MiHotAddPartitionMemory(int64_t Arg1, void *Arg2, void *Arg3, int32_t Arg4)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p10;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(void **)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (176);
    Arg2 = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x51) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x5F - 0x41) = v_xmm0;
    result = memset(local_rsp - 95 - 41, Arg2, Arg2 + 72, Arg4);
    *(uint32_t *)(local_rsp - 0x5F + 0x7F) = 14;
    if (Arg1 != (v_rip + 6469368)) goto loc_0080D654;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg3)))) & (4)) != 0) goto loc_0080D650;
loc_0080D61B:
loc_0080D620:
    Arg4 = 0;
    Arg3 = 0;
    result = MiFreePartitionTree(Arg1, local_rsp - 95 - 97, Arg3, Arg4);
loc_0080D632:
    local_rsp = (local_rsp) + (176);
    return (uint32_t)((uint32_t)((uint32_t)(0xC00000BBULL)));
loc_0080D650:
    if ((((uint8_t)((uint32_t)((uint32_t)((uint32_t)(0xC00000BBULL))))) & (8)) != 0) goto loc_0080D61B;
loc_0080D654:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg3)))) & (32)) == 0) goto loc_0080D664;
    goto loc_0080D67E;
loc_0080D664:
    result = (uint32_t)((uint32_t)((uint32_t)(0xC00000BBULL)));
    local_r14 = (uint32_t)(0x40000ULL);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg3)))) & (64)) == 0) {
        result = 0;
        if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg3)))) & (4)) != 0) { result = (uint32_t)((uint32_t)(0x40000ULL)); }
        local_r14 = (uint32_t)(result);
    }
    *(uint32_t *)(local_rsp - 0x5F - 0x69) = (uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x4)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg3)))) & (1)) == 0) goto loc_0080D697;
    goto loc_0080D6B6;
loc_0080D697:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x4)))) & (32)) == 0) goto loc_0080D6A9;
loc_0080D69F:
    goto loc_0080D620;
loc_0080D6A9:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg3)))) & (4)) != 0) goto loc_0080D69F;
    local_r12 = 0;
loc_0080D6B6:
    local_rdi = 0;
    local_rbx = 0;
loc_0080D6BA:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x69))))) goto loc_0080D6ED;
    Arg4 = 0;
    local_rdi = (local_rdi) + (*(uint64_t *)(arg2 + 0x8));
    result = MiAddRangeToPartitionTree(local_rsp - 95 - 97, *(uint64_t *)(arg2), *(uint64_t *)(arg2 + 0x8), Arg4);
    if ((uint32_t)(result) == 0) goto loc_0080D6E3;
    local_rbx = (uint32_t)((local_rbx) + 1);
    local_rsi = (Arg2) + (16);
    goto loc_0080D6BA;
loc_0080D6E3:
    goto loc_0080D620;
loc_0080D6ED:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg3)))) & (4)) == 0) goto loc_0080D708;
    result = (uint32_t)(((uint8_t)((uint32_t)(*(uint32_t *)(arg3)))) & (2));
    *(uint8_t *)(local_rsp - 0x5F - 0x18) = 1;
    result = (uint32_t)((result) | (4));
    result = (uint32_t)((result) >> (1));
    *(uint32_t *)(local_rsp - 0x5F - 0x15) = (uint32_t)(result);
    goto loc_0080D71E;
loc_0080D708:
    result = MiUpdatePartitionLargePfnBitMap(Arg1, local_rsp - 95 - 97, *(uint64_t *)(arg2 + 0x8), Arg4);
    if (sign_flag) goto loc_0080D620;
loc_0080D71E:
    local_rbx = 0;
    local_rsi = (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x39));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x4)))) & (32)) != 0) {
        *(uint8_t *)(local_rsp - 0x5F - 0x19) = 1;
        local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x39))) | (8));
    }
    if (0 != 0) goto loc_0080D742;
    local_rsi = (uint32_t)((local_rsi) | (2));
    *(uint32_t *)(local_rsp - 0x5F - 0x39) = (uint32_t)(local_rsi);
    goto loc_0080D85D;
loc_0080D742:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg3))))) & (8));
    result = (uint32_t)((result) << (3));
    *(uint32_t *)(local_rsp - 0x5F - 0x69) = (uint32_t)(result);
    local_r12 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg3))) & (2));
    if (!(condition_is_not_equal)) {
    }
    *(uint64_t *)(local_rsp - 0x5F - 0x29) = Arg1;
    result = (uint32_t)(-((uint32_t)((uint32_t)(local_r12))));
    *(uint64_t *)(local_rsp - 0x5F + 0xF) = local_r14;
    result = (uint32_t)((result) + (12));
    *(uint32_t *)(local_rsp - 0x5F - 0x55) = (uint32_t)(local_rsi);
    *(uint32_t *)(local_rsp - 0x5F + 0x7F) = (uint32_t)(result);
    local_rdi = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x39) = (uint32_t)(local_rsi);
    goto loc_0080D78B;
loc_0080D785:
loc_0080D78B:
    if (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x61)) != 0) goto loc_0080D785;
    if (*(uint64_t *)(local_rsp - 0x5F - 0x61) == 0) goto loc_0080D84B;
loc_0080D7A4:
    if (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x61) + 0x8) == 0) goto loc_0080D7D6;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x61) + 0x8)) == 0) goto loc_0080D7E0;
loc_0080D7BE:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x61) + 0x8))) != 0) goto loc_0080D7BE;
    goto loc_0080D7E0;
loc_0080D7CE:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x61) + 0x8)))) == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x61) + 0x8))))) goto loc_0080D7E0;
loc_0080D7D6:
    local_rdi = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x61) + 0x8)) + 0x10)) & (-4);
    if (condition_is_not_equal) goto loc_0080D7CE;
loc_0080D7E0:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x59))) != 0) goto loc_0080D823;
    result = MiActOnPartitionNodePages(*(uint64_t *)(local_rsp - 0x5F - 0x61), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x7F)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x69)))), local_rsp - 95 - 41);
    if (!sign_flag) goto loc_0080D81E;
    result = (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x11));
    if ((uint32_t)(local_r12) != 0) {
        Arg1 = *(uint64_t *)(local_rsp - 0x5F - 0x61) + 32;
        Arg2 = 0;
        Arg3 = *(uint64_t *)(Arg1);
        result = RtlAreBitsClearEx(Arg1, Arg2, Arg3, local_rsp - 95 - 41);
        if ((uint8_t)(result) != 0) { local_rdi = *(uint64_t *)(local_rsp - 0x5F - 0x61); }
    }
loc_0080D81E:
    if ((uint32_t)(local_r12) == 0) {
        Arg2 = *(uint64_t *)(local_rsp - 0x5F - 0x61);
        Arg1 = local_rsp - 95 - 97;
        result = RtlAvlRemoveNode(Arg1, Arg2, Arg3, local_rsp - 95 - 41);
        Arg1 = *(uint64_t *)(local_rsp - 0x5F - 0x61);
        result = MiDeletePartitionPageNode(Arg1, Arg2, Arg3, local_rsp - 95 - 41);
    }
    if (local_rdi != 0) goto loc_0080D7A4;
loc_0080D84B:
    if (*(uint64_t *)(local_rsp - 0x5F + 0x7) == 0) goto loc_0080D620;
    result = IoUpdateDumpPhysicalRanges(Arg1, Arg2, Arg3, local_rsp - 95 - 41);
loc_0080D85D:
    local_rsi = (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x55));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x77))))) & (2)) == 0) {
        local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x55))) | (1));
        *(uint32_t *)(local_rsp - 0x5F - 0x39) = (uint32_t)(local_rsi);
    }
    *(uint64_t *)(local_rsp - 0x5F - 0x51) = local_rsp - 95 - 97;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x77))))) & (4)) == 0) goto loc_0080D88A;
    Arg4 = 0;
    Arg3 = 0;
    result = MiFreePartitionTree(*(uint64_t *)(local_rsp - 0x5F + 0x67), local_rsp - 95 - 97, Arg3, Arg4);
    goto loc_0080D8A6;
loc_0080D88A:
    if ((*(uint32_t *)(local_rsp - 0x5F + 0x7F)) != 12) {
        Arg4 = *(uint64_t *)(local_rsp - 0x5F + 0x7);
        Arg3 = local_rsp - 95 - 81;
        Arg2 = *(uint64_t *)(local_rsp - 0x5F + 0x67);
        Arg1 = v_rip + 6468703;
        result = MiInsertPartitionPages(Arg1, Arg2, Arg3, Arg4);
    }
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x77) + 0x8) = *(uint64_t *)(local_rsp - 0x5F + 0x7);
    goto loc_0080D632;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg3` | `+ 0x0` | `32` | `R` |
| `Arg3` | `+ 0x4` | `32` | `R` |
| `Arg3` | `+ 0x8` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0080D5B4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
