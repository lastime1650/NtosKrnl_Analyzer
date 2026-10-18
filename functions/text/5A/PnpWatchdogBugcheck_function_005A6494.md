# PnpWatchdogBugcheck

- RVA: `0x005A6494`–`0x005A67E9` (길이 `853` bytes)
- VA: `0x00000001405A6494`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C85DC`
- 디코드: `228`개 명령, `853/853` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **23**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005A64B6` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005A64F6` → [PnpInitializeTriageBlock](PnpInitializeTriageBlock_function_005A63C8.md) (function, `0x005A63C8`)
- `0x005A6522` → [PnpWatchdogExtractTriageInformation](../4D/PnpWatchdogExtractTriageInformation_function_004D9844.md) (function, `0x004D9844`)
- `0x005A6540` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x005A6551` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x005A655D` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x005A6572` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x005A657E` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x005A6599` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x005A65AA` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x005A65C4` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x005A65DA` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x005A65F4` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x005A6609` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x005A664D` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x005A6660` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x005A666D` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x005A66AE` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x005A66E9` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x005A6751` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x005A6794` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x005A67C6` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x005A67E3` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [PnpWatchdogSecondChanceCallback](PnpWatchdogSecondChanceCallback_function_005A67F0.md) at `0x005A682A`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005A6494  40 55                           push rbp
005A6496  53                              push rbx
005A6497  56                              push rsi
005A6498  57                              push rdi
005A6499  41 56                           push r14
005A649B  41 57                           push r15
005A649D  48 8D 6C 24 D1                  lea rbp, [rsp - 0x2f]
005A64A2  48 81 EC 88 00 00 00            sub rsp, 0x88
005A64A9  33 D2                           xor edx, edx
005A64AB  48 8B D9                        mov rbx, rcx
005A64AE  48 8D 4D D7                     lea rcx, [rbp - 0x29]
005A64B2  44 8D 42 50                     lea r8d, [rdx + 0x50]
005A64B6  E8 85 07 12 00                  call 0x1406c6c40
005A64BB  48 A1 08 00 00 00 80 F7 FF FF   movabs rax, qword ptr [0xfffff78000000008]
005A64C5  48 8D 4D D7                     lea rcx, [rbp - 0x29]
005A64C9  48 8B D0                        mov rdx, rax
005A64CC  45 33 F6                        xor r14d, r14d
005A64CF  48 2B 13                        sub rdx, qword ptr [rbx]
005A64D2  48 B8 4B 59 86 38 D6 C5 6D 34   movabs rax, 0x346dc5d63886594b
005A64DC  48 F7 E2                        mul rdx
005A64DF  4C 89 75 67                     mov qword ptr [rbp + 0x67], r14
005A64E3  48 8B F2                        mov rsi, rdx
005A64E6  4C 89 75 7F                     mov qword ptr [rbp + 0x7f], r14
005A64EA  48 C1 EE 0B                     shr rsi, 0xb
005A64EE  4C 89 75 6F                     mov qword ptr [rbp + 0x6f], r14
005A64F2  4C 89 75 77                     mov qword ptr [rbp + 0x77], r14
005A64F6  E8 CD FE FF FF                  call 0x1405a63c8
005A64FB  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
005A64FE  4C 8D 4D 6F                     lea r9, [rbp + 0x6f]
005A6502  89 45 DF                        mov dword ptr [rbp - 0x21], eax
005A6505  4C 8D 45 77                     lea r8, [rbp + 0x77]
005A6509  48 8D 45 1F                     lea rax, [rbp + 0x1f]
005A650D  48 8B CB                        mov rcx, rbx
005A6510  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
005A6515  48 8D 55 67                     lea rdx, [rbp + 0x67]
005A6519  48 8D 45 17                     lea rax, [rbp + 0x17]
005A651D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
005A6522  E8 1D 33 F3 FF                  call 0x1404d9844
005A6527  48 8B 5D 67                     mov rbx, qword ptr [rbp + 0x67]
005A652B  45 8D 7E 02                     lea r15d, [r14 + 2]
005A652F  48 85 DB                        test rbx, rbx
005A6532  74 7B                           je 0x1405a65af
005A6534  BA 88 03 00 00                  mov edx, 0x388
005A6539  48 8D 7B 28                     lea rdi, [rbx + 0x28]
005A653D  48 8B CB                        mov rcx, rbx
005A6540  E8 2F 1E E8 FF                  call 0x140428374
005A6545  66 44 39 37                     cmp word ptr [rdi], r14w
005A6549  74 17                           je 0x1405a6562
005A654B  41 8B D7                        mov edx, r15d
005A654E  48 8B CF                        mov rcx, rdi
005A6551  E8 1E 1E E8 FF                  call 0x140428374
005A6556  0F B7 17                        movzx edx, word ptr [rdi]
005A6559  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
005A655D  E8 12 1E E8 FF                  call 0x140428374
005A6562  48 8D 7B 38                     lea rdi, [rbx + 0x38]
005A6566  66 44 39 37                     cmp word ptr [rdi], r14w
005A656A  74 17                           je 0x1405a6583
005A656C  41 8B D7                        mov edx, r15d
005A656F  48 8B CF                        mov rcx, rdi
005A6572  E8 FD 1D E8 FF                  call 0x140428374
005A6577  0F B7 17                        movzx edx, word ptr [rdi]
005A657A  48 8B 4B 40                     mov rcx, qword ptr [rbx + 0x40]
005A657E  E8 F1 1D E8 FF                  call 0x140428374
005A6583  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
005A6587  48 85 C0                        test rax, rax
005A658A  74 23                           je 0x1405a65af
005A658C  48 8D 48 38                     lea rcx, [rax + 0x38]
005A6590  66 44 39 31                     cmp word ptr [rcx], r14w
005A6594  74 19                           je 0x1405a65af
005A6596  41 8B D7                        mov edx, r15d
005A6599  E8 D6 1D E8 FF                  call 0x140428374
005A659E  48 8B 4B 10                     mov rcx, qword ptr [rbx + 0x10]
005A65A2  0F B7 51 38                     movzx edx, word ptr [rcx + 0x38]
005A65A6  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
005A65AA  E8 C5 1D E8 FF                  call 0x140428374
005A65AF  48 8B 4D 17                     mov rcx, qword ptr [rbp + 0x17]
005A65B3  48 89 5D 0F                     mov qword ptr [rbp + 0xf], rbx
005A65B7  48 85 C9                        test rcx, rcx
005A65BA  0F 84 D9 01 00 00               je 0x1405a6799
005A65C0  0F B7 51 02                     movzx edx, word ptr [rcx + 2]
005A65C4  E8 AB 1D E8 FF                  call 0x140428374
005A65C9  48 8B 55 17                     mov rdx, qword ptr [rbp + 0x17]
005A65CD  48 8B 4A 08                     mov rcx, qword ptr [rdx + 8]
005A65D1  48 85 C9                        test rcx, rcx
005A65D4  74 3C                           je 0x1405a6612
005A65D6  0F BF 51 02                     movsx edx, word ptr [rcx + 2]
005A65DA  E8 95 1D E8 FF                  call 0x140428374
005A65DF  48 8B 55 17                     mov rdx, qword ptr [rbp + 0x17]
005A65E3  48 8B 4A 08                     mov rcx, qword ptr [rdx + 8]
005A65E7  48 83 C1 38                     add rcx, 0x38
005A65EB  66 44 39 31                     cmp word ptr [rcx], r14w
005A65EF  74 21                           je 0x1405a6612
005A65F1  41 8B D7                        mov edx, r15d
005A65F4  E8 7B 1D E8 FF                  call 0x140428374
005A65F9  48 8B 45 17                     mov rax, qword ptr [rbp + 0x17]
005A65FD  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
005A6601  0F B7 51 38                     movzx edx, word ptr [rcx + 0x38]
005A6605  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
005A6609  E8 66 1D E8 FF                  call 0x140428374
005A660E  48 8B 55 17                     mov rdx, qword ptr [rbp + 0x17]
005A6612  48 85 D2                        test rdx, rdx
005A6615  0F 84 7E 01 00 00               je 0x1405a6799
005A661B  48 8B 82 38 01 00 00            mov rax, qword ptr [rdx + 0x138]
005A6622  4C 39 70 28                     cmp qword ptr [rax + 0x28], r14
005A6626  0F 84 6D 01 00 00               je 0x1405a6799
005A662C  48 85 D2                        test rdx, rdx
005A662F  74 06                           je 0x1405a6637
005A6631  48 8B 58 28                     mov rbx, qword ptr [rax + 0x28]
005A6635  EB 03                           jmp 0x1405a663a
005A6637  49 8B DE                        mov rbx, r14
005A663A  48 85 D2                        test rdx, rdx
005A663D  74 06                           je 0x1405a6645
005A663F  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
005A6643  EB 03                           jmp 0x1405a6648
005A6645  49 8B CE                        mov rcx, r14
005A6648  BA 88 03 00 00                  mov edx, 0x388
005A664D  E8 22 1D E8 FF                  call 0x140428374
005A6652  66 44 39 73 28                  cmp word ptr [rbx + 0x28], r14w
005A6657  74 19                           je 0x1405a6672
005A6659  41 8B D7                        mov edx, r15d
005A665C  48 8D 4B 28                     lea rcx, [rbx + 0x28]
005A6660  E8 0F 1D E8 FF                  call 0x140428374
005A6665  0F B7 53 28                     movzx edx, word ptr [rbx + 0x28]
005A6669  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
005A666D  E8 02 1D E8 FF                  call 0x140428374
005A6672  48 8B 4D 17                     mov rcx, qword ptr [rbp + 0x17]
005A6676  48 85 C9                        test rcx, rcx
005A6679  74 0D                           je 0x1405a6688
005A667B  48 8B 81 38 01 00 00            mov rax, qword ptr [rcx + 0x138]
005A6682  48 8B 50 28                     mov rdx, qword ptr [rax + 0x28]
005A6686  EB 03                           jmp 0x1405a668b
005A6688  49 8B D6                        mov rdx, r14
005A668B  66 44 39 72 38                  cmp word ptr [rdx + 0x38], r14w
005A6690  74 60                           je 0x1405a66f2
005A6692  48 85 C9                        test rcx, rcx
005A6695  74 0D                           je 0x1405a66a4
005A6697  48 8B 81 38 01 00 00            mov rax, qword ptr [rcx + 0x138]
005A669E  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
005A66A2  EB 03                           jmp 0x1405a66a7
005A66A4  49 8B CE                        mov rcx, r14
005A66A7  48 83 C1 38                     add rcx, 0x38
005A66AB  41 8B D7                        mov edx, r15d
005A66AE  E8 C1 1C E8 FF                  call 0x140428374
005A66B3  48 8B 4D 17                     mov rcx, qword ptr [rbp + 0x17]
005A66B7  48 85 C9                        test rcx, rcx
005A66BA  74 0D                           je 0x1405a66c9
005A66BC  48 8B 81 38 01 00 00            mov rax, qword ptr [rcx + 0x138]
005A66C3  48 8B 50 28                     mov rdx, qword ptr [rax + 0x28]
005A66C7  EB 03                           jmp 0x1405a66cc
005A66C9  49 8B D6                        mov rdx, r14
005A66CC  48 85 C9                        test rcx, rcx
005A66CF  74 0D                           je 0x1405a66de
005A66D1  48 8B 81 38 01 00 00            mov rax, qword ptr [rcx + 0x138]
005A66D8  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
005A66DC  EB 03                           jmp 0x1405a66e1
005A66DE  49 8B CE                        mov rcx, r14
005A66E1  0F B7 52 38                     movzx edx, word ptr [rdx + 0x38]
005A66E5  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
005A66E9  E8 86 1C E8 FF                  call 0x140428374
005A66EE  48 8B 4D 17                     mov rcx, qword ptr [rbp + 0x17]
005A66F2  48 85 C9                        test rcx, rcx
005A66F5  74 0D                           je 0x1405a6704
005A66F7  48 8B 81 38 01 00 00            mov rax, qword ptr [rcx + 0x138]
005A66FE  48 8B 50 28                     mov rdx, qword ptr [rax + 0x28]
005A6702  EB 03                           jmp 0x1405a6707
005A6704  49 8B D6                        mov rdx, r14
005A6707  4C 39 72 10                     cmp qword ptr [rdx + 0x10], r14
005A670B  0F 84 88 00 00 00               je 0x1405a6799
005A6711  48 85 C9                        test rcx, rcx
005A6714  74 0D                           je 0x1405a6723
005A6716  48 8B 81 38 01 00 00            mov rax, qword ptr [rcx + 0x138]
005A671D  48 8B 40 28                     mov rax, qword ptr [rax + 0x28]
005A6721  EB 03                           jmp 0x1405a6726
005A6723  49 8B C6                        mov rax, r14
005A6726  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
005A672A  66 44 39 70 38                  cmp word ptr [rax + 0x38], r14w
005A672F  74 68                           je 0x1405a6799
005A6731  48 85 C9                        test rcx, rcx
005A6734  74 0D                           je 0x1405a6743
005A6736  48 8B 81 38 01 00 00            mov rax, qword ptr [rcx + 0x138]
005A673D  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
005A6741  EB 03                           jmp 0x1405a6746
005A6743  49 8B CE                        mov rcx, r14
005A6746  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
005A674A  41 8B D7                        mov edx, r15d
005A674D  48 83 C1 38                     add rcx, 0x38
005A6751  E8 1E 1C E8 FF                  call 0x140428374
005A6756  48 8B 4D 17                     mov rcx, qword ptr [rbp + 0x17]
005A675A  48 85 C9                        test rcx, rcx
005A675D  74 0D                           je 0x1405a676c
005A675F  48 8B 81 38 01 00 00            mov rax, qword ptr [rcx + 0x138]
005A6766  48 8B 50 28                     mov rdx, qword ptr [rax + 0x28]
005A676A  EB 03                           jmp 0x1405a676f
005A676C  49 8B D6                        mov rdx, r14
005A676F  48 85 C9                        test rcx, rcx
005A6772  74 0D                           je 0x1405a6781
005A6774  48 8B 81 38 01 00 00            mov rax, qword ptr [rcx + 0x138]
005A677B  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
005A677F  EB 03                           jmp 0x1405a6784
005A6781  49 8B CE                        mov rcx, r14
005A6784  48 8B 42 10                     mov rax, qword ptr [rdx + 0x10]
005A6788  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
005A678C  0F B7 50 38                     movzx edx, word ptr [rax + 0x38]
005A6790  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
005A6794  E8 DB 1B E8 FF                  call 0x140428374
005A6799  48 8B 45 6F                     mov rax, qword ptr [rbp + 0x6f]
005A679D  48 85 C0                        test rax, rax
005A67A0  74 29                           je 0x1405a67cb
005A67A2  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
005A67A6  48 85 D2                        test rdx, rdx
005A67A9  74 20                           je 0x1405a67cb
005A67AB  0F B7 08                        movzx ecx, word ptr [rax]
005A67AE  66 85 C9                        test cx, cx
005A67B1  74 18                           je 0x1405a67cb
005A67B3  41 B8 08 00 00 00               mov r8d, 8
005A67B9  66 41 3B C8                     cmp cx, r8w
005A67BD  73 03                           jae 0x1405a67c2
005A67BF  44 8B C1                        mov r8d, ecx
005A67C2  48 8D 4D 7F                     lea rcx, [rbp + 0x7f]
005A67C6  E8 75 00 12 00                  call 0x1406c6840
005A67CB  4C 8B 4D 77                     mov r9, qword ptr [rbp + 0x77]
005A67CF  4C 8D 45 D7                     lea r8, [rbp - 0x29]
005A67D3  48 8B 55 7F                     mov rdx, qword ptr [rbp + 0x7f]
005A67D7  B9 D5 01 00 00                  mov ecx, 0x1d5
005A67DC  8B C6                           mov eax, esi
005A67DE  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
005A67E3  E8 78 6E F5 FF                  call 0x1404fd660
005A67E8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpWatchdogBugcheck(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m5F;
    unsigned int v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (136);
    a2 = 0;
    result = memset(v_stack_m88, a2, a2 + 80, a4);
    v_r14 = 0;
    a2 = (result) - (*(unsigned __int64 *)(a1));
    v_stack_p8 = 0;
    v_stack_p20 = 0;
    v_rsi = (a2) >> (11);
    v_stack_p10 = 0;
    v_stack_p18 = 0;
    result = PnpInitializeTriageBlock(v_stack_m88, a2, a2 + 80, a4);
    v_stack_m80 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16)));
    v_stack_m90 = v_stack_m40;
    v_stack_m98 = v_stack_m48;
    result = PnpWatchdogExtractTriageInformation(a1, v_stack_p8, v_stack_p18, v_stack_p10);
    if (v_stack_p8 == 0) goto loc_005A65AF;
    result = IoAddTriageDumpDataBlock(v_stack_p8, 904, v_stack_p18, v_stack_p10);
    if ((*(unsigned __int16 *)(v_stack_p8 + 40)) != 0) {
        a2 = (unsigned int)(v_r14 + 2);
        a1 = v_stack_p8 + 40;
        result = IoAddTriageDumpDataBlock(a1, a2, v_stack_p18, v_stack_p10);
        a2 = *(unsigned __int16 *)(v_stack_p8 + 40);
        a1 = *(unsigned __int64 *)(v_stack_p8 + 40 + 8);
        result = IoAddTriageDumpDataBlock(a1, a2, v_stack_p18, v_stack_p10);
    }
    if ((*(unsigned __int16 *)(v_stack_p8 + 56)) != 0) {
        a2 = (unsigned int)(v_r14 + 2);
        a1 = v_stack_p8 + 56;
        result = IoAddTriageDumpDataBlock(a1, a2, v_stack_p18, v_stack_p10);
        a2 = *(unsigned __int16 *)(v_stack_p8 + 56);
        a1 = *(unsigned __int64 *)(v_stack_p8 + 64);
        result = IoAddTriageDumpDataBlock(a1, a2, v_stack_p18, v_stack_p10);
    }
    if (*(unsigned __int64 *)(v_stack_p8 + 16) == 0) goto loc_005A65AF;
    result = *(unsigned __int64 *)(v_stack_p8 + 16);
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p8 + 16) + 56)) != 0) {
        a2 = (unsigned int)(v_r14 + 2);
        result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(v_stack_p8 + 16) + 56, a2, v_stack_p18, v_stack_p10);
        a1 = *(unsigned __int64 *)(v_stack_p8 + 16);
        a2 = *(unsigned __int16 *)(a1 + 56);
        a1 = *(unsigned __int64 *)(a1 + 64);
        result = IoAddTriageDumpDataBlock(a1, a2, v_stack_p18, v_stack_p10);
    }
    v_stack_m50 = v_stack_p8;
    if (v_stack_m48 == 0) goto loc_005A6799;
    result = IoAddTriageDumpDataBlock(v_stack_m48, *(unsigned __int16 *)(v_stack_m48 + 2), v_stack_p18, v_stack_p10);
    if (*(unsigned __int64 *)(v_stack_m48 + 8) == 0) goto loc_005A6612;
    result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(v_stack_m48 + 8), (__int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m48 + 8) + 2)), v_stack_p18, v_stack_p10);
    a1 = (*(unsigned __int64 *)(v_stack_m48 + 8)) + (56);
    if ((*(unsigned __int16 *)(a1)) != 0) {
        a2 = (unsigned int)(v_r14 + 2);
        result = IoAddTriageDumpDataBlock(a1, a2, v_stack_p18, v_stack_p10);
        result = v_stack_m48;
        a1 = *(unsigned __int64 *)(result + 8);
        a2 = *(unsigned __int16 *)(a1 + 56);
        a1 = *(unsigned __int64 *)(a1 + 64);
        result = IoAddTriageDumpDataBlock(a1, a2, v_stack_p18, v_stack_p10);
        a2 = v_stack_m48;
    }
    if (a2 == 0) goto loc_005A6799;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 312) + 40)) == 0) goto loc_005A6799;
    if (a2 == 0) goto loc_005A6637;
    goto loc_005A663A;
