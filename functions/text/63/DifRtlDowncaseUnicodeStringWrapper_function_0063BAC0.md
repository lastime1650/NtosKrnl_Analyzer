# DifRtlDowncaseUnicodeStringWrapper

- RVA: `0x0063BAC0`–`0x0063BC37` (길이 `375` bytes)
- VA: `0x000000014063BAC0`
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
- `0x0063BAFE` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0063BB24` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0063BB58` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063BB7E` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063BB97` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0063BBA5` → [RtlDowncaseUnicodeString](../../page/9C/RtlDowncaseUnicodeString_function_009C4190.md) (function, `0x009C4190`)
- `0x0063BBD1` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063BBF7` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063BC10` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0063BB34` → RVA `0x00F048B8` (`.data`; read)
- `0x0063BB45` → RVA `0x00F04980` (`.data`; read)
- `0x0063BB51` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0063BBA5` → [RtlDowncaseUnicodeString](../../page/9C/RtlDowncaseUnicodeString_function_009C4190.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0063BAC0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0063BAC5  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0063BACA  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
0063BACF  55                              push rbp
0063BAD0  41 54                           push r12
0063BAD2  41 55                           push r13
0063BAD4  41 56                           push r14
0063BAD6  41 57                           push r15
0063BAD8  48 8B EC                        mov rbp, rsp
0063BADB  48 83 EC 50                     sub rsp, 0x50
0063BADF  0F 57 C0                        xorps xmm0, xmm0
0063BAE2  33 C0                           xor eax, eax
0063BAE4  4C 8B E9                        mov r13, rcx
0063BAE7  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0063BAEB  B9 A3 00 00 00                  mov ecx, 0xa3
0063BAF0  45 8A F8                        mov r15b, r8b
0063BAF3  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0063BAF7  4C 8B E2                        mov r12, rdx
0063BAFA  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0063BAFE  E8 31 9F E5 FF                  call 0x140495a34
0063BB03  48 8B F0                        mov rsi, rax
0063BB06  48 85 C0                        test rax, rax
0063BB09  0F 84 8D 00 00 00               je 0x14063bb9c
0063BB0F  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0063BB12  A8 18                           test al, 0x18
0063BB14  74 0A                           je 0x14063bb20
0063BB16  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0063BB1A  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
0063BB1E  EB 0D                           jmp 0x14063bb2d
0063BB20  A8 04                           test al, 4
0063BB22  74 09                           je 0x14063bb2d
0063BB24  E8 DF 80 E9 FF                  call 0x1404d3c08
0063BB29  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0063BB2D  45 32 F6                        xor r14b, r14b
0063BB30  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
0063BB34  44 38 35 7D 8D 8C 00            cmp byte ptr [rip + 0x8c8d7d], r14b
0063BB3B  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
0063BB3F  44 88 7D D8                     mov byte ptr [rbp - 0x28], r15b
0063BB43  75 0C                           jne 0x14063bb51
0063BB45  F7 05 31 8E 8C 00 00 08 00 00   test dword ptr [rip + 0x8c8e31], 0x800
0063BB4F  74 13                           je 0x14063bb64
0063BB51  48 8D 0D 28 83 8C 00            lea rcx, [rip + 0x8c8328]
0063BB58  E8 C3 AA BD FF                  call 0x140216620
0063BB5D  44 8A F0                        mov r14b, al
0063BB60  84 C0                           test al, al
0063BB62  74 38                           je 0x14063bb9c
0063BB64  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0063BB68  48 8B 1F                        mov rbx, qword ptr [rdi]
0063BB6B  EB 19                           jmp 0x14063bb86
0063BB6D  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063BB71  48 85 C0                        test rax, rax
0063BB74  74 0D                           je 0x14063bb83
0063BB76  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063BB7A  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0063BB7E  E8 4D EF 07 00                  call 0x1406baad0
0063BB83  48 8B 1B                        mov rbx, qword ptr [rbx]
0063BB86  48 3B DF                        cmp rbx, rdi
0063BB89  75 E2                           jne 0x14063bb6d
0063BB8B  45 84 F6                        test r14b, r14b
0063BB8E  74 0C                           je 0x14063bb9c
0063BB90  48 8D 0D E9 82 8C 00            lea rcx, [rip + 0x8c82e9]
0063BB97  E8 E4 E2 D0 FF                  call 0x140349e80
0063BB9C  45 8A C7                        mov r8b, r15b
0063BB9F  49 8B D4                        mov rdx, r12
0063BBA2  49 8B CD                        mov rcx, r13
0063BBA5  E8 E6 85 38 00                  call 0x1409c4190
0063BBAA  89 45 F0                        mov dword ptr [rbp - 0x10], eax
0063BBAD  48 85 F6                        test rsi, rsi
0063BBB0  74 63                           je 0x14063bc15
0063BBB2  40 32 FF                        xor dil, dil
0063BBB5  40 38 3D FC 8C 8C 00            cmp byte ptr [rip + 0x8c8cfc], dil
0063BBBC  75 0C                           jne 0x14063bbca
0063BBBE  F7 05 B8 8D 8C 00 00 08 00 00   test dword ptr [rip + 0x8c8db8], 0x800
0063BBC8  74 13                           je 0x14063bbdd
0063BBCA  48 8D 0D AF 82 8C 00            lea rcx, [rip + 0x8c82af]
0063BBD1  E8 4A AA BD FF                  call 0x140216620
0063BBD6  40 8A F8                        mov dil, al
0063BBD9  84 C0                           test al, al
0063BBDB  74 38                           je 0x14063bc15
0063BBDD  48 83 C6 30                     add rsi, 0x30
0063BBE1  48 8B 1E                        mov rbx, qword ptr [rsi]
0063BBE4  EB 19                           jmp 0x14063bbff
0063BBE6  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063BBEA  48 85 C0                        test rax, rax
0063BBED  74 0D                           je 0x14063bbfc
0063BBEF  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063BBF3  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0063BBF7  E8 D4 EE 07 00                  call 0x1406baad0
0063BBFC  48 8B 1B                        mov rbx, qword ptr [rbx]
0063BBFF  48 3B DE                        cmp rbx, rsi
0063BC02  75 E2                           jne 0x14063bbe6
0063BC04  40 84 FF                        test dil, dil
0063BC07  74 0C                           je 0x14063bc15
0063BC09  48 8D 0D 70 82 8C 00            lea rcx, [rip + 0x8c8270]
0063BC10  E8 6B E2 D0 FF                  call 0x140349e80
0063BC15  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
0063BC18  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0063BC1D  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
0063BC21  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
0063BC25  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
0063BC29  49 8B E3                        mov rsp, r11
0063BC2C  41 5F                           pop r15
0063BC2E  41 5E                           pop r14
0063BC30  41 5D                           pop r13
0063BC32  41 5C                           pop r12
0063BC34  5D                              pop rbp
0063BC35  C3                              ret
0063BC36  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifRtlDowncaseUnicodeStringWrapper(__int64 a1, __int64 a2, unsigned __int8 a3)
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
    result = DifGetAPIThunkContextById(163, a2, a3, a4);
    if (result == 0) goto loc_0063BB9C;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0063BB20;
    v_stack_m58 = v_stack_p0;
    goto loc_0063BB2D;
loc_0063BB20:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m40 = a1;
    v_stack_m48 = a2;
    v_stack_m50 = a3;
    if ((*(unsigned __int8 *)(v_rip + 9211261)) != 0) goto loc_0063BB51;
    if (((*(unsigned int *)(v_rip + 9211441)) & (0x800ULL)) == 0) goto loc_0063BB64;
loc_0063BB51:
    result = ExAcquireRundownProtection(v_rip + 9208616, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063BB9C;
loc_0063BB64:
    goto loc_0063BB86;
loc_0063BB6D:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063BB86:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0063BB6D;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9208553;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = RtlDowncaseUnicodeString(a1, a2, a3, a4);
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_0063BC15;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9211132)) != 0) goto loc_0063BBCA;
    if (((*(unsigned int *)(v_rip + 9211320)) & (0x800ULL)) == 0) goto loc_0063BBDD;
loc_0063BBCA:
    result = ExAcquireRundownProtection(v_rip + 9208495, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063BC15;
loc_0063BBDD:
    v_rsi = (result) + (48);
    goto loc_0063BBFF;
loc_0063BBE6:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063BBFF:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0063BBE6;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9208432;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifRtlDowncaseUnicodeStringWrapper(int64_t Arg1, int64_t Arg2, uint8_t Arg3)
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
    result = DifGetAPIThunkContextById(163, Arg2, Arg3, a4);
    if (result == 0) goto loc_0063BB9C;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0063BB20;
    v_stack_m58 = v_stack_p0;
    goto loc_0063BB2D;
loc_0063BB20:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m40 = Arg1;
    v_stack_m48 = Arg2;
    v_stack_m50 = Arg3;
    if ((*(uint8_t *)(v_rip + 0x8C8D7D)) != 0) goto loc_0063BB51;
    if (((*(uint32_t *)(v_rip + 0x8C8E31)) & (0x800ULL)) == 0) goto loc_0063BB64;
loc_0063BB51:
    result = ExAcquireRundownProtection(v_rip + 9208616, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063BB9C;
loc_0063BB64:
    goto loc_0063BB86;
loc_0063BB6D:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0063BB86:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0063BB6D;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9208553;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = RtlDowncaseUnicodeString(Arg1, Arg2, Arg3, a4);
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_0063BC15;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C8CFC)) != 0) goto loc_0063BBCA;
    if (((*(uint32_t *)(v_rip + 0x8C8DB8)) & (0x800ULL)) == 0) goto loc_0063BBDD;
loc_0063BBCA:
    result = ExAcquireRundownProtection(v_rip + 9208495, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063BC15;
loc_0063BBDD:
    local_rsi = (result) + (48);
    goto loc_0063BBFF;
loc_0063BBE6:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0063BBFF:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0063BBE6;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9208432;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0063BAC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0063BAC0[BB_0063BAC0]
  bb_0063BB0F[BB_0063BB0F]
  bb_0063BB16[BB_0063BB16]
  bb_0063BB20[BB_0063BB20]
  bb_0063BB24[BB_0063BB24]
  bb_0063BB2D[BB_0063BB2D]
  bb_0063BB45[BB_0063BB45]
  bb_0063BB51[BB_0063BB51]
  bb_0063BB64[BB_0063BB64]
  bb_0063BB6D[BB_0063BB6D]
  bb_0063BB76[BB_0063BB76]
  bb_0063BB83[BB_0063BB83]
  bb_0063BB86[BB_0063BB86]
  bb_0063BB8B[BB_0063BB8B]
  bb_0063BB90[BB_0063BB90]
  bb_0063BB9C[BB_0063BB9C]
  bb_0063BBB2[BB_0063BBB2]
  bb_0063BBBE[BB_0063BBBE]
  bb_0063BBCA[BB_0063BBCA]
  bb_0063BBDD[BB_0063BBDD]
  bb_0063BBE6[BB_0063BBE6]
  bb_0063BBEF[BB_0063BBEF]
  bb_0063BBFC[BB_0063BBFC]
  bb_0063BBFF[BB_0063BBFF]
  bb_0063BC04[BB_0063BC04]
  bb_0063BC09[BB_0063BC09]
  bb_0063BC15[BB_0063BC15]
  bb_0063BC36[BB_0063BC36]
  bb_0063BAC0 -->|branch| bb_0063BB9C
  bb_0063BAC0 -->|fallthrough| bb_0063BB0F
  bb_0063BB0F -->|branch| bb_0063BB20
  bb_0063BB0F -->|fallthrough| bb_0063BB16
  bb_0063BB16 -->|branch| bb_0063BB2D
  bb_0063BB20 -->|branch| bb_0063BB2D
  bb_0063BB20 -->|fallthrough| bb_0063BB24
  bb_0063BB24 -->|flow| bb_0063BB2D
  bb_0063BB2D -->|branch| bb_0063BB51
  bb_0063BB2D -->|fallthrough| bb_0063BB45
  bb_0063BB45 -->|branch| bb_0063BB64
  bb_0063BB45 -->|fallthrough| bb_0063BB51
  bb_0063BB51 -->|branch| bb_0063BB9C
  bb_0063BB51 -->|fallthrough| bb_0063BB64
  bb_0063BB64 -->|branch| bb_0063BB86
  bb_0063BB6D -->|branch| bb_0063BB83
  bb_0063BB6D -->|fallthrough| bb_0063BB76
  bb_0063BB76 -->|flow| bb_0063BB83
  bb_0063BB83 -->|flow| bb_0063BB86
  bb_0063BB86 -->|branch| bb_0063BB6D
  bb_0063BB86 -->|fallthrough| bb_0063BB8B
  bb_0063BB8B -->|branch| bb_0063BB9C
  bb_0063BB8B -->|fallthrough| bb_0063BB90
  bb_0063BB90 -->|flow| bb_0063BB9C
  bb_0063BB9C -->|branch| bb_0063BC15
  bb_0063BB9C -->|fallthrough| bb_0063BBB2
  bb_0063BBB2 -->|branch| bb_0063BBCA
  bb_0063BBB2 -->|fallthrough| bb_0063BBBE
  bb_0063BBBE -->|branch| bb_0063BBDD
  bb_0063BBBE -->|fallthrough| bb_0063BBCA
  bb_0063BBCA -->|branch| bb_0063BC15
  bb_0063BBCA -->|fallthrough| bb_0063BBDD
  bb_0063BBDD -->|branch| bb_0063BBFF
  bb_0063BBE6 -->|branch| bb_0063BBFC
  bb_0063BBE6 -->|fallthrough| bb_0063BBEF
  bb_0063BBEF -->|flow| bb_0063BBFC
  bb_0063BBFC -->|flow| bb_0063BBFF
  bb_0063BBFF -->|branch| bb_0063BBE6
  bb_0063BBFF -->|fallthrough| bb_0063BC04
  bb_0063BC04 -->|branch| bb_0063BC15
  bb_0063BC04 -->|fallthrough| bb_0063BC09
  bb_0063BC09 -->|flow| bb_0063BC15
```
