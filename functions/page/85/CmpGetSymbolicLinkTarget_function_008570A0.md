# CmpGetSymbolicLinkTarget

- RVA: `0x008570A0`–`0x00857864` (길이 `1,988` bytes)
- VA: `0x00000001408570A0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0006A5EC`
- 디코드: `489`개 명령, `1,988/1,988` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **29**; 고유 호출 대상: **21**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00857156` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x0085716D` → [HvpGetCellContextInitialize](HvpGetCellContextInitialize_function_00855F10.md) (function, `0x00855F10`)
- `0x00857187` → [HvpGetCellContextInitialize](HvpGetCellContextInitialize_function_00855F10.md) (function, `0x00855F10`)
- `0x0085719D` → [HvpGetCellContextInitialize](HvpGetCellContextInitialize_function_00855F10.md) (function, `0x00855F10`)
- `0x008571AE` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0085726E` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x008572A3` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x008572BC` → [CmpLockKcbShared](../../pagecmrc/BC/CmpLockKcbShared_function_00BC9A1C.md) (function, `0x00BC9A1C`)
- `0x00857319` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00857345` → [RtlUnicodeStringValidateWorker](../../text/3D/RtlUnicodeStringValidateWorker_function_003D41F8.md) (function, `0x003D41F8`)
- `0x0085735B` → [RtlUnicodeStringValidateWorker](../../text/3D/RtlUnicodeStringValidateWorker_function_003D41F8.md) (function, `0x003D41F8`)
- `0x008574CF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008574E3` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x008574F0` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x00857554` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00857582` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x008575B3` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)
- `0x008575C4` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00857636` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00857664` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (function, `0x00BC98E0`)
- `0x00857691` → [CmpGetKcbAtLayerHeight](../94/CmpGetKcbAtLayerHeight_function_00949210.md) (function, `0x00949210`)
- `0x008576E0` → [CmEqualTrans](../84/CmEqualTrans_function_0084BF60.md) (function, `0x0084BF60`)
- `0x0085770A` → [HvpGetCellFlat](HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00857731` → [CmpFindNameInListWithStatus](../84/CmpFindNameInListWithStatus_function_00846B80.md) (function, `0x00846B80`)
- `0x0085774D` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00857786` → [HvpGetCellFlat](HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x008577CF` → [CmpGetValueData](CmpGetValueData_function_00856DB0.md) (function, `0x00856DB0`)
- `0x0085781D` → [CmpGetComponentNameAtIndex](../9A/CmpGetComponentNameAtIndex_function_009A7A50.md) (function, `0x009A7A50`)
- `0x0085784C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)

### Direct callers
- [CmpDoParseKey](CmpDoParseKey_function_0085F750.md) at `0x00860331`
- [CmpDoParseKey](CmpDoParseKey_function_0085F750.md) at `0x00860F11`
- [sub_00B16F66](../B1/Unknown_function_00B16F66.md) at `0x00B172D9`

### Static image references
- `0x008570BF` → RVA `0x00E0A740` (`.data`; read)
- `0x00857723` → RVA `0x00FD9C00` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **16**
  - `0x00857156` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x008571AE` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0085726E` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x008572A3` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x008572BC` → [CmpLockKcbShared](../../pagecmrc/BC/CmpLockKcbShared_function_00BC9A1C.md) (`PAGE` → `PAGECMRC`)
  - `0x00857319` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00857345` → [RtlUnicodeStringValidateWorker](../../text/3D/RtlUnicodeStringValidateWorker_function_003D41F8.md) (`PAGE` → `.text`)
  - `0x0085735B` → [RtlUnicodeStringValidateWorker](../../text/3D/RtlUnicodeStringValidateWorker_function_003D41F8.md) (`PAGE` → `.text`)
  - `0x008574CF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008574E3` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x008574F0` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x00857582` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x008575B3` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (`PAGE` → `.text`)
  - `0x008575C4` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00857664` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (`PAGE` → `PAGECMRC`)
  - `0x0085784C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **28**
  - `0x00857224` → [sub_00857F80](Unknown_function_00857F80.md) (`tail-transfer`)
  - `0x0085722D` → [sub_00857DDE + 0x1F](Unknown_function_00857DDE.md) (`tail-transfer`)
  - `0x00857235` → [sub_00857DDE + 0x1F](Unknown_function_00857DDE.md) (`tail-transfer`)
  - `0x0085724E` → [sub_00857959](Unknown_function_00857959.md) (`tail-transfer`)
  - `0x00857329` → [sub_00857959 + 0x5B](Unknown_function_00857959.md) (`tail-transfer`)
  - `0x00857455` → [sub_00857F80 + 0xB](Unknown_function_00857F80.md) (`tail-transfer`)
  - `0x00857522` → [sub_00858022](Unknown_function_00858022.md) (`tail-transfer`)
  - `0x00857533` → [sub_00857E6F](Unknown_function_00857E6F.md) (`tail-transfer`)
  - `0x0085755C` → [sub_00858022 + 0xF](Unknown_function_00858022.md) (`tail-transfer`)
  - `0x00857565` → [sub_00858022 + 0x1E](Unknown_function_00858022.md) (`tail-transfer`)
  - `0x00857573` → [sub_00858022 + 0x2C](Unknown_function_00858022.md) (`tail-transfer`)
  - `0x008575AD` → [sub_00857959 + 0x1D](Unknown_function_00857959.md) (`tail-transfer`)
  - `0x00857684` → [sub_00857A2A](Unknown_function_00857A2A.md) (`tail-transfer`)
  - `0x008576C6` → [sub_00857EB2](Unknown_function_00857EB2.md) (`tail-transfer`)
  - `0x008576D0` → [sub_00857DDE](Unknown_function_00857DDE.md) (`tail-transfer`)
  - `0x008576E7` → [sub_00857F80 + 0x22](Unknown_function_00857F80.md) (`tail-transfer`)
  - `0x00857704` → [sub_00857DDE + 0x15](Unknown_function_00857DDE.md) (`tail-transfer`)
  - `0x00857747` → [sub_00857EE7](Unknown_function_00857EE7.md) (`tail-transfer`)
  - `0x00857754` → [sub_00857EB2 + 0xD](Unknown_function_00857EB2.md) (`tail-transfer`)
  - `0x00857768` → [sub_00857EB2](Unknown_function_00857EB2.md) (`tail-transfer`)
  - `0x00857780` → [sub_00857CA1](Unknown_function_00857CA1.md) (`tail-transfer`)
  - `0x00857797` → [sub_00857F1D + 0xC](Unknown_function_00857F1D.md) (`tail-transfer`)
  - `0x008577A1` → [sub_00857F80 + 0x47](Unknown_function_00857F80.md) (`tail-transfer`)
  - `0x008577D6` → [sub_00857F80 + 0x54](Unknown_function_00857F80.md) (`tail-transfer`)
  - `0x008577E6` → [sub_00857F80 + 0x61](Unknown_function_00857F80.md) (`tail-transfer`)
  - `0x008577EF` → [sub_00857F80 + 0x6E](Unknown_function_00857F80.md) (`tail-transfer`)
  - `0x00857839` → [sub_00857DDE + 0x8](Unknown_function_00857DDE.md) (`tail-transfer`)
  - `0x0085785C` → [sub_00857F80 + 0x7B](Unknown_function_00857F80.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008570A0  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
008570A5  55                              push rbp
008570A6  56                              push rsi
008570A7  57                              push rdi
008570A8  41 54                           push r12
008570AA  41 55                           push r13
008570AC  41 56                           push r14
008570AE  41 57                           push r15
008570B0  48 8D AC 24 00 FF FF FF         lea rbp, [rsp - 0x100]
008570B8  48 81 EC 00 02 00 00            sub rsp, 0x200
008570BF  48 8B 05 7A 36 5B 00            mov rax, qword ptr [rip + 0x5b367a]
008570C6  48 33 C4                        xor rax, rsp
008570C9  48 89 85 E0 00 00 00            mov qword ptr [rbp + 0xe0], rax
008570D0  48 8B 85 70 01 00 00            mov rax, qword ptr [rbp + 0x170]
008570D7  45 33 F6                        xor r14d, r14d
008570DA  4C 8B A5 60 01 00 00            mov r12, qword ptr [rbp + 0x160]
008570E1  0F 57 C0                        xorps xmm0, xmm0
008570E4  48 8B 9D 68 01 00 00            mov rbx, qword ptr [rbp + 0x168]
008570EB  48 8B F9                        mov rdi, rcx
008570EE  48 89 45 08                     mov qword ptr [rbp + 8], rax
008570F2  48 8B 85 78 01 00 00            mov rax, qword ptr [rbp + 0x178]
008570F9  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
008570FD  48 8B 85 80 01 00 00            mov rax, qword ptr [rbp + 0x180]
00857104  48 89 45 F8                     mov qword ptr [rbp - 8], rax
00857108  48 8B 85 88 01 00 00            mov rax, qword ptr [rbp + 0x188]
0085710F  45 0F BF E9                     movsx r13d, r9w
00857113  41 0F BF F0                     movsx esi, r8w
00857117  48 89 55 D0                     mov qword ptr [rbp - 0x30], rdx
0085711B  33 D2                           xor edx, edx
0085711D  48 89 4D B0                     mov qword ptr [rbp - 0x50], rcx
00857121  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00857126  48 89 45 00                     mov qword ptr [rbp], rax
0085712A  66 44 89 6D B8                  mov word ptr [rbp - 0x48], r13w
0085712F  66 89 74 24 60                  mov word ptr [rsp + 0x60], si
00857134  0F 11 44 24 50                  movups xmmword ptr [rsp + 0x50], xmm0
00857139  4C 89 74 24 78                  mov qword ptr [rsp + 0x78], r14
0085713E  0F 11 45 A0                     movups xmmword ptr [rbp - 0x60], xmm0
00857142  4C 89 75 90                     mov qword ptr [rbp - 0x70], r14
00857146  4C 89 75 C8                     mov qword ptr [rbp - 0x38], r14
0085714A  66 44 89 74 24 70               mov word ptr [rsp + 0x70], r14w
00857150  66 44 89 74 24 74               mov word ptr [rsp + 0x74], r14w
00857156  E8 25 36 BD FF                  call 0x14042a780
0085715B  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
00857160  4C 89 74 24 48                  mov qword ptr [rsp + 0x48], r14
00857165  45 32 FF                        xor r15b, r15b
00857168  44 88 74 24 41                  mov byte ptr [rsp + 0x41], r14b
0085716D  E8 9E ED FF FF                  call 0x140855f10
00857172  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00857176  4C 89 74 24 68                  mov qword ptr [rsp + 0x68], r14
0085717B  C7 44 24 44 FF FF FF FF         mov dword ptr [rsp + 0x44], 0xffffffff
00857183  4C 89 75 D8                     mov qword ptr [rbp - 0x28], r14
00857187  E8 84 ED FF FF                  call 0x140855f10
0085718C  48 8D 4D C8                     lea rcx, [rbp - 0x38]
00857190  4C 89 75 C0                     mov qword ptr [rbp - 0x40], r14
00857194  44 88 74 24 42                  mov byte ptr [rsp + 0x42], r14b
00857199  44 89 75 80                     mov dword ptr [rbp - 0x80], r14d
0085719D  E8 6E ED FF FF                  call 0x140855f10
008571A2  48 8D 4D 30                     lea rcx, [rbp + 0x30]
008571A6  33 D2                           xor edx, edx
008571A8  41 B8 A8 00 00 00               mov r8d, 0xa8
008571AE  E8 8D FA E6 FF                  call 0x1406c6c40
008571B3  0F 57 C0                        xorps xmm0, xmm0
008571B6  B8 FF FF FF FF                  mov eax, 0xffffffff
008571BB  0F 11 45 10                     movups xmmword ptr [rbp + 0x10], xmm0
008571BF  66 89 45 12                     mov word ptr [rbp + 0x12], ax
008571C3  0F 11 45 20                     movups xmmword ptr [rbp + 0x20], xmm0
008571C7  4D 85 E4                        test r12, r12
008571CA  75 10                           jne 0x1408571dc
008571CC  66 44 39 77 02                  cmp word ptr [rdi + 2], r14w
008571D1  75 09                           jne 0x1408571dc
008571D3  0F B7 47 02                     movzx eax, word ptr [rdi + 2]
008571D7  41 B6 01                        mov r14b, 1
008571DA  EB 0E                           jmp 0x1408571ea
008571DC  48 0F BF 47 02                  movsx rax, word ptr [rdi + 2]
008571E1  83 F8 02                        cmp eax, 2
008571E4  0F 8D 56 04 00 00               jge 0x140857640
008571EA  0F AE E8                        lfence
008571ED  48 0F BF C0                     movsx rax, ax
008571F1  48 8B 4C C7 08                  mov rcx, qword ptr [rdi + rax*8 + 8]
008571F6  48 89 4D 88                     mov qword ptr [rbp - 0x78], rcx
008571FA  45 84 F6                        test r14b, r14b
008571FD  0F 84 50 04 00 00               je 0x140857653
00857203  8B 41 08                        mov eax, dword ptr [rcx + 8]
00857206  A8 08                           test al, 8
00857208  0F 84 45 04 00 00               je 0x140857653
0085720E  48 8B 41 68                     mov rax, qword ptr [rcx + 0x68]
00857212  32 C9                           xor cl, cl
00857214  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00857219  48 8B B8 28 01 00 00            mov rdi, qword ptr [rax + 0x128]
00857220  40 F6 C7 01                     test dil, 1
00857224  0F 85 56 0D 00 00               jne 0x140857f80
0085722A  48 85 FF                        test rdi, rdi
0085722D  0F 84 CA 0B 00 00               je 0x140857dfd
00857233  84 C9                           test cl, cl
00857235  0F 85 C2 0B 00 00               jne 0x140857dfd
0085723B  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00857240  B9 01 00 00 00                  mov ecx, 1
00857245  F0 48 0F C1 08                  lock xadd qword ptr [rax], rcx
0085724A  48 83 C1 01                     add rcx, 1
0085724E  0F 84 05 07 00 00               je 0x140857959
00857254  48 83 F9 01                     cmp rcx, 1
00857258  75 1A                           jne 0x140857274
0085725A  8D 51 14                        lea edx, [rcx + 0x14]
0085725D  45 33 ED                        xor r13d, r13d
00857260  8D 4A 3C                        lea ecx, [rdx + 0x3c]
00857263  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00857268  45 33 C9                        xor r9d, r9d
0085726B  45 33 C0                        xor r8d, r8d
0085726E  E8 ED 63 CA FF                  call 0x1404fd660
00857273  CC                              int3
00857274  4C 8B 75 B0                     mov r14, qword ptr [rbp - 0x50]
00857278  33 C0                           xor eax, eax
0085727A  0F B7 D8                        movzx ebx, ax
0085727D  66 41 3B 46 02                  cmp ax, word ptr [r14 + 2]
00857282  7F 2E                           jg 0x1408572b2
00857284  0F 1F 40 00                     nop dword ptr [rax]
00857288  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
00857290  48 0F BF CB                     movsx rcx, bx
00857294  66 83 FB 02                     cmp bx, 2
00857298  0F 8D 7A 03 00 00               jge 0x140857618
0085729E  49 8B 4C CE 08                  mov rcx, qword ptr [r14 + rcx*8 + 8]
008572A3  E8 18 20 37 00                  call 0x140bc92c0
008572A8  66 FF C3                        inc bx
008572AB  66 41 3B 5E 02                  cmp bx, word ptr [r14 + 2]
008572B0  7E DE                           jle 0x140857290
008572B2  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
008572B7  44 88 7C 24 40                  mov byte ptr [rsp + 0x40], r15b
008572BC  E8 5B 27 37 00                  call 0x140bc9a1c
008572C1  44 0F B7 27                     movzx r12d, word ptr [rdi]
008572C5  41 B7 01                        mov r15b, 1
008572C8  45 8B F5                        mov r14d, r13d
008572CB  8B CE                           mov ecx, esi
008572CD  41 3B F5                        cmp esi, r13d
008572D0  73 2B                           jae 0x1408572fd
008572D2  48 8B 55 D0                     mov rdx, qword ptr [rbp - 0x30]
008572D6  83 F9 08                        cmp ecx, 8
008572D9  0F 83 22 03 00 00               jae 0x140857601
008572DF  8B C1                           mov eax, ecx
008572E1  48 83 C0 02                     add rax, 2
008572E5  48 C1 E0 04                     shl rax, 4
008572E9  48 03 C2                        add rax, rdx
008572EC  0F B7 00                        movzx eax, word ptr [rax]
008572EF  41 83 C4 02                     add r12d, 2
008572F3  44 03 E0                        add r12d, eax
008572F6  FF C1                           inc ecx
008572F8  41 3B CD                        cmp ecx, r13d
008572FB  72 D9                           jb 0x1408572d6
008572FD  BE FF FF 00 00                  mov esi, 0xffff
00857302  44 3B E6                        cmp r12d, esi
00857305  0F 87 1B 03 00 00               ja 0x140857626
0085730B  41 8B D4                        mov edx, r12d
0085730E  B9 00 01 00 00                  mov ecx, 0x100
00857313  41 B8 43 4D 36 36               mov r8d, 0x36364d43
00857319  E8 D2 AD 32 00                  call 0x140b820f0
0085731E  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00857323  48 8B D8                        mov rbx, rax
00857326  48 85 C0                        test rax, rax
00857329  0F 84 85 06 00 00               je 0x1408579b4
0085732F  33 F6                           xor esi, esi
00857331  66 44 89 64 24 52               mov word ptr [rsp + 0x52], r12w
00857337  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
0085733C  66 89 74 24 50                  mov word ptr [rsp + 0x50], si
00857341  44 0F B7 D6                     movzx r10d, si
00857345  E8 AE CE B7 FF                  call 0x1403d41f8
0085734A  85 C0                           test eax, eax
0085734C  78 5F                           js 0x1408573ad
0085734E  45 0F B7 DC                     movzx r11d, r12w
00857352  48 8B CF                        mov rcx, rdi
00857355  49 D1 EB                        shr r11, 1
00857358  44 8B D6                        mov r10d, esi
0085735B  E8 98 CE B7 FF                  call 0x1403d41f8
00857360  85 C0                           test eax, eax
00857362  78 3C                           js 0x1408573a0
00857364  0F B7 07                        movzx eax, word ptr [rdi]
00857367  48 8B 57 08                     mov rdx, qword ptr [rdi + 8]
0085736B  48 D1 E8                        shr rax, 1
0085736E  4D 85 DB                        test r11, r11
00857371  74 2D                           je 0x1408573a0
00857373  4C 8B C3                        mov r8, rbx
00857376  4C 2B C2                        sub r8, rdx
00857379  4C 2B D8                        sub r11, rax
0085737C  0F 1F 40 00                     nop dword ptr [rax]
00857380  48 85 C0                        test rax, rax
00857383  74 1B                           je 0x1408573a0
00857385  0F B7 0A                        movzx ecx, word ptr [rdx]
00857388  48 FF C8                        dec rax
0085738B  66 41 89 0C 10                  mov word ptr [r8 + rdx], cx
00857390  49 FF C2                        inc r10
00857393  48 83 C2 02                     add rdx, 2
00857397  49 8D 0C 03                     lea rcx, [r11 + rax]
0085739B  48 85 C9                        test rcx, rcx
0085739E  75 E0                           jne 0x140857380
008573A0  66 45 03 D2                     add r10w, r10w
008573A4  45 8B F5                        mov r14d, r13d
008573A7  66 44 89 54 24 50               mov word ptr [rsp + 0x50], r10w
008573AD  44 0F BF 5C 24 60               movsx r11d, word ptr [rsp + 0x60]
008573B3  45 3B DE                        cmp r11d, r14d
008573B6  0F 83 04 01 00 00               jae 0x1408574c0
008573BC  4C 8B 7D 88                     mov r15, qword ptr [rbp - 0x78]
008573C0  BF FE FF 00 00                  mov edi, 0xfffe
008573C5  45 33 ED                        xor r13d, r13d
008573C8  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
008573D0  41 83 FB 08                     cmp r11d, 8
008573D4  0F 83 0B 02 00 00               jae 0x1408575e5
008573DA  41 8B CB                        mov ecx, r11d
008573DD  48 83 C1 02                     add rcx, 2
008573E1  48 C1 E1 04                     shl rcx, 4
008573E5  48 03 4D D0                     add rcx, qword ptr [rbp - 0x30]
008573E9  41 0F B7 C2                     movzx eax, r10w
008573ED  66 41 83 C2 02                  add r10w, 2
008573F2  48 D1 E8                        shr rax, 1
008573F5  66 44 89 54 24 50               mov word ptr [rsp + 0x50], r10w
008573FB  66 C7 04 43 5C 00               mov word ptr [rbx + rax*2], 0x5c
00857401  41 F6 C2 01                     test r10b, 1
00857405  0F 85 A5 00 00 00               jne 0x1408574b0
0085740B  41 F6 C4 01                     test r12b, 1
0085740F  0F 85 9B 00 00 00               jne 0x1408574b0
00857415  66 44 3B E7                     cmp r12w, di
00857419  0F 87 91 00 00 00               ja 0x1408574b0
0085741F  66 45 3B D4                     cmp r10w, r12w
00857423  0F 87 87 00 00 00               ja 0x1408574b0
00857429  0F B7 11                        movzx edx, word ptr [rcx]
0085742C  45 0F B7 C4                     movzx r8d, r12w
00857430  41 0F B7 DA                     movzx ebx, r10w
00857434  49 D1 E8                        shr r8, 1
00857437  48 D1 EB                        shr rbx, 1
0085743A  F6 C2 01                        test dl, 1
0085743D  75 6C                           jne 0x1408574ab
0085743F  0F B7 41 02                     movzx eax, word ptr [rcx + 2]
00857443  A8 01                           test al, 1
00857445  75 64                           jne 0x1408574ab
00857447  66 3B C7                        cmp ax, di
0085744A  77 5F                           ja 0x1408574ab
0085744C  66 3B D0                        cmp dx, ax
0085744F  77 5A                           ja 0x1408574ab
00857451  48 39 71 08                     cmp qword ptr [rcx + 8], rsi
00857455  0F 84 30 0B 00 00               je 0x140857f8b
0085745B  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
0085745F  4D 8B D5                        mov r10, r13
00857462  48 D1 EA                        shr rdx, 1
00857465  4C 2B C3                        sub r8, rbx
00857468  74 33                           je 0x14085749d
0085746A  4C 8B 4C 24 58                  mov r9, qword ptr [rsp + 0x58]
0085746F  48 8D 04 1B                     lea rax, [rbx + rbx]
00857473  48 2B C1                        sub rax, rcx
00857476  4C 03 C8                        add r9, rax
00857479  0F 1F 80 00 00 00 00            nop dword ptr [rax]
00857480  48 85 D2                        test rdx, rdx
00857483  74 18                           je 0x14085749d
00857485  0F B7 01                        movzx eax, word ptr [rcx]
00857488  48 FF CA                        dec rdx
0085748B  66 41 89 04 09                  mov word ptr [r9 + rcx], ax
00857490  49 FF C2                        inc r10
00857493  48 83 C1 02                     add rcx, 2
00857497  49 83 E8 01                     sub r8, 1
0085749B  75 E3                           jne 0x140857480
0085749D  66 44 03 D3                     add r10w, bx
008574A1  66 45 03 D2                     add r10w, r10w
008574A5  66 44 89 54 24 50               mov word ptr [rsp + 0x50], r10w
008574AB  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
008574B0  41 FF C3                        inc r11d
008574B3  45 3B DE                        cmp r11d, r14d
008574B6  0F 82 14 FF FF FF               jb 0x1408573d0
008574BC  4C 89 7D 88                     mov qword ptr [rbp - 0x78], r15
008574C0  48 8B 5D F0                     mov rbx, qword ptr [rbp - 0x10]
008574C4  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
008574C8  48 85 C9                        test rcx, rcx
008574CB  74 07                           je 0x1408574d4
008574CD  33 D2                           xor edx, edx
008574CF  E8 9C B3 32 00                  call 0x140b82870
008574D4  0F 28 44 24 50                  movaps xmm0, xmmword ptr [rsp + 0x50]
008574D9  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
008574DE  33 D2                           xor edx, edx
008574E0  0F 11 03                        movups xmmword ptr [rbx], xmm0
008574E3  E8 98 32 BD FF                  call 0x14042a780
008574E8  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
008574ED  48 8B CB                        mov rcx, rbx
008574F0  E8 CB 1D 37 00                  call 0x140bc92c0
008574F5  48 8B 4D 00                     mov rcx, qword ptr [rbp]
008574F9  45 32 FF                        xor r15b, r15b
008574FC  48 8B 45 F8                     mov rax, qword ptr [rbp - 8]
00857500  8B FE                           mov edi, esi
00857502  48 8B 55 88                     mov rdx, qword ptr [rbp - 0x78]
00857506  45 0F B6 F7                     movzx r14d, r15b
0085750A  48 89 74 24 48                  mov qword ptr [rsp + 0x48], rsi
0085750F  48 89 11                        mov qword ptr [rcx], rdx
00857512  48 89 18                        mov qword ptr [rax], rbx
00857515  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
0085751A  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
0085751F  48 85 DB                        test rbx, rbx
00857522  0F 85 FA 0A 00 00               jne 0x140858022
00857528  4C 8B 65 D8                     mov r12, qword ptr [rbp - 0x28]
0085752C  48 8B 4D C0                     mov rcx, qword ptr [rbp - 0x40]
00857530  48 85 C9                        test rcx, rcx
00857533  0F 85 36 09 00 00               jne 0x140857e6f
00857539  48 85 F6                        test rsi, rsi
0085753C  74 1B                           je 0x140857559
0085753E  41 F6 84 24 8C 00 00 00 01      test byte ptr [r12 + 0x8c], 1
00857547  48 8D 55 90                     lea rdx, [rbp - 0x70]
0085754B  49 8B CC                        mov rcx, r12
0085754E  0F 85 E2 00 00 00               jne 0x140857636
00857554  E8 E7 E9 FF FF                  call 0x140855f40
00857559  48 85 DB                        test rbx, rbx
0085755C  0F 85 CF 0A 00 00               jne 0x140858031
00857562  45 84 F6                        test r14b, r14b
00857565  0F 85 D5 0A 00 00               jne 0x140858040
0085756B  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
00857570  48 85 DB                        test rbx, rbx
00857573  0F 85 D5 0A 00 00               jne 0x14085804e
00857579  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0085757D  48 85 C9                        test rcx, rcx
00857580  74 05                           je 0x140857587
00857582  E8 F9 E7 C1 FF                  call 0x140475d80
00857587  48 8B 95 D0 00 00 00            mov rdx, qword ptr [rbp + 0xd0]
0085758E  48 85 D2                        test rdx, rdx
00857591  74 25                           je 0x1408575b8
00857593  65 4C 8B 04 25 20 00 00 00      mov r8, qword ptr gs:[0x20]
0085759C  49 8B 88 80 08 00 00            mov rcx, qword ptr [r8 + 0x880]
008575A3  FF 41 1C                        inc dword ptr [rcx + 0x1c]
008575A6  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
008575AA  66 39 01                        cmp word ptr [rcx], ax
008575AD  0F 83 C3 03 00 00               jae 0x140857976
008575B3  E8 F8 2F E6 FF                  call 0x1406ba5b0
008575B8  8B C7                           mov eax, edi
008575BA  48 8B 8D E0 00 00 00            mov rcx, qword ptr [rbp + 0xe0]
008575C1  48 33 CC                        xor rcx, rsp
008575C4  E8 77 50 E5 FF                  call 0x1406ac640
008575C9  48 8B 9C 24 58 02 00 00         mov rbx, qword ptr [rsp + 0x258]
008575D1  48 81 C4 00 02 00 00            add rsp, 0x200
008575D8  41 5F                           pop r15
008575DA  41 5E                           pop r14
008575DC  41 5D                           pop r13
008575DE  41 5C                           pop r12
008575E0  5F                              pop rdi
008575E1  5E                              pop rsi
008575E2  5D                              pop rbp
008575E3  C3                              ret
008575E4  CC                              int3
008575E5  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
008575E9  41 8D 4B F8                     lea ecx, [r11 - 8]
008575ED  48 83 C1 06                     add rcx, 6
008575F1  48 C1 E1 04                     shl rcx, 4
008575F5  48 03 88 A0 00 00 00            add rcx, qword ptr [rax + 0xa0]
008575FC  E9 E8 FD FF FF                  jmp 0x1408573e9
00857601  8D 41 F8                        lea eax, [rcx - 8]
00857604  48 83 C0 06                     add rax, 6
00857608  48 C1 E0 04                     shl rax, 4
0085760C  48 03 82 A0 00 00 00            add rax, qword ptr [rdx + 0xa0]
00857613  E9 D4 FC FF FF                  jmp 0x1408572ec
00857618  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
0085761C  48 8B 4C C8 F0                  mov rcx, qword ptr [rax + rcx*8 - 0x10]
00857621  E9 7D FC FF FF                  jmp 0x1408572a3
00857626  44 0F B6 74 24 40               movzx r14d, byte ptr [rsp + 0x40]
0085762C  BF 34 00 00 C0                  mov edi, 0xc0000034
00857631  E9 DF FE FF FF                  jmp 0x140857515
00857636  E8 E5 55 00 00                  call 0x14085cc20
0085763B  E9 19 FF FF FF                  jmp 0x140857559
00857640  0F AE E8                        lfence
00857643  48 8B C8                        mov rcx, rax
00857646  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
0085764A  48 8B 54 C8 F0                  mov rdx, qword ptr [rax + rcx*8 - 0x10]
0085764F  48 89 55 88                     mov qword ptr [rbp - 0x78], rdx
00857653  8B 83 A0 00 00 00               mov eax, dword ptr [rbx + 0xa0]
00857659  A8 01                           test al, 1
0085765B  75 13                           jne 0x140857670
0085765D  48 8D 8B A8 00 00 00            lea rcx, [rbx + 0xa8]
00857664  E8 77 22 37 00                  call 0x140bc98e0
00857669  83 8B A0 00 00 00 01            or dword ptr [rbx + 0xa0], 1
00857670  0F B7 77 02                     movzx esi, word ptr [rdi + 2]
00857674  33 C0                           xor eax, eax
00857676  44 8B C0                        mov r8d, eax
00857679  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
0085767D  8B 7C 24 44                     mov edi, dword ptr [rsp + 0x44]
00857681  66 85 F6                        test si, si
00857684  0F 88 A0 03 00 00               js 0x140857a2a
0085768A  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
0085768E  0F B7 D6                        movzx edx, si
00857691  E8 7A 1B 0F 00                  call 0x140949210
00857696  48 8B D8                        mov rbx, rax
00857699  4D 85 C0                        test r8, r8
0085769C  75 1D                           jne 0x1408576bb
0085769E  83 78 28 FF                     cmp dword ptr [rax + 0x28], -1
008576A2  75 10                           jne 0x1408576b4
008576A4  48 8B 40 20                     mov rax, qword ptr [rax + 0x20]
008576A8  F7 80 10 10 00 00 00 20 00 00   test dword ptr [rax + 0x1010], 0x2000
008576B2  75 07                           jne 0x1408576bb
008576B4  4C 8B C3                        mov r8, rbx
008576B7  48 89 5D E0                     mov qword ptr [rbp - 0x20], rbx
008576BB  66 83 7B 42 00                  cmp word ptr [rbx + 0x42], 0
008576C0  74 0A                           je 0x1408576cc
008576C2  80 7B 41 01                     cmp byte ptr [rbx + 0x41], 1
008576C6  0F 84 E6 07 00 00               je 0x140857eb2
008576CC  83 7B 28 FF                     cmp dword ptr [rbx + 0x28], -1
008576D0  0F 84 08 07 00 00               je 0x140857dde
008576D6  48 8B 8B 20 01 00 00            mov rcx, qword ptr [rbx + 0x120]
008576DD  49 8B D4                        mov rdx, r12
008576E0  E8 7B 48 FF FF                  call 0x14084bf60
008576E5  84 C0                           test al, al
008576E7  0F 85 B5 08 00 00               jne 0x140857fa2
008576ED  8B 53 28                        mov edx, dword ptr [rbx + 0x28]
008576F0  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
008576F5  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
008576F9  48 83 C3 20                     add rbx, 0x20
008576FD  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
00857704  0F 84 E9 06 00 00               je 0x140857df3
0085770A  E8 51 D5 FF FF                  call 0x140854c60
0085770F  48 8B 0B                        mov rcx, qword ptr [rbx]
00857712  48 8D 50 24                     lea rdx, [rax + 0x24]
00857716  48 8D 44 24 44                  lea rax, [rsp + 0x44]
0085771B  45 33 C9                        xor r9d, r9d
0085771E  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00857723  4C 8D 05 D6 24 78 00            lea r8, [rip + 0x7824d6]
0085772A  33 C0                           xor eax, eax
0085772C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00857731  E8 4A F4 FE FF                  call 0x140846b80
00857736  48 8B 0B                        mov rcx, qword ptr [rbx]
00857739  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
0085773E  8B F8                           mov edi, eax
00857740  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
00857747  0F 85 9A 07 00 00               jne 0x140857ee7
0085774D  E8 EE E7 FF FF                  call 0x140855f40
00857752  85 FF                           test edi, edi
00857754  0F 88 65 07 00 00               js 0x140857ebf
0085775A  4C 8B 23                        mov r12, qword ptr [rbx]
0085775D  8B 7C 24 44                     mov edi, dword ptr [rsp + 0x44]
00857761  4C 89 65 D8                     mov qword ptr [rbp - 0x28], r12
00857765  83 FF FF                        cmp edi, -1
00857768  0F 84 44 07 00 00               je 0x140857eb2
0085776E  41 F6 84 24 8C 00 00 00 01      test byte ptr [r12 + 0x8c], 1
00857777  4C 8D 45 90                     lea r8, [rbp - 0x70]
0085777B  8B D7                           mov edx, edi
0085777D  49 8B CC                        mov rcx, r12
00857780  0F 84 1B 05 00 00               je 0x140857ca1
00857786  E8 D5 D4 FF FF                  call 0x140854c60
0085778B  F6 40 10 02                     test byte ptr [rax + 0x10], 2
0085778F  48 8B F0                        mov rsi, rax
00857792  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00857797  0F 85 8C 07 00 00               jne 0x140857f29
0085779D  83 78 0C 06                     cmp dword ptr [rax + 0xc], 6
008577A1  0F 85 20 08 00 00               jne 0x140857fc7
008577A7  48 8D 45 C8                     lea rax, [rbp - 0x38]
008577AB  4C 8B C6                        mov r8, rsi
008577AE  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008577B3  4C 8D 4D 80                     lea r9, [rbp - 0x80]
008577B7  48 8D 44 24 42                  lea rax, [rsp + 0x42]
008577BC  8B D7                           mov edx, edi
008577BE  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008577C3  49 8B CC                        mov rcx, r12
008577C6  48 8D 45 C0                     lea rax, [rbp - 0x40]
008577CA  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008577CF  E8 DC F5 FF FF                  call 0x140856db0
008577D4  84 C0                           test al, al
008577D6  0F 84 F8 07 00 00               je 0x140857fd4
008577DC  8B 4D 80                        mov ecx, dword ptr [rbp - 0x80]
008577DF  BE FF FF 00 00                  mov esi, 0xffff
008577E4  3B CE                           cmp ecx, esi
008577E6  0F 87 F5 07 00 00               ja 0x140857fe1
008577EC  F6 C1 01                        test cl, 1
008577EF  0F 85 F9 07 00 00               jne 0x140857fee
008577F5  44 0F BF 44 24 60               movsx r8d, word ptr [rsp + 0x60]
008577FB  48 8B 45 C0                     mov rax, qword ptr [rbp - 0x40]
008577FF  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
00857803  66 89 4D A0                     mov word ptr [rbp - 0x60], cx
00857807  66 89 4D A2                     mov word ptr [rbp - 0x5e], cx
0085780B  0F B7 F9                        movzx edi, cx
0085780E  45 3B C5                        cmp r8d, r13d
00857811  73 24                           jae 0x140857837
00857813  48 8B 75 D0                     mov rsi, qword ptr [rbp - 0x30]
00857817  41 8B D0                        mov edx, r8d
0085781A  48 8B CE                        mov rcx, rsi
0085781D  E8 2E 02 15 00                  call 0x1409a7a50
00857822  83 C7 02                        add edi, 2
00857825  41 FF C0                        inc r8d
00857828  0F B7 08                        movzx ecx, word ptr [rax]
0085782B  03 F9                           add edi, ecx
0085782D  45 3B C5                        cmp r8d, r13d
00857830  72 E5                           jb 0x140857817
00857832  BE FF FF 00 00                  mov esi, 0xffff
00857837  3B FE                           cmp edi, esi
00857839  0F 87 A7 05 00 00               ja 0x140857de6
0085783F  8B D7                           mov edx, edi
00857841  B9 00 01 00 00                  mov ecx, 0x100
00857846  41 B8 43 4D 36 36               mov r8d, 0x36364d43
0085784C  E8 9F A8 32 00                  call 0x140b820f0
00857851  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00857856  48 8B D8                        mov rbx, rax
00857859  48 85 C0                        test rax, rax
0085785C  0F 84 99 07 00 00               je 0x140857ffb
00857862  33 DB                           xor ebx, ebx
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpGetSymbolicLinkTarget(__int64 a1, __int64 a2, unsigned __int16 a3, int a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int16 v_stack_m126;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int16 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int16 v_stack_m196;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned int v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int16 v_stack_m1C4;
    unsigned __int16 v_stack_m1C8;
    unsigned __int64 v_stack_m1D0;
    unsigned __int16 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned __int16 v_stack_m1E6;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned int v_stack_m1F4;
    unsigned __int8 v_stack_m1F6;
    unsigned __int8 v_stack_m1F7;
    unsigned __int8 v_stack_m1F8;
    unsigned __int64 v_stack_m218;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int8 v_stack_p40;
    unsigned __int64 v_stack_p42;
    unsigned int v_stack_p44;
    unsigned __int64 v_stack_p58;
    unsigned __int16 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p78;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (512);
    result = (*(unsigned __int64 *)(v_rip + 5977722)) ^ (v_rsp);
    v_stack_m58 = result;
    v_r14 = 0;
    v_stack_m130 = a7;
    v_stack_m148 = a8;
    v_stack_m140 = a9;
    v_stack_m168 = a2;
    a2 = 0;
    v_stack_m188 = a1;
    v_stack_m138 = a10;
    v_stack_m180 = (unsigned __int16)((__int16)((unsigned __int16)(a4)));
    v_stack_m1D8 = (unsigned __int16)((__int16)(a3));
    v_stack_m1E8 = v_xmm0;
    v_stack_m1C0 = 0;
    v_stack_m198 = v_xmm0;
    v_stack_m1A8 = 0;
    v_stack_m170 = 0;
    v_stack_m1C8 = 0;
    v_stack_m1C4 = 0;
    result = RtlInitUnicodeString(v_stack_m1E8, a2, a3, a4);
    v_stack_m1F0 = 0;
    v_r15 = 0;
    v_stack_m1F7 = 0;
    result = HvpGetCellContextInitialize(v_stack_m1C0, a2, a3, a4);
    v_stack_m1D0 = 0;
    v_stack_m1F4 = 0xFFFFFFFFULL;
    v_stack_m160 = 0;
    result = HvpGetCellContextInitialize(v_stack_m1A8, a2, a3, a4);
    v_stack_m178 = 0;
    v_stack_m1F6 = 0;
    v_stack_m1B8 = 0;
    result = HvpGetCellContextInitialize(v_stack_m170, a2, a3, a4);
    a2 = 0;
    result = memset(v_stack_m108, a2, 168, a4);
    v_stack_m128 = v_xmm0;
    v_stack_m126 = (unsigned __int16)((unsigned int)(0xFFFFFFFFULL));
    v_stack_m118 = v_xmm0;
    if (a5 != 0) goto loc_008571DC;
    if ((*(unsigned __int16 *)(a1 + 2)) != 0) goto loc_008571DC;
    goto loc_008571EA;
loc_008571DC:
    if (((unsigned int)((__int16)(*(unsigned __int16 *)(a1 + 2)))) >= 2) goto loc_00857640;
loc_008571EA:
    v_stack_m1B0 = *(unsigned __int64 *)(a1 + (__int16)((unsigned __int16)((__int16)(*(unsigned __int16 *)(a1 + 2)))) * 8 + 8);
    if (1 == 0) goto loc_00857653;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + (__int16)((unsigned __int16)((__int16)(*(unsigned __int16 *)(a1 + 2)))) * 8 + 8) + 8)))) & (8)) == 0) goto loc_00857653;
    a1 = 0;
    v_stack_m1F0 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + (__int16)((unsigned __int16)((__int16)(*(unsigned __int16 *)(a1 + 2)))) * 8 + 8) + 104);
    a1 = (1) + (1);
    result = v_stack_m1F0;
    v_r13 = (__int16)((unsigned __int16)(a4));
    if (a1 == 1) {
        a2 = a1 + 20;
        v_r13 = 0;
        a1 = a2 + 60;
        v_stack_m218 = 0;
        a4 = 0;
        a3 = 0;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = 0;
    if (0 > (*(unsigned __int16 *)(v_stack_m188 + 2))) goto loc_008572B2;
loc_00857290:
    if (0 >= 2) goto loc_00857618;
loc_008572A3:
    result = CmpUnlockKcb(*(unsigned __int64 *)(v_stack_m188 + (__int16)(0) * 8 + 8), a2, a3, a4);
    v_rbx = (unsigned __int16)((0) + 1);
    if (((unsigned __int16)(v_rbx)) <= (*(unsigned __int16 *)(v_stack_m188 + 2))) goto loc_00857290;
loc_008572B2:
    v_stack_m1F8 = 0;
    result = CmpLockKcbShared(v_stack_m1F0, a2, a3, a4);
    if (((unsigned int)((__int16)(a3))) >= 0) goto loc_008572FD;
loc_008572D6:
    if (((unsigned int)((unsigned int)((unsigned int)((__int16)(a3))))) >= 8) goto loc_00857601;
    result = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((__int16)(a3)))))) + (2);
    result = (result) << (4);
    result = (result) + (v_stack_m168);
