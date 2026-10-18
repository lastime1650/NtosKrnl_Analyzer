# CmpFindSubKeyByNumberEx

- RVA: `0x0084F1A0`–`0x0084F953` (길이 `1,971` bytes)
- VA: `0x000000014084F1A0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00069D20`
- 디코드: `485`개 명령, `1,971/1,971` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **42**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0084F1F1` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0084F25D` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0084F2C8` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0084F314` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0084F31A` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0084F35E` → [CmpDoQueueLateUnloadWorker](CmpDoQueueLateUnloadWorker_function_0084FB18.md) (function, `0x0084FB18`)
- `0x0084F38D` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0084F3AD` → [CmpFindSubkeyInHashByChildCell](../85/CmpFindSubkeyInHashByChildCell_function_0085E610.md) (function, `0x0085E610`)
- `0x0084F3E1` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0084F436` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0084F467` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0084F471` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0084F478` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0084F4CF` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0084F515` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0084F532` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0084F55E` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0084F568` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0084F575` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0084F5E8` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0084F62F` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0084F647` → [CmpDoFindSubKeyByNumber](../94/CmpDoFindSubKeyByNumber_function_00946F60.md) (function, `0x00946F60`)
- `0x0084F663` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0084F689` → [CmpFindSubkeyInHashByChildCell](../85/CmpFindSubkeyInHashByChildCell_function_0085E610.md) (function, `0x0085E610`)
- `0x0084F73B` → [CmpDoQueueLateUnloadWorker](CmpDoQueueLateUnloadWorker_function_0084FB18.md) (function, `0x0084FB18`)
- `0x0084F74E` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0084F75F` → [CmRmIsKCBVisible](../9A/CmRmIsKCBVisible_function_009A8510.md) (function, `0x009A8510`)
- `0x0084F773` → [CmpIsKeyDeleted](CmpIsKeyDeleted_function_0084BDB0.md) (function, `0x0084BDB0`)
- `0x0084F799` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0084F7B3` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0084F80C` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0084F816` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0084F820` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0084F857` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0084F86E` → [CmpDoFindSubKeyByNumber](../94/CmpDoFindSubKeyByNumber_function_00946F60.md) (function, `0x00946F60`)
- `0x0084F87C` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0084F886` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0084F8BD` → [CmListGetNextElement](../../pagecmrc/BC/CmListGetNextElement_function_00BC9940.md) (function, `0x00BC9940`)
- `0x0084F8D7` → [CmEqualTrans](CmEqualTrans_function_0084BF60.md) (function, `0x0084BF60`)
- `0x0084F909` → [CmRmIsKCBVisible](../9A/CmRmIsKCBVisible_function_009A8510.md) (function, `0x009A8510`)
- `0x0084F919` → [CmpIsKeyDeleted](CmpIsKeyDeleted_function_0084BDB0.md) (function, `0x0084BDB0`)
- `0x0084F93A` → [CmpReferenceKeyControlBlock](../85/CmpReferenceKeyControlBlock_function_0085D370.md) (function, `0x0085D370`)

