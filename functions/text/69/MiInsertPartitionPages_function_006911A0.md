# MiInsertPartitionPages

- RVA: `0x006911A0`–`0x006915BF` (길이 `1,055` bytes)
- VA: `0x00000001406911A0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D9124`
- 디코드: `321`개 명령, `1,055/1,055` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **22**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x006911DC` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x006911EA` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00691218` → [MiDuplicatePartitionNodeTree](MiDuplicatePartitionNodeTree_function_00690B54.md) (function, `0x00690B54`)
- `0x006912A2` → [MiActOnPartitionNodePages](../68/MiActOnPartitionNodePages_function_0068F7F4.md) (function, `0x0068F7F4`)
- `0x006912D8` → [MiUpdatePartitionLargePfnBitMap](../../page/80/MiUpdatePartitionLargePfnBitMap_function_0080DB50.md) (function, `0x0080DB50`)
- `0x006912F3` → [MiInitializeHugePfnDatabase](../67/MiInitializeHugePfnDatabase_function_00676410.md) (function, `0x00676410`)
- `0x00691315` → [MiFreePartitionTree](MiFreePartitionTree_function_00690E50.md) (function, `0x00690E50`)
- `0x0069132F` → [MiFreePartitionTree](MiFreePartitionTree_function_00690E50.md) (function, `0x00690E50`)
- `0x00691361` → [MiIncreaseExposedCommit](../46/MiIncreaseExposedCommit_function_00460A9C.md) (function, `0x00460A9C`)
- `0x00691372` → [MiClearPartitionPageBitMap](MiClearPartitionPageBitMap_function_00690614.md) (function, `0x00690614`)
- `0x00691384` → [MiReduceCommitLimits](../68/MiReduceCommitLimits_function_0068CDA0.md) (function, `0x0068CDA0`)
- `0x00691395` → [MiReturnCommit](../24/MiReturnCommit_function_00248410.md) (function, `0x00248410`)
- `0x006913BA` → [MiFreePartitionTree](MiFreePartitionTree_function_00690E50.md) (function, `0x00690E50`)
- `0x006913C7` → [MiRemovePhysicalMemoryBatchComplete](../67/MiRemovePhysicalMemoryBatchComplete_function_00673B98.md) (function, `0x00673B98`)
- `0x00691400` → [MiInsertHugeRangeInPartition](MiInsertHugeRangeInPartition_function_00690F28.md) (function, `0x00690F28`)
- `0x006914A7` → [RtlNumberOfSetBitsEx](../41/RtlNumberOfSetBitsEx_function_00418CA0.md) (function, `0x00418CA0`)
- `0x006914C2` → [MiActOnPartitionNodePages](../68/MiActOnPartitionNodePages_function_0068F7F4.md) (function, `0x0068F7F4`)
- `0x00691541` → [RtlAvlRemoveNode](../29/RtlAvlRemoveNode_function_00296650.md) (function, `0x00296650`)
- `0x0069155B` → [MiInsertPartitionPageNodes](MiInsertPartitionPageNodes_function_00690F94.md) (function, `0x00690F94`)
- `0x00691577` → [MiInsertHugeRangeInPartition](MiInsertHugeRangeInPartition_function_00690F28.md) (function, `0x00690F28`)
- `0x00691593` → [MiComputeCommitThresholds](../47/MiComputeCommitThresholds_function_0047C904.md) (function, `0x0047C904`)
- `0x0069159C` → [MiDeletePartitionPageNodes](MiDeletePartitionPageNodes_function_006908F0.md) (function, `0x006908F0`)

### Direct callers
- [MmRemovePhysicalMemory](../../page/7F/MmRemovePhysicalMemory_function_007FB560.md) at `0x007FB777`
- [MiAllocatePartitionPhysicalPages](../../page/80/MiAllocatePartitionPhysicalPages_function_0080C9D4.md) at `0x0080D048`
- [MiHotAddPartitionMemory](../../page/80/MiHotAddPartitionMemory_function_0080D5B4.md) at `0x0080D8A1`

### Static image references
- `0x006912B4` → RVA `0x00E38D00` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x006912D8` → [MiUpdatePartitionLargePfnBitMap](../../page/80/MiUpdatePartitionLargePfnBitMap_function_0080DB50.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006911A0  48 8B C4                        mov rax, rsp
006911A3  48 89 58 18                     mov qword ptr [rax + 0x18], rbx
006911A7  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
006911AB  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
006911AF  55                              push rbp
006911B0  56                              push rsi
006911B1  57                              push rdi
006911B2  41 54                           push r12
006911B4  41 55                           push r13
006911B6  41 56                           push r14
006911B8  41 57                           push r15
006911BA  48 8D 68 A1                     lea rbp, [rax - 0x5f]
006911BE  48 81 EC C0 00 00 00            sub rsp, 0xc0
006911C5  4D 8B E8                        mov r13, r8
006911C8  48 8B DA                        mov rbx, rdx
006911CB  4C 8B F9                        mov r15, rcx
006911CE  BF 48 00 00 00                  mov edi, 0x48
006911D3  44 8B C7                        mov r8d, edi
006911D6  48 8D 4D 87                     lea rcx, [rbp - 0x79]
006911DA  33 D2                           xor edx, edx
006911DC  E8 5F 5A 03 00                  call 0x1406c6c40
006911E1  44 8B C7                        mov r8d, edi
006911E4  48 8D 4D D7                     lea rcx, [rbp - 0x29]
006911E8  33 D2                           xor edx, edx
006911EA  E8 51 5A 03 00                  call 0x1406c6c40
006911EF  4D 8B 65 00                     mov r12, qword ptr [r13]
006911F3  4D 8D 75 18                     lea r14, [r13 + 0x18]
006911F7  41 8B 06                        mov eax, dword ptr [r14]
006911FA  33 F6                           xor esi, esi
006911FC  48 21 75 67                     and qword ptr [rbp + 0x67], rsi
00691200  24 14                           and al, 0x14
00691202  4C 89 7D 8F                     mov qword ptr [rbp - 0x71], r15
00691206  49 8B FE                        mov rdi, r14
00691209  48 89 5D 87                     mov qword ptr [rbp - 0x79], rbx
0069120D  3C 04                           cmp al, 4
0069120F  75 1E                           jne 0x14069122f
00691211  49 8B D4                        mov rdx, r12
00691214  48 8D 4D 67                     lea rcx, [rbp + 0x67]
00691218  E8 37 F9 FF FF                  call 0x140690b54
0069121D  85 C0                           test eax, eax
0069121F  75 0A                           jne 0x14069122b
00691221  BE 9A 00 00 C0                  mov esi, 0xc000009a
00691226  E9 6D 03 00 00                  jmp 0x140691598
0069122B  49 8D 7D 18                     lea rdi, [r13 + 0x18]
0069122F  41 8B 06                        mov eax, dword ptr [r14]
00691232  A8 02                           test al, 2
00691234  74 7A                           je 0x1406912b0
00691236  49 8B 04 24                     mov rax, qword ptr [r12]
0069123A  33 DB                           xor ebx, ebx
0069123C  49 8B FE                        mov rdi, r14
0069123F  48 85 C0                        test rax, rax
00691242  74 0F                           je 0x140691253
00691244  48 8B D8                        mov rbx, rax
00691247  48 8B 00                        mov rax, qword ptr [rax]
0069124A  48 85 C0                        test rax, rax
0069124D  75 F5                           jne 0x140691244
0069124F  49 8D 7D 18                     lea rdi, [r13 + 0x18]
00691253  48 85 DB                        test rbx, rbx
00691256  74 58                           je 0x1406912b0
00691258  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0069125C  4C 8B D3                        mov r10, rbx
0069125F  48 8B CB                        mov rcx, rbx
00691262  48 85 C0                        test rax, rax
00691265  74 23                           je 0x14069128a
00691267  48 8B 08                        mov rcx, qword ptr [rax]
0069126A  48 8B D8                        mov rbx, rax
0069126D  48 85 C9                        test rcx, rcx
00691270  74 22                           je 0x140691294
00691272  48 8B 01                        mov rax, qword ptr [rcx]
00691275  48 8B D9                        mov rbx, rcx
00691278  48 8B C8                        mov rcx, rax
0069127B  48 85 C0                        test rax, rax
0069127E  75 F2                           jne 0x140691272
00691280  EB 12                           jmp 0x140691294
00691282  48 39 0B                        cmp qword ptr [rbx], rcx
00691285  74 0D                           je 0x140691294
00691287  48 8B CB                        mov rcx, rbx
0069128A  48 8B 5B 10                     mov rbx, qword ptr [rbx + 0x10]
0069128E  48 83 E3 FC                     and rbx, 0xfffffffffffffffc
00691292  75 EE                           jne 0x140691282
00691294  45 33 C0                        xor r8d, r8d
00691297  4C 8D 4D 87                     lea r9, [rbp - 0x79]
0069129B  49 8B CA                        mov rcx, r10
0069129E  41 8D 50 0A                     lea edx, [r8 + 0xa]
006912A2  E8 4D E5 FF FF                  call 0x14068f7f4
006912A7  48 85 DB                        test rbx, rbx
006912AA  75 AC                           jne 0x140691258
006912AC  49 8D 7D 18                     lea rdi, [r13 + 0x18]
006912B0  41 8B 45 18                     mov eax, dword ptr [r13 + 0x18]
006912B4  48 8D 15 45 7A 7A 00            lea rdx, [rip + 0x7a7a45]
006912BB  8B C8                           mov ecx, eax
006912BD  41 BE 01 00 00 00               mov r14d, 1
006912C3  83 E1 20                        and ecx, 0x20
006912C6  A8 10                           test al, 0x10
006912C8  74 22                           je 0x1406912ec
006912CA  85 C9                           test ecx, ecx
006912CC  0F 84 CB 00 00 00               je 0x14069139d
006912D2  49 8B D4                        mov rdx, r12
006912D5  49 8B CF                        mov rcx, r15
006912D8  E8 73 C8 17 00                  call 0x14080db50
006912DD  8B F0                           mov esi, eax
006912DF  85 C0                           test eax, eax
006912E1  0F 88 B1 02 00 00               js 0x140691598
006912E7  E9 B1 00 00 00                  jmp 0x14069139d
006912EC  48 8B DF                        mov rbx, rdi
006912EF  85 C9                           test ecx, ecx
006912F1  74 59                           je 0x14069134c
006912F3  E8 18 51 FE FF                  call 0x140676410
006912F8  85 C0                           test eax, eax
006912FA  0F 84 21 FF FF FF               je 0x140691221
00691300  45 8B 45 18                     mov r8d, dword ptr [r13 + 0x18]
00691304  45 8B CE                        mov r9d, r14d
00691307  48 8B 4D 6F                     mov rcx, qword ptr [rbp + 0x6f]
0069130B  41 83 C8 04                     or r8d, 4
0069130F  49 8B D4                        mov rdx, r12
00691312  44 89 07                        mov dword ptr [rdi], r8d
00691315  E8 36 FB FF FF                  call 0x140690e50
0069131A  8B F0                           mov esi, eax
0069131C  85 C0                           test eax, eax
0069131E  79 19                           jns 0x140691339
00691320  45 8B CE                        mov r9d, r14d
00691323  41 B8 01 08 00 00               mov r8d, 0x801
00691329  49 8B D4                        mov rdx, r12
0069132C  49 8B CF                        mov rcx, r15
0069132F  E8 1C FB FF FF                  call 0x140690e50
00691334  E9 5F 02 00 00                  jmp 0x140691598
00691339  48 83 65 6F 00                  and qword ptr [rbp + 0x6f], 0
0069133E  49 8D 5D 18                     lea rbx, [r13 + 0x18]
00691342  45 33 E4                        xor r12d, r12d
00691345  48 8D 15 B4 79 7A 00            lea rdx, [rip + 0x7a79b4]
0069134C  8B 07                           mov eax, dword ptr [rdi]
0069134E  4C 3B FA                        cmp r15, rdx
00691351  75 15                           jne 0x140691368
00691353  A9 04 01 00 00                  test eax, 0x104
00691358  75 40                           jne 0x14069139a
0069135A  48 8B 55 7F                     mov rdx, qword ptr [rbp + 0x7f]
0069135E  49 8B CF                        mov rcx, r15
00691361  E8 36 F7 DC FF                  call 0x140460a9c
00691366  EB 32                           jmp 0x14069139a
00691368  A8 20                           test al, 0x20
0069136A  75 0B                           jne 0x140691377
0069136C  49 8B D4                        mov rdx, r12
0069136F  49 8B CF                        mov rcx, r15
00691372  E8 9D F2 FF FF                  call 0x140690614
00691377  48 8B 7D 7F                     mov rdi, qword ptr [rbp + 0x7f]
0069137B  49 8B CF                        mov rcx, r15
0069137E  4C 8B C7                        mov r8, rdi
00691381  48 8B D7                        mov rdx, rdi
00691384  E8 17 BA FF FF                  call 0x14068cda0
00691389  41 B8 10 00 00 00               mov r8d, 0x10
0069138F  48 8B D7                        mov rdx, rdi
00691392  49 8B CF                        mov rcx, r15
00691395  E8 76 70 BB FF                  call 0x140248410
0069139A  48 8B FB                        mov rdi, rbx
0069139D  48 8B 4D 6F                     mov rcx, qword ptr [rbp + 0x6f]
006913A1  48 8D 05 58 79 7A 00            lea rax, [rip + 0x7a7958]
006913A8  48 3B C8                        cmp rcx, rax
006913AB  0F 85 1F 01 00 00               jne 0x1406914d0
006913B1  44 8B 07                        mov r8d, dword ptr [rdi]
006913B4  45 8B CE                        mov r9d, r14d
006913B7  49 8B D4                        mov rdx, r12
006913BA  E8 91 FA FF FF                  call 0x140690e50
006913BF  8B F0                           mov esi, eax
006913C1  8B 07                           mov eax, dword ptr [rdi]
006913C3  A8 04                           test al, 4
006913C5  74 05                           je 0x1406913cc
006913C7  E8 CC 27 FE FF                  call 0x140673b98
006913CC  85 F6                           test esi, esi
006913CE  0F 89 C4 01 00 00               jns 0x140691598
006913D4  8B 07                           mov eax, dword ptr [rdi]
006913D6  A8 20                           test al, 0x20
006913D8  74 30                           je 0x14069140a
006913DA  49 8B 04 24                     mov rax, qword ptr [r12]
006913DE  33 C9                           xor ecx, ecx
006913E0  EB 06                           jmp 0x1406913e8
006913E2  48 8B C8                        mov rcx, rax
006913E5  48 8B 00                        mov rax, qword ptr [rax]
006913E8  48 85 C0                        test rax, rax
006913EB  75 F5                           jne 0x1406913e2
006913ED  48 8B 49 18                     mov rcx, qword ptr [rcx + 0x18]
006913F1  48 BF FF FF FF FF FF FF FF 3F   movabs rdi, 0x3fffffffffffffff
006913FB  48 23 CF                        and rcx, rdi
006913FE  33 D2                           xor edx, edx
00691400  E8 23 FB FF FF                  call 0x140690f28
00691405  E9 8E 01 00 00                  jmp 0x140691598
0069140A  0F 28 55 87                     movaps xmm2, xmmword ptr [rbp - 0x79]
0069140E  83 E0 FB                        and eax, 0xfffffffb
00691411  0F 28 45 97                     movaps xmm0, xmmword ptr [rbp - 0x69]
00691415  49 8B CF                        mov rcx, r15
00691418  0F 28 4D A7                     movaps xmm1, xmmword ptr [rbp - 0x59]
0069141C  33 DB                           xor ebx, ebx
0069141E  0F 29 55 D7                     movaps xmmword ptr [rbp - 0x29], xmm2
00691422  66 0F D6 55 DF                  movq qword ptr [rbp - 0x21], xmm2
00691427  0F 29 45 E7                     movaps xmmword ptr [rbp - 0x19], xmm0
0069142B  0F 28 45 B7                     movaps xmm0, xmmword ptr [rbp - 0x49]
0069142F  0F 29 4D F7                     movaps xmmword ptr [rbp - 9], xmm1
00691433  F2 0F 10 4D C7                  movsd xmm1, qword ptr [rbp - 0x39]
00691438  66 0F 73 DA 08                  psrldq xmm2, 8
0069143D  66 0F D6 55 D7                  movq qword ptr [rbp - 0x29], xmm2
00691442  89 07                           mov dword ptr [rdi], eax
00691444  0F 29 45 07                     movaps xmmword ptr [rbp + 7], xmm0
00691448  F2 0F 11 4D 17                  movsd qword ptr [rbp + 0x17], xmm1
0069144D  49 8B 04 24                     mov rax, qword ptr [r12]
00691451  48 89 4D 6F                     mov qword ptr [rbp + 0x6f], rcx
00691455  EB 06                           jmp 0x14069145d
00691457  48 8B D8                        mov rbx, rax
0069145A  48 8B 00                        mov rax, qword ptr [rax]
0069145D  48 85 C0                        test rax, rax
00691460  75 F5                           jne 0x140691457
00691462  48 85 DB                        test rbx, rbx
00691465  74 69                           je 0x1406914d0
00691467  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0069146B  48 8B FB                        mov rdi, rbx
0069146E  48 8B CB                        mov rcx, rbx
00691471  48 85 C0                        test rax, rax
00691474  74 23                           je 0x140691499
00691476  48 8B 08                        mov rcx, qword ptr [rax]
00691479  48 8B D8                        mov rbx, rax
0069147C  48 85 C9                        test rcx, rcx
0069147F  74 22                           je 0x1406914a3
00691481  48 8B 01                        mov rax, qword ptr [rcx]
00691484  48 8B D9                        mov rbx, rcx
00691487  48 8B C8                        mov rcx, rax
0069148A  48 85 C0                        test rax, rax
0069148D  75 F2                           jne 0x140691481
0069148F  EB 12                           jmp 0x1406914a3
00691491  48 39 0B                        cmp qword ptr [rbx], rcx
00691494  74 0D                           je 0x1406914a3
00691496  48 8B CB                        mov rcx, rbx
00691499  48 8B 5B 10                     mov rbx, qword ptr [rbx + 0x10]
0069149D  48 83 E3 FC                     and rbx, 0xfffffffffffffffc
006914A1  75 EE                           jne 0x140691491
006914A3  48 8D 4F 20                     lea rcx, [rdi + 0x20]
006914A7  E8 F4 77 D8 FF                  call 0x140418ca0
006914AC  41 8B 45 18                     mov eax, dword ptr [r13 + 0x18]
006914B0  A8 02                           test al, 2
006914B2  74 13                           je 0x1406914c7
006914B4  45 33 C0                        xor r8d, r8d
006914B7  4C 8D 4D D7                     lea r9, [rbp - 0x29]
006914BB  48 8B CF                        mov rcx, rdi
006914BE  41 8D 50 0A                     lea edx, [r8 + 0xa]
006914C2  E8 2D E3 FF FF                  call 0x14068f7f4
006914C7  48 85 DB                        test rbx, rbx
006914CA  75 9B                           jne 0x140691467
006914CC  48 8B 4D 6F                     mov rcx, qword ptr [rbp + 0x6f]
006914D0  48 85 C9                        test rcx, rcx
006914D3  0F 84 BF 00 00 00               je 0x140691598
006914D9  49 8B 04 24                     mov rax, qword ptr [r12]
006914DD  33 DB                           xor ebx, ebx
006914DF  EB 06                           jmp 0x1406914e7
006914E1  48 8B D8                        mov rbx, rax
006914E4  48 8B 00                        mov rax, qword ptr [rax]
006914E7  48 85 C0                        test rax, rax
006914EA  75 F5                           jne 0x1406914e1
006914EC  48 85 DB                        test rbx, rbx
006914EF  0F 84 94 00 00 00               je 0x140691589
006914F5  48 BF FF FF FF FF FF FF FF 3F   movabs rdi, 0x3fffffffffffffff
006914FF  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00691503  4C 8B FB                        mov r15, rbx
00691506  48 8B CB                        mov rcx, rbx
00691509  48 85 C0                        test rax, rax
0069150C  74 23                           je 0x140691531
0069150E  48 8B 08                        mov rcx, qword ptr [rax]
00691511  48 8B D8                        mov rbx, rax
00691514  48 85 C9                        test rcx, rcx
00691517  74 22                           je 0x14069153b
00691519  48 8B 01                        mov rax, qword ptr [rcx]
0069151C  48 8B D9                        mov rbx, rcx
0069151F  48 8B C8                        mov rcx, rax
00691522  48 85 C0                        test rax, rax
00691525  75 F2                           jne 0x140691519
00691527  EB 12                           jmp 0x14069153b
00691529  48 39 0B                        cmp qword ptr [rbx], rcx
0069152C  74 0D                           je 0x14069153b
0069152E  48 8B CB                        mov rcx, rbx
00691531  48 8B 5B 10                     mov rbx, qword ptr [rbx + 0x10]
00691535  48 83 E3 FC                     and rbx, 0xfffffffffffffffc
00691539  75 EE                           jne 0x140691529
0069153B  49 8B D7                        mov rdx, r15
0069153E  49 8B CC                        mov rcx, r12
00691541  E8 0A 51 C0 FF                  call 0x140296650
00691546  4D 8B 77 18                     mov r14, qword ptr [r15 + 0x18]
0069154A  4C 8D 4D 67                     lea r9, [rbp + 0x67]
0069154E  48 8B 4D 6F                     mov rcx, qword ptr [rbp + 0x6f]
00691552  4D 8B C7                        mov r8, r15
00691555  49 8B D5                        mov rdx, r13
00691558  4C 23 F7                        and r14, rdi
0069155B  E8 34 FA FF FF                  call 0x140690f94
00691560  85 C0                           test eax, eax
00691562  79 18                           jns 0x14069157c
00691564  85 F6                           test esi, esi
00691566  78 14                           js 0x14069157c
00691568  8B F0                           mov esi, eax
0069156A  41 8B 45 18                     mov eax, dword ptr [r13 + 0x18]
0069156E  A8 20                           test al, 0x20
00691570  74 0A                           je 0x14069157c
00691572  33 D2                           xor edx, edx
00691574  49 8B CE                        mov rcx, r14
00691577  E8 AC F9 FF FF                  call 0x140690f28
0069157C  48 85 DB                        test rbx, rbx
0069157F  0F 85 7A FF FF FF               jne 0x1406914ff
00691585  48 8B 4D 6F                     mov rcx, qword ptr [rbp + 0x6f]
00691589  41 8B 45 18                     mov eax, dword ptr [r13 + 0x18]
0069158D  A8 10                           test al, 0x10
0069158F  75 07                           jne 0x140691598
00691591  33 D2                           xor edx, edx
00691593  E8 6C B3 DE FF                  call 0x14047c904
00691598  48 8D 4D 67                     lea rcx, [rbp + 0x67]
0069159C  E8 4F F3 FF FF                  call 0x1406908f0
006915A1  48 8B 9C 24 10 01 00 00         mov rbx, qword ptr [rsp + 0x110]
006915A9  8B C6                           mov eax, esi
006915AB  48 81 C4 C0 00 00 00            add rsp, 0xc0
006915B2  41 5F                           pop r15
006915B4  41 5E                           pop r14
006915B6  41 5D                           pop r13
006915B8  41 5C                           pop r12
006915BA  5F                              pop rdi
006915BB  5E                              pop rsi
006915BC  5D                              pop rbp
006915BD  C3                              ret
006915BE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiInsertPartitionPages(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p18;

    *(unsigned __int64 *)(v_rsp + 24) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    v_rsp = (v_rsp) - (192);
    a2 = 0;
    result = memset(v_rsp - 95 - 121, a2, 72, a4);
    a2 = 0;
    result = memset(v_rsp - 95 - 41, a2, 72, a4);
    v_rsi = 0;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(a3 + 24))) & (20));
    *(unsigned __int64 *)(v_rsp - 95 - 113) = a1;
    *(unsigned __int64 *)(v_rsp - 95 - 121) = 0;
    if (((unsigned __int8)(result)) != 4) goto loc_0069122F;
    result = MiDuplicatePartitionNodeTree(v_rsp - 95 + 103, *(unsigned __int64 *)(a3), 72, a4);
    if ((unsigned int)(result) != 0) goto loc_0069122B;