loc_008572EC:
    v_r12 = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + (__int16)((unsigned __int16)((__int16)(*(unsigned __int16 *)(a1 + 2)))) * 8 + 8) + 104) + 296))) + (2));
    v_r12 = (unsigned int)((v_r12) + ((unsigned int)(*(unsigned __int16 *)(result))));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((__int16)(a3)))) + 1);
    if (((unsigned int)(a1)) < 0) goto loc_008572D6;
loc_008572FD:
    if (((unsigned int)(v_r12)) > ((unsigned int)((unsigned int)(0xFFFFULL)))) goto loc_00857626;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(v_r12)), (unsigned int)(0x36364D43ULL), a4);
    v_stack_m1E0 = result;
    v_rsi = 0;
    v_stack_m1E6 = (unsigned __int16)(v_r12);
    v_stack_m1E8 = 0;
    result = RtlUnicodeStringValidateWorker(v_stack_m1E8, (unsigned int)((unsigned int)(v_r12)), (unsigned int)(0x36364D43ULL), a4);
    if (sign_flag) goto loc_008573AD;
    v_r11 = ((unsigned __int16)(v_r12)) >> (1);
    result = RtlUnicodeStringValidateWorker(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + (__int16)((unsigned __int16)((__int16)(*(unsigned __int16 *)(a1 + 2)))) * 8 + 8) + 104) + 296), (unsigned int)((unsigned int)(v_r12)), (unsigned int)(0x36364D43ULL), a4);
    if (sign_flag) goto loc_008573A0;
    result = (*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + (__int16)((unsigned __int16)((__int16)(*(unsigned __int16 *)(a1 + 2)))) * 8 + 8) + 104) + 296))) >> (1);
    if (v_r11 == 0) goto loc_008573A0;
    a3 = (result) - (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + (__int16)((unsigned __int16)((__int16)(*(unsigned __int16 *)(a1 + 2)))) * 8 + 8) + 104) + 296) + 8));
    v_r11 = (v_r11) - (result);
