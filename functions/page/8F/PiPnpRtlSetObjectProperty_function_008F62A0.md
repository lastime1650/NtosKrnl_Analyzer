# PiPnpRtlSetObjectProperty

- RVA: `0x008F62A0`–`0x008F66E0` (길이 `1,088` bytes)
- VA: `0x00000001408F62A0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0008792C`
- 디코드: `268`개 명령, `1,088/1,088` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **7**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **10**
- RIP 상대 이미지 참조: **21**

### Outgoing calls
- `0x008F63BA` → [PnpSetObjectProperty](PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x008F63FB` → [_CmUpdateDevicePanelInterface](../A0/_CmUpdateDevicePanelInterface_function_00A09FC4.md) (function, `0x00A09FC4`)
- `0x008F642A` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x008F6501` → [CmIsRootEnumeratedDevice](CmIsRootEnumeratedDevice_function_008F6E08.md) (function, `0x008F6E08`)
- `0x008F661B` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x008F664E` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x008F6653` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)

### Direct callers
- [PnpSetDeviceInterfacePropertyData](PnpSetDeviceInterfacePropertyData_function_008F5328.md) at `0x008F5484`
- [PiSwPropertySet](PiSwPropertySet_function_008F5EEC.md) at `0x008F5FA3`
- [PnpSetDevicePropertyData](PnpSetDevicePropertyData_function_008F6114.md) at `0x008F61D5`
- [PiCMSetObjectProperty](../96/PiCMSetObjectProperty_function_00962564.md) at `0x009626AA`
- [PiDqIrpPropertySet](../96/PiDqIrpPropertySet_function_00963770.md) at `0x00963995`
- [PiDevCfgMigrateDevice](../96/PiDevCfgMigrateDevice_function_00963E60.md) at `0x0096414A`
- [PiDevCfgResetDeviceDriverSettings](../96/PiDevCfgResetDeviceDriverSettings_function_00966168.md) at `0x0096621B`
- [PiDevCfgProcessDevice](../97/PiDevCfgProcessDevice_function_00976D34.md) at `0x009772E7`
- [PiDevCfgConfigureDevice](../97/PiDevCfgConfigureDevice_function_00977BB4.md) at `0x00978D3A`
- [PiDevCfgConfigureDevice](../97/PiDevCfgConfigureDevice_function_00977BB4.md) at `0x00978E28`
- [PiDevCfgConfigureDevice](../97/PiDevCfgConfigureDevice_function_00977BB4.md) at `0x00978E8F`
- [PiDevCfgConfigureDevice](../97/PiDevCfgConfigureDevice_function_00977BB4.md) at `0x00979160`
- [PiDevCfgConfigureDevice](../97/PiDevCfgConfigureDevice_function_00977BB4.md) at `0x00979259`
- [PiDevCfgConfigureDevice](../97/PiDevCfgConfigureDevice_function_00977BB4.md) at `0x009792F8`
- [PiDevCfgConfigureDevice](../97/PiDevCfgConfigureDevice_function_00977BB4.md) at `0x00979354`
- [PiDevCfgConfigureDevice](../97/PiDevCfgConfigureDevice_function_00977BB4.md) at `0x009793B0`
- [PiDevCfgConfigureDevice](../97/PiDevCfgConfigureDevice_function_00977BB4.md) at `0x0097945D`
- [PiDevCfgConfigureDevice](../97/PiDevCfgConfigureDevice_function_00977BB4.md) at `0x00979968`
- [PiDevCfgConfigureDevice](../97/PiDevCfgConfigureDevice_function_00977BB4.md) at `0x009799BF`
- [PiDevCfgConfigureDevice](../97/PiDevCfgConfigureDevice_function_00977BB4.md) at `0x00979CF9`
- [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) at `0x00A8DBB2`