loc_00691221:
    goto loc_00691598;
loc_0069122B:
loc_0069122F:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a3 + 24)))) & (2)) == 0) goto loc_006912B0;
    v_rbx = 0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a3)) == 0) goto loc_00691253;
loc_00691244:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3))) != 0) goto loc_00691244;
loc_00691253:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a3)) == 0) goto loc_006912B0;
loc_00691258:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3)) + 8) == 0) goto loc_0069128A;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3)) + 8)) == 0) goto loc_00691294;
loc_00691272:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3)) + 8))) != 0) goto loc_00691272;
    goto loc_00691294;
loc_00691282:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3)) + 8)))) == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3)) + 8))))) goto loc_00691294;
loc_0069128A:
    v_rbx = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3)) + 8)) + 16)) & (-4);
    if (condition_is_not_equal) goto loc_00691282;
loc_00691294:
    a3 = 0;
    result = MiActOnPartitionNodePages(*(unsigned __int64 *)(*(unsigned __int64 *)(a3)), a3 + 10, a3, v_rsp - 95 - 121);
    if (v_rbx != 0) goto loc_00691258;
loc_006912B0:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 24))))) & (32));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a3 + 24)))) & (16)) == 0) goto loc_006912EC;
    if ((unsigned int)(a1) == 0) goto loc_0069139D;
    result = MiUpdatePartitionLargePfnBitMap(a1, *(unsigned __int64 *)(a3), a3, v_rsp - 95 - 121);
    if (sign_flag) goto loc_00691598;
    goto loc_0069139D;
