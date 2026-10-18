# SepAccessCheckEx

- RVA: `0x003CF7B0`–`0x003CFD85` (길이 `1,493` bytes)
- VA: `0x00000001403CF7B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00090FB4`
- 디코드: `340`개 명령, `1,493/1,493` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **7**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x003CFA0C` → [SepNormalAccessCheckEx](SepNormalAccessCheckEx_function_003CFD8C.md) (function, `0x003CFD8C`)
- `0x003CFA4E` → [Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline](../4E/Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline_function_004EF788.md) (function, `0x004EF788`)
- `0x003CFB04` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x003CFB7C` → [SepSinglePrivilegeCheck](../3D/SepSinglePrivilegeCheck_function_003D191C.md) (function, `0x003D191C`)
- `0x003CFC34` → [SepAssemblePrivileges](../../page/A2/SepAssemblePrivileges_function_00A210BC.md) (function, `0x00A210BC`)
- `0x003CFC6D` → [SepSinglePrivilegeCheck](../3D/SepSinglePrivilegeCheck_function_003D191C.md) (function, `0x003D191C`)
- `0x003CFCAF` → [Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline](../4E/Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline_function_004EF788.md) (function, `0x004EF788`)

### Direct callers
- [SepCommonAccessCheckEx](../47/SepCommonAccessCheckEx_function_0047602C.md) at `0x004768C7`
- [SepCommonAccessCheckEx](../47/SepCommonAccessCheckEx_function_0047602C.md) at `0x00476CC5`
- [SepCommonAccessCheckEx](../47/SepCommonAccessCheckEx_function_0047602C.md) at `0x00476E59`