### Direct callers
- [sub_0084E4B5](Unknown_function_0084E4B5.md) at `0x0084E614`
- [CmpFindSubKeyByNumberFromMergedView](../AB/CmpFindSubKeyByNumberFromMergedView_function_00AB8284.md) at `0x00AB83DD`
- [CmpFindSubKeyByNumberFromMergedView](../AB/CmpFindSubKeyByNumberFromMergedView_function_00AB8284.md) at `0x00AB8489`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **5**
  - `0x0084F314` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x0084F532` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x0084F799` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x0084F7B3` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x0084F8BD` → [CmListGetNextElement](../../pagecmrc/BC/CmListGetNextElement_function_00BC9940.md) (`PAGE` → `PAGECMRC`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0084F1A0  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
0084F1A5  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
0084F1AA  55                              push rbp
0084F1AB  56                              push rsi
0084F1AC  57                              push rdi
0084F1AD  41 54                           push r12
0084F1AF  41 55                           push r13
0084F1B1  41 56                           push r14
0084F1B3  41 57                           push r15
0084F1B5  48 8B EC                        mov rbp, rsp
0084F1B8  48 81 EC 80 00 00 00            sub rsp, 0x80
0084F1BF  45 33 FF                        xor r15d, r15d
0084F1C2  C7 45 C8 FF FF FF FF            mov dword ptr [rbp - 0x38], 0xffffffff
0084F1C9  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
0084F1D0  45 8B E8                        mov r13d, r8d
0084F1D3  4D 8B E1                        mov r12, r9
0084F1D6  44 89 7D CC                     mov dword ptr [rbp - 0x34], r15d
0084F1DA  48 8B D9                        mov rbx, rcx
0084F1DD  4C 89 7D B0                     mov qword ptr [rbp - 0x50], r15
0084F1E1  45 8B F7                        mov r14d, r15d
0084F1E4  4C 8D 45 C8                     lea r8, [rbp - 0x38]
0084F1E8  41 8B FF                        mov edi, r15d
0084F1EB  0F 84 29 01 00 00               je 0x14084f31a
0084F1F1  E8 6A 5A 00 00                  call 0x140854c60
0084F1F6  48 8B F0                        mov rsi, rax
0084F1F9  48 85 C0                        test rax, rax
0084F1FC  0F 84 28 06 00 00               je 0x14084f82a
0084F202  41 C7 04 24 FF FF FF FF         mov dword ptr [r12], 0xffffffff
0084F20A  4C 8B A5 80 00 00 00            mov r12, qword ptr [rbp + 0x80]
0084F211  4D 85 E4                        test r12, r12
0084F214  74 04                           je 0x14084f21a
0084F216  4D 89 3C 24                     mov qword ptr [r12], r15
0084F21A  48 8B 45 60                     mov rax, qword ptr [rbp + 0x60]
0084F21E  48 85 C0                        test rax, rax
0084F221  0F 85 58 03 00 00               jne 0x14084f57f
0084F227  B8 14 00 00 00                  mov eax, 0x14
0084F22C  C7 45 C0 FF FF FF FF            mov dword ptr [rbp - 0x40], 0xffffffff
0084F233  48 8B CE                        mov rcx, rsi
0084F236  44 89 7D C4                     mov dword ptr [rbp - 0x3c], r15d
0084F23A  8B 14 01                        mov edx, dword ptr [rcx + rax]
0084F23D  44 3B EA                        cmp r13d, edx
0084F240  0F 83 9E 02 00 00               jae 0x14084f4e4
0084F246  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0084F24D  4C 8D 45 C0                     lea r8, [rbp - 0x40]
0084F251  8B 56 1C                        mov edx, dword ptr [rsi + 0x1c]
0084F254  48 8B CB                        mov rcx, rbx
0084F257  0F 84 1B 02 00 00               je 0x14084f478
0084F25D  E8 FE 59 00 00                  call 0x140854c60
0084F262  4C 8B F0                        mov r14, rax
0084F265  48 85 C0                        test rax, rax
0084F268  0F 84 D6 06 00 00               je 0x14084f944
0084F26E  B8 72 69 00 00                  mov eax, 0x6972
0084F273  C7 45 B8 FF FF FF FF            mov dword ptr [rbp - 0x48], 0xffffffff
0084F27A  44 89 7D BC                     mov dword ptr [rbp - 0x44], r15d
0084F27E  66 41 39 06                     cmp word ptr [r14], ax
0084F282  0F 84 88 01 00 00               je 0x14084f410
0084F288  41 0F B7 06                     movzx eax, word ptr [r14]
0084F28C  BA 6C 66 00 00                  mov edx, 0x666c
0084F291  66 2B C2                        sub ax, dx
0084F294  BA FF FD 00 00                  mov edx, 0xfdff
0084F299  66 85 C2                        test dx, ax
0084F29C  41 8B C5                        mov eax, r13d
0084F29F  0F 85 45 05 00 00               jne 0x14084f7ea
0084F2A5  45 8B 74 C6 04                  mov r14d, dword ptr [r14 + rax*8 + 4]
0084F2AA  4C 8B 7D 58                     mov r15, qword ptr [rbp + 0x58]
0084F2AE  45 89 37                        mov dword ptr [r15], r14d
0084F2B1  45 33 F6                        xor r14d, r14d
0084F2B4  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0084F2BB  48 8D 55 C0                     lea rdx, [rbp - 0x40]
0084F2BF  48 8B CB                        mov rcx, rbx
0084F2C2  0F 85 AD 02 00 00               jne 0x14084f575
0084F2C8  E8 73 6C 00 00                  call 0x140855f40
0084F2CD  45 33 DB                        xor r11d, r11d
0084F2D0  4D 85 E4                        test r12, r12
0084F2D3  0F 85 8C 00 00 00               jne 0x14084f365
0084F2D9  48 85 FF                        test rdi, rdi
0084F2DC  0F 84 E6 00 00 00               je 0x14084f3c8
0084F2E2  48 8B 57 20                     mov rdx, qword ptr [rdi + 0x20]
0084F2E6  48 8B 0F                        mov rcx, qword ptr [rdi]
0084F2E9  48 83 F9 01                     cmp rcx, 1
0084F2ED  77 35                           ja 0x14084f324
0084F2EF  4C 8B 45 B0                     mov r8, qword ptr [rbp - 0x50]
0084F2F3  49 8D 80 E0 00 00 00            lea rax, [r8 + 0xe0]
0084F2FA  48 39 00                        cmp qword ptr [rax], rax
0084F2FD  0F 84 7F 01 00 00               je 0x14084f482
0084F303  BA 34 00 00 00                  mov edx, 0x34
0084F308  4C 89 5C 24 20                  mov qword ptr [rsp + 0x20], r11
0084F30D  8D 4A 1D                        lea ecx, [rdx + 0x1d]
0084F310  44 8D 4A CD                     lea r9d, [rdx - 0x33]
0084F314  E8 47 E3 CA FF                  call 0x1404fd660
0084F319  CC                              int3
0084F31A  E8 91 59 00 00                  call 0x140854cb0
0084F31F  E9 D2 FE FF FF                  jmp 0x14084f1f6
0084F324  4C 8B 4D B0                     mov r9, qword ptr [rbp - 0x50]
0084F328  4C 8D 41 FF                     lea r8, [rcx - 1]
0084F32C  49 83 F8 02                     cmp r8, 2
0084F330  0F 84 02 02 00 00               je 0x14084f538
0084F336  45 32 D2                        xor r10b, r10b
0084F339  48 8B C1                        mov rax, rcx
0084F33C  F0 4D 0F B1 01                  lock cmpxchg qword ptr [r9], r8
0084F341  48 8B C8                        mov rcx, rax
0084F344  49 8D 40 01                     lea rax, [r8 + 1]
0084F348  48 3B C8                        cmp rcx, rax
0084F34B  75 9C                           jne 0x14084f2e9
0084F34D  49 3B C8                        cmp rcx, r8
0084F350  0F 82 C9 01 00 00               jb 0x14084f51f
0084F356  45 84 D2                        test r10b, r10b
0084F359  74 6D                           je 0x14084f3c8
0084F35B  48 8B CA                        mov rcx, rdx
0084F35E  E8 B5 07 00 00                  call 0x14084fb18
0084F363  EB 63                           jmp 0x14084f3c8
0084F365  41 83 3F FF                     cmp dword ptr [r15], -1
0084F369  0F 84 6A FF FF FF               je 0x14084f2d9
0084F36F  48 85 FF                        test rdi, rdi
0084F372  75 50                           jne 0x14084f3c4
0084F374  48 85 F6                        test rsi, rsi
0084F377  74 1D                           je 0x14084f396
0084F379  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0084F380  48 8D 55 C8                     lea rdx, [rbp - 0x38]
0084F384  48 8B CB                        mov rcx, rbx
0084F387  0F 85 93 04 00 00               jne 0x14084f820
0084F38D  E8 AE 6B 00 00                  call 0x140855f40
0084F392  33 C0                           xor eax, eax
0084F394  8B F0                           mov esi, eax
0084F396  45 8B 0F                        mov r9d, dword ptr [r15]
0084F399  48 8D 45 B0                     lea rax, [rbp - 0x50]
0084F39D  48 8B 55 68                     mov rdx, qword ptr [rbp + 0x68]
0084F3A1  4C 8B C3                        mov r8, rbx
0084F3A4  48 8B 4D 60                     mov rcx, qword ptr [rbp + 0x60]
0084F3A8  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0084F3AD  E8 5E F2 00 00                  call 0x14085e610
0084F3B2  48 8B 7D B0                     mov rdi, qword ptr [rbp - 0x50]
0084F3B6  44 8B F0                        mov r14d, eax
0084F3B9  85 C0                           test eax, eax
0084F3BB  79 07                           jns 0x14084f3c4
0084F3BD  41 C7 07 FF FF FF FF            mov dword ptr [r15], 0xffffffff
0084F3C4  49 89 3C 24                     mov qword ptr [r12], rdi
0084F3C8  48 85 F6                        test rsi, rsi
0084F3CB  74 19                           je 0x14084f3e6
0084F3CD  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0084F3D4  48 8D 55 C8                     lea rdx, [rbp - 0x38]
0084F3D8  48 8B CB                        mov rcx, rbx
0084F3DB  0F 85 7D 01 00 00               jne 0x14084f55e
0084F3E1  E8 5A 6B 00 00                  call 0x140855f40
0084F3E6  48 8B 9C 24 C8 00 00 00         mov rbx, qword ptr [rsp + 0xc8]
0084F3EE  41 8B C6                        mov eax, r14d
0084F3F1  48 81 C4 80 00 00 00            add rsp, 0x80
0084F3F8  41 5F                           pop r15
0084F3FA  41 5E                           pop r14
0084F3FC  41 5D                           pop r13
0084F3FE  41 5C                           pop r12
0084F400  5F                              pop rdi
0084F401  5E                              pop rsi
0084F402  5D                              pop rbp
0084F403  C3                              ret
0084F404  CC                              int3
0084F405  66 66 66 0F 1F 84 00 00 00 00 00  nop word ptr [rax + rax]
0084F410  41 0F B7 46 02                  movzx eax, word ptr [r14 + 2]
0084F415  44 3B F8                        cmp r15d, eax
0084F418  0F 83 6A FE FF FF               jae 0x14084f288
0084F41E  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0084F425  4C 8D 45 B8                     lea r8, [rbp - 0x48]
0084F429  41 8B C7                        mov eax, r15d
0084F42C  48 8B CB                        mov rcx, rbx
0084F42F  41 8B 54 86 04                  mov edx, dword ptr [r14 + rax*4 + 4]
0084F434  74 3B                           je 0x14084f471
0084F436  E8 25 58 00 00                  call 0x140854c60
0084F43B  48 8B C8                        mov rcx, rax
0084F43E  48 85 C0                        test rax, rax
0084F441  0F 84 92 00 00 00               je 0x14084f4d9
0084F447  0F B7 40 02                     movzx eax, word ptr [rax + 2]
0084F44B  44 3B E8                        cmp r13d, eax
0084F44E  72 4A                           jb 0x14084f49a
0084F450  44 2B E8                        sub r13d, eax
0084F453  48 8D 55 B8                     lea rdx, [rbp - 0x48]
0084F457  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0084F45E  48 8B CB                        mov rcx, rbx
0084F461  0F 85 01 01 00 00               jne 0x14084f568
0084F467  E8 D4 6A 00 00                  call 0x140855f40
0084F46C  41 FF C7                        inc r15d
0084F46F  EB 9F                           jmp 0x14084f410
0084F471  E8 3A 58 00 00                  call 0x140854cb0
0084F476  EB C3                           jmp 0x14084f43b
0084F478  E8 33 58 00 00                  call 0x140854cb0
0084F47D  E9 E0 FD FF FF                  jmp 0x14084f262
0084F482  48 8B 55 78                     mov rdx, qword ptr [rbp + 0x78]
0084F486  48 8B 4A 08                     mov rcx, qword ptr [rdx + 8]
0084F48A  48 39 11                        cmp qword ptr [rcx], rdx
0084F48D  0F 84 61 03 00 00               je 0x14084f7f4
0084F493  B9 03 00 00 00                  mov ecx, 3
0084F498  CD 29                           int 0x29
0084F49A  0F B7 01                        movzx eax, word ptr [rcx]
0084F49D  BA 6C 66 00 00                  mov edx, 0x666c
0084F4A2  66 2B C2                        sub ax, dx
0084F4A5  BA FF FD 00 00                  mov edx, 0xfdff
0084F4AA  66 85 C2                        test dx, ax
0084F4AD  41 8B C5                        mov eax, r13d
0084F4B0  48 8D 55 B8                     lea rdx, [rbp - 0x48]
0084F4B4  0F 85 26 03 00 00               jne 0x14084f7e0
0084F4BA  44 8B 74 C1 04                  mov r14d, dword ptr [rcx + rax*8 + 4]
0084F4BF  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0084F4C6  48 8B CB                        mov rcx, rbx
0084F4C9  0F 85 3D 03 00 00               jne 0x14084f80c
0084F4CF  E8 6C 6A 00 00                  call 0x140855f40
0084F4D4  E9 D1 FD FF FF                  jmp 0x14084f2aa
0084F4D9  41 BE FF FF FF FF               mov r14d, 0xffffffff
0084F4DF  E9 C6 FD FF FF                  jmp 0x14084f2aa
0084F4E4  83 BB D8 00 00 00 01            cmp dword ptr [rbx + 0xd8], 1
0084F4EB  0F 86 59 04 00 00               jbe 0x14084f94a
0084F4F1  44 2B EA                        sub r13d, edx
0084F4F4  44 3B 6E 18                     cmp r13d, dword ptr [rsi + 0x18]
0084F4F8  0F 83 4C 04 00 00               jae 0x14084f94a
0084F4FE  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0084F505  4C 8D 45 C0                     lea r8, [rbp - 0x40]
0084F509  8B 56 20                        mov edx, dword ptr [rsi + 0x20]
0084F50C  48 8B CB                        mov rcx, rbx
0084F50F  0F 84 63 FF FF FF               je 0x14084f478
0084F515  E8 46 57 00 00                  call 0x140854c60
0084F51A  E9 43 FD FF FF                  jmp 0x14084f262
0084F51F  4C 8B 45 B0                     mov r8, qword ptr [rbp - 0x50]
0084F523  45 33 C9                        xor r9d, r9d
0084F526  4C 89 5C 24 20                  mov qword ptr [rsp + 0x20], r11
0084F52B  41 8D 51 25                     lea edx, [r9 + 0x25]
0084F52F  8D 4A 2C                        lea ecx, [rdx + 0x2c]
0084F532  E8 29 E1 CA FF                  call 0x1404fd660
0084F537  CC                              int3
0084F538  41 F7 81 B8 00 00 00 00 00 04 00  test dword ptr [r9 + 0xb8], 0x40000
0084F543  0F 84 ED FD FF FF               je 0x14084f336
0084F549  80 BA 80 0B 00 00 01            cmp byte ptr [rdx + 0xb80], 1
0084F550  0F 85 E0 FD FF FF               jne 0x14084f336
0084F556  41 B2 01                        mov r10b, 1
0084F559  E9 DB FD FF FF                  jmp 0x14084f339
0084F55E  E8 BD D6 00 00                  call 0x14085cc20
0084F563  E9 7E FE FF FF                  jmp 0x14084f3e6
0084F568  E8 B3 D6 00 00                  call 0x14085cc20
0084F56D  41 FF C7                        inc r15d
0084F570  E9 9B FE FF FF                  jmp 0x14084f410
0084F575  E8 A6 D6 00 00                  call 0x14085cc20
0084F57A  E9 4E FD FF FF                  jmp 0x14084f2cd
0084F57F  48 05 D0 00 00 00               add rax, 0xd0
0084F585  48 39 00                        cmp qword ptr [rax], rax
0084F588  0F 84 99 FC FF FF               je 0x14084f227
0084F58E  8B 4E 14                        mov ecx, dword ptr [rsi + 0x14]
0084F591  44 89 7D 40                     mov dword ptr [rbp + 0x40], r15d
0084F595  C7 45 D8 FF FF FF FF            mov dword ptr [rbp - 0x28], 0xffffffff
0084F59C  44 89 7D DC                     mov dword ptr [rbp - 0x24], r15d
0084F5A0  C7 45 E0 FF FF FF FF            mov dword ptr [rbp - 0x20], 0xffffffff
0084F5A7  44 89 7D E4                     mov dword ptr [rbp - 0x1c], r15d
0084F5AB  89 4D B8                        mov dword ptr [rbp - 0x48], ecx
0084F5AE  85 C9                           test ecx, ecx
0084F5B0  0F 84 8A 02 00 00               je 0x14084f840
0084F5B6  8B 56 1C                        mov edx, dword ptr [rsi + 0x1c]
0084F5B9  89 55 E8                        mov dword ptr [rbp - 0x18], edx
0084F5BC  8B 46 18                        mov eax, dword ptr [rsi + 0x18]
0084F5BF  85 C0                           test eax, eax
0084F5C1  0F 85 6E 02 00 00               jne 0x14084f835
0084F5C7  C7 45 F0 FF FF FF FF            mov dword ptr [rbp - 0x10], 0xffffffff
0084F5CE  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0084F5D5  8D 14 08                        lea edx, [rax + rcx]
0084F5D8  89 55 C0                        mov dword ptr [rbp - 0x40], edx
0084F5DB  48 8B CB                        mov rcx, rbx
0084F5DE  48 8D 55 C8                     lea rdx, [rbp - 0x38]
0084F5E2  0F 85 94 02 00 00               jne 0x14084f87c
0084F5E8  E8 53 69 00 00                  call 0x140855f40
0084F5ED  49 8B F7                        mov rsi, r15
0084F5F0  41 8B CF                        mov ecx, r15d
0084F5F3  4C 8B 7D 58                     mov r15, qword ptr [rbp + 0x58]
0084F5F7  89 4D D0                        mov dword ptr [rbp - 0x30], ecx
0084F5FA  3B 4D C0                        cmp ecx, dword ptr [rbp - 0x40]
0084F5FD  0F 83 8A 02 00 00               jae 0x14084f88d
0084F603  8B 7D B8                        mov edi, dword ptr [rbp - 0x48]
0084F606  33 C0                           xor eax, eax
0084F608  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
0084F60C  0F B6 83 8C 00 00 00            movzx eax, byte ptr [rbx + 0x8c]
0084F613  24 01                           and al, 1
0084F615  3B CF                           cmp ecx, edi
0084F617  48 8B CB                        mov rcx, rbx
0084F61A  0F 83 2C 02 00 00               jae 0x14084f84c
0084F620  8B 55 E8                        mov edx, dword ptr [rbp - 0x18]
0084F623  4C 8D 45 D8                     lea r8, [rbp - 0x28]
0084F627  84 C0                           test al, al
0084F629  0F 84 1F 01 00 00               je 0x14084f74e
0084F62F  E8 2C 56 00 00                  call 0x140854c60
0084F634  48 85 C0                        test rax, rax
0084F637  0F 84 ED 01 00 00               je 0x14084f82a
0084F63D  44 8B 45 D0                     mov r8d, dword ptr [rbp - 0x30]
0084F641  48 8B D0                        mov rdx, rax
0084F644  48 8B CB                        mov rcx, rbx
0084F647  E8 14 79 0F 00                  call 0x140946f60
0084F64C  48 8D 55 D8                     lea rdx, [rbp - 0x28]
0084F650  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0084F657  48 8B CB                        mov rcx, rbx
0084F65A  41 89 07                        mov dword ptr [r15], eax
0084F65D  0F 85 B3 01 00 00               jne 0x14084f816
0084F663  E8 D8 68 00 00                  call 0x140855f40
0084F668  45 8B 0F                        mov r9d, dword ptr [r15]
0084F66B  41 83 F9 FF                     cmp r9d, -1
0084F66F  0F 84 B5 01 00 00               je 0x14084f82a
0084F675  48 8B 55 68                     mov rdx, qword ptr [rbp + 0x68]
0084F679  48 8D 45 B0                     lea rax, [rbp - 0x50]
0084F67D  48 8B 4D 60                     mov rcx, qword ptr [rbp + 0x60]
0084F681  4C 8B C3                        mov r8, rbx
0084F684  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0084F689  E8 82 EF 00 00                  call 0x14085e610
0084F68E  44 8B F0                        mov r14d, eax
0084F691  85 C0                           test eax, eax
0084F693  0F 88 4D FD FF FF               js 0x14084f3e6
0084F699  48 8B 7D B0                     mov rdi, qword ptr [rbp - 0x50]
0084F69D  48 85 FF                        test rdi, rdi
0084F6A0  0F 85 B2 00 00 00               jne 0x14084f758
0084F6A6  FF 45 40                        inc dword ptr [rbp + 0x40]
0084F6A9  41 8D 45 01                     lea eax, [r13 + 1]
0084F6AD  39 45 40                        cmp dword ptr [rbp + 0x40], eax
0084F6B0  0F 84 17 FC FF FF               je 0x14084f2cd
0084F6B6  48 85 FF                        test rdi, rdi
0084F6B9  0F 84 85 00 00 00               je 0x14084f744
0084F6BF  4C 8B 47 20                     mov r8, qword ptr [rdi + 0x20]
0084F6C3  48 8B 0F                        mov rcx, qword ptr [rdi]
0084F6C6  48 83 F9 01                     cmp rcx, 1
0084F6CA  77 39                           ja 0x14084f705
0084F6CC  48 8B 7D B0                     mov rdi, qword ptr [rbp - 0x50]
0084F6D0  48 8D 87 E0 00 00 00            lea rax, [rdi + 0xe0]
0084F6D7  48 39 00                        cmp qword ptr [rax], rax
0084F6DA  0F 85 A5 00 00 00               jne 0x14084f785
0084F6E0  48 8B 55 78                     mov rdx, qword ptr [rbp + 0x78]
0084F6E4  48 8B 4A 08                     mov rcx, qword ptr [rdx + 8]
0084F6E8  48 39 11                        cmp qword ptr [rcx], rdx
0084F6EB  0F 85 A2 FD FF FF               jne 0x14084f493
0084F6F1  48 89 10                        mov qword ptr [rax], rdx
0084F6F4  48 89 48 08                     mov qword ptr [rax + 8], rcx
0084F6F8  48 89 01                        mov qword ptr [rcx], rax
0084F6FB  48 89 42 08                     mov qword ptr [rdx + 8], rax
0084F6FF  80 4F 40 01                     or byte ptr [rdi + 0x40], 1
0084F703  EB 3F                           jmp 0x14084f744
0084F705  4C 8B 4D B0                     mov r9, qword ptr [rbp - 0x50]
0084F709  48 8D 51 FF                     lea rdx, [rcx - 1]
0084F70D  48 83 FA 02                     cmp rdx, 2
0084F711  0F 84 A2 00 00 00               je 0x14084f7b9
0084F717  45 32 D2                        xor r10b, r10b
0084F71A  48 8B C1                        mov rax, rcx
0084F71D  F0 49 0F B1 11                  lock cmpxchg qword ptr [r9], rdx
0084F722  48 8B C8                        mov rcx, rax
0084F725  48 8D 42 01                     lea rax, [rdx + 1]
0084F729  48 3B C8                        cmp rcx, rax
0084F72C  75 98                           jne 0x14084f6c6
0084F72E  48 3B CA                        cmp rcx, rdx
0084F731  72 6C                           jb 0x14084f79f
0084F733  45 84 D2                        test r10b, r10b
0084F736  74 08                           je 0x14084f740
0084F738  49 8B C8                        mov rcx, r8
0084F73B  E8 D8 03 00 00                  call 0x14084fb18
0084F740  48 8B 7D B0                     mov rdi, qword ptr [rbp - 0x50]
0084F744  8B 4D D0                        mov ecx, dword ptr [rbp - 0x30]
0084F747  FF C1                           inc ecx
0084F749  E9 A9 FE FF FF                  jmp 0x14084f5f7
0084F74E  E8 5D 55 00 00                  call 0x140854cb0
0084F753  E9 DC FE FF FF                  jmp 0x14084f634
0084F758  48 8B 55 70                     mov rdx, qword ptr [rbp + 0x70]
0084F75C  48 8B CF                        mov rcx, rdi
0084F75F  E8 AC 8D 15 00                  call 0x1409a8510
0084F764  84 C0                           test al, al
0084F766  0F 84 3D FF FF FF               je 0x14084f6a9
0084F76C  48 8B 55 70                     mov rdx, qword ptr [rbp + 0x70]
0084F770  48 8B CF                        mov rcx, rdi
0084F773  E8 38 C6 FF FF                  call 0x14084bdb0
0084F778  84 C0                           test al, al
0084F77A  0F 84 26 FF FF FF               je 0x14084f6a6
0084F780  E9 24 FF FF FF                  jmp 0x14084f6a9
0084F785  33 C0                           xor eax, eax
0084F787  4C 8B C7                        mov r8, rdi
0084F78A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0084F78F  44 8D 48 01                     lea r9d, [rax + 1]
0084F793  8D 50 34                        lea edx, [rax + 0x34]
0084F796  8D 48 51                        lea ecx, [rax + 0x51]
0084F799  E8 C2 DE CA FF                  call 0x1404fd660
0084F79E  CC                              int3
0084F79F  4C 8B 45 B0                     mov r8, qword ptr [rbp - 0x50]
0084F7A3  33 C0                           xor eax, eax
0084F7A5  45 33 C9                        xor r9d, r9d
0084F7A8  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0084F7AD  8D 50 25                        lea edx, [rax + 0x25]
0084F7B0  8D 48 51                        lea ecx, [rax + 0x51]
0084F7B3  E8 A8 DE CA FF                  call 0x1404fd660
0084F7B8  CC                              int3
0084F7B9  41 F7 81 B8 00 00 00 00 00 04 00  test dword ptr [r9 + 0xb8], 0x40000
0084F7C4  0F 84 4D FF FF FF               je 0x14084f717
0084F7CA  41 80 B8 80 0B 00 00 01         cmp byte ptr [r8 + 0xb80], 1
0084F7D2  0F 85 3F FF FF FF               jne 0x14084f717
0084F7D8  41 B2 01                        mov r10b, 1
0084F7DB  E9 3A FF FF FF                  jmp 0x14084f71a
0084F7E0  44 8B 74 81 04                  mov r14d, dword ptr [rcx + rax*4 + 4]
0084F7E5  E9 D5 FC FF FF                  jmp 0x14084f4bf
0084F7EA  45 8B 74 86 04                  mov r14d, dword ptr [r14 + rax*4 + 4]
0084F7EF  E9 B6 FA FF FF                  jmp 0x14084f2aa
0084F7F4  48 89 10                        mov qword ptr [rax], rdx
0084F7F7  48 89 48 08                     mov qword ptr [rax + 8], rcx
0084F7FB  48 89 01                        mov qword ptr [rcx], rax
0084F7FE  48 89 42 08                     mov qword ptr [rdx + 8], rax
0084F802  41 80 48 40 01                  or byte ptr [r8 + 0x40], 1
0084F807  E9 BC FB FF FF                  jmp 0x14084f3c8
0084F80C  E8 0F D4 00 00                  call 0x14085cc20
0084F811  E9 94 FA FF FF                  jmp 0x14084f2aa
0084F816  E8 05 D4 00 00                  call 0x14085cc20
0084F81B  E9 48 FE FF FF                  jmp 0x14084f668
0084F820  E8 FB D3 00 00                  call 0x14085cc20
0084F825  E9 68 FB FF FF                  jmp 0x14084f392
0084F82A  41 BE 9A 00 00 C0               mov r14d, 0xc000009a
0084F830  E9 B1 FB FF FF                  jmp 0x14084f3e6
0084F835  8B 56 20                        mov edx, dword ptr [rsi + 0x20]
0084F838  89 55 F0                        mov dword ptr [rbp - 0x10], edx
0084F83B  E9 8E FD FF FF                  jmp 0x14084f5ce
0084F840  C7 45 E8 FF FF FF FF            mov dword ptr [rbp - 0x18], 0xffffffff
0084F847  E9 70 FD FF FF                  jmp 0x14084f5bc
0084F84C  8B 55 F0                        mov edx, dword ptr [rbp - 0x10]
0084F84F  4C 8D 45 E0                     lea r8, [rbp - 0x20]
0084F853  84 C0                           test al, al
0084F855  74 2F                           je 0x14084f886
0084F857  E8 04 54 00 00                  call 0x140854c60
0084F85C  48 85 C0                        test rax, rax
0084F85F  74 C9                           je 0x14084f82a
0084F861  44 8B 45 D0                     mov r8d, dword ptr [rbp - 0x30]
0084F865  48 8B D0                        mov rdx, rax
0084F868  44 2B C7                        sub r8d, edi
0084F86B  48 8B CB                        mov rcx, rbx
0084F86E  E8 ED 76 0F 00                  call 0x140946f60
0084F873  48 8D 55 E0                     lea rdx, [rbp - 0x20]
0084F877  E9 D4 FD FF FF                  jmp 0x14084f650
0084F87C  E8 9F D3 00 00                  call 0x14085cc20
0084F881  E9 67 FD FF FF                  jmp 0x14084f5ed
0084F886  E8 25 54 00 00                  call 0x140854cb0
0084F88B  EB CF                           jmp 0x14084f85c
0084F88D  0F 85 3A FA FF FF               jne 0x14084f2cd
0084F893  48 8B 45 60                     mov rax, qword ptr [rbp + 0x60]
0084F897  45 33 DB                        xor r11d, r11d
0084F89A  48 05 D0 00 00 00               add rax, 0xd0
0084F8A0  4C 89 5D F0                     mov qword ptr [rbp - 0x10], r11
0084F8A4  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0084F8A8  41 C7 07 FF FF FF FF            mov dword ptr [r15], 0xffffffff
0084F8AF  90                              nop
0084F8B0  41 B8 20 00 00 00               mov r8d, 0x20
0084F8B6  48 8D 55 F0                     lea rdx, [rbp - 0x10]
0084F8BA  48 8B C8                        mov rcx, rax
0084F8BD  E8 7E A0 37 00                  call 0x140bc9940
0084F8C2  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
0084F8C6  48 85 C0                        test rax, rax
0084F8C9  0F 84 01 FA FF FF               je 0x14084f2d0
0084F8CF  48 8B 55 70                     mov rdx, qword ptr [rbp + 0x70]
0084F8D3  48 8B 48 38                     mov rcx, qword ptr [rax + 0x38]
0084F8D7  E8 84 C6 FF FF                  call 0x14084bf60
0084F8DC  84 C0                           test al, al
0084F8DE  74 0A                           je 0x14084f8ea
0084F8E0  48 8B 7D E8                     mov rdi, qword ptr [rbp - 0x18]
0084F8E4  83 7F 44 01                     cmp dword ptr [rdi + 0x44], 1
0084F8E8  74 10                           je 0x14084f8fa
0084F8EA  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
0084F8EE  45 33 DB                        xor r11d, r11d
0084F8F1  41 8B FB                        mov edi, r11d
0084F8F4  4C 89 5D B0                     mov qword ptr [rbp - 0x50], r11
0084F8F8  EB B6                           jmp 0x14084f8b0
0084F8FA  48 8B 7F 58                     mov rdi, qword ptr [rdi + 0x58]
0084F8FE  48 8B 55 70                     mov rdx, qword ptr [rbp + 0x70]
0084F902  48 8B CF                        mov rcx, rdi
0084F905  48 89 7D B0                     mov qword ptr [rbp - 0x50], rdi
0084F909  E8 02 8C 15 00                  call 0x1409a8510
0084F90E  84 C0                           test al, al
0084F910  74 D8                           je 0x14084f8ea
0084F912  48 8B 55 70                     mov rdx, qword ptr [rbp + 0x70]
0084F916  48 8B CF                        mov rcx, rdi
0084F919  E8 92 C4 FF FF                  call 0x14084bdb0
0084F91E  84 C0                           test al, al
0084F920  75 C8                           jne 0x14084f8ea
0084F922  8B 45 40                        mov eax, dword ptr [rbp + 0x40]
0084F925  41 3B C5                        cmp eax, r13d
0084F928  74 07                           je 0x14084f931
0084F92A  FF C0                           inc eax
0084F92C  89 45 40                        mov dword ptr [rbp + 0x40], eax
0084F92F  EB B9                           jmp 0x14084f8ea
0084F931  8B 47 28                        mov eax, dword ptr [rdi + 0x28]
0084F934  48 8B CF                        mov rcx, rdi
0084F937  41 89 07                        mov dword ptr [r15], eax
0084F93A  E8 31 DA 00 00                  call 0x14085d370
0084F93F  E9 89 F9 FF FF                  jmp 0x14084f2cd
0084F944  41 BE 9A 00 00 C0               mov r14d, 0xc000009a
0084F94A  4C 8B 7D 58                     mov r15, qword ptr [rbp + 0x58]
0084F94E  E9 7A F9 FF FF                  jmp 0x14084f2cd
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpFindSubKeyByNumberEx(__int64 a1, __int64 a2, int a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rsp;
    unsigned int v_stack_m48;
    unsigned int v_stack_m50;
    unsigned int v_stack_m54;
    unsigned int v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned int v_stack_m60;
    unsigned int v_stack_m68;
    unsigned int v_stack_m6C;
    unsigned int v_stack_m70;
    unsigned int v_stack_m74;
    unsigned int v_stack_m78;
    unsigned int v_stack_m7C;
    unsigned int v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p20 = a4;
    v_rsp = (v_rsp) - (128);
    v_r15 = 0;
    v_stack_m70 = 0xFFFFFFFFULL;
    v_stack_m6C = 0;
    v_stack_m88 = 0;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_0084F31A;
    result = HvpGetCellFlat(a1, a2, v_stack_m70, a4);
loc_0084F1F6:
    if (result == 0) goto loc_0084F82A;
    *(unsigned int *)(a4) = 0xFFFFFFFFULL;
    if (a9 != 0) {
        *(unsigned __int64 *)(a9) = 0;
    }
    if (a5 != 0) goto loc_0084F57F;
loc_0084F227:
    v_stack_m78 = 0xFFFFFFFFULL;
    v_stack_m74 = 0;
    if (((unsigned int)((unsigned int)(a3))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(result + 20 * 1))))) goto loc_0084F4E4;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_0084F478;
    result = HvpGetCellFlat(a1, (unsigned int)(*(unsigned int *)(result + 28)), v_stack_m78, a4);
