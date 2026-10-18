# McTemplateK0jxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx_EtwWriteTransfer

- RVA: `0x00423CE4`–`0x004241B0` (길이 `1,228` bytes)
- VA: `0x0000000140423CE4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A037C`
- 디코드: `169`개 명령, `1,228/1,228` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00424192` → [McGenEventWrite_EtwWriteTransfer](McGenEventWrite_EtwWriteTransfer_function_00424FC8.md) (function, `0x00424FC8`)
- `0x004241A1` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [CcPostVolumeTelemetry](CcPostVolumeTelemetry_function_00420FF8.md) at `0x004224B0`

### Static image references
- `0x00423CF5` → RVA `0x00E0A740` (`.data`; read)
- `0x00423F40` → RVA `0x00013F60` (`.rdata`; read)
- `0x00423F60` → RVA `0x00E06BD0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00423CE4  40 55                           push rbp
00423CE6  48 8D AC 24 90 FD FF FF         lea rbp, [rsp - 0x270]
00423CEE  48 81 EC 70 03 00 00            sub rsp, 0x370
00423CF5  48 8B 05 44 6A 9E 00            mov rax, qword ptr [rip + 0x9e6a44]
00423CFC  48 33 C4                        xor rax, rsp
00423CFF  48 89 85 60 02 00 00            mov qword ptr [rbp + 0x260], rax
00423D06  48 8D 85 A0 02 00 00            lea rax, [rbp + 0x2a0]
00423D0D  4C 89 4C 24 40                  mov qword ptr [rsp + 0x40], r9
00423D12  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00423D17  48 8D 85 A8 02 00 00            lea rax, [rbp + 0x2a8]
00423D1E  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00423D23  48 8D 85 B0 02 00 00            lea rax, [rbp + 0x2b0]
00423D2A  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00423D2F  48 8D 85 B8 02 00 00            lea rax, [rbp + 0x2b8]
00423D36  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00423D3A  48 8D 85 C0 02 00 00            lea rax, [rbp + 0x2c0]
00423D41  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
00423D45  48 8D 85 C8 02 00 00            lea rax, [rbp + 0x2c8]
00423D4C  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
00423D50  48 8D 85 D0 02 00 00            lea rax, [rbp + 0x2d0]
00423D57  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
00423D5B  48 8D 85 D8 02 00 00            lea rax, [rbp + 0x2d8]
00423D62  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00423D66  48 8D 85 E0 02 00 00            lea rax, [rbp + 0x2e0]
00423D6D  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00423D71  48 8D 85 E8 02 00 00            lea rax, [rbp + 0x2e8]
00423D78  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00423D7C  48 8D 85 F0 02 00 00            lea rax, [rbp + 0x2f0]
00423D83  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00423D87  48 8D 85 F8 02 00 00            lea rax, [rbp + 0x2f8]
00423D8E  48 89 45 00                     mov qword ptr [rbp], rax
00423D92  48 8D 85 00 03 00 00            lea rax, [rbp + 0x300]
00423D99  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
00423D9D  48 8D 85 08 03 00 00            lea rax, [rbp + 0x308]
00423DA4  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
00423DA8  48 8D 85 10 03 00 00            lea rax, [rbp + 0x310]
00423DAF  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
00423DB3  48 8D 85 18 03 00 00            lea rax, [rbp + 0x318]
00423DBA  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
00423DBE  48 8D 85 20 03 00 00            lea rax, [rbp + 0x320]
00423DC5  48 89 45 50                     mov qword ptr [rbp + 0x50], rax
00423DC9  48 8D 85 28 03 00 00            lea rax, [rbp + 0x328]
00423DD0  48 89 45 60                     mov qword ptr [rbp + 0x60], rax
00423DD4  48 8D 85 30 03 00 00            lea rax, [rbp + 0x330]
00423DDB  48 89 45 70                     mov qword ptr [rbp + 0x70], rax
00423DDF  48 8D 85 38 03 00 00            lea rax, [rbp + 0x338]
00423DE6  48 89 85 80 00 00 00            mov qword ptr [rbp + 0x80], rax
00423DED  48 8D 85 40 03 00 00            lea rax, [rbp + 0x340]
00423DF4  48 89 85 90 00 00 00            mov qword ptr [rbp + 0x90], rax
00423DFB  48 8D 85 48 03 00 00            lea rax, [rbp + 0x348]
00423E02  48 89 85 A0 00 00 00            mov qword ptr [rbp + 0xa0], rax
00423E09  48 8D 85 50 03 00 00            lea rax, [rbp + 0x350]
00423E10  48 89 85 B0 00 00 00            mov qword ptr [rbp + 0xb0], rax
00423E17  48 8D 85 58 03 00 00            lea rax, [rbp + 0x358]
00423E1E  48 89 85 C0 00 00 00            mov qword ptr [rbp + 0xc0], rax
00423E25  48 8D 85 60 03 00 00            lea rax, [rbp + 0x360]
00423E2C  48 89 85 D0 00 00 00            mov qword ptr [rbp + 0xd0], rax
00423E33  48 8D 85 68 03 00 00            lea rax, [rbp + 0x368]
00423E3A  48 89 85 E0 00 00 00            mov qword ptr [rbp + 0xe0], rax
00423E41  48 8D 85 70 03 00 00            lea rax, [rbp + 0x370]
00423E48  48 C7 44 24 48 10 00 00 00      mov qword ptr [rsp + 0x48], 0x10
00423E51  48 C7 44 24 58 08 00 00 00      mov qword ptr [rsp + 0x58], 8
00423E5A  48 C7 44 24 68 08 00 00 00      mov qword ptr [rsp + 0x68], 8
00423E63  48 C7 44 24 78 08 00 00 00      mov qword ptr [rsp + 0x78], 8
00423E6C  48 C7 45 88 08 00 00 00         mov qword ptr [rbp - 0x78], 8
00423E74  48 C7 45 98 08 00 00 00         mov qword ptr [rbp - 0x68], 8
00423E7C  48 C7 45 A8 08 00 00 00         mov qword ptr [rbp - 0x58], 8
00423E84  48 C7 45 B8 08 00 00 00         mov qword ptr [rbp - 0x48], 8
00423E8C  48 C7 45 C8 08 00 00 00         mov qword ptr [rbp - 0x38], 8
00423E94  48 C7 45 D8 08 00 00 00         mov qword ptr [rbp - 0x28], 8
00423E9C  48 C7 45 E8 08 00 00 00         mov qword ptr [rbp - 0x18], 8
00423EA4  48 C7 45 F8 08 00 00 00         mov qword ptr [rbp - 8], 8
00423EAC  48 C7 45 08 08 00 00 00         mov qword ptr [rbp + 8], 8
00423EB4  48 C7 45 18 08 00 00 00         mov qword ptr [rbp + 0x18], 8
00423EBC  48 C7 45 28 08 00 00 00         mov qword ptr [rbp + 0x28], 8
00423EC4  48 C7 45 38 08 00 00 00         mov qword ptr [rbp + 0x38], 8
00423ECC  48 C7 45 48 08 00 00 00         mov qword ptr [rbp + 0x48], 8
00423ED4  48 C7 45 58 08 00 00 00         mov qword ptr [rbp + 0x58], 8
00423EDC  48 C7 45 68 08 00 00 00         mov qword ptr [rbp + 0x68], 8
00423EE4  48 C7 45 78 08 00 00 00         mov qword ptr [rbp + 0x78], 8
00423EEC  48 C7 85 88 00 00 00 08 00 00 00  mov qword ptr [rbp + 0x88], 8
00423EF7  48 C7 85 98 00 00 00 08 00 00 00  mov qword ptr [rbp + 0x98], 8
00423F02  48 C7 85 A8 00 00 00 08 00 00 00  mov qword ptr [rbp + 0xa8], 8
00423F0D  48 C7 85 B8 00 00 00 08 00 00 00  mov qword ptr [rbp + 0xb8], 8
00423F18  48 C7 85 C8 00 00 00 08 00 00 00  mov qword ptr [rbp + 0xc8], 8
00423F23  48 C7 85 D8 00 00 00 08 00 00 00  mov qword ptr [rbp + 0xd8], 8
00423F2E  48 C7 85 E8 00 00 00 08 00 00 00  mov qword ptr [rbp + 0xe8], 8
00423F39  48 89 85 F0 00 00 00            mov qword ptr [rbp + 0xf0], rax
00423F40  48 8D 15 19 00 BF FF            lea rdx, [rip - 0x40ffe7]
00423F47  48 8D 85 78 03 00 00            lea rax, [rbp + 0x378]
00423F4E  48 C7 85 F8 00 00 00 08 00 00 00  mov qword ptr [rbp + 0xf8], 8
00423F59  48 89 85 00 01 00 00            mov qword ptr [rbp + 0x100], rax
00423F60  48 8D 0D 69 2C 9E 00            lea rcx, [rip + 0x9e2c69]
00423F67  48 8D 85 80 03 00 00            lea rax, [rbp + 0x380]
00423F6E  48 C7 85 08 01 00 00 08 00 00 00  mov qword ptr [rbp + 0x108], 8
00423F79  48 89 85 10 01 00 00            mov qword ptr [rbp + 0x110], rax
00423F80  41 B9 33 00 00 00               mov r9d, 0x33
00423F86  48 8D 85 88 03 00 00            lea rax, [rbp + 0x388]
00423F8D  48 C7 85 18 01 00 00 08 00 00 00  mov qword ptr [rbp + 0x118], 8
00423F98  48 89 85 20 01 00 00            mov qword ptr [rbp + 0x120], rax
00423F9F  45 33 C0                        xor r8d, r8d
00423FA2  48 8D 85 90 03 00 00            lea rax, [rbp + 0x390]
00423FA9  48 C7 85 28 01 00 00 08 00 00 00  mov qword ptr [rbp + 0x128], 8
00423FB4  48 89 85 30 01 00 00            mov qword ptr [rbp + 0x130], rax
00423FBB  48 8D 85 98 03 00 00            lea rax, [rbp + 0x398]
00423FC2  48 89 85 40 01 00 00            mov qword ptr [rbp + 0x140], rax
00423FC9  48 8D 85 A0 03 00 00            lea rax, [rbp + 0x3a0]
00423FD0  48 89 85 50 01 00 00            mov qword ptr [rbp + 0x150], rax
00423FD7  48 8D 85 A8 03 00 00            lea rax, [rbp + 0x3a8]
00423FDE  48 89 85 60 01 00 00            mov qword ptr [rbp + 0x160], rax
00423FE5  48 8D 85 B0 03 00 00            lea rax, [rbp + 0x3b0]
00423FEC  48 89 85 70 01 00 00            mov qword ptr [rbp + 0x170], rax
00423FF3  48 8D 85 B8 03 00 00            lea rax, [rbp + 0x3b8]
00423FFA  48 89 85 80 01 00 00            mov qword ptr [rbp + 0x180], rax
00424001  48 8D 85 C0 03 00 00            lea rax, [rbp + 0x3c0]
00424008  48 89 85 90 01 00 00            mov qword ptr [rbp + 0x190], rax
0042400F  48 8D 85 C8 03 00 00            lea rax, [rbp + 0x3c8]
00424016  48 89 85 A0 01 00 00            mov qword ptr [rbp + 0x1a0], rax
0042401D  48 8D 85 D0 03 00 00            lea rax, [rbp + 0x3d0]
00424024  48 89 85 B0 01 00 00            mov qword ptr [rbp + 0x1b0], rax
0042402B  48 8D 85 D8 03 00 00            lea rax, [rbp + 0x3d8]
00424032  48 89 85 C0 01 00 00            mov qword ptr [rbp + 0x1c0], rax
00424039  48 8D 85 E0 03 00 00            lea rax, [rbp + 0x3e0]
00424040  48 89 85 D0 01 00 00            mov qword ptr [rbp + 0x1d0], rax
00424047  48 8D 85 E8 03 00 00            lea rax, [rbp + 0x3e8]
0042404E  48 89 85 E0 01 00 00            mov qword ptr [rbp + 0x1e0], rax
00424055  48 8D 85 F0 03 00 00            lea rax, [rbp + 0x3f0]
0042405C  48 89 85 F0 01 00 00            mov qword ptr [rbp + 0x1f0], rax
00424063  48 8D 85 F8 03 00 00            lea rax, [rbp + 0x3f8]
0042406A  48 89 85 00 02 00 00            mov qword ptr [rbp + 0x200], rax
00424071  48 8D 85 00 04 00 00            lea rax, [rbp + 0x400]
00424078  48 89 85 10 02 00 00            mov qword ptr [rbp + 0x210], rax
0042407F  48 8D 85 08 04 00 00            lea rax, [rbp + 0x408]
00424086  48 89 85 20 02 00 00            mov qword ptr [rbp + 0x220], rax
0042408D  48 8D 85 10 04 00 00            lea rax, [rbp + 0x410]
00424094  48 89 85 30 02 00 00            mov qword ptr [rbp + 0x230], rax
0042409B  48 8D 85 18 04 00 00            lea rax, [rbp + 0x418]
004240A2  48 89 85 40 02 00 00            mov qword ptr [rbp + 0x240], rax
004240A9  48 8D 85 20 04 00 00            lea rax, [rbp + 0x420]
004240B0  48 89 85 50 02 00 00            mov qword ptr [rbp + 0x250], rax
004240B7  48 8D 44 24 30                  lea rax, [rsp + 0x30]
004240BC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
004240C1  48 C7 85 38 01 00 00 08 00 00 00  mov qword ptr [rbp + 0x138], 8
004240CC  48 C7 85 48 01 00 00 08 00 00 00  mov qword ptr [rbp + 0x148], 8
004240D7  48 C7 85 58 01 00 00 08 00 00 00  mov qword ptr [rbp + 0x158], 8
004240E2  48 C7 85 68 01 00 00 08 00 00 00  mov qword ptr [rbp + 0x168], 8
004240ED  48 C7 85 78 01 00 00 08 00 00 00  mov qword ptr [rbp + 0x178], 8
004240F8  48 C7 85 88 01 00 00 08 00 00 00  mov qword ptr [rbp + 0x188], 8
00424103  48 C7 85 98 01 00 00 08 00 00 00  mov qword ptr [rbp + 0x198], 8
0042410E  48 C7 85 A8 01 00 00 08 00 00 00  mov qword ptr [rbp + 0x1a8], 8
00424119  48 C7 85 B8 01 00 00 08 00 00 00  mov qword ptr [rbp + 0x1b8], 8
00424124  48 C7 85 C8 01 00 00 08 00 00 00  mov qword ptr [rbp + 0x1c8], 8
0042412F  48 C7 85 D8 01 00 00 08 00 00 00  mov qword ptr [rbp + 0x1d8], 8
0042413A  48 C7 85 E8 01 00 00 08 00 00 00  mov qword ptr [rbp + 0x1e8], 8
00424145  48 C7 85 F8 01 00 00 08 00 00 00  mov qword ptr [rbp + 0x1f8], 8
00424150  48 C7 85 08 02 00 00 08 00 00 00  mov qword ptr [rbp + 0x208], 8
0042415B  48 C7 85 18 02 00 00 08 00 00 00  mov qword ptr [rbp + 0x218], 8
00424166  48 C7 85 28 02 00 00 08 00 00 00  mov qword ptr [rbp + 0x228], 8
00424171  48 C7 85 38 02 00 00 08 00 00 00  mov qword ptr [rbp + 0x238], 8
0042417C  48 C7 85 48 02 00 00 08 00 00 00  mov qword ptr [rbp + 0x248], 8
00424187  48 C7 85 58 02 00 00 08 00 00 00  mov qword ptr [rbp + 0x258], 8
00424192  E8 31 0E 00 00                  call 0x140424fc8
00424197  48 8B 8D 60 02 00 00            mov rcx, qword ptr [rbp + 0x260]
0042419E  48 33 CC                        xor rcx, rsp
004241A1  E8 9A 84 28 00                  call 0x1406ac640
004241A6  48 81 C4 70 03 00 00            add rsp, 0x370
004241AD  5D                              pop rbp
004241AE  C3                              ret
004241AF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall McTemplateK0jxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx_EtwWriteTransfer(__int64 a1, __int64 a2, int a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17, __int64 a18, __int64 a19, __int64 a20, __int64 a21, __int64 a22, __int64 a23, __int64 a24, __int64 a25, __int64 a26, __int64 a27, __int64 a28, __int64 a29, __int64 a30, __int64 a31, __int64 a32, __int64 a33, __int64 a34, __int64 a35, __int64 a36, __int64 a37, __int64 a38, __int64 a39, __int64 a40, __int64 a41, __int64 a42, __int64 a43, __int64 a44, __int64 a45, __int64 a46, __int64 a47, __int64 a48, __int64 a49, __int64 a50, __int64 a51, __int64 a52, __int64 a53)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int64 v_stack_m1C8;
    unsigned __int64 v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m200;
    unsigned __int64 v_stack_m208;
    unsigned __int64 v_stack_m210;
    unsigned __int64 v_stack_m218;
    unsigned __int64 v_stack_m220;
    unsigned __int64 v_stack_m228;
    unsigned __int64 v_stack_m230;
    unsigned __int64 v_stack_m238;
    unsigned __int64 v_stack_m240;
    unsigned __int64 v_stack_m248;
    unsigned __int64 v_stack_m250;
    unsigned __int64 v_stack_m258;
    unsigned __int64 v_stack_m260;
    unsigned __int64 v_stack_m268;
    unsigned __int64 v_stack_m270;
    unsigned __int64 v_stack_m278;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m280;
    unsigned __int64 v_stack_m288;
    unsigned __int64 v_stack_m290;
    unsigned __int64 v_stack_m298;
    unsigned __int64 v_stack_m2A0;
    unsigned __int64 v_stack_m2A8;
    unsigned __int64 v_stack_m2B0;
    unsigned __int64 v_stack_m2B8;
    unsigned __int64 v_stack_m2C0;
    unsigned __int64 v_stack_m2C8;
    unsigned __int64 v_stack_m2D0;
    unsigned __int64 v_stack_m2D8;
    unsigned __int64 v_stack_m2E0;
    unsigned __int64 v_stack_m2E8;
    unsigned __int64 v_stack_m2F0;
    unsigned __int64 v_stack_m2F8;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m300;
    unsigned __int64 v_stack_m308;
    unsigned __int64 v_stack_m310;
    unsigned __int64 v_stack_m318;
    unsigned __int64 v_stack_m320;
    unsigned __int64 v_stack_m328;
    unsigned __int64 v_stack_m330;
    unsigned __int64 v_stack_m338;
    unsigned __int64 v_stack_m348;
    unsigned __int64 v_stack_m358;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
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
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;

    v_rsp = (v_rsp) - (880);
    result = (*(unsigned __int64 *)(v_rip + 10381892)) ^ (v_rsp);
    v_stack_m18 = result;
    v_stack_m338 = a4;
    v_stack_m328 = a5;
    v_stack_m318 = a6;
    v_stack_m308 = a7;
    v_stack_m2F8 = a8;
    v_stack_m2E8 = a9;
    v_stack_m2D8 = a10;
    v_stack_m2C8 = a11;
    v_stack_m2B8 = a12;
    v_stack_m2A8 = a13;
    v_stack_m298 = a14;
    v_stack_m288 = a15;
    v_stack_m278 = a16;
    v_stack_m268 = a17;
    v_stack_m258 = a18;
    v_stack_m248 = a19;
    v_stack_m238 = a20;
    v_stack_m228 = a21;
    v_stack_m218 = a22;
    v_stack_m208 = a23;
    v_stack_m1F8 = a24;
    v_stack_m1E8 = a25;
    v_stack_m1D8 = a26;
    v_stack_m1C8 = a27;
    v_stack_m1B8 = a28;
    v_stack_m1A8 = a29;
    v_stack_m198 = a30;
    v_stack_m330 = 16;
    v_stack_m320 = 8;
    v_stack_m310 = 8;
    v_stack_m300 = 8;
    v_stack_m2F0 = 8;
    v_stack_m2E0 = 8;
    v_stack_m2D0 = 8;
    v_stack_m2C0 = 8;
    v_stack_m2B0 = 8;
    v_stack_m2A0 = 8;
    v_stack_m290 = 8;
    v_stack_m280 = 8;
    v_stack_m270 = 8;
    v_stack_m260 = 8;
    v_stack_m250 = 8;
    v_stack_m240 = 8;
    v_stack_m230 = 8;
    v_stack_m220 = 8;
    v_stack_m210 = 8;
    v_stack_m200 = 8;
    v_stack_m1F0 = 8;
    v_stack_m1E0 = 8;
    v_stack_m1D0 = 8;
    v_stack_m1C0 = 8;
    v_stack_m1B0 = 8;
    v_stack_m1A0 = 8;
    v_stack_m190 = 8;
    v_stack_m188 = a31;
    v_stack_m180 = 8;
    v_stack_m178 = a32;
    v_stack_m170 = 8;
    v_stack_m168 = a33;
    v_stack_m160 = 8;
    v_stack_m158 = a34;
    a3 = 0;
    v_stack_m150 = 8;
    v_stack_m148 = a35;
    v_stack_m138 = a36;
    v_stack_m128 = a37;
    v_stack_m118 = a38;
    v_stack_m108 = a39;
    v_stack_mF8 = a40;
    v_stack_mE8 = a41;
    v_stack_mD8 = a42;
    v_stack_mC8 = a43;
    v_stack_mB8 = a44;
    v_stack_mA8 = a45;
    v_stack_m98 = a46;
    v_stack_m88 = a47;
    v_stack_m78 = a48;
    v_stack_m68 = a49;
    v_stack_m58 = a50;
    v_stack_m48 = a51;
    v_stack_m38 = a52;
    v_stack_m28 = a53;
    v_stack_m358 = v_stack_m348;
    v_stack_m140 = 8;
    v_stack_m130 = 8;
    v_stack_m120 = 8;
    v_stack_m110 = 8;
    v_stack_m100 = 8;
    v_stack_mF0 = 8;
    v_stack_mE0 = 8;
    v_stack_mD0 = 8;
    v_stack_mC0 = 8;
    v_stack_mB0 = 8;
    v_stack_mA0 = 8;
    v_stack_m90 = 8;
    v_stack_m80 = 8;
    v_stack_m70 = 8;
    v_stack_m60 = 8;
    v_stack_m50 = 8;
    v_stack_m40 = 8;
    v_stack_m30 = 8;
    v_stack_m20 = 8;
    result = McGenEventWrite_EtwWriteTransfer(v_rip + 10366057, v_rip - 4259815, a3, 51);
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, v_rip - 4259815, a3, 51);
    v_rsp = (v_rsp) + (880);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t McTemplateK0jxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx_EtwWriteTransfer(int64_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6, int64_t Arg7, int64_t Arg8, int64_t Arg9, int64_t Arg10, int64_t Arg11, int64_t Arg12, int64_t Arg13, int64_t Arg14, int64_t Arg15, int64_t Arg16, int64_t Arg17, int64_t Arg18, int64_t Arg19, int64_t Arg20, int64_t Arg21, int64_t Arg22, int64_t Arg23, int64_t Arg24, int64_t Arg25, int64_t Arg26, int64_t Arg27, int64_t Arg28, int64_t Arg29, int64_t Arg30, int64_t Arg31, int64_t Arg32, int64_t Arg33, int64_t Arg34, int64_t Arg35, int64_t Arg36, int64_t Arg37, int64_t Arg38, int64_t Arg39, int64_t Arg40, int64_t Arg41, int64_t Arg42, int64_t Arg43, int64_t Arg44, int64_t Arg45, int64_t Arg46, int64_t Arg47, int64_t Arg48, int64_t Arg49, int64_t Arg50, int64_t Arg51, int64_t Arg52, int64_t Arg53)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m18;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint64_t v_stack_m1C8;
    uint64_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m20;
    uint64_t v_stack_m200;
    uint64_t v_stack_m208;
    uint64_t v_stack_m210;
    uint64_t v_stack_m218;
    uint64_t v_stack_m220;
    uint64_t v_stack_m228;
    uint64_t v_stack_m230;
    uint64_t v_stack_m238;
    uint64_t v_stack_m240;
    uint64_t v_stack_m248;
    uint64_t v_stack_m250;
    uint64_t v_stack_m258;
    uint64_t v_stack_m260;
    uint64_t v_stack_m268;
    uint64_t v_stack_m270;
    uint64_t v_stack_m278;
    uint64_t v_stack_m28;
    uint64_t v_stack_m280;
    uint64_t v_stack_m288;
    uint64_t v_stack_m290;
    uint64_t v_stack_m298;
    uint64_t v_stack_m2A0;
    uint64_t v_stack_m2A8;
    uint64_t v_stack_m2B0;
    uint64_t v_stack_m2B8;
    uint64_t v_stack_m2C0;
    uint64_t v_stack_m2C8;
    uint64_t v_stack_m2D0;
    uint64_t v_stack_m2D8;
    uint64_t v_stack_m2E0;
    uint64_t v_stack_m2E8;
    uint64_t v_stack_m2F0;
    uint64_t v_stack_m2F8;
    uint64_t v_stack_m30;
    uint64_t v_stack_m300;
    uint64_t v_stack_m308;
    uint64_t v_stack_m310;
    uint64_t v_stack_m318;
    uint64_t v_stack_m320;
    uint64_t v_stack_m328;
    uint64_t v_stack_m330;
    uint64_t v_stack_m338;
    uint64_t v_stack_m348;
    uint64_t v_stack_m358;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
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
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;

    local_rsp = (local_rsp) - (880);
    result = (*(uint64_t *)(v_rip + 0x9E6A44)) ^ (local_rsp);
    v_stack_m18 = result;
    v_stack_m338 = Arg4;
    v_stack_m328 = Arg5;
    v_stack_m318 = Arg6;
    v_stack_m308 = Arg7;
    v_stack_m2F8 = Arg8;
    v_stack_m2E8 = Arg9;
    v_stack_m2D8 = Arg10;
    v_stack_m2C8 = Arg11;
    v_stack_m2B8 = Arg12;
    v_stack_m2A8 = Arg13;
    v_stack_m298 = Arg14;
    v_stack_m288 = Arg15;
    v_stack_m278 = Arg16;
    v_stack_m268 = Arg17;
    v_stack_m258 = Arg18;
    v_stack_m248 = Arg19;
    v_stack_m238 = Arg20;
    v_stack_m228 = Arg21;
    v_stack_m218 = Arg22;
    v_stack_m208 = Arg23;
    v_stack_m1F8 = Arg24;
    v_stack_m1E8 = Arg25;
    v_stack_m1D8 = Arg26;
    v_stack_m1C8 = Arg27;
    v_stack_m1B8 = Arg28;
    v_stack_m1A8 = Arg29;
    v_stack_m198 = Arg30;
    v_stack_m330 = 16;
    v_stack_m320 = 8;
    v_stack_m310 = 8;
    v_stack_m300 = 8;
    v_stack_m2F0 = 8;
    v_stack_m2E0 = 8;
    v_stack_m2D0 = 8;
    v_stack_m2C0 = 8;
    v_stack_m2B0 = 8;
    v_stack_m2A0 = 8;
    v_stack_m290 = 8;
    v_stack_m280 = 8;
    v_stack_m270 = 8;
    v_stack_m260 = 8;
    v_stack_m250 = 8;
    v_stack_m240 = 8;
    v_stack_m230 = 8;
    v_stack_m220 = 8;
    v_stack_m210 = 8;
    v_stack_m200 = 8;
    v_stack_m1F0 = 8;
    v_stack_m1E0 = 8;
    v_stack_m1D0 = 8;
    v_stack_m1C0 = 8;
    v_stack_m1B0 = 8;
    v_stack_m1A0 = 8;
    v_stack_m190 = 8;
    v_stack_m188 = Arg31;
    v_stack_m180 = 8;
    v_stack_m178 = Arg32;
    v_stack_m170 = 8;
    v_stack_m168 = Arg33;
    v_stack_m160 = 8;
    v_stack_m158 = Arg34;
    Arg3 = 0;
    v_stack_m150 = 8;
    v_stack_m148 = Arg35;
    v_stack_m138 = Arg36;
    v_stack_m128 = Arg37;
    v_stack_m118 = Arg38;
    v_stack_m108 = Arg39;
    v_stack_mF8 = Arg40;
    v_stack_mE8 = Arg41;
    v_stack_mD8 = Arg42;
    v_stack_mC8 = Arg43;
    v_stack_mB8 = Arg44;
    v_stack_mA8 = Arg45;
    v_stack_m98 = Arg46;
    v_stack_m88 = Arg47;
    v_stack_m78 = Arg48;
    v_stack_m68 = Arg49;
    v_stack_m58 = Arg50;
    v_stack_m48 = Arg51;
    v_stack_m38 = Arg52;
    v_stack_m28 = Arg53;
    v_stack_m358 = v_stack_m348;
    v_stack_m140 = 8;
    v_stack_m130 = 8;
    v_stack_m120 = 8;
    v_stack_m110 = 8;
    v_stack_m100 = 8;
    v_stack_mF0 = 8;
    v_stack_mE0 = 8;
    v_stack_mD0 = 8;
    v_stack_mC0 = 8;
    v_stack_mB0 = 8;
    v_stack_mA0 = 8;
    v_stack_m90 = 8;
    v_stack_m80 = 8;
    v_stack_m70 = 8;
    v_stack_m60 = 8;
    v_stack_m50 = 8;
    v_stack_m40 = 8;
    v_stack_m30 = 8;
    v_stack_m20 = 8;
    result = McGenEventWrite_EtwWriteTransfer(v_rip + 10366057, v_rip - 4259815, Arg3, 51);
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_rip - 4259815, Arg3, 51);
    local_rsp = (local_rsp) + (880);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00423CE4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00423CE4[BB_00423CE4]
  bb_004241AF[BB_004241AF]
```