loc_006912EC:
    if ((unsigned int)(a1) == 0) goto loc_0069134C;
    result = MiInitializeHugePfnDatabase(a1, *(unsigned __int64 *)(a3), a3, v_rsp - 95 - 121);
    if ((unsigned int)(result) == 0) goto loc_00691221;
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(a3 + 24))) | (4));
    *(unsigned int *)(a3 + 24) = (unsigned int)(a3);
    result = MiFreePartitionTree(*(unsigned __int64 *)(v_rsp - 95 + 111), *(unsigned __int64 *)(a3), a3, 1);
    if (!sign_flag) goto loc_00691339;
    result = MiFreePartitionTree(a1, *(unsigned __int64 *)(a3), (unsigned int)(0x801ULL), 1);
    goto loc_00691598;
loc_00691339:
    v_r12 = 0;
loc_0069134C:
    if (a1 != (v_rip + 8026548)) goto loc_00691368;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 24)))) & (260)) != 0) goto loc_0069139A;
    result = MiIncreaseExposedCommit(a1, *(unsigned __int64 *)(v_rsp - 95 + 127), (unsigned int)(0x801ULL), 1);
    goto loc_0069139A;
loc_00691368:
    if ((((unsigned __int8)(result)) & (32)) == 0) {
        a2 = 0;
        a1 = a1;
        result = MiClearPartitionPageBitMap(a1, a2, (unsigned int)(0x801ULL), 1);
    }
    result = MiReduceCommitLimits(a1, *(unsigned __int64 *)(v_rsp - 95 + 127), *(unsigned __int64 *)(v_rsp - 95 + 127), 1);
    result = MiReturnCommit(a1, *(unsigned __int64 *)(v_rsp - 95 + 127), 16, 1);