loc_0084F262:
    if (result == 0) goto loc_0084F944;
    v_stack_m80 = 0xFFFFFFFFULL;
    v_stack_m7C = 0;
    if ((*(unsigned __int16 *)(result)) == ((unsigned __int16)((unsigned int)(0x6972ULL)))) goto loc_0084F410;
loc_0084F288:
    result = (unsigned __int16)((*(unsigned __int16 *)(result)) - ((unsigned __int16)((unsigned int)(0x666CULL))));
    if ((((unsigned __int16)((unsigned int)(0xFDFFULL))) & ((unsigned __int16)(result))) != 0) goto loc_0084F7EA;
loc_0084F2AA:
    *(unsigned int *)(v_stack_p20) = (unsigned int)((unsigned int)(*(unsigned int *)(result + (unsigned int)((unsigned int)((unsigned int)(a3))) * 8 + 4)));
    v_r14 = 0;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) != 0) goto loc_0084F575;
    result = HvpReleaseCellPaged(a1, v_stack_m78, v_stack_m78, a4);
loc_0084F2CD:
    v_r11 = 0;
loc_0084F2D0:
    if (a9 != 0) goto loc_0084F365;
loc_0084F2D9:
    if (0 == 0) goto loc_0084F3C8;
loc_0084F2E9:
    if ((*(unsigned __int64 *)(0)) > 1) goto loc_0084F324;
    if ((*(unsigned __int64 *)(v_stack_m88 + 224)) == (v_stack_m88 + 224)) goto loc_0084F482;
    v_stack_m98 = 0;
    result = KeBugCheckEx(52 + 29, 52, v_stack_m88, 52 - 51);
