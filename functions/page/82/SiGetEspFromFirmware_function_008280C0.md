# SiGetEspFromFirmware

- RVA: `0x008280C0`–`0x00828468` (길이 `936` bytes)
- VA: `0x00000001408280C0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DA724`
- 디코드: `284`개 명령, `936/936` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **28**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00828113` → [BiAcquirePrivilege](../A3/BiAcquirePrivilege_function_00A3D658.md) (function, `0x00A3D658`)
- `0x0082812A` → [ZwEnumerateBootEntries](../../text/6A/ZwEnumerateBootEntries_function_006AEDB0.md) (function, `0x006AEDB0`)
- `0x00828151` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00828166` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008281B3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008281C8` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008281E0` → [ZwQueryBootOptions](../../text/6A/ZwQueryBootOptions_function_006AFA50.md) (function, `0x006AFA50`)
- `0x00828211` → [SiGetEfiBootEntryById](SiGetEfiBootEntryById_function_00827C48.md) (function, `0x00827C48`)
- `0x00828225` → [SiBootEntryGetNtFilePath](SiBootEntryGetNtFilePath_function_00827ADC.md) (function, `0x00827ADC`)
- `0x0082823A` → [SiIsValidWindowsBootEntry](SiIsValidWindowsBootEntry_function_0082851C.md) (function, `0x0082851C`)
- `0x0082824F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00828262` → [ZwQueryBootEntryOrder](../../text/6A/ZwQueryBootEntryOrder_function_006AFA30.md) (function, `0x006AFA30`)
- `0x00828289` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008282A2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008282E6` → [SiGetEfiBootEntryById](SiGetEfiBootEntryById_function_00827C48.md) (function, `0x00827C48`)
- `0x008282FA` → [SiBootEntryGetNtFilePath](SiBootEntryGetNtFilePath_function_00827ADC.md) (function, `0x00827ADC`)
- `0x0082830D` → [SiIsValidWindowsBootEntry](SiIsValidWindowsBootEntry_function_0082851C.md) (function, `0x0082851C`)
- `0x00828326` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x0082834F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00828381` → [BiReleasePrivilege](../A3/BiReleasePrivilege_function_00A3D600.md) (function, `0x00A3D600`)
- `0x008283A8` → [SiGetDeviceNumberInformation](SiGetDeviceNumberInformation_function_00827858.md) (function, `0x00827858`)
- `0x008283CC` → [RtlStringCbPrintfW](../../text/40/RtlStringCbPrintfW_function_0040FB40.md) (function, `0x0040FB40`)
- `0x00828404` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00828413` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00828422` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00828431` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00828440` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0082844F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [SiGetEfiSystemDevice](SiGetEfiSystemDevice_function_00827C68.md) at `0x00827FD0`

### Static image references
- `0x008283B7` → RVA `0x00B08940` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **19**
  - `0x0082812A` → [ZwEnumerateBootEntries](../../text/6A/ZwEnumerateBootEntries_function_006AEDB0.md) (`PAGE` → `.text`)
  - `0x00828151` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00828166` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008281B3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008281C8` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008281E0` → [ZwQueryBootOptions](../../text/6A/ZwQueryBootOptions_function_006AFA50.md) (`PAGE` → `.text`)
  - `0x0082824F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00828262` → [ZwQueryBootEntryOrder](../../text/6A/ZwQueryBootEntryOrder_function_006AFA30.md) (`PAGE` → `.text`)
  - `0x00828289` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008282A2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00828326` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
  - `0x0082834F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008283CC` → [RtlStringCbPrintfW](../../text/40/RtlStringCbPrintfW_function_0040FB40.md) (`PAGE` → `.text`)
  - `0x00828404` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00828413` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00828422` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00828431` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00828440` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0082844F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008280C0  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