### Static image references
- `0x008F62B9` → RVA `0x00E0A740` (`.data`; read)
- `0x008F6351` → RVA `0x00011490` (`.rdata`; read)
- `0x008F6362` → RVA `0x00011498` (`.rdata`; read)
- `0x008F63D8` → RVA `0x00014DB0` (`.rdata`; read)
- `0x008F63E5` → RVA `0x00014DB8` (`.rdata`; read)
- `0x008F6447` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x008F6491` → RVA `0x00011530` (`.rdata`; read)
- `0x008F6498` → RVA `0x00011528` (`.rdata`; read)
- `0x008F64C0` → RVA `0x000116B8` (`.rdata`; read)
- `0x008F64CD` → RVA `0x000116C0` (`.rdata`; read)
- `0x008F64E5` → RVA `0x00011550` (`.rdata`; read)
- `0x008F64F2` → RVA `0x00011558` (`.rdata`; read)
- `0x008F6566` → RVA `0x000116F8` (`.rdata`; read)
- `0x008F6573` → RVA `0x00011700` (`.rdata`; read)
- `0x008F659A` → RVA `0x00011670` (`.rdata`; read)
- `0x008F65A7` → RVA `0x00011678` (`.rdata`; read)
- `0x008F65E4` → RVA `0x00011688` (`.rdata`; read)
- `0x008F65F1` → RVA `0x00011690` (`.rdata`; read)
- `0x008F660A` → RVA `0x00F8C600` (`.data`; read)
- `0x008F6660` → RVA `0x000115A0` (`.rdata`; read)
- `0x008F666D` → RVA `0x000115A8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x008F642A` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x008F661B` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x008F664E` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x008F6653` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **11**
  - `0x008F6358` → [sub_00B1EBE0](../B1/Unknown_function_00B1EBE0.md) (`tail-transfer`)
  - `0x008F6369` → [sub_00B1EBE0](../B1/Unknown_function_00B1EBE0.md) (`tail-transfer`)
  - `0x008F64DD` → [sub_00B1EBE0 + 0x1A5](../B1/Unknown_function_00B1EBE0.md) (`tail-transfer`)
  - `0x008F65DC` → [sub_00B1EBE0 + 0x2B6](../B1/Unknown_function_00B1EBE0.md) (`tail-transfer`)
  - `0x008F667D` → [sub_00B1EBE0 + 0x2F](../B1/Unknown_function_00B1EBE0.md) (`tail-transfer`)
  - `0x008F6696` → [sub_00B1EBE0 + 0xE](../B1/Unknown_function_00B1EBE0.md) (`tail-transfer`)
  - `0x008F66A3` → [sub_00B1EBE0 + 0xE](../B1/Unknown_function_00B1EBE0.md) (`tail-transfer`)
  - `0x008F66AE` → [sub_00B1EBE0 + 0x105](../B1/Unknown_function_00B1EBE0.md) (`tail-transfer`)
  - `0x008F66BB` → [sub_00B1EBE0 + 0x105](../B1/Unknown_function_00B1EBE0.md) (`tail-transfer`)
  - `0x008F66CA` → [sub_00B1EBE0 + 0x262](../B1/Unknown_function_00B1EBE0.md) (`tail-transfer`)
  - `0x008F66DB` → [sub_00B1EBE0 + 0x262](../B1/Unknown_function_00B1EBE0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008F62A0  40 55                           push rbp
008F62A2  53                              push rbx
008F62A3  56                              push rsi
008F62A4  57                              push rdi
008F62A5  41 54                           push r12
008F62A7  41 55                           push r13
008F62A9  41 56                           push r14
008F62AB  41 57                           push r15
008F62AD  48 8D 6C 24 F9                  lea rbp, [rsp - 7]
008F62B2  48 81 EC E8 00 00 00            sub rsp, 0xe8
008F62B9  48 8B 05 80 44 51 00            mov rax, qword ptr [rip + 0x514480]
008F62C0  48 33 C4                        xor rax, rsp
008F62C3  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
008F62C7  48 8B 45 6F                     mov rax, qword ptr [rbp + 0x6f]
008F62CB  45 33 D2                        xor r10d, r10d
008F62CE  48 8B 7D 77                     mov rdi, qword ptr [rbp + 0x77]
008F62D2  0F 57 C0                        xorps xmm0, xmm0
008F62D5  48 8B 9D 87 00 00 00            mov rbx, qword ptr [rbp + 0x87]
008F62DC  0F 57 C9                        xorps xmm1, xmm1
008F62DF  44 8B AD 8F 00 00 00            mov r13d, dword ptr [rbp + 0x8f]
008F62E6  41 8B F0                        mov esi, r8d
008F62E9  48 89 4D A7                     mov qword ptr [rbp - 0x59], rcx
008F62ED  45 8D 72 05                     lea r14d, [r10 + 5]
008F62F1  41 8B C8                        mov ecx, r8d
008F62F4  4C 89 4D 9F                     mov qword ptr [rbp - 0x61], r9
008F62F8  48 89 45 C7                     mov qword ptr [rbp - 0x39], rax
008F62FC  4C 8B FA                        mov r15, rdx
008F62FF  44 89 55 B3                     mov dword ptr [rbp - 0x4d], r10d
008F6303  45 8B E2                        mov r12d, r10d
008F6306  44 89 55 AF                     mov dword ptr [rbp - 0x51], r10d
008F630A  44 89 55 83                     mov dword ptr [rbp - 0x7d], r10d
008F630E  44 89 55 93                     mov dword ptr [rbp - 0x6d], r10d
008F6312  44 89 55 8B                     mov dword ptr [rbp - 0x75], r10d
008F6316  44 89 55 97                     mov dword ptr [rbp - 0x69], r10d
008F631A  44 89 55 87                     mov dword ptr [rbp - 0x79], r10d
008F631E  44 89 55 8F                     mov dword ptr [rbp - 0x71], r10d
008F6322  44 88 55 80                     mov byte ptr [rbp - 0x80], r10b
008F6326  44 88 54 24 60                  mov byte ptr [rsp + 0x60], r10b
008F632B  0F 11 45 B7                     movups xmmword ptr [rbp - 0x49], xmm0
008F632F  0F 11 4D DF                     movups xmmword ptr [rbp - 0x21], xmm1
008F6333  0F 11 45 CF                     movups xmmword ptr [rbp - 0x31], xmm0
008F6337  83 E9 01                        sub ecx, 1
008F633A  0F 84 04 01 00 00               je 0x1408f6444
008F6340  83 E9 02                        sub ecx, 2
008F6343  75 29                           jne 0x1408f636e
008F6345  81 7F 10 00 01 00 00            cmp dword ptr [rdi + 0x10], 0x100
008F634C  75 32                           jne 0x1408f6380
008F634E  48 8B 07                        mov rax, qword ptr [rdi]
008F6351  48 2B 05 38 B1 71 FF            sub rax, qword ptr [rip - 0x8e4ec8]
008F6358  0F 85 82 88 22 00               jne 0x140b1ebe0
008F635E  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
008F6362  48 2B 05 2F B1 71 FF            sub rax, qword ptr [rip - 0x8e4ed1]
008F6369  E9 72 88 22 00                  jmp 0x140b1ebe0
008F636E  83 F9 02                        cmp ecx, 2
008F6371  0F 84 B8 01 00 00               je 0x1408f652f
008F6377  83 FE 01                        cmp esi, 1
008F637A  0F 84 11 01 00 00               je 0x1408f6491
008F6380  8B 85 97 00 00 00               mov eax, dword ptr [rbp + 0x97]
008F6386  44 8B C6                        mov r8d, esi
008F6389  4C 8B 4D 9F                     mov r9, qword ptr [rbp - 0x61]
008F638D  49 8B D7                        mov rdx, r15
008F6390  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
008F6394  8B 45 7F                        mov eax, dword ptr [rbp + 0x7f]
008F6397  44 89 6C 24 40                  mov dword ptr [rsp + 0x40], r13d
008F639C  4C 8B 6D A7                     mov r13, qword ptr [rbp - 0x59]
008F63A0  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
008F63A5  49 8B CD                        mov rcx, r13
008F63A8  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
008F63AC  48 8B 45 C7                     mov rax, qword ptr [rbp - 0x39]
008F63B0  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
008F63B5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008F63BA  E8 29 03 00 00                  call 0x1408f66e8
008F63BF  8B D8                           mov ebx, eax
008F63C1  83 EE 01                        sub esi, 1
008F63C4  74 3C                           je 0x1408f6402
008F63C6  83 FE 02                        cmp esi, 2
008F63C9  75 4C                           jne 0x1408f6417
008F63CB  85 C0                           test eax, eax
008F63CD  78 48                           js 0x1408f6417
008F63CF  83 7F 10 09                     cmp dword ptr [rdi + 0x10], 9
008F63D3  75 42                           jne 0x1408f6417
008F63D5  48 8B 07                        mov rax, qword ptr [rdi]
008F63D8  48 2B 05 D1 E9 71 FF            sub rax, qword ptr [rip - 0x8e162f]
008F63DF  75 0B                           jne 0x1408f63ec
008F63E1  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
008F63E5  48 2B 05 CC E9 71 FF            sub rax, qword ptr [rip - 0x8e1634]
008F63EC  48 85 C0                        test rax, rax
008F63EF  75 26                           jne 0x1408f6417
008F63F1  4C 8B 45 9F                     mov r8, qword ptr [rbp - 0x61]
008F63F5  49 8B D7                        mov rdx, r15
008F63F8  49 8B CD                        mov rcx, r13
008F63FB  E8 C4 3B 11 00                  call 0x140a09fc4
008F6400  EB 15                           jmp 0x1408f6417
008F6402  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
008F6405  83 F8 0C                        cmp eax, 0xc
008F6408  0F 84 B2 02 00 00               je 0x1408f66c0
008F640E  41 3B C6                        cmp eax, r14d
008F6411  0F 84 A5 01 00 00               je 0x1408f65bc
008F6417  80 7D 80 00                     cmp byte ptr [rbp - 0x80], 0
008F641B  0F 85 26 02 00 00               jne 0x1408f6647
008F6421  8B C3                           mov eax, ebx
008F6423  48 8B 4D EF                     mov rcx, qword ptr [rbp - 0x11]
008F6427  48 33 CC                        xor rcx, rsp
008F642A  E8 11 62 DB FF                  call 0x1406ac640
008F642F  48 81 C4 E8 00 00 00            add rsp, 0xe8
008F6436  41 5F                           pop r15
008F6438  41 5E                           pop r14
008F643A  41 5D                           pop r13
008F643C  41 5C                           pop r12
008F643E  5F                              pop rdi
008F643F  5E                              pop rsi
008F6440  5B                              pop rbx
008F6441  5D                              pop rbp
008F6442  C3                              ret
008F6443  CC                              int3
008F6444  41 8B D2                        mov edx, r10d
008F6447  4C 8D 0D B2 9B 70 FF            lea r9, [rip - 0x8f644e]
008F644E  83 FA 10                        cmp edx, 0x10
008F6451  73 1B                           jae 0x1408f646e
008F6453  8B C2                           mov eax, edx
008F6455  4D 8B 84 C1 20 A0 00 00         mov r8, qword ptr [r9 + rax*8 + 0xa020]
008F645D  41 8B 40 10                     mov eax, dword ptr [r8 + 0x10]
008F6461  39 47 10                        cmp dword ptr [rdi + 0x10], eax
008F6464  0F 84 A2 00 00 00               je 0x1408f650c
008F646A  FF C2                           inc edx
008F646C  EB E0                           jmp 0x1408f644e
008F646E  8B 4F 10                        mov ecx, dword ptr [rdi + 0x10]
008F6471  83 F9 0C                        cmp ecx, 0xc
008F6474  0F 84 08 02 00 00               je 0x1408f6682
008F647A  83 F9 03                        cmp ecx, 3
008F647D  74 63                           je 0x1408f64e2
008F647F  83 F9 04                        cmp ecx, 4
008F6482  0F 84 0F 01 00 00               je 0x1408f6597
008F6488  83 F9 02                        cmp ecx, 2
008F648B  0F 84 CC 01 00 00               je 0x1408f665d
008F6491  48 8B 0D 98 B0 71 FF            mov rcx, qword ptr [rip - 0x8e4f68]
008F6498  48 8B 15 89 B0 71 FF            mov rdx, qword ptr [rip - 0x8e4f77]
008F649F  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
008F64A2  83 F8 0A                        cmp eax, 0xa
008F64A5  0F 84 36 01 00 00               je 0x1408f65e1
008F64AB  83 F8 0C                        cmp eax, 0xc
008F64AE  0F 84 F4 01 00 00               je 0x1408f66a8
008F64B4  41 3B C6                        cmp eax, r14d
008F64B7  0F 85 C3 FE FF FF               jne 0x1408f6380
008F64BD  48 8B 07                        mov rax, qword ptr [rdi]
008F64C0  48 2B 05 F1 B1 71 FF            sub rax, qword ptr [rip - 0x8e4e0f]
008F64C7  75 0B                           jne 0x1408f64d4
008F64C9  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
008F64CD  48 2B 05 EC B1 71 FF            sub rax, qword ptr [rip - 0x8e4e14]
008F64D4  48 85 C0                        test rax, rax
008F64D7  0F 85 A3 FE FF FF               jne 0x1408f6380
008F64DD  E9 A3 88 22 00                  jmp 0x140b1ed85
008F64E2  48 8B 07                        mov rax, qword ptr [rdi]
008F64E5  48 2B 05 64 B0 71 FF            sub rax, qword ptr [rip - 0x8e4f9c]
008F64EC  75 0B                           jne 0x1408f64f9
008F64EE  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
008F64F2  48 2B 05 5F B0 71 FF            sub rax, qword ptr [rip - 0x8e4fa1]
008F64F9  48 85 C0                        test rax, rax
008F64FC  75 81                           jne 0x1408f647f
008F64FE  49 8B CF                        mov rcx, r15
008F6501  E8 02 09 00 00                  call 0x1408f6e08
008F6506  84 C0                           test al, al
008F6508  75 87                           jne 0x1408f6491
008F650A  EB 19                           jmp 0x1408f6525
008F650C  48 8B 0F                        mov rcx, qword ptr [rdi]
008F650F  49 2B 08                        sub rcx, qword ptr [r8]
008F6512  75 08                           jne 0x1408f651c
008F6514  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
008F6518  49 2B 48 08                     sub rcx, qword ptr [r8 + 8]
008F651C  48 85 C9                        test rcx, rcx
008F651F  0F 85 45 FF FF FF               jne 0x1408f646a
008F6525  BB 22 00 00 C0                  mov ebx, 0xc0000022
008F652A  E9 F2 FE FF FF                  jmp 0x1408f6421
008F652F  41 8B D2                        mov edx, r10d
008F6532  4C 8D 0D C7 9A 70 FF            lea r9, [rip - 0x8f6539]
008F6539  41 3B D6                        cmp edx, r14d
008F653C  73 1B                           jae 0x1408f6559
008F653E  8B C2                           mov eax, edx
008F6540  4D 8B 84 C1 F8 9F 00 00         mov r8, qword ptr [r9 + rax*8 + 0x9ff8]
008F6548  41 8B 40 10                     mov eax, dword ptr [r8 + 0x10]
008F654C  39 47 10                        cmp dword ptr [rdi + 0x10], eax
008F654F  0F 84 D4 00 00 00               je 0x1408f6629
008F6555  FF C2                           inc edx
008F6557  EB E0                           jmp 0x1408f6539
008F6559  83 7F 10 69                     cmp dword ptr [rdi + 0x10], 0x69
008F655D  0F 85 1D FE FF FF               jne 0x1408f6380
008F6563  48 8B 07                        mov rax, qword ptr [rdi]
008F6566  48 2B 05 8B B1 71 FF            sub rax, qword ptr [rip - 0x8e4e75]
008F656D  75 0B                           jne 0x1408f657a
008F656F  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
008F6573  48 2B 05 86 B1 71 FF            sub rax, qword ptr [rip - 0x8e4e7a]
008F657A  48 85 C0                        test rax, rax
008F657D  0F 85 FD FD FF FF               jne 0x1408f6380
008F6583  83 7D 7F 07                     cmp dword ptr [rbp + 0x7f], 7
008F6587  0F 84 F3 FD FF FF               je 0x1408f6380
008F658D  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008F6592  E9 8A FE FF FF                  jmp 0x1408f6421
008F6597  48 8B 07                        mov rax, qword ptr [rdi]
008F659A  48 2B 05 CF B0 71 FF            sub rax, qword ptr [rip - 0x8e4f31]
008F65A1  75 0B                           jne 0x1408f65ae
008F65A3  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
008F65A7  48 2B 05 CA B0 71 FF            sub rax, qword ptr [rip - 0x8e4f36]
008F65AE  48 85 C0                        test rax, rax
008F65B1  0F 84 47 FF FF FF               je 0x1408f64fe
008F65B7  E9 D5 FE FF FF                  jmp 0x1408f6491
008F65BC  48 8B 07                        mov rax, qword ptr [rdi]
008F65BF  48 2B 05 F2 B0 71 FF            sub rax, qword ptr [rip - 0x8e4f0e]
008F65C6  75 0B                           jne 0x1408f65d3
008F65C8  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
008F65CC  48 2B 05 ED B0 71 FF            sub rax, qword ptr [rip - 0x8e4f13]
008F65D3  48 85 C0                        test rax, rax
008F65D6  0F 85 3B FE FF FF               jne 0x1408f6417
008F65DC  E9 B5 88 22 00                  jmp 0x140b1ee96
008F65E1  48 8B 07                        mov rax, qword ptr [rdi]
008F65E4  48 2B 05 9D B0 71 FF            sub rax, qword ptr [rip - 0x8e4f63]
008F65EB  75 0B                           jne 0x1408f65f8
008F65ED  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
008F65F1  48 2B 05 98 B0 71 FF            sub rax, qword ptr [rip - 0x8e4f68]
008F65F8  48 85 C0                        test rax, rax
008F65FB  0F 85 7F FD FF FF               jne 0x1408f6380
008F6601  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008F660A  48 8D 0D EF 5F 69 00            lea rcx, [rip + 0x695fef]
008F6611  B2 01                           mov dl, 1
008F6613  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008F661A  90                              nop
008F661B  E8 00 E8 91 FF                  call 0x140214e20
008F6620  C6 45 80 01                     mov byte ptr [rbp - 0x80], 1
008F6624  E9 57 FD FF FF                  jmp 0x1408f6380
008F6629  48 8B 0F                        mov rcx, qword ptr [rdi]
008F662C  49 2B 08                        sub rcx, qword ptr [r8]
008F662F  75 08                           jne 0x1408f6639
008F6631  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
008F6635  49 2B 48 08                     sub rcx, qword ptr [r8 + 8]
008F6639  48 85 C9                        test rcx, rcx
008F663C  0F 84 E3 FE FF FF               je 0x1408f6525
008F6642  E9 0E FF FF FF                  jmp 0x1408f6555
008F6647  48 8D 0D B2 5F 69 00            lea rcx, [rip + 0x695fb2]
008F664E  E8 BD 93 96 FF                  call 0x14025fa10
008F6653  E8 58 72 96 FF                  call 0x14025d8b0
008F6658  E9 C4 FD FF FF                  jmp 0x1408f6421
008F665D  48 8B 07                        mov rax, qword ptr [rdi]
008F6660  48 2B 05 39 AF 71 FF            sub rax, qword ptr [rip - 0x8e50c7]
008F6667  75 0B                           jne 0x1408f6674
008F6669  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
008F666D  48 2B 05 34 AF 71 FF            sub rax, qword ptr [rip - 0x8e50cc]
008F6674  48 85 C0                        test rax, rax
008F6677  0F 85 14 FE FF FF               jne 0x1408f6491
008F667D  E9 8D 85 22 00                  jmp 0x140b1ec0f
008F6682  48 8B 07                        mov rax, qword ptr [rdi]
008F6685  48 8B 15 9C AE 71 FF            mov rdx, qword ptr [rip - 0x8e5164]
008F668C  48 8B 0D 9D AE 71 FF            mov rcx, qword ptr [rip - 0x8e5163]
008F6693  48 2B C2                        sub rax, rdx
008F6696  0F 85 52 85 22 00               jne 0x140b1ebee
008F669C  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
008F66A0  48 2B C1                        sub rax, rcx
008F66A3  E9 46 85 22 00                  jmp 0x140b1ebee
008F66A8  48 8B 07                        mov rax, qword ptr [rdi]
008F66AB  48 2B C2                        sub rax, rdx
008F66AE  0F 85 31 86 22 00               jne 0x140b1ece5
008F66B4  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
008F66B8  48 2B C1                        sub rax, rcx
008F66BB  E9 25 86 22 00                  jmp 0x140b1ece5
008F66C0  48 8B 07                        mov rax, qword ptr [rdi]
008F66C3  48 2B 05 5E AE 71 FF            sub rax, qword ptr [rip - 0x8e51a2]
008F66CA  0F 85 72 87 22 00               jne 0x140b1ee42
008F66D0  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
008F66D4  48 2B 05 55 AE 71 FF            sub rax, qword ptr [rip - 0x8e51ab]
008F66DB  E9 62 87 22 00                  jmp 0x140b1ee42
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiPnpRtlSetObjectProperty(__int64 a1, __int64 a2, int a3, __int64 a4, __int64 a5, __int64 a6, unsigned int a7, __int64 a8, unsigned int a9, unsigned int a10)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m47;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m94;
    unsigned int v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_mB0;
    unsigned int v_stack_mB4;
    unsigned int v_stack_mB8;
    unsigned int v_stack_mBC;
    unsigned int v_stack_mC0;
    unsigned int v_stack_mC4;
    unsigned __int8 v_stack_mC7;
    unsigned __int8 v_stack_mC8;
    unsigned int v_stack_mE0;
    unsigned int v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned int v_stack_mF8;

    v_rsp = (v_rsp) - (232);
    result = (*(unsigned __int64 *)(v_rip + 5325952)) ^ (v_rsp);
    v_stack_m58 = result;
    v_r10 = 0;
    v_stack_mA0 = a1;
    v_stack_mA8 = a4;
    v_stack_m80 = a5;
    v_stack_m94 = 0;
    v_stack_m98 = 0;
    v_stack_mC4 = 0;
    v_stack_mB4 = 0;
    v_stack_mBC = 0;
    v_stack_mB0 = 0;
    v_stack_mC0 = 0;
    v_stack_mB8 = 0;
    v_stack_mC7 = 0;
    v_stack_mC8 = 0;
    v_stack_m90 = v_xmm0;
    v_stack_m68 = v_xmm1;
    v_stack_m78 = v_xmm0;
    a1 = (unsigned int)(((unsigned int)(a3)) - (1));
    if (condition_is_equal) goto loc_008F6444;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_not_equal) goto loc_008F636E;
    if ((*(unsigned int *)(a6 + 16)) != 256) goto loc_008F6380;
    result = (*(unsigned __int64 *)(a6)) - (*(unsigned __int64 *)(v_rip - 9326280));
    result = (*(unsigned __int64 *)(a6 + 8)) - (*(unsigned __int64 *)(v_rip - 9326289));