loc_00857380:
    if (result == 0) goto loc_008573A0;
    result = (result) - 1;
    *(unsigned __int16 *)(a3 + *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + (__int16)((unsigned __int16)((__int16)(*(unsigned __int16 *)(a1 + 2)))) * 8 + 8) + 104) + 296) + 8) * 1) = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + (__int16)((unsigned __int16)((__int16)(*(unsigned __int16 *)(a1 + 2)))) * 8 + 8) + 104) + 296) + 8)));
    v_r10 = (0) + 1;
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + (__int16)((unsigned __int16)((__int16)(*(unsigned __int16 *)(a1 + 2)))) * 8 + 8) + 104) + 296) + 8)) + (2);
    if (v_r11 + result * 1 != 0) goto loc_00857380;
loc_008573A0:
    v_r10 = (unsigned __int16)((v_r10) + ((unsigned __int16)(v_r10)));
    v_stack_m1E8 = (unsigned __int16)(v_r10);
loc_008573AD:
    if (((unsigned int)((__int16)(v_stack_m1D8))) >= 0) goto loc_008574C0;
    v_r13 = 0;
loc_008573D0:
    if (((unsigned int)((__int16)(v_stack_m1D8))) >= 8) goto loc_008575E5;
    a1 = ((unsigned int)((unsigned int)((__int16)(v_stack_m1D8)))) + (2);
    a1 = (a1) << (4);
    a1 = (a1) + (v_stack_m168);