008280C5  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
008280CA  89 4C 24 08                     mov dword ptr [rsp + 8], ecx
008280CE  55                              push rbp
008280CF  53                              push rbx
008280D0  56                              push rsi
008280D1  57                              push rdi
008280D2  41 54                           push r12
008280D4  41 55                           push r13
008280D6  41 56                           push r14
008280D8  41 57                           push r15
008280DA  48 8B EC                        mov rbp, rsp
008280DD  48 83 EC 58                     sub rsp, 0x58
008280E1  45 33 F6                        xor r14d, r14d
008280E4  48 8D 55 F0                     lea rdx, [rbp - 0x10]
008280E8  44 89 75 60                     mov dword ptr [rbp + 0x60], r14d
008280EC  45 8B FE                        mov r15d, r14d
008280EF  44 89 75 D8                     mov dword ptr [rbp - 0x28], r14d
008280F3  45 8B E6                        mov r12d, r14d
008280F6  44 89 75 DC                     mov dword ptr [rbp - 0x24], r14d
008280FA  45 8B EE                        mov r13d, r14d
008280FD  41 8D 4E 16                     lea ecx, [r14 + 0x16]
00828101  4C 89 75 F0                     mov qword ptr [rbp - 0x10], r14
00828105  41 8B FE                        mov edi, r14d
00828108  4C 89 75 E8                     mov qword ptr [rbp - 0x18], r14
0082810C  41 8B F6                        mov esi, r14d
0082810F  4C 89 75 E0                     mov qword ptr [rbp - 0x20], r14
00828113  E8 40 55 21 00                  call 0x140a3d658
00828118  85 C0                           test eax, eax
0082811A  0F 88 36 03 00 00               js 0x140828456
00828120  44 89 75 58                     mov dword ptr [rbp + 0x58], r14d
00828124  33 C9                           xor ecx, ecx
00828126  48 8D 55 58                     lea rdx, [rbp + 0x58]
0082812A  E8 81 6C E8 FF                  call 0x1406aedb0
0082812F  8B D8                           mov ebx, eax
00828131  3D 23 00 00 C0                  cmp eax, 0xc0000023
00828136  75 4E                           jne 0x140828186
00828138  8B 45 58                        mov eax, dword ptr [rbp + 0x58]
0082813B  44 3B F0                        cmp r14d, eax
0082813E  0F 83 36 02 00 00               jae 0x14082837a
00828144  45 33 F6                        xor r14d, r14d
00828147  4D 85 FF                        test r15, r15
0082814A  74 0D                           je 0x140828159
0082814C  33 D2                           xor edx, edx
0082814E  49 8B CF                        mov rcx, r15
00828151  E8 1A A7 35 00                  call 0x140b82870
00828156  8B 45 58                        mov eax, dword ptr [rbp + 0x58]
00828159  8B D0                           mov edx, eax
0082815B  B9 00 01 00 00                  mov ecx, 0x100
00828160  41 B8 53 59 50 4B               mov r8d, 0x4b505953
00828166  E8 85 9F 35 00                  call 0x140b820f0
0082816B  4C 8B F8                        mov r15, rax
0082816E  48 85 C0                        test rax, rax
00828171  74 09                           je 0x14082817c
00828173  44 8B 75 58                     mov r14d, dword ptr [rbp + 0x58]
00828177  48 8B C8                        mov rcx, rax
0082817A  EB AA                           jmp 0x140828126
0082817C  BB 17 00 00 C0                  mov ebx, 0xc0000017
00828181  E9 F7 01 00 00                  jmp 0x14082837d
00828186  45 33 F6                        xor r14d, r14d
00828189  85 DB                           test ebx, ebx
0082818B  0F 88 EC 01 00 00               js 0x14082837d
00828191  44 39 75 58                     cmp dword ptr [rbp + 0x58], r14d
00828195  75 0A                           jne 0x1408281a1
00828197  BB 25 02 00 C0                  mov ebx, 0xc0000225
0082819C  E9 DC 01 00 00                  jmp 0x14082837d
008281A1  B8 18 00 00 00                  mov eax, 0x18
008281A6  89 45 58                        mov dword ptr [rbp + 0x58], eax
008281A9  4D 85 ED                        test r13, r13
008281AC  74 0D                           je 0x1408281bb
008281AE  33 D2                           xor edx, edx
008281B0  49 8B CD                        mov rcx, r13
008281B3  E8 B8 A6 35 00                  call 0x140b82870
008281B8  8B 45 58                        mov eax, dword ptr [rbp + 0x58]
008281BB  8B D0                           mov edx, eax
008281BD  B9 00 01 00 00                  mov ecx, 0x100
008281C2  41 B8 53 59 50 4B               mov r8d, 0x4b505953
008281C8  E8 23 9F 35 00                  call 0x140b820f0
008281CD  4C 8B E8                        mov r13, rax
008281D0  48 85 C0                        test rax, rax
008281D3  74 A7                           je 0x14082817c
008281D5  44 8B 75 58                     mov r14d, dword ptr [rbp + 0x58]
008281D9  48 8D 55 58                     lea rdx, [rbp + 0x58]
008281DD  48 8B C8                        mov rcx, rax
008281E0  E8 6B 78 E8 FF                  call 0x1406afa50
008281E5  8B D8                           mov ebx, eax
008281E7  3D 23 00 00 C0                  cmp eax, 0xc0000023
008281EC  75 11                           jne 0x1408281ff
008281EE  8B 45 58                        mov eax, dword ptr [rbp + 0x58]
008281F1  44 3B F0                        cmp r14d, eax
008281F4  0F 83 80 01 00 00               jae 0x14082837a
008281FA  45 33 F6                        xor r14d, r14d
008281FD  EB AA                           jmp 0x1408281a9
008281FF  45 33 F6                        xor r14d, r14d
00828202  85 C0                           test eax, eax
00828204  0F 88 73 01 00 00               js 0x14082837d
0082820A  41 8B 55 0C                     mov edx, dword ptr [r13 + 0xc]
0082820E  49 8B CF                        mov rcx, r15
00828211  E8 32 FA FF FF                  call 0x140827c48
00828216  4C 8B F0                        mov r14, rax
00828219  48 85 C0                        test rax, rax
0082821C  74 3B                           je 0x140828259
0082821E  48 8D 55 E8                     lea rdx, [rbp - 0x18]
00828222  48 8B C8                        mov rcx, rax
00828225  E8 B2 F8 FF FF                  call 0x140827adc
0082822A  48 8B 7D E8                     mov rdi, qword ptr [rbp - 0x18]
0082822E  8B D8                           mov ebx, eax
00828230  85 C0                           test eax, eax
00828232  78 25                           js 0x140828259
00828234  48 8B D7                        mov rdx, rdi
00828237  49 8B CE                        mov rcx, r14
0082823A  E8 DD 02 00 00                  call 0x14082851c
0082823F  45 33 F6                        xor r14d, r14d
00828242  84 C0                           test al, al
00828244  0F 85 33 01 00 00               jne 0x14082837d
0082824A  33 D2                           xor edx, edx
0082824C  48 8B CF                        mov rcx, rdi
0082824F  E8 1C A6 35 00                  call 0x140b82870
00828254  41 8B FE                        mov edi, r14d
00828257  EB 03                           jmp 0x14082825c
00828259  45 33 F6                        xor r14d, r14d
0082825C  33 C9                           xor ecx, ecx
0082825E  48 8D 55 60                     lea rdx, [rbp + 0x60]
00828262  E8 C9 77 E8 FF                  call 0x1406afa30
00828267  8B D8                           mov ebx, eax
00828269  3D 23 00 00 C0                  cmp eax, 0xc0000023
0082826E  75 4C                           jne 0x1408282bc
00828270  8B 45 60                        mov eax, dword ptr [rbp + 0x60]
00828273  44 3B F0                        cmp r14d, eax
00828276  0F 83 FE 00 00 00               jae 0x14082837a
0082827C  45 33 F6                        xor r14d, r14d
0082827F  4D 85 E4                        test r12, r12
00828282  74 0D                           je 0x140828291
00828284  33 D2                           xor edx, edx
00828286  49 8B CC                        mov rcx, r12
00828289  E8 E2 A5 35 00                  call 0x140b82870
0082828E  8B 45 60                        mov eax, dword ptr [rbp + 0x60]
00828291  8B D0                           mov edx, eax
00828293  B9 00 01 00 00                  mov ecx, 0x100
00828298  48 C1 E2 02                     shl rdx, 2
0082829C  41 B8 53 59 50 4B               mov r8d, 0x4b505953
008282A2  E8 49 9E 35 00                  call 0x140b820f0
008282A7  4C 8B E0                        mov r12, rax
008282AA  48 85 C0                        test rax, rax
008282AD  0F 84 C9 FE FF FF               je 0x14082817c
008282B3  44 8B 75 60                     mov r14d, dword ptr [rbp + 0x60]
008282B7  48 8B C8                        mov rcx, rax
008282BA  EB A2                           jmp 0x14082825e
008282BC  45 33 F6                        xor r14d, r14d
008282BF  85 DB                           test ebx, ebx
008282C1  0F 85 B6 00 00 00               jne 0x14082837d
008282C7  44 39 75 60                     cmp dword ptr [rbp + 0x60], r14d
008282CB  0F 84 C6 FE FF FF               je 0x140828197
008282D1  41 8B DE                        mov ebx, r14d
008282D4  3B 5D 60                        cmp ebx, dword ptr [rbp + 0x60]
008282D7  0F 83 8A 00 00 00               jae 0x140828367
008282DD  8B D3                           mov edx, ebx
008282DF  49 8B CF                        mov rcx, r15
008282E2  41 8B 14 94                     mov edx, dword ptr [r12 + rdx*4]
008282E6  E8 5D F9 FF FF                  call 0x140827c48
008282EB  4C 8B F0                        mov r14, rax
008282EE  48 85 C0                        test rax, rax
008282F1  74 6A                           je 0x14082835d
008282F3  48 8D 55 E0                     lea rdx, [rbp - 0x20]
008282F7  48 8B C8                        mov rcx, rax
008282FA  E8 DD F7 FF FF                  call 0x140827adc
008282FF  48 8B 75 E0                     mov rsi, qword ptr [rbp - 0x20]
00828303  85 C0                           test eax, eax
00828305  78 3B                           js 0x140828342
00828307  48 8B D6                        mov rdx, rsi
0082830A  49 8B CE                        mov rcx, r14
0082830D  E8 0A 02 00 00                  call 0x14082851c
00828312  45 33 F6                        xor r14d, r14d
00828315  84 C0                           test al, al
00828317  74 2C                           je 0x140828345
00828319  48 85 FF                        test rdi, rdi
0082831C  74 18                           je 0x140828336
0082831E  48 8D 56 0C                     lea rdx, [rsi + 0xc]
00828322  48 8D 4F 0C                     lea rcx, [rdi + 0xc]
00828326  E8 55 7D CD FF                  call 0x140500080
0082832B  85 C0                           test eax, eax
0082832D  74 16                           je 0x140828345
0082832F  BB 51 04 00 C0                  mov ebx, 0xc0000451
00828334  EB 47                           jmp 0x14082837d
00828336  48 8B FE                        mov rdi, rsi
00828339  4C 89 75 E0                     mov qword ptr [rbp - 0x20], r14
0082833D  49 8B F6                        mov rsi, r14
00828340  EB 03                           jmp 0x140828345
00828342  45 33 F6                        xor r14d, r14d
00828345  48 85 F6                        test rsi, rsi
00828348  74 16                           je 0x140828360
0082834A  33 D2                           xor edx, edx
0082834C  48 8B CE                        mov rcx, rsi
0082834F  E8 1C A5 35 00                  call 0x140b82870
00828354  49 8B F6                        mov rsi, r14
00828357  4C 89 75 E0                     mov qword ptr [rbp - 0x20], r14
0082835B  EB 03                           jmp 0x140828360
0082835D  45 33 F6                        xor r14d, r14d
00828360  FF C3                           inc ebx
00828362  E9 6D FF FF FF                  jmp 0x1408282d4
00828367  48 8B C7                        mov rax, rdi
0082836A  BB 25 02 00 C0                  mov ebx, 0xc0000225
0082836F  48 F7 D8                        neg rax
00828372  1B C9                           sbb ecx, ecx
00828374  F7 D1                           not ecx
00828376  23 D9                           and ebx, ecx
00828378  EB 03                           jmp 0x14082837d
0082837A  45 33 F6                        xor r14d, r14d
0082837D  48 8D 4D F0                     lea rcx, [rbp - 0x10]
00828381  E8 7A 52 21 00                  call 0x140a3d600
00828386  85 DB                           test ebx, ebx
00828388  78 7F                           js 0x140828409
0082838A  48 85 FF                        test rdi, rdi
0082838D  75 07                           jne 0x140828396
0082838F  BB 01 00 00 C0                  mov ebx, 0xc0000001
00828394  EB 73                           jmp 0x140828409
00828396  44 39 75 48                     cmp dword ptr [rbp + 0x48], r14d
0082839A  75 39                           jne 0x1408283d5
0082839C  48 8D 4F 0C                     lea rcx, [rdi + 0xc]
008283A0  4C 8D 45 DC                     lea r8, [rbp - 0x24]
008283A4  48 8D 55 D8                     lea rdx, [rbp - 0x28]
008283A8  E8 AB F4 FF FF                  call 0x140827858
008283AD  8B D8                           mov ebx, eax
008283AF  85 C0                           test eax, eax
008283B1  78 56                           js 0x140828409
008283B3  44 8B 4D D8                     mov r9d, dword ptr [rbp - 0x28]
008283B7  4C 8D 05 82 05 2E 00            lea r8, [rip + 0x2e0582]
008283BE  48 8B 4D 50                     mov rcx, qword ptr [rbp + 0x50]
008283C2  BA 6A 00 00 00                  mov edx, 0x6a
008283C7  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
008283CC  E8 6F 77 BE FF                  call 0x14040fb40
008283D1  8B D8                           mov ebx, eax
008283D3  EB 34                           jmp 0x140828409
008283D5  48 8D 57 0C                     lea rdx, [rdi + 0xc]
008283D9  48 83 C8 FF                     or rax, 0xffffffffffffffff
008283DD  48 FF C0                        inc rax
008283E0  66 44 39 34 42                  cmp word ptr [rdx + rax*2], r14w
008283E5  75 F6                           jne 0x1408283dd
008283E7  8D 04 45 02 00 00 00            lea eax, [rax*2 + 2]
008283EE  89 45 58                        mov dword ptr [rbp + 0x58], eax
008283F1  83 F8 6A                        cmp eax, 0x6a
008283F4  76 07                           jbe 0x1408283fd
008283F6  BB 23 00 00 C0                  mov ebx, 0xc0000023
008283FB  EB 0C                           jmp 0x140828409
008283FD  48 8B 4D 50                     mov rcx, qword ptr [rbp + 0x50]
00828401  44 8B C0                        mov r8d, eax
00828404  E8 37 E4 E9 FF                  call 0x1406c6840
00828409  4D 85 FF                        test r15, r15
0082840C  74 0A                           je 0x140828418
0082840E  33 D2                           xor edx, edx
00828410  49 8B CF                        mov rcx, r15
00828413  E8 58 A4 35 00                  call 0x140b82870
00828418  4D 85 E4                        test r12, r12
0082841B  74 0A                           je 0x140828427
0082841D  33 D2                           xor edx, edx
0082841F  49 8B CC                        mov rcx, r12
00828422  E8 49 A4 35 00                  call 0x140b82870
00828427  4D 85 ED                        test r13, r13
0082842A  74 0A                           je 0x140828436
0082842C  33 D2                           xor edx, edx
0082842E  49 8B CD                        mov rcx, r13
00828431  E8 3A A4 35 00                  call 0x140b82870
00828436  48 85 FF                        test rdi, rdi
00828439  74 0A                           je 0x140828445
0082843B  33 D2                           xor edx, edx
0082843D  48 8B CF                        mov rcx, rdi
00828440  E8 2B A4 35 00                  call 0x140b82870
00828445  48 85 F6                        test rsi, rsi
00828448  74 0A                           je 0x140828454
0082844A  33 D2                           xor edx, edx
0082844C  48 8B CE                        mov rcx, rsi
0082844F  E8 1C A4 35 00                  call 0x140b82870
00828454  8B C3                           mov eax, ebx
00828456  48 83 C4 58                     add rsp, 0x58
0082845A  41 5F                           pop r15
0082845C  41 5E                           pop r14
0082845E  41 5D                           pop r13
00828460  41 5C                           pop r12
00828462  5F                              pop rdi
00828463  5E                              pop rsi
00828464  5B                              pop rbx
00828465  5D                              pop rbp
00828466  C3                              ret
00828467  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SiGetEspFromFirmware(int a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m64;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned int v_stack_p8;

    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (88);
    v_r14 = 0;
    v_stack_p20 = 0;
    v_stack_m68 = 0;
    v_stack_m64 = 0;
    v_stack_m50 = 0;
    v_stack_m58 = 0;
    v_stack_m60 = 0;
    result = BiAcquirePrivilege(v_r14 + 22, v_stack_m50, a3, a4);
    if (sign_flag) goto loc_00828456;
    v_stack_p18 = 0;
    a1 = 0;
loc_00828126:
    result = ZwEnumerateBootEntries(a1, v_stack_p18, a3, a4);
    if (((unsigned int)(result)) != 0xC0000023ULL) goto loc_00828186;
    if (0 >= ((unsigned int)((unsigned int)(v_stack_p18)))) goto loc_0082837A;
    v_r14 = 0;
    result = (unsigned int)(v_stack_p18);
    if (0 != 0) {
        a2 = 0;
        a1 = 0;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
        result = v_stack_p18;
    }
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(result)), (unsigned int)(0x4B505953ULL), a4);
    if (result == 0) goto loc_0082817C;
    goto loc_00828126;