loc_008F636E:
    if (((unsigned int)(a1)) == 2) goto loc_008F652F;
    if (((unsigned int)((unsigned int)(a3))) == 1) goto loc_008F6491;
loc_008F6380:
    v_stack_mE0 = (unsigned int)((unsigned int)(a10));
    v_stack_mE8 = (unsigned int)((unsigned int)(a9));
    v_stack_mF0 = a8;
    v_stack_mF8 = (unsigned int)((unsigned int)(a7));
    v_stack_m100 = a6;
    v_stack_m108 = v_stack_m80;
    result = PnpSetObjectProperty(v_stack_mA0, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), v_stack_mA8);
    v_rsi = (unsigned int)(((unsigned int)(a3)) - (1));
    if (condition_is_equal) goto loc_008F6402;
    if (((unsigned int)(v_rsi)) != 2) goto loc_008F6417;
    if (sign_flag) goto loc_008F6417;
    if ((*(unsigned int *)(a6 + 16)) != 9) goto loc_008F6417;
    result = (*(unsigned __int64 *)(a6)) - (*(unsigned __int64 *)(v_rip - 9311791));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(a6 + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 9311796));
    }
    if (result != 0) goto loc_008F6417;
    result = _CmUpdateDevicePanelInterface(v_stack_mA0, a2, v_stack_mA8, v_stack_mA8);
    goto loc_008F6417;