loc_008573E9:
    v_r10 = (unsigned __int16)((v_r10) + (2));
    result = ((unsigned __int16)(v_r10)) >> (1);
    v_stack_m1E8 = (unsigned __int16)(v_r10);
    *(unsigned __int16 *)(result + result * 2) = 92;
    if ((((unsigned __int8)(v_r10)) & (1)) != 0) goto loc_008574B0;
    if ((((unsigned __int8)(v_r12)) & (1)) != 0) goto loc_008574B0;
    if (((unsigned __int16)(v_r12)) > ((unsigned __int16)((unsigned int)(0xFFFEULL)))) goto loc_008574B0;
    if (((unsigned __int16)(v_r10)) > ((unsigned __int16)(v_r12))) goto loc_008574B0;
    a3 = ((unsigned __int16)(v_r12)) >> (1);
    v_rbx = ((unsigned __int16)(v_r10)) >> (1);
    if ((((unsigned __int8)(*(unsigned __int16 *)(a1))) & (1)) != 0) goto loc_008574AB;
    if ((((unsigned __int8)(*(unsigned __int16 *)(a1 + 2))) & (1)) != 0) goto loc_008574AB;
    if (((unsigned __int16)(*(unsigned __int16 *)(a1 + 2))) > ((unsigned __int16)((unsigned int)(0xFFFEULL)))) goto loc_008574AB;
    if (((unsigned __int16)(*(unsigned __int16 *)(a1))) > ((unsigned __int16)(*(unsigned __int16 *)(a1 + 2)))) goto loc_008574AB;
    a2 = (*(unsigned __int16 *)(a1)) >> (1);
    a3 = (a3) - (v_rbx);
    if (condition_is_equal) goto loc_0085749D;
    result = (v_rbx + v_rbx * 1) - (*(unsigned __int64 *)(a1 + 8));
    a4 = (v_stack_m1E0) + (result);