loc_005A6637:
loc_005A663A:
    if (a2 == 0) goto loc_005A6645;
    goto loc_005A6648;
loc_005A6645:
loc_005A6648:
    result = IoAddTriageDumpDataBlock(0, 904, v_stack_p18, v_stack_p10);
    if ((*(unsigned __int16 *)(0 + 40)) != 0) {
        a2 = (unsigned int)(v_r14 + 2);
        a1 = 0 + 40;
        result = IoAddTriageDumpDataBlock(a1, a2, v_stack_p18, v_stack_p10);
        a2 = *(unsigned __int16 *)(0 + 40);
        a1 = *(unsigned __int64 *)(0 + 48);
        result = IoAddTriageDumpDataBlock(a1, a2, v_stack_p18, v_stack_p10);
    }
    if (v_stack_m48 == 0) goto loc_005A6688;
    goto loc_005A668B;
loc_005A6688:
loc_005A668B:
    if ((*(unsigned __int16 *)(0 + 56)) == 0) goto loc_005A66F2;
    if (v_stack_m48 == 0) goto loc_005A66A4;
    goto loc_005A66A7;
loc_005A66A4:
loc_005A66A7:
    a1 = (0) + (56);
    result = IoAddTriageDumpDataBlock(a1, (unsigned int)((unsigned int)(v_r14 + 2)), v_stack_p18, v_stack_p10);
    if (v_stack_m48 == 0) goto loc_005A66C9;
    goto loc_005A66CC;
