# sub_003E47AF

- RVA: `0x003E47AF`–`0x003E4B89` (길이 `986` bytes)
- VA: `0x00000001403E47AF`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00094DC8`
- 디코드: `261`개 명령, `986/986` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **8**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x003E4807` → [RtlRbInsertNodeEx](../2E/RtlRbInsertNodeEx_function_002E4570.md) (function, `0x002E4570`)
- `0x003E4948` → [RtlLengthCurrentClearRunForward](RtlLengthCurrentClearRunForward_function_003E4B90.md) (function, `0x003E4B90`)
- `0x003E4978` → [RtlLengthCurrentClearRunBackward](RtlLengthCurrentClearRunBackward_function_003E4C78.md) (function, `0x003E4C78`)
- `0x003E49B3` → [MiRescanPageFileBitmapPortion](MiRescanPageFileBitmapPortion_function_003E4D08.md) (function, `0x003E4D08`)
- `0x003E4A25` → [RtlRbRemoveNode](../2E/RtlRbRemoveNode_function_002E4C10.md) (function, `0x002E4C10`)
- `0x003E4A34` → [RtlRbRemoveNode](../2E/RtlRbRemoveNode_function_002E4C10.md) (function, `0x002E4C10`)
- `0x003E4A86` → [RtlLengthCurrentClearRunBackward](RtlLengthCurrentClearRunBackward_function_003E4C78.md) (function, `0x003E4C78`)
- `0x003E4AA1` → [RtlLengthCurrentClearRunBackward](RtlLengthCurrentClearRunBackward_function_003E4C78.md) (function, `0x003E4C78`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x003E4826` → RVA `0x00012C50` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **27**
  - `0x003E47C6` → [sub_003E455D + 0xFF](Unknown_function_003E455D.md) (`tail-transfer`)
  - `0x003E47E0` → [sub_003E455D + 0xFF](Unknown_function_003E455D.md) (`tail-transfer`)
  - `0x003E480C` → [sub_003E455D + 0x228](Unknown_function_003E455D.md) (`tail-transfer`)
  - `0x003E48B6` → [sub_003E455D + 0x116](Unknown_function_003E455D.md) (`tail-transfer`)
  - `0x003E492D` → [sub_003E455D + 0x207](Unknown_function_003E455D.md) (`tail-transfer`)
  - `0x003E4935` → [sub_003E455D + 0x21B](Unknown_function_003E455D.md) (`tail-transfer`)
  - `0x003E4957` → [sub_003E455D + 0x21B](Unknown_function_003E455D.md) (`tail-transfer`)
  - `0x003E4960` → [sub_003E455D + 0x21B](Unknown_function_003E455D.md) (`tail-transfer`)
  - `0x003E4986` → [sub_003E455D + 0x21B](Unknown_function_003E455D.md) (`tail-transfer`)
  - `0x003E4990` → [sub_003E455D + 0x21B](Unknown_function_003E455D.md) (`tail-transfer`)
  - `0x003E49B8` → [sub_003E455D + 0x228](Unknown_function_003E455D.md) (`tail-transfer`)
  - `0x003E49C3` → [sub_003E455D + 0x1CB](Unknown_function_003E455D.md) (`tail-transfer`)
  - `0x003E49D2` → [sub_003E455D + 0x207](Unknown_function_003E455D.md) (`tail-transfer`)
  - `0x003E49E3` → [sub_003E455D + 0x207](Unknown_function_003E455D.md) (`tail-transfer`)
  - `0x003E49EB` → [sub_003E455D + 0x69](Unknown_function_003E455D.md) (`tail-transfer`)
  - `0x003E49F4` → [sub_003E455D + 0x69](Unknown_function_003E455D.md) (`tail-transfer`)
  - `0x003E49FC` → [sub_003E455D + 0xB4](Unknown_function_003E455D.md) (`tail-transfer`)
  - `0x003E4A0D` → [sub_003E455D + 0xB4](Unknown_function_003E455D.md) (`tail-transfer`)
  - `0x003E4A79` → [sub_003E455D + 0x116](Unknown_function_003E455D.md) (`tail-transfer`)
  - `0x003E4A8E` → [sub_003E455D + 0x116](Unknown_function_003E455D.md) (`tail-transfer`)
  - `0x003E4AB3` → [sub_003E455D + 0x116](Unknown_function_003E455D.md) (`tail-transfer`)
  - `0x003E4AC7` → [sub_003E455D + 0x181](Unknown_function_003E455D.md) (`tail-transfer`)
  - `0x003E4ACF` → [sub_003E455D + 0x73](Unknown_function_003E455D.md) (`tail-transfer`)
  - `0x003E4AF9` → [sub_003E455D + 0xFF](Unknown_function_003E455D.md) (`tail-transfer`)
  - `0x003E4B06` → [sub_003E455D + 0x94](Unknown_function_003E455D.md) (`tail-transfer`)
  - `0x003E4B0F` → [sub_003E455D + 0x94](Unknown_function_003E455D.md) (`tail-transfer`)
  - `0x003E4B18` → [sub_003E455D + 0x73](Unknown_function_003E455D.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003E47AF  8B 51 1C                        mov edx, dword ptr [rcx + 0x1c]
003E47B2  4C 8D 41 E8                     lea r8, [rcx - 0x18]
003E47B6  8B 49 18                        mov ecx, dword ptr [rcx + 0x18]
003E47B9  03 CA                           add ecx, edx
003E47BB  4C 89 44 24 30                  mov qword ptr [rsp + 0x30], r8
003E47C0  44 8D 61 FF                     lea r12d, [rcx - 1]
003E47C4  3B CF                           cmp ecx, edi
003E47C6  0F 85 90 FE FF FF               jne 0x1403e465c
003E47CC  41 39 7E 30                     cmp dword ptr [r14 + 0x30], edi
003E47D0  0F 84 3C 02 00 00               je 0x1403e4a12
003E47D6  8D 42 01                        lea eax, [rdx + 1]
003E47D9  49 8B E8                        mov rbp, r8
003E47DC  41 89 40 34                     mov dword ptr [r8 + 0x34], eax
003E47E0  E9 77 FE FF FF                  jmp 0x1403e465c
003E47E5  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
003E47E9  45 85 C0                        test r8d, r8d
003E47EC  0F 84 CE 01 00 00               je 0x1403e49c0
003E47F2  48 85 C0                        test rax, rax
003E47F5  0F 85 C2 01 00 00               jne 0x1403e49bd
003E47FB  B0 01                           mov al, 1
003E47FD  4C 8B CD                        mov r9, rbp
003E4800  44 0F B6 C0                     movzx r8d, al
003E4804  49 8B CD                        mov rcx, r13
003E4807  E8 64 FD EF FF                  call 0x1402e4570
003E480C  E9 74 FF FF FF                  jmp 0x1403e4785
003E4811  8B 45 30                        mov eax, dword ptr [rbp + 0x30]
003E4814  3B C7                           cmp eax, edi
003E4816  0F 84 62 02 00 00               je 0x1403e4a7e
003E481C  49 8B 51 08                     mov rdx, qword ptr [r9 + 8]
003E4820  8D 58 FF                        lea ebx, [rax - 1]
003E4823  45 8B 09                        mov r9d, dword ptr [r9]
003E4826  4C 8D 05 23 E4 C2 FF            lea r8, [rip - 0x3d1bdd]
003E482D  44 8B 65 34                     mov r12d, dword ptr [rbp + 0x34]
003E4831  41 8B F1                        mov esi, r9d
003E4834  41 03 DC                        add ebx, r12d
003E4837  8B C3                           mov eax, ebx
003E4839  48 C1 E8 05                     shr rax, 5
003E483D  41 8D 49 FF                     lea ecx, [r9 - 1]
003E4841  48 C1 E9 05                     shr rcx, 5
003E4845  41 83 E1 1F                     and r9d, 0x1f
003E4849  48 8D 3C 85 00 00 00 00         lea rdi, [rax*4]
003E4851  48 8D 04 8A                     lea rax, [rdx + rcx*4]
003E4855  8B 0C 3A                        mov ecx, dword ptr [rdx + rdi]
003E4858  4C 8D 1C 3A                     lea r11, [rdx + rdi]
003E485C  48 8D 50 FC                     lea rdx, [rax - 4]
003E4860  48 0F 44 D0                     cmove rdx, rax
003E4864  83 E3 1F                        and ebx, 0x1f
003E4867  45 8B 34 98                     mov r14d, dword ptr [r8 + rbx*4]
003E486B  45 8B C7                        mov r8d, r15d
003E486E  41 F7 D6                        not r14d
003E4871  41 23 CE                        and ecx, r14d
003E4874  4C 3B DA                        cmp r11, rdx
003E4877  0F 86 A3 02 00 00               jbe 0x1403e4b20
003E487D  45 85 C9                        test r9d, r9d
003E4880  74 2D                           je 0x1403e48af
003E4882  45 85 C0                        test r8d, r8d
003E4885  74 04                           je 0x1403e488b
003E4887  41 8B 4B 04                     mov ecx, dword ptr [r11 + 4]
003E488B  83 E6 1F                        and esi, 0x1f
003E488E  48 8D 05 BB E3 C2 FF            lea rax, [rip - 0x3d1c45]
003E4895  8B 04 B0                        mov eax, dword ptr [rax + rsi*4]
003E4898  F7 D0                           not eax
003E489A  0B C1                           or eax, ecx
003E489C  48 0F BC C8                     bsf rcx, rax
003E48A0  41 8B D2                        mov edx, r10d
003E48A3  0F B6 C1                        movzx eax, cl
003E48A6  0F 45 D0                        cmovne edx, eax
003E48A9  0F BE C2                        movsx eax, dl
003E48AC  44 03 C0                        add r8d, eax
003E48AF  44 2B C3                        sub r8d, ebx
003E48B2  41 83 F8 01                     cmp r8d, 1
003E48B6  0F 86 B7 FD FF FF               jbe 0x1403e4673
003E48BC  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
003E48C4  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
003E48C8  4C 8D 0C 17                     lea r9, [rdi + rdx]
003E48CC  8B 38                           mov edi, dword ptr [rax]
003E48CE  8B F7                           mov esi, edi
003E48D0  8D 4F FF                        lea ecx, [rdi - 1]
003E48D3  48 C1 E9 05                     shr rcx, 5
003E48D7  83 E7 1F                        and edi, 0x1f
003E48DA  48 8D 04 8A                     lea rax, [rdx + rcx*4]
003E48DE  41 8B 09                        mov ecx, dword ptr [r9]
003E48E1  4C 8D 58 FC                     lea r11, [rax - 4]
003E48E5  41 8B D7                        mov edx, r15d
003E48E8  4C 0F 44 D8                     cmove r11, rax
003E48EC  41 23 CE                        and ecx, r14d
003E48EF  4D 3B CB                        cmp r9, r11
003E48F2  0F 86 5F 02 00 00               jbe 0x1403e4b57
003E48F8  85 FF                           test edi, edi
003E48FA  0F 84 67 01 00 00               je 0x1403e4a67
003E4900  85 D2                           test edx, edx
003E4902  74 04                           je 0x1403e4908
003E4904  41 8B 49 04                     mov ecx, dword ptr [r9 + 4]
003E4908  83 E6 1F                        and esi, 0x1f
003E490B  48 8D 05 3E E3 C2 FF            lea rax, [rip - 0x3d1cc2]
003E4912  8B 04 B0                        mov eax, dword ptr [rax + rsi*4]
003E4915  F7 D0                           not eax
003E4917  0B C1                           or eax, ecx
003E4919  E9 38 01 00 00                  jmp 0x1403e4a56
003E491E  49 8B 45 78                     mov rax, qword ptr [r13 + 0x78]
003E4922  A8 01                           test al, 1
003E4924  0F 85 A4 00 00 00               jne 0x1403e49ce
003E492A  4C 8B F8                        mov r15, rax
003E492D  E9 32 FE FF FF                  jmp 0x1403e4764
003E4932  83 F9 20                        cmp ecx, 0x20
003E4935  0F 82 3D FE FF FF               jb 0x1403e4778
003E493B  85 F6                           test esi, esi
003E493D  74 27                           je 0x1403e4966
003E493F  44 8D 46 01                     lea r8d, [rsi + 1]
003E4943  8B D7                           mov edx, edi
003E4945  49 8B C9                        mov rcx, r9
003E4948  E8 43 02 00 00                  call 0x1403e4b90
003E494D  8D 0C 03                        lea ecx, [rbx + rax]
003E4950  8D 70 FF                        lea esi, [rax - 1]
003E4953  41 39 4F 34                     cmp dword ptr [r15 + 0x34], ecx
003E4957  0F 83 1B FE FF FF               jae 0x1403e4778
003E495D  83 F9 20                        cmp ecx, 0x20
003E4960  0F 82 12 FE FF FF               jb 0x1403e4778
003E4966  85 DB                           test ebx, ebx
003E4968  74 2C                           je 0x1403e4996
003E496A  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
003E4972  44 8D 43 01                     lea r8d, [rbx + 1]
003E4976  8B D7                           mov edx, edi
003E4978  E8 FB 02 00 00                  call 0x1403e4c78
003E497D  8D 0C 30                        lea ecx, [rax + rsi]
003E4980  8D 58 FF                        lea ebx, [rax - 1]
003E4983  83 F9 20                        cmp ecx, 0x20
003E4986  0F 82 EC FD FF FF               jb 0x1403e4778
003E498C  41 39 4F 34                     cmp dword ptr [r15 + 0x34], ecx
003E4990  0F 83 E2 FD FF FF               jae 0x1403e4778
003E4996  48 8B 94 24 98 00 00 00         mov rdx, qword ptr [rsp + 0x98]
003E499E  48 8D 44 24 30                  lea rax, [rsp + 0x30]
003E49A3  2B FB                           sub edi, ebx
003E49A5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
003E49AA  44 8B C9                        mov r9d, ecx
003E49AD  44 8B C7                        mov r8d, edi
003E49B0  49 8B CD                        mov rcx, r13
003E49B3  E8 50 03 00 00                  call 0x1403e4d08
003E49B8  E9 C8 FD FF FF                  jmp 0x1403e4785
003E49BD  48 33 C2                        xor rax, rdx
003E49C0  48 85 C0                        test rax, rax
003E49C3  0F 85 5F FD FF FF               jne 0x1403e4728
003E49C9  E9 2D FE FF FF                  jmp 0x1403e47fb
003E49CE  48 83 F8 01                     cmp rax, 1
003E49D2  0F 84 8C FD FF FF               je 0x1403e4764
003E49D8  4D 8D 7D 70                     lea r15, [r13 + 0x70]
003E49DC  49 83 CF 01                     or r15, 1
003E49E0  4C 33 F8                        xor r15, rax
003E49E3  E9 7C FD FF FF                  jmp 0x1403e4764
003E49E8  48 85 DB                        test rbx, rbx
003E49EB  0F 84 D5 FB FF FF               je 0x1403e45c6
003E49F1  48 33 D9                        xor rbx, rcx
003E49F4  E9 CD FB FF FF                  jmp 0x1403e45c6
003E49F9  41 3B F2                        cmp esi, r10d
003E49FC  0F 84 0F FC FF FF               je 0x1403e4611
003E4A02  41 FF 46 34                     inc dword ptr [r14 + 0x34]
003E4A06  49 8B EE                        mov rbp, r14
003E4A09  41 89 7E 30                     mov dword ptr [r14 + 0x30], edi
003E4A0D  E9 FF FB FF FF                  jmp 0x1403e4611
003E4A12  41 03 56 34                     add edx, dword ptr [r14 + 0x34]
003E4A16  49 8D 4D 70                     lea rcx, [r13 + 0x70]
003E4A1A  41 89 50 34                     mov dword ptr [r8 + 0x34], edx
003E4A1E  49 8B D6                        mov rdx, r14
003E4A21  45 89 7E 34                     mov dword ptr [r14 + 0x34], r15d
003E4A25  E8 E6 01 F0 FF                  call 0x1402e4c10
003E4A2A  48 8B D3                        mov rdx, rbx
003E4A2D  49 8D 8D 80 00 00 00            lea rcx, [r13 + 0x80]
003E4A34  E8 D7 01 F0 FF                  call 0x1402e4c10
003E4A39  49 8D 85 90 00 00 00            lea rax, [r13 + 0x90]
003E4A40  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
003E4A44  48 39 01                        cmp qword ptr [rcx], rax
003E4A47  0F 84 87 00 00 00               je 0x1403e4ad4
003E4A4D  B9 03 00 00 00                  mov ecx, 3
003E4A52  CD 29                           int 0x29
003E4A54  8B C1                           mov eax, ecx
003E4A56  48 0F BC C8                     bsf rcx, rax
003E4A5A  0F B6 C1                        movzx eax, cl
003E4A5D  44 0F 45 D0                     cmovne r10d, eax
003E4A61  41 0F BE C2                     movsx eax, r10b
003E4A65  03 D0                           add edx, eax
003E4A67  2B D3                           sub edx, ebx
003E4A69  41 3B D0                        cmp edx, r8d
003E4A6C  41 0F 47 D0                     cmova edx, r8d
003E4A70  8D 42 FF                        lea eax, [rdx - 1]
003E4A73  41 03 C4                        add eax, r12d
003E4A76  89 45 34                        mov dword ptr [rbp + 0x34], eax
003E4A79  E9 F5 FB FF FF                  jmp 0x1403e4673
003E4A7E  45 8B C2                        mov r8d, r10d
003E4A81  8B D7                           mov edx, edi
003E4A83  49 8B C9                        mov rcx, r9
003E4A86  E8 ED 01 00 00                  call 0x1403e4c78
003E4A8B  83 F8 01                        cmp eax, 1
003E4A8E  0F 86 DF FB FF FF               jbe 0x1403e4673
003E4A94  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
003E4A9C  44 8B C0                        mov r8d, eax
003E4A9F  8B D7                           mov edx, edi
003E4AA1  E8 D2 01 00 00                  call 0x1403e4c78
003E4AA6  2B F8                           sub edi, eax
003E4AA8  8D 48 FF                        lea ecx, [rax - 1]
003E4AAB  01 4D 34                        add dword ptr [rbp + 0x34], ecx
003E4AAE  FF C7                           inc edi
003E4AB0  89 7D 30                        mov dword ptr [rbp + 0x30], edi
003E4AB3  E9 BB FB FF FF                  jmp 0x1403e4673
003E4AB8  48 85 D2                        test rdx, rdx
003E4ABB  75 07                           jne 0x1403e4ac4
003E4ABD  32 C0                           xor al, al
003E4ABF  E9 39 FD FF FF                  jmp 0x1403e47fd
003E4AC4  49 33 D5                        xor rdx, r13
003E4AC7  E9 12 FC FF FF                  jmp 0x1403e46de
003E4ACC  48 33 D8                        xor rbx, rax
003E4ACF  E9 FC FA FF FF                  jmp 0x1403e45d0
003E4AD4  48 8B 6C 24 30                  mov rbp, qword ptr [rsp + 0x30]
003E4AD9  41 BA FF FF FF FF               mov r10d, 0xffffffff
003E4ADF  4C 8B 8C 24 80 00 00 00         mov r9, qword ptr [rsp + 0x80]
003E4AE7  48 83 CD 01                     or rbp, 1
003E4AEB  49 89 06                        mov qword ptr [r14], rax
003E4AEE  49 89 4E 08                     mov qword ptr [r14 + 8], rcx
003E4AF2  4C 89 31                        mov qword ptr [rcx], r14
003E4AF5  4C 89 70 08                     mov qword ptr [rax + 8], r14
003E4AF9  E9 5E FB FF FF                  jmp 0x1403e465c
003E4AFE  48 8B 03                        mov rax, qword ptr [rbx]
003E4B01  48 8B D3                        mov rdx, rbx
003E4B04  85 C9                           test ecx, ecx
003E4B06  0F 84 E5 FA FF FF               je 0x1403e45f1
003E4B0C  48 85 C0                        test rax, rax
003E4B0F  0F 84 DC FA FF FF               je 0x1403e45f1
003E4B15  48 33 D8                        xor rbx, rax
003E4B18  E9 B3 FA FF FF                  jmp 0x1403e45d0
003E4B1D  0F 1F 00                        nop dword ptr [rax]
003E4B20  85 C9                           test ecx, ecx
003E4B22  75 1C                           jne 0x1403e4b40
003E4B24  41 83 C0 20                     add r8d, 0x20
003E4B28  45 3B C2                        cmp r8d, r10d
003E4B2B  73 1A                           jae 0x1403e4b47
003E4B2D  4C 3B DA                        cmp r11, rdx
003E4B30  0F 84 47 FD FF FF               je 0x1403e487d
003E4B36  41 8B 4B 04                     mov ecx, dword ptr [r11 + 4]
003E4B3A  49 83 C3 04                     add r11, 4
003E4B3E  EB E0                           jmp 0x1403e4b20
003E4B40  8B C1                           mov eax, ecx
003E4B42  E9 55 FD FF FF                  jmp 0x1403e489c
003E4B47  41 8B C0                        mov eax, r8d
003E4B4A  2B C3                           sub eax, ebx
003E4B4C  41 3B C2                        cmp eax, r10d
003E4B4F  0F 83 5A FD FF FF               jae 0x1403e48af
003E4B55  EB D6                           jmp 0x1403e4b2d
003E4B57  85 C9                           test ecx, ecx
003E4B59  0F 85 F5 FE FF FF               jne 0x1403e4a54
003E4B5F  83 C2 20                        add edx, 0x20
003E4B62  41 3B D0                        cmp edx, r8d
003E4B65  73 13                           jae 0x1403e4b7a
003E4B67  4D 3B CB                        cmp r9, r11
003E4B6A  0F 84 88 FD FF FF               je 0x1403e48f8
003E4B70  41 8B 49 04                     mov ecx, dword ptr [r9 + 4]
003E4B74  49 83 C1 04                     add r9, 4
003E4B78  EB DD                           jmp 0x1403e4b57
003E4B7A  8B C2                           mov eax, edx
003E4B7C  2B C3                           sub eax, ebx
003E4B7E  41 3B C0                        cmp eax, r8d
003E4B81  0F 83 E0 FE FF FF               jae 0x1403e4a67
003E4B87  EB DE                           jmp 0x1403e4b67
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_003E47AF(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rbp;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p80;
    unsigned __int64 v_stack_p98;

    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 24))) + ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 28)))));
    v_stack_p30 = a1 - 24;
    if ((*(unsigned int *)(v_r14 + 48)) == ((unsigned int)(v_rdi))) goto loc_003E4A12;
    *(unsigned int *)(a1 - 24 + 52) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 28)) + 1);
loc_003E4A12:
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 28))) + (*(unsigned int *)(v_r14 + 52)));
    *(unsigned int *)(a1 - 24 + 52) = (unsigned int)(a2);
    *(unsigned int *)(v_r14 + 52) = (unsigned int)(v_r15);
    result = RtlRbRemoveNode(v_r13 + 112, v_r14, a1 - 24, a4);
    result = RtlRbRemoveNode(v_r13 + 128, v_rbx, a1 - 24, a4);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_r13 + 144 + 8))) == (v_r13 + 144)) goto loc_003E4AD4;
loc_003E4A54:
loc_003E4A56:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_r13 + 144 + 8))) != (v_r13 + 144)) { v_r10 = 3; }
    a2 = (unsigned int)((v_rbx) + ((unsigned int)((__int8)((unsigned __int8)(v_r10)))));
loc_003E4A67:
    a2 = (unsigned int)((a2) - ((unsigned int)(v_rbx)));
    if (((unsigned int)(a2)) > ((unsigned int)(a1 - 24))) { a2 = (unsigned int)(a1 - 24); }
    result = (unsigned int)((a2 - 1) + ((unsigned int)(a1 - 1)));
    *(unsigned int *)(a1 - 24 + 52) = (unsigned int)(result);
loc_003E4AD4:
    v_rbp = (a6) | (1);
    *(unsigned __int64 *)(v_r14) = result;
    *(unsigned __int64 *)(v_r14 + 8) = 3;
    *(unsigned __int64 *)(3) = v_r14;
    *(unsigned __int64 *)(result + 8) = v_r14;
}
```

## 5. (Beta) C Style

```c
int64_t sub_003E47AF(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, int64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint64_t Arg13, uint64_t Arg14, uint64_t Arg15, int64_t Arg16)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_rbp;
    uint64_t v_stack_p20;
    uint64_t v_stack_p30;
    uint64_t v_stack_p80;
    uint64_t v_stack_p98;

    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x18))) + ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1C)))));
    v_stack_p30 = Arg1 - 24;
    if ((*(uint32_t *)(local_r14 + 0x30)) == ((uint32_t)(local_rdi))) goto loc_003E4A12;
    *(uint32_t *)(arg1 - 0x18 + 0x34) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1C)) + 1);
loc_003E4A12:
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x1C))) + (*(uint32_t *)(local_r14 + 0x34)));
    *(uint32_t *)(arg1 - 0x18 + 0x34) = (uint32_t)(Arg2);
    *(uint32_t *)(local_r14 + 0x34) = (uint32_t)(local_r15);
    result = RtlRbRemoveNode(local_r13 + 112, local_r14, Arg1 - 24, Arg4);
    result = RtlRbRemoveNode(local_r13 + 128, local_rbx, Arg1 - 24, Arg4);
    if ((*(uint64_t *)(*(uint64_t *)(local_r13 + 0x90 + 0x8))) == (local_r13 + 144)) goto loc_003E4AD4;
loc_003E4A54:
loc_003E4A56:
    if ((*(uint64_t *)(*(uint64_t *)(local_r13 + 0x90 + 0x8))) != (local_r13 + 144)) { local_r10 = 3; }
    Arg2 = (uint32_t)((local_rbx) + ((uint32_t)((int8_t)((uint8_t)(local_r10)))));
loc_003E4A67:
    Arg2 = (uint32_t)((Arg2) - ((uint32_t)(local_rbx)));
    if (((uint32_t)(Arg2)) > ((uint32_t)(Arg1 - 24))) { Arg2 = (uint32_t)(Arg1 - 24); }
    result = (uint32_t)((Arg2 - 1) + ((uint32_t)(Arg1 - 1)));
    *(uint32_t *)(arg1 - 0x18 + 0x34) = (uint32_t)(result);
loc_003E4AD4:
    local_rbp = (Arg6) | (1);
    *(uint64_t *)(local_r14) = result;
    *(uint64_t *)(local_r14 + 0x8) = 3;
    *(uint64_t *)(3) = local_r14;
    *(uint64_t *)(result + 0x8) = local_r14;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `- 0x18` | `64` | `R` |
| `Arg1` | `+ 0x18` | `32` | `R` |
| `Arg1` | `+ 0x1C` | `32` | `R` |
| `Arg1` | `+ 0x34` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003E47AF&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