loc_0069139A:
loc_0069139D:
    if ((*(unsigned __int64 *)(v_rsp - 95 + 111)) != (v_rip + 8026456)) goto loc_006914D0;
    result = MiFreePartitionTree(*(unsigned __int64 *)(v_rsp - 95 + 111), 0, (unsigned int)(*(unsigned int *)(a3 + 24)), 1);
    result = (unsigned int)(*(unsigned int *)(a3 + 24));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a3 + 24)))) & (4)) != 0) {
        result = MiRemovePhysicalMemoryBatchComplete(*(unsigned __int64 *)(v_rsp - 95 + 111), 0, (unsigned int)(*(unsigned int *)(a3 + 24)), 1);
    }
    if (!sign_flag) goto loc_00691598;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a3 + 24)))) & (32)) == 0) goto loc_0069140A;
    a1 = 0;
    goto loc_006913E8;
loc_006913E2:
loc_006913E8:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r12)) != 0) goto loc_006913E2;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r12) + 24)) & (a3 + 24);
    a2 = 0;
    result = MiInsertHugeRangeInPartition(a1, a2, (unsigned int)(*(unsigned int *)(a3 + 24)), 1);
    goto loc_00691598;
loc_0069140A:
    result = (unsigned int)((result) & (0xFFFFFFFBULL));
    v_rbx = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 41) = v_xmm2;
    *(unsigned __int64 *)(v_rsp - 95 - 33) = v_xmm2;
    *(unsigned __int64 *)(v_rsp - 95 - 25) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 95 - 9) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 95 - 41) = v_xmm2;
    *(unsigned int *)(a3 + 24) = (unsigned int)(result);
    *(unsigned __int64 *)(v_rsp - 95 + 7) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 95 + 23) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 95 + 111) = a1;
    goto loc_0069145D;