loc_008F6402:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a6 + 16)))) == 12) goto loc_008F66C0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a6 + 16)))) == ((unsigned int)(v_r10 + 5))) goto loc_008F65BC;
loc_008F6417:
    if (v_stack_mC7 != 0) goto loc_008F6647;
loc_008F6421:
    a1 = (v_stack_m58) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, v_stack_mA8, v_stack_mA8);
    v_rsp = (v_rsp) + (232);
    return result;
loc_008F6444:
loc_008F644E:
    if (0 >= 16) goto loc_008F646E;
    if ((*(unsigned int *)(a6 + 16)) == ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip - 9397326 + 0 * 8 + 40992) + 16))))) goto loc_008F650C;
loc_008F646A:
    a2 = (unsigned int)((0) + 1);
    goto loc_008F644E;
loc_008F646E:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a6 + 16)))) == 12) goto loc_008F6682;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a6 + 16)))) == 3) goto loc_008F64E2;
loc_008F647F:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a6 + 16)))) == 4) goto loc_008F6597;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a6 + 16)))) == 2) goto loc_008F665D;
loc_008F6491:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a6 + 16)))) == 10) goto loc_008F65E1;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a6 + 16)))) == 12) goto loc_008F66A8;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a6 + 16)))) != ((unsigned int)(v_r10 + 5))) goto loc_008F6380;
    result = (*(unsigned __int64 *)(a6)) - (*(unsigned __int64 *)(v_rip - 9326095));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(a6 + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 9326100));
    }
    if (result != 0) goto loc_008F6380;
