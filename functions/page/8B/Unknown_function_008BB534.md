# sub_008BB534

- RVA: `0x008BB534`–`0x008BB987` (길이 `1,107` bytes)
- VA: `0x00000001408BB534`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00082E50`
- 디코드: `270`개 명령, `1,107/1,107` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008BB657` → [SeCaptureSubjectContext](../86/SeCaptureSubjectContext_function_0086B820.md) (function, `0x0086B820`)
- `0x008BB860` → [RtlpNormalizeAcl](RtlpNormalizeAcl_function_008BC950.md) (function, `0x008BC950`)
- `0x008BB87D` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008BB8AF` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008BB93D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x008BB87D` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008BB8AF` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008BB93D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **37**
  - `0x008BB60F` → [sub_008BBBEF](Unknown_function_008BBBEF.md) (`tail-transfer`)
  - `0x008BB639` → [sub_008BC3C4 + 0x57](Unknown_function_008BC3C4.md) (`tail-transfer`)
  - `0x008BB644` → [sub_008BC3C4 + 0x4F](Unknown_function_008BC3C4.md) (`tail-transfer`)
  - `0x008BB67D` → [sub_008BC3C4 + 0x2EF](Unknown_function_008BC3C4.md) (`tail-transfer`)
  - `0x008BB68E` → [sub_008BC3C4 + 0x2F7](Unknown_function_008BC3C4.md) (`tail-transfer`)
  - `0x008BB6B2` → [sub_00B1A906](../B1/Unknown_function_00B1A906.md) (`tail-transfer`)
  - `0x008BB6BC` → [sub_008BC25B + 0x8C](Unknown_function_008BC25B.md) (`tail-transfer`)
  - `0x008BB6C7` → [sub_008BC25B + 0xDF](Unknown_function_008BC25B.md) (`tail-transfer`)
  - `0x008BB6D7` → [sub_008BC25B + 0xDF](Unknown_function_008BC25B.md) (`tail-transfer`)
  - `0x008BB6EA` → [sub_008BC25B + 0xDF](Unknown_function_008BC25B.md) (`tail-transfer`)
  - `0x008BB6F8` → [sub_008BC25B + 0xDF](Unknown_function_008BC25B.md) (`tail-transfer`)
  - `0x008BB703` → [sub_008BC25B + 0xDF](Unknown_function_008BC25B.md) (`tail-transfer`)
  - `0x008BB70D` → [sub_008BC3C4](Unknown_function_008BC3C4.md) (`tail-transfer`)
  - `0x008BB71B` → [sub_008BC25B + 0x8](Unknown_function_008BC25B.md) (`tail-transfer`)
  - `0x008BB726` → [sub_008BC25B + 0xE9](Unknown_function_008BC25B.md) (`tail-transfer`)
  - `0x008BB737` → [sub_008BC25B + 0xE9](Unknown_function_008BC25B.md) (`tail-transfer`)
  - `0x008BB740` → [sub_008BC25B + 0xE9](Unknown_function_008BC25B.md) (`tail-transfer`)
  - `0x008BB74D` → [sub_008BC25B + 0xE9](Unknown_function_008BC25B.md) (`tail-transfer`)
  - `0x008BB757` → [sub_008BC25B + 0xE9](Unknown_function_008BC25B.md) (`tail-transfer`)
  - `0x008BB764` → [sub_008BBC01 + 0x95](Unknown_function_008BBC01.md) (`tail-transfer`)
  - `0x008BB783` → [sub_008BBC01 + 0xE](Unknown_function_008BBC01.md) (`tail-transfer`)
  - `0x008BB79C` → [sub_008BC3C4 + 0x3E1](Unknown_function_008BC3C4.md) (`tail-transfer`)
  - `0x008BB7A5` → [sub_008BBC01 + 0x3D](Unknown_function_008BBC01.md) (`tail-transfer`)
  - `0x008BB7AE` → [sub_008BBC01 + 0x4A](Unknown_function_008BBC01.md) (`tail-transfer`)
  - `0x008BB7EF` → [sub_008BC3C4 + 0x22B](Unknown_function_008BC3C4.md) (`tail-transfer`)
  - `0x008BB7F9` → [sub_008BC3C4 + 0x22B](Unknown_function_008BC3C4.md) (`tail-transfer`)
  - `0x008BB818` → [sub_008BB9AC + 0xF5](Unknown_function_008BB9AC.md) (`tail-transfer`)
  - `0x008BB835` → [sub_008BC3C4 + 0x44E](Unknown_function_008BC3C4.md) (`tail-transfer`)
  - `0x008BB83F` → [sub_008BBC01 + 0x2E6](Unknown_function_008BBC01.md) (`tail-transfer`)
  - `0x008BB8E1` → [sub_008BC3C4 + 0x479](Unknown_function_008BC3C4.md) (`tail-transfer`)
  - `0x008BB8FE` → [sub_008BBC01 + 0x608](Unknown_function_008BBC01.md) (`tail-transfer`)
  - `0x008BB907` → [sub_008BBC01 + 0x5B3](Unknown_function_008BBC01.md) (`tail-transfer`)
  - `0x008BB910` → [sub_008BBC01 + 0x3A4](Unknown_function_008BBC01.md) (`tail-transfer`)
  - `0x008BB919` → [sub_008BBC01 + 0x38A](Unknown_function_008BBC01.md) (`tail-transfer`)
  - `0x008BB922` → [sub_008BBC01 + 0x370](Unknown_function_008BBC01.md) (`tail-transfer`)
  - `0x008BB947` → [sub_008BC3C4 + 0x489](Unknown_function_008BC3C4.md) (`tail-transfer`)
  - `0x008BB985` → [sub_008BB987 + 0x9](Unknown_function_008BB987.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008BB534  49 89 73 08                     mov qword ptr [r11 + 8], rsi
008BB538  49 89 7B E8                     mov qword ptr [r11 - 0x18], rdi
008BB53C  49 8B F9                        mov rdi, r9
008BB53F  4D 89 63 E0                     mov qword ptr [r11 - 0x20], r12
008BB543  4D 89 6B D8                     mov qword ptr [r11 - 0x28], r13
008BB547  4D 8B E8                        mov r13, r8
008BB54A  89 45 38                        mov dword ptr [rbp + 0x38], eax
008BB54D  32 C0                           xor al, al
008BB54F  88 44 24 50                     mov byte ptr [rsp + 0x50], al
008BB553  88 44 24 58                     mov byte ptr [rsp + 0x58], al
008BB557  88 44 24 59                     mov byte ptr [rsp + 0x59], al
008BB55B  88 44 24 6D                     mov byte ptr [rsp + 0x6d], al
008BB55F  88 44 24 68                     mov byte ptr [rsp + 0x68], al
008BB563  88 44 24 69                     mov byte ptr [rsp + 0x69], al
008BB567  88 44 24 6A                     mov byte ptr [rsp + 0x6a], al
008BB56B  88 44 24 6B                     mov byte ptr [rsp + 0x6b], al
008BB56F  88 44 24 6C                     mov byte ptr [rsp + 0x6c], al
008BB573  4D 89 73 D0                     mov qword ptr [r11 - 0x30], r14
008BB577  44 8B F2                        mov r14d, edx
008BB57A  48 8B 95 28 01 00 00            mov rdx, qword ptr [rbp + 0x128]
008BB581  45 32 DB                        xor r11b, r11b
008BB584  4C 89 45 E0                     mov qword ptr [rbp - 0x20], r8
008BB588  45 33 C0                        xor r8d, r8d
008BB58B  41 8B C0                        mov eax, r8d
008BB58E  4C 89 4D B8                     mov qword ptr [rbp - 0x48], r9
008BB592  48 89 45 F8                     mov qword ptr [rbp - 8], rax
008BB596  45 8B E0                        mov r12d, r8d
008BB599  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
008BB59D  48 89 45 68                     mov qword ptr [rbp + 0x68], rax
008BB5A1  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
008BB5A5  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
008BB5A9  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
008BB5AD  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
008BB5B1  48 89 45 08                     mov qword ptr [rbp + 8], rax
008BB5B5  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
008BB5B9  48 89 45 18                     mov qword ptr [rbp + 0x18], rax
008BB5BD  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
008BB5C1  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
008BB5C5  88 45 F0                        mov byte ptr [rbp - 0x10], al
008BB5C8  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
008BB5CC  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
008BB5D0  41 0F B7 45 02                  movzx eax, word ptr [r13 + 2]
008BB5D5  48 89 5D C0                     mov qword ptr [rbp - 0x40], rbx
008BB5D9  48 89 55 D8                     mov qword ptr [rbp - 0x28], rdx
008BB5DD  C6 44 24 67 00                  mov byte ptr [rsp + 0x67], 0
008BB5E2  C6 44 24 66 00                  mov byte ptr [rsp + 0x66], 0
008BB5E7  44 89 44 24 70                  mov dword ptr [rsp + 0x70], r8d
008BB5EC  4C 89 45 D0                     mov qword ptr [rbp - 0x30], r8
008BB5F0  4C 89 45 28                     mov qword ptr [rbp + 0x28], r8
008BB5F4  44 89 5D C8                     mov dword ptr [rbp - 0x38], r11d
008BB5F8  44 89 44 24 60                  mov dword ptr [rsp + 0x60], r8d
008BB5FD  C7 44 24 54 00 80 00 00         mov dword ptr [rsp + 0x54], 0x8000
008BB605  0F 11 45 48                     movups xmmword ptr [rbp + 0x48], xmm0
008BB609  0F 11 45 58                     movups xmmword ptr [rbp + 0x58], xmm0
008BB60D  A8 10                           test al, 0x10
008BB60F  0F 85 DA 05 00 00               jne 0x1408bbbef
008BB615  41 8B F0                        mov esi, r8d
008BB618  49 8B 01                        mov rax, qword ptr [r9]
008BB61B  48 89 74 24 78                  mov qword ptr [rsp + 0x78], rsi
008BB620  4C 89 BC 24 B0 01 00 00         mov qword ptr [rsp + 0x1b0], r15
008BB628  0F B7 48 02                     movzx ecx, word ptr [rax + 2]
008BB62C  F6 C1 10                        test cl, 0x10
008BB62F  75 05                           jne 0x1408bb636
008BB631  4D 8B F8                        mov r15, r8
008BB634  EB 18                           jmp 0x1408bb64e
008BB636  66 85 C9                        test cx, cx
008BB639  0F 89 DC 0D 00 00               jns 0x1408bc41b
008BB63F  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
008BB642  85 C9                           test ecx, ecx
008BB644  0F 84 C9 0D 00 00               je 0x1408bc413
008BB64A  4C 8D 3C 08                     lea r15, [rax + rcx]
008BB64E  48 85 D2                        test rdx, rdx
008BB651  75 15                           jne 0x1408bb668
008BB653  48 8D 4D 48                     lea rcx, [rbp + 0x48]
008BB657  E8 C4 01 FB FF                  call 0x14086b820
008BB65C  44 8B 5D C8                     mov r11d, dword ptr [rbp - 0x38]
008BB660  48 8D 45 48                     lea rax, [rbp + 0x48]
008BB664  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
008BB668  48 8B 0F                        mov rcx, qword ptr [rdi]
008BB66B  66 44 39 61 02                  cmp word ptr [rcx + 2], r12w
008BB670  0F 8D 3D 01 00 00               jge 0x1408bb7b3
008BB676  41 0F B7 55 02                  movzx edx, word ptr [r13 + 2]
008BB67B  84 D2                           test dl, dl
008BB67D  0F 88 30 10 00 00               js 0x1408bc6b3
008BB683  45 32 D2                        xor r10b, r10b
008BB686  44 88 54 24 64                  mov byte ptr [rsp + 0x64], r10b
008BB68B  F6 C2 40                        test dl, 0x40
008BB68E  0F 85 27 10 00 00               jne 0x1408bc6bb
008BB694  44 88 64 24 65                  mov byte ptr [rsp + 0x65], r12b
008BB699  45 8B C6                        mov r8d, r14d
008BB69C  45 8B CE                        mov r9d, r14d
008BB69F  41 81 E0 80 00 00 00            and r8d, 0x80
008BB6A6  41 81 E1 00 01 00 00            and r9d, 0x100
008BB6AD  41 0F BA E6 10                  bt r14d, 0x10
008BB6B2  0F 82 4E F2 25 00               jb 0x140b1a906
008BB6B8  41 F6 C6 01                     test r14b, 1
008BB6BC  0F 85 25 0C 00 00               jne 0x1408bc2e7
008BB6C2  8B 41 04                        mov eax, dword ptr [rcx + 4]
008BB6C5  85 C0                           test eax, eax
008BB6C7  0F 84 6D 0C 00 00               je 0x1408bc33a
008BB6CD  44 8B D0                        mov r10d, eax
008BB6D0  4C 03 D1                        add r10, rcx
008BB6D3  4C 89 55 88                     mov qword ptr [rbp - 0x78], r10
008BB6D7  0F 84 5D 0C 00 00               je 0x1408bc33a
008BB6DD  48 BA 00 00 FF FF FF 7F 00 00   movabs rdx, 0x7fffffff0000
008BB6E7  4C 3B D2                        cmp r10, rdx
008BB6EA  0F 86 4A 0C 00 00               jbe 0x1408bc33a
008BB6F0  41 0F B6 02                     movzx eax, byte ptr [r10]
008BB6F4  24 0F                           and al, 0xf
008BB6F6  3C 01                           cmp al, 1
008BB6F8  0F 85 3C 0C 00 00               jne 0x1408bc33a
008BB6FE  41 80 7A 01 0F                  cmp byte ptr [r10 + 1], 0xf
008BB703  0F 87 31 0C 00 00               ja 0x1408bc33a
008BB709  41 F6 C6 02                     test r14b, 2
008BB70D  0F 85 B1 0C 00 00               jne 0x1408bc3c4
008BB713  48 8B 07                        mov rax, qword ptr [rdi]
008BB716  66 44 39 60 02                  cmp word ptr [rax + 2], r12w
008BB71B  0F 8D 42 0B 00 00               jge 0x1408bc263
008BB721  8B 48 08                        mov ecx, dword ptr [rax + 8]
008BB724  85 C9                           test ecx, ecx
008BB726  0F 84 18 0C 00 00               je 0x1408bc344
008BB72C  48 8D 3C 08                     lea rdi, [rax + rcx]
008BB730  48 89 7D 80                     mov qword ptr [rbp - 0x80], rdi
008BB734  48 85 FF                        test rdi, rdi
008BB737  0F 84 07 0C 00 00               je 0x1408bc344
008BB73D  48 3B FA                        cmp rdi, rdx
008BB740  0F 86 FE 0B 00 00               jbe 0x1408bc344
008BB746  0F B6 07                        movzx eax, byte ptr [rdi]
008BB749  24 0F                           and al, 0xf
008BB74B  3C 01                           cmp al, 1
008BB74D  0F 85 F1 0B 00 00               jne 0x1408bc344
008BB753  80 7F 01 0F                     cmp byte ptr [rdi + 1], 0xf
008BB757  0F 87 E7 0B 00 00               ja 0x1408bc344
008BB75D  41 F7 C6 F8 01 00 00            test r14d, 0x1f8
008BB764  0F 85 2C 05 00 00               jne 0x1408bbc96
008BB76A  4C 8B 65 A0                     mov r12, qword ptr [rbp - 0x60]
008BB76E  49 8B F7                        mov rsi, r15
008BB771  4C 89 7D D0                     mov qword ptr [rbp - 0x30], r15
008BB775  4C 8B 7D 98                     mov r15, qword ptr [rbp - 0x68]
008BB779  41 BB 0C 14 00 00               mov r11d, 0x140c
008BB77F  41 F6 C6 04                     test r14b, 4
008BB783  0F 84 86 04 00 00               je 0x1408bbc0f
008BB789  41 0F B7 4D 02                  movzx ecx, word ptr [r13 + 2]
008BB78E  0F B7 C1                        movzx eax, cx
008BB791  66 83 E0 04                     and ax, 4
008BB795  F6 85 10 01 00 00 01            test byte ptr [rbp + 0x110], 1
008BB79C  0F 85 03 10 00 00               jne 0x1408bc7a5
008BB7A2  66 85 C0                        test ax, ax
008BB7A5  0F 85 93 04 00 00               jne 0x1408bbc3e
008BB7AB  45 33 E4                        xor r12d, r12d
008BB7AE  E9 98 04 00 00                  jmp 0x1408bbc4b
008BB7B3  BB E7 00 00 C0                  mov ebx, 0xc00000e7
008BB7B8  E9 90 01 00 00                  jmp 0x1408bb94d
008BB7BD  8B 51 04                        mov edx, dword ptr [rcx + 4]
008BB7C0  85 D2                           test edx, edx
008BB7C2  79 02                           jns 0x1408bb7c6
008BB7C4  0B 16                           or edx, dword ptr [rsi]
008BB7C6  0F BA E2 1E                     bt edx, 0x1e
008BB7CA  73 03                           jae 0x1408bb7cf
008BB7CC  0B 56 04                        or edx, dword ptr [rsi + 4]
008BB7CF  0F BA E2 1D                     bt edx, 0x1d
008BB7D3  73 03                           jae 0x1408bb7d8
008BB7D5  0B 56 08                        or edx, dword ptr [rsi + 8]
008BB7D8  0F BA E2 1C                     bt edx, 0x1c
008BB7DC  73 03                           jae 0x1408bb7e1
008BB7DE  0B 56 0C                        or edx, dword ptr [rsi + 0xc]
008BB7E1  81 E2 FF FF FF 0F               and edx, 0xfffffff
008BB7E7  89 51 04                        mov dword ptr [rcx + 4], edx
008BB7EA  0F B6 01                        movzx eax, byte ptr [rcx]
008BB7ED  3C 0A                           cmp al, 0xa
008BB7EF  0F 87 FA 0D 00 00               ja 0x1408bc5ef
008BB7F5  41 0F A3 C1                     bt r9d, eax
008BB7F9  0F 83 F0 0D 00 00               jae 0x1408bc5ef
008BB7FF  8B 46 0C                        mov eax, dword ptr [rsi + 0xc]
008BB802  23 C2                           and eax, edx
008BB804  89 41 04                        mov dword ptr [rcx + 4], eax
008BB807  0F B7 41 02                     movzx eax, word ptr [rcx + 2]
008BB80B  41 FF C0                        inc r8d
008BB80E  48 03 C8                        add rcx, rax
008BB811  0F B7 43 04                     movzx eax, word ptr [rbx + 4]
008BB815  44 3B C0                        cmp r8d, eax
008BB818  0F 82 83 02 00 00               jb 0x1408bbaa1
008BB81E  48 8B 75 E8                     mov rsi, qword ptr [rbp - 0x18]
008BB822  8B C3                           mov eax, ebx
008BB824  48 8D 7E 10                     lea rdi, [rsi + 0x10]
008BB828  2B C6                           sub eax, esi
008BB82A  89 07                           mov dword ptr [rdi], eax
008BB82C  41 0F B7 4C 24 02               movzx ecx, word ptr [r12 + 2]
008BB832  44 3B F9                        cmp r15d, ecx
008BB835  0F 87 D7 0F 00 00               ja 0x1408bc812
008BB83B  41 F6 C6 04                     test r14b, 4
008BB83F  0F 84 A2 06 00 00               je 0x1408bbee7
008BB845  83 7E 10 00                     cmp dword ptr [rsi + 0x10], 0
008BB849  74 1F                           je 0x1408bb86a
008BB84B  F7 85 10 01 00 00 00 40 00 00   test dword ptr [rbp + 0x110], 0x4000
008BB855  74 13                           je 0x1408bb86a
008BB857  45 33 C0                        xor r8d, r8d
008BB85A  48 8B D3                        mov rdx, rbx
008BB85D  48 8B CB                        mov rcx, rbx
008BB860  E8 EB 10 00 00                  call 0x1408bc950
008BB865  44 0F B7 7B 02                  movzx r15d, word ptr [rbx + 2]
008BB86A  8B 7D CC                        mov edi, dword ptr [rbp - 0x34]
008BB86D  48 8B 55 88                     mov rdx, qword ptr [rbp - 0x78]
008BB871  44 8B C7                        mov r8d, edi
008BB874  41 8B C7                        mov eax, r15d
008BB877  48 03 D8                        add rbx, rax
008BB87A  48 8B CB                        mov rcx, rbx
008BB87D  E8 BE AF E0 FF                  call 0x1406c6840
008BB882  8B C3                           mov eax, ebx
008BB884  48 03 DF                        add rbx, rdi
008BB887  2B C6                           sub eax, esi
008BB889  80 7C 24 66 00                  cmp byte ptr [rsp + 0x66], 0
008BB88E  89 46 04                        mov dword ptr [rsi + 4], eax
008BB891  75 10                           jne 0x1408bb8a3
008BB893  49 8B 45 00                     mov rax, qword ptr [r13]
008BB897  0F B7 48 02                     movzx ecx, word ptr [rax + 2]
008BB89B  66 83 E1 01                     and cx, 1
008BB89F  66 09 4E 02                     or word ptr [rsi + 2], cx
008BB8A3  44 8B 44 24 70                  mov r8d, dword ptr [rsp + 0x70]
008BB8A8  48 8B CB                        mov rcx, rbx
008BB8AB  48 8B 55 80                     mov rdx, qword ptr [rbp - 0x80]
008BB8AF  E8 8C AF E0 FF                  call 0x1406c6840
008BB8B4  2B DE                           sub ebx, esi
008BB8B6  80 7C 24 67 00                  cmp byte ptr [rsp + 0x67], 0
008BB8BB  89 5E 08                        mov dword ptr [rsi + 8], ebx
008BB8BE  75 10                           jne 0x1408bb8d0
008BB8C0  49 8B 45 00                     mov rax, qword ptr [r13]
008BB8C4  0F B7 48 02                     movzx ecx, word ptr [rax + 2]
008BB8C8  66 83 E1 02                     and cx, 2
008BB8CC  66 09 4E 02                     or word ptr [rsi + 2], cx
008BB8D0  33 C0                           xor eax, eax
008BB8D2  49 89 75 00                     mov qword ptr [r13], rsi
008BB8D6  8B D8                           mov ebx, eax
008BB8D8  4C 8B 6D B0                     mov r13, qword ptr [rbp - 0x50]
008BB8DC  80 7C 24 59 00                  cmp byte ptr [rsp + 0x59], 0
008BB8E1  0F 85 56 0F 00 00               jne 0x1408bc83d
008BB8E7  48 8B 75 68                     mov rsi, qword ptr [rbp + 0x68]
008BB8EB  48 8B 7D A8                     mov rdi, qword ptr [rbp - 0x58]
008BB8EF  4C 8B 75 90                     mov r14, qword ptr [rbp - 0x70]
008BB8F3  4C 8B 7D 98                     mov r15, qword ptr [rbp - 0x68]
008BB8F7  4C 8B 65 A0                     mov r12, qword ptr [rbp - 0x60]
008BB8FB  48 85 F6                        test rsi, rsi
008BB8FE  0F 85 05 09 00 00               jne 0x1408bc209
008BB904  4D 85 FF                        test r15, r15
008BB907  0F 85 A7 08 00 00               jne 0x1408bc1b4
008BB90D  4D 85 E4                        test r12, r12
008BB910  0F 85 8F 06 00 00               jne 0x1408bbfa5
008BB916  4D 85 F6                        test r14, r14
008BB919  0F 85 6C 06 00 00               jne 0x1408bbf8b
008BB91F  48 85 FF                        test rdi, rdi
008BB922  0F 85 49 06 00 00               jne 0x1408bbf71
008BB928  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
008BB92C  48 85 C0                        test rax, rax
008BB92F  74 11                           je 0x1408bb942
008BB931  80 7C 24 6D 00                  cmp byte ptr [rsp + 0x6d], 0
008BB936  74 0A                           je 0x1408bb942
008BB938  33 D2                           xor edx, edx
008BB93A  48 8B C8                        mov rcx, rax
008BB93D  E8 2E 6F 2C 00                  call 0x140b82870
008BB942  80 7C 24 50 00                  cmp byte ptr [rsp + 0x50], 0
008BB947  0F 85 00 0F 00 00               jne 0x1408bc84d
008BB94D  4C 8B BC 24 B0 01 00 00         mov r15, qword ptr [rsp + 0x1b0]
008BB955  48 8D 45 48                     lea rax, [rbp + 0x48]
008BB959  4C 8B B4 24 B8 01 00 00         mov r14, qword ptr [rsp + 0x1b8]
008BB961  4C 8B AC 24 C0 01 00 00         mov r13, qword ptr [rsp + 0x1c0]
008BB969  4C 8B A4 24 C8 01 00 00         mov r12, qword ptr [rsp + 0x1c8]
008BB971  48 8B BC 24 D0 01 00 00         mov rdi, qword ptr [rsp + 0x1d0]
008BB979  48 8B B4 24 F0 01 00 00         mov rsi, qword ptr [rsp + 0x1f0]
008BB981  48 39 45 D8                     cmp qword ptr [rbp - 0x28], rax
008BB985  75 09                           jne 0x1408bb990
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_008BB534(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17, __int64 a18, __int64 a19, __int64 a20, __int64 a21, __int64 a22, __int64 a23, __int64 a24, __int64 a25, __int64 a26, __int64 a27, __int64 a28, __int64 a29, __int64 a30, __int64 a31, __int64 a32, __int64 a33, __int64 a34, __int64 a35, __int64 a36, __int64 a37, __int64 a38, __int64 a39, __int64 a40, __int64 a41, __int64 a42, __int64 a43, __int64 a44, __int64 a45, __int64 a46, __int64 a47, __int64 a48, __int64 a49, __int64 a50, __int64 a51, __int64 a52, __int64 a53, __int64 a54, __int64 a55, __int64 a56, __int64 a57, __int64 a58, __int64 a59, __int64 a60, __int64 a61, __int64 a62)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    unsigned __int64 v_stack_p1B0;
    unsigned __int8 v_stack_p50;
    unsigned int v_stack_p54;
    unsigned __int8 v_stack_p58;
    unsigned __int8 v_stack_p59;
    unsigned int v_stack_p60;
    unsigned __int8 v_stack_p64;
    unsigned __int8 v_stack_p65;
    unsigned __int8 v_stack_p66;
    unsigned __int8 v_stack_p67;
    unsigned __int8 v_stack_p68;
    unsigned __int8 v_stack_p69;
    unsigned __int8 v_stack_p6A;
    unsigned __int8 v_stack_p6B;
    unsigned __int8 v_stack_p6C;
    unsigned __int8 v_stack_p6D;
    unsigned int v_stack_p70;
    unsigned __int64 v_stack_p78;

    *(unsigned __int64 *)(v_r11 + 8) = v_rsi;
    *(unsigned __int64 *)(v_r11 - 24) = v_rdi;
    *(unsigned __int64 *)(v_r11 - 32) = v_r12;
    *(unsigned __int64 *)(v_r11 - 40) = v_r13;
    *(unsigned int *)(v_rbp + 56) = (unsigned int)(result);
    result = 0;
    v_stack_p50 = 0;
    v_stack_p58 = 0;
    v_stack_p59 = 0;
    v_stack_p6D = 0;
    v_stack_p68 = 0;
    v_stack_p69 = 0;
    v_stack_p6A = 0;
    v_stack_p6B = 0;
    v_stack_p6C = 0;
    *(unsigned __int64 *)(v_r11 - 48) = v_r14;
    v_r11 = 0;
    *(unsigned __int64 *)(v_rbp - 32) = a3;
    a3 = 0;
    *(unsigned __int64 *)(v_rbp - 72) = a4;
    *(unsigned __int64 *)(v_rbp - 8) = 0;
    *(unsigned __int64 *)(v_rbp - 24) = 0;
    *(unsigned __int64 *)(v_rbp + 104) = 0;
    *(unsigned __int64 *)(v_rbp + 64) = 0;
    *(unsigned __int64 *)(v_rbp - 96) = 0;
    *(unsigned __int64 *)(v_rbp + 16) = 0;
    *(unsigned __int64 *)(v_rbp - 104) = 0;
    *(unsigned __int64 *)(v_rbp + 8) = 0;
    *(unsigned __int64 *)(v_rbp - 112) = 0;
    *(unsigned __int64 *)(v_rbp + 24) = 0;
    *(unsigned __int64 *)(v_rbp - 88) = 0;
    *(unsigned __int64 *)(v_rbp + 32) = 0;
    *(unsigned __int8 *)(v_rbp - 16) = 0;
    *(unsigned __int64 *)(v_rbp - 80) = 0;
    *(unsigned __int64 *)(v_rbp + 48) = 0;
    *(unsigned __int64 *)(v_rbp - 64) = v_rbx;
    *(unsigned __int64 *)(v_rbp - 40) = *(unsigned __int64 *)(v_rbp + 296);
    v_stack_p67 = 0;
    v_stack_p66 = 0;
    v_stack_p70 = 0;
    *(unsigned __int64 *)(v_rbp - 48) = 0;
    *(unsigned __int64 *)(v_rbp + 40) = 0;
    *(unsigned int *)(v_rbp - 56) = 0;
    v_stack_p60 = 0;
    v_stack_p54 = 0x8000ULL;
    *(unsigned __int64 *)(v_rbp + 72) = v_xmm0;
    *(unsigned __int64 *)(v_rbp + 88) = v_xmm0;
    v_stack_p78 = 0;
    v_stack_p1B0 = v_r15;
    if ((((unsigned __int8)(*(unsigned __int16 *)(*(unsigned __int64 *)(a4) + 2))) & (16)) != 0) goto loc_008BB636;
    goto loc_008BB64E;
loc_008BB636:
loc_008BB64E:
    result = *(unsigned __int64 *)(a4);
    if (*(unsigned __int64 *)(v_rbp + 296) == 0) {
        a1 = v_rbp + 72;
        result = SeCaptureSubjectContext(a1, *(unsigned __int64 *)(v_rbp + 296), a3, a4);
        v_r11 = *(unsigned int *)(v_rbp - 56);
        result = v_rbp + 72;
        *(unsigned __int64 *)(v_rbp - 40) = result;
    }
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a4) + 2)) >= 0) goto loc_008BB7B3;
    v_r10 = 0;
    v_stack_p64 = 0;
    v_stack_p65 = 0;
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) & (128));
    a4 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) & (256));
    v_r10 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4) + 4))))) + (*(unsigned __int64 *)(a4));
    *(unsigned __int64 *)(v_rbp - 120) = v_r10;
    result = (unsigned __int8)((*(unsigned __int8 *)(v_r10)) & (15));
    *(unsigned __int64 *)(v_rbp - 128) = *(unsigned __int64 *)(a4) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4) + 8)) * 1;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(a4) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4) + 8)) * 1)) & (15));
    *(unsigned __int64 *)(v_rbp - 48) = *(unsigned __int64 *)(a4) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4) + 12)) * 1;
    result = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(a3 + 2))) & (4));
    v_r12 = 0;
loc_008BB7B3:
    goto loc_008BB94D;
loc_008BB94D:
}
```

