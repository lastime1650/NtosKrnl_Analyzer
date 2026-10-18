# DrvDbGetDeviceIdMappedProperty

- RVA: `0x0092F690`–`0x0092FABB` (길이 `1,067` bytes)
- VA: `0x000000014092F690`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0008EAB4`
- 디코드: `291`개 명령, `1,067/1,067` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x0092F749` → [wcschr](../../text/50/wcschr_function_00501A60.md) (function, `0x00501A60`)
- `0x0092F7B5` → [DrvDbOpenObjectRegKey](../93/DrvDbOpenObjectRegKey_function_00931060.md) (function, `0x00931060`)
- `0x0092F886` → [DrvDbGetDeviceIdDriverInfMatches](../99/DrvDbGetDeviceIdDriverInfMatches_function_00994250.md) (function, `0x00994250`)
- `0x0092F891` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x0092F90C` → [DrvDbGetObjectDatabaseNodeName](DrvDbGetObjectDatabaseNodeName_function_0092FAC4.md) (function, `0x0092FAC4`)
- `0x0092F9C1` → [DrvDbOpenObjectRegKey](../93/DrvDbOpenObjectRegKey_function_00931060.md) (function, `0x00931060`)
- `0x0092F9ED` → [DrvDbGetDeviceIdDriverInfMatches](../99/DrvDbGetDeviceIdDriverInfMatches_function_00994250.md) (function, `0x00994250`)
- `0x0092FA68` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x0092FAA3` → [DrvDbOpenDeviceIdRegKey](DrvDbOpenDeviceIdRegKey_function_0092F080.md) (function, `0x0092F080`)

### Direct callers
- [DrvDbDispatchDeviceId](DrvDbDispatchDeviceId_function_0092F490.md) at `0x0092F538`

