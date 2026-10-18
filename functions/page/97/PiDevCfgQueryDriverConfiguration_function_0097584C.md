# PiDevCfgQueryDriverConfiguration

- RVA: `0x0097584C`–`0x00975E98` (길이 `1,612` bytes)
- VA: `0x000000014097584C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00096678`
- 디코드: `362`개 명령, `1,612/1,612` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **24**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **16**

### Outgoing calls
- `0x009758C0` → [PiDevCfgBuildDriverConfigurationId](../AB/PiDevCfgBuildDriverConfigurationId_function_00ABC0D0.md) (function, `0x00ABC0D0`)
- `0x00975907` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00975A9B` → [RtlpQueryRegistryValues](../8C/RtlpQueryRegistryValues_function_008C9050.md) (function, `0x008C9050`)
- `0x00975AC9` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00975AE1` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00975AFA` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00975B14` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00975B30` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00975B4B` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00975B74` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00975B8C` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00975B9D` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00975BC0` → [PiDevCfgVerifyService](PiDevCfgVerifyService_function_00975EA0.md) (function, `0x00975EA0`)
- `0x00975BFB` → [PiDevCfgVerifyService](PiDevCfgVerifyService_function_00975EA0.md) (function, `0x00975EA0`)
- `0x00975C43` → [PiDevCfgVerifyService](PiDevCfgVerifyService_function_00975EA0.md) (function, `0x00975EA0`)
- `0x00975C8B` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00975D39` → [PiDevCfgQueryObjectProperties](PiDevCfgQueryObjectProperties_function_0097776C.md) (function, `0x0097776C`)
- `0x00975D5B` → [RtlStringFromGUIDEx](../91/RtlStringFromGUIDEx_function_00915450.md) (function, `0x00915450`)
- `0x00975D7C` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00975DAD` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00975E1B` → [PnpGetObjectProperty](../8E/PnpGetObjectProperty_function_008E2180.md) (function, `0x008E2180`)
- `0x00975E44` → [PiDevCfgQueryIncludedDriverConfigurations](PiDevCfgQueryIncludedDriverConfigurations_function_009754BC.md) (function, `0x009754BC`)
- `0x00975E60` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x00975E71` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PiDevCfgCheckDeviceNeedsUpdate](../73/PiDevCfgCheckDeviceNeedsUpdate_function_00731DDC.md) at `0x007323C3`
- [PiDevCfgCheckDeviceNeedsUpdate](../73/PiDevCfgCheckDeviceNeedsUpdate_function_00731DDC.md) at `0x007323E4`
- [PiDevCfgRequestDriverConfigurations](../73/PiDevCfgRequestDriverConfigurations_function_00735778.md) at `0x007357A4`
- [PiDevCfgRequestDriverConfigurations](../73/PiDevCfgRequestDriverConfigurations_function_00735778.md) at `0x007357F5`
- [PpDevCfgProcessDeviceExtensions](../73/PpDevCfgProcessDeviceExtensions_function_00736C2C.md) at `0x00736DDB`
- [PiDevCfgQueryIncludedDriverConfigurations](PiDevCfgQueryIncludedDriverConfigurations_function_009754BC.md) at `0x009756FF`
- [PiDevCfgConfigureDevice](PiDevCfgConfigureDevice_function_00977BB4.md) at `0x00977EDF`
- [PiDevCfgConfigureDevice](PiDevCfgConfigureDevice_function_00977BB4.md) at `0x00978021`