loc_00691457:
loc_0069145D:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r12)) != 0) goto loc_00691457;
    if (*(unsigned __int64 *)(v_r12) == 0) goto loc_006914D0;
loc_00691467:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r12) + 8) == 0) goto loc_00691499;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r12) + 8)) == 0) goto loc_006914A3;
loc_00691481:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r12) + 8))) != 0) goto loc_00691481;
    goto loc_006914A3;
loc_00691491:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r12) + 8)))) == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r12) + 8))))) goto loc_006914A3;
loc_00691499:
    v_rbx = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r12) + 8)) + 16)) & (-4);
    if (condition_is_not_equal) goto loc_00691491;
loc_006914A3:
    result = RtlNumberOfSetBitsEx(*(unsigned __int64 *)(v_r12) + 32, a2, (unsigned int)(*(unsigned int *)(a3 + 24)), 1);
    result = (unsigned int)(*(unsigned int *)(a3 + 24));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a3 + 24)))) & (2)) != 0) {
        a3 = 0;
        a4 = v_rsp - 95 - 41;
        a1 = *(unsigned __int64 *)(v_r12);
        a2 = a3 + 10;
        result = MiActOnPartitionNodePages(a1, a2, a3, a4);
    }
    if (v_rbx != 0) goto loc_00691467;