### Static image references
- `0x0092F6F6` → RVA `0x00011EF8` (`.rdata`; read)
- `0x0092F6FD` → RVA `0x00011F00` (`.rdata`; read)
- `0x0092F8D1` → RVA `0x00011F10` (`.rdata`; read)
- `0x0092F8DE` → RVA `0x00011F18` (`.rdata`; read)
- `0x0092F949` → RVA `0x000020E0` (`.rdata`; read)
- `0x0092F969` → RVA `0x00011F28` (`.rdata`; read)
- `0x0092F976` → RVA `0x00011F30` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x0092F749` → [wcschr](../../text/50/wcschr_function_00501A60.md) (`PAGE` → `.text`)
  - `0x0092F891` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x0092FA68` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0092FA83` → [sub_00B237BE](../B2/Unknown_function_00B237BE.md) (`tail-transfer`)
  - `0x0092FAB6` → [sub_00B237BE](../B2/Unknown_function_00B237BE.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0092F690  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
0092F695  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
0092F69A  55                              push rbp
0092F69B  56                              push rsi
0092F69C  57                              push rdi
0092F69D  41 54                           push r12
0092F69F  41 55                           push r13
0092F6A1  41 56                           push r14
0092F6A3  41 57                           push r15
0092F6A5  48 8B EC                        mov rbp, rsp
0092F6A8  48 83 EC 60                     sub rsp, 0x60
0092F6AC  4C 8B 65 60                     mov r12, qword ptr [rbp + 0x60]
0092F6B0  45 33 DB                        xor r11d, r11d
0092F6B3  48 8B 75 78                     mov rsi, qword ptr [rbp + 0x78]
0092F6B7  49 8B D8                        mov rbx, r8
0092F6BA  4C 8B EA                        mov r13, rdx
0092F6BD  4C 89 5D F8                     mov qword ptr [rbp - 8], r11
0092F6C1  4C 8B F9                        mov r15, rcx
0092F6C4  44 89 5D F0                     mov dword ptr [rbp - 0x10], r11d
0092F6C8  45 89 1C 24                     mov dword ptr [r12], r11d
0092F6CC  45 8D 73 01                     lea r14d, [r11 + 1]
0092F6D0  44 89 1E                        mov dword ptr [rsi], r11d
0092F6D3  45 8B 51 10                     mov r10d, dword ptr [r9 + 0x10]
0092F6D7  44 89 5D F4                     mov dword ptr [rbp - 0xc], r11d
0092F6DB  44 88 5D 58                     mov byte ptr [rbp + 0x58], r11b
0092F6DF  41 83 FA 02                     cmp r10d, 2
0092F6E3  0F 84 E5 01 00 00               je 0x14092f8ce
0092F6E9  41 83 FA 03                     cmp r10d, 3
0092F6ED  0F 85 44 02 00 00               jne 0x14092f937
0092F6F3  49 8B 01                        mov rax, qword ptr [r9]
0092F6F6  48 8B 15 FB 27 6E FF            mov rdx, qword ptr [rip - 0x91d805]
0092F6FD  48 8B 0D FC 27 6E FF            mov rcx, qword ptr [rip - 0x91d804]
0092F704  48 2B C2                        sub rax, rdx
0092F707  75 07                           jne 0x14092f710
0092F709  49 8B 41 08                     mov rax, qword ptr [r9 + 8]
0092F70D  48 2B C1                        sub rax, rcx
0092F710  48 85 C0                        test rax, rax
0092F713  0F 85 1E 02 00 00               jne 0x14092f937
0092F719  49 8B 01                        mov rax, qword ptr [r9]
0092F71C  48 2B C2                        sub rax, rdx
0092F71F  75 07                           jne 0x14092f728
0092F721  49 8B 41 08                     mov rax, qword ptr [r9 + 8]
0092F725  48 2B C1                        sub rax, rcx
0092F728  41 8A FE                        mov dil, r14b
0092F72B  48 85 C0                        test rax, rax
0092F72E  0F 85 4E 02 00 00               jne 0x14092f982
0092F734  66 41 83 7D 00 40               cmp word ptr [r13], 0x40
0092F73A  40 88 7D 78                     mov byte ptr [rbp + 0x78], dil
0092F73E  75 25                           jne 0x14092f765
0092F740  BA 3A 00 00 00                  mov edx, 0x3a
0092F745  49 8D 4D 02                     lea rcx, [r13 + 2]
0092F749  E8 12 23 BD FF                  call 0x140501a60
0092F74E  45 33 DB                        xor r11d, r11d
0092F751  48 85 C0                        test rax, rax
0092F754  74 0F                           je 0x14092f765
0092F756  48 83 C0 02                     add rax, 2
0092F75A  74 09                           je 0x14092f765
0092F75C  49 3B C5                        cmp rax, r13
0092F75F  0F 85 25 02 00 00               jne 0x14092f98a
0092F765  4D 39 5F 30                     cmp qword ptr [r15 + 0x30], r11
0092F769  0F 85 1B 02 00 00               jne 0x14092f98a
0092F76F  49 8D 47 10                     lea rax, [r15 + 0x10]
0092F773  4C 8B 38                        mov r15, qword ptr [rax]
0092F776  4C 3B F8                        cmp r15, rax
0092F779  0F 84 D7 00 00 00               je 0x14092f856
0092F77F  4C 8B 65 68                     mov r12, qword ptr [rbp + 0x68]
0092F783  BF 23 00 00 C0                  mov edi, 0xc0000023
0092F788  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
0092F78C  48 8D 45 F8                     lea rax, [rbp - 8]
0092F790  4C 89 5C 24 40                  mov qword ptr [rsp + 0x40], r11
0092F795  4D 8B CD                        mov r9, r13
0092F798  4C 89 5C 24 38                  mov qword ptr [rsp + 0x38], r11
0092F79D  41 B8 05 00 00 00               mov r8d, 5
0092F7A3  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0092F7A8  49 8B D7                        mov rdx, r15
0092F7AB  44 88 5C 24 28                  mov byte ptr [rsp + 0x28], r11b
0092F7B0  44 89 74 24 20                  mov dword ptr [rsp + 0x20], r14d
0092F7B5  E8 A6 18 00 00                  call 0x140931060
0092F7BA  45 33 DB                        xor r11d, r11d
0092F7BD  8B D8                           mov ebx, eax
0092F7BF  85 C0                           test eax, eax
0092F7C1  0F 89 96 00 00 00               jns 0x14092f85d
0092F7C7  3D 34 00 00 C0                  cmp eax, 0xc0000034
0092F7CC  75 59                           jne 0x14092f827
0092F7CE  41 8B DB                        mov ebx, r11d
0092F7D1  48 8B 45 40                     mov rax, qword ptr [rbp + 0x40]
0092F7D5  4D 8B 3F                        mov r15, qword ptr [r15]
0092F7D8  48 83 C0 10                     add rax, 0x10
0092F7DC  4C 3B F8                        cmp r15, rax
0092F7DF  75 A7                           jne 0x14092f788
0092F7E1  8A 45 58                        mov al, byte ptr [rbp + 0x58]
0092F7E4  85 DB                           test ebx, ebx
0092F7E6  78 42                           js 0x14092f82a
0092F7E8  84 C0                           test al, al
0092F7EA  74 6A                           je 0x14092f856
0092F7EC  44 39 1E                        cmp dword ptr [rsi], r11d
0092F7EF  0F 84 69 02 00 00               je 0x14092fa5e
0092F7F5  48 8B 45 60                     mov rax, qword ptr [rbp + 0x60]
0092F7F9  C7 00 12 20 00 00               mov dword ptr [rax], 0x2012
0092F7FF  8B 06                           mov eax, dword ptr [rsi]
0092F801  83 C0 02                        add eax, 2
0092F804  8B C8                           mov ecx, eax
0092F806  89 06                           mov dword ptr [rsi], eax
0092F808  4D 85 E4                        test r12, r12
0092F80B  0F 84 1E 02 00 00               je 0x14092fa2f
0092F811  3B 4D 70                        cmp ecx, dword ptr [rbp + 0x70]
0092F814  0F 87 15 02 00 00               ja 0x14092fa2f
0092F81A  8B C1                           mov eax, ecx
0092F81C  48 D1 E8                        shr rax, 1
0092F81F  66 45 89 5C 44 FE               mov word ptr [r12 + rax*2 - 2], r11w
0092F825  EB 07                           jmp 0x14092f82e
0092F827  8A 45 58                        mov al, byte ptr [rbp + 0x58]
0092F82A  3B DF                           cmp ebx, edi
0092F82C  74 BA                           je 0x14092f7e8
0092F82E  48 8B 4D F8                     mov rcx, qword ptr [rbp - 8]
0092F832  48 85 C9                        test rcx, rcx
0092F835  0F 85 2D 02 00 00               jne 0x14092fa68
0092F83B  8B C3                           mov eax, ebx
0092F83D  48 8B 9C 24 A8 00 00 00         mov rbx, qword ptr [rsp + 0xa8]
0092F845  48 83 C4 60                     add rsp, 0x60
0092F849  41 5F                           pop r15
0092F84B  41 5E                           pop r14
0092F84D  41 5D                           pop r13
0092F84F  41 5C                           pop r12
0092F851  5F                              pop rdi
0092F852  5E                              pop rsi
0092F853  5D                              pop rbp
0092F854  C3                              ret
0092F855  CC                              int3
0092F856  BB 34 00 00 C0                  mov ebx, 0xc0000034
0092F85B  EB D1                           jmp 0x14092f82e
0092F85D  8B 45 F4                        mov eax, dword ptr [rbp - 0xc]
0092F860  44 8B 4D 70                     mov r9d, dword ptr [rbp + 0x70]
0092F864  48 8B 55 F8                     mov rdx, qword ptr [rbp - 8]
0092F868  44 2B C8                        sub r9d, eax
0092F86B  41 D1 E9                        shr r9d, 1
0092F86E  4D 8D 04 04                     lea r8, [r12 + rax]
0092F872  44 88 75 58                     mov byte ptr [rbp + 0x58], r14b
0092F876  8A 45 78                        mov al, byte ptr [rbp + 0x78]
0092F879  88 44 24 28                     mov byte ptr [rsp + 0x28], al
0092F87D  48 8D 45 F0                     lea rax, [rbp - 0x10]
0092F881  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0092F886  E8 C5 49 06 00                  call 0x140994250
0092F88B  48 8B 4D F8                     mov rcx, qword ptr [rbp - 8]
0092F88F  8B D8                           mov ebx, eax
0092F891  E8 1A DA D7 FF                  call 0x1406ad2b0
0092F896  45 33 DB                        xor r11d, r11d
0092F899  4C 89 5D F8                     mov qword ptr [rbp - 8], r11
0092F89D  85 DB                           test ebx, ebx
0092F89F  0F 88 6E 01 00 00               js 0x14092fa13
0092F8A5  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
0092F8A8  03 C0                           add eax, eax
0092F8AA  83 F8 02                        cmp eax, 2
0092F8AD  8D 48 FE                        lea ecx, [rax - 2]
0092F8B0  0F 46 C8                        cmovbe ecx, eax
0092F8B3  4D 85 E4                        test r12, r12
0092F8B6  74 0F                           je 0x14092f8c7
0092F8B8  8B 55 F4                        mov edx, dword ptr [rbp - 0xc]
0092F8BB  8D 04 11                        lea eax, [rcx + rdx]
0092F8BE  3B 45 70                        cmp eax, dword ptr [rbp + 0x70]
0092F8C1  0F 42 D0                        cmovb edx, eax
0092F8C4  89 55 F4                        mov dword ptr [rbp - 0xc], edx
0092F8C7  01 0E                           add dword ptr [rsi], ecx
0092F8C9  E9 03 FF FF FF                  jmp 0x14092f7d1
0092F8CE  49 8B 01                        mov rax, qword ptr [r9]
0092F8D1  48 2B 05 38 26 6E FF            sub rax, qword ptr [rip - 0x91d9c8]
0092F8D8  75 0B                           jne 0x14092f8e5
0092F8DA  49 8B 41 08                     mov rax, qword ptr [r9 + 8]
0092F8DE  48 2B 05 33 26 6E FF            sub rax, qword ptr [rip - 0x91d9cd]
0092F8E5  48 85 C0                        test rax, rax
0092F8E8  75 7C                           jne 0x14092f966
0092F8EA  8B 45 70                        mov eax, dword ptr [rbp + 0x70]
0092F8ED  4D 8B C5                        mov r8, r13
0092F8F0  4C 8B 4D 68                     mov r9, qword ptr [rbp + 0x68]
0092F8F4  BA 05 00 00 00                  mov edx, 5
0092F8F9  D1 E8                           shr eax, 1
0092F8FB  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
0092F900  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0092F904  41 C7 04 24 12 00 00 00         mov dword ptr [r12], 0x12
0092F90C  E8 B3 01 00 00                  call 0x14092fac4
0092F911  BA 00 00 00 80                  mov edx, 0x80000000
0092F916  8B D8                           mov ebx, eax
0092F918  8D 0C 10                        lea ecx, [rax + rdx]
0092F91B  85 CA                           test edx, ecx
0092F91D  75 0D                           jne 0x14092f92c
0092F91F  BF 23 00 00 C0                  mov edi, 0xc0000023
0092F924  3B C7                           cmp eax, edi
0092F926  0F 85 02 FF FF FF               jne 0x14092f82e
0092F92C  8B 0E                           mov ecx, dword ptr [rsi]
0092F92E  03 C9                           add ecx, ecx
0092F930  89 0E                           mov dword ptr [rsi], ecx
0092F932  E9 F7 FE FF FF                  jmp 0x14092f82e
0092F937  41 8B D3                        mov edx, r11d
0092F93A  41 3B D6                        cmp edx, r14d
0092F93D  0F 83 11 01 00 00               jae 0x14092fa54
0092F943  8B C2                           mov eax, edx
0092F945  48 8D 0C 80                     lea rcx, [rax + rax*4]
0092F949  48 8D 05 90 27 6D FF            lea rax, [rip - 0x92d870]
0092F950  48 8D 3C C8                     lea rdi, [rax + rcx*8]
0092F954  4C 8B 07                        mov r8, qword ptr [rdi]
0092F957  45 39 50 10                     cmp dword ptr [r8 + 0x10], r10d
0092F95B  0F 84 D5 00 00 00               je 0x14092fa36
0092F961  41 03 D6                        add edx, r14d
0092F964  EB D4                           jmp 0x14092f93a
0092F966  49 8B 01                        mov rax, qword ptr [r9]
0092F969  48 2B 05 B8 25 6E FF            sub rax, qword ptr [rip - 0x91da48]
0092F970  75 0B                           jne 0x14092f97d
0092F972  49 8B 41 08                     mov rax, qword ptr [r9 + 8]
0092F976  48 2B 05 B3 25 6E FF            sub rax, qword ptr [rip - 0x91da4d]
0092F97D  48 85 C0                        test rax, rax
0092F980  75 B5                           jne 0x14092f937
0092F982  41 8A FB                        mov dil, r11b
0092F985  E9 AA FD FF FF                  jmp 0x14092f734
0092F98A  48 83 FB FF                     cmp rbx, -1
0092F98E  49 8B D3                        mov rdx, r11
0092F991  48 0F 45 D3                     cmovne rdx, rbx
0092F995  48 85 D2                        test rdx, rdx
0092F998  75 3A                           jne 0x14092f9d4
0092F99A  4C 89 5C 24 40                  mov qword ptr [rsp + 0x40], r11
0092F99F  48 8D 45 F8                     lea rax, [rbp - 8]
0092F9A3  4C 89 5C 24 38                  mov qword ptr [rsp + 0x38], r11
0092F9A8  44 8D 42 05                     lea r8d, [rdx + 5]
0092F9AC  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0092F9B1  4D 8B CD                        mov r9, r13
0092F9B4  44 88 5C 24 28                  mov byte ptr [rsp + 0x28], r11b
0092F9B9  49 8B CF                        mov rcx, r15
0092F9BC  44 89 74 24 20                  mov dword ptr [rsp + 0x20], r14d
0092F9C1  E8 9A 16 00 00                  call 0x140931060
0092F9C6  8B D8                           mov ebx, eax
0092F9C8  85 C0                           test eax, eax
0092F9CA  0F 88 5E FE FF FF               js 0x14092f82e
0092F9D0  48 8B 55 F8                     mov rdx, qword ptr [rbp - 8]
0092F9D4  44 8B 4D 70                     mov r9d, dword ptr [rbp + 0x70]
0092F9D8  48 8D 45 F0                     lea rax, [rbp - 0x10]
0092F9DC  4C 8B 45 68                     mov r8, qword ptr [rbp + 0x68]
0092F9E0  41 D1 E9                        shr r9d, 1
0092F9E3  40 88 7C 24 28                  mov byte ptr [rsp + 0x28], dil
0092F9E8  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0092F9ED  E8 5E 48 06 00                  call 0x140994250
0092F9F2  BA 00 00 00 80                  mov edx, 0x80000000
0092F9F7  8B D8                           mov ebx, eax
0092F9F9  03 C2                           add eax, edx
0092F9FB  85 C2                           test edx, eax
0092F9FD  74 73                           je 0x14092fa72
0092F9FF  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
0092FA02  03 C0                           add eax, eax
0092FA04  41 C7 04 24 12 20 00 00         mov dword ptr [r12], 0x2012
0092FA0C  89 06                           mov dword ptr [rsi], eax
0092FA0E  E9 1B FE FF FF                  jmp 0x14092f82e
0092FA13  81 FB 25 02 00 C0               cmp ebx, 0xc0000225
0092FA19  0F 84 AF FD FF FF               je 0x14092f7ce
0092FA1F  3B DF                           cmp ebx, edi
0092FA21  0F 84 7E FE FF FF               je 0x14092f8a5
0092FA27  41 8A C6                        mov al, r14b
0092FA2A  E9 FB FD FF FF                  jmp 0x14092f82a
0092FA2F  8B DF                           mov ebx, edi
0092FA31  E9 F8 FD FF FF                  jmp 0x14092f82e
0092FA36  49 8B 08                        mov rcx, qword ptr [r8]
0092FA39  49 2B 09                        sub rcx, qword ptr [r9]
0092FA3C  75 08                           jne 0x14092fa46
0092FA3E  49 8B 48 08                     mov rcx, qword ptr [r8 + 8]
0092FA42  49 2B 49 08                     sub rcx, qword ptr [r9 + 8]
0092FA46  48 85 C9                        test rcx, rcx
0092FA49  0F 85 12 FF FF FF               jne 0x14092f961
0092FA4F  48 85 FF                        test rdi, rdi
0092FA52  75 2C                           jne 0x14092fa80
0092FA54  BB 16 00 00 C0                  mov ebx, 0xc0000016
0092FA59  E9 DD FD FF FF                  jmp 0x14092f83b
0092FA5E  BB 25 02 00 C0                  mov ebx, 0xc0000225
0092FA63  E9 C6 FD FF FF                  jmp 0x14092f82e
0092FA68  E8 43 D8 D7 FF                  call 0x1406ad2b0
0092FA6D  E9 C9 FD FF FF                  jmp 0x14092f83b
0092FA72  BF 23 00 00 C0                  mov edi, 0xc0000023
0092FA77  3B DF                           cmp ebx, edi
0092FA79  74 84                           je 0x14092f9ff
0092FA7B  E9 AE FD FF FF                  jmp 0x14092f82e
0092FA80  48 85 DB                        test rbx, rbx
0092FA83  0F 85 35 3D 1F 00               jne 0x140b237be
0092FA89  48 8D 45 F8                     lea rax, [rbp - 8]
0092FA8D  4C 89 5C 24 28                  mov qword ptr [rsp + 0x28], r11
0092FA92  45 33 C9                        xor r9d, r9d
0092FA95  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0092FA9A  45 8B C6                        mov r8d, r14d
0092FA9D  49 8B D5                        mov rdx, r13
0092FAA0  49 8B CF                        mov rcx, r15
0092FAA3  E8 D8 F5 FF FF                  call 0x14092f080
0092FAA8  8B D8                           mov ebx, eax
0092FAAA  85 C0                           test eax, eax
0092FAAC  0F 88 7C FD FF FF               js 0x14092f82e
0092FAB2  48 8B 5D F8                     mov rbx, qword ptr [rbp - 8]
0092FAB6  E9 03 3D 1F 00                  jmp 0x140b237be
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DrvDbGetDeviceIdMappedProperty(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, unsigned int a7, unsigned __int8 a8)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m44;
    unsigned int v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int8 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_p10;
    unsigned __int8 v_stack_p20;
    unsigned __int8 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int8 v_stack_p40;
    unsigned __int64 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (96);
    v_r11 = 0;
    v_stack_m40 = 0;
    v_stack_m48 = 0;
    *(unsigned int *)(a5) = 0;
    *(unsigned int *)(a8) = 0;
    v_stack_m44 = 0;
    v_stack_p20 = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == 2) goto loc_0092F8CE;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) != 3) goto loc_0092F937;
    result = (*(unsigned __int64 *)(a4)) - (*(unsigned __int64 *)(v_rip - 9558021));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(a4 + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 9558020));
    }
    if (result != 0) goto loc_0092F937;
    result = (*(unsigned __int64 *)(a4)) - (*(unsigned __int64 *)(v_rip - 9558021));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(a4 + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 9558020));
    }
    if (result != 0) goto loc_0092F982;
loc_0092F734:
    v_stack_p40 = (unsigned __int8)((unsigned __int8)(v_r11 + 1));
    if ((*(unsigned __int16 *)(a2)) != 64) goto loc_0092F765;
    result = wcschr(a2 + 2, 58, a3, a4);
    v_r11 = 0;
    if (result == 0) goto loc_0092F765;
    result = (result) + (2);
    if (condition_is_equal) goto loc_0092F765;
    if (result != a2) goto loc_0092F98A;
loc_0092F765:
    if ((*(unsigned __int64 *)(a1 + 48)) != 0) goto loc_0092F98A;
    if ((*(unsigned __int64 *)(a1 + 16)) == (a1 + 16)) goto loc_0092F856;
loc_0092F788:
    v_stack_m58 = 0;
    v_stack_m60 = 0;
    v_stack_m68 = v_stack_m40;
    v_stack_m70 = 0;
    v_stack_m78 = (unsigned int)(v_r11 + 1);
    result = DrvDbOpenObjectRegKey(v_stack_p8, *(unsigned __int64 *)(a1 + 16), 5, a2);
    v_r11 = 0;
    if (!sign_flag) goto loc_0092F85D;
    if (((unsigned int)(result)) != 0xC0000034ULL) goto loc_0092F827;
loc_0092F7CE:
loc_0092F7D1:
    result = (v_stack_p8) + (16);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16))) != result) goto loc_0092F788;
    if (sign_flag) goto loc_0092F82A;
loc_0092F7E8:
    if ((unsigned __int8)(v_stack_p20) == 0) goto loc_0092F856;
    if ((*(unsigned int *)(a8)) == 0) goto loc_0092FA5E;
    *(unsigned int *)(a5) = 0x2012ULL;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a8))) + (2));
    *(unsigned int *)(a8) = (unsigned int)(result);
    if (a6 == 0) goto loc_0092FA2F;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) > a7) goto loc_0092FA2F;
    result = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))) >> (1);
    *(unsigned __int16 *)(a6 + result * 2 - 2) = 0;
    goto loc_0092F82E;
loc_0092F827:
loc_0092F82A:
    if (0 == ((unsigned int)((unsigned int)(0xC0000023ULL)))) goto loc_0092F7E8;
loc_0092F82E:
    if (v_stack_m40 != 0) goto loc_0092FA68;
loc_0092F83B:
    v_rsp = (v_rsp) + (96);
    return 0;
loc_0092F856:
    goto loc_0092F82E;
loc_0092F85D:
    a4 = (unsigned int)(((unsigned int)(a7)) - ((unsigned int)((unsigned int)(v_stack_m44))));
    a4 = (unsigned int)((a4) >> (1));
    v_stack_p20 = (unsigned __int8)(v_r11 + 1);
    v_stack_p28 = a8;
    v_stack_p20 = v_stack_m48;
    result = DrvDbGetDeviceIdDriverInfMatches(v_stack_m40, v_stack_m40, a6 + (unsigned int)(v_stack_m44) * 1, a4);
    result = ZwClose(v_stack_m40, v_stack_m40, a6 + (unsigned int)(v_stack_m44) * 1, a4);
    v_r11 = 0;
    v_stack_m40 = 0;
    if (sign_flag) goto loc_0092FA13;
loc_0092F8A5:
    result = (unsigned int)(((unsigned int)(v_stack_m48)) + ((unsigned int)((unsigned int)(v_stack_m48))));
    a1 = result - 2;
    if (((unsigned int)(result)) <= 2) { a1 = (unsigned int)(result); }
    if (a6 != 0) {
        a2 = v_stack_m44;
        result = a1 + a2 * 1;
        if (((unsigned int)(result)) < a7) { a2 = (unsigned int)(result); }
        v_stack_m44 = (unsigned int)(a2);
    }
    goto loc_0092F7D1;
loc_0092F8CE:
    result = (*(unsigned __int64 *)(a4)) - (*(unsigned __int64 *)(v_rip - 9558472));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(a4 + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 9558477));
    }
    if (result != 0) goto loc_0092F966;
    result = (unsigned int)(((unsigned int)(a7)) >> (1));
    v_stack_p28 = a8;
    v_stack_p20 = (unsigned int)(result);
    *(unsigned int *)(a6) = 18;
    result = DrvDbGetObjectDatabaseNodeName(a1, 5, a2, a6);
    if ((((unsigned int)((unsigned int)(0x80000000ULL))) & ((unsigned int)(result + (unsigned int)(0x80000000ULL) * 1))) != 0) goto loc_0092F92C;
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0xC0000023ULL)))) goto loc_0092F82E;
loc_0092F92C:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a8))) + ((unsigned int)((unsigned int)(*(unsigned int *)(a8)))));
    *(unsigned int *)(a8) = (unsigned int)(a1);
    goto loc_0092F82E;
loc_0092F937:
loc_0092F93A:
    if (0 >= ((unsigned int)(v_r11 + 1))) goto loc_0092FA54;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip - 9623664 + 0 + 0 * 4 * 8) + 16)) == ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16))))) goto loc_0092FA36;
loc_0092F961:
    a2 = (unsigned int)((0) + ((unsigned int)(v_r11 + 1)));
    goto loc_0092F93A;
loc_0092F966:
    result = (*(unsigned __int64 *)(a6)) - (*(unsigned __int64 *)(v_rip - 9558600));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(a6 + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 9558605));
    }
    if (result != 0) goto loc_0092F937;
loc_0092F982:
    goto loc_0092F734;
loc_0092F98A:
    a2 = 0;
    if (((unsigned int)((unsigned int)(result))) != -1) { a2 = (unsigned int)((unsigned int)(result)); }
    if (a2 != 0) goto loc_0092F9D4;
    v_stack_p40 = 0;
    v_stack_p38 = 0;
    v_stack_p30 = v_stack_m40;
    v_stack_p28 = 0;
    v_stack_p20 = (unsigned int)(v_r11 + 1);
    result = DrvDbOpenObjectRegKey(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16)), a2, a2 + 5, a2);
    if (sign_flag) goto loc_0092F82E;
loc_0092F9D4:
    a4 = (unsigned int)(((unsigned int)(a7)) >> (1));
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_m48;
    result = DrvDbGetDeviceIdDriverInfMatches(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16)), v_stack_m40, a6, a4);
    result = (unsigned int)((result) + ((unsigned int)((unsigned int)(0x80000000ULL))));
    if ((((unsigned int)((unsigned int)(0x80000000ULL))) & ((unsigned int)(result))) == 0) goto loc_0092FA72;
loc_0092F9FF:
    result = (unsigned int)(((unsigned int)(v_stack_m48)) + ((unsigned int)((unsigned int)(v_stack_m48))));
    *(unsigned int *)(a6) = 0x2012ULL;
    *(unsigned int *)(a8) = (unsigned int)(result);
    goto loc_0092F82E;
loc_0092FA13:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 0xC0000225ULL) goto loc_0092F7CE;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 0) goto loc_0092F8A5;
    goto loc_0092F82A;
loc_0092FA2F:
    goto loc_0092F82E;
loc_0092FA36:
    a1 = (*(unsigned __int64 *)(a6)) - (*(unsigned __int64 *)(a4));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int64 *)(a6 + 8);
        a1 = (a1) - (*(unsigned __int64 *)(a4 + 8));
    }
    if (a1 != 0) goto loc_0092F961;
    if (0 != 0) goto loc_0092FA80;
loc_0092FA54:
    goto loc_0092F83B;
loc_0092FA5E:
    goto loc_0092F82E;
loc_0092FA68:
    result = ZwClose(a1, (unsigned int)(0x80000000ULL), a6, a4);
    goto loc_0092F83B;
loc_0092FA72:
    if (((unsigned int)((unsigned int)(0xC0000225ULL))) == ((unsigned int)((unsigned int)(0xC0000023ULL)))) goto loc_0092F9FF;
    goto loc_0092F82E;
loc_0092FA80:
    v_stack_p28 = 0;
    a4 = 0;
    v_stack_p20 = v_stack_m40;
    result = DrvDbOpenDeviceIdRegKey(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16)), a2, (unsigned int)((unsigned int)(v_r11 + 1)), a4);
    if (sign_flag) goto loc_0092F82E;
}
```