### Static image references
- `0x00975872` → RVA `0x00E0A740` (`.data`; read)
- `0x0097592F` → RVA `0x00AFF010` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00975968` → RVA `0x00AFF020` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00975980` → RVA `0x00AFF040` (` ?? ::NNGAKEGL::`string'`; read)
- `0x0097599B` → RVA `0x00AFF090` (` ?? ::NNGAKEGL::`string'`; read)
- `0x009759B6` → RVA `0x00AFEE50` (` ?? ::NNGAKEGL::`string'`; read)
- `0x009759D9` → RVA `0x00AFF0B0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x009759E7` → RVA `0x00AFF0D0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x009759F5` → RVA `0x00AFF0F0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00975A11` → RVA `0x00AFF060` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00975C94` → RVA `0x00012EC8` (`.rdata`; read)
- `0x00975CBE` → RVA `0x00011F90` (`.rdata`; read)
- `0x00975CD0` → RVA `0x00012EF8` (`.rdata`; read)
- `0x00975CE8` → RVA `0x00012EE0` (`.rdata`; read)
- `0x00975DDD` → RVA `0x00E66398` (`.data`; read)
- `0x00975E0A` → RVA `0x00022018` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **6**
  - `0x00975907` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00975C8B` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00975D7C` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00975DAD` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00975E60` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x00975E71` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0097584C  48 8B C4                        mov rax, rsp
0097584F  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00975853  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00975857  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0097585B  55                              push rbp
0097585C  41 54                           push r12
0097585E  41 55                           push r13
00975860  41 56                           push r14
00975862  41 57                           push r15
00975864  48 8D A8 68 FD FF FF            lea rbp, [rax - 0x298]
0097586B  48 81 EC 70 03 00 00            sub rsp, 0x370
00975872  48 8B 05 C7 4E 49 00            mov rax, qword ptr [rip + 0x494ec7]
00975879  48 33 C4                        xor rax, rsp
0097587C  48 89 85 60 02 00 00            mov qword ptr [rbp + 0x260], rax
00975883  8B 81 B8 00 00 00               mov eax, dword ptr [rcx + 0xb8]
00975889  45 33 E4                        xor r12d, r12d
0097588C  44 88 64 24 61                  mov byte ptr [rsp + 0x61], r12b
00975891  48 8B F9                        mov rdi, rcx
00975894  44 88 64 24 60                  mov byte ptr [rsp + 0x60], r12b
00975899  44 88 64 24 62                  mov byte ptr [rsp + 0x62], r12b
0097589E  4C 89 64 24 70                  mov qword ptr [rsp + 0x70], r12
009758A3  4C 89 64 24 78                  mov qword ptr [rsp + 0x78], r12
009758A8  C7 44 24 64 01 00 00 00         mov dword ptr [rsp + 0x64], 1
009758B0  44 89 64 24 68                  mov dword ptr [rsp + 0x68], r12d
009758B5  A8 20                           test al, 0x20
009758B7  75 2F                           jne 0x1409758e8
009758B9  48 8D 91 A8 01 00 00            lea rdx, [rcx + 0x1a8]
009758C0  E8 0B 68 14 00                  call 0x140abc0d0
009758C5  8B D8                           mov ebx, eax
009758C7  85 C0                           test eax, eax
009758C9  0F 88 87 05 00 00               js 0x140975e56
009758CF  4C 39 67 18                     cmp qword ptr [rdi + 0x18], r12
009758D3  74 09                           je 0x1409758de
009758D5  48 8B 5F 20                     mov rbx, qword ptr [rdi + 0x20]
009758D9  48 85 DB                        test rbx, rbx
009758DC  75 1D                           jne 0x1409758fb
009758DE  BB 93 04 00 C0                  mov ebx, 0xc0000493
009758E3  E9 6E 05 00 00                  jmp 0x140975e56
009758E8  48 8B 59 20                     mov rbx, qword ptr [rcx + 0x20]
009758EC  48 85 DB                        test rbx, rbx
009758EF  75 0A                           jne 0x1409758fb
009758F1  BB 93 04 00 C0                  mov ebx, 0xc0000493
009758F6  E9 6A 05 00 00                  jmp 0x140975e65
009758FB  33 D2                           xor edx, edx
009758FD  48 8D 4D 30                     lea rcx, [rbp + 0x30]
00975901  41 B8 30 02 00 00               mov r8d, 0x230
00975907  E8 34 13 D5 FF                  call 0x1406c6c40
0097590C  41 B8 00 00 00 07               mov r8d, 0x7000000
00975912  C7 45 50 00 00 00 01            mov dword ptr [rbp + 0x50], 0x1000000
00975919  41 B9 20 01 00 00               mov r9d, 0x120
0097591F  44 89 85 88 00 00 00            mov dword ptr [rbp + 0x88], r8d
00975926  B9 00 00 00 04                  mov ecx, 0x4000000
0097592B  44 89 4D 38                     mov dword ptr [rbp + 0x38], r9d
0097592F  48 8D 05 DA 96 18 00            lea rax, [rip + 0x1896da]
00975936  44 89 85 C0 00 00 00            mov dword ptr [rbp + 0xc0], r8d
0097593D  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
00975941  4C 8D B7 30 01 00 00            lea r14, [rdi + 0x130]
00975948  41 8D 51 10                     lea edx, [r9 + 0x10]
0097594C  44 89 85 F8 00 00 00            mov dword ptr [rbp + 0xf8], r8d
00975953  48 8D 87 20 01 00 00            lea rax, [rdi + 0x120]
0097595A  89 55 70                        mov dword ptr [rbp + 0x70], edx
0097595D  48 89 45 48                     mov qword ptr [rbp + 0x48], rax
00975961  48 8D B7 40 01 00 00            lea rsi, [rdi + 0x140]
00975968  48 8D 05 B1 96 18 00            lea rax, [rip + 0x1896b1]
0097596F  89 95 A8 00 00 00               mov dword ptr [rbp + 0xa8], edx
00975975  48 89 45 78                     mov qword ptr [rbp + 0x78], rax
00975979  4C 8D BF 50 01 00 00            lea r15, [rdi + 0x150]
00975980  48 8D 05 B9 96 18 00            lea rax, [rip + 0x1896b9]
00975987  89 95 E0 00 00 00               mov dword ptr [rbp + 0xe0], edx
0097598D  48 89 85 B0 00 00 00            mov qword ptr [rbp + 0xb0], rax
00975994  4C 8D A7 60 01 00 00            lea r12, [rdi + 0x160]
0097599B  48 8D 05 EE 96 18 00            lea rax, [rip + 0x1896ee]
009759A2  89 8D 30 01 00 00               mov dword ptr [rbp + 0x130], ecx
009759A8  48 89 85 E8 00 00 00            mov qword ptr [rbp + 0xe8], rax
009759AF  4C 8D AF 70 01 00 00            lea r13, [rdi + 0x170]
009759B6  48 8D 05 93 94 18 00            lea rax, [rip + 0x189493]
009759BD  44 89 85 68 01 00 00            mov dword ptr [rbp + 0x168], r8d
009759C4  48 89 85 20 01 00 00            mov qword ptr [rbp + 0x120], rax
009759CB  48 8D 87 A0 01 00 00            lea rax, [rdi + 0x1a0]
009759D2  48 89 85 28 01 00 00            mov qword ptr [rbp + 0x128], rax
009759D9  48 8D 05 D0 96 18 00            lea rax, [rip + 0x1896d0]
009759E0  48 89 85 58 01 00 00            mov qword ptr [rbp + 0x158], rax
009759E7  48 8D 05 E2 96 18 00            lea rax, [rip + 0x1896e2]
009759EE  48 89 85 90 01 00 00            mov qword ptr [rbp + 0x190], rax
009759F5  48 8D 05 F4 96 18 00            lea rax, [rip + 0x1896f4]
009759FC  48 89 85 C8 01 00 00            mov qword ptr [rbp + 0x1c8], rax
00975A03  48 8D 87 A4 01 00 00            lea rax, [rdi + 0x1a4]
00975A0A  48 89 85 D0 01 00 00            mov qword ptr [rbp + 0x1d0], rax
00975A11  48 8D 05 48 96 18 00            lea rax, [rip + 0x189648]
00975A18  48 89 85 00 02 00 00            mov qword ptr [rbp + 0x200], rax
00975A1F  48 8D 87 90 01 00 00            lea rax, [rdi + 0x190]
00975A26  89 95 50 01 00 00               mov dword ptr [rbp + 0x150], edx
00975A2C  44 89 85 A0 01 00 00            mov dword ptr [rbp + 0x1a0], r8d
00975A33  89 95 88 01 00 00               mov dword ptr [rbp + 0x188], edx
00975A39  89 8D D8 01 00 00               mov dword ptr [rbp + 0x1d8], ecx
00975A3F  B9 00 00 00 C0                  mov ecx, 0xc0000000
00975A44  44 89 8D C0 01 00 00            mov dword ptr [rbp + 0x1c0], r9d
00975A4B  45 33 C9                        xor r9d, r9d
00975A4E  44 89 85 10 02 00 00            mov dword ptr [rbp + 0x210], r8d
00975A55  4C 8D 45 30                     lea r8, [rbp + 0x30]
00975A59  89 95 F8 01 00 00               mov dword ptr [rbp + 0x1f8], edx
00975A5F  48 8B D3                        mov rdx, rbx
00975A62  48 89 85 08 02 00 00            mov qword ptr [rbp + 0x208], rax
00975A69  4C 89 B5 80 00 00 00            mov qword ptr [rbp + 0x80], r14
00975A70  48 89 B5 B8 00 00 00            mov qword ptr [rbp + 0xb8], rsi
00975A77  4C 89 BD F0 00 00 00            mov qword ptr [rbp + 0xf0], r15
00975A7E  C7 85 18 01 00 00 24 01 00 00   mov dword ptr [rbp + 0x118], 0x124
00975A88  4C 89 A5 60 01 00 00            mov qword ptr [rbp + 0x160], r12
00975A8F  4C 89 AD 98 01 00 00            mov qword ptr [rbp + 0x198], r13
00975A96  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
00975A9B  E8 B0 35 F5 FF                  call 0x1408c9050
00975AA0  8B D8                           mov ebx, eax
00975AA2  3D 34 00 00 C0                  cmp eax, 0xc0000034
00975AA7  0F 84 31 FE FF FF               je 0x1409758de
00975AAD  85 C0                           test eax, eax
00975AAF  0F 88 A1 03 00 00               js 0x140975e56
00975AB5  66 41 83 3E 02                  cmp word ptr [r14], 2
00975ABA  77 12                           ja 0x140975ace
00975ABC  48 83 BF 38 01 00 00 00         cmp qword ptr [rdi + 0x138], 0
00975AC4  74 08                           je 0x140975ace
00975AC6  49 8B CE                        mov rcx, r14
00975AC9  E8 32 AD 04 00                  call 0x1409c0800
00975ACE  66 83 3E 02                     cmp word ptr [rsi], 2
00975AD2  77 12                           ja 0x140975ae6
00975AD4  48 83 BF 48 01 00 00 00         cmp qword ptr [rdi + 0x148], 0
00975ADC  74 08                           je 0x140975ae6
00975ADE  48 8B CE                        mov rcx, rsi
00975AE1  E8 1A AD 04 00                  call 0x1409c0800
00975AE6  66 41 83 3F 02                  cmp word ptr [r15], 2
00975AEB  77 12                           ja 0x140975aff
00975AED  48 83 BF 58 01 00 00 00         cmp qword ptr [rdi + 0x158], 0
00975AF5  74 08                           je 0x140975aff
00975AF7  49 8B CF                        mov rcx, r15
00975AFA  E8 01 AD 04 00                  call 0x1409c0800
00975AFF  66 41 83 3C 24 02               cmp word ptr [r12], 2
00975B05  77 12                           ja 0x140975b19
00975B07  48 83 BF 68 01 00 00 00         cmp qword ptr [rdi + 0x168], 0
00975B0F  74 08                           je 0x140975b19
00975B11  49 8B CC                        mov rcx, r12
00975B14  E8 E7 AC 04 00                  call 0x1409c0800
00975B19  45 33 E4                        xor r12d, r12d
00975B1C  66 41 83 7D 00 02               cmp word ptr [r13], 2
00975B22  77 11                           ja 0x140975b35
00975B24  4C 39 A7 78 01 00 00            cmp qword ptr [rdi + 0x178], r12
00975B2B  74 08                           je 0x140975b35
00975B2D  49 8B CD                        mov rcx, r13
00975B30  E8 CB AC 04 00                  call 0x1409c0800
00975B35  48 8D 8F 90 01 00 00            lea rcx, [rdi + 0x190]
00975B3C  66 83 39 02                     cmp word ptr [rcx], 2
00975B40  77 0E                           ja 0x140975b50
00975B42  4C 39 A7 98 01 00 00            cmp qword ptr [rdi + 0x198], r12
00975B49  74 05                           je 0x140975b50
00975B4B  E8 B0 AC 04 00                  call 0x1409c0800
00975B50  8B 87 B8 00 00 00               mov eax, dword ptr [rdi + 0xb8]
00975B56  4C 8D BF 20 01 00 00            lea r15, [rdi + 0x120]
00975B5D  A8 20                           test al, 0x20
00975B5F  74 41                           je 0x140975ba2
00975B61  8B 47 68                        mov eax, dword ptr [rdi + 0x68]
00975B64  A8 04                           test al, 4
00975B66  75 11                           jne 0x140975b79
00975B68  4C 39 A7 28 01 00 00            cmp qword ptr [rdi + 0x128], r12
00975B6F  74 08                           je 0x140975b79
00975B71  49 8B CF                        mov rcx, r15
00975B74  E8 87 AC 04 00                  call 0x1409c0800
00975B79  8B 47 68                        mov eax, dword ptr [rdi + 0x68]
00975B7C  A8 02                           test al, 2
00975B7E  75 22                           jne 0x140975ba2
00975B80  4C 39 A7 38 01 00 00            cmp qword ptr [rdi + 0x138], r12
00975B87  74 08                           je 0x140975b91
00975B89  49 8B CE                        mov rcx, r14
00975B8C  E8 6F AC 04 00                  call 0x1409c0800
00975B91  4C 39 A7 48 01 00 00            cmp qword ptr [rdi + 0x148], r12
00975B98  74 08                           je 0x140975ba2
00975B9A  48 8B CE                        mov rcx, rsi
00975B9D  E8 5E AC 04 00                  call 0x1409c0800
00975BA2  48 8B 8F 28 01 00 00            mov rcx, qword ptr [rdi + 0x128]
00975BA9  48 85 C9                        test rcx, rcx
00975BAC  74 2F                           je 0x140975bdd
00975BAE  66 45 39 27                     cmp word ptr [r15], r12w
00975BB2  74 29                           je 0x140975bdd
00975BB4  4C 8D 87 B8 01 00 00            lea r8, [rdi + 0x1b8]
00975BBB  48 8D 54 24 61                  lea rdx, [rsp + 0x61]
00975BC0  E8 DB 02 00 00                  call 0x140975ea0
00975BC5  8B D8                           mov ebx, eax
00975BC7  85 C0                           test eax, eax
00975BC9  0F 88 0F FD FF FF               js 0x1409758de
00975BCF  44 38 64 24 61                  cmp byte ptr [rsp + 0x61], r12b
00975BD4  74 07                           je 0x140975bdd
00975BD6  83 8F B8 00 00 00 10            or dword ptr [rdi + 0xb8], 0x10
00975BDD  48 8B B7 38 01 00 00            mov rsi, qword ptr [rdi + 0x138]
00975BE4  49 83 CF FF                     or r15, 0xffffffffffffffff
00975BE8  48 85 F6                        test rsi, rsi
00975BEB  74 3C                           je 0x140975c29
00975BED  66 44 39 26                     cmp word ptr [rsi], r12w
00975BF1  74 2E                           je 0x140975c21
00975BF3  45 33 C0                        xor r8d, r8d
00975BF6  33 D2                           xor edx, edx
00975BF8  48 8B CE                        mov rcx, rsi
00975BFB  E8 A0 02 00 00                  call 0x140975ea0
00975C00  8B D8                           mov ebx, eax
00975C02  85 C0                           test eax, eax
00975C04  0F 88 D4 FC FF FF               js 0x1409758de
00975C0A  49 8B C7                        mov rax, r15
00975C0D  48 FF C0                        inc rax
00975C10  66 44 39 24 46                  cmp word ptr [rsi + rax*2], r12w
00975C15  75 F6                           jne 0x140975c0d
00975C17  48 8D 34 46                     lea rsi, [rsi + rax*2]
00975C1B  48 83 C6 02                     add rsi, 2
00975C1F  EB CC                           jmp 0x140975bed
00975C21  85 DB                           test ebx, ebx
00975C23  0F 88 2D 02 00 00               js 0x140975e56
00975C29  48 8B B7 48 01 00 00            mov rsi, qword ptr [rdi + 0x148]
00975C30  48 85 F6                        test rsi, rsi
00975C33  74 3C                           je 0x140975c71
00975C35  66 44 39 26                     cmp word ptr [rsi], r12w
00975C39  74 2E                           je 0x140975c69
00975C3B  45 33 C0                        xor r8d, r8d
00975C3E  33 D2                           xor edx, edx
00975C40  48 8B CE                        mov rcx, rsi
00975C43  E8 58 02 00 00                  call 0x140975ea0
00975C48  8B D8                           mov ebx, eax
00975C4A  85 C0                           test eax, eax
00975C4C  0F 88 8C FC FF FF               js 0x1409758de
00975C52  49 8B C7                        mov rax, r15
00975C55  48 FF C0                        inc rax
00975C58  66 44 39 24 46                  cmp word ptr [rsi + rax*2], r12w
00975C5D  75 F6                           jne 0x140975c55
00975C5F  48 8D 34 46                     lea rsi, [rsi + rax*2]
00975C63  48 83 C6 02                     add rsi, 2
00975C67  EB CC                           jmp 0x140975c35
00975C69  85 DB                           test ebx, ebx
00975C6B  0F 88 E5 01 00 00               js 0x140975e56
00975C71  8B 87 B8 00 00 00               mov eax, dword ptr [rdi + 0xb8]
00975C77  A8 20                           test al, 0x20
00975C79  0F 85 D0 01 00 00               jne 0x140975e4f
00975C7F  33 D2                           xor edx, edx
00975C81  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00975C85  41 B8 A0 00 00 00               mov r8d, 0xa0
00975C8B  E8 B0 0F D5 FF                  call 0x1406c6c40
00975C90  4C 8B 4F 10                     mov r9, qword ptr [rdi + 0x10]
00975C94  48 8D 05 2D D2 69 FF            lea rax, [rip - 0x962dd3]
00975C9B  48 8B 57 40                     mov rdx, qword ptr [rdi + 0x40]
00975C9F  48 8D B7 F0 00 00 00            lea rsi, [rdi + 0xf0]
00975CA6  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
00975CAA  4C 8D B7 10 01 00 00            lea r14, [rdi + 0x110]
00975CB1  B9 06 00 00 00                  mov ecx, 6
00975CB6  C7 44 24 28 04 00 00 00         mov dword ptr [rsp + 0x28], 4
00975CBE  48 8D 05 CB C2 69 FF            lea rax, [rip - 0x963d35]
00975CC5  C7 45 98 0D 00 00 00            mov dword ptr [rbp - 0x68], 0xd
00975CCC  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
00975CD0  48 8D 05 21 D2 69 FF            lea rax, [rip - 0x962ddf]
00975CD7  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00975CDB  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00975CE0  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00975CE4  44 8D 69 02                     lea r13d, [rcx + 2]
00975CE8  48 8D 05 F1 D1 69 FF            lea rax, [rip - 0x962e0f]
00975CEF  48 89 75 A0                     mov qword ptr [rbp - 0x60], rsi
00975CF3  48 89 45 08                     mov qword ptr [rbp + 8], rax
00975CF7  45 8B C5                        mov r8d, r13d
00975CFA  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00975CFF  C7 45 A8 10 00 00 00            mov dword ptr [rbp - 0x58], 0x10
00975D06  48 89 45 18                     mov qword ptr [rbp + 0x18], rax
00975D0A  48 8D 45 90                     lea rax, [rbp - 0x70]
00975D0E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00975D13  C7 45 C0 12 00 00 00            mov dword ptr [rbp - 0x40], 0x12
00975D1A  4C 89 75 C8                     mov qword ptr [rbp - 0x38], r14
00975D1E  89 4D D4                        mov dword ptr [rbp - 0x2c], ecx
00975D21  C7 45 E8 11 00 00 00            mov dword ptr [rbp - 0x18], 0x11
00975D28  C7 45 F8 01 00 00 00            mov dword ptr [rbp - 8], 1
00975D2F  C7 45 10 12 20 00 00            mov dword ptr [rbp + 0x10], 0x2012
00975D36  89 4D 24                        mov dword ptr [rbp + 0x24], ecx
00975D39  E8 2E 1A 00 00                  call 0x14097776c
00975D3E  8B D8                           mov ebx, eax
00975D40  85 C0                           test eax, eax
00975D42  0F 88 0E 01 00 00               js 0x140975e56
00975D48  44 39 65 B0                     cmp dword ptr [rbp - 0x50], r12d
00975D4C  7C 1D                           jl 0x140975d6b
00975D4E  48 8D 97 00 01 00 00            lea rdx, [rdi + 0x100]
00975D55  41 B0 01                        mov r8b, 1
00975D58  48 8B CE                        mov rcx, rsi
00975D5B  E8 F0 F6 F9 FF                  call 0x140915450
00975D60  8B D8                           mov ebx, eax
00975D62  85 C0                           test eax, eax
00975D64  79 0B                           jns 0x140975d71
00975D66  E9 EB 00 00 00                  jmp 0x140975e56
00975D6B  0F 57 C0                        xorps xmm0, xmm0
00975D6E  0F 11 06                        movups xmmword ptr [rsi], xmm0
00975D71  44 39 65 D8                     cmp dword ptr [rbp - 0x28], r12d
00975D75  7D 0A                           jge 0x140975d81
00975D77  33 D2                           xor edx, edx
00975D79  49 8B CE                        mov rcx, r14
00975D7C  E8 FF 49 AB FF                  call 0x14042a780
00975D81  44 39 65 00                     cmp dword ptr [rbp], r12d
00975D85  7D 09                           jge 0x140975d90
00975D87  41 8A C4                        mov al, r12b
00975D8A  88 44 24 60                     mov byte ptr [rsp + 0x60], al
00975D8E  EB 04                           jmp 0x140975d94
00975D90  8A 44 24 60                     mov al, byte ptr [rsp + 0x60]
00975D94  41 3A C7                        cmp al, r15b
00975D97  75 07                           jne 0x140975da0
00975D99  83 8F B8 00 00 00 40            or dword ptr [rdi + 0xb8], 0x40
00975DA0  44 39 65 28                     cmp dword ptr [rbp + 0x28], r12d
00975DA4  7D 0C                           jge 0x140975db2
00975DA6  33 D2                           xor edx, edx
00975DA8  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
00975DAD  E8 CE 49 AB FF                  call 0x14042a780
00975DB2  4C 39 64 24 78                  cmp qword ptr [rsp + 0x78], r12
00975DB7  0F 84 84 00 00 00               je 0x140975e41
00975DBD  66 83 7C 24 70 02               cmp word ptr [rsp + 0x70], 2
00975DC3  76 7C                           jbe 0x140975e41
00975DC5  0F BA AF B8 00 00 00 07         bts dword ptr [rdi + 0xb8], 7
00975DCD  48 8D 44 24 68                  lea rax, [rsp + 0x68]
00975DD2  4C 8B 4F 10                     mov r9, qword ptr [rdi + 0x10]
00975DD6  45 8B C5                        mov r8d, r13d
00975DD9  48 8B 57 40                     mov rdx, qword ptr [rdi + 0x40]
00975DDD  48 8B 0D B4 05 4F 00            mov rcx, qword ptr [rip + 0x4f05b4]
00975DE4  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
00975DE9  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00975DEE  48 8D 44 24 62                  lea rax, [rsp + 0x62]
00975DF3  C7 44 24 40 01 00 00 00         mov dword ptr [rsp + 0x40], 1
00975DFB  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00975E00  48 8D 44 24 64                  lea rax, [rsp + 0x64]
00975E05  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00975E0A  48 8D 05 07 C2 6A FF            lea rax, [rip - 0x953df9]
00975E11  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00975E16  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00975E1B  E8 60 C3 F6 FF                  call 0x1408e2180
00975E20  85 C0                           test eax, eax
00975E22  78 15                           js 0x140975e39
00975E24  83 7C 24 64 11                  cmp dword ptr [rsp + 0x64], 0x11
00975E29  75 0E                           jne 0x140975e39
00975E2B  83 7C 24 68 01                  cmp dword ptr [rsp + 0x68], 1
00975E30  75 07                           jne 0x140975e39
00975E32  44 38 64 24 62                  cmp byte ptr [rsp + 0x62], r12b
00975E37  75 08                           jne 0x140975e41
00975E39  0F BA AF B8 00 00 00 08         bts dword ptr [rdi + 0xb8], 8
00975E41  48 8B CF                        mov rcx, rdi
00975E44  E8 73 F6 FF FF                  call 0x1409754bc
00975E49  8B D8                           mov ebx, eax
00975E4B  85 C0                           test eax, eax
00975E4D  78 07                           js 0x140975e56
00975E4F  83 8F B8 00 00 00 01            or dword ptr [rdi + 0xb8], 1
00975E56  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
00975E5B  48 85 C9                        test rcx, rcx
00975E5E  74 05                           je 0x140975e65
00975E60  E8 EB C9 20 00                  call 0x140b82850
00975E65  8B C3                           mov eax, ebx
00975E67  48 8B 8D 60 02 00 00            mov rcx, qword ptr [rbp + 0x260]
00975E6E  48 33 CC                        xor rcx, rsp
00975E71  E8 CA 67 D3 FF                  call 0x1406ac640
00975E76  4C 8D 9C 24 70 03 00 00         lea r11, [rsp + 0x370]
00975E7E  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00975E82  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00975E86  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00975E8A  49 8B E3                        mov rsp, r11
00975E8D  41 5F                           pop r15
00975E8F  41 5E                           pop r14
00975E91  41 5D                           pop r13
00975E93  41 5C                           pop r12
00975E95  5D                              pop rbp
00975E96  C3                              ret
00975E97  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiDevCfgQueryDriverConfiguration(__int64 a1)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m320;
    unsigned __int64 v_stack_m328;
    unsigned int v_stack_m330;
    unsigned int v_stack_m334;
    unsigned __int8 v_stack_m336;
    unsigned __int8 v_stack_m337;
    unsigned __int8 v_stack_m338;
    unsigned int v_stack_m348;
    unsigned __int64 v_stack_m350;
    unsigned int v_stack_m358;
    unsigned __int64 v_stack_m360;
    unsigned __int64 v_stack_m368;
    unsigned __int8 v_stack_m370;
    unsigned __int64 v_stack_m378;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (880);
    result = (*(unsigned __int64 *)(v_rip + 4804295)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 664 + 608) = result;
    v_r12 = 0;
    v_stack_m337 = 0;
    v_stack_m338 = 0;
    v_stack_m336 = 0;
    v_stack_m328 = 0;
    v_stack_m320 = 0;
    v_stack_m334 = 1;
    v_stack_m330 = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 184)))) & (32)) != 0) goto loc_009758E8;
    result = PiDevCfgBuildDriverConfigurationId(a1, a1 + 424, a3, a4);
    if (sign_flag) goto loc_00975E56;
    if ((*(unsigned __int64 *)(a1 + 24)) == 0) goto loc_009758DE;
    if (*(unsigned __int64 *)(a1 + 32) != 0) goto loc_009758FB;
