# DifKeInsertByKeyDeviceQueueWrapper

- RVA: `0x00630100`–`0x00630277` (길이 `375` bytes)
- VA: `0x0000000140630100`
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
- `0x0063013E` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00630164` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00630198` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006301BE` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006301D7` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006301E5` → [KeInsertByKeyDeviceQueue](../45/KeInsertByKeyDeviceQueue_function_0045FD80.md) (function, `0x0045FD80`)
- `0x00630211` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00630237` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00630250` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00630174` → RVA `0x00F048B8` (`.data`; read)
- `0x00630185` → RVA `0x00F04980` (`.data`; read)
- `0x00630191` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00630100  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00630105  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0063010A  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
0063010F  55                              push rbp
00630110  41 54                           push r12
00630112  41 55                           push r13
00630114  41 56                           push r14
00630116  41 57                           push r15
00630118  48 8B EC                        mov rbp, rsp
0063011B  48 83 EC 50                     sub rsp, 0x50
0063011F  0F 57 C0                        xorps xmm0, xmm0
00630122  33 C0                           xor eax, eax
00630124  4C 8B E9                        mov r13, rcx
00630127  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0063012B  B9 15 01 00 00                  mov ecx, 0x115
00630130  45 8B F8                        mov r15d, r8d
00630133  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
00630137  4C 8B E2                        mov r12, rdx
0063013A  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0063013E  E8 F1 58 E6 FF                  call 0x140495a34
00630143  48 8B F0                        mov rsi, rax
00630146  48 85 C0                        test rax, rax
00630149  0F 84 8D 00 00 00               je 0x1406301dc
0063014F  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00630152  A8 18                           test al, 0x18
00630154  74 0A                           je 0x140630160
00630156  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0063015A  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
0063015E  EB 0D                           jmp 0x14063016d
00630160  A8 04                           test al, 4
00630162  74 09                           je 0x14063016d
00630164  E8 9F 3A EA FF                  call 0x1404d3c08
00630169  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0063016D  45 32 F6                        xor r14b, r14b
00630170  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
00630174  44 38 35 3D 47 8D 00            cmp byte ptr [rip + 0x8d473d], r14b
0063017B  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
0063017F  44 89 7D D8                     mov dword ptr [rbp - 0x28], r15d
00630183  75 0C                           jne 0x140630191
00630185  F7 05 F1 47 8D 00 00 08 00 00   test dword ptr [rip + 0x8d47f1], 0x800
0063018F  74 13                           je 0x1406301a4
00630191  48 8D 0D E8 3C 8D 00            lea rcx, [rip + 0x8d3ce8]
00630198  E8 83 64 BE FF                  call 0x140216620
0063019D  44 8A F0                        mov r14b, al
006301A0  84 C0                           test al, al
006301A2  74 38                           je 0x1406301dc
006301A4  48 8D 7E 20                     lea rdi, [rsi + 0x20]
006301A8  48 8B 1F                        mov rbx, qword ptr [rdi]
006301AB  EB 19                           jmp 0x1406301c6
006301AD  48 8D 43 F0                     lea rax, [rbx - 0x10]
006301B1  48 85 C0                        test rax, rax
006301B4  74 0D                           je 0x1406301c3
006301B6  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006301BA  48 8D 4D D0                     lea rcx, [rbp - 0x30]
006301BE  E8 0D A9 08 00                  call 0x1406baad0
006301C3  48 8B 1B                        mov rbx, qword ptr [rbx]
006301C6  48 3B DF                        cmp rbx, rdi
006301C9  75 E2                           jne 0x1406301ad
006301CB  45 84 F6                        test r14b, r14b
006301CE  74 0C                           je 0x1406301dc
006301D0  48 8D 0D A9 3C 8D 00            lea rcx, [rip + 0x8d3ca9]
006301D7  E8 A4 9C D1 FF                  call 0x140349e80
006301DC  45 8B C7                        mov r8d, r15d
006301DF  49 8B D4                        mov rdx, r12
006301E2  49 8B CD                        mov rcx, r13
006301E5  E8 96 FB E2 FF                  call 0x14045fd80
006301EA  88 45 F0                        mov byte ptr [rbp - 0x10], al
006301ED  48 85 F6                        test rsi, rsi
006301F0  74 63                           je 0x140630255
006301F2  40 32 FF                        xor dil, dil
006301F5  40 38 3D BC 46 8D 00            cmp byte ptr [rip + 0x8d46bc], dil
006301FC  75 0C                           jne 0x14063020a
006301FE  F7 05 78 47 8D 00 00 08 00 00   test dword ptr [rip + 0x8d4778], 0x800
00630208  74 13                           je 0x14063021d
0063020A  48 8D 0D 6F 3C 8D 00            lea rcx, [rip + 0x8d3c6f]
00630211  E8 0A 64 BE FF                  call 0x140216620
00630216  40 8A F8                        mov dil, al
00630219  84 C0                           test al, al
0063021B  74 38                           je 0x140630255
0063021D  48 83 C6 30                     add rsi, 0x30
00630221  48 8B 1E                        mov rbx, qword ptr [rsi]
00630224  EB 19                           jmp 0x14063023f
00630226  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063022A  48 85 C0                        test rax, rax
0063022D  74 0D                           je 0x14063023c
0063022F  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00630233  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00630237  E8 94 A8 08 00                  call 0x1406baad0
0063023C  48 8B 1B                        mov rbx, qword ptr [rbx]
0063023F  48 3B DE                        cmp rbx, rsi
00630242  75 E2                           jne 0x140630226
00630244  40 84 FF                        test dil, dil
00630247  74 0C                           je 0x140630255
00630249  48 8D 0D 30 3C 8D 00            lea rcx, [rip + 0x8d3c30]
00630250  E8 2B 9C D1 FF                  call 0x140349e80
00630255  8A 45 F0                        mov al, byte ptr [rbp - 0x10]
00630258  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0063025D  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
00630261  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
00630265  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
00630269  49 8B E3                        mov rsp, r11
0063026C  41 5F                           pop r15
0063026E  41 5E                           pop r14
00630270  41 5D                           pop r13
00630272  41 5C                           pop r12
00630274  5D                              pop rbp
00630275  C3                              ret
00630276  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifKeInsertByKeyDeviceQueueWrapper(__int64 a1, __int64 a2, int a3)
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
    unsigned int v_stack_m50;
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
    result = DifGetAPIThunkContextById(277, a2, a3, a4);
    if (result == 0) goto loc_006301DC;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00630160;
    v_stack_m58 = v_stack_p0;
    goto loc_0063016D;