loc_0082817C:
    goto loc_0082837D;
loc_00828186:
    v_r14 = 0;
    if (sign_flag) goto loc_0082837D;
    if (v_stack_p18 != 0) goto loc_008281A1;
loc_00828197:
    goto loc_0082837D;
loc_008281A1:
    v_stack_p18 = 24;
loc_008281A9:
    result = 24;
    if (0 != 0) {
        a2 = 0;
        a1 = 0;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(0x4B505953ULL), a4);
        result = v_stack_p18;
    }
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(result)), (unsigned int)(0x4B505953ULL), a4);
    if (result == 0) goto loc_0082817C;
    result = ZwQueryBootOptions(result, v_stack_p18, (unsigned int)(0x4B505953ULL), a4);
    if (((unsigned int)(result)) != 0xC0000023ULL) goto loc_008281FF;
    if (((unsigned int)((unsigned int)(v_stack_p18))) >= ((unsigned int)((unsigned int)(v_stack_p18)))) goto loc_0082837A;
    v_r14 = 0;
    goto loc_008281A9;
loc_008281FF:
    v_r14 = 0;
    if (sign_flag) goto loc_0082837D;
    result = SiGetEfiBootEntryById(result, (unsigned int)(*(unsigned int *)(result + 12)), (unsigned int)(0x4B505953ULL), a4);
    if (result == 0) goto loc_00828259;
    result = SiBootEntryGetNtFilePath(result, v_stack_m58, (unsigned int)(0x4B505953ULL), a4);
    if (sign_flag) goto loc_00828259;
    result = SiIsValidWindowsBootEntry(result, v_stack_m58, (unsigned int)(0x4B505953ULL), a4);
    v_r14 = 0;
    if ((unsigned __int8)(result) != 0) goto loc_0082837D;
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m58, a2, (unsigned int)(0x4B505953ULL), a4);
    goto loc_0082825C;