loc_009758DE:
    goto loc_00975E56;
loc_009758E8:
    if (*(unsigned __int64 *)(a1 + 32) != 0) goto loc_009758FB;
    goto loc_00975E65;
loc_009758FB:
    a2 = 0;
    result = memset(v_rsp - 664 + 48, a2, 560, a4);
    *(unsigned int *)(v_rsp - 664 + 80) = 0x1000000ULL;
    *(unsigned int *)(v_rsp - 664 + 136) = (unsigned int)((unsigned int)(0x7000000ULL));
    *(unsigned int *)(v_rsp - 664 + 56) = 288;
    *(unsigned int *)(v_rsp - 664 + 192) = (unsigned int)((unsigned int)(0x7000000ULL));
    *(unsigned __int64 *)(v_rsp - 664 + 64) = v_rip + 1611482;
    *(unsigned int *)(v_rsp - 664 + 248) = (unsigned int)((unsigned int)(0x7000000ULL));
    *(unsigned int *)(v_rsp - 664 + 112) = (unsigned int)(288 + 16);
    *(unsigned __int64 *)(v_rsp - 664 + 72) = a1 + 288;
    *(unsigned int *)(v_rsp - 664 + 168) = (unsigned int)(288 + 16);
    *(unsigned __int64 *)(v_rsp - 664 + 120) = v_rip + 1611441;
    *(unsigned int *)(v_rsp - 664 + 224) = (unsigned int)(288 + 16);
    *(unsigned __int64 *)(v_rsp - 664 + 176) = v_rip + 1611449;
    *(unsigned int *)(v_rsp - 664 + 304) = (unsigned int)((unsigned int)(0x4000000ULL));
    *(unsigned __int64 *)(v_rsp - 664 + 232) = v_rip + 1611502;
    *(unsigned int *)(v_rsp - 664 + 360) = (unsigned int)((unsigned int)(0x7000000ULL));
    *(unsigned __int64 *)(v_rsp - 664 + 288) = v_rip + 1610899;
    *(unsigned __int64 *)(v_rsp - 664 + 296) = a1 + 416;
    *(unsigned __int64 *)(v_rsp - 664 + 344) = v_rip + 1611472;
    *(unsigned __int64 *)(v_rsp - 664 + 400) = v_rip + 1611490;
    *(unsigned __int64 *)(v_rsp - 664 + 456) = v_rip + 1611508;
    *(unsigned __int64 *)(v_rsp - 664 + 464) = a1 + 420;
    *(unsigned __int64 *)(v_rsp - 664 + 512) = v_rip + 1611336;
    *(unsigned int *)(v_rsp - 664 + 336) = (unsigned int)(288 + 16);
    *(unsigned int *)(v_rsp - 664 + 416) = (unsigned int)((unsigned int)(0x7000000ULL));
    *(unsigned int *)(v_rsp - 664 + 392) = (unsigned int)(288 + 16);
    *(unsigned int *)(v_rsp - 664 + 472) = (unsigned int)((unsigned int)(0x4000000ULL));
    *(unsigned int *)(v_rsp - 664 + 448) = 288;
    a4 = 0;
    *(unsigned int *)(v_rsp - 664 + 528) = (unsigned int)((unsigned int)(0x7000000ULL));
    *(unsigned int *)(v_rsp - 664 + 504) = (unsigned int)(288 + 16);
    *(unsigned __int64 *)(v_rsp - 664 + 520) = a1 + 400;
    *(unsigned __int64 *)(v_rsp - 664 + 128) = a1 + 304;
    *(unsigned __int64 *)(v_rsp - 664 + 184) = a1 + 320;
    *(unsigned __int64 *)(v_rsp - 664 + 240) = a1 + 336;
    *(unsigned int *)(v_rsp - 664 + 280) = 292;
    *(unsigned __int64 *)(v_rsp - 664 + 352) = a1 + 352;
    *(unsigned __int64 *)(v_rsp - 664 + 408) = a1 + 368;
    v_stack_m370 = 1;
    result = RtlpQueryRegistryValues((unsigned int)(0xC0000000ULL), (unsigned int)(0xC0000493ULL), v_rsp - 664 + 48, a4);
    if (((unsigned int)(result)) == 0xC0000034ULL) goto loc_009758DE;
    if (sign_flag) goto loc_00975E56;
    if ((*(unsigned __int16 *)(a1 + 304)) > 2) goto loc_00975ACE;
    if ((*(unsigned __int64 *)(a1 + 312)) != 0) {
        a1 = a1 + 304;
        result = RtlFreeAnsiString(a1, (unsigned int)(0xC0000493ULL), v_rsp - 664 + 48, a4);
    }
    if ((*(unsigned __int16 *)(a1 + 320)) > 2) goto loc_00975AE6;
    if ((*(unsigned __int64 *)(a1 + 328)) != 0) {
        a1 = a1 + 320;
        result = RtlFreeAnsiString(a1, (unsigned int)(0xC0000493ULL), v_rsp - 664 + 48, a4);
    }
    if ((*(unsigned __int16 *)(a1 + 336)) > 2) goto loc_00975AFF;
    if ((*(unsigned __int64 *)(a1 + 344)) != 0) {
        a1 = a1 + 336;
        result = RtlFreeAnsiString(a1, (unsigned int)(0xC0000493ULL), v_rsp - 664 + 48, a4);
    }
    if ((*(unsigned __int16 *)(a1 + 352)) > 2) goto loc_00975B19;
    if ((*(unsigned __int64 *)(a1 + 360)) != 0) {
        a1 = a1 + 352;
        result = RtlFreeAnsiString(a1, (unsigned int)(0xC0000493ULL), v_rsp - 664 + 48, a4);
    }
    v_r12 = 0;
    if ((*(unsigned __int16 *)(a1 + 368)) > 2) goto loc_00975B35;
    if ((*(unsigned __int64 *)(a1 + 376)) != 0) {
        a1 = a1 + 368;
        result = RtlFreeAnsiString(a1, (unsigned int)(0xC0000493ULL), v_rsp - 664 + 48, a4);
    }
    if ((*(unsigned __int16 *)(a1 + 400)) > 2) goto loc_00975B50;
    if ((*(unsigned __int64 *)(a1 + 408)) != 0) {
        result = RtlFreeAnsiString(a1 + 400, (unsigned int)(0xC0000493ULL), v_rsp - 664 + 48, a4);
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 184)))) & (32)) == 0) goto loc_00975BA2;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 104)))) & (4)) != 0) goto loc_00975B79;
    result = (unsigned int)(*(unsigned int *)(a1 + 104));
    if ((*(unsigned __int64 *)(a1 + 296)) != 0) {
        a1 = a1 + 288;
        result = RtlFreeAnsiString(a1, (unsigned int)(0xC0000493ULL), v_rsp - 664 + 48, a4);
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 104)))) & (2)) != 0) goto loc_00975BA2;
    result = (unsigned int)(*(unsigned int *)(a1 + 104));
    if ((*(unsigned __int64 *)(a1 + 312)) != 0) {
        a1 = a1 + 304;
        result = RtlFreeAnsiString(a1, (unsigned int)(0xC0000493ULL), v_rsp - 664 + 48, a4);
    }
    if ((*(unsigned __int64 *)(a1 + 328)) != 0) {
        a1 = a1 + 320;
        result = RtlFreeAnsiString(a1, (unsigned int)(0xC0000493ULL), v_rsp - 664 + 48, a4);
    }
    if (*(unsigned __int64 *)(a1 + 296) == 0) goto loc_00975BDD;
    if ((*(unsigned __int16 *)(a1 + 288)) == 0) goto loc_00975BDD;
    result = PiDevCfgVerifyService(*(unsigned __int64 *)(a1 + 296), v_stack_m337, a1 + 440, a4);
    if (sign_flag) goto loc_009758DE;
    if (v_stack_m337 != 0) {
    }
    v_r15 = (a1 + 288) | (-1);
    if (*(unsigned __int64 *)(a1 + 312) == 0) goto loc_00975C29;