loc_008F64E2:
    result = (*(unsigned __int64 *)(a6)) - (*(unsigned __int64 *)(v_rip - 9326492));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(a6 + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 9326497));
    }
    if (result != 0) goto loc_008F647F;
loc_008F64FE:
    result = CmIsRootEnumeratedDevice(a2, *(unsigned __int64 *)(v_rip - 9326455), *(unsigned __int64 *)(v_rip - 9397326 + 0 * 8 + 40992), v_rip - 9397326);
    if ((unsigned __int8)(result) != 0) goto loc_008F6491;
    goto loc_008F6525;
loc_008F650C:
    a1 = (*(unsigned __int64 *)(a6)) - (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 9397326 + 0 * 8 + 40992)));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int64 *)(a6 + 8);
        a1 = (a1) - (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 9397326 + 0 * 8 + 40992) + 8));
    }
    if (a1 != 0) goto loc_008F646A;
loc_008F6525:
    goto loc_008F6421;
loc_008F652F:
loc_008F6539:
    if (0 >= ((unsigned int)(v_r10 + 5))) goto loc_008F6559;
    if ((*(unsigned int *)(a6 + 16)) == ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip - 9397561 + 0 * 8 + 40952) + 16))))) goto loc_008F6629;
loc_008F6555:
    a2 = (unsigned int)((0) + 1);
    goto loc_008F6539;