loc_00828259:
    v_r14 = 0;
loc_0082825C:
    a1 = 0;
loc_0082825E:
    result = ZwQueryBootEntryOrder(a1, v_stack_p20, (unsigned int)(0x4B505953ULL), a4);
    if (((unsigned int)(result)) != 0xC0000023ULL) goto loc_008282BC;
    if (0 >= ((unsigned int)((unsigned int)(v_stack_p20)))) goto loc_0082837A;
    v_r14 = 0;
    result = (unsigned int)(v_stack_p20);
    if (0 != 0) {
        a2 = 0;
        a1 = 0;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(0x4B505953ULL), a4);
        result = v_stack_p20;
    }
    a2 = ((unsigned int)((unsigned int)(result))) << (2);
    result = ExAllocatePool2(256, a2, (unsigned int)(0x4B505953ULL), a4);
    if (result == 0) goto loc_0082817C;
    goto loc_0082825E;
loc_008282BC:
    v_r14 = 0;
    if ((unsigned int)((unsigned int)((unsigned int)(result))) != 0) goto loc_0082837D;
    if (v_stack_p20 == 0) goto loc_00828197;
loc_008282D4:
    if (0 >= v_stack_p20) goto loc_00828367;
    result = SiGetEfiBootEntryById(result, (unsigned int)(*(unsigned int *)(result + 0 * 4)), (unsigned int)(0x4B505953ULL), a4);
    if (result == 0) goto loc_0082835D;
    result = SiBootEntryGetNtFilePath(result, v_stack_m60, (unsigned int)(0x4B505953ULL), a4);
    if (sign_flag) goto loc_00828342;
    result = SiIsValidWindowsBootEntry(result, v_stack_m60, (unsigned int)(0x4B505953ULL), a4);
    v_r14 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_00828345;
    if (0 == 0) goto loc_00828336;
    result = wcsicmp(0 + 12, v_stack_m60 + 12, (unsigned int)(0x4B505953ULL), a4);
    if ((unsigned int)(result) == 0) goto loc_00828345;
    goto loc_0082837D;
