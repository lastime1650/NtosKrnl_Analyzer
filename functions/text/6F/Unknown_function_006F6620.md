# sub_006F6620

- RVA: `0x006F6620`–`0x006F6C53` (길이 `1,587` bytes)
- VA: `0x00000001406F6620`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B16B4`
- 디코드: `395`개 명령, `1,587/1,587` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **18**; 고유 호출 대상: **9**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **22**

### Outgoing calls
- `0x006F6686` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x006F66F5` → [PpmParkFindOverUtilizedProcessors](../2D/PpmParkFindOverUtilizedProcessors_function_002D86B8.md) (function, `0x002D86B8`)
- `0x006F67A7` → [KeGetPrcb](../2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x006F67BB` → [KeEnumerateNextProcessor](../41/KeEnumerateNextProcessor_function_00415480.md) (function, `0x00415480`)
- `0x006F6805` → [KeGetPrcb](../2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x006F683F` → [KeEnumerateNextProcessor](../41/KeEnumerateNextProcessor_function_00415480.md) (function, `0x00415480`)
- `0x006F6853` → [KeGetPrcb](../2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x006F688C` → [KeEnumerateNextProcessor](../41/KeEnumerateNextProcessor_function_00415480.md) (function, `0x00415480`)
- `0x006F68A8` → [KeCpuSetQueryUnparkRecommendation](../48/KeCpuSetQueryUnparkRecommendation_function_00483874.md) (function, `0x00483874`)
- `0x006F68E6` → [KeEnumerateNextProcessor](../41/KeEnumerateNextProcessor_function_00415480.md) (function, `0x00415480`)
- `0x006F68F2` → [KeGetPrcb](../2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x006F6906` → [KeEnumerateNextProcessor](../41/KeEnumerateNextProcessor_function_00415480.md) (function, `0x00415480`)
- `0x006F6936` → [KeGetPrcb](../2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x006F6975` → [KeEnumerateNextProcessor](../41/KeEnumerateNextProcessor_function_00415480.md) (function, `0x00415480`)
- `0x006F6B62` → [PpmParkComputeUnparkMask](../46/PpmParkComputeUnparkMask_function_0046F9C4.md) (function, `0x0046F9C4`)
- `0x006F6BC8` → [PpmEventTraceSoftCoreParkingSelection](../47/PpmEventTraceSoftCoreParkingSelection_function_0047D4EC.md) (function, `0x0047D4EC`)
- `0x006F6C0C` → [PpmParkComputeDiff](../4A/PpmParkComputeDiff_function_004ADCAC.md) (function, `0x004ADCAC`)
- `0x006F6C46` → [PpmEventLPICoreParking](../5D/PpmEventLPICoreParking_function_005DAE1C.md) (function, `0x005DAE1C`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006F6620` → RVA `0x00F083D0` (`.data`; read)
- `0x006F6633` → RVA `0x00E08380` (`.data`; read)
- `0x006F663A` → RVA `0x00F0CE0C` (`.data`; read)
- `0x006F6641` → RVA `0x00F083C8` (`.data`; read)
- `0x006F664F` → RVA `0x00F083B0` (`.data`; write)
- `0x006F6659` → RVA `0x00F083C0` (`.data`; write)
- `0x006F6676` → RVA `0x00FC6AE8` (`ALMOSTRO`; read)
- `0x006F668E` → RVA `0x00F083E0` (`.data`; read)
- `0x006F66AC` → RVA `0x00F083D8` (`.data`; read)
- `0x006F6709` → RVA `0x00FC50B8` (`ALMOSTRO`; read)
- `0x006F677B` → RVA `0x00F083A2` (`.data`; read)
- `0x006F67EF` → RVA `0x00FC6ABF` (`ALMOSTRO`; read)
- `0x006F67FC` → RVA `0x00F21FB0` (`.data`; read)
- `0x006F69CA` → RVA `0x00FC501C` (`ALMOSTRO`; read)
- `0x006F69FD` → RVA `0x00F0B24C` (`.data`; read)
- `0x006F6A9F` → RVA `0x00FC6AF1` (`ALMOSTRO`; read)
- `0x006F6AD8` → RVA `0x00FC6A86` (`ALMOSTRO`; read)
- `0x006F6C11` → RVA `0x00E67A40` (`.data`; read)
- `0x006F6C1E` → RVA `0x00E67A3C` (`.data`; read)
- `0x006F6C26` → RVA `0x00E67A48` (`.data`; read)
- `0x006F6C35` → RVA `0x00E67A3C` (`.data`; write)
- `0x006F6C3B` → RVA `0x00E67A48` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006F6C4E` → [PpmParkCalculateCoreParkingMask + 0x4F](../48/PpmParkCalculateCoreParkingMask_function_0048E5F0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006F6620  44 39 25 A9 1D 81 00            cmp dword ptr [rip + 0x811da9], r12d
006F6627  41 BD 01 00 00 00               mov r13d, 1
006F662D  0F 84 18 06 00 00               je 0x1406f6c4b
006F6633  48 8B 15 46 1D 71 00            mov rdx, qword ptr [rip + 0x711d46]
006F663A  48 63 05 CB 67 81 00            movsxd rax, dword ptr [rip + 0x8167cb]
006F6641  48 8B 0D 80 1D 81 00            mov rcx, qword ptr [rip + 0x811d80]
006F6648  48 69 C0 E8 01 00 00            imul rax, rax, 0x1e8
006F664F  44 89 25 5A 1D 81 00            mov dword ptr [rip + 0x811d5a], r12d
006F6656  48 03 C2                        add rax, rdx
006F6659  44 88 25 60 1D 81 00            mov byte ptr [rip + 0x811d60], r12b
006F6660  48 89 45 07                     mov qword ptr [rbp + 7], rax
006F6664  0F B6 80 B4 00 00 00            movzx eax, byte ptr [rax + 0xb4]
006F666B  6B D0 64                        imul edx, eax, 0x64
006F666E  89 55 CB                        mov dword ptr [rbp - 0x35], edx
006F6671  48 85 C9                        test rcx, rcx
006F6674  74 18                           je 0x1406f668e
006F6676  44 8B 05 6B 04 8D 00            mov r8d, dword ptr [rip + 0x8d046b]
006F667D  BA FF 00 00 00                  mov edx, 0xff
006F6682  49 C1 E0 02                     shl r8, 2
006F6686  E8 B5 05 FD FF                  call 0x1406c6c40
006F668B  8B 55 CB                        mov edx, dword ptr [rbp - 0x35]
006F668E  44 39 25 4B 1D 81 00            cmp dword ptr [rip + 0x811d4b], r12d
006F6695  45 8B F4                        mov r14d, r12d
006F6698  44 89 65 C7                     mov dword ptr [rbp - 0x39], r12d
006F669C  0F 84 6A 05 00 00               je 0x1406f6c0c
006F66A2  41 8B C6                        mov eax, r14d
006F66A5  48 69 F8 10 05 00 00            imul rdi, rax, 0x510
006F66AC  48 03 3D 25 1D 81 00            add rdi, qword ptr [rip + 0x811d25]
006F66B3  44 84 AF A0 04 00 00            test byte ptr [rdi + 0x4a0], r13b
006F66BA  0F 85 35 05 00 00               jne 0x1406f6bf5
006F66C0  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
006F66C4  48 8B CF                        mov rcx, rdi
006F66C7  44 0F B7 BF 92 04 00 00         movzx r15d, word ptr [rdi + 0x492]
006F66CF  48 89 47 20                     mov qword ptr [rdi + 0x20], rax
006F66D3  0F B7 87 96 04 00 00            movzx eax, word ptr [rdi + 0x496]
006F66DA  66 44 3B F8                     cmp r15w, ax
006F66DE  66 44 89 A7 E4 04 00 00         mov word ptr [rdi + 0x4e4], r12w
006F66E6  44 88 A7 E6 04 00 00            mov byte ptr [rdi + 0x4e6], r12b
006F66ED  44 0F 43 F8                     cmovae r15d, eax
006F66F1  44 89 7D A7                     mov dword ptr [rbp - 0x59], r15d
006F66F5  E8 BE 1F BE FF                  call 0x1402d86b8
006F66FA  4C 8D 8F B8 04 00 00            lea r9, [rdi + 0x4b8]
006F6701  48 89 45 0F                     mov qword ptr [rbp + 0xf], rax
006F6705  45 88 61 10                     mov byte ptr [r9 + 0x10], r12b
006F6709  8B 0D A9 E9 8C 00               mov ecx, dword ptr [rip + 0x8ce9a9]
006F670F  85 C9                           test ecx, ecx
006F6711  74 2A                           je 0x1406f673d
006F6713  4C 69 C1 10 27 00 00            imul r8, rcx, 0x2710
006F671A  33 D2                           xor edx, edx
006F671C  48 B8 08 00 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000008
006F6726  48 8B 00                        mov rax, qword ptr [rax]
006F6729  49 F7 F0                        div r8
006F672C  49 89 01                        mov qword ptr [r9], rax
006F672F  49 3B 41 08                     cmp rax, qword ptr [r9 + 8]
006F6733  74 08                           je 0x1406f673d
006F6735  45 88 69 10                     mov byte ptr [r9 + 0x10], r13b
006F6739  49 89 41 08                     mov qword ptr [r9 + 8], rax
006F673D  41 8B DC                        mov ebx, r12d
006F6740  89 5D 7F                        mov dword ptr [rbp + 0x7f], ebx
006F6743  44 38 67 0C                     cmp byte ptr [rdi + 0xc], r12b
006F6747  0F 86 A8 04 00 00               jbe 0x1406f6bf5
006F674D  48 8D 77 04                     lea rsi, [rdi + 4]
006F6751  8B C3                           mov eax, ebx
006F6753  48 89 75 FF                     mov qword ptr [rbp - 1], rsi
006F6757  48 8D 1C 80                     lea rbx, [rax + rax*4]
006F675B  48 C1 E3 07                     shl rbx, 7
006F675F  48 03 9F 08 05 00 00            add rbx, qword ptr [rdi + 0x508]
006F6766  44 89 65 6F                     mov dword ptr [rbp + 0x6f], r12d
006F676A  4C 8B 73 18                     mov r14, qword ptr [rbx + 0x18]
006F676E  4C 89 75 DF                     mov qword ptr [rbp - 0x21], r14
006F6772  4D 85 F6                        test r14, r14
006F6775  0F 84 76 04 00 00               je 0x1406f6bf1
006F677B  66 44 39 2D 1F 1C 81 00         cmp word ptr [rip + 0x811c1f], r13w
006F6783  C7 45 6F 00 00 10 00            mov dword ptr [rbp + 0x6f], 0x100000
006F678A  76 3A                           jbe 0x1406f67c6
006F678C  0F B7 06                        movzx eax, word ptr [rsi]
006F678F  4D 8B EC                        mov r13, r12
006F6792  66 89 45 BF                     mov word ptr [rbp - 0x41], ax
006F6796  48 8B 43 20                     mov rax, qword ptr [rbx + 0x20]
006F679A  48 89 45 B7                     mov qword ptr [rbp - 0x49], rax
006F679E  4C 89 65 AF                     mov qword ptr [rbp - 0x51], r12
006F67A2  EB 0F                           jmp 0x1406f67b3
006F67A4  8B 4D 77                        mov ecx, dword ptr [rbp + 0x77]
006F67A7  E8 24 1E BE FF                  call 0x1402d85d0
006F67AC  4C 0B A8 60 8E 00 00            or r13, qword ptr [rax + 0x8e60]
006F67B3  48 8D 55 AF                     lea rdx, [rbp - 0x51]
006F67B7  48 8D 4D 77                     lea rcx, [rbp + 0x77]
006F67BB  E8 C0 EC D1 FF                  call 0x140415480
006F67C0  85 C0                           test eax, eax
006F67C2  74 E0                           je 0x1406f67a4
006F67C4  EB 04                           jmp 0x1406f67ca
006F67C6  4C 8B 6B 20                     mov r13, qword ptr [rbx + 0x20]
006F67CA  4D 23 EE                        and r13, r14
006F67CD  74 05                           je 0x1406f67d4
006F67CF  0F BA 6D 6F 10                  bts dword ptr [rbp + 0x6f], 0x10
006F67D4  0F B7 0B                        movzx ecx, word ptr [rbx]
006F67D7  45 8B F7                        mov r14d, r15d
006F67DA  F3 49 0F B8 C5                  popcnt rax, r13
006F67DF  2B C8                           sub ecx, eax
006F67E1  4C 89 65 D7                     mov qword ptr [rbp - 0x29], r12
006F67E5  41 3B CF                        cmp ecx, r15d
006F67E8  45 8B FC                        mov r15d, r12d
006F67EB  44 0F 46 F1                     cmovbe r14d, ecx
006F67EF  80 3D C9 02 8D 00 00            cmp byte ptr [rip + 0x8d02c9], 0
006F67F6  0F 85 A1 00 00 00               jne 0x1406f689d
006F67FC  8B 0D AE B7 82 00               mov ecx, dword ptr [rip + 0x82b7ae]
006F6802  89 4D 77                        mov dword ptr [rbp + 0x77], ecx
006F6805  E8 C6 1D BE FF                  call 0x1402d85d0
006F680A  0F B7 16                        movzx edx, word ptr [rsi]
006F680D  0F B6 88 D0 00 00 00            movzx ecx, byte ptr [rax + 0xd0]
006F6814  66 3B CA                        cmp cx, dx
006F6817  0F 85 80 00 00 00               jne 0x1406f689d
006F681D  48 8B 80 C8 00 00 00            mov rax, qword ptr [rax + 0xc8]
006F6824  48 85 45 DF                     test qword ptr [rbp - 0x21], rax
006F6828  74 73                           je 0x1406f689d
006F682A  48 83 65 AF 00                  and qword ptr [rbp - 0x51], 0
006F682F  48 8D 4D 77                     lea rcx, [rbp + 0x77]
006F6833  66 89 55 BF                     mov word ptr [rbp - 0x41], dx
006F6837  48 8D 55 AF                     lea rdx, [rbp - 0x51]
006F683B  48 89 45 B7                     mov qword ptr [rbp - 0x49], rax
006F683F  E8 3C EC D1 FF                  call 0x140415480
006F6844  85 C0                           test eax, eax
006F6846  75 55                           jne 0x1406f689d
006F6848  8D 70 01                        lea esi, [rax + 1]
006F684B  45 3B FE                        cmp r15d, r14d
006F684E  73 45                           jae 0x1406f6895
006F6850  8B 4D 77                        mov ecx, dword ptr [rbp + 0x77]
006F6853  E8 78 1D BE FF                  call 0x1402d85d0
006F6858  48 8B 88 C8 00 00 00            mov rcx, qword ptr [rax + 0xc8]
006F685F  49 85 CD                        test r13, rcx
006F6862  75 20                           jne 0x1406f6884
006F6864  66 39 35 37 1B 81 00            cmp word ptr [rip + 0x811b37], si
006F686B  76 07                           jbe 0x1406f6874
006F686D  48 8B 88 60 8E 00 00            mov rcx, qword ptr [rax + 0x8e60]
006F6874  0F BA 6D 6F 08                  bts dword ptr [rbp + 0x6f], 8
006F6879  49 0B CC                        or rcx, r12
006F687C  4C 8B E1                        mov r12, rcx
006F687F  F3 4C 0F B8 F9                  popcnt r15, rcx
006F6884  48 8D 55 AF                     lea rdx, [rbp - 0x51]
006F6888  48 8D 4D 77                     lea rcx, [rbp + 0x77]
006F688C  E8 EF EB D1 FF                  call 0x140415480
006F6891  85 C0                           test eax, eax
006F6893  74 B6                           je 0x1406f684b
006F6895  48 8B 75 FF                     mov rsi, qword ptr [rbp - 1]
006F6899  4C 89 65 D7                     mov qword ptr [rbp - 0x29], r12
006F689D  0F B7 0E                        movzx ecx, word ptr [rsi]
006F68A0  4C 8D 45 CF                     lea r8, [rbp - 0x31]
006F68A4  48 8B 55 DF                     mov rdx, qword ptr [rbp - 0x21]
006F68A8  E8 C7 CF D8 FF                  call 0x140483874
006F68AD  4C 8B 65 CF                     mov r12, qword ptr [rbp - 0x31]
006F68B1  0F B6 C0                        movzx eax, al
006F68B4  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
006F68B8  85 C0                           test eax, eax
006F68BA  0F 84 BE 00 00 00               je 0x1406f697e
006F68C0  B8 01 00 00 00                  mov eax, 1
006F68C5  66 39 05 D6 1A 81 00            cmp word ptr [rip + 0x811ad6], ax
006F68CC  76 4E                           jbe 0x1406f691c
006F68CE  0F B7 06                        movzx eax, word ptr [rsi]
006F68D1  48 8D 55 AF                     lea rdx, [rbp - 0x51]
006F68D5  48 83 65 AF 00                  and qword ptr [rbp - 0x51], 0
006F68DA  48 8D 4D 77                     lea rcx, [rbp + 0x77]
006F68DE  66 89 45 BF                     mov word ptr [rbp - 0x41], ax
006F68E2  4C 89 65 B7                     mov qword ptr [rbp - 0x49], r12
006F68E6  E8 95 EB D1 FF                  call 0x140415480
006F68EB  85 C0                           test eax, eax
006F68ED  75 24                           jne 0x1406f6913
006F68EF  8B 4D 77                        mov ecx, dword ptr [rbp + 0x77]
006F68F2  E8 D9 1C BE FF                  call 0x1402d85d0
006F68F7  48 8D 55 AF                     lea rdx, [rbp - 0x51]
006F68FB  48 8D 4D 77                     lea rcx, [rbp + 0x77]
006F68FF  4C 0B A0 60 8E 00 00            or r12, qword ptr [rax + 0x8e60]
006F6906  E8 75 EB D1 FF                  call 0x140415480
006F690B  85 C0                           test eax, eax
006F690D  74 E0                           je 0x1406f68ef
006F690F  4C 89 65 CF                     mov qword ptr [rbp - 0x31], r12
006F6913  F3 49 0F B8 C4                  popcnt rax, r12
006F6918  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
006F691C  0F B7 06                        movzx eax, word ptr [rsi]
006F691F  48 83 65 AF 00                  and qword ptr [rbp - 0x51], 0
006F6924  66 89 45 BF                     mov word ptr [rbp - 0x41], ax
006F6928  4C 89 65 B7                     mov qword ptr [rbp - 0x49], r12
006F692C  EB 3F                           jmp 0x1406f696d
006F692E  45 3B FE                        cmp r15d, r14d
006F6931  73 4B                           jae 0x1406f697e
006F6933  8B 4D 77                        mov ecx, dword ptr [rbp + 0x77]
006F6936  E8 95 1C BE FF                  call 0x1402d85d0
006F693B  48 8B 88 C8 00 00 00            mov rcx, qword ptr [rax + 0xc8]
006F6942  49 85 CD                        test r13, rcx
006F6945  75 26                           jne 0x1406f696d
006F6947  BA 01 00 00 00                  mov edx, 1
006F694C  66 39 15 4F 1A 81 00            cmp word ptr [rip + 0x811a4f], dx
006F6953  76 07                           jbe 0x1406f695c
006F6955  48 8B 88 60 8E 00 00            mov rcx, qword ptr [rax + 0x8e60]
006F695C  48 0B 4D D7                     or rcx, qword ptr [rbp - 0x29]
006F6960  83 4D 6F 10                     or dword ptr [rbp + 0x6f], 0x10
006F6964  48 89 4D D7                     mov qword ptr [rbp - 0x29], rcx
006F6968  F3 4C 0F B8 F9                  popcnt r15, rcx
006F696D  48 8D 55 AF                     lea rdx, [rbp - 0x51]
006F6971  48 8D 4D 77                     lea rcx, [rbp + 0x77]
006F6975  E8 06 EB D1 FF                  call 0x140415480
006F697A  85 C0                           test eax, eax
006F697C  74 B0                           je 0x1406f692e
006F697E  0F B7 4B 02                     movzx ecx, word ptr [rbx + 2]
006F6982  44 3B F9                        cmp r15d, ecx
006F6985  73 1D                           jae 0x1406f69a4
006F6987  45 3B FE                        cmp r15d, r14d
006F698A  73 18                           jae 0x1406f69a4
006F698C  44 8B 45 6F                     mov r8d, dword ptr [rbp + 0x6f]
006F6990  41 3B CE                        cmp ecx, r14d
006F6993  45 8B FE                        mov r15d, r14d
006F6996  44 0F 42 F9                     cmovb r15d, ecx
006F699A  41 83 C8 04                     or r8d, 4
006F699E  44 89 45 6F                     mov dword ptr [rbp + 0x6f], r8d
006F69A2  EB 04                           jmp 0x1406f69a8
006F69A4  44 8B 45 6F                     mov r8d, dword ptr [rbp + 0x6f]
006F69A8  0F B7 43 04                     movzx eax, word ptr [rbx + 4]
006F69AC  41 8B F6                        mov esi, r14d
006F69AF  44 3B F0                        cmp r14d, eax
006F69B2  76 16                           jbe 0x1406f69ca
006F69B4  45 3B FE                        cmp r15d, r14d
006F69B7  73 11                           jae 0x1406f69ca
006F69B9  41 83 C8 08                     or r8d, 8
006F69BD  8B F0                           mov esi, eax
006F69BF  41 3B C7                        cmp eax, r15d
006F69C2  44 89 45 6F                     mov dword ptr [rbp + 0x6f], r8d
006F69C6  41 0F 46 F7                     cmovbe esi, r15d
006F69CA  44 8B 35 4B E6 8C 00            mov r14d, dword ptr [rip + 0x8ce64b]
006F69D1  45 32 D2                        xor r10b, r10b
006F69D4  41 83 E6 08                     and r14d, 8
006F69D8  74 10                           je 0x1406f69ea
006F69DA  48 8B 8F 00 05 00 00            mov rcx, qword ptr [rdi + 0x500]
006F69E1  48 63 41 04                     movsxd rax, dword ptr [rcx + 4]
006F69E5  44 8A 54 41 08                  mov r10b, byte ptr [rcx + rax*2 + 8]
006F69EA  0F B7 03                        movzx eax, word ptr [rbx]
006F69ED  44 0F B7 5B 06                  movzx r11d, word ptr [rbx + 6]
006F69F2  66 44 3B D8                     cmp r11w, ax
006F69F6  89 45 67                        mov dword ptr [rbp + 0x67], eax
006F69F9  44 0F 43 D8                     cmovae r11d, eax
006F69FD  83 3D 48 48 81 00 00            cmp dword ptr [rip + 0x814848], 0
006F6A04  45 8B CB                        mov r9d, r11d
006F6A07  74 38                           je 0x1406f6a41
006F6A09  8B 45 7F                        mov eax, dword ptr [rbp + 0x7f]
006F6A0C  F7 D8                           neg eax
006F6A0E  48 8B 45 07                     mov rax, qword ptr [rbp + 7]
006F6A12  48 1B C9                        sbb rcx, rcx
006F6A15  48 F7 D9                        neg rcx
006F6A18  0F B6 94 01 89 00 00 00         movzx edx, byte ptr [rcx + rax + 0x89]
006F6A20  B8 1F 85 EB 51                  mov eax, 0x51eb851f
006F6A25  0F AF 55 67                     imul edx, dword ptr [rbp + 0x67]
006F6A29  83 C2 32                        add edx, 0x32
006F6A2C  F7 E2                           mul edx
006F6A2E  C1 EA 05                        shr edx, 5
006F6A31  41 3B D3                        cmp edx, r11d
006F6A34  76 0B                           jbe 0x1406f6a41
006F6A36  41 83 C8 40                     or r8d, 0x40
006F6A3A  44 8B CA                        mov r9d, edx
006F6A3D  44 89 45 6F                     mov dword ptr [rbp + 0x6f], r8d
006F6A41  0F B7 05 5A 19 81 00            movzx eax, word ptr [rip + 0x81195a]
006F6A48  B9 01 00 00 00                  mov ecx, 1
006F6A4D  66 3B C1                        cmp ax, cx
006F6A50  76 11                           jbe 0x1406f6a63
006F6A52  8B C8                           mov ecx, eax
006F6A54  33 D2                           xor edx, edx
006F6A56  FF C8                           dec eax
006F6A58  44 03 C8                        add r9d, eax
006F6A5B  41 8B C1                        mov eax, r9d
006F6A5E  F7 F1                           div ecx
006F6A60  44 2B CA                        sub r9d, edx
006F6A63  45 85 F6                        test r14d, r14d
006F6A66  74 17                           je 0x1406f6a7f
006F6A68  45 84 D2                        test r10b, r10b
006F6A6B  74 12                           je 0x1406f6a7f
006F6A6D  45 3A D1                        cmp r10b, r9b
006F6A70  73 0D                           jae 0x1406f6a7f
006F6A72  41 0F BA E8 16                  bts r8d, 0x16
006F6A77  45 0F B6 CA                     movzx r9d, r10b
006F6A7B  44 89 45 6F                     mov dword ptr [rbp + 0x6f], r8d
006F6A7F  41 0F B6 C1                     movzx eax, r9b
006F6A83  41 8B CF                        mov ecx, r15d
006F6A86  66 89 43 08                     mov word ptr [rbx + 8], ax
006F6A8A  48 8B 45 EF                     mov rax, qword ptr [rbp - 0x11]
006F6A8E  41 03 C1                        add eax, r9d
006F6A91  3B C6                           cmp eax, esi
006F6A93  0F 43 C6                        cmovae eax, esi
006F6A96  41 3B C7                        cmp eax, r15d
006F6A99  0F 47 C8                        cmova ecx, eax
006F6A9C  29 75 A7                        sub dword ptr [rbp - 0x59], esi
006F6A9F  80 3D 4B 00 8D 00 00            cmp byte ptr [rip + 0x8d004b], 0
006F6AA6  0F B6 C1                        movzx eax, cl
006F6AA9  66 89 45 67                     mov word ptr [rbp + 0x67], ax
006F6AAD  66 89 43 0A                     mov word ptr [rbx + 0xa], ax
006F6AB1  75 09                           jne 0x1406f6abc
006F6AB3  0F BA 6D 6F 15                  bts dword ptr [rbp + 0x6f], 0x15
006F6AB8  8B F1                           mov esi, ecx
006F6ABA  EB 15                           jmp 0x1406f6ad1
006F6ABC  45 85 F6                        test r14d, r14d
006F6ABF  74 10                           je 0x1406f6ad1
006F6AC1  0F BA 6D 6F 17                  bts dword ptr [rbp + 0x6f], 0x17
006F6AC6  41 0F B6 C2                     movzx eax, r10b
006F6ACA  3B F0                           cmp esi, eax
006F6ACC  0F 42 C6                        cmovb eax, esi
006F6ACF  8B F0                           mov esi, eax
006F6AD1  45 33 F6                        xor r14d, r14d
006F6AD4  32 C0                           xor al, al
006F6AD6  32 D2                           xor dl, dl
006F6AD8  38 05 A8 FF 8C 00               cmp byte ptr [rip + 0x8cffa8], al
006F6ADE  74 14                           je 0x1406f6af4
006F6AE0  44 0F B7 B7 F0 04 00 00         movzx r14d, word ptr [rdi + 0x4f0]
006F6AE8  8A 87 F7 04 00 00               mov al, byte ptr [rdi + 0x4f7]
006F6AEE  8A 97 F6 04 00 00               mov dl, byte ptr [rdi + 0x4f6]
006F6AF4  4C 8B 55 DF                     mov r10, qword ptr [rbp - 0x21]
006F6AF8  44 8B 4D 7F                     mov r9d, dword ptr [rbp + 0x7f]
006F6AFC  49 8B DA                        mov rbx, r10
006F6AFF  4C 8B 47 20                     mov r8, qword ptr [rdi + 0x20]
006F6B03  48 23 5D 0F                     and rbx, qword ptr [rbp + 0xf]
006F6B07  4D 23 C2                        and r8, r10
006F6B0A  44 89 4C 24 78                  mov dword ptr [rsp + 0x78], r9d
006F6B0F  4C 8B CB                        mov r9, rbx
006F6B12  88 44 24 70                     mov byte ptr [rsp + 0x70], al
006F6B16  48 8D 87 B8 04 00 00            lea rax, [rdi + 0x4b8]
006F6B1D  88 54 24 68                     mov byte ptr [rsp + 0x68], dl
006F6B21  49 8B D2                        mov rdx, r10
006F6B24  44 89 74 24 60                  mov dword ptr [rsp + 0x60], r14d
006F6B29  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
006F6B2E  48 8D 45 6F                     lea rax, [rbp + 0x6f]
006F6B32  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
006F6B37  48 8D 45 E7                     lea rax, [rbp - 0x19]
006F6B3B  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
006F6B40  48 8D 45 F7                     lea rax, [rbp - 9]
006F6B44  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
006F6B49  48 8B 45 D7                     mov rax, qword ptr [rbp - 0x29]
006F6B4D  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
006F6B52  4C 89 6C 24 30                  mov qword ptr [rsp + 0x30], r13
006F6B57  89 74 24 28                     mov dword ptr [rsp + 0x28], esi
006F6B5B  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
006F6B5F  48 8B CF                        mov rcx, rdi
006F6B62  E8 5D 8E D7 FF                  call 0x14046f9c4
006F6B67  48 8B 4D DF                     mov rcx, qword ptr [rbp - 0x21]
006F6B6B  44 8A CE                        mov r9b, sil
006F6B6E  44 8A 45 67                     mov r8b, byte ptr [rbp + 0x67]
006F6B72  48 F7 D1                        not rcx
006F6B75  44 89 74 24 50                  mov dword ptr [rsp + 0x50], r14d
006F6B7A  48 8B C1                        mov rax, rcx
006F6B7D  48 23 47 18                     and rax, qword ptr [rdi + 0x18]
006F6B81  48 0B 45 E7                     or rax, qword ptr [rbp - 0x19]
006F6B85  48 0B 45 F7                     or rax, qword ptr [rbp - 9]
006F6B89  48 89 47 18                     mov qword ptr [rdi + 0x18], rax
006F6B8D  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
006F6B91  48 23 C1                        and rax, rcx
006F6B94  48 8B CF                        mov rcx, rdi
006F6B97  48 0B 45 E7                     or rax, qword ptr [rbp - 0x19]
006F6B9B  48 89 47 28                     mov qword ptr [rdi + 0x28], rax
006F6B9F  8B 45 6F                        mov eax, dword ptr [rbp + 0x6f]
006F6BA2  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
006F6BA6  48 8B 45 D7                     mov rax, qword ptr [rbp - 0x29]
006F6BAA  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
006F6BAF  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
006F6BB4  8B 5D 7F                        mov ebx, dword ptr [rbp + 0x7f]
006F6BB7  8B D3                           mov edx, ebx
006F6BB9  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
006F6BBE  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
006F6BC3  44 88 7C 24 20                  mov byte ptr [rsp + 0x20], r15b
006F6BC8  E8 1F 69 D8 FF                  call 0x14047d4ec
006F6BCD  0F B6 47 0C                     movzx eax, byte ptr [rdi + 0xc]
006F6BD1  41 BD 01 00 00 00               mov r13d, 1
006F6BD7  48 8B 75 FF                     mov rsi, qword ptr [rbp - 1]
006F6BDB  41 03 DD                        add ebx, r13d
006F6BDE  44 8B 7D A7                     mov r15d, dword ptr [rbp - 0x59]
006F6BE2  89 5D 7F                        mov dword ptr [rbp + 0x7f], ebx
006F6BE5  45 8D 65 FF                     lea r12d, [r13 - 1]
006F6BE9  3B D8                           cmp ebx, eax
006F6BEB  0F 82 60 FB FF FF               jb 0x1406f6751
006F6BF1  44 8B 75 C7                     mov r14d, dword ptr [rbp - 0x39]
006F6BF5  8B 55 CB                        mov edx, dword ptr [rbp - 0x35]
006F6BF8  45 03 F5                        add r14d, r13d
006F6BFB  44 3B 35 DE 17 81 00            cmp r14d, dword ptr [rip + 0x8117de]
006F6C02  44 89 75 C7                     mov dword ptr [rbp - 0x39], r14d
006F6C06  0F 82 96 FA FF FF               jb 0x1406f66a2
006F6C0C  E8 9B 70 DB FF                  call 0x1404adcac
006F6C11  44 39 25 28 0E 77 00            cmp dword ptr [rip + 0x770e28], r12d
006F6C18  41 8B D4                        mov edx, r12d
006F6C1B  0F 97 C2                        seta dl
006F6C1E  39 15 18 0E 77 00               cmp dword ptr [rip + 0x770e18], edx
006F6C24  75 0C                           jne 0x1406f6c32
006F6C26  44 39 25 1B 0E 77 00            cmp dword ptr [rip + 0x770e1b], r12d
006F6C2D  41 8B C4                        mov eax, r12d
006F6C30  74 03                           je 0x1406f6c35
006F6C32  41 8B C5                        mov eax, r13d
006F6C35  89 15 01 0E 77 00               mov dword ptr [rip + 0x770e01], edx
006F6C3B  44 89 25 06 0E 77 00            mov dword ptr [rip + 0x770e06], r12d
006F6C42  85 C0                           test eax, eax
006F6C44  74 05                           je 0x1406f6c4b
006F6C46  E8 D1 41 EE FF                  call 0x1405dae1c
006F6C4B  41 8A C5                        mov al, r13b
006F6C4E  E9 EC 79 D9 FF                  jmp 0x14048e63f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006F6620(void)
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
    unsigned int v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned int v_stack_p60;
    unsigned __int8 v_stack_p68;
    unsigned __int8 v_stack_p70;
    unsigned int v_stack_p78;

    if ((*(unsigned int *)(v_rip + 8461737)) == ((unsigned int)(v_r12))) goto loc_006F6C4B;
    result = ((int)(*(unsigned int *)(v_rip + 8480715))) * ((int)(*(unsigned int *)(v_rip + 8480715)));
    *(unsigned int *)(v_rip + 8461658) = (unsigned int)(v_r12);
    result = (result) + (*(unsigned __int64 *)(v_rip + 7413062));
    *(unsigned __int8 *)(v_rip + 8461664) = (unsigned __int8)(v_r12);
    *(unsigned __int64 *)(v_rbp + 7) = result;
    a2 = (unsigned int)((*(unsigned __int64 *)(v_rip + 7413062)) * ((unsigned int)(*(unsigned __int8 *)(result + 180))));
    *(unsigned int *)(v_rbp - 53) = (unsigned int)(a2);
    result = *(unsigned __int8 *)(result + 180);
    if (*(unsigned __int64 *)(v_rip + 8461696) != 0) {
        a3 = *(unsigned int *)(v_rip + 9241707);
        a2 = 255;
        a3 = (a3) << (2);
        result = memset(*(unsigned __int64 *)(v_rip + 8461696), a2, a3, a4);
        a2 = *(unsigned int *)(v_rbp - 53);
    }
    *(unsigned int *)(v_rbp - 57) = (unsigned int)(v_r12);
    if ((*(unsigned int *)(v_rip + 8461643)) == ((unsigned int)(v_r12))) goto loc_006F6C0C;
loc_006F66A2:
    v_rdi = (v_rdi) * ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))));
    v_rdi = (v_rdi) + (*(unsigned __int64 *)(v_rip + 8461605));
    if (((*(unsigned __int8 *)(v_rdi + 1184)) & (1)) != 0) goto loc_006F6BF5;
    *(unsigned __int64 *)(v_rdi + 32) = *(unsigned __int64 *)(v_rdi + 24);
    *(unsigned __int16 *)(v_rdi + 1252) = (unsigned __int16)(v_r12);
    *(unsigned __int8 *)(v_rdi + 1254) = (unsigned __int8)(v_r12);
    v_r15 = *(unsigned __int16 *)(v_rdi + 1170);
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rdi + 1170))) >= ((unsigned __int16)(*(unsigned __int16 *)(v_rdi + 1174)))) { v_r15 = (unsigned int)(*(unsigned __int16 *)(v_rdi + 1174)); }
    *(unsigned int *)(v_rbp - 89) = (unsigned int)(v_r15);
    result = PpmParkFindOverUtilizedProcessors(v_rdi, a2, a3, a4);
    *(unsigned __int64 *)(v_rbp + 15) = result;
    *(unsigned __int8 *)(v_rdi + 1208 + 16) = (unsigned __int8)(v_r12);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9234857))) == 0) goto loc_006F673D;
    a3 = (a3) * ((unsigned int)(*(unsigned int *)(v_rip + 9234857)));
    a2 = 0;
    *(unsigned __int64 *)(v_rdi + 1208) = *(unsigned __int64 *)(result);
    if ((*(unsigned __int64 *)(result)) != (*(unsigned __int64 *)(v_rdi + 1208 + 8))) {
        *(unsigned __int8 *)(v_rdi + 1208 + 16) = 1;
        *(unsigned __int64 *)(v_rdi + 1208 + 8) = *(unsigned __int64 *)(result);
    }
    *(unsigned int *)(v_rbp + 127) = (unsigned int)((unsigned int)((unsigned int)(v_r12)));
    if ((*(unsigned __int8 *)(v_rdi + 12)) <= ((unsigned __int8)(v_r12))) goto loc_006F6BF5;
loc_006F6751:
    *(unsigned __int64 *)(v_rbp - 1) = v_rdi + 4;
    v_rbx = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))) * 4) << (7);
    v_rbx = (v_rbx) + (*(unsigned __int64 *)(v_rdi + 1288));
    *(unsigned int *)(v_rbp + 111) = (unsigned int)(v_r12);
    *(unsigned __int64 *)(v_rbp - 33) = *(unsigned __int64 *)(v_rbx + 24);
    if (*(unsigned __int64 *)(v_rbx + 24) == 0) goto loc_006F6BF1;
    *(unsigned int *)(v_rbp + 111) = 0x100000ULL;
    if ((*(unsigned __int16 *)(v_rip + 8461343)) <= 1) goto loc_006F67C6;
    *(unsigned __int16 *)(v_rbp - 65) = (unsigned __int16)(*(unsigned __int16 *)(v_rdi + 4));
    *(unsigned __int64 *)(v_rbp - 73) = *(unsigned __int64 *)(v_rbx + 32);
    *(unsigned __int64 *)(v_rbp - 81) = v_r12;
    goto loc_006F67B3;
loc_006F67A4:
    result = KeGetPrcb((unsigned int)(*(unsigned int *)(v_rbp + 119)), a2, a3, v_rdi + 1208);
    v_r13 = (v_r12) | (*(unsigned __int64 *)(result + 36448));
loc_006F67B3:
    result = KeEnumerateNextProcessor(v_rbp + 119, v_rbp - 81, a3, v_rdi + 1208);
    if ((unsigned int)(result) == 0) goto loc_006F67A4;
    goto loc_006F67CA;
loc_006F67C6:
loc_006F67CA:
    v_r13 = (*(unsigned __int64 *)(v_rbx + 32)) & (*(unsigned __int64 *)(v_rbx + 24));
    if (!(condition_is_equal)) {
    }
    a1 = (unsigned int)((*(unsigned __int16 *)(v_rbx)) - ((unsigned int)(result)));
    *(unsigned __int64 *)(v_rbp - 41) = v_r12;
    v_r14 = (unsigned int)((unsigned int)(v_r15));
    if (((unsigned int)(a1)) <= ((unsigned int)(v_r15))) { v_r14 = (unsigned int)(a1); }
    if ((*(unsigned __int8 *)(v_rip + 9241289)) != 0) goto loc_006F689D;
    *(unsigned int *)(v_rbp + 119) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 8566702)));
    result = KeGetPrcb((unsigned int)(*(unsigned int *)(v_rip + 8566702)), v_rbp - 81, a3, v_rdi + 1208);
    if (((unsigned __int16)(*(unsigned __int8 *)(result + 208))) != ((unsigned __int16)(*(unsigned __int16 *)(v_rdi + 4)))) goto loc_006F689D;
    if (((*(unsigned __int64 *)(v_rbp - 33)) & (*(unsigned __int64 *)(result + 200))) == 0) goto loc_006F689D;
    *(unsigned __int16 *)(v_rbp - 65) = (unsigned __int16)(*(unsigned __int16 *)(v_rdi + 4));
    *(unsigned __int64 *)(v_rbp - 73) = *(unsigned __int64 *)(result + 200);
    result = KeEnumerateNextProcessor(v_rbp + 119, v_rbp - 81, a3, v_rdi + 1208);
    if ((unsigned int)(result) != 0) goto loc_006F689D;
loc_006F684B:
    if (((unsigned int)((unsigned int)((unsigned int)(v_r12)))) >= ((unsigned int)(v_r14))) goto loc_006F6895;
    result = KeGetPrcb((unsigned int)(*(unsigned int *)(v_rbp + 119)), v_rbp - 81, a3, v_rdi + 1208);
    if (((v_r13) & (*(unsigned __int64 *)(result + 200))) != 0) goto loc_006F6884;
    if ((*(unsigned __int16 *)(v_rip + 8461111)) >= = ((unsigned __int16)(result + 1))) {
        a1 = *(unsigned __int64 *)(result + 36448);
    }
    a1 = (a1) | (v_r12);
loc_006F6884:
    result = KeEnumerateNextProcessor(v_rbp + 119, v_rbp - 81, a3, v_rdi + 1208);
    if ((unsigned int)(result) == 0) goto loc_006F684B;
loc_006F6895:
    *(unsigned __int64 *)(v_rbp - 41) = a1;
loc_006F689D:
    result = KeCpuSetQueryUnparkRecommendation(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbp - 1)), *(unsigned __int64 *)(v_rbp - 33), v_rbp - 49, v_rdi + 1208);
    *(unsigned __int64 *)(v_rbp - 17) = (unsigned __int8)(result);
    if ((unsigned int)((unsigned __int8)(result)) == 0) goto loc_006F697E;
    if ((*(unsigned __int16 *)(v_rip + 8461014)) <= 1) goto loc_006F691C;
    *(unsigned __int16 *)(v_rbp - 65) = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbp - 1)));
    *(unsigned __int64 *)(v_rbp - 73) = *(unsigned __int64 *)(v_rbp - 49);
    result = KeEnumerateNextProcessor(v_rbp + 119, v_rbp - 81, v_rbp - 49, v_rdi + 1208);
    if ((unsigned int)(result) != 0) goto loc_006F6913;
loc_006F68EF:
    result = KeGetPrcb((unsigned int)(*(unsigned int *)(v_rbp + 119)), v_rbp - 81, v_rbp - 49, v_rdi + 1208);
    v_r12 = (*(unsigned __int64 *)(v_rbp - 49)) | (*(unsigned __int64 *)(result + 36448));
    result = KeEnumerateNextProcessor(v_rbp + 119, v_rbp - 81, v_rbp - 49, v_rdi + 1208);
    if ((unsigned int)(result) == 0) goto loc_006F68EF;
    *(unsigned __int64 *)(v_rbp - 49) = v_r12;
loc_006F6913:
    *(unsigned __int64 *)(v_rbp - 17) = result;
loc_006F691C:
    *(unsigned __int16 *)(v_rbp - 65) = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbp - 1)));
    *(unsigned __int64 *)(v_rbp - 73) = v_r12;
    goto loc_006F696D;
loc_006F692E:
    if (((unsigned int)((unsigned int)((unsigned int)(v_r12)))) >= ((unsigned int)(v_r14))) goto loc_006F697E;
    result = KeGetPrcb((unsigned int)(*(unsigned int *)(v_rbp + 119)), v_rbp - 81, v_rbp - 49, v_rdi + 1208);
    if (((v_r13) & (*(unsigned __int64 *)(result + 200))) != 0) goto loc_006F696D;
    if ((*(unsigned __int16 *)(v_rip + 8460879)) >= = 1) {
        a1 = *(unsigned __int64 *)(result + 36448);
    }
    a1 = (a1) | (*(unsigned __int64 *)(v_rbp - 41));
    *(unsigned __int64 *)(v_rbp - 41) = a1;
loc_006F696D:
    result = KeEnumerateNextProcessor(v_rbp + 119, v_rbp - 81, v_rbp - 49, v_rdi + 1208);
    if ((unsigned int)(result) == 0) goto loc_006F692E;
loc_006F697E:
    if (((unsigned int)((unsigned int)((unsigned int)(v_r12)))) >= ((unsigned int)(*(unsigned __int16 *)(v_rbx + 2)))) goto loc_006F69A4;
    if (((unsigned int)((unsigned int)((unsigned int)(v_r12)))) >= ((unsigned int)(v_r14))) goto loc_006F69A4;
    v_r15 = (unsigned int)((unsigned int)(v_r14));
    if (((unsigned int)(*(unsigned __int16 *)(v_rbx + 2))) < ((unsigned int)(v_r14))) { v_r15 = (unsigned int)(*(unsigned __int16 *)(v_rbx + 2)); }
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbp + 111))) | (4));
    *(unsigned int *)(v_rbp + 111) = (unsigned int)(a3);
    goto loc_006F69A8;
loc_006F69A4:
loc_006F69A8:
    if (((unsigned int)(v_r14)) <= ((unsigned int)(*(unsigned __int16 *)(v_rbx + 4)))) goto loc_006F69CA;
    v_rsi = (unsigned int)((unsigned int)(v_r14));
    if (((unsigned int)(v_r15)) < ((unsigned int)(v_r14))) {
        a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbp + 111))) | (8));
        v_rsi = (unsigned int)(*(unsigned __int16 *)(v_rbx + 4));
        *(unsigned int *)(v_rbp + 111) = (unsigned int)(a3);
        if (((unsigned int)(*(unsigned __int16 *)(v_rbx + 4))) <= ((unsigned int)(v_r15))) { v_rsi = (unsigned int)(v_r15); }
    }
    v_r10 = 0;
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 9233995))) & (8));
    result = *(unsigned __int16 *)(v_rbx + 4);
    if (!(condition_is_equal)) {
        a1 = *(unsigned __int64 *)(v_rdi + 1280);
        result = (int)(*(unsigned int *)(a1 + 4));
        v_r10 = *(unsigned __int8 *)(a1 + result * 2 + 8);
    }
    *(unsigned int *)(v_rbp + 103) = (unsigned int)(*(unsigned __int16 *)(v_rbx));
    v_r11 = *(unsigned __int16 *)(v_rbx + 6);
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rbx + 6))) >= ((unsigned __int16)(*(unsigned __int16 *)(v_rbx)))) { v_r11 = (unsigned int)(*(unsigned __int16 *)(v_rbx)); }
    if ((*(unsigned int *)(v_rip + 8472648)) == 0) goto loc_006F6A41;
    result = (unsigned int)(-((unsigned int)(*(unsigned int *)(v_rbp + 127))));
    a1 = -(a1);
    a2 = (unsigned int)((*(unsigned __int8 *)(a1 + *(unsigned __int64 *)(v_rbp + 7) * 1 + 137)) * (*(unsigned int *)(v_rbp + 103)));
    a2 = (unsigned int)((a2) + (50));
    a2 = (unsigned int)((a2) >> (5));
    if (((unsigned int)(a2)) >= = ((unsigned int)(v_r11))) {
        a3 = (unsigned int)((a3) | (64));
        a4 = (unsigned int)(a2);
        *(unsigned int *)(v_rbp + 111) = (unsigned int)(a3);
    }
    result = *(unsigned __int16 *)(v_rip + 8460634);
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rip + 8460634))) >= = 1) {
        a1 = (unsigned int)(*(unsigned __int16 *)(v_rip + 8460634));
        a2 = 0;
        result = (unsigned int)((*(unsigned __int16 *)(v_rip + 8460634)) - 1);
        a4 = (unsigned int)((a4) + ((unsigned int)(result)));
        result = (unsigned int)(a4);
        a4 = (unsigned int)((a4) - (0));
    }
    if ((unsigned int)(v_r14) == 0) goto loc_006F6A7F;
    if ((unsigned __int8)(v_r10) == 0) goto loc_006F6A7F;
    if (((unsigned __int8)(v_r10)) < ((unsigned __int8)(a4))) {
        a4 = (unsigned __int8)(v_r10);
        *(unsigned int *)(v_rbp + 111) = (unsigned int)(a3);
    }
    *(unsigned __int16 *)(v_rbx + 8) = (unsigned __int16)((unsigned __int8)(a4));
    result = (unsigned int)((*(unsigned __int64 *)(v_rbp - 17)) + ((unsigned int)(a4)));
    if (((unsigned int)(result)) >= ((unsigned int)(v_rsi))) { result = (unsigned int)(v_rsi); }
    a1 = (unsigned int)((unsigned int)(v_r15));
    if (((unsigned int)(result)) > ((unsigned int)(v_r15))) { a1 = (unsigned int)(result); }
    *(unsigned __int16 *)(v_rbp + 103) = (unsigned __int16)((unsigned __int8)(a1));
    *(unsigned __int16 *)(v_rbx + 10) = (unsigned __int16)((unsigned __int8)(a1));
    if ((*(unsigned __int8 *)(v_rip + 9240651)) != 0) goto loc_006F6ABC;
    goto loc_006F6AD1;
loc_006F6ABC:
    result = (unsigned __int8)(a1);
    v_rsi = (unsigned int)((unsigned int)(a1));
    if ((unsigned int)(v_r14) != 0) {
        result = (unsigned __int8)(v_r10);
        if (((unsigned int)((unsigned int)((unsigned int)(a1)))) < ((unsigned int)(result))) { result = (unsigned int)((unsigned int)((unsigned int)(a1))); }
        v_rsi = (unsigned int)(result);
    }
    v_r14 = 0;
    result = 0;
    a2 = 0;
    if ((*(unsigned __int8 *)(v_rip + 9240488)) != 0) {
        v_r14 = *(unsigned __int16 *)(v_rdi + 1264);
        result = *(unsigned __int8 *)(v_rdi + 1271);
        a2 = *(unsigned __int8 *)(v_rdi + 1270);
    }
    v_rbx = (*(unsigned __int64 *)(v_rbp - 33)) & (*(unsigned __int64 *)(v_rbp + 15));
    a3 = (*(unsigned __int64 *)(v_rdi + 32)) & (*(unsigned __int64 *)(v_rbp - 33));
    v_stack_p78 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbp + 127)));
    v_stack_p70 = (unsigned __int8)(result);
    v_stack_p68 = (unsigned __int8)(a2);
    v_stack_p60 = (unsigned int)(v_r14);
    v_stack_p58 = v_rdi + 1208;
    v_stack_p50 = v_rbp + 111;
    v_stack_p48 = v_rbp - 25;
    v_stack_p40 = v_rbp - 9;
    v_stack_p38 = *(unsigned __int64 *)(v_rbp - 41);
    v_stack_p30 = v_r13;
    v_stack_p28 = (unsigned int)(v_rsi);
    v_stack_p20 = (unsigned int)(a1);
    result = PpmParkComputeUnparkMask(v_rdi, *(unsigned __int64 *)(v_rbp - 33), a3, v_rbx);
    a1 = ~(*(unsigned __int64 *)(v_rbp - 33));
    v_stack_p50 = (unsigned int)(v_r14);
    result = (a1) & (*(unsigned __int64 *)(v_rdi + 24));
    result = (result) | (*(unsigned __int64 *)(v_rbp - 25));
    result = (result) | (*(unsigned __int64 *)(v_rbp - 9));
    *(unsigned __int64 *)(v_rdi + 24) = result;
    result = (*(unsigned __int64 *)(v_rdi + 40)) & (a1);
    result = (result) | (*(unsigned __int64 *)(v_rbp - 25));
    *(unsigned __int64 *)(v_rdi + 40) = result;
    v_stack_p48 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbp + 111)));
    v_stack_p40 = v_r12;
    v_stack_p38 = v_rbx;
    v_stack_p30 = *(unsigned __int64 *)(v_rbp - 41);
    v_stack_p28 = v_r13;
    v_stack_p20 = (unsigned __int8)(v_r15);
    result = PpmEventTraceSoftCoreParkingSelection(v_rdi, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rbp + 127)))), *(unsigned __int8 *)(v_rbp + 103), (unsigned __int8)(v_rsi));
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbp + 127))) + (1));
    *(unsigned int *)(v_rbp + 127) = (unsigned int)(v_rbx);
    if (((unsigned int)(v_rbx)) < ((unsigned int)(*(unsigned __int8 *)(v_rdi + 12)))) goto loc_006F6751;
loc_006F6BF1:
loc_006F6BF5:
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbp - 57))) + (1));
    *(unsigned int *)(v_rbp - 57) = (unsigned int)(v_r14);
    if (((unsigned int)(v_r14)) < (*(unsigned int *)(v_rip + 8460254))) goto loc_006F66A2;
loc_006F6C0C:
    result = PpmParkComputeDiff(v_rdi, (unsigned int)(*(unsigned int *)(v_rbp - 53)), *(unsigned __int8 *)(v_rbp + 103), (unsigned __int8)(v_rsi));
    a2 = ((*(unsigned int *)(v_rip + 7802408)) > ((unsigned int)(1 - 1))) ? 1 : 0;
    if ((*(unsigned int *)(v_rip + 7802392)) != ((unsigned int)(a2))) goto loc_006F6C32;
    result = (unsigned int)((unsigned int)(1 - 1));
    if ((*(unsigned int *)(v_rip + 7802395)) != ((unsigned int)(1 - 1))) {
        result = 1;
    }
    *(unsigned int *)(v_rip + 7802369) = (unsigned int)(a2);
    *(unsigned int *)(v_rip + 7802374) = (unsigned int)(1 - 1);
    if ((unsigned int)(result) != 0) {
        result = PpmEventLPICoreParking(v_rdi, a2, *(unsigned __int8 *)(v_rbp + 103), (unsigned __int8)(v_rsi));
    }
}
```

## 5. (Beta) C Style

```c
void sub_006F6620(void)
{
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
    uint32_t v_stack_p20;
    uint32_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint32_t v_stack_p60;
    uint8_t v_stack_p68;
    uint8_t v_stack_p70;
    uint32_t v_stack_p78;

    if ((*(uint32_t *)(v_rip + 0x811DA9)) == ((uint32_t)(local_r12))) goto loc_006F6C4B;
    result = ((int32_t)(*(uint32_t *)(v_rip + 0x8167CB))) * ((int32_t)(*(uint32_t *)(v_rip + 0x8167CB)));
    *(uint32_t *)(v_rip + 0x811D5A) = (uint32_t)(local_r12);
    result = (result) + (*(uint64_t *)(v_rip + 0x711D46));
    *(uint8_t *)(v_rip + 0x811D60) = (uint8_t)(local_r12);
    *(uint64_t *)(local_rbp + 0x7) = result;
    a2 = (uint32_t)((*(uint64_t *)(v_rip + 0x711D46)) * ((uint32_t)(*(uint8_t *)(result + 0xB4))));
    *(uint32_t *)(local_rbp - 0x35) = (uint32_t)(a2);
    result = *(uint8_t *)(result + 0xB4);
    if (*(uint64_t *)(v_rip + 0x811D80) != 0) {
        a3 = *(uint32_t *)(v_rip + 0x8D046B);
        a2 = 255;
        a3 = (a3) << (2);
        result = memset(*(uint64_t *)(v_rip + 0x811D80), a2, a3, a4);
        a2 = *(uint32_t *)(local_rbp - 0x35);
    }
    *(uint32_t *)(local_rbp - 0x39) = (uint32_t)(local_r12);
    if ((*(uint32_t *)(v_rip + 0x811D4B)) == ((uint32_t)(local_r12))) goto loc_006F6C0C;
loc_006F66A2:
    local_rdi = (local_rdi) * ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))));
    local_rdi = (local_rdi) + (*(uint64_t *)(v_rip + 0x811D25));
    if (((*(uint8_t *)(local_rdi + 0x4A0)) & (1)) != 0) goto loc_006F6BF5;
    *(uint64_t *)(local_rdi + 0x20) = *(uint64_t *)(local_rdi + 0x18);
    *(uint16_t *)(local_rdi + 0x4E4) = (uint16_t)(local_r12);
    *(uint8_t *)(local_rdi + 0x4E6) = (uint8_t)(local_r12);
    local_r15 = *(uint16_t *)(local_rdi + 0x492);
    if (((uint16_t)(*(uint16_t *)(local_rdi + 0x492))) >= ((uint16_t)(*(uint16_t *)(local_rdi + 0x496)))) { local_r15 = (uint32_t)(*(uint16_t *)(local_rdi + 0x496)); }
    *(uint32_t *)(local_rbp - 0x59) = (uint32_t)(local_r15);
    result = PpmParkFindOverUtilizedProcessors(local_rdi, a2, a3, a4);
    *(uint64_t *)(local_rbp + 0xF) = result;
    *(uint8_t *)(local_rdi + 0x4B8 + 0x10) = (uint8_t)(local_r12);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x8CE9A9))) == 0) goto loc_006F673D;
    a3 = (a3) * ((uint32_t)(*(uint32_t *)(v_rip + 0x8CE9A9)));
    a2 = 0;
    *(uint64_t *)(local_rdi + 0x4B8) = *(uint64_t *)(result);
    if ((*(uint64_t *)(result)) != (*(uint64_t *)(local_rdi + 0x4B8 + 0x8))) {
        *(uint8_t *)(local_rdi + 0x4B8 + 0x10) = 1;
        *(uint64_t *)(local_rdi + 0x4B8 + 0x8) = *(uint64_t *)(result);
    }
    *(uint32_t *)(local_rbp + 0x7F) = (uint32_t)((uint32_t)((uint32_t)(local_r12)));
    if ((*(uint8_t *)(local_rdi + 0xC)) <= ((uint8_t)(local_r12))) goto loc_006F6BF5;
loc_006F6751:
    *(uint64_t *)(local_rbp - 0x1) = local_rdi + 4;
    local_rbx = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))) * 4) << (7);
    local_rbx = (local_rbx) + (*(uint64_t *)(local_rdi + 0x508));
    *(uint32_t *)(local_rbp + 0x6F) = (uint32_t)(local_r12);
    *(uint64_t *)(local_rbp - 0x21) = *(uint64_t *)(local_rbx + 0x18);
    if (*(uint64_t *)(local_rbx + 0x18) == 0) goto loc_006F6BF1;
    *(uint32_t *)(local_rbp + 0x6F) = 0x100000ULL;
    if ((*(uint16_t *)(v_rip + 0x811C1F)) <= 1) goto loc_006F67C6;
    *(uint16_t *)(local_rbp - 0x41) = (uint16_t)(*(uint16_t *)(local_rdi + 0x4));
    *(uint64_t *)(local_rbp - 0x49) = *(uint64_t *)(local_rbx + 0x20);
    *(uint64_t *)(local_rbp - 0x51) = local_r12;
    goto loc_006F67B3;
loc_006F67A4:
    result = KeGetPrcb((uint32_t)(*(uint32_t *)(local_rbp + 0x77)), a2, a3, local_rdi + 1208);
    local_r13 = (local_r12) | (*(uint64_t *)(result + 0x8E60));
loc_006F67B3:
    result = KeEnumerateNextProcessor(local_rbp + 119, local_rbp - 81, a3, local_rdi + 1208);
    if ((uint32_t)(result) == 0) goto loc_006F67A4;
    goto loc_006F67CA;
loc_006F67C6:
loc_006F67CA:
    local_r13 = (*(uint64_t *)(local_rbx + 0x20)) & (*(uint64_t *)(local_rbx + 0x18));
    if (!(condition_is_equal)) {
    }
    a1 = (uint32_t)((*(uint16_t *)(local_rbx)) - ((uint32_t)(result)));
    *(uint64_t *)(local_rbp - 0x29) = local_r12;
    local_r14 = (uint32_t)((uint32_t)(local_r15));
    if (((uint32_t)(a1)) <= ((uint32_t)(local_r15))) { local_r14 = (uint32_t)(a1); }
    if ((*(uint8_t *)(v_rip + 0x8D02C9)) != 0) goto loc_006F689D;
    *(uint32_t *)(local_rbp + 0x77) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x82B7AE)));
    result = KeGetPrcb((uint32_t)(*(uint32_t *)(v_rip + 0x82B7AE)), local_rbp - 81, a3, local_rdi + 1208);
    if (((uint16_t)(*(uint8_t *)(result + 0xD0))) != ((uint16_t)(*(uint16_t *)(local_rdi + 0x4)))) goto loc_006F689D;
    if (((*(uint64_t *)(local_rbp - 0x21)) & (*(uint64_t *)(result + 0xC8))) == 0) goto loc_006F689D;
    *(uint16_t *)(local_rbp - 0x41) = (uint16_t)(*(uint16_t *)(local_rdi + 0x4));
    *(uint64_t *)(local_rbp - 0x49) = *(uint64_t *)(result + 0xC8);
    result = KeEnumerateNextProcessor(local_rbp + 119, local_rbp - 81, a3, local_rdi + 1208);
    if ((uint32_t)(result) != 0) goto loc_006F689D;
loc_006F684B:
    if (((uint32_t)((uint32_t)((uint32_t)(local_r12)))) >= ((uint32_t)(local_r14))) goto loc_006F6895;
    result = KeGetPrcb((uint32_t)(*(uint32_t *)(local_rbp + 0x77)), local_rbp - 81, a3, local_rdi + 1208);
    if (((local_r13) & (*(uint64_t *)(result + 0xC8))) != 0) goto loc_006F6884;
    if ((*(uint16_t *)(v_rip + 0x811B37)) >= = ((uint16_t)(result + 1))) {
        a1 = *(uint64_t *)(result + 0x8E60);
    }
    a1 = (a1) | (local_r12);
loc_006F6884:
    result = KeEnumerateNextProcessor(local_rbp + 119, local_rbp - 81, a3, local_rdi + 1208);
    if ((uint32_t)(result) == 0) goto loc_006F684B;
loc_006F6895:
    *(uint64_t *)(local_rbp - 0x29) = a1;
loc_006F689D:
    result = KeCpuSetQueryUnparkRecommendation(*(uint16_t *)(*(uint64_t *)(local_rbp - 0x1)), *(uint64_t *)(local_rbp - 0x21), local_rbp - 49, local_rdi + 1208);
    *(uint64_t *)(local_rbp - 0x11) = (uint8_t)(result);
    if ((uint32_t)((uint8_t)(result)) == 0) goto loc_006F697E;
    if ((*(uint16_t *)(v_rip + 0x811AD6)) <= 1) goto loc_006F691C;
    *(uint16_t *)(local_rbp - 0x41) = (uint16_t)(*(uint16_t *)(*(uint64_t *)(local_rbp - 0x1)));
    *(uint64_t *)(local_rbp - 0x49) = *(uint64_t *)(local_rbp - 0x31);
    result = KeEnumerateNextProcessor(local_rbp + 119, local_rbp - 81, local_rbp - 49, local_rdi + 1208);
    if ((uint32_t)(result) != 0) goto loc_006F6913;
loc_006F68EF:
    result = KeGetPrcb((uint32_t)(*(uint32_t *)(local_rbp + 0x77)), local_rbp - 81, local_rbp - 49, local_rdi + 1208);
    local_r12 = (*(uint64_t *)(local_rbp - 0x31)) | (*(uint64_t *)(result + 0x8E60));
    result = KeEnumerateNextProcessor(local_rbp + 119, local_rbp - 81, local_rbp - 49, local_rdi + 1208);
    if ((uint32_t)(result) == 0) goto loc_006F68EF;
    *(uint64_t *)(local_rbp - 0x31) = local_r12;
loc_006F6913:
    *(uint64_t *)(local_rbp - 0x11) = result;
loc_006F691C:
    *(uint16_t *)(local_rbp - 0x41) = (uint16_t)(*(uint16_t *)(*(uint64_t *)(local_rbp - 0x1)));
    *(uint64_t *)(local_rbp - 0x49) = local_r12;
    goto loc_006F696D;
loc_006F692E:
    if (((uint32_t)((uint32_t)((uint32_t)(local_r12)))) >= ((uint32_t)(local_r14))) goto loc_006F697E;
    result = KeGetPrcb((uint32_t)(*(uint32_t *)(local_rbp + 0x77)), local_rbp - 81, local_rbp - 49, local_rdi + 1208);
    if (((local_r13) & (*(uint64_t *)(result + 0xC8))) != 0) goto loc_006F696D;
    if ((*(uint16_t *)(v_rip + 0x811A4F)) >= = 1) {
        a1 = *(uint64_t *)(result + 0x8E60);
    }
    a1 = (a1) | (*(uint64_t *)(local_rbp - 0x29));
    *(uint64_t *)(local_rbp - 0x29) = a1;
loc_006F696D:
    result = KeEnumerateNextProcessor(local_rbp + 119, local_rbp - 81, local_rbp - 49, local_rdi + 1208);
    if ((uint32_t)(result) == 0) goto loc_006F692E;
loc_006F697E:
    if (((uint32_t)((uint32_t)((uint32_t)(local_r12)))) >= ((uint32_t)(*(uint16_t *)(local_rbx + 0x2)))) goto loc_006F69A4;
    if (((uint32_t)((uint32_t)((uint32_t)(local_r12)))) >= ((uint32_t)(local_r14))) goto loc_006F69A4;
    local_r15 = (uint32_t)((uint32_t)(local_r14));
    if (((uint32_t)(*(uint16_t *)(local_rbx + 0x2))) < ((uint32_t)(local_r14))) { local_r15 = (uint32_t)(*(uint16_t *)(local_rbx + 0x2)); }
    a3 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbp + 0x6F))) | (4));
    *(uint32_t *)(local_rbp + 0x6F) = (uint32_t)(a3);
    goto loc_006F69A8;
loc_006F69A4:
loc_006F69A8:
    if (((uint32_t)(local_r14)) <= ((uint32_t)(*(uint16_t *)(local_rbx + 0x4)))) goto loc_006F69CA;
    local_rsi = (uint32_t)((uint32_t)(local_r14));
    if (((uint32_t)(local_r15)) < ((uint32_t)(local_r14))) {
        a3 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbp + 0x6F))) | (8));
        local_rsi = (uint32_t)(*(uint16_t *)(local_rbx + 0x4));
        *(uint32_t *)(local_rbp + 0x6F) = (uint32_t)(a3);
        if (((uint32_t)(*(uint16_t *)(local_rbx + 0x4))) <= ((uint32_t)(local_r15))) { local_rsi = (uint32_t)(local_r15); }
    }
    local_r10 = 0;
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x8CE64B))) & (8));
    result = *(uint16_t *)(local_rbx + 0x4);
    if (!(condition_is_equal)) {
        a1 = *(uint64_t *)(local_rdi + 0x500);
        result = (int32_t)(*(uint32_t *)(a1 + 0x4));
        local_r10 = *(uint8_t *)(a1 + result * 2 + 0x8);
    }
    *(uint32_t *)(local_rbp + 0x67) = (uint32_t)(*(uint16_t *)(local_rbx));
    local_r11 = *(uint16_t *)(local_rbx + 0x6);
    if (((uint16_t)(*(uint16_t *)(local_rbx + 0x6))) >= ((uint16_t)(*(uint16_t *)(local_rbx)))) { local_r11 = (uint32_t)(*(uint16_t *)(local_rbx)); }
    if ((*(uint32_t *)(v_rip + 0x814848)) == 0) goto loc_006F6A41;
    result = (uint32_t)(-((uint32_t)(*(uint32_t *)(local_rbp + 0x7F))));
    a1 = -(a1);
    a2 = (uint32_t)((*(uint8_t *)(a1 + *(uint64_t *)(local_rbp + 0x7) * 1 + 0x89)) * (*(uint32_t *)(local_rbp + 0x67)));
    a2 = (uint32_t)((a2) + (50));
    a2 = (uint32_t)((a2) >> (5));
    if (((uint32_t)(a2)) >= = ((uint32_t)(local_r11))) {
        a3 = (uint32_t)((a3) | (64));
        a4 = (uint32_t)(a2);
        *(uint32_t *)(local_rbp + 0x6F) = (uint32_t)(a3);
    }
    result = *(uint16_t *)(v_rip + 0x81195A);
    if (((uint16_t)(*(uint16_t *)(v_rip + 0x81195A))) >= = 1) {
        a1 = (uint32_t)(*(uint16_t *)(v_rip + 0x81195A));
        a2 = 0;
        result = (uint32_t)((*(uint16_t *)(v_rip + 0x81195A)) - 1);
        a4 = (uint32_t)((a4) + ((uint32_t)(result)));
        result = (uint32_t)(a4);
        a4 = (uint32_t)((a4) - (0));
    }
    if ((uint32_t)(local_r14) == 0) goto loc_006F6A7F;
    if ((uint8_t)(local_r10) == 0) goto loc_006F6A7F;
    if (((uint8_t)(local_r10)) < ((uint8_t)(a4))) {
        a4 = (uint8_t)(local_r10);
        *(uint32_t *)(local_rbp + 0x6F) = (uint32_t)(a3);
    }
    *(uint16_t *)(local_rbx + 0x8) = (uint16_t)((uint8_t)(a4));
    result = (uint32_t)((*(uint64_t *)(local_rbp - 0x11)) + ((uint32_t)(a4)));
    if (((uint32_t)(result)) >= ((uint32_t)(local_rsi))) { result = (uint32_t)(local_rsi); }
    a1 = (uint32_t)((uint32_t)(local_r15));
    if (((uint32_t)(result)) > ((uint32_t)(local_r15))) { a1 = (uint32_t)(result); }
    *(uint16_t *)(local_rbp + 0x67) = (uint16_t)((uint8_t)(a1));
    *(uint16_t *)(local_rbx + 0xA) = (uint16_t)((uint8_t)(a1));
    if ((*(uint8_t *)(v_rip + 0x8D004B)) != 0) goto loc_006F6ABC;
    goto loc_006F6AD1;
loc_006F6ABC:
    result = (uint8_t)(a1);
    local_rsi = (uint32_t)((uint32_t)(a1));
    if ((uint32_t)(local_r14) != 0) {
        result = (uint8_t)(local_r10);
        if (((uint32_t)((uint32_t)((uint32_t)(a1)))) < ((uint32_t)(result))) { result = (uint32_t)((uint32_t)((uint32_t)(a1))); }
        local_rsi = (uint32_t)(result);
    }
    local_r14 = 0;
    result = 0;
    a2 = 0;
    if ((*(uint8_t *)(v_rip + 0x8CFFA8)) != 0) {
        local_r14 = *(uint16_t *)(local_rdi + 0x4F0);
        result = *(uint8_t *)(local_rdi + 0x4F7);
        a2 = *(uint8_t *)(local_rdi + 0x4F6);
    }
    local_rbx = (*(uint64_t *)(local_rbp - 0x21)) & (*(uint64_t *)(local_rbp + 0xF));
    a3 = (*(uint64_t *)(local_rdi + 0x20)) & (*(uint64_t *)(local_rbp - 0x21));
    v_stack_p78 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbp + 0x7F)));
    v_stack_p70 = (uint8_t)(result);
    v_stack_p68 = (uint8_t)(a2);
    v_stack_p60 = (uint32_t)(local_r14);
    v_stack_p58 = local_rdi + 1208;
    v_stack_p50 = local_rbp + 111;
    v_stack_p48 = local_rbp - 25;
    v_stack_p40 = local_rbp - 9;
    v_stack_p38 = *(uint64_t *)(local_rbp - 0x29);
    v_stack_p30 = local_r13;
    v_stack_p28 = (uint32_t)(local_rsi);
    v_stack_p20 = (uint32_t)(a1);
    result = PpmParkComputeUnparkMask(local_rdi, *(uint64_t *)(local_rbp - 0x21), a3, local_rbx);
    a1 = ~(*(uint64_t *)(local_rbp - 0x21));
    v_stack_p50 = (uint32_t)(local_r14);
    result = (a1) & (*(uint64_t *)(local_rdi + 0x18));
    result = (result) | (*(uint64_t *)(local_rbp - 0x19));
    result = (result) | (*(uint64_t *)(local_rbp - 0x9));
    *(uint64_t *)(local_rdi + 0x18) = result;
    result = (*(uint64_t *)(local_rdi + 0x28)) & (a1);
    result = (result) | (*(uint64_t *)(local_rbp - 0x19));
    *(uint64_t *)(local_rdi + 0x28) = result;
    v_stack_p48 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbp + 0x6F)));
    v_stack_p40 = local_r12;
    v_stack_p38 = local_rbx;
    v_stack_p30 = *(uint64_t *)(local_rbp - 0x29);
    v_stack_p28 = local_r13;
    v_stack_p20 = (uint8_t)(local_r15);
    result = PpmEventTraceSoftCoreParkingSelection(local_rdi, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rbp + 0x7F)))), *(uint8_t *)(local_rbp + 0x67), (uint8_t)(local_rsi));
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbp + 0x7F))) + (1));
    *(uint32_t *)(local_rbp + 0x7F) = (uint32_t)(local_rbx);
    if (((uint32_t)(local_rbx)) < ((uint32_t)(*(uint8_t *)(local_rdi + 0xC)))) goto loc_006F6751;
loc_006F6BF1:
loc_006F6BF5:
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbp - 0x39))) + (1));
    *(uint32_t *)(local_rbp - 0x39) = (uint32_t)(local_r14);
    if (((uint32_t)(local_r14)) < (*(uint32_t *)(v_rip + 0x8117DE))) goto loc_006F66A2;
loc_006F6C0C:
    result = PpmParkComputeDiff(local_rdi, (uint32_t)(*(uint32_t *)(local_rbp - 0x35)), *(uint8_t *)(local_rbp + 0x67), (uint8_t)(local_rsi));
    a2 = ((*(uint32_t *)(v_rip + 0x770E28)) > ((uint32_t)(1 - 1))) ? 1 : 0;
    if ((*(uint32_t *)(v_rip + 0x770E18)) != ((uint32_t)(a2))) goto loc_006F6C32;
    result = (uint32_t)((uint32_t)(1 - 1));
    if ((*(uint32_t *)(v_rip + 0x770E1B)) != ((uint32_t)(1 - 1))) {
        result = 1;
    }
    *(uint32_t *)(v_rip + 0x770E01) = (uint32_t)(a2);
    *(uint32_t *)(v_rip + 0x770E06) = (uint32_t)(1 - 1);
    if ((uint32_t)(result) != 0) {
        result = PpmEventLPICoreParking(local_rdi, a2, *(uint8_t *)(local_rbp + 0x67), (uint8_t)(local_rsi));
    }
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006F6620&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