loc_00630160:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m40 = a1;
    v_stack_m48 = a2;
    v_stack_m50 = (unsigned int)((unsigned int)(a3));
    if ((*(unsigned __int8 *)(v_rip + 9258813)) != 0) goto loc_00630191;
    if (((*(unsigned int *)(v_rip + 9258993)) & (0x800ULL)) == 0) goto loc_006301A4;
loc_00630191:
    result = ExAcquireRundownProtection(v_rip + 9256168, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006301DC;
loc_006301A4:
    goto loc_006301C6;
loc_006301AD:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006301C6:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_006301AD;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9256105;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = KeInsertByKeyDeviceQueue(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    v_stack_m38 = (unsigned __int8)(result);
    if (result == 0) goto loc_00630255;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9258684)) != 0) goto loc_0063020A;
    if (((*(unsigned int *)(v_rip + 9258872)) & (0x800ULL)) == 0) goto loc_0063021D;
loc_0063020A:
    result = ExAcquireRundownProtection(v_rip + 9256047, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00630255;
loc_0063021D:
    v_rsi = (result) + (48);
    goto loc_0063023F;
loc_00630226:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
loc_0063023F:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00630226;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9255984;
        result = ExReleaseRundownProtection(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
    return v_stack_m38;
}
```

## 5. (Beta) C Style

```c
int64_t DifKeInsertByKeyDeviceQueueWrapper(int64_t Arg1, int64_t Arg2, int32_t Arg3)
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
    uint32_t v_stack_m50;
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
    result = DifGetAPIThunkContextById(277, Arg2, Arg3, a4);
    if (result == 0) goto loc_006301DC;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00630160;
    v_stack_m58 = v_stack_p0;
    goto loc_0063016D;
loc_00630160:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m40 = Arg1;
    v_stack_m48 = Arg2;
    v_stack_m50 = (uint32_t)((uint32_t)(Arg3));
    if ((*(uint8_t *)(v_rip + 0x8D473D)) != 0) goto loc_00630191;
    if (((*(uint32_t *)(v_rip + 0x8D47F1)) & (0x800ULL)) == 0) goto loc_006301A4;
loc_00630191:
    result = ExAcquireRundownProtection(v_rip + 9256168, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_006301DC;
loc_006301A4:
    goto loc_006301C6;
loc_006301AD:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_006301C6:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_006301AD;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9256105;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = KeInsertByKeyDeviceQueue(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), a4);
    v_stack_m38 = (uint8_t)(result);
    if (result == 0) goto loc_00630255;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D46BC)) != 0) goto loc_0063020A;
    if (((*(uint32_t *)(v_rip + 0x8D4778)) & (0x800ULL)) == 0) goto loc_0063021D;