loc_00828336:
    v_stack_m60 = 0;
    goto loc_00828345;
loc_00828342:
    v_r14 = 0;
loc_00828345:
    if (0 == 0) goto loc_00828360;
    a2 = 0;
    result = ExFreePoolWithTag(0, a2, (unsigned int)(0x4B505953ULL), a4);
    v_stack_m60 = 0;
    goto loc_00828360;
loc_0082835D:
    v_r14 = 0;
loc_00828360:
    v_rbx = (unsigned int)(((unsigned int)(0xC0000451ULL)) + 1);
    goto loc_008282D4;
loc_00828367:
    result = -(v_stack_m60);
    a1 = (unsigned int)(~(0));
    v_rbx = (unsigned int)(((unsigned int)(0xC0000225ULL)) & (a1));
    goto loc_0082837D;
loc_0082837A:
    v_r14 = 0;
loc_0082837D:
    result = BiReleasePrivilege(v_stack_m50, a2, (unsigned int)(0x4B505953ULL), a4);
    if (sign_flag) goto loc_00828409;
    if (v_stack_m60 != 0) goto loc_00828396;
    goto loc_00828409;
loc_00828396:
    if (v_stack_p8 != 0) goto loc_008283D5;
    result = SiGetDeviceNumberInformation(v_stack_m60 + 12, v_stack_m68, v_stack_m64, a4);
    if (sign_flag) goto loc_00828409;
    v_stack_m78 = 0;
    result = RtlStringCbPrintfW(v_stack_p10, 106, v_rip + 3016066, (unsigned int)(v_stack_m68));
    goto loc_00828409;