loc_00857480:
    if (a2 == 0) goto loc_0085749D;
    a2 = (a2) - 1;
    *(unsigned __int16 *)(a4 + *(unsigned __int64 *)(a1 + 8) * 1) = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8)));
    v_r10 = (0) + 1;
    a1 = (*(unsigned __int64 *)(a1 + 8)) + (2);
    a3 = (a3) - (1);
    if (condition_is_not_equal) goto loc_00857480;
loc_0085749D:
    v_r10 = (unsigned __int16)((v_r10) + ((unsigned __int16)(v_rbx)));
    v_r10 = (unsigned __int16)((v_r10) + ((unsigned __int16)(v_r10)));
    v_stack_m1E8 = (unsigned __int16)(v_r10);
loc_008574AB:
loc_008574B0:
    v_r11 = (unsigned int)(((__int16)(v_stack_m1D8)) + 1);
    if (((unsigned int)(v_r11)) < 0) goto loc_008573D0;
    v_stack_m1B0 = v_stack_m1B0;
loc_008574C0:
    result = *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8));
    if (*(unsigned __int64 *)(v_stack_m148 + 8) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(v_stack_m148 + 8), a2, a3, a4);
    }
    a2 = 0;
    *(unsigned __int64 *)(v_stack_m148) = v_xmm0;
    result = RtlInitUnicodeString(v_stack_m1E8, a2, a3, a4);
    result = CmpUnlockKcb(v_stack_m1F0, a2, a3, a4);
    v_r15 = 0;
    v_stack_m1F0 = 0;
    *(unsigned __int64 *)(v_stack_m138) = v_stack_m1B0;
    *(unsigned __int64 *)(v_stack_m140) = v_stack_m1F0;
