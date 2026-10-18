# CcUpdateDynamicRegistrySettings

- RVA: `0x0057CFC0`–`0x0057D6C8` (길이 `1,800` bytes)
- VA: `0x000000014057CFC0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C5848`
- 디코드: `456`개 명령, `1,800/1,800` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **21**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **37**

### Outgoing calls
- `0x0057D06A` → [DbgPrintEx](../35/DbgPrintEx_function_00359290.md) (function, `0x00359290`)
- `0x0057D0AC` → [CcQueryRegKeyValue](CcQueryRegKeyValue_function_0057CACC.md) (function, `0x0057CACC`)
- `0x0057D0F6` → [CcQueryRegKeyValue](CcQueryRegKeyValue_function_0057CACC.md) (function, `0x0057CACC`)
- `0x0057D13B` → [CcQueryRegKeyValue](CcQueryRegKeyValue_function_0057CACC.md) (function, `0x0057CACC`)
- `0x0057D17E` → [CcQueryRegKeyValue](CcQueryRegKeyValue_function_0057CACC.md) (function, `0x0057CACC`)
- `0x0057D1C3` → [CcQueryRegKeyValue](CcQueryRegKeyValue_function_0057CACC.md) (function, `0x0057CACC`)
- `0x0057D208` → [CcQueryRegKeyValue](CcQueryRegKeyValue_function_0057CACC.md) (function, `0x0057CACC`)
- `0x0057D24D` → [CcQueryRegKeyValue](CcQueryRegKeyValue_function_0057CACC.md) (function, `0x0057CACC`)
- `0x0057D292` → [CcQueryRegKeyValue](CcQueryRegKeyValue_function_0057CACC.md) (function, `0x0057CACC`)
- `0x0057D2D7` → [CcQueryRegKeyValue](CcQueryRegKeyValue_function_0057CACC.md) (function, `0x0057CACC`)
- `0x0057D31C` → [CcQueryRegKeyValue](CcQueryRegKeyValue_function_0057CACC.md) (function, `0x0057CACC`)
- `0x0057D361` → [CcQueryRegKeyValue](CcQueryRegKeyValue_function_0057CACC.md) (function, `0x0057CACC`)
- `0x0057D3A3` → [CcQueryRegKeyValue](CcQueryRegKeyValue_function_0057CACC.md) (function, `0x0057CACC`)
- `0x0057D45E` → [DbgPrintEx](../35/DbgPrintEx_function_00359290.md) (function, `0x00359290`)
- `0x0057D4E5` → [DbgPrintEx](../35/DbgPrintEx_function_00359290.md) (function, `0x00359290`)
- `0x0057D4F8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0057D601` → [DbgPrintEx](../35/DbgPrintEx_function_00359290.md) (function, `0x00359290`)
- `0x0057D625` → [DbgPrintEx](../35/DbgPrintEx_function_00359290.md) (function, `0x00359290`)
- `0x0057D66E` → [DbgPrintEx](../35/DbgPrintEx_function_00359290.md) (function, `0x00359290`)
- `0x0057D692` → [DbgPrintEx](../35/DbgPrintEx_function_00359290.md) (function, `0x00359290`)
- `0x0057D6A1` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0057CFE6` → RVA `0x00E0A740` (`.data`; read)
- `0x0057D00E` → RVA `0x006C8120` (` ?? ::FNODOBFM::`string'`; read)
- `0x0057D06F` → RVA `0x006C7A60` (` ?? ::FNODOBFM::`string'`; read)
- `0x0057D085` → RVA `0x006C8250` (` ?? ::FNODOBFM::`string'`; read)
- `0x0057D0CB` → RVA `0x006C8280` (` ?? ::FNODOBFM::`string'`; read)
- `0x0057D110` → RVA `0x006C81F0` (` ?? ::FNODOBFM::`string'`; read)
- `0x0057D153` → RVA `0x006C8210` (` ?? ::FNODOBFM::`string'`; read)
- `0x0057D198` → RVA `0x006C8350` (` ?? ::FNODOBFM::`string'`; read)
- `0x0057D1DD` → RVA `0x006C8380` (` ?? ::FNODOBFM::`string'`; read)
- `0x0057D222` → RVA `0x006C82C0` (` ?? ::FNODOBFM::`string'`; read)
- `0x0057D267` → RVA `0x006C8310` (` ?? ::FNODOBFM::`string'`; read)
- `0x0057D2AC` → RVA `0x006C8420` (` ?? ::FNODOBFM::`string'`; read)
- `0x0057D2F1` → RVA `0x006C8470` (` ?? ::FNODOBFM::`string'`; read)
- `0x0057D336` → RVA `0x006C83B0` (` ?? ::FNODOBFM::`string'`; read)
- `0x0057D378` → RVA `0x006C83E0` (` ?? ::FNODOBFM::`string'`; read)
- `0x0057D3BD` → RVA `0x006C8710` (` ?? ::FNODOBFM::`string'`; read)
- `0x0057D3C7` → RVA `0x006C8700` (` ?? ::FNODOBFM::`string'`; read)
- `0x0057D435` → RVA `0x006C84A0` (` ?? ::FNODOBFM::`string'`; read)
- `0x0057D48A` → RVA `0x006C85F0` (` ?? ::FNODOBFM::`string'`; read)
- `0x0057D504` → RVA `0x00E65B90` (`.data`; write)
- `0x0057D51C` → RVA `0x00E65B54` (`.data`; write)
- `0x0057D541` → RVA `0x00E65B5C` (`.data`; write)
- `0x0057D554` → RVA `0x00E65B6C` (`.data`; write)
- `0x0057D56D` → RVA `0x00E0A870` (`.data`; write)
- `0x0057D584` → RVA `0x00F8F280` (`.data`; write)
- `0x0057D59F` → RVA `0x00F8F288` (`.data`; write)
- `0x0057D5BA` → RVA `0x00F8F290` (`.data`; write)
- `0x0057D5CA` → RVA `0x00F8F2A1` (`.data`; write)
- `0x0057D5DE` → RVA `0x00E65B96` (`.data`; write)
- `0x0057D5E9` → RVA `0x00E65B88` (`.data`; read)
- `0x0057D5F7` → RVA `0x006C8830` (` ?? ::FNODOBFM::`string'`; read)
- `0x0057D608` → RVA `0x00E65B96` (`.data`; read)
- `0x0057D60F` → RVA `0x006C88A0` (` ?? ::FNODOBFM::`string'`; read)
- `0x0057D635` → RVA `0x00E65B95` (`.data`; write)
- `0x0057D664` → RVA `0x006C8720` (` ?? ::FNODOBFM::`string'`; read)
- `0x0057D675` → RVA `0x00E65B95` (`.data`; read)
- `0x0057D67C` → RVA `0x006C87B0` (` ?? ::FNODOBFM::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0057D4F8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0057CFC0  48 8B C4                        mov rax, rsp
0057CFC3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
0057CFC7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0057CFCB  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0057CFCF  55                              push rbp
0057CFD0  41 54                           push r12
0057CFD2  41 55                           push r13
0057CFD4  41 56                           push r14
0057CFD6  41 57                           push r15
0057CFD8  48 8D A8 48 FF FF FF            lea rbp, [rax - 0xb8]
0057CFDF  48 81 EC 90 01 00 00            sub rsp, 0x190
0057CFE6  48 8B 05 53 D7 88 00            mov rax, qword ptr [rip + 0x88d753]
0057CFED  48 33 C4                        xor rax, rsp
0057CFF0  48 89 85 80 00 00 00            mov qword ptr [rbp + 0x80], rax
0057CFF7  33 DB                           xor ebx, ebx
0057CFF9  C7 45 8C 9C 00 00 00            mov dword ptr [rbp - 0x74], 0x9c
0057D000  48 8D 45 E0                     lea rax, [rbp - 0x20]
0057D004  89 5D C4                        mov dword ptr [rbp - 0x3c], ebx
0057D007  4C 8D 49 38                     lea r9, [rcx + 0x38]
0057D00B  89 5D 9C                        mov dword ptr [rbp - 0x64], ebx
0057D00E  4C 8D 05 0B B1 14 00            lea r8, [rip + 0x14b10b]
0057D015  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
0057D019  8D 53 02                        lea edx, [rbx + 2]
0057D01C  88 5D 80                        mov byte ptr [rbp - 0x80], bl
0057D01F  8D 4B 7F                        lea ecx, [rbx + 0x7f]
0057D022  44 0F B6 F3                     movzx r14d, bl
0057D026  44 8B EB                        mov r13d, ebx
0057D029  89 5D D0                        mov dword ptr [rbp - 0x30], ebx
0057D02C  88 5D A8                        mov byte ptr [rbp - 0x58], bl
0057D02F  44 8B FB                        mov r15d, ebx
0057D032  88 5D 81                        mov byte ptr [rbp - 0x7f], bl
0057D035  8B FB                           mov edi, ebx
0057D037  89 5D AC                        mov dword ptr [rbp - 0x54], ebx
0057D03A  44 8B E3                        mov r12d, ebx
0057D03D  88 5D 82                        mov byte ptr [rbp - 0x7e], bl
0057D040  89 5D B0                        mov dword ptr [rbp - 0x50], ebx
0057D043  88 5D 83                        mov byte ptr [rbp - 0x7d], bl
0057D046  89 5D B4                        mov dword ptr [rbp - 0x4c], ebx
0057D049  88 5D 84                        mov byte ptr [rbp - 0x7c], bl
0057D04C  89 5D D4                        mov dword ptr [rbp - 0x2c], ebx
0057D04F  88 5D 85                        mov byte ptr [rbp - 0x7b], bl
0057D052  89 5D D8                        mov dword ptr [rbp - 0x28], ebx
0057D055  88 5D A9                        mov byte ptr [rbp - 0x57], bl
0057D058  89 5D B8                        mov dword ptr [rbp - 0x48], ebx
0057D05B  88 5D 86                        mov byte ptr [rbp - 0x7a], bl
0057D05E  89 5D BC                        mov dword ptr [rbp - 0x44], ebx
0057D061  88 5D 87                        mov byte ptr [rbp - 0x79], bl
0057D064  88 5D 88                        mov byte ptr [rbp - 0x78], bl
0057D067  88 5D 89                        mov byte ptr [rbp - 0x77], bl
0057D06A  E8 21 C2 DD FF                  call 0x140359290
0057D06F  48 8D 05 EA A9 14 00            lea rax, [rip + 0x14a9ea]
0057D076  C7 45 C0 A8 00 AA 00            mov dword ptr [rbp - 0x40], 0xaa00a8
0057D07D  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
0057D081  4C 8D 4D 90                     lea r9, [rbp - 0x70]
0057D085  48 8D 05 C4 B1 14 00            lea rax, [rip + 0x14b1c4]
0057D08C  C7 45 98 22 00 24 00            mov dword ptr [rbp - 0x68], 0x240022
0057D093  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
0057D097  4C 8D 45 8C                     lea r8, [rbp - 0x74]
0057D09B  48 8D 45 80                     lea rax, [rbp - 0x80]
0057D09F  48 8D 55 98                     lea rdx, [rbp - 0x68]
0057D0A3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0057D0A8  48 8D 4D C0                     lea rcx, [rbp - 0x40]
0057D0AC  E8 1B FA FF FF                  call 0x14057cacc
0057D0B1  8D 73 01                        lea esi, [rbx + 1]
0057D0B4  85 C0                           test eax, eax
0057D0B6  78 13                           js 0x14057d0cb
0057D0B8  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
0057D0BC  8B 41 08                        mov eax, dword ptr [rcx + 8]
0057D0BF  44 8B 2C 08                     mov r13d, dword ptr [rax + rcx]
0057D0C3  41 83 FD 03                     cmp r13d, 3
0057D0C7  44 0F 42 F6                     cmovb r14d, esi
0057D0CB  48 8D 05 AE B1 14 00            lea rax, [rip + 0x14b1ae]
0057D0D2  C7 45 98 3C 00 3E 00            mov dword ptr [rbp - 0x68], 0x3e003c
0057D0D9  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
0057D0DD  4C 8D 4D 90                     lea r9, [rbp - 0x70]
0057D0E1  48 8D 45 80                     lea rax, [rbp - 0x80]
0057D0E5  4C 8D 45 8C                     lea r8, [rbp - 0x74]
0057D0E9  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0057D0EE  48 8D 55 98                     lea rdx, [rbp - 0x68]
0057D0F2  48 8D 4D C0                     lea rcx, [rbp - 0x40]
0057D0F6  E8 D1 F9 FF FF                  call 0x14057cacc
0057D0FB  85 C0                           test eax, eax
0057D0FD  78 11                           js 0x14057d110
0057D0FF  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
0057D103  40 88 75 A8                     mov byte ptr [rbp - 0x58], sil
0057D107  8B 41 08                        mov eax, dword ptr [rcx + 8]
0057D10A  8B 04 08                        mov eax, dword ptr [rax + rcx]
0057D10D  89 45 D0                        mov dword ptr [rbp - 0x30], eax
0057D110  48 8D 05 D9 B0 14 00            lea rax, [rip + 0x14b0d9]
0057D117  C7 45 98 1C 00 1E 00            mov dword ptr [rbp - 0x68], 0x1e001c
0057D11E  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
0057D122  4C 8D 4D 90                     lea r9, [rbp - 0x70]
0057D126  48 8D 45 80                     lea rax, [rbp - 0x80]
0057D12A  4C 8D 45 8C                     lea r8, [rbp - 0x74]
0057D12E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0057D133  48 8D 55 98                     lea rdx, [rbp - 0x68]
0057D137  48 8D 4D C0                     lea rcx, [rbp - 0x40]
0057D13B  E8 8C F9 FF FF                  call 0x14057cacc
0057D140  85 C0                           test eax, eax
0057D142  78 0F                           js 0x14057d153
0057D144  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
0057D148  40 88 75 81                     mov byte ptr [rbp - 0x7f], sil
0057D14C  8B 41 08                        mov eax, dword ptr [rcx + 8]
0057D14F  44 8B 3C 08                     mov r15d, dword ptr [rax + rcx]
0057D153  48 8D 05 B6 B0 14 00            lea rax, [rip + 0x14b0b6]
0057D15A  C7 45 98 36 00 38 00            mov dword ptr [rbp - 0x68], 0x380036
0057D161  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
0057D165  4C 8D 4D 90                     lea r9, [rbp - 0x70]
0057D169  48 8D 45 80                     lea rax, [rbp - 0x80]
0057D16D  4C 8D 45 8C                     lea r8, [rbp - 0x74]
0057D171  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0057D176  48 8D 55 98                     lea rdx, [rbp - 0x68]
0057D17A  48 8D 4D C0                     lea rcx, [rbp - 0x40]
0057D17E  E8 49 F9 FF FF                  call 0x14057cacc
0057D183  85 C0                           test eax, eax
0057D185  78 11                           js 0x14057d198
0057D187  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
0057D18B  40 88 75 82                     mov byte ptr [rbp - 0x7e], sil
0057D18F  8B 41 08                        mov eax, dword ptr [rcx + 8]
0057D192  8B 04 08                        mov eax, dword ptr [rax + rcx]
0057D195  89 45 AC                        mov dword ptr [rbp - 0x54], eax
0057D198  48 8D 05 B1 B1 14 00            lea rax, [rip + 0x14b1b1]
0057D19F  C7 45 98 2A 00 2C 00            mov dword ptr [rbp - 0x68], 0x2c002a
0057D1A6  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
0057D1AA  4C 8D 4D 90                     lea r9, [rbp - 0x70]
0057D1AE  48 8D 45 80                     lea rax, [rbp - 0x80]
0057D1B2  4C 8D 45 8C                     lea r8, [rbp - 0x74]
0057D1B6  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0057D1BB  48 8D 55 98                     lea rdx, [rbp - 0x68]
0057D1BF  48 8D 4D C0                     lea rcx, [rbp - 0x40]
0057D1C3  E8 04 F9 FF FF                  call 0x14057cacc
0057D1C8  85 C0                           test eax, eax
0057D1CA  78 11                           js 0x14057d1dd
0057D1CC  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
0057D1D0  40 88 75 83                     mov byte ptr [rbp - 0x7d], sil
0057D1D4  8B 41 08                        mov eax, dword ptr [rcx + 8]
0057D1D7  8B 04 08                        mov eax, dword ptr [rax + rcx]
0057D1DA  89 45 B0                        mov dword ptr [rbp - 0x50], eax
0057D1DD  48 8D 05 9C B1 14 00            lea rax, [rip + 0x14b19c]
0057D1E4  C7 45 98 22 00 24 00            mov dword ptr [rbp - 0x68], 0x240022
0057D1EB  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
0057D1EF  4C 8D 4D 90                     lea r9, [rbp - 0x70]
0057D1F3  48 8D 45 80                     lea rax, [rbp - 0x80]
0057D1F7  4C 8D 45 8C                     lea r8, [rbp - 0x74]
0057D1FB  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0057D200  48 8D 55 98                     lea rdx, [rbp - 0x68]
0057D204  48 8D 4D C0                     lea rcx, [rbp - 0x40]
0057D208  E8 BF F8 FF FF                  call 0x14057cacc
0057D20D  85 C0                           test eax, eax
0057D20F  78 11                           js 0x14057d222
0057D211  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
0057D215  40 88 75 84                     mov byte ptr [rbp - 0x7c], sil
0057D219  8B 41 08                        mov eax, dword ptr [rcx + 8]
0057D21C  8B 04 08                        mov eax, dword ptr [rax + rcx]
0057D21F  89 45 B4                        mov dword ptr [rbp - 0x4c], eax
0057D222  48 8D 05 97 B0 14 00            lea rax, [rip + 0x14b097]
0057D229  C7 45 98 40 00 42 00            mov dword ptr [rbp - 0x68], 0x420040
0057D230  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
0057D234  4C 8D 4D 90                     lea r9, [rbp - 0x70]
0057D238  48 8D 45 80                     lea rax, [rbp - 0x80]
0057D23C  4C 8D 45 8C                     lea r8, [rbp - 0x74]
0057D240  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0057D245  48 8D 55 98                     lea rdx, [rbp - 0x68]
0057D249  48 8D 4D C0                     lea rcx, [rbp - 0x40]
0057D24D  E8 7A F8 FF FF                  call 0x14057cacc
0057D252  85 C0                           test eax, eax
0057D254  78 11                           js 0x14057d267
0057D256  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
0057D25A  40 88 75 85                     mov byte ptr [rbp - 0x7b], sil
0057D25E  8B 41 08                        mov eax, dword ptr [rcx + 8]
0057D261  8B 04 08                        mov eax, dword ptr [rax + rcx]
0057D264  89 45 D4                        mov dword ptr [rbp - 0x2c], eax
0057D267  48 8D 05 A2 B0 14 00            lea rax, [rip + 0x14b0a2]
0057D26E  C7 45 98 3E 00 40 00            mov dword ptr [rbp - 0x68], 0x40003e
0057D275  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
0057D279  4C 8D 4D 90                     lea r9, [rbp - 0x70]
0057D27D  48 8D 45 80                     lea rax, [rbp - 0x80]
0057D281  4C 8D 45 8C                     lea r8, [rbp - 0x74]
0057D285  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0057D28A  48 8D 55 98                     lea rdx, [rbp - 0x68]
0057D28E  48 8D 4D C0                     lea rcx, [rbp - 0x40]
0057D292  E8 35 F8 FF FF                  call 0x14057cacc
0057D297  85 C0                           test eax, eax
0057D299  78 11                           js 0x14057d2ac
0057D29B  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
0057D29F  40 88 75 A9                     mov byte ptr [rbp - 0x57], sil
0057D2A3  8B 41 08                        mov eax, dword ptr [rcx + 8]
0057D2A6  8B 14 08                        mov edx, dword ptr [rax + rcx]
0057D2A9  89 55 D8                        mov dword ptr [rbp - 0x28], edx
0057D2AC  48 8D 05 6D B1 14 00            lea rax, [rip + 0x14b16d]
0057D2B3  C7 45 98 40 00 42 00            mov dword ptr [rbp - 0x68], 0x420040
0057D2BA  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
0057D2BE  4C 8D 4D 90                     lea r9, [rbp - 0x70]
0057D2C2  48 8D 45 80                     lea rax, [rbp - 0x80]
0057D2C6  4C 8D 45 8C                     lea r8, [rbp - 0x74]
0057D2CA  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0057D2CF  48 8D 55 98                     lea rdx, [rbp - 0x68]
0057D2D3  48 8D 4D C0                     lea rcx, [rbp - 0x40]
0057D2D7  E8 F0 F7 FF FF                  call 0x14057cacc
0057D2DC  85 C0                           test eax, eax
0057D2DE  78 11                           js 0x14057d2f1
0057D2E0  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
0057D2E4  40 88 75 86                     mov byte ptr [rbp - 0x7a], sil
0057D2E8  8B 41 08                        mov eax, dword ptr [rcx + 8]
0057D2EB  8B 04 08                        mov eax, dword ptr [rax + rcx]
0057D2EE  89 45 B8                        mov dword ptr [rbp - 0x48], eax
0057D2F1  48 8D 05 78 B1 14 00            lea rax, [rip + 0x14b178]
0057D2F8  C7 45 98 2A 00 2C 00            mov dword ptr [rbp - 0x68], 0x2c002a
0057D2FF  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
0057D303  4C 8D 4D 90                     lea r9, [rbp - 0x70]
0057D307  48 8D 45 80                     lea rax, [rbp - 0x80]
0057D30B  4C 8D 45 8C                     lea r8, [rbp - 0x74]
0057D30F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0057D314  48 8D 55 98                     lea rdx, [rbp - 0x68]
0057D318  48 8D 4D C0                     lea rcx, [rbp - 0x40]
0057D31C  E8 AB F7 FF FF                  call 0x14057cacc
0057D321  85 C0                           test eax, eax
0057D323  78 11                           js 0x14057d336
0057D325  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
0057D329  40 88 75 87                     mov byte ptr [rbp - 0x79], sil
0057D32D  8B 41 08                        mov eax, dword ptr [rcx + 8]
0057D330  8B 04 08                        mov eax, dword ptr [rax + rcx]
0057D333  89 45 BC                        mov dword ptr [rbp - 0x44], eax
0057D336  48 8D 05 73 B0 14 00            lea rax, [rip + 0x14b073]
0057D33D  C7 45 98 28 00 2A 00            mov dword ptr [rbp - 0x68], 0x2a0028
0057D344  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
0057D348  4C 8D 4D 90                     lea r9, [rbp - 0x70]
0057D34C  48 8D 45 80                     lea rax, [rbp - 0x80]
0057D350  4C 8D 45 8C                     lea r8, [rbp - 0x74]
0057D354  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0057D359  48 8D 55 98                     lea rdx, [rbp - 0x68]
0057D35D  48 8D 4D C0                     lea rcx, [rbp - 0x40]
0057D361  E8 66 F7 FF FF                  call 0x14057cacc
0057D366  85 C0                           test eax, eax
0057D368  78 0E                           js 0x14057d378
0057D36A  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
0057D36E  40 88 75 88                     mov byte ptr [rbp - 0x78], sil
0057D372  8B 41 08                        mov eax, dword ptr [rcx + 8]
0057D375  8B 3C 08                        mov edi, dword ptr [rax + rcx]
0057D378  48 8D 05 61 B0 14 00            lea rax, [rip + 0x14b061]
0057D37F  C7 45 98 32 00 34 00            mov dword ptr [rbp - 0x68], 0x340032
0057D386  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
0057D38A  4C 8D 4D 90                     lea r9, [rbp - 0x70]
0057D38E  48 8D 45 80                     lea rax, [rbp - 0x80]
0057D392  4C 8D 45 8C                     lea r8, [rbp - 0x74]
0057D396  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0057D39B  48 8D 55 98                     lea rdx, [rbp - 0x68]
0057D39F  48 8D 4D C0                     lea rcx, [rbp - 0x40]
0057D3A3  E8 24 F7 FF FF                  call 0x14057cacc
0057D3A8  48 8B 75 90                     mov rsi, qword ptr [rbp - 0x70]
0057D3AC  85 C0                           test eax, eax
0057D3AE  78 0B                           js 0x14057d3bb
0057D3B0  8B 46 08                        mov eax, dword ptr [rsi + 8]
0057D3B3  C6 45 89 01                     mov byte ptr [rbp - 0x77], 1
0057D3B7  44 8B 24 30                     mov r12d, dword ptr [rax + rsi]
0057D3BB  33 C0                           xor eax, eax
0057D3BD  4C 8D 1D 4C B3 14 00            lea r11, [rip + 0x14b34c]
0057D3C4  38 45 84                        cmp byte ptr [rbp - 0x7c], al
0057D3C7  48 8D 1D 32 B3 14 00            lea rbx, [rip + 0x14b332]
0057D3CE  4C 8B D3                        mov r10, rbx
0057D3D1  4C 8B CB                        mov r9, rbx
0057D3D4  4D 0F 44 D3                     cmove r10, r11
0057D3D8  4C 8B C3                        mov r8, rbx
0057D3DB  38 45 83                        cmp byte ptr [rbp - 0x7d], al
0057D3DE  48 8B D3                        mov rdx, rbx
0057D3E1  4C 89 54 24 70                  mov qword ptr [rsp + 0x70], r10
0057D3E6  48 8B CB                        mov rcx, rbx
0057D3E9  44 8B 55 B4                     mov r10d, dword ptr [rbp - 0x4c]
0057D3ED  4D 0F 44 CB                     cmove r9, r11
0057D3F1  38 45 82                        cmp byte ptr [rbp - 0x7e], al
0057D3F4  44 89 54 24 68                  mov dword ptr [rsp + 0x68], r10d
0057D3F9  4C 89 4C 24 60                  mov qword ptr [rsp + 0x60], r9
0057D3FE  4D 0F 44 C3                     cmove r8, r11
0057D402  38 45 81                        cmp byte ptr [rbp - 0x7f], al
0057D405  44 8B 4D B0                     mov r9d, dword ptr [rbp - 0x50]
0057D409  44 89 4C 24 58                  mov dword ptr [rsp + 0x58], r9d
0057D40E  49 0F 44 D3                     cmove rdx, r11
0057D412  38 45 A8                        cmp byte ptr [rbp - 0x58], al
0057D415  45 8B CD                        mov r9d, r13d
0057D418  4C 89 44 24 50                  mov qword ptr [rsp + 0x50], r8
0057D41D  48 8B C3                        mov rax, rbx
0057D420  44 8B 45 AC                     mov r8d, dword ptr [rbp - 0x54]
0057D424  49 0F 44 CB                     cmove rcx, r11
0057D428  44 89 44 24 48                  mov dword ptr [rsp + 0x48], r8d
0057D42D  45 84 F6                        test r14b, r14b
0057D430  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
0057D435  4C 8D 05 64 B0 14 00            lea r8, [rip + 0x14b064]
0057D43C  44 89 7C 24 38                  mov dword ptr [rsp + 0x38], r15d
0057D441  BA 02 00 00 00                  mov edx, 2
0057D446  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
0057D44B  49 0F 44 C3                     cmove rax, r11
0057D44F  8B 4D D0                        mov ecx, dword ptr [rbp - 0x30]
0057D452  89 4C 24 28                     mov dword ptr [rsp + 0x28], ecx
0057D456  8D 4A 7D                        lea ecx, [rdx + 0x7d]
0057D459  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0057D45E  E8 2D BE DD FF                  call 0x140359290
0057D463  45 33 D2                        xor r10d, r10d
0057D466  4C 8D 0D A3 B2 14 00            lea r9, [rip + 0x14b2a3]
0057D46D  44 38 55 89                     cmp byte ptr [rbp - 0x77], r10b
0057D471  4C 8B C3                        mov r8, rbx
0057D474  48 8B CB                        mov rcx, rbx
0057D477  48 8B D3                        mov rdx, rbx
0057D47A  4D 0F 44 C1                     cmove r8, r9
0057D47E  48 8B C3                        mov rax, rbx
0057D481  44 38 55 88                     cmp byte ptr [rbp - 0x78], r10b
0057D485  4C 89 44 24 60                  mov qword ptr [rsp + 0x60], r8
0057D48A  4C 8D 05 5F B1 14 00            lea r8, [rip + 0x14b15f]
0057D491  49 0F 44 C9                     cmove rcx, r9
0057D495  44 89 64 24 58                  mov dword ptr [rsp + 0x58], r12d
0057D49A  44 38 55 87                     cmp byte ptr [rbp - 0x79], r10b
0057D49E  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
0057D4A3  8B 4D BC                        mov ecx, dword ptr [rbp - 0x44]
0057D4A6  49 0F 44 D1                     cmove rdx, r9
0057D4AA  44 38 55 86                     cmp byte ptr [rbp - 0x7a], r10b
0057D4AE  89 7C 24 48                     mov dword ptr [rsp + 0x48], edi
0057D4B2  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
0057D4B7  49 0F 44 C1                     cmove rax, r9
0057D4BB  44 38 55 85                     cmp byte ptr [rbp - 0x7b], r10b
0057D4BF  41 8D 52 02                     lea edx, [r10 + 2]
0057D4C3  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
0057D4C7  8D 4A 7D                        lea ecx, [rdx + 0x7d]
0057D4CA  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0057D4CF  49 0F 44 D9                     cmove rbx, r9
0057D4D3  8B 45 B8                        mov eax, dword ptr [rbp - 0x48]
0057D4D6  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
0057D4DA  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0057D4DF  8B 5D D4                        mov ebx, dword ptr [rbp - 0x2c]
0057D4E2  44 8B CB                        mov r9d, ebx
0057D4E5  E8 A6 BD DD FF                  call 0x140359290
0057D4EA  80 7D 80 00                     cmp byte ptr [rbp - 0x80], 0
0057D4EE  74 0D                           je 0x14057d4fd
0057D4F0  BA 43 63 66 78                  mov edx, 0x78666343
0057D4F5  48 8B CE                        mov rcx, rsi
0057D4F8  E8 73 53 60 00                  call 0x140b82870
0057D4FD  33 F6                           xor esi, esi
0057D4FF  45 84 F6                        test r14b, r14b
0057D502  74 07                           je 0x14057d50b
0057D504  44 89 2D 85 86 8E 00            mov dword ptr [rip + 0x8e8685], r13d
0057D50B  40 38 75 81                     cmp byte ptr [rbp - 0x7f], sil
0057D50F  74 1C                           je 0x14057d52d
0057D511  45 85 FF                        test r15d, r15d
0057D514  74 11                           je 0x14057d527
0057D516  41 8B C7                        mov eax, r15d
0057D519  C1 E0 0A                        shl eax, 0xa
0057D51C  89 05 32 86 8E 00               mov dword ptr [rip + 0x8e8632], eax
0057D522  41 3B C7                        cmp eax, r15d
0057D525  77 06                           ja 0x14057d52d
0057D527  89 35 27 86 8E 00               mov dword ptr [rip + 0x8e8627], esi
0057D52D  40 38 75 82                     cmp byte ptr [rbp - 0x7e], sil
0057D531  74 14                           je 0x14057d547
0057D533  8B 55 AC                        mov edx, dword ptr [rbp - 0x54]
0057D536  8B CE                           mov ecx, esi
0057D538  8D 42 FF                        lea eax, [rdx - 1]
0057D53B  83 F8 63                        cmp eax, 0x63
0057D53E  0F 46 CA                        cmovbe ecx, edx
0057D541  89 0D 15 86 8E 00               mov dword ptr [rip + 0x8e8615], ecx
0057D547  40 38 75 83                     cmp byte ptr [rbp - 0x7d], sil
0057D54B  74 0D                           je 0x14057d55a
0057D54D  8B 45 B0                        mov eax, dword ptr [rbp - 0x50]
0057D550  85 C0                           test eax, eax
0057D552  74 06                           je 0x14057d55a
0057D554  89 05 12 86 8E 00               mov dword ptr [rip + 0x8e8612], eax
0057D55A  40 38 75 84                     cmp byte ptr [rbp - 0x7c], sil
0057D55E  74 13                           je 0x14057d573
0057D560  8B 4D B4                        mov ecx, dword ptr [rbp - 0x4c]
0057D563  8D 41 FF                        lea eax, [rcx - 1]
0057D566  3D FF 7F 00 00                  cmp eax, 0x7fff
0057D56B  77 06                           ja 0x14057d573
0057D56D  89 0D FD D2 88 00               mov dword ptr [rip + 0x88d2fd], ecx
0057D573  40 38 75 85                     cmp byte ptr [rbp - 0x7b], sil
0057D577  74 12                           je 0x14057d58b
0057D579  85 DB                           test ebx, ebx
0057D57B  74 0E                           je 0x14057d58b
0057D57D  48 69 CB 80 69 67 FF            imul rcx, rbx, -0x989680
0057D584  48 89 0D F5 1C A1 00            mov qword ptr [rip + 0xa11cf5], rcx
0057D58B  40 38 75 A9                     cmp byte ptr [rbp - 0x57], sil
0057D58F  74 15                           je 0x14057d5a6
0057D591  8B 45 D8                        mov eax, dword ptr [rbp - 0x28]
0057D594  85 C0                           test eax, eax
0057D596  74 0E                           je 0x14057d5a6
0057D598  48 69 C8 80 96 98 00            imul rcx, rax, 0x989680
0057D59F  48 89 0D E2 1C A1 00            mov qword ptr [rip + 0xa11ce2], rcx
0057D5A6  40 38 75 86                     cmp byte ptr [rbp - 0x7a], sil
0057D5AA  74 15                           je 0x14057d5c1
0057D5AC  8B 45 B8                        mov eax, dword ptr [rbp - 0x48]
0057D5AF  85 C0                           test eax, eax
0057D5B1  74 0E                           je 0x14057d5c1
0057D5B3  48 69 C8 80 96 98 00            imul rcx, rax, 0x989680
0057D5BA  48 89 0D CF 1C A1 00            mov qword ptr [rip + 0xa11ccf], rcx
0057D5C1  40 38 75 87                     cmp byte ptr [rbp - 0x79], sil
0057D5C5  74 0A                           je 0x14057d5d1
0057D5C7  39 75 BC                        cmp dword ptr [rbp - 0x44], esi
0057D5CA  0F 95 05 D0 1C A1 00            setne byte ptr [rip + 0xa11cd0]
0057D5D1  40 38 75 88                     cmp byte ptr [rbp - 0x78], sil
0057D5D5  74 53                           je 0x14057d62a
0057D5D7  83 FF 01                        cmp edi, 1
0057D5DA  77 2C                           ja 0x14057d608
0057D5DC  85 FF                           test edi, edi
0057D5DE  0F 95 05 B1 85 8E 00            setne byte ptr [rip + 0x8e85b1]
0057D5E5  85 FF                           test edi, edi
0057D5E7  74 41                           je 0x14057d62a
0057D5E9  40 38 35 98 85 8E 00            cmp byte ptr [rip + 0x8e8598], sil
0057D5F0  75 38                           jne 0x14057d62a
0057D5F2  BA 02 00 00 00                  mov edx, 2
0057D5F7  4C 8D 05 32 B2 14 00            lea r8, [rip + 0x14b232]
0057D5FE  8D 4A 7D                        lea ecx, [rdx + 0x7d]
0057D601  E8 8A BC DD FF                  call 0x140359290
0057D606  EB 22                           jmp 0x14057d62a
0057D608  0F B6 05 87 85 8E 00            movzx eax, byte ptr [rip + 0x8e8587]
0057D60F  4C 8D 05 8A B2 14 00            lea r8, [rip + 0x14b28a]
0057D616  BA 02 00 00 00                  mov edx, 2
0057D61B  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0057D61F  44 8B CF                        mov r9d, edi
0057D622  8D 4A 7D                        lea ecx, [rdx + 0x7d]
0057D625  E8 66 BC DD FF                  call 0x140359290
0057D62A  40 38 75 89                     cmp byte ptr [rbp - 0x77], sil
0057D62E  74 67                           je 0x14057d697
0057D630  45 85 E4                        test r12d, r12d
0057D633  75 09                           jne 0x14057d63e
0057D635  40 88 35 59 85 8E 00            mov byte ptr [rip + 0x8e8559], sil
0057D63C  EB 59                           jmp 0x14057d697
0057D63E  41 83 FC 01                     cmp r12d, 1
0057D642  75 31                           jne 0x14057d675
0057D644  40 38 35 3D 85 8E 00            cmp byte ptr [rip + 0x8e853d], sil
0057D64B  74 12                           je 0x14057d65f
0057D64D  40 38 35 42 85 8E 00            cmp byte ptr [rip + 0x8e8542], sil
0057D654  74 09                           je 0x14057d65f
0057D656  44 88 25 38 85 8E 00            mov byte ptr [rip + 0x8e8538], r12b
0057D65D  EB 38                           jmp 0x14057d697
0057D65F  BA 02 00 00 00                  mov edx, 2
0057D664  4C 8D 05 B5 B0 14 00            lea r8, [rip + 0x14b0b5]
0057D66B  8D 4A 7D                        lea ecx, [rdx + 0x7d]
0057D66E  E8 1D BC DD FF                  call 0x140359290
0057D673  EB 22                           jmp 0x14057d697
0057D675  0F B6 05 19 85 8E 00            movzx eax, byte ptr [rip + 0x8e8519]
0057D67C  4C 8D 05 2D B1 14 00            lea r8, [rip + 0x14b12d]
0057D683  BA 02 00 00 00                  mov edx, 2
0057D688  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0057D68C  45 8B CC                        mov r9d, r12d
0057D68F  8D 4A 7D                        lea ecx, [rdx + 0x7d]
0057D692  E8 F9 BB DD FF                  call 0x140359290
0057D697  48 8B 8D 80 00 00 00            mov rcx, qword ptr [rbp + 0x80]
0057D69E  48 33 CC                        xor rcx, rsp
0057D6A1  E8 9A EF 12 00                  call 0x1406ac640
0057D6A6  4C 8D 9C 24 90 01 00 00         lea r11, [rsp + 0x190]
0057D6AE  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0057D6B2  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0057D6B6  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
0057D6BA  49 8B E3                        mov rsp, r11
0057D6BD  41 5F                           pop r15
0057D6BF  41 5E                           pop r14
0057D6C1  41 5D                           pop r13
0057D6C3  41 5C                           pop r12
0057D6C5  5D                              pop rbp
0057D6C6  C3                              ret
0057D6C7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CcUpdateDynamicRegistrySettings(__int64 a1)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m148;
    unsigned int v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned int v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned int v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned int v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned int v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m28;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (400);
    result = (*(unsigned __int64 *)(v_rip + 8968019)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 184 + 128) = result;
    v_rbx = 0;
    *(unsigned int *)(v_rsp - 184 - 116) = 156;
    *(unsigned int *)(v_rsp - 184 - 60) = 0;
    *(unsigned int *)(v_rsp - 184 - 100) = 0;
    *(unsigned __int64 *)(v_rsp - 184 - 112) = v_rsp - 184 - 32;
    *(unsigned __int8 *)(v_rsp - 184 - 128) = 0;
    *(unsigned int *)(v_rsp - 184 - 48) = 0;
    *(unsigned __int8 *)(v_rsp - 184 - 88) = 0;
    *(unsigned __int8 *)(v_rsp - 184 - 127) = 0;
    *(unsigned int *)(v_rsp - 184 - 84) = 0;
    *(unsigned __int8 *)(v_rsp - 184 - 126) = 0;
    *(unsigned int *)(v_rsp - 184 - 80) = 0;
    *(unsigned __int8 *)(v_rsp - 184 - 125) = 0;
    *(unsigned int *)(v_rsp - 184 - 76) = 0;
    *(unsigned __int8 *)(v_rsp - 184 - 124) = 0;
    *(unsigned int *)(v_rsp - 184 - 44) = 0;
    *(unsigned __int8 *)(v_rsp - 184 - 123) = 0;
    *(unsigned int *)(v_rsp - 184 - 40) = 0;
    *(unsigned __int8 *)(v_rsp - 184 - 87) = 0;
    *(unsigned int *)(v_rsp - 184 - 72) = 0;
    *(unsigned __int8 *)(v_rsp - 184 - 122) = 0;
    *(unsigned int *)(v_rsp - 184 - 68) = 0;
    *(unsigned __int8 *)(v_rsp - 184 - 121) = 0;
    *(unsigned __int8 *)(v_rsp - 184 - 120) = 0;
    *(unsigned __int8 *)(v_rsp - 184 - 119) = 0;
    result = DbgPrintEx(v_rbx + 127, v_rbx + 2, v_rip + 1356043, a1 + 56);
    *(unsigned int *)(v_rsp - 184 - 64) = 0xAA00A8ULL;
    *(unsigned __int64 *)(v_rsp - 184 - 56) = v_rip + 1354218;
    *(unsigned int *)(v_rsp - 184 - 104) = 0x240022ULL;
    *(unsigned __int64 *)(v_rsp - 184 - 96) = v_rip + 1356228;
    v_stack_m198 = v_rsp - 184 - 128;
    result = CcQueryRegKeyValue(v_rsp - 184 - 64, v_rsp - 184 - 104, v_rsp - 184 - 116, v_rsp - 184 - 112);
    v_r13 = 0;
    v_r14 = 0;
    if (!(sign_flag)) {
        a1 = *(unsigned __int64 *)(v_rsp - 184 - 112);
        result = *(unsigned int *)(a1 + 8);
        v_r13 = *(unsigned int *)(result + a1 * 1);
        v_r14 = 0;
        if (((unsigned int)(v_r13)) < 3) { v_r14 = (unsigned int)(v_rbx + 1); }
    }
    *(unsigned int *)(v_rsp - 184 - 104) = 0x3E003CULL;
    *(unsigned __int64 *)(v_rsp - 184 - 96) = v_rip + 1356206;
    v_stack_m198 = v_rsp - 184 - 128;
    result = CcQueryRegKeyValue(v_rsp - 184 - 64, v_rsp - 184 - 104, v_rsp - 184 - 116, v_rsp - 184 - 112);
    if (!(sign_flag)) {
        a1 = *(unsigned __int64 *)(v_rsp - 184 - 112);
        *(unsigned __int8 *)(v_rsp - 184 - 88) = (unsigned __int8)(v_rbx + 1);
        result = *(unsigned int *)(a1 + 8);
        result = *(unsigned int *)(result + a1 * 1);
        *(unsigned int *)(v_rsp - 184 - 48) = (unsigned int)(result);
    }
    *(unsigned int *)(v_rsp - 184 - 104) = 0x1E001CULL;
    *(unsigned __int64 *)(v_rsp - 184 - 96) = v_rip + 1355993;
    v_stack_m198 = v_rsp - 184 - 128;
    result = CcQueryRegKeyValue(v_rsp - 184 - 64, v_rsp - 184 - 104, v_rsp - 184 - 116, v_rsp - 184 - 112);
    v_r15 = 0;
    if (!(sign_flag)) {
        a1 = *(unsigned __int64 *)(v_rsp - 184 - 112);
        *(unsigned __int8 *)(v_rsp - 184 - 127) = (unsigned __int8)(v_rbx + 1);
        result = *(unsigned int *)(a1 + 8);
        v_r15 = *(unsigned int *)(result + a1 * 1);
    }
    *(unsigned int *)(v_rsp - 184 - 104) = 0x380036ULL;
    *(unsigned __int64 *)(v_rsp - 184 - 96) = v_rip + 1355958;
    v_stack_m198 = v_rsp - 184 - 128;
    result = CcQueryRegKeyValue(v_rsp - 184 - 64, v_rsp - 184 - 104, v_rsp - 184 - 116, v_rsp - 184 - 112);
    if (!(sign_flag)) {
        a1 = *(unsigned __int64 *)(v_rsp - 184 - 112);
        *(unsigned __int8 *)(v_rsp - 184 - 126) = (unsigned __int8)(v_rbx + 1);
        result = *(unsigned int *)(a1 + 8);
        result = *(unsigned int *)(result + a1 * 1);
        *(unsigned int *)(v_rsp - 184 - 84) = (unsigned int)(result);
    }
    *(unsigned int *)(v_rsp - 184 - 104) = 0x2C002AULL;
    *(unsigned __int64 *)(v_rsp - 184 - 96) = v_rip + 1356209;
    v_stack_m198 = v_rsp - 184 - 128;
    result = CcQueryRegKeyValue(v_rsp - 184 - 64, v_rsp - 184 - 104, v_rsp - 184 - 116, v_rsp - 184 - 112);
    if (!(sign_flag)) {
        a1 = *(unsigned __int64 *)(v_rsp - 184 - 112);
        *(unsigned __int8 *)(v_rsp - 184 - 125) = (unsigned __int8)(v_rbx + 1);
        result = *(unsigned int *)(a1 + 8);
        result = *(unsigned int *)(result + a1 * 1);
        *(unsigned int *)(v_rsp - 184 - 80) = (unsigned int)(result);
    }
    *(unsigned int *)(v_rsp - 184 - 104) = 0x240022ULL;
    *(unsigned __int64 *)(v_rsp - 184 - 96) = v_rip + 1356188;
    v_stack_m198 = v_rsp - 184 - 128;
    result = CcQueryRegKeyValue(v_rsp - 184 - 64, v_rsp - 184 - 104, v_rsp - 184 - 116, v_rsp - 184 - 112);
    if (!(sign_flag)) {
        a1 = *(unsigned __int64 *)(v_rsp - 184 - 112);
        *(unsigned __int8 *)(v_rsp - 184 - 124) = (unsigned __int8)(v_rbx + 1);
        result = *(unsigned int *)(a1 + 8);
        result = *(unsigned int *)(result + a1 * 1);
        *(unsigned int *)(v_rsp - 184 - 76) = (unsigned int)(result);
    }
    *(unsigned int *)(v_rsp - 184 - 104) = 0x420040ULL;
    *(unsigned __int64 *)(v_rsp - 184 - 96) = v_rip + 1355927;
    v_stack_m198 = v_rsp - 184 - 128;
    result = CcQueryRegKeyValue(v_rsp - 184 - 64, v_rsp - 184 - 104, v_rsp - 184 - 116, v_rsp - 184 - 112);
    if (!(sign_flag)) {
        a1 = *(unsigned __int64 *)(v_rsp - 184 - 112);
        *(unsigned __int8 *)(v_rsp - 184 - 123) = (unsigned __int8)(v_rbx + 1);
        result = *(unsigned int *)(a1 + 8);
        result = *(unsigned int *)(result + a1 * 1);
        *(unsigned int *)(v_rsp - 184 - 44) = (unsigned int)(result);
    }
    *(unsigned int *)(v_rsp - 184 - 104) = 0x40003EULL;
    *(unsigned __int64 *)(v_rsp - 184 - 96) = v_rip + 1355938;
    v_stack_m198 = v_rsp - 184 - 128;
    result = CcQueryRegKeyValue(v_rsp - 184 - 64, v_rsp - 184 - 104, v_rsp - 184 - 116, v_rsp - 184 - 112);
    if (!(sign_flag)) {
        a1 = *(unsigned __int64 *)(v_rsp - 184 - 112);
        *(unsigned __int8 *)(v_rsp - 184 - 87) = (unsigned __int8)(v_rbx + 1);
        result = *(unsigned int *)(a1 + 8);
        a2 = *(unsigned int *)(result + a1 * 1);
        *(unsigned int *)(v_rsp - 184 - 40) = (unsigned int)(a2);
    }
    *(unsigned int *)(v_rsp - 184 - 104) = 0x420040ULL;
    *(unsigned __int64 *)(v_rsp - 184 - 96) = v_rip + 1356141;
    v_stack_m198 = v_rsp - 184 - 128;
    result = CcQueryRegKeyValue(v_rsp - 184 - 64, v_rsp - 184 - 104, v_rsp - 184 - 116, v_rsp - 184 - 112);
    if (!(sign_flag)) {
        a1 = *(unsigned __int64 *)(v_rsp - 184 - 112);
        *(unsigned __int8 *)(v_rsp - 184 - 122) = (unsigned __int8)(v_rbx + 1);
        result = *(unsigned int *)(a1 + 8);
        result = *(unsigned int *)(result + a1 * 1);
        *(unsigned int *)(v_rsp - 184 - 72) = (unsigned int)(result);
    }
    *(unsigned int *)(v_rsp - 184 - 104) = 0x2C002AULL;
    *(unsigned __int64 *)(v_rsp - 184 - 96) = v_rip + 1356152;
    v_stack_m198 = v_rsp - 184 - 128;
    result = CcQueryRegKeyValue(v_rsp - 184 - 64, v_rsp - 184 - 104, v_rsp - 184 - 116, v_rsp - 184 - 112);
    if (!(sign_flag)) {
        a1 = *(unsigned __int64 *)(v_rsp - 184 - 112);
        *(unsigned __int8 *)(v_rsp - 184 - 121) = (unsigned __int8)(v_rbx + 1);
        result = *(unsigned int *)(a1 + 8);
        result = *(unsigned int *)(result + a1 * 1);
        *(unsigned int *)(v_rsp - 184 - 68) = (unsigned int)(result);
    }
    *(unsigned int *)(v_rsp - 184 - 104) = 0x2A0028ULL;
    *(unsigned __int64 *)(v_rsp - 184 - 96) = v_rip + 1355891;
    v_stack_m198 = v_rsp - 184 - 128;
    result = CcQueryRegKeyValue(v_rsp - 184 - 64, v_rsp - 184 - 104, v_rsp - 184 - 116, v_rsp - 184 - 112);
    v_rdi = 0;
    if (!(sign_flag)) {
        a1 = *(unsigned __int64 *)(v_rsp - 184 - 112);
        *(unsigned __int8 *)(v_rsp - 184 - 120) = (unsigned __int8)(v_rbx + 1);
        result = *(unsigned int *)(a1 + 8);
        v_rdi = *(unsigned int *)(result + a1 * 1);
    }
    *(unsigned int *)(v_rsp - 184 - 104) = 0x340032ULL;
    *(unsigned __int64 *)(v_rsp - 184 - 96) = v_rip + 1355873;
    v_stack_m198 = v_rsp - 184 - 128;
    result = CcQueryRegKeyValue(v_rsp - 184 - 64, v_rsp - 184 - 104, v_rsp - 184 - 116, v_rsp - 184 - 112);
    v_r12 = 0;
    if (!(sign_flag)) {
        result = *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 184 - 112) + 8);
        *(unsigned __int8 *)(v_rsp - 184 - 119) = 1;
        v_r12 = *(unsigned int *)(result + *(unsigned __int64 *)(v_rsp - 184 - 112) * 1);
    }
    result = 0;
    v_r10 = v_rip + 1356594;
    if ((*(unsigned __int8 *)(v_rsp - 184 - 124)) == 0) { v_r10 = v_rip + 1356620; }
    v_stack_m148 = v_r10;
    a4 = v_rip + 1356594;
    if ((*(unsigned __int8 *)(v_rsp - 184 - 125)) == 0) { a4 = v_rip + 1356620; }
    v_stack_m150 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 184 - 76)));
    v_stack_m158 = a4;
    a3 = v_rip + 1356594;
    if ((*(unsigned __int8 *)(v_rsp - 184 - 126)) == 0) { a3 = v_rip + 1356620; }
    v_stack_m160 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 184 - 80)));
    a2 = v_rip + 1356594;
    if ((*(unsigned __int8 *)(v_rsp - 184 - 127)) == 0) { a2 = v_rip + 1356620; }
    v_stack_m168 = a3;
    a1 = v_rip + 1356594;
    if ((*(unsigned __int8 *)(v_rsp - 184 - 88)) == 0) { a1 = v_rip + 1356620; }
    v_stack_m170 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 184 - 84)));
    v_stack_m178 = a2;
    v_stack_m180 = (unsigned int)(v_r15);
    v_stack_m188 = a1;
    result = v_rip + 1356594;
    if ((unsigned __int8)(v_r14) == 0) { result = v_rip + 1356620; }
    v_stack_m190 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 184 - 48)));
    v_stack_m198 = result;
    result = DbgPrintEx(2 + 125, 2, v_rip + 1355876, (unsigned int)((unsigned int)(v_r13)));
    v_r10 = 0;
    a3 = v_rip + 1356594;
    if ((*(unsigned __int8 *)(v_rsp - 184 - 119)) == 0) { a3 = v_rip + 1356451; }
    v_stack_m158 = a3;
    a1 = v_rip + 1356594;
    if ((*(unsigned __int8 *)(v_rsp - 184 - 120)) == 0) { a1 = v_rip + 1356451; }
    v_stack_m160 = (unsigned int)(v_r12);
    v_stack_m168 = a1;
    a2 = v_rip + 1356594;
    if ((*(unsigned __int8 *)(v_rsp - 184 - 121)) == 0) { a2 = v_rip + 1356451; }
    v_stack_m170 = (unsigned int)(v_rdi);
    v_stack_m178 = a2;
    result = v_rip + 1356594;
    if ((*(unsigned __int8 *)(v_rsp - 184 - 122)) == 0) { result = v_rip + 1356451; }
    v_stack_m180 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 184 - 68)));
    v_stack_m188 = result;
    v_rbx = v_rip + 1356594;
    if ((*(unsigned __int8 *)(v_rsp - 184 - 123)) == 0) { v_rbx = v_rip + 1356451; }
    v_stack_m190 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 184 - 72)));
    v_stack_m198 = v_rbx;
    result = DbgPrintEx(v_r10 + 2 + 125, v_r10 + 2, v_rip + 1356127, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 184 - 44)))));
    if ((*(unsigned __int8 *)(v_rsp - 184 - 128)) != 0) {
        a2 = 0x78666343ULL;
        a1 = *(unsigned __int64 *)(v_rsp - 184 - 112);
        result = ExFreePoolWithTag(a1, a2, v_rip + 1356127, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 184 - 44)))));
    }
    v_rsi = 0;
    if ((unsigned __int8)(v_r14) != 0) {
        *(unsigned int *)(v_rip + 9340549) = (unsigned int)(v_r13);
    }
    if ((*(unsigned __int8 *)(v_rsp - 184 - 127)) == 0) goto loc_0057D52D;
    if ((unsigned int)(v_r15) == 0) goto loc_0057D527;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) << (10));
    *(unsigned int *)(v_rip + 9340466) = (unsigned int)(result);
    if (((unsigned int)(result)) <= ((unsigned int)(v_r15))) {
        *(unsigned int *)(v_rip + 9340455) = 0;
    }
    if ((*(unsigned __int8 *)(v_rsp - 184 - 126)) != 0) {
        a2 = *(unsigned int *)(v_rsp - 184 - 84);
        a1 = 0;
        result = a2 - 1;
        if (((unsigned int)(result)) <= 99) { a1 = (unsigned int)(a2); }
        *(unsigned int *)(v_rip + 9340437) = (unsigned int)(a1);
    }
    if ((*(unsigned __int8 *)(v_rsp - 184 - 125)) == 0) goto loc_0057D55A;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 184 - 80))) != 0) {
        *(unsigned int *)(v_rip + 9340434) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 184 - 80)));
    }
    if ((*(unsigned __int8 *)(v_rsp - 184 - 124)) == 0) goto loc_0057D573;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 184 - 76)) - 1)) <= 0x7FFFULL) {
        *(unsigned int *)(v_rip + 8966909) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 184 - 76)));
    }
    if ((*(unsigned __int8 *)(v_rsp - 184 - 123)) == 0) goto loc_0057D58B;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 184 - 44))) != 0) {
        a1 = ((unsigned int)(*(unsigned int *)(v_rsp - 184 - 76))) * ((unsigned int)(*(unsigned int *)(v_rsp - 184 - 44)));
        *(unsigned __int64 *)(v_rip + 10558709) = a1;
    }
    if ((*(unsigned __int8 *)(v_rsp - 184 - 87)) == 0) goto loc_0057D5A6;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 184 - 40))) != 0) {
        a1 = (a1) * ((unsigned int)(*(unsigned int *)(v_rsp - 184 - 40)));
        *(unsigned __int64 *)(v_rip + 10558690) = a1;
    }
    if ((*(unsigned __int8 *)(v_rsp - 184 - 122)) == 0) goto loc_0057D5C1;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 184 - 72))) != 0) {
        a1 = (a1) * ((unsigned int)(*(unsigned int *)(v_rsp - 184 - 72)));
        *(unsigned __int64 *)(v_rip + 10558671) = a1;
    }
    if ((*(unsigned __int8 *)(v_rsp - 184 - 121)) != 0) {
    }
    if ((*(unsigned __int8 *)(v_rsp - 184 - 120)) == 0) goto loc_0057D62A;
    if (((unsigned int)(v_rdi)) > 1) goto loc_0057D608;
    if ((unsigned int)(v_rdi) == 0) goto loc_0057D62A;
    if ((*(unsigned __int8 *)(v_rip + 9340312)) != 0) goto loc_0057D62A;
    result = DbgPrintEx(2 + 125, 2, v_rip + 1356338, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 184 - 44)))));
    goto loc_0057D62A;
loc_0057D608:
    v_stack_m198 = (unsigned int)(*(unsigned __int8 *)(v_rip + 9340295));
    result = DbgPrintEx(2 + 125, 2, v_rip + 1356426, (unsigned int)((unsigned int)(v_rdi)));
loc_0057D62A:
    if ((*(unsigned __int8 *)(v_rsp - 184 - 119)) == 0) goto loc_0057D697;
    if ((unsigned int)(v_r12) != 0) goto loc_0057D63E;
    *(unsigned __int8 *)(v_rip + 9340249) = 0;
    goto loc_0057D697;
loc_0057D63E:
    if (((unsigned int)(v_r12)) != 1) goto loc_0057D675;
    if ((*(unsigned __int8 *)(v_rip + 9340221)) == 0) goto loc_0057D65F;
    if ((*(unsigned __int8 *)(v_rip + 9340226)) == 0) goto loc_0057D65F;
    *(unsigned __int8 *)(v_rip + 9340216) = (unsigned __int8)(v_r12);
    goto loc_0057D697;
loc_0057D65F:
    result = DbgPrintEx(2 + 125, 2, v_rip + 1355957, (unsigned int)((unsigned int)(v_rdi)));
    goto loc_0057D697;
loc_0057D675:
    v_stack_m198 = (unsigned int)(*(unsigned __int8 *)(v_rip + 9340185));
    result = DbgPrintEx(2 + 125, 2, v_rip + 1356077, (unsigned int)((unsigned int)(v_r12)));
loc_0057D697:
    a1 = (*(unsigned __int64 *)(v_rsp - 184 + 128)) ^ (v_rsp);
    result = _security_check_cookie(a1, 2, v_rip + 1356077, (unsigned int)((unsigned int)(v_r12)));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CcUpdateDynamicRegistrySettings(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m148;
    uint32_t v_stack_m150;
    uint64_t v_stack_m158;
    uint32_t v_stack_m160;
    uint64_t v_stack_m168;
    uint32_t v_stack_m170;
    uint64_t v_stack_m178;
    uint32_t v_stack_m180;
    uint64_t v_stack_m188;
    uint32_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m28;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (400);
    result = (*(uint64_t *)(v_rip + 0x88D753)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0xB8 + 0x80) = result;
    local_rbx = 0;
    *(uint32_t *)(local_rsp - 0xB8 - 0x74) = 156;
    *(uint32_t *)(local_rsp - 0xB8 - 0x3C) = 0;
    *(uint32_t *)(local_rsp - 0xB8 - 0x64) = 0;
    *(uint64_t *)(local_rsp - 0xB8 - 0x70) = local_rsp - 184 - 32;
    *(uint8_t *)(local_rsp - 0xB8 - 0x80) = 0;
    *(uint32_t *)(local_rsp - 0xB8 - 0x30) = 0;
    *(uint8_t *)(local_rsp - 0xB8 - 0x58) = 0;
    *(uint8_t *)(local_rsp - 0xB8 - 0x7F) = 0;
    *(uint32_t *)(local_rsp - 0xB8 - 0x54) = 0;
    *(uint8_t *)(local_rsp - 0xB8 - 0x7E) = 0;
    *(uint32_t *)(local_rsp - 0xB8 - 0x50) = 0;
    *(uint8_t *)(local_rsp - 0xB8 - 0x7D) = 0;
    *(uint32_t *)(local_rsp - 0xB8 - 0x4C) = 0;
    *(uint8_t *)(local_rsp - 0xB8 - 0x7C) = 0;
    *(uint32_t *)(local_rsp - 0xB8 - 0x2C) = 0;
    *(uint8_t *)(local_rsp - 0xB8 - 0x7B) = 0;
    *(uint32_t *)(local_rsp - 0xB8 - 0x28) = 0;
    *(uint8_t *)(local_rsp - 0xB8 - 0x57) = 0;
    *(uint32_t *)(local_rsp - 0xB8 - 0x48) = 0;
    *(uint8_t *)(local_rsp - 0xB8 - 0x7A) = 0;
    *(uint32_t *)(local_rsp - 0xB8 - 0x44) = 0;
    *(uint8_t *)(local_rsp - 0xB8 - 0x79) = 0;
    *(uint8_t *)(local_rsp - 0xB8 - 0x78) = 0;
    *(uint8_t *)(local_rsp - 0xB8 - 0x77) = 0;
    result = DbgPrintEx(local_rbx + 127, local_rbx + 2, v_rip + 1356043, Arg1 + 56);
    *(uint32_t *)(local_rsp - 0xB8 - 0x40) = 0xAA00A8ULL;
    *(uint64_t *)(local_rsp - 0xB8 - 0x38) = v_rip + 1354218;
    *(uint32_t *)(local_rsp - 0xB8 - 0x68) = 0x240022ULL;
    *(uint64_t *)(local_rsp - 0xB8 - 0x60) = v_rip + 1356228;
    v_stack_m198 = local_rsp - 184 - 128;
    result = CcQueryRegKeyValue(local_rsp - 184 - 64, local_rsp - 184 - 104, local_rsp - 184 - 116, local_rsp - 184 - 112);
    local_r13 = 0;
    local_r14 = 0;
    if (!(sign_flag)) {
        Arg1 = *(uint64_t *)(local_rsp - 0xB8 - 0x70);
        result = *(uint32_t *)(arg1 + 0x8);
        local_r13 = *(uint32_t *)(result + arg1 * 1);
        local_r14 = 0;
        if (((uint32_t)(local_r13)) < 3) { local_r14 = (uint32_t)(local_rbx + 1); }
    }
    *(uint32_t *)(local_rsp - 0xB8 - 0x68) = 0x3E003CULL;
    *(uint64_t *)(local_rsp - 0xB8 - 0x60) = v_rip + 1356206;
    v_stack_m198 = local_rsp - 184 - 128;
    result = CcQueryRegKeyValue(local_rsp - 184 - 64, local_rsp - 184 - 104, local_rsp - 184 - 116, local_rsp - 184 - 112);
    if (!(sign_flag)) {
        Arg1 = *(uint64_t *)(local_rsp - 0xB8 - 0x70);
        *(uint8_t *)(local_rsp - 0xB8 - 0x58) = (uint8_t)(local_rbx + 1);
        result = *(uint32_t *)(arg1 + 0x8);
        result = *(uint32_t *)(result + arg1 * 1);
        *(uint32_t *)(local_rsp - 0xB8 - 0x30) = (uint32_t)(result);
    }
    *(uint32_t *)(local_rsp - 0xB8 - 0x68) = 0x1E001CULL;
    *(uint64_t *)(local_rsp - 0xB8 - 0x60) = v_rip + 1355993;
    v_stack_m198 = local_rsp - 184 - 128;
    result = CcQueryRegKeyValue(local_rsp - 184 - 64, local_rsp - 184 - 104, local_rsp - 184 - 116, local_rsp - 184 - 112);
    local_r15 = 0;
    if (!(sign_flag)) {
        Arg1 = *(uint64_t *)(local_rsp - 0xB8 - 0x70);
        *(uint8_t *)(local_rsp - 0xB8 - 0x7F) = (uint8_t)(local_rbx + 1);
        result = *(uint32_t *)(arg1 + 0x8);
        local_r15 = *(uint32_t *)(result + arg1 * 1);
    }
    *(uint32_t *)(local_rsp - 0xB8 - 0x68) = 0x380036ULL;
    *(uint64_t *)(local_rsp - 0xB8 - 0x60) = v_rip + 1355958;
    v_stack_m198 = local_rsp - 184 - 128;
    result = CcQueryRegKeyValue(local_rsp - 184 - 64, local_rsp - 184 - 104, local_rsp - 184 - 116, local_rsp - 184 - 112);
    if (!(sign_flag)) {
        Arg1 = *(uint64_t *)(local_rsp - 0xB8 - 0x70);
        *(uint8_t *)(local_rsp - 0xB8 - 0x7E) = (uint8_t)(local_rbx + 1);
        result = *(uint32_t *)(arg1 + 0x8);
        result = *(uint32_t *)(result + arg1 * 1);
        *(uint32_t *)(local_rsp - 0xB8 - 0x54) = (uint32_t)(result);
    }
    *(uint32_t *)(local_rsp - 0xB8 - 0x68) = 0x2C002AULL;
    *(uint64_t *)(local_rsp - 0xB8 - 0x60) = v_rip + 1356209;
    v_stack_m198 = local_rsp - 184 - 128;
    result = CcQueryRegKeyValue(local_rsp - 184 - 64, local_rsp - 184 - 104, local_rsp - 184 - 116, local_rsp - 184 - 112);
    if (!(sign_flag)) {
        Arg1 = *(uint64_t *)(local_rsp - 0xB8 - 0x70);
        *(uint8_t *)(local_rsp - 0xB8 - 0x7D) = (uint8_t)(local_rbx + 1);
        result = *(uint32_t *)(arg1 + 0x8);
        result = *(uint32_t *)(result + arg1 * 1);
        *(uint32_t *)(local_rsp - 0xB8 - 0x50) = (uint32_t)(result);
    }
    *(uint32_t *)(local_rsp - 0xB8 - 0x68) = 0x240022ULL;
    *(uint64_t *)(local_rsp - 0xB8 - 0x60) = v_rip + 1356188;
    v_stack_m198 = local_rsp - 184 - 128;
    result = CcQueryRegKeyValue(local_rsp - 184 - 64, local_rsp - 184 - 104, local_rsp - 184 - 116, local_rsp - 184 - 112);
    if (!(sign_flag)) {
        Arg1 = *(uint64_t *)(local_rsp - 0xB8 - 0x70);
        *(uint8_t *)(local_rsp - 0xB8 - 0x7C) = (uint8_t)(local_rbx + 1);
        result = *(uint32_t *)(arg1 + 0x8);
        result = *(uint32_t *)(result + arg1 * 1);
        *(uint32_t *)(local_rsp - 0xB8 - 0x4C) = (uint32_t)(result);
    }
    *(uint32_t *)(local_rsp - 0xB8 - 0x68) = 0x420040ULL;
    *(uint64_t *)(local_rsp - 0xB8 - 0x60) = v_rip + 1355927;
    v_stack_m198 = local_rsp - 184 - 128;
    result = CcQueryRegKeyValue(local_rsp - 184 - 64, local_rsp - 184 - 104, local_rsp - 184 - 116, local_rsp - 184 - 112);
    if (!(sign_flag)) {
        Arg1 = *(uint64_t *)(local_rsp - 0xB8 - 0x70);
        *(uint8_t *)(local_rsp - 0xB8 - 0x7B) = (uint8_t)(local_rbx + 1);
        result = *(uint32_t *)(arg1 + 0x8);
        result = *(uint32_t *)(result + arg1 * 1);
        *(uint32_t *)(local_rsp - 0xB8 - 0x2C) = (uint32_t)(result);
    }
    *(uint32_t *)(local_rsp - 0xB8 - 0x68) = 0x40003EULL;
    *(uint64_t *)(local_rsp - 0xB8 - 0x60) = v_rip + 1355938;
    v_stack_m198 = local_rsp - 184 - 128;
    result = CcQueryRegKeyValue(local_rsp - 184 - 64, local_rsp - 184 - 104, local_rsp - 184 - 116, local_rsp - 184 - 112);
    if (!(sign_flag)) {
        Arg1 = *(uint64_t *)(local_rsp - 0xB8 - 0x70);
        *(uint8_t *)(local_rsp - 0xB8 - 0x57) = (uint8_t)(local_rbx + 1);
        result = *(uint32_t *)(arg1 + 0x8);
        a2 = *(uint32_t *)(result + arg1 * 1);
        *(uint32_t *)(local_rsp - 0xB8 - 0x28) = (uint32_t)(a2);
    }
    *(uint32_t *)(local_rsp - 0xB8 - 0x68) = 0x420040ULL;
    *(uint64_t *)(local_rsp - 0xB8 - 0x60) = v_rip + 1356141;
    v_stack_m198 = local_rsp - 184 - 128;
    result = CcQueryRegKeyValue(local_rsp - 184 - 64, local_rsp - 184 - 104, local_rsp - 184 - 116, local_rsp - 184 - 112);
    if (!(sign_flag)) {
        Arg1 = *(uint64_t *)(local_rsp - 0xB8 - 0x70);
        *(uint8_t *)(local_rsp - 0xB8 - 0x7A) = (uint8_t)(local_rbx + 1);
        result = *(uint32_t *)(arg1 + 0x8);
        result = *(uint32_t *)(result + arg1 * 1);
        *(uint32_t *)(local_rsp - 0xB8 - 0x48) = (uint32_t)(result);
    }
    *(uint32_t *)(local_rsp - 0xB8 - 0x68) = 0x2C002AULL;
    *(uint64_t *)(local_rsp - 0xB8 - 0x60) = v_rip + 1356152;
    v_stack_m198 = local_rsp - 184 - 128;
    result = CcQueryRegKeyValue(local_rsp - 184 - 64, local_rsp - 184 - 104, local_rsp - 184 - 116, local_rsp - 184 - 112);
    if (!(sign_flag)) {
        Arg1 = *(uint64_t *)(local_rsp - 0xB8 - 0x70);
        *(uint8_t *)(local_rsp - 0xB8 - 0x79) = (uint8_t)(local_rbx + 1);
        result = *(uint32_t *)(arg1 + 0x8);
        result = *(uint32_t *)(result + arg1 * 1);
        *(uint32_t *)(local_rsp - 0xB8 - 0x44) = (uint32_t)(result);
    }
    *(uint32_t *)(local_rsp - 0xB8 - 0x68) = 0x2A0028ULL;
    *(uint64_t *)(local_rsp - 0xB8 - 0x60) = v_rip + 1355891;
    v_stack_m198 = local_rsp - 184 - 128;
    result = CcQueryRegKeyValue(local_rsp - 184 - 64, local_rsp - 184 - 104, local_rsp - 184 - 116, local_rsp - 184 - 112);
    local_rdi = 0;
    if (!(sign_flag)) {
        Arg1 = *(uint64_t *)(local_rsp - 0xB8 - 0x70);
        *(uint8_t *)(local_rsp - 0xB8 - 0x78) = (uint8_t)(local_rbx + 1);
        result = *(uint32_t *)(arg1 + 0x8);
        local_rdi = *(uint32_t *)(result + arg1 * 1);
    }
    *(uint32_t *)(local_rsp - 0xB8 - 0x68) = 0x340032ULL;
    *(uint64_t *)(local_rsp - 0xB8 - 0x60) = v_rip + 1355873;
    v_stack_m198 = local_rsp - 184 - 128;
    result = CcQueryRegKeyValue(local_rsp - 184 - 64, local_rsp - 184 - 104, local_rsp - 184 - 116, local_rsp - 184 - 112);
    local_r12 = 0;
    if (!(sign_flag)) {
        result = *(uint32_t *)(*(uint64_t *)(local_rsp - 0xB8 - 0x70) + 0x8);
        *(uint8_t *)(local_rsp - 0xB8 - 0x77) = 1;
        local_r12 = *(uint32_t *)(result + *(uint64_t *)(local_rsp - 0xB8 - 0x70) * 1);
    }
    result = 0;
    local_r10 = v_rip + 1356594;
    if ((*(uint8_t *)(local_rsp - 0xB8 - 0x7C)) == 0) { local_r10 = v_rip + 1356620; }
    v_stack_m148 = local_r10;
    a4 = v_rip + 1356594;
    if ((*(uint8_t *)(local_rsp - 0xB8 - 0x7D)) == 0) { a4 = v_rip + 1356620; }
    v_stack_m150 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xB8 - 0x4C)));
    v_stack_m158 = a4;
    a3 = v_rip + 1356594;
    if ((*(uint8_t *)(local_rsp - 0xB8 - 0x7E)) == 0) { a3 = v_rip + 1356620; }
    v_stack_m160 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xB8 - 0x50)));
    a2 = v_rip + 1356594;
    if ((*(uint8_t *)(local_rsp - 0xB8 - 0x7F)) == 0) { a2 = v_rip + 1356620; }
    v_stack_m168 = a3;
    Arg1 = v_rip + 1356594;
    if ((*(uint8_t *)(local_rsp - 0xB8 - 0x58)) == 0) { Arg1 = v_rip + 1356620; }
    v_stack_m170 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xB8 - 0x54)));
    v_stack_m178 = a2;
    v_stack_m180 = (uint32_t)(local_r15);
    v_stack_m188 = Arg1;
    result = v_rip + 1356594;
    if ((uint8_t)(local_r14) == 0) { result = v_rip + 1356620; }
    v_stack_m190 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xB8 - 0x30)));
    v_stack_m198 = result;
    result = DbgPrintEx(2 + 125, 2, v_rip + 1355876, (uint32_t)((uint32_t)(local_r13)));
    local_r10 = 0;
    a3 = v_rip + 1356594;
    if ((*(uint8_t *)(local_rsp - 0xB8 - 0x77)) == 0) { a3 = v_rip + 1356451; }
    v_stack_m158 = a3;
    Arg1 = v_rip + 1356594;
    if ((*(uint8_t *)(local_rsp - 0xB8 - 0x78)) == 0) { Arg1 = v_rip + 1356451; }
    v_stack_m160 = (uint32_t)(local_r12);
    v_stack_m168 = Arg1;
    a2 = v_rip + 1356594;
    if ((*(uint8_t *)(local_rsp - 0xB8 - 0x79)) == 0) { a2 = v_rip + 1356451; }
    v_stack_m170 = (uint32_t)(local_rdi);
    v_stack_m178 = a2;
    result = v_rip + 1356594;
    if ((*(uint8_t *)(local_rsp - 0xB8 - 0x7A)) == 0) { result = v_rip + 1356451; }
    v_stack_m180 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xB8 - 0x44)));
    v_stack_m188 = result;
    local_rbx = v_rip + 1356594;
    if ((*(uint8_t *)(local_rsp - 0xB8 - 0x7B)) == 0) { local_rbx = v_rip + 1356451; }
    v_stack_m190 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xB8 - 0x48)));
    v_stack_m198 = local_rbx;
    result = DbgPrintEx(local_r10 + 2 + 125, local_r10 + 2, v_rip + 1356127, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xB8 - 0x2C)))));
    if ((*(uint8_t *)(local_rsp - 0xB8 - 0x80)) != 0) {
        a2 = 0x78666343ULL;
        Arg1 = *(uint64_t *)(local_rsp - 0xB8 - 0x70);
        result = ExFreePoolWithTag(Arg1, a2, v_rip + 1356127, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xB8 - 0x2C)))));
    }
    local_rsi = 0;
    if ((uint8_t)(local_r14) != 0) {
        *(uint32_t *)(v_rip + 0x8E8685) = (uint32_t)(local_r13);
    }
    if ((*(uint8_t *)(local_rsp - 0xB8 - 0x7F)) == 0) goto loc_0057D52D;
    if ((uint32_t)(local_r15) == 0) goto loc_0057D527;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) << (10));
    *(uint32_t *)(v_rip + 0x8E8632) = (uint32_t)(result);
    if (((uint32_t)(result)) <= ((uint32_t)(local_r15))) {
        *(uint32_t *)(v_rip + 0x8E8627) = 0;
    }
    if ((*(uint8_t *)(local_rsp - 0xB8 - 0x7E)) != 0) {
        a2 = *(uint32_t *)(local_rsp - 0xB8 - 0x54);
        Arg1 = 0;
        result = a2 - 1;
        if (((uint32_t)(result)) <= 99) { Arg1 = (uint32_t)(a2); }
        *(uint32_t *)(v_rip + 0x8E8615) = (uint32_t)(Arg1);
    }
    if ((*(uint8_t *)(local_rsp - 0xB8 - 0x7D)) == 0) goto loc_0057D55A;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xB8 - 0x50))) != 0) {
        *(uint32_t *)(v_rip + 0x8E8612) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xB8 - 0x50)));
    }
    if ((*(uint8_t *)(local_rsp - 0xB8 - 0x7C)) == 0) goto loc_0057D573;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xB8 - 0x4C)) - 1)) <= 0x7FFFULL) {
        *(uint32_t *)(v_rip + 0x88D2FD) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xB8 - 0x4C)));
    }
    if ((*(uint8_t *)(local_rsp - 0xB8 - 0x7B)) == 0) goto loc_0057D58B;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xB8 - 0x2C))) != 0) {
        Arg1 = ((uint32_t)(*(uint32_t *)(local_rsp - 0xB8 - 0x4C))) * ((uint32_t)(*(uint32_t *)(local_rsp - 0xB8 - 0x2C)));
        *(void **)(v_rip + 0xA11CF5) = Arg1;
    }
    if ((*(uint8_t *)(local_rsp - 0xB8 - 0x57)) == 0) goto loc_0057D5A6;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xB8 - 0x28))) != 0) {
        Arg1 = (Arg1) * ((uint32_t)(*(uint32_t *)(local_rsp - 0xB8 - 0x28)));
        *(void **)(v_rip + 0xA11CE2) = Arg1;
    }
    if ((*(uint8_t *)(local_rsp - 0xB8 - 0x7A)) == 0) goto loc_0057D5C1;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xB8 - 0x48))) != 0) {
        Arg1 = (Arg1) * ((uint32_t)(*(uint32_t *)(local_rsp - 0xB8 - 0x48)));
        *(void **)(v_rip + 0xA11CCF) = Arg1;
    }
    if ((*(uint8_t *)(local_rsp - 0xB8 - 0x79)) != 0) {
    }
    if ((*(uint8_t *)(local_rsp - 0xB8 - 0x78)) == 0) goto loc_0057D62A;
    if (((uint32_t)(local_rdi)) > 1) goto loc_0057D608;
    if ((uint32_t)(local_rdi) == 0) goto loc_0057D62A;
    if ((*(uint8_t *)(v_rip + 0x8E8598)) != 0) goto loc_0057D62A;
    result = DbgPrintEx(2 + 125, 2, v_rip + 1356338, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xB8 - 0x2C)))));
    goto loc_0057D62A;
loc_0057D608:
    v_stack_m198 = (uint32_t)(*(uint8_t *)(v_rip + 0x8E8587));
    result = DbgPrintEx(2 + 125, 2, v_rip + 1356426, (uint32_t)((uint32_t)(local_rdi)));
loc_0057D62A:
    if ((*(uint8_t *)(local_rsp - 0xB8 - 0x77)) == 0) goto loc_0057D697;
    if ((uint32_t)(local_r12) != 0) goto loc_0057D63E;
    *(uint8_t *)(v_rip + 0x8E8559) = 0;
    goto loc_0057D697;
loc_0057D63E:
    if (((uint32_t)(local_r12)) != 1) goto loc_0057D675;
    if ((*(uint8_t *)(v_rip + 0x8E853D)) == 0) goto loc_0057D65F;
    if ((*(uint8_t *)(v_rip + 0x8E8542)) == 0) goto loc_0057D65F;
    *(uint8_t *)(v_rip + 0x8E8538) = (uint8_t)(local_r12);
    goto loc_0057D697;
loc_0057D65F:
    result = DbgPrintEx(2 + 125, 2, v_rip + 1355957, (uint32_t)((uint32_t)(local_rdi)));
    goto loc_0057D697;
loc_0057D675:
    v_stack_m198 = (uint32_t)(*(uint8_t *)(v_rip + 0x8E8519));
    result = DbgPrintEx(2 + 125, 2, v_rip + 1356077, (uint32_t)((uint32_t)(local_r12)));
loc_0057D697:
    Arg1 = (*(uint64_t *)(local_rsp - 0xB8 + 0x80)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, 2, v_rip + 1356077, (uint32_t)((uint32_t)(local_r12)));
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x38` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0057CFC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