loc_0063020A:
    result = ExAcquireRundownProtection(v_rip + 9256047, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), a4);
    if ((uint8_t)(result) == 0) goto loc_00630255;
loc_0063021D:
    local_rsi = (result) + (48);
    goto loc_0063023F;
loc_00630226:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), a4);
    }
loc_0063023F:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00630226;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9255984;
        result = ExReleaseRundownProtection(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), a4);
    }
    return v_stack_m38;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00630100&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00630100[BB_00630100]
  bb_0063014F[BB_0063014F]
  bb_00630156[BB_00630156]
  bb_00630160[BB_00630160]
  bb_00630164[BB_00630164]
  bb_0063016D[BB_0063016D]
  bb_00630185[BB_00630185]
  bb_00630191[BB_00630191]
  bb_006301A4[BB_006301A4]
  bb_006301AD[BB_006301AD]
  bb_006301B6[BB_006301B6]
  bb_006301C3[BB_006301C3]
  bb_006301C6[BB_006301C6]
  bb_006301CB[BB_006301CB]
  bb_006301D0[BB_006301D0]
  bb_006301DC[BB_006301DC]
  bb_006301F2[BB_006301F2]
  bb_006301FE[BB_006301FE]
  bb_0063020A[BB_0063020A]
  bb_0063021D[BB_0063021D]
  bb_00630226[BB_00630226]
  bb_0063022F[BB_0063022F]
  bb_0063023C[BB_0063023C]
  bb_0063023F[BB_0063023F]
  bb_00630244[BB_00630244]
  bb_00630249[BB_00630249]
  bb_00630255[BB_00630255]
  bb_00630276[BB_00630276]
  bb_00630100 -->|branch| bb_006301DC
  bb_00630100 -->|fallthrough| bb_0063014F
  bb_0063014F -->|branch| bb_00630160
  bb_0063014F -->|fallthrough| bb_00630156
  bb_00630156 -->|branch| bb_0063016D
  bb_00630160 -->|branch| bb_0063016D
  bb_00630160 -->|fallthrough| bb_00630164
  bb_00630164 -->|flow| bb_0063016D
  bb_0063016D -->|branch| bb_00630191
  bb_0063016D -->|fallthrough| bb_00630185
  bb_00630185 -->|branch| bb_006301A4
  bb_00630185 -->|fallthrough| bb_00630191
  bb_00630191 -->|branch| bb_006301DC
  bb_00630191 -->|fallthrough| bb_006301A4
  bb_006301A4 -->|branch| bb_006301C6
  bb_006301AD -->|branch| bb_006301C3
  bb_006301AD -->|fallthrough| bb_006301B6
  bb_006301B6 -->|flow| bb_006301C3
  bb_006301C3 -->|flow| bb_006301C6
  bb_006301C6 -->|branch| bb_006301AD
  bb_006301C6 -->|fallthrough| bb_006301CB
  bb_006301CB -->|branch| bb_006301DC
  bb_006301CB -->|fallthrough| bb_006301D0
  bb_006301D0 -->|flow| bb_006301DC
  bb_006301DC -->|branch| bb_00630255
  bb_006301DC -->|fallthrough| bb_006301F2
  bb_006301F2 -->|branch| bb_0063020A
  bb_006301F2 -->|fallthrough| bb_006301FE
  bb_006301FE -->|branch| bb_0063021D
  bb_006301FE -->|fallthrough| bb_0063020A
  bb_0063020A -->|branch| bb_00630255
  bb_0063020A -->|fallthrough| bb_0063021D
  bb_0063021D -->|branch| bb_0063023F
  bb_00630226 -->|branch| bb_0063023C
  bb_00630226 -->|fallthrough| bb_0063022F
  bb_0063022F -->|flow| bb_0063023C
  bb_0063023C -->|flow| bb_0063023F
  bb_0063023F -->|branch| bb_00630226
  bb_0063023F -->|fallthrough| bb_00630244
  bb_00630244 -->|branch| bb_00630255
  bb_00630244 -->|fallthrough| bb_00630249
  bb_00630249 -->|flow| bb_00630255
```