loc_005A66C9:
loc_005A66CC:
    if (v_stack_m48 == 0) goto loc_005A66DE;
    goto loc_005A66E1;
loc_005A66DE:
loc_005A66E1:
    result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(0 + 64), *(unsigned __int16 *)(0 + 56), v_stack_p18, v_stack_p10);
loc_005A66F2:
    if (v_stack_m48 == 0) goto loc_005A6704;
    goto loc_005A6707;
loc_005A6704:
loc_005A6707:
    if ((*(unsigned __int64 *)(0 + 16)) == 0) goto loc_005A6799;
    if (v_stack_m48 == 0) goto loc_005A6723;
    goto loc_005A6726;
loc_005A6723:
loc_005A6726:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(0 + 16) + 56)) == 0) goto loc_005A6799;
    if (v_stack_m48 == 0) goto loc_005A6743;
    goto loc_005A6746;
loc_005A6743:
loc_005A6746:
    a1 = (*(unsigned __int64 *)(0 + 16)) + (56);
    result = IoAddTriageDumpDataBlock(a1, (unsigned int)((unsigned int)(v_r14 + 2)), v_stack_p18, v_stack_p10);
    if (v_stack_m48 == 0) goto loc_005A676C;
    goto loc_005A676F;
loc_005A676C:
loc_005A676F:
    if (v_stack_m48 == 0) goto loc_005A6781;
    goto loc_005A6784;