loc_00975BED:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 312))) == 0) goto loc_00975C21;
    a3 = 0;
    a2 = 0;
    result = PiDevCfgVerifyService(*(unsigned __int64 *)(a1 + 312), a2, a3, a4);
    if (sign_flag) goto loc_009758DE;
loc_00975C0D:
    result = (v_r15) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 312) + result * 2)) != 0) goto loc_00975C0D;
    v_rsi = (*(unsigned __int64 *)(a1 + 312) + result * 2) + (2);
    goto loc_00975BED;
loc_00975C21:
    if (sign_flag) goto loc_00975E56;
loc_00975C29:
    if (*(unsigned __int64 *)(a1 + 328) == 0) goto loc_00975C71;
loc_00975C35:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 328))) == 0) goto loc_00975C69;
    a3 = 0;
    a2 = 0;
    result = PiDevCfgVerifyService(*(unsigned __int64 *)(a1 + 328), a2, a3, a4);
    if (sign_flag) goto loc_009758DE;
loc_00975C55:
    result = (v_r15) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 328) + result * 2)) != 0) goto loc_00975C55;
    v_rsi = (*(unsigned __int64 *)(a1 + 328) + result * 2) + (2);
    goto loc_00975C35;
loc_00975C69:
    if (sign_flag) goto loc_00975E56;