loc_008283D5:
    result = (result) | (-1);
loc_008283DD:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(v_stack_m60 + 12 + result * 2)) != 0) goto loc_008283DD;
    v_stack_p18 = (unsigned int)(result * 2 + 2);
    if (((unsigned int)(result * 2 + 2)) <= 106) goto loc_008283FD;
    goto loc_00828409;
loc_008283FD:
    result = memcpy(v_stack_p10, v_stack_m60 + 12, (unsigned int)((unsigned int)(result * 2 + 2)), (unsigned int)(v_stack_m68));
loc_00828409:
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)((unsigned int)(result * 2 + 2)), (unsigned int)(v_stack_m68));
    }
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)((unsigned int)(result * 2 + 2)), (unsigned int)(v_stack_m68));
    }
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)((unsigned int)(result * 2 + 2)), (unsigned int)(v_stack_m68));
    }
    if (v_stack_m60 != 0) {
        a2 = 0;
        a1 = v_stack_m60;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)((unsigned int)(result * 2 + 2)), (unsigned int)(v_stack_m68));
    }
    if (0 != 0) {
        a2 = 0;
        a1 = 0;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)((unsigned int)(result * 2 + 2)), (unsigned int)(v_stack_m68));
    }
loc_00828456:
    v_rsp = (v_rsp) + (88);
    return (unsigned int)((unsigned int)((unsigned int)(0xC0000023ULL)));
}
```

## 5. (Beta) C Style

```c
int64_t SiGetEspFromFirmware(int32_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint32_t v_stack_m64;
    uint32_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint32_t v_stack_p8;

    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (88);
    local_r14 = 0;
    v_stack_p20 = 0;
    v_stack_m68 = 0;
    v_stack_m64 = 0;
    v_stack_m50 = 0;
    v_stack_m58 = 0;
    v_stack_m60 = 0;
    result = BiAcquirePrivilege(local_r14 + 22, v_stack_m50, Arg3, a4);
    if (sign_flag) goto loc_00828456;
    v_stack_p18 = 0;
    Arg1 = 0;
loc_00828126:
    result = ZwEnumerateBootEntries(Arg1, v_stack_p18, Arg3, a4);
    if (((uint32_t)(result)) != 0xC0000023ULL) goto loc_00828186;
    if (0 >= ((uint32_t)((uint32_t)(v_stack_p18)))) goto loc_0082837A;
    local_r14 = 0;
    result = (uint32_t)(v_stack_p18);
    if (0 != 0) {
        Arg2 = 0;
        Arg1 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, a4);
        result = v_stack_p18;
    }
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(result)), (uint32_t)(0x4B505953ULL), a4);
    if (result == 0) goto loc_0082817C;
    goto loc_00828126;