loc_005A6781:
loc_005A6784:
    result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(*(unsigned __int64 *)(0 + 16) + 64), *(unsigned __int16 *)(*(unsigned __int64 *)(0 + 16) + 56), v_stack_p18, v_stack_p10);
loc_005A6799:
    if (v_stack_p10 == 0) goto loc_005A67CB;
    if (*(unsigned __int64 *)(v_stack_p10 + 8) == 0) goto loc_005A67CB;
    if ((unsigned __int16)(*(unsigned __int16 *)(v_stack_p10)) == 0) goto loc_005A67CB;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_p10))) < 8) {
        a3 = (unsigned int)(*(unsigned __int16 *)(v_stack_p10));
    }
    result = memcpy(v_stack_p20, *(unsigned __int64 *)(v_stack_p10 + 8), a3, v_stack_p10);
loc_005A67CB:
    v_stack_m98 = (unsigned int)((unsigned int)(v_rsi));
    result = KeBugCheckEx(469, v_stack_p20, v_stack_m88, v_stack_p18);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PnpWatchdogBugcheck(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r14;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m5F;
    uint32_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (136);
    Arg2 = 0;
    result = memset(v_stack_m88, Arg2, Arg2 + 80, a4);
    local_r14 = 0;
    Arg2 = (result) - (*(uint64_t *)(arg1));
    v_stack_p8 = 0;
    v_stack_p20 = 0;
    local_rsi = (Arg2) >> (11);
    v_stack_p10 = 0;
    v_stack_p18 = 0;
    result = PnpInitializeTriageBlock(v_stack_m88, Arg2, Arg2 + 80, a4);
    v_stack_m80 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10)));
    v_stack_m90 = v_stack_m40;
    v_stack_m98 = v_stack_m48;
    result = PnpWatchdogExtractTriageInformation(Arg1, v_stack_p8, v_stack_p18, v_stack_p10);
    if (v_stack_p8 == 0) goto loc_005A65AF;
    result = IoAddTriageDumpDataBlock(v_stack_p8, 904, v_stack_p18, v_stack_p10);
    if ((*(uint16_t *)(v_stack_p8 + 0x28)) != 0) {
        Arg2 = (uint32_t)(local_r14 + 2);
        Arg1 = v_stack_p8 + 40;
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, v_stack_p18, v_stack_p10);
        Arg2 = *(uint16_t *)(v_stack_p8 + 0x28);
        Arg1 = *(uint64_t *)(v_stack_p8 + 0x28 + 0x8);
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, v_stack_p18, v_stack_p10);
    }
    if ((*(uint16_t *)(v_stack_p8 + 0x38)) != 0) {
        Arg2 = (uint32_t)(local_r14 + 2);
        Arg1 = v_stack_p8 + 56;
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, v_stack_p18, v_stack_p10);
        Arg2 = *(uint16_t *)(v_stack_p8 + 0x38);
        Arg1 = *(uint64_t *)(v_stack_p8 + 0x40);
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, v_stack_p18, v_stack_p10);
    }
    if (*(uint64_t *)(v_stack_p8 + 0x10) == 0) goto loc_005A65AF;
    result = *(uint64_t *)(v_stack_p8 + 0x10);
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_p8 + 0x10) + 0x38)) != 0) {
        Arg2 = (uint32_t)(local_r14 + 2);
        result = IoAddTriageDumpDataBlock(*(uint64_t *)(v_stack_p8 + 0x10) + 56, Arg2, v_stack_p18, v_stack_p10);
        Arg1 = *(uint64_t *)(v_stack_p8 + 0x10);
        Arg2 = *(uint16_t *)(arg1 + 0x38);
        Arg1 = *(uint64_t *)(arg1 + 0x40);
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, v_stack_p18, v_stack_p10);
    }
    v_stack_m50 = v_stack_p8;
    if (v_stack_m48 == 0) goto loc_005A6799;
    result = IoAddTriageDumpDataBlock(v_stack_m48, *(uint16_t *)(v_stack_m48 + 0x2), v_stack_p18, v_stack_p10);
    if (*(uint64_t *)(v_stack_m48 + 0x8) == 0) goto loc_005A6612;
    result = IoAddTriageDumpDataBlock(*(uint64_t *)(v_stack_m48 + 0x8), (int16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_m48 + 0x8) + 0x2)), v_stack_p18, v_stack_p10);
    Arg1 = (*(uint64_t *)(v_stack_m48 + 0x8)) + (56);
    if ((*(uint16_t *)(arg1)) != 0) {
        Arg2 = (uint32_t)(local_r14 + 2);
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, v_stack_p18, v_stack_p10);
        result = v_stack_m48;
        Arg1 = *(uint64_t *)(result + 0x8);
        Arg2 = *(uint16_t *)(arg1 + 0x38);
        Arg1 = *(uint64_t *)(arg1 + 0x40);
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, v_stack_p18, v_stack_p10);
        Arg2 = v_stack_m48;
    }
    if (Arg2 == 0) goto loc_005A6799;
    if ((*(uint64_t *)(*(uint64_t *)(Arg2 + 0x138) + 0x28)) == 0) goto loc_005A6799;
    if (Arg2 == 0) goto loc_005A6637;
    goto loc_005A663A;