loc_00975C71:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 184)))) & (32)) != 0) goto loc_00975E4F;
    a2 = 0;
    result = memset(v_rsp - 664 - 112, a2, 160, a4);
    *(unsigned __int64 *)(v_rsp - 664 - 112) = v_rip - 9842131;
    v_stack_m370 = 4;
    *(unsigned int *)(v_rsp - 664 - 104) = 13;
    *(unsigned __int64 *)(v_rsp - 664 - 72) = v_rip - 9846069;
    *(unsigned __int64 *)(v_rsp - 664 - 32) = v_rip - 9842143;
    *(unsigned __int64 *)(v_rsp - 664 - 16) = v_stack_m338;
    *(unsigned __int64 *)(v_rsp - 664 - 96) = a1 + 240;
    *(unsigned __int64 *)(v_rsp - 664 + 8) = v_rip - 9842191;
    *(unsigned int *)(v_rsp - 664 - 88) = 16;
    *(unsigned __int64 *)(v_rsp - 664 + 24) = v_stack_m328;
    v_stack_m378 = v_rsp - 664 - 112;
    *(unsigned int *)(v_rsp - 664 - 64) = 18;
    *(unsigned __int64 *)(v_rsp - 664 - 56) = a1 + 272;
    *(unsigned int *)(v_rsp - 664 - 44) = 6;
    *(unsigned int *)(v_rsp - 664 - 24) = 17;
    *(unsigned int *)(v_rsp - 664 - 8) = 1;
    *(unsigned int *)(v_rsp - 664 + 16) = 0x2012ULL;
    *(unsigned int *)(v_rsp - 664 + 36) = 6;
    result = PiDevCfgQueryObjectProperties(6, *(unsigned __int64 *)(a1 + 64), (unsigned int)((unsigned int)(6 + 2)), *(unsigned __int64 *)(a1 + 16));
    if (sign_flag) goto loc_00975E56;
    if ((*(unsigned int *)(v_rsp - 664 - 80)) < 0) goto loc_00975D6B;
    result = RtlStringFromGUIDEx(a1 + 240, a1 + 256, 1, *(unsigned __int64 *)(a1 + 16));
    if (!sign_flag) goto loc_00975D71;
    goto loc_00975E56;