loc_008F6559:
    if ((*(unsigned int *)(a6 + 16)) != 105) goto loc_008F6380;
    result = (*(unsigned __int64 *)(a6)) - (*(unsigned __int64 *)(v_rip - 9326197));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(a6 + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 9326202));
    }
    if (result != 0) goto loc_008F6380;
    if (a7 == 7) goto loc_008F6380;
    goto loc_008F6421;
loc_008F6597:
    result = (*(unsigned __int64 *)(a6)) - (*(unsigned __int64 *)(v_rip - 9326385));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(a6 + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 9326390));
    }
    if (result == 0) goto loc_008F64FE;
    goto loc_008F6491;
loc_008F65BC:
    result = (*(unsigned __int64 *)(a6)) - (*(unsigned __int64 *)(v_rip - 9326350));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(a6 + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 9326355));
    }
    if (result != 0) goto loc_008F6417;
loc_008F65E1:
    result = (*(unsigned __int64 *)(a6)) - (*(unsigned __int64 *)(v_rip - 9326435));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(a6 + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 9326440));
    }
    if (result != 0) goto loc_008F6380;
    result = ExAcquireResourceExclusiveLite(v_rip + 6905839, 1, *(unsigned __int64 *)(v_rip - 9397561 + 0 * 8 + 40952), v_rip - 9397561);
    v_stack_mC7 = 1;
    goto loc_008F6380;
loc_008F6629:
    a1 = (*(unsigned __int64 *)(a6)) - (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 9397561 + 0 * 8 + 40952)));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int64 *)(a6 + 8);
        a1 = (a1) - (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 9397561 + 0 * 8 + 40952) + 8));
    }
    if (a1 == 0) goto loc_008F6525;
    goto loc_008F6555;
loc_008F6647:
    result = ExReleaseResourceLite(v_rip + 6905778, 1, *(unsigned __int64 *)(v_rip - 9397561 + 0 * 8 + 40952), v_rip - 9397561);
    result = KeLeaveCriticalRegion(v_rip + 6905778, 1, *(unsigned __int64 *)(v_rip - 9397561 + 0 * 8 + 40952), v_rip - 9397561);
    goto loc_008F6421;