loc_00857515:
    if (v_stack_m1D0 == 0) goto loc_00857559;
    if (((*(unsigned __int8 *)(v_stack_m160 + 140)) & (1)) != 0) goto loc_00857636;
    result = HvpReleaseCellPaged(v_stack_m160, v_stack_m1A8, a3, a4);
loc_00857559:
    if (v_stack_m110 != 0) {
        result = CmSiFreeMemory(v_stack_m110, v_stack_m1A8, a3, a4);
    }
    if (v_stack_m68 == 0) goto loc_008575B8;
    result = ExpInterlockedPushEntrySList(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2176), v_stack_m68, *(unsigned __int64 *)(gs_base + (0 + 32)), a4);
loc_008575B8:
    a1 = (v_stack_m58) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m68, *(unsigned __int64 *)(gs_base + (0 + 32)), a4);
    v_rsp = (v_rsp) + (512);
    return result;
loc_008575E5:
    a1 = (v_r11 - 8) + (6);
    a1 = (a1) << (4);
    a1 = (a1) + (*(unsigned __int64 *)(v_stack_m168 + 160));
    goto loc_008573E9;
loc_00857601:
    result = (a1 - 8) + (6);
    result = (result) << (4);
    result = (result) + (*(unsigned __int64 *)(v_stack_m68 + 160));
    goto loc_008572EC;
loc_00857618:
    goto loc_008572A3;
loc_00857626:
    goto loc_00857515;
loc_00857636:
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(0 + 24) + a1 * 8 - 16), v_stack_m68, *(unsigned __int64 *)(gs_base + (0 + 32)), a4);
    goto loc_00857559;
loc_00857640:
    v_stack_m1B0 = *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC0000034ULL) + 24) + result * 8 - 16);
loc_00857653:
    result = (unsigned int)(*(unsigned int *)(v_stack_p20 + 160));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p20 + 160)))) & (1)) == 0) {
        a1 = v_stack_p20 + 168;
        result = CmpAttachToRegistryProcess(a1, *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC0000034ULL) + 24) + result * 8 - 16), *(unsigned __int64 *)(gs_base + (0 + 32)), a4);
    }
    result = 0;
    v_stack_m158 = 0;
    result = CmpGetKcbAtLayerHeight(v_stack_m188, (unsigned __int16)(*(unsigned __int16 *)((unsigned int)(0xC0000034ULL) + 2)), 0, a4);
    if (0 != 0) goto loc_008576BB;
    if ((*(unsigned int *)(result + 40)) != -1) goto loc_008576B4;
    if (((*(unsigned int *)(*(unsigned __int64 *)(result + 32) + 4112)) & (0x2000ULL)) == 0) {
        a3 = result;
        v_stack_m158 = result;
    }
    if ((*(unsigned __int16 *)(result + 66)) == 0) goto loc_008576CC;
loc_008576CC:
    result = CmEqualTrans(*(unsigned __int64 *)(result + 288), v_stack_m160, a3, a4);
    v_rbx = (result) + (32);
    result = HvpGetCellFlat(*(unsigned __int64 *)(result + 32), (unsigned int)(*(unsigned int *)(result + 40)), v_stack_p78, a4);
    a4 = 0;
    v_stack_p28 = v_stack_p44;
    result = 0;
    v_stack_p20 = 0;
    result = CmpFindNameInListWithStatus(*(unsigned __int64 *)(v_rbx), result + 36, v_rip + 7873750, a4);
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(v_rbx), v_stack_p78, v_rip + 7873750, a4);
    v_stack_m160 = *(unsigned __int64 *)(v_rbx);
    result = HvpGetCellFlat(*(unsigned __int64 *)(v_rbx), (unsigned int)((unsigned int)((unsigned int)(v_stack_p44))), v_stack_m1A8, a4);
    v_stack_p68 = result;
    v_stack_p30 = v_stack_m170;
    v_stack_p28 = v_stack_p42;
    v_stack_p20 = v_stack_m178;
    result = CmpGetValueData(*(unsigned __int64 *)(v_rbx), (unsigned int)((unsigned int)((unsigned int)(v_stack_p44))), result, v_stack_m1B8);
    v_stack_m190 = v_stack_m178;
    v_stack_m198 = (unsigned __int16)((unsigned int)(v_stack_m1B8));
    v_stack_m196 = (unsigned __int16)((unsigned int)(v_stack_m1B8));
    if (((unsigned int)((__int16)(v_stack_p60))) >= 0) goto loc_00857837;
loc_00857817:
    result = CmpGetComponentNameAtIndex(v_stack_m168, (unsigned int)((unsigned int)((__int16)(v_stack_p60))), (__int16)(v_stack_p60), v_stack_m1B8);
    v_rdi = (unsigned int)(((unsigned __int16)((unsigned int)(v_stack_m1B8))) + (2));
    a3 = (unsigned int)(((__int16)(v_stack_p60)) + 1);
    v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(*(unsigned __int16 *)(result))));
    if (a3 < 0) goto loc_00857817;