## 5. (Beta) C Style

```c
int64_t DrvDbGetDeviceIdMappedProperty(void *Arg1, void *Arg2, int64_t Arg3, void *Arg4, void *Arg5, int64_t Arg6, uint32_t Arg7, void *Arg8)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg5 = (uint8_t *)Arg5;
    uint8_t *arg8 = (uint8_t *)Arg8;

    int64_t result;
    int64_t local_r11;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint32_t v_stack_m44;
    uint32_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint8_t v_stack_m70;
    uint32_t v_stack_m78;
    uint64_t v_stack_p10;
    uint8_t v_stack_p20;
    uint8_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint8_t v_stack_p40;
    uint64_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (96);
    local_r11 = 0;
    v_stack_m40 = 0;
    v_stack_m48 = 0;
    *(uint32_t *)(arg5) = 0;
    *(uint32_t *)(arg8) = 0;
    v_stack_m44 = 0;
    v_stack_p20 = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == 2) goto loc_0092F8CE;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) != 3) goto loc_0092F937;
    result = (*(uint64_t *)(arg4)) - (*(uint64_t *)(v_rip - 0x91D805));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(arg4 + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x91D804));
    }
    if (result != 0) goto loc_0092F937;
    result = (*(uint64_t *)(arg4)) - (*(uint64_t *)(v_rip - 0x91D805));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(arg4 + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x91D804));
    }
    if (result != 0) goto loc_0092F982;
loc_0092F734:
    v_stack_p40 = (uint8_t)((uint8_t)(local_r11 + 1));
    if ((*(uint16_t *)(arg2)) != 64) goto loc_0092F765;
    result = wcschr(Arg2 + 2, 58, Arg3, Arg4);
    local_r11 = 0;
    if (result == 0) goto loc_0092F765;
    result = (result) + (2);
    if (condition_is_equal) goto loc_0092F765;
    if (result != Arg2) goto loc_0092F98A;
loc_0092F765:
    if ((*(uint64_t *)(arg1 + 0x30)) != 0) goto loc_0092F98A;
    if ((*(uint64_t *)(arg1 + 0x10)) == (Arg1 + 16)) goto loc_0092F856;
loc_0092F788:
    v_stack_m58 = 0;
    v_stack_m60 = 0;
    v_stack_m68 = v_stack_m40;
    v_stack_m70 = 0;
    v_stack_m78 = (uint32_t)(local_r11 + 1);
    result = DrvDbOpenObjectRegKey(v_stack_p8, *(uint64_t *)(arg1 + 0x10), 5, Arg2);
    local_r11 = 0;
    if (!sign_flag) goto loc_0092F85D;
    if (((uint32_t)(result)) != 0xC0000034ULL) goto loc_0092F827;
loc_0092F7CE:
loc_0092F7D1:
    result = (v_stack_p8) + (16);
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x10))) != result) goto loc_0092F788;
    if (sign_flag) goto loc_0092F82A;
loc_0092F7E8:
    if ((uint8_t)(v_stack_p20) == 0) goto loc_0092F856;
    if ((*(uint32_t *)(arg8)) == 0) goto loc_0092FA5E;
    *(uint32_t *)(arg5) = 0x2012ULL;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg8))) + (2));
    *(uint32_t *)(arg8) = (uint32_t)(result);
    if (Arg6 == 0) goto loc_0092FA2F;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) > Arg7) goto loc_0092FA2F;
    result = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))) >> (1);
    *(uint16_t *)(Arg6 + result * 2 - 0x2) = 0;
    goto loc_0092F82E;
loc_0092F827:
loc_0092F82A:
    if (0 == ((uint32_t)((uint32_t)(0xC0000023ULL)))) goto loc_0092F7E8;
loc_0092F82E:
    if (v_stack_m40 != 0) goto loc_0092FA68;
loc_0092F83B:
    local_rsp = (local_rsp) + (96);
    return 0;
loc_0092F856:
    goto loc_0092F82E;
loc_0092F85D:
    Arg4 = (uint32_t)(((uint32_t)(Arg7)) - ((uint32_t)((uint32_t)(v_stack_m44))));
    Arg4 = (uint32_t)((Arg4) >> (1));
    v_stack_p20 = (uint8_t)(local_r11 + 1);
    v_stack_p28 = Arg8;
    v_stack_p20 = v_stack_m48;
    result = DrvDbGetDeviceIdDriverInfMatches(v_stack_m40, v_stack_m40, Arg6 + (uint32_t)(v_stack_m44) * 1, Arg4);
    result = ZwClose(v_stack_m40, v_stack_m40, Arg6 + (uint32_t)(v_stack_m44) * 1, Arg4);
    local_r11 = 0;
    v_stack_m40 = 0;
    if (sign_flag) goto loc_0092FA13;
loc_0092F8A5:
    result = (uint32_t)(((uint32_t)(v_stack_m48)) + ((uint32_t)((uint32_t)(v_stack_m48))));
    Arg1 = result - 2;
    if (((uint32_t)(result)) <= 2) { Arg1 = (uint32_t)(result); }
    if (Arg6 != 0) {
        Arg2 = v_stack_m44;
        result = Arg1 + Arg2 * 1;
        if (((uint32_t)(result)) < Arg7) { Arg2 = (uint32_t)(result); }
        v_stack_m44 = (uint32_t)(Arg2);
    }
    goto loc_0092F7D1;
loc_0092F8CE:
    result = (*(uint64_t *)(arg4)) - (*(uint64_t *)(v_rip - 0x91D9C8));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(arg4 + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x91D9CD));
    }
    if (result != 0) goto loc_0092F966;
    result = (uint32_t)(((uint32_t)(Arg7)) >> (1));
    v_stack_p28 = Arg8;
    v_stack_p20 = (uint32_t)(result);
    *(uint32_t *)(Arg6) = 18;
    result = DrvDbGetObjectDatabaseNodeName(Arg1, 5, Arg2, Arg6);
    if ((((uint32_t)((uint32_t)(0x80000000ULL))) & ((uint32_t)(result + (uint32_t)(0x80000000ULL) * 1))) != 0) goto loc_0092F92C;
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0xC0000023ULL)))) goto loc_0092F82E;
loc_0092F92C:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg8))) + ((uint32_t)((uint32_t)(*(uint32_t *)(arg8)))));
    *(uint32_t *)(arg8) = (uint32_t)(Arg1);
    goto loc_0092F82E;
loc_0092F937:
loc_0092F93A:
    if (0 >= ((uint32_t)(local_r11 + 1))) goto loc_0092FA54;
    if ((*(uint32_t *)(*(uint64_t *)(v_rip - 0x92D870 + 0x0 + 0x0 * 4 * 8) + 0x10)) == ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10))))) goto loc_0092FA36;
loc_0092F961:
    Arg2 = (uint32_t)((0) + ((uint32_t)(local_r11 + 1)));
    goto loc_0092F93A;
loc_0092F966:
    result = (*(uint64_t *)(Arg6)) - (*(uint64_t *)(v_rip - 0x91DA48));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(Arg6 + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x91DA4D));
    }
    if (result != 0) goto loc_0092F937;
loc_0092F982:
    goto loc_0092F734;
loc_0092F98A:
    Arg2 = 0;
    if (((uint32_t)((uint32_t)(result))) != -1) { Arg2 = (uint32_t)((uint32_t)(result)); }
    if (Arg2 != NULL) goto loc_0092F9D4;
    v_stack_p40 = 0;
    v_stack_p38 = 0;
    v_stack_p30 = v_stack_m40;
    v_stack_p28 = 0;
    v_stack_p20 = (uint32_t)(local_r11 + 1);
    result = DrvDbOpenObjectRegKey(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10)), Arg2, Arg2 + 5, Arg2);
    if (sign_flag) goto loc_0092F82E;
loc_0092F9D4:
    Arg4 = (uint32_t)(((uint32_t)(Arg7)) >> (1));
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_m48;
    result = DrvDbGetDeviceIdDriverInfMatches(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10)), v_stack_m40, Arg6, Arg4);
    result = (uint32_t)((result) + ((uint32_t)((uint32_t)(0x80000000ULL))));
    if ((((uint32_t)((uint32_t)(0x80000000ULL))) & ((uint32_t)(result))) == 0) goto loc_0092FA72;
loc_0092F9FF:
    result = (uint32_t)(((uint32_t)(v_stack_m48)) + ((uint32_t)((uint32_t)(v_stack_m48))));
    *(uint32_t *)(Arg6) = 0x2012ULL;
    *(uint32_t *)(arg8) = (uint32_t)(result);
    goto loc_0092F82E;
loc_0092FA13:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 0xC0000225ULL) goto loc_0092F7CE;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 0) goto loc_0092F8A5;
    goto loc_0092F82A;
loc_0092FA2F:
    goto loc_0092F82E;
loc_0092FA36:
    Arg1 = (*(uint64_t *)(Arg6)) - (*(uint64_t *)(arg4));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint64_t *)(Arg6 + 0x8);
        Arg1 = (Arg1) - (*(uint64_t *)(arg4 + 0x8));
    }
    if (Arg1 != NULL) goto loc_0092F961;
    if (0 != 0) goto loc_0092FA80;
loc_0092FA54:
    goto loc_0092F83B;
loc_0092FA5E:
    goto loc_0092F82E;
loc_0092FA68:
    result = ZwClose(Arg1, (uint32_t)(0x80000000ULL), Arg6, Arg4);
    goto loc_0092F83B;
loc_0092FA72:
    if (((uint32_t)((uint32_t)(0xC0000225ULL))) == ((uint32_t)((uint32_t)(0xC0000023ULL)))) goto loc_0092F9FF;
    goto loc_0092F82E;
loc_0092FA80:
    v_stack_p28 = 0;
    Arg4 = 0;
    v_stack_p20 = v_stack_m40;
    result = DrvDbOpenDeviceIdRegKey(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10)), Arg2, (uint32_t)((uint32_t)(local_r11 + 1)), Arg4);
    if (sign_flag) goto loc_0092F82E;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg2` | `+ 0x0` | `16` | `R` |
| `Arg2` | `+ 0x2` | `64` | `R` |
| `Arg4` | `+ 0x0` | `64` | `R` |
| `Arg4` | `+ 0x8` | `64` | `R` |
| `Arg4` | `+ 0x10` | `32` | `R` |
| `Arg5` | `+ 0x0` | `32` | `W` |
| `Arg8` | `+ 0x0` | `32` | `R` |
| `Arg8` | `+ 0x0` | `32` | `R/W` |
| `Arg8` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0092F690&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