loc_00975D6B:
    *(unsigned __int64 *)(a1 + 240) = v_xmm0;
loc_00975D71:
    if ((*(unsigned int *)(v_rsp - 664 - 40)) < 0) {
        a2 = 0;
        a1 = a1 + 272;
        result = RtlInitUnicodeString(a1, a2, 1, *(unsigned __int64 *)(a1 + 16));
    }
    if ((*(unsigned int *)(v_rsp - 664)) >= 0) goto loc_00975D90;
    v_stack_m338 = 0;
    goto loc_00975D94;
loc_00975D90:
loc_00975D94:
    if (((unsigned __int8)(v_stack_m338)) == ((unsigned __int8)(v_r15))) {
    }
    result = v_stack_m338;
    if ((*(unsigned int *)(v_rsp - 664 + 40)) < 0) {
        a2 = 0;
        a1 = v_stack_m328;
        result = RtlInitUnicodeString(a1, a2, 1, *(unsigned __int64 *)(a1 + 16));
    }
    if (v_stack_m320 == 0) goto loc_00975E41;
    if (v_stack_m328 <= 2) goto loc_00975E41;
    v_stack_m348 = 0;
    v_stack_m350 = v_stack_m330;
    v_stack_m358 = 1;
    v_stack_m360 = v_stack_m336;
    v_stack_m368 = v_stack_m334;
    v_stack_m370 = v_rip - 9780729;
    v_stack_m378 = 0;
    result = PnpGetObjectProperty(*(unsigned __int64 *)(v_rip + 5178804), *(unsigned __int64 *)(a1 + 64), (unsigned int)((unsigned int)(6 + 2)), *(unsigned __int64 *)(a1 + 16));
    if (sign_flag) goto loc_00975E39;
    if (v_stack_m334 != 17) goto loc_00975E39;
    if (v_stack_m330 != 1) goto loc_00975E39;
    if (v_stack_m336 == 0) {
    }
    result = PiDevCfgQueryIncludedDriverConfigurations(a1, *(unsigned __int64 *)(a1 + 64), (unsigned int)((unsigned int)(6 + 2)), *(unsigned __int64 *)(a1 + 16));
    if (!(sign_flag)) {
    }
    if (v_stack_m320 != 0) {
        result = ExFreePool(v_stack_m320, *(unsigned __int64 *)(a1 + 64), (unsigned int)((unsigned int)(6 + 2)), *(unsigned __int64 *)(a1 + 16));
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 664 + 608)) ^ (v_rsp);
    result = _security_check_cookie(a1, *(unsigned __int64 *)(a1 + 64), (unsigned int)((unsigned int)(6 + 2)), *(unsigned __int64 *)(a1 + 16));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PiDevCfgQueryDriverConfiguration(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m320;
    uint64_t v_stack_m328;
    uint32_t v_stack_m330;
    uint32_t v_stack_m334;
    uint8_t v_stack_m336;
    uint8_t v_stack_m337;
    uint8_t v_stack_m338;
    uint32_t v_stack_m348;
    uint64_t v_stack_m350;
    uint32_t v_stack_m358;
    uint64_t v_stack_m360;
    uint64_t v_stack_m368;
    uint8_t v_stack_m370;
    uint64_t v_stack_m378;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (880);
    result = (*(uint64_t *)(v_rip + 0x494EC7)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x298 + 0x260) = result;
    local_r12 = 0;
    v_stack_m337 = 0;
    v_stack_m338 = 0;
    v_stack_m336 = 0;
    v_stack_m328 = 0;
    v_stack_m320 = 0;
    v_stack_m334 = 1;
    v_stack_m330 = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0xB8)))) & (32)) != 0) goto loc_009758E8;
    result = PiDevCfgBuildDriverConfigurationId(Arg1, Arg1 + 424, a3, a4);
    if (sign_flag) goto loc_00975E56;
    if ((*(uint64_t *)(arg1 + 0x18)) == 0) goto loc_009758DE;
    if (*(uint64_t *)(arg1 + 0x20) != 0) goto loc_009758FB;
loc_009758DE:
    goto loc_00975E56;
loc_009758E8:
    if (*(uint64_t *)(arg1 + 0x20) != 0) goto loc_009758FB;
    goto loc_00975E65;
