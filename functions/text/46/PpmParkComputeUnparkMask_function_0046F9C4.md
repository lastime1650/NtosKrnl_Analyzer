# PpmParkComputeUnparkMask

- RVA: `0x0046F9C4`–`0x004701D0` (길이 `2,060` bytes)
- VA: `0x000000014046F9C4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000ABCB8`
- 디코드: `494`개 명령, `2,060/2,060` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **13**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **17**

### Outgoing calls
- `0x0046FA44` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0046FA55` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0046FA66` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0046FA77` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0046FA88` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0046FA9F` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0046FAB0` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0046FD1B` → [KeGetPrcb](../2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x0046FDF7` → [EtwEventEnabled](../39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x0046FEFC` → [KeEnumerateNextProcessor](../41/KeEnumerateNextProcessor_function_00415480.md) (function, `0x00415480`)
- `0x0046FF3D` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0046FF6C` → [KeFindFirstSetRightAffinityEx](../47/KeFindFirstSetRightAffinityEx_function_004701E0.md) (function, `0x004701E0`)
- `0x00470066` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [sub_006F6620](../6F/Unknown_function_006F6620.md) at `0x006F6B62`

### Static image references
- `0x0046F9E0` → RVA `0x00E0A740` (`.data`; read)
- `0x0046FAB5` → RVA `0x00E08380` (`.data`; read)
- `0x0046FABF` → RVA `0x00F0CE0C` (`.data`; read)
- `0x0046FB39` → RVA `0x00F0E280` (`.data`; read)
- `0x0046FBA1` → RVA `0x00FC501C` (`ALMOSTRO`; read)
- `0x0046FCAA` → RVA `0x00FC6B40` (`ALMOSTRO`; read)
- `0x0046FD11` → RVA `0x00F231B8` (`.data`; read)
- `0x0046FD26` → RVA `0x00F083C1` (`.data`; read)
- `0x0046FD6A` → RVA `0x00F083C8` (`.data`; read)
- `0x0046FD8F` → RVA `0x00E67A39` (`.data`; read)
- `0x0046FDE9` → RVA `0x00F083E8` (`.data`; read)
- `0x0046FDF0` → RVA `0x00019F00` (`.rdata`; read)
- `0x0046FF18` → RVA `0x00F083B8` (`.data`; read)
- `0x0046FF71` → RVA `0x00F083B0` (`.data`; read)
- `0x0046FF98` → RVA `0x00F083C0` (`.data`; write)
- `0x0046FFA1` → RVA `0x00F083B0` (`.data`; write)
- `0x0046FFA7` → RVA `0x00F231B0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **16**
  - `0x0046FB4A` → [sub_006F3648](../6F/Unknown_function_006F3648.md) (`tail-transfer`)
  - `0x0046FBA9` → [sub_006F3648 + 0x1BB](../6F/Unknown_function_006F3648.md) (`tail-transfer`)
  - `0x0046FE00` → [sub_006F3648 + 0x352](../6F/Unknown_function_006F3648.md) (`tail-transfer`)
  - `0x0046FE74` → [sub_006F3648 + 0x4D5](../6F/Unknown_function_006F3648.md) (`tail-transfer`)
  - `0x0046FEB7` → [sub_006F3648 + 0x242](../6F/Unknown_function_006F3648.md) (`tail-transfer`)
  - `0x0046FF05` → [sub_006F3648 + 0x33A](../6F/Unknown_function_006F3648.md) (`tail-transfer`)
  - `0x0046FF13` → [sub_006F3648 + 0x2F8](../6F/Unknown_function_006F3648.md) (`tail-transfer`)
  - `0x0047009A` → [sub_006F3648 + 0x4E6](../6F/Unknown_function_006F3648.md) (`tail-transfer`)
  - `0x004700F7` → [sub_006F3648 + 0x23A](../6F/Unknown_function_006F3648.md) (`tail-transfer`)
  - `0x0047014E` → [sub_006F3648 + 0x4C5](../6F/Unknown_function_006F3648.md) (`tail-transfer`)
  - `0x00470157` → [sub_006F3648 + 0x4C5](../6F/Unknown_function_006F3648.md) (`tail-transfer`)
  - `0x00470169` → [sub_006F3648 + 0x4CD](../6F/Unknown_function_006F3648.md) (`tail-transfer`)
  - `0x00470172` → [sub_006F3648 + 0x4CD](../6F/Unknown_function_006F3648.md) (`tail-transfer`)
  - `0x00470185` → [sub_006F3648 + 0x4DE](../6F/Unknown_function_006F3648.md) (`tail-transfer`)
  - `0x0047018E` → [sub_006F3648 + 0x4DE](../6F/Unknown_function_006F3648.md) (`tail-transfer`)
  - `0x004701CB` → [sub_006F3648 + 0x4E6](../6F/Unknown_function_006F3648.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0046F9C4  40 55                           push rbp
0046F9C6  53                              push rbx
0046F9C7  56                              push rsi
0046F9C8  57                              push rdi
0046F9C9  41 54                           push r12
0046F9CB  41 55                           push r13
0046F9CD  41 56                           push r14
0046F9CF  41 57                           push r15
0046F9D1  48 8D AC 24 18 F7 FF FF         lea rbp, [rsp - 0x8e8]
0046F9D9  48 81 EC E8 09 00 00            sub rsp, 0x9e8
0046F9E0  48 8B 05 59 AD 99 00            mov rax, qword ptr [rip + 0x99ad59]
0046F9E7  48 33 C4                        xor rax, rsp
0046F9EA  48 89 85 D0 08 00 00            mov qword ptr [rbp + 0x8d0], rax
0046F9F1  48 8B 85 70 09 00 00            mov rax, qword ptr [rbp + 0x970]
0046F9F8  48 8B FA                        mov rdi, rdx
0046F9FB  4C 8B B5 78 09 00 00            mov r14, qword ptr [rbp + 0x978]
0046FA02  48 8B D9                        mov rbx, rcx
0046FA05  48 8B B5 80 09 00 00            mov rsi, qword ptr [rbp + 0x980]
0046FA0C  0F 57 C0                        xorps xmm0, xmm0
0046FA0F  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
0046FA14  41 BF 08 01 00 00               mov r15d, 0x108
0046FA1A  33 C0                           xor eax, eax
0046FA1C  4C 89 45 C8                     mov qword ptr [rbp - 0x38], r8
0046FA20  48 89 4D 98                     mov qword ptr [rbp - 0x68], rcx
0046FA24  45 8B C7                        mov r8d, r15d
0046FA27  33 D2                           xor edx, edx
0046FA29  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
0046FA2D  48 8D 8D D0 05 00 00            lea rcx, [rbp + 0x5d0]
0046FA34  4C 89 4D D8                     mov qword ptr [rbp - 0x28], r9
0046FA38  4C 89 75 20                     mov qword ptr [rbp + 0x20], r14
0046FA3C  48 89 75 28                     mov qword ptr [rbp + 0x28], rsi
0046FA40  0F 11 45 00                     movups xmmword ptr [rbp], xmm0
0046FA44  E8 F7 71 25 00                  call 0x1406c6c40
0046FA49  45 8B C7                        mov r8d, r15d
0046FA4C  48 8D 8D C0 04 00 00            lea rcx, [rbp + 0x4c0]
0046FA53  33 D2                           xor edx, edx
0046FA55  E8 E6 71 25 00                  call 0x1406c6c40
0046FA5A  45 8B C7                        mov r8d, r15d
0046FA5D  48 8D 8D A0 02 00 00            lea rcx, [rbp + 0x2a0]
0046FA64  33 D2                           xor edx, edx
0046FA66  E8 D5 71 25 00                  call 0x1406c6c40
0046FA6B  45 8B C7                        mov r8d, r15d
0046FA6E  48 8D 8D 80 00 00 00            lea rcx, [rbp + 0x80]
0046FA75  33 D2                           xor edx, edx
0046FA77  E8 C4 71 25 00                  call 0x1406c6c40
0046FA7C  45 8B C7                        mov r8d, r15d
0046FA7F  48 8D 8D E0 06 00 00            lea rcx, [rbp + 0x6e0]
0046FA86  33 D2                           xor edx, edx
0046FA88  E8 B3 71 25 00                  call 0x1406c6c40
0046FA8D  33 C0                           xor eax, eax
0046FA8F  48 8D 8D B0 03 00 00            lea rcx, [rbp + 0x3b0]
0046FA96  45 8B C7                        mov r8d, r15d
0046FA99  89 44 24 5C                     mov dword ptr [rsp + 0x5c], eax
0046FA9D  33 D2                           xor edx, edx
0046FA9F  E8 9C 71 25 00                  call 0x1406c6c40
0046FAA4  45 8B C7                        mov r8d, r15d
0046FAA7  48 8D 8D 90 01 00 00            lea rcx, [rbp + 0x190]
0046FAAE  33 D2                           xor edx, edx
0046FAB0  E8 8B 71 25 00                  call 0x1406c6c40
0046FAB5  48 8B 15 C4 88 99 00            mov rdx, qword ptr [rip + 0x9988c4]
0046FABC  45 33 C9                        xor r9d, r9d
0046FABF  48 63 05 46 D3 A9 00            movsxd rax, dword ptr [rip + 0xa9d346]
0046FAC6  45 8B F9                        mov r15d, r9d
0046FAC9  44 0F B7 63 04                  movzx r12d, word ptr [rbx + 4]
0046FACE  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
0046FAD3  48 69 C8 E8 01 00 00            imul rcx, rax, 0x1e8
0046FADA  66 44 89 64 24 52               mov word ptr [rsp + 0x52], r12w
0046FAE0  8A 84 11 F0 01 00 00            mov al, byte ptr [rcx + rdx + 0x1f0]
0046FAE7  88 44 24 56                     mov byte ptr [rsp + 0x56], al
0046FAEB  8A 84 11 F1 01 00 00            mov al, byte ptr [rcx + rdx + 0x1f1]
0046FAF2  88 44 24 55                     mov byte ptr [rsp + 0x55], al
0046FAF6  0F B7 83 E4 04 00 00            movzx eax, word ptr [rbx + 0x4e4]
0046FAFD  89 45 A0                        mov dword ptr [rbp - 0x60], eax
0046FB00  48 8B 83 E8 04 00 00            mov rax, qword ptr [rbx + 0x4e8]
0046FB07  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0046FB0B  8A 84 11 F2 01 00 00            mov al, byte ptr [rcx + rdx + 0x1f2]
0046FB12  4D 89 08                        mov qword ptr [r8], r9
0046FB15  88 44 24 57                     mov byte ptr [rsp + 0x57], al
0046FB19  4D 89 0E                        mov qword ptr [r14], r9
0046FB1C  44 39 8D 58 09 00 00            cmp dword ptr [rbp + 0x958], r9d
0046FB23  0F 84 30 05 00 00               je 0x140470059
0046FB29  44 8B AD 50 09 00 00            mov r13d, dword ptr [rbp + 0x950]
0046FB30  45 85 ED                        test r13d, r13d
0046FB33  0F 84 20 05 00 00               je 0x140470059
0046FB39  4C 8B 35 40 E7 A9 00            mov r14, qword ptr [rip + 0xa9e740]
0046FB40  48 8B 9D 60 09 00 00            mov rbx, qword ptr [rbp + 0x960]
0046FB47  4D 85 F6                        test r14, r14
0046FB4A  0F 85 F8 3A 28 00               jne 0x1406f3648
0046FB50  45 8B E9                        mov r13d, r9d
0046FB53  4C 89 4D F0                     mov qword ptr [rbp - 0x10], r9
0046FB57  45 8B F1                        mov r14d, r9d
0046FB5A  48 8B 85 68 09 00 00            mov rax, qword ptr [rbp + 0x968]
0046FB61  4D 8B E6                        mov r12, r14
0046FB64  4D 0B E5                        or r12, r13
0046FB67  4C 89 75 E0                     mov qword ptr [rbp - 0x20], r14
0046FB6B  4C 0B E3                        or r12, rbx
0046FB6E  49 89 38                        mov qword ptr [r8], rdi
0046FB71  4C 0B E0                        or r12, rax
0046FB74  BA 00 02 00 00                  mov edx, 0x200
0046FB79  49 F7 D4                        not r12
0046FB7C  41 BA 00 04 00 00               mov r10d, 0x400
0046FB82  4C 23 E7                        and r12, rdi
0046FB85  41 BB 00 08 00 00               mov r11d, 0x800
0046FB8B  4C 89 65 30                     mov qword ptr [rbp + 0x30], r12
0046FB8F  48 85 F8                        test rax, rdi
0046FB92  0F 85 07 05 00 00               jne 0x14047009f
0046FB98  49 85 FE                        test r14, rdi
0046FB9B  0F 85 3F 05 00 00               jne 0x1404700e0
0046FBA1  8B 05 75 54 B5 00               mov eax, dword ptr [rip + 0xb55475]
0046FBA7  A8 08                           test al, 8
0046FBA9  0F 85 54 3C 28 00               jne 0x1406f3803
0046FBAF  49 85 FC                        test r12, rdi
0046FBB2  0F 84 39 05 00 00               je 0x1404700f1
0046FBB8  44 09 1E                        or dword ptr [rsi], r11d
0046FBBB  45 8B FB                        mov r15d, r11d
0046FBBE  49 8B 18                        mov rbx, qword ptr [r8]
0046FBC1  49 23 DC                        and rbx, r12
0046FBC4  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
0046FBC8  41 8B C9                        mov ecx, r9d
0046FBCB  48 8B 55 D8                     mov rdx, qword ptr [rbp - 0x28]
0046FBCF  4C 8B EB                        mov r13, rbx
0046FBD2  48 23 D0                        and rdx, rax
0046FBD5  48 89 5D 88                     mov qword ptr [rbp - 0x78], rbx
0046FBD9  48 33 C7                        xor rax, rdi
0046FBDC  4C 89 4C 24 78                  mov qword ptr [rsp + 0x78], r9
0046FBE1  48 23 45 D8                     and rax, qword ptr [rbp - 0x28]
0046FBE5  45 8B F1                        mov r14d, r9d
0046FBE8  0F B7 7C 24 52                  movzx edi, word ptr [rsp + 0x52]
0046FBED  48 89 45 18                     mov qword ptr [rbp + 0x18], rax
0046FBF1  B0 FF                           mov al, 0xff
0046FBF3  88 44 24 54                     mov byte ptr [rsp + 0x54], al
0046FBF7  88 44 24 50                     mov byte ptr [rsp + 0x50], al
0046FBFB  4C 89 4D 80                     mov qword ptr [rbp - 0x80], r9
0046FBFF  48 89 55 F8                     mov qword ptr [rbp - 8], rdx
0046FC03  89 4C 24 58                     mov dword ptr [rsp + 0x58], ecx
0046FC07  44 89 4C 24 60                  mov dword ptr [rsp + 0x60], r9d
0046FC0C  48 89 7D E8                     mov qword ptr [rbp - 0x18], rdi
0046FC10  EB 77                           jmp 0x14046fc89
0046FC12  4C 23 CA                        and r9, rdx
0046FC15  0F B6 4C 24 57                  movzx ecx, byte ptr [rsp + 0x57]
0046FC1A  4C 89 4D 80                     mov qword ptr [rbp - 0x80], r9
0046FC1E  85 C9                           test ecx, ecx
0046FC20  74 13                           je 0x14046fc35
0046FC22  83 E9 01                        sub ecx, 1
0046FC25  74 0E                           je 0x14046fc35
0046FC27  83 E9 01                        sub ecx, 1
0046FC2A  74 09                           je 0x14046fc35
0046FC2C  83 F9 01                        cmp ecx, 1
0046FC2F  0F 84 66 05 00 00               je 0x14047019b
0046FC35  48 8B 87 60 8E 00 00            mov rax, qword ptr [rdi + 0x8e60]
0046FC3C  0F B7 7C 24 52                  movzx edi, word ptr [rsp + 0x52]
0046FC41  48 F7 D0                        not rax
0046FC44  8B 4C 24 58                     mov ecx, dword ptr [rsp + 0x58]
0046FC48  48 23 D8                        and rbx, rax
0046FC4B  44 8B 74 24 60                  mov r14d, dword ptr [rsp + 0x60]
0046FC50  48 8B 55 F8                     mov rdx, qword ptr [rbp - 8]
0046FC54  4D 85 ED                        test r13, r13
0046FC57  75 2D                           jne 0x14046fc86
0046FC59  4D 85 DB                        test r11, r11
0046FC5C  75 21                           jne 0x14046fc7f
0046FC5E  48 85 DB                        test rbx, rbx
0046FC61  0F 84 AD 03 00 00               je 0x140470014
0046FC67  4C 8B DB                        mov r11, rbx
0046FC6A  4D 23 DA                        and r11, r10
0046FC6D  4C 0F 44 DB                     cmove r11, rbx
0046FC71  49 8B C3                        mov rax, r11
0046FC74  49 23 C1                        and rax, r9
0046FC77  4C 0F 45 D8                     cmovne r11, rax
0046FC7B  4C 89 5D 88                     mov qword ptr [rbp - 0x78], r11
0046FC7F  8B 4C 24 58                     mov ecx, dword ptr [rsp + 0x58]
0046FC83  4D 8B EB                        mov r13, r11
0046FC86  45 33 C9                        xor r9d, r9d
0046FC89  3B 8D 58 09 00 00               cmp ecx, dword ptr [rbp + 0x958]
0046FC8F  0F 83 C7 03 00 00               jae 0x14047005c
0046FC95  4D 85 ED                        test r13, r13
0046FC98  0F 84 BE 03 00 00               je 0x14047005c
0046FC9E  49 8B C5                        mov rax, r13
0046FCA1  48 23 C2                        and rax, rdx
0046FCA4  0F 85 62 04 00 00               jne 0x14047010c
0046FCAA  8B 15 90 6E B5 00               mov edx, dword ptr [rip + 0xb56e90]
0046FCB0  8D 42 FD                        lea eax, [rdx - 3]
0046FCB3  A9 FC FF FF FF                  test eax, 0xfffffffc
0046FCB8  0F 84 F0 01 00 00               je 0x14046feae
0046FCBE  49 8B C5                        mov rax, r13
0046FCC1  48 23 45 18                     and rax, qword ptr [rbp + 0x18]
0046FCC5  0F 85 52 04 00 00               jne 0x14047011d
0046FCCB  48 8B 85 88 09 00 00            mov rax, qword ptr [rbp + 0x988]
0046FCD2  44 38 48 10                     cmp byte ptr [rax + 0x10], r9b
0046FCD6  75 19                           jne 0x14046fcf1
0046FCD8  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
0046FCDC  48 F7 D0                        not rax
0046FCDF  49 23 C5                        and rax, r13
0046FCE2  74 0D                           je 0x14046fcf1
0046FCE4  B9 00 20 00 00                  mov ecx, 0x2000
0046FCE9  4C 8B E8                        mov r13, rax
0046FCEC  09 0E                           or dword ptr [rsi], ecx
0046FCEE  44 0B F9                        or r15d, ecx
0046FCF1  41 8B CE                        mov ecx, r14d
0046FCF4  44 89 4C 24 70                  mov dword ptr [rsp + 0x70], r9d
0046FCF9  49 8B C5                        mov rax, r13
0046FCFC  48 D3 C8                        ror rax, cl
0046FCFF  48 0F BC D0                     bsf rdx, rax
0046FD03  0F B7 C7                        movzx eax, di
0046FD06  41 03 D6                        add edx, r14d
0046FD09  C1 E0 06                        shl eax, 6
0046FD0C  83 E2 3F                        and edx, 0x3f
0046FD0F  03 D0                           add edx, eax
0046FD11  48 8B 05 A0 34 AB 00            mov rax, qword ptr [rip + 0xab34a0]
0046FD18  8B 0C 90                        mov ecx, dword ptr [rax + rdx*4]
0046FD1B  E8 B0 88 E6 FF                  call 0x1402d85d0
0046FD20  33 D2                           xor edx, edx
0046FD22  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
0046FD26  38 15 95 86 A9 00               cmp byte ptr [rip + 0xa98695], dl
0046FD2C  48 8B F8                        mov rdi, rax
0046FD2F  0F 84 FA 03 00 00               je 0x14047012f
0046FD35  4C 8B B0 60 8E 00 00            mov r14, qword ptr [rax + 0x8e60]
0046FD3C  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
0046FD41  49 8B C6                        mov rax, r14
0046FD44  8B 4C 24 58                     mov ecx, dword ptr [rsp + 0x58]
0046FD48  48 F7 D0                        not rax
0046FD4B  44 8B 8D 50 09 00 00            mov r9d, dword ptr [rbp + 0x950]
0046FD52  4C 89 74 24 70                  mov qword ptr [rsp + 0x70], r14
0046FD57  49 21 00                        and qword ptr [r8], rax
0046FD5A  41 3B C9                        cmp ecx, r9d
0046FD5D  0F 82 59 01 00 00               jb 0x14046febc
0046FD63  48 8B 45 20                     mov rax, qword ptr [rbp + 0x20]
0046FD67  4C 09 30                        or qword ptr [rax], r14
0046FD6A  48 39 15 57 86 A9 00            cmp qword ptr [rip + 0xa98657], rdx
0046FD71  0F 85 A1 01 00 00               jne 0x14046ff18
0046FD77  4C 8B 5D 88                     mov r11, qword ptr [rbp - 0x78]
0046FD7B  4C 8B 4D 80                     mov r9, qword ptr [rbp - 0x80]
0046FD7F  4C 8B 54 24 78                  mov r10, qword ptr [rsp + 0x78]
0046FD84  F3 49 0F B8 C6                  popcnt rax, r14
0046FD89  03 C8                           add ecx, eax
0046FD8B  48 89 5D 68                     mov qword ptr [rbp + 0x68], rbx
0046FD8F  38 15 A4 7C 9F 00               cmp byte ptr [rip + 0x9f7ca4], dl
0046FD95  48 8B 45 D8                     mov rax, qword ptr [rbp - 0x28]
0046FD99  48 89 45 70                     mov qword ptr [rbp + 0x70], rax
0046FD9D  49 8B 00                        mov rax, qword ptr [r8]
0046FDA0  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
0046FDA4  8B 85 90 09 00 00               mov eax, dword ptr [rbp + 0x990]
0046FDAA  89 45 90                        mov dword ptr [rbp - 0x70], eax
0046FDAD  8B 85 58 09 00 00               mov eax, dword ptr [rbp + 0x958]
0046FDB3  89 45 B8                        mov dword ptr [rbp - 0x48], eax
0046FDB6  8B 85 50 09 00 00               mov eax, dword ptr [rbp + 0x950]
0046FDBC  89 45 B0                        mov dword ptr [rbp - 0x50], eax
0046FDBF  0F B7 44 24 52                  movzx eax, word ptr [rsp + 0x52]
0046FDC4  89 45 A8                        mov dword ptr [rbp - 0x58], eax
0046FDC7  89 4C 24 58                     mov dword ptr [rsp + 0x58], ecx
0046FDCB  4C 89 5D 60                     mov qword ptr [rbp + 0x60], r11
0046FDCF  4C 89 4D 58                     mov qword ptr [rbp + 0x58], r9
0046FDD3  4C 89 55 50                     mov qword ptr [rbp + 0x50], r10
0046FDD7  4C 89 75 48                     mov qword ptr [rbp + 0x48], r14
0046FDDB  4C 89 6D 38                     mov qword ptr [rbp + 0x38], r13
0046FDDF  44 89 7C 24 70                  mov dword ptr [rsp + 0x70], r15d
0046FDE4  89 4D C0                        mov dword ptr [rbp - 0x40], ecx
0046FDE7  74 2F                           je 0x14046fe18
0046FDE9  48 8B 0D F8 85 A9 00            mov rcx, qword ptr [rip + 0xa985f8]
0046FDF0  48 8D 15 09 A1 BA FF            lea rdx, [rip - 0x455ef7]
0046FDF7  E8 54 26 F2 FF                  call 0x140392450
0046FDFC  33 D2                           xor edx, edx
0046FDFE  84 C0                           test al, al
0046FE00  0F 85 94 3B 28 00               jne 0x1406f399a
0046FE06  4C 8B 5D 88                     mov r11, qword ptr [rbp - 0x78]
0046FE0A  4C 8B 54 24 78                  mov r10, qword ptr [rsp + 0x78]
0046FE0F  4C 8B 4D 80                     mov r9, qword ptr [rbp - 0x80]
0046FE13  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
0046FE18  48 8B 87 C0 00 00 00            mov rax, qword ptr [rdi + 0xc0]
0046FE1F  44 8B FA                        mov r15d, edx
0046FE22  0F B6 97 D0 00 00 00            movzx edx, byte ptr [rdi + 0xd0]
0046FE29  48 8B 88 80 00 00 00            mov rcx, qword ptr [rax + 0x80]
0046FE30  48 8B 84 D7 18 8C 00 00         mov rax, qword ptr [rdi + rdx*8 + 0x8c18]
0046FE38  48 F7 D1                        not rcx
0046FE3B  48 F7 D0                        not rax
0046FE3E  4C 23 E9                        and r13, rcx
0046FE41  0F B6 4C 24 55                  movzx ecx, byte ptr [rsp + 0x55]
0046FE46  4C 23 D8                        and r11, rax
0046FE49  33 C0                           xor eax, eax
0046FE4B  4C 89 5D 88                     mov qword ptr [rbp - 0x78], r11
0046FE4F  85 C9                           test ecx, ecx
0046FE51  74 12                           je 0x14046fe65
0046FE53  83 E9 01                        sub ecx, 1
0046FE56  0F 84 00 03 00 00               je 0x14047015c
0046FE5C  83 F9 01                        cmp ecx, 1
0046FE5F  0F 84 D6 02 00 00               je 0x14047013b
0046FE65  4C 8B D0                        mov r10, rax
0046FE68  4C 89 54 24 78                  mov qword ptr [rsp + 0x78], r10
0046FE6D  66 3B 97 10 9F 00 00            cmp dx, word ptr [rdi + 0x9f10]
0046FE74  0F 83 A3 3C 28 00               jae 0x1406f3b1d
0046FE7A  48 8B 94 D7 18 9F 00 00         mov rdx, qword ptr [rdi + rdx*8 + 0x9f18]
0046FE82  0F B6 4C 24 56                  movzx ecx, byte ptr [rsp + 0x56]
0046FE87  33 C0                           xor eax, eax
0046FE89  85 C9                           test ecx, ecx
0046FE8B  0F 84 02 03 00 00               je 0x140470193
0046FE91  83 E9 01                        sub ecx, 1
0046FE94  0F 85 DD 02 00 00               jne 0x140470177
0046FE9A  48 F7 D2                        not rdx
0046FE9D  49 85 D1                        test r9, rdx
0046FEA0  0F 85 6C FD FF FF               jne 0x14046fc12
0046FEA6  4D 8B 08                        mov r9, qword ptr [r8]
0046FEA9  E9 64 FD FF FF                  jmp 0x14046fc12
0046FEAE  83 FA 04                        cmp edx, 4
0046FEB1  0F 84 07 FE FF FF               je 0x14046fcbe
0046FEB7  E9 CE 39 28 00                  jmp 0x1406f388a
0046FEBC  48 39 55 D0                     cmp qword ptr [rbp - 0x30], rdx
0046FEC0  0F 84 B1 FE FF FF               je 0x14046fd77
0046FEC6  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
0046FECA  83 B8 D0 04 00 00 03            cmp dword ptr [rax + 0x4d0], 3
0046FED1  0F 85 A0 FE FF FF               jne 0x14046fd77
0046FED7  0F B7 44 24 52                  movzx eax, word ptr [rsp + 0x52]
0046FEDC  41 FF C9                        dec r9d
0046FEDF  8B 7D A0                        mov edi, dword ptr [rbp - 0x60]
0046FEE2  2B F9                           sub edi, ecx
0046FEE4  48 89 55 00                     mov qword ptr [rbp], rdx
0046FEE8  48 8D 4C 24 5C                  lea rcx, [rsp + 0x5c]
0046FEED  66 89 45 10                     mov word ptr [rbp + 0x10], ax
0046FEF1  48 8D 55 00                     lea rdx, [rbp]
0046FEF5  4C 89 75 08                     mov qword ptr [rbp + 8], r14
0046FEF9  41 03 F9                        add edi, r9d
0046FEFC  E8 7F 55 FA FF                  call 0x140415480
0046FF01  33 D2                           xor edx, edx
0046FF03  85 C0                           test eax, eax
0046FF05  0F 85 77 3A 28 00               jne 0x1406f3982
0046FF0B  4C 8B 65 98                     mov r12, qword ptr [rbp - 0x68]
0046FF0F  48 8B 75 D0                     mov rsi, qword ptr [rbp - 0x30]
0046FF13  E9 28 3A 28 00                  jmp 0x1406f3940
0046FF18  48 39 15 99 84 A9 00            cmp qword ptr [rip + 0xa98499], rdx
0046FF1F  0F 84 52 FE FF FF               je 0x14046fd77
0046FF25  41 B8 00 01 00 00               mov r8d, 0x100
0046FF2B  48 C7 85 80 00 00 00 01 00 20 00  mov qword ptr [rbp + 0x80], 0x200001
0046FF36  48 8D 8D 88 00 00 00            lea rcx, [rbp + 0x88]
0046FF3D  E8 FE 6C 25 00                  call 0x1406c6c40
0046FF42  0F B7 44 24 52                  movzx eax, word ptr [rsp + 0x52]
0046FF47  0F B7 BD 80 00 00 00            movzx edi, word ptr [rbp + 0x80]
0046FF4E  66 3B F8                        cmp di, ax
0046FF51  0F 86 6D 01 00 00               jbe 0x1404700c4
0046FF57  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
0046FF5B  4C 09 B4 C5 88 00 00 00         or qword ptr [rbp + rax*8 + 0x88], r14
0046FF63  EB 76                           jmp 0x14046ffdb
0046FF65  48 8D 8D 80 00 00 00            lea rcx, [rbp + 0x80]
0046FF6C  E8 6F 02 00 00                  call 0x1404701e0
0046FF71  8B 15 39 84 A9 00               mov edx, dword ptr [rip + 0xa98439]
0046FF77  8B C8                           mov ecx, eax
0046FF79  48 8B 05 48 84 A9 00            mov rax, qword ptr [rip + 0xa98448]
0046FF80  89 4C 24 5C                     mov dword ptr [rsp + 0x5c], ecx
0046FF84  89 14 88                        mov dword ptr [rax + rcx*4], edx
0046FF87  48 8B 05 2A 84 A9 00            mov rax, qword ptr [rip + 0xa9842a]
0046FF8E  3B 14 88                        cmp edx, dword ptr [rax + rcx*4]
0046FF91  74 0B                           je 0x14046ff9e
0046FF93  B8 01 00 00 00                  mov eax, 1
0046FF98  88 05 22 84 A9 00               mov byte ptr [rip + 0xa98422], al
0046FF9E  8D 42 01                        lea eax, [rdx + 1]
0046FFA1  89 05 09 84 A9 00               mov dword ptr [rip + 0xa98409], eax
0046FFA7  48 8B 05 02 32 AB 00            mov rax, qword ptr [rip + 0xab3202]
0046FFAE  44 8B 04 88                     mov r8d, dword ptr [rax + rcx*4]
0046FFB2  41 8B C8                        mov ecx, r8d
0046FFB5  C1 E9 06                        shr ecx, 6
0046FFB8  0F B7 C7                        movzx eax, di
0046FFBB  3B C1                           cmp eax, ecx
0046FFBD  76 23                           jbe 0x14046ffe2
0046FFBF  8B D1                           mov edx, ecx
0046FFC1  41 8B C8                        mov ecx, r8d
0046FFC4  83 E1 3F                        and ecx, 0x3f
0046FFC7  48 8B 84 D5 88 00 00 00         mov rax, qword ptr [rbp + rdx*8 + 0x88]
0046FFCF  48 0F B3 C8                     btr rax, rcx
0046FFD3  48 89 84 D5 88 00 00 00         mov qword ptr [rbp + rdx*8 + 0x88], rax
0046FFDB  0F B7 BD 80 00 00 00            movzx edi, word ptr [rbp + 0x80]
0046FFE2  33 D2                           xor edx, edx
0046FFE4  0F B7 CA                        movzx ecx, dx
0046FFE7  66 3B CF                        cmp cx, di
0046FFEA  73 16                           jae 0x140470002
0046FFEC  0F B7 C1                        movzx eax, cx
0046FFEF  48 39 94 C5 88 00 00 00         cmp qword ptr [rbp + rax*8 + 0x88], rdx
0046FFF7  0F 85 68 FF FF FF               jne 0x14046ff65
0046FFFD  66 FF C1                        inc cx
00470000  EB E5                           jmp 0x14046ffe7
00470002  8B 4C 24 58                     mov ecx, dword ptr [rsp + 0x58]
00470006  48 8B 7D 90                     mov rdi, qword ptr [rbp - 0x70]
0047000A  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
0047000F  E9 63 FD FF FF                  jmp 0x14046fd77
00470014  49 8B 08                        mov rcx, qword ptr [r8]
00470017  48 8B 85 68 09 00 00            mov rax, qword ptr [rbp + 0x968]
0047001E  48 85 C8                        test rax, rcx
00470021  0F 85 80 01 00 00               jne 0x1404701a7
00470027  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
0047002B  48 85 C8                        test rax, rcx
0047002E  75 7F                           jne 0x1404700af
00470030  8B 05 E6 4F B5 00               mov eax, dword ptr [rip + 0xb54fe6]
00470036  A8 08                           test al, 8
00470038  75 46                           jne 0x140470080
0047003A  49 85 CC                        test r12, rcx
0047003D  0F 85 6E 01 00 00               jne 0x1404701b1
00470043  48 8B D9                        mov rbx, rcx
00470046  48 23 5D F0                     and rbx, qword ptr [rbp - 0x10]
0047004A  0F 85 76 01 00 00               jne 0x1404701c6
00470050  33 C0                           xor eax, eax
00470052  8B D8                           mov ebx, eax
00470054  E9 0E FC FF FF                  jmp 0x14046fc67
00470059  49 89 38                        mov qword ptr [r8], rdi
0047005C  48 8B 8D D0 08 00 00            mov rcx, qword ptr [rbp + 0x8d0]
00470063  48 33 CC                        xor rcx, rsp
00470066  E8 D5 C5 23 00                  call 0x1406ac640
0047006B  48 81 C4 E8 09 00 00            add rsp, 0x9e8
00470072  41 5F                           pop r15
00470074  41 5E                           pop r14
00470076  41 5D                           pop r13
00470078  41 5C                           pop r12
0047007A  5F                              pop rdi
0047007B  5E                              pop rsi
0047007C  5B                              pop rbx
0047007D  5D                              pop rbp
0047007E  C3                              ret
0047007F  CC                              int3
00470080  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
00470084  48 23 8C C5 98 01 00 00         and rcx, qword ptr [rbp + rax*8 + 0x198]
0047008C  0F 84 D5 FB FF FF               je 0x14046fc67
00470092  48 8B D9                        mov rbx, rcx
00470095  B8 00 00 40 00                  mov eax, 0x400000
0047009A  E9 8F 3A 28 00                  jmp 0x1406f3b2e
0047009F  09 16                           or dword ptr [rsi], edx
004700A1  44 8B FA                        mov r15d, edx
004700A4  49 8B 18                        mov rbx, qword ptr [r8]
004700A7  48 23 D8                        and rbx, rax
004700AA  E9 15 FB FF FF                  jmp 0x14046fbc4
004700AF  B9 00 04 00 00                  mov ecx, 0x400
004700B4  09 0E                           or dword ptr [rsi], ecx
004700B6  44 8B F9                        mov r15d, ecx
004700B9  49 8B 18                        mov rbx, qword ptr [r8]
004700BC  48 23 D8                        and rbx, rax
004700BF  E9 A3 FB FF FF                  jmp 0x14046fc67
004700C4  66 39 85 82 00 00 00            cmp word ptr [rbp + 0x82], ax
004700CB  0F 86 11 FF FF FF               jbe 0x14046ffe2
004700D1  66 FF C0                        inc ax
004700D4  66 89 85 80 00 00 00            mov word ptr [rbp + 0x80], ax
004700DB  E9 77 FE FF FF                  jmp 0x14046ff57
004700E0  44 09 16                        or dword ptr [rsi], r10d
004700E3  45 8B FA                        mov r15d, r10d
004700E6  49 8B 18                        mov rbx, qword ptr [r8]
004700E9  49 23 DE                        and rbx, r14
004700EC  E9 D3 FA FF FF                  jmp 0x14046fbc4
004700F1  48 8B DF                        mov rbx, rdi
004700F4  49 23 DD                        and rbx, r13
004700F7  0F 84 85 37 28 00               je 0x1406f3882
004700FD  B8 00 00 08 00                  mov eax, 0x80000
00470102  09 06                           or dword ptr [rsi], eax
00470104  44 8B F8                        mov r15d, eax
00470107  E9 B8 FA FF FF                  jmp 0x14046fbc4
0047010C  0F BA 2E 11                     bts dword ptr [rsi], 0x11
00470110  4C 8B E8                        mov r13, rax
00470113  41 0F BA EF 11                  bts r15d, 0x11
00470118  E9 8D FB FF FF                  jmp 0x14046fcaa
0047011D  B9 00 10 00 00                  mov ecx, 0x1000
00470122  4C 8B E8                        mov r13, rax
00470125  09 0E                           or dword ptr [rsi], ecx
00470127  44 0B F9                        or r15d, ecx
0047012A  E9 9C FB FF FF                  jmp 0x14046fccb
0047012F  4C 8B B0 C8 00 00 00            mov r14, qword ptr [rax + 0xc8]
00470136  E9 01 FC FF FF                  jmp 0x14046fd3c
0047013B  48 8B 8F 70 8E 00 00            mov rcx, qword ptr [rdi + 0x8e70]
00470142  49 8B C6                        mov rax, r14
00470145  48 F7 D0                        not rax
00470148  48 23 C8                        and rcx, rax
0047014B  49 85 CA                        test r10, rcx
0047014E  0F 85 B9 39 28 00               jne 0x1406f3b0d
00470154  4D 8B 10                        mov r10, qword ptr [r8]
00470157  E9 B1 39 28 00                  jmp 0x1406f3b0d
0047015C  48 8B 87 70 8E 00 00            mov rax, qword ptr [rdi + 0x8e70]
00470163  48 F7 D0                        not rax
00470166  49 85 C2                        test r10, rax
00470169  0F 85 A6 39 28 00               jne 0x1406f3b15
0047016F  4D 8B 10                        mov r10, qword ptr [r8]
00470172  E9 9E 39 28 00                  jmp 0x1406f3b15
00470177  83 F9 01                        cmp ecx, 1
0047017A  75 17                           jne 0x140470193
0047017C  49 F7 D6                        not r14
0047017F  4C 23 F2                        and r14, rdx
00470182  4D 85 F1                        test r9, r14
00470185  0F 85 9B 39 28 00               jne 0x1406f3b26
0047018B  4D 8B 08                        mov r9, qword ptr [r8]
0047018E  E9 93 39 28 00                  jmp 0x1406f3b26
00470193  4C 8B C8                        mov r9, rax
00470196  E9 7A FA FF FF                  jmp 0x14046fc15
0047019B  48 8B 87 C8 00 00 00            mov rax, qword ptr [rdi + 0xc8]
004701A2  E9 95 FA FF FF                  jmp 0x14046fc3c
004701A7  B9 00 02 00 00                  mov ecx, 0x200
004701AC  E9 03 FF FF FF                  jmp 0x1404700b4
004701B1  B8 00 08 00 00                  mov eax, 0x800
004701B6  09 06                           or dword ptr [rsi], eax
004701B8  44 8B F8                        mov r15d, eax
004701BB  49 8B 18                        mov rbx, qword ptr [r8]
004701BE  49 23 DC                        and rbx, r12
004701C1  E9 A1 FA FF FF                  jmp 0x14046fc67
004701C6  B8 00 00 08 00                  mov eax, 0x80000
004701CB  E9 5E 39 28 00                  jmp 0x1406f3b2e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmParkComputeUnparkMask(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, unsigned int a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, unsigned int a13)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m248;
    unsigned __int64 v_stack_m358;
    unsigned __int64 v_stack_m468;
    unsigned __int64 v_stack_m578;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m688;
    unsigned __int64 v_stack_m798;
    unsigned __int64 v_stack_m8A0;
    unsigned __int16 v_stack_m8A6;
    unsigned __int64 v_stack_m8A8;
    unsigned __int64 v_stack_m8B8;
    unsigned __int64 v_stack_m8C0;
    unsigned __int64 v_stack_m8C8;
    unsigned __int64 v_stack_m8D0;
    unsigned __int64 v_stack_m8D8;
    unsigned __int64 v_stack_m8E0;
    unsigned __int64 v_stack_m8E8;
    unsigned __int64 v_stack_m8F0;
    unsigned __int64 v_stack_m8F8;
    unsigned __int64 v_stack_m900;
    unsigned __int64 v_stack_m908;
    unsigned __int64 v_stack_m910;
    unsigned __int64 v_stack_m918;
    unsigned __int64 v_stack_m920;
    unsigned __int64 v_stack_m928;
    unsigned __int64 v_stack_m930;
    unsigned __int64 v_stack_m938;
    unsigned __int64 v_stack_m940;
    unsigned __int64 v_stack_m948;
    unsigned __int64 v_stack_m950;
    unsigned __int64 v_stack_m958;
    unsigned __int64 v_stack_m960;
    unsigned int v_stack_m968;
    unsigned int v_stack_m970;
    unsigned int v_stack_m978;
    unsigned int v_stack_m980;
    unsigned int v_stack_m988;
    unsigned __int64 v_stack_m990;
    unsigned __int64 v_stack_m998;
    unsigned __int64 v_stack_m9A0;
    unsigned __int64 v_stack_m9A8;
    unsigned __int64 v_stack_m9B0;
    unsigned int v_stack_m9B8;
    unsigned __int64 v_stack_m9C0;
    unsigned int v_stack_m9C8;
    unsigned int v_stack_m9CC;
    unsigned int v_stack_m9D0;
    unsigned __int8 v_stack_m9D1;
    unsigned __int8 v_stack_m9D2;
    unsigned __int8 v_stack_m9D3;
    unsigned __int8 v_stack_m9D4;
    unsigned __int16 v_stack_m9D6;
    unsigned __int8 v_stack_m9D8;

    v_rsp = (v_rsp) - (0x9E8ULL);
    result = (*(unsigned __int64 *)(v_rip + 10071385)) ^ (v_rsp);
    v_stack_m58 = result;
    v_stack_m9C0 = a9;
    result = 0;
    v_stack_m960 = a3;
    v_stack_m990 = a1;
    a2 = 0;
    v_stack_m918 = 0;
    v_stack_m950 = a4;
    v_stack_m908 = a10;
    v_stack_m900 = a11;
    v_stack_m928 = v_xmm0;
    result = memset(v_stack_m358, a2, 264, a4);
    a2 = 0;
    result = memset(v_stack_m468, a2, 264, a4);
    a2 = 0;
    result = memset(v_stack_m688, a2, 264, a4);
    a2 = 0;
    result = memset(v_stack_m8A8, a2, 264, a4);
    a2 = 0;
    result = memset(v_stack_m248, a2, 264, a4);
    result = 0;
    v_stack_m9CC = 0;
    a2 = 0;
    result = memset(v_stack_m578, a2, 264, a4);
    a2 = 0;
    result = memset(v_stack_m798, a2, 264, a4);
    a4 = 0;
    a1 = (v_stack_m798) * ((int)(*(unsigned int *)(v_rip + 11129670)));
    v_stack_m9D6 = (unsigned __int16)(*(unsigned __int16 *)(a1 + 4));
    v_stack_m9D2 = (unsigned __int8)(*(unsigned __int8 *)(a1 + *(unsigned __int64 *)(v_rip + 10062020) * 1 + 496));
    v_stack_m9D3 = (unsigned __int8)(*(unsigned __int8 *)(a1 + *(unsigned __int64 *)(v_rip + 10062020) * 1 + 497));
    v_stack_m988 = (unsigned int)(*(unsigned __int16 *)(a1 + 1252));
    v_stack_m958 = *(unsigned __int64 *)(a1 + 1256);
    *(unsigned __int64 *)(v_stack_m9C0) = 0;
    v_stack_m9D1 = (unsigned __int8)(*(unsigned __int8 *)(a1 + *(unsigned __int64 *)(v_rip + 10062020) * 1 + 498));
    *(unsigned __int64 *)(a10) = 0;
    if (a6 == 0) goto loc_00470059;
    if ((unsigned int)((unsigned int)(a5)) == 0) goto loc_00470059;
    v_stack_m938 = 0;
    v_r12 = (0) | (0);
    v_stack_m948 = 0;
    v_r12 = (v_r12) | (a7);
    *(unsigned __int64 *)(v_stack_m9C0) = 0;
    v_r12 = (v_r12) | (a8);
    v_r12 = ~(v_r12);
    v_r12 = (v_r12) & (0);
    v_stack_m8F8 = v_r12;
    if (((a8) & (0)) != 0) goto loc_0047009F;
    if (0 != 0) goto loc_004700E0;
    if (((v_r12) & (0)) == 0) goto loc_004700F1;
    v_rbx = (*(unsigned __int64 *)(v_stack_m9C0)) & (v_r12);
loc_0046FBC4:
    a2 = (v_stack_m950) & (v_stack_m960);
    v_stack_m9A0 = v_rbx;
    result = (v_stack_m960) ^ (a2);
    v_stack_m9B0 = 0;
    result = (result) & (v_stack_m950);
    v_stack_m910 = result;
    v_stack_m9D4 = 255;
    v_stack_m9D8 = 255;
    v_stack_m9A8 = 0;
    v_stack_m930 = a2;
    v_stack_m9D0 = 0;
    v_stack_m9C8 = 0;
    v_stack_m940 = v_stack_m9D6;
    goto loc_0046FC89;
loc_0046FC12:
    a4 = (a4) & (a2);
loc_0046FC15:
    v_stack_m9A8 = a4;
    if ((unsigned int)(v_stack_m9D1) == 0) goto loc_0046FC35;
    a1 = (unsigned int)((v_stack_m9D1) - (1));
    if (condition_is_equal) goto loc_0046FC35;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0046FC35;
    if (((unsigned int)(a1)) == 1) goto loc_0047019B;
loc_0046FC35:
loc_0046FC3C:
    result = ~(*(unsigned __int64 *)(v_stack_m9D6 + 36448));
    v_rbx = (v_rbx) & (result);
    if (v_rbx != 0) goto loc_0046FC86;
    if ((unsigned int)(0x800ULL) != 0) goto loc_0046FC7F;
    if (v_rbx == 0) goto loc_00470014;
loc_0046FC67:
    v_r11 = (v_rbx) & ((unsigned int)(0x400ULL));
    if (condition_is_equal) { v_r11 = v_rbx; }
    result = (v_r11) & (a4);
    if (condition_is_not_equal) { v_r11 = result; }
    v_stack_m9A0 = v_r11;
loc_0046FC7F:
loc_0046FC86:
    a4 = 0;
loc_0046FC89:
    if (((unsigned int)((unsigned int)(v_stack_m9D0))) >= a6) goto loc_0047005C;
    if (v_r11 == 0) goto loc_0047005C;
    result = (v_r11) & (v_stack_m930);
    if (condition_is_not_equal) goto loc_0047010C;
loc_0046FCAA:
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11890320)) - 3)) & (0xFFFFFFFCULL)) == 0) goto loc_0046FEAE;
loc_0046FCBE:
    result = (v_r11) & (v_stack_m910);
    if (condition_is_not_equal) goto loc_0047011D;
loc_0046FCCB:
    if ((*(unsigned __int8 *)(a12 + 16)) != 0) goto loc_0046FCF1;
    result = ~(v_stack_m960);
    result = (result) & (v_r11);
    v_r13 = v_r11;
    v_r15 = (unsigned int)((unsigned int)((unsigned int)(0x800ULL)));
    if (!(condition_is_equal)) {
        a1 = 0x2000ULL;
        v_r13 = result;
        v_r15 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x800ULL)))) | ((unsigned int)(a1)));
    }
    v_stack_m9B8 = 0;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 11890320))) + ((unsigned int)((unsigned int)(v_stack_m9C8))));
    result = (unsigned int)(((unsigned __int16)(v_stack_m9D6)) << (6));
    a2 = (unsigned int)((a2) & (63));
    a2 = (unsigned int)((a2) + ((unsigned int)(result)));
    result = KeGetPrcb((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11220128) + a2 * 4)), a2, v_stack_m9C0, a4);
    a2 = 0;
    v_stack_m998 = result;
    if ((*(unsigned __int8 *)(v_rip + 11110037)) == 0) goto loc_0047012F;
loc_0046FD3C:
    result = ~(*(unsigned __int64 *)(result + 36448));
    v_stack_m9B8 = *(unsigned __int64 *)(result + 36448);
    if (((unsigned int)((unsigned int)(v_stack_m9D0))) < ((unsigned int)((unsigned int)(a5)))) goto loc_0046FEBC;
    if ((*(unsigned __int64 *)(v_rip + 11109975)) != 0) goto loc_0046FF18;
loc_0046FD77:
    a1 = (unsigned int)(((unsigned int)(v_stack_m9D0)) + ((unsigned int)(v_stack_m908)));
    v_stack_m8C0 = v_rbx;
    v_stack_m8B8 = v_stack_m950;
    v_stack_m8E8 = *(unsigned __int64 *)(v_stack_m9C0);
    v_stack_m998 = (unsigned int)((unsigned int)(a13));
    v_stack_m970 = (unsigned int)((unsigned int)(a6));
    v_stack_m978 = (unsigned int)((unsigned int)(a5));
    v_stack_m980 = (unsigned int)(v_stack_m9D6);
    v_stack_m9D0 = (unsigned int)(a1);
    v_stack_m8C8 = v_stack_m9A0;
    v_stack_m8D0 = v_stack_m9A8;
    v_stack_m8D8 = v_stack_m9B0;
    v_stack_m8E0 = *(unsigned __int64 *)(result + 36448);
    v_stack_m8F0 = v_r13;
    v_stack_m9B8 = (unsigned int)(v_r15);
    v_stack_m968 = (unsigned int)(a1);
    if ((*(unsigned __int8 *)(v_rip + 10452132)) == 0) goto loc_0046FE18;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 11109880), v_rip - 4546295, v_stack_m9C0, v_stack_m9A8);
    a2 = 0;
loc_0046FE18:
    a1 = ~(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 192) + 128));
    result = ~(*(unsigned __int64 *)(result + *(unsigned __int8 *)(result + 208) * 8 + 35864));
    v_r13 = (v_r13) & (a1);
    v_r11 = (v_stack_m9A0) & (result);
    result = 0;
    v_stack_m9A0 = v_r11;
    if ((unsigned int)(v_stack_m9D3) == 0) goto loc_0046FE65;
    a1 = (unsigned int)((v_stack_m9D3) - (1));
    if (condition_is_equal) goto loc_0047015C;
    if (((unsigned int)(a1)) == 1) goto loc_0047013B;
loc_0046FE65:
    v_stack_m9B0 = 0;
    result = 0;
    if ((unsigned int)(v_stack_m9D2) == 0) goto loc_00470193;
    a1 = (unsigned int)((v_stack_m9D2) - (1));
    if (condition_is_not_equal) goto loc_00470177;
    a2 = ~(*(unsigned __int64 *)(result + *(unsigned __int8 *)(result + 208) * 8 + 40728));
    if (((v_stack_m9A8) & (a2)) != 0) goto loc_0046FC12;
    goto loc_0046FC12;
loc_0046FEAE:
    if (((unsigned int)(a2)) == 4) goto loc_0046FCBE;
loc_0046FEBC:
    if (v_stack_m958 == a2) goto loc_0046FD77;
    if ((*(unsigned int *)(v_stack_m990 + 1232)) != 3) goto loc_0046FD77;
    a4 = (unsigned int)((*(unsigned __int64 *)(v_stack_m9C0)) - 1);
    v_rdi = (unsigned int)(((unsigned int)(v_stack_m988)) - ((unsigned int)(a1)));
    v_stack_m928 = a2;
    v_stack_m918 = (unsigned __int16)(v_stack_m9D6);
    v_stack_m920 = *(unsigned __int64 *)(result + 36448);
    v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(a4)));
    result = KeEnumerateNextProcessor(v_stack_m9CC, v_stack_m928, v_stack_m9C0, a4);
    a2 = 0;
loc_0046FF18:
    if ((*(unsigned __int64 *)(v_rip + 11109529)) == 0) goto loc_0046FD77;
    v_stack_m8A8 = 0x200001ULL;
    result = memset(v_stack_m8A0, a2, 256, a4);
    if (((unsigned __int16)(v_stack_m8A8)) <= ((unsigned __int16)(v_stack_m9D6))) goto loc_004700C4;
loc_0046FF57:
    goto loc_0046FFDB;
loc_0046FF65:
    result = KeFindFirstSetRightAffinityEx(v_stack_m8A8, a2, 256, a4);
    v_stack_m9CC = (unsigned int)((unsigned int)((unsigned int)(result)));
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 11109448) + (unsigned int)((unsigned int)(result)) * 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11109433)));
    result = *(unsigned __int64 *)(v_rip + 11109418);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11109433)))) != (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11109418) + (unsigned int)((unsigned int)(result)) * 4))) {
        result = 1;
        *(unsigned __int8 *)(v_rip + 11109410) = (unsigned __int8)(result);
    }
    *(unsigned int *)(v_rip + 11109385) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11109433)) + 1);
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11219458) + (unsigned int)((unsigned int)(result)) * 4))))) >> (6));
    if (((unsigned int)((unsigned __int16)(v_stack_m8A8))) <= ((unsigned int)(a1))) goto loc_0046FFE2;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11219458) + (unsigned int)((unsigned int)(result)) * 4))))) & (63));
    *(unsigned __int64 *)(v_stack_m928 + (unsigned int)((unsigned int)(a1)) * 8 + 136) = *(unsigned __int64 *)(v_stack_m928 + (unsigned int)((unsigned int)(a1)) * 8 + 136);
loc_0046FFDB:
loc_0046FFE2:
    a2 = 0;
loc_0046FFE7:
    if (0 >= ((unsigned __int16)(v_stack_m8A8))) goto loc_00470002;
    if ((*(unsigned __int64 *)(v_stack_m928 + 0 * 8 + 136)) != 0) goto loc_0046FF65;
    a1 = (unsigned __int16)((0) + 1);
    goto loc_0046FFE7;
loc_00470002:
    goto loc_0046FD77;
loc_00470014:
    if (((a8) & (*(unsigned __int64 *)(v_stack_m9C0))) != 0) goto loc_004701A7;
    if (((v_stack_m948) & (*(unsigned __int64 *)(v_stack_m9C0))) != 0) goto loc_004700AF;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11882470)))) & (8)) != 0) goto loc_00470080;
    if (((v_stack_m990) & (*(unsigned __int64 *)(v_stack_m9C0))) != 0) goto loc_004701B1;
    v_rbx = (*(unsigned __int64 *)(v_stack_m9C0)) & (v_stack_m938);
    if (condition_is_not_equal) goto loc_004701C6;
    result = 0;
    goto loc_0046FC67;
loc_00470059:
    *(unsigned __int64 *)(v_stack_m9C0) = v_stack_m998;
loc_0047005C:
    a1 = (v_stack_m58) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, v_stack_m9C0, a4);
    v_rsp = (v_rsp) + (0x9E8ULL);
    return result;
loc_00470080:
    a1 = (a1) & (*(unsigned __int64 *)(v_stack_m928 + v_stack_m940 * 8 + 408));
    if (condition_is_equal) goto loc_0046FC67;
loc_0047009F:
    v_rbx = (*(unsigned __int64 *)(v_stack_m9C0)) & ((unsigned int)(0x400000ULL));
    goto loc_0046FBC4;
loc_004700AF:
loc_004700B4:
    v_rbx = (*(unsigned __int64 *)(v_stack_m9C0)) & ((unsigned int)(0x400000ULL));
    goto loc_0046FC67;
loc_004700C4:
    if (v_stack_m8A6 <= ((unsigned __int16)((unsigned int)(0x400000ULL)))) goto loc_0046FFE2;
    result = (unsigned __int16)(((unsigned int)(0x400000ULL)) + 1);
    v_stack_m8A8 = (unsigned __int16)(result);
    goto loc_0046FF57;
loc_004700E0:
    v_rbx = (*(unsigned __int64 *)(v_stack_m9C0)) & (*(unsigned __int64 *)(result + 36448));
    goto loc_0046FBC4;
loc_004700F1:
    v_rbx = (v_stack_m998) & (v_r13);
    goto loc_0046FBC4;
loc_0047010C:
    goto loc_0046FCAA;
loc_0047011D:
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x80000ULL)))) | ((unsigned int)((unsigned int)(0x1000ULL))));
    goto loc_0046FCCB;
loc_0047012F:
    goto loc_0046FD3C;
loc_0047013B:
    result = ~(*(unsigned __int64 *)((unsigned int)(0x80000ULL) + 200));
    a1 = (*(unsigned __int64 *)(v_stack_m998 + 36464)) & (result);
loc_0047015C:
    result = ~(*(unsigned __int64 *)(v_stack_m998 + 36464));
loc_00470177:
    if (((unsigned int)(a1)) != 1) goto loc_00470193;
    v_r14 = ~(*(unsigned __int64 *)((unsigned int)(0x80000ULL) + 200));
    v_r14 = (v_r14) & (0);
loc_00470193:
    goto loc_0046FC15;
loc_0047019B:
    goto loc_0046FC3C;
loc_004701A7:
    goto loc_004700B4;
loc_004701B1:
    v_rbx = (*(unsigned __int64 *)(v_stack_m9C0)) & (v_stack_m990);
    goto loc_0046FC67;
loc_004701C6:
}
```

## 5. (Beta) C Style

```c
int64_t PpmParkComputeUnparkMask(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5, uint32_t Arg6, int64_t Arg7, int64_t Arg8, int64_t Arg9, void *Arg10, void *Arg11, void *Arg12, uint32_t Arg13)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg10 = (uint8_t *)Arg10;
    uint8_t *arg11 = (uint8_t *)Arg11;
    uint8_t *arg12 = (uint8_t *)Arg12;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m248;
    uint64_t v_stack_m358;
    uint64_t v_stack_m468;
    uint64_t v_stack_m578;
    uint64_t v_stack_m58;
    uint64_t v_stack_m688;
    uint64_t v_stack_m798;
    uint64_t v_stack_m8A0;
    uint16_t v_stack_m8A6;
    uint64_t v_stack_m8A8;
    uint64_t v_stack_m8B8;
    uint64_t v_stack_m8C0;
    uint64_t v_stack_m8C8;
    uint64_t v_stack_m8D0;
    uint64_t v_stack_m8D8;
    uint64_t v_stack_m8E0;
    uint64_t v_stack_m8E8;
    uint64_t v_stack_m8F0;
    uint64_t v_stack_m8F8;
    uint64_t v_stack_m900;
    uint64_t v_stack_m908;
    uint64_t v_stack_m910;
    uint64_t v_stack_m918;
    uint64_t v_stack_m920;
    uint64_t v_stack_m928;
    uint64_t v_stack_m930;
    uint64_t v_stack_m938;
    uint64_t v_stack_m940;
    uint64_t v_stack_m948;
    uint64_t v_stack_m950;
    uint64_t v_stack_m958;
    uint64_t v_stack_m960;
    uint32_t v_stack_m968;
    uint32_t v_stack_m970;
    uint32_t v_stack_m978;
    uint32_t v_stack_m980;
    uint32_t v_stack_m988;
    uint64_t v_stack_m990;
    uint64_t v_stack_m998;
    uint64_t v_stack_m9A0;
    uint64_t v_stack_m9A8;
    uint64_t v_stack_m9B0;
    uint32_t v_stack_m9B8;
    uint64_t v_stack_m9C0;
    uint32_t v_stack_m9C8;
    uint32_t v_stack_m9CC;
    uint32_t v_stack_m9D0;
    uint8_t v_stack_m9D1;
    uint8_t v_stack_m9D2;
    uint8_t v_stack_m9D3;
    uint8_t v_stack_m9D4;
    uint16_t v_stack_m9D6;
    uint8_t v_stack_m9D8;

    local_rsp = (local_rsp) - (0x9E8ULL);
    result = (*(uint64_t *)(v_rip + 0x99AD59)) ^ (local_rsp);
    v_stack_m58 = result;
    v_stack_m9C0 = Arg9;
    result = 0;
    v_stack_m960 = Arg3;
    v_stack_m990 = Arg1;
    Arg2 = 0;
    v_stack_m918 = 0;
    v_stack_m950 = Arg4;
    v_stack_m908 = Arg10;
    v_stack_m900 = Arg11;
    v_stack_m928 = v_xmm0;
    result = memset(v_stack_m358, Arg2, 264, Arg4);
    Arg2 = 0;
    result = memset(v_stack_m468, Arg2, 264, Arg4);
    Arg2 = 0;
    result = memset(v_stack_m688, Arg2, 264, Arg4);
    Arg2 = 0;
    result = memset(v_stack_m8A8, Arg2, 264, Arg4);
    Arg2 = 0;
    result = memset(v_stack_m248, Arg2, 264, Arg4);
    result = 0;
    v_stack_m9CC = 0;
    Arg2 = 0;
    result = memset(v_stack_m578, Arg2, 264, Arg4);
    Arg2 = 0;
    result = memset(v_stack_m798, Arg2, 264, Arg4);
    Arg4 = 0;
    Arg1 = (v_stack_m798) * ((int32_t)(*(uint32_t *)(v_rip + 0xA9D346)));
    v_stack_m9D6 = (uint16_t)(*(uint16_t *)(arg1 + 0x4));
    v_stack_m9D2 = (uint8_t)(*(uint8_t *)(arg1 + *(uint64_t *)(v_rip + 0x9988C4) * 1 + 0x1F0));
    v_stack_m9D3 = (uint8_t)(*(uint8_t *)(arg1 + *(uint64_t *)(v_rip + 0x9988C4) * 1 + 0x1F1));
    v_stack_m988 = (uint32_t)(*(uint16_t *)(arg1 + 0x4E4));
    v_stack_m958 = *(uint64_t *)(arg1 + 0x4E8);
    *(uint64_t *)(v_stack_m9C0) = 0;
    v_stack_m9D1 = (uint8_t)(*(uint8_t *)(arg1 + *(uint64_t *)(v_rip + 0x9988C4) * 1 + 0x1F2));
    *(uint64_t *)(arg10) = 0;
    if (Arg6 == 0) goto loc_00470059;
    if ((uint32_t)((uint32_t)(Arg5)) == 0) goto loc_00470059;
    v_stack_m938 = 0;
    local_r12 = (0) | (0);
    v_stack_m948 = 0;
    local_r12 = (local_r12) | (Arg7);
    *(uint64_t *)(v_stack_m9C0) = 0;
    local_r12 = (local_r12) | (Arg8);
    local_r12 = ~(local_r12);
    local_r12 = (local_r12) & (0);
    v_stack_m8F8 = local_r12;
    if (((Arg8) & (0)) != 0) goto loc_0047009F;
    if (0 != 0) goto loc_004700E0;
    if (((local_r12) & (0)) == 0) goto loc_004700F1;
    local_rbx = (*(uint64_t *)(v_stack_m9C0)) & (local_r12);
loc_0046FBC4:
    Arg2 = (v_stack_m950) & (v_stack_m960);
    v_stack_m9A0 = local_rbx;
    result = (v_stack_m960) ^ (Arg2);
    v_stack_m9B0 = 0;
    result = (result) & (v_stack_m950);
    v_stack_m910 = result;
    v_stack_m9D4 = 255;
    v_stack_m9D8 = 255;
    v_stack_m9A8 = 0;
    v_stack_m930 = Arg2;
    v_stack_m9D0 = 0;
    v_stack_m9C8 = 0;
    v_stack_m940 = v_stack_m9D6;
    goto loc_0046FC89;
loc_0046FC12:
    Arg4 = (Arg4) & (Arg2);
loc_0046FC15:
    v_stack_m9A8 = Arg4;
    if ((uint32_t)(v_stack_m9D1) == 0) goto loc_0046FC35;
    Arg1 = (uint32_t)((v_stack_m9D1) - (1));
    if (condition_is_equal) goto loc_0046FC35;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0046FC35;
    if (((uint32_t)(Arg1)) == 1) goto loc_0047019B;
loc_0046FC35:
loc_0046FC3C:
    result = ~(*(uint64_t *)(v_stack_m9D6 + 0x8E60));
    local_rbx = (local_rbx) & (result);
    if (local_rbx != 0) goto loc_0046FC86;
    if ((uint32_t)(0x800ULL) != 0) goto loc_0046FC7F;
    if (local_rbx == 0) goto loc_00470014;
loc_0046FC67:
    local_r11 = (local_rbx) & ((uint32_t)(0x400ULL));
    if (condition_is_equal) { local_r11 = local_rbx; }
    result = (local_r11) & (Arg4);
    if (condition_is_not_equal) { local_r11 = result; }
    v_stack_m9A0 = local_r11;
loc_0046FC7F:
loc_0046FC86:
    Arg4 = 0;
loc_0046FC89:
    if (((uint32_t)((uint32_t)(v_stack_m9D0))) >= Arg6) goto loc_0047005C;
    if (local_r11 == 0) goto loc_0047005C;
    result = (local_r11) & (v_stack_m930);
    if (condition_is_not_equal) goto loc_0047010C;
loc_0046FCAA:
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB56E90)) - 3)) & (0xFFFFFFFCULL)) == 0) goto loc_0046FEAE;
loc_0046FCBE:
    result = (local_r11) & (v_stack_m910);
    if (condition_is_not_equal) goto loc_0047011D;
loc_0046FCCB:
    if ((*(uint8_t *)(arg12 + 0x10)) != 0) goto loc_0046FCF1;
    result = ~(v_stack_m960);
    result = (result) & (local_r11);
    local_r13 = local_r11;
    local_r15 = (uint32_t)((uint32_t)((uint32_t)(0x800ULL)));
    if (!(condition_is_equal)) {
        Arg1 = 0x2000ULL;
        local_r13 = result;
        local_r15 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x800ULL)))) | ((uint32_t)(Arg1)));
    }
    v_stack_m9B8 = 0;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xB56E90))) + ((uint32_t)((uint32_t)(v_stack_m9C8))));
    result = (uint32_t)(((uint16_t)(v_stack_m9D6)) << (6));
    Arg2 = (uint32_t)((Arg2) & (63));
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(result)));
    result = KeGetPrcb((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xAB34A0) + Arg2 * 4)), Arg2, v_stack_m9C0, Arg4);
    Arg2 = 0;
    v_stack_m998 = result;
    if ((*(uint8_t *)(v_rip + 0xA98695)) == 0) goto loc_0047012F;
loc_0046FD3C:
    result = ~(*(uint64_t *)(result + 0x8E60));
    v_stack_m9B8 = *(uint64_t *)(result + 0x8E60);
    if (((uint32_t)((uint32_t)(v_stack_m9D0))) < ((uint32_t)((uint32_t)(Arg5)))) goto loc_0046FEBC;
    if ((*(uint64_t *)(v_rip + 0xA98657)) != 0) goto loc_0046FF18;
loc_0046FD77:
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m9D0)) + ((uint32_t)(v_stack_m908)));
    v_stack_m8C0 = local_rbx;
    v_stack_m8B8 = v_stack_m950;
    v_stack_m8E8 = *(uint64_t *)(v_stack_m9C0);
    v_stack_m998 = (uint32_t)((uint32_t)(Arg13));
    v_stack_m970 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m978 = (uint32_t)((uint32_t)(Arg5));
    v_stack_m980 = (uint32_t)(v_stack_m9D6);
    v_stack_m9D0 = (uint32_t)(Arg1);
    v_stack_m8C8 = v_stack_m9A0;
    v_stack_m8D0 = v_stack_m9A8;
    v_stack_m8D8 = v_stack_m9B0;
    v_stack_m8E0 = *(uint64_t *)(result + 0x8E60);
    v_stack_m8F0 = local_r13;
    v_stack_m9B8 = (uint32_t)(local_r15);
    v_stack_m968 = (uint32_t)(Arg1);
    if ((*(uint8_t *)(v_rip + 0x9F7CA4)) == 0) goto loc_0046FE18;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0xA985F8), v_rip - 4546295, v_stack_m9C0, v_stack_m9A8);
    Arg2 = 0;
loc_0046FE18:
    Arg1 = ~(*(uint64_t *)(*(uint64_t *)(result + 0xC0) + 0x80));
    result = ~(*(uint64_t *)(result + *(uint8_t *)(result + 0xD0) * 8 + 0x8C18));
    local_r13 = (local_r13) & (Arg1);
    local_r11 = (v_stack_m9A0) & (result);
    result = 0;
    v_stack_m9A0 = local_r11;
    if ((uint32_t)(v_stack_m9D3) == 0) goto loc_0046FE65;
    Arg1 = (uint32_t)((v_stack_m9D3) - (1));
    if (condition_is_equal) goto loc_0047015C;
    if (((uint32_t)(Arg1)) == 1) goto loc_0047013B;
loc_0046FE65:
    v_stack_m9B0 = 0;
    result = 0;
    if ((uint32_t)(v_stack_m9D2) == 0) goto loc_00470193;
    Arg1 = (uint32_t)((v_stack_m9D2) - (1));
    if (condition_is_not_equal) goto loc_00470177;
    Arg2 = ~(*(uint64_t *)(result + *(uint8_t *)(result + 0xD0) * 8 + 0x9F18));
    if (((v_stack_m9A8) & (Arg2)) != 0) goto loc_0046FC12;
    goto loc_0046FC12;
loc_0046FEAE:
    if (((uint32_t)(Arg2)) == 4) goto loc_0046FCBE;
loc_0046FEBC:
    if (v_stack_m958 == Arg2) goto loc_0046FD77;
    if ((*(uint32_t *)(v_stack_m990 + 0x4D0)) != 3) goto loc_0046FD77;
    Arg4 = (uint32_t)((*(uint64_t *)(v_stack_m9C0)) - 1);
    local_rdi = (uint32_t)(((uint32_t)(v_stack_m988)) - ((uint32_t)(Arg1)));
    v_stack_m928 = Arg2;
    v_stack_m918 = (uint16_t)(v_stack_m9D6);
    v_stack_m920 = *(uint64_t *)(result + 0x8E60);
    local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(Arg4)));
    result = KeEnumerateNextProcessor(v_stack_m9CC, v_stack_m928, v_stack_m9C0, Arg4);
    Arg2 = 0;
loc_0046FF18:
    if ((*(uint64_t *)(v_rip + 0xA98499)) == 0) goto loc_0046FD77;
    v_stack_m8A8 = 0x200001ULL;
    result = memset(v_stack_m8A0, Arg2, 256, Arg4);
    if (((uint16_t)(v_stack_m8A8)) <= ((uint16_t)(v_stack_m9D6))) goto loc_004700C4;
loc_0046FF57:
    goto loc_0046FFDB;
loc_0046FF65:
    result = KeFindFirstSetRightAffinityEx(v_stack_m8A8, Arg2, 256, Arg4);
    v_stack_m9CC = (uint32_t)((uint32_t)((uint32_t)(result)));
    *(uint32_t *)(*(uint64_t *)(v_rip + 0xA98448) + (uint32_t)((uint32_t)(result)) * 4) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA98439)));
    result = *(uint64_t *)(v_rip + 0xA9842A);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA98439)))) != (*(uint32_t *)(*(uint64_t *)(v_rip + 0xA9842A) + (uint32_t)((uint32_t)(result)) * 4))) {
        result = 1;
        *(uint8_t *)(v_rip + 0xA98422) = (uint8_t)(result);
    }
    *(uint32_t *)(v_rip + 0xA98409) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA98439)) + 1);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xAB3202) + (uint32_t)((uint32_t)(result)) * 4))))) >> (6));
    if (((uint32_t)((uint16_t)(v_stack_m8A8))) <= ((uint32_t)(Arg1))) goto loc_0046FFE2;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xAB3202) + (uint32_t)((uint32_t)(result)) * 4))))) & (63));
    *(uint64_t *)(v_stack_m928 + (uint32_t)((uint32_t)(arg1)) * 8 + 0x88) = *(uint64_t *)(v_stack_m928 + (uint32_t)((uint32_t)(arg1)) * 8 + 0x88);
loc_0046FFDB:
loc_0046FFE2:
    Arg2 = 0;
loc_0046FFE7:
    if (0 >= ((uint16_t)(v_stack_m8A8))) goto loc_00470002;
    if ((*(uint64_t *)(v_stack_m928 + 0x0 * 8 + 0x88)) != 0) goto loc_0046FF65;
    Arg1 = (uint16_t)((0) + 1);
    goto loc_0046FFE7;
loc_00470002:
    goto loc_0046FD77;
loc_00470014:
    if (((Arg8) & (*(uint64_t *)(v_stack_m9C0))) != 0) goto loc_004701A7;
    if (((v_stack_m948) & (*(uint64_t *)(v_stack_m9C0))) != 0) goto loc_004700AF;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB54FE6)))) & (8)) != 0) goto loc_00470080;
    if (((v_stack_m990) & (*(uint64_t *)(v_stack_m9C0))) != 0) goto loc_004701B1;
    local_rbx = (*(uint64_t *)(v_stack_m9C0)) & (v_stack_m938);
    if (condition_is_not_equal) goto loc_004701C6;
    result = 0;
    goto loc_0046FC67;
loc_00470059:
    *(uint64_t *)(v_stack_m9C0) = v_stack_m998;
loc_0047005C:
    Arg1 = (v_stack_m58) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, v_stack_m9C0, Arg4);
    local_rsp = (local_rsp) + (0x9E8ULL);
    return result;
loc_00470080:
    Arg1 = (Arg1) & (*(uint64_t *)(v_stack_m928 + v_stack_m940 * 8 + 0x198));
    if (condition_is_equal) goto loc_0046FC67;
loc_0047009F:
    local_rbx = (*(uint64_t *)(v_stack_m9C0)) & ((uint32_t)(0x400000ULL));
    goto loc_0046FBC4;
loc_004700AF:
loc_004700B4:
    local_rbx = (*(uint64_t *)(v_stack_m9C0)) & ((uint32_t)(0x400000ULL));
    goto loc_0046FC67;
loc_004700C4:
    if (v_stack_m8A6 <= ((uint16_t)((uint32_t)(0x400000ULL)))) goto loc_0046FFE2;
    result = (uint16_t)(((uint32_t)(0x400000ULL)) + 1);
    v_stack_m8A8 = (uint16_t)(result);
    goto loc_0046FF57;
loc_004700E0:
    local_rbx = (*(uint64_t *)(v_stack_m9C0)) & (*(uint64_t *)(result + 0x8E60));
    goto loc_0046FBC4;
loc_004700F1:
    local_rbx = (v_stack_m998) & (local_r13);
    goto loc_0046FBC4;
loc_0047010C:
    goto loc_0046FCAA;
loc_0047011D:
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x80000ULL)))) | ((uint32_t)((uint32_t)(0x1000ULL))));
    goto loc_0046FCCB;
loc_0047012F:
    goto loc_0046FD3C;
loc_0047013B:
    result = ~(*(uint64_t *)((uint32_t)(0x80000ULL) + 0xC8));
    Arg1 = (*(uint64_t *)(v_stack_m998 + 0x8E70)) & (result);
loc_0047015C:
    result = ~(*(uint64_t *)(v_stack_m998 + 0x8E70));
loc_00470177:
    if (((uint32_t)(Arg1)) != 1) goto loc_00470193;
    local_r14 = ~(*(uint64_t *)((uint32_t)(0x80000ULL) + 0xC8));
    local_r14 = (local_r14) & (0);
loc_00470193:
    goto loc_0046FC15;
loc_0047019B:
    goto loc_0046FC3C;
loc_004701A7:
    goto loc_004700B4;
loc_004701B1:
    local_rbx = (*(uint64_t *)(v_stack_m9C0)) & (v_stack_m990);
    goto loc_0046FC67;
loc_004701C6:
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x4` | `16` | `R` |
| `Arg1` | `+ 0x4E4` | `16` | `R` |
| `Arg1` | `+ 0x4E8` | `64` | `R` |
| `Arg10` | `+ 0x0` | `64` | `W` |
| `Arg11` | `+ 0x0` | `32` | `R/W` |
| `Arg12` | `+ 0x10` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0046F9C4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