loc_005A6637:
loc_005A663A:
    if (Arg2 == 0) goto loc_005A6645;
    goto loc_005A6648;
loc_005A6645:
loc_005A6648:
    result = IoAddTriageDumpDataBlock(0, 904, v_stack_p18, v_stack_p10);
    if ((*(uint16_t *)(0 + 0x28)) != 0) {
        Arg2 = (uint32_t)(local_r14 + 2);
        Arg1 = 0 + 40;
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, v_stack_p18, v_stack_p10);
        Arg2 = *(uint16_t *)(0 + 0x28);
        Arg1 = *(uint64_t *)(0 + 0x30);
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, v_stack_p18, v_stack_p10);
    }
    if (v_stack_m48 == 0) goto loc_005A6688;
    goto loc_005A668B;
loc_005A6688:
loc_005A668B:
    if ((*(uint16_t *)(0 + 0x38)) == 0) goto loc_005A66F2;
    if (v_stack_m48 == 0) goto loc_005A66A4;
    goto loc_005A66A7;
loc_005A66A4:
loc_005A66A7:
    Arg1 = (0) + (56);
    result = IoAddTriageDumpDataBlock(Arg1, (uint32_t)((uint32_t)(local_r14 + 2)), v_stack_p18, v_stack_p10);
    if (v_stack_m48 == 0) goto loc_005A66C9;
    goto loc_005A66CC;