### Static image references
- `0x003CF7C7` → RVA `0x00E0A740` (`.data`; read)
- `0x003CFB75` → RVA `0x00FD9B38` (`PAGEDATA`; read)
- `0x003CFC66` → RVA `0x00FD9B00` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x003CFC34` → [SepAssemblePrivileges](../../page/A2/SepAssemblePrivileges_function_00A210BC.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **19**
  - `0x003CF960` → [sub_006E89DA + 0x368](../6E/Unknown_function_006E89DA.md) (`tail-transfer`)
  - `0x003CF969` → [sub_006E89DA + 0x368](../6E/Unknown_function_006E89DA.md) (`tail-transfer`)
  - `0x003CF9A3` → [sub_006E89DA + 0x1B7](../6E/Unknown_function_006E89DA.md) (`tail-transfer`)
  - `0x003CFB65` → [sub_006E89DA + 0x12A](../6E/Unknown_function_006E89DA.md) (`tail-transfer`)
  - `0x003CFB83` → [sub_006E89DA + 0x82](../6E/Unknown_function_006E89DA.md) (`tail-transfer`)
  - `0x003CFC56` → [sub_006E89DA + 0x424](../6E/Unknown_function_006E89DA.md) (`tail-transfer`)
  - `0x003CFC82` → [sub_006E89DA + 0x2F](../6E/Unknown_function_006E89DA.md) (`tail-transfer`)
  - `0x003CFC95` → [sub_006E89DA + 0x18](../6E/Unknown_function_006E89DA.md) (`tail-transfer`)
  - `0x003CFCC0` → [sub_006E89DA + 0xE6](../6E/Unknown_function_006E89DA.md) (`tail-transfer`)
  - `0x003CFCCC` → [sub_006E89DA + 0xE6](../6E/Unknown_function_006E89DA.md) (`tail-transfer`)
  - `0x003CFCD9` → [sub_006E89DA + 0x424](../6E/Unknown_function_006E89DA.md) (`tail-transfer`)
  - `0x003CFCE3` → [sub_006E89DA + 0x424](../6E/Unknown_function_006E89DA.md) (`tail-transfer`)
  - `0x003CFD05` → [sub_006E89DA + 0x18E](../6E/Unknown_function_006E89DA.md) (`tail-transfer`)
  - `0x003CFD18` → [sub_006E89DA + 0x18E](../6E/Unknown_function_006E89DA.md) (`tail-transfer`)
  - `0x003CFD41` → [sub_006E89DA + 0x196](../6E/Unknown_function_006E89DA.md) (`tail-transfer`)
  - `0x003CFD53` → [sub_006E89DA + 0x1AC](../6E/Unknown_function_006E89DA.md) (`tail-transfer`)
  - `0x003CFD5D` → [sub_006E89DA + 0x1AC](../6E/Unknown_function_006E89DA.md) (`tail-transfer`)
  - `0x003CFD6C` → [sub_006E89DA + 0x1AC](../6E/Unknown_function_006E89DA.md) (`tail-transfer`)
  - `0x003CFD76` → [sub_006E89DA + 0x1A9](../6E/Unknown_function_006E89DA.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003CF7B0  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
003CF7B5  55                              push rbp
003CF7B6  56                              push rsi
003CF7B7  57                              push rdi
003CF7B8  41 54                           push r12
003CF7BA  41 55                           push r13
003CF7BC  41 56                           push r14
003CF7BE  41 57                           push r15
003CF7C0  48 81 EC 00 01 00 00            sub rsp, 0x100
003CF7C7  48 8B 05 72 AF A3 00            mov rax, qword ptr [rip + 0xa3af72]
003CF7CE  48 33 C4                        xor rax, rsp
003CF7D1  48 89 84 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], rax
003CF7D9  44 8B 94 24 60 01 00 00         mov r10d, dword ptr [rsp + 0x160]
003CF7E1  45 33 DB                        xor r11d, r11d
003CF7E4  4C 8B B4 24 68 01 00 00         mov r14, qword ptr [rsp + 0x168]
003CF7EC  4C 8B E9                        mov r13, rcx
003CF7EF  48 8B 8C 24 90 01 00 00         mov rcx, qword ptr [rsp + 0x190]
003CF7F7  49 8B C0                        mov rax, r8
003CF7FA  4C 8B 84 24 D8 01 00 00         mov r8, qword ptr [rsp + 0x1d8]
003CF802  4D 8B E1                        mov r12, r9
003CF805  4C 8B 8C 24 78 01 00 00         mov r9, qword ptr [rsp + 0x178]
003CF80D  0F 57 C0                        xorps xmm0, xmm0
003CF810  48 8B 94 24 A8 01 00 00         mov rdx, qword ptr [rsp + 0x1a8]
003CF818  4D 85 E4                        test r12, r12
003CF81B  48 8B 9C 24 C8 01 00 00         mov rbx, qword ptr [rsp + 0x1c8]
003CF823  41 BF 01 00 00 00               mov r15d, 1
003CF829  48 89 8C 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rcx
003CF831  4C 0F 44 E0                     cmove r12, rax
003CF835  48 8B 8C 24 98 01 00 00         mov rcx, qword ptr [rsp + 0x198]
003CF83D  41 8B F2                        mov esi, r10d
003CF840  48 89 8C 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rcx
003CF848  48 8B 8C 24 A0 01 00 00         mov rcx, qword ptr [rsp + 0x1a0]
003CF850  48 89 8C 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rcx
003CF858  48 8B 8C 24 D0 01 00 00         mov rcx, qword ptr [rsp + 0x1d0]
003CF860  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
003CF868  8B 84 24 70 01 00 00            mov eax, dword ptr [rsp + 0x170]
003CF86F  48 89 8C 24 98 00 00 00         mov qword ptr [rsp + 0x98], rcx
003CF877  4C 89 8C 24 90 00 00 00         mov qword ptr [rsp + 0x90], r9
003CF87F  4C 89 84 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], r8
003CF887  44 89 5C 24 74                  mov dword ptr [rsp + 0x74], r11d
003CF88C  44 88 5C 24 72                  mov byte ptr [rsp + 0x72], r11b
003CF891  44 88 5C 24 70                  mov byte ptr [rsp + 0x70], r11b
003CF896  44 88 5C 24 71                  mov byte ptr [rsp + 0x71], r11b
003CF89B  4C 89 A4 24 80 00 00 00         mov qword ptr [rsp + 0x80], r12
003CF8A3  0F 11 84 24 C8 00 00 00         movups xmmword ptr [rsp + 0xc8], xmm0
003CF8AB  0F 11 84 24 D8 00 00 00         movups xmmword ptr [rsp + 0xd8], xmm0
003CF8B3  0F 11 84 24 E8 00 00 00         movups xmmword ptr [rsp + 0xe8], xmm0
003CF8BB  85 C0                           test eax, eax
003CF8BD  75 2B                           jne 0x1403cf8ea
003CF8BF  83 8C 24 DC 00 00 00 FF         or dword ptr [rsp + 0xdc], 0xffffffff
003CF8C7  4C 8D B4 24 C8 00 00 00         lea r14, [rsp + 0xc8]
003CF8CF  41 8B EF                        mov ebp, r15d
003CF8D2  49 8D 46 28                     lea rax, [r14 + 0x28]
003CF8D6  8B CD                           mov ecx, ebp
003CF8D8  48 89 10                        mov qword ptr [rax], rdx
003CF8DB  48 83 EA 80                     sub rdx, -0x80
003CF8DF  48 8D 40 30                     lea rax, [rax + 0x30]
003CF8E3  49 2B CF                        sub rcx, r15
003CF8E6  75 F0                           jne 0x1403cf8d8
003CF8E8  EB 06                           jmp 0x1403cf8f0
003CF8EA  8B E8                           mov ebp, eax
003CF8EC  85 C0                           test eax, eax
003CF8EE  75 E2                           jne 0x1403cf8d2
003CF8F0  41 0F BA E2 18                  bt r10d, 0x18
003CF8F5  0F 82 60 03 00 00               jb 0x1403cfc5b
003CF8FB  8B BC 24 80 01 00 00            mov edi, dword ptr [rsp + 0x180]
003CF902  41 0F B7 55 02                  movzx edx, word ptr [r13 + 2]
003CF907  B9 00 80 00 00                  mov ecx, 0x8000
003CF90C  0F B7 C2                        movzx eax, dx
003CF90F  44 0F B7 C2                     movzx r8d, dx
003CF913  66 23 C1                        and ax, cx
003CF916  66 41 83 E0 04                  and r8w, 4
003CF91B  74 15                           je 0x1403cf932
003CF91D  66 85 C0                        test ax, ax
003CF920  0F 84 74 03 00 00               je 0x1403cfc9a
003CF926  41 8B 4D 10                     mov ecx, dword ptr [r13 + 0x10]
003CF92A  85 C9                           test ecx, ecx
003CF92C  74 04                           je 0x1403cf932
003CF92E  4E 8D 1C 29                     lea r11, [rcx + r13]
003CF932  4C 89 9C 24 88 00 00 00         mov qword ptr [rsp + 0x88], r11
003CF93A  F6 C2 10                        test dl, 0x10
003CF93D  74 15                           je 0x1403cf954
003CF93F  66 85 C0                        test ax, ax
003CF942  0F 84 5B 03 00 00               je 0x1403cfca3
003CF948  41 8B 45 0C                     mov eax, dword ptr [r13 + 0xc]
003CF94C  85 C0                           test eax, eax
003CF94E  0F 85 D1 01 00 00               jne 0x1403cfb25
003CF954  45 33 ED                        xor r13d, r13d
003CF957  4C 89 6C 24 78                  mov qword ptr [rsp + 0x78], r13
003CF95C  66 45 85 C0                     test r8w, r8w
003CF960  0F 84 DC 93 31 00               je 0x1406e8d42
003CF966  4D 85 DB                        test r11, r11
003CF969  0F 84 D3 93 31 00               je 0x1406e8d42
003CF96F  41 BA 00 00 08 00               mov r10d, 0x80000
003CF975  41 85 F2                        test r10d, esi
003CF978  0F 85 EC 01 00 00               jne 0x1403cfb6a
003CF97E  44 8A 6C 24 70                  mov r13b, byte ptr [rsp + 0x70]
003CF983  33 C9                           xor ecx, ecx
003CF985  66 41 39 4B 04                  cmp word ptr [r11 + 4], cx
003CF98A  0F 84 1C 03 00 00               je 0x1403cfcac
003CF990  41 BC 00 00 00 02               mov r12d, 0x2000000
003CF996  48 89 5C 24 68                  mov qword ptr [rsp + 0x68], rbx
003CF99B  44 85 A4 24 60 01 00 00         test dword ptr [rsp + 0x160], r12d
003CF9A3  0F 85 E8 91 31 00               jne 0x1406e8b91
003CF9A9  8B 84 24 70 01 00 00            mov eax, dword ptr [rsp + 0x170]
003CF9B0  4D 8B CB                        mov r9, r11
003CF9B3  44 8A A4 24 C0 01 00 00         mov r12b, byte ptr [rsp + 0x1c0]
003CF9BB  44 8A AC 24 B8 01 00 00         mov r13b, byte ptr [rsp + 0x1b8]
003CF9C3  4C 8B 84 24 A0 00 00 00         mov r8, qword ptr [rsp + 0xa0]
003CF9CB  48 8B 94 24 80 00 00 00         mov rdx, qword ptr [rsp + 0x80]
003CF9D3  44 88 64 24 60                  mov byte ptr [rsp + 0x60], r12b
003CF9D8  44 88 6C 24 58                  mov byte ptr [rsp + 0x58], r13b
003CF9DD  88 4C 24 50                     mov byte ptr [rsp + 0x50], cl
003CF9E1  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
003CF9E5  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
003CF9ED  4C 89 74 24 40                  mov qword ptr [rsp + 0x40], r14
003CF9F2  89 6C 24 38                     mov dword ptr [rsp + 0x38], ebp
003CF9F6  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
003CF9FB  8B CE                           mov ecx, esi
003CF9FD  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
003CFA02  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
003CFA07  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
003CFA0C  E8 7B 03 00 00                  call 0x1403cfd8c
003CFA11  41 8B 46 18                     mov eax, dword ptr [r14 + 0x18]
003CFA15  33 C9                           xor ecx, ecx
003CFA17  89 43 0C                        mov dword ptr [rbx + 0xc], eax
003CFA1A  41 39 4E 18                     cmp dword ptr [r14 + 0x18], ecx
003CFA1E  0F 85 AD 02 00 00               jne 0x1403cfcd1
003CFA24  48 8B 94 24 80 00 00 00         mov rdx, qword ptr [rsp + 0x80]
003CFA2C  8B 82 C8 00 00 00               mov eax, dword ptr [rdx + 0xc8]
003CFA32  A8 10                           test al, 0x10
003CFA34  0F 85 FB 00 00 00               jne 0x1403cfb35
003CFA3A  45 33 ED                        xor r13d, r13d
003CFA3D  41 8B 46 18                     mov eax, dword ptr [r14 + 0x18]
003CFA41  89 43 0C                        mov dword ptr [rbx + 0xc], eax
003CFA44  45 39 6E 18                     cmp dword ptr [r14 + 0x18], r13d
003CFA48  0F 85 90 02 00 00               jne 0x1403cfcde
003CFA4E  E8 35 FD 11 00                  call 0x1404ef788
003CFA53  4C 8B 94 24 80 00 00 00         mov r10, qword ptr [rsp + 0x80]
003CFA5B  41 8B 92 C8 00 00 00            mov edx, dword ptr [r10 + 0xc8]
003CFA62  85 C0                           test eax, eax
003CFA64  0F 84 C2 02 00 00               je 0x1403cfd2c
003CFA6A  8B C2                           mov eax, edx
003CFA6C  25 00 60 00 00                  and eax, 0x6000
003CFA71  3D 00 20 00 00                  cmp eax, 0x2000
003CFA76  74 33                           je 0x1403cfaab
003CFA78  0B B4 24 60 01 00 00            or esi, dword ptr [rsp + 0x160]
003CFA7F  0F BA E2 0E                     bt edx, 0xe
003CFA83  0F 83 81 02 00 00               jae 0x1403cfd0a
003CFA89  8B 4B 08                        mov ecx, dword ptr [rbx + 8]
003CFA8C  8B C6                           mov eax, esi
003CFA8E  0B 4B 04                        or ecx, dword ptr [rbx + 4]
003CFA91  0B 03                           or eax, dword ptr [rbx]
003CFA93  F7 D1                           not ecx
003CFA95  8B F1                           mov esi, ecx
003CFA97  23 F0                           and esi, eax
003CFA99  0F 85 49 02 00 00               jne 0x1403cfce8
003CFA9F  41 89 76 18                     mov dword ptr [r14 + 0x18], esi
003CFAA3  85 F6                           test esi, esi
003CFAA5  0F 85 33 02 00 00               jne 0x1403cfcde
003CFAAB  0B BC 24 60 01 00 00            or edi, dword ptr [rsp + 0x160]
003CFAB2  41 8B DD                        mov ebx, r13d
003CFAB5  44 8A 6C 24 70                  mov r13b, byte ptr [rsp + 0x70]
003CFABA  85 FF                           test edi, edi
003CFABC  0F 84 B9 02 00 00               je 0x1403cfd7b
003CFAC2  44 0F 20 C0                     mov rax, cr8
003CFAC6  3C 02                           cmp al, 2
003CFAC8  0F 82 3F 01 00 00               jb 0x1403cfc0d
003CFACE  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
003CFAD6  89 18                           mov dword ptr [rax], ebx
003CFAD8  48 8B 84 24 B8 00 00 00         mov rax, qword ptr [rsp + 0xb8]
003CFAE0  89 38                           mov dword ptr [rax], edi
003CFAE2  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
003CFAEA  48 85 C0                        test rax, rax
003CFAED  74 07                           je 0x1403cfaf6
003CFAEF  85 DB                           test ebx, ebx
003CFAF1  0F 99 C1                        setns cl
003CFAF4  88 08                           mov byte ptr [rax], cl
003CFAF6  41 8A C7                        mov al, r15b
003CFAF9  48 8B 8C 24 F8 00 00 00         mov rcx, qword ptr [rsp + 0xf8]
003CFB01  48 33 CC                        xor rcx, rsp
003CFB04  E8 37 CB 2D 00                  call 0x1406ac640
003CFB09  48 8B 9C 24 48 01 00 00         mov rbx, qword ptr [rsp + 0x148]
003CFB11  48 81 C4 00 01 00 00            add rsp, 0x100
003CFB18  41 5F                           pop r15
003CFB1A  41 5E                           pop r14
003CFB1C  41 5D                           pop r13
003CFB1E  41 5C                           pop r12
003CFB20  5F                              pop rdi
003CFB21  5E                              pop rsi
003CFB22  5D                              pop rbp
003CFB23  C3                              ret
003CFB24  CC                              int3
003CFB25  49 03 C5                        add rax, r13
003CFB28  45 33 ED                        xor r13d, r13d
003CFB2B  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
003CFB30  E9 27 FE FF FF                  jmp 0x1403cf95c
003CFB35  A8 08                           test al, 8
003CFB37  0F 84 BA 00 00 00               je 0x1403cfbf7
003CFB3D  4C 8B 84 24 90 00 00 00         mov r8, qword ptr [rsp + 0x90]
003CFB45  41 8B 48 08                     mov ecx, dword ptr [r8 + 8]
003CFB49  41 0B 08                        or ecx, dword ptr [r8]
003CFB4C  F7 D1                           not ecx
003CFB4E  41 23 48 04                     and ecx, dword ptr [r8 + 4]
003CFB52  81 C9 00 00 0D 01               or ecx, 0x10d0000
003CFB58  85 8C 24 60 01 00 00            test dword ptr [rsp + 0x160], ecx
003CFB5F  0F 84 D5 FE FF FF               je 0x1403cfa3a
003CFB65  E9 9A 8F 31 00                  jmp 0x1406e8b04
003CFB6A  44 8A 84 24 88 01 00 00         mov r8b, byte ptr [rsp + 0x188]
003CFB72  49 8B D4                        mov rdx, r12
003CFB75  48 8B 0D BC 9F C0 00            mov rcx, qword ptr [rip + 0xc09fbc]
003CFB7C  E8 9B 1D 00 00                  call 0x1403d191c
003CFB81  84 C0                           test al, al
003CFB83  0F 84 D3 8E 31 00               je 0x1406e8a5c
003CFB89  0F BA F6 13                     btr esi, 0x13
003CFB8D  41 0B FA                        or edi, r10d
003CFB90  85 ED                           test ebp, ebp
003CFB92  74 41                           je 0x1403cfbd5
003CFB94  4D 8D 4E 28                     lea r9, [r14 + 0x28]
003CFB98  44 8B D5                        mov r10d, ebp
003CFB9B  4D 8B 01                        mov r8, qword ptr [r9]
003CFB9E  41 8B C7                        mov eax, r15d
003CFBA1  41 8B D5                        mov edx, r13d
003CFBA4  4D 85 C0                        test r8, r8
003CFBA7  74 23                           je 0x1403cfbcc
003CFBA9  85 C0                           test eax, eax
003CFBAB  74 1F                           je 0x1403cfbcc
003CFBAD  0F BA E0 13                     bt eax, 0x13
003CFBB1  72 07                           jb 0x1403cfbba
003CFBB3  41 03 D7                        add edx, r15d
003CFBB6  03 C0                           add eax, eax
003CFBB8  EB EF                           jmp 0x1403cfba9
003CFBBA  8B CA                           mov ecx, edx
003CFBBC  45 39 2C 88                     cmp dword ptr [r8 + rcx*4], r13d
003CFBC0  75 F1                           jne 0x1403cfbb3
003CFBC2  41 C7 04 88 09 00 20 00         mov dword ptr [r8 + rcx*4], 0x200009
003CFBCA  EB E7                           jmp 0x1403cfbb3
003CFBCC  49 83 C1 30                     add r9, 0x30
003CFBD0  4D 2B D7                        sub r10, r15
003CFBD3  75 C6                           jne 0x1403cfb9b
003CFBD5  44 01 7C 24 74                  add dword ptr [rsp + 0x74], r15d
003CFBDA  33 C9                           xor ecx, ecx
003CFBDC  44 88 7C 24 70                  mov byte ptr [rsp + 0x70], r15b
003CFBE1  45 8A EF                        mov r13b, r15b
003CFBE4  85 F6                           test esi, esi
003CFBE6  0F 85 99 FD FF FF               jne 0x1403cf985
003CFBEC  45 33 DB                        xor r11d, r11d
003CFBEF  41 8B DB                        mov ebx, r11d
003CFBF2  E9 C3 FE FF FF                  jmp 0x1403cfaba
003CFBF7  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
003CFBFF  8B 49 0C                        mov ecx, dword ptr [rcx + 0xc]
003CFC02  81 C9 FF FF 1F 00               or ecx, 0x1fffff
003CFC08  E9 4B FF FF FF                  jmp 0x1403cfb58
003CFC0D  8B 44 24 74                     mov eax, dword ptr [rsp + 0x74]
003CFC11  85 C0                           test eax, eax
003CFC13  0F 84 B5 FE FF FF               je 0x1403cface
003CFC19  48 8B B4 24 A8 00 00 00         mov rsi, qword ptr [rsp + 0xa8]
003CFC21  45 8A C5                        mov r8b, r13b
003CFC24  44 8A 4C 24 71                  mov r9b, byte ptr [rsp + 0x71]
003CFC29  8B C8                           mov ecx, eax
003CFC2B  8A 54 24 72                     mov dl, byte ptr [rsp + 0x72]
003CFC2F  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
003CFC34  E8 83 14 65 00                  call 0x140a210bc
003CFC39  45 33 ED                        xor r13d, r13d
003CFC3C  48 85 F6                        test rsi, rsi
003CFC3F  0F 84 89 FE FF FF               je 0x1403cface
003CFC45  4C 39 2E                        cmp qword ptr [rsi], r13
003CFC48  0F 85 80 FE FF FF               jne 0x1403cface
003CFC4E  45 8A FD                        mov r15b, r13b
003CFC51  BB 17 00 00 C0                  mov ebx, 0xc0000017
003CFC56  E9 A3 91 31 00                  jmp 0x1406e8dfe
003CFC5B  44 8A 84 24 88 01 00 00         mov r8b, byte ptr [rsp + 0x188]
003CFC63  49 8B D4                        mov rdx, r12
003CFC66  48 8B 0D 93 9E C0 00            mov rcx, qword ptr [rip + 0xc09e93]
003CFC6D  E8 AA 1C 00 00                  call 0x1403d191c
003CFC72  4D 8B CE                        mov r9, r14
003CFC75  B9 00 00 00 01                  mov ecx, 0x1000000
003CFC7A  41 B8 08 00 00 00               mov r8d, 8
003CFC80  84 C0                           test al, al
003CFC82  0F 85 81 8D 31 00               jne 0x1406e8a09
003CFC88  45 33 ED                        xor r13d, r13d
003CFC8B  BB 61 00 00 C0                  mov ebx, 0xc0000061
003CFC90  BA 00 00 10 00                  mov edx, 0x100000
003CFC95  E9 58 8D 31 00                  jmp 0x1406e89f2
003CFC9A  4D 8B 5D 20                     mov r11, qword ptr [r13 + 0x20]
003CFC9E  E9 8F FC FF FF                  jmp 0x1403cf932
003CFCA3  49 8B 45 18                     mov rax, qword ptr [r13 + 0x18]
003CFCA7  E9 7C FE FF FF                  jmp 0x1403cfb28
003CFCAC  89 73 0C                        mov dword ptr [rbx + 0xc], esi
003CFCAF  E8 D4 FA 11 00                  call 0x1404ef788
003CFCB4  41 8B 8C 24 C8 00 00 00         mov ecx, dword ptr [r12 + 0xc8]
003CFCBC  0F BA E1 0E                     bt ecx, 0xe
003CFCC0  0F 83 FA 8D 31 00               jae 0x1406e8ac0
003CFCC6  8B 03                           mov eax, dword ptr [rbx]
003CFCC8  F7 D0                           not eax
003CFCCA  23 F8                           and edi, eax
003CFCCC  E9 EF 8D 31 00                  jmp 0x1406e8ac0
003CFCD1  BB 22 00 00 C0                  mov ebx, 0xc0000022
003CFCD6  45 33 ED                        xor r13d, r13d
003CFCD9  E9 20 91 31 00                  jmp 0x1406e8dfe
003CFCDE  BB 22 00 00 C0                  mov ebx, 0xc0000022
003CFCE3  E9 16 91 31 00                  jmp 0x1406e8dfe
003CFCE8  44 39 6B 0C                     cmp dword ptr [rbx + 0xc], r13d
003CFCEC  0F 85 AD FD FF FF               jne 0x1403cfa9f
003CFCF2  B8 00 00 00 03                  mov eax, 0x3000000
003CFCF7  23 D0                           and edx, eax
003CFCF9  3B D0                           cmp edx, eax
003CFCFB  0F 85 9E FD FF FF               jne 0x1403cfa9f
003CFD01  44 88 7B 17                     mov byte ptr [rbx + 0x17], r15b
003CFD05  E9 5E 8E 31 00                  jmp 0x1406e8b68
003CFD0A  0F BA E2 0D                     bt edx, 0xd
003CFD0E  0F 82 8B FD FF FF               jb 0x1403cfa9f
003CFD14  44 38 6B 14                     cmp byte ptr [rbx + 0x14], r13b
003CFD18  0F 84 4A 8E 31 00               je 0x1406e8b68
003CFD1E  8B 43 04                        mov eax, dword ptr [rbx + 4]
003CFD21  0B 33                           or esi, dword ptr [rbx]
003CFD23  F7 D0                           not eax
003CFD25  23 F0                           and esi, eax
003CFD27  E9 73 FD FF FF                  jmp 0x1403cfa9f
003CFD2C  0F BA E2 0D                     bt edx, 0xd
003CFD30  0F 82 75 FD FF FF               jb 0x1403cfaab
003CFD36  0B B4 24 60 01 00 00            or esi, dword ptr [rsp + 0x160]
003CFD3D  0F BA E2 0E                     bt edx, 0xe
003CFD41  0F 83 29 8E 31 00               jae 0x1406e8b70
003CFD47  8B 4B 08                        mov ecx, dword ptr [rbx + 8]
003CFD4A  0B 4B 04                        or ecx, dword ptr [rbx + 4]
003CFD4D  0B 33                           or esi, dword ptr [rbx]
003CFD4F  F7 D1                           not ecx
003CFD51  23 CE                           and ecx, esi
003CFD53  0F 84 2D 8E 31 00               je 0x1406e8b86
003CFD59  44 39 6B 0C                     cmp dword ptr [rbx + 0xc], r13d
003CFD5D  0F 85 23 8E 31 00               jne 0x1406e8b86
003CFD63  B8 00 00 00 03                  mov eax, 0x3000000
003CFD68  23 D0                           and edx, eax
003CFD6A  3B D0                           cmp edx, eax
003CFD6C  0F 85 14 8E 31 00               jne 0x1406e8b86
003CFD72  44 88 7B 17                     mov byte ptr [rbx + 0x17], r15b
003CFD76  E9 08 8E 31 00                  jmp 0x1406e8b83
003CFD7B  BB 22 00 00 C0                  mov ebx, 0xc0000022
003CFD80  E9 49 FD FF FF                  jmp 0x1403cface
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SepAccessCheckEx(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, __int64 a6, unsigned int a7, __int64 a8, unsigned int a9, unsigned __int8 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, unsigned __int8 a16, unsigned __int8 a17, __int64 a18, __int64 a19, __int64 a20)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r13;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m5C;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC4;
    unsigned __int8 v_stack_mC6;
    unsigned __int8 v_stack_mC7;
    unsigned __int8 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int8 v_stack_mD8;
    unsigned __int8 v_stack_mE0;
    unsigned __int8 v_stack_mE8;
    unsigned int v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p160;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int8 v_stack_p70;
    unsigned __int8 v_stack_p71;
    unsigned __int8 v_stack_p72;
    unsigned int v_stack_p74;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p90;
    unsigned __int64 v_stack_pA8;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (256);
    result = (*(unsigned __int64 *)(v_rip + 10727282)) ^ (v_rsp);
    v_stack_m40 = result;
    v_r11 = 0;
    v_stack_m80 = a11;
    if (a4 == 0) { a4 = a3; }
    v_stack_m90 = a12;
    v_stack_m88 = a13;
    v_stack_m98 = a3;
    v_stack_mA0 = a19;
    v_stack_mA8 = a8;
    v_stack_m78 = a20;
    v_stack_mC4 = 0;
    v_stack_mC6 = 0;
    v_stack_mC8 = 0;
    v_stack_mC7 = 0;
    v_stack_mB8 = a4;
    v_stack_m70 = v_xmm0;
    v_stack_m60 = v_xmm0;
    v_stack_m50 = v_xmm0;
    if ((unsigned int)((unsigned int)(a7)) != 0) goto loc_003CF8EA;
loc_003CF8D2:
loc_003CF8D8:
    *(unsigned __int64 *)(v_stack_m70 + 40) = a14;
    a2 = (a14) - (-128);
    a1 = (1) - (1);
    if (condition_is_not_equal) goto loc_003CF8D8;
    goto loc_003CF8F0;
loc_003CF8EA:
    if ((unsigned int)(v_stack_m70 + 40 + 48) != 0) goto loc_003CF8D2;
loc_003CF8F0:
    if (condition_is_below) goto loc_003CFC5B;
    result = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(a1 + 2))) & ((unsigned __int16)((unsigned int)(0x8000ULL))));
    a3 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(a1 + 2))) & (4));
    if (condition_is_equal) goto loc_003CF932;
    if ((unsigned __int16)(result) == 0) goto loc_003CFC9A;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16))) != 0) {
        v_r11 = (unsigned int)(*(unsigned int *)(a1 + 16)) + a1 * 1;
    }
    v_stack_mB0 = v_r11;
    if ((((unsigned __int8)(*(unsigned __int16 *)(a1 + 2))) & (16)) == 0) goto loc_003CF954;
    if ((unsigned __int16)(result) == 0) goto loc_003CFCA3;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 12))) != 0) goto loc_003CFB25;
loc_003CF954:
    v_r13 = 0;
    v_stack_mC0 = 0;
loc_003CF95C:
    if ((((unsigned int)((unsigned int)(0x80000ULL))) & ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a5)))))) != 0) goto loc_003CFB6A;
    a1 = 0;
loc_003CF985:
    if ((*(unsigned __int16 *)(v_r11 + 4)) == 0) goto loc_003CFCAC;
    v_stack_mD0 = a18;
    v_stack_mD8 = a17;
    v_stack_mE0 = a16;
    v_stack_mE8 = 0;
    v_stack_mF0 = (unsigned int)((unsigned int)(a7));
    v_stack_mF8 = v_stack_m70;
    v_stack_m100 = (unsigned int)((unsigned int)((unsigned int)(v_stack_m70 + 40 + 48)));
    v_stack_m108 = 0;
    v_stack_m110 = v_stack_mA0;
    v_stack_m118 = v_stack_mC0;
    result = SepNormalAccessCheckEx((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a5))))), v_stack_mB8, v_stack_m98, v_r11);
    a1 = 0;
    *(unsigned int *)(a18 + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m70 + 24)));
    if ((*(unsigned int *)(v_stack_m70 + 24)) != 0) goto loc_003CFCD1;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_mB8 + 200)))) & (16)) != 0) goto loc_003CFB35;
loc_003CFA3A:
    v_r13 = 0;
    *(unsigned int *)(a18 + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m70 + 24)));
    if ((*(unsigned int *)(v_stack_m70 + 24)) != 0) goto loc_003CFCDE;
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(a1, v_stack_mB8, v_stack_m98, v_r11);
    if ((unsigned int)(result) == 0) goto loc_003CFD2C;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mB8 + 200))))) & (0x6000ULL));
    if (((unsigned int)(result)) == 0x2000ULL) goto loc_003CFAAB;
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a5)))) | (a5));
    if (condition_is_above_or_equal) goto loc_003CFD0A;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a18 + 8))) | (*(unsigned int *)(a18 + 4)));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) | (*(unsigned int *)(a18)));
    a1 = (unsigned int)(~(a1));
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(a1))) & ((unsigned int)(result)));
    if (condition_is_not_equal) goto loc_003CFCE8;
loc_003CFA9F:
    *(unsigned int *)(v_stack_m70 + 24) = (unsigned int)(v_rsi);
    if ((unsigned int)(v_rsi) != 0) goto loc_003CFCDE;
loc_003CFAAB:
    v_rdi = (unsigned int)(((unsigned int)(a9)) | (a5));
loc_003CFABA:
    if ((unsigned int)(v_rdi) == 0) goto loc_003CFD7B;
    if (((unsigned __int8)(v_cr8)) < 2) goto loc_003CFC0D;
loc_003CFACE:
    *(unsigned int *)(v_stack_m88) = 0;
    *(unsigned int *)(v_stack_m80) = (unsigned int)(v_rdi);
    if (v_stack_m78 != 0) {
        a1 = (!sign_flag) ? 1 : 0;
        *(unsigned __int8 *)(v_stack_m78) = (unsigned __int8)(a1);
    }
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned int)(*(unsigned int *)(v_stack_mB8 + 200)), v_stack_m98, v_r11);
    v_rsp = (v_rsp) + (256);
    return result;
loc_003CFB25:
    result = (result) + (v_stack_mC8);
loc_003CFB28:
    v_r13 = 0;
    v_stack_p78 = result;
    goto loc_003CF95C;
loc_003CFB35:
    if ((((unsigned __int8)(result)) & (8)) == 0) goto loc_003CFBF7;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p90 + 8))) | (*(unsigned int *)(v_stack_p90)));
    a1 = (unsigned int)(~(a1));
    a1 = (unsigned int)((a1) & (*(unsigned int *)(v_stack_p90 + 4)));
    a1 = (unsigned int)((a1) | (0x10D0000ULL));
loc_003CFB58:
    if (((v_stack_p160) & ((unsigned int)(a1))) == 0) goto loc_003CFA3A;
loc_003CFB6A:
    result = SepSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 12623804), a17, a10, v_r11);
    v_rdi = (unsigned int)((v_rdi) | ((unsigned int)(v_stack_mB8)));
    if ((unsigned int)((unsigned int)((unsigned int)(v_stack_m70 + 40 + 48))) == 0) goto loc_003CFBD5;
loc_003CFB9B:
    if (*(unsigned __int64 *)(v_stack_m70 + 40) == 0) goto loc_003CFBCC;
loc_003CFBA9:
    if (1 == 0) goto loc_003CFBCC;
    if (condition_is_below) goto loc_003CFBBA;
loc_003CFBB3:
    a2 = (unsigned int)((0) + (1));
    result = (unsigned int)((1) + (1));
    goto loc_003CFBA9;
loc_003CFBBA:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m70 + 40) + (unsigned int)((unsigned int)(a2)) * 4)) != 0) goto loc_003CFBB3;
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m70 + 40) + (unsigned int)((unsigned int)(a2)) * 4) = 0x200009ULL;
    goto loc_003CFBB3;
loc_003CFBCC:
    a4 = (v_stack_m70 + 40) + (48);
    v_r10 = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m70 + 40 + 48))))) - (1);
    if (condition_is_not_equal) goto loc_003CFB9B;
loc_003CFBD5:
    a1 = 0;
    v_stack_p70 = 1;
    if ((unsigned int)(v_rsi) != 0) goto loc_003CF985;
    v_r11 = 0;
    goto loc_003CFABA;
loc_003CFBF7:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p90 + 12))) | (0x1FFFFFULL));
    goto loc_003CFB58;
loc_003CFC0D:
    if ((unsigned int)((unsigned int)(v_stack_p74)) == 0) goto loc_003CFACE;
    v_stack_p20 = v_stack_pA8;
    result = SepAssemblePrivileges((unsigned int)((unsigned int)((unsigned int)(v_stack_p74))), v_stack_p72, 1, v_stack_p71);
    v_r13 = 0;
    if (v_stack_pA8 == 0) goto loc_003CFACE;
    if ((*(unsigned __int64 *)(v_stack_pA8)) != 0) goto loc_003CFACE;
loc_003CFC5B:
    result = SepSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 12623507), a17, a10, v_stack_p71);
    v_r13 = 0;
loc_003CFC9A:
    goto loc_003CF932;
loc_003CFCA3:
    goto loc_003CFB28;
loc_003CFCAC:
    *(unsigned int *)((unsigned int)(0xC0000061ULL) + 12) = (unsigned int)(v_stack_pA8);
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline((unsigned int)(0x1000000ULL), (unsigned int)(0x100000ULL), 8, v_stack_m70);
    result = (unsigned int)(~((unsigned int)(*(unsigned int *)((unsigned int)(0xC0000061ULL)))));
    v_rdi = (unsigned int)((v_rdi) & ((unsigned int)(result)));
loc_003CFCD1:
    v_r13 = 0;
loc_003CFCDE:
loc_003CFCE8:
    if ((*(unsigned int *)((unsigned int)(0xC0000022ULL) + 12)) != 0) goto loc_003CFA9F;
    a2 = (unsigned int)(((unsigned int)(0x100000ULL)) & ((unsigned int)((unsigned int)(0x3000000ULL))));
    if (((unsigned int)(a2)) != ((unsigned int)((unsigned int)(0x3000000ULL)))) goto loc_003CFA9F;
    *(unsigned __int8 *)((unsigned int)(0xC0000022ULL) + 23) = 0;
loc_003CFD0A:
    if (((unsigned int)(a2)) < ((unsigned int)((unsigned int)(0x3000000ULL)))) goto loc_003CFA9F;
    v_rsi = (unsigned int)((v_stack_pA8) | (*(unsigned int *)((unsigned int)(0xC0000022ULL))));
    result = (unsigned int)(~((unsigned int)(*(unsigned int *)((unsigned int)(0xC0000022ULL) + 4))));
    v_rsi = (unsigned int)((v_rsi) & ((unsigned int)(result)));
    goto loc_003CFA9F;
loc_003CFD2C:
    if (condition_is_below) goto loc_003CFAAB;
    v_rsi = (unsigned int)((v_rsi) | (a5));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)(0xC0000022ULL) + 8))) | (*(unsigned int *)((unsigned int)(0xC0000022ULL) + 4)));
    v_rsi = (unsigned int)((v_rsi) | (*(unsigned int *)((unsigned int)(0xC0000022ULL))));
    a1 = (unsigned int)(~(a1));
    a1 = (unsigned int)((a1) & ((unsigned int)(v_rsi)));
    a2 = (unsigned int)((a2) & ((unsigned int)((unsigned int)(0x3000000ULL))));
    *(unsigned __int8 *)((unsigned int)(0xC0000022ULL) + 23) = 0;
loc_003CFD7B:
    goto loc_003CFACE;
}
```

