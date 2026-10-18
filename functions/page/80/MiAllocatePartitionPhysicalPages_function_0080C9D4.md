# MiAllocatePartitionPhysicalPages

- RVA: `0x0080C9D4`–`0x0080D06E` (길이 `1,690` bytes)
- VA: `0x000000014080C9D4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D9100`
- 디코드: `452`개 명령, `1,690/1,690` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **25**; 고유 호출 대상: **24**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x0080CAB1` → [MiAcquireNonPagedResources](../../text/28/MiAcquireNonPagedResources_function_00286C60.md) (function, `0x00286C60`)
- `0x0080CB6D` → [MiInitializeDemandCoalesceContext](../../text/3D/MiInitializeDemandCoalesceContext_function_003D3350.md) (function, `0x003D3350`)
- `0x0080CBC8` → [MiGetHugeBadRangeFromNode](../../text/67/MiGetHugeBadRangeFromNode_function_00675818.md) (function, `0x00675818`)
- `0x0080CBED` → [MiInitializePageColorBase](../../text/32/MiInitializePageColorBase_function_00320410.md) (function, `0x00320410`)
- `0x0080CC01` → [MiGetNextPageColor](../../text/44/MiGetNextPageColor_function_00442D64.md) (function, `0x00442D64`)
- `0x0080CC21` → [MiGetHugeRange](../../text/67/MiGetHugeRange_function_00675954.md) (function, `0x00675954`)
- `0x0080CC5C` → [MiHugeRangeIsZeroed](../../text/67/MiHugeRangeIsZeroed_function_006763EC.md) (function, `0x006763EC`)
- `0x0080CCC8` → [MiFindLargeNodePage](../../text/4D/MiFindLargeNodePage_function_004DB7E8.md) (function, `0x004DB7E8`)
- `0x0080CCFF` → [MiGetPfnPageSizeIndex](../../text/31/MiGetPfnPageSizeIndex_function_0031C710.md) (function, `0x0031C710`)
- `0x0080CD1E` → [MiInitializeFoundLargeNodePage](../../text/4F/MiInitializeFoundLargeNodePage_function_004F97E8.md) (function, `0x004F97E8`)
- `0x0080CD4F` → [MiHugePageOperation](../../text/68/MiHugePageOperation_function_0068C490.md) (function, `0x0068C490`)
- `0x0080CD65` → [MiZeroLargePage](../../text/2C/MiZeroLargePage_function_002C6914.md) (function, `0x002C6914`)
- `0x0080CD91` → [MiAddRangeToPartitionTree](../../text/69/MiAddRangeToPartitionTree_function_0069020C.md) (function, `0x0069020C`)
- `0x0080CDD4` → [MiInsertHugeRangeInPartition](../../text/69/MiInsertHugeRangeInPartition_function_00690F28.md) (function, `0x00690F28`)
- `0x0080CDF0` → [MiFreeMdlPageRun](../../text/37/MiFreeMdlPageRun_function_00375A4C.md) (function, `0x00375A4C`)
- `0x0080CE38` → [MiReleaseNonPagedResourcesNotExposed](../../text/3F/MiReleaseNonPagedResourcesNotExposed_function_003F8258.md) (function, `0x003F8258`)
- `0x0080CF31` → [MiAllocatePagesForMdl](../../text/3E/MiAllocatePagesForMdl_function_003EABEC.md) (function, `0x003EABEC`)
- `0x0080CF6C` → [MiAddMdlToPartitionTree](../../text/69/MiAddMdlToPartitionTree_function_00690120.md) (function, `0x00690120`)
- `0x0080CF87` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0080CF95` → [MiFreePagesFromMdl](../../text/3F/MiFreePagesFromMdl_function_003F8300.md) (function, `0x003F8300`)
- `0x0080CF9F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0080CFBE` → [MiUpdatePartitionLargePfnBitMap](MiUpdatePartitionLargePfnBitMap_function_0080DB50.md) (function, `0x0080DB50`)
- `0x0080CFD9` → [MiFreePartitionTree](../../text/69/MiFreePartitionTree_function_00690E50.md) (function, `0x00690E50`)
- `0x0080D048` → [MiInsertPartitionPages](../../text/69/MiInsertPartitionPages_function_006911A0.md) (function, `0x006911A0`)
- `0x0080D054` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [MiReleasePartitionHugeIoSpace](../../text/67/MiReleasePartitionHugeIoSpace_function_00677038.md) at `0x00677079`
- [MmManagePartitionMoveMemory](MmManagePartitionMoveMemory_function_0080E1F4.md) at `0x0080E44C`

