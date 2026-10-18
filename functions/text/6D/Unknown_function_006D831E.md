# sub_006D831E

- RVA: `0x006D831E`–`0x006D8C29` (길이 `2,315` bytes)
- VA: `0x00000001406D831E`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063804`
- 디코드: `545`개 명령, `2,315/2,315` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **30**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x006D8356` → [KiSelectIdleProcessor](../3F/KiSelectIdleProcessor_function_003FE160.md) (function, `0x003FE160`)
- `0x006D83CF` → [KiSelectIdleProcessor](../3F/KiSelectIdleProcessor_function_003FE160.md) (function, `0x003FE160`)
- `0x006D8438` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x006D848D` → [KiFindRankBiasedIdleSmtSet](../3F/KiFindRankBiasedIdleSmtSet_function_003FE40C.md) (function, `0x003FE40C`)
- `0x006D84BF` → [KiReduceByEffectiveIdleSmtSet](../25/KiReduceByEffectiveIdleSmtSet_function_00256E00.md) (function, `0x00256E00`)
- `0x006D84FE` → [RtlCopyVolatileMemory](../6B/RtlCopyVolatileMemory_function_006BC9D0.md) (function, `0x006BC9D0`)
- `0x006D850D` → [KiReduceAffinityToRankListMinimums](../39/KiReduceAffinityToRankListMinimums_function_0039EFA0.md) (function, `0x0039EFA0`)
- `0x006D85E4` → [KeInitializeSchedulerSubNodeEnumerationContext](../41/KeInitializeSchedulerSubNodeEnumerationContext_function_0041E4B0.md) (function, `0x0041E4B0`)
- `0x006D85F1` → [KeEnumerateNextSchedulerSubNodeInNode](../25/KeEnumerateNextSchedulerSubNodeInNode_function_002566D8.md) (function, `0x002566D8`)
- `0x006D8636` → [KiSelectIdleProcessor](../3F/KiSelectIdleProcessor_function_003FE160.md) (function, `0x003FE160`)
- `0x006D86A3` → [KiEnumerateNextNodeInSystem](../44/KiEnumerateNextNodeInSystem_function_0044BC00.md) (function, `0x0044BC00`)
- `0x006D8702` → [KeInitializeSchedulerSubNodeEnumerationContext](../41/KeInitializeSchedulerSubNodeEnumerationContext_function_0041E4B0.md) (function, `0x0041E4B0`)
- `0x006D870F` → [KeEnumerateNextSchedulerSubNodeInNode](../25/KeEnumerateNextSchedulerSubNodeInNode_function_002566D8.md) (function, `0x002566D8`)
- `0x006D8756` → [KiSelectIdleProcessor](../3F/KiSelectIdleProcessor_function_003FE160.md) (function, `0x003FE160`)
- `0x006D87B3` → [KeIsEmptyAffinityEx](../2D/KeIsEmptyAffinityEx_function_002D1580.md) (function, `0x002D1580`)
- `0x006D87D8` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x006D881C` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x006D8832` → [KiCopyAffinityEx](../2C/KiCopyAffinityEx_function_002CE860.md) (function, `0x002CE860`)
- `0x006D884B` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x006D88A2` → [KiFindRankBiasedIdleSmtSet](../3F/KiFindRankBiasedIdleSmtSet_function_003FE40C.md) (function, `0x003FE40C`)
- `0x006D88D4` → [KiReduceByEffectiveIdleSmtSet](../25/KiReduceByEffectiveIdleSmtSet_function_00256E00.md) (function, `0x00256E00`)
- `0x006D8913` → [RtlCopyVolatileMemory](../6B/RtlCopyVolatileMemory_function_006BC9D0.md) (function, `0x006BC9D0`)
- `0x006D8922` → [KiReduceAffinityToRankListMinimums](../39/KiReduceAffinityToRankListMinimums_function_0039EFA0.md) (function, `0x0039EFA0`)
- `0x006D8A86` → [KiSelectIdleProcessor](../3F/KiSelectIdleProcessor_function_003FE160.md) (function, `0x003FE160`)
- `0x006D8B0C` → [KiSelectIdleProcessor](../3F/KiSelectIdleProcessor_function_003FE160.md) (function, `0x003FE160`)
- `0x006D8B50` → [KeIsEmptyAffinityEx](../2D/KeIsEmptyAffinityEx_function_002D1580.md) (function, `0x002D1580`)
- `0x006D8B6B` → [KiInitializeSystemSubNodeEnumerationContext](../42/KiInitializeSystemSubNodeEnumerationContext_function_0042798C.md) (function, `0x0042798C`)
- `0x006D8B78` → [KiEnumerateNextSchedulerSubNodeInSystem](../25/KiEnumerateNextSchedulerSubNodeInSystem_function_002569C0.md) (function, `0x002569C0`)
- `0x006D8BBD` → [KiSelectIdleProcessor](../3F/KiSelectIdleProcessor_function_003FE160.md) (function, `0x003FE160`)
- `0x006D8BFE` → [KeIsEmptyAffinityEx](../2D/KeIsEmptyAffinityEx_function_002D1580.md) (function, `0x002D1580`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006D84DF` → RVA `0x00FC6D18` (`ALMOSTRO`; read)
- `0x006D8546` → RVA `0x00FC5084` (`ALMOSTRO`; read)
- `0x006D8590` → RVA `0x00F231B8` (`.data`; read)
- `0x006D859C` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x006D86CC` → RVA `0x00FC6B38` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **19**
  - `0x006D832A` → [KiChooseTargetProcessor + 0x46F](../25/KiChooseTargetProcessor_function_002556D8.md) (`tail-transfer`)
  - `0x006D8335` → [KiChooseTargetProcessor + 0x46F](../25/KiChooseTargetProcessor_function_002556D8.md) (`tail-transfer`)
  - `0x006D8364` → [KiChooseTargetProcessor + 0x2DC](../25/KiChooseTargetProcessor_function_002556D8.md) (`tail-transfer`)
  - `0x006D8378` → [KiChooseTargetProcessor + 0x46F](../25/KiChooseTargetProcessor_function_002556D8.md) (`tail-transfer`)
  - `0x006D8392` → [KiChooseTargetProcessor + 0x46F](../25/KiChooseTargetProcessor_function_002556D8.md) (`tail-transfer`)
  - `0x006D83A3` → [KiChooseTargetProcessor + 0x783](../25/KiChooseTargetProcessor_function_002556D8.md) (`tail-transfer`)
  - `0x006D83AE` → [KiChooseTargetProcessor + 0x783](../25/KiChooseTargetProcessor_function_002556D8.md) (`tail-transfer`)
  - `0x006D83DD` → [KiChooseTargetProcessor + 0x86D](../25/KiChooseTargetProcessor_function_002556D8.md) (`tail-transfer`)
  - `0x006D83F1` → [KiChooseTargetProcessor + 0x783](../25/KiChooseTargetProcessor_function_002556D8.md) (`tail-transfer`)
  - `0x006D840B` → [KiChooseTargetProcessor + 0x783](../25/KiChooseTargetProcessor_function_002556D8.md) (`tail-transfer`)
  - `0x006D868B` → [KiChooseTargetProcessor + 0x32C](../25/KiChooseTargetProcessor_function_002556D8.md) (`tail-transfer`)
  - `0x006D8696` → [KiChooseTargetProcessor + 0x304](../25/KiChooseTargetProcessor_function_002556D8.md) (`tail-transfer`)
  - `0x006D86AA` → [KiChooseTargetProcessor + 0x32C](../25/KiChooseTargetProcessor_function_002556D8.md) (`tail-transfer`)
  - `0x006D87A6` → [KiChooseTargetProcessor + 0x97F](../25/KiChooseTargetProcessor_function_002556D8.md) (`tail-transfer`)
  - `0x006D87BD` → [KiChooseTargetProcessor + 0x338](../25/KiChooseTargetProcessor_function_002556D8.md) (`tail-transfer`)
  - `0x006D8956` → [KiChooseTargetProcessor + 0x984](../25/KiChooseTargetProcessor_function_002556D8.md) (`tail-transfer`)
  - `0x006D8C12` → [KiChooseTargetProcessor + 0x338](../25/KiChooseTargetProcessor_function_002556D8.md) (`tail-transfer`)
  - `0x006D8C1B` → [KiChooseTargetProcessor + 0x97F](../25/KiChooseTargetProcessor_function_002556D8.md) (`tail-transfer`)
  - `0x006D8C24` → [KiChooseTargetProcessor + 0x32C](../25/KiChooseTargetProcessor_function_002556D8.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006D831E  0F B7 87 88 00 00 00            movzx eax, word ptr [rdi + 0x88]
006D8325  66 41 3B 04 24                  cmp ax, word ptr [r12]
006D832A  0F 83 17 D8 B7 FF               jae 0x140255b47
006D8330  4D 39 5C C4 08                  cmp qword ptr [r12 + rax*8 + 8], r11
006D8335  0F 84 0C D8 B7 FF               je 0x140255b47
006D833B  48 8D 44 24 30                  lea rax, [rsp + 0x30]
006D8340  4C 8B CF                        mov r9, rdi
006D8343  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
006D8348  4D 8B C7                        mov r8, r15
006D834B  49 8B D5                        mov rdx, r13
006D834E  4C 89 5C 24 20                  mov qword ptr [rsp + 0x20], r11
006D8353  49 8B CC                        mov rcx, r12
006D8356  E8 05 5E D2 FF                  call 0x1403fe160
006D835B  45 33 DB                        xor r11d, r11d
006D835E  48 8B D8                        mov rbx, rax
006D8361  48 85 C0                        test rax, rax
006D8364  0F 85 4A D6 B7 FF               jne 0x1402559b4
006D836A  0F B7 87 88 00 00 00            movzx eax, word ptr [rdi + 0x88]
006D8371  66 39 85 80 00 00 00            cmp word ptr [rbp + 0x80], ax
006D8378  0F 86 C9 D7 B7 FF               jbe 0x140255b47
006D837E  8B C8                           mov ecx, eax
006D8380  48 8B 87 80 00 00 00            mov rax, qword ptr [rdi + 0x80]
006D8387  48 F7 D0                        not rax
006D838A  48 21 84 CD 88 00 00 00         and qword ptr [rbp + rcx*8 + 0x88], rax
006D8392  E9 B0 D7 B7 FF                  jmp 0x140255b47
006D8397  0F B7 87 88 00 00 00            movzx eax, word ptr [rdi + 0x88]
006D839E  66 41 3B 04 24                  cmp ax, word ptr [r12]
006D83A3  0F 83 B2 DA B7 FF               jae 0x140255e5b
006D83A9  4D 39 5C C4 08                  cmp qword ptr [r12 + rax*8 + 8], r11
006D83AE  0F 84 A7 DA B7 FF               je 0x140255e5b
006D83B4  48 8D 44 24 30                  lea rax, [rsp + 0x30]
006D83B9  4C 8B CF                        mov r9, rdi
006D83BC  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
006D83C1  4D 8B C7                        mov r8, r15
006D83C4  49 8B D5                        mov rdx, r13
006D83C7  4C 89 5C 24 20                  mov qword ptr [rsp + 0x20], r11
006D83CC  49 8B CC                        mov rcx, r12
006D83CF  E8 8C 5D D2 FF                  call 0x1403fe160
006D83D4  45 33 DB                        xor r11d, r11d
006D83D7  48 8B D8                        mov rbx, rax
006D83DA  48 85 C0                        test rax, rax
006D83DD  0F 85 62 DB B7 FF               jne 0x140255f45
006D83E3  0F B7 87 88 00 00 00            movzx eax, word ptr [rdi + 0x88]
006D83EA  66 39 85 80 00 00 00            cmp word ptr [rbp + 0x80], ax
006D83F1  0F 86 64 DA B7 FF               jbe 0x140255e5b
006D83F7  8B C8                           mov ecx, eax
006D83F9  48 8B 87 80 00 00 00            mov rax, qword ptr [rdi + 0x80]
006D8400  48 F7 D0                        not rax
006D8403  48 21 84 CD 88 00 00 00         and qword ptr [rbp + rcx*8 + 0x88], rax
006D840B  E9 4B DA B7 FF                  jmp 0x140255e5b
006D8410  41 8B F3                        mov esi, r11d
006D8413  3B 74 24 40                     cmp esi, dword ptr [rsp + 0x40]
006D8417  4C 8B 75 98                     mov r14, qword ptr [rbp - 0x68]
006D841B  0F 4F FE                        cmovg edi, esi
006D841E  89 7C 24 34                     mov dword ptr [rsp + 0x34], edi
006D8422  4D 85 F6                        test r14, r14
006D8425  0F 84 B1 01 00 00               je 0x1406d85dc
006D842B  33 D2                           xor edx, edx
006D842D  48 8D 8D 20 03 00 00            lea rcx, [rbp + 0x320]
006D8434  44 8D 42 40                     lea r8d, [rdx + 0x40]
006D8438  E8 03 E8 FE FF                  call 0x1406c6c40
006D843D  41 0F B7 86 88 00 00 00         movzx eax, word ptr [r14 + 0x88]
006D8445  45 33 DB                        xor r11d, r11d
006D8448  66 41 3B 04 24                  cmp ax, word ptr [r12]
006D844D  73 07                           jae 0x1406d8456
006D844F  49 8B 4C C4 08                  mov rcx, qword ptr [r12 + rax*8 + 8]
006D8454  EB 03                           jmp 0x1406d8459
006D8456  49 8B CB                        mov rcx, r11
006D8459  49 8B 7E 08                     mov rdi, qword ptr [r14 + 8]
006D845D  48 63 44 24 34                  movsxd rax, dword ptr [rsp + 0x34]
006D8462  49 8B 5C C6 10                  mov rbx, qword ptr [r14 + rax*8 + 0x10]
006D8467  48 23 DF                        and rbx, rdi
006D846A  48 23 D9                        and rbx, rcx
006D846D  48 89 5C 24 78                  mov qword ptr [rsp + 0x78], rbx
006D8472  74 57                           je 0x1406d84cb
006D8474  41 F6 86 B8 00 00 00 01         test byte ptr [r14 + 0xb8], 1
006D847C  74 6C                           je 0x1406d84ea
006D847E  44 38 5C 24 30                  cmp byte ptr [rsp + 0x30], r11b
006D8483  74 14                           je 0x1406d8499
006D8485  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
006D848A  49 8B CE                        mov rcx, r14
006D848D  E8 7A 5F D2 FF                  call 0x1403fe40c
006D8492  45 33 DB                        xor r11d, r11d
006D8495  84 C0                           test al, al
006D8497  75 2B                           jne 0x1406d84c4
006D8499  49 8B 4E 18                     mov rcx, qword ptr [r14 + 0x18]
006D849D  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
006D84A2  48 23 CB                        and rcx, rbx
006D84A5  75 2C                           jne 0x1406d84d3
006D84A7  44 38 5C 24 30                  cmp byte ptr [rsp + 0x30], r11b
006D84AC  75 1D                           jne 0x1406d84cb
006D84AE  4D 39 B5 C0 00 00 00            cmp qword ptr [r13 + 0xc0], r14
006D84B5  75 33                           jne 0x1406d84ea
006D84B7  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
006D84BC  49 8B CD                        mov rcx, r13
006D84BF  E8 3C E9 B7 FF                  call 0x140256e00
006D84C4  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
006D84C9  EB 1F                           jmp 0x1406d84ea
006D84CB  49 8B DB                        mov rbx, r11
006D84CE  E9 E4 00 00 00                  jmp 0x1406d85b7
006D84D3  44 38 5C 24 30                  cmp byte ptr [rsp + 0x30], r11b
006D84D8  74 0D                           je 0x1406d84e7
006D84DA  F3 48 0F B8 C7                  popcnt rax, rdi
006D84DF  3B 05 33 E8 8E 00               cmp eax, dword ptr [rip + 0x8ee833]
006D84E5  72 E4                           jb 0x1406d84cb
006D84E7  48 8B D9                        mov rbx, rcx
006D84EA  49 8D 96 40 02 00 00            lea rdx, [r14 + 0x240]
006D84F1  41 B8 40 00 00 00               mov r8d, 0x40
006D84F7  48 8D 8D 20 03 00 00            lea rcx, [rbp + 0x320]
006D84FE  E8 CD 44 FE FF                  call 0x1406bc9d0
006D8503  48 8D 95 20 03 00 00            lea rdx, [rbp + 0x320]
006D850A  48 8B CB                        mov rcx, rbx
006D850D  E8 8E 6A CC FF                  call 0x14039efa0
006D8512  48 8B D0                        mov rdx, rax
006D8515  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
006D851A  49 85 85 C8 00 00 00            test qword ptr [r13 + 0xc8], rax
006D8521  74 0B                           je 0x1406d852e
006D8523  49 8B DD                        mov rbx, r13
006D8526  45 33 DB                        xor r11d, r11d
006D8529  E9 80 00 00 00                  jmp 0x1406d85ae
006D852E  4D 8B 85 60 8E 00 00            mov r8, qword ptr [r13 + 0x8e60]
006D8535  4C 23 C2                        and r8, rdx
006D8538  75 2F                           jne 0x1406d8569
006D853A  4D 8B 85 78 8E 00 00            mov r8, qword ptr [r13 + 0x8e78]
006D8541  4C 23 C2                        and r8, rdx
006D8544  75 23                           jne 0x1406d8569
006D8546  8B 05 38 CB 8E 00               mov eax, dword ptr [rip + 0x8ecb38]
006D854C  4C 8B C2                        mov r8, rdx
006D854F  A8 01                           test al, 1
006D8551  74 1B                           je 0x1406d856e
006D8553  49 8B 85 70 8E 00 00            mov rax, qword ptr [r13 + 0x8e70]
006D855A  48 23 C2                        and rax, rdx
006D855D  74 0F                           je 0x1406d856e
006D855F  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
006D8564  4C 8B C0                        mov r8, rax
006D8567  EB 05                           jmp 0x1406d856e
006D8569  4C 89 44 24 78                  mov qword ptr [rsp + 0x78], r8
006D856E  41 0F B6 8D D1 00 00 00         movzx ecx, byte ptr [r13 + 0xd1]
006D8576  45 33 DB                        xor r11d, r11d
006D8579  41 0F B6 95 D0 00 00 00         movzx edx, byte ptr [r13 + 0xd0]
006D8581  49 D3 C8                        ror r8, cl
006D8584  49 0F BC C0                     bsf rax, r8
006D8588  C1 E2 06                        shl edx, 6
006D858B  03 C8                           add ecx, eax
006D858D  89 45 E0                        mov dword ptr [rbp - 0x20], eax
006D8590  48 8B 05 21 AC 84 00            mov rax, qword ptr [rip + 0x84ac21]
006D8597  83 E1 3F                        and ecx, 0x3f
006D859A  03 D1                           add edx, ecx
006D859C  48 8D 0D 5D 7A 92 FF            lea rcx, [rip - 0x6d85a3]
006D85A3  8B 04 90                        mov eax, dword ptr [rax + rdx*4]
006D85A6  48 8B 9C C1 40 8C FC 00         mov rbx, qword ptr [rcx + rax*8 + 0xfc8c40]
006D85AE  48 85 DB                        test rbx, rbx
006D85B1  0F 85 C9 00 00 00               jne 0x1406d8680
006D85B7  41 0F B7 86 88 00 00 00         movzx eax, word ptr [r14 + 0x88]
006D85BF  66 39 85 80 00 00 00            cmp word ptr [rbp + 0x80], ax
006D85C6  76 14                           jbe 0x1406d85dc
006D85C8  8B C8                           mov ecx, eax
006D85CA  49 8B 86 80 00 00 00            mov rax, qword ptr [r14 + 0x80]
006D85D1  48 F7 D0                        not rax
006D85D4  48 21 84 CD 88 00 00 00         and qword ptr [rbp + rcx*8 + 0x88], rax
006D85DC  48 8B 55 B0                     mov rdx, qword ptr [rbp - 0x50]
006D85E0  48 8D 4D 28                     lea rcx, [rbp + 0x28]
006D85E4  E8 C7 5E D4 FF                  call 0x14041e4b0
006D85E9  48 8D 55 E8                     lea rdx, [rbp - 0x18]
006D85ED  48 8D 4D 28                     lea rcx, [rbp + 0x28]
006D85F1  E8 E2 E0 B7 FF                  call 0x1402566d8
006D85F6  45 33 DB                        xor r11d, r11d
006D85F9  85 C0                           test eax, eax
006D85FB  75 72                           jne 0x1406d866f
006D85FD  48 8B 7D E8                     mov rdi, qword ptr [rbp - 0x18]
006D8601  49 3B FE                        cmp rdi, r14
006D8604  74 E3                           je 0x1406d85e9
006D8606  0F B7 87 88 00 00 00            movzx eax, word ptr [rdi + 0x88]
006D860D  66 41 3B 04 24                  cmp ax, word ptr [r12]
006D8612  73 D5                           jae 0x1406d85e9
006D8614  4D 39 5C C4 08                  cmp qword ptr [r12 + rax*8 + 8], r11
006D8619  74 CE                           je 0x1406d85e9
006D861B  48 8D 44 24 30                  lea rax, [rsp + 0x30]
006D8620  4C 8B CF                        mov r9, rdi
006D8623  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
006D8628  4D 8B C7                        mov r8, r15
006D862B  49 8B D5                        mov rdx, r13
006D862E  4C 89 5C 24 20                  mov qword ptr [rsp + 0x20], r11
006D8633  49 8B CC                        mov rcx, r12
006D8636  E8 25 5B D2 FF                  call 0x1403fe160
006D863B  45 33 DB                        xor r11d, r11d
006D863E  48 8B D8                        mov rbx, rax
006D8641  48 85 C0                        test rax, rax
006D8644  75 3A                           jne 0x1406d8680
006D8646  0F B7 87 88 00 00 00            movzx eax, word ptr [rdi + 0x88]
006D864D  66 39 85 80 00 00 00            cmp word ptr [rbp + 0x80], ax
006D8654  76 93                           jbe 0x1406d85e9
006D8656  8B C8                           mov ecx, eax
006D8658  48 8B 87 80 00 00 00            mov rax, qword ptr [rdi + 0x80]
006D865F  48 F7 D0                        not rax
006D8662  48 21 84 CD 88 00 00 00         and qword ptr [rbp + rcx*8 + 0x88], rax
006D866A  E9 7A FF FF FF                  jmp 0x1406d85e9
006D866F  3B 74 24 40                     cmp esi, dword ptr [rsp + 0x40]
006D8673  7E 0B                           jle 0x1406d8680
006D8675  FF CE                           dec esi
006D8677  89 74 24 34                     mov dword ptr [rsp + 0x34], esi
006D867B  E9 A2 FD FF FF                  jmp 0x1406d8422
006D8680  8B 7C 24 40                     mov edi, dword ptr [rsp + 0x40]
006D8684  89 7C 24 34                     mov dword ptr [rsp + 0x34], edi
006D8688  48 85 DB                        test rbx, rbx
006D868B  0F 85 73 D3 B7 FF               jne 0x140255a04
006D8691  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
006D8696  E9 41 D3 B7 FF                  jmp 0x1402559dc
006D869B  48 8D 55 F0                     lea rdx, [rbp - 0x10]
006D869F  48 8D 4D A8                     lea rcx, [rbp - 0x58]
006D86A3  E8 58 35 D7 FF                  call 0x14044bc00
006D86A8  85 C0                           test eax, eax
006D86AA  0F 85 54 D3 B7 FF               jne 0x140255a04
006D86B0  4C 8B 7D F0                     mov r15, qword ptr [rbp - 0x10]
006D86B4  4C 3B 7D B0                     cmp r15, qword ptr [rbp - 0x50]
006D86B8  74 E1                           je 0x1406d869b
006D86BA  4C 3B 7D B8                     cmp r15, qword ptr [rbp - 0x48]
006D86BE  74 DB                           je 0x1406d869b
006D86C0  4C 3B 7D C0                     cmp r15, qword ptr [rbp - 0x40]
006D86C4  74 D5                           je 0x1406d869b
006D86C6  33 C0                           xor eax, eax
006D86C8  4C 89 5D A0                     mov qword ptr [rbp - 0x60], r11
006D86CC  F7 05 62 E4 8E 00 00 00 80 00   test dword ptr [rip + 0x8ee462], 0x800000
006D86D6  0F 57 C0                        xorps xmm0, xmm0
006D86D9  0F 11 45 40                     movups xmmword ptr [rbp + 0x40], xmm0
006D86DD  48 89 45 50                     mov qword ptr [rbp + 0x50], rax
006D86E1  49 8B DB                        mov rbx, r11
006D86E4  74 07                           je 0x1406d86ed
006D86E6  41 F6 47 0A 08                  test byte ptr [r15 + 0xa], 8
006D86EB  75 03                           jne 0x1406d86f0
006D86ED  41 8B F3                        mov esi, r11d
006D86F0  3B F7                           cmp esi, edi
006D86F2  8B C7                           mov eax, edi
006D86F4  0F 4F C6                        cmovg eax, esi
006D86F7  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
006D86FB  49 8B D7                        mov rdx, r15
006D86FE  48 8D 4D 40                     lea rcx, [rbp + 0x40]
006D8702  E8 A9 5D D4 FF                  call 0x14041e4b0
006D8707  48 8D 55 A0                     lea rdx, [rbp - 0x60]
006D870B  48 8D 4D 40                     lea rcx, [rbp + 0x40]
006D870F  E8 C4 DF B7 FF                  call 0x1402566d8
006D8714  33 D2                           xor edx, edx
006D8716  85 C0                           test eax, eax
006D8718  75 73                           jne 0x1406d878d
006D871A  4C 8B 75 A0                     mov r14, qword ptr [rbp - 0x60]
006D871E  4D 85 F6                        test r14, r14
006D8721  74 E4                           je 0x1406d8707
006D8723  41 0F B7 86 88 00 00 00         movzx eax, word ptr [r14 + 0x88]
006D872B  66 41 3B 04 24                  cmp ax, word ptr [r12]
006D8730  73 D5                           jae 0x1406d8707
006D8732  49 39 54 C4 08                  cmp qword ptr [r12 + rax*8 + 8], rdx
006D8737  74 CE                           je 0x1406d8707
006D8739  4C 8B 44 24 48                  mov r8, qword ptr [rsp + 0x48]
006D873E  48 8D 44 24 30                  lea rax, [rsp + 0x30]
006D8743  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
006D8748  4D 8B CE                        mov r9, r14
006D874B  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
006D8750  49 8B CC                        mov rcx, r12
006D8753  49 8B D5                        mov rdx, r13
006D8756  E8 05 5A D2 FF                  call 0x1403fe160
006D875B  48 8B D8                        mov rbx, rax
006D875E  48 85 C0                        test rax, rax
006D8761  75 39                           jne 0x1406d879c
006D8763  41 0F B7 86 88 00 00 00         movzx eax, word ptr [r14 + 0x88]
006D876B  66 39 85 80 00 00 00            cmp word ptr [rbp + 0x80], ax
006D8772  76 93                           jbe 0x1406d8707
006D8774  8B C8                           mov ecx, eax
006D8776  49 8B 86 80 00 00 00            mov rax, qword ptr [r14 + 0x80]
006D877D  48 F7 D0                        not rax
006D8780  48 21 84 CD 88 00 00 00         and qword ptr [rbp + rcx*8 + 0x88], rax
006D8788  E9 7A FF FF FF                  jmp 0x1406d8707
006D878D  3B F7                           cmp esi, edi
006D878F  7E 0B                           jle 0x1406d879c
006D8791  FF CE                           dec esi
006D8793  89 74 24 34                     mov dword ptr [rsp + 0x34], esi
006D8797  E9 5F FF FF FF                  jmp 0x1406d86fb
006D879C  89 7C 24 34                     mov dword ptr [rsp + 0x34], edi
006D87A0  48 8B F3                        mov rsi, rbx
006D87A3  48 85 DB                        test rbx, rbx
006D87A6  0F 85 AB D8 B7 FF               jne 0x140256057
006D87AC  48 8D 8D 80 00 00 00            lea rcx, [rbp + 0x80]
006D87B3  E8 C8 8D BF FF                  call 0x1402d1580
006D87B8  45 33 DB                        xor r11d, r11d
006D87BB  85 C0                           test eax, eax
006D87BD  0F 85 4D D2 B7 FF               jne 0x140255a10
006D87C3  8D 73 01                        lea esi, [rbx + 1]
006D87C6  E9 D0 FE FF FF                  jmp 0x1406d869b
006D87CB  41 B8 00 01 00 00               mov r8d, 0x100
006D87D1  48 8D 8D 98 01 00 00            lea rcx, [rbp + 0x198]
006D87D8  E8 63 E4 FE FF                  call 0x1406c6c40
006D87DD  4D 8B BE C0 00 00 00            mov r15, qword ptr [r14 + 0xc0]
006D87E4  48 8D 8D 98 01 00 00            lea rcx, [rbp + 0x198]
006D87EB  48 8B BB C0 00 00 00            mov rdi, qword ptr [rbx + 0xc0]
006D87F2  33 C0                           xor eax, eax
006D87F4  0F 57 C0                        xorps xmm0, xmm0
006D87F7  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
006D87FB  33 D2                           xor edx, edx
006D87FD  4C 89 7D 98                     mov qword ptr [rbp - 0x68], r15
006D8801  41 B8 00 01 00 00               mov r8d, 0x100
006D8807  48 C7 85 90 01 00 00 01 00 20 00  mov qword ptr [rbp + 0x190], 0x200001
006D8812  0F 11 45 58                     movups xmmword ptr [rbp + 0x58], xmm0
006D8816  8B F0                           mov esi, eax
006D8818  0F 11 45 68                     movups xmmword ptr [rbp + 0x68], xmm0
006D881C  E8 1F E4 FE FF                  call 0x1406c6c40
006D8821  0F B7 95 92 01 00 00            movzx edx, word ptr [rbp + 0x192]
006D8828  48 8D 8D 90 01 00 00            lea rcx, [rbp + 0x190]
006D882F  4D 8B C4                        mov r8, r12
006D8832  E8 29 60 BF FF                  call 0x1402ce860
006D8837  4C 3B FF                        cmp r15, rdi
006D883A  48 8D 8D 60 03 00 00            lea rcx, [rbp + 0x360]
006D8841  49 0F 44 F6                     cmove rsi, r14
006D8845  33 D2                           xor edx, edx
006D8847  44 8D 42 40                     lea r8d, [rdx + 0x40]
006D884B  E8 F0 E3 FE FF                  call 0x1406c6c40
006D8850  0F B7 87 88 00 00 00            movzx eax, word ptr [rdi + 0x88]
006D8857  45 33 DB                        xor r11d, r11d
006D885A  66 41 3B 04 24                  cmp ax, word ptr [r12]
006D885F  73 07                           jae 0x1406d8868
006D8861  49 8B 4C C4 08                  mov rcx, qword ptr [r12 + rax*8 + 8]
006D8866  EB 03                           jmp 0x1406d886b
006D8868  49 8B CB                        mov rcx, r11
006D886B  4C 8B 77 08                     mov r14, qword ptr [rdi + 8]
006D886F  48 63 44 24 34                  movsxd rax, dword ptr [rsp + 0x34]
006D8874  48 8B 5C C7 10                  mov rbx, qword ptr [rdi + rax*8 + 0x10]
006D8879  49 23 DE                        and rbx, r14
006D887C  48 23 D9                        and rbx, rcx
006D887F  48 89 5C 24 60                  mov qword ptr [rsp + 0x60], rbx
006D8884  74 5A                           je 0x1406d88e0
006D8886  B9 01 00 00 00                  mov ecx, 1
006D888B  84 8F B8 00 00 00               test byte ptr [rdi + 0xb8], cl
006D8891  74 6C                           je 0x1406d88ff
006D8893  44 38 5C 24 30                  cmp byte ptr [rsp + 0x30], r11b
006D8898  74 14                           je 0x1406d88ae
006D889A  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
006D889F  48 8B CF                        mov rcx, rdi
006D88A2  E8 65 5B D2 FF                  call 0x1403fe40c
006D88A7  45 33 DB                        xor r11d, r11d
006D88AA  84 C0                           test al, al
006D88AC  75 2B                           jne 0x1406d88d9
006D88AE  48 8B 4F 18                     mov rcx, qword ptr [rdi + 0x18]
006D88B2  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
006D88B7  48 23 CB                        and rcx, rbx
006D88BA  75 2C                           jne 0x1406d88e8
006D88BC  44 38 5C 24 30                  cmp byte ptr [rsp + 0x30], r11b
006D88C1  75 1D                           jne 0x1406d88e0
006D88C3  49 39 BD C0 00 00 00            cmp qword ptr [r13 + 0xc0], rdi
006D88CA  75 33                           jne 0x1406d88ff
006D88CC  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
006D88D1  49 8B CD                        mov rcx, r13
006D88D4  E8 27 E5 B7 FF                  call 0x140256e00
006D88D9  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
006D88DE  EB 1F                           jmp 0x1406d88ff
006D88E0  49 8B DB                        mov rbx, r11
006D88E3  E9 2E 01 00 00                  jmp 0x1406d8a16
006D88E8  44 38 5C 24 30                  cmp byte ptr [rsp + 0x30], r11b
006D88ED  74 0D                           je 0x1406d88fc
006D88EF  F3 49 0F B8 C6                  popcnt rax, r14
006D88F4  3B 05 1E E4 8E 00               cmp eax, dword ptr [rip + 0x8ee41e]
006D88FA  72 E4                           jb 0x1406d88e0
006D88FC  48 8B D9                        mov rbx, rcx
006D88FF  48 8D 97 40 02 00 00            lea rdx, [rdi + 0x240]
006D8906  41 B8 40 00 00 00               mov r8d, 0x40
006D890C  48 8D 8D 60 03 00 00            lea rcx, [rbp + 0x360]
006D8913  E8 B8 40 FE FF                  call 0x1406bc9d0
006D8918  48 8D 95 60 03 00 00            lea rdx, [rbp + 0x360]
006D891F  48 8B CB                        mov rcx, rbx
006D8922  E8 79 66 CC FF                  call 0x14039efa0
006D8927  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
006D892C  45 33 DB                        xor r11d, r11d
006D892F  4C 8B C0                        mov r8, rax
006D8932  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
006D8937  48 85 83 C8 00 00 00            test qword ptr [rbx + 0xc8], rax
006D893E  0F 85 C9 00 00 00               jne 0x1406d8a0d
006D8944  48 85 F6                        test rsi, rsi
006D8947  74 12                           je 0x1406d895b
006D8949  48 85 86 C8 00 00 00            test qword ptr [rsi + 0xc8], rax
006D8950  74 09                           je 0x1406d895b
006D8952  8B 7C 24 34                     mov edi, dword ptr [rsp + 0x34]
006D8956  E9 01 D7 B7 FF                  jmp 0x14025605c
006D895B  48 8B 83 60 8E 00 00            mov rax, qword ptr [rbx + 0x8e60]
006D8962  49 23 C0                        and rax, r8
006D8965  75 11                           jne 0x1406d8978
006D8967  48 85 F6                        test rsi, rsi
006D896A  74 16                           je 0x1406d8982
006D896C  48 8B 86 60 8E 00 00            mov rax, qword ptr [rsi + 0x8e60]
006D8973  49 23 C0                        and rax, r8
006D8976  74 0A                           je 0x1406d8982
006D8978  4C 8B C0                        mov r8, rax
006D897B  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
006D8980  EB 50                           jmp 0x1406d89d2
006D8982  49 8B C0                        mov rax, r8
006D8985  48 23 83 78 8E 00 00            and rax, qword ptr [rbx + 0x8e78]
006D898C  75 EA                           jne 0x1406d8978
006D898E  48 85 F6                        test rsi, rsi
006D8991  74 0C                           je 0x1406d899f
006D8993  49 8B C0                        mov rax, r8
006D8996  48 23 86 60 8E 00 00            and rax, qword ptr [rsi + 0x8e60]
006D899D  75 D9                           jne 0x1406d8978
006D899F  8B 05 DF C6 8E 00               mov eax, dword ptr [rip + 0x8ec6df]
006D89A5  B9 01 00 00 00                  mov ecx, 1
006D89AA  84 C1                           test cl, al
006D89AC  74 24                           je 0x1406d89d2
006D89AE  49 8B C0                        mov rax, r8
006D89B1  48 23 83 70 8E 00 00            and rax, qword ptr [rbx + 0x8e70]
006D89B8  75 BE                           jne 0x1406d8978
006D89BA  48 85 F6                        test rsi, rsi
006D89BD  74 13                           je 0x1406d89d2
006D89BF  49 8B C0                        mov rax, r8
006D89C2  48 23 86 70 8E 00 00            and rax, qword ptr [rsi + 0x8e70]
006D89C9  4C 0F 45 C0                     cmovne r8, rax
006D89CD  4C 89 44 24 60                  mov qword ptr [rsp + 0x60], r8
006D89D2  0F B6 8B D1 00 00 00            movzx ecx, byte ptr [rbx + 0xd1]
006D89D9  0F B6 93 D0 00 00 00            movzx edx, byte ptr [rbx + 0xd0]
006D89E0  49 D3 C8                        ror r8, cl
006D89E3  49 0F BC C0                     bsf rax, r8
006D89E7  C1 E2 06                        shl edx, 6
006D89EA  03 C8                           add ecx, eax
006D89EC  89 45 E4                        mov dword ptr [rbp - 0x1c], eax
006D89EF  48 8B 05 C2 A7 84 00            mov rax, qword ptr [rip + 0x84a7c2]
006D89F6  83 E1 3F                        and ecx, 0x3f
006D89F9  03 D1                           add edx, ecx
006D89FB  48 8D 0D FE 75 92 FF            lea rcx, [rip - 0x6d8a02]
006D8A02  8B 04 90                        mov eax, dword ptr [rax + rdx*4]
006D8A05  48 8B 9C C1 40 8C FC 00         mov rbx, qword ptr [rcx + rax*8 + 0xfc8c40]
006D8A0D  48 85 DB                        test rbx, rbx
006D8A10  0F 85 0A 02 00 00               jne 0x1406d8c20
006D8A16  0F B7 87 88 00 00 00            movzx eax, word ptr [rdi + 0x88]
006D8A1D  44 0F B7 B5 90 01 00 00         movzx r14d, word ptr [rbp + 0x190]
006D8A25  66 44 3B F0                     cmp r14w, ax
006D8A29  76 1C                           jbe 0x1406d8a47
006D8A2B  8B C8                           mov ecx, eax
006D8A2D  48 8B 87 80 00 00 00            mov rax, qword ptr [rdi + 0x80]
006D8A34  48 F7 D0                        not rax
006D8A37  48 21 84 CD 98 01 00 00         and qword ptr [rbp + rcx*8 + 0x198], rax
006D8A3F  44 0F B7 B5 90 01 00 00         movzx r14d, word ptr [rbp + 0x190]
006D8A47  4C 3B FF                        cmp r15, rdi
006D8A4A  74 4E                           je 0x1406d8a9a
006D8A4C  41 0F B7 87 88 00 00 00         movzx eax, word ptr [r15 + 0x88]
006D8A54  66 41 3B C6                     cmp ax, r14w
006D8A58  73 40                           jae 0x1406d8a9a
006D8A5A  48 83 BC C5 98 01 00 00 00      cmp qword ptr [rbp + rax*8 + 0x198], 0
006D8A63  74 35                           je 0x1406d8a9a
006D8A65  4C 8B 44 24 48                  mov r8, qword ptr [rsp + 0x48]
006D8A6A  48 8D 44 24 30                  lea rax, [rsp + 0x30]
006D8A6F  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
006D8A74  4D 8B CF                        mov r9, r15
006D8A77  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
006D8A7B  49 8B D5                        mov rdx, r13
006D8A7E  49 8B CC                        mov rcx, r12
006D8A81  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
006D8A86  E8 D5 56 D2 FF                  call 0x1403fe160
006D8A8B  45 33 DB                        xor r11d, r11d
006D8A8E  48 8B D8                        mov rbx, rax
006D8A91  48 85 C0                        test rax, rax
006D8A94  0F 85 86 01 00 00               jne 0x1406d8c20
006D8A9A  41 0F B7 87 88 00 00 00         movzx eax, word ptr [r15 + 0x88]
006D8AA2  66 44 3B F0                     cmp r14w, ax
006D8AA6  76 1A                           jbe 0x1406d8ac2
006D8AA8  49 8B 8F 80 00 00 00            mov rcx, qword ptr [r15 + 0x80]
006D8AAF  48 F7 D1                        not rcx
006D8AB2  48 21 8C C5 98 01 00 00         and qword ptr [rbp + rax*8 + 0x198], rcx
006D8ABA  44 0F B7 B5 90 01 00 00         movzx r14d, word ptr [rbp + 0x190]
006D8AC2  49 8B B5 C0 00 00 00            mov rsi, qword ptr [r13 + 0xc0]
006D8AC9  48 89 75 D0                     mov qword ptr [rbp - 0x30], rsi
006D8ACD  48 3B F7                        cmp rsi, rdi
006D8AD0  74 4E                           je 0x1406d8b20
006D8AD2  49 3B F7                        cmp rsi, r15
006D8AD5  74 49                           je 0x1406d8b20
006D8AD7  0F B7 86 88 00 00 00            movzx eax, word ptr [rsi + 0x88]
006D8ADE  66 41 3B C6                     cmp ax, r14w
006D8AE2  73 3C                           jae 0x1406d8b20
006D8AE4  48 83 BC C5 98 01 00 00 00      cmp qword ptr [rbp + rax*8 + 0x198], 0
006D8AED  74 31                           je 0x1406d8b20
006D8AEF  4C 8B 44 24 48                  mov r8, qword ptr [rsp + 0x48]
006D8AF4  48 8D 44 24 30                  lea rax, [rsp + 0x30]
006D8AF9  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
006D8AFE  4C 8B CE                        mov r9, rsi
006D8B01  49 8B D5                        mov rdx, r13
006D8B04  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
006D8B09  49 8B CC                        mov rcx, r12
006D8B0C  E8 4F 56 D2 FF                  call 0x1403fe160
006D8B11  45 33 DB                        xor r11d, r11d
006D8B14  48 8B D8                        mov rbx, rax
006D8B17  48 85 C0                        test rax, rax
006D8B1A  0F 85 00 01 00 00               jne 0x1406d8c20
006D8B20  0F B7 86 88 00 00 00            movzx eax, word ptr [rsi + 0x88]
006D8B27  66 44 3B F0                     cmp r14w, ax
006D8B2B  76 1C                           jbe 0x1406d8b49
006D8B2D  8B C8                           mov ecx, eax
006D8B2F  48 8B 86 80 00 00 00            mov rax, qword ptr [rsi + 0x80]
006D8B36  48 F7 D0                        not rax
006D8B39  48 21 84 CD 98 01 00 00         and qword ptr [rbp + rcx*8 + 0x198], rax
006D8B41  44 0F B7 B5 90 01 00 00         movzx r14d, word ptr [rbp + 0x190]
006D8B49  48 8D 8D 90 01 00 00            lea rcx, [rbp + 0x190]
006D8B50  E8 2B 8A BF FF                  call 0x1402d1580
006D8B55  45 33 DB                        xor r11d, r11d
006D8B58  85 C0                           test eax, eax
006D8B5A  0F 85 AE 00 00 00               jne 0x1406d8c0e
006D8B60  0F B7 97 8A 00 00 00            movzx edx, word ptr [rdi + 0x8a]
006D8B67  48 8D 4D 58                     lea rcx, [rbp + 0x58]
006D8B6B  E8 1C EE D4 FF                  call 0x14042798c
006D8B70  48 8D 55 D0                     lea rdx, [rbp - 0x30]
006D8B74  48 8D 4D 58                     lea rcx, [rbp + 0x58]
006D8B78  E8 43 DE B7 FF                  call 0x1402569c0
006D8B7D  45 33 DB                        xor r11d, r11d
006D8B80  85 C0                           test eax, eax
006D8B82  0F 85 98 00 00 00               jne 0x1406d8c20
006D8B88  4C 8B 7D D0                     mov r15, qword ptr [rbp - 0x30]
006D8B8C  4C 3B FF                        cmp r15, rdi
006D8B8F  74 DF                           je 0x1406d8b70
006D8B91  4C 3B 7D 98                     cmp r15, qword ptr [rbp - 0x68]
006D8B95  74 D9                           je 0x1406d8b70
006D8B97  4D 3B BD C0 00 00 00            cmp r15, qword ptr [r13 + 0xc0]
006D8B9E  74 D0                           je 0x1406d8b70
006D8BA0  4C 8B 44 24 48                  mov r8, qword ptr [rsp + 0x48]
006D8BA5  48 8D 44 24 30                  lea rax, [rsp + 0x30]
006D8BAA  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
006D8BAF  4D 8B CF                        mov r9, r15
006D8BB2  49 8B D5                        mov rdx, r13
006D8BB5  4C 89 5C 24 20                  mov qword ptr [rsp + 0x20], r11
006D8BBA  49 8B CC                        mov rcx, r12
006D8BBD  E8 9E 55 D2 FF                  call 0x1403fe160
006D8BC2  48 8B D8                        mov rbx, rax
006D8BC5  48 8B F0                        mov rsi, rax
006D8BC8  48 85 C0                        test rax, rax
006D8BCB  75 4A                           jne 0x1406d8c17
006D8BCD  41 0F B7 87 88 00 00 00         movzx eax, word ptr [r15 + 0x88]
006D8BD5  66 44 3B F0                     cmp r14w, ax
006D8BD9  76 1C                           jbe 0x1406d8bf7
006D8BDB  8B C8                           mov ecx, eax
006D8BDD  49 8B 87 80 00 00 00            mov rax, qword ptr [r15 + 0x80]
006D8BE4  48 F7 D0                        not rax
006D8BE7  48 21 84 CD 98 01 00 00         and qword ptr [rbp + rcx*8 + 0x198], rax
006D8BEF  44 0F B7 B5 90 01 00 00         movzx r14d, word ptr [rbp + 0x190]
006D8BF7  48 8D 8D 90 01 00 00            lea rcx, [rbp + 0x190]
006D8BFE  E8 7D 89 BF FF                  call 0x1402d1580
006D8C03  45 33 DB                        xor r11d, r11d
006D8C06  85 C0                           test eax, eax
006D8C08  0F 84 62 FF FF FF               je 0x1406d8b70
006D8C0E  8B 7C 24 34                     mov edi, dword ptr [rsp + 0x34]
006D8C12  E9 F9 CD B7 FF                  jmp 0x140255a10
006D8C17  8B 7C 24 34                     mov edi, dword ptr [rsp + 0x34]
006D8C1B  E9 37 D4 B7 FF                  jmp 0x140256057
006D8C20  8B 7C 24 34                     mov edi, dword ptr [rsp + 0x34]
006D8C24  E9 DB CD B7 FF                  jmp 0x140255a04
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006D831E(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_r11;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned int v_stack_p34;
    unsigned int v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p78;

    v_stack_p28 = a6;
    v_stack_p20 = v_r11;
    result = KiSelectIdleProcessor(v_r12, v_r13, v_r15, v_rdi);
    v_r11 = 0;
    result = ~(*(unsigned __int64 *)(v_rdi + 128));
}
```

## 5. (Beta) C Style

```c
int64_t sub_006D831E(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, int64_t Arg6)
{
    int64_t result;
    int64_t local_r11;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint32_t v_stack_p34;
    uint32_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p78;

    v_stack_p28 = Arg6;
    v_stack_p20 = local_r11;
    result = KiSelectIdleProcessor(local_r12, local_r13, local_r15, local_rdi);
    local_r11 = 0;
    result = ~(*(uint64_t *)(local_rdi + 0x80));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006D831E&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