## 5. (Beta) C Style

```c
int64_t sub_008BB534(int64_t Arg1, int32_t Arg2, void *Arg3, void *Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint64_t Arg13, uint64_t Arg14, uint64_t Arg15, uint64_t Arg16, uint64_t Arg17, uint64_t Arg18, uint64_t Arg19, uint64_t Arg20, uint64_t Arg21, uint64_t Arg22, uint64_t Arg23, uint64_t Arg24, uint64_t Arg25, uint64_t Arg26, uint64_t Arg27, uint64_t Arg28, uint64_t Arg29, uint64_t Arg30, uint64_t Arg31, uint64_t Arg32, uint64_t Arg33, uint64_t Arg34, uint64_t Arg35, uint64_t Arg36, uint64_t Arg37, uint64_t Arg38, uint64_t Arg39, uint64_t Arg40, uint64_t Arg41, uint64_t Arg42, uint64_t Arg43, uint64_t Arg44, uint64_t Arg45, uint64_t Arg46, uint64_t Arg47, uint64_t Arg48, uint64_t Arg49, uint64_t Arg50, uint64_t Arg51, uint64_t Arg52, uint64_t Arg53, int64_t Arg54, int64_t Arg55, int64_t Arg56, int64_t Arg57, int64_t Arg58, uint64_t Arg59, uint64_t Arg60, uint64_t Arg61, int64_t Arg62)
{
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    uint64_t v_stack_p1B0;
    uint8_t v_stack_p50;
    uint32_t v_stack_p54;
    uint8_t v_stack_p58;
    uint8_t v_stack_p59;
    uint32_t v_stack_p60;
    uint8_t v_stack_p64;
    uint8_t v_stack_p65;
    uint8_t v_stack_p66;
    uint8_t v_stack_p67;
    uint8_t v_stack_p68;
    uint8_t v_stack_p69;
    uint8_t v_stack_p6A;
    uint8_t v_stack_p6B;
    uint8_t v_stack_p6C;
    uint8_t v_stack_p6D;
    uint32_t v_stack_p70;
    uint64_t v_stack_p78;

    *(uint64_t *)(local_r11 + 0x8) = local_rsi;
    *(uint64_t *)(local_r11 - 0x18) = local_rdi;
    *(uint64_t *)(local_r11 - 0x20) = local_r12;
    *(uint64_t *)(local_r11 - 0x28) = local_r13;
    *(uint32_t *)(local_rbp + 0x38) = (uint32_t)(result);
    result = 0;
    v_stack_p50 = 0;
    v_stack_p58 = 0;
    v_stack_p59 = 0;
    v_stack_p6D = 0;
    v_stack_p68 = 0;
    v_stack_p69 = 0;
    v_stack_p6A = 0;
    v_stack_p6B = 0;
    v_stack_p6C = 0;
    *(uint64_t *)(local_r11 - 0x30) = local_r14;
    local_r11 = 0;
    *(void **)(local_rbp - 0x20) = Arg3;
    Arg3 = 0;
    *(void **)(local_rbp - 0x48) = Arg4;
    *(uint64_t *)(local_rbp - 0x8) = 0;
    *(uint64_t *)(local_rbp - 0x18) = 0;
    *(uint64_t *)(local_rbp + 0x68) = 0;
    *(uint64_t *)(local_rbp + 0x40) = 0;
    *(uint64_t *)(local_rbp - 0x60) = 0;
    *(uint64_t *)(local_rbp + 0x10) = 0;
    *(uint64_t *)(local_rbp - 0x68) = 0;
    *(uint64_t *)(local_rbp + 0x8) = 0;
    *(uint64_t *)(local_rbp - 0x70) = 0;
    *(uint64_t *)(local_rbp + 0x18) = 0;
    *(uint64_t *)(local_rbp - 0x58) = 0;
    *(uint64_t *)(local_rbp + 0x20) = 0;
    *(uint8_t *)(local_rbp - 0x10) = 0;
    *(uint64_t *)(local_rbp - 0x50) = 0;
    *(uint64_t *)(local_rbp + 0x30) = 0;
    *(uint64_t *)(local_rbp - 0x40) = local_rbx;
    *(uint64_t *)(local_rbp - 0x28) = *(uint64_t *)(local_rbp + 0x128);
    v_stack_p67 = 0;
    v_stack_p66 = 0;
    v_stack_p70 = 0;
    *(uint64_t *)(local_rbp - 0x30) = 0;
    *(uint64_t *)(local_rbp + 0x28) = 0;
    *(uint32_t *)(local_rbp - 0x38) = 0;
    v_stack_p60 = 0;
    v_stack_p54 = 0x8000ULL;
    *(uint64_t *)(local_rbp + 0x48) = v_xmm0;
    *(uint64_t *)(local_rbp + 0x58) = v_xmm0;
    v_stack_p78 = 0;
    v_stack_p1B0 = local_r15;
    if ((((uint8_t)(*(uint16_t *)(*(uint64_t *)(arg4) + 0x2))) & (16)) != 0) goto loc_008BB636;
    goto loc_008BB64E;
loc_008BB636:
loc_008BB64E:
    result = *(uint64_t *)(arg4);
    if (*(uint64_t *)(local_rbp + 0x128) == 0) {
        Arg1 = local_rbp + 72;
        result = SeCaptureSubjectContext(Arg1, *(uint64_t *)(local_rbp + 0x128), Arg3, Arg4);
        local_r11 = *(uint32_t *)(local_rbp - 0x38);
        result = local_rbp + 72;
        *(uint64_t *)(local_rbp - 0x28) = result;
    }
    if ((*(uint16_t *)(*(uint64_t *)(arg4) + 0x2)) >= 0) goto loc_008BB7B3;
    local_r10 = 0;
    v_stack_p64 = 0;
    v_stack_p65 = 0;
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) & (128));
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) & (256));
    local_r10 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4) + 0x4))))) + (*(uint64_t *)(arg4));
    *(uint64_t *)(local_rbp - 0x78) = local_r10;
    result = (uint8_t)((*(uint8_t *)(local_r10)) & (15));
    *(uint64_t *)(local_rbp - 0x80) = *(uint64_t *)(arg4) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4) + 0x8)) * 1;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(arg4) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4) + 0x8)) * 1)) & (15));
    *(uint64_t *)(local_rbp - 0x30) = *(uint64_t *)(arg4) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4) + 0xC)) * 1;
    result = (uint16_t)(((uint16_t)(*(uint16_t *)(arg3 + 0x2))) & (4));
    local_r12 = 0;
loc_008BB7B3:
    goto loc_008BB94D;
loc_008BB94D:
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x2` | `16` | `R` |
| `Arg4` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008BB534&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