loc_0084F31A:
    result = HvpGetCellPaged(52 + 29, 52, v_stack_m88, 52 - 51);
    goto loc_0084F1F6;
loc_0084F324:
    if ((52 + 29 - 1) == 2) goto loc_0084F538;
loc_0084F336:
    v_r10 = 0;
loc_0084F339:
    if ((52 + 29) != (52 + 29 - 1 + 1)) goto loc_0084F2E9;
    if ((52 + 29) < (52 + 29 - 1)) goto loc_0084F51F;
    if (0 == 0) goto loc_0084F3C8;
    result = CmpDoQueueLateUnloadWorker(52, 52, 52 + 29 - 1, v_stack_m88);
    goto loc_0084F3C8;
loc_0084F365:
    if ((*(unsigned int *)(v_stack_p20)) == -1) goto loc_0084F2D9;
    if (0 != 0) goto loc_0084F3C4;
    if (result == 0) goto loc_0084F396;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) != 0) goto loc_0084F820;
    result = HvpReleaseCellPaged(a1, v_stack_m70, 52 + 29 - 1, v_stack_m88);
loc_0084F392:
    result = 0;
loc_0084F396:
    v_stack_m98 = v_stack_m88;
    result = CmpFindSubkeyInHashByChildCell(a5, a6, a1, (unsigned int)(*(unsigned int *)(v_stack_p20)));
    if (sign_flag) {
        *(unsigned int *)(v_stack_p20) = 0xFFFFFFFFULL;
    }
    *(unsigned __int64 *)(a9) = v_stack_m88;