loc_009758FB:
    a2 = 0;
    result = memset(local_rsp - 664 + 48, a2, 560, a4);
    *(uint32_t *)(local_rsp - 0x298 + 0x50) = 0x1000000ULL;
    *(uint32_t *)(local_rsp - 0x298 + 0x88) = (uint32_t)((uint32_t)(0x7000000ULL));
    *(uint32_t *)(local_rsp - 0x298 + 0x38) = 288;
    *(uint32_t *)(local_rsp - 0x298 + 0xC0) = (uint32_t)((uint32_t)(0x7000000ULL));
    *(uint64_t *)(local_rsp - 0x298 + 0x40) = v_rip + 1611482;
    *(uint32_t *)(local_rsp - 0x298 + 0xF8) = (uint32_t)((uint32_t)(0x7000000ULL));
    *(uint32_t *)(local_rsp - 0x298 + 0x70) = (uint32_t)(288 + 16);
    *(void **)(local_rsp - 0x298 + 0x48) = Arg1 + 288;
    *(uint32_t *)(local_rsp - 0x298 + 0xA8) = (uint32_t)(288 + 16);
    *(uint64_t *)(local_rsp - 0x298 + 0x78) = v_rip + 1611441;
    *(uint32_t *)(local_rsp - 0x298 + 0xE0) = (uint32_t)(288 + 16);
    *(uint64_t *)(local_rsp - 0x298 + 0xB0) = v_rip + 1611449;
    *(uint32_t *)(local_rsp - 0x298 + 0x130) = (uint32_t)((uint32_t)(0x4000000ULL));
    *(uint64_t *)(local_rsp - 0x298 + 0xE8) = v_rip + 1611502;
    *(uint32_t *)(local_rsp - 0x298 + 0x168) = (uint32_t)((uint32_t)(0x7000000ULL));
    *(uint64_t *)(local_rsp - 0x298 + 0x120) = v_rip + 1610899;
    *(void **)(local_rsp - 0x298 + 0x128) = Arg1 + 416;
    *(uint64_t *)(local_rsp - 0x298 + 0x158) = v_rip + 1611472;
    *(uint64_t *)(local_rsp - 0x298 + 0x190) = v_rip + 1611490;
    *(uint64_t *)(local_rsp - 0x298 + 0x1C8) = v_rip + 1611508;
    *(void **)(local_rsp - 0x298 + 0x1D0) = Arg1 + 420;
    *(uint64_t *)(local_rsp - 0x298 + 0x200) = v_rip + 1611336;
    *(uint32_t *)(local_rsp - 0x298 + 0x150) = (uint32_t)(288 + 16);
    *(uint32_t *)(local_rsp - 0x298 + 0x1A0) = (uint32_t)((uint32_t)(0x7000000ULL));
    *(uint32_t *)(local_rsp - 0x298 + 0x188) = (uint32_t)(288 + 16);
    *(uint32_t *)(local_rsp - 0x298 + 0x1D8) = (uint32_t)((uint32_t)(0x4000000ULL));
    *(uint32_t *)(local_rsp - 0x298 + 0x1C0) = 288;
    a4 = 0;
    *(uint32_t *)(local_rsp - 0x298 + 0x210) = (uint32_t)((uint32_t)(0x7000000ULL));
    *(uint32_t *)(local_rsp - 0x298 + 0x1F8) = (uint32_t)(288 + 16);
    *(void **)(local_rsp - 0x298 + 0x208) = Arg1 + 400;
    *(void **)(local_rsp - 0x298 + 0x80) = Arg1 + 304;
    *(void **)(local_rsp - 0x298 + 0xB8) = Arg1 + 320;
    *(void **)(local_rsp - 0x298 + 0xF0) = Arg1 + 336;
    *(uint32_t *)(local_rsp - 0x298 + 0x118) = 292;
    *(void **)(local_rsp - 0x298 + 0x160) = Arg1 + 352;
    *(void **)(local_rsp - 0x298 + 0x198) = Arg1 + 368;
    v_stack_m370 = 1;
    result = RtlpQueryRegistryValues((uint32_t)(0xC0000000ULL), (uint32_t)(0xC0000493ULL), local_rsp - 664 + 48, a4);
    if (((uint32_t)(result)) == 0xC0000034ULL) goto loc_009758DE;
    if (sign_flag) goto loc_00975E56;
    if ((*(uint16_t *)(arg1 + 0x130)) > 2) goto loc_00975ACE;
    if ((*(uint64_t *)(arg1 + 0x138)) != 0) {
        Arg1 = Arg1 + 304;
        result = RtlFreeAnsiString(Arg1, (uint32_t)(0xC0000493ULL), local_rsp - 664 + 48, a4);
    }
    if ((*(uint16_t *)(arg1 + 0x140)) > 2) goto loc_00975AE6;
    if ((*(uint64_t *)(arg1 + 0x148)) != 0) {
        Arg1 = Arg1 + 320;
        result = RtlFreeAnsiString(Arg1, (uint32_t)(0xC0000493ULL), local_rsp - 664 + 48, a4);
    }
    if ((*(uint16_t *)(arg1 + 0x150)) > 2) goto loc_00975AFF;
    if ((*(uint64_t *)(arg1 + 0x158)) != 0) {
        Arg1 = Arg1 + 336;
        result = RtlFreeAnsiString(Arg1, (uint32_t)(0xC0000493ULL), local_rsp - 664 + 48, a4);
    }
    if ((*(uint16_t *)(arg1 + 0x160)) > 2) goto loc_00975B19;
    if ((*(uint64_t *)(arg1 + 0x168)) != 0) {
        Arg1 = Arg1 + 352;
        result = RtlFreeAnsiString(Arg1, (uint32_t)(0xC0000493ULL), local_rsp - 664 + 48, a4);
    }
    local_r12 = 0;
    if ((*(uint16_t *)(arg1 + 0x170)) > 2) goto loc_00975B35;
    if ((*(uint64_t *)(arg1 + 0x178)) != 0) {
        Arg1 = Arg1 + 368;
        result = RtlFreeAnsiString(Arg1, (uint32_t)(0xC0000493ULL), local_rsp - 664 + 48, a4);
    }
    if ((*(uint16_t *)(arg1 + 0x190)) > 2) goto loc_00975B50;
    if ((*(uint64_t *)(arg1 + 0x198)) != 0) {
        result = RtlFreeAnsiString(Arg1 + 400, (uint32_t)(0xC0000493ULL), local_rsp - 664 + 48, a4);
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0xB8)))) & (32)) == 0) goto loc_00975BA2;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x68)))) & (4)) != 0) goto loc_00975B79;
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x68));
    if ((*(uint64_t *)(arg1 + 0x128)) != 0) {
        Arg1 = Arg1 + 288;
        result = RtlFreeAnsiString(Arg1, (uint32_t)(0xC0000493ULL), local_rsp - 664 + 48, a4);
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x68)))) & (2)) != 0) goto loc_00975BA2;
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x68));
    if ((*(uint64_t *)(arg1 + 0x138)) != 0) {
        Arg1 = Arg1 + 304;
        result = RtlFreeAnsiString(Arg1, (uint32_t)(0xC0000493ULL), local_rsp - 664 + 48, a4);
    }
    if ((*(uint64_t *)(arg1 + 0x148)) != 0) {
        Arg1 = Arg1 + 320;
        result = RtlFreeAnsiString(Arg1, (uint32_t)(0xC0000493ULL), local_rsp - 664 + 48, a4);
    }
    if (*(uint64_t *)(arg1 + 0x128) == 0) goto loc_00975BDD;
    if ((*(uint16_t *)(arg1 + 0x120)) == 0) goto loc_00975BDD;
    result = PiDevCfgVerifyService(*(uint64_t *)(arg1 + 0x128), v_stack_m337, Arg1 + 440, a4);
    if (sign_flag) goto loc_009758DE;
    if (v_stack_m337 != 0) {
    }
    local_r15 = (Arg1 + 288) | (-1);
    if (*(uint64_t *)(arg1 + 0x138) == 0) goto loc_00975C29;