loc_00857837:
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(v_rdi)), (unsigned int)(0x36364D43ULL), v_stack_m1B8);
    v_stack_p58 = result;
    v_rbx = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmpGetSymbolicLinkTarget(void *Arg1, int64_t Arg2, uint16_t Arg3, int32_t Arg4, int64_t Arg5, void *Arg6, int64_t Arg7, int64_t Arg8, int64_t Arg9, int64_t Arg10)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint16_t v_stack_m126;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint16_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint16_t v_stack_m196;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint32_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint16_t v_stack_m1C4;
    uint16_t v_stack_m1C8;
    uint64_t v_stack_m1D0;
    uint16_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint16_t v_stack_m1E6;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint32_t v_stack_m1F4;
    uint8_t v_stack_m1F6;
    uint8_t v_stack_m1F7;
    uint8_t v_stack_m1F8;
    uint64_t v_stack_m218;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint8_t v_stack_p40;
    uint64_t v_stack_p42;
    uint32_t v_stack_p44;
    uint64_t v_stack_p58;
    uint16_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p78;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (512);
    result = (*(uint64_t *)(v_rip + 0x5B367A)) ^ (local_rsp);
    v_stack_m58 = result;
    local_r14 = 0;
    v_stack_m130 = Arg7;
    v_stack_m148 = Arg8;
    v_stack_m140 = Arg9;
    v_stack_m168 = Arg2;
    Arg2 = 0;
    v_stack_m188 = Arg1;
    v_stack_m138 = Arg10;
    v_stack_m180 = (uint16_t)((int16_t)((uint16_t)(Arg4)));
    v_stack_m1D8 = (uint16_t)((int16_t)(Arg3));
    v_stack_m1E8 = v_xmm0;
    v_stack_m1C0 = 0;
    v_stack_m198 = v_xmm0;
    v_stack_m1A8 = 0;
    v_stack_m170 = 0;
    v_stack_m1C8 = 0;
    v_stack_m1C4 = 0;
    result = RtlInitUnicodeString(v_stack_m1E8, Arg2, Arg3, Arg4);
    v_stack_m1F0 = 0;
    local_r15 = 0;
    v_stack_m1F7 = 0;
    result = HvpGetCellContextInitialize(v_stack_m1C0, Arg2, Arg3, Arg4);
    v_stack_m1D0 = 0;
    v_stack_m1F4 = 0xFFFFFFFFULL;
    v_stack_m160 = 0;
    result = HvpGetCellContextInitialize(v_stack_m1A8, Arg2, Arg3, Arg4);
    v_stack_m178 = 0;
    v_stack_m1F6 = 0;
    v_stack_m1B8 = 0;
    result = HvpGetCellContextInitialize(v_stack_m170, Arg2, Arg3, Arg4);
    Arg2 = 0;
    result = memset(v_stack_m108, Arg2, 168, Arg4);
    v_stack_m128 = v_xmm0;
    v_stack_m126 = (uint16_t)((uint32_t)(0xFFFFFFFFULL));
    v_stack_m118 = v_xmm0;
    if (Arg5 != 0) goto loc_008571DC;
    if ((*(uint16_t *)(arg1 + 0x2)) != 0) goto loc_008571DC;
    goto loc_008571EA;
loc_008571DC:
    if (((uint32_t)((int16_t)(*(uint16_t *)(arg1 + 0x2)))) >= 2) goto loc_00857640;
loc_008571EA:
    v_stack_m1B0 = *(uint64_t *)(arg1 + (int16_t)((uint16_t)((int16_t)(*(uint16_t *)(arg1 + 0x2)))) * 8 + 0x8);
    if (1 == 0) goto loc_00857653;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + (int16_t)((uint16_t)((int16_t)(*(uint16_t *)(arg1 + 0x2)))) * 8 + 0x8) + 0x8)))) & (8)) == 0) goto loc_00857653;
    Arg1 = 0;
    v_stack_m1F0 = *(uint64_t *)(*(uint64_t *)(arg1 + (int16_t)((uint16_t)((int16_t)(*(uint16_t *)(arg1 + 0x2)))) * 8 + 0x8) + 0x68);
    Arg1 = (1) + (1);
    result = v_stack_m1F0;
    local_r13 = (int16_t)((uint16_t)(Arg4));
    if (Arg1 == 1) {
        Arg2 = Arg1 + 20;
        local_r13 = 0;
        Arg1 = Arg2 + 60;
        v_stack_m218 = 0;
        Arg4 = 0;
        Arg3 = 0;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    result = 0;
    if (0 > (*(uint16_t *)(v_stack_m188 + 0x2))) goto loc_008572B2;
loc_00857290:
    if (0 >= 2) goto loc_00857618;
loc_008572A3:
    result = CmpUnlockKcb(*(uint64_t *)(v_stack_m188 + (int16_t)(0) * 8 + 0x8), Arg2, Arg3, Arg4);
    local_rbx = (uint16_t)((0) + 1);
    if (((uint16_t)(local_rbx)) <= (*(uint16_t *)(v_stack_m188 + 0x2))) goto loc_00857290;
loc_008572B2:
    v_stack_m1F8 = 0;
    result = CmpLockKcbShared(v_stack_m1F0, Arg2, Arg3, Arg4);
    if (((uint32_t)((int16_t)(Arg3))) >= 0) goto loc_008572FD;
loc_008572D6:
    if (((uint32_t)((uint32_t)((uint32_t)((int16_t)(Arg3))))) >= 8) goto loc_00857601;
    result = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((int16_t)(Arg3)))))) + (2);
    result = (result) << (4);
    result = (result) + (v_stack_m168);
loc_008572EC:
    local_r12 = (uint32_t)((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + (int16_t)((uint16_t)((int16_t)(*(uint16_t *)(arg1 + 0x2)))) * 8 + 0x8) + 0x68) + 0x128))) + (2));
    local_r12 = (uint32_t)((local_r12) + ((uint32_t)(*(uint16_t *)(result))));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((int16_t)(Arg3)))) + 1);
    if (((uint32_t)(Arg1)) < 0) goto loc_008572D6;
loc_008572FD:
    if (((uint32_t)(local_r12)) > ((uint32_t)((uint32_t)(0xFFFFULL)))) goto loc_00857626;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(local_r12)), (uint32_t)(0x36364D43ULL), Arg4);
    v_stack_m1E0 = result;
    local_rsi = 0;
    v_stack_m1E6 = (uint16_t)(local_r12);
    v_stack_m1E8 = 0;
    result = RtlUnicodeStringValidateWorker(v_stack_m1E8, (uint32_t)((uint32_t)(local_r12)), (uint32_t)(0x36364D43ULL), Arg4);
    if (sign_flag) goto loc_008573AD;
    local_r11 = ((uint16_t)(local_r12)) >> (1);
    result = RtlUnicodeStringValidateWorker(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + (int16_t)((uint16_t)((int16_t)(*(uint16_t *)(arg1 + 0x2)))) * 8 + 0x8) + 0x68) + 0x128), (uint32_t)((uint32_t)(local_r12)), (uint32_t)(0x36364D43ULL), Arg4);
    if (sign_flag) goto loc_008573A0;
    result = (*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + (int16_t)((uint16_t)((int16_t)(*(uint16_t *)(arg1 + 0x2)))) * 8 + 0x8) + 0x68) + 0x128))) >> (1);
    if (local_r11 == 0) goto loc_008573A0;
    Arg3 = (result) - (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + (int16_t)((uint16_t)((int16_t)(*(uint16_t *)(arg1 + 0x2)))) * 8 + 0x8) + 0x68) + 0x128) + 0x8));
    local_r11 = (local_r11) - (result);
loc_00857380:
    if (result == 0) goto loc_008573A0;
    result = (result) - 1;
    *(uint16_t *)(Arg3 + *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + (int16_t)((uint16_t)((int16_t)(*(uint16_t *)(arg1 + 0x2)))) * 8 + 0x8) + 0x68) + 0x128) + 0x8) * 1) = (uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + (int16_t)((uint16_t)((int16_t)(*(uint16_t *)(arg1 + 0x2)))) * 8 + 0x8) + 0x68) + 0x128) + 0x8)));
    local_r10 = (0) + 1;
    Arg2 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + (int16_t)((uint16_t)((int16_t)(*(uint16_t *)(arg1 + 0x2)))) * 8 + 0x8) + 0x68) + 0x128) + 0x8)) + (2);
    if (local_r11 + result * 1 != 0) goto loc_00857380;
loc_008573A0:
    local_r10 = (uint16_t)((local_r10) + ((uint16_t)(local_r10)));
    v_stack_m1E8 = (uint16_t)(local_r10);
loc_008573AD:
    if (((uint32_t)((int16_t)(v_stack_m1D8))) >= 0) goto loc_008574C0;
    local_r13 = 0;
loc_008573D0:
    if (((uint32_t)((int16_t)(v_stack_m1D8))) >= 8) goto loc_008575E5;
    Arg1 = ((uint32_t)((uint32_t)((int16_t)(v_stack_m1D8)))) + (2);
    Arg1 = (Arg1) << (4);
    Arg1 = (Arg1) + (v_stack_m168);