loc_0084F3C8:
    if (0 == 0) goto loc_0084F3E6;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) != 0) goto loc_0084F55E;
    result = HvpReleaseCellPaged(a1, v_stack_m70, a1, (unsigned int)(*(unsigned int *)(v_stack_p20)));
loc_0084F3E6:
    v_rsp = (v_rsp) + (128);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_0084F410:
    if (((unsigned int)(v_stack_p20)) >= ((unsigned int)(*(unsigned __int16 *)((unsigned int)((unsigned int)(result)) + 2)))) goto loc_0084F288;
    if (((*(unsigned __int8 *)(v_stack_p10 + 140)) & (1)) == 0) goto loc_0084F471;
    result = HvpGetCellFlat(v_stack_p10, (unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(result)) + (unsigned int)((unsigned int)(v_stack_p20)) * 4 + 4)), v_stack_m80, (unsigned int)(*(unsigned int *)(v_stack_p20)));
loc_0084F43B:
    if (result == 0) goto loc_0084F4D9;
    if (((unsigned int)((unsigned int)(a3))) < ((unsigned int)(*(unsigned __int16 *)(result + 2)))) goto loc_0084F49A;
    v_r13 = (unsigned int)(((unsigned int)(a3)) - ((unsigned int)(*(unsigned __int16 *)(result + 2))));
    if (((*(unsigned __int8 *)(v_stack_p10 + 140)) & (1)) != 0) goto loc_0084F568;
    result = HvpReleaseCellPaged(v_stack_p10, v_stack_m80, v_stack_m80, (unsigned int)(*(unsigned int *)(v_stack_p20)));
    v_r15 = (unsigned int)((v_stack_p20) + 1);
    goto loc_0084F410;
loc_0084F471:
    result = HvpGetCellPaged(v_stack_p10, v_stack_m80, v_stack_m80, (unsigned int)(*(unsigned int *)(v_stack_p20)));
    goto loc_0084F43B;
loc_0084F478:
    result = HvpGetCellPaged(v_stack_p10, v_stack_m80, v_stack_m80, (unsigned int)(*(unsigned int *)(v_stack_p20)));
    goto loc_0084F262;
loc_0084F482:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 8))) == a8) goto loc_0084F7F4;
loc_0084F493:
loc_0084F49A:
    result = (unsigned __int16)((*(unsigned __int16 *)(3)) - ((unsigned __int16)((unsigned int)(0x666CULL))));
    if ((((unsigned __int16)((unsigned int)(0xFDFFULL))) & ((unsigned __int16)(result))) != 0) goto loc_0084F7E0;
loc_0084F4BF:
    if (((*(unsigned __int8 *)(v_stack_p10 + 140)) & (1)) != 0) goto loc_0084F80C;
    result = HvpReleaseCellPaged(v_stack_p10, v_stack_m80, v_stack_m80, (unsigned int)(*(unsigned int *)(v_stack_p20)));
    goto loc_0084F2AA;
loc_0084F4D9:
    goto loc_0084F2AA;
loc_0084F4E4:
    if ((*(unsigned int *)(v_stack_p10 + 216)) <= 1) goto loc_0084F94A;
    v_r13 = (unsigned int)((v_r13) - ((unsigned int)(v_stack_m80)));
    if (((unsigned int)(v_r13)) >= (*(unsigned int *)(0 + 24))) goto loc_0084F94A;
    if (((*(unsigned __int8 *)(v_stack_p10 + 140)) & (1)) == 0) goto loc_0084F478;
    result = HvpGetCellFlat(v_stack_p10, (unsigned int)(*(unsigned int *)(0 + 32)), v_stack_m78, (unsigned int)(*(unsigned int *)(v_stack_p20)));
    goto loc_0084F262;
loc_0084F51F:
    a4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(a4 + 37 + 44, a4 + 37, v_stack_m88, a4);
loc_0084F538:
    if (((*(unsigned int *)(a4 + 184)) & (0x40000ULL)) == 0) goto loc_0084F336;
    if ((*(unsigned __int8 *)(a4 + 37 + 2944)) != 1) goto loc_0084F336;
    goto loc_0084F339;
loc_0084F55E:
    result = HvpReleaseCellFlat(a4 + 37 + 44, a4 + 37, v_stack_m88, a4);
    goto loc_0084F3E6;
loc_0084F568:
    result = HvpReleaseCellFlat(a4 + 37 + 44, a4 + 37, v_stack_m88, a4);
    v_r15 = (unsigned int)((v_r15) + 1);
    goto loc_0084F410;
loc_0084F575:
    result = HvpReleaseCellFlat(a4 + 37 + 44, a4 + 37, v_stack_m88, a4);
    goto loc_0084F2CD;
loc_0084F57F:
    result = (result) + (208);
    if ((*(unsigned __int64 *)(result)) == result) goto loc_0084F227;
    v_stack_p8 = (unsigned int)(v_r15);
    v_stack_m60 = 0xFFFFFFFFULL;
    v_stack_m5C = (unsigned int)(v_r15);
    v_stack_m58 = 0xFFFFFFFFULL;
    v_stack_m54 = (unsigned int)(v_r15);
    v_stack_m80 = (unsigned int)((unsigned int)(*(unsigned int *)(0 + 20)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(0 + 20))) == 0) goto loc_0084F840;
    v_stack_m50 = (unsigned int)((unsigned int)(*(unsigned int *)(0 + 28)));
loc_0084F5BC:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(0 + 24))) != 0) goto loc_0084F835;
    v_stack_m48 = 0xFFFFFFFFULL;
loc_0084F5CE:
    v_stack_m78 = (unsigned int)((unsigned int)(*(unsigned int *)(0 + 24)) + (unsigned int)(*(unsigned int *)(0 + 20)) * 1);
    if (((*(unsigned __int8 *)(v_stack_p10 + 140)) & (1)) != 0) goto loc_0084F87C;
    result = HvpReleaseCellPaged(v_stack_p10, v_stack_m70, v_stack_m88, a4);