loc_006914D0:
    if (*(unsigned __int64 *)(v_rsp - 95 + 111) == 0) goto loc_00691598;
    v_rbx = 0;
    goto loc_006914E7;
loc_006914E1:
loc_006914E7:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r12)) != 0) goto loc_006914E1;
    if (*(unsigned __int64 *)(v_r12) == 0) goto loc_00691589;
loc_006914FF:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r12) + 8) == 0) goto loc_00691531;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r12) + 8)) == 0) goto loc_0069153B;
loc_00691519:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r12) + 8))) != 0) goto loc_00691519;
    goto loc_0069153B;
loc_00691529:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r12) + 8)))) == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r12) + 8))))) goto loc_0069153B;
loc_00691531:
    v_rbx = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r12) + 8)) + 16)) & (-4);
    if (condition_is_not_equal) goto loc_00691529;
loc_0069153B:
    result = RtlAvlRemoveNode(0, *(unsigned __int64 *)(v_r12), a3, a4);
    v_r14 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r12) + 24)) & (*(unsigned __int64 *)(v_r12));
    result = MiInsertPartitionPageNodes(*(unsigned __int64 *)(v_rsp - 95 + 111), 0, *(unsigned __int64 *)(v_r12), v_rsp - 95 + 103);
    if (!sign_flag) goto loc_0069157C;
    if (sign_flag) goto loc_0069157C;
    result = (unsigned int)(*(unsigned int *)(a3 + 24));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a3 + 24)))) & (32)) != 0) {
        a2 = 0;
        a1 = v_r14;
        result = MiInsertHugeRangeInPartition(a1, a2, *(unsigned __int64 *)(v_r12), v_rsp - 95 + 103);
    }
    if (v_rbx != 0) goto loc_006914FF;
