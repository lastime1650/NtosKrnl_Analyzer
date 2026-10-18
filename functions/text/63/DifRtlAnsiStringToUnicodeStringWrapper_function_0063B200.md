# DifRtlAnsiStringToUnicodeStringWrapper

- RVA: `0x0063B200`–`0x0063B377` (길이 `375` bytes)
- VA: `0x000000014063B200`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A9A64`
- 디코드: `108`개 명령, `375/375` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0063B23E` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0063B264` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0063B298` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063B2BE` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063B2D7` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0063B2E5` → [RtlAnsiStringToUnicodeString](../../page/90/RtlAnsiStringToUnicodeString_function_0090BEA0.md) (function, `0x0090BEA0`)
- `0x0063B311` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063B337` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063B350` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0063B274` → RVA `0x00F048B8` (`.data`; read)
- `0x0063B285` → RVA `0x00F04980` (`.data`; read)
- `0x0063B291` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0063B2E5` → [RtlAnsiStringToUnicodeString](../../page/90/RtlAnsiStringToUnicodeString_function_0090BEA0.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0063B200  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0063B205  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0063B20A  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
0063B20F  55                              push rbp
0063B210  41 54                           push r12
0063B212  41 55                           push r13
0063B214  41 56                           push r14
0063B216  41 57                           push r15
0063B218  48 8B EC                        mov rbp, rsp
0063B21B  48 83 EC 50                     sub rsp, 0x50
0063B21F  0F 57 C0                        xorps xmm0, xmm0
0063B222  33 C0                           xor eax, eax
0063B224  4C 8B E9                        mov r13, rcx
0063B227  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0063B22B  B9 A9 00 00 00                  mov ecx, 0xa9
0063B230  45 8A F8                        mov r15b, r8b
0063B233  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0063B237  4C 8B E2                        mov r12, rdx
0063B23A  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0063B23E  E8 F1 A7 E5 FF                  call 0x140495a34
0063B243  48 8B F0                        mov rsi, rax
0063B246  48 85 C0                        test rax, rax
0063B249  0F 84 8D 00 00 00               je 0x14063b2dc
0063B24F  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0063B252  A8 18                           test al, 0x18
0063B254  74 0A                           je 0x14063b260
0063B256  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0063B25A  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
0063B25E  EB 0D                           jmp 0x14063b26d
0063B260  A8 04                           test al, 4
0063B262  74 09                           je 0x14063b26d
0063B264  E8 9F 89 E9 FF                  call 0x1404d3c08
0063B269  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0063B26D  45 32 F6                        xor r14b, r14b
0063B270  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
0063B274  44 38 35 3D 96 8C 00            cmp byte ptr [rip + 0x8c963d], r14b
0063B27B  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
0063B27F  44 88 7D D8                     mov byte ptr [rbp - 0x28], r15b
0063B283  75 0C                           jne 0x14063b291
0063B285  F7 05 F1 96 8C 00 00 08 00 00   test dword ptr [rip + 0x8c96f1], 0x800
0063B28F  74 13                           je 0x14063b2a4
0063B291  48 8D 0D E8 8B 8C 00            lea rcx, [rip + 0x8c8be8]
0063B298  E8 83 B3 BD FF                  call 0x140216620
0063B29D  44 8A F0                        mov r14b, al
0063B2A0  84 C0                           test al, al
0063B2A2  74 38                           je 0x14063b2dc
0063B2A4  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0063B2A8  48 8B 1F                        mov rbx, qword ptr [rdi]
0063B2AB  EB 19                           jmp 0x14063b2c6
0063B2AD  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063B2B1  48 85 C0                        test rax, rax
0063B2B4  74 0D                           je 0x14063b2c3
0063B2B6  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063B2BA  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0063B2BE  E8 0D F8 07 00                  call 0x1406baad0
0063B2C3  48 8B 1B                        mov rbx, qword ptr [rbx]
0063B2C6  48 3B DF                        cmp rbx, rdi
0063B2C9  75 E2                           jne 0x14063b2ad
0063B2CB  45 84 F6                        test r14b, r14b
0063B2CE  74 0C                           je 0x14063b2dc
0063B2D0  48 8D 0D A9 8B 8C 00            lea rcx, [rip + 0x8c8ba9]
0063B2D7  E8 A4 EB D0 FF                  call 0x140349e80
0063B2DC  45 8A C7                        mov r8b, r15b
0063B2DF  49 8B D4                        mov rdx, r12
0063B2E2  49 8B CD                        mov rcx, r13
0063B2E5  E8 B6 0B 2D 00                  call 0x14090bea0
0063B2EA  89 45 F0                        mov dword ptr [rbp - 0x10], eax
0063B2ED  48 85 F6                        test rsi, rsi
0063B2F0  74 63                           je 0x14063b355
0063B2F2  40 32 FF                        xor dil, dil
0063B2F5  40 38 3D BC 95 8C 00            cmp byte ptr [rip + 0x8c95bc], dil
0063B2FC  75 0C                           jne 0x14063b30a
0063B2FE  F7 05 78 96 8C 00 00 08 00 00   test dword ptr [rip + 0x8c9678], 0x800
0063B308  74 13                           je 0x14063b31d
0063B30A  48 8D 0D 6F 8B 8C 00            lea rcx, [rip + 0x8c8b6f]
0063B311  E8 0A B3 BD FF                  call 0x140216620
0063B316  40 8A F8                        mov dil, al
0063B319  84 C0                           test al, al
0063B31B  74 38                           je 0x14063b355
0063B31D  48 83 C6 30                     add rsi, 0x30
0063B321  48 8B 1E                        mov rbx, qword ptr [rsi]
0063B324  EB 19                           jmp 0x14063b33f
0063B326  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063B32A  48 85 C0                        test rax, rax
0063B32D  74 0D                           je 0x14063b33c
0063B32F  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063B333  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0063B337  E8 94 F7 07 00                  call 0x1406baad0
0063B33C  48 8B 1B                        mov rbx, qword ptr [rbx]
0063B33F  48 3B DE                        cmp rbx, rsi
0063B342  75 E2                           jne 0x14063b326
0063B344  40 84 FF                        test dil, dil
0063B347  74 0C                           je 0x14063b355
0063B349  48 8D 0D 30 8B 8C 00            lea rcx, [rip + 0x8c8b30]
0063B350  E8 2B EB D0 FF                  call 0x140349e80
0063B355  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
0063B358  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0063B35D  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
0063B361  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
0063B365  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
0063B369  49 8B E3                        mov rsp, r11
0063B36C  41 5F                           pop r15
0063B36E  41 5E                           pop r14
0063B370  41 5D                           pop r13
0063B372  41 5C                           pop r12
0063B374  5D                              pop rbp
0063B375  C3                              ret
0063B376  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifRtlAnsiStringToUnicodeStringWrapper(__int64 a1, __int64 a2, unsigned __int8 a3)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int8 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p18 = v_rdi;
    v_rsp = (v_rsp) - (80);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(169, a2, a3, a4);
    if (result == 0) goto loc_0063B2DC;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0063B260;
    v_stack_m58 = v_stack_p0;
    goto loc_0063B26D;
loc_0063B260:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m40 = a1;
    v_stack_m48 = a2;
    v_stack_m50 = a3;
    if ((*(unsigned __int8 *)(v_rip + 9213501)) != 0) goto loc_0063B291;
    if (((*(unsigned int *)(v_rip + 9213681)) & (0x800ULL)) == 0) goto loc_0063B2A4;
loc_0063B291:
    result = ExAcquireRundownProtection(v_rip + 9210856, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063B2DC;
loc_0063B2A4:
    goto loc_0063B2C6;
loc_0063B2AD:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063B2C6:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0063B2AD;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9210793;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = RtlAnsiStringToUnicodeString(a1, a2, a3, a4);
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_0063B355;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9213372)) != 0) goto loc_0063B30A;
    if (((*(unsigned int *)(v_rip + 9213560)) & (0x800ULL)) == 0) goto loc_0063B31D;
loc_0063B30A:
    result = ExAcquireRundownProtection(v_rip + 9210735, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063B355;
loc_0063B31D:
    v_rsi = (result) + (48);
    goto loc_0063B33F;
loc_0063B326:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063B33F:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0063B326;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9210672;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifRtlAnsiStringToUnicodeStringWrapper(int64_t Arg1, int64_t Arg2, uint8_t Arg3)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint8_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p18 = local_rdi;
    local_rsp = (local_rsp) - (80);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(169, Arg2, Arg3, a4);
    if (result == 0) goto loc_0063B2DC;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0063B260;
    v_stack_m58 = v_stack_p0;
    goto loc_0063B26D;
loc_0063B260:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m40 = Arg1;
    v_stack_m48 = Arg2;
    v_stack_m50 = Arg3;
    if ((*(uint8_t *)(v_rip + 0x8C963D)) != 0) goto loc_0063B291;
    if (((*(uint32_t *)(v_rip + 0x8C96F1)) & (0x800ULL)) == 0) goto loc_0063B2A4;
loc_0063B291:
    result = ExAcquireRundownProtection(v_rip + 9210856, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063B2DC;
loc_0063B2A4:
    goto loc_0063B2C6;
loc_0063B2AD:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0063B2C6:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0063B2AD;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9210793;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = RtlAnsiStringToUnicodeString(Arg1, Arg2, Arg3, a4);
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_0063B355;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C95BC)) != 0) goto loc_0063B30A;
    if (((*(uint32_t *)(v_rip + 0x8C9678)) & (0x800ULL)) == 0) goto loc_0063B31D;
loc_0063B30A:
    result = ExAcquireRundownProtection(v_rip + 9210735, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063B355;
loc_0063B31D:
    local_rsi = (result) + (48);
    goto loc_0063B33F;
loc_0063B326:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0063B33F:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0063B326;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9210672;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0063B200&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0063B200[BB_0063B200]
  bb_0063B24F[BB_0063B24F]
  bb_0063B256[BB_0063B256]
  bb_0063B260[BB_0063B260]
  bb_0063B264[BB_0063B264]
  bb_0063B26D[BB_0063B26D]
  bb_0063B285[BB_0063B285]
  bb_0063B291[BB_0063B291]
  bb_0063B2A4[BB_0063B2A4]
  bb_0063B2AD[BB_0063B2AD]
  bb_0063B2B6[BB_0063B2B6]
  bb_0063B2C3[BB_0063B2C3]
  bb_0063B2C6[BB_0063B2C6]
  bb_0063B2CB[BB_0063B2CB]
  bb_0063B2D0[BB_0063B2D0]
  bb_0063B2DC[BB_0063B2DC]
  bb_0063B2F2[BB_0063B2F2]
  bb_0063B2FE[BB_0063B2FE]
  bb_0063B30A[BB_0063B30A]
  bb_0063B31D[BB_0063B31D]
  bb_0063B326[BB_0063B326]
  bb_0063B32F[BB_0063B32F]
  bb_0063B33C[BB_0063B33C]
  bb_0063B33F[BB_0063B33F]
  bb_0063B344[BB_0063B344]
  bb_0063B349[BB_0063B349]
  bb_0063B355[BB_0063B355]
  bb_0063B376[BB_0063B376]
  bb_0063B200 -->|branch| bb_0063B2DC
  bb_0063B200 -->|fallthrough| bb_0063B24F
  bb_0063B24F -->|branch| bb_0063B260
  bb_0063B24F -->|fallthrough| bb_0063B256
  bb_0063B256 -->|branch| bb_0063B26D
  bb_0063B260 -->|branch| bb_0063B26D
  bb_0063B260 -->|fallthrough| bb_0063B264
  bb_0063B264 -->|flow| bb_0063B26D
  bb_0063B26D -->|branch| bb_0063B291
  bb_0063B26D -->|fallthrough| bb_0063B285
  bb_0063B285 -->|branch| bb_0063B2A4
  bb_0063B285 -->|fallthrough| bb_0063B291
  bb_0063B291 -->|branch| bb_0063B2DC
  bb_0063B291 -->|fallthrough| bb_0063B2A4
  bb_0063B2A4 -->|branch| bb_0063B2C6
  bb_0063B2AD -->|branch| bb_0063B2C3
  bb_0063B2AD -->|fallthrough| bb_0063B2B6
  bb_0063B2B6 -->|flow| bb_0063B2C3
  bb_0063B2C3 -->|flow| bb_0063B2C6
  bb_0063B2C6 -->|branch| bb_0063B2AD
  bb_0063B2C6 -->|fallthrough| bb_0063B2CB
  bb_0063B2CB -->|branch| bb_0063B2DC
  bb_0063B2CB -->|fallthrough| bb_0063B2D0
  bb_0063B2D0 -->|flow| bb_0063B2DC
  bb_0063B2DC -->|branch| bb_0063B355
  bb_0063B2DC -->|fallthrough| bb_0063B2F2
  bb_0063B2F2 -->|branch| bb_0063B30A
  bb_0063B2F2 -->|fallthrough| bb_0063B2FE
  bb_0063B2FE -->|branch| bb_0063B31D
  bb_0063B2FE -->|fallthrough| bb_0063B30A
  bb_0063B30A -->|branch| bb_0063B355
  bb_0063B30A -->|fallthrough| bb_0063B31D
  bb_0063B31D -->|branch| bb_0063B33F
  bb_0063B326 -->|branch| bb_0063B33C
  bb_0063B326 -->|fallthrough| bb_0063B32F
  bb_0063B32F -->|flow| bb_0063B33C
  bb_0063B33C -->|flow| bb_0063B33F
  bb_0063B33F -->|branch| bb_0063B326
  bb_0063B33F -->|fallthrough| bb_0063B344
  bb_0063B344 -->|branch| bb_0063B355
  bb_0063B344 -->|fallthrough| bb_0063B349
  bb_0063B349 -->|flow| bb_0063B355
```