loc_008573E9:
    local_r10 = (uint16_t)((local_r10) + (2));
    result = ((uint16_t)(local_r10)) >> (1);
    v_stack_m1E8 = (uint16_t)(local_r10);
    *(uint16_t *)(result + result * 2) = 92;
    if ((((uint8_t)(local_r10)) & (1)) != 0) goto loc_008574B0;
    if ((((uint8_t)(local_r12)) & (1)) != 0) goto loc_008574B0;
    if (((uint16_t)(local_r12)) > ((uint16_t)((uint32_t)(0xFFFEULL)))) goto loc_008574B0;
    if (((uint16_t)(local_r10)) > ((uint16_t)(local_r12))) goto loc_008574B0;
    Arg3 = ((uint16_t)(local_r12)) >> (1);
    local_rbx = ((uint16_t)(local_r10)) >> (1);
    if ((((uint8_t)(*(uint16_t *)(arg1))) & (1)) != 0) goto loc_008574AB;
    if ((((uint8_t)(*(uint16_t *)(arg1 + 0x2))) & (1)) != 0) goto loc_008574AB;
    if (((uint16_t)(*(uint16_t *)(arg1 + 0x2))) > ((uint16_t)((uint32_t)(0xFFFEULL)))) goto loc_008574AB;
    if (((uint16_t)(*(uint16_t *)(arg1))) > ((uint16_t)(*(uint16_t *)(arg1 + 0x2)))) goto loc_008574AB;
    Arg2 = (*(uint16_t *)(arg1)) >> (1);
    Arg3 = (Arg3) - (local_rbx);
    if (condition_is_equal) goto loc_0085749D;
    result = (local_rbx + local_rbx * 1) - (*(uint64_t *)(arg1 + 0x8));
    Arg4 = (v_stack_m1E0) + (result);
loc_00857480:
    if (Arg2 == 0) goto loc_0085749D;
    Arg2 = (Arg2) - 1;
    *(uint16_t *)(Arg4 + *(uint64_t *)(arg1 + 0x8) * 1) = (uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8)));
    local_r10 = (0) + 1;
    Arg1 = (*(uint64_t *)(arg1 + 0x8)) + (2);
    Arg3 = (Arg3) - (1);
    if (condition_is_not_equal) goto loc_00857480;
loc_0085749D:
    local_r10 = (uint16_t)((local_r10) + ((uint16_t)(local_rbx)));
    local_r10 = (uint16_t)((local_r10) + ((uint16_t)(local_r10)));
    v_stack_m1E8 = (uint16_t)(local_r10);
loc_008574AB:
loc_008574B0:
    local_r11 = (uint32_t)(((int16_t)(v_stack_m1D8)) + 1);
    if (((uint32_t)(local_r11)) < 0) goto loc_008573D0;
    v_stack_m1B0 = v_stack_m1B0;
loc_008574C0:
    result = *(uint16_t *)(*(uint64_t *)(arg1 + 0x8));
    if (*(uint64_t *)(v_stack_m148 + 0x8) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(v_stack_m148 + 0x8), Arg2, Arg3, Arg4);
    }
    Arg2 = 0;
    *(uint64_t *)(v_stack_m148) = v_xmm0;
    result = RtlInitUnicodeString(v_stack_m1E8, Arg2, Arg3, Arg4);
    result = CmpUnlockKcb(v_stack_m1F0, Arg2, Arg3, Arg4);
    local_r15 = 0;
    v_stack_m1F0 = 0;
    *(uint64_t *)(v_stack_m138) = v_stack_m1B0;
    *(uint64_t *)(v_stack_m140) = v_stack_m1F0;
loc_00857515:
    if (v_stack_m1D0 == 0) goto loc_00857559;
    if (((*(uint8_t *)(v_stack_m160 + 0x8C)) & (1)) != 0) goto loc_00857636;
    result = HvpReleaseCellPaged(v_stack_m160, v_stack_m1A8, Arg3, Arg4);
loc_00857559:
    if (v_stack_m110 != 0) {
        result = CmSiFreeMemory(v_stack_m110, v_stack_m1A8, Arg3, Arg4);
    }
    if (v_stack_m68 == 0) goto loc_008575B8;
    result = ExpInterlockedPushEntrySList(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x880), v_stack_m68, *(uint64_t *)(gs_base + (0 + 0x20)), Arg4);
loc_008575B8:
    Arg1 = (v_stack_m58) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m68, *(uint64_t *)(gs_base + (0 + 0x20)), Arg4);
    local_rsp = (local_rsp) + (512);
    return result;
loc_008575E5:
    Arg1 = (local_r11 - 8) + (6);
    Arg1 = (Arg1) << (4);
    Arg1 = (Arg1) + (*(uint64_t *)(v_stack_m168 + 0xA0));
    goto loc_008573E9;
loc_00857601:
    result = (Arg1 - 8) + (6);
    result = (result) << (4);
    result = (result) + (*(uint64_t *)(v_stack_m68 + 0xA0));
    goto loc_008572EC;
loc_00857618:
    goto loc_008572A3;
loc_00857626:
    goto loc_00857515;
loc_00857636:
    result = HvpReleaseCellFlat(*(uint64_t *)(*(uint64_t *)(0 + 0x18) + arg1 * 8 - 0x10), v_stack_m68, *(uint64_t *)(gs_base + (0 + 0x20)), Arg4);
    goto loc_00857559;
loc_00857640:
    v_stack_m1B0 = *(uint64_t *)(*(uint64_t *)((uint32_t)(0xC0000034ULL) + 0x18) + result * 8 - 0x10);
loc_00857653:
    result = (uint32_t)(*(uint32_t *)(v_stack_p20 + 0xA0));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0xA0)))) & (1)) == 0) {
        Arg1 = v_stack_p20 + 168;
        result = CmpAttachToRegistryProcess(Arg1, *(uint64_t *)(*(uint64_t *)((uint32_t)(0xC0000034ULL) + 0x18) + result * 8 - 0x10), *(uint64_t *)(gs_base + (0 + 0x20)), Arg4);
    }
    result = 0;
    v_stack_m158 = 0;
    result = CmpGetKcbAtLayerHeight(v_stack_m188, (uint16_t)(*(uint16_t *)((uint32_t)(0xC0000034ULL) + 0x2)), 0, Arg4);
    if (0 != 0) goto loc_008576BB;
    if ((*(uint32_t *)(result + 0x28)) != -1) goto loc_008576B4;
    if (((*(uint32_t *)(*(uint64_t *)(result + 0x20) + 0x1010)) & (0x2000ULL)) == 0) {
        Arg3 = result;
        v_stack_m158 = result;
    }
    if ((*(uint16_t *)(result + 0x42)) == 0) goto loc_008576CC;
loc_008576CC:
    result = CmEqualTrans(*(uint64_t *)(result + 0x120), v_stack_m160, Arg3, Arg4);
    local_rbx = (result) + (32);
    result = HvpGetCellFlat(*(uint64_t *)(result + 0x20), (uint32_t)(*(uint32_t *)(result + 0x28)), v_stack_p78, Arg4);
    Arg4 = 0;
    v_stack_p28 = v_stack_p44;
    result = 0;
    v_stack_p20 = 0;
    result = CmpFindNameInListWithStatus(*(uint64_t *)(local_rbx), result + 36, v_rip + 7873750, Arg4);
    result = HvpReleaseCellPaged(*(uint64_t *)(local_rbx), v_stack_p78, v_rip + 7873750, Arg4);
    v_stack_m160 = *(uint64_t *)(local_rbx);
    result = HvpGetCellFlat(*(uint64_t *)(local_rbx), (uint32_t)((uint32_t)((uint32_t)(v_stack_p44))), v_stack_m1A8, Arg4);
    v_stack_p68 = result;
    v_stack_p30 = v_stack_m170;
    v_stack_p28 = v_stack_p42;
    v_stack_p20 = v_stack_m178;
    result = CmpGetValueData(*(uint64_t *)(local_rbx), (uint32_t)((uint32_t)((uint32_t)(v_stack_p44))), result, v_stack_m1B8);
    v_stack_m190 = v_stack_m178;
    v_stack_m198 = (uint16_t)((uint32_t)(v_stack_m1B8));
    v_stack_m196 = (uint16_t)((uint32_t)(v_stack_m1B8));
    if (((uint32_t)((int16_t)(v_stack_p60))) >= 0) goto loc_00857837;
loc_00857817:
    result = CmpGetComponentNameAtIndex(v_stack_m168, (uint32_t)((uint32_t)((int16_t)(v_stack_p60))), (int16_t)(v_stack_p60), v_stack_m1B8);
    local_rdi = (uint32_t)(((uint16_t)((uint32_t)(v_stack_m1B8))) + (2));
    Arg3 = (uint32_t)(((int16_t)(v_stack_p60)) + 1);
    local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(*(uint16_t *)(result))));
    if (Arg3 < 0) goto loc_00857817;
loc_00857837:
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(local_rdi)), (uint32_t)(0x36364D43ULL), v_stack_m1B8);
    v_stack_p58 = result;
    local_rbx = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x2` | `16` | `R` |
| `Arg1` | `+ 0x8 + rax*8` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg6` | `+ 0xA0` | `32` | `R` |
| `Arg6` | `+ 0xA0` | `32` | `R/W` |
| `Arg6` | `+ 0xA8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008570A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