loc_0084F5ED:
loc_0084F5F7:
    v_stack_m68 = (unsigned int)((unsigned int)((unsigned int)(v_r15)));
    if (((unsigned int)((unsigned int)((unsigned int)(v_r15)))) >= v_stack_m78) goto loc_0084F88D;
    result = 0;
    v_stack_m88 = 0;
    result = (unsigned __int8)((*(unsigned __int8 *)(v_stack_p10 + 140)) & (1));
    if (((unsigned int)((unsigned int)((unsigned int)(v_r15)))) >= ((unsigned int)((unsigned int)(v_stack_m80)))) goto loc_0084F84C;
    if ((unsigned __int8)(result) == 0) goto loc_0084F74E;
    result = HvpGetCellFlat(v_stack_p10, (unsigned int)(v_stack_m50), v_stack_m60, a4);
loc_0084F634:
    if (result == 0) goto loc_0084F82A;
    result = CmpDoFindSubKeyByNumber(v_stack_p10, result, (unsigned int)(v_stack_m68), a4);
loc_0084F650:
    *(unsigned int *)(v_stack_p20) = (unsigned int)(result);
    if (((*(unsigned __int8 *)(v_stack_p10 + 140)) & (1)) != 0) goto loc_0084F816;
    result = HvpReleaseCellPaged(v_stack_p10, v_stack_m60, (unsigned int)(v_stack_m68), a4);
loc_0084F668:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20)))) == -1) goto loc_0084F82A;
    v_stack_p20 = v_stack_m88;
    result = CmpFindSubkeyInHashByChildCell(a5, a6, v_stack_p10, (unsigned int)(*(unsigned int *)(v_stack_p20)));
    if (sign_flag) goto loc_0084F3E6;
    if (v_stack_m88 != 0) goto loc_0084F758;
loc_0084F6A6:
loc_0084F6A9:
    if (v_stack_p8 == ((unsigned int)(v_r13 + 1))) goto loc_0084F2CD;
    if (v_stack_m88 == 0) goto loc_0084F744;
loc_0084F6C6:
    if ((*(unsigned __int64 *)(v_stack_m88)) > 1) goto loc_0084F705;
    if ((*(unsigned __int64 *)(v_stack_m88 + 224)) != (v_stack_m88 + 224)) goto loc_0084F785;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 8))) != a8) goto loc_0084F493;
    *(unsigned __int64 *)(v_stack_m88 + 224) = a8;
    *(unsigned __int64 *)(v_stack_m88 + 224 + 8) = *(unsigned __int64 *)(a8 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 8)) = v_stack_m88 + 224;
    *(unsigned __int64 *)(a8 + 8) = v_stack_m88 + 224;
    goto loc_0084F744;
loc_0084F705:
    if ((*(unsigned __int64 *)(a8 + 8) - 1) == 2) goto loc_0084F7B9;
loc_0084F717:
    v_r10 = 0;
loc_0084F71A:
    if ((*(unsigned __int64 *)(a8 + 8)) != (*(unsigned __int64 *)(a8 + 8) - 1 + 1)) goto loc_0084F6C6;
    if ((*(unsigned __int64 *)(a8 + 8)) < (*(unsigned __int64 *)(a8 + 8) - 1)) goto loc_0084F79F;
    result = *(unsigned __int64 *)(a8 + 8) - 1 + 1;
    if (0 != 0) {
        a1 = *(unsigned __int64 *)(v_stack_m88 + 32);
        result = CmpDoQueueLateUnloadWorker(a1, *(unsigned __int64 *)(a8 + 8) - 1, *(unsigned __int64 *)(v_stack_m88 + 32), v_stack_m88);
    }
loc_0084F744:
    a1 = (unsigned int)(((unsigned int)(v_stack_m68)) + 1);
    goto loc_0084F5F7;
loc_0084F74E:
    result = HvpGetCellPaged(a1, *(unsigned __int64 *)(a8 + 8) - 1, *(unsigned __int64 *)(v_stack_m88 + 32), v_stack_m88);
    goto loc_0084F634;
loc_0084F758:
    result = CmRmIsKCBVisible(v_stack_m88, a7, *(unsigned __int64 *)(v_stack_m88 + 32), v_stack_m88);
    if ((unsigned __int8)(result) == 0) goto loc_0084F6A9;
    result = CmpIsKeyDeleted(v_stack_m88, a7, *(unsigned __int64 *)(v_stack_m88 + 32), v_stack_m88);
    if ((unsigned __int8)(result) == 0) goto loc_0084F6A6;
    goto loc_0084F6A9;
loc_0084F785:
    result = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(result + 81, result + 52, v_stack_m88, result + 1);
loc_0084F79F:
    result = 0;
    a4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(result + 81, result + 37, v_stack_m88, a4);
loc_0084F7B9:
    if (((*(unsigned int *)(a4 + 184)) & (0x40000ULL)) == 0) goto loc_0084F717;
    if ((*(unsigned __int8 *)(v_stack_m88 + 2944)) != 1) goto loc_0084F717;
    goto loc_0084F71A;
loc_0084F7E0:
    goto loc_0084F4BF;
loc_0084F7EA:
    goto loc_0084F2AA;
loc_0084F7F4:
    *(unsigned __int64 *)(result) = result + 37;
    *(unsigned __int64 *)(result + 8) = result + 81;
    *(unsigned __int64 *)(result + 81) = result;
    *(unsigned __int64 *)(result + 37 + 8) = result;
    goto loc_0084F3C8;
loc_0084F80C:
    result = HvpReleaseCellFlat(result + 81, result + 37, v_stack_m88, a4);
    goto loc_0084F2AA;
loc_0084F816:
    result = HvpReleaseCellFlat(result + 81, result + 37, v_stack_m88, a4);
    goto loc_0084F668;
loc_0084F820:
    result = HvpReleaseCellFlat(result + 81, result + 37, v_stack_m88, a4);
    goto loc_0084F392;
loc_0084F82A:
    goto loc_0084F3E6;
loc_0084F835:
    v_stack_m48 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r15 + 32)));
    goto loc_0084F5CE;
loc_0084F840:
    v_stack_m50 = 0xFFFFFFFFULL;
    goto loc_0084F5BC;
loc_0084F84C:
    if ((unsigned __int8)(result) == 0) goto loc_0084F886;
    result = HvpGetCellFlat(result + 81, (unsigned int)(v_stack_m48), v_stack_m58, a4);
loc_0084F85C:
    if (result == 0) goto loc_0084F82A;
    a3 = (unsigned int)(((unsigned int)(v_stack_m68)) - ((unsigned int)(v_stack_m88)));
    result = CmpDoFindSubKeyByNumber(v_stack_p10, result, a3, a4);
    goto loc_0084F650;
loc_0084F87C:
    result = HvpReleaseCellFlat(v_stack_p10, v_stack_m58, a3, a4);
    goto loc_0084F5ED;
loc_0084F886:
    result = HvpGetCellPaged(v_stack_p10, v_stack_m58, a3, a4);
    goto loc_0084F85C;
loc_0084F88D:
    if (condition_is_not_equal) goto loc_0084F2CD;
    v_r11 = 0;
    result = (a5) + (208);
    v_stack_m48 = 0;
    v_stack_m68 = result;
    *(unsigned int *)(v_stack_p20) = 0xFFFFFFFFULL;
loc_0084F8B0:
    result = CmListGetNextElement(result, v_stack_m48, 32, a4);
    v_stack_m50 = result;
    if (result == 0) goto loc_0084F2D0;
    result = CmEqualTrans(*(unsigned __int64 *)(result + 56), a7, 32, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0084F8EA;
    if ((*(unsigned int *)(v_stack_m50 + 68)) == 1) goto loc_0084F8FA;
loc_0084F8EA:
    v_r11 = 0;
    v_stack_m88 = 0;
    goto loc_0084F8B0;
loc_0084F8FA:
    v_stack_m88 = *(unsigned __int64 *)(0 + 88);
    result = CmRmIsKCBVisible(*(unsigned __int64 *)(0 + 88), a7, 32, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0084F8EA;
    result = CmpIsKeyDeleted(*(unsigned __int64 *)(0 + 88), a7, 32, a4);
    if ((unsigned __int8)(result) != 0) goto loc_0084F8EA;
    if (((unsigned int)((unsigned int)(v_stack_p8))) == ((unsigned int)(v_r13))) goto loc_0084F931;
    result = (unsigned int)(((unsigned int)(v_stack_p8)) + 1);
    v_stack_p8 = (unsigned int)(result);
    goto loc_0084F8EA;
loc_0084F931:
    *(unsigned int *)(v_stack_p20) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(0 + 88) + 40)));
    result = CmpReferenceKeyControlBlock(*(unsigned __int64 *)(0 + 88), a7, 32, a4);
    goto loc_0084F2CD;
loc_0084F944:
loc_0084F94A:
    goto loc_0084F2CD;
}
```

## 5. (Beta) C Style

```c
int64_t CmpFindSubKeyByNumberEx(void *Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6, int64_t Arg7, void *Arg8, int64_t Arg9)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg8 = (uint8_t *)Arg8;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rsp;
    uint32_t v_stack_m48;
    uint32_t v_stack_m50;
    uint32_t v_stack_m54;
    uint32_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint32_t v_stack_m60;
    uint32_t v_stack_m68;
    uint32_t v_stack_m6C;
    uint32_t v_stack_m70;
    uint32_t v_stack_m74;
    uint32_t v_stack_m78;
    uint32_t v_stack_m7C;
    uint32_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m98;
    uint64_t v_stack_p10;
    uint64_t v_stack_p20;
    uint32_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p20 = Arg4;
    local_rsp = (local_rsp) - (128);
    local_r15 = 0;
    v_stack_m70 = 0xFFFFFFFFULL;
    v_stack_m6C = 0;
    v_stack_m88 = 0;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_0084F31A;
    result = HvpGetCellFlat(Arg1, Arg2, v_stack_m70, Arg4);