loc_0082817C:
    goto loc_0082837D;
loc_00828186:
    local_r14 = 0;
    if (sign_flag) goto loc_0082837D;
    if (v_stack_p18 != 0) goto loc_008281A1;
loc_00828197:
    goto loc_0082837D;
loc_008281A1:
    v_stack_p18 = 24;
loc_008281A9:
    result = 24;
    if (0 != 0) {
        Arg2 = 0;
        Arg1 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)(0x4B505953ULL), a4);
        result = v_stack_p18;
    }
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(result)), (uint32_t)(0x4B505953ULL), a4);
    if (result == 0) goto loc_0082817C;
    result = ZwQueryBootOptions(result, v_stack_p18, (uint32_t)(0x4B505953ULL), a4);
    if (((uint32_t)(result)) != 0xC0000023ULL) goto loc_008281FF;
    if (((uint32_t)((uint32_t)(v_stack_p18))) >= ((uint32_t)((uint32_t)(v_stack_p18)))) goto loc_0082837A;
    local_r14 = 0;
    goto loc_008281A9;
loc_008281FF:
    local_r14 = 0;
    if (sign_flag) goto loc_0082837D;
    result = SiGetEfiBootEntryById(result, (uint32_t)(*(uint32_t *)(result + 0xC)), (uint32_t)(0x4B505953ULL), a4);
    if (result == 0) goto loc_00828259;
    result = SiBootEntryGetNtFilePath(result, v_stack_m58, (uint32_t)(0x4B505953ULL), a4);
    if (sign_flag) goto loc_00828259;
    result = SiIsValidWindowsBootEntry(result, v_stack_m58, (uint32_t)(0x4B505953ULL), a4);
    local_r14 = 0;
    if ((uint8_t)(result) != 0) goto loc_0082837D;
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m58, Arg2, (uint32_t)(0x4B505953ULL), a4);
    goto loc_0082825C;
loc_00828259:
    local_r14 = 0;
loc_0082825C:
    Arg1 = 0;