### Static image references
- `0x0080C9ED` → RVA `0x00E0A740` (`.data`; read)
- `0x0080CA01` → RVA `0x00E38D00` (`.data`; read)
- `0x0080CAE1` → RVA `0x00FC5000` (`ALMOSTRO`; read)
- `0x0080CAE8` → RVA `0x00E2DBD0` (`.data`; read)
- `0x0080CD79` → RVA `0x00011C60` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **24**
  - `0x0080CAB1` → [MiAcquireNonPagedResources](../../text/28/MiAcquireNonPagedResources_function_00286C60.md) (`PAGE` → `.text`)
  - `0x0080CB6D` → [MiInitializeDemandCoalesceContext](../../text/3D/MiInitializeDemandCoalesceContext_function_003D3350.md) (`PAGE` → `.text`)
  - `0x0080CBC8` → [MiGetHugeBadRangeFromNode](../../text/67/MiGetHugeBadRangeFromNode_function_00675818.md) (`PAGE` → `.text`)
  - `0x0080CBED` → [MiInitializePageColorBase](../../text/32/MiInitializePageColorBase_function_00320410.md) (`PAGE` → `.text`)
  - `0x0080CC01` → [MiGetNextPageColor](../../text/44/MiGetNextPageColor_function_00442D64.md) (`PAGE` → `.text`)
  - `0x0080CC21` → [MiGetHugeRange](../../text/67/MiGetHugeRange_function_00675954.md) (`PAGE` → `.text`)
  - `0x0080CC5C` → [MiHugeRangeIsZeroed](../../text/67/MiHugeRangeIsZeroed_function_006763EC.md) (`PAGE` → `.text`)
  - `0x0080CCC8` → [MiFindLargeNodePage](../../text/4D/MiFindLargeNodePage_function_004DB7E8.md) (`PAGE` → `.text`)
  - `0x0080CCFF` → [MiGetPfnPageSizeIndex](../../text/31/MiGetPfnPageSizeIndex_function_0031C710.md) (`PAGE` → `.text`)
  - `0x0080CD1E` → [MiInitializeFoundLargeNodePage](../../text/4F/MiInitializeFoundLargeNodePage_function_004F97E8.md) (`PAGE` → `.text`)
  - `0x0080CD4F` → [MiHugePageOperation](../../text/68/MiHugePageOperation_function_0068C490.md) (`PAGE` → `.text`)
  - `0x0080CD65` → [MiZeroLargePage](../../text/2C/MiZeroLargePage_function_002C6914.md) (`PAGE` → `.text`)
  - `0x0080CD91` → [MiAddRangeToPartitionTree](../../text/69/MiAddRangeToPartitionTree_function_0069020C.md) (`PAGE` → `.text`)
  - `0x0080CDD4` → [MiInsertHugeRangeInPartition](../../text/69/MiInsertHugeRangeInPartition_function_00690F28.md) (`PAGE` → `.text`)
  - `0x0080CDF0` → [MiFreeMdlPageRun](../../text/37/MiFreeMdlPageRun_function_00375A4C.md) (`PAGE` → `.text`)
  - `0x0080CE38` → [MiReleaseNonPagedResourcesNotExposed](../../text/3F/MiReleaseNonPagedResourcesNotExposed_function_003F8258.md) (`PAGE` → `.text`)
  - `0x0080CF31` → [MiAllocatePagesForMdl](../../text/3E/MiAllocatePagesForMdl_function_003EABEC.md) (`PAGE` → `.text`)
  - `0x0080CF6C` → [MiAddMdlToPartitionTree](../../text/69/MiAddMdlToPartitionTree_function_00690120.md) (`PAGE` → `.text`)
  - `0x0080CF87` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0080CF95` → [MiFreePagesFromMdl](../../text/3F/MiFreePagesFromMdl_function_003F8300.md) (`PAGE` → `.text`)
  - `0x0080CF9F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0080CFD9` → [MiFreePartitionTree](../../text/69/MiFreePartitionTree_function_00690E50.md) (`PAGE` → `.text`)
  - `0x0080D048` → [MiInsertPartitionPages](../../text/69/MiInsertPartitionPages_function_006911A0.md) (`PAGE` → `.text`)
  - `0x0080D054` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0080C9D4  40 55                           push rbp
0080C9D6  53                              push rbx
0080C9D7  56                              push rsi
0080C9D8  57                              push rdi
0080C9D9  41 54                           push r12
0080C9DB  41 55                           push r13
0080C9DD  41 56                           push r14
0080C9DF  41 57                           push r15
0080C9E1  48 8D 6C 24 B8                  lea rbp, [rsp - 0x48]
0080C9E6  48 81 EC 48 01 00 00            sub rsp, 0x148
0080C9ED  48 8B 05 4C DD 5F 00            mov rax, qword ptr [rip + 0x5fdd4c]
0080C9F4  48 33 C4                        xor rax, rsp
0080C9F7  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
0080C9FB  8B 9D B0 00 00 00               mov ebx, dword ptr [rbp + 0xb0]
0080CA01  4C 8D 2D F8 C2 62 00            lea r13, [rip + 0x62c2f8]
0080CA08  0F 57 C0                        xorps xmm0, xmm0
0080CA0B  48 89 55 B8                     mov qword ptr [rbp - 0x48], rdx
0080CA0F  48 8B C2                        mov rax, rdx
0080CA12  4C 89 44 24 68                  mov qword ptr [rsp + 0x68], r8
0080CA17  33 D2                           xor edx, edx
0080CA19  41 8B F1                        mov esi, r9d
0080CA1C  48 21 55 90                     and qword ptr [rbp - 0x70], rdx
0080CA20  4D 8B D0                        mov r10, r8
0080CA23  48 85 C9                        test rcx, rcx
0080CA26  48 89 55 20                     mov qword ptr [rbp + 0x20], rdx
0080CA2A  89 55 28                        mov dword ptr [rbp + 0x28], edx
0080CA2D  4C 0F 45 E9                     cmovne r13, rcx
0080CA31  48 21 54 24 70                  and qword ptr [rsp + 0x70], rdx
0080CA36  8B D3                           mov edx, ebx
0080CA38  B9 00 00 10 00                  mov ecx, 0x100000
0080CA3D  81 E2 00 04 00 00               and edx, 0x400
0080CA43  89 55 A8                        mov dword ptr [rbp - 0x58], edx
0080CA46  0F 11 45 C0                     movups xmmword ptr [rbp - 0x40], xmm0
0080CA4A  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0080CA4E  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
0080CA52  0F 11 45 00                     movups xmmword ptr [rbp], xmm0
0080CA56  0F 11 45 10                     movups xmmword ptr [rbp + 0x10], xmm0
0080CA5A  74 05                           je 0x14080ca61
0080CA5C  8D 41 01                        lea eax, [rcx + 1]
0080CA5F  EB 0F                           jmp 0x14080ca70
0080CA61  8B 40 04                        mov eax, dword ptr [rax + 4]
0080CA64  A8 20                           test al, 0x20
0080CA66  B8 01 00 10 00                  mov eax, 0x100001
0080CA6B  0F 44 C8                        cmove ecx, eax
0080CA6E  8B C1                           mov eax, ecx
0080CA70  44 8B F8                        mov r15d, eax
0080CA73  8B CB                           mov ecx, ebx
0080CA75  83 E1 04                        and ecx, 4
0080CA78  41 0F BA EF 0F                  bts r15d, 0xf
0080CA7D  85 C9                           test ecx, ecx
0080CA7F  89 4D 80                        mov dword ptr [rbp - 0x80], ecx
0080CA82  41 B8 00 02 00 00               mov r8d, 0x200
0080CA88  44 0F 44 F8                     cmove r15d, eax
0080CA8C  48 83 64 24 60 00               and qword ptr [rsp + 0x60], 0
0080CA92  8B C3                           mov eax, ebx
0080CA94  44 89 7C 24 5C                  mov dword ptr [rsp + 0x5c], r15d
0080CA99  41 23 C0                        and eax, r8d
0080CA9C  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
0080CAA0  75 2D                           jne 0x14080cacf
0080CAA2  41 B9 08 00 00 00               mov r9d, 8
0080CAA8  45 33 C0                        xor r8d, r8d
0080CAAB  49 8B D2                        mov rdx, r10
0080CAAE  49 8B CD                        mov rcx, r13
0080CAB1  E8 AA A1 A7 FF                  call 0x140286c60
0080CAB6  85 C0                           test eax, eax
0080CAB8  79 0A                           jns 0x14080cac4
0080CABA  B8 9A 00 00 C0                  mov eax, 0xc000009a
0080CABF  E9 89 05 00 00                  jmp 0x14080d04d
0080CAC4  4C 8B 54 24 68                  mov r10, qword ptr [rsp + 0x68]
0080CAC9  41 B8 00 02 00 00               mov r8d, 0x200
0080CACF  8B C3                           mov eax, ebx
0080CAD1  41 BE 01 00 00 00               mov r14d, 1
0080CAD7  41 23 C6                        and eax, r14d
0080CADA  8B FE                           mov edi, esi
0080CADC  89 45 A4                        mov dword ptr [rbp - 0x5c], eax
0080CADF  74 21                           je 0x14080cb02
0080CAE1  0F B7 15 18 85 7B 00            movzx edx, word ptr [rip + 0x7b8518]
0080CAE8  48 8B 05 E1 10 62 00            mov rax, qword ptr [rip + 0x6210e1]
0080CAEF  8B CA                           mov ecx, edx
0080CAF1  0F AF CE                        imul ecx, esi
0080CAF4  4C 8D 24 88                     lea r12, [rax + rcx*4]
0080CAF8  49 8D 0C 94                     lea rcx, [r12 + rdx*4]
0080CAFC  48 89 4D B0                     mov qword ptr [rbp - 0x50], rcx
0080CB00  EB 0B                           jmp 0x14080cb0d
0080CB02  45 33 E4                        xor r12d, r12d
0080CB05  48 C7 45 B0 04 00 00 00         mov qword ptr [rbp - 0x50], 4
0080CB0D  B8 00 00 04 00                  mov eax, 0x40000
0080CB12  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
0080CB16  4C 3B D0                        cmp r10, rax
0080CB19  72 14                           jb 0x14080cb2f
0080CB1B  8B C3                           mov eax, ebx
0080CB1D  25 80 01 00 00                  and eax, 0x180
0080CB22  F7 D8                           neg eax
0080CB24  48 1B C9                        sbb rcx, rcx
0080CB27  81 E1 00 FE 03 00               and ecx, 0x3fe00
0080CB2D  EB 0D                           jmp 0x14080cb3c
0080CB2F  4D 3B D0                        cmp r10, r8
0080CB32  48 1B C9                        sbb rcx, rcx
0080CB35  48 81 E1 10 FE FF FF            and rcx, 0xfffffffffffffe10
0080CB3C  49 03 C8                        add rcx, r8
0080CB3F  33 D2                           xor edx, edx
0080CB41  49 8B C2                        mov rax, r10
0080CB44  41 B9 00 00 00 00               mov r9d, 0
0080CB4A  48 F7 F1                        div rcx
0080CB4D  8B D3                           mov edx, ebx
0080CB4F  49 3B C6                        cmp rax, r14
0080CB52  49 0F 46 C6                     cmovbe rax, r14
0080CB56  81 E2 A2 00 00 00               and edx, 0xa2
0080CB5C  89 55 A0                        mov dword ptr [rbp - 0x60], edx
0080CB5F  4C 8B C0                        mov r8, rax
0080CB62  48 8B D1                        mov rdx, rcx
0080CB65  41 0F 95 C1                     setne r9b
0080CB69  48 8D 4D F0                     lea rcx, [rbp - 0x10]
0080CB6D  E8 DE 67 BC FF                  call 0x1403d3350
0080CB72  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0080CB77  48 8B C1                        mov rax, rcx
0080CB7A  48 2B 44 24 60                  sub rax, qword ptr [rsp + 0x60]
0080CB7F  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
0080CB83  48 3D 00 02 00 00               cmp rax, 0x200
0080CB89  0F 82 78 02 00 00               jb 0x14080ce07
0080CB8F  41 8B CE                        mov ecx, r14d
0080CB92  89 4C 24 50                     mov dword ptr [rsp + 0x50], ecx
0080CB96  F6 C3 60                        test bl, 0x60
0080CB99  75 0E                           jne 0x14080cba9
0080CB9B  48 3D 00 00 04 00               cmp rax, 0x40000
0080CBA1  1B C0                           sbb eax, eax
0080CBA3  23 C8                           and ecx, eax
0080CBA5  89 4C 24 50                     mov dword ptr [rsp + 0x50], ecx
0080CBA9  83 7C 24 54 00                  cmp dword ptr [rsp + 0x54], 0
0080CBAE  0F 84 BD 00 00 00               je 0x14080cc71
0080CBB4  8B C3                           mov eax, ebx
0080CBB6  25 00 08 00 00                  and eax, 0x800
0080CBBB  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
0080CBBF  85 C0                           test eax, eax
0080CBC1  74 0C                           je 0x14080cbcf
0080CBC3  8B D7                           mov edx, edi
0080CBC5  49 8B CD                        mov rcx, r13
0080CBC8  E8 4B 8C E6 FF                  call 0x140675818
0080CBCD  EB 57                           jmp 0x14080cc26
0080CBCF  48 83 65 E8 00                  and qword ptr [rbp - 0x18], 0
0080CBD4  44 8D 47 01                     lea r8d, [rdi + 1]
0080CBD8  8B C7                           mov eax, edi
0080CBDA  4C 8D 4D E0                     lea r9, [rbp - 0x20]
0080CBDE  48 69 D8 80 DF 00 00            imul rbx, rax, 0xdf80
0080CBE5  33 D2                           xor edx, edx
0080CBE7  33 C9                           xor ecx, ecx
0080CBE9  49 03 5D 10                     add rbx, qword ptr [r13 + 0x10]
0080CBED  E8 1E 38 B1 FF                  call 0x140320410
0080CBF2  4C 8D 8B 70 3B 00 00            lea r9, [rbx + 0x3b70]
0080CBF9  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0080CBFD  4C 89 4D E0                     mov qword ptr [rbp - 0x20], r9
0080CC01  E8 5E 61 C3 FF                  call 0x140442d64
0080CC06  41 8B CF                        mov ecx, r15d
0080CC09  8B D0                           mov edx, eax
0080CC0B  41 22 CE                        and cl, r14b
0080CC0E  F6 D9                           neg cl
0080CC10  49 8B CD                        mov rcx, r13
0080CC13  45 1B C0                        sbb r8d, r8d
0080CC16  41 83 E0 D0                     and r8d, 0xffffffd0
0080CC1A  41 81 C0 30 10 00 00            add r8d, 0x1030
0080CC21  E8 2E 8D E6 FF                  call 0x140675954
0080CC26  4C 8B F8                        mov r15, rax
0080CC29  41 81 E7 FF FF 3F 00            and r15d, 0x3fffff
0080CC30  75 20                           jne 0x14080cc52
0080CC32  49 83 C4 04                     add r12, 4
0080CC36  4C 3B 65 B0                     cmp r12, qword ptr [rbp - 0x50]
0080CC3A  0F 84 C3 01 00 00               je 0x14080ce03
0080CC40  41 8B 3C 24                     mov edi, dword ptr [r12]
0080CC44  44 8B 7C 24 5C                  mov r15d, dword ptr [rsp + 0x5c]
0080CC49  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
0080CC4D  E9 6D FF FF FF                  jmp 0x14080cbbf
0080CC52  48 8B D0                        mov rdx, rax
0080CC55  49 C1 E7 12                     shl r15, 0x12
0080CC59  45 33 C0                        xor r8d, r8d
0080CC5C  E8 8B 97 E6 FF                  call 0x1406763ec
0080CC61  33 C9                           xor ecx, ecx
0080CC63  85 C0                           test eax, eax
0080CC65  0F 95 C1                        setne cl
0080CC68  89 4C 24 58                     mov dword ptr [rsp + 0x58], ecx
0080CC6C  E9 05 01 00 00                  jmp 0x14080cd76
0080CC71  B8 00 00 00 00                  mov eax, 0
0080CC76  48 8D 55 F0                     lea rdx, [rbp - 0x10]
0080CC7A  F7 C3 80 05 00 00               test ebx, 0x580
0080CC80  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
0080CC85  44 8B C1                        mov r8d, ecx
0080CC88  0F 94 C0                        sete al
0080CC8B  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
0080CC8F  44 8B C8                        mov r9d, eax
0080CC92  EB 25                           jmp 0x14080ccb9
0080CC94  49 83 C4 04                     add r12, 4
0080CC98  4C 3B 65 B0                     cmp r12, qword ptr [rbp - 0x50]
0080CC9C  0F 84 61 01 00 00               je 0x14080ce03
0080CCA2  41 8B 3C 24                     mov edi, dword ptr [r12]
0080CCA6  48 8D 45 F0                     lea rax, [rbp - 0x10]
0080CCAA  44 8B 4C 24 58                  mov r9d, dword ptr [rsp + 0x58]
0080CCAF  44 8B 44 24 50                  mov r8d, dword ptr [rsp + 0x50]
0080CCB4  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0080CCB9  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
0080CCBE  8B D7                           mov edx, edi
0080CCC0  49 8B CD                        mov rcx, r13
0080CCC3  44 89 7C 24 20                  mov dword ptr [rsp + 0x20], r15d
0080CCC8  E8 1B EB CC FF                  call 0x1404db7e8
0080CCCD  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
0080CCD2  48 8B D8                        mov rbx, rax
0080CCD5  48 85 C0                        test rax, rax
0080CCD8  74 BA                           je 0x14080cc94
0080CCDA  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0080CCE4  4C 8B FB                        mov r15, rbx
0080CCE7  48 8B CB                        mov rcx, rbx
0080CCEA  4C 2B F8                        sub r15, rax
0080CCED  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
0080CCF7  49 C1 FF 04                     sar r15, 4
0080CCFB  4C 0F AF F8                     imul r15, rax
0080CCFF  E8 0C FA B0 FF                  call 0x14031c710
0080CD04  48 8B 5B 10                     mov rbx, qword ptr [rbx + 0x10]
0080CD08  45 8B C6                        mov r8d, r14d
0080CD0B  8B 54 24 5C                     mov edx, dword ptr [rsp + 0x5c]
0080CD0F  81 E3 E0 03 00 00               and ebx, 0x3e0
0080CD15  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
0080CD1A  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
0080CD1E  E8 C5 CA CE FF                  call 0x1404f97e8
0080CD23  33 C9                           xor ecx, ecx
0080CD25  48 85 DB                        test rbx, rbx
0080CD28  0F 94 C1                        sete cl
0080CD2B  89 4C 24 58                     mov dword ptr [rsp + 0x58], ecx
0080CD2F  48 85 DB                        test rbx, rbx
0080CD32  74 3D                           je 0x14080cd71
0080CD34  33 C9                           xor ecx, ecx
0080CD36  89 4C 24 58                     mov dword ptr [rsp + 0x58], ecx
0080CD3A  44 84 74 24 5C                  test byte ptr [rsp + 0x5c], r14b
0080CD3F  75 30                           jne 0x14080cd71
0080CD41  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
0080CD45  85 C0                           test eax, eax
0080CD47  75 0D                           jne 0x14080cd56
0080CD49  49 8B D7                        mov rdx, r15
0080CD4C  49 8B CD                        mov rcx, r13
0080CD4F  E8 3C F7 E7 FF                  call 0x14068c490
0080CD54  EB 14                           jmp 0x14080cd6a
0080CD56  21 4C 24 20                     and dword ptr [rsp + 0x20], ecx
0080CD5A  45 8B CE                        mov r9d, r14d
0080CD5D  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
0080CD62  44 8B C0                        mov r8d, eax
0080CD65  E8 AA 9B AB FF                  call 0x1402c6914
0080CD6A  41 8B CE                        mov ecx, r14d
0080CD6D  89 4C 24 58                     mov dword ptr [rsp + 0x58], ecx
0080CD71  44 8B 44 24 50                  mov r8d, dword ptr [rsp + 0x50]
0080CD76  41 8B C0                        mov eax, r8d
0080CD79  48 8D 1D E0 4E 80 FF            lea rbx, [rip - 0x7fb120]
0080CD80  44 8B C9                        mov r9d, ecx
0080CD83  49 8B D7                        mov rdx, r15
0080CD86  48 8D 4D 90                     lea rcx, [rbp - 0x70]
0080CD8A  48 8B 1C C3                     mov rbx, qword ptr [rbx + rax*8]
0080CD8E  4C 8B C3                        mov r8, rbx
0080CD91  E8 76 34 E8 FF                  call 0x14069020c
0080CD96  85 C0                           test eax, eax
0080CD98  74 2B                           je 0x14080cdc5
0080CD9A  4C 8B 7C 24 60                  mov r15, qword ptr [rsp + 0x60]
0080CD9F  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0080CDA4  4C 03 FB                        add r15, rbx
0080CDA7  4C 89 7C 24 60                  mov qword ptr [rsp + 0x60], r15
0080CDAC  4C 3B F9                        cmp r15, rcx
0080CDAF  0F 84 A5 00 00 00               je 0x14080ce5a
0080CDB5  8B 9D B0 00 00 00               mov ebx, dword ptr [rbp + 0xb0]
0080CDBB  44 8B 7C 24 5C                  mov r15d, dword ptr [rsp + 0x5c]
0080CDC0  E9 B2 FD FF FF                  jmp 0x14080cb77
0080CDC5  8B 7C 24 54                     mov edi, dword ptr [rsp + 0x54]
0080CDC9  49 8B CF                        mov rcx, r15
0080CDCC  85 FF                           test edi, edi
0080CDCE  74 0F                           je 0x14080cddf
0080CDD0  8B 54 24 58                     mov edx, dword ptr [rsp + 0x58]
0080CDD4  E8 4F 41 E8 FF                  call 0x140690f28
0080CDD9  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
0080CDDD  EB 2C                           jmp 0x14080ce0b
0080CDDF  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
0080CDE5  45 8B CE                        mov r9d, r14d
0080CDE8  44 8B 44 24 58                  mov r8d, dword ptr [rsp + 0x58]
0080CDED  48 8B D3                        mov rdx, rbx
0080CDF0  E8 57 8C B6 FF                  call 0x140375a4c
0080CDF5  48 8B D0                        mov rdx, rax
0080CDF8  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0080CDFD  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
0080CE01  EB 0D                           jmp 0x14080ce10
0080CE03  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
0080CE07  8B 7C 24 54                     mov edi, dword ptr [rsp + 0x54]
0080CE0B  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
0080CE10  4C 8B 7C 24 60                  mov r15, qword ptr [rsp + 0x60]
0080CE15  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0080CE1A  4C 3B F9                        cmp r15, rcx
0080CE1D  74 3B                           je 0x14080ce5a
0080CE1F  85 FF                           test edi, edi
0080CE21  74 0A                           je 0x14080ce2d
0080CE23  BB 17 00 00 C0                  mov ebx, 0xc0000017
0080CE28  E9 9C 01 00 00                  jmp 0x14080cfc9
0080CE2D  48 2B C2                        sub rax, rdx
0080CE30  74 15                           je 0x14080ce47
0080CE32  48 8B D0                        mov rdx, rax
0080CE35  49 8B CD                        mov rcx, r13
0080CE38  E8 1B B4 BE FF                  call 0x1403f8258
0080CE3D  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0080CE42  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
0080CE47  83 7D A0 00                     cmp dword ptr [rbp - 0x60], 0
0080CE4B  0F 85 53 01 00 00               jne 0x14080cfa4
0080CE51  48 85 D2                        test rdx, rdx
0080CE54  0F 85 4A 01 00 00               jne 0x14080cfa4
0080CE5A  8B 44 24 5C                     mov eax, dword ptr [rsp + 0x5c]
0080CE5E  8B 7D A4                        mov edi, dword ptr [rbp - 0x5c]
0080CE61  41 23 C6                        and eax, r14d
0080CE64  44 8B A5 B0 00 00 00            mov r12d, dword ptr [rbp + 0xb0]
0080CE6B  41 33 FE                        xor edi, r14d
0080CE6E  8D 3C 7D 00 00 40 00            lea edi, [rdi*2 + 0x400000]
0080CE75  0B F8                           or edi, eax
0080CE77  48 B8 00 00 00 00 01 00 00 00   movabs rax, 0x100000000
0080CE81  83 CF 10                        or edi, 0x10
0080CE84  F7 5D 80                        neg dword ptr [rbp - 0x80]
0080CE87  4D 1B D2                        sbb r10, r10
0080CE8A  33 DB                           xor ebx, ebx
0080CE8C  4C 23 D0                        and r10, rax
0080CE8F  4C 89 54 24 78                  mov qword ptr [rsp + 0x78], r10
0080CE94  41 F6 C4 10                     test r12b, 0x10
0080CE98  74 0F                           je 0x14080cea9
0080CE9A  83 CF 40                        or edi, 0x40
0080CE9D  BB 00 00 20 00                  mov ebx, 0x200000
0080CEA2  B8 00 00 04 00                  mov eax, 0x40000
0080CEA7  EB 34                           jmp 0x14080cedd
0080CEA9  41 F6 C4 40                     test r12b, 0x40
0080CEAD  74 0F                           je 0x14080cebe
0080CEAF  83 CF 40                        or edi, 0x40
0080CEB2  B8 00 02 00 00                  mov eax, 0x200
0080CEB7  BB 00 00 20 00                  mov ebx, 0x200000
0080CEBC  EB 1B                           jmp 0x14080ced9
0080CEBE  41 0F BA E4 08                  bt r12d, 8
0080CEC3  73 0F                           jae 0x14080ced4
0080CEC5  83 CF 40                        or edi, 0x40
0080CEC8  B8 00 00 04 00                  mov eax, 0x40000
0080CECD  BB 00 00 00 40                  mov ebx, 0x40000000
0080CED2  EB 05                           jmp 0x14080ced9
0080CED4  B8 FF FF 0F 00                  mov eax, 0xfffff
0080CED9  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
0080CEDD  4C 3B F9                        cmp r15, rcx
0080CEE0  0F 84 C5 00 00 00               je 0x14080cfab
0080CEE6  48 8B D1                        mov rdx, rcx
0080CEE9  4C 8B CB                        mov r9, rbx
0080CEEC  49 2B D7                        sub rdx, r15
0080CEEF  48 3B D0                        cmp rdx, rax
0080CEF2  48 0F 47 D0                     cmova rdx, rax
0080CEF6  48 83 64 24 48 00               and qword ptr [rsp + 0x48], 0
0080CEFC  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0080CF05  49 83 C8 FF                     or r8, 0xffffffffffffffff
0080CF09  48 C1 E2 0C                     shl rdx, 0xc
0080CF0D  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0080CF14  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
0080CF19  49 8B CD                        mov rcx, r13
0080CF1C  89 7C 24 38                     mov dword ptr [rsp + 0x38], edi
0080CF20  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
0080CF24  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
0080CF29  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
0080CF2E  49 8B D2                        mov rdx, r10
0080CF31  E8 B6 DC BD FF                  call 0x1403eabec
0080CF36  4C 8B F8                        mov r15, rax
0080CF39  48 85 C0                        test rax, rax
0080CF3C  75 24                           jne 0x14080cf62
0080CF3E  40 F6 C7 40                     test dil, 0x40
0080CF42  74 60                           je 0x14080cfa4
0080CF44  83 E7 BF                        and edi, 0xffffffbf
0080CF47  83 CF 20                        or edi, 0x20
0080CF4A  4C 8B 7C 24 60                  mov r15, qword ptr [rsp + 0x60]
0080CF4F  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0080CF54  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
0080CF58  4C 8B 54 24 78                  mov r10, qword ptr [rsp + 0x78]
0080CF5D  E9 7B FF FF FF                  jmp 0x14080cedd
0080CF62  44 8B C7                        mov r8d, edi
0080CF65  48 8D 4D 90                     lea rcx, [rbp - 0x70]
0080CF69  49 8B D7                        mov rdx, r15
0080CF6C  E8 AF 31 E8 FF                  call 0x140690120
0080CF71  33 D2                           xor edx, edx
0080CF73  49 8B CF                        mov rcx, r15
0080CF76  85 C0                           test eax, eax
0080CF78  74 14                           je 0x14080cf8e
0080CF7A  41 8B 47 28                     mov eax, dword ptr [r15 + 0x28]
0080CF7E  48 C1 E8 0C                     shr rax, 0xc
0080CF82  48 01 44 24 60                  add qword ptr [rsp + 0x60], rax
0080CF87  E8 E4 58 37 00                  call 0x140b82870
0080CF8C  EB BC                           jmp 0x14080cf4a
0080CF8E  45 33 C9                        xor r9d, r9d
0080CF91  45 8D 41 0B                     lea r8d, [r9 + 0xb]
0080CF95  E8 66 B3 BE FF                  call 0x1403f8300
0080CF9A  33 D2                           xor edx, edx
0080CF9C  49 8B CF                        mov rcx, r15
0080CF9F  E8 CC 58 37 00                  call 0x140b82870
0080CFA4  BB 9A 00 00 C0                  mov ebx, 0xc000009a
0080CFA9  EB 1E                           jmp 0x14080cfc9
0080CFAB  8B 44 24 54                     mov eax, dword ptr [rsp + 0x54]
0080CFAF  48 8B 7D B8                     mov rdi, qword ptr [rbp - 0x48]
0080CFB3  85 C0                           test eax, eax
0080CFB5  75 2F                           jne 0x14080cfe6
0080CFB7  48 8D 55 90                     lea rdx, [rbp - 0x70]
0080CFBB  48 8B CF                        mov rcx, rdi
0080CFBE  E8 8D 0B 00 00                  call 0x14080db50
0080CFC3  8B D8                           mov ebx, eax
0080CFC5  85 C0                           test eax, eax
0080CFC7  79 19                           jns 0x14080cfe2
0080CFC9  45 8B CE                        mov r9d, r14d
0080CFCC  48 8D 55 90                     lea rdx, [rbp - 0x70]
0080CFD0  41 B8 01 08 00 00               mov r8d, 0x801
0080CFD6  49 8B CD                        mov rcx, r13
0080CFD9  E8 72 3E E8 FF                  call 0x140690e50
0080CFDE  8B C3                           mov eax, ebx
0080CFE0  EB 6B                           jmp 0x14080d04d
0080CFE2  8B 44 24 54                     mov eax, dword ptr [rsp + 0x54]
0080CFE6  83 7D A8 00                     cmp dword ptr [rbp - 0x58], 0
0080CFEA  48 8D 4D 90                     lea rcx, [rbp - 0x70]
0080CFEE  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
0080CFF2  0F 57 C0                        xorps xmm0, xmm0
0080CFF5  B9 21 00 00 00                  mov ecx, 0x21
0080CFFA  44 0F 45 F1                     cmovne r14d, ecx
0080CFFE  44 89 75 D8                     mov dword ptr [rbp - 0x28], r14d
0080D002  F3 0F 7F 45 C8                  movdqu xmmword ptr [rbp - 0x38], xmm0
0080D007  4C 3B EF                        cmp r13, rdi
0080D00A  74 08                           je 0x14080d014
0080D00C  41 83 CE 02                     or r14d, 2
0080D010  44 89 75 D8                     mov dword ptr [rbp - 0x28], r14d
0080D014  41 F6 C4 08                     test r12b, 8
0080D018  74 08                           je 0x14080d022
0080D01A  41 83 CE 04                     or r14d, 4
0080D01E  44 89 75 D8                     mov dword ptr [rbp - 0x28], r14d
0080D022  85 C0                           test eax, eax
0080D024  74 08                           je 0x14080d02e
0080D026  41 83 CE 10                     or r14d, 0x10
0080D02A  44 89 75 D8                     mov dword ptr [rbp - 0x28], r14d
0080D02E  41 8B 45 04                     mov eax, dword ptr [r13 + 4]
0080D032  84 C0                           test al, al
0080D034  79 05                           jns 0x14080d03b
0080D036  0F BA 6D D8 09                  bts dword ptr [rbp - 0x28], 9
0080D03B  4D 8B CF                        mov r9, r15
0080D03E  4C 8D 45 C0                     lea r8, [rbp - 0x40]
0080D042  48 8B D7                        mov rdx, rdi
0080D045  49 8B CD                        mov rcx, r13
0080D048  E8 53 41 E8 FF                  call 0x1406911a0
0080D04D  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
0080D051  48 33 CC                        xor rcx, rsp
0080D054  E8 E7 F5 E9 FF                  call 0x1406ac640
0080D059  48 81 C4 48 01 00 00            add rsp, 0x148
0080D060  41 5F                           pop r15
0080D062  41 5E                           pop r14
0080D064  41 5D                           pop r13
0080D066  41 5C                           pop r12
0080D068  5F                              pop rdi
0080D069  5E                              pop rsi
0080D06A  5B                              pop rbx
0080D06B  5D                              pop rbp
0080D06C  C3                              ret
0080D06D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiAllocatePartitionPhysicalPages(__int64 a1, __int64 a2, __int64 a3, int a4, unsigned int a5)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned int v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned int v_stack_m12C;
    unsigned int v_stack_m130;
    unsigned int v_stack_m134;
    unsigned int v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned int v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned int v_stack_m160;
    unsigned int v_stack_m168;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned int v_stack_mE0;
    unsigned int v_stack_mE4;
    unsigned int v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;

    v_rsp = (v_rsp) - (328);
    result = (*(unsigned __int64 *)(v_rip + 6282572)) ^ (v_rsp);
    v_stack_m58 = result;
    v_stack_mD0 = a2;
    v_stack_m120 = a3;
    a2 = 0;
    v_stack_m68 = 0;
    v_stack_m60 = 0;
    v_r13 = v_rip + 6472440;
    if (a1 != 0) { v_r13 = a1; }
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a5)))) & (0x400ULL));
    v_stack_mE0 = (unsigned int)(a2);
    v_stack_mC8 = v_xmm0;
    v_stack_mB8 = v_xmm0;
    v_stack_m98 = v_xmm0;
    v_stack_m88 = v_xmm0;
    v_stack_m78 = v_xmm0;
    if (condition_is_equal) goto loc_0080CA61;
    goto loc_0080CA70;
loc_0080CA61:
    a1 = (unsigned int)(0x100000ULL);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)((unsigned int)(0x100000ULL) + 1 + 4)))) & (32)) == 0) { a1 = (unsigned int)((unsigned int)(0x100001ULL)); }
loc_0080CA70:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a5)))) & (4));
    v_stack_m108 = (unsigned int)(a1);
    v_r15 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1))));
    if ((unsigned int)(a1) == 0) { v_r15 = (unsigned int)((unsigned int)((unsigned int)(a1))); }
    v_stack_m12C = (unsigned int)(v_r15);
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a5)))) & (512));
    v_stack_m134 = (unsigned int)(result);
    if (condition_is_not_equal) goto loc_0080CACF;
    a3 = 0;
    result = MiAcquireNonPagedResources(v_r13, 0, a3, 8);
    if (!sign_flag) goto loc_0080CAC4;
    goto loc_0080D04D;
loc_0080CAC4:
loc_0080CACF:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a5)))) & (1));
    v_stack_mE4 = (unsigned int)(result);
    if (condition_is_equal) goto loc_0080CB02;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rip + 8095000)))) * ((unsigned int)((unsigned int)(a4))));
    v_stack_mD8 = *(unsigned __int64 *)(v_rip + 6426849) + a1 * 4 + *(unsigned __int16 *)(v_rip + 8095000) * 4;
    goto loc_0080CB0D;
loc_0080CB02:
    v_r12 = 0;
    v_stack_mD8 = 4;
loc_0080CB0D:
    v_stack_m100 = (unsigned int)(0x40000ULL);
    if (v_stack_m120 < ((unsigned int)(0x40000ULL))) goto loc_0080CB2F;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a5)))) & (384));
    result = (unsigned int)(-(result));
    a1 = (unsigned int)((*(unsigned __int64 *)(v_rip + 6426849) + a1 * 4 + *(unsigned __int16 *)(v_rip + 8095000) * 4) & (0x3FE00ULL));
    goto loc_0080CB3C;
loc_0080CB2F:
    a1 = (a1) & (-496);
loc_0080CB3C:
    a1 = (a1) + (512);
    a2 = 0;
    result = v_stack_m120;
    if (v_stack_m120 <= 1) { result = 1; }
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a5)))) & (162));
    v_stack_mE8 = (unsigned int)(a2);
    a4 = (condition_is_not_equal) ? 1 : 0;
    result = MiInitializeDemandCoalesceContext(v_stack_m98, a1, result, a4);
loc_0080CB77:
    result = (v_stack_m120) - (v_stack_m128);
    v_stack_mF0 = result;
    if (result < 512) goto loc_0080CE07;
    v_stack_m138 = 1;
    if ((((unsigned __int8)((unsigned int)(a5))) & (96)) == 0) {
        a1 = (unsigned int)((1) & ((unsigned int)(result)));
        v_stack_m138 = (unsigned int)(a1);
    }
    if (v_stack_m134 == 0) goto loc_0080CC71;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a5)))) & (0x800ULL));
    v_stack_m138 = (unsigned int)(result);
loc_0080CBBF:
    if ((unsigned int)(result) == 0) goto loc_0080CBCF;
    result = MiGetHugeBadRangeFromNode(v_r13, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a4))))), result, a4);
    goto loc_0080CC26;
loc_0080CBCF:
    v_rbx = ((unsigned int)(a5)) * ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a4))))));
    a2 = 0;
    a1 = 0;
    v_rbx = (v_rbx) + (*(unsigned __int64 *)(v_r13 + 16));
    result = MiInitializePageColorBase(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a4))) + 1, v_stack_mA8);
    v_stack_mA8 = v_rbx + 15216;
    result = MiGetNextPageColor(v_stack_mA8, a2, (unsigned int)((unsigned int)((unsigned int)(a4))) + 1, v_rbx + 15216);
    a1 = (unsigned __int8)(((unsigned int)((unsigned int)(v_r15))) & (1));
    a1 = (unsigned __int8)(-(a1));
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a4))) + 1) & (0xFFFFFFD0ULL));
    a3 = (unsigned int)((a3) + (0x1030ULL));
    result = MiGetHugeRange(v_r13, (unsigned int)((unsigned int)(result)), a3, v_rbx + 15216);
loc_0080CC26:
    v_r15 = (unsigned int)((result) & (0x3FFFFFULL));
    if (condition_is_not_equal) goto loc_0080CC52;
    v_r12 = (v_r12) + (4);
    if (v_r12 == v_stack_mD8) goto loc_0080CE03;
    goto loc_0080CBBF;
loc_0080CC52:
    v_r15 = ((unsigned int)(v_stack_m12C)) << (18);
    a3 = 0;
    result = MiHugeRangeIsZeroed(v_r13, (unsigned int)(v_stack_m138), a3, v_rbx + 15216);
    a1 = 0;
    a1 = ((unsigned int)(result) != 0) ? 1 : 0;
    v_stack_m130 = (unsigned int)(a1);
    goto loc_0080CD76;
loc_0080CC71:
    v_stack_m158 = v_stack_m98;
    result = ((((unsigned int)(v_rbx)) & (0x580ULL)) == 0) ? 1 : 0;
    v_stack_m130 = (unsigned int)(result);
    goto loc_0080CCB9;
loc_0080CC94:
    v_r12 = (v_r12) + (4);
    if (v_r12 == v_stack_mD8) goto loc_0080CE03;
    v_stack_m158 = v_stack_m98;
loc_0080CCB9:
    v_stack_m160 = 1;
    v_stack_m168 = (unsigned int)(v_r15);
    result = MiFindLargeNodePage(v_r13, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r12)))), (unsigned int)(v_stack_m138), (unsigned int)(v_stack_m130));
    v_stack_m110 = result;
    if (result == 0) goto loc_0080CC94;
    v_r15 = (result) - (result);
    v_r15 = (v_r15) >> (4);
    v_r15 = (v_r15) * (result);
    result = MiGetPfnPageSizeIndex(result, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r12)))), (unsigned int)(v_stack_m138), (unsigned int)(v_stack_m130));
    v_rbx = (unsigned int)((*(unsigned __int64 *)(result + 16)) & (992));
    v_stack_m138 = (unsigned int)(result);
    result = MiInitializeFoundLargeNodePage(v_stack_m110, (unsigned int)(v_stack_m12C), 1, (unsigned int)(v_stack_m130));
    a1 = 0;
    a1 = (v_rbx == 0) ? 1 : 0;
    v_stack_m130 = (unsigned int)(a1);
    if (v_rbx == 0) goto loc_0080CD71;
    a1 = 0;
    v_stack_m130 = 0;
    if (((v_stack_m12C) & (1)) != 0) goto loc_0080CD71;
    if ((unsigned int)((unsigned int)(v_stack_m138)) != 0) goto loc_0080CD56;
    result = MiHugePageOperation(v_r13, v_r15, 1, (unsigned int)(v_stack_m130));
    goto loc_0080CD6A;
loc_0080CD56:
    result = MiZeroLargePage(v_r13, v_stack_m110, (unsigned int)((unsigned int)(result)), 1);
loc_0080CD6A:
    v_stack_m130 = 1;
loc_0080CD71:
loc_0080CD76:
    result = MiAddRangeToPartitionTree(v_stack_mF8, v_r15, *(unsigned __int64 *)(v_rip - 8368416 + (unsigned int)((unsigned int)((unsigned int)(v_stack_m138))) * 8), 1);
    if ((unsigned int)(result) == 0) goto loc_0080CDC5;
    v_r15 = (v_stack_m128) + (*(unsigned __int64 *)(v_rip - 8368416 + (unsigned int)((unsigned int)((unsigned int)(v_stack_m138))) * 8));
    v_stack_m128 = v_r15;
    if (v_r15 == v_stack_m120) goto loc_0080CE5A;
    goto loc_0080CB77;
loc_0080CDC5:
    if ((unsigned int)((unsigned int)(v_stack_m134)) == 0) goto loc_0080CDDF;
    result = MiInsertHugeRangeInPartition((unsigned int)(v_stack_m12C), (unsigned int)(v_stack_m130), *(unsigned __int64 *)(v_rip - 8368416 + (unsigned int)((unsigned int)((unsigned int)(v_stack_m138))) * 8), 1);
    goto loc_0080CE0B;
loc_0080CDDF:
    result = MiFreeMdlPageRun((unsigned int)(v_stack_m12C), (unsigned int)(a5), (unsigned int)(v_stack_m130), 1);
    v_stack_m118 = result;
    goto loc_0080CE10;
loc_0080CE03:
loc_0080CE07:
loc_0080CE0B:
loc_0080CE10:
    if (v_stack_m128 == v_stack_m120) goto loc_0080CE5A;
    if ((unsigned int)((unsigned int)(v_stack_m134)) == 0) goto loc_0080CE2D;
    goto loc_0080CFC9;
loc_0080CE2D:
    result = (v_stack_mF0) - (v_stack_m118);
    if (!(condition_is_equal)) {
        a2 = result;
        a1 = v_r13;
        result = MiReleaseNonPagedResourcesNotExposed(a1, a2, (unsigned int)(v_stack_m130), 1);
        a1 = v_stack_m120;
        a2 = v_stack_m118;
    }
    if (v_stack_mE8 != 0) goto loc_0080CFA4;
    if (a2 != 0) goto loc_0080CFA4;
loc_0080CE5A:
    result = (unsigned int)(((unsigned int)(v_stack_m12C)) & (1));
    v_rdi = (unsigned int)(((unsigned int)(v_stack_mE4)) ^ (1));
    v_rdi = (unsigned int)((v_rdi * 2 + 4194304) | ((unsigned int)(result)));
    v_rdi = (unsigned int)((v_rdi) | (16));
    v_rbx = 0;
    v_r10 = (v_stack_m120) & (result);
    v_stack_m110 = v_r10;
    if ((((unsigned __int8)((unsigned int)(a5))) & (16)) == 0) goto loc_0080CEA9;
    v_rdi = (unsigned int)((v_rdi) | (64));
    goto loc_0080CEDD;
loc_0080CEA9:
    if ((((unsigned __int8)((unsigned int)(a5))) & (64)) == 0) goto loc_0080CEBE;
    v_rdi = (unsigned int)((v_rdi) | (64));
    goto loc_0080CED9;
loc_0080CEBE:
    if (condition_is_above_or_equal) goto loc_0080CED4;
    v_rdi = (unsigned int)((v_rdi) | (64));
    goto loc_0080CED9;
loc_0080CED4:
loc_0080CED9:
    v_stack_m100 = (unsigned int)(0xFFFFFULL);
loc_0080CEDD:
    if (v_stack_m128 == a1) goto loc_0080CFAB;
    a2 = (a1) - (v_stack_m128);
    if (a2 > ((unsigned int)(0xFFFFFULL))) { a2 = (unsigned int)(0xFFFFFULL); }
    a3 = ((unsigned int)(v_stack_m130)) | (-1);
    a2 = (a2) << (12);
    v_stack_m148 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    v_stack_m150 = (unsigned int)(v_rdi);
    v_stack_m158 = (unsigned int)((unsigned int)(a4));
    v_stack_m160 = 1;
    v_stack_m168 = a2;
    result = MiAllocatePagesForMdl(v_r13, v_r10, a3, (unsigned int)(0x40000000ULL));
    if (result != 0) goto loc_0080CF62;
    if ((((unsigned __int8)(v_rdi)) & (64)) == 0) goto loc_0080CFA4;
    v_rdi = (unsigned int)((v_rdi) & (0xFFFFFFBFULL));
    v_rdi = (unsigned int)((v_rdi) | (32));
loc_0080CF4A:
    goto loc_0080CEDD;
loc_0080CF62:
    result = MiAddMdlToPartitionTree(v_stack_mF8, v_stack_m128, (unsigned int)((unsigned int)(v_rdi)), (unsigned int)(0x40000000ULL));
    a2 = 0;
    if ((unsigned int)(result) == 0) goto loc_0080CF8E;
    result = ((unsigned int)(*(unsigned int *)(v_stack_m128 + 40))) >> (12);
    result = ExFreePoolWithTag(v_stack_m128, a2, (unsigned int)((unsigned int)(v_rdi)), (unsigned int)(0x40000000ULL));
    goto loc_0080CF4A;
loc_0080CF8E:
    a4 = 0;
    result = MiFreePagesFromMdl(v_stack_m128, a2, a4 + 11, a4);
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m128, a2, a4 + 11, a4);
loc_0080CFA4:
    goto loc_0080CFC9;
loc_0080CFAB:
    if ((unsigned int)((unsigned int)(v_stack_m134)) != 0) goto loc_0080CFE6;
    result = MiUpdatePartitionLargePfnBitMap(v_stack_mD0, v_stack_mF8, a4 + 11, a4);
    if (!sign_flag) goto loc_0080CFE2;
loc_0080CFC9:
    result = MiFreePartitionTree(v_r13, v_stack_mF8, (unsigned int)(0x801ULL), 1);
    goto loc_0080D04D;
loc_0080CFE2:
loc_0080CFE6:
    v_stack_mC8 = v_stack_mF8;
    v_r14 = 1;
    if (v_stack_mE0 != 0) { v_r14 = 33; }
    v_stack_mB0 = (unsigned int)(v_r14);
    v_stack_mC0 = v_xmm0;
    if (v_r13 != v_stack_mD0) {
        v_r14 = (unsigned int)((v_r14) | (2));
        v_stack_mB0 = (unsigned int)(v_r14);
    }
    if ((((unsigned __int8)((unsigned int)(a5))) & (8)) != 0) {
        v_r14 = (unsigned int)((v_r14) | (4));
        v_stack_mB0 = (unsigned int)(v_r14);
    }
    if ((unsigned int)((unsigned int)(v_stack_m134)) != 0) {
        v_r14 = (unsigned int)((v_r14) | (16));
        v_stack_mB0 = (unsigned int)(v_r14);
    }
    if (sign_flag) {
    }
    result = MiInsertPartitionPages(v_r13, v_stack_mD0, v_stack_mC8, v_stack_m128);
loc_0080D04D:
    a1 = (v_stack_m58) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_mD0, v_stack_mC8, v_stack_m128);
    v_rsp = (v_rsp) + (328);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiAllocatePartitionPhysicalPages(int64_t Arg1, void *Arg2, int64_t Arg3, int32_t Arg4, uint32_t Arg5)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint32_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint32_t v_stack_m12C;
    uint32_t v_stack_m130;
    uint32_t v_stack_m134;
    uint32_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint32_t v_stack_m150;
    uint64_t v_stack_m158;
    uint32_t v_stack_m160;
    uint32_t v_stack_m168;
    uint64_t v_stack_m58;
    uint32_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m88;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint32_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint32_t v_stack_mE0;
    uint32_t v_stack_mE4;
    uint32_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;

    local_rsp = (local_rsp) - (328);
    result = (*(uint64_t *)(v_rip + 0x5FDD4C)) ^ (local_rsp);
    v_stack_m58 = result;
    v_stack_mD0 = Arg2;
    v_stack_m120 = Arg3;
    Arg2 = 0;
    v_stack_m68 = 0;
    v_stack_m60 = 0;
    local_r13 = v_rip + 6472440;
    if (Arg1 != 0) { local_r13 = Arg1; }
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg5)))) & (0x400ULL));
    v_stack_mE0 = (uint32_t)(Arg2);
    v_stack_mC8 = v_xmm0;
    v_stack_mB8 = v_xmm0;
    v_stack_m98 = v_xmm0;
    v_stack_m88 = v_xmm0;
    v_stack_m78 = v_xmm0;
    if (condition_is_equal) goto loc_0080CA61;
    goto loc_0080CA70;
loc_0080CA61:
    Arg1 = (uint32_t)(0x100000ULL);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)((uint32_t)(0x100000ULL) + 0x1 + 0x4)))) & (32)) == 0) { Arg1 = (uint32_t)((uint32_t)(0x100001ULL)); }
loc_0080CA70:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg5)))) & (4));
    v_stack_m108 = (uint32_t)(Arg1);
    local_r15 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1))));
    if ((uint32_t)(Arg1) == 0) { local_r15 = (uint32_t)((uint32_t)((uint32_t)(Arg1))); }
    v_stack_m12C = (uint32_t)(local_r15);
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg5)))) & (512));
    v_stack_m134 = (uint32_t)(result);
    if (condition_is_not_equal) goto loc_0080CACF;
    Arg3 = 0;
    result = MiAcquireNonPagedResources(local_r13, 0, Arg3, 8);
    if (!sign_flag) goto loc_0080CAC4;
    goto loc_0080D04D;
loc_0080CAC4:
loc_0080CACF:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg5)))) & (1));
    v_stack_mE4 = (uint32_t)(result);
    if (condition_is_equal) goto loc_0080CB02;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(v_rip + 0x7B8518)))) * ((uint32_t)((uint32_t)(Arg4))));
    v_stack_mD8 = *(uint64_t *)(v_rip + 0x6210E1) + Arg1 * 4 + *(uint16_t *)(v_rip + 0x7B8518) * 4;
    goto loc_0080CB0D;
loc_0080CB02:
    local_r12 = 0;
    v_stack_mD8 = 4;
loc_0080CB0D:
    v_stack_m100 = (uint32_t)(0x40000ULL);
    if (v_stack_m120 < ((uint32_t)(0x40000ULL))) goto loc_0080CB2F;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg5)))) & (384));
    result = (uint32_t)(-(result));
    Arg1 = (uint32_t)((*(uint64_t *)(v_rip + 0x6210E1) + Arg1 * 4 + *(uint16_t *)(v_rip + 0x7B8518) * 4) & (0x3FE00ULL));
    goto loc_0080CB3C;
loc_0080CB2F:
    Arg1 = (Arg1) & (-496);
loc_0080CB3C:
    Arg1 = (Arg1) + (512);
    Arg2 = 0;
    result = v_stack_m120;
    if (v_stack_m120 <= 1) { result = 1; }
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg5)))) & (162));
    v_stack_mE8 = (uint32_t)(Arg2);
    Arg4 = (condition_is_not_equal) ? 1 : 0;
    result = MiInitializeDemandCoalesceContext(v_stack_m98, Arg1, result, Arg4);
loc_0080CB77:
    result = (v_stack_m120) - (v_stack_m128);
    v_stack_mF0 = result;
    if (result < 512) goto loc_0080CE07;
    v_stack_m138 = 1;
    if ((((uint8_t)((uint32_t)(Arg5))) & (96)) == 0) {
        Arg1 = (uint32_t)((1) & ((uint32_t)(result)));
        v_stack_m138 = (uint32_t)(Arg1);
    }
    if (v_stack_m134 == 0) goto loc_0080CC71;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg5)))) & (0x800ULL));
    v_stack_m138 = (uint32_t)(result);
loc_0080CBBF:
    if ((uint32_t)(result) == 0) goto loc_0080CBCF;
    result = MiGetHugeBadRangeFromNode(local_r13, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg4))))), result, Arg4);
    goto loc_0080CC26;
loc_0080CBCF:
    local_rbx = ((uint32_t)(Arg5)) * ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg4))))));
    Arg2 = 0;
    Arg1 = 0;
    local_rbx = (local_rbx) + (*(uint64_t *)(local_r13 + 0x10));
    result = MiInitializePageColorBase(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg4))) + 1, v_stack_mA8);
    v_stack_mA8 = local_rbx + 15216;
    result = MiGetNextPageColor(v_stack_mA8, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg4))) + 1, local_rbx + 15216);
    Arg1 = (uint8_t)(((uint32_t)((uint32_t)(local_r15))) & (1));
    Arg1 = (uint8_t)(-(Arg1));
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg4))) + 1) & (0xFFFFFFD0ULL));
    Arg3 = (uint32_t)((Arg3) + (0x1030ULL));
    result = MiGetHugeRange(local_r13, (uint32_t)((uint32_t)(result)), Arg3, local_rbx + 15216);
loc_0080CC26:
    local_r15 = (uint32_t)((result) & (0x3FFFFFULL));
    if (condition_is_not_equal) goto loc_0080CC52;
    local_r12 = (local_r12) + (4);
    if (local_r12 == v_stack_mD8) goto loc_0080CE03;
    goto loc_0080CBBF;
loc_0080CC52:
    local_r15 = ((uint32_t)(v_stack_m12C)) << (18);
    Arg3 = 0;
    result = MiHugeRangeIsZeroed(local_r13, (uint32_t)(v_stack_m138), Arg3, local_rbx + 15216);
    Arg1 = 0;
    Arg1 = ((uint32_t)(result) != 0) ? 1 : 0;
    v_stack_m130 = (uint32_t)(Arg1);
    goto loc_0080CD76;
loc_0080CC71:
    v_stack_m158 = v_stack_m98;
    result = ((((uint32_t)(local_rbx)) & (0x580ULL)) == 0) ? 1 : 0;
    v_stack_m130 = (uint32_t)(result);
    goto loc_0080CCB9;
loc_0080CC94:
    local_r12 = (local_r12) + (4);
    if (local_r12 == v_stack_mD8) goto loc_0080CE03;
    v_stack_m158 = v_stack_m98;
loc_0080CCB9:
    v_stack_m160 = 1;
    v_stack_m168 = (uint32_t)(local_r15);
    result = MiFindLargeNodePage(local_r13, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r12)))), (uint32_t)(v_stack_m138), (uint32_t)(v_stack_m130));
    v_stack_m110 = result;
    if (result == 0) goto loc_0080CC94;
    local_r15 = (result) - (result);
    local_r15 = (local_r15) >> (4);
    local_r15 = (local_r15) * (result);
    result = MiGetPfnPageSizeIndex(result, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r12)))), (uint32_t)(v_stack_m138), (uint32_t)(v_stack_m130));
    local_rbx = (uint32_t)((*(uint64_t *)(result + 0x10)) & (992));
    v_stack_m138 = (uint32_t)(result);
    result = MiInitializeFoundLargeNodePage(v_stack_m110, (uint32_t)(v_stack_m12C), 1, (uint32_t)(v_stack_m130));
    Arg1 = 0;
    Arg1 = (local_rbx == 0) ? 1 : 0;
    v_stack_m130 = (uint32_t)(Arg1);
    if (local_rbx == 0) goto loc_0080CD71;
    Arg1 = 0;
    v_stack_m130 = 0;
    if (((v_stack_m12C) & (1)) != 0) goto loc_0080CD71;
    if ((uint32_t)((uint32_t)(v_stack_m138)) != 0) goto loc_0080CD56;
    result = MiHugePageOperation(local_r13, local_r15, 1, (uint32_t)(v_stack_m130));
    goto loc_0080CD6A;
loc_0080CD56:
    result = MiZeroLargePage(local_r13, v_stack_m110, (uint32_t)((uint32_t)(result)), 1);
loc_0080CD6A:
    v_stack_m130 = 1;
loc_0080CD71:
loc_0080CD76:
    result = MiAddRangeToPartitionTree(v_stack_mF8, local_r15, *(uint64_t *)(v_rip - 0x7FB120 + (uint32_t)((uint32_t)((uint32_t)(v_stack_m138))) * 8), 1);
    if ((uint32_t)(result) == 0) goto loc_0080CDC5;
    local_r15 = (v_stack_m128) + (*(uint64_t *)(v_rip - 0x7FB120 + (uint32_t)((uint32_t)((uint32_t)(v_stack_m138))) * 8));
    v_stack_m128 = local_r15;
    if (local_r15 == v_stack_m120) goto loc_0080CE5A;
    goto loc_0080CB77;
loc_0080CDC5:
    if ((uint32_t)((uint32_t)(v_stack_m134)) == 0) goto loc_0080CDDF;
    result = MiInsertHugeRangeInPartition((uint32_t)(v_stack_m12C), (uint32_t)(v_stack_m130), *(uint64_t *)(v_rip - 0x7FB120 + (uint32_t)((uint32_t)((uint32_t)(v_stack_m138))) * 8), 1);
    goto loc_0080CE0B;
loc_0080CDDF:
    result = MiFreeMdlPageRun((uint32_t)(v_stack_m12C), (uint32_t)(Arg5), (uint32_t)(v_stack_m130), 1);
    v_stack_m118 = result;
    goto loc_0080CE10;
loc_0080CE03:
loc_0080CE07:
loc_0080CE0B:
loc_0080CE10:
    if (v_stack_m128 == v_stack_m120) goto loc_0080CE5A;
    if ((uint32_t)((uint32_t)(v_stack_m134)) == 0) goto loc_0080CE2D;
    goto loc_0080CFC9;
loc_0080CE2D:
    result = (v_stack_mF0) - (v_stack_m118);
    if (!(condition_is_equal)) {
        Arg2 = result;
        Arg1 = local_r13;
        result = MiReleaseNonPagedResourcesNotExposed(Arg1, Arg2, (uint32_t)(v_stack_m130), 1);
        Arg1 = v_stack_m120;
        Arg2 = v_stack_m118;
    }
    if (v_stack_mE8 != 0) goto loc_0080CFA4;
    if (Arg2 != NULL) goto loc_0080CFA4;
loc_0080CE5A:
    result = (uint32_t)(((uint32_t)(v_stack_m12C)) & (1));
    local_rdi = (uint32_t)(((uint32_t)(v_stack_mE4)) ^ (1));
    local_rdi = (uint32_t)((local_rdi * 2 + 4194304) | ((uint32_t)(result)));
    local_rdi = (uint32_t)((local_rdi) | (16));
    local_rbx = 0;
    local_r10 = (v_stack_m120) & (result);
    v_stack_m110 = local_r10;
    if ((((uint8_t)((uint32_t)(Arg5))) & (16)) == 0) goto loc_0080CEA9;
    local_rdi = (uint32_t)((local_rdi) | (64));
    goto loc_0080CEDD;
loc_0080CEA9:
    if ((((uint8_t)((uint32_t)(Arg5))) & (64)) == 0) goto loc_0080CEBE;
    local_rdi = (uint32_t)((local_rdi) | (64));
    goto loc_0080CED9;
loc_0080CEBE:
    if (condition_is_above_or_equal) goto loc_0080CED4;
    local_rdi = (uint32_t)((local_rdi) | (64));
    goto loc_0080CED9;
loc_0080CED4:
loc_0080CED9:
    v_stack_m100 = (uint32_t)(0xFFFFFULL);
loc_0080CEDD:
    if (v_stack_m128 == Arg1) goto loc_0080CFAB;
    Arg2 = (Arg1) - (v_stack_m128);
    if (Arg2 > ((uint32_t)(0xFFFFFULL))) { Arg2 = (uint32_t)(0xFFFFFULL); }
    Arg3 = ((uint32_t)(v_stack_m130)) | (-1);
    Arg2 = (Arg2) << (12);
    v_stack_m148 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    v_stack_m150 = (uint32_t)(local_rdi);
    v_stack_m158 = (uint32_t)((uint32_t)(Arg4));
    v_stack_m160 = 1;
    v_stack_m168 = Arg2;
    result = MiAllocatePagesForMdl(local_r13, local_r10, Arg3, (uint32_t)(0x40000000ULL));
    if (result != 0) goto loc_0080CF62;
    if ((((uint8_t)(local_rdi)) & (64)) == 0) goto loc_0080CFA4;
    local_rdi = (uint32_t)((local_rdi) & (0xFFFFFFBFULL));
    local_rdi = (uint32_t)((local_rdi) | (32));
loc_0080CF4A:
    goto loc_0080CEDD;
loc_0080CF62:
    result = MiAddMdlToPartitionTree(v_stack_mF8, v_stack_m128, (uint32_t)((uint32_t)(local_rdi)), (uint32_t)(0x40000000ULL));
    Arg2 = 0;
    if ((uint32_t)(result) == 0) goto loc_0080CF8E;
    result = ((uint32_t)(*(uint32_t *)(v_stack_m128 + 0x28))) >> (12);
    result = ExFreePoolWithTag(v_stack_m128, Arg2, (uint32_t)((uint32_t)(local_rdi)), (uint32_t)(0x40000000ULL));
    goto loc_0080CF4A;
loc_0080CF8E:
    Arg4 = 0;
    result = MiFreePagesFromMdl(v_stack_m128, Arg2, Arg4 + 11, Arg4);
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m128, Arg2, Arg4 + 11, Arg4);
loc_0080CFA4:
    goto loc_0080CFC9;
loc_0080CFAB:
    if ((uint32_t)((uint32_t)(v_stack_m134)) != 0) goto loc_0080CFE6;
    result = MiUpdatePartitionLargePfnBitMap(v_stack_mD0, v_stack_mF8, Arg4 + 11, Arg4);
    if (!sign_flag) goto loc_0080CFE2;
loc_0080CFC9:
    result = MiFreePartitionTree(local_r13, v_stack_mF8, (uint32_t)(0x801ULL), 1);
    goto loc_0080D04D;
loc_0080CFE2:
loc_0080CFE6:
    v_stack_mC8 = v_stack_mF8;
    local_r14 = 1;
    if (v_stack_mE0 != 0) { local_r14 = 33; }
    v_stack_mB0 = (uint32_t)(local_r14);
    v_stack_mC0 = v_xmm0;
    if (local_r13 != v_stack_mD0) {
        local_r14 = (uint32_t)((local_r14) | (2));
        v_stack_mB0 = (uint32_t)(local_r14);
    }
    if ((((uint8_t)((uint32_t)(Arg5))) & (8)) != 0) {
        local_r14 = (uint32_t)((local_r14) | (4));
        v_stack_mB0 = (uint32_t)(local_r14);
    }
    if ((uint32_t)((uint32_t)(v_stack_m134)) != 0) {
        local_r14 = (uint32_t)((local_r14) | (16));
        v_stack_mB0 = (uint32_t)(local_r14);
    }
    if (sign_flag) {
    }
    result = MiInsertPartitionPages(local_r13, v_stack_mD0, v_stack_mC8, v_stack_m128);
loc_0080D04D:
    Arg1 = (v_stack_m58) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_mD0, v_stack_mC8, v_stack_m128);
    local_rsp = (local_rsp) + (328);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x4` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0080C9D4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
