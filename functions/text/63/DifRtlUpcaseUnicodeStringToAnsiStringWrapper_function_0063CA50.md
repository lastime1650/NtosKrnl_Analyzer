# DifRtlUpcaseUnicodeStringToAnsiStringWrapper

- RVA: `0x0063CA50`–`0x0063CBC7` (길이 `375` bytes)
- VA: `0x000000014063CA50`
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
- `0x0063CA8E` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0063CAB4` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0063CAE8` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063CB0E` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063CB27` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0063CB35` → [RtlUpcaseUnicodeStringToAnsiString](../../page/78/RtlUpcaseUnicodeStringToAnsiString_function_0078A830.md) (function, `0x0078A830`)
- `0x0063CB61` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063CB87` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063CBA0` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0063CAC4` → RVA `0x00F048B8` (`.data`; read)
- `0x0063CAD5` → RVA `0x00F04980` (`.data`; read)
- `0x0063CAE1` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0063CB35` → [RtlUpcaseUnicodeStringToAnsiString](../../page/78/RtlUpcaseUnicodeStringToAnsiString_function_0078A830.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0063CA50  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0063CA55  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0063CA5A  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
0063CA5F  55                              push rbp
0063CA60  41 54                           push r12
0063CA62  41 55                           push r13
0063CA64  41 56                           push r14
0063CA66  41 57                           push r15
0063CA68  48 8B EC                        mov rbp, rsp
0063CA6B  48 83 EC 50                     sub rsp, 0x50
0063CA6F  0F 57 C0                        xorps xmm0, xmm0
0063CA72  33 C0                           xor eax, eax
0063CA74  4C 8B E9                        mov r13, rcx
0063CA77  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0063CA7B  B9 98 00 00 00                  mov ecx, 0x98
0063CA80  45 8A F8                        mov r15b, r8b
0063CA83  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0063CA87  4C 8B E2                        mov r12, rdx
0063CA8A  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0063CA8E  E8 A1 8F E5 FF                  call 0x140495a34
0063CA93  48 8B F0                        mov rsi, rax
0063CA96  48 85 C0                        test rax, rax
0063CA99  0F 84 8D 00 00 00               je 0x14063cb2c
0063CA9F  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0063CAA2  A8 18                           test al, 0x18
0063CAA4  74 0A                           je 0x14063cab0
0063CAA6  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0063CAAA  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
0063CAAE  EB 0D                           jmp 0x14063cabd
0063CAB0  A8 04                           test al, 4
0063CAB2  74 09                           je 0x14063cabd
0063CAB4  E8 4F 71 E9 FF                  call 0x1404d3c08
0063CAB9  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0063CABD  45 32 F6                        xor r14b, r14b
0063CAC0  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
0063CAC4  44 38 35 ED 7D 8C 00            cmp byte ptr [rip + 0x8c7ded], r14b
0063CACB  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
0063CACF  44 88 7D D8                     mov byte ptr [rbp - 0x28], r15b
0063CAD3  75 0C                           jne 0x14063cae1
0063CAD5  F7 05 A1 7E 8C 00 00 08 00 00   test dword ptr [rip + 0x8c7ea1], 0x800
0063CADF  74 13                           je 0x14063caf4
0063CAE1  48 8D 0D 98 73 8C 00            lea rcx, [rip + 0x8c7398]
0063CAE8  E8 33 9B BD FF                  call 0x140216620
0063CAED  44 8A F0                        mov r14b, al
0063CAF0  84 C0                           test al, al
0063CAF2  74 38                           je 0x14063cb2c
0063CAF4  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0063CAF8  48 8B 1F                        mov rbx, qword ptr [rdi]
0063CAFB  EB 19                           jmp 0x14063cb16
0063CAFD  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063CB01  48 85 C0                        test rax, rax
0063CB04  74 0D                           je 0x14063cb13
0063CB06  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063CB0A  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0063CB0E  E8 BD DF 07 00                  call 0x1406baad0
0063CB13  48 8B 1B                        mov rbx, qword ptr [rbx]
0063CB16  48 3B DF                        cmp rbx, rdi
0063CB19  75 E2                           jne 0x14063cafd
0063CB1B  45 84 F6                        test r14b, r14b
0063CB1E  74 0C                           je 0x14063cb2c
0063CB20  48 8D 0D 59 73 8C 00            lea rcx, [rip + 0x8c7359]
0063CB27  E8 54 D3 D0 FF                  call 0x140349e80
0063CB2C  45 8A C7                        mov r8b, r15b
0063CB2F  49 8B D4                        mov rdx, r12
0063CB32  49 8B CD                        mov rcx, r13
0063CB35  E8 F6 DC 14 00                  call 0x14078a830
0063CB3A  89 45 F0                        mov dword ptr [rbp - 0x10], eax
0063CB3D  48 85 F6                        test rsi, rsi
0063CB40  74 63                           je 0x14063cba5
0063CB42  40 32 FF                        xor dil, dil
0063CB45  40 38 3D 6C 7D 8C 00            cmp byte ptr [rip + 0x8c7d6c], dil
0063CB4C  75 0C                           jne 0x14063cb5a
0063CB4E  F7 05 28 7E 8C 00 00 08 00 00   test dword ptr [rip + 0x8c7e28], 0x800
0063CB58  74 13                           je 0x14063cb6d
0063CB5A  48 8D 0D 1F 73 8C 00            lea rcx, [rip + 0x8c731f]
0063CB61  E8 BA 9A BD FF                  call 0x140216620
0063CB66  40 8A F8                        mov dil, al
0063CB69  84 C0                           test al, al
0063CB6B  74 38                           je 0x14063cba5
0063CB6D  48 83 C6 30                     add rsi, 0x30
0063CB71  48 8B 1E                        mov rbx, qword ptr [rsi]
0063CB74  EB 19                           jmp 0x14063cb8f
0063CB76  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063CB7A  48 85 C0                        test rax, rax
0063CB7D  74 0D                           je 0x14063cb8c
0063CB7F  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063CB83  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0063CB87  E8 44 DF 07 00                  call 0x1406baad0
0063CB8C  48 8B 1B                        mov rbx, qword ptr [rbx]
0063CB8F  48 3B DE                        cmp rbx, rsi
0063CB92  75 E2                           jne 0x14063cb76
0063CB94  40 84 FF                        test dil, dil
0063CB97  74 0C                           je 0x14063cba5
0063CB99  48 8D 0D E0 72 8C 00            lea rcx, [rip + 0x8c72e0]
0063CBA0  E8 DB D2 D0 FF                  call 0x140349e80
0063CBA5  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
0063CBA8  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0063CBAD  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
0063CBB1  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
0063CBB5  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
0063CBB9  49 8B E3                        mov rsp, r11
0063CBBC  41 5F                           pop r15
0063CBBE  41 5E                           pop r14
0063CBC0  41 5D                           pop r13
0063CBC2  41 5C                           pop r12
0063CBC4  5D                              pop rbp
0063CBC5  C3                              ret
0063CBC6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifRtlUpcaseUnicodeStringToAnsiStringWrapper(__int64 a1, __int64 a2, unsigned __int8 a3)
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
    result = DifGetAPIThunkContextById(152, a2, a3, a4);
    if (result == 0) goto loc_0063CB2C;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0063CAB0;
    v_stack_m58 = v_stack_p0;
    goto loc_0063CABD;
loc_0063CAB0:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m40 = a1;
    v_stack_m48 = a2;
    v_stack_m50 = a3;
    if ((*(unsigned __int8 *)(v_rip + 9207277)) != 0) goto loc_0063CAE1;
    if (((*(unsigned int *)(v_rip + 9207457)) & (0x800ULL)) == 0) goto loc_0063CAF4;
loc_0063CAE1:
    result = ExAcquireRundownProtection(v_rip + 9204632, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063CB2C;
loc_0063CAF4:
    goto loc_0063CB16;
loc_0063CAFD:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063CB16:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0063CAFD;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9204569;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = RtlUpcaseUnicodeStringToAnsiString(a1, a2, a3, a4);
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_0063CBA5;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9207148)) != 0) goto loc_0063CB5A;
    if (((*(unsigned int *)(v_rip + 9207336)) & (0x800ULL)) == 0) goto loc_0063CB6D;
loc_0063CB5A:
    result = ExAcquireRundownProtection(v_rip + 9204511, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063CBA5;
loc_0063CB6D:
    v_rsi = (result) + (48);
    goto loc_0063CB8F;
loc_0063CB76:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063CB8F:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0063CB76;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9204448;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifRtlUpcaseUnicodeStringToAnsiStringWrapper(int64_t Arg1, int64_t Arg2, uint8_t Arg3)
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
    result = DifGetAPIThunkContextById(152, Arg2, Arg3, a4);
    if (result == 0) goto loc_0063CB2C;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0063CAB0;
    v_stack_m58 = v_stack_p0;
    goto loc_0063CABD;
loc_0063CAB0:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m40 = Arg1;
    v_stack_m48 = Arg2;
    v_stack_m50 = Arg3;
    if ((*(uint8_t *)(v_rip + 0x8C7DED)) != 0) goto loc_0063CAE1;
    if (((*(uint32_t *)(v_rip + 0x8C7EA1)) & (0x800ULL)) == 0) goto loc_0063CAF4;
loc_0063CAE1:
    result = ExAcquireRundownProtection(v_rip + 9204632, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063CB2C;
loc_0063CAF4:
    goto loc_0063CB16;
loc_0063CAFD:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0063CB16:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0063CAFD;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9204569;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = RtlUpcaseUnicodeStringToAnsiString(Arg1, Arg2, Arg3, a4);
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_0063CBA5;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C7D6C)) != 0) goto loc_0063CB5A;
    if (((*(uint32_t *)(v_rip + 0x8C7E28)) & (0x800ULL)) == 0) goto loc_0063CB6D;
loc_0063CB5A:
    result = ExAcquireRundownProtection(v_rip + 9204511, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063CBA5;
loc_0063CB6D:
    local_rsi = (result) + (48);
    goto loc_0063CB8F;
loc_0063CB76:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0063CB8F:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0063CB76;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9204448;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0063CA50&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0063CA50[BB_0063CA50]
  bb_0063CA9F[BB_0063CA9F]
  bb_0063CAA6[BB_0063CAA6]
  bb_0063CAB0[BB_0063CAB0]
  bb_0063CAB4[BB_0063CAB4]
  bb_0063CABD[BB_0063CABD]
  bb_0063CAD5[BB_0063CAD5]
  bb_0063CAE1[BB_0063CAE1]
  bb_0063CAF4[BB_0063CAF4]
  bb_0063CAFD[BB_0063CAFD]
  bb_0063CB06[BB_0063CB06]
  bb_0063CB13[BB_0063CB13]
  bb_0063CB16[BB_0063CB16]
  bb_0063CB1B[BB_0063CB1B]
  bb_0063CB20[BB_0063CB20]
  bb_0063CB2C[BB_0063CB2C]
  bb_0063CB42[BB_0063CB42]
  bb_0063CB4E[BB_0063CB4E]
  bb_0063CB5A[BB_0063CB5A]
  bb_0063CB6D[BB_0063CB6D]
  bb_0063CB76[BB_0063CB76]
  bb_0063CB7F[BB_0063CB7F]
  bb_0063CB8C[BB_0063CB8C]
  bb_0063CB8F[BB_0063CB8F]
  bb_0063CB94[BB_0063CB94]
  bb_0063CB99[BB_0063CB99]
  bb_0063CBA5[BB_0063CBA5]
  bb_0063CBC6[BB_0063CBC6]
  bb_0063CA50 -->|branch| bb_0063CB2C
  bb_0063CA50 -->|fallthrough| bb_0063CA9F
  bb_0063CA9F -->|branch| bb_0063CAB0
  bb_0063CA9F -->|fallthrough| bb_0063CAA6
  bb_0063CAA6 -->|branch| bb_0063CABD
  bb_0063CAB0 -->|branch| bb_0063CABD
  bb_0063CAB0 -->|fallthrough| bb_0063CAB4
  bb_0063CAB4 -->|flow| bb_0063CABD
  bb_0063CABD -->|branch| bb_0063CAE1
  bb_0063CABD -->|fallthrough| bb_0063CAD5
  bb_0063CAD5 -->|branch| bb_0063CAF4
  bb_0063CAD5 -->|fallthrough| bb_0063CAE1
  bb_0063CAE1 -->|branch| bb_0063CB2C
  bb_0063CAE1 -->|fallthrough| bb_0063CAF4
  bb_0063CAF4 -->|branch| bb_0063CB16
  bb_0063CAFD -->|branch| bb_0063CB13
  bb_0063CAFD -->|fallthrough| bb_0063CB06
  bb_0063CB06 -->|flow| bb_0063CB13
  bb_0063CB13 -->|flow| bb_0063CB16
  bb_0063CB16 -->|branch| bb_0063CAFD
  bb_0063CB16 -->|fallthrough| bb_0063CB1B
  bb_0063CB1B -->|branch| bb_0063CB2C
  bb_0063CB1B -->|fallthrough| bb_0063CB20
  bb_0063CB20 -->|flow| bb_0063CB2C
  bb_0063CB2C -->|branch| bb_0063CBA5
  bb_0063CB2C -->|fallthrough| bb_0063CB42
  bb_0063CB42 -->|branch| bb_0063CB5A
  bb_0063CB42 -->|fallthrough| bb_0063CB4E
  bb_0063CB4E -->|branch| bb_0063CB6D
  bb_0063CB4E -->|fallthrough| bb_0063CB5A
  bb_0063CB5A -->|branch| bb_0063CBA5
  bb_0063CB5A -->|fallthrough| bb_0063CB6D
  bb_0063CB6D -->|branch| bb_0063CB8F
  bb_0063CB76 -->|branch| bb_0063CB8C
  bb_0063CB76 -->|fallthrough| bb_0063CB7F
  bb_0063CB7F -->|flow| bb_0063CB8C
  bb_0063CB8C -->|flow| bb_0063CB8F
  bb_0063CB8F -->|branch| bb_0063CB76
  bb_0063CB8F -->|fallthrough| bb_0063CB94
  bb_0063CB94 -->|branch| bb_0063CBA5
  bb_0063CB94 -->|fallthrough| bb_0063CB99
  bb_0063CB99 -->|flow| bb_0063CBA5
```