loc_008F665D:
    result = (*(unsigned __int64 *)(a6)) - (*(unsigned __int64 *)(v_rip - 9326791));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(a6 + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 9326796));
    }
    if (result != 0) goto loc_008F6491;
loc_008F6682:
    result = (*(unsigned __int64 *)(a6)) - (*(unsigned __int64 *)(v_rip - 9326948));
    result = (*(unsigned __int64 *)(a6 + 8)) - (*(unsigned __int64 *)(v_rip - 9326947));
loc_008F66A8:
    result = (*(unsigned __int64 *)(a6)) - (*(unsigned __int64 *)(v_rip - 9326948));
    result = (*(unsigned __int64 *)(a6 + 8)) - (*(unsigned __int64 *)(v_rip - 9326947));
loc_008F66C0:
    result = (*(unsigned __int64 *)(a6)) - (*(unsigned __int64 *)(v_rip - 9327010));
    result = (*(unsigned __int64 *)(a6 + 8)) - (*(unsigned __int64 *)(v_rip - 9327019));
}
```

## 5. (Beta) C Style

```c
int64_t PiPnpRtlSetObjectProperty(int64_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, int64_t Arg5, void *Arg6, uint32_t Arg7, int64_t Arg8, uint32_t Arg9, uint32_t Arg10)
{
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r10;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m47;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m90;
    uint32_t v_stack_m94;
    uint32_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint32_t v_stack_mB0;
    uint32_t v_stack_mB4;
    uint32_t v_stack_mB8;
    uint32_t v_stack_mBC;
    uint32_t v_stack_mC0;
    uint32_t v_stack_mC4;
    uint8_t v_stack_mC7;
    uint8_t v_stack_mC8;
    uint32_t v_stack_mE0;
    uint32_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint32_t v_stack_mF8;

    local_rsp = (local_rsp) - (232);
    result = (*(uint64_t *)(v_rip + 0x514480)) ^ (local_rsp);
    v_stack_m58 = result;
    local_r10 = 0;
    v_stack_mA0 = Arg1;
    v_stack_mA8 = Arg4;
    v_stack_m80 = Arg5;
    v_stack_m94 = 0;
    v_stack_m98 = 0;
    v_stack_mC4 = 0;
    v_stack_mB4 = 0;
    v_stack_mBC = 0;
    v_stack_mB0 = 0;
    v_stack_mC0 = 0;
    v_stack_mB8 = 0;
    v_stack_mC7 = 0;
    v_stack_mC8 = 0;
    v_stack_m90 = v_xmm0;
    v_stack_m68 = v_xmm1;
    v_stack_m78 = v_xmm0;
    Arg1 = (uint32_t)(((uint32_t)(Arg3)) - (1));
    if (condition_is_equal) goto loc_008F6444;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_not_equal) goto loc_008F636E;
    if ((*(uint32_t *)(arg6 + 0x10)) != 256) goto loc_008F6380;
    result = (*(uint64_t *)(arg6)) - (*(uint64_t *)(v_rip - 0x8E4EC8));
    result = (*(uint64_t *)(arg6 + 0x8)) - (*(uint64_t *)(v_rip - 0x8E4ED1));
loc_008F636E:
    if (((uint32_t)(Arg1)) == 2) goto loc_008F652F;
    if (((uint32_t)((uint32_t)(Arg3))) == 1) goto loc_008F6491;
loc_008F6380:
    v_stack_mE0 = (uint32_t)((uint32_t)(Arg10));
    v_stack_mE8 = (uint32_t)((uint32_t)(Arg9));
    v_stack_mF0 = Arg8;
    v_stack_mF8 = (uint32_t)((uint32_t)(Arg7));
    v_stack_m100 = Arg6;
    v_stack_m108 = v_stack_m80;
    result = PnpSetObjectProperty(v_stack_mA0, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), v_stack_mA8);
    local_rsi = (uint32_t)(((uint32_t)(Arg3)) - (1));
    if (condition_is_equal) goto loc_008F6402;
    if (((uint32_t)(local_rsi)) != 2) goto loc_008F6417;
    if (sign_flag) goto loc_008F6417;
    if ((*(uint32_t *)(arg6 + 0x10)) != 9) goto loc_008F6417;
    result = (*(uint64_t *)(arg6)) - (*(uint64_t *)(v_rip - 0x8E162F));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(arg6 + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x8E1634));
    }
    if (result != 0) goto loc_008F6417;
    result = _CmUpdateDevicePanelInterface(v_stack_mA0, Arg2, v_stack_mA8, v_stack_mA8);
    goto loc_008F6417;
loc_008F6402:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg6 + 0x10)))) == 12) goto loc_008F66C0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg6 + 0x10)))) == ((uint32_t)(local_r10 + 5))) goto loc_008F65BC;
loc_008F6417:
    if (v_stack_mC7 != 0) goto loc_008F6647;
loc_008F6421:
    Arg1 = (v_stack_m58) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, v_stack_mA8, v_stack_mA8);
    local_rsp = (local_rsp) + (232);
    return result;
loc_008F6444:
loc_008F644E:
    if (0 >= 16) goto loc_008F646E;
    if ((*(uint32_t *)(arg6 + 0x10)) == ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip - 0x8F644E + 0x0 * 8 + 0xA020) + 0x10))))) goto loc_008F650C;
loc_008F646A:
    Arg2 = (uint32_t)((0) + 1);
    goto loc_008F644E;