loc_0082825E:
    result = ZwQueryBootEntryOrder(Arg1, v_stack_p20, (uint32_t)(0x4B505953ULL), a4);
    if (((uint32_t)(result)) != 0xC0000023ULL) goto loc_008282BC;
    if (0 >= ((uint32_t)((uint32_t)(v_stack_p20)))) goto loc_0082837A;
    local_r14 = 0;
    result = (uint32_t)(v_stack_p20);
    if (0 != 0) {
        Arg2 = 0;
        Arg1 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)(0x4B505953ULL), a4);
        result = v_stack_p20;
    }
    Arg2 = ((uint32_t)((uint32_t)(result))) << (2);
    result = ExAllocatePool2(256, Arg2, (uint32_t)(0x4B505953ULL), a4);
    if (result == 0) goto loc_0082817C;
    goto loc_0082825E;
loc_008282BC:
    local_r14 = 0;
    if ((uint32_t)((uint32_t)((uint32_t)(result))) != 0) goto loc_0082837D;
    if (v_stack_p20 == 0) goto loc_00828197;
loc_008282D4:
    if (0 >= v_stack_p20) goto loc_00828367;
    result = SiGetEfiBootEntryById(result, (uint32_t)(*(uint32_t *)(result + 0x0 * 4)), (uint32_t)(0x4B505953ULL), a4);
    if (result == 0) goto loc_0082835D;
    result = SiBootEntryGetNtFilePath(result, v_stack_m60, (uint32_t)(0x4B505953ULL), a4);
    if (sign_flag) goto loc_00828342;
    result = SiIsValidWindowsBootEntry(result, v_stack_m60, (uint32_t)(0x4B505953ULL), a4);
    local_r14 = 0;
    if ((uint8_t)(result) == 0) goto loc_00828345;
    if (0 == 0) goto loc_00828336;
    result = wcsicmp(0 + 12, v_stack_m60 + 12, (uint32_t)(0x4B505953ULL), a4);
    if ((uint32_t)(result) == 0) goto loc_00828345;
    goto loc_0082837D;
loc_00828336:
    v_stack_m60 = 0;
    goto loc_00828345;
loc_00828342:
    local_r14 = 0;
loc_00828345:
    if (0 == 0) goto loc_00828360;
    Arg2 = 0;
    result = ExFreePoolWithTag(0, Arg2, (uint32_t)(0x4B505953ULL), a4);
    v_stack_m60 = 0;
    goto loc_00828360;
loc_0082835D:
    local_r14 = 0;
loc_00828360:
    local_rbx = (uint32_t)(((uint32_t)(0xC0000451ULL)) + 1);
    goto loc_008282D4;
loc_00828367:
    result = -(v_stack_m60);
    Arg1 = (uint32_t)(~(0));
    local_rbx = (uint32_t)(((uint32_t)(0xC0000225ULL)) & (Arg1));
    goto loc_0082837D;
loc_0082837A:
    local_r14 = 0;
loc_0082837D:
    result = BiReleasePrivilege(v_stack_m50, Arg2, (uint32_t)(0x4B505953ULL), a4);
    if (sign_flag) goto loc_00828409;
    if (v_stack_m60 != 0) goto loc_00828396;
    goto loc_00828409;
loc_00828396:
    if (v_stack_p8 != 0) goto loc_008283D5;
    result = SiGetDeviceNumberInformation(v_stack_m60 + 12, v_stack_m68, v_stack_m64, a4);
    if (sign_flag) goto loc_00828409;
    v_stack_m78 = 0;
    result = RtlStringCbPrintfW(v_stack_p10, 106, v_rip + 3016066, (uint32_t)(v_stack_m68));
    goto loc_00828409;
loc_008283D5:
    result = (result) | (-1);
loc_008283DD:
    result = (result) + 1;
    if ((*(uint16_t *)(v_stack_m60 + 0xC + result * 2)) != 0) goto loc_008283DD;
    v_stack_p18 = (uint32_t)(result * 2 + 2);
    if (((uint32_t)(result * 2 + 2)) <= 106) goto loc_008283FD;
    goto loc_00828409;
loc_008283FD:
    result = memcpy(v_stack_p10, v_stack_m60 + 12, (uint32_t)((uint32_t)(result * 2 + 2)), (uint32_t)(v_stack_m68));
loc_00828409:
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)((uint32_t)(result * 2 + 2)), (uint32_t)(v_stack_m68));
    }
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)((uint32_t)(result * 2 + 2)), (uint32_t)(v_stack_m68));
    }
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)((uint32_t)(result * 2 + 2)), (uint32_t)(v_stack_m68));
    }
    if (v_stack_m60 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m60;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)((uint32_t)(result * 2 + 2)), (uint32_t)(v_stack_m68));
    }
    if (0 != 0) {
        Arg2 = 0;
        Arg1 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)((uint32_t)(result * 2 + 2)), (uint32_t)(v_stack_m68));
    }
loc_00828456:
    local_rsp = (local_rsp) + (88);
    return (uint32_t)((uint32_t)((uint32_t)(0xC0000023ULL)));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008280C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