loc_005A66C9:
loc_005A66CC:
    if (v_stack_m48 == 0) goto loc_005A66DE;
    goto loc_005A66E1;
loc_005A66DE:
loc_005A66E1:
    result = IoAddTriageDumpDataBlock(*(uint64_t *)(0 + 0x40), *(uint16_t *)(0 + 0x38), v_stack_p18, v_stack_p10);
loc_005A66F2:
    if (v_stack_m48 == 0) goto loc_005A6704;
    goto loc_005A6707;
loc_005A6704:
loc_005A6707:
    if ((*(uint64_t *)(0 + 0x10)) == 0) goto loc_005A6799;
    if (v_stack_m48 == 0) goto loc_005A6723;
    goto loc_005A6726;
loc_005A6723:
loc_005A6726:
    if ((*(uint16_t *)(*(uint64_t *)(0 + 0x10) + 0x38)) == 0) goto loc_005A6799;
    if (v_stack_m48 == 0) goto loc_005A6743;
    goto loc_005A6746;
loc_005A6743:
loc_005A6746:
    Arg1 = (*(uint64_t *)(0 + 0x10)) + (56);
    result = IoAddTriageDumpDataBlock(Arg1, (uint32_t)((uint32_t)(local_r14 + 2)), v_stack_p18, v_stack_p10);
    if (v_stack_m48 == 0) goto loc_005A676C;
    goto loc_005A676F;