loc_008F646E:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg6 + 0x10)))) == 12) goto loc_008F6682;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg6 + 0x10)))) == 3) goto loc_008F64E2;
loc_008F647F:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg6 + 0x10)))) == 4) goto loc_008F6597;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg6 + 0x10)))) == 2) goto loc_008F665D;
loc_008F6491:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg6 + 0x10)))) == 10) goto loc_008F65E1;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg6 + 0x10)))) == 12) goto loc_008F66A8;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg6 + 0x10)))) != ((uint32_t)(local_r10 + 5))) goto loc_008F6380;
    result = (*(uint64_t *)(arg6)) - (*(uint64_t *)(v_rip - 0x8E4E0F));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(arg6 + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x8E4E14));
    }
    if (result != 0) goto loc_008F6380;
loc_008F64E2:
    result = (*(uint64_t *)(arg6)) - (*(uint64_t *)(v_rip - 0x8E4F9C));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(arg6 + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x8E4FA1));
    }
    if (result != 0) goto loc_008F647F;
loc_008F64FE:
    result = CmIsRootEnumeratedDevice(Arg2, *(uint64_t *)(v_rip - 0x8E4F77), *(uint64_t *)(v_rip - 0x8F644E + 0x0 * 8 + 0xA020), v_rip - 9397326);
    if ((uint8_t)(result) != 0) goto loc_008F6491;
    goto loc_008F6525;
loc_008F650C:
    Arg1 = (*(uint64_t *)(arg6)) - (*(uint64_t *)(*(uint64_t *)(v_rip - 0x8F644E + 0x0 * 8 + 0xA020)));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint64_t *)(arg6 + 0x8);
        Arg1 = (Arg1) - (*(uint64_t *)(*(uint64_t *)(v_rip - 0x8F644E + 0x0 * 8 + 0xA020) + 0x8));
    }
    if (Arg1 != 0) goto loc_008F646A;
loc_008F6525:
    goto loc_008F6421;
loc_008F652F:
loc_008F6539:
    if (0 >= ((uint32_t)(local_r10 + 5))) goto loc_008F6559;
    if ((*(uint32_t *)(arg6 + 0x10)) == ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip - 0x8F6539 + 0x0 * 8 + 0x9FF8) + 0x10))))) goto loc_008F6629;
loc_008F6555:
    Arg2 = (uint32_t)((0) + 1);
    goto loc_008F6539;
loc_008F6559:
    if ((*(uint32_t *)(arg6 + 0x10)) != 105) goto loc_008F6380;
    result = (*(uint64_t *)(arg6)) - (*(uint64_t *)(v_rip - 0x8E4E75));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(arg6 + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x8E4E7A));
    }
    if (result != 0) goto loc_008F6380;
    if (Arg7 == 7) goto loc_008F6380;
    goto loc_008F6421;
loc_008F6597:
    result = (*(uint64_t *)(arg6)) - (*(uint64_t *)(v_rip - 0x8E4F31));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(arg6 + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x8E4F36));
    }
    if (result == 0) goto loc_008F64FE;
    goto loc_008F6491;
loc_008F65BC:
    result = (*(uint64_t *)(arg6)) - (*(uint64_t *)(v_rip - 0x8E4F0E));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(arg6 + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x8E4F13));
    }
    if (result != 0) goto loc_008F6417;
loc_008F65E1:
    result = (*(uint64_t *)(arg6)) - (*(uint64_t *)(v_rip - 0x8E4F63));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(arg6 + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x8E4F68));
    }
    if (result != 0) goto loc_008F6380;
    result = ExAcquireResourceExclusiveLite(v_rip + 6905839, 1, *(uint64_t *)(v_rip - 0x8F6539 + 0x0 * 8 + 0x9FF8), v_rip - 9397561);
    v_stack_mC7 = 1;
    goto loc_008F6380;
loc_008F6629:
    Arg1 = (*(uint64_t *)(arg6)) - (*(uint64_t *)(*(uint64_t *)(v_rip - 0x8F6539 + 0x0 * 8 + 0x9FF8)));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint64_t *)(arg6 + 0x8);
        Arg1 = (Arg1) - (*(uint64_t *)(*(uint64_t *)(v_rip - 0x8F6539 + 0x0 * 8 + 0x9FF8) + 0x8));
    }
    if (Arg1 == 0) goto loc_008F6525;
    goto loc_008F6555;
loc_008F6647:
    result = ExReleaseResourceLite(v_rip + 6905778, 1, *(uint64_t *)(v_rip - 0x8F6539 + 0x0 * 8 + 0x9FF8), v_rip - 9397561);
    result = KeLeaveCriticalRegion(v_rip + 6905778, 1, *(uint64_t *)(v_rip - 0x8F6539 + 0x0 * 8 + 0x9FF8), v_rip - 9397561);
    goto loc_008F6421;
loc_008F665D:
    result = (*(uint64_t *)(arg6)) - (*(uint64_t *)(v_rip - 0x8E50C7));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(arg6 + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x8E50CC));
    }
    if (result != 0) goto loc_008F6491;
loc_008F6682:
    result = (*(uint64_t *)(arg6)) - (*(uint64_t *)(v_rip - 0x8E5164));
    result = (*(uint64_t *)(arg6 + 0x8)) - (*(uint64_t *)(v_rip - 0x8E5163));
loc_008F66A8:
    result = (*(uint64_t *)(arg6)) - (*(uint64_t *)(v_rip - 0x8E5164));
    result = (*(uint64_t *)(arg6 + 0x8)) - (*(uint64_t *)(v_rip - 0x8E5163));
loc_008F66C0:
    result = (*(uint64_t *)(arg6)) - (*(uint64_t *)(v_rip - 0x8E51A2));
    result = (*(uint64_t *)(arg6 + 0x8)) - (*(uint64_t *)(v_rip - 0x8E51AB));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg6` | `+ 0x0` | `64` | `R` |
| `Arg6` | `+ 0x8` | `64` | `R` |
| `Arg6` | `+ 0x10` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008F62A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