loc_00691589:
    result = (unsigned int)(*(unsigned int *)(a3 + 24));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a3 + 24)))) & (16)) == 0) {
        a2 = 0;
        result = MiComputeCommitThresholds(*(unsigned __int64 *)(v_rsp - 95 + 111), a2, *(unsigned __int64 *)(v_r12), v_rsp - 95 + 103);
    }
    result = MiDeletePartitionPageNodes(v_rsp - 95 + 103, a2, *(unsigned __int64 *)(v_r12), v_rsp - 95 + 103);
    v_rsp = (v_rsp) + (192);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
}
```

## 5. (Beta) C Style

```c
int64_t MiInsertPartitionPages(int64_t Arg1, int64_t Arg2, void *Arg3, int64_t Arg4)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p18;

    *(uint64_t *)(local_rsp + 0x18) = local_rbx;
    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    local_rsp = (local_rsp) - (192);
    Arg2 = 0;
    result = memset(local_rsp - 95 - 121, Arg2, 72, Arg4);
    Arg2 = 0;
    result = memset(local_rsp - 95 - 41, Arg2, 72, Arg4);
    local_rsi = 0;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(arg3 + 0x18))) & (20));
    *(uint64_t *)(local_rsp - 0x5F - 0x71) = Arg1;
    *(uint64_t *)(local_rsp - 0x5F - 0x79) = 0;
    if (((uint8_t)(result)) != 4) goto loc_0069122F;
    result = MiDuplicatePartitionNodeTree(local_rsp - 95 + 103, *(uint64_t *)(arg3), 72, Arg4);
    if ((uint32_t)(result) != 0) goto loc_0069122B;
loc_00691221:
    goto loc_00691598;
loc_0069122B:
loc_0069122F:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg3 + 0x18)))) & (2)) == 0) goto loc_006912B0;
    local_rbx = 0;
    if (*(uint64_t *)(*(uint64_t *)(arg3)) == 0) goto loc_00691253;
loc_00691244:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg3))) != 0) goto loc_00691244;
loc_00691253:
    if (*(uint64_t *)(*(uint64_t *)(arg3)) == 0) goto loc_006912B0;
loc_00691258:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg3)) + 0x8) == 0) goto loc_0069128A;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg3)) + 0x8)) == 0) goto loc_00691294;
loc_00691272:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg3)) + 0x8))) != 0) goto loc_00691272;
    goto loc_00691294;
loc_00691282:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg3)) + 0x8)))) == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg3)) + 0x8))))) goto loc_00691294;
loc_0069128A:
    local_rbx = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg3)) + 0x8)) + 0x10)) & (-4);
    if (condition_is_not_equal) goto loc_00691282;
loc_00691294:
    Arg3 = 0;
    result = MiActOnPartitionNodePages(*(uint64_t *)(*(uint64_t *)(arg3)), Arg3 + 10, Arg3, local_rsp - 95 - 121);
    if (local_rbx != 0) goto loc_00691258;
loc_006912B0:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x18))))) & (32));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg3 + 0x18)))) & (16)) == 0) goto loc_006912EC;
    if ((uint32_t)(Arg1) == 0) goto loc_0069139D;
    result = MiUpdatePartitionLargePfnBitMap(Arg1, *(uint64_t *)(arg3), Arg3, local_rsp - 95 - 121);
    if (sign_flag) goto loc_00691598;
    goto loc_0069139D;
loc_006912EC:
    if ((uint32_t)(Arg1) == 0) goto loc_0069134C;
    result = MiInitializeHugePfnDatabase(Arg1, *(uint64_t *)(arg3), Arg3, local_rsp - 95 - 121);
    if ((uint32_t)(result) == 0) goto loc_00691221;
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg3 + 0x18))) | (4));
    *(uint32_t *)(arg3 + 0x18) = (uint32_t)(Arg3);
    result = MiFreePartitionTree(*(uint64_t *)(local_rsp - 0x5F + 0x6F), *(uint64_t *)(arg3), Arg3, 1);
    if (!sign_flag) goto loc_00691339;
    result = MiFreePartitionTree(Arg1, *(uint64_t *)(arg3), (uint32_t)(0x801ULL), 1);
    goto loc_00691598;
loc_00691339:
    local_r12 = 0;
loc_0069134C:
    if (Arg1 != (v_rip + 8026548)) goto loc_00691368;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x18)))) & (260)) != 0) goto loc_0069139A;
    result = MiIncreaseExposedCommit(Arg1, *(uint64_t *)(local_rsp - 0x5F + 0x7F), (uint32_t)(0x801ULL), 1);
    goto loc_0069139A;
loc_00691368:
    if ((((uint8_t)(result)) & (32)) == 0) {
        Arg2 = 0;
        Arg1 = Arg1;
        result = MiClearPartitionPageBitMap(Arg1, Arg2, (uint32_t)(0x801ULL), 1);
    }
    result = MiReduceCommitLimits(Arg1, *(uint64_t *)(local_rsp - 0x5F + 0x7F), *(uint64_t *)(local_rsp - 0x5F + 0x7F), 1);
    result = MiReturnCommit(Arg1, *(uint64_t *)(local_rsp - 0x5F + 0x7F), 16, 1);
loc_0069139A:
loc_0069139D:
    if ((*(uint64_t *)(local_rsp - 0x5F + 0x6F)) != (v_rip + 8026456)) goto loc_006914D0;
    result = MiFreePartitionTree(*(uint64_t *)(local_rsp - 0x5F + 0x6F), 0, (uint32_t)(*(uint32_t *)(arg3 + 0x18)), 1);
    result = (uint32_t)(*(uint32_t *)(arg3 + 0x18));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg3 + 0x18)))) & (4)) != 0) {
        result = MiRemovePhysicalMemoryBatchComplete(*(uint64_t *)(local_rsp - 0x5F + 0x6F), 0, (uint32_t)(*(uint32_t *)(arg3 + 0x18)), 1);
    }
    if (!sign_flag) goto loc_00691598;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg3 + 0x18)))) & (32)) == 0) goto loc_0069140A;
    Arg1 = 0;
    goto loc_006913E8;