loc_0084F1F6:
    if (result == 0) goto loc_0084F82A;
    *(uint32_t *)(Arg4) = 0xFFFFFFFFULL;
    if (Arg9 != 0) {
        *(uint64_t *)(Arg9) = 0;
    }
    if (Arg5 != 0) goto loc_0084F57F;
loc_0084F227:
    v_stack_m78 = 0xFFFFFFFFULL;
    v_stack_m74 = 0;
    if (((uint32_t)((uint32_t)(Arg3))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x14 * 1))))) goto loc_0084F4E4;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_0084F478;
    result = HvpGetCellFlat(Arg1, (uint32_t)(*(uint32_t *)(result + 0x1C)), v_stack_m78, Arg4);
loc_0084F262:
    if (result == 0) goto loc_0084F944;
    v_stack_m80 = 0xFFFFFFFFULL;
    v_stack_m7C = 0;
    if ((*(uint16_t *)(result)) == ((uint16_t)((uint32_t)(0x6972ULL)))) goto loc_0084F410;
loc_0084F288:
    result = (uint16_t)((*(uint16_t *)(result)) - ((uint16_t)((uint32_t)(0x666CULL))));
    if ((((uint16_t)((uint32_t)(0xFDFFULL))) & ((uint16_t)(result))) != 0) goto loc_0084F7EA;
loc_0084F2AA:
    *(uint32_t *)(v_stack_p20) = (uint32_t)((uint32_t)(*(uint32_t *)(result + (uint32_t)((uint32_t)((uint32_t)(Arg3))) * 8 + 0x4)));
    local_r14 = 0;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) != 0) goto loc_0084F575;
    result = HvpReleaseCellPaged(Arg1, v_stack_m78, v_stack_m78, Arg4);
loc_0084F2CD:
    local_r11 = 0;
loc_0084F2D0:
    if (Arg9 != 0) goto loc_0084F365;
loc_0084F2D9:
    if (0 == 0) goto loc_0084F3C8;
loc_0084F2E9:
    if ((*(uint64_t *)(0)) > 1) goto loc_0084F324;
    if ((*(uint64_t *)(v_stack_m88 + 0xE0)) == (v_stack_m88 + 224)) goto loc_0084F482;
    v_stack_m98 = 0;
    result = KeBugCheckEx(52 + 29, 52, v_stack_m88, 52 - 51);
loc_0084F31A:
    result = HvpGetCellPaged(52 + 29, 52, v_stack_m88, 52 - 51);
    goto loc_0084F1F6;
loc_0084F324:
    if ((52 + 29 - 1) == 2) goto loc_0084F538;
loc_0084F336:
    local_r10 = 0;
loc_0084F339:
    if ((52 + 29) != (52 + 29 - 1 + 1)) goto loc_0084F2E9;
    if ((52 + 29) < (52 + 29 - 1)) goto loc_0084F51F;
    if (0 == 0) goto loc_0084F3C8;
    result = CmpDoQueueLateUnloadWorker(52, 52, 52 + 29 - 1, v_stack_m88);
    goto loc_0084F3C8;
loc_0084F365:
    if ((*(uint32_t *)(v_stack_p20)) == -1) goto loc_0084F2D9;
    if (0 != 0) goto loc_0084F3C4;
    if (result == 0) goto loc_0084F396;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) != 0) goto loc_0084F820;
    result = HvpReleaseCellPaged(Arg1, v_stack_m70, 52 + 29 - 1, v_stack_m88);
loc_0084F392:
    result = 0;
loc_0084F396:
    v_stack_m98 = v_stack_m88;
    result = CmpFindSubkeyInHashByChildCell(Arg5, Arg6, Arg1, (uint32_t)(*(uint32_t *)(v_stack_p20)));
    if (sign_flag) {
        *(uint32_t *)(v_stack_p20) = 0xFFFFFFFFULL;
    }
    *(uint64_t *)(Arg9) = v_stack_m88;
loc_0084F3C8:
    if (0 == 0) goto loc_0084F3E6;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) != 0) goto loc_0084F55E;
    result = HvpReleaseCellPaged(Arg1, v_stack_m70, Arg1, (uint32_t)(*(uint32_t *)(v_stack_p20)));
loc_0084F3E6:
    local_rsp = (local_rsp) + (128);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_0084F410:
    if (((uint32_t)(v_stack_p20)) >= ((uint32_t)(*(uint16_t *)((uint32_t)((uint32_t)(result)) + 0x2)))) goto loc_0084F288;
    if (((*(uint8_t *)(v_stack_p10 + 0x8C)) & (1)) == 0) goto loc_0084F471;
    result = HvpGetCellFlat(v_stack_p10, (uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(result)) + (uint32_t)((uint32_t)(v_stack_p20)) * 4 + 0x4)), v_stack_m80, (uint32_t)(*(uint32_t *)(v_stack_p20)));
loc_0084F43B:
    if (result == 0) goto loc_0084F4D9;
    if (((uint32_t)((uint32_t)(Arg3))) < ((uint32_t)(*(uint16_t *)(result + 0x2)))) goto loc_0084F49A;
    local_r13 = (uint32_t)(((uint32_t)(Arg3)) - ((uint32_t)(*(uint16_t *)(result + 0x2))));
    if (((*(uint8_t *)(v_stack_p10 + 0x8C)) & (1)) != 0) goto loc_0084F568;
    result = HvpReleaseCellPaged(v_stack_p10, v_stack_m80, v_stack_m80, (uint32_t)(*(uint32_t *)(v_stack_p20)));
    local_r15 = (uint32_t)((v_stack_p20) + 1);
    goto loc_0084F410;
loc_0084F471:
    result = HvpGetCellPaged(v_stack_p10, v_stack_m80, v_stack_m80, (uint32_t)(*(uint32_t *)(v_stack_p20)));
    goto loc_0084F43B;
loc_0084F478:
    result = HvpGetCellPaged(v_stack_p10, v_stack_m80, v_stack_m80, (uint32_t)(*(uint32_t *)(v_stack_p20)));
    goto loc_0084F262;
loc_0084F482:
    if ((*(uint64_t *)(*(uint64_t *)(arg8 + 0x8))) == Arg8) goto loc_0084F7F4;
loc_0084F493:
loc_0084F49A:
    result = (uint16_t)((*(uint16_t *)(3)) - ((uint16_t)((uint32_t)(0x666CULL))));
    if ((((uint16_t)((uint32_t)(0xFDFFULL))) & ((uint16_t)(result))) != 0) goto loc_0084F7E0;
loc_0084F4BF:
    if (((*(uint8_t *)(v_stack_p10 + 0x8C)) & (1)) != 0) goto loc_0084F80C;
    result = HvpReleaseCellPaged(v_stack_p10, v_stack_m80, v_stack_m80, (uint32_t)(*(uint32_t *)(v_stack_p20)));
    goto loc_0084F2AA;
loc_0084F4D9:
    goto loc_0084F2AA;
loc_0084F4E4:
    if ((*(uint32_t *)(v_stack_p10 + 0xD8)) <= 1) goto loc_0084F94A;
    local_r13 = (uint32_t)((local_r13) - ((uint32_t)(v_stack_m80)));
    if (((uint32_t)(local_r13)) >= (*(uint32_t *)(0 + 0x18))) goto loc_0084F94A;
    if (((*(uint8_t *)(v_stack_p10 + 0x8C)) & (1)) == 0) goto loc_0084F478;
    result = HvpGetCellFlat(v_stack_p10, (uint32_t)(*(uint32_t *)(0 + 0x20)), v_stack_m78, (uint32_t)(*(uint32_t *)(v_stack_p20)));
    goto loc_0084F262;
loc_0084F51F:
    Arg4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(Arg4 + 37 + 44, Arg4 + 37, v_stack_m88, Arg4);
loc_0084F538:
    if (((*(uint32_t *)(Arg4 + 0xB8)) & (0x40000ULL)) == 0) goto loc_0084F336;
    if ((*(uint8_t *)(Arg4 + 0x25 + 0xB80)) != 1) goto loc_0084F336;
    goto loc_0084F339;
loc_0084F55E:
    result = HvpReleaseCellFlat(Arg4 + 37 + 44, Arg4 + 37, v_stack_m88, Arg4);
    goto loc_0084F3E6;
loc_0084F568:
    result = HvpReleaseCellFlat(Arg4 + 37 + 44, Arg4 + 37, v_stack_m88, Arg4);
    local_r15 = (uint32_t)((local_r15) + 1);
    goto loc_0084F410;
loc_0084F575:
    result = HvpReleaseCellFlat(Arg4 + 37 + 44, Arg4 + 37, v_stack_m88, Arg4);
    goto loc_0084F2CD;
loc_0084F57F:
    result = (result) + (208);
    if ((*(uint64_t *)(result)) == result) goto loc_0084F227;
    v_stack_p8 = (uint32_t)(local_r15);
    v_stack_m60 = 0xFFFFFFFFULL;
    v_stack_m5C = (uint32_t)(local_r15);
    v_stack_m58 = 0xFFFFFFFFULL;
    v_stack_m54 = (uint32_t)(local_r15);
    v_stack_m80 = (uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x14)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x14))) == 0) goto loc_0084F840;
    v_stack_m50 = (uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x1C)));
loc_0084F5BC:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x18))) != 0) goto loc_0084F835;
    v_stack_m48 = 0xFFFFFFFFULL;