loc_005A676C:
loc_005A676F:
    if (v_stack_m48 == 0) goto loc_005A6781;
    goto loc_005A6784;
loc_005A6781:
loc_005A6784:
    result = IoAddTriageDumpDataBlock(*(uint64_t *)(*(uint64_t *)(0 + 0x10) + 0x40), *(uint16_t *)(*(uint64_t *)(0 + 0x10) + 0x38), v_stack_p18, v_stack_p10);
loc_005A6799:
    if (v_stack_p10 == 0) goto loc_005A67CB;
    if (*(uint64_t *)(v_stack_p10 + 0x8) == 0) goto loc_005A67CB;
    if ((uint16_t)(*(uint16_t *)(v_stack_p10)) == 0) goto loc_005A67CB;
    if (((uint16_t)(*(uint16_t *)(v_stack_p10))) < 8) {
        a3 = (uint32_t)(*(uint16_t *)(v_stack_p10));
    }
    result = memcpy(v_stack_p20, *(uint64_t *)(v_stack_p10 + 0x8), a3, v_stack_p10);
loc_005A67CB:
    v_stack_m98 = (uint32_t)((uint32_t)(local_rsi));
    result = KeBugCheckEx(469, v_stack_p20, v_stack_m88, v_stack_p18);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x10` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005A6494&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