loc_00975BED:
    if ((*(uint16_t *)(*(uint64_t *)(arg1 + 0x138))) == 0) goto loc_00975C21;
    a3 = 0;
    a2 = 0;
    result = PiDevCfgVerifyService(*(uint64_t *)(arg1 + 0x138), a2, a3, a4);
    if (sign_flag) goto loc_009758DE;
loc_00975C0D:
    result = (local_r15) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(arg1 + 0x138) + result * 2)) != 0) goto loc_00975C0D;
    local_rsi = (*(uint64_t *)(arg1 + 0x138) + result * 2) + (2);
    goto loc_00975BED;
loc_00975C21:
    if (sign_flag) goto loc_00975E56;
loc_00975C29:
    if (*(uint64_t *)(arg1 + 0x148) == 0) goto loc_00975C71;
loc_00975C35:
    if ((*(uint16_t *)(*(uint64_t *)(arg1 + 0x148))) == 0) goto loc_00975C69;
    a3 = 0;
    a2 = 0;
    result = PiDevCfgVerifyService(*(uint64_t *)(arg1 + 0x148), a2, a3, a4);
    if (sign_flag) goto loc_009758DE;
loc_00975C55:
    result = (local_r15) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(arg1 + 0x148) + result * 2)) != 0) goto loc_00975C55;
    local_rsi = (*(uint64_t *)(arg1 + 0x148) + result * 2) + (2);
    goto loc_00975C35;
loc_00975C69:
    if (sign_flag) goto loc_00975E56;
loc_00975C71:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0xB8)))) & (32)) != 0) goto loc_00975E4F;
    a2 = 0;
    result = memset(local_rsp - 664 - 112, a2, 160, a4);
    *(uint64_t *)(local_rsp - 0x298 - 0x70) = v_rip - 9842131;
    v_stack_m370 = 4;
    *(uint32_t *)(local_rsp - 0x298 - 0x68) = 13;
    *(uint64_t *)(local_rsp - 0x298 - 0x48) = v_rip - 9846069;
    *(uint64_t *)(local_rsp - 0x298 - 0x20) = v_rip - 9842143;
    *(uint64_t *)(local_rsp - 0x298 - 0x10) = v_stack_m338;
    *(void **)(local_rsp - 0x298 - 0x60) = Arg1 + 240;
    *(uint64_t *)(local_rsp - 0x298 + 0x8) = v_rip - 9842191;
    *(uint32_t *)(local_rsp - 0x298 - 0x58) = 16;
    *(uint64_t *)(local_rsp - 0x298 + 0x18) = v_stack_m328;
    v_stack_m378 = local_rsp - 664 - 112;
    *(uint32_t *)(local_rsp - 0x298 - 0x40) = 18;
    *(void **)(local_rsp - 0x298 - 0x38) = Arg1 + 272;
    *(uint32_t *)(local_rsp - 0x298 - 0x2C) = 6;
    *(uint32_t *)(local_rsp - 0x298 - 0x18) = 17;
    *(uint32_t *)(local_rsp - 0x298 - 0x8) = 1;
    *(uint32_t *)(local_rsp - 0x298 + 0x10) = 0x2012ULL;
    *(uint32_t *)(local_rsp - 0x298 + 0x24) = 6;
    result = PiDevCfgQueryObjectProperties(6, *(uint64_t *)(arg1 + 0x40), (uint32_t)((uint32_t)(6 + 2)), *(uint64_t *)(arg1 + 0x10));
    if (sign_flag) goto loc_00975E56;
    if ((*(uint32_t *)(local_rsp - 0x298 - 0x50)) < 0) goto loc_00975D6B;
    result = RtlStringFromGUIDEx(Arg1 + 240, Arg1 + 256, 1, *(uint64_t *)(arg1 + 0x10));
    if (!sign_flag) goto loc_00975D71;
    goto loc_00975E56;
loc_00975D6B:
    *(uint64_t *)(arg1 + 0xF0) = v_xmm0;
loc_00975D71:
    if ((*(uint32_t *)(local_rsp - 0x298 - 0x28)) < 0) {
        a2 = 0;
        Arg1 = Arg1 + 272;
        result = RtlInitUnicodeString(Arg1, a2, 1, *(uint64_t *)(arg1 + 0x10));
    }
    if ((*(uint32_t *)(local_rsp - 0x298)) >= 0) goto loc_00975D90;
    v_stack_m338 = 0;
    goto loc_00975D94;
loc_00975D90:
loc_00975D94:
    if (((uint8_t)(v_stack_m338)) == ((uint8_t)(local_r15))) {
    }
    result = v_stack_m338;
    if ((*(uint32_t *)(local_rsp - 0x298 + 0x28)) < 0) {
        a2 = 0;
        Arg1 = v_stack_m328;
        result = RtlInitUnicodeString(Arg1, a2, 1, *(uint64_t *)(arg1 + 0x10));
    }
    if (v_stack_m320 == 0) goto loc_00975E41;
    if (v_stack_m328 <= 2) goto loc_00975E41;
    v_stack_m348 = 0;
    v_stack_m350 = v_stack_m330;
    v_stack_m358 = 1;
    v_stack_m360 = v_stack_m336;
    v_stack_m368 = v_stack_m334;
    v_stack_m370 = v_rip - 9780729;
    v_stack_m378 = 0;
    result = PnpGetObjectProperty(*(uint64_t *)(v_rip + 0x4F05B4), *(uint64_t *)(arg1 + 0x40), (uint32_t)((uint32_t)(6 + 2)), *(uint64_t *)(arg1 + 0x10));
    if (sign_flag) goto loc_00975E39;
    if (v_stack_m334 != 17) goto loc_00975E39;
    if (v_stack_m330 != 1) goto loc_00975E39;
    if (v_stack_m336 == 0) {
    }
    result = PiDevCfgQueryIncludedDriverConfigurations(Arg1, *(uint64_t *)(arg1 + 0x40), (uint32_t)((uint32_t)(6 + 2)), *(uint64_t *)(arg1 + 0x10));
    if (!(sign_flag)) {
    }
    if (v_stack_m320 != 0) {
        result = ExFreePool(v_stack_m320, *(uint64_t *)(arg1 + 0x40), (uint32_t)((uint32_t)(6 + 2)), *(uint64_t *)(arg1 + 0x10));
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0x298 + 0x260)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, *(uint64_t *)(arg1 + 0x40), (uint32_t)((uint32_t)(6 + 2)), *(uint64_t *)(arg1 + 0x10));
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `R` |
| `Arg1` | `+ 0x0` | `128` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x68` | `32` | `R` |
| `Arg1` | `+ 0xB8` | `32` | `R` |
| `Arg1` | `+ 0xB8` | `32` | `R/W` |
| `Arg1` | `+ 0xF0` | `64` | `R` |
| `Arg1` | `+ 0x100` | `64` | `R` |
| `Arg1` | `+ 0x110` | `64` | `R` |
| `Arg1` | `+ 0x120` | `64` | `R` |
| `Arg1` | `+ 0x128` | `64` | `R` |
| `Arg1` | `+ 0x130` | `64` | `R` |
| `Arg1` | `+ 0x138` | `64` | `R` |
| `Arg1` | `+ 0x140` | `64` | `R` |
| `Arg1` | `+ 0x148` | `64` | `R` |
| `Arg1` | `+ 0x150` | `64` | `R` |
| `Arg1` | `+ 0x158` | `64` | `R` |
| `Arg1` | `+ 0x160` | `64` | `R` |
| `Arg1` | `+ 0x168` | `64` | `R` |
| `Arg1` | `+ 0x170` | `64` | `R` |
| `Arg1` | `+ 0x178` | `64` | `R` |
| `Arg1` | `+ 0x190` | `64` | `R` |
| `Arg1` | `+ 0x198` | `64` | `R` |
| `Arg1` | `+ 0x1A0` | `64` | `R` |
| `Arg1` | `+ 0x1A4` | `64` | `R` |
| `Arg1` | `+ 0x1A8` | `64` | `R` |
| `Arg1` | `+ 0x1B8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0097584C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