loc_0084F5CE:
    v_stack_m78 = (uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x18)) + (uint32_t)(*(uint32_t *)(0 + 0x14)) * 1);
    if (((*(uint8_t *)(v_stack_p10 + 0x8C)) & (1)) != 0) goto loc_0084F87C;
    result = HvpReleaseCellPaged(v_stack_p10, v_stack_m70, v_stack_m88, Arg4);
loc_0084F5ED:
loc_0084F5F7:
    v_stack_m68 = (uint32_t)((uint32_t)((uint32_t)(local_r15)));
    if (((uint32_t)((uint32_t)((uint32_t)(local_r15)))) >= v_stack_m78) goto loc_0084F88D;
    result = 0;
    v_stack_m88 = 0;
    result = (uint8_t)((*(uint8_t *)(v_stack_p10 + 0x8C)) & (1));
    if (((uint32_t)((uint32_t)((uint32_t)(local_r15)))) >= ((uint32_t)((uint32_t)(v_stack_m80)))) goto loc_0084F84C;
    if ((uint8_t)(result) == 0) goto loc_0084F74E;
    result = HvpGetCellFlat(v_stack_p10, (uint32_t)(v_stack_m50), v_stack_m60, Arg4);
loc_0084F634:
    if (result == 0) goto loc_0084F82A;
    result = CmpDoFindSubKeyByNumber(v_stack_p10, result, (uint32_t)(v_stack_m68), Arg4);
loc_0084F650:
    *(uint32_t *)(v_stack_p20) = (uint32_t)(result);
    if (((*(uint8_t *)(v_stack_p10 + 0x8C)) & (1)) != 0) goto loc_0084F816;
    result = HvpReleaseCellPaged(v_stack_p10, v_stack_m60, (uint32_t)(v_stack_m68), Arg4);
loc_0084F668:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20)))) == -1) goto loc_0084F82A;
    v_stack_p20 = v_stack_m88;
    result = CmpFindSubkeyInHashByChildCell(Arg5, Arg6, v_stack_p10, (uint32_t)(*(uint32_t *)(v_stack_p20)));
    if (sign_flag) goto loc_0084F3E6;
    if (v_stack_m88 != 0) goto loc_0084F758;
loc_0084F6A6:
loc_0084F6A9:
    if (v_stack_p8 == ((uint32_t)(local_r13 + 1))) goto loc_0084F2CD;
    if (v_stack_m88 == 0) goto loc_0084F744;
loc_0084F6C6:
    if ((*(uint64_t *)(v_stack_m88)) > 1) goto loc_0084F705;
    if ((*(uint64_t *)(v_stack_m88 + 0xE0)) != (v_stack_m88 + 224)) goto loc_0084F785;
    if ((*(uint64_t *)(*(uint64_t *)(arg8 + 0x8))) != Arg8) goto loc_0084F493;
    *(void **)(v_stack_m88 + 0xE0) = Arg8;
    *(uint64_t *)(v_stack_m88 + 0xE0 + 0x8) = *(uint64_t *)(arg8 + 0x8);
    *(uint64_t *)(*(uint64_t *)(arg8 + 0x8)) = v_stack_m88 + 224;
    *(uint64_t *)(arg8 + 0x8) = v_stack_m88 + 224;
    goto loc_0084F744;
loc_0084F705:
    if ((*(uint64_t *)(arg8 + 0x8) - 1) == 2) goto loc_0084F7B9;
loc_0084F717:
    local_r10 = 0;
loc_0084F71A:
    if ((*(uint64_t *)(arg8 + 0x8)) != (*(uint64_t *)(arg8 + 0x8) - 1 + 1)) goto loc_0084F6C6;
    if ((*(uint64_t *)(arg8 + 0x8)) < (*(uint64_t *)(arg8 + 0x8) - 1)) goto loc_0084F79F;
    result = *(uint64_t *)(arg8 + 0x8) - 1 + 1;
    if (0 != 0) {
        Arg1 = *(uint64_t *)(v_stack_m88 + 0x20);
        result = CmpDoQueueLateUnloadWorker(Arg1, *(uint64_t *)(arg8 + 0x8) - 1, *(uint64_t *)(v_stack_m88 + 0x20), v_stack_m88);
    }
loc_0084F744:
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m68)) + 1);
    goto loc_0084F5F7;
loc_0084F74E:
    result = HvpGetCellPaged(Arg1, *(uint64_t *)(arg8 + 0x8) - 1, *(uint64_t *)(v_stack_m88 + 0x20), v_stack_m88);
    goto loc_0084F634;
loc_0084F758:
    result = CmRmIsKCBVisible(v_stack_m88, Arg7, *(uint64_t *)(v_stack_m88 + 0x20), v_stack_m88);
    if ((uint8_t)(result) == 0) goto loc_0084F6A9;
    result = CmpIsKeyDeleted(v_stack_m88, Arg7, *(uint64_t *)(v_stack_m88 + 0x20), v_stack_m88);
    if ((uint8_t)(result) == 0) goto loc_0084F6A6;
    goto loc_0084F6A9;
loc_0084F785:
    result = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(result + 81, result + 52, v_stack_m88, result + 1);
loc_0084F79F:
    result = 0;
    Arg4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(result + 81, result + 37, v_stack_m88, Arg4);
loc_0084F7B9:
    if (((*(uint32_t *)(Arg4 + 0xB8)) & (0x40000ULL)) == 0) goto loc_0084F717;
    if ((*(uint8_t *)(v_stack_m88 + 0xB80)) != 1) goto loc_0084F717;
    goto loc_0084F71A;
loc_0084F7E0:
    goto loc_0084F4BF;
loc_0084F7EA:
    goto loc_0084F2AA;
loc_0084F7F4:
    *(uint64_t *)(result) = result + 37;
    *(uint64_t *)(result + 0x8) = result + 81;
    *(uint64_t *)(result + 0x51) = result;
    *(uint64_t *)(result + 0x25 + 0x8) = result;
    goto loc_0084F3C8;
loc_0084F80C:
    result = HvpReleaseCellFlat(result + 81, result + 37, v_stack_m88, Arg4);
    goto loc_0084F2AA;
loc_0084F816:
    result = HvpReleaseCellFlat(result + 81, result + 37, v_stack_m88, Arg4);
    goto loc_0084F668;
loc_0084F820:
    result = HvpReleaseCellFlat(result + 81, result + 37, v_stack_m88, Arg4);
    goto loc_0084F392;
loc_0084F82A:
    goto loc_0084F3E6;
loc_0084F835:
    v_stack_m48 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r15 + 0x20)));
    goto loc_0084F5CE;
loc_0084F840:
    v_stack_m50 = 0xFFFFFFFFULL;
    goto loc_0084F5BC;
loc_0084F84C:
    if ((uint8_t)(result) == 0) goto loc_0084F886;
    result = HvpGetCellFlat(result + 81, (uint32_t)(v_stack_m48), v_stack_m58, Arg4);
loc_0084F85C:
    if (result == 0) goto loc_0084F82A;
    Arg3 = (uint32_t)(((uint32_t)(v_stack_m68)) - ((uint32_t)(v_stack_m88)));
    result = CmpDoFindSubKeyByNumber(v_stack_p10, result, Arg3, Arg4);
    goto loc_0084F650;
loc_0084F87C:
    result = HvpReleaseCellFlat(v_stack_p10, v_stack_m58, Arg3, Arg4);
    goto loc_0084F5ED;
loc_0084F886:
    result = HvpGetCellPaged(v_stack_p10, v_stack_m58, Arg3, Arg4);
    goto loc_0084F85C;
loc_0084F88D:
    if (condition_is_not_equal) goto loc_0084F2CD;
    local_r11 = 0;
    result = (Arg5) + (208);
    v_stack_m48 = 0;
    v_stack_m68 = result;
    *(uint32_t *)(v_stack_p20) = 0xFFFFFFFFULL;
loc_0084F8B0:
    result = CmListGetNextElement(result, v_stack_m48, 32, Arg4);
    v_stack_m50 = result;
    if (result == 0) goto loc_0084F2D0;
    result = CmEqualTrans(*(uint64_t *)(result + 0x38), Arg7, 32, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0084F8EA;
    if ((*(uint32_t *)(v_stack_m50 + 0x44)) == 1) goto loc_0084F8FA;
loc_0084F8EA:
    local_r11 = 0;
    v_stack_m88 = 0;
    goto loc_0084F8B0;
loc_0084F8FA:
    v_stack_m88 = *(uint64_t *)(0 + 0x58);
    result = CmRmIsKCBVisible(*(uint64_t *)(0 + 0x58), Arg7, 32, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0084F8EA;
    result = CmpIsKeyDeleted(*(uint64_t *)(0 + 0x58), Arg7, 32, Arg4);
    if ((uint8_t)(result) != 0) goto loc_0084F8EA;
    if (((uint32_t)((uint32_t)(v_stack_p8))) == ((uint32_t)(local_r13))) goto loc_0084F931;
    result = (uint32_t)(((uint32_t)(v_stack_p8)) + 1);
    v_stack_p8 = (uint32_t)(result);
    goto loc_0084F8EA;
loc_0084F931:
    *(uint32_t *)(v_stack_p20) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(0 + 0x58) + 0x28)));
    result = CmpReferenceKeyControlBlock(*(uint64_t *)(0 + 0x58), Arg7, 32, Arg4);
    goto loc_0084F2CD;
loc_0084F944:
loc_0084F94A:
    goto loc_0084F2CD;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8C` | `8` | `R` |
| `Arg1` | `+ 0xD8` | `32` | `R` |
| `Arg8` | `+ 0x8` | `64` | `R` |
| `Arg8` | `+ 0x8` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0084F1A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