## 5. (Beta) C Style

```c
int64_t SepAccessCheckEx(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5, int64_t Arg6, uint32_t Arg7, int64_t Arg8, uint32_t Arg9, uint8_t Arg10, int64_t Arg11, int64_t Arg12, int64_t Arg13, int64_t Arg14, uint64_t Arg15, uint8_t Arg16, uint8_t Arg17, void *Arg18, int64_t Arg19, int64_t Arg20)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg18 = (uint8_t *)Arg18;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r13;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m40;
    uint64_t v_stack_m50;
    uint32_t v_stack_m5C;
    uint64_t v_stack_m60;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC4;
    uint8_t v_stack_mC6;
    uint8_t v_stack_mC7;
    uint8_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint8_t v_stack_mD8;
    uint8_t v_stack_mE0;
    uint8_t v_stack_mE8;
    uint32_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p10;
    uint32_t v_stack_p160;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint8_t v_stack_p70;
    uint8_t v_stack_p71;
    uint8_t v_stack_p72;
    uint32_t v_stack_p74;
    uint64_t v_stack_p78;
    uint64_t v_stack_p90;
    uint64_t v_stack_pA8;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (256);
    result = (*(uint64_t *)(v_rip + 0xA3AF72)) ^ (local_rsp);
    v_stack_m40 = result;
    local_r11 = 0;
    v_stack_m80 = Arg11;
    if (Arg4 == 0) { Arg4 = Arg3; }
    v_stack_m90 = Arg12;
    v_stack_m88 = Arg13;
    v_stack_m98 = Arg3;
    v_stack_mA0 = Arg19;
    v_stack_mA8 = Arg8;
    v_stack_m78 = Arg20;
    v_stack_mC4 = 0;
    v_stack_mC6 = 0;
    v_stack_mC8 = 0;
    v_stack_mC7 = 0;
    v_stack_mB8 = Arg4;
    v_stack_m70 = v_xmm0;
    v_stack_m60 = v_xmm0;
    v_stack_m50 = v_xmm0;
    if ((uint32_t)((uint32_t)(Arg7)) != 0) goto loc_003CF8EA;
loc_003CF8D2:
loc_003CF8D8:
    *(uint64_t *)(v_stack_m70 + 0x28) = Arg14;
    Arg2 = (Arg14) - (-128);
    Arg1 = (1) - (1);
    if (condition_is_not_equal) goto loc_003CF8D8;
    goto loc_003CF8F0;
loc_003CF8EA:
    if ((uint32_t)(v_stack_m70 + 40 + 48) != 0) goto loc_003CF8D2;
loc_003CF8F0:
    if (condition_is_below) goto loc_003CFC5B;
    result = (uint16_t)(((uint16_t)(*(uint16_t *)(arg1 + 0x2))) & ((uint16_t)((uint32_t)(0x8000ULL))));
    Arg3 = (uint16_t)(((uint16_t)(*(uint16_t *)(arg1 + 0x2))) & (4));
    if (condition_is_equal) goto loc_003CF932;
    if ((uint16_t)(result) == 0) goto loc_003CFC9A;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10))) != 0) {
        local_r11 = (uint32_t)(*(uint32_t *)(arg1 + 0x10)) + Arg1 * 1;
    }
    v_stack_mB0 = local_r11;
    if ((((uint8_t)(*(uint16_t *)(arg1 + 0x2))) & (16)) == 0) goto loc_003CF954;
    if ((uint16_t)(result) == 0) goto loc_003CFCA3;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xC))) != 0) goto loc_003CFB25;
loc_003CF954:
    local_r13 = 0;
    v_stack_mC0 = 0;
loc_003CF95C:
    if ((((uint32_t)((uint32_t)(0x80000ULL))) & ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg5)))))) != 0) goto loc_003CFB6A;
    Arg1 = 0;
loc_003CF985:
    if ((*(uint16_t *)(local_r11 + 0x4)) == 0) goto loc_003CFCAC;
    v_stack_mD0 = Arg18;
    v_stack_mD8 = Arg17;
    v_stack_mE0 = Arg16;
    v_stack_mE8 = 0;
    v_stack_mF0 = (uint32_t)((uint32_t)(Arg7));
    v_stack_mF8 = v_stack_m70;
    v_stack_m100 = (uint32_t)((uint32_t)((uint32_t)(v_stack_m70 + 40 + 48)));
    v_stack_m108 = 0;
    v_stack_m110 = v_stack_mA0;
    v_stack_m118 = v_stack_mC0;
    result = SepNormalAccessCheckEx((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg5))))), v_stack_mB8, v_stack_m98, local_r11);
    Arg1 = 0;
    *(uint32_t *)(arg18 + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m70 + 0x18)));
    if ((*(uint32_t *)(v_stack_m70 + 0x18)) != 0) goto loc_003CFCD1;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_mB8 + 0xC8)))) & (16)) != 0) goto loc_003CFB35;
loc_003CFA3A:
    local_r13 = 0;
    *(uint32_t *)(arg18 + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m70 + 0x18)));
    if ((*(uint32_t *)(v_stack_m70 + 0x18)) != 0) goto loc_003CFCDE;
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(Arg1, v_stack_mB8, v_stack_m98, local_r11);
    if ((uint32_t)(result) == 0) goto loc_003CFD2C;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mB8 + 0xC8))))) & (0x6000ULL));
    if (((uint32_t)(result)) == 0x2000ULL) goto loc_003CFAAB;
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg5)))) | (Arg5));
    if (condition_is_above_or_equal) goto loc_003CFD0A;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg18 + 0x8))) | (*(uint32_t *)(arg18 + 0x4)));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) | (*(uint32_t *)(arg18)));
    Arg1 = (uint32_t)(~(Arg1));
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) & ((uint32_t)(result)));
    if (condition_is_not_equal) goto loc_003CFCE8;
loc_003CFA9F:
    *(uint32_t *)(v_stack_m70 + 0x18) = (uint32_t)(local_rsi);
    if ((uint32_t)(local_rsi) != 0) goto loc_003CFCDE;
loc_003CFAAB:
    local_rdi = (uint32_t)(((uint32_t)(Arg9)) | (Arg5));
loc_003CFABA:
    if ((uint32_t)(local_rdi) == 0) goto loc_003CFD7B;
    if (((uint8_t)(v_cr8)) < 2) goto loc_003CFC0D;
loc_003CFACE:
    *(uint32_t *)(v_stack_m88) = 0;
    *(uint32_t *)(v_stack_m80) = (uint32_t)(local_rdi);
    if (v_stack_m78 != 0) {
        Arg1 = (!sign_flag) ? 1 : 0;
        *(uint8_t *)(v_stack_m78) = (uint8_t)(Arg1);
    }
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint32_t)(*(uint32_t *)(v_stack_mB8 + 0xC8)), v_stack_m98, local_r11);
    local_rsp = (local_rsp) + (256);
    return result;
loc_003CFB25:
    result = (result) + (v_stack_mC8);
loc_003CFB28:
    local_r13 = 0;
    v_stack_p78 = result;
    goto loc_003CF95C;
loc_003CFB35:
    if ((((uint8_t)(result)) & (8)) == 0) goto loc_003CFBF7;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p90 + 0x8))) | (*(uint32_t *)(v_stack_p90)));
    Arg1 = (uint32_t)(~(Arg1));
    Arg1 = (uint32_t)((Arg1) & (*(uint32_t *)(v_stack_p90 + 0x4)));
    Arg1 = (uint32_t)((Arg1) | (0x10D0000ULL));
loc_003CFB58:
    if (((v_stack_p160) & ((uint32_t)(Arg1))) == 0) goto loc_003CFA3A;
loc_003CFB6A:
    result = SepSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0xC09FBC), Arg17, Arg10, local_r11);
    local_rdi = (uint32_t)((local_rdi) | ((uint32_t)(v_stack_mB8)));
    if ((uint32_t)((uint32_t)((uint32_t)(v_stack_m70 + 40 + 48))) == 0) goto loc_003CFBD5;
loc_003CFB9B:
    if (*(uint64_t *)(v_stack_m70 + 0x28) == 0) goto loc_003CFBCC;
loc_003CFBA9:
    if (1 == 0) goto loc_003CFBCC;
    if (condition_is_below) goto loc_003CFBBA;
loc_003CFBB3:
    Arg2 = (uint32_t)((0) + (1));
    result = (uint32_t)((1) + (1));
    goto loc_003CFBA9;
loc_003CFBBA:
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_m70 + 0x28) + (uint32_t)((uint32_t)(Arg2)) * 4)) != 0) goto loc_003CFBB3;
    *(uint32_t *)(*(uint64_t *)(v_stack_m70 + 0x28) + (uint32_t)((uint32_t)(Arg2)) * 4) = 0x200009ULL;
    goto loc_003CFBB3;
loc_003CFBCC:
    Arg4 = (v_stack_m70 + 40) + (48);
    local_r10 = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m70 + 40 + 48))))) - (1);
    if (condition_is_not_equal) goto loc_003CFB9B;
loc_003CFBD5:
    Arg1 = 0;
    v_stack_p70 = 1;
    if ((uint32_t)(local_rsi) != 0) goto loc_003CF985;
    local_r11 = 0;
    goto loc_003CFABA;
loc_003CFBF7:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p90 + 0xC))) | (0x1FFFFFULL));
    goto loc_003CFB58;
loc_003CFC0D:
    if ((uint32_t)((uint32_t)(v_stack_p74)) == 0) goto loc_003CFACE;
    v_stack_p20 = v_stack_pA8;
    result = SepAssemblePrivileges((uint32_t)((uint32_t)((uint32_t)(v_stack_p74))), v_stack_p72, 1, v_stack_p71);
    local_r13 = 0;
    if (v_stack_pA8 == 0) goto loc_003CFACE;
    if ((*(uint64_t *)(v_stack_pA8)) != 0) goto loc_003CFACE;
loc_003CFC5B:
    result = SepSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0xC09E93), Arg17, Arg10, v_stack_p71);
    local_r13 = 0;
loc_003CFC9A:
    goto loc_003CF932;
loc_003CFCA3:
    goto loc_003CFB28;
loc_003CFCAC:
    *(uint32_t *)((uint32_t)(0xC0000061ULL) + 0xC) = (uint32_t)(v_stack_pA8);
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline((uint32_t)(0x1000000ULL), (uint32_t)(0x100000ULL), 8, v_stack_m70);
    result = (uint32_t)(~((uint32_t)(*(uint32_t *)((uint32_t)(0xC0000061ULL)))));
    local_rdi = (uint32_t)((local_rdi) & ((uint32_t)(result)));
loc_003CFCD1:
    local_r13 = 0;
loc_003CFCDE:
loc_003CFCE8:
    if ((*(uint32_t *)((uint32_t)(0xC0000022ULL) + 0xC)) != 0) goto loc_003CFA9F;
    Arg2 = (uint32_t)(((uint32_t)(0x100000ULL)) & ((uint32_t)((uint32_t)(0x3000000ULL))));
    if (((uint32_t)(Arg2)) != ((uint32_t)((uint32_t)(0x3000000ULL)))) goto loc_003CFA9F;
    *(uint8_t *)((uint32_t)(0xC0000022ULL) + 0x17) = 0;
loc_003CFD0A:
    if (((uint32_t)(Arg2)) < ((uint32_t)((uint32_t)(0x3000000ULL)))) goto loc_003CFA9F;
    local_rsi = (uint32_t)((v_stack_pA8) | (*(uint32_t *)((uint32_t)(0xC0000022ULL))));
    result = (uint32_t)(~((uint32_t)(*(uint32_t *)((uint32_t)(0xC0000022ULL) + 0x4))));
    local_rsi = (uint32_t)((local_rsi) & ((uint32_t)(result)));
    goto loc_003CFA9F;
loc_003CFD2C:
    if (condition_is_below) goto loc_003CFAAB;
    local_rsi = (uint32_t)((local_rsi) | (Arg5));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)(0xC0000022ULL) + 0x8))) | (*(uint32_t *)((uint32_t)(0xC0000022ULL) + 0x4)));
    local_rsi = (uint32_t)((local_rsi) | (*(uint32_t *)((uint32_t)(0xC0000022ULL))));
    Arg1 = (uint32_t)(~(Arg1));
    Arg1 = (uint32_t)((Arg1) & ((uint32_t)(local_rsi)));
    Arg2 = (uint32_t)((Arg2) & ((uint32_t)((uint32_t)(0x3000000ULL))));
    *(uint8_t *)((uint32_t)(0xC0000022ULL) + 0x17) = 0;
loc_003CFD7B:
    goto loc_003CFACE;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x2` | `16` | `R` |
| `Arg1` | `+ 0xC` | `32` | `R` |
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg18` | `+ 0x0` | `32` | `R` |
| `Arg18` | `+ 0x4` | `32` | `R` |
| `Arg18` | `+ 0x8` | `32` | `R` |
| `Arg18` | `+ 0xC` | `32` | `R` |
| `Arg18` | `+ 0xC` | `32` | `W` |
| `Arg18` | `+ 0x14` | `8` | `R` |
| `Arg18` | `+ 0x17` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003CF7B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