loc_006913E2:
loc_006913E8:
    if (*(uint64_t *)(*(uint64_t *)(local_r12)) != 0) goto loc_006913E2;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(local_r12) + 0x18)) & (Arg3 + 24);
    Arg2 = 0;
    result = MiInsertHugeRangeInPartition(Arg1, Arg2, (uint32_t)(*(uint32_t *)(arg3 + 0x18)), 1);
    goto loc_00691598;
loc_0069140A:
    result = (uint32_t)((result) & (0xFFFFFFFBULL));
    local_rbx = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x29) = v_xmm2;
    *(uint64_t *)(local_rsp - 0x5F - 0x21) = v_xmm2;
    *(uint64_t *)(local_rsp - 0x5F - 0x19) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x5F - 0x9) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x5F - 0x29) = v_xmm2;
    *(uint32_t *)(arg3 + 0x18) = (uint32_t)(result);
    *(uint64_t *)(local_rsp - 0x5F + 0x7) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x5F + 0x17) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x5F + 0x6F) = Arg1;
    goto loc_0069145D;
loc_00691457:
loc_0069145D:
    if (*(uint64_t *)(*(uint64_t *)(local_r12)) != 0) goto loc_00691457;
    if (*(uint64_t *)(local_r12) == 0) goto loc_006914D0;
loc_00691467:
    if (*(uint64_t *)(*(uint64_t *)(local_r12) + 0x8) == 0) goto loc_00691499;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r12) + 0x8)) == 0) goto loc_006914A3;
loc_00691481:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r12) + 0x8))) != 0) goto loc_00691481;
    goto loc_006914A3;
loc_00691491:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r12) + 0x8)))) == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r12) + 0x8))))) goto loc_006914A3;
loc_00691499:
    local_rbx = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r12) + 0x8)) + 0x10)) & (-4);
    if (condition_is_not_equal) goto loc_00691491;
loc_006914A3:
    result = RtlNumberOfSetBitsEx(*(uint64_t *)(local_r12) + 32, Arg2, (uint32_t)(*(uint32_t *)(arg3 + 0x18)), 1);
    result = (uint32_t)(*(uint32_t *)(arg3 + 0x18));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg3 + 0x18)))) & (2)) != 0) {
        Arg3 = 0;
        Arg4 = local_rsp - 95 - 41;
        Arg1 = *(uint64_t *)(local_r12);
        Arg2 = Arg3 + 10;
        result = MiActOnPartitionNodePages(Arg1, Arg2, Arg3, Arg4);
    }
    if (local_rbx != 0) goto loc_00691467;
loc_006914D0:
    if (*(uint64_t *)(local_rsp - 0x5F + 0x6F) == 0) goto loc_00691598;
    local_rbx = 0;
    goto loc_006914E7;
loc_006914E1:
loc_006914E7:
    if (*(uint64_t *)(*(uint64_t *)(local_r12)) != 0) goto loc_006914E1;
    if (*(uint64_t *)(local_r12) == 0) goto loc_00691589;
loc_006914FF:
    if (*(uint64_t *)(*(uint64_t *)(local_r12) + 0x8) == 0) goto loc_00691531;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r12) + 0x8)) == 0) goto loc_0069153B;
loc_00691519:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r12) + 0x8))) != 0) goto loc_00691519;
    goto loc_0069153B;
loc_00691529:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r12) + 0x8)))) == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r12) + 0x8))))) goto loc_0069153B;
loc_00691531:
    local_rbx = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r12) + 0x8)) + 0x10)) & (-4);
    if (condition_is_not_equal) goto loc_00691529;
loc_0069153B:
    result = RtlAvlRemoveNode(0, *(uint64_t *)(local_r12), Arg3, Arg4);
    local_r14 = (*(uint64_t *)(*(uint64_t *)(local_r12) + 0x18)) & (*(uint64_t *)(local_r12));
    result = MiInsertPartitionPageNodes(*(uint64_t *)(local_rsp - 0x5F + 0x6F), 0, *(uint64_t *)(local_r12), local_rsp - 95 + 103);
    if (!sign_flag) goto loc_0069157C;
    if (sign_flag) goto loc_0069157C;
    result = (uint32_t)(*(uint32_t *)(arg3 + 0x18));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg3 + 0x18)))) & (32)) != 0) {
        Arg2 = 0;
        Arg1 = local_r14;
        result = MiInsertHugeRangeInPartition(Arg1, Arg2, *(uint64_t *)(local_r12), local_rsp - 95 + 103);
    }
    if (local_rbx != 0) goto loc_006914FF;
loc_00691589:
    result = (uint32_t)(*(uint32_t *)(arg3 + 0x18));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg3 + 0x18)))) & (16)) == 0) {
        Arg2 = 0;
        result = MiComputeCommitThresholds(*(uint64_t *)(local_rsp - 0x5F + 0x6F), Arg2, *(uint64_t *)(local_r12), local_rsp - 95 + 103);
    }
    result = MiDeletePartitionPageNodes(local_rsp - 95 + 103, Arg2, *(uint64_t *)(local_r12), local_rsp - 95 + 103);
    local_rsp = (local_rsp) + (192);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `32` | `R` |
| `Arg3` | `+ 0x0` | `32` | `W` |
| `Arg3` | `+ 0x0` | `64` | `R` |
| `Arg3` | `+ 0x18` | `32` | `R` |
| `Arg3` | `+ 0x18` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006911A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
